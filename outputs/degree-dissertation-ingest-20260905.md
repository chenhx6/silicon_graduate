---
type: output
title: "2026-09-05 学位论文批次摄入报告"
created: 2026-09-05
updated: 2026-09-05
status: ai-draft
review_status: unreviewed
tags: [degree-dissertation, ingest, evidence-audit, 2026-09-05]
---

# 2026-09-05 学位论文批次摄入报告

## Result status

内容摄入已完成：15 篇真正的学位论文（丁兵已有 source、Alwaleedi 复读、13 篇新增 source）以及 1 篇附加实验报告。所有新增 source 均完成 staged evidence reading，目标状态为 `deep-read`；`review_status` 仍为 `unreviewed`，重要 claims 仍保留 `needs_review: true`。

Git 采用内容与发布分轨：内容写入和 lint 已完成，批次发布由 `script/git20260905.py` 负责一次显式暂存、提交和非 force push。Docker 终端 Codex 已接手，旧的 PowerShell/profile/ACL 阻断不再适用；当前仍未新增 commit 或 push，等待用户审核和 dry-run。

## Sources handled

| 类别 | 文件/来源 | 处理结果 |
|---|---|---|
| 已有论文复读 | `Band structures of 131Ce.pdf` / Alwaleedi 2013 | 复核 Abstract、Fig.4.1、Tables 4.1–5.4、Fig.5.5；无新科学修改，更新 raw path 与复读记录。 |
| 已有论文 | `丁兵 - 博士论文.pdf` | source/nucleus/band/experiment 已在前置 WIP；本批次修正 `degree dissertation` raw path。 |
| 新 thesis | 强赟华 2019 | `130,131Ba`、`87Zr`；新 source。 |
| 新 thesis | 车兴来 2007 | `108,112Ru`、`134,135Ba`；新 source。 |
| 新 thesis | Smith 1998 | `127–131Pr` 多形状带；新 source。 |
| 新 thesis | Sensharma 2021 | `135Pr`/`187Au` wobbling/chiral-wobbler；新 source。 |
| 新 thesis | Régis 2011 | LaBr₃(Ce) fast timing/MSCD；新 source。 |
| 新 thesis | 王华磊 2006 | `170Re`/`176Ir`；新 source。 |
| 新 thesis | Wang Enhong 2015 | 裂变碎片多核素高自旋；新 source。 |
| 新 thesis | Hinke 2010 | GSI `100Sn`/`100In`；新 source。 |
| 新 thesis | Lubos 2016 | RIKEN `100Sn` 与邻近核素；新 source。 |
| 新 thesis | Morgan 2008 | `237Pu` 第二势阱/Nilsson 轨道；新 source。 |
| 新 thesis | Hayes 2005 | `178Hf` K 守恒破缺；视觉/OCR 核对关键页，新 source。 |
| 新 thesis | Pálffy 2006 | NEEC 理论；新 source-only。 |
| 新 thesis | 陈思泽 2014 | `6Li(p,γ)7Be`；新 source-only。 |
| 附加实验报告 | Dietrich 等 1974 `UUIP-882` | `103Pd` 实验报告，不计入 15 篇学位论文。 |

`100Sn.pdf` 与 `Spectroscopy of the doubly magic nucleus 100Sn and its decay.pdf` SHA-256 相同；不重复创建 source。旧 ProQuest preview 已由用户替换为 `Decay Spectroscopy of 100 Sn and Neighboring Nuclei.pdf`，该文件作为 Lubos 2016 使用。

## New or touched knowledge pages

- Sources：14 个新 source，加 Alwaleedi raw path/复读记录；丁兵 source path 已纠正。
- Nucleus/concept/observable：`100sn`、`gamow-teller-strength`、`lifetime`、`signature-inversion`。
- Existing relation touch：`131Ba`、`108Ru`、`112Ru`、`135Pr`、`187Au` 及相关实验页的 source/independence links。
- Index：新增本批次来源入口。

