"""Phase 4 — heuristic evaluation of the three rendered tiers.

A single-evaluator, author-conducted walkthrough of the Phase-3 artifacts on
disk against WCAG 2.1 (POUR) and Nielsen's 10 usability heuristics. The
assessment is AUTHORED and encoded here as data — no LLM runs at inference.
Every rating names the artifact detail it came from; contrast ratios are
computed from the palette constants in ``src.render`` so the numbers move if
the palette does.

Emits:
    results/tables/heuristic_matrix.csv       criterion x tier, rating + rationale
    results/tables/heuristic_evaluation.md    matrix + synthesis + gaps + method

INTEGRITY — this evaluates an EXPLANATION DESIGN rendered on public data
(UCI Maternal Health Risk, id=863). It is not user testing, not a clinical
evaluation, and makes no claim about real patients' outcomes.

Run:
    python -m src.evaluate
"""
from __future__ import annotations

import sys

import pandas as pd

from src import config
from src.render import BAND_HEX, BAND_RGB

TIERS = ["clinician", "ASHA", "mother"]
RATINGS = {"Pass", "Partial", "Fail", "Deferred"}

METHOD_NOTE = (
    "This is a single-evaluator, author-conducted heuristic evaluation against "
    "WCAG 2.1 (POUR) and Nielsen's 10 usability heuristics — a formative, "
    "design-stage assessment. It is NOT user testing and NOT a multi-evaluator "
    "study. No usability scores, evaluator panels, or user feedback are implied. "
    "User studies with ASHAs, mothers, and clinicians are future work, gated on "
    "the ethics clearance noted in Limitations."
)


# ---------------------------------------------------------------------------
# WCAG contrast, computed from the live palette (the part worth a self-check)
# ---------------------------------------------------------------------------
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


