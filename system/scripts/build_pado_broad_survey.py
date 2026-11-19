"""Render an evidence-screened PDM survey without modifying earlier workbooks."""

import argparse
import json
import os
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.drawing.image import Image
from openpyxl.worksheet.hyperlink import Hyperlink

from build_pado_nuclide_summary_workbook import FIELDS, HEADERS, RFIELDS, style
from add_pado_original_data_sheet import HEADERS as DATA_HEADERS


def link(cell, sheet, row):
    cell.hyperlink = Hyperlink(ref=cell.coordinate, location=f"'{sheet}'!A{row}")
    cell.style = 'Hyperlink'


def build(data, output, root):
    if output.exists():
        raise FileExistsError(output)
    records, refs, rows = data['records'], data['refs'], data['data_rows']
    ref_ids = [r['ref_id'] for r in refs]
    assert len(set(ref_ids)) == len(ref_ids)
    assert all(r.get('p_joint_verified') is True for r in records)
    pairs = [(r['nuclide'], r['ref_id']) for r in records]
    assert len(set(pairs)) == len(pairs)
    assert all(r['ref_id'] in ref_ids for r in records)
    for row in rows:
        assert len(row) == len(DATA_HEADERS)
        assert (row[0], row[1]) in pairs
        for value in row[7:9]:
            assert value is None or (isinstance(value, (int, float)) and value >= 0)
        assert row[-1], 'Each data row requires a primary-source locator'

    wb = Workbook()
    ns = wb.active
    ns.title = 'Nuclide'
    ds = wb.create_sheet('Data')
    rs = wb.create_sheet('References')
    gs = wb.create_sheet('说明')
    ns.append(HEADERS)
    ds.append(DATA_HEADERS)
    rs.append(['文献编号', 'DOI', '提取位置', '本地正文', '本地补充材料', '网上入口'])
    for record in records:
        ns.append([record.get(k) for k in FIELDS])
    for row in rows:
        ds.append(row)
    for ref in refs:
        rs.append([ref.get(k) for k in RFIELDS])
    gs.append(['项目', '说明'])
    for row in [
        ('用途', '核对σ/I报道与处理方法；保存原文δ及P、角信息，准备PDM复算。'),
        ('范围', '不限年代；E2/M1；P必须参与定量δ约束。Nuclide按核素－研究列出，不按跃迁计数。'),
        ('数据', 'Data只放原文结果和输入。空白表示未提取到可核实数值；图示保留原图或定位，不估读。'),
        ('偏振', 'P和实测不对称度分列；未把Δ/Q计算结果冒充原文表列P。'),
        ('误差', 'δ下、上误差是相对中心值的正绝对偏移，不是百分数。保留原文分支。'),
        ('σ/I', '未报道不等于固定；分别记录假定固定、标定后固定、联合拟合、扫描及其他布居参数。'),
        ('导航', '点击核素在Nuclide与Data间跳转；点击文献编号和References中的路径/链接打开原文。'),
        ('检索边界', data.get('coverage_note', '本表是可追溯的阶段结果，不宣称穷尽。')),
    ]:
        gs.append(row)
    style(ns, [12, 16, 34, 35, 28, 24, 20, 38, 36, 40], 'NuclideSurvey')
    style(ds, [12, 16, 14, 12, 12, 29, 14, 14, 14, 27, 29, 25, 25, 22, 37, 22, 22, 22, 43, 39, 53], 'OriginalPDMData')
    style(rs, [16, 36, 45, 65, 65, 60], 'NuclideReferences')
    style(gs, [20, 110], 'ReadingGuide')
    ds.freeze_panes = 'D2'
    ni = {pair: i for i, pair in enumerate(pairs, 2)}
    ri = {r['ref_id']: i for i, r in enumerate(refs, 2)}
    first = {}
    for i, row in enumerate(rows, 2):
        pair = (row[0], row[1])
        first.setdefault(pair, i)
        link(ds.cell(i, 1), 'Nuclide', ni[pair])
        link(ds.cell(i, 2), 'References', ri[row[1]])
        ds.row_dimensions[i].height = 60
        for c in ds[i]:
            if isinstance(c.value, (float, int)):
                c.number_format = '0.######'
    for pair, i in ni.items():
        if pair in first:
            link(ns.cell(i, 1), 'Data', first[pair])
        link(ns.cell(i, 2), 'References', ri[pair[1]])
    for ref in refs:
        i = ri[ref['ref_id']]
        link(rs.cell(i, 1), 'Nuclide', next(j for pair, j in ni.items() if pair[1] == ref['ref_id']))
        if ref.get('doi'):
            rs.cell(i, 2).hyperlink = 'https://doi.org/' + ref['doi']
        if ref.get('url'):
            rs.cell(i, 6).hyperlink = ref['url']
        for col, field in [(4, 'local_file'), (5, 'supplement_file')]:
            if ref.get(field):
                path = root / ref[field]
                assert path.is_file(), path
                rs.cell(i, col).hyperlink = os.path.relpath(path, output.parent)
                rs.cell(i, col).style = 'Hyperlink'
    anchor = len(rows) + 5
    for item in data.get('figures', []):
        path = root / item['path']
        assert path.is_file(), path
        ds.cell(anchor, 1, item['caption'])
        image = Image(path)
        factor = min(1, 1000 / image.width)
        image.width *= factor
        image.height *= factor
        ds.add_image(image, f'A{anchor + 1}')
        anchor += max(16, int(image.height / 20) + 5)
    ns.sheet_properties.tabColor = '148A8A'
    wb.active = 0
    output.parent.mkdir(parents=True, exist_ok=True)
    wb.save(output)
    check = load_workbook(output)
    for sheet in check:
        for row in sheet:
            for cell in row:
                assert cell.data_type != 'f', 'Source text must not become an Excel formula'
                if cell.hyperlink and cell.hyperlink.location:
                    name, address = cell.hyperlink.location.split('!')
                    assert check[name.strip("'")][address].value is not None
                if cell.hyperlink and cell.hyperlink.target and not cell.hyperlink.target.startswith('http'):
                    assert (output.parent / cell.hyperlink.target).resolve().is_file()
    assert list(check['Data'].values)[1:len(rows) + 1] == [tuple(r) for r in rows]
    return {'workbook': str(output), 'nuclides': len({r['nuclide'] for r in records}),
            'studies': len(refs), 'nuclide_study_rows': len(records),
            'data_rows': len(rows), 'validation': 'passed'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    args = parser.parse_args()
    print(json.dumps(build(json.loads(args.data.read_text()), args.output, args.root), ensure_ascii=False))
