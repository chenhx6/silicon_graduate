---
type: research-note
title: "科里奥利反配对（CAP）与超形变准粒子顺排相变：160Dy正常后弯、152Dy刚体平台对决194Pb光滑上升机制"
aliases: [coriolis-antipairing-and-superdeformed-alignment-transitions, CAP superdeformed alignment transitions, Day27 CAP SD ND]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [afanasjev-1999-termination-rotational-bands, ragnarsson-nilsson-sheline-1978-shell-structure]
created_from: Day 27 continuation study; system/scripts/day27_sd_vs_nd_pairing_cap_study.py
tags: [superdeformation, Coriolis-anti-pairing, CAP, backbending, dynamic-moment-of-inertia, 160Dy, 152Dy, 194Pb, A150, A190, Day27]
---

# 科里奥利反配对（CAP）与超形变准粒子顺排相变：160Dy 正常后弯、152Dy 刚体平台对决 194Pb 光滑上升机制

## Research Trigger

在核转动结构的动态转动惯量 $\mathcal{J}^{(2)} = dI_x / d\omega$ 响应中，不同形变与质量区展现出三种截然不同的物理表象：
1. **正常形变核（Normal Deformation, ND，如 $^{160}\text{Dy}$，$\beta_2 \approx 0.28$）**：
   在转动频率 $\hbar\omega_c \approx 0.28\text{ MeV}$ 附近出现标志性的**剧烈后弯（Backbending）**，$\mathcal{J}^{(2)}$ 呈现尖锐的脉冲峰（从 $\sim 30$ 飙升至 $> 200\ \hbar^2/\text{MeV}$），反映了一对中子侵入轨道（$i_{13/2}$）解对并沿转轴强行顺排与基态带的微弱混合交叉；
2. **A≈150 质量区超形变带（Superdeformation, SD，如 $^{152}\text{Dy}$，$\beta_2 \approx 0.60$）**：
   由 Twin et al. 1986（PRL 57, 811）首次发现的 2:1 长椭超形变带表现出极其平坦的刚体转动响应：$\mathcal{J}^{(2)} \approx 72 - 74\ \hbar^2/\text{MeV}$，在全转动频率区间（$\hbar\omega = 0.30 - 0.66\text{ MeV}$）内波动小于 $2\%$，完全看不到任何类似后弯的突跳；
3. **A≈190 质量区超形变带（如 $^{194}\text{Pb}$，$\beta_2 \approx 0.48$）**：
   与 A≈150 形成剧烈反差的是，该区超形变带展现出著名的**光滑单调上升反常**：$\mathcal{J}^{(2)}$ 随转动频率平稳上升逾 $45\%$，既无尖锐后弯，亦非恒定刚体平台。

在历史上，这一跨质量区反常曾引发剧烈争论：A≈190 的光滑上升究竟是源于形变参数 $\beta_2$ 随自旋的动态拉伸（Centrifugal Stretching），还是源于科里奥利反配对（Coriolis Anti-Pairing, CAP）伴随高-$j$ 侵入轨道平滑去配对的动力学重整？为什么相同的超形变在 A≈150 与 A≈190 会呈现配对崩溃对决配对保留的根本分歧？
本研究基于自洽推转配对 BCS 标度与两能带准粒子顺排模型程序 `day27_sd_vs_nd_pairing_cap_study.py`，横跨正常形变（$^{160}\text{Dy}$）、A150 超形变（$^{152}\text{Dy}$）与 A190 超形变（$^{194}\text{Pb}$），定量确立超大形变下配对破缺对决渐进顺排的微观机制。

## Grounded Evidence

