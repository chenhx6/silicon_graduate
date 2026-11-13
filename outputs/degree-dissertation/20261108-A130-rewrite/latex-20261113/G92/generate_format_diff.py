# -*- coding: utf-8 -*-
import subprocess, os

canonical_root = "raw/writing/gpt/A130/these_2023_template/these_template"
project_root = "tmp/a130-release-29-20261113/project"

files_to_compare = [
    "Tex/Sections/sec-3-7.tex",
    "Tex/Sections/sec-4-4.tex",
    "Tex/Sections/sec-4-5.tex",
    "Tex/Sections/sec-4-8.tex",
    "Tex/Appendices/AppendixA.tex"
]

all_diffs = []
for rel in files_to_compare:
    c_path = os.path.join(canonical_root, rel)
    p_path = os.path.join(project_root, rel)
    if os.path.exists(c_path) and os.path.exists(p_path):
        res = subprocess.run(["diff", "-u", c_path, p_path], capture_output=True, text=True)
        if res.stdout:
            all_diffs.append(res.stdout)

diff_content = "\n".join(all_diffs)
diff_path = "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G92/typesetting-format-diff.patch"
with open(diff_path, "w", encoding="utf-8") as f:
    f.write(diff_content)

print(f"Generated {diff_path}, total size: {len(diff_content)} bytes")
