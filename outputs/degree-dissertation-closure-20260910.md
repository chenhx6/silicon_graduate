---
type: output
title: "2026-09-10 学位论文批次证据闭合与停止记录"
created: 2026-09-10
updated: 2026-09-12
status: ai-draft
review_status: unreviewed
tags: [degree-dissertation, closure, 2026-09-10]
---

# 2026-09-10 学位论文批次证据闭合与停止记录

## Coverage ledger

| 状态 | 数量 | 定义 |
|---|---:|---|
| `deep-read` / carry-forward | 16 | 上一批已有 source，全文主线和关键 evidence chain 已记录，本轮只复核问题池、谱系和 locator。 |
| `deep-read` / new | 29 | 本批次新增学位论文 source 页，包含实际覆盖范围、关键图表、issue、locator、竞争解释和停止边界。 |
| `read` / new related PDF | 1 | 吴鸿毅等 2021 DAQ 方法短文，全文 8 页实际读取；按 `read` 记录而非伪装成 thesis deep-read。 |
| `source-only` | 6 | 完成题名页、摘要、目录/末页最低覆盖，当前主线复用有限，保留未来方法或相邻核科学用途。 |
| `skimmed` | 2 | 真实有限覆盖，尚未核对正文和关键图表。 |
| `duplicate` | 1 | `丁兵.pdf` 与 `丁兵 - 博士论文.pdf` SHA-256 相同。 |

总计 55 个学位论文/附加报告 PDF；degree source 页 raw 映射 46 个文件，另有 6 个 source-only、2 个 skimmed 和 1 个 duplicate。所有文件均有明确状态，没有实际读完但仍停留在 `queued` 的文件。本轮另取得 8 个外部研究 PDF（`135Nd` crosswalk 5 个、`100Sn` context 1 个、`135Pr` controversy 2 个），独立记录在 acquisition manifests 中，不计入 55 个学位论文文件；另有一个 `100Sn` figure CSV supporting artifact。

## Source closure

46 个 degree source 页的 `raw_file`、SHA-256、reading depth、Covered scope/Not covered、关键 claim locator、竞争解释、Knowledge Impact 和 P0/P1 triage 已回写。继续阶段新建/补齐的 10 个 degree source 页，以及本轮新建的 4 个外部 source 页（2019 PRC `135Nd`、2024 Nature Physics `100Sn`、2026 PRC `135Pr`、Guo comment），均保留各自证据层级：

- `78Br`、`12C`、PSM、`136Nd/135Nd`、DAQ 2021、`16C`、Gamma Ball、`74As`、`32S`、CSR detector/PID；外部 crosswalk/context sources 为 `135Nd` 2019 PRC、`100Sn` 2024 Nature Physics、`135Pr` 2026 PRC 与 Guo comment。

degree source 页仍是 `review_status: unreviewed`，其既有 claim 保留原有 `needs_review` 边界；新建 2019 PRC source 页也为 `unreviewed`，但其 LV19 claims 已由 Codex 完成直接来源 self-audit 并标为 `needs_review: false`。闭合表示证据状态已登记，不表示人工科学审核完成。

## Issue and research closure

- 初始问题池：10 组 P0、5 组 P1；初始去重后仍为 P0=10、P1=5。
- 本轮 source-linked issue：40 个稳定 `DD-20260910-*` ID，其中 P0=24、P1=16。
- 最终工作登记表：P0=34、P1=21，共 55 个稳定 issue；共享 thesis/journal/装置谱系不重复计为独立实验。
- L3：启动 55、完成 31、部分完成 21、停止 3。
- L4：启动、完成、部分完成和停止均为 0；没有满足 manifest、参数、代码/计算记录及敏感性/负例检查的单元。

## Stop reasons

停止或部分完成来自 10 小时窗口内的信息增益排序、raw 数据/计算 manifest 缺失、装置版本数值冲突，以及跨来源独立性尚未闭合。`135Nd` thesis parity conflict 已通过 2019 PRC 外部原始 crosswalk 完成，残余的 D3 `334.4 keV` 表格异常不再作为停止项。Yue Gamma Ball 的 `82/83%` 效率和 `1025/1077 kg` 质量/体积冲突本轮已完成 locator 级 L3 定位，但仍需 GEANT4 输入、CAD 清单或后续工程来源才能判断最终口径；Yan `CSR-01` 的实测/模拟效率差异也已完成 locator 级 L3 定位，而 `CSR-04` 仍因原始谱和 GEANT4 manifest 缺失停止；`16C` 跨能量 `R_s` 比较保留下一自主路线。`74As` 额外完成了 thesis–journal L3 crosswalk：正宇称 Band 1/2 标签级映射闭合，负宇称 thesis Bands 3/4 与 journal Band 3 未形成唯一逐线对应，`6.17×10^9` 与 `1.9×10^9` 事件统计按来源口径并列。`32S` 摘要/正文 `Q_S` 冲突已完成 locator 级 L3 定位：摘要 physical PDF p.3 / printed p.i 给 `-0.10±0.7 eb`，GOSIA/result conclusion physical PDF pp.59–60、p.63 给 `-0.099±0.068 eb`，阶段采用详细正文/结论值但不推断摘要原意。

## Runtime boundary

Goal `01a08869-6209-7ce3-a85a-8a996da25567` 的 completion audit 已通过；farmer PID 231566 已加载重复 rollout、超大 metadata 和长尾事件读取修复，完成时无 pending 续接。运行器恢复不改变本批次证据状态；本地 WIP 继续保留。

