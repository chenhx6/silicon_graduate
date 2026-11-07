---
type: source
title: "Isomerism in the “south-east” of 132Sn and a predicted neutron-decaying isomer in 129Pd"
aliases: [Yuan 2016 129Pd neutron-decaying isomer, Yuan 2016 PLB]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
source_type: journal-article-theory
reading_depth: deep-read
title_original: "Isomerism in the “south-east” of 132Sn and a predicted neutron-decaying isomer in 129Pd"
authors: [Cenxi Yuan, Zhong Liu, Furong Xu, P. M. Walker, Zs. Podolyák, C. Xu, Z. Z. Ren, B. Ding, M. L. Liu, X. Y. Liu, H. S. Xu, Y. H. Zhang, X. H. Zhou, W. Zuo]
journal: Physics Letters B
year: 2016
volume: 762
pages: 237–242
doi: 10.1016/j.physletb.2016.09.030
language: en
canonical_source: doi:10.1016/j.physletb.2016.09.030
citation_key:
raw_file: "raw/papers/isomer/isomer_application/nuclear_astrophysics/2016_Yuan et al_Isomerism in the “south-east” of 132Sn and a predicted neutron-decaying isomer in 129Pd 1.pdf"
raw_sha256: cf9c983dc4f88bffc8e2d5041948b0c1e0aabf396a696edd710be3f8c8e1ade1
archive_required: true
nuclei: [129pd, 128pd, 131cd, 130cd, 132in, 134in, 135sn, 136sn, 138sn]
reactions: []
experiments: []
models: [shell-model, oxbash, jj46-hamiltonian, monopole-based-universal-interaction, m3y-spin-orbit, two-potential-approach]
observables: [level-energy, one-neutron-separation-energy, b-e2, partial-half-life, neutron-decay-width]
methods: [large-scale-shell-model, bohr-sommerfeld-quantization, barrier-penetration]
tags: [shell-model, 129pd, neutron-radioactivity, isomer, southeast-132sn, jj46, theoretical-prediction]
---

# Yuan 等（2016）：`132Sn`“东南区”同核异能性与 `129Pd` 中预测的中子放射性同核异能态

## Bibliographic Record

The article was published in *Physics Letters B* 762, 237–242 (2016), received 2 July 2016, accepted 9 September 2016, available online 21 September 2016 (DOI: 10.1016/j.physletb.2016.09.030). The 6-page PDF is preserved at `raw/papers/isomer/isomer_application/nuclear_astrophysics/2016_Yuan et al_Isomerism in the “south-east” of 132Sn and a predicted neutron-decaying isomer in 129Pd 1.pdf` with SHA-256 `cf9c983dc4f88bffc8e2d5041948b0c1e0aabf396a696edd710be3f8c8e1ade1` (517,797 bytes). `archive_required: true` is preserved.

## Scope and Reading Depth

The 6-page paper was read in full, covering theoretical model construction, effective single-particle energy evolutions, calculated level schemes, Table 1 (neutron separation energies), Table 2 (isomer properties and transition rates), and equations (1)–(3) for the two-potential neutron barrier penetration.

## Summary

Yuan et al. developed a new shell-model Hamiltonian, designated `jj46`, tailored for the "south-east" quadrant of $^{132}_{50}\text{Sn}_{82}$ ($Z \le 50, N \ge 82$). The valence space comprises 4 proton hole/particle orbits ($\pi 0f_{5/2}, 1p_{3/2}, 1p_{1/2}, 0g_{9/2}$) and 6 neutron orbits ($\nu 1f_{7/2}, 2p_{3/2}, 2p_{1/2}, 0h_{9/2}, 1f_{5/2}, 0i_{13/2}$). The proton-proton and neutron-neutron matrix elements are derived from CD-Bonn $G$-matrix interactions, while the cross-shell proton-neutron interaction is constructed from the monopole-based universal interaction ($V_{MU}$) augmented by M3Y spin-orbit force ($V_{MU} + LS$).

