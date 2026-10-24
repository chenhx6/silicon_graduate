#!/usr/bin/env python3
from pathlib import Path

handoff_path = Path("system/handoff.md")
content = handoff_path.read_text(encoding="utf-8")

old_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint139：排版印刷异常与物理证伪边界对账）

139完成Lv 2019 Table I三项局部异常排版印刷与物理反证边界对账：
1. 三大异常对账闭环：998.1keV与打印Ei=5412.6闭合残差<1e-6（与5411.6之1.0keV差系门谱拟合残差）；334.4keV之'-'系100%违反选择律的孤立印刷脱漏（正文/图1/IPDCO确证为正宇称）；934.9/966.3keV系LaTeX换页续表排版归入D6列（实属D5带内跃迁）。
2. 证据门准则：严禁静默篡改原始出版物文字，严禁将出版物孤立排版印刷异常拔高为物理证伪证据，物理证伪必须依赖客观物理观测量（如134建立的偏振P>0判决）。

138全相空间ft精确对账（残差0.27%）、137相空间幂律、136口试核定18/24、135寿命向隧穿对称恢复保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-139，恢复next-continuation-139.md。"""

new_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint140：课程交付物全要素对账与收束就绪）

140完成Day 21课程标准五大交付物全要素对账与收束就绪核定：
1. 交付物闭环核验：回忆（7层推断阶梯）、主线（135Nd与100Sn逐claim对账）、练习（可以说/不能说/下一步证据门）、反证（134偏振排他设计，16.3h达3σ）、交付（口试评分18/24与第三周REFLECT）全五项要素全部达成并经验证。
2. 治理与收束准备：全库保留needs_review: true，严禁设置human-reviewed；写回块104项结构严整有效；保持运行窗口至15:00硬截止，15:00准时转入收束缓冲小时执行终末计卡、回执与显式路径发布。

139排版异常对账、138全相空间ft对账（残差0.27%）、137相空间幂律、136口试核定18/24保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-140，恢复next-continuation-140.md。"""

assert old_entry in content, "Old entry not found"
content = content.replace(old_entry, new_entry)
handoff_path.write_text(content, encoding="utf-8")
print("Handoff updated to Checkpoint 140")
