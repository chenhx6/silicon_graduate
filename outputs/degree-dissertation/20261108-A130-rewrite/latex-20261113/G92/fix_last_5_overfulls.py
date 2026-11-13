# -*- coding: utf-8 -*-
import os

proj_root = "tmp/a130-release-29-20261113/project"

# 1. sec-4-4.tex
p_44 = os.path.join(proj_root, "Tex/Sections/sec-4-4.tex")
with open(p_44, "r", encoding="utf-8") as f:
    text_44 = f.read()

# Fix Table 4.1 column widths
old_t41_header = r"\begin{tabularx}{\textwidth}{p{2.3cm} p{1.6cm} p{1.6cm} p{1.8cm} p{1.6cm} >{\raggedright\arraybackslash}X}"
new_t41_header = r"\begin{tabularx}{\textwidth}{p{2.1cm} p{1.4cm} p{1.5cm} p{1.6cm} p{1.5cm} >{\raggedright\arraybackslash}X}"
assert old_t41_header in text_44, "old_t41_header not found"
text_44 = text_44.replace(old_t41_header, new_t41_header)

# Fix Line 283 break without changing words
old_283 = r"特征跃迁 $376\ \mathrm{keV}$（$11/2^- \to 9/2^-$）与 $462\ \mathrm{keV}$（$15/2^- \to 13/2^-$）支持小混合比解"
new_283 = r"特征跃迁 $376\ \mathrm{keV}$（$11/2^-$ $\to 9/2^-$）与 $462\ \mathrm{keV}$（$15/2^-$ $\to 13/2^-$）支持小混合比解"
assert old_283 in text_44, "old_283 not found"
text_44 = text_44.replace(old_283, new_283)

# Fix Line 321 break without changing words
old_321 = r"形状不变量无量纲比值 $R \equiv q_3 / q_2^{3/2}$（正比于 $\langle Q^3 \cos 3\delta \rangle / \langle Q^2 \rangle^{3/2}$），包含了体系在全部内禀形变空间中的大振幅积分权重。"
new_321 = r"形状不变量无量纲比值 $R \equiv q_3 / q_2^{3/2}$（正比于 $\langle Q^3 \cos 3\delta \rangle$ $/ \langle Q^2 \rangle^{3/2}$），包含了体系在全部内禀形变空间中的大振幅积分权重。"
assert old_321 in text_44, "old_321 not found"
text_44 = text_44.replace(old_321, new_321)

# Fix Table 4.2b column widths
old_t42b_header = r"\begin{tabularx}{\textwidth}{p{2.4cm} p{3.2cm} p{4.0cm} >{\raggedright\arraybackslash}X}"
new_t42b_header = r"\begin{tabularx}{\textwidth}{p{2.1cm} p{3.1cm} p{3.8cm} >{\raggedright\arraybackslash}X}"
assert old_t42b_header in text_44, "old_t42b_header not found"
text_44 = text_44.replace(old_t42b_header, new_t42b_header)

with open(p_44, "w", encoding="utf-8") as f:
    f.write(text_44)
print("Updated sec-4-4.tex")

# 2. sec-4-5.tex Table 4.3 column widths
p_45 = os.path.join(proj_root, "Tex/Sections/sec-4-5.tex")
with open(p_45, "r", encoding="utf-8") as f:
    text_45 = f.read()

old_t43_header = r"\begin{tabularx}{\textwidth}{p{2.1cm}p{1.7cm}p{2.0cm}p{2.9cm}X}"
new_t43_header = r"\begin{tabularx}{\textwidth}{p{2.0cm}p{1.6cm}p{1.9cm}p{3.0cm}>{\raggedright\arraybackslash}X}"
assert old_t43_header in text_45, "old_t43_header not found"
text_45 = text_45.replace(old_t43_header, new_t43_header)

with open(p_45, "w", encoding="utf-8") as f:
    f.write(text_45)
print("Updated sec-4-5.tex")
