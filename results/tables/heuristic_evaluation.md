# Phase 4 — Heuristic evaluation of the three-tier renderer

One prediction from a public-data model, rendered as a clinician dashboard, an ASHA plain-language card, and a mother-to-be traffic light with a spoken message. This document evaluates those three renderings as an *explanation design*.

## Method and limitations

> This is a single-evaluator, author-conducted heuristic evaluation against WCAG 2.1 (POUR) and Nielsen's 10 usability heuristics — a formative, design-stage assessment. It is NOT user testing and NOT a multi-evaluator study. No usability scores, evaluator panels, or user feedback are implied. User studies with ASHAs, mothers, and clinicians are future work, gated on the ethics clearance noted in Limitations.

Scope notes, stated so no reader has to infer them:

- Every rating below is grounded in a specific detail of an artifact on disk or in the code that produced it. Contrast ratios are computed at run time from the palette constants in `src/render.py`, not typed in by hand.
- The artifacts assessed are the four rendered cases — `boundary_mid` (primary), `confident_low`, `confident_high`, `failure_mode` — across `results/figures/tier_*.png`, `results/tables/tier_*.txt` and `results/audio/tier_mother_*_hi.mp3`.
- This evaluates an explanation design on the public UCI Maternal Health Risk dataset. Nothing here claims the underlying prediction is clinically valid or applicable to real patients, and no condition is named in any tier.

### Rating scale

| Rating | Meaning |
|---|---|
| **Pass** | The artifact satisfies the criterion, for a stated reason. |
| **Partial** | Satisfied in part; a specific, named shortfall remains. |
| **Fail** | Not satisfied; the defect is named and a fix is given. |
| **Deferred** | A static artifact cannot exercise this. Relevant at deployment (an ANMOL-style app or an IVR call flow), recorded rather than faked. |

Distribution across 48 cells: 22 Pass, 15 Partial, 5 Fail, 6 Deferred.

## Matrix

| Criterion | Clinician | ASHA | Mother-to-be |
|---|---|---|---|
| 1.1.1 Text alternative for non-text content | Partial | Pass | Partial |
| 1.4.1 Use of colour (colour not the only cue) | Pass | Pass | Partial |
| 1.4.3 Contrast (minimum) | Pass | Fail | Pass |
| 1.4.5 Images of text | Fail | Partial | Pass |
| 2.1 / 2.4 Keyboard, focus order, navigation | Deferred | Deferred | Deferred |
| 3.1.1 / 3.1.2 Language of page and of parts | Pass | Partial | Partial |
| 3.1.5 Reading level / plain language | Partial | Partial | Pass |
| 3.2.4 Consistent identification | Pass | Fail | Pass |
| 4.1.2 Name, role, value | Deferred | Deferred | Deferred |
| 1. Visibility of system status | Pass | Partial | Pass |
| 2. Match between system and the real world | Pass | Partial | Pass |
| 4. Consistency and standards | Pass | Fail | Pass |
| 5. Error prevention | Pass | Partial | Pass |
| 6. Recognition rather than recall | Partial | Pass | Partial |
| 8. Aesthetic and minimalist design | Partial | Pass | Pass |
| 10. Help and documentation | Partial | Pass | Fail |

## Findings, cell by cell

### 1.1.1 Text alternative for non-text content
*Perceivable*

- **clinician — Partial.** Every number is burned into the PNG and this is the only tier with no text sibling — tier_asha_*.txt and tier_mother_*_hi.txt exist, tier_clinician_*.txt does not; the nearest machine-readable form is shap_case_contributions.csv, which is data, not a caption.
- **ASHA — Pass.** `results/tables/tier_asha_<case>.txt` reproduces the card verbatim — band, both drivers, next step, accountability line, disclaimer — so nothing on the PNG is image-only.
- **mother — Partial.** The spoken line has a deterministic transcript on disk (`tier_mother_<case>_hi.txt`), but render_mother() draws three ellipses and nothing else: no caption is rendered, so a deaf or hard-of-hearing viewer gets no text alternative in the artifact she is handed.

### 1.4.1 Use of colour (colour not the only cue)
*Perceivable*

- **clinician — Pass.** Bar direction plus a signed numeric label carries every SHAP sign without hue (BS +0.204, DiastolicBP -0.024 on boundary_mid); probability bars are labelled with class name and value, so the green/amber/red fill is redundant.
- **ASHA — Pass.** The header colour restates the header text — 'ROUTINE' on green, 'ELEVATED — needs follow-up' on amber; removing all colour loses no information.
- **mother — Partial.** Hue is the primary cue. Two redundancies verified: lamp POSITION is fixed (red top / amber middle / green bottom) and lit-vs-unlit differs by 3.97:1 in luminance, so which lamp is lit survives colour-vision deficiency; the spoken Hindi line is a second non-colour channel. Residual gap: a viewer who is both colour-blind and deaf has position only, and position assumes the traffic-light convention.

