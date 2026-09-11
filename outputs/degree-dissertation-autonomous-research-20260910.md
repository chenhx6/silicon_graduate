---
type: output
title: "2026-09-10 学位论文批次自主研究报告"
created: 2026-09-10
updated: 2026-09-13
status: ai-draft
review_status: unreviewed
tags: [degree-dissertation, autonomous-research, l3, l4, 2026-09-10]
---

# 2026-09-10 学位论文批次自主研究报告

## 1. 执行结果

本批次按计划使用 10 小时研究预算，执行链为“发现问题 → 实际读取学位论文和相关 PDF → L3 证据研究 → 知识增量 → 批次报告”。raw 目录共有 55 个 PDF、54 个唯一 SHA-256，`丁兵.pdf` 与 `丁兵 - 博士论文.pdf` 是 1 个重复文件。当前有 46 个 raw 文件映射到 source 页；6 个文件保留 `source-only`，2 个文件保留 `skimmed`，重复文件不重复摄入。所有 55 个文件都完成了最低真实覆盖，不能把 source-only 或 skimmed 改写成完整深读。

本次继续实际读完并写回 degree source 页的 10 个文件为：刘晨 `78Br`、刘红娜 `12C`、刘艳鑫 PSM、吕冰峰 `136Nd/135Nd`、吴鸿毅 2021 DAQ、孙亚洲 `16C`、岳珂 Gamma Ball、肖骁 `74As`、Mavela `32S`、闫铎 CSR 探测器系统。它们均记录了题名页、摘要、目录、方法/实验、结果/讨论、结论及问题相关图表的覆盖范围；未覆盖内容和下一路线写在对应 source 页。本轮另完成四篇外部温故知新/争议 crosswalk source 的全文或重点核验：2019 PRC `135Nd` parity crosswalk、2024 Nature Physics `100Sn` shell-closure context、2021 Guo `135Pr` methodological comment 和 2026 Sensharma `135Pr` 后续高统计论文。

研究没有修改 raw PDF、OCR/image artifact、`PLAN.md`、system workflow 或受保护 BibTeX。source 页保持 `review_status: unreviewed`；已有学位论文 claims 保留原证据边界，新建的外部 crosswalk claims 经 Codex self-audit 标为 `needs_review: false`，没有任何页面被写成 `human-reviewed`。“未完成”只表示研究状态、来源缺口或时间停止，不转成用户待办。

问题统计采用稳定 `issue_id`，不按 claim 行数或重复论文计数：上一批入口为 10 组 P0、5 组 P1，初始去重后仍为 P0=10、P1=5；本轮 10 个实际读入 source 页新增 40 个 source-linked issue（P0=24、P1=16）。把初始问题组与本轮稳定 issue ID 合并后，当前工作登记表为最终唯一 P0=34、P1=21，共 55 个 issue。共享 thesis/journal 或同一装置谱系只保留一个研究单元，source-linked issue 不等于独立实验数。

## 2. L3/L4 研究统计

本报告按一个稳定 `issue_id` 计一个 L3 研究单元；初始 15 组和本轮 40 个 source-linked issue 均已启动证据加载或研究路由。

| 研究层级 | 启动 | 完成 | 部分完成 | 停止 | 停止/边界说明 |
|---|---:|---:|---:|---:|---|
| L3 文献/证据研究 | 55 | 31 | 21 | 3 | 3 个停止单元为数据/manifest边界；`135Nd` parity source conflict 已由后续原始期刊 crosswalk 完成，残余表格异常单独保留。 |
| L4 公开数据/可靠模拟 | 0 | 0 | 0 | 0 | 没有同时具备 manifest、参数、代码/计算记录和敏感性或负例检查的单元；用户真实数据关口未触发。 |

本轮新增 source-linked issue 的状态可复算为：P0 24 个，其中完成 18、部分完成 6、停止 0；P1 16 个，其中完成 12、部分完成 1、停止 3。2026 `135Pr` 外部材料继续审计既有 `SE21-1..8`，没有另造 issue ID 或虚增独立实验数。初始 10 组 P0 与 5 组 P1 作为跨来源问题入口均仍保留其原始 provenance；没有把同一 issue 的多个 locator 再次计数。

