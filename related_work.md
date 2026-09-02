# related_work.md — Related Work foundation & novelty positioning

**Provenance:** Compiled from a structured literature sweep using the Consensus
academic search tool (8 searches across 5 sub-areas) plus OpenAlex verification,
2026-09. Every paper listed in §6 was **returned by a search tool in this
session** — none is from unverified recall.

**No-hallucination discipline (READ FIRST):**
- Do NOT invent DOIs, page numbers, or citation counts. The metadata in §6 is
  what the tools returned; treat it as a lead, not a final citation.
- Before the bibliography is frozen, **resolve every DOI via Crossref** and
  confirm author list, year, and venue. Only Mamun 2025 has a DOI confirmed here
  (via OpenAlex): `10.1002/eng2.70491`.
- The papers in §7 are **quarantined**: relevant but NOT verified in this sweep.
  Do not cite any of them until their DOI is resolved and the paper is read.

---

## 1. The one-sentence novelty claim (everything in Related Work serves this)

> When a model is uncertain, the *abstention decision itself* should be rendered
> differently across stakeholders **by vulnerability** — the least-powerful user
> receives a de-escalated signal, not a gentler copy of the same uncertainty.

This is the **only** claim that survives the literature. It is narrow, it is a
**design principle (not an evaluated result)**, and it must be positioned against
BOTH the stakeholder-XAI axis AND the uncertainty/abstention axis at once. State
it that way in the abstract and intro; do not claim "tiered explanations" or
"uncertainty-aware XAI" as novel — both are occupied (§2).

---

## 2. Novelty triangulation — the empty cell

Three mature literatures surround #7. It is novel ONLY at their intersection.

1. **Stakeholder-tailored XAI** renders the *explanation* per audience, but
   abstains for no one. (Kim 2023 already does clinician-vs-patient tailoring.)
2. **Uncertainty communication** conveys uncertainty per audience (Bhatt 2020),
   but as *display*, not as an alarm gate.
3. **Selective prediction / reject-option / learn-to-defer** gates on confidence
   and routes to a human — but **uniformly**, identically for everyone
   (Hendrickx 2021; Mozannar 2020). The 0.15-margin rule is a hand-set instance
   of this 50-year-old mechanism. **Do not claim the mechanism.**

**Empty cell:** a single uncertain prediction rendered as *graded, per-stakeholder
action-signals where the most vulnerable user gets the most conservative
rendering.* Abstention differentiated by stakeholder power. Unoccupied — claim
this, and only this.

---

## 3. Related Work section — draft from these stubs

Each stub = the papers to cite + the point to make + the concession to fold in.
Suggested order mirrors the paper's argument.

### 3.1 Stakeholder-tailored / audience-specific XAI  → "the concept is not ours"
Cite: Arya 2019 (AIX360, the canonical "one explanation does not fit all");
Kim 2023 (clinician-vs-patient interfaces — closest to two of our tiers);
Bello 2025 (a *three-level* technical→natural-language framework — our structural
twin, but LLM-mediated); Imrie 2023 (five interpretability types for healthcare
stakeholders).
Point: audience-specific explanation is a well-populated space; our contribution
is NOT that different users need different explanations.
**Concession (Suresh 2021):** Suresh et al. explicitly reject *role-based*
stakeholder categories, arguing knowledge must be decoupled from role. Our tiers
are named by role. Concede this openly, then argue role is a defensible **proxy**
in *this* deployment: here role tightly tracks literacy, modality, and power (the
ASHA is the Class-8-educated worker; the mother may not read at all). Szymanski
2025 can support that role/expertise often co-vary in practice.
Contrast to bake in: Bello 2025 uses an LLM as the mediator; we use **deterministic
templates over SHAP** — auditable, reproducible, no hallucination at inference.
That contrast is one of our listed contributions.

