---
type: research-note
title: "PNC-CSM中的Cd反磁转动配对阻塞与Vπν响应"
aliases: [AMR PNC blocking Cd, particle-number-conserving pairing blocking interaction evolution]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [zhang-2013-105106cd-pnc-superfluidity, zhang-2019-104pd-pnc-antimagnetic-rotation, zhao-2012-105cd-cdft-antimagnetic, wu-2011-pairing-rotation-blocking-pnc, roy-2011-cd110-systematics-antimagnetic]
created_from: Day26 delegated PNC-CSM pairing-blocking and V_pinu audit
promotion_target: antimagnetic-rotation
tags: [antimagnetic-rotation, PNC-CSM, pairing, Pauli-blocking, 105Cd, 106Cd, 108Cd, 110Cd, V-pinu]
---

# PNC-CSM中的Cd反磁转动配对阻塞与Vπν响应

## Research Trigger

本页审计三个相互耦合的问题：奇中子核 105Cd 中 νd5/2 或 νg7/2 阻塞如何改变剩余中子配对关联、对齐和动态惯量；偶偶 106、108、110Cd 中 ν(h11/2)^2 与 π(g9/2)^−2 的双剪刀构型如何随配对和占据演化；以及半经典模型使用的 Vπν=1.2 MeV 能否被解释成含核芯极化和配对相干的微观有效量。

任务中“PNC 保留有限粒子数超流相干”需要精确定义。固定 N 的 PNC-CSM 不产生 BCS 意义下的异常平均 ⟨aa⟩；它在固定粒子数 CMPC/Fock 空间中保留不同配对占据组态的相干混合。Zhang 2013 将这种处理用于 105、106Cd（PDF pp.4–10，Eqs.(1)–(12)、Figs.2–4），Zhang 2019 将相同方法用于 104Pd（PDF pp.2、4–7，Eqs.(1)–(11)、Figs.3–7）。

## Grounded Evidence

| 证据问题 | 直接来源与定位 | 可安全采用的结论 | 边界 |
|---|---|---|---|
| PNC-CSM 的粒子数与阻塞 | [[zhang-2013-105106cd-pnc-superfluidity]]，PDF pp.4–6，Eqs.(1)–(11)；[[wu-2011-pairing-rotation-blocking-pnc]]，PDF pp.2–5，Eqs.(1)–(12) | 在截断多粒子组态空间直接对角化单极配对推转哈密顿量，固定 N，Pauli 占据由 Fock 代数显式处理 | “精确”只针对选定 Hamiltonian、单粒子空间和截断，不是全核精确解 |
| 105Cd 的奇粒子响应 | Zhang 2013，PDF pp.7–10，Figs.2–4 | 约 0.4 MeV 的 νg7/2 对齐交叉被作者用于解释 105Cd；加入配对后中子交叉更平滑/推迟，质子空穴闭合更明显；配对计算使 Q20 在约 0.45–0.75 MeV 从 0.55 降到 0.41 eb | 文中 105Cd 采用 Gn=0.80 MeV，属于模型输入；不能把差异全归因于自动阻塞或把 Q20 轨迹当成独立实验测量 |
| 106Cd 的占据与 E2 | Zhang 2013，PDF pp.7–10，Figs.2–4 | 约 0.3 MeV 的 (g7/2,d5/2)→h11/2 占据变化参与交叉；固定形变不能完整重现高频 B(E2)，需 ε2 约 0.14→0.12 的变化 | 106Cd 的 Gn=0.45 MeV 也是输入；固定形变和配对不能单独给出全部绝对 B(E2) |
| 105Cd 的无配对基准 | [[zhao-2012-105cd-cdft-antimagnetic]]，PDF pp.11、13–19、22–23，Eq.(21)、Figs.2、6、8–9 | TAC-CDFT 计算直接忽略配对，并在 h11/2 奇中子上实施阻塞；带含 πg9/2^-2、一个 h11/2 奇中子及 gd 混合中子的对齐贡献 | 该成功的 AMR 几何计算不能证明真实配对为零，且不是 PNC 结果 |
| 106、108、110Cd 的有效 Vπν | [[roy-2011-cd110-systematics-antimagnetic]]，printed pp.324–326，Eqs.(3)–(6)、Fig.3及结论 | 三个偶偶 Cd 核均采用 Vπν=1.2 MeV；随 N 变化的显式输入主要是 jν、n 和核芯响应，而不是已测得的 Vπν 单调变化 | 1.2 MeV 是粒子加转子角势中的有效参数，不是裸 πν 两体矩阵元 |
| 110Cd 的绝对强度与平台边界 | Roy 2011，p.324 Table 1；pp.325–326，Fig.4 | 16+–24+ 的 B(E2) 为 0.14(1)、0.12(2)、0.11(2)、0.09(3)、0.06(2) e²b²，呈平缓下降；1323→1314 keV 的有限差分给出负 J^(2) 候选点，必须保留其边界 | DSAM stopping power、feeding、两条相近能线和高自旋端有效寿命限制反演；平缓下降不是严格常数平台 |
| 同 N 的 Pd/Cd 对照 | [[rather-2014-104pd-antimagnetic-arxiv-full]]，PDF pp.4–6，Eqs.(4)–(9)；[[zhang-2019-104pd-pnc-antimagnetic-rotation]]，PDF pp.5–7，Figs.4–7 | 104Pd 直接沿用 Vπν=1.2 MeV、Vππ=0.2 MeV 的有效参数；PNC 四个部分质子空穴与有效两空穴粒子加转子构型不是同一归一化 | 不能把四空穴数目直接变成 Vπν=2.4 MeV |

