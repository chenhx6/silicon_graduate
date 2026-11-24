#!/usr/bin/env python3
"""Read the PDM workbook by headers and audit a frozen source-reviewed shortlist."""

import argparse
import csv
from collections import Counter, defaultdict
from contextlib import closing
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from fractions import Fraction
import hashlib
from io import BytesIO
import json
from pathlib import Path
import re
import unicodedata
from zipfile import ZipFile

from openpyxl import Workbook, load_workbook


HERE = Path(__file__).resolve().parent
ROOT = Path.cwd()
DATA_HEADERS = {
    "nuclide": "\u6838\u7d20",
    "energy": "E\u03b3 (keV)",
    "reference": "\u6587\u732e",
    "initial": "Ji\u03c0",
    "final": "Jf\u03c0",
    "P": "P\uff08\u539f\u6587\u8bb0\u53f7\uff09",
    "R_ADO": "R_ADO\uff08\u539f\u6587\uff09",
    "R_DCO": "R_DCO\uff08\u539f\u6587\uff09",
    "delta_label": "\u03b4\uff08\u539f\u6587\uff09",
    "delta_center": "\u03b4\u4e2d\u5fc3\u503c",
    "delta_minus": "\u03b4\u4e0b\u8bef\u5dee\uff08\u7edd\u5bf9\u91cf\uff09",
    "delta_plus": "\u03b4\u4e0a\u8bef\u5dee\uff08\u7edd\u5bf9\u91cf\uff09",
}
REFERENCE_HEADERS = {
    "reference": "\u6587\u732e",
    "title": "\u539f\u6587\u9898\u540d",
    "doi": "DOI",
    "locator": "\u6570\u636e\u4f4d\u7f6e",
    "pdf": "\u672c\u5730\u539f\u6587/\u6750\u6599",
    "supplement": "\u672c\u5730\u8865\u5145\u6750\u6599",
}
NUMBER = r"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)"
MODE_FIELDS = {
    "P_ADO": ("P", "R_ADO"),
    "P_DCO": ("P", "R_DCO"),
    "PDCO": ("P_cond", "R_DCO"),
}


def normalized(value):
    return unicodedata.normalize("NFKC", str(value)).translate(
        str.maketrans({"\u2212": "-", "\u2013": "-", "\u2014": "-"})
    ).strip()


def header_key(value):
    return re.sub(r"\s+", "", normalized(value)).casefold()


def canonical_nuclide(value):
    text = re.sub(r"\s+", "", normalized(value))
    match = re.fullmatch(r"\^?([0-9]+)-?([A-Za-z]{1,3})", text)
    if match:
        mass, element = match.groups()
    else:
        match = re.fullmatch(r"([A-Za-z]{1,3})-?([0-9]+)", text)
        if not match:
            raise ValueError(f"Invalid nuclide {value!r}")
        element, mass = match.groups()
    if int(mass) <= 0:
        raise ValueError(f"Invalid mass number {value!r}")
    return f"{int(mass)}{element.capitalize()}"


def canonical_energy(value):
    match = re.fullmatch(
        rf"({NUMBER})(?:\s*\([0-9.]+\))?(?:\s*keV)?", normalized(value), re.I
    )
    if not match or Decimal(match[1]) <= 0:
        raise ValueError(f"Invalid transition energy {value!r}")
    return Decimal(match[1]).normalize()


def measured_value(value):
    """Return value and positive error widths, or None for a blank/locator cell."""
    if value is None:
        return None
    text = re.sub(r"\s+", "", normalized(value)).replace("+/-", "\u00b1")
    symmetric = re.fullmatch(rf"({NUMBER})(?:\((\d+(?:\.\d+)?)\)|\u00b1({NUMBER}))", text)
    asymmetric = re.fullmatch(
        rf"({NUMBER})(?:\(\+({NUMBER}),?-({NUMBER})\)|\+({NUMBER})-({NUMBER}))",
        text,
    )
    if symmetric:
        central = Decimal(symmetric[1])
        if symmetric[2] is None:
            width = Decimal(symmetric[3])
        elif "." in symmetric[2]:
            width = Decimal(symmetric[2])
        else:
            width = Decimal(symmetric[2]).scaleb(central.as_tuple().exponent)
        minus = plus = width
    elif asymmetric:
        central = Decimal(asymmetric[1])
        plus = Decimal(asymmetric[2] or asymmetric[4])
        minus = Decimal(asymmetric[3] or asymmetric[5])
    else:
        return None
    if min(minus, plus) <= 0:
        raise ValueError(f"Nonpositive observation uncertainty in {value!r}")
    return {"value": float(central), "minus": float(minus), "plus": float(plus)}


