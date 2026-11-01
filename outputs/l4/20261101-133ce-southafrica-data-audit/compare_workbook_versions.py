#!/usr/bin/env python3
from datetime import datetime
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile
from zoneinfo import ZoneInfo

import openpyxl


ROOT = Path(__file__).resolve().parents[3]
FIRST = ROOT / "raw/data/SouthAfrica/133Ce/analysis/intensity.xlsx"
SECOND = ROOT / "raw/data/SouthAfrica/133Ce/analysis/intensity_iThemba2019_export.xlsx"
OUTPUT = Path(__file__).with_name("workbook-version-audit.json")


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compare_cells(data_only):
    first = openpyxl.load_workbook(FIRST, read_only=True, data_only=data_only)
    second = openpyxl.load_workbook(SECOND, read_only=True, data_only=data_only)
    differences = []
    checked_cells = 0
    for name in sorted(set(first.sheetnames) | set(second.sheetnames)):
        if name not in first.sheetnames or name not in second.sheetnames:
            differences.append({"sheet": name, "kind": "missing-sheet"})
            continue
        first_rows = list(first[name].iter_rows(values_only=True))
        second_rows = list(second[name].iter_rows(values_only=True))
        for row in range(max(len(first_rows), len(second_rows))):
            first_values = first_rows[row] if row < len(first_rows) else ()
            second_values = second_rows[row] if row < len(second_rows) else ()
            for column in range(max(len(first_values), len(second_values))):
                first_value = first_values[column] if column < len(first_values) else None
                second_value = second_values[column] if column < len(second_values) else None
                checked_cells += 1
                if first_value != second_value:
                    differences.append({
                        "sheet": name, "row": row + 1, "column": column + 1,
                        "first": first_value, "second": second_value,
                    })
    first.close()
    second.close()
    return {"checked_cells": checked_cells, "differences": differences}


def compare_members():
    with ZipFile(FIRST) as first, ZipFile(SECOND) as second:
        first_names = set(first.namelist())
        second_names = set(second.namelist())
        shared = sorted(first_names & second_names)
        different = [name for name in shared if first.read(name) != second.read(name)]
        charts = [name for name in shared if name.startswith("xl/charts/chart") and name.endswith(".xml")]
        return {
            "unique_first": sorted(first_names - second_names),
            "unique_second": sorted(second_names - first_names),
            "differing_members": different,
            "chart_members_compared": len(charts),
            "differing_chart_members": [name for name in charts if name in different],
        }


def main():
    result = {
        "created_at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
        "visibility": "private",
        "inputs": [
            {"path": str(path.relative_to(ROOT)), "size": path.stat().st_size, "sha256": sha256(path)}
            for path in (FIRST, SECOND)
        ],
        "formula_cells": compare_cells(data_only=False),
        "cached_cells": compare_cells(data_only=True),
        "container_members": compare_members(),
        "interpretation": "Content/version comparison of supplied analysis artifacts; no independent experimental replication or physical interpretation.",
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(OUTPUT),
        "formula_differences": len(result["formula_cells"]["differences"]),
        "cached_value_differences": len(result["cached_cells"]["differences"]),
        "container_members_different": len(result["container_members"]["differing_members"]),
        "chart_members_different": len(result["container_members"]["differing_chart_members"]),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