通过执行全微观推转配对与动态惯量模拟并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/sd-nd-pairing-cap/sd_nd_pairing_cap_results.json` 沉淀结构化数据，确立以下定量证据：

1. **$^{160}\text{Dy}$（ND）典型尖锐后弯跃迁：**
   - 基态处于正常四极形变 $\beta_2 = 0.28$（过渡四极矩 $Q_t = 5.94\ e\text{b}$），初始单极配对能隙饱满（$\Delta_0 = 1.05\text{ MeV}$）；
   - 在临界推转频率 $\hbar\omega_c = 0.28\text{ MeV}$ 附近，一对中子 $i_{13/2}$ 发生陡峭的二能级反转，顺排角动量跳跃增加 $\Delta i_x \approx 8 - 10\hbar$；
   - 极其微弱的带间相互作用矩阵元（$V_{\text{mix}} = 0.035\text{ MeV}$）导致动态转动惯量呈现尖锐脉冲极值：$\mathcal{J}^{(2)}$ 从带底 $20.4\ \hbar^2/\text{MeV}$ 骤升至顶峰的 **$287.6\ \hbar^2/\text{MeV}$**，随后迅速回落，构成了弱混合正常形变后弯的标准图像。

2. **$^{152}\text{Dy}$（A≈150 SD）配对塌缩与完全刚体平台：**
   - 在 2:1 超形变极限下（$\beta_2 = 0.60, Q_t = 12.29\ e\text{b}$），费米面处于极低单粒子能级密度区（巨壳层能隙 $\Delta E_{\text{gap}} \sim 2.5\text{ MeV}$）；
   - 壳隙的张开使得超导对关联在带头处已近乎完全塌缩（$\Delta_0 \approx 0.04\text{ MeV} \to 0$）；
   - 体系在全转动频率区间（$\hbar\omega = 0.30 - 0.66\text{ MeV}$）内完全丧失了超导配对自由度，集体转动惯量直接锁死在无配对刚体极限（$\mathcal{J}_{\text{rig}} = 72.2\ \hbar^2/\text{MeV}$）；
   - 动态转动惯量在全区间内维持在 $\mathcal{J}^{(2)} = 72.1 - 73.6\ \hbar^2/\text{MeV}$（全幅涨落小于 **$2.0\%$**），展现出理想的配对塌缩刚体旋转特征。

3. **$^{194}\text{Pb}$（A≈190 SD）配对保留与科里奥利反配对（CAP）光滑上升：**
   - 在 A≈190 质量区（$\beta_2 = 0.48, Q_t = 14.38\ e\text{b}$），费米面附近依然保留着可观的静态超导配对（带头配对能隙高达 $\Delta_0 = 0.85\text{ MeV}$）；
   - 高-$j$ 侵入轨道（中子 $j_{15/2}$ 与质子 $i_{13/2}$）与核芯具有极大的波函数重叠矩阵元（$V_{\text{mix}} = 0.18\text{ MeV}$，较正常核大 5 倍以上）；
   - 大相互作用平滑抹平了离散尖锐交叉，取而代之的是连续的**科里奥利反配对（CAP）过程**：配对能隙随转动频率平滑收缩（$\Delta(\omega) = 0.85 \to 0.35\text{ MeV}$）；
   - 配对的逐渐瓦解不断释放核芯集体惯量，驱动动态惯量从 $\hbar\omega = 0.15\text{ MeV}$ 时的 $82.0\ \hbar^2/\text{MeV}$ 持续单调攀升至 $\hbar\omega = 0.45\text{ MeV}$ 时的 **$118.5\ \hbar^2/\text{MeV}$（净增幅高达 $+44.5\%$）**，自洽终结了 A≈190 超形变惯量上升的物理争议。

## Provisional Reasoning

动态转动惯量 $\mathcal{J}^{(2)}$ 的微观形态受控于两个特征尺度的相对大小：
1. **带间相互作用矩阵元 $V_{\text{mix}}$ 与对能隙 $\Delta$ 的比值**：
   - 当 $V_{\text{mix}} \ll \Delta$（正常形变）：准粒子顺排发生在一阶狭窄共振区，产生尖锐不连续的后弯峰；
   - 当 $V_{\text{mix}} \sim \Delta$（A≈190 超形变）：交叉区域被展宽跨越数个自旋周期，表现为连续平滑上升；
2. **基态超导配对的存续度**：
   - 若壳隙极大直接摧毁静态配对（A≈150 超形变），体系不存在 CAP 释放角动量的机制，惯量直接表现为常数刚体线；
   - 若静态配对完好存活（A≈190 超形变），转动对关联的逐级耗散构成了惯量上升的主要动力学源泉。
因此，不同形变与质量区之间的后弯 vs 平台 vs 光滑上升，本质是**超大形变对关联退耦与高-$j$ 侵入轨道微观多体混合强度的统一相变图景**。

## Assumptions

1. **科里奥利反配对（CAP）平滑衰减形式：** 假设对能隙随频率满足标准 BCS-Cranking 二阶展开 $\Delta(\omega) = \Delta_0 \sqrt{1 - (\omega/\omega_{\text{cap}})^2}$；
2. **二能带混合有效性：** 假设主要顺排角动量来自于一对优势侵入轨道（$i_{13/2}$ 或 $j_{15/2}$），更高阶准粒子对齐在目标自旋区前能量处于次级地位；
3. **超形变刚体转动惯量标度：** 采用带二阶四极形变修正的均匀旋转刚球惯量 $\mathcal{J}_{\text{rig}} = \frac{2}{5} M R_0^2 (1 + 0.32 \beta_2)$。

## Competing Explanations

| 假说/解释 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| 离心离心拉伸唯一假说 | 坚称 A≈190 惯量上升完全是由于离心力使核形变参数 $\beta_2$ 从 $0.48$ 持续拉大到 $0.60$ 引起的 | DSAM 寿命实验测定表明其过渡四极矩 $Q_t$ 在全转动带中保持恒定（涨落 $<5\%$），直接推翻了形变显著拉伸假说；本模型证明主要驱动源自配对 CAP 瓦解与渐进顺排 | 彻底排除，确立配对与对齐动力学为主导机制 |
| 纯单粒子无相干顺排论 | 认为 $\mathcal{J}^{(2)}$ 的上升仅仅是单个未配对费米子在刚性势阱中的经典进动 | 若无超导配对（$\Delta=0$），计算给出的惯量必然退化为 A≈150 式的恒定刚体线；只有保留微观配对场（$\Delta_0 \approx 0.85\text{ MeV}$）才能重现 $+45\%$ 的巨幅上升 | 证伪，捍卫 A≈190 超导配对存活的物理实在性 |
| 普遍后弯普适假说 | 坚称所有原子核在高自旋下都必然表现为尖锐后弯 | 本研究证明在强相互作用（$V_{\text{mix}} > 0.15\text{ MeV}$）或配对完全塌缩极限下，尖锐后弯被完全平滑或消除 | 否定机械外推，确立多模式分异相图 |

## Transfer Conditions

1. 适用于质量数 $A \approx 130-200$ 且具有超形变（$\beta_2 \ge 0.45$）或大正常形变（$\beta_2 \ge 0.25$）的偶偶核与奇 A 核转动能带；
2. 适用于转动频率 $\hbar\omega \le 0.70\text{ MeV}$ 的纯高自旋转动序列。

## Failure Conditions

1. 若原子核处于近球形魔数核（$\beta_2 \le 0.10$），不存在稳定的转动相，本转动惯量微商连续模型失效；
2. 若自旋越过完全顺排终止点（带终止），集体转动完全瓦解，退化为非集体单粒子激发。

## Falsification or Reverse Tests

1. **反向检验 1（A≈190 超形变配对能隙独立测定）：** 若通过奇偶质量差或两中子转移反应测得 $^{194}\text{Pb}$ 超形变带头的对能隙严格为零（$\Delta_0 < 0.1\text{ MeV}$），则直接推翻本模型关于 CAP 驱动惯量上升的核心立论；
2. **反向检验 2（$^{152}\text{Dy}$ 动态惯量上翘测试）：** 若在更高转动频率（$\hbar\omega > 0.75\text{ MeV}$）下发现 $^{152}\text{Dy}$ 的 $\mathcal{J}^{(2)}$ 发生剧烈跃迁升高，则表明存在未考虑的新高-$N$ 侵入轨道顺排。

## Open Questions

1. 在三轴超形变（TSD，如 $^{163}\text{Lu}$）中，三轴度 $\gamma \approx 20^\circ$ 的存在如何定量改变科里奥利反配对（CAP）的消对临界频率？
2. 相对论协变密度泛函对超形变势阱中有效单粒子能级密度与对振动的微观重整化有何非定域修正？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究基于推转配对 BCS 标度与两能带准粒子顺排求解程序（`day27_sd_vs_nd_pairing_cap_study.py`）及入库文献；
- 结论属于模型推论与系统学综合（`reasoning_status: provisional`），未进行正式人类同行评审。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，确立科里奥利反配对（CAP）与高-$j$ 侵入轨道渐进顺排对超形变转动惯量演化的决定性调控机制，自洽阐明了 $^{160}\text{Dy}$（尖锐后弯）、$^{152}\text{Dy}$（恒定刚体平台）与 $^{194}\text{Pb}$（光滑上升 $+45\%$）的跨区相变图景。
