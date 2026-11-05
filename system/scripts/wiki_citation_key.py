#!/usr/bin/env python3
"""Generate and manage citation keys for Wiki source pages.

Actions:
  audit   - Report sources missing or having empty citation_key (dry-run).
  fill    - Generate citation_key for sources that lack one; write back to YAML.
  export  - Export all citation_key-bearing sources to BibTeX.
  sync    - fill + export in sequence.

Key format: firstauthor_year_shortkeyword
  - firstauthor: last name of first author, lowercased, ASCII-transliterated
  - year: four-digit publication year
  - shortkeyword: 1-3 tokens auto-selected from nuclei, title, or tags

BibTeX output: raw/zotero/wiki-auto-generated.bib
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import unicodedata
from pathlib import Path

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _strip_yaml_block(text: str) -> tuple[dict, str]:
    """Minimal YAML frontmatter parser (no PyYAML dependency)."""
    if not text.lstrip("\ufeff").startswith("---"):
        return {}, text
    body = text.lstrip("\ufeff")
    end = body.find("\n---", 3)
    if end < 0:
        return {}, text
    header = body[4:end]
    rest = body[end + 4:]
    meta: dict = {}
    for line in header.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r'^(\w[\w-]*)\s*:\s*(.*)', line)
        if m:
            key = m.group(1)
            val = m.group(2).strip()
            # Handle YAML lists on one line: [a, b, c]
            if val.startswith("[") and val.endswith("]"):
                items = [v.strip().strip('"').strip("'") for v in val[1:-1].split(",")]
                meta[key] = [i for i in items if i]
            else:
                meta[key] = val.strip('"').strip("'")
    return meta, rest


def _ascii_transliterate(s: str) -> str:
    """Transliterate to ASCII, keeping only letters/digits/hyphens."""
    # Normalize unicode
    s = unicodedata.normalize("NFKD", s)
    # Drop combining marks
    s = "".join(c for c in s if not unicodedata.combining(c))
    # Keep only ASCII letters, digits, spaces, hyphens
    s = re.sub(r'[^a-zA-Z0-9 -]', '', s)
    return s.strip()


# Pinyin table for common Chinese surnames (covers most nuclear physics authors)
_CHINESE_SURNAME_PINYIN = {
    "丁": "ding", "王": "wang", "李": "li", "张": "zhang", "刘": "liu",
    "陈": "chen", "杨": "yang", "黄": "huang", "赵": "zhao", "周": "zhou",
    "吴": "wu", "徐": "xu", "孙": "sun", "马": "ma", "朱": "zhu",
    "胡": "hu", "郭": "guo", "林": "lin", "何": "he", "高": "gao",
    "罗": "luo", "郑": "zheng", "梁": "liang", "宋": "song", "唐": "tang",
    "许": "xu", "韩": "han", "冯": "feng", "邓": "deng", "曹": "cao",
    "彭": "peng", "曾": "zeng", "肖": "xiao", "田": "tian", "董": "dong",
    "潘": "pan", "袁": "yuan", "蔡": "cai", "蒋": "jiang", "余": "yu",
    "于": "yu", "叶": "ye", "程": "cheng", "贺": "he", "柳": "liu",
    "龚": "gong", "石": "shi", "夏": "xia", "方": "fang", "车": "che",
    "强": "qiang", "穆": "mu", "闫": "yan", "岳": "yue", "卢": "lu",
    "吕": "lv", "谢": "xie", "苏": "su", "严": "yan", "邹": "zou",
    "汪": "wang", "邵": "shao", "江": "jiang", "孟": "meng",
    "华": "hua", "同": "tong", "雷": "lei", "鞠": "ju",
}


def _extract_first_author_surname(authors) -> str:
    """Extract and normalize the first author's surname."""
    if not authors:
        return "unknown"
    if isinstance(authors, list):
        first = authors[0]
    else:
        first = str(authors)

    first = first.strip().strip('"').strip("'")
    if not first:
        return "unknown"

    # Handle "et al." or trailing info
    first = re.sub(r',?\s*et\s+al\.?.*', '', first, flags=re.IGNORECASE)

    # Chinese name: try first character
    if any('\u4e00' <= c <= '\u9fff' for c in first):
        surname_char = first[0]
        if surname_char in _CHINESE_SURNAME_PINYIN:
            return _CHINESE_SURNAME_PINYIN[surname_char]
        # Two-char surnames
        if len(first) >= 2 and first[:2] in _CHINESE_SURNAME_PINYIN:
            return _CHINESE_SURNAME_PINYIN[first[:2]]
        # Fallback: transliterate
        return _ascii_transliterate(surname_char).lower() or "unknown"

    # Western name: "Surname, First" or "First Surname" or "F. Surname"
    if "," in first:
        surname = first.split(",")[0].strip()
    else:
        parts = first.strip().split()
        if not parts:
            surname = first
        elif len(parts) >= 2 and parts[0].isupper() and not parts[0].endswith(".") and len(parts[0]) > 1:
            # ALL-CAPS first token is likely East Asian surname: "WANG Hai-Xia"
            surname = parts[0]
        else:
            # Last token is surname: "J. T. Matta" -> "Matta"
            surname = parts[-1]

    surname = _ascii_transliterate(surname).lower()
    surname = re.sub(r'[^a-z]', '', surname)
    return surname or "unknown"


