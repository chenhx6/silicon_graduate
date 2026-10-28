# E3 sum-rule and localization unit 027

## Source acquisition

Butler *et al.*, “Evolution of Octupole Deformation in Radium Nuclei from Coulomb Excitation of Radioactive `222Ra` and `228Ra` Beams,” *Phys. Rev. Lett.* **124**, 042503 (2020), DOI `10.1103/PhysRevLett.124.042503`.

- Published APS harvest PDF: 6 pages, `%PDF-1.4`, SHA-256 `c0f8646afcd78d8647a7011046c036aa7c8ae7969839f72151646464a43b1502`.
- arXiv `2001.09681` PDF: 16 pages, read through page 16; pages 7–16 append level schemes, fitted yields, E2 systematics and E1 Table II. The browser-dependent downloader attempt failed before retrieval; these files came from public APS harvest/arXiv endpoints.
- APS PRL PDF p.3 Table I is the primary E3 locator. Higher entries marked `*` were coupled through rotational assumptions and are not fully independent.

## Physics result

For a complete set of negative-parity `3−` states from a `0+` initial state,

\[
m_0(E3)=\sum_f B(E3;0^+\to3^-_f)=\sum_\mu\langle0^+|M_{3\mu}^\dagger M_{3\mu}|0^+\rangle .
\]

A single measured `0+→3−` line is one nonnegative term and therefore supplies a lower bound on this non-energy-weighted sum. It does not complete the sum over unobserved `3−` states. The energy-weighted sum requires

\[
m_1=\frac12\sum_\mu\langle0^+|[M_{3\mu}^\dagger,[H,M_{3\mu}]]|0^+\rangle,
\]

so it cannot be recovered from Table I alone.

## Numerical partial sums

The script squares the printed central E3 reduced matrix elements in `e b^(3/2)` and reports partial sums only:

| isotope | all listed rows | unstarred rows | listed downward B proxy |
|---|---:|---:|---:|
| `222Ra` | `30.9635` | `6.0135` | `4.99644` |
| `228Ra` | `5.6942` | `0.7569` | `1.73014` |

The sums mix different initial spins and are not a closure-complete `m0`; they are arithmetic diagnostics. The data pattern is more informative than the totals: `222Ra` has several nonzero Q3 conversions, while `228Ra` has a near-zero `2+→3−` entry (`−0.06(+0.23/−0.16)*`) despite a nonzero `0+→3−` (`0.87(15)`).

## Identifiability boundary

Multiple E3 links and approximate Q3 constancy provide a rotor-like consistency test. They still depend on phase conventions, GOSIA couplings, pairing, unobserved states and the rotor conversion from a matrix element to Q3. Butler *et al.* interpret the pattern as stable octupole deformation in `222Ra` and octupole-vibrator behavior in `228Ra` (PRL pp.1, 4–5); the paper also retains rotationally aligned octupole phonons as an alternative that does not require a permanent octupole distortion.

`144,146Ba` direct Coulomb excitation establishes strong single `0+↔3−` E3 strengths, while Gaffney 2013 and Butler 2020 supply richer multi-transition patterns in the Ra region. A model-independent static density or energy-weighted sum needs additional high-lying `3−` strength, excitation energies, relative phases and covariance.

## Reproducibility

Run:

```bash
python3 octupole-sum-rule-and-localization-027.py
```

The generated JSON records the input rows, partial sums, validation flags and explicit closure limitations.
