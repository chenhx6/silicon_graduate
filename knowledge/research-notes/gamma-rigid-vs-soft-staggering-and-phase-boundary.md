---
type: research-note
title: "γ带交错符号纠错：Wilets–Jean与Davydov极限、零点非相界反例与跨核迁移边界"
aliases: [gamma-rigid-vs-soft-staggering-and-phase-boundary, davydov filippov vs wilets jean, signature staggering s4, o6 dynamical symmetry]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [zamfir-casten-1991-gamma-softness-triaxiality, ayangeakaa-2019-rigid-triaxial-ge76]
created_from: Day 27 continuation study; system/scripts/day27_gamma_rigid_vs_soft_staggering_study.py
tags: [triaxiality, gamma-rigid, gamma-soft, staggering, source-correction, model-limit, Day27]
---

# γ带交错符号纠错与迁移边界

## Research Trigger

Day27旧版把交错符号和能级分组反转，并将未经逐条核验的八核能量输入直接分类为刚性、软性或相变临界点。随后增加的 provisional 附录没有修正该错误。本页以原件和独立模型计算替代旧结论；旧笔记、旧脚本和旧JSON已保存到本run的 `scientific-corrections-045/superseded-gamma-artifacts.json`，仅供撤回追溯。

本页不把旧输入算出的76Ge负S值直接解释成刚性，也不以此推翻Ayangeakaa2019的高阶矩解释。两个结论涉及不同观测和推断步骤。

## Grounded Evidence

本轮定向回读 [[zamfir-casten-1991-gamma-softness-triaxiality]] 本地6页PDF的PDF1–4（印刷265–268）文字，并视觉核PDF3/印刷267的Eq.(2)、能量示例和Eq.(4)。原件SHA-256为 `faa1b32dfa651fc613a9c4bac87c2c4b569d1bd725939580ea5ee3744d8c963a`，未修改raw。没有重新通读全部参考文献。

定义：

\[
S(4,3,2)=\frac{E(4_\gamma^+)-2E(3_\gamma^+)+E(2_\gamma^+)}{E(2_1^+)}.
\]

| 来源与定位 | 直接支持的内容 | 边界 |
| --- | --- | --- |
| ZC91-1；印刷265–266，Fig.1及正文 | γ-unstable的分组为单立2、成对(3,4)、(5,6)；γ=30° Davydov的成对分组为(2,3)、(4,5)、(6,7) | 是两个模型极限；成对表示相对聚集，不能都读成精确简并 |
| ZC91-2及ZC91-D27-R045-1；印刷267，Eq.(2)后示例 | 以E(2₁)归一，Wilets–Jean的(2γ,3γ,4γ)=(2.5,4.5,4.5)，S₄=−2；Davydov为(2,3,5.67)，S₄≈+1.67 | 5.67为原文舍入；本任务转子对角化独立恢复17/3与5/3 |
| ZC91-4及ZC91-D22-R091-1；印刷268，Fig.2后第一段 | S接近零不意味着势能刚度处于两个极限的中间；很弱γ依赖已可明显改变交错 | 不提供S=0普适相变点或固定±0.2判决阈值 |
| [[ayangeakaa-2019-rigid-triaxial-ge76]] AY19-D20-1/4/5/7 | 2019作者的76Ge低自旋刚性解释来自拟合矩阵元的高阶dispersion；103为E2/M1合计，完整协方差与高spin范围有边界；76Se刚性并未据该文确定 | 此处只回读source的既有原件审计，不声称本轮重建该实验或新读其PDF；不是S₄符号的独立定标 |

## Provisional Reasoning

### 两条独立路线重现模型极限

1. 精确算术重放：Wilets–Jean给出 `9/2 − 2×9/2 + 5/2 = −2`。Davydov给出 `17/3 − 2×3 + 2 = 5/3`。
2. 独立矩阵路线：在整自旋 `|I,K>` 空间构造三个角动量矩阵，再投影到偶偶核D₂对称基。K为偶数；K=0只对偶I保留，非零K基为 `(|K>+(−1)^I|−K>)/sqrt(2)`。取 `J_k ∝ sin²(γ−2πk/3)`，对角化 `H=Σ I_k²/J_k`，公共能标消去。
3. γ=30°时，I=2的本征值为12、24；I=3为36；I=4为32、68、80。按该模型基态带/γ带分支取 `E2g=24,E3g=36,E4g=68`，基态2₁为12，因此S₄=(68−72+24)/12=5/3。

