# -*- coding: utf-8 -*-
import os, shutil, json, hashlib

src_root = "raw/writing/gpt/A130/these_2023_template/these_template"
target_root = "tmp/a130-release-29-20261113/project"

if os.path.exists(target_root):
    shutil.rmtree(target_root)
os.makedirs(target_root, exist_ok=True)

# 1. Copy Style and Biblio
shutil.copytree(os.path.join(src_root, "Style"), os.path.join(target_root, "Style"))
shutil.copytree(os.path.join(src_root, "Biblio"), os.path.join(target_root, "Biblio"))

# 2. Copy ALL figures in Img/ (including ucas_logo and all figure pairs)
shutil.copytree(os.path.join(src_root, "Img"), os.path.join(target_root, "Img"))
img_files = os.listdir(os.path.join(target_root, "Img"))
print(f"Copied {len(img_files)} files to Img/")

# 3. Copy Thesis.tex and base Tex files
shutil.copy2(os.path.join(src_root, "Thesis.tex"), os.path.join(target_root, "Thesis.tex"))
os.makedirs(os.path.join(target_root, "Tex"), exist_ok=True)

base_tex = [
    "Frontinfo.tex", "Frontmatter.tex", "figuretable.tex", "Prematter.tex",
    "Mainmatter.tex", "Backmatter.tex", "Appendix.tex",
    "Chapter1.tex", "Chapter2.tex", "Chapter3.tex", "Chapter4.tex", "Chapter5.tex"
]
for bt in base_tex:
    shutil.copy2(os.path.join(src_root, "Tex", bt), os.path.join(target_root, "Tex", bt))

# 4. Copy ONLY the 33 accepted sections
os.makedirs(os.path.join(target_root, "Tex", "Sections"), exist_ok=True)
with open("raw/writing/gpt/A130/manuscript-status.json", "r", encoding="utf-8") as f:
    ms = json.load(f)

whitelist = ms.get("accepted_content_sections", [])
print(f"Copying {len(whitelist)} whitelisted sections:")
for sid in whitelist:
    dash_id = sid.replace(".", "-")
    sec_name = f"sec-{dash_id}.tex"
    src_sec = os.path.join(src_root, "Tex", "Sections", sec_name)
    assert os.path.exists(src_sec), f"Missing section file: {src_sec}"
    shutil.copy2(src_sec, os.path.join(target_root, "Tex", "Sections", sec_name))

# 5. Copy admitted appendices: A, B, C, E, F
os.makedirs(os.path.join(target_root, "Tex", "Appendices"), exist_ok=True)
admitted_appendices = ["AppendixA.tex", "AppendixB.tex", "AppendixC.tex", "AppendixE.tex", "AppendixF.tex"]
for app in admitted_appendices:
    src_app = os.path.join(src_root, "Tex", "Appendices", app)
    assert os.path.exists(src_app), f"Missing appendix file: {src_app}"
    shutil.copy2(src_app, os.path.join(target_root, "Tex", "Appendices", app))

print("Successfully populated tmp/a130-release-29-20261113/project with 33 sections and Appendices A/B/C/E/F!")