# Words to skip when building short keywords from titles
_STOP_WORDS = {
    "the", "a", "an", "of", "in", "for", "and", "on", "with", "to", "from",
    "by", "at", "via", "using", "its", "their", "new", "novel", "study",
    "investigation", "evidence", "structure", "states", "nuclear", "high",
    "spin", "low", "properties", "observation", "measurements", "results",
    "analysis", "spectroscopy", "experimental", "theoretical", "model",
    "based", "method", "approach", "first",
}


def _generate_short_keyword(meta: dict) -> str:
    """Auto-select 1-3 keyword tokens from nuclei, title, or tags."""
    parts: list[str] = []

    # Prefer nuclei field
    nuclei = meta.get("nuclei", [])
    if isinstance(nuclei, str):
        nuclei = [n.strip() for n in nuclei.strip("[]").split(",") if n.strip()]
    if nuclei:
        # Use first nucleus (e.g., "135pr")
        nuc = nuclei[0].strip().lower().replace('"', '').replace("'", "")
        parts.append(nuc)

    # Add 1-2 title-derived keywords
    title = meta.get("title_original", "") or meta.get("title", "")
    title = str(title).strip('"').strip("'")
    if title:
        words = re.findall(r'[a-zA-Z]{3,}', _ascii_transliterate(title))
        keywords = [w.lower() for w in words if w.lower() not in _STOP_WORDS]
        # Pick up to 2 distinctive words
        needed = 3 - len(parts)
        for kw in keywords[:needed]:
            if kw not in parts:
                parts.append(kw)

    # Fallback to tags
    if not parts:
        tags = meta.get("tags", [])
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.strip("[]").split(",") if t.strip()]
        for tag in tags[:2]:
            tag_clean = tag.strip().lower().replace('"', '').replace("'", "")
            if tag_clean and tag_clean not in parts:
                parts.append(tag_clean)

    if not parts:
        parts.append("source")

    return "-".join(parts[:3])


def generate_citation_key(meta: dict) -> str:
    """Generate citation_key from source page YAML metadata."""
    surname = _extract_first_author_surname(meta.get("authors"))
    year = str(meta.get("year", "0000")).strip('"').strip("'")
    keyword = _generate_short_keyword(meta)
    return f"{surname}_{year}_{keyword}"


def _ensure_unique(key: str, existing: set[str]) -> str:
    """Append -a, -b, ... suffix if key collides."""
    if key not in existing:
        return key
    for suffix in "abcdefghijklmnopqrstuvwxyz":
        candidate = f"{key}-{suffix}"
        if candidate not in existing:
            return candidate
    # Extremely unlikely
    return f"{key}-{hashlib.sha1(key.encode()).hexdigest()[:4]}"


# ---------------------------------------------------------------------------
# YAML rewriting: update citation_key in frontmatter
# ---------------------------------------------------------------------------