## Provisional Reasoning

### 1. 固定 N 的 PNC 配对与奇粒子阻塞

采用文献同类的推转单极配对形式

$$
H'(\omega)=H_{\rm sp}-\omega J_x-G\sum_{ab}P_a^\dagger P_b,\qquad
P_a^\dagger=\sum_{m>0}\eta_{am}a_{am}^\dagger a_{a\bar m}^\dagger .
$$

在固定 N 的 CMPC 基底 $|\alpha\rangle$ 中，$|\Psi_N(\omega)\rangle=\sum_\alpha C_\alpha(\omega)|\alpha\rangle$，所以 $\mathrm{Var}(N)=0$。固定 N 不等于没有配对：配对散射项使不同成对占据组态发生混合，并给出负的配对关联能。这里使用

$$
E_{\rm pair}=\langle H_{\rm pair}\rangle\le0,
\qquad \widetilde\Delta_{\rm PNC}=\sqrt{G[-E_{\rm pair}]}
$$

作为关联能型 gap 诊断。它不是 BCS 的异常场 $\Delta=G\sum uv$，也不意味着固定 N 态有非零 $\langle aa\rangle$。Wu 2011 的 PDF p.5 Eq.(10) 同样把关联能型量与异常平均区分开。

奇粒子阻塞在本页的可复现求解中定义为：固定奇数 N，并从所选阻塞轨道的 $P_a^\dagger P_b$ 通道中移除该轨道。这样保留奇粒子占据和显式 $J_x$，同时禁止该轨道参与成对散射。它是 PNC-CSM 阻塞的透明小空间实现，不声称复现 Zhang 2013 的完整 Nilsson 空间。

### 2. 对 105Cd 的物理含义

阻塞降低剩余活跃轨道的配对散射相空间，因此预期 $-E_{\rm pair}$、$\widetilde\Delta_{\rm PNC}$ 和成对相干密度下降；但 $J_x$ 响应的方向取决于被阻塞的是 d5/2 还是 g7/2。这个“配对减弱、惯量方向依轨道而异”的组合比“奇粒子一定使惯量增大”更符合微观结构。

本轮小空间计算（参数和结果见 Reproducible Artifacts）在 $\hbar\omega=0.4$ MeV 的数值对照为：未阻塞奇数参考的 $-E_{\rm pair}=7.34$ MeV、$\widetilde\Delta=2.42$ MeV、$J_x'\simeq7.92\,\hbar^2$/MeV；d5/2 阻塞为 3.89 MeV、1.76 MeV 和 8.94 $\hbar^2$/MeV；g7/2 阻塞为 1.95 MeV、1.25 MeV 和 24.29 $\hbar^2$/MeV。由于是 toy 空间，绝对 MeV 和惯量不可外推；可靠的局部结论是阻塞强度和 $J^{(2)}$ 响应具有轨道依赖，不能用一个“奇粒子抑制因子”概括。Zhang 2013 原件支持 105Cd 配对推迟中子对齐交叉，但没有给出本页 toy 数值。