L3 动态停止或保留 source-level uncertainty 的主要原因是：继续阅读只会增加背景而不改变阶段判断；缺少原始谱、事件树、GOSIA/GEANT4 输入或后续独立来源；以及摘要与正文、早期设计与详细构型之间的数值冲突。`135Nd` D3/D4 parity 的外部原始 provenance 已补齐，但 2019 PRC Table I 的 D3 `334.4 keV` 行仍是局部表格异常。`135Pr` 新论文增加了 DB1/DB2 连接和旧数据 χ² branch 论证，但 Guo 2021/Lv 2022 的双解、小 `|δ|` 和独立 `P-R_ac` 反证仍未由统一 raw response/covariance pipeline 解决。Gamma Ball 的效率/质量冲突和 Yan `CSR-01` 实测/模拟效率比较均已完成 locator 级 L3 定位，但因缺少 GEANT4 输入、CAD 清单或作者勘误，不启动 L4；Yan `CSR-04` 仍因缺少原始谱和 manifest 停止。L4 没有被“模拟结果”名义替代，所有未复现的模型数字仍标为 source/model boundary。

## 3. 核心主张与阶段结论

### 初始问题组

- `QY19`：`130Ba/131Ba` t-band、MχD、E1/八极关联的带号和组态继续保持 P0 部分完成；共享 GALILEO 数据和作者解释不能升级为独立实验事实。
- `CX07`：`Ru/Ba` 二声子 γ、二准中子、回弯和形变参数保留模型与 OCR/locator 边界。
- `SM98`：`130Pr` SD/ED、TRS 组态和中子数形变趋势仍需寿命/绝对矩阵元约束。
- `SE21`：`135Pr/187Au` wobbling、连续声子间距和 chiral-wobbler 解释与后续反方来源并列，不由能量趋势单独裁决。
- `WHL06`：`170Re` signature inversion、`176Ir` 新能级和 isomer 结论保留带号、寿命与组态定位边界。
- `HK10`/`LB16`：两条 `100Sn`/`100In` 证据链按实验谱系分开，B(GT)、Q-value 和 50-keV link 仍需 convention/independence 核对。
- `TM08`：`237Pu` 第二势阱、149 条 γ 线、54.0(3) keV placement 和 Nilsson labels 保留原文 locator，不以 OCR 补全轨道符号。
- `HB05`：`178Hf` 两个 Coulomb-excitation 实验、K-mixing 和 hindrance 保留模型/产额拟合依赖。
- `DP74`：`103Pd` level count、tentative assignments、784-keV `11/2−` 和 `25±2 ns` 仍按来源层级记录。
- `RG11`/`WE15`/`AP06`/`CS14`/`SHARED-THESIS`：P1 路由继续处理 fast timing、裂变数据独立性、NEEC 适用条件、`6Li(p,γ)7Be` resonance 候选和共享 citation/raw lineage；均不写成逐项人工审核清单。

### 本轮实际读取来源

