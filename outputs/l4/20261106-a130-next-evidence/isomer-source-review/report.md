The \(^{137}\)Ba observation is **downward \(B(E2;(19/2^-)_1\rightarrow(15/2^-)_1)=0.46(3)\) W.u.**, from the 2349.9-keV isomer to the 2229.8-keV state. It is not the \(15/2^-\rightarrow11/2^-\) denominator. Vogt2017 Table III (accepted PDF p.14, printed p.13) identifies the isotope, direction, \(T_{1/2}=589(20)\) ns and strength; its caption states that the strength is already corrected for internal conversion. Fig.7/Section III B (PDF p.9) assigns the lifetime to the upstream isomer.

Use the **ordinary decay Weisskopf unit** requested in the protocol:
\[
W_d(E2)=\frac1{4\pi}\left(\frac35\right)^2
[1.2A^{1/3}]^4\,e^2\mathrm{fm}^4
=0.0594042641992\,A^{4/3}\,e^2\mathrm{fm}^4.
\]
Since \(1\,\mathrm b=100\,\mathrm{fm}^2\), \(1\,\mathrm b^2=10^4\,\mathrm{fm}^4\). At \(A=137\):

| Quantity | Value |
|---|---:|
| One ordinary downward E2 W.u. | \(41.9544833325\ e^2\mathrm{fm}^4\) |
| Same unit | \(0.00419544833325\ e^2\mathrm b^2\) |
| Reported downward strength | \(0.00192990623330\ e^2\mathrm b^2\) |
| Converted quoted margin only | \(0.00012586345000\ e^2\mathrm b^2\) |

Thus a compact display is **\((1.930\pm0.126)\times10^{-3}\ e^2\mathrm b^2\)**. This is a unit conversion, not a new uncertainty estimate. The source's 0.03-W.u. margin is carried through unchanged in meaning; no confidence level, model error, lifetime error or ICC error is added.

Two specific documentation issues are confirmed in the parent's archived HTML:

1. **B(E2) help, lines 60–70:** the general formula is explicitly introduced for downward transitions. The following prose specifies \(0^+\rightarrow2^+\), and its coefficient **0.297** is the rounded **fivefold special upward reference**. However, line 70 prints a downward arrow. The coefficient agrees with the surrounding upward context; the arrow is inconsistent. This does not justify using \(0.297A^{4/3}\) for the present \(19/2\rightarrow15/2\) decay.
2. **Gamma-emission help, lines 178–192:** the page calls \(T_\gamma\) a partial half-life and then prints \(B\) in W.u. as \(T_\gamma/T_W\). At fixed energy and multipolarity, the radiative rate is proportional to \(B\), so matched partial-photon half-lives require
   \[
   \frac{B}{B_W}=\frac{\lambda_\gamma}{\lambda_{\gamma,W}}
   =\frac{T_{\gamma,W}}{T_\gamma}.
   \]
   The printed reciprocal is a hindrance ratio under those definitions. An \(\alpha=0\), single-branch example already proves the reversal, independently of any intensity/ICC ambiguity.

The independent textbook check is Bohr and Mottelson, *Nuclear Structure I*, printed p.382 / local PDF p.401, Eqs. (3C-16)–(3C-18): the radiative rate is proportional to \(E_\gamma^{2\lambda+1}B\), with the RME normalization \(1/(2J_i+1)\). The book's \(T(E2)\) denotes a **rate per second**, not a half-life. Only these relevant definitions were checked; this is not a general rejection of NNDC documentation or data.

For this isomer comparison,
\[
B_\downarrow=\frac{|\langle15/2\|T(E2)\|19/2\rangle|^2}{20},
\qquad
B_\uparrow(15/2\rightarrow19/2)=\frac{20}{16}B_\downarrow.
\]
The physical reverse factor is **1.25**, not 5. The factor 5 in the B(E2) help belongs to its \(0^+\leftrightarrow2^+\) application; scaling both the upward strength and its special reference by five leaves their dimensionless ratio unchanged. An already normalized model \(B_\downarrow\) should be compared directly with the converted datum, without another division by 20.

No strength was derived from the 589-ns level half-life or an assumed \(\alpha\). Radiative partial times cannot simply be replaced by total level times when conversion or branching matters. \(T_{1/2}\) and mean lifetime also require consistent definitions. The measured lifetime and the strength derived from it form **one linked decay-evidence group**, not two independent likelihood terms.

Artifacts: [unit-audit.json](unit-audit.json), the single-observation [CSV](observed-strength.csv), and [check_units.py](check_units.py). The script checks the archived expressions, ordinary/special unit factors, SI area conversion, exact detailed-balance factors, four abstract lifetime-ratio controls, and input hashes. It imports no model, performs no solve/refit, and leaves the parent's primary/energy-only state mapping unchanged.

Durable delta: [nndc-e2-weisskopf-direction-and-lifetime-ratio.md](/workspace/wiki/knowledge/sources/nndc-e2-weisskopf-direction-and-lifetime-ratio.md). Raw help provenance remains in the parent's `raw/papers/gpt/query/20261106-ba137-isomer-validation/manifest.json`; no raw file was changed.
