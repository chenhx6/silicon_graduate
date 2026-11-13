# -*- coding: utf-8 -*-
import json, hashlib

def sha256_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

tex_path = "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-3-7.tex"
tex_sha = sha256_file(tex_path)

# Update ledger
ledger_path = "raw/writing/gpt/A130/latex-evidence-ledger/section-3-7.json"
with open(ledger_path, "r", encoding="utf-8") as f:
    ledger = json.load(f)
ledger["canonical_paths"]["tex_sha256"] = tex_sha
with open(ledger_path, "w", encoding="utf-8") as f:
    json.dump(ledger, f, indent=2, ensure_ascii=False)

# Update receipt
receipt_path = "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G88/section-3-7-receipt.json"
with open(receipt_path, "r", encoding="utf-8") as f:
    receipt = json.load(f)

files_to_hash = {
    "sec_3_7_tex": tex_path,
    "ledger_json": ledger_path,
    "research_note": "knowledge/research-notes/a130-rewrite-parity-chirality-and-e1-limits-20261113.md",
    "bib_file": "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G88/new-references-3-7.bib"
}

receipt["file_hashes"] = {k: {"path": v, "sha256": sha256_file(v)} for k, v in files_to_hash.items()}

with open(receipt_path, "w", encoding="utf-8") as f:
    json.dump(receipt, f, indent=2, ensure_ascii=False)

print("Rehashed Section 3.7 files successfully, tex_sha:", tex_sha[:16])
