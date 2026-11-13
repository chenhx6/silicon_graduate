# -*- coding: utf-8 -*-
import os

proj_root = "tmp/a130-release-29-20261113/project"

# 1. Update sec-4-5.tex: replace \makecell with built-in \shortstack[l]
p_45 = os.path.join(proj_root, "Tex/Sections/sec-4-5.tex")
with open(p_45, "r", encoding="utf-8") as f:
    text_45 = f.read()

text_45 = text_45.replace(
    r"\makecell[l]{$^{70}\mathrm{Zn}$\\$(^{12}\mathrm{C}, p3n)$}",
    r"\shortstack[l]{$^{70}\mathrm{Zn}$\\$(^{12}\mathrm{C}, p3n)$}"
)
text_45 = text_45.replace(
    r"\makecell[l]{$^{74}\mathrm{Ge}$\\$(^4\mathrm{He}, 1p3n)$}",
    r"\shortstack[l]{$^{74}\mathrm{Ge}$\\$(^4\mathrm{He}, 1p3n)$}"
)

with open(p_45, "w", encoding="utf-8") as f:
    f.write(text_45)
print("Updated sec-4-5.tex (makecell -> shortstack)")

# 2. Update sec-4-4.tex Table 4.2b column widths and newline
p_44 = os.path.join(proj_root, "Tex/Sections/sec-4-4.tex")
with open(p_44, "r", encoding="utf-8") as f:
    text_44 = f.read()

old_t42b_header = r"\begin{tabularx}{\textwidth}{p{2.1cm} p{3.1cm} p{3.8cm} >{\raggedright\arraybackslash}X}"
new_t42b_header = r"\begin{tabularx}{\textwidth}{p{2.1cm} p{3.0cm} p{4.3cm} >{\raggedright\arraybackslash}X}"
assert old_t42b_header in text_44, "old_t42b_header not found"
text_44 = text_44.replace(old_t42b_header, new_t42b_header)

old_row = r"$Q_t \approx 6.7$--$9.9\ \mathrm{b}$；带间 $B(E2)_{\mathrm{out}} \approx$ $0.54$--$0.70\ e^2\mathrm{b}^2$（约 $100$--$132\ \mathrm{W.u.}$）；采用 $\delta \approx -3.10$"
new_row = r"$Q_t \approx 6.7$--$9.9\ \mathrm{b}$；\newline 带间 $B(E2)_{\mathrm{out}} \approx 0.54$--$0.70\ e^2\mathrm{b}^2$（约 $100$--$132\ \mathrm{W.u.}$）；采用 $\delta \approx -3.10$"
if old_row in text_44:
    text_44 = text_44.replace(old_row, new_row)

with open(p_44, "w", encoding="utf-8") as f:
    f.write(text_44)
print("Updated sec-4-4.tex (Table 4.2b width & newline)")
