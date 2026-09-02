# Related work — two-axis review for P5

_Compiled 2026-09-03. Every entry below was retrieved in-session and its DOI
verified against the Crossref API (`api.crossref.org/works/<doi>`), except
where explicitly marked UNVERIFIED. Nothing here is cited from memory._

**Tooling note.** The `literature-review` skill mandates the Consensus search
tool, which was not available in this session (no Consensus MCP server is
configured; the two configured servers, `firecrawl` and `agents-observe`,
both failed to connect at startup). The review was run instead over web search
with per-citation DOI verification through Crossref. That satisfies the
no-hallucinated-references constraint directly, but it is **not** a systematic
Consensus sweep: coverage is narrower and citation counts were not collected.
Treat this as a positioning document, not an exhaustive survey. Re-run through
Consensus before submission if the tool becomes available.

---

## 1. The headline claim, and what actually threatens it

Our thesis (Decision Log #7): *a knife-edge prediction must not reach the
least-powerful stakeholder as an alarm*, implemented as a top-2 probability
margin gate that down-ranks RED to AMBER below 0.15.

The literature splits cleanly into two mature axes that, as far as this review
found, **have not been joined**:

- **Axis 1** knows that different stakeholders need different explanations, and
  has taxonomised that thoroughly — but treats confidence as one more thing to
  *display*, not as a gate on *what the explanation is allowed to say*.
- **Axis 2** knows how to abstain, calibrate, and defer on low-confidence
  predictions — but the abstention decision is uniform across audiences. The
  model abstains, or it does not; who is downstream does not change the rule.

The gap our claim occupies: **abstention/derating as a per-audience rendering
decision rather than a global model decision.** The clinician still sees the
0.487/0.499 split in full; only the mother's channel is derated. Nothing found
in this review does that.

### The real threat is not Axis 1 in general — it is two specific papers

Two recent papers do XAI for community health workers in India, which is our
exact deployment framing:

- **Okolo, Agarwal, Dell & Vashistha (CSCW 2024)** — semi-structured interviews
  with CHWs interacting with a design probe that predicts **neonatal jaundice**
  with accompanying explanations. Same country, same worker cadre, adjacent
  clinical domain, and it studies how CHWs actually interpret explanations.
- **Solano-Kamaiko, Mishra, Dell & Vashistha (CHI 2024)** — "Explorable
  Explainable AI," improving AI understanding for CHWs in India.

**These must be cited and explicitly distinguished, in Related Work, not in a
footnote.** A reviewer who knows this space will look for them first, and their
absence would read as not knowing the field. The honest distinction:

| | Okolo 2024 / Solano-Kamaiko 2024 | This work |
|---|---|---|
| Audience | CHW only (single tier) | Three tiers from one prediction |
| Method | Empirical, with real CHWs | Design artifact + heuristic evaluation, no users |
| Contribution | How CHWs perceive explanations | A rule for what each tier is *permitted* to assert |
| Uncertainty | Not the object of study | The object of study |

Note the asymmetry honestly: **they have users and we do not.** Our
compensating claim is architectural, not empirical — we are not claiming to
know better what CHWs want, we are proposing a rendering rule and evaluating
the artifact. Say that in as many words; do not imply parity of evidence.

Okolo (AIES 2023), "Navigating the Limits of AI Explainability: Designing for
Novice Technology Users in Low-Resource Settings," is the position-paper
companion and is the cleanest single citation for *why* low-resource
explainability needs its own treatment.

---

## 2. Axis 1 — stakeholder-relative / audience-specific XAI

**What the field establishes.** That explanation needs are stakeholder-relative
is settled, not novel, and our Intro must not claim it. Arya et al. named it in
the title — *One Explanation Does Not Fit All* — in 2019. Suresh et al. then
made the strongest version of the argument, deliberately moving *beyond* role
labels ("clinician", "patient") to decouple a stakeholder's knowledge from
their interpretability needs, and distilling a hierarchical typology that
separates high-level domain goals from low-level interpretability tasks.

**Consequence for our framing, and it is sharp.** Our three tiers are named by
*role* — clinician / ASHA / mother. Suresh et al. is a direct argument that
role is the wrong axis. Two defensible responses, and the paper must pick one:

1. Concede the point and re-ground the tiers in what each reader *lacks* —
   which is what Decision Log #17 already does (modality, literacy,
   decision authority), with the role names kept only as shorthand. **Recommended.**
