#!/usr/bin/env python3
"""Discover public GitHub Agent capabilities and save pinned files for review."""

import argparse
import base64
import binascii
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import tempfile
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import HTTPRedirectHandler, Request, build_opener


API = "https://api.github.com"
ROOT = Path(__file__).resolve().parents[4]
CACHE = ROOT / "tmp" / "agent-capability-learning" / "github"
REPOSITORY = re.compile(r"[A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9_.-]+")
OBJECT_ID = re.compile(r"[0-9a-f]{40}")
MAX_RESPONSE = 8 * 1024 * 1024
MAX_BLOB = 1024 * 1024
MAX_FILES = 12


class GitHubError(Exception):
    pass


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, response, code, message, headers, new_url):
        return None


def get_json(path, **query):
    url = API + path
    if query:
        url += "?" + urlencode(query)
    request = Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "wiki-evolution",
    })
    try:
        with build_opener(NoRedirect()).open(request, timeout=15) as response:
            content = response.read(MAX_RESPONSE + 1)
    except HTTPError as error:
        raise GitHubError(f"{path}: GitHub HTTP {error.code} ({error.reason})") from error
    except (URLError, TimeoutError) as error:
        raise GitHubError(f"{path}: {error}") from error
    if len(content) > MAX_RESPONSE:
        raise GitHubError(f"{path}: response exceeds {MAX_RESPONSE} bytes")
    try:
        return json.loads(content)
    except (UnicodeError, json.JSONDecodeError) as error:
        raise GitHubError(f"{path}: GitHub returned invalid JSON") from error


def repository_path(repository):
    if not REPOSITORY.fullmatch(repository) or repository.split("/")[1] in {".", ".."}:
        raise GitHubError("expected a GitHub repository in OWNER/REPO form")
    return f"/repos/{repository}"


def object_id(value):
    if not OBJECT_ID.fullmatch(value):
        raise GitHubError("expected a full Git SHA in lowercase hexadecimal")
    return value


def repository_info(data):
    return {
        "repository": data["full_name"],
        "url": data["html_url"],
        "description": data.get("description"),
        "stars": data.get("stargazers_count"),
        "pushed_at": data.get("pushed_at"),
        "archived": data.get("archived", False),
        "license_hint": (data.get("license") or {}).get("spdx_id"),
    }


def search(query, limit, sort):
    result = get_json(
        "/search/repositories", q=query, per_page=limit, sort=sort, order="desc",
    )
    return {
        "query": query, "sort": sort, "total_count": result["total_count"],
        "incomplete_results": result["incomplete_results"],
        "repositories": [repository_info(item) for item in result["items"]],
    }


def read_tree(repository, ref=None):
    endpoint = repository_path(repository)
    repo = get_json(endpoint)
    commit = get_json(f"{endpoint}/commits/{quote(ref or repo['default_branch'], safe='')}")
    revision = object_id(commit["sha"])
    if ref and OBJECT_ID.fullmatch(ref) and ref != revision:
        raise GitHubError("GitHub returned a different commit")
    tree_sha = object_id(commit["commit"]["tree"]["sha"])
    tree = get_json(f"{endpoint}/git/trees/{tree_sha}", recursive=1)
    if tree["sha"] != tree_sha:
        raise GitHubError("GitHub returned a different tree")
    return {**repository_info(repo), "commit": revision, "tree_truncated": tree["truncated"]}, tree["tree"]


def entry_kind(path):
    parts = PurePosixPath(path).parts
    name = parts[-1].lower()
    if name == "skill.md":
        return "skill"
    if name == "hooks.json" or "hooks" in parts[:-1] or path in {".claude/settings.json", ".codex/config.toml"}:
        return "hook-or-config"
    if name == "plugin.json":
        return "plugin"
    if name.startswith(("readme", "license", "copying", "notice")):
        return "docs-or-license"
    if path.startswith(".github/workflows/"):
        return "workflow"
    return None


def inspect(repo, ref, prefix):
    info, tree = read_tree(repo, ref)
    files = []
    for entry in tree:
        path = entry["path"]
        kind = entry_kind(path) if path.startswith(prefix) and entry["type"] == "blob" else None
        if kind:
            files.append({"path": path, "kind": kind, "size": entry.get("size"), "mode": entry["mode"]})
    return {**info, "prefix": prefix, "matching_files": len(files), "files": files[:100]}


