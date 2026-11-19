"""Build the reviewed delta-extraction workbook and audited v2 ledger."""

import argparse
import json
import math
import os
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.hyperlink import Hyperlink
from openpyxl.worksheet.table import Table, TableStyleInfo

ALIGNMENTS = {
    "FIX_ASSUMED": "假定单值固定",
    "FIX_CALIBRATED": "标定后固定",
    "FIX_UNSPECIFIED": "固定但来源未明",
    "SCAN_COMBINE": "扫描并合并",
    "FREE_JOINT": "自由联合拟合",
    "CONSTRAINED_JOINT": "受约束联合拟合",
    "MARGINALIZED": "边缘化",
    "UNREPORTED": "未报告",
    "UNRESOLVED": "未能判定",
    "NA": "不适用",
}

RATIOS = {
    "R_ADO": "取向核角分布比 (R_ADO)",
    "R_DCO": "方向角关联比 (R_DCO)",
    "RATIO_OTHER": "其他有明确实验定义的比值",
    "UNRESOLVED": "定义待核",
    "NA": "不适用/全角分布拟合",
}

RESULT_ORIGINS = {
    "ORIGINAL_MEASUREMENT": "独立实验测量提取",
    "REANALYSIS": "历史/已有数据重新分析",
    "ADOPTED": "文献/编评采用值",
    "UNRESOLVED": "文中报告，提取来源未明确",
}

DATASET_FIELDS = [
    "dataset_id", "ref_id", "nucleus", "E_gamma_keV", "Ei_keV", "Ef_keV",
    "Ji_pi", "Jf_pi", "delta_center", "delta_err_minus", "delta_err_plus",
    "delta_low", "delta_high", "delta_original", "delta_definition",
    "result_origin", "method", "used_data", "alignment_treatment", "sigma_I",
    "angular_coeffs", "ratio_status", "ratio_original_name", "ratio_value",
    "A_pol", "P", "alpha_IC", "comparison_dataset_id", "locator", "notes",
]

SETTINGS_FIELDS = [
    "dataset_id", "ref_id", "nucleus", "reaction_setup", "ratio_status",
    "ratio_original_name", "angular_definition", "angles", "gate",
    "polarization_calibration", "alignment_treatment", "alignment_value",
    "curve_evaluation", "final_alignment_condition", "alignment_details",
    "uncertainty_model", "locator",
]

REF_FIELDS = [
    "ref_id", "doi", "extraction", "local_file", "supplement_file", "url",
]

PUBLISHER_URLS = {
    "W77": "https://iopscience.iop.org/article/10.1088/0305-4616/3/1/007",
    "L22": "https://www.sciencedirect.com/science/article/pii/S0370269321007802",
    "M15": "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.114.082501",
    "G22": "https://www.sciencedirect.com/science/article/pii/S0370269322001447",
    "S20": "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.124.052501",
}

CONCISE_EXTRACTIONS = {
    "W77": "Table 3, pp.40-41; method Sec.2, p.36",
    "L22": "Table 1/Fig.2, p.3; SI pp.1,4-5",
    "M15": "Table I, p.4; Figs.2-3; method p.3",
    "G22": "Fig.3, p.3; SI pp.1-4/Fig.2",
    "S20": "Fig.3, p.4; method p.3",
}


def as_cell(value):
    if value is None:
        return None
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, str):
        if value.startswith(("=", "+", "@")):
            return "'" + value
    return value


def internal_link(cell, sheet, row, column="A"):
    cell.hyperlink = Hyperlink(
        ref=cell.coordinate, location=f"'{sheet}'!{column}{row}", display=str(cell.value)
    )
    cell.font = Font(name="Calibri", size=11, color="0563C1", underline="single")


def clean_notes(note_raw):
    if not note_raw:
        return ""
    text = note_raw
    text = text.replace(" Ef用于能级身份对照；若由Ei-Egamma补足，非独立测量。", "")
    text = text.replace("Ef用于能级身份对照；若由Ei-Egamma补足，非独立测量。", "")
    return text.strip()


