---
type: research-note
title: "133Ce triaxial core and collective-mode research route"
aliases: [133Ce triaxial deformation route, 133Ce collective excitation prospectus]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
visibility: private
publication_status: local-only-unpublished-user-data
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [userdata-133ce-southafrica-dataset, nuclearmap-jcnp-pc-pk1]
created_from: "User-authorized South Africa data cleanup and 133Ce collective-mode research"
tags: [133ce, triaxiality, collective-excitation, wobbling, potential-energy-surface, nuclear-map, user-data]
---

# `133Ce` triaxial core and collective-mode research route

## Research Trigger

The user provided specific doctoral research context from the midterm review
(`raw/personal/graduation_process/midterm_review/附件4：中期报告模板.doc`),
authorized a clean organization of the private South Africa archive, and
directed subsequent doctoral work to focus on the triaxial core and collective
excitations of both `131Ce` and `133Ce`. The South Africa archive is organized
by provenance and immutable input boundaries:

- `raw/data/SouthAfrica/133Ce_iThemba2019/`: immutable acquisition layer
  including experiment records, sorter configuration, calibration source spectra
  (`calibration/source-spectra/`), cube products (`cube/`), original processed
  matrices (`mat/m4b/`), and supplied ROOT representations (`mat/root/`).
- `raw/data/SouthAfrica/133Ce/`: derived analysis and systematics layer
  including analysis workbooks (`analysis/intensity.xlsx` and
  `analysis/intensity_iThemba2019_export.xlsx`), figures, analysis code,
  notebooks, and cross-nucleus systematics.

The cleanup manifest is
`outputs/l4/20261101-133ce-southafrica-data-audit/raw-cleanup-plan-20261101.json`,
and the second-pass fixed-input ledger and receipt are
`fixed-input-reclassification-plan.json` and
`fixed-input-reclassification-receipt.json`.

## Grounded Evidence

### NuclearMap route

The user supplied `http://nuclearmap.jcnp.org/` as a local research entry
point. The retrieved theory page, observation script and neighboring PES
images are archived under
`raw/figures/gpt/learning-daily/20261101-day29-133ce-nuclearmap-pes/`, with
the file-level hashes in `manifest.json`. The accessible site identifies its
calculation as triaxial
relativistic Hartree–Bogoliubov (RHB) results with the PC-PK1 density
functional. Its theory page describes constrained quadrupole calculations in
`β` and `γ`, followed by a five-dimensional collective Hamiltonian (5DCH)
with vibrational and rotational kinetic terms and a collective potential.
The page states that moments of inertia use the Inglis–Belyaev formula, mass
parameters use a cranking approximation, and the collective potential includes
zero-point-motion subtraction. These are properties of the website's
calculation framework, not direct measurements of `133Ce`.

Across the even-even Cerium core chain ($Z=58$), the PC-PK1 RHB calculations
demonstrate a pronounced shape evolution:

- $N=70$ (`128Ce`): $\beta=0.32, \gamma=0^\circ$ (strongly deformed prolate)
- $N=72$ (`130Ce`): $\beta=0.25, \gamma=0^\circ$ (prolate)
- $N=74$ (`132Ce`): $\beta=0.22, \gamma=17^\circ$ (triaxial equilibrium ground-state minimum)
- $N=76$ (`134Ce`): $\beta=0.17, \gamma=0^\circ$ (prolate ground state, but with soft $\gamma$ valley extending to $\sim 25^\circ$)
- $N=78$ (`136Ce`): $\beta=0.13, \gamma=0^\circ$
- $N=82$ (`140Ce`): $\beta=0.00, \gamma=0^\circ$ (spherical shell closure)

This establishes that `131Ce` ($N=73$) and `133Ce` ($N=75$) bracket the triaxial
minimum `132Ce` ($N=74$). `131Ce` is located at the transition into triaxiality
from `130Ce`, whereas `133Ce` sits between the triaxial `132Ce` and the $\gamma$-soft
`134Ce`.

### Midterm review doctoral context

The author's doctoral midterm report records the primary experimental findings
for both target nuclei:

