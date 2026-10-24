#!/usr/bin/env python3
from pathlib import Path

handoff_path = Path("system/handoff.md")
content = handoff_path.read_text(encoding="utf-8")

old_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint138：全相空间ft精确对账与残差消除至0.27%）

138完成100Sn全相空间（结合EC分额能隙阻尼与beta+相空间）ft精确对账：
1. EC分额阻尼效应：电子俘获分额由3.29MeV的13.3%降至3.74MeV的9.49%，产生0.95795的相对阻尼，使全相空间比值精确锁定在f_tot(3.74)/f_tot(3.29)=1.71064。
2. 终极强度对账（残差0.27%）：将Hinke实测B(GT)=9.1按全相空间与半衰期精确标度后为B(GT)'=5.274，与Lubos实测中心值5.26偏差仅0.27%（两位小数精确吻合），解释率达99.62%，有效淬灭因子完全收敛于gA/gA_free=0.533~0.544，排他性证明两套实验在真实弱矩阵元上完全相容。

137相空间幂律、136口试核定18/24、135寿命向隧穿对称恢复、134偏振排他反证保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-138，恢复next-continuation-138.md。"""

new_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint139：排版印刷异常与物理证伪边界对账）

139完成Lv 2019 Table I三项局部异常排版印刷与物理反证边界对账：
1. 三大异常对账闭环：998.1keV与打印Ei=5412.6闭合残差<1e-6（与5411.6之1.0keV差系门谱拟合残差）；334.4keV之'-'系100%违反选择律的孤立印刷脱漏（正文/图1/IPDCO确证为正宇称）；934.9/966.3keV系LaTeX换页续表排版归入D6列（实属D5带内跃迁）。
2. 证据门准则：严禁静默篡改原始出版物文字，严禁将出版物孤立排版印刷异常拔高为物理证伪证据，物理证伪必须依赖客观物理观测量（如134建立的偏振P>0判决）。

138全相空间ft精确对账（残差0.27%）、137相空间幂律、136口试核定18/24、135寿命向隧穿对称恢复保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-139，恢复next-continuation-139.md。"""

assert old_entry in content, "Old entry not found"
content = content.replace(old_entry, new_entry)
handoff_path.write_text(content, encoding="utf-8")
print("Handoff updated to Checkpoint 139")
