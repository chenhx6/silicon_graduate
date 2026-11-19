"""Build the original-data collection, without a PDM-applicability filter."""

import argparse
import json
import os
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.hyperlink import Hyperlink
from openpyxl.worksheet.table import Table, TableStyleInfo


NUCLIDE_FIELDS = ['nuclide', 'ref_id', 'method', 'p_role', 'p_data', 'angular',
                  'sigma_reported', 'sigma_value', 'sigma_treatment', 'locator']
NUCLIDE_HEADERS = ['核素', '文献', '原文δ提取方法', 'P在原文中的用途', '原文偏振数据',
                   '原文角信息', 'σ/I是否报道', 'σ/I数值', '原文取向参数处理', '原文定位']
DATA_HEADERS = [
    '核素', '文献', 'Eγ (keV)', 'Jiπ', 'Jfπ', 'δ（原文）', 'δ中心值',
    'δ下误差（绝对量）', 'δ上误差（绝对量）', 'P（原文记号）', '偏振观测量（原文记号）',
    '角系数1（a₂/A₂₂等）', '角系数2（a₄/A₄₄等）', '角比值记号',
    '角比值（原文）', 'R_ADO（原文）', 'R_DCO（原文）', '取向参数（原文）',
    '角度/几何（原文）', '门/级联（原文）', '原文位置', '其他原文输入量',
]
REFERENCE_FIELDS = ['ref_id', 'title', 'doi', 'extraction', 'local_file',
                    'supplement_file', 'url', 'access_status']
REFERENCE_HEADERS = ['文献', '原文题名', 'DOI', '数据位置', '本地原文/材料',
                     '本地补充材料', '网上入口', '原件情况']


def style(sheet, widths, table_name):
    sheet.freeze_panes = 'C2'
    sheet.sheet_view.zoomScale = 80
    sheet.row_dimensions[1].height = 40
    for cell in sheet[1]:
        cell.font = Font(name='Microsoft YaHei', size=11, bold=True, color='FFFFFF')
        cell.fill = PatternFill('solid', fgColor='214D60')
        cell.alignment = Alignment(wrap_text=True, vertical='center')
    for row in sheet.iter_rows(min_row=2):
        sheet.row_dimensions[row[0].row].height = 68 if sheet.title == 'Data' else 100
        for cell in row:
            cell.font = Font(name='Microsoft YaHei', size=11)
            cell.alignment = Alignment(wrap_text=True, vertical='center')
            if isinstance(cell.value, (int, float)):
                cell.number_format = '0.######'
    for index, width in enumerate(widths, 1):
        sheet.column_dimensions[get_column_letter(index)].width = width
    if sheet.max_row > 1:
        table = Table(displayName=table_name, ref=sheet.dimensions)
        table.tableStyleInfo = TableStyleInfo(name='TableStyleMedium2', showRowStripes=True)
        sheet.add_table(table)
    sheet.print_title_rows = '1:1'
    sheet.page_setup.orientation = 'landscape'
    sheet.page_setup.fitToWidth = 1
    sheet.page_setup.fitToHeight = 0
    sheet.sheet_properties.pageSetUpPr.fitToPage = True


def internal_link(cell, sheet, row):
    cell.hyperlink = Hyperlink(ref=cell.coordinate, location=f"'{sheet}'!A{row}")
    cell.style = 'Hyperlink'