### 1.4.3 Contrast (minimum)
*Perceivable*

- **clinician — Pass.** Text is matplotlib near-black on white; the smallest element, the 8pt italic disclaimer at #555, measures 7.46:1. Bar fills measure 3.91:1 and 3.45:1 against white, clearing the 3:1 non-text threshold (1.4.11).
- **ASHA — Fail.** White bold header text on the ELEVATED amber measures 2.12:1 — below the 3:1 large-text minimum. The ROUTINE green passes at 3.38:1. Amber is the header for three of the four rendered cases, so the failing state is the common one; near-black on the same amber would measure 8.23:1.
- **mother — Pass.** No text to contrast. The perceivable object is the lit lamp, which measures 6.69:1 against the #2b2b2b housing. Caveat named honestly: the unlit lamps sit at 1.68:1 against the housing, so on a low-fidelity print or a dim screen the three-lamp layout that carries the position cue may read as one lamp on a dark slab.

### 1.4.5 Images of text
*Perceivable*

- **clinician — Fail.** Titles, axis labels, the probability values and the raw-value table are all rasterised at 150 dpi: text cannot be resized, reflowed, restyled or selected, and no text sibling exists.
- **ASHA — Partial.** The card itself is an image of text and fails as rendered, but the verbatim .txt sibling gives a deployment a conforming, restylable source for every string on it.
- **mother — Pass.** Vacuously — the visual contains no text at all. Note the tension: the same design choice that clears 1.4.5 here is what makes 1.1.1 Partial above.

### 2.1 / 2.4 Keyboard, focus order, navigation
*Operable*

- **clinician — Deferred.** Static PNG with no controls. Keyboard operability and focus order are properties of the dashboard that would embed this figure — relevant at deployment, not exercisable here.
- **ASHA — Deferred.** Static card. Navigation, dismissal and re-display belong to the host app (an ANMOL-style Android form) — relevant at deployment.
- **mother — Deferred.** Relevant at deployment and non-trivial: an IVR delivery must offer repeat-the-message and must not time out (2.2.1). A one-shot MP3 file cannot exercise either, and we do not claim a rating it cannot earn.

### 3.1.1 / 3.1.2 Language of page and of parts
*Understandable*

- **clinician — Pass.** Single language throughout (English), consistent across all four cases, matching the tier's stated reader.
- **ASHA — Partial.** English only. The tier's user is a community health worker who may read a regional language first, and the tier below her (mother) IS localised — so the middle tier is the one gap in the chain. The template design supports localisation: every string is a fixed constant (PLAIN_NAMES, ASHA_NEXT_STEP, ASHA_FOOTER) with no generation at inference.
- **mother — Partial.** Hindi text with a matching Hindi TTS voice (lang='hi'), which is right. But the message embeds the Latin-script acronym 'ANM' inside Devanagari with no language-of-parts marking, and a Hindi engine may voice it unpredictably — the one wrinkle in an otherwise clean tier.

### 3.1.5 Reading level / plain language
*Understandable*

- **clinician — Partial.** Deliberately technical — 'SHAP waterfall', 'base E[f(x)] = 0.250' — which is correct for a trained reader but fails the letter of 3.1.5, since the tier carries no simpler supplement of its own. The supplement exists: it is the other two tiers. That is the architecture's point.
- **ASHA — Partial.** Short sentences and field vocabulary via the fixed PLAIN_NAMES map ('raised blood sugar', not a clinical term). Above plain register: the header word 'ELEVATED' and the phrase 'medical officer', both of which a lower-literacy reader may stumble on.
- **mother — Pass.** One spoken Hindi sentence, no number, no percentage, no condition named, ending in an action ('please get checked at your ANM or the nearest health centre soon'). Requires no literacy of any kind — the only tier of the three that does not.

### 3.2.4 Consistent identification
*Understandable*

- **clinician — Pass.** Class colours (green/amber/red for low/mid/high) are the same palette the other tiers use, and identical across all four cases.
- **ASHA — Fail.** The card band is binary — render_asha() colours by 'is the prediction low risk', collapsing mid and high — so confident_high renders an AMBER card while the SAME case renders a RED lamp to the mother. One prediction is identified by two different colours in two tiers.
- **mother — Pass.** Three bands mapped consistently to the shared palette; the same band always renders the same lamp and the same sentence (boundary_mid and failure_mode produce byte-identical Hindi text, as they should).

