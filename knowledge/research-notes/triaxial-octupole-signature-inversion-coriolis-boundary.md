---
type: research-note
title: "三轴八极势能面上的转动对齐与高自旋旋称反转：微观 Coriolis 竞争机制"
date: 2026-10-29
category: research-notes
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
aliases: [triaxial octupole signature inversion, Coriolis competition in octupole PRM]
tags: [triaxial, octupole, signature-inversion, high-spin, coriolis]
evidence_sources: [liu-1996-signature-inversion-a130, simons-2005-130cs-chiral-structures, ma-1990-131ba-competing-alignments, ding-2021-131ba-133ce-signature-splitting, guo-2020-pseudospin-chiral-quartet-131ba, nndc-2009-ra225-adopted-parity-doublet]
created_from: Day26 triaxial-octupole signature-inversion Coriolis mechanism investigation
promotion_target: triaxial-octupole-coriolis-model
---

# 三轴八极势能面上的转动对齐与高自旋旋称反转

## 结论摘要

本笔记的核心结论是：在奇核或奇奇核中，旋称反转点 Ic 不是单一的 γ 形变标尺。三轴转动惯量改变各体轴上的 Coriolis 矩阵元，粒子—转子波函数的 jk 对齐又会随自旋和组态交叉重排；八极自由度通过相反宇称轨道混合、局域 ±β3 双阱隧穿及其与质子—中子残余相互作用的干涉，进一步重整这些矩阵元。因此 Ic 可以漂移、消失或出现多次反转。

现有 Wiki 证据支持 A≈130 中的强旋称交错、三轴/γ-soft 模型竞争和高自旋质子—中子对齐，但没有把 130Cs、131Ba 或 133Ce 直接认证为同时具有静态 γ≠0 与静态 β3≠0 的核。131Ba 的 RAT-PRM 使用 β2=0.22、γ=27.1°、β3=0.05 是模型输入；225Ra 的评价谱学则直接显示低能相反宇称伙伴与 E1，但并不提供三轴形变测量。以下模型和扫描是机制示意与可复现边界测试，不能替代自洽 CDFT/GCM 或带寿命的实验拟合。

## 实验证据与证据分层

| 核素/来源 | 直接谱学事实 | 模型解释 | 本题可用边界 |
|---|---|---|---|
| 130Cs | Simons 等以 Euroball 建立/延伸两条同宇称带，报告交叉 M1/E2 连接、S(I) 和相对 B(M1)/B(E2)；未给绝对寿命和绝对强度。[[simons-2005-130cs-chiral-structures]] | core–quasiparticle 模型使用 γ=27.6°、β2=0.185，高自旋约 I≈16 的交叉归因于 νh11/2 对齐。 | 支持三轴 Coriolis/对齐竞争的实验控制；不能单独证明八极静态形变。Liu 1996 的 130Cs 带头自旋仍有 I0=9 或 11 的竞争方案，旋称标签会随 I0 奇数平移而对换。[[liu-1996-signature-inversion-a130]] |
| 131Ba | νh11/2 yrast 带低自旋旋称劈裂约 160 keV；实验和 alignment 提取显示约 0.43 MeV 附近的质子/中子对齐候选。[[ma-1990-131ba-competing-alignments]] | CSM/TRS 把低自旋劈裂与负 γ 或 γ-soft 形状联系，把质子对齐后的形状推向近长椭、把中子对齐后的候选带推向近扁椭。 | 对齐与三轴自由度的直接机制前例；形变和组态仍是模型结果。 |
| 131Ba、133Ce | νg7/2[404]7/2+ 带出现强 signature splitting；两核实验带头分别约 525.3 和 340.3 keV。[[ding-2021-131ba-133ce-signature-splitting]] | QTR/CSM 显示近邻 νs1/2 的 Coriolis 混合在较小 γ 下也能产生劈裂；衰减 Coriolis 后需更大 γ。PES 的 γ 是模型极小值。 | 证明“劈裂幅度 → γ”存在连续简并山谷；不能从能谱唯一反演三轴度，更没有直接 β3 证据。 |
| 131Ba 多带候选 | RAT-PRM 取 β2=0.22、γ=27.1°、β3=0.05，并用 E1 网络讨论八极关联。[[guo-2020-pseudospin-chiral-quartet-131ba]] | 三轴与八极自由度可以在同一有效计算中共存。 | β3 是 tentative 模型输入；没有寿命/绝对 B(E1) 或静态梨形测量，不可升级为已确证三轴八极核。 |
| 225Ra | ENSDF 评价给出 1/2+ 基态带与 3/2−、1/2−、7/2−、5/2− 低能伙伴；31.50-keV E1 的 B(E1)=0.00081(20) W.u.。[[nndc-2009-ra225-adopted-parity-doublet]] | 奇 A 八极双阱/宇称投影可产生交错伙伴；K=1/2 的 Coriolis 解耦项产生强烈 odd-even staggering。 | 是反射不对称和宇称伙伴的锚点，不是三轴形变的直接证据；不能把 225Ra 的 parity-doublet 直接命名为 signature inversion in a triaxial octupole nucleus。 |

