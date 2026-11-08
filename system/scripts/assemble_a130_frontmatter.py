#!/usr/bin/env python3
"""Assemble existing A130 sections and render a citation-aware MathML preview.

This renderer does not approve scientific claims and never reads the archived
old manuscript.  It refuses raw TeX that Pandoc would silently omit from HTML.
"""

from __future__ import annotations

import argparse
import collections
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[2]
PAPER = ROOT / "raw/writing/gpt/A130"
OUT = ROOT / "outputs/degree-dissertation/20261108-A130-rewrite"
CHAPTERS = {
    1: "从谱线提出问题：原子核形状与集体运动的证据",
    2: "从核子到量子形状：占据、配对与集体动力学",
    3: "三轴及耦合激发：取向、形状与有限体系的对称性",
    4: "六区的条件比较：跨区迁移与两翼探针",
    5: "在束γ谱与数字化实验：从信号到结构推断",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pandoc(args: list[str], text: str, *, warning_log: list[str] | None = None) -> str:
    result = subprocess.run(
        ["pandoc", *args], input=text, capture_output=True, text=True, cwd=ROOT
    )
    diagnostics = result.stderr.strip()
    # This installed Pandoc lacks Chinese template translations. Titles are
    # supplied explicitly below; retain this known limitation in the receipt.
    # Math/citation warnings must still fail, including exit-0 math fallbacks.
    remaining = diagnostics
    for known in (
        "[WARNING] Could not load translations for zh-CN\n"
        "  data file translations/zh.yaml not found",
        "[WARNING] The term Abstract has no translation defined.",
    ):
        remaining = remaining.replace(known, "")
    if result.returncode or remaining.strip():
        raise RuntimeError(
            f"Pandoc exit={result.returncode}; {result.stderr.strip()}"
        )
    if diagnostics and warning_log is not None:
        warning_log.append(diagnostics)
    return result.stdout


def inspect_ast(tree: object) -> dict:
    counts: collections.Counter = collections.Counter()
    citations: set[str] = set()
    raw_tex: list[str] = []

    def walk(item: object) -> None:
        if isinstance(item, dict):
            kind = item.get("t")
            content = item.get("c")
            if kind == "Math":
                counts[content[0]["t"]] += 1
            if kind == "Cite":
                citations.update(c["citationId"] for c in content[0])
            if kind in {"RawInline", "RawBlock"} and content[0] in {"tex", "latex"}:
                raw_tex.append(content[1][:140])
            for value in item.values():
                walk(value)
        elif isinstance(item, list):
            for value in item:
                walk(value)

    walk(tree)
    return {"math": dict(counts), "citations": sorted(citations), "raw_tex": raw_tex}


def normalize_headings(text: str, section_id: str) -> str:
    first = re.search(r"^(#{1,6})\s+(.+)$", text, re.MULTILINE)
    if not first or not first[2].startswith(section_id + " "):
        raise ValueError(f"{section_id}: missing expected opening section heading")
    shift = 2 - len(first[1])
    return re.sub(
        r"^(#{1,6})(\s+)",
        lambda m: "#" * min(6, max(1, len(m[1]) + shift)) + m[2],
        text,
        flags=re.MULTILINE,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sections", help="Comma-separated planned IDs; default: all existing")
    args = parser.parse_args()
    if not shutil.which("pandoc"):
        raise RuntimeError("Pandoc is not available; no PDF or preview claimed")

    status = json.loads((PAPER / "manuscript-status.json").read_text())
    planned = {entry["id"] for entry in status["sections"]}
    selected = args.sections.split(",") if args.sections else sorted(
        (
            sid for sid in planned
            if (PAPER / f"research-draft/section-{sid.replace('.', '-')}.md").is_file()
        ),
        key=lambda sid: tuple(map(int, sid.split("."))),
    )
    if not selected or len(selected) != len(set(selected)) or set(selected) - planned:
        raise ValueError("Choose distinct existing section IDs from the manuscript plan")
    selected.sort(key=lambda sid: tuple(map(int, sid.split("."))))
    bibliography = PAPER / "references.csl.json"
    references = json.loads(bibliography.read_text())
    known = {entry["id"] for entry in references}
    pieces: list[str] = []
    inputs: list[dict] = []
    chapter = None

    for sid in selected:
        path = PAPER / f"research-draft/section-{sid.replace('.', '-')}.md"
        if not path.resolve().is_relative_to(PAPER.resolve()):
            raise ValueError("Section path leaves the active manuscript")
        text = path.read_text(encoding="utf-8")
        if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f\r]", text):
            raise ValueError(f"{sid}: control character in manuscript")
        ast = json.loads(pandoc(["-f", "markdown", "-t", "json"], text))
        if ast["meta"]:
            raise ValueError(f"{sid}: section must not override document metadata")
        inspected = inspect_ast(ast)
        if inspected["raw_tex"]:
            raise ValueError(
                f"{sid}: raw TeX would disappear from HTML; use $/$$ math: "
                + repr(inspected["raw_tex"][:2])
            )
        missing = set(inspected["citations"]) - known
        if missing:
            raise ValueError(f"{sid}: unknown reference IDs: {sorted(missing)}")
        current_chapter = int(sid.split(".")[0])
        if current_chapter != chapter:
            pieces.append(f"# 第{current_chapter}章 {CHAPTERS[current_chapter]}\n")
            chapter = current_chapter
        pieces.append(normalize_headings(text, sid).strip() + "\n")
        inputs.append(
            {
                "id": sid, "path": str(path.relative_to(ROOT)), "sha256": sha(path),
                "math": inspected["math"], "citations": inspected["citations"],
            }
        )

    text = "\n\n".join(pieces) + "\n\n# 参考文献\n\n::: {#refs}\n:::\n"
    warnings: list[str] = []
    html = pandoc(
        [
            "-f", "markdown+tex_math_dollars+fenced_divs-raw_html-raw_tex",
            "-t", "html5", "--standalone", "--toc", "--toc-depth=3", "--mathml",
            "--citeproc", "--bibliography", str(bibliography),
            "-M", "lang=zh-CN",
            "-M", "title=核形状、三轴动力学与实验观测：前置章节研究稿",
            "-M", "subtitle=样节预览：" + "、".join(selected),
            "-M", "toc-title=目录",
        ],
        text, warning_log=warnings,
    )
    markdown_path = PAPER / "frontmatter-draft.md"
    html_path = PAPER / "frontmatter-preview.html"
    markdown_path.write_text(text, encoding="utf-8")
    html_path.write_text(html, encoding="utf-8")
    OUT.mkdir(parents=True, exist_ok=True)
    receipt = {
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "command_sections": selected, "planned_total": len(planned),
        "inputs": inputs, "bibliography_sha256": sha(bibliography),
        "outputs": [
            {"path": str(p.relative_to(ROOT)), "sha256": sha(p)}
            for p in [markdown_path, html_path]
        ],
        "known_template_translation_warnings": warnings,
        "scientific_admission": False, "school_submission_ready": False,
        "scope": "Existing section preview; no automatic scientific or reader-effect approval",
    }
    (OUT / "assembly-receipt.json").write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({"sections": selected, "preview": str(html_path.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