def extract_v2_data(v1_ledger, se72_path=None):
    v1 = json.loads(v1_ledger.read_text())
    old_setups = {s["setup_id"]: s for s in v1["setups"]}

    transitions = [
        t for t in v1["transitions"]
        if t.get("delta_center") is not None
        and t.get("delta_definition", "").startswith("E2/M1")
    ]

    ref_prefix = {"W77": "NI77", "L22": "PR22", "M15": "PR15", "G22": "AU22", "S20": "AU20"}

    datasets = []
    settings = []

    for t in transitions:
        ref = t["ref_id"]
        prefix = ref_prefix[ref]
        eg = int(round(t["E_gamma_keV"]))
        did = f"{prefix}-{eg}"

        if ref in ("G22", "L22"):
            ratio_status = "R_ADO"
            ratio_name = "Rac"
        else:
            ratio_status = "NA"
            ratio_name = None

        old_s = old_setups[t["setup_id"]]
        note = clean_notes(t.get("notes", ""))

        d_row = {
            "dataset_id": did,
            "ref_id": ref,
            "nucleus": t["nucleus"],
            "E_gamma_keV": t["E_gamma_keV"],
            "Ei_keV": t.get("Ei_keV"),
            "Ef_keV": t.get("Ef_keV"),
            "Ji_pi": t["Ji_pi"],
            "Jf_pi": t["Jf_pi"],
            "delta_center": t["delta_center"],
            "delta_err_minus": t["delta_err_minus"],
            "delta_err_plus": t["delta_err_plus"],
            "delta_low": t["delta_low"],
            "delta_high": t["delta_high"],
            "delta_original": t["delta_original"],
            "delta_definition": "E2/M1",
            "result_origin": "ORIGINAL_MEASUREMENT",
            "method": t["method"],
            "used_data": t["used_data"],
            "alignment_treatment": t["alignment_treatment"],
            "sigma_I": t.get("sigma_I"),
            "angular_coeffs": t.get("angular_coeffs"),
            "ratio_status": ratio_status,
            "ratio_original_name": ratio_name,
            "ratio_value": t.get("ratio_value"),
            "A_pol": t.get("A_pol"),
            "P": t.get("P"),
            "alpha_IC": t.get("alpha_IC"),
            "comparison_dataset_id": None,
            "locator": t.get("locator"),
            "notes": note,
        }
        datasets.append(d_row)

        s_row = {
            "dataset_id": did,
            "ref_id": ref,
            "nucleus": t["nucleus"],
            "reaction_setup": old_s["reaction_setup"],
            "ratio_status": ratio_status,
            "ratio_original_name": ratio_name,
            "angular_definition": old_s["angular_definition"],
            "angles": old_s["angles"],
            "gate": old_s.get("gate"),
            "polarization_calibration": old_s.get("polarization_calibration"),
            "alignment_treatment": old_s["alignment_treatment"],
            "alignment_value": old_s.get("alignment_value"),
            "curve_evaluation": old_s.get("curve_evaluation"),
            "final_alignment_condition": old_s.get("final_alignment_condition"),
            "alignment_details": old_s.get("alignment_details"),
            "uncertainty_model": old_s.get("uncertainty_model"),
            "locator": old_s.get("locator"),
        }
        settings.append(s_row)

    # Establish comparison links (tolerance <= 0.6 keV, same nucleus, same Ji/Jf, different ref)
    for d1 in datasets:
        for d2 in datasets:
            if d1["dataset_id"] == d2["dataset_id"] or d1["ref_id"] == d2["ref_id"]:
                continue
            if d1["nucleus"] == d2["nucleus"] and d1["Ji_pi"] == d2["Ji_pi"] and d1["Jf_pi"] == d2["Jf_pi"]:
                if abs(d1["E_gamma_keV"] - d2["E_gamma_keV"]) <= 0.6:
                    d1["comparison_dataset_id"] = d2["dataset_id"]

    # References
    refs = []
    for r in v1["refs"]:
        ref_id = r["ref_id"]
        refs.append({
            "ref_id": ref_id,
            "doi": r["doi"],
            "extraction": CONCISE_EXTRACTIONS.get(ref_id, r.get("extraction", "")),
            "local_file": r["local_file"],
            "supplement_file": r.get("supplement_file"),
            "url": PUBLISHER_URLS.get(ref_id, r.get("url", "")),
        })

    # Optional 72Se incorporation
    if se72_path and se72_path.is_file():
        se72_data = json.loads(se72_path.read_text())
        if "refs" in se72_data:
            existing_ref_ids = {r["ref_id"] for r in refs}
            for sr in se72_data["refs"]:
                if sr["ref_id"] not in existing_ref_ids:
                    refs.append(sr)
        se72_transitions = se72_data.get("datasets") or se72_data.get("transitions") or []
        for st in se72_transitions:
            if st.get("delta_center") is not None and st.get("delta_definition", "").startswith("E2/M1"):
                st["delta_definition"] = "E2/M1"
                st["result_origin"] = st.get("result_origin", "ORIGINAL_MEASUREMENT")
                datasets.append(st)
        se72_settings = se72_data.get("settings") or se72_data.get("setups") or []
        for ss in se72_settings:
            settings.append(ss)

    return datasets, settings, refs


