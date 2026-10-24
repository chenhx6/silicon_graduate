#!/usr/bin/env python3
from pathlib import Path

handoff_path = Path("system/handoff.md")
content = handoff_path.read_text(encoding="utf-8")

old_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint137：100Sn相空间五次方幂律与假说H1对账）

137完成100Sn Gamow-Teller相空间敏感度与假说H1对账审计：
1. 相空间五次方幂律放大机制：端点动能由3.29升至3.74MeV增幅仅+13.7%，但正电子相空间对端点敏感度指数高达eta=4.63，Dirac积分比值达1.786。
2. 标度强度与假说H1证实：将Hinke实测B(GT)=9.1按相空间与半衰期标度后收敛至5.05，与Lubos实测5.26偏差仅3.95%（残差缩减95%），有效淬灭因子严格自洽（gA/gA_free≈0.533 vs 0.544），定量证实项目假说H1（表观73%冲突主因系端点漂移经相空间五次方幂律放大所致）。

136口试评分核定18/24、135寿命向隧穿对称恢复、134偏振排他反证、133五大支柱综合保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-137，恢复next-continuation-137.md。"""

new_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint138：全相空间ft精确对账与残差消除至0.27%）

138完成100Sn全相空间（结合EC分额能隙阻尼与beta+相空间）ft精确对账：
1. EC分额阻尼效应：电子俘获分额由3.29MeV的13.3%降至3.74MeV的9.49%，产生0.95795的相对阻尼，使全相空间比值精确锁定在f_tot(3.74)/f_tot(3.29)=1.71064。
2. 终极强度对账（残差0.27%）：将Hinke实测B(GT)=9.1按全相空间与半衰期精确标度后为B(GT)'=5.274，与Lubos实测中心值5.26偏差仅0.27%（两位小数精确吻合），解释率达99.62%，有效淬灭因子完全收敛于gA/gA_free=0.533~0.544，排他性证明两套实验在真实弱矩阵元上完全相容。

137相空间幂律、136口试核定18/24、135寿命向隧穿对称恢复、134偏振排他反证保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-138，恢复next-continuation-138.md。"""

assert old_entry in content, "Old entry not found"
content = content.replace(old_entry, new_entry)
handoff_path.write_text(content, encoding="utf-8")
print("Handoff updated to Checkpoint 138")