2. Argue that in this deployment the roles are tightly bound to the knowledge
   profiles, so role is a serviceable proxy. Weaker, and invites the reviewer
   to do the decoupling for you.

Liao, Gruen & Miller supply the practitioner-facing complement: an
algorithm-informed XAI question bank, built from interviews with 20 UX and
design practitioners, framing user needs as prototypical questions a user might
ask. Useful for us as the source of the "what question is this tier answering?"
move — our mother tier answers *what do I do next*, deliberately not *how
likely is X* (Decision Log #6).

Mohseni, Zarei & Ragan is the evaluation-side anchor and the best citation for
positioning our P4: a multidisciplinary framework for XAI design **and
evaluation**, which is where a formative heuristic evaluation with no users
sits legitimately in the design cycle.

| Paper | Venue / year | DOI (verified) | Why it matters here |
|---|---|---|---|
| Arya et al., *One Explanation Does Not Fit All: A Toolkit and Taxonomy of AI Explainability Techniques* | arXiv 2019 (AIX360) | arXiv:1909.03012 (no Crossref DOI) | Earliest crisp statement that audiences differ; names the exact premise we build on |
| Suresh, Gomez, Nam & Satyanarayan, *Beyond Expertise and Roles* | CHI 2021 | 10.1145/3411764.3445088 | The strongest challenge to role-based tiering — engage it directly |
| Liao, Gruen & Miller, *Questioning the AI* | CHI 2020 | 10.1145/3313831.3376590 | Question-driven framing of explanation needs |
| Mohseni, Zarei & Ragan, *A Multidisciplinary Survey and Framework for Design and Evaluation of Explainable AI Systems* | ACM TiiS 11, 2021 | 10.1145/3387166 | Legitimises formative, non-user evaluation; anchors P4 |
| Okolo, Agarwal, Dell & Vashistha, *"If it is easy to understand then it will have value"* | PACM HCI 8 (CSCW1), 2024 | 10.1145/3637348 | Closest prior work — CHWs in rural India, XAI design probe |
| Solano-Kamaiko, Mishra, Dell & Vashistha, *Explorable Explainable AI* | CHI 2024 | 10.1145/3613904.3642733 | Closest prior work — CHW AI understanding in India |
| Okolo, *Navigating the Limits of AI Explainability* | AIES 2023 | 10.1145/3600211.3604759 | Position piece on low-resource explainability |

---

## 3. Axis 2 — uncertainty communication, selective prediction, calibration

**What the field establishes.** Abstention has a long formal lineage: the
error–reject trade-off dates to Chow in the 1970s, with modern treatments
including Geifman & El-Yaniv's risk–coverage framework and SelectiveNet, which
learns classification and rejection jointly rather than thresholding a
pre-trained model's softmax. Guo et al. established that modern networks are
badly calibrated and that temperature scaling largely fixes it — the reason any
margin-based rule has to state whether its probabilities are calibrated.

**The two papers that matter most to our thesis:**

- **Bhatt et al. (AIES 2021), *Uncertainty as a Form of Transparency*.** The
  closest thing to a direct ancestor of Decision Log #7. It argues uncertainty
  is itself a form of transparency, and — critically for us — *outlines methods
  for displaying uncertainty to stakeholders*, drawing across ML, visualisation/
  HCI, design, decision-making and fairness. This is the paper our claim must
  be positioned against most carefully. Our delta: Bhatt et al. treat display
  as audience-aware; we treat **suppression** as audience-aware. Uncertainty in
  our design does not get shown to the mother in a gentler format — it changes
  the assertion she receives at all.
- **Kompa, Snoek & Beam (npj Digital Medicine 2021), *Second opinion needed*.**
  Uncertainty quantification and **abstention** specifically in medical ML;
  models should abstain on high-uncertainty samples for safety. This is our
  bridge from a generic ML mechanism to the clinical-safety argument, and it is
  the citation that makes "derate the alarm" a safety move rather than a UX
  preference.

**Zhang, Liao & Bellamy (FAT\* 2020)** is the empirical cautionary note and
belongs in Limitations as much as Related Work: showing confidence alongside
explanations affects trust calibration in AI-assisted decisions, and the effect
is not uniformly positive. Our margin gate is an untested intervention of
exactly this type — we should cite this as the study design our future work
owes.

| Paper | Venue / year | DOI / ID | Role |
|---|---|---|---|
| Bhatt et al., *Uncertainty as a Form of Transparency* | AIES 2021 | 10.1145/3461702.3462571 (verified) | Nearest ancestor; distinguish display vs. suppression |
| Kompa, Snoek & Beam, *Second opinion needed* | npj Digital Medicine, 2021 | 10.1038/s41746-020-00367-3 (verified) | Abstention as clinical safety |
| Zhang, Liao & Bellamy, *Effect of confidence and explanation on accuracy and trust calibration* | FAT\* 2020 | 10.1145/3351095.3372852 (verified) | Confidence display is not automatically good; our future-work design |
| Guo, Pleiss, Sun & Weinberger, *On Calibration of Modern Neural Networks* | ICML 2017 | arXiv:1706.04599; PMLR v70 | Forces us to state our calibration position |
| Geifman & El-Yaniv, *SelectiveNet* | ICML 2019 | arXiv:1901.09192; PMLR v97 | Selective prediction as a learned objective |

> **Open item.** Chow's error–reject trade-off was described in returned
> summaries but no primary record was retrieved and no DOI verified. Do not
> cite it until the primary reference is pulled.

---

## 4. Health-communication thread — risk conveyance without literacy

This axis supplies our mother tier's evidence base and, usefully, its
strongest counter-evidence.

**Supporting.** Icon arrays and pictographs measurably help low-numeracy
readers: Garcia-Retamero, Galesic & Gigerenzer show icon arrays reduce
denominator neglect, and the benefit is repeatedly reported as largest among
exactly the lower-numeracy readers our tier targets. Colour-coded front-of-pack
labelling has a systematic review and network meta-analysis behind it (Song et
al., PLOS Medicine 2021), which is the strongest available evidence that a
green/amber/red encoding is comprehensible at population scale.

**Counter-evidence, and we should cite it against ourselves.** Clark et al.
(BJGP 2022) found the **NICE traffic light system did not accurately detect
children admitted with serious illness** and concluded it is not suitable as a
clinical tool in general practice. A traffic light is comprehensible; that is
not the same as it being safe. Citing this is the honest move and it
strengthens rather than weakens our position, because our design does not use
the lamp as a clinical instrument — Decision Log #6 caps the tier at an
*action*, and Decision Log #7 derates it under uncertainty precisely because a
three-state colour code compresses away the information a borderline case needs.
That is the argument, and Clark et al. is the evidence that the argument is
necessary.

| Paper | Venue / year | DOI (verified) | Role |
|---|---|---|---|
| Garcia-Retamero, Galesic & Gigerenzer, *Do Icon Arrays Help Reduce Denominator Neglect?* | Medical Decision Making 30(6), 2010 | 10.1177/0272989X10369000 | Visual risk aids help low-numeracy readers |
| Song et al., *Impact of color-coded and warning nutrition labelling schemes* | PLOS Medicine, 2021 | 10.1371/journal.pmed.1003765 | Systematic review + NMA of traffic-light colour coding |
| Clark, Cannings-John, Blyth, Hay, Butler & Hughes, *Accuracy of the NICE traffic light system in children presenting to general practice* | BJGP 72(719), 2022 | 10.3399/bjgp.2021.0633 | Traffic lights can be comprehensible and still unsafe — cite against ourselves |

> Zikmund-Fisher et al. ("Blocks, Ovals, or People?", Medical Decision Making
> 2014) and Galesic & Garcia-Retamero on graph literacy appeared in results but
> their DOIs were not verified in-session. Verify before citing.

---

## 5. The duplicate-row / leakage claim — verdict: downgrade the wording

**Searched for:** published documentation of exact-duplicate rows in UCI
Maternal Health Risk (id=863), deduplication in prior preprocessing, and any
report of ~451/452 unique rows.

**Found:** nothing. Papers using this dataset consistently report **n = 1014**
and describe preprocessing as normalisation and "removal of inconsistencies",
with no duplicate handling stated. The UCI dataset page itself carries no
data-quality note — it states only that there are no missing values.

**Not established:** absence of evidence here is weak evidence. Kaggle notebook
pages were not retrievable in-session, and Kaggle-level awareness of a
`drop_duplicates()` result is entirely plausible and would not be indexed as
literature. One directly relevant paper — **Mamun et al., "Identification of
Maternal Health Risk From Optimal Features Using Explainable Machine Learning,"
Engineering Reports, 2025, 10.1002/eng2.70491** — uses this dataset *with SHAP*
and is therefore both a novelty check for Axis 1 and a leakage check. **Its
full text was paywalled (HTTP 403) and its preprocessing is UNVERIFIED. Pull
this paper before submission; it is the single highest-value open item in this
review.**

**Recommended wording, and it is deliberately weaker than what you can prove
about your own numbers:**

> We do not claim to be the first to notice these duplicates. We report what
> they cost: scoring the identical model and identical cross-validation with
> duplicates retained moves macro-recall from 0.580 to 0.859 and accuracy from
> 0.641 to 0.854, placing it inside the 83–88% band reported in prior work on
> this dataset. We therefore report deduplicated figures and state the
> comparison explicitly, so our lower headline is legible as hygiene rather
> than as a weaker model.

Claim *quantification*, not *discovery*. It is unfalsifiable-adjacent to claim
you were first; the measurement is yours regardless, it is reproducible from
`results/tables/p1_duplicate_leakage.csv`, and it survives a reviewer who
replies "everyone knows about those duplicates" — which, on this evidence, some
of them may.

---

## 6. Gaps this review exposes in our own paper

1. **Role-based tiering is directly challenged by Suresh et al.** Re-ground the
   tiers in modality/literacy/authority (Decision Log #17 already does this) and
   say so explicitly, or a reviewer will make the point for us.
2. **Two CHW-in-India XAI papers must be cited and distinguished** (Okolo CSCW
   2024, Solano-Kamaiko CHI 2024). They have users; we do not. State the
   asymmetry rather than let it be discovered.
3. **The 0.15 margin threshold has no empirical basis and now has a literature
   that would expect one.** Zhang, Liao & Bellamy is the shape of the study that
   would justify it. Keep it a declared design choice; name the study we owe.
4. **Calibration is unaddressed.** Our gate thresholds a *margin between random
   forest class probabilities*. Guo et al. makes "are these probabilities
   calibrated?" a foreseeable reviewer question. One sentence, honestly: RF
   probabilities are uncalibrated votes, the threshold is a design constant not
   a probability statement, and calibration is future work.
5. **Cite the counter-evidence on traffic lights** (Clark et al.). It makes the
   uncertainty gate look necessary rather than decorative.
6. **Pull Mamun et al. 2025** — the one paper that could change both the
   novelty framing and the leakage claim.

---

## Bibliography (alphabetical; DOIs verified via Crossref unless marked)

- Arya, V. et al. (2019). *One Explanation Does Not Fit All: A Toolkit and Taxonomy of AI Explainability Techniques.* arXiv:1909.03012. https://arxiv.org/abs/1909.03012 — arXiv ID only, no Crossref DOI
- Bhatt, U., Antorán, J., Zhang, Y., Liao, Q. V., Sattigeri, P., Fogliato, R., Melançon, G., Krishnan, R., Stanley, J., Tickoo, O., Nachman, L., Chunara, R., Srikumar, M., Weller, A. & Xiang, A. (2021). *Uncertainty as a Form of Transparency: Measuring, Communicating, and Using Uncertainty.* AIES 2021. https://doi.org/10.1145/3461702.3462571
- Clark, A., Cannings-John, R., Blyth, M., Hay, A. D., Butler, C. C. & Hughes, K. (2022). *Accuracy of the NICE traffic light system in children presenting to general practice: a retrospective cohort study.* British Journal of General Practice 72(719). https://doi.org/10.3399/bjgp.2021.0633
- Garcia-Retamero, R., Galesic, M. & Gigerenzer, G. (2010). *Do Icon Arrays Help Reduce Denominator Neglect?* Medical Decision Making 30(6). https://doi.org/10.1177/0272989X10369000
- Geifman, Y. & El-Yaniv, R. (2019). *SelectiveNet: A Deep Neural Network with an Integrated Reject Option.* ICML 2019. arXiv:1901.09192 — arXiv/PMLR only
- Guo, C., Pleiss, G., Sun, Y. & Weinberger, K. Q. (2017). *On Calibration of Modern Neural Networks.* ICML 2017. arXiv:1706.04599 — arXiv/PMLR only
- Kompa, B., Snoek, J. & Beam, A. L. (2021). *Second opinion needed: communicating uncertainty in medical machine learning.* npj Digital Medicine. https://doi.org/10.1038/s41746-020-00367-3
- Liao, Q. V., Gruen, D. & Miller, S. (2020). *Questioning the AI: Informing Design Practices for Explainable AI User Experiences.* CHI 2020. https://doi.org/10.1145/3313831.3376590
- Mamun et al. (2025). *Identification of Maternal Health Risk From Optimal Features Using Explainable Machine Learning.* Engineering Reports. https://doi.org/10.1002/eng2.70491 — **UNVERIFIED: paywalled, author list and preprocessing not confirmed**
- Mohseni, S., Zarei, N. & Ragan, E. D. (2021). *A Multidisciplinary Survey and Framework for Design and Evaluation of Explainable AI Systems.* ACM TiiS 11. https://doi.org/10.1145/3387166
- Okolo, C. T. (2023). *Navigating the Limits of AI Explainability: Designing for Novice Technology Users in Low-Resource Settings.* AIES 2023. https://doi.org/10.1145/3600211.3604759
- Okolo, C. T., Agarwal, D., Dell, N. & Vashistha, A. (2024). *"If it is easy to understand then it will have value": Examining Perceptions of Explainable AI with Community Health Workers in Rural India.* PACM HCI 8 (CSCW1). https://doi.org/10.1145/3637348
- Solano-Kamaiko, I. R., Mishra, D., Dell, N. & Vashistha, A. (2024). *Explorable Explainable AI: Improving AI Understanding for Community Health Workers in India.* CHI 2024. https://doi.org/10.1145/3613904.3642733
- Song, J., Brown, M. K., Tan, M., MacGregor, G. A., Webster, J., Campbell, N. R. C., Trieu, K., Ni Mhurchu, C., Cobb, L. K. & He, F. J. (2021). *Impact of color-coded and warning nutrition labelling schemes: A systematic review and network meta-analysis.* PLOS Medicine. https://doi.org/10.1371/journal.pmed.1003765
- Suresh, H., Gomez, S. R., Nam, K. K. & Satyanarayan, A. (2021). *Beyond Expertise and Roles: A Framework to Characterize the Stakeholders of Interpretable Machine Learning and their Needs.* CHI 2021. https://doi.org/10.1145/3411764.3445088
- Zhang, Y., Liao, Q. V. & Bellamy, R. K. E. (2020). *Effect of confidence and explanation on accuracy and trust calibration in AI-assisted decision making.* FAT\* 2020. https://doi.org/10.1145/3351095.3372852
