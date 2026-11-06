Neither experimental \(R_{\rm stat}^{(1)}\) is determined by the bounded source set. The superscript denotes the first \(15/2^-\) target, rather than a sum over the entire \(J+2\) channel. \(^{135}\)Ba has a tentative target transition but no parent lifetime/absolute strength; \(^{137}\)Ba lacks an assigned \(15/2^-\) target in both checked datasets. This extension creates new files and preserves the static-v1 results, source constraints, CSVs and report byte-for-byte.

| Nucleus | Target mapping | Available information | Missing for this ratio |
|---|---|---|---|
| \(^{135}\)Ba | Adopted \(950.5(3)\)-keV \((15/2^-)\rightarrow268.218(20)\)-keV \(11/2^-_1\) | 682.3-keV photon, RI=100, multipolarity field `Q`; originating reaction gives DCO=1.18(3) | Parent \(T_{1/2}\), ICC, absolute E2 strength, justified branch/purity completeness; retain tentative adopted assignment |
| \(^{137}\)Ba | No assigned \(15/2\) level in the adopted or \((\alpha,3n\gamma)\) object | Static \(11/2^-_1\) moment and other transitions exist | Validated lowest-\(15/2^-\) identity and its absolute E2 transition to \(11/2^-_1\) |

For \(^{135}\)Ba, adopted ENSDF lines **202–206** retain the spin in parentheses; its general comment at **51–54** identifies the assignment as proposed from DCO/systematics. The reaction record, dataset **135056005**, lines **53–57**, prints \(15/2^-\) without parentheses and supplies the DCO, but no lifetime. Its RI/DCO lineage includes **2007ChZZ**, a private communication, alongside **2006Ch51** and **1987Dr13** (reaction lines 6–25; archived reference record). Preserve the adopted qualification. The older reaction reports 682.7 keV separately. RI=100 is a relative photon normalization, not an absolute decay rate or proof of unit total branch. Blank ICC is not zero. With the tentative same-parity assignment accepted, quadrupole order is consistent with E2; the literal evaluated field remains `Q`.

The **28.7-hour** lifetime belongs to the daughter \(11/2^-\) isomer. It cannot be used as the lifetime of the emitting \(15/2^-\) parent. The listed excitation-energy closure differs by only 0.018 keV, so the candidate connection itself is coherent at the quoted precision.

For \(^{137}\)Ba, a \(2047.4\)-keV **unassigned** level feeds the 661.659-keV \(11/2^-\) isomer through 1385.7 keV (adopted **147–150**). The originating dataset **137056005** gives the parent as 2047.2 keV and lists a \(T_{1/2}<10\) ns timing bound for this line in its general comment (**7**, **25–26**). Neither spin nor multipolarity identifies it as the requested \(15/2^-\) E2 transition. This bound cannot become a measured absolute \(B(E2)\) or a unique level assignment.

The measured \(0.59(10)\,\mu\mathrm{s}\) E2 decay instead belongs to
\[
2349.1\;(17/2^-)\xrightarrow{120.2}
2229.5\;(13/2^-),
\]
with \(\alpha_{\rm tot}=1.004(17)\) and evaluated \(B(E2)=0.45(8)\) W.u. (adopted **192–200**). It is a different spin pair. The \(7/2^-\rightarrow11/2^-\) E2 at adopted **106–111** is likewise outside the requested \(J+2\) channel. Neither may be substituted. The 2.552-minute \(11/2^-\) isomer lifetime also belongs to the wrong parent.

The normalization is
\[
S_{\rm stat}=\frac{|R_{11/2,11/2}|^2}{12}
=\frac{91}{176\pi}Q_s^2,\qquad
B_\uparrow(11/2\rightarrow15/2)=\frac{16}{12}
B_\downarrow(15/2\rightarrow11/2),
\]
\[
R_{\rm stat}^{(1)}=\frac{273}{704\pi}\frac{Q_s^2}{B_\downarrow}.
\]
Here \(Q_s\) is in e b and \(B(E2)\) in \(e^2b^2\). A lifetime extraction requires the **emitting parent half-life**, \(\ln2/T_{1/2}\), the E2 photon fraction, \(E_\gamma^5\), and conversion-corrected complete branch accounting. It cannot be obtained from a relative peak area alone. Squaring \(Q_s\) also removes its sign, so keep the signed static comparison separately.

The parent CSV gives model \(R_{\rm stat}^{(1)}=2.2722073553\) and **1.3565277480** for 135 and 137. Its implied model \(B_\downarrow\) values are **0.0752477701** and **0.0543661664 \(e^2b^2\)**. These are model outputs, not recovered measurements. All experimental denominator/ratio fields remain null in [rstat-readiness.json](rstat-readiness.json) and [CSV](rstat-readiness.csv); the ratio columns are explicitly named `model_Rstat_first` and `experimental_Rstat_first`.

The static verdict remains: \(^{135}\)Ba overpredicts the paper/adopted central moment; \(^{137}\)Ba agrees with a source-named \(e_F\) calibration anchor. A future measured transition denominator could add EM information, but the 137 static numerator remains calibration-linked. No energy agreement, weak-coupling core estimate, or model denominator can replace that measurement.

[check_rstat_availability.py](check_rstat_availability.py) checked the CG coefficient, \(16/12\) reversal, parent-CSV reconstruction, source fields and static-v1 hashes; exit code 0. Only the two originating reaction datasets were newly fetched, into `raw/papers/gpt/query/20261106-ba-rstat-readiness/`. This is a bounded availability result, not a claim that no relevant measurement exists anywhere.
