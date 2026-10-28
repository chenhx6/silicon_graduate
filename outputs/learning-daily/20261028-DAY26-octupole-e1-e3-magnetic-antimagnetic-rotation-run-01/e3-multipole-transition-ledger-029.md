# E3 multipole transition ledger 029

## Scope

This ledger reconciles E3 reduced matrix elements, units, intrinsic (Q_3) conversions and rotational coupling labels for the archived `144,146Ba`, `220Rn`, `224Ra`, `222Ra` and `228Ra` sources. It does not download new literature, construct a closure complete sum rule or compute an energy weighted sum.

## Unit and direction audit

For Butler/Bucher, the E3 reduced matrix element is printed in (e,b^{3/2}); (1,b^{3/2}=1000,mathrm{fm}^3). Gaffney prints E3 matrix elements in (e,mathrm{fm}^3). The transition probability convention is

\[
B(E\lambda;J_i\to J_f)=\frac{|\langle J_f\Vert M(E\lambda)\Vert J_i\rangle|^2}{2J_i+1}.
\]

The table row direction must be read from each source before applying the denominator. In particular, the 027 script's `partial_sum_downward_B_eb3` uses the first listed spin and is only an illustrative proxy; it is not a certified B sum. Its raw square sums, `30.9635` for `222Ra` and `5.6942` for `228Ra`, mix rows with different initial spins and cannot be interpreted as (m_0(0^+)).

## Cross nucleus ledger

| Nucleus | E3 matrix element | (Q_3) | B(E3) or status | Locator |
|---|---|---|---|---|
| `144Ba` | `0.65(+0.17/−0.23) e b^(3/2)` | `1.73(+0.45/−0.62)×10^3 e fm^3` | `48(+25/−34) W.u.` downward | Bucher 2016 PDF p.4 Table I/text |
| `146Ba` | `0.65(+0.14/−0.20) e b^(3/2)` | not independently reused here | `48(+21/−29) W.u.` downward | Bucher 2017 PDF p.3 Table I/text |
| `220Rn` | `810(50) e fm^3` | `2180(130) e fm^3` | `33(4) W.u.` | Gaffney 2013 PDF p.3 Table 1; p.4 Table 2 |
| `224Ra` | `940(30) e fm^3` | `2520(90) e fm^3` | `42(3) W.u.` | Gaffney 2013 PDF p.3 Table 1; p.4 Table 2 |
| `222Ra` | `1.13(9) e b^(3/2)` | `3030(240)` per transition; `3120(190)` rotor aggregate | direction-specific B not recomputed | Butler 2020 PDF p.3 Table I |
| `228Ra` | `0.87(15) e b^(3/2)` | `2300(400)` per transition; `2230(290)` rotor aggregate | direction-specific B not recomputed | Butler 2020 PDF p.3 Table I |

Butler's starred entries are fit-coupled through rotational relations and are not fully independent. In `222Ra`, the unstarred central E3 rows are `1.13, 0.85, −0.90, 1.79`; starred rows include `−2.10, 2.60, −1.70, 3.30`. In `228Ra`, `0.87` is unstarred while `1.36, −0.06, 1.71, 0.40` are starred. The `228Ra 2+→3−` near-zero entry is a pattern observation with a large uncertainty, not an exact zero.

## Sum-rule boundary

For a (0^+) initial state, the non-energy weighted E3 closure sum is

\[
m_0=\sum_f B(E3;0^+\to3^-_f).
\]

One measured `0+→3−` line is one nonnegative term and therefore supplies a lower bound if the transition convention is fixed. Matrix elements beginning from `2+` or `4+` belong to different closure sums and cannot be added to the (0^+) sum. The energy weighted sum requires (H) through a double commutator and is not computed here.

## Evidence gradient

`144,146Ba` establish strong direct single E3 strengths. Gaffney's `220Rn/224Ra` and Butler's `222Ra/228Ra` multi-transition networks add a pattern test: approximately constant rotor-converted (Q_3) values support a static-like interpretation, while selected near-zero links in `228Ra` support the author's vibrator interpretation. Neither pattern is a model-independent density reconstruction; couplings, phases, pairing, unobserved states and rotor conversion remain relevant.

## Reproducibility and limits

The machine-readable ledger is `e3-multipole-transition-ledger-029.json`. Source pages retain their own locators and `needs_review` flags. No energy weighted quantity, closure fraction, posterior shape probability or complete covariance was generated.