1. **`133Ce` (iThemba LABS experiment)**:
   - 21 new $\gamma$ transitions identified.
   - A new low-spin rotational band with bandhead spin $13/2^-$ consisting of
     12 transitions was established.
   - Extracted multipole mixing ratios $\delta$ of interband transitions connecting
     the new band to known sequences are negative with small absolute values,
     demonstrating strong $M1$ character.
   - The new band exhibits signature splitting with signature inversion at
     intermediate spin.
   - Comparison with isotonic partners `131Ba` ($N=75$) and `135Nd` ($N=75$)
     indicates a triaxial core transition from $\gamma$-soft to $\gamma$-rigid.
2. **Methodological breakthrough: Probability-Density Mapping (PDM)**:
   - Developed by Hong-Xing Chen, Song Guo et al. (*Nuclear Science and Techniques*,
     under review) to extract $\gamma$-ray multipole mixing ratios without
     preset spin alignment $\sigma/I$.
   - Takes $(R_{ADO}, P)$ joint likelihood, maps through the transformation
     Jacobian to $(\delta, \sigma/I)$, and marginalizes over $\sigma/I$,
     correctly propagating asymmetric uncertainties and secondary solutions.
3. **`131Ce` (CIAE Beijing Tandem experiment)**:
   - Data acquired at the HI-13 tandem accelerator national laboratory.
   - Energy calibration and coincidence analysis are underway to complete the
     high-spin level scheme, assign spin/parity, and extract multipolarities.

### Private-data observations

The integer bin comparison in `matrix-content-audit.json` proves that the five
supplied ROOT matrices fall into two distinct coincidence processing sets:

- `g45allmatprompt.root` and `g90allmatprompt.root` match the `prompt`-gated
  binary arrays (`m4b/g45allmatprompt.m4b` and `m4b/g90allmatprompt.m4b`) with
  zero bin mismatches.
- `gg.root`, `hgg.root` and `vgg.root` match the unprompted binary arrays
  (`m4b/ggmat.m4b`, `m4b/hggmat.m4b`, `m4b/vggmat.m4b`) with zero bin
  mismatches.

This division must be preserved in any future analysis: angular distributions
($R_{ADO}$) from 45°/90° prompt matrices cannot be directly combined with
polarization asymmetries from unprompted $H/V$ matrices without correcting for
the different prompt time-gate cut and background continuum.

## Provisional Reasoning

### Physical origin of negative, small-$\delta$ connecting transitions

In the transverse wobbling model (Frauendorf & Dönau 2014), the $n=1 \to n=0$
wobbling transition is characterized by enhanced collective $E2$ strength
($B(E2)_{out}/B(E2)_{in} \sim 0.2 - 0.5$) and large mixing ratios ($|\delta| \gg 1$).
The experimental observation in `133Ce` that the interband connecting transitions
have negative, small absolute mixing ratios ($|\delta| \lesssim 0.5$) provides
strong experimental evidence against a simple one-phonon wobbling interpretation
for this branch.

Instead, small negative $\delta$ values with dominant $M1$ character are the
hallmark of:

1. **Unfavored signature partner coupling**: Single-quasiparticle $h_{11/2}$ neutron
   matrix elements in an odd-$A$ triaxial rotor naturally produce predominant
   $M1$ connecting transitions with small negative $\delta$ (Chakraborty 2023,
   Rose & Brink 1967).
2. **Signature inversion**: In odd-$A$ nuclei in the $A \sim 130$ region, Coriolis
   mixing of low-$\Omega$ $h_{11/2}$ components in a $\gamma$-soft or triaxial
   potential can invert the normal energy ordering of favored and unfavored
   signatures as spin increases.
3. **Core $\gamma$-softness vs $\gamma$-rigidity**:
   - In an axially symmetric rotor, no signature inversion occurs without large
     $j$-shell mixing.
   - In a triaxial rotor with $\gamma \sim 15^\circ - 25^\circ$, the non-axial
     Coriolis coupling naturally drives signature inversion and dictates the
     staggering phase of $B(M1)/B(E2)$ ratios.
   - The evolution from `131Ba` ($\gamma$-soft) to `133Ce` and `135Nd` traces the
     microscopic competition between the prolate-driving $h_{11/2}$ neutron and
     the triaxial-polarizing core.

## Falsification or Reverse Tests

