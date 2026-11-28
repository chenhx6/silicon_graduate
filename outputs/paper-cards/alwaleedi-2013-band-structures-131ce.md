# Paper Card：Alwaleedi 2013《Band Structures of 131Ce》

> Source coverage: Full paper
> Extraction confidence: Mixed
> Locator mode: structure-grounded
> Primary analytical lens: discovery
> Secondary analytical lens: None
> Context verification: Targeted external check
> Card completeness: Complete relative to supplied source
> Preparation note: 标准 script 因环境缺少 PyMuPDF 未成功；使用章节、图、表和公式 locator，关键页已视觉复核。

## 01 基本信息

- 作者：Mohammed Abdullah Alwaleedi；University of Liverpool / Oliver Lodge Laboratory。
- 年份与类型：2013，博士学位论文，97 页。
- 领域：奇 A 核高自旋 γ 谱学、带结构、准粒子组态。
- Citation key：`mohammedabdullahalwaleedi_2013_Bandstructures`；DOI：`10.17638/00015073`；arXiv：未提供。
- 原始文件：`raw/papers/Band structures of 131Ce.pdf`；SHA-256 `B50C...8C1`。
- 阅读日期：2026-07-27；研究位置：`131Ce` 结构基线与 L3 集体模式判别入口。

## 02 一句话总结

论文用 165 MeV `100Mo(36S,5nγ)131Ce` 的 Gammasphere 符合谱扩展 Bands 1–7，并通过 angular ratios、alignments、crossings 与模型比较给出组态图，但没有足以独立裁决 wobbling、chirality 或形状共存的电磁与形变 observable。[Paper: Abstract; Figure 4.1; Table 5.3]

## 03 研究问题

- 具体问题：`131Ce` 各高自旋带的能级关系、spin/parity 和准粒子组态是什么？
- 重要性：它决定 A≈130 奇 A 核中单粒子与集体转动如何耦合。
- 既有不足：旧纲图和组态指认不完整，尤其缺少 Bands 4、7 及高自旋扩展。
- Can question：能否用 coincidence、angular intensity ratios、alignment/crossing 与 branching ratios 建立一致的 Bands 1–7 组态解释？

## 04 研究背景与发展路径

论文以早期 `129,131Ce` 带结构研究和 cranked-shell/Nilsson 解释为背景，位置是“扩展纲图并更新组态指认”。外部定向核验发现 Gizon et al. 1977（DOI `10.1016/0375-9474(77)90679-0`）和 Bharti et al. 2010（DOI `10.1007/s12043-010-0047-2`）与该历史链相关；本卡未完成系统 prior-art review。

## 05 论文识别的核心痛点

| 痛点 | 表现 | 原因或作者解释 | 论文证据 |
|---|---|---|---|
| 能级纲图不完整 | 多条带在高自旋处终止或连接不足 | 统计量与弱连接跃迁受限 | [Paper: Chapter 4; Figure 4.1] |
| 组态并非直接可见 | 相似谱学行为可对应不同轨道 | 需结合 alignment、crossing 和 Routhian | [Paper: Chapter 5; Tables 5.1–5.3] |
| 跃迁强度信息有限 | Figure 5.5 使用在目标能级以上设门的 branching intensities，但这些输入未列表 | 无寿命且采用 `δ=0`；Tables 4.1–4.7 是相对 508 keV 的全局强度 | [Paper: Tables 4.1–4.7; Equations 5.6–5.7; Figure 5.5] |

## 06 核心思想

1. 表层方法：建立扩展能级纲图并逐带比较 angular ratios、alignments 和 crossings。
2. 核心洞见：单一谱学量不能唯一决定组态，必须把连接关系、signature、转动响应和模型轨道联合约束。
3. `[Analysis]` 可迁移原则：集体模式命名必须晚于 band identity 和电磁性质验证，不能由能量相似性先行。

## 07 方法概览

- 输入：Gammasphere prompt γ–γ coincidences、角度分组强度、理论 Routhians。
- 输出：Bands 1–7 纲图、spin/parity、crossing frequencies、configuration map 和相对 `B(M1)/B(E2)`。
- 流程：束流/靶 → coincidence sorting → level scheme → angular ratio → alignment/crossing → configuration comparison → bounded interpretation。
- 关键假设：模型形变背景、轨道标签、`δ=0` 和半经典 g factors。

