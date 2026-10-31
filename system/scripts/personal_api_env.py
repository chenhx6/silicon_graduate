#!/usr/bin/env python3
"""Safely load allowlisted personal API settings from the Wiki dotenv file."""
from __future__ import annotations

import shlex
from pathlib import Path


ALLOWED_VARS = frozenset(
    {
        "USER_EMAIL",
        "USER_ORCID",
        "OPENALEX_API_KEY",
        "SEMANTIC_SCHOLAR_API_KEY",
        "WEB_OF_SCIENCE_API_KEY_Institutional_Member_Plan",
        "WEB_OF_SCIENCE_API_KEY_Free_Trial_Plan",
        "ELSEVIER_API_KEY",
        "SPRINGER_META_API_KEY",
        "SPRINGER_OPEN_ACCESS_API_KEY",
        "CORE_API_KEY",
        "IEEE_METADATA_API_KEY",
    }
)

# These names are exposed to local academic-search processes. Existing
# non-empty environment values always win over the private dotenv file.
DEFAULT_MAPPINGS = (
    ("USER_EMAIL", "PUBMED_EMAIL"),
    ("USER_ORCID", "USER_ORCID"),
    ("USER_ORCID", "ORCID_ID"),
    ("OPENALEX_API_KEY", "OPENALEX_API_KEY"),
    ("SEMANTIC_SCHOLAR_API_KEY", "SEMANTIC_SCHOLAR_API_KEY"),
    ("CORE_API_KEY", "CORE_API_KEY"),
    ("IEEE_METADATA_API_KEY", "IEEE_METADATA_API_KEY"),
    ("IEEE_METADATA_API_KEY", "IEEE_API_KEY"),
)


def read_dotenv(path: Path) -> dict[str, str]:
    """Read only simple, allowlisted dotenv assignments; never execute them."""
    if not path.is_file():
        return {}

    values: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        entry = line.strip()
        if not entry or entry.startswith("#"):
            continue
        if entry.startswith("export "):
            entry = entry[7:].lstrip()
        name, separator, value = entry.partition("=")
        name = name.strip()
        if not separator or name not in ALLOWED_VARS:
            continue
        try:
            tokens = shlex.split(value, comments=True, posix=True)
        except ValueError as exc:
            raise ValueError(f"Invalid {name} quoting") from exc
        if len(tokens) > 1:
            raise ValueError(f"{name} must be a single value")
        values[name] = tokens[0] if tokens else ""
    return values


def read_api_key(path: Path, variable: str) -> str:
    """Read one allowlisted value for compatibility with existing callers."""
    if variable not in ALLOWED_VARS:
        raise ValueError("Unsupported credential variable")
    return read_dotenv(path).get(variable, "")


def apply_personal_env(
    env: dict[str, str], path: Path, mappings=DEFAULT_MAPPINGS
) -> dict[str, str]:
    """Return an environment enriched from dotenv without overwriting values."""
    values = read_dotenv(path)
    for source, target in mappings:
        if not env.get(target, "").strip() and values.get(source, "").strip():
            env[target] = values[source]
    return env
