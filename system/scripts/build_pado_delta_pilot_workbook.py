"""Build the bounded delta-extraction pilot from an audited JSON ledger."""

import argparse
import json
import math
import os
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.comments import Comment
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
    "AD_RATIO": "角分布比",
    "DCO_RATIO": "方向角关联比",
    "GATED_RATIO_OTHER": "门控比/须按实际响应处理",
    "UNRESOLVED": "定义待核",
    "NA": "不适用/未用比值",
}

TRANSITION_FIELDS = [
    "record_id", "ref_id", "setup_id", "nucleus", "E_gamma_keV", "Ji_pi", "Jf_pi",
    "delta_center", "delta_err_minus", "delta_err_plus", "delta_low", "delta_high",
    "delta_definition", "method", "used_data", "alignment_treatment", "sigma_I",
    "angular_coeffs", "ratio_status", "ratio_original_name", "ratio_value",
    "A_pol", "P", "alpha_IC", "locator", "delta_original", "delta_basis",
    "Ei_keV", "Ef_keV", "notes",
]
SETUP_FIELDS = [
    "setup_id", "ref_id", "dataset_id", "reaction_setup", "ratio_status",
    "ratio_original_name", "angular_definition", "angles", "gate",
    "polarization_calibration", "alignment_treatment", "alignment_value",
    "curve_evaluation", "final_alignment_condition", "alignment_details",
    "delta_convention", "uncertainty_model", "locator",
]
REF_FIELDS = [
    "ref_id", "doi", "extraction", "local_file", "supplement_file", "url",
]


def as_cell(value):
    if value is None:
        return None
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, str) and value.startswith(("=", "+", "@")):
        # Preserve source strings rather than interpreting them as formulas.
        return "'" + value
    return value


def internal_link(cell, sheet, row, column="A"):
    cell.hyperlink = Hyperlink(
        ref=cell.coordinate, location=f"'{sheet}'!{column}{row}", display=str(cell.value)
    )
    cell.font = Font(name="Calibri", size=11, color="0563C1", underline="single")


def populate(wb, name, fields, records, tablename):
    ws = wb.create_sheet(name)
    ws.append(fields)
    for record in records:
        ws.append([as_cell(record.get(f)) for f in fields])
    ws.freeze_panes = "H2" if name == "Delta" else "C2"
    ws.sheet_view.zoomScale = 80
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.sheet_properties.tabColor = "147D92"
    ws.row_dimensions[1].height = 34
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
        ws.row_dimensions[row[0].row].height = 78
    for i, field in enumerate(fields, 1):
        from openpyxl.utils import get_column_letter
        width = 16
        if field in ("notes", "extraction", "alignment_details", "angular_definition",
                     "curve_evaluation", "final_alignment_condition"):
            width = 62
        elif field in ("local_file", "supplement_file", "url", "locator", "method",
                       "polarization_calibration", "reaction_setup", "delta_convention",
                       "uncertainty_model", "gate"):
            width = 45
        elif field in ("angular_coeffs", "used_data", "alignment_treatment"):
            width = 29
        ws.column_dimensions[get_column_letter(i)].width = width
    if records:
        table = Table(displayName=tablename, ref=ws.dimensions)
        table.tableStyleInfo = TableStyleInfo(
            name="TableStyleMedium2", showRowStripes=True
        )
        ws.add_table(table)
    ws.print_title_rows = "1:1"
    ws.page_setup.orientation = "landscape"
    ws.page_setup.paperSize = ws.PAPERSIZE_A3
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    return ws