| source / issue | 核心主张与证据 locator | 阶段结论与适用边界 |
|---|---|---|
| [[liu-chen-2016-78br-chirality-reflection-symmetry-thesis]] / `DD-20260910-78BR-01..05` | `70Zn(12C,p3n)78Br`、AFRODITE/DIAMANT、44 条新跃迁/21 个新能级；两对 MχD 候选和 8 条 E1 links（PDF pp.34–91）。 | 论文与 2016 期刊同一实验；保留 candidate chirality 与 octupole-softness，不写成静态手征或稳定八极形变的直接测量。 |
| [[liu-hongna-2015-12c-np-correlations-thesis]] / `DD-20260910-12C-01..04` | `190 MeV/u 12C+9Be`、BigRIPS/SAMURAI/DALI2；四个截面、`σ_np/σ_pp=4.6(3)`、`T=0/T=1=5.9(4)`（PDF pp.47–110）。 | `T=0 np` 关联增强是模型定义下的 proxy；WBP/eikonal 低估与 NCSM+3N 绝对值缺口未能单独归因于三体力。 |
| [[liu-yanxin-2012-projected-shell-model-exotic-nuclei]] / `DD-20260910-PSM-01..04` | PSM/TPSM、Zr/Mo 能级和 γ 多声子预测；`110Mo` `2γ/1γ=2.81` 为理论预测，`108Zr` 异能态偏向高-K/三轴候选（PDF pp.21–92）。 | 全部为 model result/input；不能把参数化形变或未测 `110Mo` 带写成实验事实。 |
| [[lv-bingfeng-2019-chirality-136nd-135nd-thesis]] / `DD-20260910-136ND-01..04` | `136Nd` D1–D6、`135Nd` 新双重带、RDT 和 `Doppler/RDCO/Rac` 方法（PDF pp.53–151）。 | thesis 的 D4 parity 文字冲突已由 [[lv-2019-chirality-135nd-reexamined]] 的 2019 PRC 正文、IPDCO、E2/E1 连接和 Table I 外部支持为 D3/D4 正宇称；PRC 的 D3 `334.4 keV` 表格行异常和 RDT 事件级数据缺口仍保留。 |
| [[guo-2021-comment-transverse-wobbling-135pr]] / `SE21-1..8` continuation | Matta 2015 747/813/755/594 keV links 的 angular-distribution 双解与 polarization sign 非唯一性（PDF pp.1–2, Figs.1–2）。 | methodological counter-comment，依赖既有 Matta 报告，不是独立实验；需与 Lv 2022 `P-R_ac` 和 Sensharma 2026 Fig.12 的 branch treatment 一起比较。 |
| [[sensharma-2026-evolution-chirality-transverse-wobbling-135pr]] / `SE21-1..8` continuation | 80 MeV `123Sb(16O,4n)135Pr` Gammasphere 合并数据、新增 DB1/DB2 五条连接、642/573/477 keV 小 `|δ|`，以及 746/812/754 keV 旧数据 χ² response（PDF pp.2–6、12–15）。 | 增加支持方实验和模型信息，但当前 run 无 polarization、无绝对寿命/partner-resolved strengths；与 Guo 2021/Lv 2022 的 branch 冲突仍未统一裁决。 |
| [[wu-2021-general-purpose-digital-daq-waveform-analysis]] / `DD-20260910-DAQ-01..03` | Pixie-16/MZTIO、约 `109 MB/s`、3–11 k/s HPGe benchmark、约 80 ns pile-up 分解（PDF pp.2–8）。 | 是特定硬件、固件、整形和噪声条件下的方法结果；不外推为所有数字 DAQ 的通用上限。 |
| [[sun-yazhou-2019-16c-single-proton-knockout-thesis]] / `DD-20260910-16C-01..04` | 240 MeV/u `12C(16C,15B)X`，截面 `15.9(2.1) mb`；与 75/400 MeV/u 数据比较（PDF pp.21–100）。 | 阶段结论是“当前误差内未见明确 `R_s` 能量趋势”，不是证明不存在能量依赖；跨实验模型/协方差仍缺。 |
| [[yue-ke-2010-hirfl-csr-gamma-ball-csi-thesis]] / `DD-20260910-CSI-01..04` | 4608 CsI(Tl)+APD 单元、`6°–129.2°` 几何、模拟效率约 `82–83%`、5% 级分辨、662-keV 单元测试；质量/体积存在 `1025/1077 kg` 两组版本（printed pp.I–II、35、56、71、95、103）。 | 形成 Gamma Ball 设计和单元测试证据链；`82/83%` 和 `1025/1077 kg` 已完成 L3 locator 定位，但最终口径仍需后续工程/GEANT4 provenance。 |
| [[xiao-xiao-2019-high-spin-74as-thesis]] / `DD-20260910-74AS-01..04` | thesis：58/62 MeV `74Ge(α,1p3n)74As`，约 170 h、`6.17×10^9` γγ 事件、27 条新跃迁、9 个新能级，新带为 Band 2 和 Band 4（摘要；物理 PDF p.33/印刷 p.25；pp.45–47）。journal：`1.9×10^9` γγ 事件，三条 `ΔI=1` 带，四条新跨宇称跃迁（journal PDF pp.3–7）。 | Bands 1/2 是手征候选，thesis 与 journal 正宇称 Band 1/2 标签级对应已闭合；thesis Bands 3/4 按最终结论更适合 pseudospin partner candidate，journal 单一负宇称 Band 3 的 E1/octupole interpretation 不能倒灌为 thesis 某一负宇称带结论；没有寿命测量。 |
| [[mavela-2019-32s-quadrupole-moment-doppler-correction-thesis]] / `DD-20260910-32S-01..04` | 安全库仑激发 `120.3 MeV 32S+194Pt`、`S_min>6.5 fm`、S3+AFRODITE、GOSIA 重定向效应（PDF pp.24–54）。 | L3 已定位摘要 physical PDF p.3 / printed p.i 的 `Q_S=-0.10±0.7 eb` 与 GOSIA/result conclusion physical PDF pp.59–60、p.63 的 `⟨2_1+‖E2‖2_1+⟩=-0.131±0.090 eb`、`Q_S=-0.099±0.068 eb` 冲突；阶段采用详细正文/结论值，不静默修正摘要。 |
| [[yan-duo-2015-csr-coulomb-excitation-detector-system-thesis]] / `DD-20260910-CSR-01..04` | Gamma Ball `1173.2 keV` Add-back 效率实测 `38.9%`、GEANT4 `66.0%`；七层 CsI(Tl) telescope 的 E–Range PID 和约 5% 单层分辨（PDF pp.35–90）。 | `CSR-01` 的实测/模拟因子约 2 的差异已完成 L3 locator 重建，仍是重要失败边界；`CSR-02/03` 的 PID、分辨和 calibration 结论依赖晶体、层厚、阈值和束流条件，不能普适外推。 |

