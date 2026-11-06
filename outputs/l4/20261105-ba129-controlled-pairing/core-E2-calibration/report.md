# Even-Ba first-2+ E2 calibration inputs

The five selected \(B(E2;2_1^+\rightarrow0_1^+)\) central values are
**0.2765251611, 0.2326, 0.1720, 0.1358, 0.0814 \(e^2b^2\)** for
\(^{128,130,132,134,136}\)Ba, respectively.

The numerical deliverables are [ba-core-E2.csv](ba-core-E2.csv) and
[ba-core-E2.json](ba-core-E2.json). The JSON is authoritative for literal source
tokens, full locators, direction, error meaning, dependency and alternatives.
[alternatives.csv](alternatives.csv) retains 23 method/component/branch records,
all excluded from the baseline calibration. No model fit or confidence interval
was produced.

The existing128/130 originals were reused without downloading them again.
New132/134/136 records came from official NNDC ENSDF interfaces, including adopted
PDFs and Coulomb-excitation summaries. The task label is November6,2026; acquisition
and creation timestamps retain the actual measured UTC clock, rather than
inheriting a date from the directory label.

## Selected strengths and quoted margins

In this report, ↑ means \(0_1^+\rightarrow2_1^+\), and ↓ means
\(2_1^+\rightarrow0_1^+\). All absolute strengths below are in \(e^2b^2\).
Parentheses retain the source's last-digit uncertainty convention; the converted
margins are not assigned a new confidence level or an error distribution.

| Nucleus | Selected source input | \(B(E2)\uparrow\) | \(B(E2)\downarrow\) | Margin interpretation |
|---|---|---:|---:|---|
| 128Ba | \(T_{1/2}=105(9)\) ps, with actual gamma energy and ICC | 1.3826258057, derived | 0.2765251611, derived | T-only first-order contribution: 0.0237021567 downward; full uncertainty remains unspecified |
| 130Ba | Adopted Coulomb \(B(E2)\uparrow=1.163(11)\) | 1.163(11) | 0.2326, quoted margin0.0022 | Source margin divided by5 |
| 132Ba | Adopted Coulomb \(B(E2)\uparrow=0.86(6)\) | 0.86(6) | 0.1720, quoted margin0.0120 | Source margin divided by5 |
| 134Ba | Adopted comment/Coulomb \(B(E2)\uparrow=0.679(11)\) | 0.679(11) | 0.1358, quoted margin0.0022 | Source margin divided by5 |
| 136Ba | Adopted Coulomb \(B(E2)\uparrow=0.407(7)\) | 0.407(7) | 0.0814, quoted margin0.0014 | Source margin divided by5 |

The upward arrow was checked in the rendered adopted PDFs for130/132/136Ba,
all on PDFp.1. For134Ba, the adopted lifetime comment does not print an arrow;
the separately requested official
[Coulomb PDF](/workspace/wiki/raw/papers/gpt/query/20261106-ba-core-E2-calibration/nndc134-coulomb.pdf),
p.1, explicitly prints \(B(E2)\uparrow=0.679(11)\).

128Ba has a reported downward `BE2W=72 7` in its decay table, rather than an
explicit absolute Coulomb Bup. That rounded W.u. quantity is retained in the
JSON but not counted again or used to introduce a separate radius convention.
The selected absolute value uses the parent/task-declared rate coefficient.

## First-state identity, gamma branch and ICC

Each selected level is the lowest unambiguous \(2^+\) level in the adopted file.
The ground state is0+, and the first-state block contains exactly one listed
gamma transition, pure E2 to the ground state. This source-specific branch
selection excludes the higher \(2^+\) levels at884.50,908.02,1031.672,1167.968
and1550.987keV.

| Nucleus | Adopted \(E_x(2_1^+)\), keV | Actual \(E_\gamma\), keV | Adopted \(T_{1/2}\), ps | Total ICC \(\alpha\) | Listed branch |
|---|---:|---:|---:|---:|---|
| 128Ba | 284.00(8) | **284.10(8)** | 105(9) | 0.0539 | E2, relative \(I_\gamma=100\), to0+ |
| 130Ba | 357.38(8) | 357.4(1) | 41.8(12) | 0.0262 | E2, relative \(I_\gamma=100\), to0+ |
| 132Ba | 464.508(12) | 464.52(3) | 15.1(11) | 0.0121 | E2, relative \(I_\gamma=100\), to0+ |
| 134Ba | 604.7223(19) | 604.721(2) | 5.12(9) | 0.00599 | E2, relative \(I_\gamma=100\), to0+ |
| 136Ba | 818.522(10) | 818.514(12) | 1.89(3) | 0.00283 | E2, relative \(I_\gamma=100\), to0+ |

The total ICC fields have no explicit quoted uncertainty. They remain
`quoted_margin: null`, not zero-error measurements. Subshell ICC errors, where
printed, were not silently summed into a total-ICC uncertainty.
Relative intensity100 is the source normalization, not an additional100-count
measurement or an inferred statistical error.

