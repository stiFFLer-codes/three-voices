"""Phase 3 — the three-tier renderer. This is the contribution.

ONE prediction, rendered three ways, from the saved Phase-2 SHAP artifacts:

  Tier 1  clinician   full technical detail — SHAP waterfall + probabilities +
                      raw feature table.  results/figures/tier_clinician_<case>.png
  Tier 2  ASHA        deterministic plain-language card built by TEMPLATE over
                      the local SHAP values. No LLM at inference.
                      results/figures/tier_asha_<case>.png  +  .../tables/tier_asha_<case>.txt
  Tier 3  mother      non-numeric traffic light + Hindi voice message.
                      results/figures/tier_mother_<case>.png,
                      results/audio/tier_mother_<case>_hi.mp3,
                      results/tables/tier_mother_<case>_hi.txt

One band, computed once per case by ``band_for``, drives BOTH the ASHA header
and the mother's lamp: a prediction cannot be amber in one tier and red in the
next. The ASHA driver list is SIGN-AWARE — only features pushing toward the
elevated class are listed, and a routine card lists none at all (P4 found the
old |SHAP| ranking printing a feature that argued against the prediction).

INTEGRITY — this is an ILLUSTRATIVE rendering on PUBLIC data (UCI Maternal
Health Risk, id=863). It is NOT a diagnosis, NOT medical advice, and NOT
clinically validated. The model flags factors for follow-up; the referral
decision remains with the ASHA / clinician. No output below names a disease,
and no probability or percentage is ever shown to the mother tier.

Run:
    python -m src.render                    # boundary_mid (the teaching case)
    python -m src.render --case all
"""
from __future__ import annotations

import argparse
import sys
import textwrap

import matplotlib

matplotlib.use("Agg")  # headless, deterministic figure output
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageDraw

from src import config
from src.data import load_dataset
from src.model import prepare_modeling_frame

DISCLAIMER = (
    "Illustrative rendering on public data (UCI Maternal Health Risk). "
    "Not a diagnosis, not medical advice, not clinically validated."
)

# Tier 2 is template-only. This map is FIXED — no generation at inference.
PLAIN_NAMES = {
    "SystolicBP": "upper blood pressure",
    "DiastolicBP": "lower blood pressure",
    "BS": "blood sugar",
    "BodyTemp": "body temperature",
    "HeartRate": "heart rate",
    "Age": "age",
}

# Direction words, per feature. Age gets its own pair: nobody says "low age".
DIRECTION_WORDS = {"Age": ("young", "older")}
DIRECTION_DEFAULT = ("low", "raised")

ASHA_NEXT_STEP = (
    "Arrange a clinic check-up soon and share these readings with the "
    "medical officer."
)
# A routine card must not ask for a check-up it has no reason to ask for.
ASHA_NEXT_STEP_ROUTINE = (
    "Continue routine antenatal care and share these readings at the next "
    "scheduled visit."
)
ASHA_HEADING_ELEVATED = "What the model flagged for follow-up:"
ASHA_HEADING_ROUTINE = "No specific risk factors flagged."
ASHA_FOOTER = "The referral decision remains with the health worker and clinician."

# Tier 3 message, one per band. Deterministic, no numbers, no disease names.
MOTHER_HI = {
    "GREEN": "नमस्ते। आपकी जाँच सामान्य दिख रही है। कृपया अपनी नियमित जाँच जारी रखें।",
    "AMBER": (
        "नमस्ते। आपकी जाँच में कुछ बातें ऐसी हैं जिन पर ध्यान देना ज़रूरी है। "
        "घबराएँ नहीं, पर कृपया जल्दी ही अपनी ANM या नज़दीकी स्वास्थ्य केंद्र पर जाँच करवाएँ।"
    ),
    "RED": (
        "नमस्ते। आपकी जाँच में कुछ ज़रूरी बातें सामने आई हैं। "
        "कृपया जितनी जल्दी हो सके अपने डॉक्टर या स्वास्थ्य केंद्र पर जाएँ।"
    ),
}