## 4. Wiki 知识增量

### 新知识

- 补入 10 个实际读取 source 页和 40 个稳定 source-linked issue：`78Br` thesis 的章节级 MχD/E1 locator、`12C` `np` 关联截面链、PSM/TPSM Zr/Mo 预测、`136Nd/135Nd` 方法与候选带、DAQ 2021 benchmark、`16C` knockout 数据点、Gamma Ball 几何和单元测试、`74As` thesis 级带判据、`32S` GOSIA 重定向分析以及 CSR 外靶 Gamma Ball/CsI telescope 性能。
- 这些来源扩展了 Wiki 的方法桥接：高统计 γ 谱学、数字 DAQ、GEANT4 探测器模拟、粒子射程 PID、safe Coulomb excitation 和中能单粒子敲出。

### 纠正知识

- `74As` Bands 3/4：论文最终明确指出其不满足手征判据，阶段措辞改为 pseudospin partner candidate；thesis 新建负宇称带为 Band 4，而 2022 journal 使用单一 Band 3 讨论三条 E1/octupole correlations，当前不能把 journal 结论倒灌为 thesis 某一负宇称带结论。
- `32S` `Q_S`：已用页面图像定位摘要 physical PDF p.3 / printed p.i 的 `-0.10±0.7 eb` 与 GOSIA 正文/结论 physical PDF pp.59–60、p.63 的 `-0.099±0.068 eb` 冲突；阶段采用正文/结论值，未提升审核状态，也未推断摘要原意。
- Gamma Ball 设计：第 3 章构型汇总和第 6 章同页后半给出约 `238738 cm³`、`1077 kg`，第 6 章同页前半和第 7 章总结给出约 `227305 cm³`、`1025 kg`；同时区分 detailed Fig.4.23 页的 `>82%`、摘要 `0.5–10 MeV >83%` 和第 4 章小结 `2–10 MeV >83%`。旧单值不再被当作无条件最终值。
- `16C`：把“误差内未见明显 `R_s` 能量依赖”保留为有限比较结论，不改写成不存在能量依赖。
- `135Nd` D3/D4：后续 2019 PRC 明确支持正宇称 pair，关闭 thesis “缺少外部原始来源”的停止原因；同时保留其 Table I `334.4 keV` `27/2−→25/2+` 局部异常和 MχD 的作者/模型解释边界。

### 总结知识

- 手征、wobbling、稳定八极形变、刚性三轴和形状共存都需要组合证据；近简并、`S(I)`、`B(M1)/B(E2)`、E1、ADO/DCO、偏振或模型几何单项只能启动 L3。
- Detector-method 数值必须绑定几何、能量、阈值、整形、触发、feeding 和响应模型；Gamma Ball 的 `38.9%`/`66.0%` 差异说明“模拟效率”不能替代实测验证。
- thesis、journal、review 和同一装置的技术论文属于 evidence lineage；来源数量不等于独立实验数量。`74As` 的 `6.17×10^9` 与 `1.9×10^9` γγ 事件数按来源报告口径并列，不在缺少共同 gate/selection 定义时判为矛盾。

### 边界/失败知识

- 本轮没有 L4：没有公开数据 manifest、可执行代码/输入、参数记录及敏感性/负例检查的完整组合。
- `78Br`/`74As` 手征候选没有独立寿命和绝对矩阵元闭合；`32S` 摘要/正文冲突虽已完成 L3 locator 定位，但 GOSIA 没有 raw yield/可复现输入，不能启动 L4；Yue/CSR Gamma Ball 没有原始效率谱、完整 GEANT4 几何或最终 CAD/工程清单；`12C`/`16C` 的截面和 `R_s` 仍受反应模型/末态/接受度影响。`135Nd` 目前只保留局部表格异常，不再作为来源不足停止项。
- OCR、扫描编码、带号和轨道符号仍需原页定位；这些边界被写入 source 页，未被转化为人工审核任务。

## 5. 未完成研究