def _hex(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


WHITE, INK = (255, 255, 255), (26, 26, 26)
UNLIT = {k: tuple(int(c * 0.22 + 60) for c in v) for k, v in BAND_RGB.items()}  # src.render
HOUSING = (43, 43, 43)  # #2b2b2b traffic-light body

CR = {
    "asha_amber": contrast(WHITE, _hex(BAND_HEX["AMBER"])),      # 2.12 — fails
    "asha_green": contrast(WHITE, _hex(BAND_HEX["GREEN"])),      # 3.38 — large-text pass
    "asha_amber_fixed": contrast(INK, _hex(BAND_HEX["AMBER"])),  # 8.23 — the fix
    "clinician_disclaimer": contrast((85, 85, 85), WHITE),       # #555 italic 8pt
    "shap_pos": contrast(_hex("#ff0051"), WHITE),
    "shap_neg": contrast(_hex("#008bfb"), WHITE),
    "lamp_lit": contrast(BAND_RGB["AMBER"], HOUSING),
    "lamp_lit_vs_unlit": contrast(BAND_RGB["AMBER"], UNLIT["RED"]),
    "lamp_unlit": contrast(UNLIT["RED"], HOUSING),
}
_R = {k: f"{v:.2f}:1" for k, v in CR.items()}


# ---------------------------------------------------------------------------
# The assessment. Authored data: (block, criterion, {tier: (rating, why)}).
# Every "why" names something visible in the artifact or in src/render.py.
# ---------------------------------------------------------------------------
ASSESSMENT: list[tuple[str, str, dict[str, tuple[str, str]]]] = [
    ("Perceivable", "1.1.1 Text alternative for non-text content", {
        "clinician": ("Partial",
            "Every number is burned into the PNG and this is the only tier with no text sibling — "
            "tier_asha_*.txt and tier_mother_*_hi.txt exist, tier_clinician_*.txt does not; the "
            "nearest machine-readable form is shap_case_contributions.csv, which is data, not a caption."),
        "ASHA": ("Pass",
            "`results/tables/tier_asha_<case>.txt` reproduces the card verbatim — band, both drivers, "
            "next step, accountability line, disclaimer — so nothing on the PNG is image-only."),
        "mother": ("Partial",
            "The spoken line has a deterministic transcript on disk (`tier_mother_<case>_hi.txt`), but "
            "render_mother() draws three ellipses and nothing else: no caption is rendered, so a deaf "
            "or hard-of-hearing viewer gets no text alternative in the artifact she is handed."),
    }),
    ("Perceivable", "1.4.1 Use of colour (colour not the only cue)", {
        "clinician": ("Pass",
            "Bar direction plus a signed numeric label carries every SHAP sign without hue "
            "(BS +0.204, DiastolicBP -0.024 on boundary_mid); probability bars are labelled with "
            "class name and value, so the green/amber/red fill is redundant."),
        "ASHA": ("Pass",
            "The header colour restates the header text — 'ROUTINE' on green, 'ELEVATED — needs "
            "follow-up' on amber; removing all colour loses no information."),
        "mother": ("Partial",
            f"Hue is the primary cue. Two redundancies verified: lamp POSITION is fixed (red top / "
            f"amber middle / green bottom) and lit-vs-unlit differs by {_R['lamp_lit_vs_unlit']} in "
            f"luminance, so which lamp is lit survives colour-vision deficiency; the spoken Hindi line "
            f"is a second non-colour channel. Residual gap: a viewer who is both colour-blind and deaf "
            f"has position only, and position assumes the traffic-light convention."),
    }),
    ("Perceivable", "1.4.3 Contrast (minimum)", {
        "clinician": ("Pass",
            f"Text is matplotlib near-black on white; the smallest element, the 8pt italic disclaimer "
            f"at #555, measures {_R['clinician_disclaimer']}. Bar fills measure {_R['shap_pos']} and "
            f"{_R['shap_neg']} against white, clearing the 3:1 non-text threshold (1.4.11)."),
        "ASHA": ("Fail",
            f"White bold header text on the ELEVATED amber measures {_R['asha_amber']} — below the 3:1 "
            f"large-text minimum. The ROUTINE green passes at {_R['asha_green']}. Amber is the header "
            f"for three of the four rendered cases, so the failing state is the common one; "
            f"near-black on the same amber would measure {_R['asha_amber_fixed']}."),
        "mother": ("Pass",
            f"No text to contrast. The perceivable object is the lit lamp, which measures "
            f"{_R['lamp_lit']} against the #2b2b2b housing. Caveat named honestly: the unlit lamps sit "
            f"at {_R['lamp_unlit']} against the housing, so on a low-fidelity print or a dim screen the "
            f"three-lamp layout that carries the position cue may read as one lamp on a dark slab."),
    }),
    ("Perceivable", "1.4.5 Images of text", {
        "clinician": ("Fail",
            "Titles, axis labels, the probability values and the raw-value table are all rasterised at "
            "150 dpi: text cannot be resized, reflowed, restyled or selected, and no text sibling exists."),
        "ASHA": ("Partial",
            "The card itself is an image of text and fails as rendered, but the verbatim .txt sibling "
            "gives a deployment a conforming, restylable source for every string on it."),
        "mother": ("Pass",
            "Vacuously — the visual contains no text at all. Note the tension: the same design choice "
            "that clears 1.4.5 here is what makes 1.1.1 Partial above."),
    }),
    ("Operable", "2.1 / 2.4 Keyboard, focus order, navigation", {
        "clinician": ("Deferred",
            "Static PNG with no controls. Keyboard operability and focus order are properties of the "
            "dashboard that would embed this figure — relevant at deployment, not exercisable here."),
        "ASHA": ("Deferred",
            "Static card. Navigation, dismissal and re-display belong to the host app (an ANMOL-style "
            "Android form) — relevant at deployment."),
        "mother": ("Deferred",
            "Relevant at deployment and non-trivial: an IVR delivery must offer repeat-the-message and "
            "must not time out (2.2.1). A one-shot MP3 file cannot exercise either, and we do not "
            "claim a rating it cannot earn."),
    }),
    ("Understandable", "3.1.1 / 3.1.2 Language of page and of parts", {
        "clinician": ("Pass",
            "Single language throughout (English), consistent across all four cases, matching the "
            "tier's stated reader."),
        "ASHA": ("Partial",
            "English only. The tier's user is a community health worker who may read a regional "
            "language first, and the tier below her (mother) IS localised — so the middle tier is the "
            "one gap in the chain. The template design supports localisation: every string is a fixed "
            "constant (PLAIN_NAMES, ASHA_NEXT_STEP, ASHA_FOOTER) with no generation at inference."),
        "mother": ("Partial",
            "Hindi text with a matching Hindi TTS voice (lang='hi'), which is right. But the message "
            "embeds the Latin-script acronym 'ANM' inside Devanagari with no language-of-parts marking, "
            "and a Hindi engine may voice it unpredictably — the one wrinkle in an otherwise clean tier."),
    }),
    ("Understandable", "3.1.5 Reading level / plain language", {
        "clinician": ("Partial",
            "Deliberately technical — 'SHAP waterfall', 'base E[f(x)] = 0.250' — which is correct for a "
            "trained reader but fails the letter of 3.1.5, since the tier carries no simpler supplement "
            "of its own. The supplement exists: it is the other two tiers. That is the architecture's point."),
        "ASHA": ("Partial",
            "Short sentences and field vocabulary via the fixed PLAIN_NAMES map ('raised blood sugar', "
            "not a clinical term). Above plain register: the header word 'ELEVATED' and the phrase "
            "'medical officer', both of which a lower-literacy reader may stumble on."),
        "mother": ("Pass",
            "One spoken Hindi sentence, no number, no percentage, no condition named, ending in an "
            "action ('please get checked at your ANM or the nearest health centre soon'). Requires no "
            "literacy of any kind — the only tier of the three that does not."),
    }),
    ("Understandable", "3.2.4 Consistent identification", {
        "clinician": ("Pass",
            "Class colours (green/amber/red for low/mid/high) are the same palette the other tiers use, "
            "and identical across all four cases."),
        "ASHA": ("Fail",
            "The card band is binary — render_asha() colours by 'is the prediction low risk', collapsing "
            "mid and high — so confident_high renders an AMBER card while the SAME case renders a RED "
            "lamp to the mother. One prediction is identified by two different colours in two tiers."),
        "mother": ("Pass",
            "Three bands mapped consistently to the shared palette; the same band always renders the "
            "same lamp and the same sentence (boundary_mid and failure_mode produce byte-identical "
            "Hindi text, as they should)."),
    }),
    ("Robust", "4.1.2 Name, role, value", {
        "clinician": ("Deferred",
            "PNG and MP3 carry no programmatic semantics; assistive-technology exposure is a property "
            "of the host app. Noted for deployment: this tier ships no accessible string, so an "
            "implementer has to author one."),
        "ASHA": ("Deferred",
            "Same — but the .txt sibling hands a deployment a ready accessible name/value for the card."),
        "mother": ("Deferred",
            "Same — the Hindi transcript is the ready accessible string; the lamp itself has no role or "
            "state exposed and would need one in an app."),
    }),

    ("Nielsen", "1. Visibility of system status", {
        "clinician": ("Pass",
            "Shows true class, predicted class, all three probabilities to three decimals, the base "
            "value and f(x). On boundary_mid the reader sees 0.487 vs 0.499 and knows immediately that "
            "the call is a coin flip."),
        "ASHA": ("Partial",
            "The card states a band but never how certain the model was: boundary_mid (top-2 margin "
            "0.012) and confident_high (margin 1.000) print the identical 'ELEVATED — needs follow-up' "
            "header. The ASHA is the person acting on it, and she gets no confidence signal."),
        "mother": ("Pass",
            "Status is exactly one lamp, and model uncertainty is what chooses it (see error prevention). "
            "By design the tier reports an action, not a state — which is the right 'status' for it."),
    }),
    ("Nielsen", "2. Match between system and the real world", {
        "clinician": ("Pass",
            "Raw clinical units on the axis (BS = 9, BodyTemp = 102, SystolicBP = 85), not model-space "
            "values — the final model uses no scaler, so the waterfall reads in the clinician's own units."),
        "ASHA": ("Partial",
            "The phrasing matches field speech, but the direction word is median-relative, not clinical: "
            "confident_low prints 'raised blood sugar' for BS = 7.7 against a dataset median of 7.5. An "
            "unremarkable reading is worded as a concern."),
        "mother": ("Pass",
            "A traffic light is a near-universal metaphor, and the sentence names the real institutions "
            "in her world — her ANM, the nearest health centre — and opens by telling her not to panic, "
            "which is how the news would be delivered in person."),
    }),
    ("Nielsen", "4. Consistency and standards", {
        "clinician": ("Pass",
            "Layout, palette and label conventions are identical across all four rendered cases; the "
            "figure is generated by one code path with no per-case special-casing."),
        "ASHA": ("Fail",
            "The heading 'What the model flagged for follow-up:' is fixed text printed on every card, "
            "including the ROUTINE one — where the two features listed (raised blood sugar, low upper "
            "blood pressure on confident_low) are the top contributors TO the low-risk prediction. The "
            "same sentence means opposite things on different cards, and the ROUTINE card still tells "
            "the reader to arrange a check-up."),
        "mother": ("Pass",
            "One image and one sentence per band, fixed; nothing varies between cases that share a band."),
    }),
    ("Nielsen", "5. Error prevention", {
        "clinician": ("Pass",
            "The tier surfaces its own failure rather than hiding it: on failure_mode the waterfall "
            "shows BodyTemp +0.216 driving a high-risk call in a 13-year-old while blood sugar argues "
            "against it, and true vs predicted are both printed in the title. A reader can catch the "
            "spurious flag from the figure alone."),
        "ASHA": ("Partial",
            "Strong on accountability — nothing is a diagnosis, the footer returns the referral decision "
            "to the human, the next step carries no medical timeframe. Weak on direction: top_drivers() "
            "ranks by |SHAP| with no sign filter, so a feature that argues AGAINST the prediction can be "
            "printed as a flag. Verified on failure_mode, where 'low blood sugar' is listed although its "
            "contribution to the predicted class is -0.085 — it pushed away from high risk."),
        "mother": ("Pass",
            "The uncertainty-aware down-ranking is a genuine control, not a cosmetic one: RED requires "
            "predicted-high AND a top-2 margin >= 0.15, so boundary_mid (0.012) and failure_mode (0.002) "
            "both light AMBER. failure_mode is a true-low case, so the rule demonstrably suppressed a "
            "false red alarm to a mother. This is the strongest single design decision in the three tiers."),
    }),
    ("Nielsen", "6. Recognition rather than recall", {
        "clinician": ("Partial",
            "The waterfall assumes recalled SHAP conventions: nothing on the figure states that red "
            "pushes toward the predicted class or what 'base E[f(x)]' is. One legend line would close it."),
        "ASHA": ("Pass",
            "Everything needed to act is on the card — band, the two drivers, the next step, who decides. "
            "Nothing has to be remembered from a previous screen or a training session."),
        "mother": ("Partial",
            "The lamp requires recalling the traffic-light convention, and nothing on the image explains "
            "it. Recognition is restored only by the audio, which is a separate channel and may not be "
            "co-present with the picture."),
    }),
    ("Nielsen", "8. Aesthetic and minimalist design", {
        "clinician": ("Partial",
            "Three panels, no chrome, every element carrying data — but the raw-value table repeats the "
            "values already printed on the waterfall's y-axis labels ('BS = 9' and 'BS | 9'). Minor, and "
            "the only redundancy in the tier."),
        "ASHA": ("Pass",
            "Five elements: band, two drivers, action, accountability line, disclaimer. Nothing on the "
            "card can be removed without losing something the ASHA needs."),
        "mother": ("Pass",
            "Three circles on a housing. There is nothing left to strip — though see help and "
            "documentation for what that minimalism costs."),
    }),
    ("Nielsen", "10. Help and documentation", {
        "clinician": ("Partial",
            "The disclaimer is present on the figure, but there is no legend, no method note and no "
            "pointer to how the case was selected; the reader has to go to the repository."),
        "ASHA": ("Pass",
            "The card carries both the accountability line and the full disclaimer, so the person acting "
            "on it is told what it is and who decides."),
        "mother": ("Fail",
            "Nothing on the mother artifact says what it is, where it came from, or that it is not a "
            "diagnosis. The disclaimer that both other tiers carry is absent from the image, and the "
            "spoken line does not carry it either. A mother receiving lamp plus voice has no route to "
            "help beyond 'go to the ANM'. Deliberate (the tier is text-free by design) but a real gap; "
            "a short spoken provenance clause is the obvious fix."),
    }),
]

# Ranked gaps. Each is (title, evidence, fix) and each traces to a cell above.
GAPS = [
    ("ASHA driver list is sign-blind",
     "top_drivers() in src/render.py sorts by |SHAP| only, so a feature arguing against the prediction "
     "can be printed under 'What the model flagged for follow-up'. failure_mode lists 'low blood sugar' "
     "with a contribution of -0.085 to the predicted class; confident_low lists two features that are "
     "the reasons the model said LOW.",
     "Filter to positive contributions for the predicted class, or word negative ones explicitly as "
     "'argues against'. Highest priority: this is the one gap that can put a wrong cue in front of the "
     "person making the referral."),
    ("ASHA header text fails contrast in its most common state",
     f"White bold on the ELEVATED amber measures {_R['asha_amber']}, under the 3:1 large-text minimum "
     f"(WCAG 1.4.3); amber is the header for three of the four rendered cases.",
     f"Near-black header text on the same amber measures {_R['asha_amber_fixed']} — a one-constant change."),
    ("Mother visual has no rendered text alternative",
     "The traffic light is text-free by design (Decision Log #6), so a deaf or hard-of-hearing mother "
     "has no channel: the Hindi transcript exists only as a file on disk, not on the artifact.",
     "A rendered caption or an SMS companion carrying the same templated sentence. Future work — it "
     "reopens the literacy assumption the tier was built to avoid, so it needs user input, not a "
     "unilateral design call."),
    ("Mother tier carries no provenance in any channel",
     "Neither the image nor the spoken line states that this is an illustrative, non-diagnostic output, "
     "while both other tiers print the disclaimer.",
     "A short spoken provenance clause appended to each band's template — audio, so it costs no literacy."),
    ("Same prediction, two colours across tiers",
     "render_asha() bands binary (low vs not-low) while the mother tier bands three ways with an "
     "uncertainty rule, so confident_high is amber on the card and red on the lamp.",
     "Give the ASHA card the same three-band function the mother tier uses, and show the band name as "
     "text as it already does."),
    ("Everything is an image of text",
     "All three tiers ship as rasterised PNG (WCAG 1.4.5); text cannot be resized or restyled. The "
     "ASHA and mother tiers have .txt siblings, the clinician tier has none.",
     "Emit a `tier_clinician_<case>.txt` alongside the figure; treat SVG or in-app rendering as the "
     "deployment answer."),
    ("'Raised' and 'low' are median-relative, not clinical",
     "The direction word compares the reading to the dataset median (BS 7.7 vs 7.5 prints 'raised'), so "
     "a trivial deviation is worded like a concern.",
     "A deadband around the median, or reference ranges — the latter needs clinical input this preprint "
     "deliberately does not claim."),
    ("ASHA tier is English-only",
     "The mother tier is localised to Hindi; the tier between her and the clinician is not.",
     "Translate the fixed template constants. Cheap, because the tier is template-based by design — "
     "there is no generated text to translate at inference."),
]

SYNTHESIS = """\
The three tiers are one system rendered three ways, and the evaluation separates
cleanly along that line.

**Universal Design says one system should serve everyone.** It does not follow that
one *rendering* can. Read the matrix column by column and each tier fails exactly
where a single universal artifact would have to compromise: the clinician tier is
unreadable without chart and English literacy (3.1.5), the mother tier is
unreadable without hearing (1.1.1), and neither weakness is repairable inside its
own tier without destroying what that tier is for. Read it row by row instead and
the criteria are covered — the system as a whole carries a technical view, a
plain-language view and a non-literate view of the same prediction. The
architecture is what conforms; no single output does.

**Ability-Based Design says build on what the user can do.** Each tier does, and
the evaluation can name what each one assumes: charts and SHAP conventions
(clinician), functional literacy in English (ASHA), hearing and the traffic-light
convention (mother). Stating the assumption is what makes the gap findable — the
deaf-and-colour-blind intersection at the mother tier is visible precisely because
the tier declares that it leans on hearing.

**The strongest result is the uncertainty-aware down-ranking.** RED requires both
a high-risk prediction and a top-2 margin of at least 0.15, so the two knife-edge
cases (margins 0.012 and 0.002) reach the mother as AMBER rather than as an alarm —
and one of those two is a true-low case, so the rule visibly suppressed a false
red. Model uncertainty is rendered as caution rather than discarded at the tier
where the reader has the least ability to discount it. That is the transfer worth
carrying to other three-tier systems.

**The weakest result is the ASHA tier**, and it is weak in an instructive way. Its
two content defects — the sign-blind driver list (error prevention) and the fixed
'flagged for follow-up' heading on a routine card (consistency, and the tier's one
outright Fail on content rather than colour) — come from one root: the template
renders |SHAP| magnitude while the sentence around it asserts direction. The
template approach is right (deterministic, reproducible, no hallucination); this
particular template is under-specified. That is a fixable defect, not an argument
for a language model at inference.

{deferred} of the {total} cells are Deferred, all of them operability and
robustness. That is not evasion, it is the honest boundary of a static-artifact
evaluation: keyboard access, focus order, IVR replay and timing, and
assistive-technology semantics are properties of a deployed application. They are
recorded as relevant-at-deployment so that a later study inherits the list rather
than rediscovering it."""


# ---------------------------------------------------------------------------
def build_rows() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {"block": block, "criterion": crit, "tier": tier,
             "rating": rating, "rationale": " ".join(why.split())}
            for block, crit, cells in ASSESSMENT
            for tier in TIERS
            for rating, why in [cells[tier]]
        ]
    )