def find_table(workbook, required, fields):
    wanted = {header_key(label): key for key, label in fields.items()}
    tables = []
    for sheet in workbook:
        for offset, row in enumerate(sheet.values, 1):
            columns = defaultdict(list)
            for index, value in enumerate(row):
                if isinstance(value, str) and (label := header_key(value)) in wanted:
                    columns[wanted[label]].append(index)
            if not required <= columns.keys():
                continue
            duplicate = [key for key, indices in columns.items() if len(indices) > 1]
            if duplicate:
                raise ValueError(f"Duplicate headers in {sheet.title} row {offset}: {duplicate}")
            tables.append((sheet, offset, {key: indices[0] for key, indices in columns.items()}))
    if len(tables) != 1:
        raise ValueError(f"Expected one table with {sorted(required)}, found {len(tables)}")
    return tables[0]


def table_records(workbook, required, fields):
    sheet, header_row, columns = find_table(workbook, required, fields)
    for offset, row in enumerate(sheet.iter_rows(min_row=header_row + 1, values_only=True), header_row + 1):
        record = {key: row[index] if index < len(row) else None for key, index in columns.items()}
        if any(value is not None for value in record.values()):
            yield f"{sheet.title}:{offset}", record


@dataclass(frozen=True)
class Transition:
    nuclide: str
    energy: Decimal
    initial: str
    final: str
    records: tuple


class WorkbookReader:
    """Keep source records and literature branches distinct within each spin assignment."""

    def __init__(self, workbook):
        records_by_line = defaultdict(lambda: defaultdict(list))
        unresolved = []
        for location, record in table_records(
            workbook, {"nuclide", "energy", "reference", "initial", "final"}, DATA_HEADERS
        ):
            try:
                nuclide = canonical_nuclide(record["nuclide"])
                energy = canonical_energy(record["energy"])
                if not record["reference"]:
                    raise ValueError("Missing reference")
            except (ValueError, InvalidOperation) as error:
                unresolved.append({"location": location, "reason": str(error), "record": record})
                continue
            spins = tuple(header_key(record[field]) if record[field] is not None else "" for field in ("initial", "final"))
            records_by_line[nuclide, energy][spins].append(record)
        self.transitions = {
            key: tuple(
                Transition(*key, *spins, tuple(sorted(records, key=stable_json)))
                for spins, records in sorted(assignments.items())
            )
            for key, assignments in sorted(records_by_line.items())
        }
        self.unresolved = unresolved

    def alternatives(self, nuclide, energy):
        return self.transitions.get((canonical_nuclide(nuclide), canonical_energy(energy)), ())

    def select(self, nuclide, energy, *, spins=None, reference=None):
        alternatives = self.alternatives(nuclide, energy)
        if spins is not None:
            wanted = tuple(map(header_key, spins))
            alternatives = tuple(line for line in alternatives if (line.initial, line.final) == wanted)
        matches = []
        for line in alternatives:
            records = tuple(
                record for record in line.records
                if reference is None or header_key(record["reference"]) == header_key(reference)
            )
            if records:
                matches.append(Transition(line.nuclide, line.energy, line.initial, line.final, records))
        if len(matches) != 1:
            detail = ", ".join(f"{line.initial} -> {line.final}" for line in matches)
            raise LookupError(
                f"{canonical_nuclide(nuclide)} {format(canonical_energy(energy), 'f')} keV: "
                f"{'multiple spin assignments (' + detail + ')' if matches else 'no matching row'}"
            )
        return matches[0]


def stable_json(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, default=str)