1. **PDM re-extraction test**: Apply the PDM algorithm to the raw counts of the
   625, 582, and 464 keV transitions extracted from `g45allmatprompt.root` and
   `g90allmatprompt.root` and compare with the cached values in
   `133Ce/analysis/intensity.xlsx`. If the marginalized posterior of $\delta$
   excludes the large-$\delta$ wobbling domain, the transverse wobbling
   assignment for this band is ruled out.
2. **Time-gate matching check**: Project the 170 keV and 620 keV gates from both
   `ggmatprompt.m4b` and `m4b/ggmat.m4b` to quantify the prompt time cut
   efficiency. A valid $R_{ADO}$ or asymmetry ratio must show invariance under
   the prompt gate definition.
3. **Isotonic staggering test**: Compare the signature splitting energy difference
   $\Delta E(I) = E(I) - \frac{1}{2}[E(I+1) + E(I-1)]$ between `133Ce`, `131Ba`,
   and `135Nd`. If the signature inversion point in `133Ce` tracks `131Ba`,
   $\gamma$-softness dominates; if it tracks `135Nd`, a more rigid triaxial core
   is favored.

## Failure Conditions

Stop at partial-L4 readiness if event-level records, detector efficiency matrices,
prompt gate timing curves, or independent holdout gates cannot be recovered from the
supplied archive. Do not synthesize counts or manufacture an unmeasured $E2$ branch.

## Assumptions

The neighboring even-even PES from NuclearMap provide a qualitative mean-field
core prior. The odd neutron is assumed to occupy predominantly the $1h_{11/2}$
subshell for negative-parity states, with potential mixing from $2f_{7/2}$.

## Competing Explanations

1. Signature-partner band with signature inversion.
2. Tilted precession (TiP) band (Lawrie 2020).
3. Quasi-$\gamma$ bandhead coupled to a single quasiparticle.
4. Transverse wobbling (substantially disfavored by small negative $\delta$).

## Transfer Conditions

Transfer conclusions between `131Ce` and `133Ce` only by accounting for the
two-neutron hole/particle position relative to the $N=74$ triaxial core `132Ce`.
`131Ce` ($N=73$) has a smaller Fermi level in the $h_{11/2}$ shell, leading to
different signature splitting and alignment frequencies than `133Ce` ($N=75$).

## Open Questions

- What are the experimental $R_{ADO}$ and polarization values for the 12 transitions
  in the new $13/2^-$ band of `133Ce`?
- Can the PDM method be run directly on the matrix projection counts of `133Ce`?
- What is the exact level scheme for `131Ce` from the CIAE HI-13 experiment, and
  does it exhibit a partner band similar to `133Ce`?

## Human Review

This note records the author's doctoral research direction and a Codex self-audit.
It remains `unreviewed`.

## Promotion or Rejection History

2026-11-01: updated with the author's doctoral research roadmap, PDM methodology,
and triaxial core systematics across `131Ce` and `133Ce`.

Local archive locators:

- `raw/figures/gpt/learning-daily/20261101-day29-133ce-nuclearmap-pes/132Ce_Z058N074_pes.png`
- `raw/figures/gpt/learning-daily/20261101-day29-133ce-nuclearmap-pes/134Ce_Z058N076_pes.png`
- `raw/figures/gpt/learning-daily/20261101-day29-133ce-nuclearmap-pes/nuclearmap-theory.html`
- `raw/figures/gpt/learning-daily/20261101-day29-133ce-nuclearmap-pes/nuclearmap-obs.js`

The site exposes even-neutron entries around this chain but no direct
`133Ce` entry (`Z=58`, `N=75`) in the inspected JavaScript/PES route. A
single interpolated `γ` would discard the difference between the two core
surfaces and would not describe odd-particle polarization. Retain the two
surfaces as competing core priors, not a calculation or measurement of
odd-mass `133Ce`. The missing odd-neutron calculation is itself
a useful boundary: the odd particle must be coupled explicitly before using
the neighboring PES to classify a `133Ce` mode.

### Private-data observations

The two local intensity workbooks,
`raw/data/SouthAfrica/133Ce/analysis/intensity.xlsx` and
`raw/data/SouthAfrica/133Ce/analysis/intensity_iThemba2019_export.xlsx`, have
different archive SHA-256 values but identical sheet names, formulas and
cell-level cached values under the current `openpyxl` readout. They are
retained as distinct provenance artifacts rather than silently collapsed.
This supports arithmetic reproducibility while leaving workbook version and
producer identity open.

