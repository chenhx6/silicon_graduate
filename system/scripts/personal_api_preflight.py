#!/usr/bin/env python3
"""Check the personal ORCID, CORE and IEEE API settings without printing secrets."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import urllib.error
import urllib.parse
import urllib.request

from personal_api_env import read_dotenv


USER_AGENT = "silicon-graduate-wiki-api-preflight/1.0"


def request_json(
    url: str, headers: dict[str, str] | None = None
) -> tuple[int, str, dict | list | None, str]:
    request_headers = {"Accept": "application/json", "User-Agent": USER_AGENT}
    request_headers.update(headers or {})
    request = urllib.request.Request(url, headers=request_headers)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            raw = response.read(2_000_000)
            try:
                payload = json.loads(raw.decode("utf-8"))
            except json.JSONDecodeError:
                payload = None
            return response.status, response.headers.get_content_type(), payload, ""
    except urllib.error.HTTPError as exc:
        detail = exc.read(1000).decode("utf-8", "replace")
        return exc.code, exc.headers.get_content_type(), None, detail
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return 0, "", None, str(exc)


def check_orcid(orcid: str) -> dict:
    normalized = orcid.strip().rstrip("/").rsplit("/", 1)[-1]
    if not normalized:
        return {"configured": False, "status": "missing"}
    url = f"https://pub.orcid.org/v3.0/{urllib.parse.quote(normalized)}/record"
    status, content_type, payload, error = request_json(url)
    return {
        "configured": True,
        "status_code": status,
        "content_type": content_type,
        "record": status == 200 and isinstance(payload, dict),
        "orcid_suffix": normalized[-4:],
        **({"error": error[:240]} if error else {}),
    }


def check_core(api_key: str) -> dict:
    if not api_key.strip():
        return {"configured": False, "status": "missing"}
    params = urllib.parse.urlencode({"q": "nuclear structure", "limit": 1})
    url = f"https://api.core.ac.uk/v3/search/works?{params}"
    status, content_type, payload, error = request_json(
        url, {"Authorization": f"Bearer {api_key}"}
    )
    results = payload.get("results") if isinstance(payload, dict) else None
    return {
        "configured": True,
        "status_code": status,
        "content_type": content_type,
        "search_results": isinstance(results, list),
        "result_count": len(results) if isinstance(results, list) else 0,
        **({"error": error[:240]} if error else {}),
    }


def check_ieee(api_key: str) -> dict:
    if not api_key.strip():
        return {"configured": False, "status": "missing"}
    params = urllib.parse.urlencode(
        {
            "apikey": api_key,
            "format": "json",
            "max_records": 1,
            "start_record": 1,
            "querytext": "nuclear structure",
        }
    )
    url = f"https://ieeexploreapi.ieee.org/api/v1/search/articles?{params}"
    status, content_type, payload, error = request_json(url)
    articles = payload.get("articles") if isinstance(payload, dict) else None
    return {
        "configured": True,
        "status_code": status,
        "content_type": content_type,
        "article_results": isinstance(articles, list),
        "article_count": len(articles) if isinstance(articles, list) else 0,
        "total_records": payload.get("total_records")
        if isinstance(payload, dict)
        else None,
        **({"error": error[:240]} if error else {}),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--env",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "raw/personal/.env",
        help="private dotenv path",
    )
    args = parser.parse_args()

    try:
        values = read_dotenv(args.env)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"Cannot read allowlisted dotenv settings: {exc}", file=sys.stderr)
        return 2

    report = {
        "env_path": str(args.env),
        "orcid": check_orcid(values.get("USER_ORCID", "")),
        "core": check_core(values.get("CORE_API_KEY", "")),
        "ieee": check_ieee(values.get("IEEE_METADATA_API_KEY", "")),
    }
    print(json.dumps(report, ensure_ascii=True, indent=2))
    return 0 if all(
        item.get("status_code") == 200
        for item in (report["orcid"], report["core"], report["ieee"])
    ) else 1


if __name__ == "__main__":
    raise SystemExit(main())