未完成项按研究状态而不是“是否读过 PDF”统计：当前 21 个 issue 为 `partially-researched`，3 个 issue 因来源/数据停止；55 个学位论文 PDF 均已有真实阅读状态，另有 8 个本轮外部研究 PDF 和一个 `100Sn` figure CSV 记录在 acquisition manifests 中。

| 停止类别 | issue / 文件范围 | 已完成范围 | 下一自主研究路线 |
|---|---|---|---|
| 时间/信息增益停止 | 初始 `QY19/CX07/SM98/SE21/WHL06/HK10/LB16/TM08/HB05/DP74/RG11/WE15/AP06/CS14/SHARED-THESIS` 入口及其部分交叉 issue；`DD-20260910-74AS-03` 的负宇称逐线带号映射 | 已完成问题去重、核心 claim、来源谱系和优先级；`74As` 已闭合正宇称 Band 1/2 映射并隔离负宇称倒灌风险，未逐项闭合全部竞争解释。 | 按信息增益继续做 claim-level crosswalk，先处理能改变判断的寿命/绝对强度/独立性证据；`74As` 需取得完整能级表/逐线跃迁对应后再判定 thesis Bands 3/4 ↔ journal Band 3。 |
| 来源/数据不足 | `DD-20260910-16C-04`、`DD-20260910-32S-04`、`DD-20260910-CSR-04` | 已读正文、记录模型/分析路线和缺失的 raw/manifest；`135Nd` 已由外部 PRC source crosswalk 移出本类。 | 获得跨能量原始数据、GOSIA 输入或 GEANT4 几何后，再启动具 manifest 的 L4 敏感性/负例检查。 |
| 已解决的来源冲突（保留局部异常） | `DD-20260910-136ND-03` | 2019 PRC pp.2–3、6、8–9 的正文、IPDCO、D4↔D3 E2、D4→D1 E1 和 Table I 直接支持 D3/D4 正宇称；D3 `334.4 keV` 行仍逐字保留。 | 后续论文写作/问答若引用具体 `J^π` 或 IPDCO，回到 2019 PRC Table I 和原文；不把孤立表格行扩展为整条带的反向结论。 |
| 证据冲突已定位但需外部 provenance | `DD-20260910-CSI-02/04`、`DD-20260910-CSR-01` 与 `DD-20260910-32S-02` 已完成 L3 locator 定位但仍保留 source-level uncertainty | 已定位 Gamma Ball 的 `82/83%`、`1025/1077 kg` 和 Yan `CSR-01` 的 `38.9%/66.0%` 比较到摘要、正文曲线、小结、构型页、效率定义和总结；`32S` 摘要/正文 `Q_S` 差异已定位到 abstract physical PDF p.3 / printed p.i 与 GOSIA/result conclusion physical PDF pp.59–60、p.63。 | Gamma Ball 继续查找后续工程论文、GEANT4 macro 或 CAD 清单；Yan `CSR-01` 仍需原始效率谱、完整 solid-angle/acceptance 和 GEANT4 输入来解释差异；`32S` 继续查找作者版本、机构记录或勘误，均不在缺少 provenance 时启动 L4。 |
| 文件级低相关边界 | 6 个 `source-only`（周旭、孟令杰、王世陶、王凯龙、高丙水、黄忠魁）和 2 个 `skimmed`（李广顺、滑伟） | 已完成题名页/摘要/目录/末页或有限索引覆盖，并在台账中给出状态。 | 仅当出现与当前 P0/P1 直接相关的可检验 claim 时补正文；否则保持 source-only/skimmed，不把它们列为未读。 |

下一轮自主研究仍按 L3 信息增益停止；若 L3 不能提出可检验、可追溯的公开数据问题，则继续保持 L4=0。本轮完成 `135Nd` parity crosswalk 后，剩余 3 个停止项均是 raw/data/manifest 缺口，不因继续搜索背景文献而自动升级 L4。Goal completion audit 已通过；farmer 的重复 rollout、超大 metadata 和长尾事件修复解决了运行器恢复问题，但不改变上述科学停止分类。

## 6. 验证结果