def build_paper_overview(refs, datasets):
    overview = []
    for r in refs:
        ref_id = r["ref_id"]
        ref_datasets = [d for d in datasets if d["ref_id"] == ref_id]
        if not ref_datasets:
            continue
        nucleus = ref_datasets[0]["nucleus"]
        count = len(ref_datasets)
        alignment = ref_datasets[0]["alignment_treatment"]
        ratio_stat = ref_datasets[0]["ratio_status"]
        if ref_id == "W77":
            reaction = "58Fe(alpha, n) @ Liverpool; Ge(Li) spectrometer + polarimeter"
        elif ref_id == "L22":
            reaction = "100Mo(40Ar, 1p4n) @ JYFL; JUROGAM2 array"
        elif ref_id == "M15":
            reaction = "123Sb(16O, 4n) @ ATLAS; Gammasphere array"
        elif ref_id == "G22":
            reaction = "175Lu(18O, 6n) @ HIRFL; Clover array"
        elif ref_id == "S20":
            reaction = "174Yb(19F, 6n) @ ATLAS; Gammasphere array"
        else:
            reaction = "Experimental setup"
        overview.append({
            "ref_id": ref_id,
            "nucleus": nucleus,
            "count": count,
            "alignment_treatment": alignment,
            "ratio_status": ratio_stat,
            "reaction_facility": reaction,
        })
    return overview


def validate_records(datasets, settings, refs, root):
    d_ids = [d["dataset_id"] for d in datasets]
    assert len(d_ids) == len(set(d_ids)), f"Duplicate dataset_id in Dataset: {d_ids}"
    s_ids = [s["dataset_id"] for s in settings]
    assert len(s_ids) == len(set(s_ids)), f"Duplicate dataset_id in Settings: {s_ids}"
    assert set(d_ids) == set(s_ids), f"Dataset IDs mismatch between Dataset and Settings"

    ref_ids = [r["ref_id"] for r in refs]
    assert len(ref_ids) == len(set(ref_ids)), f"Duplicate ref_id in References: {ref_ids}"
    ref_id_set = set(ref_ids)

    for d in datasets:
        assert d["ref_id"] in ref_id_set, f"Unknown ref_id in Dataset: {d['ref_id']}"
        assert d["delta_definition"] == "E2/M1", f"Non-E2/M1 definition: {d['delta_definition']}"
        c = d["delta_center"]
        assert isinstance(c, (int, float)) and math.isfinite(c), f"Invalid delta_center: {c}"
        m, p = d["delta_err_minus"], d["delta_err_plus"]
        assert m is not None and m >= 0, f"Invalid delta_err_minus: {m}"
        assert p is not None and p >= 0, f"Invalid delta_err_plus: {p}"
        assert math.isclose(c - m, d["delta_low"], abs_tol=1e-6), f"delta_low mismatch: {d}"
        assert math.isclose(c + p, d["delta_high"], abs_tol=1e-6), f"delta_high mismatch: {d}"
        assert d["alignment_treatment"] in ALIGNMENTS, f"Invalid alignment: {d['alignment_treatment']}"
        assert d["ratio_status"] in RATIOS, f"Invalid ratio_status: {d['ratio_status']}"
        assert d["result_origin"] in RESULT_ORIGINS, f"Invalid result_origin: {d['result_origin']}"

        comp = d.get("comparison_dataset_id")
        if comp:
            assert comp in set(d_ids), f"Unknown comparison target: {comp}"

    for r in refs:
        if r.get("local_file"):
            p = root / r["local_file"]
            assert p.is_file(), f"Missing local_file: {p}"
        if r.get("supplement_file"):
            p = root / r["supplement_file"]
            assert p.is_file(), f"Missing supplement_file: {p}"
        assert r.get("doi"), f"Missing DOI: {r}"
        assert r.get("url"), f"Missing URL: {r}"
        assert not r["url"].startswith("https://doi.org/"), f"URL must be genuine direct publisher link, not DOI resolver: {r['url']}"