def references(workbook):
    result = {}
    for location, record in table_records(workbook, {"reference", "title", "doi"}, REFERENCE_HEADERS):
        key = header_key(record["reference"])
        if key in result:
            raise ValueError(f"Duplicate reference key {record['reference']!r} at {location}")
        result[key] = record
    return result


def sha256(path):
    with path.open("rb") as stream:
        return hashlib.sha256(stream.read()).hexdigest()


def changed_layout(workbook, kind):
    copy = Workbook()
    copy.remove(copy.active)
    for original in reversed(workbook.worksheets):
        sheet = copy.create_sheet(original.title + " rearranged")
        header, *body = original.values
        width = len(header)
        order = list(range(width))
        if kind in {"columns", "combined"}:
            order = list(range(1, width, 2))[::-1] + list(range(0, width, 2))
        if kind in {"rows", "combined"}:
            body = sorted(body, key=stable_json, reverse=True)
        sheet.append(("metadata before header",))
        sheet.append(tuple(header[index] for index in order))
        for offset, row in enumerate(body):
            if offset % 97 == 0:
                sheet.append((None,))
            values = tuple(row[index] if index < len(row) else None for index in order)
            sheet.append(values)
            for column, value in enumerate(values, 1):
                if isinstance(value, str) and value.startswith("="):
                    sheet.cell(sheet.max_row, column).data_type = "s"
    buffer = BytesIO()
    copy.save(buffer)
    buffer.seek(0)
    return load_workbook(buffer, read_only=True, data_only=True)


def test_layout(workbook, reader, refs):
    outcomes = {}
    for kind in ("rows", "columns", "combined"):
        with closing(changed_layout(workbook, kind)) as rearranged:
            parsed = WorkbookReader(rearranged)
            same_unresolved = Counter(stable_json(item["record"]) for item in parsed.unresolved) == Counter(
                stable_json(item["record"]) for item in reader.unresolved
            )
            if parsed.transitions != reader.transitions or references(rearranged) != refs or not same_unresolved:
                raise AssertionError(f"Workbook parsing changed after in-memory {kind} rearrangement")
            outcomes[kind] = "identical"
    return outcomes


def check_reader_fixture():
    workbook = Workbook()
    sheet = workbook.active
    fields = ("reference", "final", "energy", "nuclide", "initial", "delta_center")
    sheet.append(("arbitrary lead-in",))
    sheet.append(tuple(DATA_HEADERS[field] for field in fields))
    sheet.append(("S1", "2+", "123.40(5)", "Se-80", "3+", 0.1))
    sheet.append(("S1", "2+", 123.4, "\u2078\u2070Se", "3+", 2.0))
    sheet.append(("S2", "2+", 123.4, "80Se", "3+", 0.15))
    sheet.append(("S3", "4+", 123.4, "80Se", "5+", 0.42))
    reader = WorkbookReader(workbook)
    if len(reader.select("80Se", "123.4", spins=("3+", "2+")).records) != 3:
        raise AssertionError("Literature branches or sources were merged or dropped")
    if len(reader.select("80Se", 123.4, reference="S1").records) != 2:
        raise AssertionError("Source selection dropped a literature branch")
    try:
        reader.select("80Se", "123.4")
    except LookupError:
        return "branches and independent sources preserved; conflicting spin assignments require selection"
    raise AssertionError("Different spin assignments silently merged")


def selection_label(record):
    center = float(record["delta_center"])
    e2 = center**2 / (1 + center**2)
    return {
        "reported_delta": record.get("delta_label"),
        "center": center,
        "minus": record.get("delta_minus"),
        "plus": record.get("delta_plus"),
        "sign": "positive" if center > 0 else "negative" if center < 0 else "zero",
        "e2_fraction": e2,
        "e2_bin": "low" if e2 < 0.2 else "high" if e2 > 0.8 else "intermediate",
    }