The `jj46` Hamiltonian successfully reproduces experimental $S_n$ values, level energies, and isomeric $B(E2)$ values in $^{134,136,138}\text{Sn}$, $^{130}\text{Cd}$, and $^{128}\text{Pd}$. The authors systematically predict several unobserved isomers across the region:
1. In $^{135}\text{Sn}$, a $21/2^-$ isomer at $2.288\text{ MeV}$ with $\tau_{E2} \approx 100\text{ ns}$ ($\nu(1f_{7/2})^2(0h_{9/2})$).
2. In odd-odd $^{132,134}\text{In}$ and $^{130}\text{Ag}$, low-lying $5^-$ isomers located $\sim 70\text{ keV}$ above the $7^-$ ground states with extended lifetimes due to $\pi-\nu$ transition cancellation.
3. In $^{129}_{46}\text{Pd}_{83}$, a $19/2^-$ isomer is predicted at $E_x = 1.903\text{ MeV}$, which lies above the calculated one-neutron separation energy ($S_n = 1.524\text{ MeV}$ in `jj46`, giving $Q_n = 0.379\text{ MeV}$; $S_n = 1.461\text{ MeV}$ in FRDM, giving $Q_n = 0.442\text{ MeV}$). Decay to the $2^+$ first excited state of $^{128}\text{Pd}$ ($1.311\text{ MeV}$) is energetically closed, so neutron emission can proceed only to the $0^+$ ground state with orbital angular momentum $\ell = 9$. The calculated partial neutron half-life $T_{1/2}(n) \approx 0.3–10\ \mu\text{s}$ competes directly with the calculated $E2$ $\gamma$ decay ($\tau_{E2} = 0.955\ \mu\text{s}$).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| YUA16-1 | A shell-model Hamiltonian `jj46` is constructed for $Z \le 50, N \ge 82$ using CD-Bonn $G$-matrix for $\pi\pi/\nu\nu$ and $V_{MU} + LS$ for $\pi\nu$, reproducing experimental $S_n$, levels, and seniority $B(E2)$ in $^{134,136,138}\text{Sn}$, $^{130}\text{Cd}$, and $^{128}\text{Pd}$. | model-calculation | direct | PDF p. 1–2, Table 1, Fig. 1 | false |
| YUA16-2 | In $^{129}\text{Pd}$, the ground state is predicted to be $7/2^-$ ($\pi(0g_{9/2})^{-4} \nu(1f_{7/2})$) and a $19/2^-$ seniority-core isomer is predicted at $E_x = 1.903\text{ MeV}$ ($\pi(0g_{9/2})^{-4}_{8^+} \otimes \nu(1f_{7/2})$). | model-calculation | direct | PDF p. 4, Table 2, Fig. 3 | false |
| YUA16-3 | The calculated one-neutron separation energy $S_n$ for $^{129}\text{Pd}$ is $1.524\text{ MeV}$ in `jj46` ($1.461\text{ MeV}$ in FRDM; $1.780\text{ MeV}$ in AME2012 extrapolation), placing the $19/2^-$ isomer at $Q_n = 0.379\text{ MeV}$ ($0.442\text{ MeV}$ in FRDM; $0.123\text{ MeV}$ in AME2012) above the $^{128}\text{Pd}(0^+) + n$ threshold, while decay to $^{128}\text{Pd}(2^+, 1.311\text{ MeV})$ is energetically closed. | model-calculation | direct | PDF p. 2, 4, Table 1, text col. 1 | false |
| YUA16-4 | Using the two-potential approach with Bohr-Sommerfeld quantization (Eqs. 2–3), the partial half-life for $\ell=9\hbar$ centrifugal-barrier neutron emission to $^{128}\text{Pd}(0^+)$ is predicted to be $T_{1/2}(n) \approx 0.3–10\ \mu\text{s}$, which is directly competitive with the calculated $E2$ $\gamma$-decay mean life ($\tau_{E2} = 0.955\ \mu\text{s}$, $B(E2) = 12.88\ e^2\text{fm}^4$). | model-calculation | direct | PDF p. 4–5, Table 2, text col. 2 | false |
## Competing Interpretations and Limitations

### Distinction Between Theoretical Prediction and Physical Observation
The neutron-decaying $19/2^-$ isomer in $^{129}\text{Pd}$ is strictly a **THEORETICAL MODEL PREDICTION** within the Yuan et al. (2016) paper, not an experimental observation reported by the authors.
- In Yuan et al. (2016), the authors explicitly state: "The predicted $19/2^-$ isomer in $^{129}\text{Pd}$ could decay by both electromagnetic transitions and neutron emission with comparable partial life-times, making it a good candidate for neutron radioactivity, a decay mode which is yet to be discovered."
- Kinematics and Threshold Sensitivity: Because $E_x(19/2^-) = 1.903\text{ MeV}$, the decay energy $Q_n = E_x - S_n$ is finite and positive for $S_n < 1.903\text{ MeV}$ (e.g. $Q_n = 0.379\text{ MeV}$ in `jj46`; $0.442\text{ MeV}$ in FRDM; $0.123\text{ MeV}$ using AME2012 mass extrapolation). Closing the neutron decay channel requires $S_n \ge 1.903\text{ MeV}$ (an increase of $\Delta S_n \ge 379\text{ keV}$ over `jj46`), or a lower isomeric level energy. A $+200\text{ keV}$ shift in $S_n$ reduces $Q_n$ to $\sim 0.18\text{ MeV}$, which substantially suppresses the $\ell = 9$ penetration rate due to the centrifugal barrier, but does not strictly close the channel unless $Q_n \le 0$.
- The claim must be cited as a model prediction and candidate for experimental verification, never as an observed physical decay.

## Source Self-Audit

- Audit date: 2026-11-07 by Codex research agent (self-audit, not human-reviewed).
- Consistency check: confirmed that $E_x(19/2^-) = 1.903\text{ MeV}$, $S_n(jj46) = 1.524\text{ MeV}$, $B(E2) = 12.88\ e^2\text{fm}^4$, $\tau_{E2} = 0.955\ \mu\text{s}$, and $T_{1/2}(n) = 0.3–10\ \mu\text{s}$ match Table 1, Table 2, and text on PDF p. 4–5.
- Status classification: purely theoretical paper (`source_type: journal-article-theory`).

## Extracted Pages

- PDF p. 1 (237): Abstract; introduction to $N=82$ shell gap and isomer stepping stones; motivation for neutron radioactivity.
- PDF p. 2 (238): Construction of `jj46` Hamiltonian; model space; Table 1 one-neutron separation energies $S_n$ across Sn, In, Cd, Ag, Pd.
- PDF p. 3 (239): Fig. 1 levels of $^{134,136,138}\text{Sn}$; Fig. 2 neutron effective single-particle energies (ESPE); configuration mixing discussion.
- PDF p. 4 (240): Fig. 3 levels of In, Cd, Pd; Fig. 4 $\pi^{-1}\nu$ multiplets in $^{132}\text{In}$; Fig. 5 proton-hole and neutron-particle ESPEs; Table 2 predicted isomer properties.
- PDF p. 5 (241): Table 2 continuation; Eqs. (2)–(3) two-potential model for neutron emission barrier penetration; predicted $\ell=9\hbar$ neutron decay lifetime in $^{129}\text{Pd}$.
- PDF p. 6 (242): Summary, acknowledgments, and references (1–37).
