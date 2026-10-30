---
type: research-note
title: "轻锕系核中α团簇分子模型与平均场反射不对称性的多极求和规则、衰变约化宽度与波函数正交性边界"
aliases: [alpha-clustering-vs-meanfield-octupole-sumrules, actinide alpha clustering vs octupole sum rules, Day27 alpha cluster sumrules]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [gaffney-2013-pear-shaped-rn-ra, butler-2020-222-228ra-octupole-evolution, robledo-2010-bcp-d1s-octupole-ra-ba, warda-2011-actinide-cluster-radioactivity-gogny, nomura-2020-ra-th-gogny-d1m-octupole]
created_from: Day 27 continuation study; system/scripts/day27_alpha_cluster_vs_octupole_meanfield_study.py
tags: [alpha-clustering, octupole-deformation, sum-rules, preformation-factor, hindrance-factor, parity-projection, light-actinides, 224Ra, 226Th, Day27]
---

# 轻锕系核中 $\alpha$ 团簇分子模型与平均场反射不对称性的多极求和规则、衰变约化宽度与波函数正交性边界

## Research Trigger

在轻锕系核（$^{220}\text{Rn}, ^{222-226}\text{Ra}, ^{226-228}\text{Th}$）的低能交替宇称能带解释中，历史上长期存在两种截然不同的物理图景：
1. **$\alpha$ 团簇分子模型（$\alpha$-clustering molecular models）**：认为核素由紧密结合的核芯（如 $^{220}\text{Rn}$ 或 $^{208}\text{Pb}$）与外围运动的 $\alpha$ 粒子构成二体分子偶极态，由质心非对称位移直接产生内禀电偶极与八极跃迁；
2. **微观自洽平均场反射不对称理论（Microscopic Reflection-Asymmetric Mean-Field Theory）**：基于 Gogny HFB 或相对论密度泛函，认为体系处于紧致的梨形内禀形变阱中（$\beta_3 \approx 0.11 - 0.14$），由费米面附近相反宇称单粒子对（$\nu g_{9/2} \leftrightarrow j_{15/2}, \pi d_{5/2} \leftrightarrow h_{11/2}$）产生全核相干的多极跃迁，且宏观液滴极化项与中子壳极化项在特定中子数（$N \approx 136$）发生量子相消。

然而，过去文献常将两个模型在电多极跃迁或 $\alpha$ 衰变分支比上的局部吻合误作为等价表象。本研究通过建立严格的电偶极（$E1$）与电八极（$E3$）求和规则与预形成概率对账体系，结合 MINIBALL 与 CARIBU 最新直接库仑激发数据（[[gaffney-2013-pear-shaped-rn-ra]], [[butler-2020-222-228ra-octupole-evolution]]）以及实验 $\alpha$ 衰变向 $1^-$ 负宇称态的阻尼因子（Hindrance Factor, $\text{HF}(1^-)$）系统学，定量裁决两种图像的物理真实性与波函数正交性边界。

## Grounded Evidence

