---
type: research-note
title: "A130重写研学：弱衰变能窗、缓发级联竞争与双贝塔矩阵元边界"
aliases: [A130 weak windows cascades and double-beta boundaries]
created: 2026-11-13
updated: 2026-11-14
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "针对博士论文第4.7节弱衰变三子模块微观机制与多体边界的定向研学（2026-11-14 G96完成全项对账与纠偏修补）"
promotion_target: ""
evidence_sources: [dimitriou-2021-beta-delayed-neutron-reference-database, cirigliano-2018-leading-short-range-double-beta, engel-menendez-2017-double-beta-matrix-elements-review, doctoral-r1-g34-zhi-2013-prc-shell-model-half-lives, wang-2026-axial-coupling-quenching-joint-effects, book-suhonen-from-nucleons-to-nucleus]
tags: [A130, doctoral-foundations, weak-decay, beta-decay, first-forbidden, delayed-neutrons, double-beta, majorana]
---

# 弱衰变能窗、缓发粒子级联与双贝塔矩阵元微观边界

## Research Trigger

在第 4.7 节的体系构建中，弱衰变常被简化为单一的 $Q_\beta$ 能窗积分，或将缓发中子发射几率 $P_n$ 机械等同于 $Q_\beta - S_n$ 能窗大小，亦或将无中微子双贝塔衰变（$0\nu\beta\beta$）核矩阵元与低能单 $\beta$ 淬灭无条件挂钩。本笔记基于国际原子能机构（IAEA）缓发中子基准数据库、手征有效场论短程接触算符与从头算双贝塔矩阵元综述，确立有限衰变能窗下允许与禁戒跃迁的相空间结构、$\beta$ 馈送后 $\gamma/n$ 统计竞争级联的条件概率分解，以及高动量转移下轻 Majorana 交换 $0\nu\beta\beta$ 矩阵元的真实微观依赖。
最新方法学核验与完整数学对账见本库研究笔记 [[a130-rewrite-weak-operator-and-counting-network-audit-20261114]]。

## Grounded Evidence

| 依赖与本轮核读 locator | 实际载体和核验 | 支持范围及证据身份 |
|---|---|---|
| [[dimitriou-2021-beta-delayed-neutron-reference-database]]，全书 96 页，Section II PDF pp. 4–11，PDF pp. 18, 24，Section IV PDF pp. 84–85 | `raw/papers/gpt/query/20261108-r3-g52-beta-delayed-particles/dimitriou-2021-iaea-beta-delayed-neutron-database.pdf`；SHA-256 `ca0b475131704e33f6732163ef996467e630fbea88898dba73cc9f66e7f5684f` | 缓发中子基准数据库：$P_{1n}$、$P_{2n}$、$P_{\ge 1n}$ 与平均中子多重度 $\langle M_n \rangle$ 的操作定义；离散态与准连续谱馈送的条件概率模型；非折叠展开在探测器响应中的必要性。 |
| [[cirigliano-2018-leading-short-range-double-beta]]，PRL 120, 202001 (2018) | `raw/papers/gpt/query/20261108-r3-t07-weak-renormalization/cirigliano-2018-prl120-202001-arxiv-1802.10097v1.pdf`；SHA-256 `c15e22bdb9c811e986493ff2a0b01f2794c8a33a6493b4ba6d62701525304996` | 手征 EFT 下 $0\nu\beta\beta$ 的两核子短程接触算符：在非微扰 $^1S_0$ 散射框架下，单轻中微子势的紫外重整化要求引入领头阶接触项 $V_{\mathrm{CT}}^{(R)} = -2 g_\nu^{NN} \delta_R^{(3)} t_{1,-} t_{2,-}$；核子--核子散射 CIB 数据仅约束特定反项组合，不能唯一单独定值。 |
| [[engel-menendez-2017-double-beta-matrix-elements-review]]，RPP 80, 046301 (2017) | `raw/papers/gpt/query/20261108-r3-g48-weak-operators/engel-menendez-2017-rpp-0nubb-nme.pdf`；SHA-256 `813111c10bab58d8d0f19ca91833383a8a521a33c0434b276eacd4fead195417` | $0\nu\beta\beta$ 核矩阵元综述：特征动量传递 $|\mathbf{q}| \sim 100\text{--}200\,\mathrm{MeV}/c$；BCS 超流配对相干增强与母子核四极形变错位压制；相空间因子与 $g_A^4$ 提取约定。 |
| [[doctoral-r1-g34-zhi-2013-prc-shell-model-half-lives]]，PRC 87, 025803 (2013) | `raw/papers/gpt/query/20261108-foundations-G34/Zhi_2013_PRC_87_025803_SM_halflives_first_forbidden.pdf`；SHA-256 `eaedbd4539854e3d1f0e7860ef7ab9c647d4fa44cd8144b4989ba220ec639333` | 大尺度壳模型计算：微分相空间能谱与形状因子 $C(W)$；一阶禁戒衰变算符张量秩分解（$r$ 属矢量流，$[\mathbf{r}\times\boldsymbol{\sigma}]^1$ 属轴流）；介质增强（轴荷 $\xi' v$）与空间淬灭（$x, u, w, z$）；$N=126$ 等待点核区 FF 贡献超 GT。 |
| [[wang-2026-axial-coupling-quenching-joint-effects]]，arXiv:2605.21218v1 (2026) | `raw/papers/gpt/query/20261113-A130-axial-currents/wang-2026-arxiv2605.21218v1.pdf`；SHA-256 `64b8098517bdf4754ff71d80ab4256aab77102aaa9257390f99db1b3788c0c8d` | RPA 与 PVC 联合计算：$^{56}\mathrm{Ni}$（电子俘获道）PVC 解除闭壳冻结，而 $^{132}\mathrm{Sn}$ 在 SGII 参数下在物理 $Q_\beta$ 能窗内依然零 GT 强度，半衰期受一阶禁戒主导。 |

