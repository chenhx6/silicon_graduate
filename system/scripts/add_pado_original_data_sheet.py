"""Append reported numerical inputs to the five-nuclide survey workbook."""

import argparse
import json
import re
from pathlib import Path

import pymupdf
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.hyperlink import Hyperlink
from openpyxl.worksheet.table import Table, TableStyleInfo


HEADERS = [
    '核素', '文献', 'Eγ (keV)', 'Jiπ', 'Jfπ', 'δ（原文数值）',
    'δ中心值', 'δ下误差', 'δ上误差', 'P（原文）', '偏振不对称度（原文）',
    'a₂（原文）', 'a₄（原文）', '角比值原文记号', '角比值（原文）',
    'R_ADO（原文）', 'R_DCO（原文）', 'σ/I或σ/j（原文）', '角度（°）',
    '门条件（keV）', '原文位置',
]


def original_text(value):
    if value is None:
        return None
    if isinstance(value, str):
        return value.replace('\\pm', '±').replace('+/-', '±')
    return value


def delta_text(row):
    c, lower, upper = (row[k] for k in ('delta_center', 'delta_err_minus', 'delta_err_plus'))
    if lower == upper:
        return f'{c:g} ± {lower:g}'
    return f'{c:g} (+{upper:g}, −{lower:g})'


def values(row):
    ref, energy = row['ref_id'], row['E_gamma_keV']
    a2 = a4 = rado = rdco = angles = gate = None
    coefficients = row.get('angular_coeffs') or ''
    for label, value in re.findall(r'(a[24])=([^;]+)', coefficients):
        if label == 'a2':
            a2 = original_text(value.strip())
        else:
            a4 = original_text(value.strip())
    p = original_text(row.get('P'))
    ratio = original_text(row.get('ratio_value'))
    if ref == 'W77':
        angles = 'P: 90°'
        match = re.search(r'Table 3, p\. (40|41)', row['locator'])
        if match:
            row = dict(row, locator=f'Table 3, p.{match.group(1)}')
    elif ref == 'L22':
        rado = ratio
        angles = 'Rac: (157.6°,133.6°)/(75.5°,104.5°)'
        gate = {747.3: 'P: 450', 813.2: 'P: 796', 450.2: 'P: 747'}[energy]
    elif ref == 'G22':
        panel = 'a' if energy == 376 else 'b'
        p = ratio = rado = f'Fig.3({panel})'
        angles = 'Rac: 154°/90°; P: 90°'
        gate = ('316,319,400,417,471,565,625' if energy == 376
                else '316,400; 313（峰左侧）')
    elif ref == 'SE22':
        matches = dict(re.findall(r'(RDCO|R_ADO)=([^;]+)', ratio))
        rado, rdco = matches.get('R_ADO'), matches.get('RDCO')
        ratio = f'RDCO={rdco}; Rθ={rado}'
        angles = 'RDCO: 148°/90°; Rθ: 148°/90°; P: 90°'
        gate = 'RDCO/Rθ: 976.7' if energy == 454.5 else 'RDCO/Rθ: 862.0'
    elif ref == 'ND22':
        gate = 'P: 989'
    return [
        row['nucleus'], ref, energy, row['Ji_pi'], row['Jf_pi'], delta_text(row),
        row['delta_center'], row['delta_err_minus'], row['delta_err_plus'], p,
        original_text(row.get('A_pol')), a2, a4, row.get('ratio_original_name'),
        ratio, rado, rdco,
        f"σ/j={row['sigma_I']:g}" if ref == 'SE22' and row.get('sigma_I') is not None else row.get('sigma_I'),
        angles, gate, row['locator'],
    ]


def figure(ws, pdf, page_index, clip, scratch, filename, caption, anchor_row):
    output = scratch / filename
    document = pymupdf.open(pdf)
    document[page_index].get_pixmap(matrix=pymupdf.Matrix(3, 3),
                                  clip=pymupdf.Rect(*clip)).save(output)
    ws.cell(anchor_row, 1, caption)
    picture = Image(output)
    factor = min(1, 1000 / picture.width)
    picture.width *= factor
    picture.height *= factor
    ws.add_image(picture, f'A{anchor_row + 1}')