def _rewrite_citation_key(filepath: Path, new_key: str) -> bool:
    """Set or replace citation_key in YAML frontmatter. Returns True if file changed."""
    text = filepath.read_text(encoding="utf-8")
    bom = ""
    if text.startswith("\ufeff"):
        bom = "\ufeff"
        text = text[1:]

    if not text.startswith("---"):
        return False

    end = text.find("\n---", 3)
    if end < 0:
        return False

    header = text[3:end]
    rest = text[end:]

    # Replace or insert citation_key
    # Match citation_key line precisely: colon, optional space, optional value (quoted or bare), to EOL
    pattern = re.compile(r'^citation_key\s*:.*$', re.MULTILINE)
    if pattern.search(header):
        new_header = pattern.sub(f'citation_key: "{new_key}"', header, count=1)
    else:
        # Insert after year or doi or before first blank line
        lines = header.split("\n")
        insert_idx = len(lines)
        for i, line in enumerate(lines):
            if line.strip().startswith("year:") or line.strip().startswith("doi:"):
                insert_idx = i + 1
        lines.insert(insert_idx, f'citation_key: "{new_key}"')
        new_header = "\n".join(lines)

    new_text = bom + "---" + new_header + rest
    if new_text == (bom + text):
        return False
    filepath.write_text(new_text, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# BibTeX export
# ---------------------------------------------------------------------------

_BIBTEX_TYPE_MAP = {
    "journal-article": "article",
    "journal-article-experiment": "article",
    "journal-article-experiment-and-model": "article",
    "journal-article-theory": "article",
    "journal-article-theory-and-method": "article",
    "experiment-article": "article",
    "experimental-paper": "article",
    "experimental-paper-with-model-comparison": "article",
    "experimental-lifetime-paper": "article",
    "experiment": "article",
    "experiment-and-method": "article",
    "theory": "article",
    "theory-article": "article",
    "theoretical-paper": "article",
    "theory-method-and-applications": "article",
    "review": "article",
    "method": "article",
    "method-paper": "article",
    "phd-thesis": "phdthesis",
    "phd-thesis-experiment": "phdthesis",
    "phd-thesis-experiment-and-model": "phdthesis",
    "masters-thesis": "mastersthesis",
    "book": "book",
    "book-chapter": "incollection",
    "conference-proceedings": "inproceedings",
    "evaluated-nuclear-data": "misc",
    "evaluated-nuclear-data-object": "misc",
    "software-code": "misc",
    "software-source-code": "misc",
    "bibliographic-metadata": "misc",
}


def _format_authors_bibtex(authors) -> str:
    """Format author list for BibTeX."""
    if not authors:
        return ""
    if isinstance(authors, str):
        return authors
    return " and ".join(str(a) for a in authors)


def _escape_bibtex(s: str) -> str:
    """Escape special LaTeX characters in BibTeX values."""
    if not s:
        return ""
    # Protect existing braces
    s = s.replace("\\", "\\\\")
    for ch in ("&", "%", "#", "_"):
        s = s.replace(ch, f"\\{ch}")
    return s


def export_bibtex(sources_dir: Path, output_path: Path) -> int:
    """Export all source pages with citation_key to BibTeX. Returns entry count."""
    entries: list[tuple[str, str]] = []

    for md in sorted(sources_dir.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        meta, _ = _strip_yaml_block(text)
        key = meta.get("citation_key", "")
        if not key:
            continue

        source_type = meta.get("source_type", "misc")
        bib_type = _BIBTEX_TYPE_MAP.get(source_type, "misc")

        authors = _format_authors_bibtex(meta.get("authors"))
        title = str(meta.get("title_original", meta.get("title", ""))).strip('"').strip("'")
        year = str(meta.get("year", "")).strip('"').strip("'")
        journal = str(meta.get("journal", "")).strip('"').strip("'")
        volume = str(meta.get("volume", "")).strip('"').strip("'")
        pages = str(meta.get("pages", "")).strip('"').strip("'")
        doi = str(meta.get("doi", "")).strip('"').strip("'")
        arxiv = str(meta.get("arxiv", "")).strip('"').strip("'")

        lines = [f"@{bib_type}{{{key},"]
        if authors:
            lines.append(f"  author = {{{_escape_bibtex(authors)}}},")
        if title:
            lines.append(f"  title = {{{{{_escape_bibtex(title)}}}}},")
        if year:
            lines.append(f"  year = {{{year}}},")
        if journal and bib_type == "article":
            lines.append(f"  journal = {{{_escape_bibtex(journal)}}},")
        if volume:
            lines.append(f"  volume = {{{volume}}},")
        if pages:
            lines.append(f"  pages = {{{_escape_bibtex(pages)}}},")
        if doi:
            lines.append(f"  doi = {{{doi}}},")
        if arxiv:
            lines.append(f"  eprint = {{{arxiv}}},")
            lines.append(f"  archiveprefix = {{arXiv}},")
        lines.append("}")
        entries.append((key, "\n".join(lines)))

    # Write BibTeX file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    header = (
        "% Auto-generated by system/scripts/wiki_citation_key.py\n"
        "% Do not edit manually; regenerate with: python3 system/scripts/wiki_citation_key.py export\n"
        f"% {len(entries)} entries from knowledge/sources/\n\n"
    )
    output_path.write_text(
        header + "\n\n".join(e[1] for e in entries) + "\n",
        encoding="utf-8"
    )
    return len(entries)


# ---------------------------------------------------------------------------
# Main actions
# ---------------------------------------------------------------------------

def run_audit(sources_dir: Path) -> int:
    missing = 0
    for md in sorted(sources_dir.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        meta, _ = _strip_yaml_block(text)
        key = meta.get("citation_key", "")
        if not key:
            missing += 1
    print(f"Sources total: {len(list(sources_dir.glob('*.md')))}")
    print(f"Missing/empty citation_key: {missing}")
    return missing


def run_fill(sources_dir: Path, dry_run: bool = False) -> int:
    existing_keys: set[str] = set()
    # First pass: collect existing keys
    for md in sources_dir.glob("*.md"):
        text = md.read_text(encoding="utf-8")
        meta, _ = _strip_yaml_block(text)
        key = meta.get("citation_key", "")
        if key:
            existing_keys.add(key)

    # Second pass: generate missing keys
    filled = 0
    for md in sorted(sources_dir.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        meta, _ = _strip_yaml_block(text)
        key = meta.get("citation_key", "")
        if key:
            continue

        new_key = generate_citation_key(meta)
        new_key = _ensure_unique(new_key, existing_keys)

        if dry_run:
            print(f"  [dry-run] {md.name} -> {new_key}")
        else:
            if _rewrite_citation_key(md, new_key):
                filled += 1
            else:
                print(f"  [skip] {md.name}: could not rewrite frontmatter")
                continue
        existing_keys.add(new_key)

    action = "would fill" if dry_run else "filled"
    count = len([1 for md in sources_dir.glob("*.md")
                 if not _strip_yaml_block(md.read_text(encoding="utf-8"))[0].get("citation_key", "")]) if dry_run else 0
    print(f"{action}: {filled if not dry_run else len(existing_keys)} keys")
    return filled


def main():
    parser = argparse.ArgumentParser(description="Wiki citation_key manager")
    parser.add_argument("action", choices=["audit", "fill", "export", "sync"],
                        help="Action to perform")
    parser.add_argument("--root", default=".", help="Wiki root directory")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview changes without writing (fill only)")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    sources_dir = root / "knowledge" / "sources"
    bib_path = root / "raw" / "zotero" / "wiki-auto-generated.bib"

    if not sources_dir.is_dir():
        print(f"ERROR: {sources_dir} not found", file=sys.stderr)
        sys.exit(1)

    if args.action == "audit":
        run_audit(sources_dir)

    elif args.action == "fill":
        run_fill(sources_dir, dry_run=args.dry_run)

    elif args.action == "export":
        n = export_bibtex(sources_dir, bib_path)
        print(f"Exported {n} entries to {bib_path}")

    elif args.action == "sync":
        run_fill(sources_dir, dry_run=args.dry_run)
        if not args.dry_run:
            n = export_bibtex(sources_dir, bib_path)
            print(f"Exported {n} entries to {bib_path}")


if __name__ == "__main__":
    main()
