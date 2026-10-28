# E3 direction and degeneracy audit 035

## Input

Only Butler 2020 PRL 124 042503 Table I central E3 values already recorded in 029/032 were used. Matrix elements are in (e,b^{3/2}), so squared values are (e^2b^3). No new fit or W.u. conversion was performed.

## Rule

For a transition with initial spin (J_i),

\[
B(E3;J_i\to J_f)=\frac{|M|^2}{2J_i+1}.
\]

Hermiticity gives the same reduced-matrix-element magnitude in the reverse direction, but

\[
\frac{B(J_i\to J_f)}{B(J_f\to J_i)}=\frac{2J_f+1}{2J_i+1}.
\]

Thus a printed `0+→3−` central matrix element gives (B_{0\to3}=|M|^2) and (B_{3\to0}=|M|^2/7). The direction labels here follow Butler's printed transition notation; they are not a claim that the table's bra-ket typography independently establishes an experimental decay direction.

## Selected numerical checks

| Nucleus / printed row | (|M|^2) | (B) printed direction | (B) reversed direction | Ratio |
|---|---:|---:|---:|---:|
| `222Ra 0+→3−` | `1.2769` | `1.2769` | `0.182414` | `7.0` |
| `222Ra 2+→1−` | `0.7225` | `0.1445` | `0.240833` | `0.6` |
| `222Ra 2+→3−` | `0.81` | `0.162` | `0.115714` | `1.4` |
| `222Ra 4+→7−`* | `10.89` | `1.21` | `0.726` | `1.667` |
| `228Ra 0+→3−` | `0.7569` | `0.7569` | `0.108129` | `7.0` |
| `228Ra 2+→3−`* | `0.0036` | `0.000720` | `0.000514` | `1.4` |

The full machine-readable table includes every central E3 row from 222Ra and 228Ra in Table I. Asterisks retain Butler's fit-coupling status: they are not independent measurements and should not be treated as independent draws in a statistical sum.

## Closure guard

The (0^+) non-energy-weighted closure sum is (sum_fB(E3;0^+\to3^-_f)). Only rows with (J_i=0) belong to that particular sum; rows beginning at (2^+) or (4^+) belong to different initial-state sums. The table therefore must not be summed across all (J_i) to create a closure strength. No energy-weighted sum was computed.

## Limits

These are conditional B values from printed central matrix elements. They do not restore GOSIA covariance, resolve table-direction conventions beyond the stated printed arrows, or convert the coupled entries into independent data. The `228Ra 2+→3−` central value remains a near-zero fit result with an interval crossing zero, as recorded in 032.