## Provisional Reasoning

### 1. 衰变能窗区分与微分能谱

核弱衰变必须精确区分衰变能释放窗口：
- $\beta^-$ 衰变：$Q_{\beta^-} = [M(A, Z) - M(A, Z+1)] c^2$；
- $\beta^+$ 衰变：$Q_{\beta^+} = [M(A, Z) - M(A, Z-1) - 2m_e] c^2$（门槛阈值 $2m_e c^2$）；
- 电子俘获（EC）：$Q_{\mathrm{EC}} = [M(A, Z) - M(A, Z-1)] c^2$（单色中微子能量 $E_\nu = Q_{\mathrm{EC}} - E_x - B_j$）。不可将 $\beta^+$ 的 $-2m_e c^2$ 阈值套用至 EC。

出射带电轻子的最低阶微分发射能谱正比于 $F(Z, W) p W (W_0 - W)^2 C(W)$。前因子常数未加辐射修正时为 $K_0 \approx 6291.77\text{ s}$，Zhi 等采用的参考常数为 $K = 6146\text{ s}$（不由两值之差反推修正组成）（Zhi 2013 Eq. 2），Zhi Eq. (4) 给出的是跃迁强度定义式而非微分谱。

### 2. 缓发粒子统计级联与多重度守恒

前驱母核直接弱相互作用馈送满足总衰变分支比归一：
$$
\sum_i I_\beta(i) = b_\beta \le 1.
$$
处于连续谱激发态的能级通过中子发射与辐射 $\gamma$ 竞争退激，满足差分吸收递推关系：
$$
\Pi_x(a) = \sum_{b, r} \frac{\Gamma^{(r)}_{a \to b}}{\Gamma_{\mathrm{tot}}(a)} \Pi_{x-r}(b), \qquad \Pi_{x < 0}(a) \equiv 0, \quad \Pi_x(t) = \delta_{x0}.
$$
每次母核总衰变归一的 $x$ 中子发射净分支比为 $P_{xn}^{(\beta;\mathrm{parent})} = \sum_i I_\beta(i) \Pi_x(i)$，满足 $\sum_{x \ge 0} P_{xn}^{(\beta;\mathrm{parent})} = b_\beta$；当 $b_\beta>0$ 时，条件 $\beta$ 归一几率为 $P_{xn}^{(\beta\mid\beta)} = P_{xn}^{(\beta;\mathrm{parent})} / b_\beta$，满足 $\sum_{x \ge 0} P_{xn}^{(\beta\mid\beta)} = 1$。
单步近似 $\Pi_1(i) \approx \Gamma_n(i)/\Gamma_{\mathrm{tot}}(i)$ 仅在略去多步相继发射且辐射退激直达束缚态的极限下成立。在标准 R-矩阵定义下 $\Gamma_n = 2\gamma_l^2 P_l(\Delta E)$，离心势垒穿透因子满足 $P_l \propto (\Delta E)^{l+1/2}$，不可重复计入速度相空间因子。无门母衰变探测中非 $\beta$ 产中子道（如自发裂变）需独立计入响应项 $p_y^{\mathrm{non\text{-}}\beta}$，不可混淆。

### 3. 轻 Majorana 中微子交换与手征接触项

在标准轻 Majorana 中微子交换机制下，物理过程由核内两核子弱流顶点之间交换一条虚中微子传播子所驱动（特征虚动量 $|\mathbf{q}| \sim 100\text{--}200\,\mathrm{MeV}/c$）。半衰期因式分解为 $[T_{1/2}^{0\nu}]^{-1} = G_{0\nu} g_A^4 |M_{0\nu}|^2 |m_{\beta\beta}/m_e|^2$。
Cirigliano 等（2018）指出，两核子 $^1S_0$ 非微扰散射的重整化要求显式引入手征领头阶短程接触算符，在 $t_3(n) = +1/2, t_- |n\rangle = |p\rangle$ 规范下剥离势为 $V_{\mathrm{CT}}^{(R)} = -2 g_\nu^{NN} \delta_R^{(3)} t_{1,-} t_{2,-}$。核子--核子散射中的 CIB 数据约束 counterterm 组合 $(C_1 + C_2)$，无法单独唯一确定，亦专属于 $0\nu\beta\beta$ 超弱通道而非单 $\beta$ 两体流淬灭。