### 旋称交错与反转量的定义

对于固定带的相邻自旋，常用旋称交错量可写成

S(I) = [E(I) − E(I−1)] / (2I) × (−1)^(I+1/2)

（整数自旋带使用相应的 (−1)^I 约定）。本任务指定的旋转基线残差为

ΔE_rot(I) = E(I) − E(I−1) − I/J_ref。

旋称反转是 favored 与 unfavored 分支顺序反常改变；在计算中用同一宇称扇区的

Δ_sig^(p)(I) = E(p,s=−)(I) − E(p,s=+)(I)

的符号变化定位 Ic。带头自旋如果错一个奇数单位，会同时改变 α 标签和 favored/unfavored 命名，这正是 Liu 1996 对 A≈130 系统学的主要警告。

## 三轴八极粒子—转子哈密顿量

### 固定自旋的粒子—转子形式

令总角动量为 I=R+j，在体轴 k=1,2,3 中使用

H_I = Σk (I_k − j_k)²/(2J_k(β2,γ)) + H_sp + V_oct(β3,γ)。

展开得到

H_I = Σk (I_k²+j_k²)/(2J_k) + H_sp + V_oct − Σk I_k j_k/J_k。

由于 I_k 与 j_k 作用在不同张量因子上，最后一项等于

H_C = −1/2 Σk (I_k j_k + j_k I_k)/J_k = −Σk I_k j_k/J_k。

若从 I=R+j 的平方项书写，交叉项为 +2R_kj_k/(2J_k)；把 R_k=I_k−j_k 代回、并把纯 j_k² 吸收进 H_sp 后，就得到上述常用的负号形式。这个约定差异不能被误写成不同物理机制。

在未耦合体轴基底中，非对角元为

⟨I mI; j mj | H_C | I mI'; j mj'⟩
 = −Σk ⟨I mI|I_k|I mI'⟩ ⟨j mj|j_k|j mj'⟩ / J_k。

因此 Ixjx 和 Iyjy 含 I±j∓，改变体轴投影并混合相邻 K 分量；Izjz 是对角的。三轴性通过 J1≠J2≠J3 改变各通道权重，而不是简单地给 S(I) 乘上一个 sinγ 因子。

### 八极自由度与宇称投影

为了在最小模型中同时保持实验室宇称和局域反射不对称，使用两个二能级空间：

- σz=±1：相反宇称的有效轨道对，例如 πh11/2↔πd5/2 或 νi13/2↔νf7/2 的降维表示；
- τz=±1：局域 +β3 与 −β3 八极井。

取

H_sp = εσz + Δ_well τx， V_oct = κ3β3 σxτz， P = σzτx。

因为 P(σxτz)P−1=σxτz，所以 [H,P]=0，实验室宇称仍是好量子数；局域态本身却含有反射不对称的 τz 分量。V_oct 的二阶效应改变相反宇称分量、对齐概率和有效 Coriolis 矩阵元；若双阱很深，Δ_well 小，得到近简并 parity doublet；若势面软，Δ_well 大，八极效应表现为动态混合而非静态梨形。

### 对齐与 Ic 漂移

定义固定 (p,s) 分支的粒子对齐

a_k^(p,s)(I) = ⟨Ψ_Ips|j_k|Ψ_Ips⟩。

当高 j 轨道在旋转频率附近发生对齐时，a_k 突然变化，导致