The small differences between fitted level energy and gamma energy are retained.
In particular, substituting284.00 for284.10keV would change the128Ba rate
conversion. Rounded Coulomb labels such as465,605 or819keV identify the same
first2+ states but do not replace the adopted gamma energies.

## Declared conversion

The parent/task-declared electric-quadrupole rate convention is

\[
\lambda_\gamma(E2)
=C_{E2}\,[E_\gamma(\mathrm{MeV})]^5
 B(E2;2_1^+\rightarrow0_1^+),\qquad C_{E2}=1.2239\times10^{13},
\]

with \(\lambda_\gamma\) in s\(^{-1}\) and B in \(e^2b^2\).
For the single listed E2 transition, including its conversion electrons,

\[
B(E2)\downarrow
=\frac{\ln2}
 {T_{1/2}(\mathrm{s})\,C_{E2}\,[E_\gamma(\mathrm{MeV})]^5(1+\alpha)}.
\]

For multiple pure-E2 branches the photon factor would instead be
\(I_{\gamma,j}/\sum_k I_{\gamma,k}(1+\alpha_k)\); this task does not replace
missing ICCs with zero or apply a single-branch formula to a multibranch level.

Detailed balance fixes

\[
(2J_i+1)B(i\rightarrow f)=(2J_f+1)B(f\rightarrow i),
\qquad B(E2)\uparrow=5B(E2)\downarrow.
\]

128Ba therefore gives0.276525161133\(e^2b^2\). Its propagated T-only
first-order margin is \(B_\downarrow(9/105)=0.023702156669\).
The separate first-order gamma-energy contribution is
\(5B_\downarrow(0.08/284.10)=0.000389334968\).
Neither is a complete uncertainty budget: ICC uncertainty, the coefficient's
uncertainty, and source covariances have not been supplied. No confidence
interval or Gaussian likelihood is inferred from these contributions.

## Exact source locators and versions

The first-state level/strength table is PDFp.1 in every adopted PDF.
The first-state gamma table is at PDFp.5,3,6,5,7 for128,130,132,134,136Ba.
Line numbers refer to the exact UTF-8 text extracted from the sole HTML pre.

| Nucleus | Adopted dataset / record stamp | Literature cutoff; evaluation | ENSDF first-state locators | Coulomb dataset / selected Bup locator |
|---|---|---|---|---|
| 128Ba | 128056001 / 201510 | 28-Feb-2015; Elekes & Timar, NDS129,191(2015) | L48; gammaL51; W.u.L52; lifetime methodL17–18 | Not needed for selected conversion |
| 130Ba | 130056001 / 200107 | 11-May-2001; Singh, NDS93,33(2001) | L43; BupL46; lifetime dependencyL55–56; gammaL58 | 130056007; BupL18; interference choicesL20–22 |
| 132Ba | 132056001 / 200504 | 10-Feb-2005; Khazov et al., NDS104,497(2005) | L75; BupL77; T-from-BL81; gammaL82 | 132056010; BupL13; sign alternativesL15–17 |
| 134Ba | 134056001 / 200410 | 31-Jul-2004; Sonzogni, NDS103,1(2004) | L25; source BL29; gammaL31 | 134056008; BupL15; componentsL17–19; T-from-BL24 |
| 136Ba | 136056001 / 201810 | 1-Apr-2018; McCutchan, NDS152,331(2018) | L51; BupL53; T-from-BL55; gammaL62 | 136056012; BupL47; alternate TL49; B alternativesL50–54 |

Canonical source files:

- [128 adopted ENSDF](/workspace/wiki/raw/papers/gpt/query/20261105-ba129-core-constraints/nndc128-adopted-text.ens:48).
- [130 adopted ENSDF](/workspace/wiki/raw/papers/gpt/query/20261105-ba129-core-constraints/nndc130-adopted-text.ens:43)
  and [130 Coulomb summary](/workspace/wiki/raw/papers/gpt/query/20261105-ba129-core-constraints/nndc130-coulomb-text.ens:18).
- [132 adopted ENSDF](/workspace/wiki/raw/papers/gpt/query/20261106-ba-core-E2-calibration/nndc132-adopted-text.ens:75)
  and [132 Coulomb summary](/workspace/wiki/raw/papers/gpt/query/20261106-ba-core-E2-calibration/nndc132-coulomb-text.ens:13).
- [134 adopted ENSDF](/workspace/wiki/raw/papers/gpt/query/20261106-ba-core-E2-calibration/nndc134-adopted-text.ens:25)
  and [134 Coulomb summary](/workspace/wiki/raw/papers/gpt/query/20261106-ba-core-E2-calibration/nndc134-coulomb-text.ens:15).
- [136 adopted ENSDF](/workspace/wiki/raw/papers/gpt/query/20261106-ba-core-E2-calibration/nndc136-adopted-text.ens:51)
  and [136 Coulomb summary](/workspace/wiki/raw/papers/gpt/query/20261106-ba-core-E2-calibration/nndc136-coulomb-text.ens:47).

