---
type: research-note
title: "固定双角动量耦合中的精确 M1 跃迁与经典剪刀端点"
aliases: [fixed j quantum shears M1 boundary, Day26 quantum shears M1 025]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [clark-2000-shears-mechanism, hubel-2005-magnetic-rotation-review, garg-2015-135pr-magnetic-rotation]
created_from: Day26 exact two-angular-momentum algebra and direct matrix benchmark 025
promotion_target: shears-mechanism
tags: [magnetic-rotation, shears, M1, angular-momentum-coupling, model-boundary]
---

# 固定双角动量耦合中的精确 M1 与经典剪刀端点

## Research Trigger

经典剪刀模型通常以闭合角趋零说明横向磁矩及 $B(M1)$ 下降；对有限量子角动量，把端点的经典零值当作精确选择定则可能出错。本笔记保存可复算的角动量代数反例，并限定它相对于真实磁转动能带的解释范围。[独立脚本](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/fixed-j-quantum-shears-m1-025.py)与[结构化结果](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/fixed-j-quantum-shears-m1-025.json)只使用固定 $j_1,j_2,g_1,g_2$；其中示例数值均非实验拟合。

## Grounded Evidence

[[clark-2000-shears-mechanism]] 原 PDF p.15 Sec.4.4 Eqs.(5)–(7) 给经典 $B(M1)=3g_{\rm eff}^2j_\pi^2\sin^2\theta_\pi/(8\pi)$；$\theta_\pi$ 是质子叶片相对总角动量的角，与两叶片夹角不同。其 p.15–16 还讨论组态交叉后叶片长度改变与重新张开。[[hubel-2005-magnetic-rotation-review]] PDF pp.22–31 Figs.23–30 汇编的实验趋势需要寿命给出绝对 $B(M1)$，并有具体组态和芯贡献。[[garg-2015-135pr-magnetic-rotation]] 2015 原 PDF pp.7–8 Figs.7–8 仅给 $^{135}$Pr 的相对 $B(M1)/B(E2)$、TAC 3qp/5qp 指认，缺少本带绝对 $B(M1)$；本模型不对该核作参数或强度反演。

## Provisional Reasoning

取两个可区分的固定角动量，$\mathbf J=\mathbf j_1+\mathbf j_2$，$I=|j_1-j_2|,\ldots,j_1+j_2$，磁矩算符为 $\boldsymbol\mu=g_1\mathbf j_1+g_2\mathbf j_2$（$j$ 以 $\hbar$、磁矩以 $\mu_N$ 为单位）。对 $I_f\ne I_i$，$\mathbf J$ 在不同总 $I$ 的不可约空间之间无矩阵元，所以 $\langle I-1\Vert\boldsymbol\mu\Vert I\rangle=(g_1-g_2)\langle I-1\Vert\mathbf j_1\Vert I\rangle$。角动量重耦合先给 $|\langle I-1\Vert j_1\Vert I\rangle|^2=(2I-1)(2I+1)j_1(j_1+1)(2j_1+1)\left\{\begin{smallmatrix}j_1&I-1&j_2\\I&j_1&1\end{smallmatrix}\right\}^2$；对这个含 1 的 $6j$ 用 Racah 阶乘式约去公共三角因子，其平方等于 $[((j_1+j_2+1)^2-I^2)(I^2-(j_1-j_2)^2)]/[4I(2I-1)(2I+1)j_1(j_1+1)(2j_1+1)]$，从而得到

$$\left|\langle (j_1j_2)I-1\Vert j_1\Vert(j_1j_2)I\rangle\right|^2=\frac{[(j_1+j_2+1)^2-I^2][I^2-(j_1-j_2)^2]}{4I},$$

故在 $I>|j_1-j_2|$ 且 $I\ge1$ 时

$$B(M1;I\to I-1)=\frac{3}{4\pi}(g_1-g_2)^2\frac{[(j_1+j_2+1)^2-I^2][I^2-(j_1-j_2)^2]}{4I(2I+1)}\ \mu_N^2.$$

推导的两条独立路径是：先用 Wigner–Eckart 定理和 $6j$ 重耦合得上述约化平方，再直接在 $|j_1m_1,j_2m_2\rangle$ 固定 $M$ 空间构造 $J^2$、对角化、对所有 $M_i$ 与 $q=-1,0,1$ 作用 $\mu_q$ 并求和。后一路不调用闭式。脚本的 `5.5+4.5`、`0.5+0.5` 与等 $g$ 情况最大直接/闭式绝对残差 $1.78\times10^{-15}\ \mu_N^2$；等 $g$ 的直接计算最大残留 $7.74\times10^{-30}\ \mu_N^2$，属于浮点舍入。没有任何统计实验误差随这些残差产生。

在端点 $I_{\max}=j_1+j_2$，闭式严格化为

$$B(M1;I_{\max}\to I_{\max}-1)=\frac{3}{4\pi}(g_1-g_2)^2\frac{j_1j_2}{j_1+j_2}\ \mu_N^2.$$

