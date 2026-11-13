# -*- coding: utf-8 -*-
import os

proj_root = "tmp/a130-release-29-20261113/project"

# 1. Update sec-4-4.tex: Table 4.1 and Table 4.2b
p_44 = os.path.join(proj_root, "Tex/Sections/sec-4-4.tex")
with open(p_44, "r", encoding="utf-8") as f:
    text_44 = f.read()

# Table 4.1: use natural c columns with shortstack for numbers with asymmetric errors, and allow link transitions to wrap
old_t41_header = r"\begin{tabularx}{\textwidth}{p{2.1cm} p{1.4cm} p{1.5cm} p{1.6cm} p{1.5cm} >{\raggedright\arraybackslash}X}"
new_t41_header = r"\begin{tabularx}{\textwidth}{p{2.2cm} p{2.0cm} c c c >{\raggedright\arraybackslash}X}"

old_t41_cols = r"""\shortstack{能带与\\跃迁通道} & \shortstack{初态自旋\\$I_i^\pi$} & \shortstack{光子能量\\$E_\gamma$ [keV]} & \shortstack{平均寿命\\$\tau$ [ps]} & \shortstack{跃迁四极矩\\$Q_t$ [b]} & \shortstack{跃迁几率 / 强度\\$B(E2)$ 与 $B(M1)$} \\"""
new_t41_cols = r"""\shortstack{能带与\\跃迁通道} & \shortstack{跃迁自旋\\$I_i^\pi \to I_f^\pi$} & \shortstack{$E_\gamma$\\$\text{[keV]}$} & \shortstack{$\tau$\\$\text{[ps]}$} & \shortstack{$Q_t$\\$\text{[b]}$} & \shortstack{跃迁几率 / 强度\\$B(E2)$ 与 $B(M1)$} \\"""

assert old_t41_header in text_44, "old_t41_header not found"
text_44 = text_44.replace(old_t41_header, new_t41_header)

assert old_t41_cols in text_44, "old_t41_cols not found"
text_44 = text_44.replace(old_t41_cols, new_t41_cols)

# Table 4.2b line 361 B(E2)_out break
old_t42b_line = r"带间 $B(E2)_{\mathrm{out}} \approx 0.54$--$0.70\ e^2\mathrm{b}^2$（约 $100$--$132\ \mathrm{W.u.}$）；采用 $\delta \approx -3.10$"
new_t42b_line = r"带间 $B(E2)_{\mathrm{out}} \approx$ $0.54$--$0.70\ e^2\mathrm{b}^2$（约 $100$--$132\ \mathrm{W.u.}$）；采用 $\delta \approx -3.10$"
assert old_t42b_line in text_44, "old_t42b_line not found"
text_44 = text_44.replace(old_t42b_line, new_t42b_line)

with open(p_44, "w", encoding="utf-8") as f:
    f.write(text_44)
print("Updated sec-4-4.tex")

# 2. Update sec-4-5.tex Table 4.3 column 1 breaks
p_45 = os.path.join(proj_root, "Tex/Sections/sec-4-5.tex")
with open(p_45, "r", encoding="utf-8") as f:
    text_45 = f.read()

old_zn = r"$^{70}\mathrm{Zn}(^{12}\mathrm{C}, p3n)$"
new_zn = r"\makecell[l]{$^{70}\mathrm{Zn}$\\$(^{12}\mathrm{C}, p3n)$}"
assert old_zn in text_45, "old_zn not found"
text_45 = text_45.replace(old_zn, new_zn)

old_ge = r"$^{74}\mathrm{Ge}(^4\mathrm{He}, 1p3n)$"
new_ge = r"\makecell[l]{$^{74}\mathrm{Ge}$\\$(^4\mathrm{He}, 1p3n)$}"
assert old_ge in text_45, "old_ge not found"
text_45 = text_45.replace(old_ge, new_ge)

with open(p_45, "w", encoding="utf-8") as f:
    f.write(text_45)
print("Updated sec-4-5.tex")