δE_C(I) ≈ −Σk ⟨I_k⟩ a_k/J_k

的分支差发生回折。八极混合使

a_k ≈ |c+|²a_k(+) + |c−|²a_k(−) + 2 Re[c+*c−a_k(+-)]，

其中 c−/c+ 随 β3、γ 和 I 改变。于是 Ic 的漂移不是“八极项单独把某一级拉低”，而是八极诱导的轨道混合改变了 Coriolis 对齐和 p-n 残余相互作用的相对相位。对某些参数，交叉项相消，反转会推迟或消失；对另一些参数，协同增强，反转提前或出现第二个零点。

## 可复现数值模型

代码位于 outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/triaxial-octupole-inversion/triaxial_octupole_signature_inversion.py，运行工件为同目录的 signature-inversion-scan.csv、signature-inversion-scan.json 和 README.md。

模型采用 j=11/2、β2=0.24、J0=32 ħ²/MeV，并扫描 (γ,β3)=(0,0)、(20°,0)、(20°,0.06)、(28°,0.12)、(34°,0.12)。其中最后一项有效 V_pn(I,γ,β3)U_signature 不是微观从头算，而是将低自旋质子—中子残余相互作用压缩到固定 I signature 扇区的最小 phenomenological term；它使反转机制可在有限空间内显式出现，必须与 Coriolis、β3 和 γ 效应分开解释。

一次运行得到：

| case | γ | β3 | 计算的反转点 |
|---|---:|---:|---:|
| axial reference | 0° | 0 | I=19/2 |
| triaxial | 20° | 0 | I=19/2 |
| triaxial + weak octupole | 20° | 0.06 | I=19/2 |
| triaxial + strong octupole | 28° | 0.12 | I=21/2 |
| more triaxial + strong octupole | 34° | 0.12 | I=21/2 |

结果只证明此哈密顿量中的竞争项可以造成 Ic 漂移；不证明相应核素的实验 Ic 等于这些数值。JSON 中的数值检查为：最大厄米误差 0；[H,P] 最大元 0；[H,U_signature] 最大元约 2.6×10−15；厄米化前后本征能最大差 8.9×10−15 MeV；随机态幺正时间演化的能量漂移为 0。

## 竞争解释与适用边界

1. **单纯三轴 Coriolis 解释**：131Ba/133Ce 的 QTR 结果表明近邻低 j 轨道的 Coriolis 混合可在较小 γ 下制造强 signature splitting；因此交错本身不能证明八极耦合。
2. **轴对称残余 p-n 解释**：Liu 1996 的 particle–triaxial-rotor/Semmes–Ragnarsson 比较可在修正带头自旋后重现 A≈130 反转趋势；模型参数与 spin anchor 依赖使其不能作为独立 γ 测量。
3. **静态八极双阱解释**：225Ra 的相反宇称伙伴与 E1 支持反射不对称自由度；但其评价谱学不提供三轴测量，不能直接移植到 A≈130。
4. **动态八极软性/组态混合**：E1 网络或近简并也可由软势面、声子耦合和多组态混合产生。必须用绝对 B(E1)、B(E2)、B(M1)、partner-resolved lifetimes、对齐和带交叉同时约束。

### 不能从当前证据声称的内容

- 不能把 130Cs、131Ba、133Ce 的 signature inversion 直接称为“已确证三轴八极形变”；
- 不能把模型输入 β3=0.05 当作 131Ba 的静态实验 β3；
- 不能用 225Ra 的 parity-doublet 直接证明三轴 Coriolis 旋称反转；
- 不能把 toy scan 的 Ic=19/2、21/2 写成实验值。

## 自审、反证与下一步

### 反证条件

- 若在同一组态空间内加入 β3 后，绝对 E1/E2/M1、对齐和 signature splitting 不能同时改善，八极—Coriolis 协同解释应降级为三轴/低 j 混合；
- 若修正带头自旋后旋称交错仍由轴对称残余 p-n 项完全重现，则 γ 与 β3 的反演不可识别；
- 若 225Ra 或候选 A≈130 核的 E1 只出现孤立分支而无随自旋稳定的异宇称网络，应优先考虑局部组态混合而非静态八极双阱。

### 下一步最有信息量的计算/实验