def build(payload, target, root):
    if target.exists():
        raise FileExistsError(target)
    records, refs, rows = payload['records'], payload['refs'], payload['data_rows']
    pairs = [(r['nuclide'], r['ref_id']) for r in records]
    assert len(set(pairs)) == len(pairs), 'Duplicate nuclide-study identity'
    ref_ids = [r['ref_id'] for r in refs]
    assert len(set(ref_ids)) == len(ref_ids)
    assert all(r['ref_id'] in ref_ids for r in records)
    for row in rows:
        assert len(row) == len(DATA_HEADERS)
        assert (row[0], row[1]) in pairs
        assert row[20], 'A data locator is required'
        for value in row[7:9]:
            assert value is None or (isinstance(value, (int, float)) and value >= 0)

    wb = Workbook()
    ns = wb.active
    ns.title = 'Nuclide'
    ds = wb.create_sheet('Data')
    rs = wb.create_sheet('References')
    ns.append(NUCLIDE_HEADERS)
    ds.append(DATA_HEADERS)
    rs.append(REFERENCE_HEADERS)
    for r in records:
        ns.append([r.get(k) for k in NUCLIDE_FIELDS])
    for row in rows:
        ds.append(row)
    for r in refs:
        rs.append([r.get(k) for k in REFERENCE_FIELDS])
    style(ns, [12, 14, 38, 24, 36, 34, 30, 22, 38, 42], 'NuclideCollection')
    style(ds, [12, 14, 14, 12, 12, 32, 15, 15, 15, 29, 37, 30, 30, 20, 32, 25, 25, 25, 38, 35, 55, 52], 'OriginalDataCollection')
    style(rs, [14, 65, 38, 46, 70, 70, 65, 31], 'ReferenceCollection')
    ds.freeze_panes = 'D2'
    ni = {pair: i for i, pair in enumerate(pairs, 2)}
    ri = {ref: i for i, ref in enumerate(ref_ids, 2)}
    first = {}
    for i, row in enumerate(rows, 2):
        pair = (row[0], row[1])
        first.setdefault(pair, i)
        internal_link(ds.cell(i, 1), 'Nuclide', ni[pair])
        internal_link(ds.cell(i, 2), 'References', ri[row[1]])
    for pair, i in ni.items():
        if pair in first:
            internal_link(ns.cell(i, 1), 'Data', first[pair])
        internal_link(ns.cell(i, 2), 'References', ri[pair[1]])
    for ref in refs:
        i = ri[ref['ref_id']]
        match = next((j for pair, j in ni.items() if pair[1] == ref['ref_id']), None)
        if match is not None:
            internal_link(rs.cell(i, 1), 'Nuclide', match)
        if ref.get('doi'):
            rs.cell(i, 3).hyperlink = 'https://doi.org/' + ref['doi']
        if ref.get('url'):
            rs.cell(i, 7).hyperlink = ref['url']
        for col, field in [(5, 'local_file'), (6, 'supplement_file')]:
            if ref.get(field):
                path = root / ref[field]
                assert path.is_file(), path
                rs.cell(i, col).hyperlink = os.path.relpath(path, target.parent)
                rs.cell(i, col).style = 'Hyperlink'
    anchor = len(rows) + 5
    for item in payload.get('figures', []):
        path = root / item['path']
        assert path.is_file(), path
        ds.cell(anchor, 1, item['caption'])
        pic = Image(path)
        factor = min(1, 1050 / pic.width)
        pic.width *= factor
        pic.height *= factor
        ds.add_image(pic, f'A{anchor + 1}')
        anchor += max(15, int(pic.height / 20) + 5)
    ns.sheet_properties.tabColor = '148A8A'
    wb.active = 0
    # Literal source equations starting with '=' must never become executable cells.
    for sheet in wb:
        for row in sheet:
            for cell in row:
                if isinstance(cell.value, str):
                    cell.data_type = 's'
    target.parent.mkdir(parents=True, exist_ok=True)
    wb.save(target)
    check = load_workbook(target)
    assert check.sheetnames == ['Nuclide', 'Data', 'References']
    assert list(check['Data'].values)[1:len(rows) + 1] == [tuple(r) for r in rows]
    for sh in check:
        for row in sh:
            for cell in row:
                assert cell.data_type != 'f', 'Original text must not become an Excel formula'
                if cell.hyperlink and cell.hyperlink.location:
                    name, address = cell.hyperlink.location.split('!')
                    assert check[name.strip("'")][address].value is not None
                if cell.hyperlink and cell.hyperlink.target and not cell.hyperlink.target.startswith('http'):
                    assert (target.parent / cell.hyperlink.target).resolve().is_file()
    return {'workbook': str(target), 'nuclides': len({r['nuclide'] for r in records}),
            'nuclide_study_rows': len(records), 'studies_with_data': len({r[1] for r in rows}),
            'references': len(refs), 'original_data_rows': len(rows), 'validation': 'passed'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    args = parser.parse_args()
    print(json.dumps(build(json.loads(args.data.read_text()), args.output, args.root), ensure_ascii=False))
