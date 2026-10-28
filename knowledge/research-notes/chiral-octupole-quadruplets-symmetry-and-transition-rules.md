---
type: research-note
title: "三轴八极奇奇核的手征—八极四重态：离散对称性与跃迁选择定则"
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br, wang-2023-experimental-studies-nuclear-chirality-china, guo-2020-pseudospin-chiral-quartet-131ba, petrache-1996-rotational-bands-134pr, tonev-2006-134pr-lifetime-chiral]
aliases: [chiral-octupole-quadruplets, chiral octupole quadruplet bands]
created_from: Day26 chiral-octupole quadruplets symmetry and transition investigation
promotion_target: chiral-octupole-coexistence
tags: [chiral-octupole, quadruplet, odd-odd, 78Br, 134Pr, 131Ba, simplex, signature, E1, M1, E2]
---

# 三轴八极奇奇核的手征—八极四重态

## Research Trigger

本轮问题是把“$gammaapprox30^\circ$ 的三轴手征自由度”和反射不对称八极自由度放进同一个可计算的四态模型，明确哪些量子数是实验室投影后的好量子数，以及哪些跃迁通道只是模型中强、不能被当作普适定理。目标核优先参考 `78Br`、`134Pr`，并以 `131Ba` 的四带流形作为更直接的理论—实验对照。

## Grounded Evidence

### `78Br`：四重态动机而非四重态确证

Liu et al. 在 `78Br` 报告正宇称 Bands 1–2、负宇称 Bands 3–4 两对候选双带，并观测 Band 1 与 Band 3 之间八条强 E1 连接；TPRM 给出 nonplanar effective-angle 结果，MDC-CDFT 给出反射不对称势面沿 $\beta_{30}$ 的软性（Liu 2016 source 页 `L16-5`–`L16-13`；原文 PDF pp.3–5, Figs.1–6）。

同一论文明确把单核 chirality–parity quartet 写成未来可观测性方向，没有把当前四条带直接标记为已建立 quartet；其 `\beta_{30}` 结果是软势面，不能替代静态非零八极极小（`L16-14`；原文 PDF p.5）。因此 `78Br` 支持“手征双带与八极关联共存”的研究动机，不能单独支持四重简并或静态 `\beta_3>0`。

### Wang 2023：综述层面的可检验假说

Wang et al. 综述不是新实验，覆盖的是候选核 census、能量位移、$S(I)$、alignment、$B(M1)/B(E2)$ 和寿命证据层（PDF pp.1–15；source 页 `WC23-1`、`WC23-4`、`WC23-11`）。它把 `78Br` 归入 MχD 加八极关联案例，并把 `^{76-82}`Br 中实验劈裂变化快于反射对称 TPRM 的差异解释为“八极关联可能催化手征”；但该 TPRM 不含反射不对称，故这是综述级、可检验的跨核推断，不是八极因果的直接测量（`WC23-15`–`WC23-16`；PDF pp.13–14, Fig.12；source 页 `117`）。

### `131Ba`：四带流形的实验前例与边界

Guo et al. 在 `131Ba` 实验上建立互相连接的正宇称 D3–D6 四带流形，另有负宇称 D7/D8 候选双带；D7 到 D3–D6 的多条 E1 连接支持八极关联。RAT-PRM 采用 `\beta_2=0.22,\gamma=27.1^\circ`，并“tentatively”取 `\beta_3=0.05`（原文 PDF pp.1–5；source 页 `GU20-2`–`GU20-14`）。

关键边界是：D3–D6 不能仅由能量和连接唯一分为两对，D5 的相对 E1 feeding 存在模型偏差，角动量几何留待后续工作，且没有寿命或绝对约化跃迁概率（`GU20-7`, `GU20-11`, `GU20-13`, `GU20-15`, `GU20-16`；source 页 `103`–`108`）。这使 `131Ba` 成为“多带耦合与 E1 网络”的证据前例，而不是本文 toy 四重态的参数标定。

### `134Pr`：近简并不能替代绝对电磁向量