### 4.1.2 Name, role, value
*Robust*

- **clinician — Deferred.** PNG and MP3 carry no programmatic semantics; assistive-technology exposure is a property of the host app. Noted for deployment: this tier ships no accessible string, so an implementer has to author one.
- **ASHA — Deferred.** Same — but the .txt sibling hands a deployment a ready accessible name/value for the card.
- **mother — Deferred.** Same — the Hindi transcript is the ready accessible string; the lamp itself has no role or state exposed and would need one in an app.

### 1. Visibility of system status
*Nielsen*

- **clinician — Pass.** Shows true class, predicted class, all three probabilities to three decimals, the base value and f(x). On boundary_mid the reader sees 0.487 vs 0.499 and knows immediately that the call is a coin flip.
- **ASHA — Partial.** The card states a band but never how certain the model was: boundary_mid (top-2 margin 0.012) and confident_high (margin 1.000) print the identical 'ELEVATED — needs follow-up' header. The ASHA is the person acting on it, and she gets no confidence signal.
- **mother — Pass.** Status is exactly one lamp, and model uncertainty is what chooses it (see error prevention). By design the tier reports an action, not a state — which is the right 'status' for it.

### 2. Match between system and the real world
*Nielsen*

- **clinician — Pass.** Raw clinical units on the axis (BS = 9, BodyTemp = 102, SystolicBP = 85), not model-space values — the final model uses no scaler, so the waterfall reads in the clinician's own units.
- **ASHA — Partial.** The phrasing matches field speech, but the direction word is median-relative, not clinical: confident_low prints 'raised blood sugar' for BS = 7.7 against a dataset median of 7.5. An unremarkable reading is worded as a concern.
- **mother — Pass.** A traffic light is a near-universal metaphor, and the sentence names the real institutions in her world — her ANM, the nearest health centre — and opens by telling her not to panic, which is how the news would be delivered in person.

### 4. Consistency and standards
*Nielsen*

- **clinician — Pass.** Layout, palette and label conventions are identical across all four rendered cases; the figure is generated by one code path with no per-case special-casing.
- **ASHA — Fail.** The heading 'What the model flagged for follow-up:' is fixed text printed on every card, including the ROUTINE one — where the two features listed (raised blood sugar, low upper blood pressure on confident_low) are the top contributors TO the low-risk prediction. The same sentence means opposite things on different cards, and the ROUTINE card still tells the reader to arrange a check-up.
- **mother — Pass.** One image and one sentence per band, fixed; nothing varies between cases that share a band.

### 5. Error prevention
*Nielsen*

- **clinician — Pass.** The tier surfaces its own failure rather than hiding it: on failure_mode the waterfall shows BodyTemp +0.216 driving a high-risk call in a 13-year-old while blood sugar argues against it, and true vs predicted are both printed in the title. A reader can catch the spurious flag from the figure alone.
- **ASHA — Partial.** Strong on accountability — nothing is a diagnosis, the footer returns the referral decision to the human, the next step carries no medical timeframe. Weak on direction: top_drivers() ranks by |SHAP| with no sign filter, so a feature that argues AGAINST the prediction can be printed as a flag. Verified on failure_mode, where 'low blood sugar' is listed although its contribution to the predicted class is -0.085 — it pushed away from high risk.
- **mother — Pass.** The uncertainty-aware down-ranking is a genuine control, not a cosmetic one: RED requires predicted-high AND a top-2 margin >= 0.15, so boundary_mid (0.012) and failure_mode (0.002) both light AMBER. failure_mode is a true-low case, so the rule demonstrably suppressed a false red alarm to a mother. This is the strongest single design decision in the three tiers.

### 6. Recognition rather than recall
*Nielsen*

- **clinician — Partial.** The waterfall assumes recalled SHAP conventions: nothing on the figure states that red pushes toward the predicted class or what 'base E[f(x)]' is. One legend line would close it.
- **ASHA — Pass.** Everything needed to act is on the card — band, the two drivers, the next step, who decides. Nothing has to be remembered from a previous screen or a training session.
- **mother — Partial.** The lamp requires recalling the traffic-light convention, and nothing on the image explains it. Recognition is restored only by the audio, which is a separate channel and may not be co-present with the picture.

### 8. Aesthetic and minimalist design
*Nielsen*