Record stamps, evaluation cutoffs and retrieval times are separate fields.
These are snapshots of the evaluations served by NNDC; a2026 retrieval does
not turn a2001/2004/2005/2015/2018 evaluation into a new measurement.
Later mass-Q references in some files do not change the stated spectroscopy
literature cutoff.

## Alternatives and source dependence

The adopted centers were preserved as printed. Components were not re-averaged,
and their quoted errors were not used to choose a preferred interference sign.

| Isotope | Preserved alternative or method detail | Source IDs / treatment |
|---|---|---|
| 128Ba | General lifetime attribution: RDDS2000Pe20/2000Pe19 or DSA1998Pe17. No row-specific decomposition is printed in the adopted first2+ block. | Keep the general-source scope; do not invent separate measurements behind105(9)ps. |
| 130Ba | Bup1.167(11), constructive;1.159(12), destructive. Bdown0.2334 with margin0.0022, or0.2318 with margin0.0024. Older1.21(38),1.36(14),0.75(18) also retained. | 1989Bu07 branches;1973ToXW,1967Si03,1958Fa01 older values. |
| 130Ba | Adopted T41.8(12)ps combines43.2(5)ps RDDS and40.7(4)ps derived from Coulomb Bup. | 2000St07 recorded only from the existing summary; no Stuch access retry. T and selected Bup are dependent. |
| 132Ba | Bup0.821(16) for negative product of four matrix elements;0.897(16) for positive product. Downward values0.1642 and0.1794, each with margin0.0032. Older0.73(18) retained. | 1985Bu01 sign alternatives;2001Ra27 recommendation0.86(6);1958Fa01 older value. |
| 134Ba | Listed components0.672(16),0.700(15),0.665(5); adopted0.679(11) retained literally. | 1972Ke16,1977Kl05,1989Bu07. No new weighted average calculated. |
| 136Ba | Adopted0.407(7) cites components0.399(3),0.419(4),0.418(11). Other inverse-kinematics value0.46(4) retained. | 1984Be20,1986Ro15,1972Ke16;2002Ra21. |
| 136Ba | Destructive0.417(4) accompanies the1986 lineage;0.388(10)/0.400(10) are constructive/destructive with the source's \(Q=-0.19(17)\) assumption;1972 gives0.418(11)/0.417(12). Older0.53(16) retained. | 1986BaZJ/1986Ro15,1985Bu01,1972Ke16,1963Al31. The repeated0.418(11) entry is counted once in alternatives. |
| 136Ba | Other \(T_{1/2}=2.2(3)\)ps from DSAM, distinct from the evaluator's B-derived1.89(3)ps. | 1973Fi15; retained as an unselected method alternative. |

For132/134/136Ba, the first-state lifetime explicitly comes from B(E2).
For134/136Ba this overrides the file's general neutron-inelastic/DSAM lifetime
provenance. For130Ba the adopted T includes the Coulomb B-derived result.
The dataset therefore contains one selected strength per isotope, with T,
the reverse-direction B and decay-table W.u. values in the same dependency block.
The23 alternative records are not23 additional calibration points.

“Independent even-core input” here means separate from fitting the odd129Ba
observables. It does not certify statistical independence across the five
isotopes:1989Bu07 occurs in130/134Ba, and1972Ke16 occurs in134/136Ba. No numerical
cross-isotope covariance was provided by the summaries.

## Retrieval, reproducibility and checks

[fetch_nndc.py](fetch_nndc.py) selects the actual adopted or Coulomb dataset ID
from each archived official index before issuing a POST. The text request uses:

```text
dbclass=ensdf
page-source=singular
chooseit=ENSDF text format
datasetcheck=<verified dataset ID>,<mass>BA
```

Every HTTP response body is kept intact. A separate `*-text.ens` file contains
the exact decoded text of the sole pre element, without stripping, reflowing or
normalizing record whitespace. `derived_from_sha256` binds it to the wire HTML.
The134Ba Coulomb PDF uses the site's actual `PDF Version` option.

The archive [manifest](/workspace/wiki/raw/papers/gpt/query/20261106-ba-core-E2-calibration/manifest.json)
records root-relative paths, actual retrieval UTC, size, SHA-256, request method
and parameters, access boundaries and evaluation metadata. Reused128/130 inputs
are identified separately with their earlier acquisition records.

Offline rebuild:

```bash
python3 -B outputs/l4/20261105-ba129-controlled-pairing/core-E2-calibration/build_calibration.py
```

The builder verifies input hashes and exact single-pre extraction, selects the
lowest definite2+ state, requires one listed E2 gamma to0+, retains the actual
gamma energy and nonzero ICC, and checks the five central values. Rendered
level/gamma tables and direction arrows were also inspected. Results are recorded
in `checks.json`; these checks validate extraction and arithmetic, not a new
experimental confidence level or an IBFM prediction.

Only the requested raw collection and output subtree were written. No existing
128/130 raw file, PLAN, other-session file, configuration or Git index/history
was changed. No primary paper was downloaded, no Stuch route was retried, and
the get-paper skill was not inspected or used.