Petrache 1996 的 `134Pr` Band 1/Band 2 结构早于手征术语，报告 Band 2 不能由简单 unfavoured-signature partner 一致解释，且 TRS 表面三轴但显著 `\gamma`-soft（原文 PDF pp.12–20；source 页 `PE96-5`–`PE96-12`）。Tonev 2006 的 RDDS/DSAM 寿命显示近简并区 Band 1 的带内 $B(E2)$ 约为 Band 2 的 2–3 倍，$B(M1)$ 平滑而无预期交错；作者结论是不支持静态手征，形状涨落/动态手征仍可兼容（原文 PDF pp.3–4；source 页 `TO06-D24-003`–`TO06-D24-005`）。这提供了本题“隧穿劈裂与电磁矩阵元必须同时处理”的直接反例。

## Provisional Reasoning

### 1. 内禀四态和投影

用两个局域二态自由度表示左右手性与八极双阱：

$$
|\chi,\xi\rangle\in\{|L,+\rangle,|R,+\rangle,|L,-\rangle,|R,-\rangle\},
$$

其中 $\chi=\pm1$ 只标记左/右局域波包，$\xi=\pm1$ 标记 $\beta_3$ 的两个反射不对称井。局域态本身不是良好宇称态。取 $\mathcal C=\mathcal T R_x(\pi)$（具体旋转轴依约定可改为等价的主轴）把左右波包互换，取 $\mathcal P$ 把 $\xi=+$ 与 $\xi=-$ 互换。投影后

$$
|\chi_s,p\rangle=\frac{1}{2}(1+\chi_s\mathcal C)(1+p\mathcal P)|\text{localized}\rangle,
\qquad \chi_s,p=\pm1,
$$

得到四类实验室序列 $|\chi_s,p;I,M\rangle$。这里 $\chi_s$ 是 toy 模型中 $\tau_x$ 的对称/反对称标签；真实有限核中它是近似标签，不能误写成可直接测量的“左右手征量”。

### 2. 四重态能量矩阵与双重劈裂纠缠

在局域基底中使用最小 Hamiltonian

$$
H_I=E_0(I)\,1-t_\chi(I)\tau_x-t_\pi(I)\xi_x-t_{\chi\pi}(I)\tau_x\xi_x.
$$

投影基底中的四个能量为

$$
E_I(\chi_s,p)=E_0(I)-\chi_s t_\chi(I)-p t_\pi(I)-\chi_s p t_{\chi\pi}(I).
$$

因此

$$
\Delta E_\chi(p)=E_I(-1,p)-E_I(+1,p)=2[t_\chi+p\,t_{\chi\pi}],
$$
$$
\Delta E_\pi(\chi)=E_I(\chi,-1)-E_I(\chi,+1)=2[t_\pi+\chi\,t_{\chi\pi}].
$$

$t_{\chi\pi}$ 是手征与宇称隧穿的最低阶纠缠项；它使正/负宇称子空间的手征劈裂不同，也使左右手性子空间的宇称劈裂不同。若 $t_{\chi\pi}=0$，才得到两个相互独立的双重劈裂。脚本采用 $I=8$–14 的纯示意参数，$I=8$ 时输出 $\Delta E_\chi(+)=170$ keV、$\Delta E_\chi(-)=110$ keV、$\Delta E_\pi(+)=250$ keV、$\Delta E_\pi(-)=190$ keV；这些不是 `78Br` 或 `134Pr` 的数据。

### 3. Signature 与 simplex

旋称（signature）定义为

$$r_\alpha=e^{-i\pi\alpha},$$

其中奇奇核整数自旋序列通常用 $\alpha=0,1$，故 $r=+1,-1$；奇质量核半整数序列则用 $\alpha=\pm1/2$，故 $r=\mp i$。对主轴半转动的 simplex 算符

$$\hat S_x=\hat P\hat R_x(\pi),\qquad s=p\,r_\alpha,$$
$$
\hat S_x|I\alpha p\rangle=s|I\alpha p\rangle.
$$

所以 simplex 是 signature 与宇称的复合本征值；对 `odd–odd` 的整数 $I$，$s=\pm1$，对半整数 $I$，$s=\pm i$。不能把符号 $s$ 同时当作数值指数和本征值；脚本 JSON 的 `simplex_table` 明确保存了 $p,\alpha,r,s$ 的复数分量。`\mathcal C` 与 $S_x$ 是否对易取决于轴和相位约定，故实际带标签必须以所用 PRM/TAC 哈密顿量的离散群为准。

### 4. 电磁跃迁选择定则