def fetch_blob(endpoint, entry):
    sha = object_id(entry["sha"])
    response = get_json(f"{endpoint}/git/blobs/{sha}")
    if response["sha"] != sha or response["encoding"] != "base64":
        raise GitHubError(f"unexpected Git blob for {entry['path']!r}")
    try:
        content = base64.b64decode("".join(response["content"].split()), validate=True)
    except (ValueError, binascii.Error) as error:
        raise GitHubError(f"invalid Base64 for {entry['path']!r}") from error
    git_header = f"blob {len(content)}\0".encode("ascii")
    if len(content) != entry["size"] or hashlib.sha1(git_header + content).hexdigest() != sha:
        raise GitHubError(f"size or Git blob hash mismatch for {entry['path']!r}")
    return content


def fetch(repo, commit, paths, cache=CACHE):
    object_id(commit)
    if not 1 <= len(paths) <= MAX_FILES or len(set(paths)) != len(paths):
        raise GitHubError(f"select 1–{MAX_FILES} distinct files")
    endpoint = repository_path(repo)
    info, tree = read_tree(repo, commit)
    by_path = {entry["path"]: entry for entry in tree}
    entries = []
    for path in paths:
        entry = by_path.get(path)
        if not entry:
            boundary = " (GitHub tree is truncated)" if info["tree_truncated"] else ""
            raise GitHubError(f"file absent from pinned tree: {path!r}{boundary}")
        if entry["type"] != "blob" or entry["mode"] not in {"100644", "100755"}:
            raise GitHubError(f"only regular Git files can be sampled: {path!r}")
        if not 0 <= entry["size"] <= MAX_BLOB:
            raise GitHubError(f"file exceeds {MAX_BLOB} bytes: {path!r}")
        entries.append(entry)

    contents = [fetch_blob(endpoint, entry) for entry in entries]
    if cache == CACHE and not cache.resolve().is_relative_to((ROOT / "tmp").resolve()):
        raise GitHubError("sample directory resolves outside the Wiki tmp directory")
    cache.mkdir(parents=True, exist_ok=True)
    directory = Path(tempfile.mkdtemp(prefix=f"{repo.replace('/', '--')}-{commit[:12]}-", dir=cache))
    files = []
    for number, (entry, content) in enumerate(zip(entries, contents), start=1):
        name = f"{number:02d}.blob"
        path = entry["path"]
        (directory / name).write_bytes(content)
        files.append({
            "path": path, "local_file": name, "size": len(content), "git_mode": entry["mode"],
            "url": f"https://github.com/{repo}/blob/{commit}/{quote(path, safe='/')}",
            "git_blob_sha": entry["sha"], "sha256": hashlib.sha256(content).hexdigest(),
        })
    result = {**info, "retrieved_at": datetime.now(timezone.utc).isoformat(), "files": files}
    manifest = directory / "manifest.json"
    manifest.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {**result, "manifest": str(manifest)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    search_cmd = commands.add_parser("search", help="search public repositories")
    search_cmd.add_argument("query")
    search_cmd.add_argument("--limit", type=int, choices=range(1, 11), default=6)
    search_cmd.add_argument("--sort", choices=("stars", "updated"), default="stars")
    inspect_cmd = commands.add_parser("inspect", help="resolve a commit and list reviewable file paths")
    inspect_cmd.add_argument("repo")
    inspect_cmd.add_argument("--ref")
    inspect_cmd.add_argument("--prefix", default="")
    fetch_cmd = commands.add_parser("fetch", help="save explicit files from a full commit SHA")
    fetch_cmd.add_argument("repo")
    fetch_cmd.add_argument("commit")
    fetch_cmd.add_argument("paths", nargs="+")
    args = parser.parse_args()
    try:
        if args.command == "search":
            result = search(args.query, args.limit, args.sort)
        elif args.command == "inspect":
            result = inspect(args.repo, args.ref, args.prefix)
        else:
            result = fetch(args.repo, args.commit, args.paths)
    except (GitHubError, OSError, KeyError, TypeError) as error:
        parser.exit(1, f"github_learning: {error}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
