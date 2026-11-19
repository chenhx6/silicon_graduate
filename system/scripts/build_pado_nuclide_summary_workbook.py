"""Render the P-required, nuclide-level PDM literature summary."""
import argparse
import json
import os
from pathlib import Path
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.worksheet.hyperlink import Hyperlink
from openpyxl.worksheet.table import Table, TableStyleInfo

FIELDS = ['nuclide','ref_id','method','p_data','angular','sigma_reported','sigma_value','sigma_treatment','pdm_readiness','locator']
HEADERS = ['核素','文献','δ怎样联合提取','P数据情况','联合使用的角信息','是否报告σ/I数值','σ/I数值','σ/I如何处理','PDM复算还需准备什么','原文定位']
RFIELDS = ['ref_id','doi','extraction','local_file','supplement_file','url']


def style(ws, widths, name):
    ws.freeze_panes='C2'
    ws.sheet_view.zoomScale=80
    ws.row_dimensions[1].height=42
    for c in ws[1]:
        c.font=Font(name='Microsoft YaHei',size=11,bold=True,color='FFFFFF')
        c.fill=PatternFill('solid',fgColor='214D60')
        c.alignment=Alignment(wrap_text=True,vertical='center')
    for row in ws.iter_rows(min_row=2):
        ws.row_dimensions[row[0].row].height=106
        for c in row:
            c.font=Font(name='Microsoft YaHei',size=11)
            c.alignment=Alignment(wrap_text=True,vertical='center')
    for i,width in enumerate(widths,1):
        from openpyxl.utils import get_column_letter
        ws.column_dimensions[get_column_letter(i)].width=width
    table=Table(displayName=name,ref=ws.dimensions)
    table.tableStyleInfo=TableStyleInfo(name='TableStyleMedium2',showRowStripes=True)
    ws.add_table(table)
    ws.print_title_rows='1:1'
    ws.page_setup.orientation='landscape'
    ws.page_setup.paperSize=ws.PAPERSIZE_A3
    ws.page_setup.fitToWidth=1
    ws.page_setup.fitToHeight=1
    ws.sheet_properties.pageSetUpPr.fitToPage=True


def build(data, target, root):
    records=data['records'];refs=data['refs']
    assert len(records)==5 and {r['nuclide'] for r in records}=={'61Ni','135Pr','187Au','72Se','136Nd'}
    assert len(refs)==5 and {r['ref_id'] for r in refs}=={r['ref_id'] for r in records}
    assert all(r.get('p_joint_verified') is True for r in records)
    assert not target.exists(), f'Refusing to replace {target}'
    wb=Workbook();ws=wb.active;ws.title='Nuclide';ws.append(HEADERS)
    rs=wb.create_sheet('References');rs.append(['文献编号','DOI','提取位置','本地正文','本地补充材料','网上入口'])
    guide=wb.create_sheet('说明')
    for r in records:ws.append([r.get(k) for k in FIELDS])
    for r in refs:rs.append([r.get(k) for k in RFIELDS])
    style(ws,[12,12,34,35,25,23,14,36,40,35],'NuclideSurvey')
    style(rs,[12,36,45,65,65,60],'NuclideReferences')
    rindex={r['ref_id']:i for i,r in enumerate(refs,2)}
    nindex={r['ref_id']:i for i,r in enumerate(records,2)}
    for i,r in enumerate(records,2):
        ws.cell(i,2).hyperlink=Hyperlink(ref=ws.cell(i,2).coordinate,location=f"'References'!A{rindex[r['ref_id']]}")
        ws.cell(i,2).style='Hyperlink'
    for i,r in enumerate(refs,2):
        rs.cell(i,1).hyperlink=Hyperlink(ref=rs.cell(i,1).coordinate,location=f"'Nuclide'!A{nindex[r['ref_id']]}")
        rs.cell(i,1).style='Hyperlink'
        rs.cell(i,2).hyperlink='https://doi.org/'+r['doi']
        rs.cell(i,6).hyperlink=r['url']
        for col,key in [(4,'local_file'),(5,'supplement_file')]:
            if r.get(key):
                p=root/r[key];assert p.is_file(),p
                rs.cell(i,col).hyperlink=os.path.relpath(p,target.parent)
                rs.cell(i,col).style='Hyperlink'
    notes=[
        ('用途','①核对文献是否给σ/I及其处理方法，准备审稿回复；②查明P和角信息是否足够用于PDM复算。'),
        ('怎样读','先看Nuclide，一核素一行。点文献编号打开References，再点正文或DOI看原文。'),
        ('纳入条件','限E2/M1研究；P必须参与定量联合求解δ。只有偏振符号确认或无P的文章不纳入。'),
        ('P与不对称度','实测不对称度Δ配合灵敏度Q可得到P；表中明确区分。Δ不能直接当P输入。'),
        ('σ/I','分别记录是否给出数值、取值及处理方式。未给σ/I、改用其他布居参数、扫描、联合拟合和固定有不同含义。'),
        ('角信息','G22为单角R_ADO，L22为探测器分组R_ADO；DCO复算还需要对应门条件及DCO响应。'),
        ('范围','这五行对应所选的五篇P联合求解研究，未穷尽五个核素的全部文献。未做新的PDM拟合。'),
        ('下一步','先检查这五行是否清楚，再选择可用输入开展PDM复算；当前不展开逐跃迁δ表。')]
    guide.append(['项目','说明'])
    for row in notes:guide.append(row)
    style(guide,[20,110],'ReadingGuide')
    ws.sheet_properties.tabColor='148A8A';ws.sheet_view.tabSelected=True;wb.active=0
    target.parent.mkdir(parents=True,exist_ok=True);wb.save(target)
    check=load_workbook(target)
    assert check.sheetnames==['Nuclide','References','说明']
    assert check['Nuclide'].max_row==6
    assert not any(c.data_type=='f' for sh in check for row in sh for c in row)
    for sh in check:
        for row in sh:
            for c in row:
                if c.hyperlink and c.hyperlink.location:
                    name,cell=c.hyperlink.location.split('!');assert check[name.strip("'")][cell].value is not None
                if c.hyperlink and c.hyperlink.target and not c.hyperlink.target.startswith('http'):
                    assert (target.parent/c.hyperlink.target).resolve().is_file()
    print(json.dumps({'workbook':str(target),'nuclides':5,'references':5,'sheets':check.sheetnames,'validation':'passed'},ensure_ascii=False))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--data',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--root',type=Path,default=Path.cwd());a=p.parse_args()
    build(json.loads(a.data.read_text()),a.output,a.root)