Wigner–Eckart 与宇称给出普适部分：

$$
|I_i-I_f|\le\lambda\le I_i+I_f,
$$
$$
E\lambda:\ p_f=p_i(-1)^\lambda,\qquad
M\lambda:\ p_f=p_i(-1)^{\lambda+1}.
$$

因此 E1 必须变宇称，M1 保持宇称，E2 保持宇称；$0\to0$ 的偶极跃迁禁戒。对本模型额外假定的主导矩阵元是：

| 通道 | toy 内禀矩阵元 | 典型选择 | 物理解释边界 |
|---|---|---|---|
| chiral-partner M1 | $\langle-\chi,p|\hat M1|\chi,p\rangle$ | $\Delta I=1$, 同宇称 | 与三轴手征伙伴的强 M1 相容；不是由“手征”单独保证 |
| parity-partner E1 | $\langle\chi,-p|\hat E1|\chi,p\rangle$ | $\Delta I=1$, 异宇称 | 八极混合/关联可增强；E1 连接不等于静态 $\beta_3$ |
| diagonal E2 crossover | $\langle\chi,p|\hat E2|\chi,p\rangle$ | $\Delta I=2$, 同宇称 | 同一投影序列的四极 crossover |
| chiral E2 crossover | $\langle-\chi,p|\hat E2|\chi,p\rangle$ | $\Delta I=2$, 同宇称 | 与 diagonal E2 的相位相干叠加，产生干涉强弱 |

脚本使用 $\Gamma_{X\lambda}\propto E_\gamma^{2\lambda+1}|A_{X\lambda}|^2$，并在 E2 中加入 $q_0+\chi q_\chi+p q_\pi+\chi p q_{\chi\pi}$ 的相干项；这只是显示选择定则和干涉的最小数值实现。真实 $B(X\lambda)$ 还需要具体波函数、Clebsch–Gordan 系数、内转换、寿命和 feeding 处理。

## Assumptions

1. $\tau$ 与 $\xi$ 是两个独立局域二态坐标，$t_\chi,t_\pi,t_{\chi\pi}$ 随自旋变化但不从具体核的 PES 或寿命反演。
2. $\gamma\approx30^\circ$ 只作为允许 aplanar 几何的背景窗口；本笔记不把它当实验测量。Guo 2020 的 `\gamma=27.1^\circ` 和 `\beta_3=0.05` 是模型输入（PDF p.5），Liu 2016 的 `\gamma=15.1^\circ/26.3^\circ` 也是组态相关计算输入（PDF p.3）。
3. E1 强通道被建模为同一 $\chi_s$、相反 $p$，M1 强通道为同一 $p$、相反 $\chi_s$；这是一种用于诊断的最小算符选择，不能替代完整 RAT-PRM/TPRM。
4. 脚本的自旋、隧穿参数、矩阵元和相对率均为 synthetic 输入；输出不构成任何核素的观测值。

## Competing Explanations

- `78Br` 的 E1 网络可能来自八极关联、组态混合或反射不对称耦合；Liu 2016 自身将 `f5/2-p3/2` mixing 作为 TPRM 偏差来源（PDF pp.3–4；`L16-7`, `L16-10`）。
- `134Pr` 的双带近简并可以与形状涨落、$\gamma$-phonon coupling 和配置混合共存；Tonev 2006 的寿命结果直接削弱静态手征极限（PDF pp.3–4；`TO06-D24-003`–`TO06-D24-005`）。
- `131Ba` D3–D6 的四带连接不能唯一分解成两对手征伙伴；D4/D5/D6 交叉和 D5 E1 feeding 模型偏差要求保留准粒子对齐与 Coriolis 混合（Guo 2020 PDF pp.4–5；`GU20-7`, `GU20-11`, `GU20-13`）。
- 相同宇称的 E2 交叉强度可能被带混合、相位约定和共同核芯四极矩改变；不能用一个 E2 比值反推唯一的三轴形状。

## Transfer Conditions

要把此 toy 框架转移到 `78Br` 或 `134Pr`，至少需要同一带组的逐线自旋宇称、偏振/混合比、partner-resolved 寿命、绝对 $B(E1)$、$B(M1)$、$B(E2)$、feeding 协方差，以及同一组态空间下同时含 $\gamma$、$\beta_3$ 和隧穿的 PRM/TAC/CDFT 计算。Wang 2023 明确把绝对跃迁概率和寿命视为强于能量/分支指纹的检验（PDF pp.10–13；`WC23-11`）。

