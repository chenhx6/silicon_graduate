# -*- coding: utf-8 -*-
path = "knowledge/research-notes/a130-rewrite-parity-chirality-and-e1-limits-20261113.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Add link to canonical intrinsic-dipole-moment in Grounded Evidence
table_anchor = "| [[butler-nazarewicz-1996-intrinsic-reflection-asymmetry]]"
canonical_row = "| [[intrinsic-dipole-moment]]，规范定义与 K=0 化简 | `knowledge/observables/intrinsic-dipole-moment.md` | 本库权威可观测量页面。确立 12/5 显式 CG 比与 8/5[(2I-1)/(I-1)] 已化简 K=0 比两套自洽公式，明确撤回未化简 CG 前直接乘 8/5 的旧历史错误 |\n"

if "[[intrinsic-dipole-moment]]" not in text:
    text = text.replace(table_anchor, canonical_row + table_anchor)

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("Aligned research note with canonical intrinsic-dipole-moment")