## Human review triage

### P0

- 强赟华 QY19-3/QY19-5/QY19-6：`130Ba` t-band、`131Ba` 一负两正 MχD、E1/八极关联的带号、组态和措辞。
- 车兴来 CX07-4/CX07-5/CX07-6/CX07-7：`Ru/Ba` 二声子 γ、二准中子、回弯和模型形变参数。
- Smith SM98-3/SM98-6/SM98-7：`130Pr` SD/ED、TRS 组态和 ED 形变随 N 变化趋势。
- Sensharma SE21-1/SE21-2/SE21-3/SE21-5/SE21-6/SE21-7：wobbling links、successive phonon spacing、`187Au` 横/纵向分类和 `135Pr` chiral-wobbler 候选。
- Wang Hua-Lei WHL06-3/WHL06-5/WHL06-6：`170Re` 组态/signature inversion 与 `176Ir` 新能级、长寿命 isomer。
- Hinke HK10-2/HK10-4/HK10-5/HK10-7：`100Sn` T1/2、endpoint、BGT、`100In` 五条 γ 线和 6+ isomer search。
- Lubos LB16-2/LB16-3/LB16-5/LB16-7：独立 RIKEN `100Sn` BGT/Q-value、50 keV link、`93Ag` proton emitter 和 `90Rh` isomer。
- Morgan TM08-2/TM08-3/TM08-5/TM08-6：`237Pu` 两个 fission-isomer、149 γ transitions、54.0(3) keV placement 和四个 Nilsson labels。
- Hayes HB05-1/HB05-2/HB05-3/HB05-4/HB05-7：两个 Coulomb-excitation 实验、K-mixing trend、hindrance 和 OCR/视觉 locator 边界。
- Dietrich DP74-1/DP74-2/DP74-3：`103Pd` level count、tentative assignments 与 784 keV `11/2−` `25±2 ns`。

### P1

- Régis RG11-2/RG11-3/RG11-4/RG11-5/RG11-6：CFD time-walk、MSCD/PRD、benchmark lifetimes、`176W` IBA 与 systematics。
- Wang Enhong WE15-1/WE15-4/WE15-5/WE15-7：21 核素范围、`147Ce/148Ce/158Sm` 候选解释和裂变数据独立性。
- Pálffy AP06-2/AP06-3/AP06-5/AP06-6：NEEC relativistic formalism、截面数量级、RR interference 和角分布适用条件。
- 陈思泽 CS14-2/CS14-3/CS14-4/CS14-6：相对归一化、195 keV resonance/`7Be` `3/2+` 候选及独立验证路线。
- All thesis sources：citation key 缺失处保持空值；论文级使用前必须回到 raw/source locator 和用户确认。

## Checks

- Raw PDF hashes：所有 14 个新增 source 的 `raw_file` 存在且 SHA-256 匹配。
- Batch wikilink audit：新 source/nucleus/concept/observable 页面无缺失内部链接。
- `python system/scripts/wiki_lint.py --fail-on error`：0 errors；现有 warnings/info 保持并已按 source/review policy 解释。
- QMD：`update` 索引 27 个新页面、13 个更新页面；`embed -c nuclear-knowledge` 完成，最终 384 files / 2615 vectors / 0 pending。
- Protected files：`raw/zotero/wiki-inbox.bib`、`.codex/config.toml`、`system/lint-config.json` 不纳入本批次 stage。
- Commit/push：迁移后应先运行 `python3 script/git20260905.py --dry-run`；确认范围后再由用户运行 `python3 script/git20260905.py` 或 `script\git20260905.cmd`。不使用 `git add .`，不 force-push。

## Next action

内容和检查已完成；本运行状态为 `content-complete / final-not-pushed`。由用户审核 manifest 后运行 Python 发布脚本；不删除或 reset 已完成知识页。