- **PDF 台账**：55 个 PDF、54 个唯一 SHA-256、1 个重复；46 个 raw 文件映射到 source 页，6 个 source-only、2 个 skimmed。
- **Source/raw 回链**：逐一检查 46 个 degree-dissertation source 的 `raw_file` 与 SHA-256；4 个 external source 的本地 PDF path/SHA 也已通过核验，完整值写入各 source 页和 acquisition manifests。
- **Issue 统计**：固定初始 P0=10/P1=5；本轮新增稳定 source-linked issue 40（P0=24/P1=16）；最终工作登记表 P0=34/P1=21；不按 claim 行、论文数量或 shared lineage 重复计数。
- **L3/L4**：L3 启动 55、完成 31、部分完成 21、停止 3；`DD-20260910-136ND-03` 由 stopped 改为 completed，Yue `CSI-02/04` 与 Yan `CSR-01` 保持 locator 级完成但仍有 source-level uncertainty；Yan `CSR-04` 继续因数据/manifest 缺口停止。L4 启动/完成/部分/停止仍为 0，无 manifest/code/parameter/sensitivity artifact 可声称存在。
- **状态边界**：新增外部 source 页保持 `review_status: unreviewed`，其 LV19/KAR24/SH26/GU21 claims 由 Codex 完成 direct-source self-audit 并标为 `needs_review: false`；没有新增 `human-reviewed` 或未经证据支持的 `confidence: high`，也没有把研究状态写成用户待办。
- **检查命令**：本轮执行 `python3 system/scripts/wiki_lint.py --fail-on error`（`errors=0`、`warnings=144`、`info=869`；`pages=416`、`wikilinks=3723`、`hashes=143`；`claims=1410`、`claim_missing_locator=0`、`claim_missing_kind=0`、`source_missing_raw_file=0`）、`git diff --check`、外部 acquisition manifest JSON 校验、8 个新外部 PDF 与一个 `100Sn` figure CSV SHA/path 校验和受保护文件检查；结果写入最终回执。raw、OCR、`PLAN.md`、workflow 和 protected BibTeX 未修改。
- **研究产物**：本报告、`degree-dissertation-reading-queue-20260910.md`、`degree-dissertation-closure-20260910.md`、`degree-dissertation-full-wiki-reflect-20260910.md`、`degree-dissertation-self-audit-20260910.md`、14 个新增/回写 source 页、四个 external acquisition manifest、`135Nd`/`100Sn`/`135Pr`/`187Au` 汇总页、三个 project 更新和 `knowledge/index.md` 入口。

## 7. 2026-09-11 L3 continuation audit

本次继续处理交接中优先级最高的 `DD-20260910-136ND-03`（`135Nd` D3/D4 宇称与 MχD 解释）。回到 raw PDF 后，physical p.127（printed p.126）在同一段先写 D4 parity changed to positive，随后又写 `therefore adopt a negative parity for band D4`；physical p.130（printed p.129）又把 D3/D4 称为 positive-parity doublet bands。Table 6.1 physical p.136（printed p.135）的 D4 行全部列正宇称，而 D3 的 `334.4 keV` 行另写出 `27/2−→25/2+`，构成表格级异常。

这轮新增的是“冲突已由页面视觉核对定位”，不是最终宇称裁决。该 issue 继续为 `stopped`，停止原因由笼统的待重读收敛为 `source-text/table conflict`；不改变任何 `review_status`、`needs_review`、confidence 或 MχD 强度。`DD-20260910-136ND-02` 仍因 D1–D5 partner-resolved lifetime/absolute `B(E2)/B(M1)` 缺失而 `partially-researched`。当前 55 个 L3 单元的 `30/21/4` 汇总口径不因这次定位而改变。

下一路线是取得原始 `135Nd` 期刊、论文引用 [128] 或作者版本/勘误，再逐条复核 `R_DCO/R_ac`、连接跃迁和表格宇称；在取得这些外部 provenance 前不启动 L4，也不把孤立表格行改写成确定结论。

## 8. 2026-09-11 Independence and lifetime continuation audit

继续审计 `DD-20260910-QY-002` 的寿命与实验独立性。`87Zr` 部分由 `87Nb` β+ 衰变经 SHANS β–γ delayed coincidence 测量；201-keV γ 的卷积拟合在 Qiang thesis physical p.71 给出 `τ=1017(16) ps`，同页分析链给出 `B(E2)=11.3(7) W.u.` 和 `B(M1)=0.0033(2) W.u.`，其中 δ=`−0.35` 与 `αT=0.0370` 来自所引资料，故派生强度仍需按输入条件使用。

`130Ba` K-isomer 的同一 source 内数值也被显式保留：Ch.5.1 physical p.55（printed p.54）写 `T1/2=9.4 ms`，摘要/总结约写 `9.5 ms`。对 `131Ba`，Qiang thesis 的 65-MeV `122Sn(13C,xn)` GALILEO 链与 Guo 2020、Ding 2021 的 65-MeV `122Sn(13C,4n)` GALILEO 数据相符，支持 dependent shared-campaign 判定；相同反应、阵列和事件总量不足以推出三份文件的精确子集关系，也不增加独立实验数。

