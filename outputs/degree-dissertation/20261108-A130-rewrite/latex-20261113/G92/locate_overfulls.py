# -*- coding: utf-8 -*-
import re

with open("tmp/a130-release-29-20261113/build/Thesis.log", "r", encoding="latin-1") as f:
    text = f.read()

# Pattern for overfull hbox with line numbers
matches = list(re.finditer(r"Overfull \\hbox \(([0-9.]+)pt too wide\)[^\n]*?(?:lines? ([0-9]+)(?:--([0-9]+))?|detected at line ([0-9]+))\n(.*?)(?=\n\n|\n[^\s]|\Z)", text, re.DOTALL))
print(f"Total matched overfulls: {len(matches)}")

for i, m in enumerate(matches, 1):
    pt = m.group(1)
    l1 = m.group(2) or m.group(4)
    l2 = m.group(3)
    snippet = m.group(5)[:160].replace("\n", " ")
    print(f"{i:2d}. pt={pt:>6} lines={l1}{('-'+l2) if l2 else ''} snippet: {snippet}")
