# Day27 independent K-isomer parity and lifetime audit

Scope: read-only inspection of the named research note, script, Walker--Dracoulis source page, and its local raw PDF. Only this report was written. Findings distinguish elementary derivation, direct readback of a review, and experimental claims still requiring retrieval. No wider literature search or replacement isotope dataset was attempted.

Evidence keys (line numbers refer to the audited snapshot):

- **N**: `knowledge/research-notes/k-isomer-triaxial-tunneling-and-hindrance-collapse.md`
- **S**: `system/scripts/day27_k_isomer_triaxial_breakdown_study.py`
- **W**: `knowledge/sources/walker-dracoulis-2001-exotic-isomers.md`
- **PDF**: `raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/奇特原子核/综述/2001_Walker_Dracoulis_Exotic Isomers in Deformed Atomic Nuclei.pdf`

The PDF exists, contains 25 pages, and its SHA-256 is `62cc9071a6101118535d16aeb66f0f192e7ad8904abdfa80b6b56119473c1489`, matching W:18-20. Below, PDF page numbers are one-based; printed page = PDF page + 82. PDF text was directly inspected; the original experiments cited by this review were not independently retrieved.

## 1. High: six tabulated E2 branches violate parity

**Locations:** N:35-39, N:41; S:27, S:33, S:39, S:45, S:51, S:63. These label `178Hf 16+ -> 14-` and the five listed `8- -> 6+` branches in `176Yb`, `180W`, `130Ba`, `134Nd`, and `188Pb` as E2.

**Elementary derivation:** For parity eigenstates, a nonzero matrix element requires `pi_f*pi_i = (-1)^lambda` for E-lambda, and `pi_f*pi_i = (-1)^(lambda+1)` for M-lambda. This follows by inserting the parity operator on both sides of the electromagnetic operator. E2 preserves parity; all six displayed branches change it. With `|I_i-I_f|=2`, dipole radiation is also excluded by the angular-momentum triangle rule. M2 and E3 are possible *selection-rule candidates*, not established assignments. If `Delta K=8`, their nominal forbiddenness differs: M2 gives `nu=6`, E3 gives `nu=5`.

Quadrupole triaxiality, gamma tunneling, and Coriolis K mixing do not remove the laboratory electromagnetic parity rule. Their invocation cannot rescue these E2 labels.

**Action:** Remove the six branches from an experimental E2 comparison pending branch-specific source retrieval. Do not mechanically replace all E2 labels by E3. The `136Ce 10+ -> 8+ E2` (S:57) and `190Pt 7- -> 6+ E1` (S:69) pass this elementary screen only; their existence and numbers remain unverified here.

## 2. High: the Hf normalization branch conflicts with the local PDF

**Locations:** N:21, N:35, N:98; S:25-28, S:114-117.

**Direct review readback:** Printed p.89 / PDF p.7, Sec.2.4, states that the 31-year K=16 isomer decays predominantly to the **I=13 member of the K=8 band**, through a **13-keV, lambda=3 transition with nu=5**. Printed p.98 / PDF p.16, Sec.3.3, identifies the K=16 decay as **E3 with reduced hindrance 66**. Together these support the reviewed `16+ -> 13-`, E3, `Delta K=8`, `nu=5` reference, rather than S:27's E2-to-14- branch and `nu=6`.

**Action:** Rebuild the reference around the actual documented branch, retaining its review provenance. The PDF does not establish `f_6=60.5` for the branch claimed here. A newer branch or revised value would need its own primary locator. Do not simply replace 60.5 by 66 while preserving exponent 6, or transfer 66 unchanged to another multipolarity. The 31-year total half-life alone does not specify a radiative partial half-life.

## 3. High: the script cannot reproduce its claimed experimental reduced hindrances

**Locations:** N:20-25, N:32-42; S:23-71, S:102-117, S:127-137. The formula in N:20 is valid when its half-life is the specified *partial gamma-ray* half-life. The dataset instead stores level half-lives and hard-coded `f_nu_exp`; it has no transition energy, gamma/total branching convention, internal-conversion coefficient, or component fraction for a mixed transition. S:115 only raises the supplied value to a power.

