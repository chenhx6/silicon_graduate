---
type: source
title: "Impact of Nuclear Mass Uncertainties on the r Process"
aliases: [Martin 2016 r-process mass uncertainties, Martin 2016 PRL]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
source_type: journal-article-theory
reading_depth: deep-read
title_original: "Impact of Nuclear Mass Uncertainties on the r Process"
authors: [D. Martin, A. Arcones, W. Nazarewicz, E. Olsen]
journal: Physical Review Letters
year: 2016
volume: 116
pages: 121101
doi: 10.1103/PhysRevLett.116.121101
language: en
canonical_source: doi:10.1103/PhysRevLett.116.121101
citation_key:
raw_file: "raw/papers/isomer/isomer_application/nuclear_astrophysics/2016_Martin et al_Impact of Nuclear Mass Uncertainties on the r Process.pdf"
raw_sha256: bcc1be2537c180ae5197cad0574b85402e34112e6c1ec6dd9625a7000123605b
alternate_version_file: "raw/papers/isomer/isomer_application/nuclear_astrophysics/2016_Martin et al_Impact of Nuclear Mass Uncertainties on the r Process 1.pdf"
alternate_version_sha256: c9045474ae93257657a0d20716a33d5bbc3417d77556ed57db4b8df83c226c09
alternate_version_identity: "CHORUS accepted author manuscript (7 pages, 1,708,925 bytes)"
archive_required: true
nuclei: [128pd, 130cd, 132sn, 134sn, 195pt]
reactions: [neutron-capture, photodissociation, r-process-network]
experiments: []
models: [nuclear-density-functional-theory, skyrme-edf, talys-statistical-model, reaction-network]
observables: [neutron-separation-energy, r-process-abundance, reaction-rate]
methods: [dft-mass-modeling, talys-cross-sections, r-process-simulations]
tags: [r-process, mass-uncertainties, skyrme-edf, astromer, shell-closure, nuclear-astrophysics]
---

# Martin 等（2016）：原子核质量不确定度对快速中子俘获过程（r 过程）的影响

## Bibliographic Record

The paper was published in *Physical Review Letters* 116, 121101 (2016), received 10 December 2015, published 25 March 2016 (DOI: 10.1103/PhysRevLett.116.121101). The published 6-page PDF is retained at `raw/papers/isomer/isomer_application/nuclear_astrophysics/2016_Martin et al_Impact of Nuclear Mass Uncertainties on the r Process.pdf` with SHA-256 `bcc1be2537c180ae5197cad0574b85402e34112e6c1ec6dd9625a7000123605b` (794,047 bytes). The CHORUS accepted author manuscript (7 pages) is preserved in the same directory as `... 1.pdf` with SHA-256 `c9045474ae93257657a0d20716a33d5bbc3417d77556ed57db4b8df83c226c09` (1,708,925 bytes). `archive_required: true` is preserved.

## Scope and Reading Depth

The published 6-page paper was read in full, including text, figures 1–3, and equations. The study computes $r$-process nucleosynthesis yields in realistic astrophysical trajectories (neutron star mergers and magneto-rotational jet-like supernovae) using neutron capture and photodissociation rates based on nuclear density functional theory (DFT) with six Skyrme energy density functionals (EDFs: SkM*, SkP, SLy4, SV-min, UNEDF0, UNEDF1).

## Summary