### 3.2 Uncertainty communication & selective prediction  → "the mechanism is not ours; the *targeting* is"
Cite: Bhatt 2020 (uncertainty as transparency, communicated to stakeholders — our
nearest ancestor); Kompa 2021 (medical-ML abstention as a safety feature);
Hendrickx 2021 (reject-option survey — defines our AMBER-on-near-tie as "ambiguity
rejection"); Mozannar 2020 (learning to defer to a human expert).
Point: gating on confidence and routing to a human is established. Our delta is
that the gate's *output is rendered differently by stakeholder vulnerability* —
the mother gets a de-escalated non-alarm, the clinician gets the full uncertainty.
This section is where the novelty lives; give it real space. (Code's first pass
essentially skipped this axis — do not.)

### 3.3 XAI for community health workers in the Global South  → "the context, and the honest 'no users' gap"
Cite: Okolo 2022 (systematic review — only 1 of 16 Global-South XAI papers ever
deployed with users; this is the gap we sit in); Okolo 2021 & 2024, Solano-Kamaiko
2024 (design probes with real CHWs); Srinidhi 2021 (ASHA Kirana — a real
deployment where ASHAs collect data → algorithm → report for doctors; our data
flow, minus tiering/gating).
**Concession (comprehensibility is unproven):** Okolo 2024 and Solano-Kamaiko 2024
found CHWs *struggled to understand AI explanations even when simplified.* So our
ASHA card's comprehensibility is an **open empirical question**, not an assumption.
Cite this as precisely *why* a user study is the stated next step.
**Concession (no users):** every paper here has real users; we have none. State it
plainly; frame ours as a design/feasibility artifact that these user-grounded works
motivate.

### 3.4 Risk communication to low-literacy / low-numeracy patients  → "why no number is a principled choice"
Cite: Galesic 2009 (icon arrays for low numeracy); García-Retamero & Cokely 2017
(systematic review + design heuristics; visual aids especially help vulnerable
users); Richter 2023 (verbal-only risk communication should be avoided);
Peters 2025 (best practices); Bradley 2025 (maternity-specific risk graphics).
**Tension to resolve (do not ignore):** this literature generally favors
*transparent visual aids that convey magnitude* (icon arrays). Our mother tier
strips magnitude to an ordinal color band. Resolve it, don't dodge it: those
recommendations presuppose a *trustworthy* magnitude; under model uncertainty
(our thesis), an icon array would convey **false precision**. So "uncertainty-gated
ordinal band + action, not a number" is a principled departure justified *by* this
literature, not an omission that ignores it. This actually strengthens §3.2.

### 3.5 ML + SHAP on the UCI Maternal Health Risk dataset  → "the model is a vehicle (and the field forces that)"
Cite: Mamun 2025, Maisoon 2026, Widyawati 2025, Rahman 2023, Maheswari 2024,
Hossen 2024.
Point: ML+SHAP on this exact dataset is saturated — so "the model is a vehicle" is
not a modest framing choice, it is **forced by the field**; there is no ML novelty
to claim and we do not claim any.
**Distinguish Maisoon 2026 explicitly** — it is our closest methodological neighbor
(same dataset, same 2-outlier removal 1014→1012, RF+XGBoost+SMOTE, stratified
5-fold CV, SHAP, low-resource framing, same top features BS/BP). Our differentiators:
deduplication, the three-tier rendering, uncertainty gating, and the voice-first
mother tier. Note the corroboration: Maisoon's and Widyawati's SHAP also rank blood
sugar + systolic BP on top — consistent with our finding.

---

## 4. Required concessions (fold into prose; a reviewer will raise each)

1. **Role-based tiers vs. Suresh 2021** — concede; argue role-as-proxy for
   literacy/modality/power in this deployment. (§3.1)
2. **ASHA comprehensibility is unproven** — Okolo 2024 / Solano-Kamaiko 2024 found
   CHWs struggle; our card is a design proposal, not a validated interface. (§3.3)
3. **No users** — the whole system is pre-user-study; the evaluation is formative
   heuristic self-critique, not validation. (§3.3 + Evaluation section)
4. **Mother tier omits magnitude** against risk-comm norms — justify via
   uncertainty (false precision). (§3.4)
5. **Maisoon 2026 is a near-identical pipeline** — distinguish carefully. (§3.5)
6. **Dataset ≠ preeclampsia** — HOLD THE LINE: stay in generic "maternal-health
   risk" language throughout; the dataset has no preeclampsia labels or markers,
   and the top driver is glycemic. Do not let COG1's preeclampsia framing survive.

---

## 5. The leakage audit — belongs in Data/Methods, NOT Related Work

Frame (honest bound): we did **not** discover leakage as a concept, nor that
duplicates inflate performance. We **quantify** it for this specific popular
benchmark. Claim the quantification, not the discovery.

- Concept anchor: **Kapoor & Narayanan 2023** (Patterns, 897 cites) — leakage
  taxonomy / reproducibility crisis.
- Direct mechanism: **Rosenblatt 2024** (Nature Communications) — "leakage via
  repeated subjects drastically inflates performance," worsened on **small
  datasets.** This is exactly our case (duplicate rows, small n).
- Precedent for the contribution *type* (re-analyze an inflated published result →
  true number): **Eltawil 2026** (99%→~80% after fixing pre-split resampling);
  **Young 2025** (94%→66% under proper validation in Alzheimer's DL).
- Exhibit A on THIS dataset: **Mamun 2025** reports **99.51%** accuracy, 10-fold
  CV, no deduplication. Our two-row table (dups-kept 0.859 vs deduped 0.580)
  reproduces the inflated band and then removes it.
- No prior paper documenting the 562 duplicates was found in this sweep — so the
  quantification claim is safe. (Re-check Kaggle discussions before final claim;
  Kaggle is not indexed as literature and was not retrievable here.)

Suggested wording: *"Consistent with known duplicate-driven leakage [Kapoor 2023;
Rosenblatt 2024], we find the published 83–99% accuracy band on this dataset
[Mamun 2025; Maisoon 2026] is recoverable only when 562 exact-duplicate rows are
allowed to straddle the train/test split; after deduplication, macro-recall is
0.580."*

---

## 6. Bibliography (verified in-session; RESOLVE DOIs before freezing)

Format per entry: Author(s) (Year). Title. Venue. [cites at sweep time] — Consensus
lookup URL. DOIs are NOT included unless confirmed; resolve via Crossref.

### Stakeholder-tailored XAI
- Kim, M. et al. (2023). Do stakeholder needs differ? — Designing stakeholder-tailored Explainable AI interfaces. *Int. J. Human-Computer Studies.* [61] — https://consensus.app/papers/details/aeab3adcd4605953bc6c0eb367adc305/
- Arya, V. et al. (2019). One Explanation Does Not Fit All: A Toolkit and Taxonomy of AI Explainability Techniques (AIX360). *arXiv.* [479] — https://consensus.app/papers/details/99491c79aa685082ad1edfa1ac8231fd/
- Bello, M. et al. (2025). A Three-level Framework for LLM-enhanced Explainable AI: From Technical Explanations to Natural Language. *Information Systems Frontiers.* [7] — https://consensus.app/papers/details/4420d4b1e2155a8db329dbb09df59f3c/
- Imrie, F. et al. (2023). Multiple stakeholders drive diverse interpretability requirements for machine learning in healthcare. *Nature Machine Intelligence.* [45] — https://consensus.app/papers/details/11b0b6c05ee25435a8de32a9465086de/
- Suresh, H. et al. (2021). Beyond Expertise and Roles: A Framework to Characterize the Stakeholders of Interpretable ML and their Needs. *CHI 2021.* [161] — https://consensus.app/papers/details/036fc6536b9857e38152277317d770e6/
- Szymanski, M. et al. (2025). Disentangling Stakeholder Role and Expertise in User-Centered Explainable AI. *ACM UMAP 2025.* [1] — https://consensus.app/papers/details/20cd5b547ceb5b63be3f8400d23a9365/

### Uncertainty communication & selective prediction / abstention
- Bhatt, U. et al. (2020/2021). Uncertainty as a Form of Transparency: Measuring, Communicating, and Using Uncertainty. *AAAI/ACM AIES.* [340] — https://consensus.app/papers/details/f9bcee3b42f852649d0cf8d7eebed2b3/
- Kompa, B. et al. (2021). Second opinion needed: communicating uncertainty in medical machine learning. *NPJ Digital Medicine.* [510] — https://consensus.app/papers/details/ff2180d83cab53458afcfa594ffc8350/
- Hendrickx, K. et al. (2021). Machine learning with a reject option: a survey. *Machine Learning.* [213] — https://consensus.app/papers/details/c23973398705566ca53070e49a668d99/
- Mozannar, H. & Sontag, D. (2020). Consistent Estimators for Learning to Defer to an Expert. *ICML 2020.* [333] — https://consensus.app/papers/details/e74bbf297fe25ec3a701e6d04d3a64ba/
- Franc, V. et al. (2021). Optimal strategies for reject option classifiers. *JMLR.* [85] — https://consensus.app/papers/details/7f57ff3a604858b58b4ea0c41d80de7c/  *(optional depth)*

### XAI for community health workers, Global South
- Okolo, C. T. et al. (2021). "It cannot do all of my work": CHW Perceptions of AI-Enabled Mobile Health Applications in Rural India. *CHI 2021.* [90] — https://consensus.app/papers/details/c1b306c9d48f57f096d4746e4ac65df6/
- Okolo, C. T. et al. (2022). Making AI Explainable in the Global South: A Systematic Review. *ACM COMPASS 2022.* [56] — https://consensus.app/papers/details/4739c2ed9d275bd795903a1a921cebd1/
- Okolo, C. T. et al. (2024). "If it is easy to understand then it will have value": Perceptions of Explainable AI with CHWs in Rural India. *PACMHCI (CSCW).* [20] — https://consensus.app/papers/details/e8a8e8d21c245b3d8a373f20de19920b/
- Solano-Kamaiko, I. et al. (2024). Explorable Explainable AI: Improving AI Understanding for CHWs in India. *CHI 2024.* [23] — https://consensus.app/papers/details/618b422b155f588b92434591e246ef58/
- Srinidhi, V. et al. (2021). ASHA Kirana: when digital technology empowered front-line health workers. *BMJ Global Health.* [23] — https://consensus.app/papers/details/c3089a5543de5c4bacb67420226dcd37/

### Risk communication to low-literacy / low-numeracy patients
- Galesic, M. et al. (2009). Using icon arrays to communicate medical risks: overcoming low numeracy. *Health Psychology.* [399] — https://consensus.app/papers/details/acb9d4206aaf58e1abbc7c84690490cf/
- García-Retamero, R. & Cokely, E. T. (2017). Designing Visual Aids That Promote Risk Literacy: A Systematic Review... *Human Factors.* [292] — https://consensus.app/papers/details/d53f531eb20950a0a45f60f991256da5/
- Richter, R. et al. (2023). Communication of benefits and harms in shared decision making with patients with limited health literacy: A systematic review. *Patient Education and Counseling.* [42] — https://consensus.app/papers/details/7ef9086c035c5ee891f35e09f37b13bb/
- Peters, E. et al. (2025). Communicating Numeric Risk Information to Patients. *J. General Internal Medicine.* [2] — https://consensus.app/papers/details/576fb68a4c065d2582c97f7fa43aa575/
- Bradley, V. et al. (2025). How Should We Communicate Information Regarding Birth Choices to Women? An Online Randomised Survey. *BJOG.* [6] — https://consensus.app/papers/details/12debfe153dc582989fa19509b666444/

### ML + SHAP on the UCI Maternal Health Risk dataset
- Mamun, M. S. I. et al. (2025). Identification of Maternal Health Risk From Optimal Features Using Explainable ML. *Engineering Reports.* [3] — **DOI 10.1002/eng2.70491 (CONFIRMED, open access)** — 99.51% acc, 10-fold CV, no dedup.
- Maisoon, M. et al. (2026). Maternal Health Risk Stratification in Low-Resource Settings: Comparative Analysis of ML Models With XAI. *IEEE Access.* [0] — https://consensus.app/papers/details/9915742450045e358cb311676679ee53/ — closest neighbor; 83.74%, keeps dups.
- Widyawati, L. et al. (2025). Explainable Ensemble Learning for Maternal Health Risk in Low-Resource Settings. *Jurnal RESTI.* [0] — https://consensus.app/papers/details/f9875577de855e8e974ef085a3625457/
- Rahman, A. et al. (2023). Explainable AI based Maternal Health Risk Prediction using ML and DL. *IEEE World AI IoT Congress.* [16] — https://consensus.app/papers/details/c002fe2c51d25623bf92bb9058be60fe/
- Maheswari, B. et al. (2024). ML Algorithm for Maternal Health Risk Classification with SMOTE and Explainable AI. *IEEE I2CT.* [9] — https://consensus.app/papers/details/437367c0c117527d8888f361261da587/
- Hossen, M. S. et al. (2024). An Explainable AI Driven ML Approach for Maternal Health Risk Analysis. *ICCIT 2024.* [10] — https://consensus.app/papers/details/a8e1c1c5c6ea5f2a9573a0622de3c7ed/

### Data leakage / reproducibility (Data-Methods section)
- Kapoor, S. & Narayanan, A. (2023). Leakage and the reproducibility crisis in machine-learning-based science. *Patterns.* [897] — https://consensus.app/papers/details/f7b850c06abb58db8d431f9ce35d007c/
- Rosenblatt, M. et al. (2024). Data leakage inflates prediction performance in connectome-based ML models. *Nature Communications.* [173] — https://consensus.app/papers/details/9a2618e1a1e95fc988d197c0fce39246/
- Bernett, J. et al. (2024). Guiding questions to avoid data leakage in biological ML applications. *Nature Methods.* [115] — https://consensus.app/papers/details/88497b0f96275933a175ff7991957049/
- Eltawil, M. et al. (2026). Comment on Iacobescu et al. (re-analysis showing pre-split-resampling leakage). *J. Cardiovasc. Dev. Dis.* [3] — https://consensus.app/papers/details/e5872011f51c567cb8fb1206c35c456c/
- Young, V. et al. (2025). Data Leakage in Deep Learning for Alzheimer's Disease Diagnosis: A Scoping Review. *Diagnostics.* [17] — https://consensus.app/papers/details/17659bb8822259eeb8539cbfa003c0c6/

---

## 7. QUARANTINE — relevant but NOT verified in this sweep (do NOT cite until checked)

- **Liao, Q. V. et al. (2020). "Questioning the AI: Informing Design Practices for
  Explainable AI User Experiences." CHI 2020.** Real and highly relevant to §3.1,
  but did NOT surface in this session's Consensus searches. Resolve DOI + read
  before citing.
- **Clark et al. (2022, BJGP). NICE traffic-light system missing seriously ill
  children.** Code's counter-citation for the mother tier; useful ("shows a
  traffic-light gate can fail"), but I did not independently verify it. Confirm DOI
  before use. (The §3.4 risk-comm cluster is stronger anyway.)
- **Kilkari / mMitra / ARMMAN voice-mHealth citations** — carried over from the
  COG1 report (verified there, not re-verified here). Fine to reuse; re-confirm the
  exact references from the COG1 bibliography.
- Any citation not appearing in §6 or resolved from §7 must NOT enter the
  manuscript. This is the anti-hallucination gate.

---

## 8. What is genuinely ours (the honest contribution stack)

1. **(Headline)** Vulnerability-differentiated abstention: rendering an uncertain
   prediction as graded per-stakeholder signals, most-conservative for the
   least-powerful. The empty cell at the intersection of §3.1–§3.2.
2. **(Contribution)** Deterministic, auditable templating over SHAP as an explicit
   alternative to LLM-mediated tiering (foil: Bello 2025).
3. **(Contribution)** A quantified leakage audit of a widely-used benchmark
   (§5), in the Eltawil/Young mold.

This is a design-and-feasibility preprint, pre-user-study, positioned honestly
against a field that has users. That honesty is the paper's strength — lean into
it, don't paper over it.
