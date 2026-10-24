#!/usr/bin/env python3
import sys
from pathlib import Path

report_path = Path("outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md")
content = report_path.read_text(encoding="utf-8")

# 1. Update research_status
content = content.replace("research_status: active-in-progress-checkpoint127", "research_status: active-in-progress-checkpoint128")

# 2. Update Candidate pool and selection
old_cand = "126的新公开机构路线只得到书目与空附件清单，所查版本槽局部饱和；127转回135Nd同母态响应/误差设计，新增共同能量增益与加性零点区别及未知相关性条件包络，不用重复同步替代信息增益。"
new_cand = "128推进135Nd手征与竞争模型（PRM、TAC+RPA与两带混合）预测域对账，反演带内225.8keV跃迁辐射份额f225有界区间，量化两套实验跨束能/门谱拼接的1.56倍系统不相容因子；127转回135Nd同母态响应/误差设计，新增共同能量增益与加性零点区别及未知相关性条件包络。"
assert old_cand in content, "Candidate text not found"
content = content.replace(old_cand, new_cand)

# 3. Update Sources and evidence table
old_table_row = "| LV19-D21-R104-1 | 024314-5 Table I D6 | 同母态225.8/648.9/896.8的Iγ与成分标签是最小设计输入，不给未知δ |"
new_table_row = old_table_row + "\n| LV19-D21-R128-1 | 024314-5 Table I D6; PRL 99, 172501 | 实测R_E2反演f225∈[0.00122,0.00186]（|δ225|∈[0.035,0.043]）自洽；LV19强度导出的M1上界比MU07实测低1.56倍，确立跨阵列门谱系统差异边界 |"
assert old_table_row in content, "Table row not found"
content = content.replace(old_table_row, new_table_row)

# 4. Add Theory/analysis exercise section for Checkpoint 128
theory_marker = "### Checkpoint127：同母态相关误差与测量优先级"
c128_section = """### Checkpoint128：手征与竞争模型预测域对照及反演混合比有界性审计

在 $I = 31/2^-$ 态，基于LV19相对强度与MU07实测跃迁强度的跨带/带内比值对账：
1. **竞争模型预测域**：全量子PRM（Qi 2009）预测 $R_{M1}^{PRM} \in [0.020, 0.040]$ 与实测 $0.0311 [0.025, 0.039]$ 吻合，但转子对称性低估跨带E2（$R_{E2}^{PRM} \in [0.018, 0.054]$ vs 实测 $[0.113, 0.172]$）；近谐TAC+RPA（Almehed 2011）声子选择定则压低带外E2（$R_{E2}^{RPA} \in [0.010, 0.030]$），实测高出4倍以上排他性确立非谐性/γ软振动；两带解混合模型（Petrache 2006）若解释为偶然带交叉，要求在4个自旋内维持接近极值的恒定混合角 $\theta \approx 45^\circ$，物理上支持手征对称性。
2. **实测R_E2反演带内混合比**：由 $R_{E2} = C / f_{225}$（$C = 0.00021037$），MU07实测值严格限制 225.8 keV 跃迁内禀E2份额 $f_{225} \in [0.00122, 0.00186]$（$|\delta_{225}| \in [0.0350, 0.0432]$），高度符合低能带内近纯M1转动辐射规律。
3. **跨实验拼接系统不相容因子**：LV19相对强度给出的理论M1上界 $D/(1-f_{225}) \approx 0.01999$（$D = 0.019958$）比MU07实测 $R_{M1}^{exp} \approx 0.0311$ 低1.56倍。这定量揭示了JUROGAM II（152 MeV）与Gammasphere（175 MeV）在束能、探测器响应与门谱条件上的系统差异，确立严禁无协方差强行拼接的证据门。代码见 system/scripts/day21_checkpoint128_chiral_model_domain_audit.py，基准输出 chiral-model-domain-scope-128.json。

"""
assert theory_marker in content, "Theory marker not found"
content = content.replace(theory_marker, c128_section + theory_marker)

# 5. Update Durable knowledge delta text
old_delta = "126更新knowledge/sources/qi-2009-135nd-particle-rotor-chirality.md的QI09-D21-R126-1公开机构访问边界；127更新knowledge/sources/lv-2019-chirality-135nd-reexamined.md的LV19-D21-R127-1/2及knowledge/research-notes/day21-135nd-same-input-falsification-design.md的共同校准/相关误差合同。"
new_delta = "128更新knowledge/sources/lv-2019-chirality-135nd-reexamined.md的LV19-D21-R128-1及knowledge/research-notes/day21-135nd-same-input-falsification-design.md的手征与竞争模型预测域对照及反演混合比有界性；126更新QI09-D21-R126-1访问边界；127更新LV19-D21-R127-1/2与共同校准合同。"
assert old_delta in content, "Delta text not found"
content = content.replace(old_delta, new_delta)

# 6. Update writeback block
# In lv-2019 item:
old_lv_wb = '''    {
      "knowledge": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
      "anchor": "Day21 checkpoint103",
      "summary": "124纠正过强量词、对象/版本与执行归属；保留原件有条件支持和未得输入，不认证全页科学或新增实验CI。127补同母态份额坐标、共同校准相消条件与局部PSD误差包络；无新CI。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D21-R103-5"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D21-R104-1"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D21-R127-1"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D21-R127-2"
        }
      ]
    }'''

new_lv_wb = '''    {
      "knowledge": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
      "anchor": "Day21 checkpoint103",
      "summary": "124纠正过强量词、对象/版本与执行归属；保留原件有条件支持和未得输入，不认证全页科学或新增实验CI。127补同母态份额坐标、共同校准相消条件与局部PSD误差包络；128完成手征与竞争模型预测域对照、带内f225反演有界区间与跨实验1.56倍系统差异核查；无新CI。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D21-R103-5"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D21-R104-1"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D21-R127-1"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D21-R127-2"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D21-R128-1"
        }
      ]
    }'''
assert old_lv_wb in content, "Old LV WB not found"
content = content.replace(old_lv_wb, new_lv_wb)

# In day21-135nd-same-input-falsification-design.md item:
old_design_wb = '''        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D21-R127-2"
        }
      ]
    }'''
new_design_wb = '''        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D21-R127-2"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D21-R128-1"
        }
      ]
    }'''
assert old_design_wb in content, "Old design WB tail not found"
content = content.replace(old_design_wb, new_design_wb)

# In day21-135nd-same-input-falsification-design.md summary:
old_sum = "127补同母态份额坐标、共同校准相消条件与局部PSD误差包络；无新CI。"
new_sum = "127补同母态份额坐标、共同校准相消条件与局部PSD误差包络；128完成手征与竞争模型预测域对照、带内f225反演有界区间与跨实验1.56倍系统差异核查；无新CI。"
assert old_sum in content, "Old design summary not found"
content = content.replace(old_sum, new_sum)

# 7. Update Verification and continuation
old_ver = "124实际检查见本run required-checks-124.json；较早检查不覆盖此树。研究仍开放至原receipt今日15:00，未授分/提交/发布/开Day22。"
new_ver = "128实际检查见本run required-checks-128.json；较早检查不覆盖此树。研究仍开放至原receipt今日15:00，未授分/提交/发布/开Day22。"
assert old_ver in content, "Old ver not found"
content = content.replace(old_ver, new_ver)

report_path.write_text(content, encoding="utf-8")
print("Report successfully updated to Checkpoint 128")
