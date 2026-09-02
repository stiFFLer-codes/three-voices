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

Distribution across 48 cells: 28 Pass, 13 Partial, 1 Fail, 6 Deferred.

## Matrix

| Criterion | Clinician | ASHA | Mother-to-be |
|---|---|---|---|
| 1.1.1 Text alternative for non-text content | Partial | Pass | Partial |
| 1.4.1 Use of colour (colour not the only cue) | Pass | Pass | Partial |
| 1.4.3 Contrast (minimum) | Pass | Pass | Pass |
| 1.4.5 Images of text | Fail | Partial | Pass |
| 2.1 / 2.4 Keyboard, focus order, navigation | Deferred | Deferred | Deferred |
| 3.1.1 / 3.1.2 Language of page and of parts | Pass | Partial | Partial |
| 3.1.5 Reading level / plain language | Partial | Partial | Pass |
| 3.2.4 Consistent identification | Pass | Pass | Pass |
| 4.1.2 Name, role, value | Deferred | Deferred | Deferred |
| 1. Visibility of system status | Pass | Pass | Pass |
| 2. Match between system and the real world | Pass | Pass | Pass |
| 4. Consistency and standards | Pass | Pass | Pass |
| 5. Error prevention | Pass | Pass | Pass |
| 6. Recognition rather than recall | Partial | Pass | Partial |
| 8. Aesthetic and minimalist design | Partial | Pass | Pass |
| 10. Help and documentation | Partial | Pass | Partial |

## Findings, cell by cell

### 1.1.1 Text alternative for non-text content
*Perceivable*

- **clinician — Partial.** Every number is burned into the PNG and this is the only tier with no text sibling — tier_asha_*.txt and tier_mother_*_hi.txt exist, tier_clinician_*.txt does not; the nearest machine-readable form is shap_case_contributions.csv, which is data, not a caption.
- **ASHA — Pass.** `results/tables/tier_asha_<case>.txt` reproduces the card verbatim — band label and band name, the driver list (empty on a routine card, as on the PNG), next step, accountability line, disclaimer — so nothing on the PNG is image-only.
- **mother — Partial.** The spoken line has a deterministic transcript on disk (`tier_mother_<case>_hi.txt`), but render_mother() draws three ellipses and nothing else: no caption is rendered, so a deaf or hard-of-hearing viewer gets no text alternative in the artifact she is handed.

### 1.4.1 Use of colour (colour not the only cue)
*Perceivable*

- **clinician — Pass.** Bar direction plus a signed numeric label carries every SHAP sign without hue (BS +0.204, DiastolicBP -0.024 on boundary_mid); probability bars are labelled with class name and value, so the green/amber/red fill is redundant.
- **ASHA — Pass.** The header colour restates the header text, and the three-band unification kept it that way: the band word is printed under the label ('band: AMBER', 'band: RED'), so the amber and red states — which share the label 'ELEVATED — needs follow-up' — are still told apart in text. Removing all colour loses no information.
- **mother — Partial.** Hue is the primary cue. Two redundancies verified: lamp POSITION is fixed (red top / amber middle / green bottom) and lit-vs-unlit differs by 3.97:1 in luminance, so which lamp is lit survives colour-vision deficiency; the spoken Hindi line is a second non-colour channel. Residual gap: a viewer who is both colour-blind and deaf has position only, and position assumes the traffic-light convention.

### 1.4.3 Contrast (minimum)
*Perceivable*

- **clinician — Pass.** Text is matplotlib near-black on white; the smallest element, the 8pt italic disclaimer at #555, measures 7.46:1. Bar fills measure 3.91:1 and 3.45:1 against white, clearing the 3:1 non-text threshold (1.4.11).
- **ASHA — Pass.** Header ink is now chosen per band by render.text_on(), which compares both candidates against the band colour: near-black on amber 8.23:1, near-black on green 5.14:1, white on red 5.54:1. Worst case 5.14:1 clears the 4.5:1 normal-text minimum, not merely the 3:1 large-text one. Previously white was hardcoded and the amber header — the most common state — measured 2.12:1.
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
- **ASHA — Pass.** One band_for() call per case now drives the card header and the mother's lamp, so the two tiers cannot disagree: confident_high is RED in both, boundary_mid and failure_mode AMBER in both, confident_low GREEN in both. The card prints the band name, so the shared identity is legible and not merely chromatic.
- **mother — Pass.** Three bands mapped consistently to the shared palette; the same band always renders the same lamp and the same sentence (boundary_mid and failure_mode produce byte-identical Hindi text, as they should).

### 4.1.2 Name, role, value
*Robust*

- **clinician — Deferred.** PNG and MP3 carry no programmatic semantics; assistive-technology exposure is a property of the host app. Noted for deployment: this tier ships no accessible string, so an implementer has to author one.
- **ASHA — Deferred.** Same — but the .txt sibling hands a deployment a ready accessible name/value for the card.
- **mother — Deferred.** Same — the Hindi transcript is the ready accessible string; the lamp itself has no role or state exposed and would need one in an app.

