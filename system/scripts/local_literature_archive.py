#!/usr/bin/env python3
"""Agent-internal, local-only literature catalogue. Never modifies originals.

catalog.json preserves stable accessions; index.sqlite and extracted text are
derived search aids. No network, ingestion or citation export runs implicitly.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3
import sys
import tempfile
import unicodedata
import uuid
import zipfile

HOME = Path(".agents/local-literature")
DEFAULT_ROOTS = ("raw/papers", "raw/books", "raw/theses", "raw/reports", "raw/notes")
DOCUMENTS = {".pdf", ".epub", ".djvu", ".html", ".htm", ".txt", ".md"}
EXCLUDED = {"personal", ".git", "node_modules", "__pycache__", ".venv",
            ".qmd", ".obsidian"}
EDITION_ORDER = {"published": 0, "accepted": 1, "manuscript": 2,
                 "preprint": 3, "unknown": 4}
SCHEMA = "local-literature-archive-v1"


def extractor_version(path):
    return ("html-container-v2" if Path(path).suffix.lower() in
            {".epub", ".djvu", ".html", ".htm", ".txt"} else "base-v1")


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def norm(value):
    return "".join(c for c in unicodedata.normalize("NFKC", str(value)).casefold()
                   if c.isalnum())


def doi_id(value):
    value = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "",
                   str(value).strip(), flags=re.I).lower().rstrip(".,;")
    return value if re.fullmatch(r"10\.\d+/[^\s]+", value) else ""


def arxiv_id(value):
    value = re.sub(r"^(?:arxiv:|https?://arxiv\.org/(?:abs|pdf)/)", "",
                   str(value).strip(), flags=re.I).removesuffix(".pdf")
    return re.sub(r"v\d+$", "", value.lower()) if re.fullmatch(
        r"(?:\d{4}\.\d{4,5}|[a-z-]+/\d{7})(?:v\d+)?", value, re.I) else ""


def safe_path(root, value):
    """Reject every symlink component and private path, even inside the repo."""
    value = str(value).replace("\\", "/")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("path must be repository-relative without '..'")
    if any(p in EXCLUDED or p.casefold().startswith(".env") for p in path.parts):
        raise ValueError("private or excluded path")
    if not path.parts or path.parts[0] != "raw":
        raise ValueError("only raw originals are indexable")
    current = root
    for part in path.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError("symlinks are not followed")
    if not current.resolve().is_relative_to(root):
        raise ValueError("path outside repository")
    if len(path.parts) > 1 and path.parts[1] == "data":
        if len(path.parts) < 3 or path.parts[2] != "gpt":
            raise ValueError("experimental data excluded")
    return current


def load_json(path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8-sig"))


def atomic_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".catalog-", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(data, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
        os.replace(name, path)
    finally:
        Path(name).unlink(missing_ok=True)


@contextmanager
def writer(root):
    home = root / HOME
    home.mkdir(parents=True, exist_ok=True)
    path = home / "write.lock"
    try:
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        raise RuntimeError(f"catalogue locked: {path}; inspect the writer before removing a stale lock")
    try:
        with os.fdopen(fd, "w") as stream:
            stream.write(json.dumps({"pid": os.getpid(), "started": now()}))
        yield home
    finally:
        path.unlink(missing_ok=True)


def source_metadata(page):
    text = page.read_text(encoding="utf-8-sig")
    from wiki_lint import parse_frontmatter_text
    fallback, _, errors = parse_frontmatter_text(text)
    try:
        import yaml
        header = text.split("---", 2)[1]
        metadata = yaml.safe_load(header)
        if not isinstance(metadata, dict):
            raise ValueError("frontmatter is not a mapping")
        return metadata, errors
    except (ImportError, ValueError, IndexError) as exc:
        return fallback, errors + [str(exc)]
    except Exception as exc:
        # A bad source must remain visible without poisoning the whole library.
        return fallback, errors + [f"{type(exc).__name__}: {exc}"]


def extract(path):
    info = {"readability": "readable", "page_count": None, "text": "",
            "pdf_title": "", "pdf_author": "", "edition_hint": ""}
    try:
        if path.suffix.lower() == ".pdf":
            import pymupdf
            # MuPDF's native diagnostics otherwise leak into stdout and corrupt
            # the agent JSON protocol; exceptions remain in artifact.error.
            pymupdf.TOOLS.mupdf_display_errors(False)
            pymupdf.TOOLS.mupdf_display_warnings(False)
            with pymupdf.open(path) as doc:
                if doc.needs_pass:
                    raise ValueError("password required")
                if not len(doc):
                    raise ValueError("empty PDF")
                info["page_count"] = len(doc)
                info["pdf_title"] = (doc.metadata or {}).get("title") or ""
                info["pdf_author"] = (doc.metadata or {}).get("author") or ""
                info["text"] = "\n".join(doc[i].get_text() for i in range(min(2, len(doc))))[:18000]
                if len(info["text"].strip()) < 40:
                    info["readability"] = "ocr-required"
        elif path.suffix.lower() in {".epub", ".djvu"}:
            if path.suffix.lower() == ".epub":
                with zipfile.ZipFile(path) as book:
                    if book.read("mimetype").strip() != b"application/epub+zip":
                        raise ValueError("not an EPUB container")
            else:
                with path.open("rb") as stream:
                    if stream.read(8) != b"AT&TFORM":
                        raise ValueError("not a DjVu container")
            info["readability"] = "reader-required"
        elif path.suffix.lower() in {".zip", ".gz", ".root", ".tar"}:
            info["readability"] = "container-or-data"
        else:
            with path.open("rb") as stream:
                info["text"] = stream.read(32000).decode("utf-8", errors="replace")
        text = info["text"]
        if path.suffix.lower() in {".html", ".htm", ".txt"}:
            title = re.search(r"<title[^>]*>(.*?)</title>", text, re.I | re.S)
            check = title.group(1) if title else text[:350]
            if re.search(r"access denied|403 forbidden|404 not found|just a moment|captcha|"
                         r"verify (?:you are|you're) human|request rejected", check, re.I):
                info["readability"] = "access-failure"
        if re.search(r"arxiv|preprint|accepted manuscript", path.name, re.I):
            info["edition_hint"] = "accepted" if "accepted" in path.name.lower() else "preprint"
        elif re.search(r"(?:^|[-_. ])(?:published|version-of-record)(?:[-_. ]|$)", path.name, re.I):
            info["edition_hint"] = "published"
        # PDF content is a discovery lead, never an automatically trusted DOI.
        info["identifier_leads"] = list(dict.fromkeys(
            re.findall(r"10\.\d{4,9}/[^\s<>]+", text)))[:12]
        match = re.search(r"arxiv[: _-]*(\d{4}\.\d{4,5})(?:v\d+)?",
                          path.name + "\n" + text[:1500], re.I)
        info["arxiv_lead"] = arxiv_id(match.group(1)) if match else ""
    except Exception as exc:
        info["readability"] = "unreadable"
        info["error"] = f"{type(exc).__name__}: {exc}"
    return info


class Groups:
    def __init__(self):
        self.parent = {}

    def find(self, value):
        self.parent.setdefault(value, value)
        if self.parent[value] != value:
            self.parent[value] = self.find(self.parent[value])
        return self.parent[value]

    def join(self, *values):
        values = [v for v in values if v]
        if not values:
            return
        root = self.find(values[0])
        for value in values[1:]:
            self.parent[self.find(value)] = root


def scan_files(root, roots):
    found = set()
    for relative in roots:
        start = safe_path(root, relative)
        if start.is_file():
            found.add(start.relative_to(root).as_posix())
            continue
        for parent, dirs, files in os.walk(start, followlinks=False):
            dirs[:] = [d for d in dirs if d not in EXCLUDED and
                       not (Path(parent) / d).is_symlink()]
            for name in files:
                path = Path(parent) / name
                if path.suffix.lower() not in DOCUMENTS and path.name != "manifest.json":
                    continue
                relative = path.relative_to(root).as_posix()
                try:
                    safe_path(root, relative)
                    found.add(relative)
                except ValueError:
                    pass
    return found


def rebuild_sqlite(home, catalogue):
    fd, temporary = tempfile.mkstemp(prefix=".index-", suffix=".sqlite", dir=home)
    os.close(fd)
    try:
        connection = sqlite3.connect(temporary)
        connection.execute("CREATE TABLE generation (value TEXT)")
        connection.execute("INSERT INTO generation VALUES (?)", (catalogue["generation"],))
        connection.execute("CREATE VIRTUAL TABLE search USING fts5(work_id UNINDEXED, body)")
        for work in catalogue["works"]:
            text = work["search_text"]
            for artifact in work["artifacts"]:
                cache = home / "fulltext" / (artifact.get("sha256", "") + ".txt")
                if cache.is_file():
                    text += "\n" + cache.read_text(encoding="utf-8")
            connection.execute("INSERT INTO search VALUES (?, ?)", (work["id"], text))
        connection.commit()
        connection.close()
        os.replace(temporary, home / "index.sqlite")
    finally:
        Path(temporary).unlink(missing_ok=True)


def inventory(root, roots=None):
    root = Path(root).resolve()
    with writer(root) as home:
        old = load_json(home / "catalog.json", {})
        if roots is None:
            roots = old.get("scan_roots", list(DEFAULT_ROOTS))
        old_artifacts = {a["path"]: a for w in old.get("works", []) for a in w["artifacts"]}
        old_ids = {key: w["id"] for w in old.get("works", []) for key in w["identity_keys"]}
        old_merged = {w["id"]: w.get("merged_accessions", []) for w in old.get("works", [])}
        next_id = old.get("next_accession", 1)
        overrides = load_json(home / "overrides.json", {}).get("artifacts", {})
        warnings = []
        if not isinstance(overrides, dict):
            raise ValueError("overrides.artifacts must be an object")
        overrides = dict(overrides)
        for name, override in list(overrides.items()):
            if not isinstance(override, dict) or not override.get("basis"):
                warnings.append({"path": name, "kind": "override-without-basis",
                                 "error": "Override ignored; record local source/page evidence in basis."})
                overrides.pop(name)
        groups = Groups()
        source_rows = []
        paths = scan_files(root, roots)
        for name in old_artifacts:
            if any(name == r or name.startswith(r.rstrip("/") + "/") for r in roots):
                paths.add(name)
        bindings = {}
        expected = {}
        rejected_manifests = set()
        source_dir = root / "knowledge/sources"
        if ((root / "knowledge").is_symlink() or source_dir.is_symlink() or
                not source_dir.resolve().is_relative_to(root)):
            raise ValueError("source directory symlink or path escape")
        for page in sorted(source_dir.glob("*.md")):
            if page.is_symlink() or not page.resolve().is_relative_to(source_dir.resolve()):
                warnings.append({"source": page.name, "kind": "excluded-source-symlink"})
                continue
            meta, errors = source_metadata(page)
            relative = page.relative_to(root).as_posix()
            if errors:
                warnings.append({"source": relative, "kind": "source-parse", "errors": errors})
            src = {"path": relative, "title": str(meta.get("title_original") or meta.get("title") or page.stem),
                   "authors": meta.get("authors", []), "year": str(meta.get("year", "")),
                   "doi": doi_id(meta.get("doi", "")), "arxiv": arxiv_id(meta.get("arxiv", "")),
                   "citation_key": meta.get("citation_key", ""), "reading_depth": meta.get("reading_depth", ""),
                   "source_type": str(meta.get("source_type", "")),
                   "journal": str(meta.get("journal", "")), "aliases": meta.get("aliases", []),
                   "tags": meta.get("tags", []), "role": "main", "artifact_paths": []}
            key = "source:" + relative
            identifiers = [key]
            if src["doi"]:
                identifiers.append("doi:" + src["doi"])
            if src["arxiv"]:
                identifiers.append("arxiv:" + src["arxiv"])
            groups.join(*identifiers)
            src["key"] = key
            source_rows.append(src)
            raw = meta.get("raw_file")
            if not isinstance(raw, str) or not raw:
                warnings.append({"source": relative, "kind": "no-raw-pointer"})
                continue
            try:
                rawpath = safe_path(root, raw)
                raw = rawpath.relative_to(root).as_posix()
                expected[raw] = str(meta.get("raw_sha256", ""))
                members = [{"path": raw, "role": "main", "sha256": expected[raw]}]
                if rawpath.suffix.lower() == ".json" and rawpath.is_file():
                    if expected[raw] and digest(rawpath) != expected[raw].lower():
                        warnings.append({"source": relative, "kind": "manifest-hash-mismatch"})
                        rejected_manifests.add(raw)
                        continue
                    payload = load_json(rawpath, {})
                    if isinstance(payload, dict) and isinstance(payload.get("files"), list):
                        members = payload["files"]
                # A source may cite a collection of independent papers.
                # One explicit main plus typed attachments is a same-work
                # package; otherwise keep members as identity candidates.
                explicit_main = [m for m in members if m.get("role") == "main"]
                typed_package = (len(explicit_main) == 1 and all(
                    m.get("role") in {"main", "supplement", "erratum", "license", "metadata", "translation"}
                    for m in members))
                for member in members:
                    name = member.get("path") or member.get("raw_file")
                    if not name:
                        continue
                    safe = safe_path(root, name)
                    name = safe.relative_to(root).as_posix()
                    paths.add(name)
                    expected[name] = str(member.get("sha256", ""))
                    belongs = (len(members) == 1 or typed_package or
                               member.get("source_page") == relative or
                               member.get("work_key") in {key, "doi:" + src["doi"]} or
                               bool(src["doi"] and doi_id(member.get("doi", "")) == src["doi"]))
                    if belongs:
                        src["artifact_paths"].append(name)
                        bindings.setdefault(name, []).append((src, str(member.get("role", "main"))))
                        groups.join(key, "file:" + name)
                    else:
                        src.setdefault("candidate_artifact_paths", []).append(name)
            except (ValueError, OSError, TypeError) as exc:
                warnings.append({"source": relative, "kind": "raw-pointer", "error": str(exc)})
        # A collection can contain many papers: only explicit parent/source
        # relationships bind members, never the mere shared manifest directory.
        source_by_path = {s["path"]: s for s in source_rows}
        member_roles = {}
        for name in sorted(paths.copy()):
            if not name.endswith("manifest.json") or name in bindings or name in rejected_manifests:
                continue
            try:
                payload = load_json(safe_path(root, name), {})
                for member in payload.get("files", []):
                    target = member.get("path")
                    if target:
                        safe_path(root, target)
                        paths.add(target)
                        member_roles[target] = str(member.get("role", "main"))
                        parent = source_by_path.get(member.get("source_page"))
                        # Standalone collections cannot invent a new main
                        # artifact for an existing source merely by naming it.
                        if parent is not None and (
                                target in parent["artifact_paths"] or
                                member_roles[target] in {"license", "supplement", "erratum", "metadata", "translation"}):
                            bindings.setdefault(target, []).append((parent, member_roles[target]))
                            groups.join(parent["key"], "file:" + target)
            except (ValueError, OSError, TypeError, AttributeError) as exc:
                warnings.append({"path": name, "kind": "manifest", "error": str(exc)})
        artifacts = {}
        reextracted = 0
        for name in sorted(paths | set(overrides)):
            try:
                path = safe_path(root, name)
            except ValueError as exc:
                warnings.append({"path": name, "kind": "excluded", "error": str(exc)})
                continue
            # Index a manifest's members, not the JSON as a pretend full text.
            if name.endswith("manifest.json"):
                continue
            key = "file:" + name
            groups.find(key)
            override = overrides.get(name, {})
            srcs = bindings.get(name, [])
            role = override.get("role") or (srcs[0][1] if srcs else member_roles.get(name, "main"))
            if role == "main" and re.search(r"(?:supplement|supp[-_]|erratum|corrigendum)", path.stem, re.I):
                role = "erratum" if re.search("erratum|corrigendum", path.stem, re.I) else "supplement"
            metadata_only = bool(srcs and all(
                any(t in src["source_type"] for t in ("metadata", "abstract", "journal-instructions"))
                for src, _ in srcs))
            artifact = {"path": name, "role": role, "metadata_only": metadata_only,
                        "expected_sha256": expected.get(name, ""), "edition": override.get("edition", "unknown"),
                        "exists": path.is_file(), "readability": "missing", "sha256": "",
                        "extractor_version": extractor_version(path)}
            if artifact["exists"]:
                stat = path.stat()
                signature = [stat.st_size, stat.st_mtime_ns]
                cached = old_artifacts.get(name)
                if (cached and cached.get("signature") == signature and
                        cached.get("extractor_version", "base-v1") == extractor_version(path)):
                    for field in ("sha256", "extraction", "readability", "signature"):
                        artifact[field] = cached[field]
                else:
                    before = signature
                    artifact["sha256"] = digest(path)
                    artifact["extraction"] = extract(path)
                    stat = path.stat()
                    if before != [stat.st_size, stat.st_mtime_ns]:
                        raise ValueError("file changed during extraction; refresh again")
                    artifact["signature"] = before
                    artifact["readability"] = artifact["extraction"]["readability"]
                    reextracted += 1
                if artifact["readability"] == "access-failure":
                    artifact["metadata_only"] = True
                groups.join(key, "bytes:" + artifact["sha256"])
                if artifact["expected_sha256"] and artifact["sha256"] != artifact["expected_sha256"].lower():
                    artifact["identity_conflict"] = True
                    warnings.append({"path": name, "kind": "recorded-hash-mismatch"})
                hint = artifact["extraction"].get("edition_hint")
                if artifact["edition"] == "unknown":
                    if hint:
                        artifact["edition"] = hint
                    elif any("manuscript" in src["source_type"] for src, _ in srcs):
                        artifact["edition"] = "manuscript"
                lead = artifact["extraction"].get("arxiv_lead")
                # A printed arXiv ID is a candidate until a source/override ties it
                # to this artifact, or it appears explicitly in its filename.
                if lead and norm(lead) in norm(path.name):
                    groups.join(key, "arxiv:" + lead)
            elif name in old_artifacts and old_artifacts[name].get("sha256"):
                artifact["sha256"] = old_artifacts[name]["sha256"]
                groups.join(key, "bytes:" + artifact["sha256"])
            if override.get("work_key"):
                groups.join(key, str(override["work_key"]))
            if override.get("parent_work_key"):
                groups.join(key, str(override["parent_work_key"]))
            for field, normalize in (("doi", doi_id), ("arxiv", arxiv_id)):
                value = normalize(override.get(field, ""))
                if value:
                    groups.join(key, field + ":" + value)
            artifact["override"] = override
            artifacts[name] = artifact
        buckets = {}
        for name, artifact in artifacts.items():
            buckets.setdefault(groups.find("file:" + name), {"artifacts": [], "sources": []})["artifacts"].append(artifact)
        for src in source_rows:
            buckets.setdefault(groups.find(src["key"]), {"artifacts": [], "sources": []})["sources"].append(src)
        keys_by_bucket = {representative: sorted(k for k in groups.parent if groups.find(k) == representative)
                          for representative in buckets}
        # On a split, a prior accession can belong to only one new component.
        # Retain it with the strongest surviving registered/byte identity.
        owners = {}
        for representative, keys in keys_by_bucket.items():
            scores = {}
            for key in keys:
                if key in old_ids:
                    weight = 10 if key.startswith(("doi:", "arxiv:")) else 4 if key.startswith("bytes:") else 3 if key.startswith("source:") else 1
                    scores[old_ids[key]] = scores.get(old_ids[key], 0) + weight
            for old_id, score in scores.items():
                candidate = (-score, representative)
                if old_id not in owners or candidate < owners[old_id]:
                    owners[old_id] = candidate
        works = []
        for representative, bucket in sorted(buckets.items()):
            keys = keys_by_bucket[representative]
            prior = sorted({old_ids[k] for k in keys if k in old_ids and
                            owners[old_ids[k]][1] == representative})
            accession = prior[0] if prior else f"LIT-{next_id:06d}"
            if not prior:
                next_id += 1
            sources = bucket["sources"]
            primary = next((s for s in sources if not re.search(
                r"erratum|corrigendum", s["source_type"], re.I)), sources[0] if sources else {})
            files = bucket["artifacts"]
            override = next((a["override"] for a in files if a["override"].get("title")), {})
            first = next((a for a in files if a["exists"]), {})
            title = override.get("title") or primary.get("title")
            if not title:
                extraction = first.get("extraction", {})
                title = extraction.get("pdf_title") or Path(first.get("path", representative)).stem
            usable = sorted((a for a in files if is_usable(a)), key=preference)
            preferred = usable[0]["path"] if usable else None
            editions = {a["edition"] for a in files if a["role"] == "main"}
            canonical = "published" if "published" in editions or any(
                s["journal"] and s["doi"] for s in sources) else next(
                    (e for e in EDITION_ORDER if e in editions), "unknown")
            search_text = "\n".join([str(title)] + [json.dumps(s, ensure_ascii=False) for s in sources] +
                                    [a["path"] + "\n" + a.get("extraction", {}).get("text", "") for a in files])
            merged = sorted((set(prior[1:]) | {alias for old_id in prior
                              for alias in old_merged.get(old_id, [])}) - {accession})
            works.append({"id": accession, "merged_accessions": merged,
                          "identity_keys": keys, "title": title,
                          "canonical_edition": canonical, "preferred_artifact": preferred,
                          "artifacts": files, "sources": sources, "search_text": search_text})
        catalogue = {"schema": SCHEMA, "generation": uuid.uuid4().hex,
                     "updated_at": now(), "scan_roots": list(roots), "next_accession": next_id,
                     "refresh": {"files_reextracted": reextracted}, "warnings": warnings,
                     "works": works}
        # Two atomic snapshots; query checks their generation before using FTS.
        atomic_json(home / "catalog.json", catalogue)
        try:
            rebuild_sqlite(home, catalogue)
        except sqlite3.Error as exc:
            catalogue["warnings"].append({"kind": "fts-unavailable", "error": str(exc)})
            atomic_json(home / "catalog.json", catalogue)
        return catalogue


def preference(artifact):
    return (EDITION_ORDER.get(artifact["edition"], 5),
            artifact["readability"] != "readable", artifact["path"])


def is_usable(artifact):
    return (artifact.get("exists") and artifact.get("role") == "main" and
            not artifact.get("metadata_only") and not artifact.get("identity_conflict") and
            artifact.get("readability") not in {"missing", "unreadable"})


def load_catalog(root):
    return load_json(Path(root) / HOME / "catalog.json", None)


def find(root, query="", doi="", arxiv="", limit=10):
    root = Path(root).resolve()
    if not doi and not arxiv:
        if doi_id(query):
            doi, query = query, ""
        elif arxiv_id(query):
            arxiv, query = query, ""
    catalogue = load_catalog(root)
    if not catalogue:
        return {"status": "index-incomplete", "results": [], "reason": "inventory required"}
    exact = "doi:" + doi_id(doi) if doi else "arxiv:" + arxiv_id(arxiv) if arxiv else ""
    tokens = re.findall(r"\w+", unicodedata.normalize("NFKC", query).casefold())
    ranked = {}
    fts_used = False
    if tokens and not exact and (root / HOME / "index.sqlite").is_file():
        try:
            connection = sqlite3.connect((root / HOME / "index.sqlite").as_uri() + "?mode=ro", uri=True)
            try:
                generation = connection.execute("SELECT value FROM generation").fetchone()[0]
                if generation == catalogue["generation"]:
                    phrase = " AND ".join('"' + token.replace('"', '""') + '"' for token in tokens)
                    ranked = {row[0]: -row[1] for row in connection.execute(
                        "SELECT work_id, bm25(search) FROM search WHERE search MATCH ? ORDER BY bm25(search)",
                        (phrase,))}
                    fts_used = True
            finally:
                connection.close()
        except sqlite3.Error:
            pass
    results = []
    for work in catalogue["works"]:
        identifier_candidate = False
        if exact and exact not in work["identity_keys"]:
            leads = []
            for artifact in work["artifacts"]:
                extracted = artifact.get("extraction", {})
                leads.extend("doi:" + doi_id(v) for v in extracted.get("identifier_leads", []))
                if extracted.get("arxiv_lead"):
                    leads.append("arxiv:" + extracted["arxiv_lead"])
            if exact not in leads:
                continue
            identifier_candidate = True
        if tokens and not exact:
            if fts_used:
                if (work["id"] not in ranked and
                        not all(norm(t) in norm(work["search_text"]) for t in tokens)):
                    continue
            elif not all(norm(t) in norm(work["search_text"]) for t in tokens):
                continue
        item = {k: v for k, v in work.items() if k != "search_text"}
        item["match_basis"] = ("unverified-identifier-mention" if identifier_candidate else
                               "registered-identifier" if exact else "metadata-or-indexed-text")
        item["score"] = 0 if identifier_candidate else ranked.get(work["id"], 1)
        requested_paths = set()
        if exact:
            for source in item["sources"]:
                if exact in {"doi:" + source["doi"], "arxiv:" + source["arxiv"]}:
                    requested_paths.update(source["artifact_paths"])
        usable = []
        changed = False
        for artifact in item["artifacts"]:
            requested_attachment = (artifact["path"] in requested_paths and
                artifact["role"] in {"erratum", "supplement", "translation"} and
                artifact["exists"] and not artifact.get("metadata_only") and
                not artifact.get("identity_conflict") and
                artifact["readability"] not in {"missing", "unreadable"})
            if not is_usable(artifact) and not requested_attachment:
                continue
            try:
                path = safe_path(root, artifact["path"])
                stat = path.stat()
                if artifact.get("signature") != [stat.st_size, stat.st_mtime_ns]:
                    changed = True
                    continue
                usable.append(artifact)
            except (ValueError, OSError):
                changed = True
        usable.sort(key=lambda a: (bool(requested_paths) and a["path"] not in requested_paths,
                                   preference(a)))
        if usable:
            # Validate actual selected bytes; mtime is only an indexing hint.
            selected = usable[0]
            if digest(safe_path(root, selected["path"])) != selected["sha256"]:
                usable = []
                changed = True
        item["preferred_artifact"] = usable[0]["path"] if usable else None
        candidate_paths = [p for s in item["sources"] for p in s.get("candidate_artifact_paths", [])]
        has_candidates = False
        for path in candidate_paths:
            try:
                has_candidates = has_candidates or safe_path(root, path).is_file()
            except ValueError:
                pass
        item["status"] = ("found-usable" if usable else "index-incomplete" if changed else
                          "candidate-needs-identification" if has_candidates or any(a.get("identity_conflict") for a in item["artifacts"]) else
                          "unreadable" if any(a.get("exists") and not a.get("metadata_only")
                                              for a in item["artifacts"]) else "metadata-only")
        item["actual_edition"] = usable[0]["edition"] if usable else None
        if identifier_candidate:
            item["status"] = "candidate-needs-identification"
            item["candidate_artifact_paths"] = [a["path"] for a in item["artifacts"]]
            item["preferred_artifact"] = None
            item["actual_edition"] = None
            item["identity_boundary"] = "Identifier mention can be a reference; inspect the paper identity before reuse."
        results.append(item)
    results.sort(key=lambda w: (w["status"] != "found-usable", -w["score"], w["id"]))
    selected = results[:limit]
    status = selected[0]["status"] if selected else "missing"
    return {"status": status, "results": selected, "index_updated_at": catalogue["updated_at"],
            "scope": catalogue["scan_roots"], "absence_boundary": "no match in this catalogue snapshot"}


def stats(root):
    catalogue = load_catalog(root)
    if not catalogue:
        return {"status": "index-incomplete"}
    works = catalogue["works"]
    artifacts = [a for w in works for a in w["artifacts"]]
    return {"status": "indexed", "updated_at": catalogue["updated_at"],
            "scan_roots": catalogue["scan_roots"], "works": len(works),
            "artifacts": len(artifacts), "with_sources": sum(bool(w["sources"]) for w in works),
            "source_records": sum(len(w["sources"]) for w in works),
            "published_editions_identified_locally": sum(any(is_usable(a) and a["edition"] == "published"
                                       for a in w["artifacts"]) for w in works),
            "publication_known_bibliographically": sum(w["canonical_edition"] == "published" for w in works),
            "local_edition_unclassified": sum(a["exists"] and a["edition"] == "unknown"
                                             for a in artifacts if a["role"] == "main"),
            "preprint_only_locally": sum(bool(w["preferred_artifact"]) and
                all(a["edition"] == "preprint" for a in w["artifacts"] if is_usable(a)) for w in works),
            "attachments": sum(a["role"] != "main" for a in artifacts),
            "missing_paths": sum(not a["exists"] for a in artifacts),
            "unreadable": sum(a["readability"] == "unreadable" for a in artifacts),
            "warnings": catalogue["warnings"], "refresh": catalogue["refresh"]}


def index_text(root, relative):
    root = Path(root).resolve()
    with writer(root) as home:
        catalogue = load_catalog(root)
        if not catalogue:
            raise ValueError("inventory required")
        artifact = next((a for w in catalogue["works"] for a in w["artifacts"]
                         if a["path"] == relative), None)
        if not artifact:
            raise ValueError("path not present in the catalogue")
        path = safe_path(root, relative)
        if digest(path) != artifact["sha256"]:
            raise ValueError("bytes changed; refresh and recheck identity")
        import pymupdf
        pymupdf.TOOLS.mupdf_display_errors(False)
        pymupdf.TOOLS.mupdf_display_warnings(False)
        with pymupdf.open(path) as doc:
            text = "\n".join(f"\n[PDF page {i+1}]\n" + page.get_text()
                             for i, page in enumerate(doc))
        cache = home / "fulltext" / (artifact["sha256"] + ".txt")
        cache.parent.mkdir(exist_ok=True)
        fd, temporary = tempfile.mkstemp(prefix=".text-", dir=cache.parent)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as stream:
                stream.write(text)
            os.replace(temporary, cache)
        finally:
            Path(temporary).unlink(missing_ok=True)
        rebuild_sqlite(home, catalogue)
        return {"path": relative, "sha256": artifact["sha256"],
                "indexed_characters": len(text), "reading_credit": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["inventory", "refresh", "find", "check-local", "stats", "index-text"])
    parser.add_argument("--root", default=".")
    parser.add_argument("--scan-root", action="append")
    parser.add_argument("--query", default="")
    parser.add_argument("--doi", default="")
    parser.add_argument("--arxiv", default="")
    parser.add_argument("--path")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--json", action="store_true", help="Compatibility: output is always JSON")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    try:
        if args.action in {"inventory", "refresh"}:
            inventory(root, args.scan_root)
            result = stats(root)
        elif args.action in {"find", "check-local"}:
            if not (args.query or args.doi or args.arxiv):
                parser.error("provide --query, --doi or --arxiv")
            result = find(root, args.query, args.doi, args.arxiv, args.limit)
        elif args.action == "index-text":
            if not args.path:
                parser.error("--path required")
            result = index_text(root, args.path)
        else:
            result = stats(root)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError, RuntimeError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "error", "error": str(exc)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