The workbook audit recomputes `65` ADO rows, `22` DCO rows and `44` asymmetry
rows. The selected derived matrices are readable `TH2I` objects with
`4096×4096` bins, but their event-to-matrix history and response covariance
remain unresolved.

The local `raw/data/SouthAfrica/133Ce/analysis/figure/wobbling frequency.xlsx`
contains a `133Ce` column in both sheets. Sheet 1 stores candidate derived
values `315`, `232.5`, `200.5`, `36`, `262`, `14` and `324.5` over the listed
spin entries; Sheet 2 stores candidate values beginning at `252`, `368`,
`209`, `399`, `492`, `378`, `606`, `331`. These are workbook-derived
quantities whose transition identity, uncertainty propagation and band
assignment must be reconstructed before they are called wobbling energies or
phonon spacings.

## Provisional Reasoning

### H0: near-axial core plus quasiparticle or signature dynamics

The neighboring `γ` values may reflect a rapid approach to an axial minimum,
and the apparent non-monotonic collective-energy pattern may instead arise
from signature splitting, configuration mixing, feeding or a tilted
precession branch.

### H1: triaxial core coupled to a collective wobbling excitation

The `133Ce` odd particle couples to a soft triaxial core. A credible version
of this hypothesis requires a joint description of excitation energies,
interband E2 strength, ADO, DCO, PDCO/linear polarization, branching ratios,
alignment and response nuisance parameters. A falling or alternating
workbook-derived sequence alone is insufficient.

The useful belief-revision observables are therefore the intersection of the
two hypotheses: transition identity and parity/signature, energy spacings,
same-parent branching ratios, interband E2 estimates, ADO/DCO, polarization,
and a model comparison in which triaxial PRM/TAC or equivalent calculations
are tested against signature-partner and tilted-precession alternatives.

## Falsification or Reverse Tests

1. Build a transition-identity ledger from `133Ce.gls`, `133Ce_w.gls`,
   `ce.lev`, the two intensity workbooks and the matrix/gate products.
2. Reconstruct the exact spin-to-energy mapping behind the two
   `wobbling frequency.xlsx` sheets, preserving formula cells and cached
   values separately.
3. Use `132Ce` and `134Ce` NuclearMap PES values as a neighboring-core prior,
   while explicitly marking the `133Ce` interpolation as provisional.
4. Fit or calculate only after the observable ledger is closed: compare
   near-axial/signature, tilted-precession and triaxial-wobbling hypotheses
   with shared calibration, efficiency, background and gate nuisances.
5. Reserve an untouched gate family or transition block as a holdout. If
   producer identity, response covariance or holdout data cannot be recovered,
   stop at partial-L4/readiness and do not manufacture a posterior.

## Failure Conditions

This note contains a local-data audit and a provisional research design. It
does not claim that `133Ce` has a measured triaxial minimum, a confirmed
wobbling phonon, or a reproduced event-level result. The NuclearMap entries
are neighboring even-even model outputs; the private workbook values are
derived analysis products; and the matrix files are structural inputs until
their producer and response lineage are closed.

## Assumptions

The two neighboring even-even PES are retained as alternative core inputs.
No interpolation is assumed to determine the odd-neutron configuration or
the finite-spin response of `133Ce`.

## Competing Explanations

The near-axial/signature and triaxial-wobbling hypotheses above must also be
compared with tilted precession, configuration mixing and gate-dependent
background effects. Neither a PES minimum nor an energy-spacing trend
selects a unique excitation mechanism.

## Transfer Conditions

Transfer the core calculation only after mapping the deformation convention,
quasiparticle configuration and spin range. Transfer private workbook values
only with their transition, gate, calibration and uncertainty provenance.

## Open Questions

- Which matrix export and gate set produced each intensity workbook row?
- Are the two workbook variants merely presentation versions of the same
  counts and formulas?
- How does a blocked odd-neutron calculation modify the neighboring-core PES?
- Which unused gate or transition can serve as an independent holdout?

## Human Review

This is a Codex self-audit and provisional research route. It remains
`unreviewed`; the private data and derived quantities have no publication
authorization from this note.

## Promotion or Rejection History

2026-11-01: registered the neighboring-core model route and private-data
audit; no measured shape, unique mode or event-level likelihood was promoted.