1. 在同一 cranked HFB/CDFT 或 GCM 空间同时改变 γ、β3，输出 ak(I)、Jk(1,2)、B(E1)、B(E2)、B(M1) 和带交叉位置；
2. 对 131Ba/133Ce 做同一组态的 γ-only、β3-only、γ+β3 三组反事实计算；
3. 对 130Cs 先独立锁定绝对带头自旋，再讨论 favored/unfavored 反转；
4. 对 225Ra 将 odd-A parity-doublet 的 K=1/2 解耦公式与可能的 γ-soft/三轴扩展并列拟合，避免把反射不对称和三轴性混成一个标签。

## 状态说明

本页按任务要求发布到 knowledge/research-notes/，但 review_status: unreviewed、reasoning_status: provisional 保留。实验事实、作者解释、模型结果和本任务推断已分开；研究笔记不能替代 knowledge/sources/ 的原件证据，也不能把可复现 toy model 当作核素定量预测。

## Research Trigger

本轮任务要求把 A≈130 旋称反转、三轴转动对齐和八极反射不对称放进同一粒子—转子推导，并用独立脚本检验 Hermiticity、对易性、能量稳定性和 Ic 漂移。

## Grounded Evidence

本页实验事实来自 Liu 1996、Simons 2005、Ma 1990、Ding 2021、Guo 2020 和 NNDC 225Ra 评价页；每条具体证据在上方“实验证据与证据分层”表中保留 source wikilink 与适用边界。研究笔记中的 toy 参数、扫描值和推断不属于这些来源的直接报告。

## Provisional Reasoning

三轴惯量差、Coriolis 非对角元、八极宇称轨道混合和固定自旋的有效 p-n 项共同决定 signature splitting；扫描结果只验证这一机制在有限维模型中可实现，不构成核素拟合。

## Assumptions

- 用 j=11/2 有效载体表示一对相反宇称高-j 轨道，约化矩阵元吸收到 κ3。
- 局域八极井由 τz=±1 表示，宇称投影取 P=σzτx。
- 惯量的 γ 依赖采用正定 irrotational-like 处方；其数值不是实验反演。
- 有效 V_pn(I,γ,β3)U_signature 仅用于显示竞争和反转窗口。

## Competing Explanations

低 j Coriolis 混合、带头自旋误指认、轴对称残余 p-n 相互作用、γ-soft 涨落和动态八极声子都能产生部分旋称交错。没有绝对跃迁强度、寿命和组态交叉证据时，不能排他地归因于三轴八极静态形变。

## Transfer Conditions

将 toy 结果转移到具体核素前，必须有同一组态空间的绝对自旋、逐带寿命、B(E1)/B(E2)/B(M1)、alignment 和带交叉计算；尤其要对 gamma-only、beta3-only 与 gamma+beta3 做同输入反事实比较。

## Failure Conditions

若加入 β3 后不能同时改善 signature splitting、对齐和绝对电磁强度，或所有反转都可由修正带头自旋后的轴对称 p-n 项重现，则本页的八极—Coriolis 协同解释应降级。

## Falsification or Reverse Tests

运行同目录 triaxial_octupole_signature_inversion.py，检查 signature-inversion-scan.json 的 verification.passed；再用同一组态空间将 κ3 设为零，比较 Ic、对齐和宇称劈裂的联合变化。

## Open Questions

- 131Ba/133Ce 是否存在可由绝对 E1 和寿命同时约束的 γ–β3 联合势能面？
- 130Cs 在锁定绝对带头自旋后，旋称反转是否仍需要三轴项？
- 225Ra 的 K=1/2 解耦与 γ-soft/三轴扩展能否由同一套 partner-resolved 矩阵元区分？

## Human Review

本页为 Codex self-audit，review_status 保持 unreviewed；status: ai-draft 仅表示按本轮任务完成写入，不表示用户或同行已审核。需要人工裁决的重点是有效 V_pn 项的参数化以及将 RAT-PRM 的 β3 输入与静态形变术语分开的措辞。

## Promotion or Rejection History

2026-10-29：创建并发布为 provisional research note；保留 130Cs、131Ba、133Ce、225Ra 的实验/模型证据边界，未晋升为正式 model 或 synthesis 页面。