def source_metadata(specification, refs, root):
    sources = {}
    for key, evidence in specification["sources"].items():
        reference = refs[header_key(key)]
        if header_key(reference["doi"]) != header_key(evidence["doi"]):
            raise ValueError(f"Unexpected DOI for {key}: {reference['doi']}")
        files = []
        for field in evidence.get("files", ["pdf"]):
            relative = Path(reference[field])
            path = (root / relative).resolve()
            if not path.is_relative_to(root / "raw" / "papers"):
                raise ValueError(f"Source path outside raw/papers for {key}")
            files.append({
                "role": field, "path": str(relative), "bytes": path.stat().st_size,
                "sha256": sha256(path), "archive_required": True,
            })
        sources[key] = {**evidence, "workbook_title": reference["title"], "audited_files": files}
    return sources


def audit_candidate(spec, reader, sources, exclusions):
    source = sources[spec["source"]]
    line = reader.select(spec["nuclide"], spec["energy_keV"], spins=spec["spins"], reference=spec["source"])
    if line.nuclide in exclusions["nuclides"] or source["doi"].casefold() in exclusions["dois"]:
        raise ValueError(f"Excluded source or nuclide in shortlist: {line.nuclide}, {source['doi']}")
    observations = {}
    for field, literal in spec.get("observations", {}).items():
        checked = measured_value(literal)
        if checked is None:
            raise ValueError(f"Invalid audited observable {field}={literal!r}")
        workbook_field = "P" if field == "P_cond" else field
        workbook_numbers = [measured_value(record.get(workbook_field)) for record in line.records]
        if any(number != checked for number in workbook_numbers):
            raise ValueError(f"PDF/workbook mismatch for {line.nuclide} {line.energy} {field}")
        observations[field] = {**checked, "as_reported": literal}
    auxiliary = {}
    for field, literal in spec.get("auxiliary_observations", {}).items():
        checked = measured_value(literal)
        if checked is None:
            raise ValueError(f"Invalid auxiliary observable {field}={literal!r}")
        auxiliary[field] = {**checked, "as_reported": literal}
    mode_status = {}
    for mode, fields in MODE_FIELDS.items():
        if mode in source["candidate_modes"] and all(field in observations for field in fields):
            status = "measured_pair_pending_model_mapping"
        elif mode == "PDCO" and "P_cond" in observations and "R_DCO" not in observations:
            status = "measured_conditional_P_only"
        elif mode in source["candidate_modes"]:
            status = "source_gap"
        else:
            status = "unavailable"
        mode_status[mode] = status
    selection = [
        selection_label(record) for record in line.records if record.get("delta_center") is not None
    ] if spec["tier"] != "gap" else []
    energy = format(line.energy, "f")
    return {
        "display": f"{line.nuclide} {energy} keV",
        "nuclide": line.nuclide,
        "energy_keV": float(line.energy),
        "nuclear_class": spec["nuclear_class"],
        "tier": spec["tier"],
        "spins": spec["spins"],
        "observations": observations,
        "auxiliary_observations": auxiliary,
        "mode_status": mode_status,
        "gate_path": spec["gate_path"],
        "missing": spec.get("missing", []),
        "source_locator": spec.get("locator", source["locator"]),
        "selection_only": selection,
        "provenance": {
            "reference": spec["source"],
            "workbook_records": len(line.records),
            "workbook_literature_branches": [
                {key: record.get(key) for key in ("delta_label", "delta_center", "delta_minus", "delta_plus")}
                for record in line.records if record.get("delta_label") is not None
            ],
        },
    }


def make_coverage(cases):
    reviewed = [case for case in cases if case["tier"] != "gap"]
    classes = defaultdict(list)
    for case in reviewed:
        classes[case["nuclear_class"]].append(case)
    mode_coverage = {}
    for mode in MODE_FIELDS:
        pairs = [
            case for case in reviewed
            if case["mode_status"][mode] == "measured_pair_pending_model_mapping"
        ]
        mode_coverage[mode] = {
            "source_measured_pairs": len(pairs),
            "nuclides_with_source_measured_pairs": sorted({case["nuclide"] for case in pairs}),
            "fit_ready": 0,
        }
    return {
        "tiers": dict(Counter(case["tier"] for case in cases)),
        "nuclear_classes": {
            category: {
                "lines": len(lines),
                "nuclides": sorted({case["nuclide"] for case in lines}),
            }
            for category, lines in sorted(classes.items())
        },
        "selection_delta_sign": dict(Counter(
            label["sign"] for case in reviewed for label in case["selection_only"]
        )),
        "selection_e2_bin": dict(Counter(
            label["e2_bin"] for case in reviewed for label in case["selection_only"]
        )),
        "modes": mode_coverage,
        "measured_conditional_P_without_matching_DCO": sum(
            case["mode_status"]["PDCO"] == "measured_conditional_P_only" for case in cases
        ),
    }


