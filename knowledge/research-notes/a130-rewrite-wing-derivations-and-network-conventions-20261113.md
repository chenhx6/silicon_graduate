---
type: research-note
title: "A130两翼算符与开放网络深入推导：准自旋相消、禁戒阻碍度与吸收马尔可夫链"
aliases: [A130 wing derivations and network conventions]
created: 2026-11-13
updated: 2026-11-14
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "附录D两翼算符与开放网络的深入推导合同（2026-11-14 G96清除C0控制字符并修正准自旋相消与开放网络边界）"
promotion_target: ""
evidence_sources: [book-jain-nuclear-isomers, book-suhonen-from-nucleons-to-nucleus, doctoral-r1-g34-zhi-2013-prc-shell-model-half-lives, cirigliano-2018-leading-short-range-double-beta, dimitriou-2021-beta-delayed-neutron-reference-database, book-bertulani-nuclear-reactions]
tags: [A130, quasispin, seniority, K-isomer, first-forbidden, 0nubb, beta-delayed-neutron, Markov-chain, open-networks]
---

# 两翼算符与开放网络的深入推导与微观边界

## Research Trigger

在第 4 章“两翼展开与环境布居”中，原子核结构理论向三个纵深方向展开：
其一是亚稳同核异能态的对称性与禁戒跃迁机制（Seniority 异能态与 $K$ 异能态，第 4.6 节）；
其二是弱衰变多极算符、形状因子与双贝塔微观矩阵元（第 4.7 节）；
其三是超形变带退激与天体开放环境布居动力学（第 4.8 节）。
正文侧重于物理图像与系统规律，为确保正文逻辑紧凑，复杂的算符代数证明、高阶禁戒分量解析展开、马尔可夫吸收链递推以及两态开放主方程本征模推导移至附录 D。
本笔记系统固化附录 D 所需的微观算符定义、代数推导与边界条件。

## Grounded Evidence

1. **准自旋 $\mathrm{SU}(2)$ 代数与同资数跃迁相消**：
   - Jain 等《Nuclear Isomers: A Primer》（2021, Springer）第 3 章（PDF pp. 52–53, 式 3.14–3.15）系统推导了单 $j$ 壳层的准自旋形式体系。
   - 准自旋产生算符 $\hat{S}_+ = \frac{1}{2}\sum_m (-1)^{j-m} a_{jm}^\dagger a_{j,-m}^\dagger$ 与湮灭算符 $\hat{S}_-$ 生成对，$\hat{S}_0 = \frac{1}{2}(\hat{N} - \Omega_j)$，其中 $\Omega_j = j + 1/2$。
   - 单体偶多极电算符（$L > 0$ 且为偶数，如 $E2, E4$）在准自旋空间变换为秩 1 矢量张量（$\kappa=1, \kappa_0=0$）。以最低权重基准态 $n=v$（$S_0 = -S = (v - \Omega_j)/2$）为基准，根据 Wigner-Eckart 定理，同资数跃迁矩阵元满足：
     $$
     \langle j^n v I_f \| \mathcal{M}(EL) \| j^n v I_i \rangle = \frac{\Omega_j - n}{\Omega_j - v} \langle j^v v I_f \| \mathcal{M}(EL) \| j^v v I_i \rangle.
     $$
   - 物理占据粒子数遍历 $n = v, v+2, \dots, 2\Omega_j - v$（满足 $v \le \min(n, 2\Omega_j - n)$）。代数相消点 $n = \Omega_j$ 仅当 $\Omega_j \equiv v \pmod 2$ 时才是准自旋阶梯上允许物理占据的可达态。
   - 在纯单 $j$ 壳层同种费米子体系中，同资数的所有偶多极电算符（含 $E4$ 等）在半满处同样精确相消；内转换与光子辐射共享同一微观核矩阵元，在零点内转换几率同样为零；同种核子纯单 $j$ 壳层内磁偶极算符 $\hat{\mathbf{M}}(M1) \propto \hat{\mathbf{J}}$，无非对角跃迁。这不排除同资数奇秩磁跃迁（如非零 $M3$）的算符出口；实际衰变还需正的能量释放，纯配对简并例不产生有限能光子。真实退激也可涉及跨资数跃迁或组态混合。撤回 $^{210}\mathrm{Po}$ 的 $8^+$ 态（两价质子 $n=2 \ne \Omega=5$）作为半满相消例，规范对接第 4.6 节已核定的 $^{130}\mathrm{Sn}$ 两空穴结构条件。

2. **$K$ 异能态折合阻碍度与三轴相干混合**：
   - Jain 等（2021）第 5 章规范：$K$ 禁戒度 $\nu = |K_i - K_f| - \lambda$。经验平均折合阻碍度 $f_\nu = (F_W)^{1/\nu}$。
   - $f_\nu$ 是实验宏观跃迁率的几何平均表征，非微观第一性原理守恒常数。三轴非轴对称形变引入强烈的 $\Delta K = \pm 2$ 组态混合，形成旁路跃迁通道，导致表观 $f_\nu$ 剧烈下降至小于 5 甚至接近 1。