## Verification snapshot

- `python3 system/scripts/wiki_lint.py --fail-on error`：exit 0；`errors=0`、`warnings=144`、`info=869`，`pages=416`、`wikilinks=3723`、`hashes=143`。
- 46 个学位论文 raw-to-source 映射逐一通过 path/SHA-256 核对；新增外部 8 个 PDF 和 `100Sn` figure CSV 由 `outputs/literature-acquisition/20260912-135nd-crosswalk.json`、`20260912-100sn-refresh.json`、`20260913-135pr-refresh.json`、`20260913-187au-refresh.json` 记录 path/bytes/SHA/身份与核验状态；index 链接目标存在；`git diff --check` 通过。
- raw PDF、OCR/image artifact、`PLAN.md`、system workflow 和 `raw/zotero/wiki-inbox.bib` 未进入本轮 diff。

## 2026-09-11 continuation audit

对 `DD-20260910-136ND-03` 的 raw 页面复核确认：物理 PDF p.127（印刷 p.126）同段同时出现 D4 parity changed to positive 与 `therefore adopt a negative parity for band D4`；p.130（印刷 p.129）将 D3/D4 称为 positive-parity doublet；Table 6.1 p.136（印刷 p.135）D4 行均为正宇称，D3 的 `334.4 keV` 行另有 `27/2−→25/2+` 异常。该阶段记录关闭了 OCR 误读可能性，但当时仍等待外部 provenance；后续 2019 PRC crosswalk 已完成裁决。

## 2026-09-11 independence/lifetime continuation

`DD-20260910-QY-002` 的 continuation audit 进一步区分了同一论文中的两类实验：`87Nb` β+→`87Zr` 的 SHANS β–γ delayed-coincidence 结果在 physical p.71 给出 `τ=1017(16) ps`、`B(E2)=11.3(7) W.u.` 和 `B(M1)=0.0033(2) W.u.`；`130,131Ba` 则属于 65-MeV GALILEO 在束数据。Qiang thesis、Guo 2020 和 Ding 2021 的 `131Ba` 反应/阵列/事件量支持 shared dependent lineage，而非三个独立实验。`130Ba` K-isomer 的 `9.4/9.5 ms` source-internal difference 和派生强度输入仍保留 review boundary，未改变批次 L3 `30/21/4` 统计。

## 2026-09-11 wobbling lineage continuation

`SE21-1..8` 的 continuation audit 将 Sensharma thesis 与 Sensharma 2019/2020 归为支持方 dependent lineage，将 Lv 2022 `135Pr` 与 Guo 2022 `187Au` 分别归为独立 counter/reinterpretation 数据链；Guo supplementary 不另计实验。两边的 lifetime/absolute-strength 缺口、弱 link/polarization 和 band-identity 边界仍在，未改变 L3 `30/21/4` 或 L4=0。

## 2026-09-11 manifest-gap audit

仓库内只读检查显示，学位论文目录没有为 `136Nd` RDT、`16C` 跨能量 `R_s`、`32S` GOSIA 或 CSR Gamma Ball 性能提供对应 event tree、yield/input、GEANT4 geometry/response 或可执行参数 manifest；找到的其它 manifest 属于不同任务，不能借用。2019 PRC parity crosswalk 只关闭了来源冲突，不提供这些 L4 输入；当前仍有 3 个 source/data 停止项，L4 保持 0。

## 2026-09-12 external `135Nd` crosswalk closure

2019 PRC PDF pp.2–3、6、8–9 的正文、IPDCO 数值、D4↔D3 E2、D4→D1 E1 和 Table I 正宇称行，直接支持 D3/D4 为正宇称；D3 `334.4 keV` 的 `27/2−→25/2+` 仅作为该版本的局部表格异常保留。2003 PRL Band A/B、2007 PRL lifetime paper、2009 PRM 和 2020 CDFT 作为历史/模型 crosswalk，不重复计数。`DD-20260910-136ND-03` 从 `stopped` 更新为 `completed`；L3 变为 `31/21/3`，L4 仍为 0。

## 2026-09-12 `100Sn` warm-up closure

Karthein 等 2024 的 Nature Physics source 与 Zenodo metadata/结果图 CSV 完成 Codex self-audit。该工作提供 `101–131In` ground-state electromagnetic moments/charge-radii 的 `N=50` collectivity context，对现有 Hinke/Lubos `100Sn` B(GT) comparison 没有 material change；其两个大型 raw archive 不下载、不启动 L4。预印本 Ref.[99] 与 publisher/Zenodo 结果图 DOI 的 metadata discrepancy 已单独记录，不作为物理冲突。

## 2026-09-13 `135Pr` controversy continuation closure

Sensharma 2026 PRC（arXiv `2403.10749v2`）与 Guo 2021 comment（arXiv `2011.14364v3`）完成全文/重点页面核对并写入独立 source pages。前者在 shared Gammasphere lineage 中新增 DB1/DB2 五条连接、三条小 `|δ|` mixing ratios 和 17-keV crossing，并以 Fig.12 对旧数据 χ² 结果回应 Lv 2022；后者保留旧角分布双解和正 polarization sign 非唯一性的 counter-methodological 论证。两份材料均未提供可启动 L4 的 raw response/covariance/代码组合，且没有 partner-resolved absolute lifetime/strengths；因此既有 `SE21-1..8` 仍为开放争议单元，L3/L4 总统计不变。
