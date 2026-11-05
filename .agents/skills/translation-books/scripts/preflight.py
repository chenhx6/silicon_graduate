"""Read-only translation tool and language-review dependency inventory."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil


def skill_roots(explicit):
    if explicit is not None:
        return [Path(p).expanduser() for p in explicit]
    home = Path.home()
    codex = Path(os.environ.get("CODEX_HOME", home / ".codex"))
    return [Path.cwd() / ".agents" / "skills", home / ".agents" / "skills",
            codex / "skills"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path)
    parser.add_argument("--review-skill", default="shuorenhua")
    parser.add_argument("--skill-root", action="append",
                        help="Override filesystem roots; may be repeated.")
    parser.add_argument("--tex-engine", type=Path,
                        help="Explicit installed engine outside PATH.")
    args = parser.parse_args()
    roots = skill_roots(args.skill_root)
    names = [args.review_skill, args.review_skill.split(":")[-1]]
    candidates = [root / name / "SKILL.md" for root in roots for name in names]
    reviewer = next((p.resolve() for p in candidates
                     if p.is_file() and os.access(p, os.R_OK)), None)
    tools = {name: shutil.which(name) for name in
             ["xelatex", "tectonic", "pdffonts", "pdftotext", "pdftoppm", "tesseract"]}
    engine = str(args.tex_engine.resolve()) if (
        args.tex_engine and args.tex_engine.is_file()
        and os.access(args.tex_engine, os.X_OK)) else tools["xelatex"] or tools["tectonic"]
    issues = []
    if not reviewer:
        issues.append({
            "code": "language_review_skill_missing",
            "action": "提示安装所请求的语言审校技能，或询问用户选用哪个替代技能；不静默替换。"
        })
    if not engine:
        issues.append({"code": "tex_engine_missing",
                       "action": "定位可用 XeLaTeX/Tectonic；按环境授权解决安装。"})
    source = None
    if args.source:
        if args.source.is_file():
            digest = hashlib.sha256()
            with args.source.open("rb") as stream:
                for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                    digest.update(chunk)
            source = {"path": str(args.source.resolve()),
                      "bytes": args.source.stat().st_size,
                      "sha256": digest.hexdigest()}
        else:
            issues.append({"code": "source_missing", "path": str(args.source)})
    report = {
        "source": source, "tools": tools, "tex_engine": engine,
        "python_modules": {name: importlib.util.find_spec(name) is not None
                           for name in ["pymupdf", "PIL"]},
        "review_skill": {"requested": args.review_skill,
                         "path": str(reviewer) if reviewer else None,
                         "roots_checked": [str(p) for p in roots]},
        "issues": issues,
        "note": "Inventory only: does not install tools, read the reviewer instructions, or certify fonts/OCR."
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 2 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
