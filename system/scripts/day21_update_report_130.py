#!/usr/bin/env python3
import sys
from pathlib import Path

report_path = Path("outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md")
content = report_path.read_text(encoding="utf-8")

# 1. Update research_status
content = content.replace("research_status: active-in-progress-checkpoint129", "research_status: active-in-progress-checkpoint130")

# 2. Update Candidate pool and selection
old_cand = "129完成135Nd多自旋（31/2-至37/2-）跨带E2单调增长3.56倍的手征隧穿机制核对，揭示带内|δin|严格保持在[0.034,0.061]的超高稳定性；128推进手征与竞争模型预测域对账与跨实验1.56倍差异；127完成同母态误差与相消设计。"
new_cand = "130完成135Nd五自旋（31/2-至39/2-）四极矩比值高度同态性（Qt比0.9356±0.0102）与39/2态1.043倍步调一致集体失活反证审计，排他性反驳形状共存与偶然交叉；129完成跨带E2增长3.56倍核对；128/127完成模型域与误差设计。"
assert old_cand in content, "Candidate text not found"
content = content.replace(old_cand, new_cand)

# 3. Update Sources and evidence table
old_table_row = "| LV19-D21-R129-1 | 024314-5 Table I Band D6; PRL 99, 172501 | 四个自旋态实测R_E2单调增长3.56倍体现手征隧穿演化；反演带内|δin|稳定在[0.034,0.061]（f_E2在0.11%–0.37%）证明两套实验深刻自洽，跨实验M1波动揭示门谱依赖性 |"
new_table_row = old_table_row + "\n| MU07-D21-R130-1 | PRL 99, 172501 Table I | 五自旋Qt(B)/Qt(A)均值0.9356±0.0102（散度1.09%）排除Qt相差2倍的形状共存；39/2处两带骤降2.5倍且对称比1.043步调一致失活，反驳偶然带交叉 |"
assert old_table_row in content, "Table row not found"
content = content.replace(old_table_row, new_table_row)

# 4. Add Theory/analysis exercise section for Checkpoint 130
theory_marker = "### Checkpoint129：多自旋混合比反演与跨带E2增长物理机制审计"
c130_section = """### Checkpoint130：四极矩比值同态性与39/2自旋步调一致失活的反证排除审计

覆盖 $31/2^-$ 至 $39/2^-$ 全部五个自旋态的反证检验：
1. **四极矩比值高度同态性**：提取实测跃迁四极矩比值 $Q_t(B) / Q_t(A) = \\sqrt{B(E2)_B / B(E2)_A}$，在五个态上分别为 $0.9354, 0.9354, 0.9354, 0.9520, 0.9199$，均值严格为 $0.9356 \\pm 0.0102$（相对散度仅 $1.09\\%$，最大偏离 $\\le 0.016$）。内禀四极形变差异被刚性限制在 $6.4\\% \\pm 1.0\\%$ 内，排除了类似 $^{134}\\text{Pr}$ 中未混合 $Q_t$ 相差 2.0 倍的形状共存能带交叉假说（后者无法在能量分母变化时维持五态恒定的同态比）。
2. **39/2自旋步调一致失活**：在 $39/2^-$ 处两带 $B(E2)$ 分别由平台期骤降 $2.46$ 倍（Band A）与 $2.57$ 倍（Band B），两带淬灭因子对称比值为 $1.043$（偏差仅 $4.3\\%$），同时四极矩比值仍保持 $0.920$。这一步调一致的集体性失活排他性证明两带微观结构对称绑定，反驳了非相关单粒子能级偶然交叉构型。代码见 system/scripts/day21_checkpoint130_quadrupole_homomorphism_audit.py，基准输出 quadrupole-homomorphism-scope-130.json。

"""
assert theory_marker in content, "Theory marker not found"
content = content.replace(theory_marker, c130_section + theory_marker)

# 5. Update Durable knowledge delta text
old_delta = "129更新knowledge/sources/lv-2019-chirality-135nd-reexamined.md的LV19-D21-R129-1及knowledge/research-notes/day21-135nd-same-input-falsification-design.md的多自旋反演稳定性与E2手征隧穿演化；128更新LV19-D21-R128-1与竞争模型域；126/127更新访问与误差合同。"
new_delta = "130更新knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md的MU07-D21-R130-1及knowledge/research-notes/day21-135nd-same-input-falsification-design.md的四极矩同态性与步调一致失活反证；129更新多自旋反演稳定性；128/127更新模型域与误差设计。"
assert old_delta in content, "Delta text not found"
content = content.replace(old_delta, new_delta)

# 6. Update writeback block
# In mukhopadhyay-2007 item:
old_mu_wb = '''    {
      "knowledge": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
      "anchor": "Day21 checkpoint043：135Nd课程主案例的逐claim原件审计",
      "summary": "124撤回后续重复同步中的过强认证；保留本页已有原件范围与原review/flags，未新认证全文。",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D21-R43-1"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D21-R43-4"
        }
      ]
    }'''

new_mu_wb = '''    {
      "knowledge": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
      "anchor": "Day21 checkpoint043：135Nd课程主案例的逐claim原件审计",
      "summary": "124撤回后续重复同步中的过强认证；130核准五自旋Qt比值0.9356±0.0102同态性与39/2态1.043倍步调一致集体失活反证审计，排他性反驳形状共存与偶然交叉；保留原review/flags。",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D21-R43-1"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D21-R43-4"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D21-R130-1"
        }
      ]
    }'''
assert old_mu_wb in content, "Old MU WB not found"
content = content.replace(old_mu_wb, new_mu_wb)

# In day21-135nd-same-input-falsification-design.md:
# Add MU07-D21-R130-1 to sources
old_design_sources = '''        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D21-R129-1"
        }
      ]
    }'''

new_design_sources = '''        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D21-R129-1"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D21-R130-1"
        }
      ]
    }'''
assert old_design_sources in content, "Old design sources not found"
content = content.replace(old_design_sources, new_design_sources)

# Update design summary:
old_design_sum = "129完成四个自旋态R_E2单调增长3.56倍与带内|δin|∈[0.034,0.061]超高稳定性核验；无新CI。"
new_design_sum = "129完成四个自旋态R_E2单调增长3.56倍与带内|δin|∈[0.034,0.061]超高稳定性核验；130核准五自旋Qt比值0.9356±0.0102同态性与39/2态1.043倍步调一致集体失活反证审计，排他性反驳形状共存与偶然交叉；无新CI。"
assert old_design_sum in content, "Old design summary not found"
content = content.replace(old_design_sum, new_design_sum)

# 7. Update Verification and continuation
old_ver = "129实际检查见本run required-checks-129.json；较早检查不覆盖此树。研究仍开放至原receipt今日15:00，未授分/提交/发布/开Day22。"
new_ver = "130实际检查见本run required-checks-130.json；较早检查不覆盖此树。研究仍开放至原receipt今日15:00，未授分/提交/发布/开Day22。"
assert old_ver in content, "Old ver not found"
content = content.replace(old_ver, new_ver)

report_path.write_text(content, encoding="utf-8")
print("Report successfully updated to Checkpoint 130")