BAND_RGB = {"RED": (200, 40, 40), "AMBER": (235, 165, 20), "GREEN": (40, 160, 70)}
BAND_HEX = {"RED": "#c82828", "AMBER": "#eba514", "GREEN": "#28a046"}
RED_MARGIN = 0.15  # top-2 probability margin required before the mother sees RED

# One band drives the mother's lamp AND the ASHA header, so a case cannot be
# amber in one tier and red in the next. GREEN <=> predicted low risk.
# The label states the level in words — one distinct string per band — so the
# card never leans on hue to tell the three states apart (WCAG 1.4.1).
BAND_LABEL = {
    "GREEN": "LOW — routine care",
    "AMBER": "ELEVATED — needs follow-up",
    "RED": "HIGH — needs follow-up",
}

# Direction words are attached only outside a deadband of this many IQRs
# around the clean-set median (see ``direction_word``).
DEADBAND_IQRS = 0.25

INK, PAPER = "#1a1a1a", "#ffffff"


# ---------------------------------------------------------------------------
# WCAG contrast (also imported by src.evaluate, so the palette has one source)
# ---------------------------------------------------------------------------
def hex_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def _linear(channel: int) -> float:
    c = channel / 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(rgb: tuple[int, int, int]) -> float:
    r, g, b = (_linear(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    """WCAG 2.1 contrast ratio between two sRGB colours (1.0 – 21.0)."""
    lo, hi = sorted((luminance(a), luminance(b)))
    return (hi + 0.05) / (lo + 0.05)


def text_on(bg_hex: str) -> str:
    """Ink or paper — whichever contrasts more with this background.

    Computed from the hex, so re-tuning a band colour cannot silently leave
    unreadable text behind it.
    """
    bg = hex_rgb(bg_hex)
    return INK if contrast(hex_rgb(INK), bg) >= contrast(hex_rgb(PAPER), bg) else PAPER


# ---------------------------------------------------------------------------
# Deterministic logic (the part worth a self-check)
# ---------------------------------------------------------------------------
def band_for(predicted: str, margin: float) -> str:
    """Uncertainty-aware traffic-light band for the mother tier.

    GREEN when the model predicts low risk. RED only when it predicts high
    risk AND is not on a knife edge (top-2 margin >= 0.15). Everything else —
    mid risk, and any near-tie — is AMBER. A coin-flip must not be shown to a
    mother as a red alarm.
    """
    if predicted == "low risk":
        return "GREEN"
    if predicted == "high risk" and margin >= RED_MARGIN:
        return "RED"
    return "AMBER"


def direction_word(feature: str, value: float, ref: pd.DataFrame) -> str:
    """Plain phrase for one reading: direction word only outside the deadband.

    A reading within 0.25 IQR of the clean-set median is unremarkable, so it is
    named plainly ("blood sugar") rather than editorialised ("raised blood
    sugar"). The deadband is derived from the data, not from clinical
    reference ranges — this preprint claims no clinical thresholds.
    """
    med, dead = ref.loc[feature, "median"], ref.loc[feature, "deadband"]
    name = PLAIN_NAMES[feature]
    if abs(value - med) <= dead:
        return name
    low, high = DIRECTION_WORDS.get(feature, DIRECTION_DEFAULT)
    return f"{high if value > med else low} {name}"


def top_drivers(contrib: pd.DataFrame, ref: pd.DataFrame, elevated: bool,
                k: int = 2) -> list[str]:
    """The top-k features PUSHING TOWARD an elevated prediction, as phrases.

    Sign matters, and ranking by |SHAP| got it wrong: a feature arguing
    AGAINST the prediction has a large magnitude and a negative sign, and
    printing it under "flagged for follow-up" puts a false cue in front of the
    person making the referral. So: keep only positive contributions to the
    predicted class, rank by signed value descending.

    A routine (predicted-low) card lists nothing at all. Its top contributors
    are the reasons the model said LOW; naming them as "flagged" would invert
    their meaning.
    """
    if not elevated:
        return []
    pos = contrib[contrib.shap_pred_class > 0].sort_values(
        "shap_pred_class", ascending=False
    )
    return [direction_word(r.feature, r.feature_value, ref)
            for r in pos.head(k).itertuples()]


def _selfcheck() -> None:
    assert band_for("low risk", 0.99) == "GREEN"
    assert band_for("high risk", 0.90) == "RED"
    assert band_for("high risk", 0.012) == "AMBER"  # boundary_mid: near-tie
    assert band_for("mid risk", 0.90) == "AMBER"
    # Each band must be distinguishable in text alone — hue is the backup cue.
    assert len(set(BAND_LABEL.values())) == 3
    # Every band's header text must clear WCAG AA (4.5:1) on its own colour.
    for band, hexc in BAND_HEX.items():
        cr = contrast(hex_rgb(text_on(hexc)), hex_rgb(hexc))
        assert cr >= 4.5, f"{band} header text is {cr:.2f}:1"

    ref = pd.DataFrame(
        {"median": {"BS": 7.5, "BodyTemp": 98.0, "Age": 25.0},
         "deadband": {"BS": 0.25, "BodyTemp": 0.0, "Age": 4.0}}
    )
    df = pd.DataFrame(
        {"feature": ["BS", "BodyTemp", "Age"], "feature_value": [7.7, 102.0, 13.0],
         "shap_pred_class": [-0.30, 0.20, 0.05]}
    )
    # BS has the largest |SHAP| but argues AGAINST the prediction — it must not
    # be listed; BS 7.7 against a 7.5 median is inside the deadband anyway.
    assert top_drivers(df, ref, elevated=True) == ["raised body temperature", "young age"]
    assert top_drivers(df, ref, elevated=False) == []
    assert direction_word("BS", 7.7, ref) == "blood sugar"
    assert direction_word("BS", 9.0, ref) == "raised blood sugar"


# ---------------------------------------------------------------------------
# Tier 1 — clinician
# ---------------------------------------------------------------------------
def render_clinician(case: str, s: pd.Series, contrib: pd.DataFrame, probs: pd.Series):
    """Composite technical view. Holds nothing back — this tier gets everything."""
    # TreeExplainer output is additive in probability space, so the waterfall's
    # base value is recoverable exactly from the saved data.
    base = probs[s.predicted] - contrib.shap_pred_class.sum()
    w = contrib.reindex(contrib.shap_pred_class.abs().sort_values().index)

    fig = plt.figure(figsize=(13, 7))
    gs = fig.add_gridspec(2, 2, width_ratios=[1.7, 1], hspace=0.35, wspace=0.3)

    # --- waterfall -------------------------------------------------------
    ax = fig.add_subplot(gs[:, 0])
    left = base
    edges = [base]
    for i, r in enumerate(w.itertuples()):
        ax.barh(i, r.shap_pred_class, left=left, height=0.6,
                color="#ff0051" if r.shap_pred_class > 0 else "#008bfb")
        ax.text(left + r.shap_pred_class, i,
                f" {r.shap_pred_class:+.3f} ", va="center", fontsize=9,
                ha="left" if r.shap_pred_class > 0 else "right")
        left += r.shap_pred_class
        edges.append(left)
    lo, hi = min(edges), max(edges)
    ax.set_xlim(lo - 0.18 * (hi - lo), hi + 0.18 * (hi - lo))  # room for the labels
    ax.axvline(base, color="grey", ls="--", lw=1)
    ax.set_yticks(range(len(w)))
    ax.set_yticklabels([f"{r.feature} = {r.feature_value:g}" for r in w.itertuples()])
    ax.set_xlabel(f"P({s.predicted})   —   base E[f(x)] = {base:.3f}  ->  f(x) = {probs[s.predicted]:.3f}")
    ax.set_title(f"SHAP waterfall — predicted class '{s.predicted}'")

    # --- probability bar --------------------------------------------------
    ax = fig.add_subplot(gs[0, 1])
    ax.barh(list(probs.index), list(probs.values),
            color=[BAND_HEX["GREEN"], BAND_HEX["AMBER"], BAND_HEX["RED"]])
    for i, v in enumerate(probs.values):
        ax.text(v + 0.01, i, f"{v:.3f}", va="center", fontsize=9)
    ax.set_xlim(0, 1.15)
    ax.invert_yaxis()
    ax.set_title("Predicted probability", fontsize=10)

    # --- raw feature values ----------------------------------------------
    ax = fig.add_subplot(gs[1, 1])
    ax.axis("off")
    tbl = ax.table(
        cellText=[[r.feature, f"{r.feature_value:g}"] for r in contrib.itertuples()],
        colLabels=["feature", "raw value"], loc="center", cellLoc="left",
    )
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(9)
    tbl.scale(1, 1.4)
    ax.set_title("Raw feature values", fontsize=10)

    fig.suptitle(
        f"Tier 1 — clinician view   |   case '{case}' (row {s.row_index})   |   "
        f"true: {s.true}   predicted: {s.predicted}",
        fontsize=12,
    )
    fig.text(0.5, 0.005, DISCLAIMER, ha="center", fontsize=8, style="italic", color="#555")
    out = config.FIGURES_DIR / f"tier_clinician_{case}.png"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return out


# ---------------------------------------------------------------------------
# Tier 2 — ASHA
# ---------------------------------------------------------------------------
def render_asha(case: str, s: pd.Series, contrib: pd.DataFrame, ref: pd.DataFrame,
                band: str):
    """Deterministic template over the local SHAP values. No LLM, ever.

    ``band`` is the same value the mother's lamp uses, so one prediction can
    never be amber on the card and red on the lamp.
    """
    elevated = band != "GREEN"
    label = BAND_LABEL[band]
    drivers = top_drivers(contrib, ref, elevated)
    heading = ASHA_HEADING_ELEVATED if elevated else ASHA_HEADING_ROUTINE
    next_step = ASHA_NEXT_STEP if elevated else ASHA_NEXT_STEP_ROUTINE

    text = "\n".join([
        f"ASHA CARD — {label}",
        "",
        heading,
        *[f"  • {d}" for d in drivers],
        "",
        f"Next step: {next_step}",
        "",
        ASHA_FOOTER,
        DISCLAIMER,
    ])
    txt_out = config.TABLES_DIR / f"tier_asha_{case}.txt"
    txt_out.write_text(text, encoding="utf-8")

    fig = plt.figure(figsize=(7.5, 5))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis("off")
    colour = BAND_HEX[band]
    ink = text_on(colour)  # AA-checked against this band, not assumed white
    ax.add_patch(plt.Rectangle((0.04, 0.05), 0.92, 0.9, fill=False, ec="#999", lw=1.5))
    ax.add_patch(plt.Rectangle((0.04, 0.79), 0.92, 0.16, color=colour))
    # The label itself carries the level, so hue is redundant, not load-bearing.
    ax.text(0.5, 0.87, label, ha="center", va="center", fontsize=17,
            color=ink, fontweight="bold")

    ax.text(0.09, 0.70, heading, fontsize=12, fontweight="bold")
    for i, d in enumerate(drivers):
        ax.text(0.12, 0.62 - 0.08 * i, f"•  {d}", fontsize=14)

    # Close the gap the driver list would have occupied on a routine card.
    y = 0.38 if drivers else 0.58
    ax.text(0.09, y, "Next step", fontsize=12, fontweight="bold")
    ax.text(0.09, y - 0.10, textwrap.fill(next_step, 52), fontsize=12,
            va="top", bbox=dict(fc="#f2f2f2", ec="none", pad=6))
    ax.text(0.09, 0.155, ASHA_FOOTER, fontsize=10, style="italic", color="#333")
    ax.text(0.09, 0.11, textwrap.fill(DISCLAIMER, 95), fontsize=7.5, va="top",
            style="italic", color="#666")

    out = config.FIGURES_DIR / f"tier_asha_{case}.png"
    fig.savefig(out, dpi=150)
    plt.close(fig)
    return out, txt_out, text


# ---------------------------------------------------------------------------
# Tier 3 — mother-to-be
# ---------------------------------------------------------------------------
def render_mother(case: str, band: str):
    """Non-numeric traffic light + Hindi voice. No number, no text, no disease."""
    W, H, R = 320, 720, 90
    img = Image.new("RGB", (W, H), "#f4f4f4")
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([30, 30, W - 30, H - 30], radius=40, fill="#2b2b2b")
    for i, name in enumerate(("RED", "AMBER", "GREEN")):
        cy = 150 + i * 210
        fill = BAND_RGB[name] if name == band else tuple(
            int(c * 0.22 + 60) for c in BAND_RGB[name]
        )
        d.ellipse([W // 2 - R, cy - R, W // 2 + R, cy + R], fill=fill,
                  outline="#1a1a1a", width=4)
    png = config.FIGURES_DIR / f"tier_mother_{case}.png"
    img.save(png)

    message = MOTHER_HI[band]
    # The spoken line stays exactly as templated — provenance is written
    # alongside it, NOT read aloud. A one-time spoken IVR framing is
    # deployment work, not something to bolt onto every message.
    txt = config.TABLES_DIR / f"tier_mother_{case}_hi.txt"
    txt.write_text(
        "\n".join([
            message,
            "",
            "--- provenance (written, not spoken) ---",
            f"case: {case}   band: {band}",
            DISCLAIMER,
        ]) + "\n",
        encoding="utf-8",
    )

    audio_dir = config.RESULTS_DIR / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)
    (audio_dir / ".gitkeep").touch()
    mp3 = audio_dir / f"tier_mother_{case}_hi.mp3"
    try:
        from gtts import gTTS

        gTTS(message, lang="hi").save(str(mp3))
    except Exception as exc:  # network or gTTS unavailable — text still written
        print(f"  [warn] Hindi MP3 skipped ({type(exc).__name__}: {exc}). "
              f"Message text was still written to {txt}")
        mp3 = None
    return png, txt, mp3, message


# ---------------------------------------------------------------------------
def render_case(case: str, summary: pd.DataFrame, contribs: pd.DataFrame,
                ref: pd.DataFrame) -> None:
    s = summary.set_index("case").loc[case]
    contrib = contribs[contribs.case == case].reset_index(drop=True)
    probs = pd.Series(
        {"low risk": s.p_low, "mid risk": s.p_mid, "high risk": s.p_high}
    )
    margin = float(probs.nlargest(2).diff().iloc[-1] * -1)
    band = band_for(s.predicted, margin)

    print(f"\ncase '{case}' — row {s.row_index}: true {s.true}, predicted "
          f"{s.predicted} (top-2 margin {margin:.3f}) -> mother band {band}")
    print(f"  tier 1 -> {render_clinician(case, s, contrib, probs)}")
    a_png, a_txt, a_text = render_asha(case, s, contrib, ref, band)
    print(f"  tier 2 -> {a_png}\n           {a_txt}")
    print("           " + a_text.splitlines()[0])
    m_png, m_txt, m_mp3, _ = render_mother(case, band)
    print(f"  tier 3 -> {m_png}\n           {m_txt}"
          + (f"\n           {m_mp3}" if m_mp3 else ""))


def run(case: str = "boundary_mid") -> None:
    config.set_seeds()
    _selfcheck()

    summary = pd.read_csv(config.TABLES_DIR / "shap_case_summary.csv")
    contribs = pd.read_csv(config.TABLES_DIR / "shap_case_contributions.csv")
    # Reference stats for the direction words: median plus a deadband of
    # 0.25 IQR. BodyTemp's IQR is 0 on the clean set (readings pile up at
    # 98F), so any deviation there counts — which is the behaviour we want.
    X, _, _ = prepare_modeling_frame(*load_dataset())
    ref = pd.DataFrame({
        "median": X.median(),
        "deadband": (X.quantile(0.75) - X.quantile(0.25)) * DEADBAND_IQRS,
    })

    config.FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    config.TABLES_DIR.mkdir(parents=True, exist_ok=True)

    print("Phase 3 — three-tier renderer")
    print("=" * 60)
    print(DISCLAIMER)

    cases = list(summary.case) if case == "all" else [case]
    for c in cases:
        render_case(c, summary, contribs, ref)
    print("\nOK")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--case", default="boundary_mid",
                   help="case tag from shap_case_summary.csv, or 'all'")
    run(p.parse_args().case)
    sys.exit(0)
