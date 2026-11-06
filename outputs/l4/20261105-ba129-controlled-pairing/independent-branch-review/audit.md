The Kumar report supports a distinct reported acquisition and a potentially useful photon-intensity cross-check. It does **not yet supply a validated, angle-integrated branch dataset or independently measured mixing ratios**. The six upper-panel points can be recovered from vector graphics; the two figures repeat that dataset. The lower panels depend on a rotational assumption, and the printed mixing prescription is incomplete under the report's own branching definition.

The primary source [P] is [kumar-branch-report.pdf](/workspace/wiki/raw/papers/gpt/query/20261106-ba129-independent-branch-data/kumar-branch-report.pdf), two PDF pages, SHA-256 `210c65109df9b2d203f95643e0fb89746a20f836265c802bb0f2010aabb5eda1`. Bibliographic source [M] is the parent's archived [inspire-lookup-0.json](/workspace/wiki/raw/papers/gpt/query/20261106-ba129-independent-branch-data/inspire-lookup-0.json), SHA-256 `e865a2238377e795b0dae5a7f08cc015bc1934442228b6f474b7d3d46ea6a8b2`.

**Publication identity is resolved at the metadata level:** [M], `hits.hits[0]`, is record **2765575**, whose document key matches the PDF acquisition manifest. Its `metadata.publication_info[0]` gives *DAE Symp. Nucl. Phys.* **67 (2024), 121–122**; `metadata.imprints[0].date` records the same year within that record. The conference identifier is `C23-12-09`. The PDF has no printed publication year; its creation timestamp is September 15, 2023, which is not a publication date. The supplied record 2770104 returned HTTP 404. Use the archived exact-document lookup, not that identifier or a search snippet. The new source-collection date label is November 6; actual tool timestamps remain November 5 UTC and have not been relabelled.

[P], PDF p. 1, title block, names **S. Kumar, Mallicka Kundu, P. S. Rawat, Ksh. Rojeeta Devi, H. Chutani, and M. Goyal**. INSPIRE's author array omits Ksh. Rojeeta Devi; retain the PDF's six authors. [P], p. 1, Experimental Details, specifies \(^{121}\mathrm{Sb}(^{12}\mathrm C,p3n)^{129}\mathrm{Ba}\), **66 MeV**, IUAC New Delhi, a **1.2 mg/cm²** Sb target with **10.0 mg/cm² \(^{197}\)Au backing**, and INGA with **18 Compton-suppressed clovers plus two LEPS detectors**. It gives neither an acquisition date nor a total coincidence-event count.

For historical comparison, [R] is the [2014 reaction ENSDF object](/workspace/wiki/raw/papers/gpt/learning-daily/20261016-DAY15-ado-angular-distribution-geometry/nndc-129ba-129056013-201408-09194d4feed3.ens); [A] is the corresponding [adopted object](/workspace/wiki/raw/papers/gpt/learning-daily/20261016-DAY15-ado-angular-distribution-geometry/nndc-129ba-129056001-201408-15d8e353eb23.ens). Line numbers below are one-based, including their initial blank line.

| Evidence component | Independence and dependency |
|---|---|
| Present experiment | Its reported Sb/C reaction and apparatus distinguish it from the earlier acquisitions. [R]:5–9 describes the 1992 Sn/C and Cd/O measurements and the 1977/1978 Sn/C measurements. This supports a new event sample as reported; raw events were unavailable for checking acquisition provenance directly. |
| Upper experimental points | Derived from intensities with \(\delta=0\), [P] p. 1 Eqs. 1–2; p. 2 paragraph following Eq. 3 and figure captions. A photon-ratio representation, conditional on the underlying intensity treatment. |
| “Previous work” points | Explicitly attributed to Byrne et al. (1992), [P] p. 2, reference [3]. [R]:22 assigns its photon energies/intensities to that same measurement. These are repeated historical evidence. |
| Lower experimental points | Reprocess the intensity observable using a \(K\)-dependent rotational prescription for mixing. They are not independent angular-distribution or polarization measurements of \(\delta\). |
| Theory curves | Donau-formula calculations; \(Q_0=3.4\) e·b and \(g_R=0.34\) are taken from Byrne, with quasiparticle \(g\) factors from another compilation. [P] p. 2, Eq. 4 and paragraph below Fig. 2. Their agreement is model-dependent. |

Write \(E_d=E_\gamma(I\rightarrow I-1)\), \(E_q=E_\gamma(I\rightarrow I-2)\), \(r=I_{\gamma d}/I_{\gamma q}\), and \(S\) for the upper-panel ordinate. Rewriting [P] Eqs. 1–2 gives

\[
S=0.6967\,\frac{E_q^5}{E_d^3}\,r,\qquad
r=\frac{S E_d^3}{0.6967E_q^5},\qquad
\frac{B(M1)}{B(E2)}=\frac{S}{1+\delta^2}.
\]

Energies must be in **MeV**. The powers are the E2 and M1 photon-rate powers, five and three. The inversion removes the assumed \(\delta=0\) interpretation of \(S\); it does not remove intensity-systematic errors. These are photon ratios, without an added internal-conversion factor. A total electromagnetic branching ratio would require conversion coefficients separately. The two-page report has no numerical transition-pair/intensity table: Fig. 1 labels some energies but does not unambiguously identify every plotted pair.

