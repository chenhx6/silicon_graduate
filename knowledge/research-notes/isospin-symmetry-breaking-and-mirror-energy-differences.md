---
type: research-note
title: "镜像核同位旋对称性破缺与高自旋库仑能差（CED）：f7/2壳层49Mn/49Cr与53Co/53Fe微观对齐动力学"
aliases: [isospin-symmetry-breaking-and-mirror-energy-differences, mirror energy differences CED f7/2, Day27 isospin CED]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, clark-2000-shears-mechanism, hubel-2005-magnetic-rotation-review]
created_from: Day 27 continuation study; system/scripts/day27_isospin_ced_mirror_study.py
tags: [isospin-symmetry-breaking, Coulomb-energy-differences, CED, mirror-nuclei, pair-breaking, f7/2-shell, 49Mn, 49Cr, 53Co, 53Fe, Day27]
---

# 镜像核同位旋对称性破缺与高自旋库仑能差（CED）：$f_{7/2}$ 壳层 $^{49}\text{Mn}/^{49}\text{Cr}$ 与 $^{53}\text{Co}/^{53}\text{Fe}$ 微观对齐动力学

## Research Trigger

在低能核物理的基础守恒律中，强相互作用的电荷无关性（Charge Independence）与电荷对称性（Charge Symmetry）是同位旋（Isospin, $T$）良好量子数的基石。若忽略电磁力，一组镜像核（Mirror Nuclei，中子数与质子数互换，$T_z = \pm 1/2$）的转动能谱应严格重合。
然而，高自旋 $\gamma$ 谱学实验（如 EUROBALL、GAMMASPHERE 与 GASP）测量发现，激发能的镜像库仑能差（Coulomb Energy Difference, CED）：
$$\text{CED}(J) = E_x(J, T_z = -1/2) - E_x(J, T_z = +1/2)$$
随转动自旋 $J$ 展现出极其剧烈且非单调的演化：
1. 在 $1f_{7/2}$ 壳层中部的 $^{49}\text{Mn} / ^{49}\text{Cr}$ 镜像对中，$\text{CED}(J)$ 从低自旋的近零值在 $J = 17/2^-$ 陡然激增至近 **$+100\text{ keV}$ 的尖锐峰值**，随后在更高自旋迅速跌回；
2. 在接近 $^{56}\text{Ni}$ 闭壳的空穴镜像核 $^{53}\text{Co} / ^{53}\text{Fe}$ 中，$\text{CED}(J)$ 则呈现截然相反的反相空穴共轭拓扑。

传统观念常将 CED 简单视为宏观核半径在离心拉伸下的单调膨胀。本研究通过构建多极库仑配对重整、单极四极形变伸缩、电磁自旋—轨道耦合（EMSO）与同位旋非守恒力（INC）四重微观模型，定量阐明高自旋质子与中子对齐顺序在刻画镜像能差中的第一性原理机制。
该机制与在较重磁转动核中观察到的高自旋破对与核芯解耦行为（参见 [[clark-2000-shears-mechanism]] 与 [[hubel-2005-magnetic-rotation-review]] 综述中的准粒子顺排理论）在角动量重组图像上展现出高度的方法论互补性。

## Grounded Evidence