脚本的5°–30°角度扫描只改变模型几何，没有拟合真实核素，也未给实验置信水平。轴对称端点的流体惯量为零，程序将其视为本实现的奇异端点，不能把数值奇异性写成核物理禁戒。

### 保持γ独立而穿过S₄=0的条件反例

Zamfir–Casten印刷267 Eq.(4)给出O(6)低表示的能谱 `E=Bτ(τ+3)+CJ(J+1)`；文中为比较Wilets–Jean而取C=0，并说明实际C通常小。本任务保留C作独立运动学参数，γ带的τ取2、3、3，得到：

\[
S_4=\frac{-8B+2C}{4B+6C}.
\]

| C/B（自设） | S₄（任务推导） |
| --- | --- |
| 0 | −2 |
| 1/4 | −15/11≈−1.363636 |
| 1 | −3/5 |
| 4 | 0 |
| 6 | 1/10 |

`J(J+1)`项改变旋转能谱；本模型仍未引入γ依赖势。因而在这个明确限定的O(5)+O(3)能谱族内，S₄可以穿零而不要求γ势发生相变。C/B=4或6是合成反例，不是对真实Ru/Pt/Ba参数的估计，不与原文“实际C通常小”混同。这一反例只反驳零点的无条件充分性，不抹去交错的谱学比较价值。

### 旧八核输入的处置

脚本保留76Ge/76Se/Ru/Ba/Pt旧能量输入以重放算术，所有行均为 `legacy-unverified-no-experimental-certification`；输出不再含刚性/软性分类，也不提供新的Coulex角度。未回读对应ENSDF评价条目、能级Jπ、γ带身份及误差之前，不能把这些行称为实测系统学，不能把Ru链零点称作首次发现的相变。

## Assumptions

- 转子使用流体惯量与偶偶核D₂对称空间；偶自旋取第二态、奇自旋取最低态的γ分支约定限定于本模型比较。
- O(6)能谱族只比较固定τ分支；C/B扫描是代数反例，不代表真实核素路径。
- S₄的分母是基态带2₁激发能，分子三项来自同一γ带，不能混用同自旋其它态。

## Competing Explanations

相同交错趋势可受带混合、不同惯量或动力学项、错误能级/带指认和γ势变化影响。高阶矩的实验解释与能量交错涉及不同证据；需保留2019刚性解释、其有限网络/协方差边界以及其它模型解释，而不是按一个S值替实验裁决。

## Transfer Conditions

可迁移的是明确S定义、分支身份和两个理想极限的比较坐标。更换核素、质量区、惯量、γ势、组态或自旋范围后应重新求谱及电磁矩阵元；负值不能无条件确证软性，正值不能无条件确证刚性，近零不能确证相变。

## Failure Conditions

原始能级来源、带身份或误差缺失时只做算术。显著组态交叉、非集体混合或不同交错定义出现时，不套用本页极限值；不得将奇A高自旋的旋称交错与这里偶偶低自旋γ带二阶差分混为一谈。

## Falsification or Reverse Tests

- 旧程序实际返回刚性−1.75和软性+0.65，与原PDF反号，修订前失败记录已保存。
- 修订程序以角动量矩阵对角化对照原件归一能量，以精确分数计算对照S值，两路线同时通过；未调整容差迎合旧结论。
- O(5)+O(3)合成反例在C/B=4穿零、6为正，排除“S=0普适临界点”的逻辑充分性。
- 八核旧表只作为未核输入重放，没有借算术通过给它们补来源或实验学分。

## Open Questions

1. 从评价谱或直接实验逐条恢复76Ge与Ru链的γ带能级和误差后，S₄及更高自旋交错如何变化？先校准输入再比较模型。
2. 在同一电荷算符、网络截断与协方差约定下，S序列与高阶四极不变量能联合约束哪些参数，哪些仍不可辨识？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

本页为Codex定向原件self-audit与条件模型验证，保持 `unreviewed/provisional`。原source的既有人审状态不升级本页；脚本通过只证明所声明模型和源级极限相容。

## Promotion or Rejection History

- 2026-10-30 Day27 checkpoint033/后续附录：旧“负S刚性、正S软性”和Ru链相变认证撤回，附录降级未修复符号错误。
- 2026-10-30 checkpoint045：原件印刷267/268核验、D₂转子独立对角化和Eq.(4)条件反例替代旧结论。脚本输出 `gamma_rigid_vs_soft_corrected_results.json`；旧工件只保留撤回历史，不作为科学事实源或新实验。