def build(ledger, destination, root):
    data = json.loads(ledger.read_text())
    transitions, setups, refs = (data[k] for k in ("transitions", "setups", "refs"))
    for key, rows, field in (("refs", refs, "ref_id"), ("setups", setups, "setup_id"),
                             ("transitions", transitions, "record_id")):
        ids = [row[field] for row in rows]
        assert len(ids) == len(set(ids)), f"Duplicate IDs in {key}"
    ref_rows = {r["ref_id"]: i for i, r in enumerate(refs, 2)}
    setup_rows = {r["setup_id"]: i for i, r in enumerate(setups, 2)}
    for row in transitions:
        assert row["ref_id"] in ref_rows and row["setup_id"] in setup_rows
        for key in ("delta_center", "delta_err_minus", "delta_err_plus",
                    "delta_low", "delta_high"):
            v = row.get(key)
            assert v is None or (isinstance(v, (float, int)) and math.isfinite(v)), (row["record_id"], key, v)
        for key in ("delta_err_minus", "delta_err_plus"):
            assert row.get(key) is None or row[key] >= 0
        c = row.get("delta_center")
        for err, bound, sign in (("delta_err_minus", "delta_low", -1),
                                  ("delta_err_plus", "delta_high", 1)):
            if c is not None and row.get(err) is not None and row.get(bound) is not None:
                assert math.isclose(c + sign * row[err], row[bound], abs_tol=1e-7)
        assert row["ratio_status"] in RATIOS
        assert row["alignment_treatment"] in ALIGNMENTS
    wb = Workbook()
    guide = wb.active
    guide.title = "Readme"
    guide.append(["项目", "说明"])
    instructions = [
        ("目的", "为 NST Reviewer 2 Comment 1 收集可追溯的方法证据；试填仅含 135Pr、187Au、61Ni，不用于估计全领域 commonly 的比例。"),
        ("范围", "不限年代；本轮为指定核素和所列文献的表格试填，不声称穷尽三个核素的所有文献。待用户审查表格后再扩大收集。"),
        ("导航", "Delta 主表：点击 ref_id 到文献，setup_id 到实验条件。Setups/References 的编号链接回对应首条数据，可再按编号筛选全部行。"),
        ("数据粒度", "一条记录是一篇文献的一条跃迁在一种分析条件下的一个结果/解支。文献采用值与本实验提取值用 delta_basis 区分。"),
        ("五列 delta", "delta_center=中心值；delta_err_minus/plus=向左/向右误差量（正数、非百分比）；delta_low/high=上下边界。"),
        ("边界含义", "普通误差条的边界=中心值减/加误差；只给限值/范围/多根时不虚构中心及误差，原文形式保存在 delta_original。"),
        ("缺失", "数值单元格留空表示没有可忠实填入的数值，不代表0；原因见 notes/设置表。NR=未报告，NA=不适用。"),
        ("原文与换算", "主表保留原文 delta 符号及约定；不会为匹配 PADO 静默反号。自行重建的 ratio 或校准换算须标明 derived，不能冒充实测。"),
        ("ratio 分类", "ratio_original_name 保留 Rac/Rtheta/RDCO 等原文记号；ratio_status 按实际定义分类，不能按名字推断。GATED_RATIO_OTHER 不预断该比值已等效于简单 W(theta1)/W(theta2)。"),
        ("测量与实际使用", "used_data 是提取该条 delta 实际使用的量；其他列出现数据不自动表示它参加了拟合。偏振不对称 A_pol 与校准后的 P 分列。"),
        ("固定的两个层次", "计算 response 曲线时固定 sigma 与最终推断固定单一 sigma 是不同问题；SCAN_COMBINE 保留逐值条件曲线及最后合并的事实。"),
        ("未报告", "UNREPORTED 不等于 FIX_ASSUMED。未报 sigma 也不证明完全没有取向假设；如用其他布居参数则在设置表注明。"),
        ("统计单位", "未来 commonly 的计数应以独立实验/分析方案为主；同实验多条跃迁、重复发表和同数据重分析不能当独立票数。"),
        ("原件追溯", "References 只保留 ref_id、DOI、extraction、原文/附件路径、网上链接。哈希等归档信息不进入工作簿。"),
        ("本地链接", "PDF超链接相对于本工作簿；保留Wiki目录结构时可迁移。办公软件可能要求允许打开本地文件。"),
        ("模型与审查", "Gemini 3.8 Flash (Tiered), reasoning high 承担初提取；父代理核对数字、方法和原件。用户本次审查的是表格输出；尚未启动大规模收集。"),
    ]
    for item in instructions:
        guide.append(item)
    guide.append(("alignment_treatment", "定义"))
    for key, value in ALIGNMENTS.items():
        guide.append((key, value))
    guide.append(("ratio_status", "定义"))
    for key, value in RATIOS.items():
        guide.append((key, value))
    guide.column_dimensions["A"].width = 30
    guide.column_dimensions["B"].width = 125
    guide.freeze_panes = "B2"
    for row in guide:
        guide.row_dimensions[row[0].row].height = 45
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.font = Font(name="Calibri", size=11)
    guide["A1"].fill = guide["B1"].fill = PatternFill("solid", fgColor="173B53")
    guide["A1"].font = guide["B1"].font = Font(color="FFFFFF", bold=True)
    for ref in refs:
        ref["extraction"] = ref.get("extraction") or (
            f'{ref.get("title", "")} ({ref.get("year", "")}); '
            f'{ref.get("extraction_version", "")}'
        )
    ws = populate(wb, "Delta", TRANSITION_FIELDS, transitions, "DeltaData")
    ss = populate(wb, "Setups", SETUP_FIELDS, setups, "SetupData")
    rs = populate(wb, "References", REF_FIELDS, refs, "ReferenceData")
    for index, row in enumerate(transitions, 2):
        internal_link(ws.cell(index, 2), "References", ref_rows[row["ref_id"]])
        internal_link(ws.cell(index, 3), "Setups", setup_rows[row["setup_id"]])
        if row.get("delta_err_minus") is not None:
            ws.cell(index, 9).comment = Comment("正的向左偏移量，不是误差百分比。", "Codex")
        if row.get("delta_err_plus") is not None:
            ws.cell(index, 10).comment = Comment("正的向右偏移量，不是误差百分比。", "Codex")
        for col in range(8, 13):
            ws.cell(index, col).fill = PatternFill("solid", fgColor="E6F2EE")
        if row.get("notes") and any(t in row["notes"].lower() for t in ["sign", "符号", "branch", "分支", "unclear"]):
            ws.cell(index, 30).fill = PatternFill("solid", fgColor="FFF1CE")
    for index, row in enumerate(setups, 2):
        first = next((i for i, t in enumerate(transitions, 2) if t["setup_id"] == row["setup_id"]), None)
        if first:
            internal_link(ss.cell(index, 1), "Delta", first)
        internal_link(ss.cell(index, 2), "References", ref_rows[row["ref_id"]])
    local_links = 0
    for index, row in enumerate(refs, 2):
        first = next((i for i, t in enumerate(transitions, 2) if t["ref_id"] == row["ref_id"]), None)
        if first:
            internal_link(rs.cell(index, 1), "Delta", first)
        if row.get("doi"):
            rs.cell(index, 2).hyperlink = "https://doi.org/" + row["doi"]
        for col, field in ((4, "local_file"), (5, "supplement_file")):
            if row.get(field):
                path = root / row[field]
                assert path.is_file(), path
                rs.cell(index, col).hyperlink = os.path.relpath(path, destination.parent)
                rs.cell(index, col).style = "Hyperlink"
                local_links += 1
        if row.get("url"):
            rs.cell(index, 6).hyperlink = row["url"]
    for column, choices in (("P", ALIGNMENTS), ("S", RATIOS)):
        validation = DataValidation(type="list", formula1='"' + ",".join(choices) + '"')
        validation.errorTitle = "请选择说明页中的分类"
        validation.error = "保留原文记号，按实际方法分类。"
        validation.showErrorMessage = True
        ws.add_data_validation(validation)
        validation.add(f"{column}2:{column}{max(2, ws.max_row)}")
    wb.active = wb.sheetnames.index("Delta")
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        raise FileExistsError(f"Refusing to replace workbook: {destination}")
    wb.save(destination)
    check = load_workbook(destination, data_only=False)
    assert check["Delta"].max_row == len(transitions) + 1
    assert check["References"].max_row == len(refs) + 1
    assert all(check["Delta"].cell(i, 2).hyperlink.location for i in range(2, len(transitions) + 2))
    assert not any(c.data_type == "f" for sheet in check for row in sheet for c in row)
    print(json.dumps({"workbook": str(destination), "transitions": len(transitions),
                      "setups": len(setups), "refs": len(refs),
                      "local_links_verified": local_links, "validation": "passed"}, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    build(args.ledger, args.output, args.root)