def _selfcheck(df: pd.DataFrame) -> None:
    assert round(contrast(WHITE, (0, 0, 0)), 2) == 21.0
    assert CR["asha_amber"] < 3.0 < CR["asha_amber_fixed"]  # the finding and its fix
    assert set(df.rating) <= RATINGS
    assert len(df) == len(ASSESSMENT) * 3 and not df.rationale.eq("").any()
    assert df.rating.nunique() == 4, "a matrix that is all one rating is a rubber stamp"
    assert (df.rating == "Pass").mean() < 0.6, "too many passes to be an honest evaluation"


def write_csv(df: pd.DataFrame):
    out = config.TABLES_DIR / "heuristic_matrix.csv"
    df.to_csv(out, index=False)
    return out


def write_markdown(df: pd.DataFrame):
    counts = df.rating.value_counts()
    grid = df.pivot(index="criterion", columns="tier", values="rating").reindex(
        [c for _, c, _ in ASSESSMENT]
    )[TIERS]

    L = [
        "# Phase 4 — Heuristic evaluation of the three-tier renderer",
        "",
        "One prediction from a public-data model, rendered as a clinician dashboard, an ASHA "
        "plain-language card, and a mother-to-be traffic light with a spoken message. This "
        "document evaluates those three renderings as an *explanation design*.",
        "",
        "## Method and limitations",
        "",
        "> " + METHOD_NOTE,
        "",
        "Scope notes, stated so no reader has to infer them:",
        "",
        "- Every rating below is grounded in a specific detail of an artifact on disk or in the "
        "code that produced it. Contrast ratios are computed at run time from the palette "
        "constants in `src/render.py`, not typed in by hand.",
        "- The artifacts assessed are the four rendered cases — `boundary_mid` (primary), "
        "`confident_low`, `confident_high`, `failure_mode` — across `results/figures/tier_*.png`, "
        "`results/tables/tier_*.txt` and `results/audio/tier_mother_*_hi.mp3`.",
        "- This evaluates an explanation design on the public UCI Maternal Health Risk dataset. "
        "Nothing here claims the underlying prediction is clinically valid or applicable to real "
        "patients, and no condition is named in any tier.",
        "",
        "### Rating scale",
        "",
        "| Rating | Meaning |",
        "|---|---|",
        "| **Pass** | The artifact satisfies the criterion, for a stated reason. |",
        "| **Partial** | Satisfied in part; a specific, named shortfall remains. |",
        "| **Fail** | Not satisfied; the defect is named and a fix is given. |",
        "| **Deferred** | A static artifact cannot exercise this. Relevant at deployment "
        "(an ANMOL-style app or an IVR call flow), recorded rather than faked. |",
        "",
        f"Distribution across {len(df)} cells: "
        + ", ".join(f"{counts.get(r, 0)} {r}" for r in ["Pass", "Partial", "Fail", "Deferred"])
        + ".",
        "",
        "## Matrix",
        "",
        "| Criterion | Clinician | ASHA | Mother-to-be |",
        "|---|---|---|---|",
    ]
    for crit, row in grid.iterrows():
        L.append(f"| {crit} | {row['clinician']} | {row['ASHA']} | {row['mother']} |")

    L += ["", "## Findings, cell by cell", ""]
    for block, crit, cells in ASSESSMENT:
        L += [f"### {crit}", f"*{block}*", ""]
        for tier in TIERS:
            rating, why = cells[tier]
            L.append(f"- **{tier} — {rating}.** {' '.join(why.split())}")
        L.append("")

    L += ["## Accessibility gaps identified", "",
          "Ranked by how much harm the gap can do to the person reading that tier.", ""]
    for i, (title, evidence, fix) in enumerate(GAPS, 1):
        L += [f"**{i}. {title}**", "",
              f"- *Evidence:* {' '.join(evidence.split())}",
              f"- *Fix:* {' '.join(fix.split())}", ""]

    L += ["## Synthesis", "",
          SYNTHESIS.format(deferred=counts.get("Deferred", 0), total=len(df)), "",
          "---", "",
          f"Generated by `python -m src.evaluate`. Machine-readable form: "
          f"`results/tables/heuristic_matrix.csv`."]

    out = config.TABLES_DIR / "heuristic_evaluation.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    return out


def run() -> None:
    config.set_seeds()
    df = build_rows()
    _selfcheck(df)
    config.TABLES_DIR.mkdir(parents=True, exist_ok=True)

    print("Phase 4 — heuristic evaluation (WCAG 2.1 + Nielsen)")
    print("=" * 60)
    print("Single-evaluator, author-conducted, formative. Not user testing.")
    print(f"\n{len(ASSESSMENT)} criteria x {len(TIERS)} tiers = {len(df)} cells")
    for rating in ["Pass", "Partial", "Fail", "Deferred"]:
        print(f"  {rating:<9} {(df.rating == rating).sum():>3}")
    print("\nFails:")
    for r in df[df.rating == "Fail"].itertuples():
        print(f"  {r.tier:<10} {r.criterion}")
    print(f"\n  -> {write_csv(df)}")
    print(f"  -> {write_markdown(df)}")
    print("\nOK")


if __name__ == "__main__":
    run()
    sys.exit(0)