### 1. Visibility of system status
*Nielsen*

- **clinician — Pass.** Shows true class, predicted class, all three probabilities to three decimals, the base value and f(x). On boundary_mid the reader sees 0.487 vs 0.499 and knows immediately that the call is a coin flip.
- **ASHA — Pass.** Since banding was unified, the card inherits the mother tier's uncertainty rule: confident_high (margin 1.000) prints 'band: RED' and boundary_mid (margin 0.012) prints 'band: AMBER', so the person making the referral can tell a confident call from a knife-edge one. The margin itself is still not printed — deliberately, since the card is the tier that must not turn into a probability read-out.
- **mother — Pass.** Status is exactly one lamp, and model uncertainty is what chooses it (see error prevention). By design the tier reports an action, not a state — which is the right 'status' for it.

### 2. Match between system and the real world
*Nielsen*

- **clinician — Pass.** Raw clinical units on the axis (BS = 9, BodyTemp = 102, SystolicBP = 85), not model-space values — the final model uses no scaler, so the waterfall reads in the clinician's own units.
- **ASHA — Pass.** Phrasing matches field speech, and a deadband of 0.25 IQR around the clean-set median now gates the direction word: a reading inside it is named plainly ('blood sugar'), only a reading outside it is called 'raised' or 'low'. BS 7.7 against a 7.5 median no longer reads as a concern; BS 9.0 on boundary_mid and 15.0 on confident_high still do. BodyTemp's IQR is 0 on the clean set, so 102F is flagged as raised, which is the right behaviour.
- **mother — Pass.** A traffic light is a near-universal metaphor, and the sentence names the real institutions in her world — her ANM, the nearest health centre — and opens by telling her not to panic, which is how the news would be delivered in person.

### 4. Consistency and standards
*Nielsen*

- **clinician — Pass.** Layout, palette and label conventions are identical across all four rendered cases; the figure is generated by one code path with no per-case special-casing.
- **ASHA — Pass.** The heading now follows the band rather than being fixed text: an elevated card reads 'What the model flagged for follow-up:' and lists drivers, while the routine card reads 'No specific risk factors flagged.' and lists none. The next step follows too — routine cards say continue antenatal care and share the readings at the next scheduled visit, not arrange a check-up. No sentence now means opposite things on different cards.
- **mother — Pass.** One image and one sentence per band, fixed; nothing varies between cases that share a band.

### 5. Error prevention
*Nielsen*

- **clinician — Pass.** The tier surfaces its own failure rather than hiding it: on failure_mode the waterfall shows BodyTemp +0.216 driving a high-risk call in a 13-year-old while blood sugar argues against it, and true vs predicted are both printed in the title. A reader can catch the spurious flag from the figure alone.
- **ASHA — Pass.** Strong on accountability — nothing is a diagnosis, the footer returns the referral decision to the human, the next step carries no medical timeframe — and the sign defect is closed: top_drivers() keeps only positive contributions to the predicted class and ranks by signed value. Verified on failure_mode, where BS (-0.085, arguing AGAINST high risk) is no longer listed despite its magnitude; the card now shows BodyTemp (+0.216) and Age (+0.056), the two features actually driving the call.
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
- **mother — Partial.** `tier_mother_<case>_hi.txt` now carries a provenance block — case, band and the full disclaimer — under a '(written, not spoken)' rule, so the artifact set is self-describing and a deployment inherits the text it must show. The gap that remains is real and deliberate: neither the image nor the audio carries it, so a mother handed lamp plus voice still has no route to help beyond 'go to the ANM'. A one-time spoken IVR framing at call setup is the deployment answer; appending it to every message was rejected as it would bury the one action the tier exists to deliver.

## Defects found and corrected

This evaluation was first run against the original P3 artifacts. These defects were found there, fixed in `src/render.py`, and the tiers re-rendered; every rating above describes the CORRECTED artifacts. Recorded so the finding survives its own repair.

**C1. ASHA driver list is now sign-aware**

- *Was:* top_drivers() ranked by |SHAP| with no sign filter, so a feature arguing AGAINST the prediction could be printed under 'What the model flagged for follow-up'. On failure_mode the card listed 'low blood sugar' whose contribution to the predicted class was -0.085 — it pushed away from high risk. The routine card was worse: confident_low listed the two features that were the reasons the model said LOW, under a heading announcing them as flags, above a next step telling the reader to arrange a check-up.
- *Now:* Only positive contributions to the predicted class are listed, ranked by signed value. A predicted-low card lists nothing and says so ('No specific risk factors flagged.'), and its next step is to continue routine antenatal care. failure_mode now shows BodyTemp (+0.216) and Age (+0.056); confident_low shows no drivers. This was the highest-priority gap — the only one that could put a wrong cue in front of the person making the referral.

**C2. One band across both tiers**