- **clinician — Partial.** Three panels, no chrome, every element carrying data — but the raw-value table repeats the values already printed on the waterfall's y-axis labels ('BS = 9' and 'BS | 9'). Minor, and the only redundancy in the tier.
- **ASHA — Pass.** Five elements: band, two drivers, action, accountability line, disclaimer. Nothing on the card can be removed without losing something the ASHA needs.
- **mother — Pass.** Three circles on a housing. There is nothing left to strip — though see help and documentation for what that minimalism costs.

### 10. Help and documentation
*Nielsen*

- **clinician — Partial.** The disclaimer is present on the figure, but there is no legend, no method note and no pointer to how the case was selected; the reader has to go to the repository.
- **ASHA — Pass.** The card carries both the accountability line and the full disclaimer, so the person acting on it is told what it is and who decides.
- **mother — Fail.** Nothing on the mother artifact says what it is, where it came from, or that it is not a diagnosis. The disclaimer that both other tiers carry is absent from the image, and the spoken line does not carry it either. A mother receiving lamp plus voice has no route to help beyond 'go to the ANM'. Deliberate (the tier is text-free by design) but a real gap; a short spoken provenance clause is the obvious fix.

## Accessibility gaps identified

Ranked by how much harm the gap can do to the person reading that tier.

**1. ASHA driver list is sign-blind**

- *Evidence:* top_drivers() in src/render.py sorts by |SHAP| only, so a feature arguing against the prediction can be printed under 'What the model flagged for follow-up'. failure_mode lists 'low blood sugar' with a contribution of -0.085 to the predicted class; confident_low lists two features that are the reasons the model said LOW.
- *Fix:* Filter to positive contributions for the predicted class, or word negative ones explicitly as 'argues against'. Highest priority: this is the one gap that can put a wrong cue in front of the person making the referral.

**2. ASHA header text fails contrast in its most common state**

- *Evidence:* White bold on the ELEVATED amber measures 2.12:1, under the 3:1 large-text minimum (WCAG 1.4.3); amber is the header for three of the four rendered cases.
- *Fix:* Near-black header text on the same amber measures 8.23:1 — a one-constant change.

**3. Mother visual has no rendered text alternative**

- *Evidence:* The traffic light is text-free by design (Decision Log #6), so a deaf or hard-of-hearing mother has no channel: the Hindi transcript exists only as a file on disk, not on the artifact.
- *Fix:* A rendered caption or an SMS companion carrying the same templated sentence. Future work — it reopens the literacy assumption the tier was built to avoid, so it needs user input, not a unilateral design call.

**4. Mother tier carries no provenance in any channel**

- *Evidence:* Neither the image nor the spoken line states that this is an illustrative, non-diagnostic output, while both other tiers print the disclaimer.
- *Fix:* A short spoken provenance clause appended to each band's template — audio, so it costs no literacy.

**5. Same prediction, two colours across tiers**

- *Evidence:* render_asha() bands binary (low vs not-low) while the mother tier bands three ways with an uncertainty rule, so confident_high is amber on the card and red on the lamp.
- *Fix:* Give the ASHA card the same three-band function the mother tier uses, and show the band name as text as it already does.

**6. Everything is an image of text**

- *Evidence:* All three tiers ship as rasterised PNG (WCAG 1.4.5); text cannot be resized or restyled. The ASHA and mother tiers have .txt siblings, the clinician tier has none.
- *Fix:* Emit a `tier_clinician_<case>.txt` alongside the figure; treat SVG or in-app rendering as the deployment answer.

**7. 'Raised' and 'low' are median-relative, not clinical**

- *Evidence:* The direction word compares the reading to the dataset median (BS 7.7 vs 7.5 prints 'raised'), so a trivial deviation is worded like a concern.
- *Fix:* A deadband around the median, or reference ranges — the latter needs clinical input this preprint deliberately does not claim.

**8. ASHA tier is English-only**

- *Evidence:* The mother tier is localised to Hindi; the tier between her and the clinician is not.
- *Fix:* Translate the fixed template constants. Cheap, because the tier is template-based by design — there is no generated text to translate at inference.

## Synthesis

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

6 of the 48 cells are Deferred, all of them operability and
robustness. That is not evasion, it is the honest boundary of a static-artifact
evaluation: keyboard access, focus order, IVR replay and timing, and
assistive-technology semantics are properties of a deployed application. They are
recorded as relevant-at-deployment so that a later study inherits the list rather
than rediscovering it.

---

Generated by `python -m src.evaluate`. Machine-readable form: `results/tables/heuristic_matrix.csv`.