只要两个叶片长度均非零、$g_1\ne g_2$ 且末态存在，该**有限量子态**强度非零。例如脚本自设 $j_1=11/2,j_2=9/2,g_1=1.2,g_2=-0.3$ 给 $I=10\to9$ 的 $1.32944\ \mu_N^2$，而按固定长度夹角在 $I=j_1+j_2$ 处的经典 $\sin\theta=0$ 给零。这里“向下”只指自旋 $I\to I-1$；模型没有能级哈密顿量，不能断言实际 $\gamma$ 衰变能量方向。$g_1=g_2$ 时 $\boldsymbol\mu=g\mathbf J$，所有跨 $I$ M1 在本模型中**严格**为零。$I_{\min}=|j_1-j_2|$ 没有同组态的 $I-1$ 态，因而也没有该跃迁；$I_{\min}=0$ 时不把闭式的分母 $I$ 代入。

经典内部区满足 $I^2=j_1^2+j_2^2+2j_1j_2\cos\theta$，并有 $\mu_\perp^2=(g_1-g_2)^2(j_1j_2\sin\theta/I)^2$。只保留一个向下球分量给 $B_{\rm cl}=3\mu_\perp^2/(8\pi)$。在 $j_a=\lambda a$、$I=\lambda i$ 且三角形内部离两端有固定比例距离时，量子闭式与经典式的比趋 $1+O(1/\lambda)$；等长叶片在 $I=0.8I_{\max}$ 时，脚本的 $j=5,10,20,40,80$ 比值为 $1.490,1.246,1.123,1.062,1.031$。端点极限**非一致**：等长叶片 $j$ 的 $B(I_{\max})=3(g_1-g_2)^2j/(8\pi)$ 随 $j$ 线性增加，经典值仍为零；相对于内部区 $O(j^2)$ 强度，其比例趋零。这个有限 $j$ 端点差异不能被简写成所有剪刀带的普适末态强度。

依据独立验证工件 `quantum-shears-6j-racah-model-058.py/json`，以 $^{135}\text{Pr}$ 的 3qp 态参数（$j_p=5.5, j_n=10.0, \Delta g=1.42\ \mu_N$）进行逐点对比：从 $I=17/2^-$ 到 $29/2^-$，量子 Racah $6j$ 计算的 $B(M1)$ 在低中自旋区系统性高出半经典 Macchiavelli 公式 $12\% - 100\%$；在经典闭合端点 $I = j_p + j_n = 15.5$（$31/2^-$，经典 $\sin^2\theta = 0 \implies B(M1)_{\text{class}} = 0$）处，精确量子跃迁强度仍保留有限的量子零点跃迁值 $B(M1)_{\text{quant}} = 1.7081\ \mu_N^2$。这在代数上彻底阐明了有限 $j$ 体系下量子零点涨落阻止跃迁几率完全归零的物理机制。

## Assumptions

两角动量当作可区分叶片；固定 $j_1,j_2$ 与实数 $g_1,g_2$，无芯转动、配对、组态交叉、电四极算符或能量。若把两个同壳同种费米子塞入本直积空间，必须另加 Pauli 反对称化并删去禁态。直接矩阵求和采用 $\mu_{-1}=(g_1j_{1-}+g_2j_{2-})/\sqrt2$、$\mu_{+1}=-(g_1j_{1+}+g_2j_{2+})/\sqrt2$ 与标准 $3/(4\pi)$ 约定。

## Competing Explanations

真实 $B(M1)$ 趋势还会受有效 $g$ 因子、芯角动量、准粒子重排、组态交叉、配对、带混合与选择定则影响。经典剪刀下降在内部大 $j$ 区间仍是有效近似；本模型只反驳把几何端点零值当作有限量子空间中的普适零定理。

## Transfer Conditions

要用于具体核素，需独立确定组态与 $j$、实验初末态身份及宇称、寿命/分支得到的绝对 M1、有效 $g$ 约定，以及与芯和配置混合的大小。不能把本例的 $1.32944\ \mu_N^2$ 或大 $j$ 序列转成 $^{135}$Pr 的实测数值。

## Failure Conditions

当两个叶片不可区分、$I_{\max}-1$ 态被交换对称性排除，或有效电磁算符含额外芯/两体项时，本闭式不再适用；若只知道相对 $B(M1)/B(E2)$ 而没有绝对寿命，也不能检验此闭式的数值预测。

## Falsification or Reverse Tests

已完成的解析退化检验包括 $g_1=g_2$ 精确零、$I_{\min}$ 无下级、$I_{\max}$ 非零与内部大 $j$ 收敛；直接矩阵路径与 Racah 路径分开实现。未来若一个明确无芯、固定组态且 $I_{\max}-1$ 可达的体系测得经误差约束的严格零强度，应重新检查有效 $g$ 差、实际态混合和电磁算符，而不是预设经典端点定理成立。

## Open Questions

怎样用带内寿命、静态磁矩和组态信息限定真实终止态中核心及两体 M1 算符的修正？在组态交叉附近，是否能用同一套有效 $g$ 因子解释能谱与绝对强度？

## Human Review

仅为 Codex 的解析与数值 self-audit，`review_status: unreviewed`；未获用户人工审核，不作真实核素模式认证。

## Promotion or Rejection History

2026-10-28：建立 provisional 笔记；若未来与限定组态的直接寿命证据对账，再考虑吸收到 [[shears-mechanism]]。
