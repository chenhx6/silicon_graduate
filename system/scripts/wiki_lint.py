#!/usr/bin/env python3
"""Dependency-free structural and scientific guardrail lint for this Wiki."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Any, Iterable


SEVERITY_ORDER = {"info": 0, "warning": 1, "error": 2}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
NUCLIDE_SLUG_RE = re.compile(r"^\d+[a-z]+$")
SHA256_RE = re.compile(r"^[A-Fa-f0-9]{64}$")
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")
HEADING_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
FIELD_RE = re.compile(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$")
REACTION_RE = re.compile(
    r"^\s*(\d+)([A-Za-z]+)\((\d+)([A-Za-z]+),\s*([^)]+)\)(\d+)([A-Za-z]+)\s*$",
    re.IGNORECASE,
)
EXACT_CHANNEL_RE = re.compile(r"^(?:(\d*)p)?(?:(\d*)n)?(?:\s+gamma)?$", re.IGNORECASE)
SPONTANEOUS_FISSION_RE = re.compile(r"^\s*(\d+)([A-Za-z]+)\s+spontaneous fission\s*$", re.IGNORECASE)


@dataclass(frozen=True)
class Issue:
    severity: str
    code: str
    path: str
    message: str


@dataclass
class Page:
    path: Path
    relative: str
    slug: str
    expected_type: str
    meta: dict[str, Any]
    body: str


@dataclass
class GovernanceMetrics:
    page_unreviewed: int = 0
    source_unreviewed: int = 0
    claims_total: int = 0
    claim_needs_review: int = 0
    claim_missing_locator: int = 0
    claim_missing_kind: int = 0
    source_missing_raw_file: int = 0
    source_missing_citation_key: int = 0


@dataclass
class Report:
    root: str
    checked_at: str
    pages: int
    wikilinks: int
    source_hashes_checked: int
    governance: GovernanceMetrics
    issues: list[Issue]

    @property
    def counts(self) -> Counter[str]:
        return Counter(issue.severity for issue in self.issues)

    def exit_code(self, fail_on: str) -> int:
        if fail_on == "never":
            return 0
        threshold = SEVERITY_ORDER[fail_on]
        return int(
            any(SEVERITY_ORDER[issue.severity] >= threshold for issue in self.issues)
        )


def split_inline_list(raw: str) -> list[str]:
    inner = raw.strip()[1:-1].strip()
    if not inner:
        return []
    values: list[str] = []
    current: list[str] = []
    quote = ""
    for char in inner:
        if char in "\"'":
            if quote == char:
                quote = ""
            elif not quote:
                quote = char
            current.append(char)
        elif char == "," and not quote:
            values.append(clean_scalar("".join(current).strip()))
            current = []
        else:
            current.append(char)
    values.append(clean_scalar("".join(current).strip()))
    return [str(value) for value in values]


def clean_scalar(raw: str) -> Any:
    value = raw.strip()
    if value.startswith("[") and value.endswith("]"):
        return split_inline_list(value)
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def parse_frontmatter_text(text: str) -> tuple[dict[str, Any], str, list[str]]:
    normalized = text.replace("\r\n", "\n")
    lines = normalized.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, normalized, ["missing opening ---"]
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return {}, normalized, ["missing closing ---"]

    meta: dict[str, Any] = {}
    errors: list[str] = []
    for lineno, line in enumerate(lines[1:end], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = FIELD_RE.match(line)
        if not match:
            errors.append(f"unsupported YAML syntax at line {lineno}: {line}")
            continue
        key, raw = match.groups()
        if key in meta:
            errors.append(f"duplicate field {key} at line {lineno}")
        meta[key] = clean_scalar(raw or "")
    return meta, "\n".join(lines[end + 1 :]), errors


def read_page(path: Path, root: Path, expected_type: str) -> tuple[Page, list[Issue]]:
    relative = path.relative_to(root).as_posix()
    issues: list[Issue] = []
    try:
        text = path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError as exc:
        return (
            Page(path, relative, path.stem, expected_type, {}, ""),
            [Issue("error", "ENCODING", relative, f"not valid UTF-8: {exc}")],
        )
    meta, body, yaml_errors = parse_frontmatter_text(text)
    for error in yaml_errors:
        issues.append(Issue("error", "FRONTMATTER_PARSE", relative, error))
    return Page(path, relative, path.stem, expected_type, meta, body), issues


def strip_fenced_code(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


def wikilinks(text: str) -> list[str]:
    return [match.group(1).strip() for match in WIKILINK_RE.finditer(strip_fenced_code(text))]


def headings(text: str) -> set[str]:
    return {match.group(1).strip() for match in HEADING_RE.finditer(text)}


def markdown_table_cells(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    return [cell.strip() for cell in stripped.strip("|").split("|")]


def is_markdown_separator(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def claim_rows(body: str, config: dict[str, Any]) -> list[tuple[int, dict[str, str]]]:
    fields = config["governance_fields"]
    required_headers = {
        fields["claim_kind"],
        fields["locator"],
        fields["needs_review"],
    }
    lines = body.splitlines()
    rows: list[tuple[int, dict[str, str]]] = []
    index = 0
    while index < len(lines):
        header = markdown_table_cells(lines[index])
        if header is None or not required_headers.issubset(set(header)):
            index += 1
            continue
        index += 1
        while index < len(lines):
            cells = markdown_table_cells(lines[index])
            if cells is None:
                break
            if not is_markdown_separator(cells):
                padded = cells + [""] * max(0, len(header) - len(cells))
                rows.append((index + 1, dict(zip(header, padded))))
            index += 1
    return rows


def value_missing(meta: dict[str, Any], field: str) -> bool:
    if field not in meta:
        return True
    value = meta[field]
    return value == "" or value is None


def add(issues: list[Issue], severity: str, code: str, path: str, message: str) -> None:
    issues.append(Issue(severity, code, path, message))


def validate_page(page: Page, config: dict[str, Any], issues: list[Issue]) -> None:
    meta = page.meta
    for field in config["common_required_fields"]:
        if value_missing(meta, field):
            add(issues, "error", "FIELD_REQUIRED", page.relative, f"missing {field}")
    for field in config["type_required_fields"].get(page.expected_type, []):
        if value_missing(meta, field):
            add(issues, "error", "FIELD_REQUIRED", page.relative, f"missing {field}")

    if meta.get("type") != page.expected_type:
        add(
            issues,
            "error",
            "TYPE_DIRECTORY",
            page.relative,
            f"type={meta.get('type')!r}, expected {page.expected_type!r}",
        )
    if meta.get("status") not in config["allowed_status"]:
        add(issues, "error", "STATUS_VALUE", page.relative, f"invalid status {meta.get('status')!r}")
    if meta.get("review_status") not in config["allowed_review_status"]:
        add(
            issues,
            "error",
            "REVIEW_STATUS_VALUE",
            page.relative,
            f"invalid review_status {meta.get('review_status')!r}",
        )
    if meta.get("review_status") == "needs-human-review":
        add(issues, "info", "HUMAN_REVIEW", page.relative, "page awaits human review")

    if page.expected_type == "research-note":
        reasoning_status = meta.get("reasoning_status")
        if reasoning_status not in config["allowed_reasoning_status"]:
            add(
                issues,
                "error",
                "REASONING_STATUS_VALUE",
                page.relative,
                f"invalid reasoning_status {reasoning_status!r}",
            )
        if reasoning_status == "promoted" and value_missing(meta, "promotion_target"):
            add(
                issues,
                "error",
                "PROMOTION_TARGET_MISSING",
                page.relative,
                "promoted research-note requires promotion_target",
            )
        evidence_sources = meta.get("evidence_sources")
        if not isinstance(evidence_sources, list) or not any(
            str(source).strip() for source in evidence_sources
        ):
            add(
                issues,
                "error",
                "EVIDENCE_SOURCES_EMPTY",
                page.relative,
                "research-note requires at least one grounded evidence source",
            )
        if reasoning_status == "promoted" and meta.get("review_status") not in {
            "human-reviewed",
            "verified",
        }:
            add(
                issues,
                "error",
                "PROMOTED_WITHOUT_REVIEW",
                page.relative,
                "promoted research-note requires human-reviewed or verified review_status",
            )

    for field in ("created", "updated"):
        raw = str(meta.get(field, ""))
        if not DATE_RE.fullmatch(raw):
            add(issues, "error", "DATE_FORMAT", page.relative, f"{field}={raw!r}")
        else:
            try:
                date.fromisoformat(raw)
            except ValueError:
                add(issues, "error", "DATE_VALUE", page.relative, f"{field}={raw!r}")
    if DATE_RE.fullmatch(str(meta.get("created", ""))) and DATE_RE.fullmatch(
        str(meta.get("updated", ""))
    ):
        if str(meta["updated"]) < str(meta["created"]):
            add(issues, "error", "DATE_ORDER", page.relative, "updated precedes created")

    slug_re = NUCLIDE_SLUG_RE if page.expected_type == "nucleus" else SLUG_RE
    if not slug_re.fullmatch(page.slug):
        add(issues, "error", "SLUG_FORMAT", page.relative, f"invalid slug {page.slug!r}")

    page_headings = headings(page.body)
    for section in config["required_sections"].get(page.expected_type, []):
        if section not in page_headings:
            add(issues, "error", "SECTION_REQUIRED", page.relative, f"missing ## {section}")

    if meta.get("confidence") == "high":
        if value_missing(meta, "high_confirmed_by") or value_missing(meta, "high_confirmed_date"):
            add(
                issues,
                "error",
                "HIGH_UNCONFIRMED",
                page.relative,
                "confidence: high requires high_confirmed_by and high_confirmed_date",
            )


def validate_source(
    page: Page, root: Path, config: dict[str, Any], issues: list[Issue]
) -> int:
    checked = 0
    meta = page.meta
    if meta.get("reading_depth") not in config["allowed_reading_depth"]:
        add(
            issues,
            "error",
            "READING_DEPTH",
            page.relative,
            f"invalid reading_depth {meta.get('reading_depth')!r}",
        )
    raw_value = str(meta.get("raw_file", "")).replace("\\", "/")
    if not raw_value.startswith("raw/"):
        add(issues, "error", "RAW_PATH", page.relative, f"raw_file must be under raw/: {raw_value!r}")
        return checked
    raw_path = (root / raw_value).resolve()
    raw_root = (root / "raw").resolve()
    try:
        raw_path.relative_to(raw_root)
    except ValueError:
        add(issues, "error", "RAW_PATH_ESCAPE", page.relative, f"path escapes raw/: {raw_value!r}")
        return checked

    expected = str(meta.get("raw_sha256", ""))
    if not SHA256_RE.fullmatch(expected):
        add(issues, "error", "SHA256_FORMAT", page.relative, "raw_sha256 must be 64 hex characters")
    if not raw_path.is_file():
        add(
            issues,
            "warning",
            "RAW_MISSING",
            page.relative,
            f"{raw_value} unavailable; hash check not executed",
        )
        return checked

    digest = hashlib.sha256()
    with raw_path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    checked += 1
    if digest.hexdigest().upper() != expected.upper():
        add(
            issues,
            "error",
            "RAW_HASH_MISMATCH",
            page.relative,
            f"SHA-256 differs for {raw_value}",
        )
    if "claim_kind" not in page.body or "evidence_level" not in page.body or "locator" not in page.body:
        add(
            issues,
            "error",
            "CLAIM_TABLE",
            page.relative,
            "Key Results must expose claim_kind, evidence_level, and locator",
        )
    return checked


def validate_nucleus(page: Page, config: dict[str, Any], issues: list[Issue]) -> None:
    meta = page.meta
    try:
        mass, protons, neutrons = int(meta["A"]), int(meta["Z"]), int(meta["N"])
    except (KeyError, TypeError, ValueError):
        add(issues, "error", "NUCLIDE_NUMERIC", page.relative, "A, Z, and N must be integers")
        return
    if mass != protons + neutrons:
        add(issues, "error", "NUCLIDE_SUM", page.relative, f"A={mass}, but Z+N={protons + neutrons}")
    element = str(meta.get("element", "")).lower()
    expected_z = config["element_z"].get(element)
    if expected_z is None:
        add(issues, "warning", "ELEMENT_UNKNOWN", page.relative, f"element {element!r} not in lint config")
    elif expected_z != protons:
        add(issues, "error", "ELEMENT_Z", page.relative, f"{element} requires Z={expected_z}, got {protons}")
    expected_nuclide = f"{mass}{element}"
    if str(meta.get("nuclide", "")).lower() != expected_nuclide or page.slug != expected_nuclide:
        add(
            issues,
            "error",
            "NUCLIDE_ID",
            page.relative,
            f"expected nuclide and slug {expected_nuclide!r}",
        )


def validate_experiment(page: Page, config: dict[str, Any], issues: list[Issue]) -> None:
    reaction = str(page.meta.get("reaction", ""))
    element_z = config["element_z"]
    fission = SPONTANEOUS_FISSION_RE.fullmatch(reaction)
    if fission:
        _, parent_element = fission.groups()
        if parent_element.lower() not in element_z:
            add(issues, "warning", "REACTION_ELEMENT", page.relative, "fission parent contains unconfigured element")
        # The product channel is not specified, so conservation cannot be checked here.
        return
    match = REACTION_RE.fullmatch(reaction)
    if not match:
        add(
            issues,
            "warning",
            "REACTION_PARSE",
            page.relative,
            f"reaction not automatically parsed: {reaction!r}",
        )
        return
    target_a, target_e, beam_a, beam_e, channel, residual_a, residual_e = match.groups()
    symbols = (target_e.lower(), beam_e.lower(), residual_e.lower())
    if any(symbol not in element_z for symbol in symbols):
        add(issues, "warning", "REACTION_ELEMENT", page.relative, "reaction contains unconfigured element")
        return
    exact_channel = EXACT_CHANNEL_RE.fullmatch(channel)
    if exact_channel is None or not any(group is not None for group in exact_channel.groups()):
        add(issues, "warning", "REACTION_CHANNEL_UNRESOLVED", page.relative, f"evaporation channel cannot be balanced: {channel!r}")
        return
    protons, neutrons = (int(group or 1) if group is not None else 0 for group in exact_channel.groups())
    expected_a = int(target_a) + int(beam_a) - protons - neutrons
    expected_z = element_z[target_e.lower()] + element_z[beam_e.lower()] - protons
    if expected_a != int(residual_a) or expected_z != element_z[residual_e.lower()]:
        add(
            issues,
            "error",
            "REACTION_BALANCE",
            page.relative,
            f"reaction does not conserve A/Z: {reaction}",
        )


def validate_links(
    root: Path, pages: list[Page], issues: list[Issue]
) -> tuple[int, dict[str, int]]:
    all_markdown = sorted((root / "knowledge").rglob("*.md"))
    slug_paths: dict[str, list[str]] = defaultdict(list)
    texts: dict[str, str] = {}
    for path in all_markdown:
        relative = path.relative_to(root).as_posix()
        slug_paths[path.stem.lower()].append(relative)
        texts[relative] = path.read_text(encoding="utf-8-sig")
    for slug, paths in sorted(slug_paths.items()):
        if len(paths) > 1:
            add(issues, "error", "SLUG_DUPLICATE", ", ".join(paths), f"duplicate slug {slug!r}")

    known = set(slug_paths)
    incoming_without_index: Counter[str] = Counter()
    total = 0
    for relative, text in texts.items():
        for target in wikilinks(text):
            total += 1
            target_slug = Path(target.replace("\\", "/")).stem.lower()
            if target_slug not in known:
                add(issues, "error", "WIKILINK_BROKEN", relative, f"unresolved [[{target}]]")
            elif relative != "knowledge/index.md":
                incoming_without_index[target_slug] += 1

    index_text = texts.get("knowledge/index.md", "")
    indexed = {
        Path(target.replace("\\", "/")).stem.lower() for target in wikilinks(index_text)
    }
    for page in pages:
        if page.slug.lower() not in indexed:
            add(issues, "error", "INDEX_MISSING", page.relative, "not linked from knowledge/index.md")
        if incoming_without_index[page.slug.lower()] == 0:
            add(issues, "warning", "ORPHAN_PAGE", page.relative, "no inbound knowledge link outside index")
    return total, dict(incoming_without_index)


def validate_aliases(pages: list[Page], issues: list[Issue]) -> None:
    identities: dict[str, set[str]] = defaultdict(set)
    for page in pages:
        identities[page.slug.casefold()].add(page.relative)
        title = str(page.meta.get("title", "")).strip().casefold()
        if title:
            identities[title].add(page.relative)
        aliases = page.meta.get("aliases", [])
        if isinstance(aliases, list):
            for alias in aliases:
                normalized = str(alias).strip().casefold()
                if normalized:
                    identities[normalized].add(page.relative)
    for identity, paths in sorted(identities.items()):
        if len(paths) > 1:
            add(
                issues,
                "warning",
                "ALIAS_COLLISION",
                ", ".join(sorted(paths)),
                f"identity/alias {identity!r} belongs to multiple pages",
            )


def validate_unique_sources(pages: list[Page], issues: list[Issue]) -> None:
    for field in ("canonical_source", "raw_file"):
        values: dict[str, list[str]] = defaultdict(list)
        for page in pages:
            if page.expected_type == "source":
                value = str(page.meta.get(field, "")).strip().casefold()
                if value:
                    values[value].append(page.relative)
        for value, paths in values.items():
            if len(paths) > 1:
                add(
                    issues,
                    "error",
                    "SOURCE_DUPLICATE",
                    ", ".join(paths),
                    f"duplicate {field}: {value}",
                )


def audit_governance(
    pages: list[Page], config: dict[str, Any], issues: list[Issue]
) -> GovernanceMetrics:
    fields = config["governance_fields"]
    metrics = GovernanceMetrics()
    for page in pages:
        if page.meta.get("review_status") == "unreviewed":
            metrics.page_unreviewed += 1
        if page.expected_type != "source":
            continue
        if page.meta.get("review_status") == "unreviewed":
            metrics.source_unreviewed += 1
        if value_missing(page.meta, fields["raw_file"]):
            metrics.source_missing_raw_file += 1
        if value_missing(page.meta, fields["citation_key"]):
            metrics.source_missing_citation_key += 1
            add(
                issues,
                "warning",
                "CITATION_KEY_MISSING",
                page.relative,
                "source has no citation_key",
            )

        for line_number, row in claim_rows(page.body, config):
            metrics.claims_total += 1
            claim_id = row.get("ID", "").strip() or f"line {line_number}"
            kind = row.get(fields["claim_kind"], "").strip()
            locator = row.get(fields["locator"], "").strip()
            needs_review = row.get(fields["needs_review"], "").strip().casefold()
            if not kind:
                metrics.claim_missing_kind += 1
                add(
                    issues,
                    "error",
                    "CLAIM_KIND_MISSING",
                    page.relative,
                    f"{claim_id} has no {fields['claim_kind']}",
                )
            if not locator:
                metrics.claim_missing_locator += 1
                add(
                    issues,
                    "error",
                    "CLAIM_LOCATOR_MISSING",
                    page.relative,
                    f"{claim_id} has no locator",
                )
            if needs_review == "true":
                metrics.claim_needs_review += 1
                add(
                    issues,
                    "info",
                    "CLAIM_NEEDS_REVIEW",
                    page.relative,
                    f"{claim_id} awaits human review",
                )
    return metrics


def find_git() -> str | None:
    discovered = shutil.which("git")
    if discovered:
        return discovered
    candidates = [
        Path(sys.executable).resolve().parent.parent / "native" / "git" / "cmd" / "git.exe",
        Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Git" / "cmd" / "git.exe",
    ]
    return next((str(path) for path in candidates if path.is_file()), None)


def run_git(root: Path, args: list[str]) -> subprocess.CompletedProcess[str] | None:
    git = find_git()
    if not git:
        return None
    return subprocess.run(
        [git, *args],
        cwd=root,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=False,
    )


def validate_git(root: Path, pages: list[Page], issues: list[Issue]) -> None:
    status = run_git(root, ["status", "--porcelain", "--untracked-files=all", "--", "raw"])
    if status is None:
        add(issues, "warning", "GIT_UNAVAILABLE", ".", "git unavailable; raw change check not executed")
        return
    if status.returncode != 0:
        add(issues, "warning", "GIT_STATUS", ".", status.stderr.strip() or "git status failed")
    elif status.stdout.strip():
        changed = ", ".join(line[3:] for line in status.stdout.splitlines())
        add(issues, "warning", "RAW_GIT_CHANGE", "raw", f"working tree contains raw changes: {changed}")

    relative_paths = [page.relative for page in pages]
    git = find_git()
    if git:
        ignored = subprocess.run(
            [git, "check-ignore", "--stdin"],
            cwd=root,
            input="\n".join(relative_paths) + "\n",
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            check=False,
        )
        for path in ignored.stdout.splitlines():
            add(issues, "error", "KNOWLEDGE_IGNORED", path, "formal knowledge page is gitignored")


def validate_system(root: Path, config: dict[str, Any], issues: list[Issue]) -> None:
    for relative in config["required_paths"]:
        if not (root / relative).is_file():
            add(issues, "error", "PATH_REQUIRED", relative, "required file missing")
    system_root = root / "system"
    for path in sorted(system_root.rglob("*.md")):
        if "templates" in path.parts:
            continue
        relative = path.relative_to(root).as_posix()
        meta, _, errors = parse_frontmatter_text(path.read_text(encoding="utf-8-sig"))
        for error in errors:
            add(issues, "error", "SYSTEM_FRONTMATTER", relative, error)
        if meta.get("graph-excluded") is not True:
            add(issues, "error", "SYSTEM_GRAPH", relative, "graph-excluded must be true")


def load_config(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def run_lint(root: Path, config_path: Path, check_git: bool = True) -> Report:
    root = root.resolve()
    config = load_config(config_path)
    issues: list[Issue] = []
    pages: list[Page] = []
    hashes_checked = 0

    validate_system(root, config, issues)
    for directory, expected_type in config["knowledge_types"].items():
        folder = root / "knowledge" / directory
        if not folder.is_dir():
            add(issues, "error", "TYPE_DIRECTORY_MISSING", folder.as_posix(), "directory missing")
            continue
        for path in sorted(folder.glob("*.md")):
            page, read_issues = read_page(path, root, expected_type)
            pages.append(page)
            issues.extend(read_issues)
            validate_page(page, config, issues)
            if expected_type == "source":
                hashes_checked += validate_source(page, root, config, issues)
            elif expected_type == "nucleus":
                validate_nucleus(page, config, issues)
            elif expected_type == "experiment":
                validate_experiment(page, config, issues)

    validate_aliases(pages, issues)
    validate_unique_sources(pages, issues)
    governance = audit_governance(pages, config, issues)
    link_count, _ = validate_links(root, pages, issues)
    if check_git:
        validate_git(root, pages, issues)

    issues.sort(
        key=lambda item: (-SEVERITY_ORDER[item.severity], item.path.casefold(), item.code)
    )
    return Report(
        root=str(root),
        checked_at=date.today().isoformat(),
        pages=len(pages),
        wikilinks=link_count,
        source_hashes_checked=hashes_checked,
        governance=governance,
        issues=issues,
    )


def report_as_text(report: Report) -> str:
    lines: list[str] = []
    for issue in report.issues:
        lines.append(
            f"[{issue.severity.upper():7}] {issue.code:22} {issue.path} - {issue.message}"
        )
    counts = report.counts
    governance = report.governance
    lines.append(
        "GOVERNANCE "
        f"page_unreviewed={governance.page_unreviewed} "
        f"source_unreviewed={governance.source_unreviewed} "
        f"claims={governance.claims_total} "
        f"claim_needs_review={governance.claim_needs_review} "
        f"claim_missing_locator={governance.claim_missing_locator} "
        f"claim_missing_kind={governance.claim_missing_kind} "
        f"source_missing_raw_file={governance.source_missing_raw_file} "
        f"source_missing_citation_key={governance.source_missing_citation_key}"
    )
    lines.append(
        "SUMMARY "
        f"pages={report.pages} wikilinks={report.wikilinks} "
        f"hashes={report.source_hashes_checked} "
        f"errors={counts['error']} warnings={counts['warning']} info={counts['info']}"
    )
    return "\n".join(lines)


def report_as_json(report: Report) -> str:
    payload = {
        "root": report.root,
        "checked_at": report.checked_at,
        "pages": report.pages,
        "wikilinks": report.wikilinks,
        "source_hashes_checked": report.source_hashes_checked,
        "governance": asdict(report.governance),
        "counts": dict(report.counts),
        "issues": [asdict(issue) for issue in report.issues],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def build_parser() -> argparse.ArgumentParser:
    default_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=default_root, help="Wiki repository root")
    parser.add_argument("--config", type=Path, help="Lint JSON configuration")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--output", type=Path, help="Write report to a file")
    parser.add_argument(
        "--fail-on",
        choices=("error", "warning", "never"),
        default="error",
        help="Exit nonzero at this severity (default: error)",
    )
    parser.add_argument("--no-git", action="store_true", help="Skip working-tree checks")
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    config = (args.config or root / "system" / "lint-config.json").resolve()
    report = run_lint(root, config, check_git=not args.no_git)
    rendered = report_as_json(report) if args.format == "json" else report_as_text(report)
    if args.output:
        output = args.output if args.output.is_absolute() else root / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return report.exit_code(args.fail_on)


if __name__ == "__main__":
    raise SystemExit(main())