def write_csv(path, cases):
    fields = ["display", "tier", "nuclear_class", "initial", "final", *MODE_FIELDS]
    for field in ("P", "P_cond", "R_ADO", "R_DCO"):
        fields.extend(f"{field}_{suffix}" for suffix in ("value", "minus", "plus"))
    fields.extend(("selection_delta_sign", "selection_e2_fraction", "selection_e2_bin", "gate_path", "missing"))
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fields)
        writer.writeheader()
        for case in cases:
            initial, final = case["spins"]
            row = {
                "display": case["display"], "tier": case["tier"], "nuclear_class": case["nuclear_class"],
                "initial": initial, "final": final, **case["mode_status"],
                "gate_path": case["gate_path"], "missing": " | ".join(case["missing"]),
            }
            for field, observation in case["observations"].items():
                row.update({f"{field}_{part}": observation[part] for part in ("value", "minus", "plus")})
            for field in ("sign", "e2_fraction", "e2_bin"):
                row[f"selection_{'delta_' if field == 'sign' else ''}{field}"] = " | ".join(
                    str(round(label[field], 6) if field == "e2_fraction" else label[field])
                    for label in case["selection_only"]
                )
            writer.writerow(row)


def observed_job(case, mode, geometry):
    def spin_value(spin):
        return float(Fraction(normalized(spin).strip("()").rstrip("+-")))

    initial, final = map(spin_value, case["spins"])
    observations = {}
    for field in MODE_FIELDS[mode]:
        observed = case["observations"][field]
        observations[field] = {
            "value": observed["value"],
            "err_minus": observed["minus"],
            "err_plus": observed["plus"],
        }
    return {
        "mode": mode,
        "label": case["display"],
        "target": {"spin_initial": initial, "spin_final": final, "multipoles": ["M1", "E2"]},
        "observations": observations,
        "geometry": geometry,
    }


