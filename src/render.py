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

ASHA_NEXT_STEP = (
    "Arrange a clinic check-up soon and share these readings with the "
    "medical officer."
)
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


def top_drivers(contrib: pd.DataFrame, medians: pd.Series, k: int = 2) -> list[str]:
    """Top-k LOCAL drivers by |SHAP| for the predicted class, as plain phrases.

    Direction word comes from the reading vs. the dataset median — a fixed
    comparison, not a clinical threshold.
    """
    top = contrib.reindex(contrib.shap_pred_class.abs().sort_values(ascending=False).index)
    return [
        f"{'raised' if r.feature_value > medians[r.feature] else 'low'} "
        f"{PLAIN_NAMES[r.feature]}"
        for r in top.head(k).itertuples()
    ]


def _selfcheck() -> None:
    assert band_for("low risk", 0.99) == "GREEN"
    assert band_for("high risk", 0.90) == "RED"
    assert band_for("high risk", 0.012) == "AMBER"  # boundary_mid: near-tie
    assert band_for("mid risk", 0.90) == "AMBER"
    med = pd.Series({"BS": 7.5, "BodyTemp": 98.0})
    df = pd.DataFrame(
        {"feature": ["BS", "BodyTemp"], "feature_value": [9.0, 97.0],
         "shap_pred_class": [0.20, -0.30]}
    )
    assert top_drivers(df, med) == ["low body temperature", "raised blood sugar"]


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
def render_asha(case: str, s: pd.Series, contrib: pd.DataFrame, medians: pd.Series):
    """Deterministic template over the local SHAP values. No LLM, ever."""
    routine = s.predicted == "low risk"
    band = "ROUTINE" if routine else "ELEVATED — needs follow-up"
    drivers = top_drivers(contrib, medians)

    text = "\n".join([
        f"ASHA CARD — {band}",
        "",
        "What the model flagged for follow-up:",
        *[f"  • {d}" for d in drivers],
        "",
        f"Next step: {ASHA_NEXT_STEP}",
        "",
        ASHA_FOOTER,
        DISCLAIMER,
    ])
    txt_out = config.TABLES_DIR / f"tier_asha_{case}.txt"
    txt_out.write_text(text, encoding="utf-8")

    fig = plt.figure(figsize=(7.5, 5))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis("off")
    colour = BAND_HEX["GREEN"] if routine else BAND_HEX["AMBER"]
    ax.add_patch(plt.Rectangle((0.04, 0.05), 0.92, 0.9, fill=False, ec="#999", lw=1.5))
    ax.add_patch(plt.Rectangle((0.04, 0.79), 0.92, 0.16, color=colour))
    ax.text(0.5, 0.87, band, ha="center", va="center", fontsize=17,
            color="white", fontweight="bold")

    ax.text(0.09, 0.70, "What the model flagged for follow-up:", fontsize=12,
            fontweight="bold")
    for i, d in enumerate(drivers):
        ax.text(0.12, 0.62 - 0.08 * i, f"•  {d}", fontsize=14)

    ax.text(0.09, 0.38, "Next step", fontsize=12, fontweight="bold")
    ax.text(0.09, 0.28, textwrap.fill(ASHA_NEXT_STEP, 52), fontsize=12,
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
    txt = config.TABLES_DIR / f"tier_mother_{case}_hi.txt"
    txt.write_text(message, encoding="utf-8")

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
                medians: pd.Series) -> None:
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
    a_png, a_txt, a_text = render_asha(case, s, contrib, medians)
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
    X, _, _ = prepare_modeling_frame(*load_dataset())
    medians = X.median()

    config.FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    config.TABLES_DIR.mkdir(parents=True, exist_ok=True)

    print("Phase 3 — three-tier renderer")
    print("=" * 60)
    print(DISCLAIMER)

    cases = list(summary.case) if case == "all" else [case]
    for c in cases:
        render_case(c, summary, contribs, medians)
    print("\nOK")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--case", default="boundary_mid",
                   help="case tag from shap_case_summary.csv, or 'all'")
    run(p.parse_args().case)
    sys.exit(0)