本轮把“`87Zr` 直接寿命 locator 已闭合”和“`131Ba` lineage 已闭合”与“`130Ba` 数值冲突、g-factor/B(E2) 误差传播、MχD 绝对强度仍需人工核对”分开记录。L3 总统计仍为 `30 completed / 21 partially-researched / 4 stopped`，L4 仍为 `0`；未修改任何 confidence 或 review status。

## 9. 2026-09-11 `135Pr/187Au` lineage continuation audit

对 `SE21-1..8` 做了支持方/反方实验独立性分层。`135Pr` 的 Sensharma 2019 与 thesis 都来自 `123Sb(16O,4n)`、80 MeV Gammasphere 链；Lv 2022 则是 `100Mo(40Ar,1p4n)`、152 MeV JUROGAM II 链，约 `5.1×10^10` fold≥3 events，并用联合 `P-R_ac` 给出 747/813/450 keV 的小 `|δ|` 约束。`187Au` 的 thesis 与 Sensharma 2020 共享两次 `19F+174Yb` Gammasphere 支持链；Guo 2022 的 HIRFL `18O` 数据为独立 counter/reinterpretation 链，supplementary 仍属于同一 Guo 实验。

本轮结论是 independence map 已补齐，但不是 wobbling 争议裁决：双方仍缺可统一比较的 partner-resolved lifetime/absolute `B(E2)/B(M1)`，且弱 link、band identity、polarization 与模型近似仍可能触发解释排序变化。`SE21` 相关问题继续保留原 review boundary；L3/L4 总统计不变。

## 10. 2026-09-11 manifest-gap audit

对四个来源/数据停止项 `DD-20260910-136ND-03`、`DD-20260910-16C-04`、`DD-20260910-32S-04` 和 `DD-20260910-CSR-04` 做了仓库内只读 manifest 检查。学位论文目录只提供对应 PDF；仓库内现有的 JSON manifest 属于其它 `135Pr`/`106Ag` 任务，未提供上述四项所需的 RDT event tree、跨能量 `R_s` 输入、GOSIA yield/input 或 Gamma Ball GEANT4 geometry/response。

因此本轮没有伪造或借用不相干 manifest，也没有把论文中报告的模拟曲线当作 L4 输入。四项继续分别保持 source-text conflict 或 missing data/provenance 停止状态；在原始数据、参数、代码/输入和必要的 sensitivity/negative-control 条件出现前，不启动 L4。该审计不改变 55 个 L3 单元的 `30/21/4` 统计。

## 11. 2026-09-12 `135Nd` external original-paper crosswalk

本轮按计划取得并核对 2019 年 PRC 原始论文 *Chirality of `135Nd` reexamined: Evidence for multiple chiral doublet bands*（arXiv `1907.12809`，DOI `10.1103/PhysRevC.100.024314`）。本地 PDF 为 10 页、285508 bytes，SHA-256 为 `97182e90125ce57ac2faa0feeef42b6bc12952b3287f82f277a04f8d32cf0303`；下载、元数据和关键页面视觉核验记录在 `outputs/literature-acquisition/20260912-135nd-crosswalk.json` 与新 source 页中。另核对 2003 PRL Band A/B、2007 PRL lifetime/transition-probability paper、2009 PRM 和 2020 CDFT theory PDF，五份文件按历史/模型 crosswalk 使用，不计为五个独立实验。

2019 PRC PDF p.2 明确给出 `830/1015/1161/1184 keV` 四条连接的 IPDCO `0.043(8)/0.089(28)/0.008(2)/0.018(5)`，并据 electric character 固定 D2、D3、D4 正宇称；同页以 D4↔D3 的 `589/649/780 keV` E2 和 D4→负宇称 D1 的 `1184 keV` E1 说明 D4 与 D3 同宇称。PDF pp.8–9 的 D4 表格行也全部为正宇称。该外部原始论文因此解决 thesis 中“D4 positive/negative”文字冲突：`DD-20260910-136ND-03` 从 `stopped` 改为 `completed`。

仍保留一个精确的残余异常：2019 PRC Table I PDF p.8 的 D3 `334.4 keV` 行写作 `27/2−→25/2+`，而同表其它 D3 行、正文和 Fig.1 的整体记录支持 D3 正宇称。当前将其写成 PRC table-level anomaly，不把它静默改成正宇称，也不把它扩大为整条 D3 负宇称结论。MχD 仍属于作者/模型解释，partner-resolved absolute strengths/lifetimes 仍不完整。