def write_point_angle_exports(output, spec, report):
    ado_filename = "point_angle_ado_jobs.json"
    dco_filename = "point_angle_dco_scenarios.json"
    ado_jobs = []
    dco_jobs = []
    readiness = []
    configured_dco = spec["dco_scenarios"]
    seen_dco = set()
    for case in report["candidates"]:
        display = case["display"]
        review = {
            "display": display,
            "tier": case["tier"],
            "published_response_replay": "unverified",
            "point_angle": {
                mode: {"status": status} for mode, status in case["mode_status"].items()
            },
        }
        modes = review["point_angle"]
        source = case["provenance"]["reference"]
        review["observation_source"] = {
            "reference": source,
            "locator": case["source_locator"],
        }
        ado = spec["ado_by_source"].get(source)
        if ado and case["mode_status"]["P_ADO"] == "measured_pair_pending_model_mapping":
            ado_jobs.append(observed_job(case, "P_ADO", ado["geometry"]))
            modes["P_ADO"] = {
                "status": "point_angle_benchmark",
                "job_file": ado_filename,
                "job_number": len(ado_jobs),
                **ado,
            }
        if reason := spec["dco_gate_review"].get(display):
            modes["P_DCO"] = {"status": "gate_or_path_gap", "reason": reason}
        if display in configured_dco:
            scenario = configured_dco[display]
            geometries = []
            seen_dco.add(display)
            for theta_a, theta_b in scenario["theta_orders_deg"]:
                for phi in scenario["phi_values_deg"]:
                    geometry = {
                        "theta_p_deg": scenario["theta_p_deg"],
                        "theta_a_deg": theta_a,
                        "theta_b_deg": theta_b,
                        "relative_phi_deg": phi,
                    }
                    job = observed_job(case, "P_DCO", geometry)
                    for key in ("gate", "target_first", "intermediates"):
                        job[key] = scenario[key]
                    dco_jobs.append(job)
                    geometries.append({"job_number": len(dco_jobs), **geometry})
            modes["P_DCO"] = {
                "status": "point_angle_sensitivity_only",
                "job_file": dco_filename,
                "geometry_method_reference": "N20",
                "scenarios": geometries,
                **scenario,
            }
        readiness.append(review)
    if seen_dco != configured_dco.keys():
        raise ValueError("An approved DCO scenario is absent from the frozen candidate list")
    batches = ((ado_filename, ado_jobs), (dco_filename, dco_jobs))
    batch_provenance = {}
    for filename, jobs in batches:
        path = output / filename
        path.write_text(json.dumps({"jobs": jobs}, indent=2, allow_nan=False) + "\n", encoding="utf-8")
        batch_provenance[filename] = {"sha256": sha256(path), "jobs": len(jobs)}
    model_report = {
        "job_numbers_are_one_based": True,
        "workbook_sha256": report["workbook"]["sha256"],
        "job_file_provenance": batch_provenance,
        "sources": {
            key: {field: source[field] for field in ("doi", "locator", "audited_files")}
            for key, source in report["sources"].items()
        },
        "published_response_replay_ready": 0,
        "point_angle_ado_jobs": len(ado_jobs),
        "point_angle_dco_jobs": len(dco_jobs),
        "point_angle_dco_distinct_lines": len(seen_dco),
        "conditional_pdco_jobs": 0,
        "cases": readiness,
    }
    (output / "modeling_readiness.json").write_text(
        json.dumps(model_report, indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workbook", type=Path, required=True)
    parser.add_argument("--source-root", type=Path, default=Path.cwd(), help="Root for source paths in the supplied bibliography")
    parser.add_argument("--spec", type=Path, default=HERE.parent / "cases/source_evidence.json")
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    output = args.out_dir.resolve()
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    before = sha256(args.workbook)
    with closing(load_workbook(args.workbook, read_only=True, data_only=True)) as workbook:
        reader = WorkbookReader(workbook)
        refs = references(workbook)
        layout = test_layout(workbook, reader, refs)
        exact_alias = any(
            header_key(value) == "shu74" for sheet in workbook for row in sheet.values
            for value in row if isinstance(value, str)
        )
    with ZipFile(args.workbook) as package:
        alias_xml = [
            name for name in package.namelist()
            if name.endswith(".xml") and b"SHU74" in package.read(name).upper()
        ]
    if before != sha256(args.workbook):
        raise RuntimeError("Input workbook SHA-256 changed during the audit")
    exclusions = spec["exclusions"]
    exclusions["SHU74"]["workbook_exact_cell_match"] = exact_alias
    exclusions["SHU74"]["workbook_xml_matches"] = alias_xml
    exclusions["workbook_74Br_rows_excluded"] = sum(
        len(line.records) for key, lines in reader.transitions.items() if key[0] == "74Br" for line in lines
    )
    sources = source_metadata(spec, refs, args.source_root.resolve())
    cases = [audit_candidate(case, reader, sources, exclusions) for case in spec["cases"]]
    coverage = make_coverage(cases)
    report = {
        "workbook": {"sha256": before, "unchanged": True, "reference_records": len(refs)},
        "reader": {
            "nuclide_energy_keys": len(reader.transitions),
            "spin_assignments": sum(map(len, reader.transitions.values())),
            "key_conflicts": sum(len(lines) > 1 for lines in reader.transitions.values()),
            "retained_rows": sum(len(line.records) for lines in reader.transitions.values() for line in lines),
            "unresolved_rows": reader.unresolved,
            "in_memory_layout_checks": layout,
            "ambiguity_check": check_reader_fixture(),
        },
        "exclusions": exclusions,
        "coverage": coverage,
        "sources": sources,
        "candidates": cases,
        "fit_ready_definition": "Exact published-response replay. Declared point-angle inputs are listed separately in modeling_readiness.json.",
        "fit_ready_cases": [],
    }
    output.mkdir(parents=True, exist_ok=True)
    (output / "candidates.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_csv(output / "candidates.csv", cases)
    write_point_angle_exports(output, spec["point_angle"], report)
    print(json.dumps(coverage, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