def populate_sheet(wb, sheet_name, fields, records, tablename, freeze_col="D2"):
    ws = wb.create_sheet(sheet_name)
    ws.append(fields)
    for record in records:
        ws.append([as_cell(record.get(f)) for f in fields])
    ws.freeze_panes = freeze_col
    ws.sheet_view.zoomScale = 80
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.sheet_properties.tabColor = "147D92"
    ws.row_dimensions[1].height = 32

    for cell in ws[1]:
        cell.fill = PatternFill("solid", fgColor="173B53")
        cell.font = Font(name="Calibri", color="FFFFFF", bold=True, size=11)
        cell.alignment = Alignment(wrap_text=True, vertical="center")

    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.font = Font(name="Calibri", size=11)
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            if isinstance(cell.value, (float, int)):
                cell.number_format = "0.######"
        ws.row_dimensions[row[0].row].height = 54

    for i, field in enumerate(fields, 1):
        from openpyxl.utils import get_column_letter
        width = 16
        if field in ("notes", "angular_definition", "alignment_details", "curve_evaluation", "final_alignment_condition"):
            width = 52
        elif field in ("local_file", "supplement_file", "url", "locator", "method", "polarization_calibration", "reaction_setup", "gate"):
            width = 40
        elif field in ("extraction", "result_origin", "comparison_dataset_id", "alignment_treatment", "ratio_status"):
            width = 24
        elif field in ("dataset_id", "ref_id", "nucleus", "Ji_pi", "Jf_pi"):
            width = 12
        ws.column_dimensions[get_column_letter(i)].width = width

    if records:
        table = Table(displayName=tablename, ref=ws.dimensions)
        table.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True)
        ws.add_table(table)

    ws.print_title_rows = "1:1"
    ws.page_setup.orientation = "landscape"
    ws.page_setup.paperSize = ws.PAPERSIZE_A3
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    return ws