截至本轮，L3 更新为启动 55、完成 31、部分完成 21、停止 3；L4 仍为 0。状态变化只来自一个有直接外部原始证据的停止项，未改变用户审核状态；新 source 的 claim-level `needs_review: false` 是 Codex self-audit 结果，不是 `human-reviewed`。

本轮温故知新还核对了 Karthein 等 2024 的 *Nature Physics* 原始论文（arXiv `2310.15093`，DOI `10.1038/s41567-024-02612-y`；PDF 26 页、SHA-256 `4a833c6fbf425ae2f6b190661103ea61335ec1547728788bc9f21f25bf40bd17`）。其 ISOLDE/CRIS 激光谱学测量 `101–131In` 的 `Q_s`、磁矩和电荷半径，作者据此支持接近 `N=50` 的 `100Sn` 双幻数；它不测 `100Sn` β 衰变、`100In` branching 或 `B(GT)`，因此对 `100Sn` GSI/RIKEN `B(GT)` 差异为 **no material change**。Zenodo 图数据已下载并哈希，两个大型 archive 只核对 metadata；未启动 L4。

## 12. 2026-09-13 `135Pr` external controversy crosswalk

本轮将既有 `SE21-1..8` 继续单元接入两份外部原始材料。Sensharma 等 2026（PRC 113, 024313；arXiv `2403.10749v2`，PDF 17 页，SHA-256 `294f791a230a12005ef43a237afb25b9bf731f8f520a1a65d6b32d0386ef91b3`）使用 80 MeV `123Sb(16O,4n)` Gammasphere 数据，确认 DB1/DB2 并新增五条 DB2→DB1 `ΔI=1` links。642.2、572.9、476.9 keV 三条最低能新连接的 MCMC angular-distribution mixing ratios 分别为 `-0.10(6)`、`-0.15(3)`、`-0.11(2)`，作者将其判为主要 dipole；DB1/DB2 的最小能量差约为 17 keV。由于当前 run 没有 polarization measurement，DB1/DB2 parity 仍是 tentative；论文也没有提供 partner-resolved absolute lifetime 或 absolute transition strengths。

同一 2026 论文 Fig.12（PDF pp.14–15）对既有 746、812、754 keV Gammasphere angular distributions 进行 χ² branch comparison，作者报告大 `|δ|` 分支较优，并据此回应 Lv 2022。Guo comment（arXiv `2011.14364v3`，PDF 2 页，SHA-256 `cc9e43e07f23c3e85250c4acf55032d1085901e14d075591bcb141e5fddcdafc`）则指出在假定 `σ/I` 下旧角分布可同时容纳大/小 `|δ|`，正 polarization asymmetry 不能单独排除小 `|δ|`。这两者是对旧数据/报告的不同方法学处理，不是两次独立新实验。

阶段结论：`135Pr` 的证据图由“支持方 E2-rich/wobbling chain—Guo 方法学质疑—Lv 独立 JUROGAM 小 `|δ|` counter chain—Sensharma 2026 新数据与 χ² response”组成。新论文增强 DB1/DB2 的 chiral-partner candidate 结构证据，但没有消除 branch、parity、polarization response、`σ/I`、absolute-strength 和 common-covariance 缺口；wobbling、TiP/realignment、signature-partner 与 chiral interpretations 继续并列，未形成终局裁决。L3 仍按原 55 个 issue 统计为 `31 completed / 21 partially-researched / 3 stopped`，L4 仍为 `0`。

## 13. 2026-09-13 `187Au` targeted search closure

对 `187Au low-spin wobbling` 做了定向 OpenAlex/Crossref/arXiv 检索。唯一直接命中是 Guo 等 *Physics Letters B* 828, 137010 (2022)，其 arXiv `2011.14354v3` 与当前已摄入发表版 PDF 同一来源（现已补入 source metadata），没有新的 `187Au` 直接实验或核素专属后续计算。检索到的 2026 `185Au` transverse-to-longitudinal wobbling 论文属于不同核素，已在 acquisition manifest 中标为 out-of-scope，不创建 source。

阶段结论：`187Au` 的 Sensharma 2020 大 `|δ|`/LW 支持链与 Guo 2022 独立 `R_ac+P` 小 `|δ|`/single-particle counter chain 仍是主要证据，当前 ranking **no material change**。band (3) identity、早期 internal-conversion/β-decay 原始 crosswalk、absolute lifetime/strength 和 common-input benchmark 仍保持开放；没有启动 L4。
