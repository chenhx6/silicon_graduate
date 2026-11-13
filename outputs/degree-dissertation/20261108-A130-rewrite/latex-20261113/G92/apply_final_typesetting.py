# -*- coding: utf-8 -*-
import os

proj_root = "tmp/a130-release-29-20261113/project"

# 1. sec-3-7.tex
p_37 = os.path.join(proj_root, "Tex/Sections/sec-3-7.tex")
with open(p_37, "r", encoding="utf-8") as f:
    text_37 = f.read()

old_37 = r"""\item 空间反射对称性破缺：由正负八极形变核态 $|\Phi(+\beta_3)\rangle$ 与 $|\Phi(-\beta_3)\rangle = \hat{\Pi} |\Phi(+\beta_3)\rangle$ 关联；
\item 手征转动对称性破缺：由左手三面角取向态 $|L\rangle$ 与右手三面角取向态 $|R\rangle = \mathcal{C} |L\rangle$ 关联，其中标准手征反转算符定义为 $\mathcal{C} \equiv \mathcal{T} \mathcal{R}_y(\pi)$。"""

new_37 = r"""\item 空间反射对称性破缺：由正负八极形变态 $|\Phi(+\beta_3)\rangle$ 与反演态 $|\Phi(-\beta_3)\rangle = \hat{\Pi} |\Phi(+\beta_3)\rangle$ 关联；
\item 手征转动对称性破缺：由左手三面角态 $|L\rangle$ 与右手态 $|R\rangle = \mathcal{C} |L\rangle$ 关联，标准手征算符为 $\mathcal{C} \equiv \mathcal{T} \mathcal{R}_y(\pi)$。"""

assert old_37 in text_37, "old_37 not found"
text_37 = text_37.replace(old_37, new_37)
with open(p_37, "w", encoding="utf-8") as f:
    f.write(text_37)
print("Updated sec-3-7.tex")

# 2. sec-4-5.tex
p_45 = os.path.join(proj_root, "Tex/Sections/sec-4-5.tex")
with open(p_45, "r", encoding="utf-8") as f:
    text_45 = f.read()

old_45 = r"\begin{tabularx}{\textwidth}{p{2.1cm}p{1.7cm}p{2.3cm}p{2.6cm}X}"
new_45 = r"\begin{tabularx}{\textwidth}{p{2.1cm}p{1.7cm}p{2.0cm}p{2.9cm}X}"

assert old_45 in text_45, "old_45 not found"
text_45 = text_45.replace(old_45, new_45)
with open(p_45, "w", encoding="utf-8") as f:
    f.write(text_45)
print("Updated sec-4-5.tex")

# 3. AppendixA.tex
p_appA = os.path.join(proj_root, "Tex/Appendices/AppendixA.tex")
with open(p_appA, "r", encoding="utf-8") as f:
    text_appA = f.read()

old_appA = r"""\begin{align}\label{eq:appA-rational-verification}
\sum_{x=1}^3 (2x + 1) \begin{Bmatrix} 1 & 2 & x \\ 1 & 2 & 2 \end{Bmatrix}^2 &= (2\times 1 + 1) \left(-\frac{1}{10}\right)^2 + (2\times 2 + 1) \left(\frac{1}{6}\right)^2 + (2\times 3 + 1) \left(\frac{1}{15}\right)^2 \notag \\
&= 3 \times \frac{1}{100} + 5 \times \frac{1}{36} + 7 \times \frac{1}{225} \notag \\
&= \frac{3}{100} + \frac{5}{36} + \frac{7}{225} .
\end{align}"""

new_appA = r"""\begin{align}\label{eq:appA-rational-verification}
\sum_{x=1}^3 (2x + 1) \begin{Bmatrix} 1 & 2 & x \\ 1 & 2 & 2 \end{Bmatrix}^2
&= (2\times 1 + 1) \left(-\frac{1}{10}\right)^2 + (2\times 2 + 1) \left(\frac{1}{6}\right)^2 \notag \\
&\quad + (2\times 3 + 1) \left(\frac{1}{15}\right)^2 \notag \\
&= 3 \times \frac{1}{100} + 5 \times \frac{1}{36} + 7 \times \frac{1}{225} \notag \\
&= \frac{3}{100} + \frac{5}{36} + \frac{7}{225} .
\end{align}"""

assert old_appA in text_appA, "old_appA not found"
text_appA = text_appA.replace(old_appA, new_appA)
with open(p_appA, "w", encoding="utf-8") as f:
    f.write(text_appA)
print("Updated AppendixA.tex")