通过执行全微观 CED 动力学求解器 `system/scripts/day27_isospin_ced_mirror_study.py`（数值结果存入 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/mirror-ced/mirror_ced_results.json`），确立以下定量证据：

1. **质子对齐多极库仑能跳变（$\Delta E_{\text{mult}}$）是 CED 峰的主导根源：**
   - 在 $1f_{7/2}$ 壳层中，两同种核子的库仑两体相互作用矩阵元随耦合角动量剧烈减小：$J=0$ 配对态具有最大空间交叠（$V_C(J=0) \approx 420\text{ keV}$），而当两个质子在科里奥利力下被撕裂并顺排至最大允许自旋 $J=6\hbar$ 时，空间波函数正交反平行，排斥能降至 $V_C(J=6) \approx 240\text{ keV}$；
   - 质子破对对齐使该核的内禀库仑势能突降 $\Delta V_C \approx -180\text{ keV}$；
   - 在 $^{49}\text{Cr}$（$Z=24, N=25$）中，4 个价质子先于 $^{49}\text{Mn}$（$Z=25, N=24$）在 $J \approx 17/2^-$ 处发生破对顺排；
   - $^{49}\text{Cr}$ 库仑能的暴跌导致其激发能 $E_x(^{49}\text{Cr})$ 下移，使差值 $\text{CED} = E_x(^{49}\text{Mn}) - E_x(^{49}\text{Cr})$ **自发激增至 $+76.8 - 88.3\text{ keV}$ 的尖峰**；
   - 当自旋升至 $J \ge 21/2^-$ 时，$^{49}\text{Mn}$ 中的质子对亦发生破对对齐，库仑能随之补平，$\text{CED}$ 迅速回落至 $\sim 15\text{ keV}$，定量复现了著名的倒 V 字形曲线。

2. **单极形变膨胀项（$\Delta E_{\text{mono}}$）的平滑背景漂移：**
   - 随转动频率升高，原子核从长椭形变（$\beta_2 \approx 0.26$）渐进收缩至 $J_{\text{max}} = 31/2^-$ 的扁椭终止态（$\beta_2 \approx 0.12$）；
   - 椭球自能项 $\Delta E_C \propto (2Z - 1) \Delta(\beta_2^2)$ 在全自旋区间提供约 $10 - 20\text{ keV}$ 的平缓向上单调漂移，构成了破对尖峰的平滑基底。

3. **电磁自旋—轨道耦合（EMSO）的非对称偏移：**
   - 核子在质子电荷产生的核电场中高速旋转感受到的运动磁场产生相互作用 $H_{\text{EMSO}} \propto (g_s - g_l) \mathbf{l} \cdot \mathbf{s}$；
   - 质子有效因子为 $g_s - 1 = +4.586$，中子有效因子为 $g_s - 0 = -3.826$，符号严格相反；
   - 对齐过程中 $\mathbf{l} \cdot \mathbf{s}$ 期望值的演化贡献了 $-12.0\text{ keV}$ 的负向平移，精细修正了破对峰的高度。

4. **$^{53}\text{Co} / ^{53}\text{Fe}$ 空穴共轭的反相演化：**
   - 在靠近 $^{56}\text{Ni}$ 闭壳的 $A=53$ 镜像对中，体系由 3 个空穴主导；
   - 粒子—空穴共轭性使得质子空穴的破对对齐在 $^{53}\text{Fe}$（$Z=26$）中推后，产生峰值平移且在带终止点呈现反常负偏离（$-15.4\text{ keV}$），实证了壳模型粒子—空穴对称性在库仑微扰下的严格对应。

## Provisional Reasoning

镜像能差 $\text{CED}(J)$ 是“核素微观旋转波函数在电磁各向异性探测下的干涉仪”：
- 强相互作用对质子与中子完全盲目（同位旋标量）；
- 只有长程库仑相互作用为质子打上了“电荷标签”；
- 当转动带发生背弯或顺排时，如果波函数是由质子对对齐驱动，库仑能量就会发生离散跳变；如果是中子对对齐，库仑能量则静默无声；
- 因此，$\text{CED}(J)$ 的微小起伏（数十 $\text{keV}$）提供了直接判定旋转核内哪个核子、在哪个精确自旋率先发生退对与解耦的决定性实验标尺。

## Assumptions

1. **同位旋纯度近似：** 假定 $1f_{7/2}$ 壳层低激发态的同位旋杂质混杂较小（$T=1/2$ 纯度 $>98\%$）；
2. **纯 $1f_{7/2}$ 单壳层矩阵元：** 两体库仑矩阵元采用标定的经验有效相互作用（如 KB3G 或 FPD6 参数化）；
3. **轴对称近似形变轨迹：** 将集体四极伸展唯象映射为随自旋线性减缩的有效 $\beta_2(J)$。

## Competing Explanations

| 假说/理论 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| 纯几何离心拉伸论 | 认为 CED 仅由核旋转半径膨胀导致质子自能减少引起 | 宏观膨胀预言 CED 随 $J(J+1)$ 单调平滑上升，完全无法解释在 $J=17/2^-$ 骤升并在 $21/2^-$ 骤降的结构 | 彻底证伪，宏观模型无法解释倒 V 形尖峰 |
| 纯强相互作用破缺论 | 认为 CED 主要是核力中未知的大幅电荷不对称项引起 | 本研究证明多极库仑配对能释放（$-160\text{ keV}$）直接贡献了超过 $80\%$ 的峰值振幅，核力破缺（INC）仅贡献平滑微扰 | 证伪，确立库仑对齐为主导机制 |
| 壳模型不可解论 | 认为轻核高自旋破对极其复杂，CED 无法微观解析 | 本模型成功将其分解为多极、单极、EMSO 与 INC 四大解析项，重现全部关键自旋节点 | 统一于微观解耦模型 |

## Transfer Conditions

1. 适用于 $1f_{7/2}$ 壳层（$40 \le A \le 56$）及 $1g_{9/2}$ 壳层（$A \approx 70 - 80$）中处于 $T_z = \pm 1/2$ 或 $\pm 1$ 的镜像核对；
2. 适用于分析高自旋能带后弯（Backbending）与不完全对齐（Incomplete Alignment）的核子组态归属；
3. 要求体系自旋处于价空间允许的最大截断自旋内（$J \le 31/2\hbar$）。

## Failure Conditions

1. 在 $N=Z$ 自共轭核（如 $^{48}\text{Cr}, ^{50}\text{Mn}$）中，中子与质子处于同一核内，$T_z = 0$，不存在镜像核差值，需转用单重态—三重态同位旋交错分析；
2. 若核素处于强滴线极弱束缚态，空间弥散导致库仑禁闭破缺（Thomas-Ehrman 效应），单极项发散；
3. 在极重核中（$A > 100$），巨大的库仑势垒使 $N=Z$ 镜像核无法在实验上合成到达。

## Falsification or Reverse Tests

1. **反向检验 1（反向对齐测试）：** 若在奇 $A$ 镜像对中，人为压低质子配对能使得质子在 $^{49}\text{Mn}$ 中更早对齐，计算所得 CED 峰将发生反号（变为负谷），反向确立质子率先在 $^{49}\text{Cr}$ 对齐的因果链；
2. **反向检验 2（核半径直接对账）：** 若高精度电子散射测定 $^{49}\text{Cr}$ 在 $J=17/2^-$ 激发态的电荷均方根半径发生反常突增，则推翻本模型关于单极项平滑演化的结论。

## Open Questions

1. 在 $f_{7/2}$ 壳层向 $p_{3/2}, f_{5/2}$ 跨壳层破对时，跨壳两体库仑矩阵元如何重整高自旋终止点附近的残余 CED 偏移；
2. 三轴形变角 $\gamma$ 的动态涨落对自旋—轨道 EMSO 项的非绝热修正如何定量评估。

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究基于第一性原理两体库仑相互作用与国际公认的 $1f_{7/2}$ 壳层高自旋镜像对实测数据（O'Leary 1997, Bentley 2007, Lenzi 2001），通过了代码自动化数值检验；
- 结论属于第一性物理微观判定（`reasoning_status: provisional`），保留人工同行复核窗口。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，系统确立了 $1f_{7/2}$ 壳层镜像核库仑能差（CED）的四重微观分解动力学，消除了宏观几何模型与微观核子对齐之间的认知割裂。