## 08 核心模块拆解

| 模块 | 功能 | 必要性 | 输入与输出 | 支持证据 | 移除影响 |
|---|---|---|---|---|---|
| coincidence 建谱 | 建立级联与 links | 确认 band identity | γ–γ events → Figure 4.1 | Chapter 4 | 无法可靠扩展纲图 |
| angular intensity ratio | 约束多极性 | 支撑 spin/parity | 角度分组谱 → ratios | Chapter 3; Tables 4.1–4.7 | 指认退化 |
| alignment/crossing | 识别准粒子对齐 | 区分候选组态 | energies → i_x, ω_c | Tables 5.1–5.3 | 组态约束显著减弱 |
| branching-ratio analysis | 比较电磁趋势 | 检验组态一致性 | intensities, Eγ → B(M1)/B(E2) | Eqs. 5.6–5.7; Fig. 5.5 | 失去一项相对电磁检查 |

## 09 必要公式与符号

- Equations 5.6–5.7：由带内 ΔI=1 与 crossover ΔI=2 分支强度及 γ 能量构造 `B(M1)/B(E2)`；`δ` 为 ΔI=1 跃迁的 E2/M1 mixing ratio，本论文取 `δ=0`。固定其它输入时 `R(δ)=R(0)/(1+δ²)`；`|δ|≤0.5` 时 δ=0 相对真实值最多高估 25%，相对 `R(0)` 的差值最多 20%。用途是比较组态模型的相对趋势，不能恢复绝对矩阵元。[Paper: Equations 5.6–5.7]
- rotational frequency 与 alignment 的定义用于定位 band crossing；具体实现见 Chapter 5 的 alignment plots 和 Table 5.1。

## 10 实验设计与证据链

- Population/instrument：165 MeV `36S` + 两张约 600 µg/cm² enriched `100Mo` 靶；101-detector Gammasphere。
- Evaluation：coincidence placement、angular ratios、crossing/alignment 一致性与半经典 ratio comparison。

| 实验 | 检验 claim | 条件 | 结果 | 支持结论 | 不支持的更强结论 | 来源 |
|---|---|---|---|---|---|---|
| level-scheme analysis | 新带与扩展是否存在 | 多重 coincidences | 新 Bands 4、7；扩展 1、2、6 | Bands 1–7 结构基线 | 集体模式唯一性 | Fig. 4.1; Tables 4.1–4.7 |
| crossing analysis | 组态是否与对齐轨道一致 | experimental i_x vs model | Table 5.1 频率与 Table 5.3 map | 候选组态排序 | 直接形变测量 | Tables 5.1–5.3 |
| ratio comparison | 指认是否符合电磁趋势 | `δ=0`, semiclassical inputs；gated branching inputs 未列表 | 作者报告总体趋势相符；L4 无法从表中全局强度独立复现 | 论文内部的组态一致性支持 | 可独立复算的 absolute B values 或 wobbling/chirality 证明 | Eqs. 5.6–5.7; Fig. 5.5 |

## 11 结论的正确解释

- 任务边界：这是特定 fusion-evaporation 布居窗口中的高自旋谱学，不是 `131Ce` 全能区结构测量。
- 模型依赖：轨道与形变指认依赖 Woods–Saxon/TRS 和半经典输入。
- 不确定性：弱 links、多极性、Table 5.1 的 Band 2 宇称不一致、未列表的 gated branching inputs 和 `δ=0` 都限制结论强度。
- `[User]` Figure 4.1-based working parity 为 Bands 2/3/5 正宇称、1/4/6/7 负宇称；Figure 4.1、Tables 4.1–4.7 与 Chapter 5 整体支持该 provisional map。Table 5.1 的 Band 2 负宇称保留为 probable typo/source conflict。
- 有界重述：论文可靠扩展了 `131Ce` 纲图并给出自洽的 configuration-coupling 解释，但没有独立验证 γ 势刚性或新型集体模式。

## 12 作者明确承认的局限

论文没有以统一 “Limitations” 段列出局限。作者讨论中承认组态解释依赖模型比较、部分带行为可能需要 spin-dependent core polarization/non-axial deformation，并以假定参数计算跃迁比（Chapter 5）。这些是作者陈述的约束，不应扩写成其未明说的正式限制清单。

## 13 批判性分析