**Eq. 3 was inspected visually**, including its denominator. Define the rotational E2-strength ratio \(F_{IK}=B(E2;I\rightarrow I-1)/B(E2;I\rightarrow I-2)\). For a common intrinsic quadrupole moment and good \(K\), independent angular-momentum algebra gives

\[
F_{IK}=\frac{2K^2(2I-1)}
 {(I+1)(I+K-1)(I-K-1)}.
\]

With the report's \(\lambda=I_{\gamma q}/I_{\gamma d}\), the E2 fraction in the mixed branch must be

\[
f=\frac{\delta^2}{1+\delta^2}
  =\lambda F_{IK}(E_d/E_q)^5 .
\]

The visually checked Eq. 3 omits **\(\lambda\)**. This is an algebraic omission under Eq. 2, unless an unstated \(\lambda=1\) restriction is imposed. It does not establish which numerical prescription the authors actually used. The amended relation also requires \(0\le f<1\) for finite real \(\delta\), and gives no sign of \(\delta\). At \(K=11/2,I=13/2\), its nominal \(I-2\) final spin is below \(K\); the corresponding CG coefficient is zero, so this same-band ratio is undefined.

Using candidate energies from [R], the amended \(K=9/2\) prescription reproduces the six **previous-work** lower points within approximately 0.00173 in the plotted ordinate. It does not reproduce all present-work points. In particular, the present central values give \(f\approx1.070\) and \(1.383\) at \(I=17/2\) and \(21/2\). These are conditional central-value admissibility warnings, **not statistical rejections**: the new pair assignments, uncertainty model, and authors' numerical procedure are unavailable. No clipping, absolute-value operation, or replacement mixing prescription was applied.

**The gate requires a conditional audit.** [P] p. 1, Fig. 1 caption and Results opening, show a **174.1-keV gate**. They do not state that this single spectrum alone generated every ratio, nor describe efficiency, angular-correlation, timing, background, contamination, or path-acceptance corrections. Schematically, background-subtracted gated counts obey

\[
C_{i|g}\ \propto\
N_{\rm parent}b_i^\gamma\,\epsilon_i\epsilon_g\,p_{g|i}\,A_{i,g},
\]

where \(p_{g|i}\) is the downstream gate-photon probability and \(A_{i,g}\) includes geometry/correlation and timing acceptance. Their cancellation in a same-parent ratio must be demonstrated.

The plausible ENSDF counterpart is the **173.6-keV E1**, \(182.04\;(9/2^-)\rightarrow8.42\;(7/2^+)\), [A]:83,108–119. The report provides no level scheme or calibration statement resolving the 0.5-keV difference. **Conditional on that identification**, the 643.6-keV parent has paths

\[
643.6\xrightarrow{364.7}278.81\xrightarrow{96.8}182.04,
\qquad
643.6\xrightarrow{461.6}182.04 .
\]

Thus this downstream gate does not intrinsically veto either branch in the listed cascade ([R]:79–104,132–142). Internal conversion of the unobserved 96.8-keV step still feeds the 182-keV level; detecting that photon is not required by a gate on the subsequent decay. A topological check of the listed negative-parity cascade through \(25/2\) likewise reaches that common state. This proves neither cascade completeness nor equal experimental acceptance. Its evaluated \(T_{1/2}=15.2(10)\) ns ([A]:108–114) makes the unspecified timing treatment relevant.

**Digitization is feasible and useful for screening.** Vector-marker extraction finds six present and six previous points in each upper panel, at \(I=13/2,15/2,17/2,19/2,21/2,25/2\); no experimental point was extracted at \(23/2\). Fig. 2 uses \(K=9/2\), Fig. 3 uses \(K=11/2\). Their upper experimental series repeat, with maximum ordinate difference **0.007915**; do not average them or count them twice. The previous upper series agrees with the [R] Eq. 1 reconstruction within **0.002197**.

[conditional-graphic-checks.csv](conditional-graphic-checks.csv) records approximate centres and a **conditional** inversion using explicitly labelled ENSDF/1992 energy pairs. For example, the present \(13/2\) point gives \(r\approx5.58\) using 364.7/461.6 keV. This is an audit candidate, not a certified new branching measurement. Displayed error bars were not converted into statistical uncertainties; confidence levels, systematic components and covariance are unspecified. Digitization agreement is not measurement precision.

Actual verification: `python3 -B outputs/l4/20261105-ba129-controlled-pairing/independent-branch-review/check_source.py --write` exited **0**. It checked **15 exact CG ratios**, **nine scalar/vector/completeness controls**, **three exact photon-rate identities**, the forbidden-\(K\) case, vector extraction/axis mapping, historical intensity reconstruction, and restricted cascade closure. [source-audit-results.json](source-audit-results.json) records results, actual tool time, four input hashes and their unchanged status. The script imports no frozen physics kernel.

The appropriate status is **candidate independent intensity evidence, pending extraction-protocol clarification**. Upper points may eventually test energy-calibrated EM predictions through photon ratios; lower points and theory-derived mixing cannot serve as independent EM holdouts. No absolute strengths, lifetimes, mixing signs, physical-shape validation, novelty claim, or mode verdict follow. Publisher pages/crops and extracted text remain solely under `tmp/ba129-independent-branch-data/`; this output directory contains the authored audit, numerical checks, JSON and CSV only.