Martin et al. performed the first systematic evaluation of mass-model uncertainty bands in $r$-process nucleosynthesis using microscopic DFT mass inputs from six Skyrme functionals. For each functional, Maxwellian-averaged $(n,\gamma)$ and $(\gamma,n)$ rates were computed with the TALYS statistical model code and input into a comprehensive reaction network. The authors found that systematic abundance uncertainty bands are strongly correlated and non-uniform across mass number $A$:
1. The $A \approx 130$ second peak is constrained by fission recycling in neutron star mergers, but displays significant mass sensitivity around shell closures ($N=82$) where nuclei transition between deformed and spherical shapes.
2. The pre-peak and post-peak abundances and the $A \approx 195$ third peak are directly governed by the fine trends in two-neutron separation energy $S_{2n}$ and single-neutron separation energy $S_n$, because photodissociation rates scale exponentially as $\lambda_{(\gamma,n)} \propto \exp(-S_n / kT)$.
3. The paper establishes that microphysics uncertainties at magic shell gaps ($N=82$ and $N=126$) leave immediate imprints on the freeze-out path and final elemental distributions.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MAR16-1 | Using six microscopically optimized Skyrme EDFs (SkM*, SkP, SLy4, SV-min, UNEDF0, UNEDF1), the authors compute correlated systematic uncertainty bands for $r$-process abundances in neutron star mergers and jet-like supernovae. | model-calculation | direct | PDF p. 1–2, Abstract, Fig. 1 | false |
| MAR16-2 | The abundance uncertainty bands are non-uniform across mass number $A$, contrasting with random mass variations, because DFT forces maintain physical correlations between binding energies of neighboring isotopes. | author-interpretation | direct | PDF p. 2, text col. 2, Fig. 1 | false |
| MAR16-3 | Freeze-out abundances and the formation of peaks at $A \sim 130$ ($N=82$) and $A \sim 195$ ($N=126$) directly correlate with local variations in two-neutron separation energies $S_{2n}$ along isotopic chains. | model-calculation | direct | PDF p. 2–4, Fig. 2 | false |
| MAR16-4 | Photodissociation rates $\lambda_{(\gamma,n)}$ depend exponentially on neutron separation energies $S_n$, amplifying small mass model variations ($300–500\text{ keV}$) into orders-of-magnitude rate shifts during $(n,\gamma) \rightleftharpoons (\gamma,n)$ equilibrium. | derived-observable | direct | PDF p. 2, col. 1, Eq. context | false |
## Competing Interpretations and Limitations

### Mass Model Variations and Isomer Equilibrium Assumptions
In standard $r$-process networks (including those used in Martin 2016), each isotopic species is assumed to occupy its ground state or to maintain instantaneous thermal Boltzmann equilibrium with all low-lying excited states. However, in nuclei near the $N=82$ waiting point (e.g. $^{128}\text{Pd}$ $8^+$, $^{126}\text{Pd}$ $5^-/7^-$, $^{131}\text{In}$ $1/2^-$, and predicted isomers such as $^{129}\text{Pd}$ $19/2^-$):
1. When isomer de-excitation is hindered by large spin differences ($\Delta J \ge 3$ or $K$-forbiddenness) and low transition energies, thermal coupling requires photo-excitation through intermediate "doorway" states.
2. If thermalization timescales are slower than expansion and $\beta$-decay timescales, the isomer and ground state act as decoupled "astromers" with distinct neutron-capture cross sections and beta-decay half-lives.
3. As demonstrated by Martin 2016's sensitivity to $S_n$, if an isomer has an effective neutron separation energy $S_n^{\text{iso}} = S_n^{\text{g.s.}} - E_x$, its photodissociation rate is enhanced, which can alter local reaction paths during freeze-out.

## Source Self-Audit

- Audit date: 2026-11-07 by Codex research agent (self-audit, not human-reviewed).
- File lineage check: identified published PRL version (6 pages, 794,047 bytes, SHA `bcc1be25...`) vs CHORUS accepted manuscript (7 pages, 1,708,925 bytes, SHA `c9045474...`).
- Consistency check: verified that six Skyrme EDFs are SkM*, SkP, SLy4, SV-min, UNEDF0, and UNEDF1 matching Ref. [42] (Erler et al. Nature 2012).

## Extracted Pages

- PDF p. 1 (121101-1): Motivation; astrophysical sites (NS mergers vs jet-like SNe); Skyrme EDF selection; abstract.
- PDF p. 2 (121101-2): Reaction network description; TALYS statistical rate calculations; Fig. 1 abundance uncertainty bands.
- PDF p. 3 (121101-3): Fig. 2 analysis of $S_{2n}$ trends along isotopic chains and comparison of freeze-out vs final abundances for SkM*, SLy4, and UNEDF0.
- PDF p. 4 (121101-4): Microscopic origin of abundance troughs and peaks; discussion of deformation transitions around $N=82$ and $N=126$.
- PDF p. 5 (121101-5): Sensitivity of jet-like SNe vs NS mergers; fission recycling impact on $A \sim 130$.
- PDF p. 6 (121101-6): Conclusions and references (1–66).