## Failure Conditions

- 把 `78Br` 四条候选带直接写成已观测的四重简并；Liu 2016 只提出未来 quartet 可能性（PDF p.5；`L16-14`）。
- 把相反宇称 E1 连接写成稳定静态 `\beta_3>0` 的直接测量；Liu 2016 和 Guo 2020 都保留 softness/correlation 边界（`L16-13`, `GU20-14`）。
- 把 `\Delta I=1` M1 或 E1 的“强”当作群论必然性；强度依赖波函数、有效 $g$ 因子、八极混合和几何。
- 把 `s=pr` 的 simplex 本征值与签名指数 $\alpha$ 混用，或忽略奇奇核整数自旋与奇质量核半整数自旋的差异。
- 把 `134Pr` 的近简并和 `78Br` 的八条 E1 当作独立且充分的 static-chirality 证明，忽略 Tonev 2006 的寿命反证和 source lineage。

## Falsification or Reverse Tests

1. 对候选四重态作联合拟合：若单一 $t_\chi,t_\pi,t_{\chi\pi}$ 无法同时再现四带的 $\Delta E(I)$、E1/M1/E2 分支和相位，则四态张量积模型被否定或必须引入额外自由度。
2. 若 partner-resolved 绝对强度显示两条同宇称带的 $B(E2)$ 持续出现 `134Pr` 式 2–3 倍差异，且 M1 交错缺失，则静态手征伙伴解释应降级为动态手征/形状涨落（Tonev 2006 PDF pp.3–4）。
3. 若 E1 只在少数组态混合跃迁出现、随自旋不形成稳定异宇称网络，或反射不对称计算不需要非零 $\beta_3$ 即可重现，则“八极四重态”解释不再优于组态混合。
4. 若测得明显独立的第四条带但其 simplex/signature 组合与 $s=pr$ 预测不一致，应优先检查带号、轴约定和相位规范，而不是强行重标记。

## Open Questions

- `78Br` 是否存在逐自旋闭合的四带、partner-resolved lifetime 和绝对 E1/M1/E2 矩阵？Liu 2016 的八条 E1 与 softness 仍不足以回答。
- `134Pr` 的 Band 1/Band 2 能否在含八极坐标的统一 GCM/PRM 中重现寿命不对称，而不牺牲能谱和 $B(M1)$ 趋势？
- `131Ba` D3–D6 的 pseudospin splitting 与 chiral splitting 是否能用同一角动量投影和 mixing kernel 区分？Guo 2020 留下了几何和绝对强度缺口。
- 四重态中 $t_{\chi\pi}$ 是否能从同一自旋下两种宇称的手征劈裂差反演，还是被带混合和实验分辨率完全遮蔽？
- E2 crossover 干涉是否能通过线偏振、寿命和多级联共同确定相位，而非仅由分支比推断？

## Human Review

本页由 Codex 依据仓库中已摄入的 Liu 2016、Wang 2023、Guo 2020、Petrache 1996 和 Tonev 2006 source 页及其原文定位完成 self-audit；`review_status: unreviewed`，未写成 `human-reviewed`。需要用户裁决的重点是：四态 toy Hamiltonian 是否作为后续 PRM/GCM 的最小参数化起点，以及将 `\mathcal C=\mathcal T R_x(\pi)` 作为具体轴约定时的相位/反幺正规范。

## Promotion or Rejection History

- 2026-10-29：`supports` Liu 2016 提出的“单核手征—宇称 quartet 可观测性”研究方向；保留其 future-proposal 边界。
- 2026-10-29：`supports` Guo 2020 的正宇称四带流形与 E1 网络作为实验—模型前例；`limits` 其四带配对、几何和静态 `\beta_3` 结论。
- 2026-10-29：`revises` 把 signature/simplex、双重隧穿劈裂和 E1/M1/E2 四通道写成可计算的选择定则 toy 模型；不晋升为任何核素的定量拟合。
- 2026-10-29：`rejects` “近简并 + E1 = 已确证静态手征—八极四重态”这一过强命题，反证来自 `134Pr` 寿命和现有 `78Br`/`131Ba` 证据边界。