3. **弱衰变算符分解与手征接触项**：
   - Zhi 等（2013, PRC 87, 025803）：一阶禁戒衰变算符分解中，$\mathbf{r}$ 与 $\mathbf{p}/m_N$ 属矢量流算符，$[\mathbf{r}\times\boldsymbol{\sigma}]^{(1)}$ 属轴矢量流算符。介质增强主要体现在类时轴荷算符（$q(\xi' v) = 1.266$），空间分量算符呈现淬灭。
   - Cirigliano 等（2018, PRL 120, 202001）：标准轻 Majorana 交换由单一虚中微子线驱动，非微扰两核子 $^1S_0$ 散射的紫外重整化要求引入领头阶接触势，在 $t_3(n) = +1/2, t_- |n\rangle = |p\rangle$ 规范下写作 $V_{\mathrm{CT}}^{(R)} = -2 g_\nu^{NN} \delta_R^{(3)} t_{1,-} t_{2,-}$。核子--核子散射中的 CIB 数据约束反项组合 $(C_1 + C_2)$，无法单独唯一标定 $g_\nu^{NN}$。

4. **相继级联退激的吸收马尔可夫链模型**：
   - Dimitriou 等（2021, NDS 173, 144）：本任务在退激背景下可用带累积中子数的增广状态 $(a,m)$ 计数，或用核素质量标签/生成函数保留同样信息；并非该综述直接给出了以下完整马尔可夫推导。条件模型，满足差分吸收平衡方程 $\Pi_x(a) = \sum_{b, r} [\Gamma_{a\to b}^{(r)} / \Gamma_{\mathrm{tot}}(a)] \Pi_{x-r}(b)$（$\Pi_{x<0} \equiv 0$）与吸收终态边界条件 $\Pi_x(t) = \delta_{x0}$。
   - 母核总衰变分支比满足 $\sum_i I_\beta(i) = b_\beta \le 1$；净中子发射分支满足 $\sum_x P_{xn}^{(\beta;\mathrm{parent})} = b_\beta$；条件 $\beta$ 归一满足 $\sum_x P_{xn}^{(\beta\mid\beta)} = 1$。
   - 在标准 R-矩阵通道穿透因子定义下（Bertulani & Danielewicz 2021 式 4.102），$\Gamma_n = 2\gamma_l^2 P_l(\Delta E)$，其中 $P_l \propto (\Delta E)^{l+1/2}$ 已包含相空间速度因子，不可重复计入 $\sqrt{\Delta E}$。

5. **开放两态动力学主方程与本征模**：
   - 两态主方程以损耗衰变率 $D_1, D_2$（$\mathrm{s}^{-1}$）描述耗散，耦合矩阵为 $\mathbf{A} = \begin{pmatrix} -(a+D_1) & b \\ a & -(b+D_2) \end{pmatrix}$。
   - 特征判别式 $\Delta = [(a-b)+(D_1-D_2)]^2 + 4ab \ge 0$ 严格非负，重根完整条件为 $ab=0$ 且 $a-b+D_1-D_2=0$；可存在单向交换的非平凡 Jordan 块。无源非负布居有界来自总布居不增加，而非 Jordan 形式的一般保证。
   - 封闭交换极限（$D_1 = D_2 = 0$）下收敛时间为 $\tau_{\mathrm{exch}} = 1/(a+b)$（要求 $a+b > 0$）；等共同漏失（$D_1 = D_2 = D > 0$）、无源、$a+b>0$ 且总布居非零时，归一化组分份额 $f = N_2/(N_1+N_2)$ 依然严格以速率 $a+b$ 弛豫至 $a/(a+b)$。
   - 开放分层极限下快模展开为 $\lambda_{\mathrm{fast}} \approx -(a+b) - \frac{aD_1+bD_2}{a+b}$，慢模为 $\lambda_{\mathrm{slow}} \approx -\frac{bD_1+aD_2}{a+b}$。
   - 对任意固定非负源存在唯一全局渐近稳定非负定态的充要条件为两态均可达非零耗散通道（$a D_2 + b D_1 + D_1 D_2 > 0$）；细致平衡依赖于完全热动平衡黑体光子浴假定，非热非相干过程依然可用经典反应主方程描述。

## Assumptions

1. 单 $j$ 壳层配对哈密顿量满足严格准自旋李代数。
2. 吸收马尔可夫链假定退激属于瞬发核过程，在所选观测时窗内完全吸收。
3. 两态主方程适用于非相干速率主导下的开放粒子数布居演化。

## Competing Explanations

1. **半满相消与总衰变通道**：纯单 $j$ 壳层同资数偶多极电跃迁与内转换在半满壳处完全相消，且单 $j$ 同种费米子 $M1$ 无非对角转移；不能据此排除同资数 $M3$ 等奇秩磁矩阵元；实际退激还需能级顺序及能量释放，也可能涉及跨资数通道或组态混合。
2. **$f_\nu$ 异常塌缩机制**：折合阻碍度的大幅下降既可源于非轴对称三轴形变诱导的 $\Delta K = \pm 2$ 混合，亦可由低位准粒子激发或八极形变旁路引起。
3. **细致平衡的破缺与主方程形式**：外场强相干性打破细致平衡，但不意味着必须机械套用 Lindblad 形式；非相干非热过程仍可通过反应截面加权的经典主方程精确求解。

## Failure Conditions

1. 准自旋 Wigner-Eckart 约化错误采用 $+S$ 最高权重基准态分母，导致 CG 比值出现中间负号矛盾；
2. 误称单 $j$ 壳层半满相消后仍可通过同资数 $E4$、内转换或单 $j$ 内 $M1$ 维持跃迁；
3. 将 $^{210}\mathrm{Po}$ 的 $8^+$ 态（两价质子 $n=2 \ne \Omega=5$）误作半满相消实例；
4. 缓发中子级联差分方程未显式扣除当前发射中子数 $r$；
5. 在标准穿透因子 $P_l \propto (\Delta E)^{l+1/2}$ 之外重复乘入 $\sqrt{\Delta E}$ 速度因子；
6. 开放两态主方程在无漏失（$D_1 = D_2 = 0$）且有正源注入下误算定态解。

## Validation Plan

1. 验证准自旋 Clebsch-Gordan 系数比值在 $n=v$ 时严格为 $+1$；
2. 验证单核子单 $j$ 壳层内单体偶多极算符粒子-空穴变换符号反转与准自旋矢量性质；
3. 验证吸收马尔可夫链在单一 $1n$ 路径下的中子数递减一致性；
4. 验证开放两态主方程在等漏失下的归一化组分弛豫方程。

## Falsification or Reverse Tests

1. **反向测试 1（最高权重分母）：** 若分母取 $\langle S, S, 1, 0 | S, S \rangle = +S/\sqrt{S(S+1)}$，则代入 $n=v$ 给出比值 $-1$，与基准态自矩阵元矛盾。
2. **反向测试 2（E4 半满存活假说）：** 计算同资数单体 $E4$ 矩阵元粒子-空穴对置性质，证实其准自旋张量同样为秩 1 矢量，在 $n=\Omega$ 处必须与 $E2$ 同步精确相消。
3. **反向测试 3（无漏失有限定态）：** 若令 $D_1 = D_2 = 0$ 并设定正源注入，主方程行列式为 0，粒子总数线性发散，反证无漏失定态解不存在。

## Open Questions

1. 实际形变核中三轴参数 $\gamma$ 的动力学涨落如何定量打破轴对称 $K$ 投影守恒？
2. 在极高激发能的准连续谱区，中子发射道与巨多极辐射道之间的能级密度重叠对吸收马尔可夫链的微观有效宽度矩阵元有哪些修饰？

## Human Review

本笔记由 Agent 自主完成理论推导梳理与来源定位，不包含人工审核事件；历史 review 字段保持中立。

## Promotion or Rejection History

- 2026-11-13：初稿建立。
- 2026-11-14：由 G96 全面接管并修正：彻底清除 C0 控制字符（`\f`, `\b` 等转义字符）；修正准自旋最低权重基准态分母符号；证明单 $j$ 壳层同资数偶多极（含 $E4$）半满相消、内转换共享零矩阵元与单 $j$ 内 $M1$ 无非对角转移；撤回 $^{210}\mathrm{Po}$ 半满断言；更新 Jain 专著版本至 canonical 2021 年版；确立开放网络判别式非负性、等漏失弛豫率与对任意非负源的唯一稳定定态可达漏失条件（不排除奇异网络对特定源的定态族）。

2026-11-14 总控追加核查：半满偶阶电相消不关闭所有奇秩磁矩阵元；$d>0$ 的结论限于任意源的唯一稳定定态；重根需保留单向交换反例。计数增广仅是一种实现，最终吸收归一与有限观测窗须分开。双端投影、FF 秩分块与可复现有限控制见 [[a130-rewrite-seniority-projection-open-network-boundaries-20261114]]。本条不是用户审核事件。

## Provisional Reasoning

准自旋、双端投影和两态网络的条件化推演以 [[a130-rewrite-seniority-projection-open-network-boundaries-20261114]] 的显式公式为当前依据；前述来源只支持各自所核理论或数据背景，不是所有网络推导的直接出处。

## Transfer Conditions

资数公式须保留价空间、同种粒子与允许占据；能谱秩分块须保留未极化和角积分；网络定态须保留非负固定速率及源项条件。向真实核素迁移还需实际能级和跃迁矩阵元。