def build(root, source, output, ledger, scratch):
    assert source.is_file() and not output.exists()
    original = load_workbook(source)
    baseline = {s.title: list(s.values) for s in original}
    refs = json.loads((root / 'outputs/literature-acquisition/20261118-pado-nuclide-summary/summary.json').read_text())['refs']
    old = json.loads(ledger.read_text())
    selected = {r['ref_id'] for r in refs}
    rows = [r for r in old['datasets'] if r['ref_id'] in selected]
    rows.append({
        'nucleus': '136Nd', 'ref_id': 'ND22', 'E_gamma_keV': 751,
        'Ji_pi': '17+', 'Jf_pi': '16+', 'delta_center': -0.48,
        'delta_err_minus': 0.14, 'delta_err_plus': 0.13,
        'P': '0.02 (+0.04, −0.05)', 'A_pol': '0.03 (+0.06, −0.07)',
        'ratio_original_name': 'Rac', 'ratio_value': '0.55(5)',
        'locator': 'PRC105,034302, 主文pp.3–4; Fig.3',
    })
    assert len(rows) == 22
    ws = original.create_sheet('Data', 1)
    ws.append(HEADERS)
    for row in rows:
        ws.append(values(row))
    count = ws.max_row
    ws.freeze_panes = 'D2'
    ws.sheet_view.zoomScale = 80
    ws.row_dimensions[1].height = 38
    for cell in ws[1]:
        cell.font = Font(name='Microsoft YaHei', color='FFFFFF', bold=True, size=11)
        cell.fill = PatternFill('solid', fgColor='214D60')
        cell.alignment = Alignment(wrap_text=True, vertical='center')
    widths = [12, 12, 14, 12, 12, 29, 14, 14, 14, 27, 29, 25, 25, 22, 37, 22, 22, 16, 43, 39, 53]
    from openpyxl.utils import get_column_letter
    for index, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(index)].width = width
    for row in ws.iter_rows(min_row=2, max_row=count):
        ws.row_dimensions[row[0].row].height = 48
        for cell in row:
            cell.font = Font(name='Microsoft YaHei', size=11)
            cell.alignment = Alignment(wrap_text=True, vertical='center')
            if isinstance(cell.value, (float, int)):
                cell.number_format = '0.######'
    table = Table(displayName='OriginalPDMData', ref=f'A1:U{count}')
    table.tableStyleInfo = TableStyleInfo(name='TableStyleMedium2', showRowStripes=True)
    ws.add_table(table)
    rindex = {r['ref_id']:i for i,r in enumerate(refs,2)}
    nindex = {original['Nuclide'].cell(i,2).value:i for i in range(2,7)}
    first = {}
    for i,row in enumerate(rows,2):
        ref = row['ref_id'];first.setdefault(ref,i)
        ws.cell(i,1).hyperlink = Hyperlink(ref=f'A{i}', location=f"'Nuclide'!A{nindex[ref]}")
        ws.cell(i,2).hyperlink = Hyperlink(ref=f'B{i}', location=f"'References'!A{rindex[ref]}")
        ws.cell(i,1).style = ws.cell(i,2).style = 'Hyperlink'
        if ref == 'G22':
            for column in (10, 15, 16):
                cell = ws.cell(i, column)
                cell.hyperlink = Hyperlink(ref=cell.coordinate, location="'Data'!A27")
                cell.style = 'Hyperlink'
    for ref, i in first.items():
        c = original['Nuclide'].cell(nindex[ref],1)
        c.hyperlink = Hyperlink(ref=c.coordinate, location=f"'Data'!A{i}")
        c.style = 'Hyperlink'
    scratch.mkdir(parents=True, exist_ok=True)
    byref = {r['ref_id']:r for r in refs}
    figure(ws, root/byref['G22']['local_file'], 2, (140,50,454,173), scratch,
           'g22_fig3ab.png', 'G22 · 原文Fig.3(a,b)', 27)
    se = root/byref['SE22']['local_file']
    figure(ws, se, 6, (28,57,562,199), scratch, 'se22_tableII.png',
           'SE22 · 原文Table II', 50)
    figure(ws, se, 6, (28,535,295,734), scratch, 'se22_fig6.png',
           'SE22 · 原文Fig.6', 76)
    guide = original['说明']
    for row in guide:
        for c in row:
            if isinstance(c.value,str) and '当前不展开逐跃迁δ表' in c.value:
                c.value = '点击Nuclide页核素可打开Data页；Data只列原文数据和原文图表。'
    original.active = 0
    original.save(output)
    check = load_workbook(output)
    assert list(check['Nuclide'].values) == baseline['Nuclide']
    assert list(check['References'].values) == baseline['References']
    assert len(check['Data'].tables) == 1 and len(check['Data']._images) == 3
    assert check['Data'].tables['OriginalPDMData'].ref == 'A1:U23'
    for i,r in enumerate(rows,2):
        assert check['Data'].cell(i,7).value == r['delta_center']
        assert check['Data'].cell(i,8).value == r['delta_err_minus']
        assert check['Data'].cell(i,9).value == r['delta_err_plus']
    assert not any(c.comment for row in check['Data'] for c in row)
    print(json.dumps({'output':str(output),'records':len(rows),'source_figures':3,
                      'sheets':check.sheetnames,'checks':'passed'},ensure_ascii=False))


if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--root',type=Path,default=Path.cwd())
    p.add_argument('--source',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--ledger',type=Path,required=True)
    p.add_argument('--scratch',type=Path,required=True)
    a=p.parse_args();build(a.root,a.source,a.output,a.ledger,a.scratch)