def build_workbook(datasets, settings, refs, overview, destination, root):
    wb = Workbook()
    readme = wb.active
    readme.title = "Readme"

    # Header
    readme.append(["原子核低能结构 γ 跃迁混合比 δ 及实验自旋取向 (σ/I) 审查工作簿"])
    readme.append(["项目", "说明 / 内容"])

    # Table 1: Compact Paper Overview
    readme.append(["[文献概览 / Paper Overview]", f"共 {len(overview)} 项研究体系，涵盖 {len(datasets)} 条 E2/M1 跃迁测量"])
    overview_headers = ["ref_id", "核素", "E2/M1条目数", "取向处理 (alignment_treatment)", "比值类型 (ratio_status)", "反应与探测装置"]
    readme.append(overview_headers)
    for o in overview:
        readme.append([o["ref_id"], o["nucleus"], o["count"], o["alignment_treatment"], o["ratio_status"], o["reaction_facility"]])
    readme.append([])

    # Table 2: Schema & Navigation
    schema_notes = [
        ("[主表导航 / Navigation]", "Dataset 与 Settings 表严格使用同名 dataset_id（1:1对应），点击 dataset_id 实现两表同跃迁瞬时互跳；点击 ref_id 直达 References 文献行。"),
        ("[同跃迁独立对照 / Comparison]", "AU22 与 AU20（187Au）、PR22 与 PR15（135Pr）互设 comparison_dataset_id 跳转链接；两者均为独立的原创实验测量 (ORIGINAL_MEASUREMENT)，非同批数据。"),
        ("[五列数值 δ / Five Delta Columns]", "delta_center(中心值)、delta_err_minus(向左误差量，非负绝对值)、delta_err_plus(向右误差量)、delta_low/high(置信下上限)；保留原文 delta_original。"),
        ("[比值分类 / Ratio Status]", "G22 与 L22 采用取向核角分布比 R_ADO（G22典型154°/90°，L22分组角度158°+134° vs 76°+105°）；W77、M15、S20 采用多角度全角分布 W(θ) 拟合，分类为 NA。"),
        ("[文献追溯 / References]", "DOI 提供官方解析链接；URL 提供独立直接出版物全文页面；local_file 与 supplement_file 为本地相对 PDF 链接。"),
    ]
    for k, v in schema_notes:
        readme.append([k, v])
    readme.append([])

    # Table 3: Controlled Vocabularies
    readme.append(["[受控词表 / Vocabularies]", "分类定义与代码说明"])
    readme.append(["受控字段", "代码", "说明"])
    for k, v in ALIGNMENTS.items():
        readme.append(["alignment_treatment", k, v])
    for k, v in RATIOS.items():
        readme.append(["ratio_status", k, v])
    for k, v in RESULT_ORIGINS.items():
        readme.append(["result_origin", k, v])

    # Format Readme
    readme.column_dimensions["A"].width = 24
    readme.column_dimensions["B"].width = 30
    readme.column_dimensions["C"].width = 70
    readme.freeze_panes = "A3"
    readme.sheet_view.zoomScale = 85
    readme.row_dimensions[1].height = 28
    readme["A1"].font = Font(name="Calibri", size=14, bold=True, color="173B53")
    readme["A2"].fill = readme["B2"].fill = PatternFill("solid", fgColor="173B53")
    readme["A2"].font = readme["B2"].font = Font(name="Calibri", color="FFFFFF", bold=True, size=11)

    # Populate Sheets
    ws = populate_sheet(wb, "Dataset", DATASET_FIELDS, datasets, "DatasetData", "D2")
    ss = populate_sheet(wb, "Settings", SETTINGS_FIELDS, settings, "SettingsData", "D2")
    rs = populate_sheet(wb, "References", REF_FIELDS, refs, "ReferenceData", "B2")

    # Row maps
    dataset_row_map = {d["dataset_id"]: i for i, d in enumerate(datasets, 2)}
    settings_row_map = {s["dataset_id"]: i for i, s in enumerate(settings, 2)}
    ref_row_map = {r["ref_id"]: i for i, r in enumerate(refs, 2)}
    first_data_row_of_ref = {}
    for i, d in enumerate(datasets, 2):
        if d["ref_id"] not in first_data_row_of_ref:
            first_data_row_of_ref[d["ref_id"]] = i

    # Hyperlinks in Dataset
    for i, d in enumerate(datasets, 2):
        did = d["dataset_id"]
        ref_id = d["ref_id"]
        # Link dataset_id to Settings
        internal_link(ws.cell(i, 1), "Settings", settings_row_map[did], "A")
        # Link ref_id to References
        internal_link(ws.cell(i, 2), "References", ref_row_map[ref_id], "A")
        # Link comparison_dataset_id
        comp = d.get("comparison_dataset_id")
        if comp and comp in dataset_row_map:
            internal_link(ws.cell(i, 28), "Dataset", dataset_row_map[comp], "A")

        # Soft green fill for delta columns (cols 9 to 13: delta_center..delta_high)
        for col_idx in range(9, 14):
            ws.cell(i, col_idx).fill = PatternFill("solid", fgColor="E6F2EE")

        # Soft amber fill for notes with sign warnings or discrepancies
        note_val = d.get("notes", "") or ""
        if any(w in note_val for w in ("符号", "差异", "Rose-Brink", "对照", "质疑")):
            ws.cell(i, 30).fill = PatternFill("solid", fgColor="FFF1CE")

    # Hyperlinks in Settings
    for i, s in enumerate(settings, 2):
        did = s["dataset_id"]
        ref_id = s["ref_id"]
        # Link dataset_id back to Dataset
        internal_link(ss.cell(i, 1), "Dataset", dataset_row_map[did], "A")
        # Link ref_id to References
        internal_link(ss.cell(i, 2), "References", ref_row_map[ref_id], "A")

    # Hyperlinks in References
    local_links = 0
    for i, r in enumerate(refs, 2):
        ref_id = r["ref_id"]
        # Link ref_id to first row in Dataset
        if ref_id in first_data_row_of_ref:
            internal_link(rs.cell(i, 1), "Dataset", first_data_row_of_ref[ref_id], "A")
        # DOI link
        doi = r.get("doi")
        if doi:
            rs.cell(i, 2).hyperlink = "https://doi.org/" + doi
            rs.cell(i, 2).font = Font(name="Calibri", size=11, color="0563C1", underline="single")
        # Local PDF link
        loc = r.get("local_file")
        if loc:
            rel = os.path.relpath(root / loc, destination.parent)
            rs.cell(i, 4).hyperlink = rel
            rs.cell(i, 4).font = Font(name="Calibri", size=11, color="0563C1", underline="single")
            local_links += 1
        # Supplement PDF link
        sup = r.get("supplement_file")
        if sup:
            rel = os.path.relpath(root / sup, destination.parent)
            rs.cell(i, 5).hyperlink = rel
            rs.cell(i, 5).font = Font(name="Calibri", size=11, color="0563C1", underline="single")
            local_links += 1
        # Publisher URL link
        url = r.get("url")
        if url:
            rs.cell(i, 6).hyperlink = url
            rs.cell(i, 6).font = Font(name="Calibri", size=11, color="0563C1", underline="single")

    # Data Validations on Dataset
    val_align = DataValidation(type="list", formula1='"' + ",".join(ALIGNMENTS.keys()) + '"')
    ws.add_data_validation(val_align)
    val_align.add(f"S2:S{len(datasets) + 1}")

    val_ratio = DataValidation(type="list", formula1='"' + ",".join(RATIOS.keys()) + '"')
    ws.add_data_validation(val_ratio)
    val_ratio.add(f"V2:V{len(datasets) + 1}")

    val_origin = DataValidation(type="list", formula1='"' + ",".join(RESULT_ORIGINS.keys()) + '"')
    ws.add_data_validation(val_origin)
    val_origin.add(f"P2:P{len(datasets) + 1}")

    wb.active = wb.sheetnames.index("Dataset")
    destination.parent.mkdir(parents=True, exist_ok=True)
    wb.save(destination)

    # Verification on disk
    check = load_workbook(destination, data_only=False)
    assert check["Dataset"].max_row == len(datasets) + 1
    assert check["Settings"].max_row == len(settings) + 1
    assert check["References"].max_row == len(refs) + 1
    assert all(check["Dataset"].cell(i, 1).hyperlink.location for i in range(2, len(datasets) + 2))
    assert all(check["Settings"].cell(i, 1).hyperlink.location for i in range(2, len(settings) + 2))
    assert not any(c.data_type == "f" for sheet in check for row in sheet for c in row)

    print(json.dumps({
        "status": "success",
        "workbook": str(destination),
        "datasets": len(datasets),
        "settings": len(settings),
        "refs": len(refs),
        "local_links": local_links,
    }, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description="Build reviewed delta extraction workbook.")
    parser.add_argument("--ledger", type=Path, default=Path("outputs/literature-acquisition/20261110-pado-delta-pilot/audited-extraction.json"))
    parser.add_argument("--se72", type=Path, default=None)
    parser.add_argument("--v2-json", type=Path, default=Path("outputs/literature-acquisition/20261111-pado-delta-pilot-v2/audited-v2.json"))
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    se72_candidate = args.se72 or Path("tmp/pado-delta-v2/se72.json")
    se72_to_load = se72_candidate if se72_candidate.is_file() else None

    # Determine default output
    if args.output:
        dest = args.output
    elif se72_to_load:
        dest = Path("raw/writing/pado/20261029_review_v1/mixing_ratio_sigma_I_pilot_20261111.xlsx")
    else:
        dest = Path("tmp/pado-delta-v2/formatter/mixing_ratio_sigma_I_pilot_20261111_temp.xlsx")

    datasets, settings, refs = extract_v2_data(args.ledger, se72_to_load)
    overview = build_paper_overview(refs, datasets)
    validate_records(datasets, settings, refs, args.root)

    # Save audited-v2.json
    v2_payload = {
        "schema_version": "2.0",
        "pilot_scope": "low_spin_e2_m1_mixing_ratios",
        "total_datasets": len(datasets),
        "se72_incorporated": se72_to_load is not None,
        "paper_overview": overview,
        "refs": refs,
        "datasets": datasets,
        "settings": settings,
    }
    args.v2_json.parent.mkdir(parents=True, exist_ok=True)
    args.v2_json.write_text(json.dumps(v2_payload, indent=2, ensure_ascii=False))
    print(f"Saved audited v2 ledger to: {args.v2_json}")

    # Build workbook
    build_workbook(datasets, settings, refs, overview, dest, args.root)


if __name__ == "__main__":
    main()
