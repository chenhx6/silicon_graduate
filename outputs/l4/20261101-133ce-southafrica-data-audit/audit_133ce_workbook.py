#!/usr/bin/env python3
import json
import math
from pathlib import Path

import openpyxl


ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "raw/data/SouthAfrica"
WORKBOOK = DATA / "133Ce/analysis/intensity_iThemba2019_export.xlsx"
OUTPUT = Path(__file__).resolve().parent / "workbook-audit.json"


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def audit_ado(ws):
    rows = []
    for row in range(3, ws.max_row + 1):
        gate, energy, counts_s, error_s, counts_l, error_l, efficiency = (
            ws.cell(row, col).value for col in range(1, 8)
        )
        if not all(number(v) for v in (gate, energy, counts_s, error_s, counts_l, error_l, efficiency)):
            continue
        cached = ws.cell(row, 8).value
        expected = counts_s / counts_l / efficiency
        expected_error = expected * math.sqrt(
            (error_l / counts_l) ** 2
            + (error_s / counts_s) ** 2
            + (0.01 / efficiency) ** 2
        )
        rows.append(
            {
                "row": row,
                "gate": gate,
                "energy": energy,
                "expected_ado": expected,
                "cached_ado": cached if number(cached) else None,
                "expected_error": expected_error,
                "absolute_difference": abs(expected - cached) if number(cached) else None,
            }
        )
    return rows


def audit_dco(ws):
    rows = []
    for row in range(3, ws.max_row + 1):
        gate, energy, counts_sl, error_sl, counts_ls, error_ls, transition_eff, gate_eff = (
            ws.cell(row, col).value for col in range(1, 9)
        )
        if not all(number(v) for v in (gate, energy, counts_sl, error_sl, counts_ls, error_ls, transition_eff, gate_eff)):
            continue
        cached = ws.cell(row, 9).value
        expected = counts_sl / counts_ls / transition_eff * gate_eff
        expected_error = expected * math.sqrt(
            (error_sl / counts_sl) ** 2
            + (error_ls / counts_ls) ** 2
            + 0.0008
        )
        rows.append(
            {
                "row": row,
                "gate": gate,
                "energy": energy,
                "expected_dco": expected,
                "cached_dco": cached if number(cached) else None,
                "expected_error": expected_error,
                "absolute_difference": abs(expected - cached) if number(cached) else None,
            }
        )
    return rows


def audit_asymmetry(ws):
    rows = []
    for row in range(3, ws.max_row + 1):
        gate, energy, vertical, error_vertical, horizontal, error_horizontal = (
            ws.cell(row, col).value for col in range(1, 7)
        )
        if not all(number(v) for v in (gate, energy, vertical, error_vertical, horizontal, error_horizontal)):
            continue
        alpha = 1.0038 - 8 * energy / 10_000_000
        expected = (vertical * alpha - horizontal) / (vertical * (1.0569 - 0.00003 * energy) + horizontal)
        cached = ws.cell(row, 10).value
        rows.append(
            {
                "row": row,
                "gate": gate,
                "energy": energy,
                "expected_asymmetry": expected,
                "cached_asymmetry": cached if number(cached) else None,
                "absolute_difference": abs(expected - cached) if number(cached) else None,
            }
        )
    return rows


def main():
    workbook_formula = openpyxl.load_workbook(WORKBOOK, read_only=False, data_only=False)
    workbook_values = openpyxl.load_workbook(WORKBOOK, read_only=False, data_only=True)
    result = {
        "schema_version": 1,
        "data_root": str(DATA),
        "workbook": str(WORKBOOK),
        "sheets": workbook_formula.sheetnames,
        "formula_checks": {
            "ado": audit_ado(workbook_values["ADO"]),
            "dco": audit_dco(workbook_values["DCO"]),
            "asymmetry": audit_asymmetry(workbook_values["Asymmetry"]),
        },
        "formula_presence": {
            "ADO_H3": workbook_formula["ADO"]["H3"].value,
            "DCO_I3": workbook_formula["DCO"]["I3"].value,
            "Asymmetry_J3": workbook_formula["Asymmetry"]["J3"].value,
        },
        "interpretation": {
            "status": "partial-l4-readiness",
            "raw_unchanged": True,
            "synthetic_counts": False,
            "claim_boundary": "Workbook arithmetic and formula consistency only; no event-level reanalysis or independent covariance is claimed.",
        },
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"output": str(OUTPUT), "ado_rows": len(result["formula_checks"]["ado"]), "dco_rows": len(result["formula_checks"]["dco"]), "asymmetry_rows": len(result["formula_checks"]["asymmetry"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