## Assumptions

1. 允许跃迁微分谱基于非相对论核子反冲与冲量近似。
2. 吸收马尔可夫链假定核退激属于瞬发过程，且状态在观测时窗内完全吸收。
3. $0\nu\beta\beta$ 矩阵元假定标准轻 Majorana 中微子质量项主导轻子数破坏。

## Competing Explanations

1. **能窗与发射几率**：$Q_\beta > S_n$ 是运动学充要条件而非中子发射充分条件；高离心势垒阻碍可使 $S_n$ 以上能态依然由辐射 $\gamma$ 衰变占优。
2. **多体关联与解阻塞**：PVC 打破了闭壳冻结，但其效应高度依赖于核素与相互作用（$^{132}\mathrm{Sn}$ 在 SGII 参数下在物理能窗内仍无 GT 强度）。
3. **有效淬灭外推**：低能单 $\beta$ 衰变经验淬灭因子 $q_A \sim 0.75$ 不可直接套用到高动量转移 $0\nu\beta\beta$ 计算中。

## Transfer Conditions

本笔记结论直接支撑博士论文第 4.7 节三子模块的写作与台账对账；天体物理核合成网络中具体的核反应截面与元素丰度计算移交第 4.8 节；实验测量中的符合探测器立体角、死时间修正与定时算法移交第 5 章。

## Failure Conditions

- 将动学能窗 $Q_\beta - S_n > 0$ 当作必定发射缓发中子的充分条件；
- 将母核衰变分支比归一（$b_\beta \le 1$）与条件 $\beta$ 归一混同，或将自发裂变中子误作缓发中子；
- 缓发中子级联差分方程未扣除当前释放中子数 $r$；
- 混淆单 $\beta$ 衰变的长波长零动量转移极限与 $0\nu\beta\beta$ 的宽动量积分尺度；
- 将手征领头阶短程接触算符混同为单 $\beta$ 衰变的两体弱轴流（2BC）。

## Validation Plan

1. 核对相继缓发中子吸收递推公式的边界条件；
2. 验证裸 Gamow-Teller 算符在同位旋约定下的初态自旋统计平均与差和定则；
3. 核实未加辐射修正相空间常数 $K_0$ 与参考常数 $K$ 的定义边界；
4. 核对手征 EFT 领头阶两核子接触项的重整化自洽性前提。

## Falsification or Reverse Tests

1. **反向测试 1（未扣除发射中子数）：** 若递推写 $\Pi_x(b)$ 而非 $\Pi_{x-r}(b)$，则单一 $1n$ 发射路径将被错误判定为 $0n$；
2. **反向测试 2（未区分能窗）：** 若将 $\beta^+$ 阈值套用至 EC，将错误禁戒低能 EC 通道；
3. **反向测试 3（CIB 单一标定）：** 若声称 CIB 数据能唯一测定 $g_\nu^{NN}$，则抹除了微观理论不确定度。

## Open Questions

1. 实验测得的有效 $q$ 值如何精确解耦两体弱介子交换流（2BC）与高能组态粒子-空穴截断（核芯极化）的各自份额？
2. 在复杂统计退激中，具有宽能级重叠的非正交共振态之间是否存在不可忽略的量子干涉项对中子-光子分支比产生微观调制？

## Human Review

本笔记由 Agent 基于 IAEA 缓发中子数据库、手征有效场论原件及从头算核矩阵元综述定向核读后建立，保留所有模型假设与适用边界；未进行真实用户审核。

## Promotion or Rejection History

- 2026-11-13：初稿建立。
- 2026-11-14：由 G96 全面接管并修正：更新 Dimitriou 真实 SHA-256（`ca0b4...`）；区分母核归一 $b_\beta \le 1$ 与条件 $\beta$ 归一；明确递减吸收平衡方程 $\Pi_x(a) = \sum [\Gamma/\Gamma] \Pi_{x-r}(b)$；明确区分 $Q_{\beta^-}, Q_{\beta^+}, Q_{\mathrm{EC}}$；澄清 $^{132}\mathrm{Sn}$ SGII 物理能窗内零 GT 强度；规范轻 Majorana 虚中微子线机制与 Cirigliano 剥离接触势。

2026-11-14 总控追加核查：半满偶阶电相消不关闭所有奇秩磁矩阵元；$d>0$ 的结论限于任意源的唯一稳定定态；重根需保留单向交换反例。计数增广仅是一种实现，最终吸收归一与有限观测窗须分开。双端投影、FF 秩分块与可复现有限控制见 [[a130-rewrite-seniority-projection-open-network-boundaries-20261114]]。本条不是用户审核事件。