- *Was:* render_asha() banded binary (low vs not-low) while the mother tier banded three ways with the uncertainty rule, so confident_high rendered an AMBER card and a RED lamp — one prediction, two identities.
- *Now:* band_for() is computed once per case and passed to both tiers. The card prints the band name as text under the label, so amber and red — which share the label 'ELEVATED — needs follow-up' — stay distinguishable without colour.

**C3. Header ink is computed, not assumed**

- *Was:* White header text was hardcoded. On the ELEVATED amber it measured 2.12:1, under even the 3:1 large-text minimum, and amber is the header for two of the four rendered cases; the ROUTINE green managed only 3.38:1.
- *Now:* render.text_on() picks ink or paper per band by measured contrast. Worst case across the three bands is now 5.14:1, clearing the 4.5:1 normal-text threshold; a self-check asserts it, so re-tuning a band colour cannot silently reintroduce the defect.

**C4. Direction words have a deadband**

- *Was:* 'Raised' and 'low' were attached whenever the reading differed from the dataset median at all, so confident_low printed 'raised blood sugar' for BS = 7.7 against a median of 7.5 — a trivial deviation worded like a concern.
- *Now:* The word is attached only outside 0.25 IQR of the clean-set median; inside it the factor is named plainly ('blood sugar'). Still median-relative, not clinical — reference ranges would need clinical input this preprint deliberately does not claim.

**C5. Mother tier carries written provenance**

- *Was:* Neither the image, the audio, nor the transcript file said what the output was or that it is not a diagnosis, while both other tiers printed the disclaimer.
- *Now:* tier_mother_<case>_hi.txt now carries case, band and the full disclaimer under an explicit '(written, not spoken)' rule. The spoken line is unchanged: appending provenance to every message would bury the single action the tier exists to deliver, so a one-time spoken framing at IVR call setup is recorded as deployment work.

## Inherent limitations

What remains after those fixes. These are properties of the design rather than bugs in it — each is a deliberate trade-off, ranked by how much harm it can do to the person reading that tier.

**1. Mother visual has no rendered text alternative**

- *Evidence:* The traffic light is text-free by design (Decision Log #6), so a deaf or hard-of-hearing mother has no channel: the Hindi transcript exists only as a file on disk, not on the artifact.
- *Fix:* A rendered caption or an SMS companion carrying the same templated sentence. Future work — it reopens the literacy assumption the tier was built to avoid, so it needs user input, not a unilateral design call.

**2. The mother tier leans on colour**

- *Evidence:* Hue is the primary cue in the lamp. Position and the lit/unlit luminance step are real redundancies, and the spoken line is a second channel, but a viewer who is both colour-blind and deaf has position alone — and position assumes the traffic-light convention.
- *Fix:* Shape or iconography per band, tested with the intended users. Not a unilateral fix: it trades against the minimalism that makes the tier readable at all.

**3. The clinician tier assumes chart and English literacy**

- *Evidence:* 'SHAP waterfall', 'base E[f(x)] = 0.250' and an English title are correct for the stated reader and unreadable to anyone else; the tier carries no simpler supplement of its own.
- *Fix:* None within the tier — the supplement is the other two tiers, which is the architecture's point. Recorded so the scope is explicit rather than implied.

**4. Everything is an image of text**

- *Evidence:* All three tiers ship as rasterised PNG (WCAG 1.4.5); text cannot be resized or restyled. The ASHA and mother tiers have .txt siblings, the clinician tier has none.
- *Fix:* Emit a `tier_clinician_<case>.txt` alongside the figure; treat SVG or in-app rendering as the deployment answer.

**5. ASHA tier is English-only**

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

**The most useful result is what the first pass of this evaluation caught.** Run
against the original artifacts it returned four Fails, three of them in the ASHA
tier, and they shared one root: the template rendered |SHAP| magnitude while the
sentence around it asserted direction. A routine card announced the reasons the
model said LOW as things "flagged for follow-up" and told the reader to arrange a
check-up; a false-positive card listed a feature that argued against its own
prediction. Both are the kind of defect that reaches the person making a referral
and neither is visible from the model metrics — only from reading the artifact as
its user would. All four are now fixed in `src/render.py` and this document
re-rates the corrected outputs; the defects and their fixes are recorded above so
the finding is not lost by being repaired. The template approach was never the
problem — a deterministic template is auditable in exactly the way that let a
heuristic pass find these at all. It was under-specified, which is a fixable
defect and not an argument for a language model at inference.

6 of the 48 cells are Deferred, all of them operability and
robustness. That is not evasion, it is the honest boundary of a static-artifact
evaluation: keyboard access, focus order, IVR replay and timing, and
assistive-technology semantics are properties of a deployed application. They are
recorded as relevant-at-deployment so that a later study inherits the list rather
than rediscovering it.

---

Generated by `python -m src.evaluate`. Machine-readable form: `results/tables/heuristic_matrix.csv`.