**Verified definition:** Printed p.98 / PDF p.16, Sec.3.3, explicitly defines `f_nu=(T_gamma/T_W)^(1/nu)` with a **partial gamma-ray half-life**. Printed p.99 / PDF p.17, Table II, makes the Weisskopf half-life dependent on **transition energy**, mass, and multipolarity. `E_x_keV` is not generally the transition energy.

**Elementary rate bookkeeping:** If `b_t` is the branch fraction including gamma emission and internal conversion, `alpha=lambda_IC/lambda_gamma`, and `T` is the level half-life, then `T_gamma=T*(1+alpha)/b_t`. If an absolute gamma probability `b_gamma` per parent decay is supplied instead, use `T_gamma=T/b_gamma`; do not apply conversion twice. A mixed multipole additionally requires the radiative fraction of the component being compared. A mean lifetime requires `T=ln(2)*tau`.

**Action:** Treat all eight supplied hindrances as unverified inputs until the branch records close these fields. Recompute component-specific `B`, `T_W`, `F`, and `f_nu` with explicit conventions and uncertainties. This audit supplies no new isotope measurements.

## 4. Medium: a conditional hindrance ratio is presented as an observed lifetime collapse

**Locations:** N:24-25, N:35, N:38-42, N:99-100; S:114-117, S:142, S:148.

**Arithmetic replay only:** S computes `(60.5/f_input)^nu`. Its Ba value is `29,592,495.7`; multiplying the supplied 9.54 ms by this gives `282,312.4 s = 3.2675 d`. Those calculations reproduce a conditional surrogate. They do not measure a lifetime enhancement or establish its mechanism. Even the two listed total half-lives give a different ratio: `(31 y)/(9.54 ms) = 1.02546e11`, which itself is not a controlled mechanism comparison.

For actual branch half-lives, `T_gamma=F*T_W`; a comparison needs the Weisskopf factors, energies, multipolarities, and branch/conversion corrections as well as `F`. With different `nu`, S:116 also constructs a hypothetical normalization at the *target's* exponent, rather than the Hf branch's measured total hindrance. Small arithmetic error: N:35 gives `60.5^6` as `4.62e10`; it is `4.90379434e10`.

**Action:** Label the factors as conditional results of the assumed common hindrance baseline. Withdraw measured lifetime-collapse language until findings 1-3 are resolved.

## 5. High: empirical labels and mechanism exclusion exceed both the calculation and the cited review

**Locations:** N:26, N:32, N:55, N:66, N:79, N:88, N:116; S:12-22, S:74-89, S:134, S:143, S:151-154.

S evaluates a prescribed exponential with fixed coefficients and an imposed floor `max(2.5, f_pred)`. It does not solve a tunneling equation, derive electromagnetic matrix elements, retrieve experimental branching data, or test a statistical-mixing likelihood. The clustered numbers are hard-coded; the model floor is an assumption. Citation comments lack branch-level locators and cannot authenticate the eight experimental rows.

**Direct review readback:** Printed pp.98-100 / PDF pp.16-18, Sec.3.3, discusses Coriolis mixing, gamma tunneling, and level density. Printed p.99 explicitly allows explanations of the low-hindrance cases in `174Hf`, `176W`, and `182Os` without gamma tunneling, using high-K admixtures in ground-state bands; pp.99-100 retain an unresolved combined theoretical treatment. This does not decide the listed Ba/Nd/Ce/Pb/Pt cases, but it rules out citing this review as proof that low hindrance uniquely establishes gamma tunneling or excludes alternative mixing.

**Action:** Retain the exponential only as a phenomenological sensitivity exercise. Mark the isotope-specific lifetimes, hindrances, effective gamma values, and exclusion claims as requiring primary retrieval; withdraw assertions of microscopic solution and definitive statistical falsification. Experimental source acquisition is follow-up work, not a fact supplied by this audit.

Validation boundary: calculations above were evaluated in memory from the script's dataset expression. `run_study()` was not executed because it writes shared output. No lint result was used as scientific evidence. Shared notes, scripts, indices, reports, handoff, log, and run state were not edited.