| `[Analysis]` 观察 | 潜在问题或替代解释 | 为什么重要 | 如何检验 | 依据 |
|---|---|---|---|---|
| Table 5.1 Band 2 宇称与正文不一致 | 表格 typo 或 band mapping error | 会污染 crossing 的 parity 分类 | 回看原表、正文与早期 source | Table 5.1 vs Chapter 4 |
| `δ=0` 固定 | mixed M1/E2 会移动 ratio | 影响 configuration comparison | angular correlation + polarization 测 δ | Eqs. 5.6–5.7 |
| Figure 5.5 输入不可复算 | 35 对全局强度 proxy 中有 10 对在 `\|δ\|≤0.5` 后仍超出图示包络；最大值 23.30/34.79 | ratio agreement 不能作为独立可复现证据 | 发布 gated spectra/intensities 或以原始矩阵重提分支 | Tables 4.1–4.7 vs Section 5.3/Figure 5.5; [L4 report](../l4/131ce-thesis-baseline/report.md) |
| 形变由单一模型背景给出 | γ-soft core 或组态混合也可产生相似谱 | 决定 collective-mode 命名 | lifetime/Q_t、E2 branching、系统模型比较 | Chapter 5 |
| 近邻系统学可能被过度迁移 | `133Ce` chirality 不自动适用于 `131Ce` | 防止按核区标签倒灌结论 | 逐带 identity 与 observable matrix | external Wiki sources |

## 14 学到的知识

### Agent-derived knowledge candidates

- 高自旋 band assignment 的证据链应按 coincidence → multipolarity → alignment/crossing → electromagnetic ratios 分层。
- 相对 `B(M1)/B(E2)` 必须记录 mixing-ratio 假设；没有寿命时不能替代 absolute transition probabilities。
- TRS 的 `(β2,β4,γ)` 点是模型结果，不等于实验测得的 γ 刚性。

## 15 与现有知识的联系

- `133Ce` MχD 来源提供三轴/chirality 候选，但其 lifetime gap 和模型依赖不能反向证明 `131Ce`。
- Ding 2021 的 `131Ba/133Ce` signature-splitting 分析支持“非轴形变 + 低-j Coriolis mixing”可产生伙伴带现象。
- `131Xe` wobbling 争论及 IBFM 反解释提示：能谱相似性需要带间 E2、mixing ratio 和 polarization 才能区分 collective wobbling 与 signature/core coupling。
- 以上连接是跨来源 L3 候选，不是 Alwaleedi 论文自身结论。

## 16 研究构想

### Agent-derived research candidates

1. **最小 observable 判别集**
   - 起点：本论文缺少 lifetime、absolute B(E2)、polarization 与 measured δ。
   - 假设：把带间/带内 E2 strength、δ 和 polarization 联合起来，可显著改变 wobbling、chirality 与 signature-partner 的排序。
   - Initial method：先建立各解释的可证伪预测矩阵，再用公开数值或用户数据逐项填充；gated branching inputs 与 lifetime 数据分开建 manifest。
   - Validation：检查新增 observable 是否改变模型排序并能排除至少一个候选。
   - Possible failure modes：band identity 无法跨来源对齐，或公开数据不含误差与 mixing ratio。
   - Innovation status: `unverified`。
2. **γ-soft core-coupling 统一解释测试**
   - 起点：轴对称 TRS 背景与高自旋非轴 core polarization 并存。
   - 假设：γ-soft particle-core coupling 能同时描述 signature splitting、crossing 后 alignment 和部分伙伴带，而无需预设 wobbling/chirality。
   - Initial method：对 `131Ce/133Ce` 及必要邻核比较能量、staggering 与 E2/M1 observables。
   - Validation：预注册参数范围并检验是否同时再现多个独立 observable。
   - Possible failure modes：模型参数自由度导致不可辨识，或不同核的 band mapping 不同源。
   - Innovation status: `partially checked`。
3. **Band-identity 审计**
   - 起点：来源编号和 Table 5.1/5.3 内部不一致。
   - 假设：以 bandhead、signature、links 和配置联合映射可消除跨论文编号歧义。
   - Initial method：建立逐跃迁 crosswalk。
   - Validation：由能量、spin/parity、signature 和 links 独立复核映射。
   - Possible failure modes：公开表格缺少必要 links。
   - Innovation status: `unverified`。