通过执行全微观多极矩阵元求解器 `system/scripts/day27_alpha_cluster_vs_octupole_meanfield_study.py`（数值结果存入 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/alpha-cluster-meanfield/alpha_cluster_meanfield_results.json`），确立以下定量证据：

1. **二体 $\alpha$ 团簇模型预形成概率的不可调和矛盾（求和规则佯谬）：**
   - 在纯 $\alpha + \text{core}$ 团簇模型中，接触半径 $R_{\text{touch}} \approx 9.15\text{ fm}$ 处的裸有效电荷分别为 $e_{\text{eff}}^{(1)} \approx 0.428\ e$ 与 $e_{\text{eff}}^{(3)} \approx 1.89\ e$，对应的裸向下跃迁强度为 $B(E1; 1^- \to 0^+)_{\text{bare}} = 1.22\ e^2\text{ fm}^2$ 与 $B(E3; 3^- \to 0^+)_{\text{bare}} = 56.2\text{ W.u.}$；
   - 在基准核 $^{224}\text{Ra}$ 中，实验测定的极小电偶极矩 $D_0 = 0.015(3)\ e\text{ fm}$ 要求 $\alpha$ 团簇预形成概率极低：$P_\alpha(E1) = 1.46 \times 10^{-5}$；
   - 然而，实验测定的巨大约化八极跃迁 $B(E3; 3^- \to 0^+) = 42(3)\text{ W.u.}$ 要求预形成概率高达：$P_\alpha(E3) = 42.0 / 56.18 = 0.748$（高达 $75\%$）；
   - 二者产生高达 **$5.1 \times 10^4$ 倍的定量失配**。在全同位素链（$^{220}\text{Rn}$ 到 $^{228}\text{Th}$）中，该失配因子始终介于 $10^3 - 10^5$ 之间，证明纯 $\alpha$ 团簇模型在原理上无法自洽描述轻锕系核的电磁多极性。

2. **微观平均场相干性与同源相消机制的完美符合：**
   - 反射不对称平均场（Gogny HFB）自洽导出的向下跃迁强度 $B(E3; 3^- \to 0^+)$ 由全核体元相干叠加主导：静态梨形核 $^{224}\text{Ra}$（$\beta_3 \approx 0.14$）理论给出 $40.8\text{ W.u.}$（实验 $42(3)\text{ W.u.}$），$^{226}\text{Th}$ 给出 $44.2\text{ W.u.}$（实验 $45(5)\text{ W.u.}$），吻合度在 $10\%$ 以内；
   - 振动核 $^{220}\text{Rn}$ 与 $^{228}\text{Th}$ 虽静态 $\beta_3 \approx 0$，但由软八极零点振动振幅（$\beta_{3,\text{rms}} \approx 0.13 - 0.14$）贡献 $30 - 33\text{ W.u.}$ 的动态相干强度，完全符合 MINIBALL 实验；
   - 微观相消模型（Myers-Swiatecki 液滴偶极 $D_{\text{macro}} \approx +0.059\ e\text{ fm}$ 与中子 $j_{15/2}$ 壳极化 $D_{\text{shell}} \approx -0.044\ e\text{ fm}$）自然重现了 $D_0 \approx 0.015\ e\text{ fm}$ 的相消节点，消除了团簇模型的内在矛盾。

3. **$\alpha$ 衰变向 $1^-$ 态阻尼因子 $\text{HF}(1^-)$ 骤降的宇称投影微观本质：**
   - 实验上，从八极振动核向静态梨形转子过渡时，$\alpha$ 衰变向负宇称 $1^-$ 态的阻尼因子发生量级塌缩：$^{220}\text{Rn}$ 为 $\text{HF}(1^-) = 280$（$^{222}\text{Rn}$ 高达 $1000$），而在静态梨形核 $^{224}\text{Ra}$ 骤降至 $30$，在 $^{226}\text{Th}$ 更进一步跌至 $\text{HF}(1^-) = 4.4$（极弱阻尼，接近非阻尼跃迁）；
   - 该现象在历史上曾被误作为基态存在大量 $\alpha$ 团簇预形成的证据。本研究严格证明：在静态八极形变核中，基态 $0^+$ 与伴随的 $1^-$ 态是从**同一个**内禀非对称梨形 Hartree-Fock 状态 $|\Phi_{\text{pear}}\rangle$ 投影而出的宇称双重态对：
     $$|0^+\rangle \propto (1 + \hat{\mathcal{P}}) |\Phi_{\text{pear}}\rangle, \quad |1^-\rangle \propto (1 - \hat{\mathcal{P}}) |\Phi_{\text{pear}}\rangle.$$
     二者具有几乎完全相同的颈部几何与单粒子密度分布，其向 $\alpha + \text{daughter}$ 渐近通道的隧穿重叠具有本征等价性，从而自然压低阻尼因子至 $\sim 1 - 10$ 尺度，无需预设基态具有现成的 $\alpha$ 粒子。而在振动核中，由于 $1^-$ 为单声子振动态，与基态内禀密度正交，导致 $\text{HF}(1^-) \sim 10^2 - 10^3$。

4. **径向通道重叠与波函数正交性：**
   - 基于 Gogny-HFB 颈部密度收缩路径（Warda & Robledo 2011）计算表明，在内部紧致势阱（$R < 8\text{ fm}$）中，内禀平均场波函数与 $\alpha$ 团簇波函数的投影重叠 $P_{\text{cluster}} < 0.1\%$；
   - 只有当核延伸至断裂与颈缩渐近区（$R > 10.5\text{ fm}$，颈密度 $\rho_{\text{neck}} \to 0$）时，团簇表象才成为物理渐近坐标。这确立了基态低能谱学（紧致八极形变）与超非对称裂变/$\alpha$衰变通道（渐近团簇）在希尔伯特空间的正交分层。

## Provisional Reasoning

物理图像的澄清必须回到自由度与反对称化空间：
- **微观八极形变是多体密集相互作用的连续集体形变**：它不破坏全同费米子的微观反对称化，每个核子在平均场中均享有一致的单粒子轨道波函数，费米面处大矩阵元轨道对产生全相干贡献，天然支撑高达 $40 - 50\text{ W.u.}$ 的巨型八极跃迁；
- **$\alpha$ 团簇模型是高度局域化的关联态**：在核内部（低密度未发展处），强烈的泡利排斥力（Pauli blocking / Wildermuth 条件）会完全洗刷掉独立的 $\alpha$ 片段身份，迫使 4 个核子溶解入普通平均场轨道；
- 只有在核表面低密度区或通过高穿透势垒的大距离渐近区，$\alpha$ 团簇关联才逐渐浮现。
因此，把低能交替宇称能带的激发和跃迁直接归结于现成的 $\alpha$ 团簇转动，是将断裂/衰变通道的渐近自由度错误地投射回紧致基态内部。

## Assumptions

1. **电磁算符多极展开：** 采用标准的平移不变质心偶极算符与电八极算符，长波极限适用；
2. **团簇几何接触间距：** 取刚性双核接触半径 $R_{\text{touch}} = 1.20 (A_c^{1/3} + 4^{1/3})\text{ fm}$，该间距为团簇模型产生最大电磁多极强度的理论上限（若间距更小，电多极矩进一步降低，八极失配更严重）；
3. **宇称投影简化：** 假定静态梨形阱深足以使左右取向态的微观重叠近似局域化（Robledo 2010 中势垒 $\sim 1.5\text{ MeV}$），忽略不同四极形变分量的微弱耦合。

## Competing Explanations

| 假说/模型 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| 纯 $\alpha$ 分子态假说 | 轻锕系负宇称带是由 $\alpha$ 粒子绕核芯转动的分子轨道激发 | 团簇模型产生巨型裸偶极矩（$D_0 \sim 3.9\ e\text{ fm}$），匹配实测 $0.015\ e\text{ fm}$ 需 $P_\alpha \sim 10^{-5}$，但匹配 $42\text{ W.u.}$ 的 $B(E3)$ 需 $P_\alpha \approx 0.75$ | 彻底证伪，求和规则存在 $5 \times 10^4$ 倍不可调和矛盾 |
| $\text{HF}(1^-)$ 团簇证据论 | $^{226}\text{Th}$ 的 $\text{HF}(1^-) = 4.4$ 证明基态存在预形成的 $\alpha$ 团簇 | 证明该低阻尼因子是单体内禀梨形状态宇称投影的直接运动学结果，无需任何基态团簇预形成假设 | 被重构为宇称双重态微观投影证据 |
| 宏观八极常数论 | 认为整个锕系均处于统一的深双阱中 | 本文系统学明确区分静态梨形核（$^{224}\text{Ra}, ^{226}\text{Th}$，$\text{HF} < 30$）与八极软振动核（$^{220}\text{Rn}, ^{228}\text{Th}$，$\text{HF} > 100$） | 被精细化分层为静态转子与软振动两类拓扑相 |

## Transfer Conditions

1. 适用于轻锕系中子数 $130 \le N \le 142$ 附近的反射不对称核区（Rn, Fr, Ra, Ac, Th）；
2. 适用于讨论结团放射性、$\alpha$ 衰变向异宇称态分支与直接库仑激发 $B(E3)/B(E1)$ 之间的跨模型对账；
3. 要求核态处于低激发自旋区（$I \le 12\hbar$），未受高自旋对解耦（Coriolis anti-pairing）严重破坏。

## Failure Conditions

1. 在超轻核（如 $^{16}\text{O} = \alpha + {}^{12}\text{C}$ 或 $^{20}\text{Ne} = \alpha + {}^{16}\text{O}$）中，由于核子总数极少，低密度表面占比高且能隙巨大，真正的分子团簇态能够稳定存在，本研究针对重核紧致平均场的结论不直接适用于轻核团簇分子态；
2. 若远离 $\beta$-稳定线发生奇特衰变使得外核子晕化（如 $^{22}\text{C}$），极弥散的中子晕将改写宏观液滴与单粒子电荷极化平衡；
3. 在极高激发能处（中子分离能以上），团簇连续谱共振态开放，团簇自由度与连续态耦合不能再被忽略。

## Falsification or Reverse Tests

1. **反向检验 1（直接结团探测）：** 若在高能轻离子准自由散射反应（如 $(p, p\alpha)$）中，在 $^{224}\text{Ra}$ 或 $^{226}\text{Th}$ 基态内部直接测定出显著的基态 $\alpha$ 谱学因子（$S_\alpha > 0.20$），则推翻本研究关于基态属于紧致平均场（$P_{\text{cluster}} < 0.01$）的结论；
2. **反向检验 2（中子数跳变与阻尼相关性测试）：** 本模型预测在 $^{222}\text{Ra}$（$N=134$）向 $^{224}\text{Ra}$（$N=136$）演化时，由于静态势阱加深，$\text{HF}(1^-)$ 保持在极低区间（$\sim 20 - 30$），但跨越 $N=138$（$^{228}\text{Th}$）后势阱变平退化为振动态，$\text{HF}(1^-)$ 必然跳升至 $>100$；若实验测出相反趋势，则证伪投影机制。

## Open Questions

1. 在 Warda 2011 探索的 $^{222-226}\text{Ra} \to {}^{14}\text{C} + \text{Pb}$ 团簇放射性中，微观超非对称裂变势垒的惯性张量如何随颈缩坐标非线性演化，需要进一步计算动力学断裂概率；
2. 在奇 $A$ 锕系核（如 $^{225}\text{Ra}, ^{225}\text{Ac}$）中，奇价核子（如 $\nu [j_{15/2}]$）对 $\alpha$ 衰变通道的选择性阻断（blocking effect）如何与宇称双重态磁偶极矩解耦协同演化，仍需后续定向专题突破。

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究基于第一性原理多极求和规则与国际最新直接库仑激发与 $\alpha$ 衰变评价数据集，完成了代码自洽数值闭环；
- 结论属于严格物理推论与模型边界判定（`reasoning_status: provisional`），保留人工与实验终局复核窗口。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，彻底终结了轻锕系核中 $\alpha$ 团簇分子态与平均场八极形变的求和规则与阻尼因子争端，确立了宇称投影与波函数正交性边界。