### 3. Vπν 的微观来源和相干重整化

从可分离四极相互作用开始：

$$
H_Q=-\kappa_{\pi\nu}\,Q_\pi\cdot Q_\nu,
\qquad
Q_\tau=\sum_{ij\in\tau}q_{ij}a_i^\dagger a_j .
$$

在 BCS 表象中，四极算符连接两个准粒子时会出现一类相干组合

$$
\mathcal C^{\rm BCS}_{jj'}\propto u_jv_{j'}+v_ju_{j'}
$$

（具体正负号随时间反演相位和算符通道约定）。于是把 $Q_\nu$ 投影到粒子–空穴角变量 $\theta$ 后，$P_2(\cos\theta)$ 的系数包含轨道四极矩、占据、配对相干和核芯极化，而不是单独的裸 $\kappa_{\pi\nu}$。

固定 N 时，以二体密度替换 BCS 的异常平均：

$$
\rho^{(2)}_{ab}(\omega)=
\langle\Psi_N(\omega)|P_a^\dagger P_b|\Psi_N(\omega)\rangle,
$$

并令 $Q_\nu^{\rm PNC}(\omega)$ 由一体占据和 $\rho^{(2)}$ 共同构成。对同一算符归一化和同一投影约定，可定义条件有效量

$$
V_{\pi\nu}^{\rm eff}(\omega)=V_{\pi\nu}^{\rm ref}
\frac{Q_\pi^{\rm eff}(\omega)Q_\nu^{\rm PNC}(\omega)}
{Q_\pi^{\rm eff}(0)Q_\nu^{\rm PNC}(0)},
\qquad V_{\pi\nu}^{\rm ref}=1.2\ {
m MeV}.
$$

这只在固定构型、$P_2$ 截断、同一有效电荷和同一核芯消元下才是可比较的定义。脚本使用更简化的 $V_{\pi\nu}^{\rm proxy}=1.2\,C_{\rm pair}(\omega)/C_{\rm pair}(0)$，用于显示配对相干软化趋势；它不是对 Roy 2011 的 1.2 MeV 重新拟合，也不是微观裸 TBME。

核芯极化可用二次响应说明：

$$
E_c=\frac12q_c^TCq_c-q_c^T(F_\pi Q_\pi+F_\nu Q_\nu),
\quad
\Delta E_{\pi\nu}^{\rm ind}=-Q_\pi^TF_\pi^TC^{-1}F_\nu Q_\nu.
$$

因此四极软度可增强或削弱有效粒子–空穴力矩，取决于 $C^{-1}$、轨道四极矩符号和配对相干。四极软度也不等同于时间奇 Coriolis 响应，不能由 $V_{\pi\nu}$ 单独推出 $\mathcal J_c$。

### 4. B(E2) 平台与 J^(2) 极值的敏感性

Roy 2011 的 110Cd 绝对 $B(E2)$ 是 0.14→0.06 e²b² 的缓降序列，而不是零误差平台（p.324 Table 1）。其 1323→1314 keV 相邻能量差导致 $4/\Delta E_\gamma<0$ 的异常有限差分（printed p.324 Table 1），因此 $J^{(2)}/B(E2)$ 极值对中心化、自旋映射和线形重叠敏感。

在 toy PNC 输出中，$B(E2)$ 采用 $[Q_{20}^{\rm RMS}(\omega)/Q_{20}^{\rm RMS}(0)]^2$，$J^{(2)}$ 采用 $d\langle J_x\rangle/d\omega$。所有 106–110Cd 偶偶代理在 0.4 MeV 附近的 $B(E2)$ 代理约 0.86–0.87，0.8 MeV 约 0.59–0.62；配对相干代理的 $V_{\pi\nu}^{\rm proxy}$ 从 1.2 MeV 降至约 0.99 MeV（0.4 MeV）和 0.52–0.62 MeV（0.8 MeV）。这只是同一 toy Hamiltonian 的内部响应，不能与 Roy 的绝对 e²b² 数值直接比较。

配对强度 $G$ 的变化会同时改变避免交叉宽度、占据转移、$Q_{20}$ 和 $dJ_x/d\omega$。因此，绝对 $B(E2)$ 平台高度主要约束 $Q_{\rm eff}$、形变和相干振幅的乘积；$J^{(2)}$ 极值更多约束能量曲率、准粒子对齐和核芯惯量。两者联合才能减少 $G$、$V_{\pi\nu}$、$\mathcal J_c$ 与形变路径的不可辨识性。

## Assumptions

- 计算只保留 νd5/2 和 νg7/2 两个球形 $j$ 壳，共 14 个单粒子态；$N_{\rm active}=5,6,7,8$ 只是 105–110Cd 的活动空间代理，不是实际价粒子数。
- $\epsilon_{d}=0$、$\epsilon_g=0.28$ MeV、两轨道 $q$ 系数、$G_{105}=0.80$ MeV、$G_{106,108,110}=0.45$ MeV 都是透明 toy 输入。只有文献中的配对强度定位来自 Zhang 2013；toy 单粒子输入没有实验身份。
- $J_x$ 以每个 $j$ 壳的标准相邻 $m$ 矩阵元构造；$Q_{20}^{\rm RMS}$ 只作相对响应指标。
- “阻塞”是移除阻塞轨道的配对散射通道，同时保留奇数 N；没有自洽重求形变、核芯极化或完整 Nilsson 波函数。
- $V_{\pi\nu}^{\rm proxy}$ 用相对 pair density 归一化，只表示条件软化趋势，不替代 Roy/Rather 的有效 1.2 MeV。

## Competing Explanations

- 105Cd 的交叉和惯量变化可来自 g7/2→h11/2 占据重排、Coriolis 混合、形变变化或奇粒子轨道选择，而不只是配对阻塞（Zhang 2013，PDF pp.7–10；Zhao 2012，PDF pp.13–23）。
- 106–110Cd 的 $B(E2)$ 下降可由剪刀闭合、核芯转动、频率依赖形变、有效电荷、配对和 side-feeding/寿命系统误差共同产生。Roy 2011 的 110Cd 结果支持 AMR+core 解释，但不提供各项贡献的唯一分解。
- PNC 的平滑关联能不排除固定 N 空间内的真实对称性/构型交叉；它也不等于所有转频下均无锐结构。Sheikh 2002 的有限模型显示 LN、PAV、PHFB 与精确数投影的差异依赖弱配对和变分路径（[[sheikh-2002-number-projection-pairing-comparison]]，PDF pp.8–13）。
- 1.2 MeV 的半经典 Vπν 是有效角势系数；用 π(g9/2)^−4 的空穴数把它机械乘二会重复计数，且与 PNC 的四空穴空间不是同一归一化（Rather 2014，PDF pp.4–6；Zhang 2019，PDF pp.5–7）。

## Transfer Conditions

可迁移的是：固定 N 的 CMPC 对角化、显式移除阻塞配对通道、用 $\langle P_a^\dagger P_b\rangle$ 代替固定 N 下不存在的异常平均、以及在同一算符归一化内比较 $V_{\pi\nu}^{\rm eff}(\omega)/V_{\pi\nu}^{\rm eff}(0)$。

不能直接迁移的是：toy 输出的绝对 gap、$J^{(2)}$、B(E2)、轨道能、1.2 MeV 乘相干比值、105–110Cd 的活动 N 代理、以及“阻塞 d5/2 比 g7/2 更增大惯量”等数值方向。跨核素使用前必须统一 Nilsson/EDF 单粒子场、配对强度拟合规则、形变约束、阻塞自洽条件和实验寿命归一化。

## Failure Conditions

以下情况会使当前推断失效：把 $\widetilde\Delta_{\rm PNC}$ 写成 BCS 异常场；把固定 N 的 pair density 写成粒子数涨落；把 Jx 的非对角单体干涉项写成配对势矩阵元；把 1.2 MeV 写成裸 πν 两体矩阵元；把 $Q_{20}^{\rm RMS}$ 代理当作绝对 e²b²；把 Roy 的负有限差分点删掉后再宣称 $J^{(2)}$ 单调；或者把 Zhao 的“忽略配对”模型结果当作真实配对为零的实验事实。

## Falsification or Reverse Tests

1. 在相同单粒子空间和 $N$ 下分别运行未阻塞、d5/2 阻塞和 g7/2 阻塞；若 $-E_{\rm pair}$ 不因移除相应配对通道而下降，说明阻塞实现或算符符号有误。
2. 固定 $G$ 和阻塞，改变 $V_{\pi\nu}^{\rm ref}$；若归一化 B(E2)(I) 在 $\mathcal J_c=0$ 时改变，说明把角势参数错误地写进了固定自旋的四极观测量。
3. 在同一 PNC Hamiltonian 中逐项冻结占据、配对散射和 $Q_{20}$，分别比较 $d\langle J_x\rangle/d\omega$ 与 $B(E2)$；只有配对松开时出现的变化才可归因于 pair density 通道。
4. 未来若取得完整 CMPC 系数，可直接计算 $\rho^{(2)}_{ab}$ 并与 toy 的 `pair_coherence` 对照；若 PNC 二体密度不随频率减小而实验 $B(E2)$ 仍保持相同平台，当前“Vπν 由配对相干软化”的解释应降级为非唯一可能。
5. 对 110Cd 保留 1323→1314 keV 的负 $J^{(2)}$ 有限差分，并用原始 gate/feeding 协方差重算；若极值在寿命和能线解耦后消失，不能把该极值归因于配对。

## Open Questions

- 能否取得 Zhang 2013 的 CMPC 权重或至少 $\langle P_a^\dagger P_b\rangle$、轨道占据和一/二体密度，以把本页的 coherence proxy 换成原计算的 operator-resolved 响应？
- 同一 Nilsson/PNC 参数是否能同时描述 105Cd 的奇阻塞、106Cd 的 gd→h11/2 交叉及 108、110Cd 的不同 $j_\nu$ 和核芯响应？
- 在统一四极算符、有效电荷和 DSAM 归一化后，106、108、110Cd 的绝对 B(E2) 平台高度与 $J^{(2)}$ 极值分别对 $G$、$V_{\pi\nu}$、形变和 $\mathcal J_c$ 的 Fisher 信息有多大？
- 能否用自洽 blocking+triaxial deformation 计算检验 105Cd νd5/2 与 νg7/2 候选，而不把谱学评论的争议（Roy 2013 元数据页）误写成已解决？

## Human Review

尚无用户逐条科学审核；`review_status: unreviewed`。本页的直接来源定位由 Codex self-audit 完成，toy 计算和 Vπν proxy 均明确保留条件边界，不能写成 `human-reviewed` 或论文级定论。

## Promotion or Rejection History

2026-10-29：建立本页。保留 Zhang 2013 对 105/106Cd 配对与交叉的原件定位、Zhao 2012 的无配对 TAC-CDFT 对照、Roy 2011 的 106–110Cd 统一 1.2 MeV 有效参数和 110Cd 绝对 B(E2) 证据。拒绝“固定 N 保证所有曲线严格平滑”“奇粒子必然增大惯量”“四个 g9/2 空穴使 Vπν 自动加倍”和“toy proxy 是微观 TBME”的表述。

## Reproducible Artifacts

目录：`outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-pnc-blocking/`。

- `pnc_blocking_response.py`：标准 CMPC/Fock 空间固定 N 对角化；显式 $J_x$、单极配对、d5/2/g7/2 阻塞和相对 Vπν proxy。
- `pnc_blocking_response.csv`：54 行（5 个体系/阻塞扇区 × 9 个频率点）的能量、配对关联、关联 gap、占据、对齐、$J^{(2)}$ proxy、$Q_{20}^{\rm RMS}$、B(E2) proxy 和 Vπν proxy。
- `pnc_blocking_response_summary.json`：方程、输入、证据 locator 和适用边界。
- `provenance.json`：运行命令、脚本哈希和生成物清单。

运行命令：

```bash
cd outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-pnc-blocking
python3 pnc_blocking_response.py
```

脚本运行得到 54 行输出，使用 `scipy.sparse.linalg.eigsh` 对每个固定 N、频率和阻塞扇区求最低本征态；没有读取或改写 `raw/`。
