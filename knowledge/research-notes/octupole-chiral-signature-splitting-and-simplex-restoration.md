---
type: research-note
title: "八极—手征复合核中旋称劈裂与单纯形恢复的动力学微观相互作用"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [octupole chiral signature splitting, simplex restoration in octupole nuclei]
tags: [octupole, chirality, signature-splitting, simplex-symmetry, high-spin]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: Day26 octupole-chiral signature-splitting and simplex-restoration investigation
evidence_sources: [frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, butler-nazarewicz-1996-intrinsic-reflection-asymmetry]
---

# 八极—手征复合核中旋称劈裂与单纯形恢复

## Research Trigger

本轮问题要求把三轴非共面转动、反射不对称八极自由度、高-$j$ 粒子对准和
旋称（signature）交错放入同一动力学框架，并为 `78Br`、`130Cs` 和 `133Ce`
提供可复现的机制诊断。直接目标是计算

$$
\Delta E_{\rm rot}(I)=E(I)-E(I-1)-\frac{I}{\mathcal J_{\rm eff}},
\qquad
S(I)=\frac{(-1)^{I+1}}{2I}[E(I)-E(I-1)]
$$

并跟踪八极双阱在自旋变化下的极小、势垒和单纯形扇区隧穿劈裂。这里的数值
输入是 synthetic；不反演任何一条实验能带。

## Grounded Evidence

Frauendorf 的综述把高自旋平均场写成旋转系 Routhian
$h'=h-\boldsymbol\omega\cdot\boldsymbol J$，并区分主轴、平面倾转和非平面
（手征）解；非平面左右解在实验室投影后可形成同宇称的近简并
$\Delta I=1$ 带。综述同时强调 TAC 是半经典几何，量子隧穿、角动量投影和
对称性恢复需要 PRM、投影或生成坐标等超越平均场方法
（[[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]，F01-4--F01-9，
PDF pp.467--485）。反射不对称平均场的八极矩、E1/E3 和宇称伙伴是对称性
破缺的响应，却不能单独证明稳定的静态八极极小（同页 F01-13，PDF
pp.495--498）。

Butler--Nazarewicz 的综述将内禀反射不对称处理为八极自由度、宇称投影和
集体涨落问题；其适用边界是平均场的局域 $±\beta_3$ 解需要投影或 GCM 才能
与实验宇称态对应（[[butler-nazarewicz-1996-intrinsic-reflection-asymmetry]]，
具体页码和 claim locator 仍需回到原件核验）。

Wiki 中的 `78Br`、`134Pr` 和 `131Ba` 先例只支持研究动机和条件性模型：
`78Br` 有手征候选双带与 E1 网络，但八极势面被报道为软性；`134Pr` 的近简并
带有寿命不对称，不能只由静态手征解释；`131Ba` 的 RAT-PRM 采用
$\gamma\approx27^\circ$、$\beta_3=0.05$ 作为模型输入，而非直接形变测量。
`131Ba/133Ce` 的 $g_{7/2}$ 强耦合带说明 signature splitting 同时受非轴性、
近邻低-$j$ 轨道和 Coriolis 混合控制，不能把 $S(I)$ 单独当作 $\gamma$ 的测量。

## Provisional Reasoning

### 1. 复合离散对称性与表示分类

先纠正题目中的一个代数前提。空间宇称是中心元，故

$$
[\hat P,\hat R_x(\pi)]=0,
\qquad
\hat S_x=\hat P\hat R_x^{-1}(\pi),
\qquad
[\hat R_x(\pi),\hat S_x]=0.
$$

在固定自旋 $I$ 的 SU(2) 表示中

$$
\hat R_x(\pi)^2=(-1)^{2I}.
$$

奇奇核的整数 $I$ 给出 $r=\pm1$，奇质量核的半整数 $I$ 给出
$r=\pm i$。若 $p=\pm1$ 是宇称本征值，则

$$
s_x=p r^{-1}
$$

是单纯形本征值。因此仅由 $P$、$R_x$ 和 $S_x$ 得到的是可约的
$\mathbb Z_2^P\times C_4^R$（整数自旋时按中心元约化），不是非对易拓扑。
反幺正手征操作（例如含时间反演的轴变换）可以引入反线性相位和项目表示，
但它不是 $[R_x,S_x]$ 的非零结果，必须单独声明轴、时间反演平方和相位规范。

四态基底来自两个独立的局域交换坐标，而非来自上述三个算符的非对易：

$$
\{|L,+\rangle,|R,+\rangle,|L,-\rangle,|R,-\rangle\}
\cong \mathbb C^2_{\chi}\otimes\mathbb C^2_{\beta_3}.
$$

取 $C_\chi=\tau_x$ 交换左右手性，取 $P_{\beta_3}=\xi_x$ 交换
$+\beta_3$ 与 $-\beta_3$ 局域井。两者对易，故可同时对角化为
$(\chi_s,p_3)=(\pm1,\pm1)$ 四个扇区。最小固定自旋 Hamiltonian 为

$$
H_I=E_0(I)\mathbf1-t_\chi(I)\tau_x-t_3(I)\xi_x
          -t_{\chi3}(I)\tau_x\xi_x,
$$

其能量

$$
E_I(\chi_s,p_3)=E_0(I)-\chi_s t_\chi-p_3t_3-\chi_s p_3t_{\chi3}.
$$

$t_{\chi3}$ 是手性隧穿和八极隧穿的最低阶耦合；它使不同宇称扇区的
手征劈裂不相同。真实核中这四态是近似局域基底，不能把 $L/R$ 当作可直接
测量的量子数。

### 2. 高-$j$ Coriolis 对准与双重调制

三轴粒子—转子 Hamiltonian 的交叉项为

$$
H_C=-\sum_{k=1}^3\frac{I_kj_k}{\mathcal J_k},
$$

其中 $\mathcal J_1\ne\mathcal J_2\ne\mathcal J_3$。对于高-$j$ 粒子，
$j_\perp=\sqrt{j(j+1)-K^2}$，并令 $\omega_I\simeq(I+1/2)/\mathcal J_{\rm eff}$。
把三轴、八极和 Coriolis 振幅写成

$$
V_{p}(I)=V_{\rm tri}\sin3\gamma+pV_3\beta_3
 -c\,\omega_Ij_\perp\cos(\phi_0+p\phi_3),
$$

则 $p=+1$ 和 $p=-1$ 的 Coriolis 项相对相位相反。一个两分支诊断谱为

$$
E_{p,s}(I)=\frac{I(I+1)}{2\mathcal J_{\rm eff}}
 +p\frac{\Delta_\pi}{2}+sV_p(I),\qquad s=\pm1.
$$

当 $|V_C|\ll|V_{\rm tri}\pm V_3\beta_3|$ 时，两宇称的 $S(I)$ 图样近似平滑；
当 $|V_C|$ 与两项相当时，正、负宇称分支对相位的响应不同，出现手征振动区
到静态手征区的分岔。这里“分岔”是有限模型的能量响应分岔，不是由能谱单独
证明静态手征。`ding-2021-131ba-133ce-signature-splitting` 的实验—模型边界
正是这种 $\gamma$、低-$j$ Coriolis 混合和组态依赖的非唯一性。

### 3. 离心八极双阱与单纯形极限

令八极集体坐标为 $q\propto\beta_3$：

$$
V_I(q)=a(I)q^2+bq^4,
\qquad
a(I)=a_0-\eta\frac{I(I+1)}{I_s^2}.
$$

该符号来自 $\mathcal J(q)\simeq\mathcal J_0(1+\kappa q^2)$ 的展开：若
$\kappa>0$，转动能降低 $q^2$ 系数并加深八极双阱；若 $\kappa<0$，则把极小
推回 $q=0$。在 $a<0$ 时

$$
q_0=\sqrt{-a/(2b)},\qquad
V_b=\frac{a^2}{4b}\propto|I-I_c|^2.
$$

因此深阱侧的 WKB 隧穿劈裂可写成诊断形式

$$
\Delta_s\sim\hbar\omega_q\exp[-2\mathcal S],
\qquad
\mathcal S\approx\pi V_b/(\hbar\omega_q).
$$

当离心项加深双阱时，$\Delta_s\to0$ 是指数抑制，表示两个 simplex/parity
投影态近简并；其标度不是幂律，势垒本身的临界指数为 2。若离心项令
$a\to0^-$，则 $q_0\propto|I-I_c|^{1/2}$，这是平均场的 simplex-breaking
序参量恢复，然而局域谐振能隙一般趋向有限的 $\hbar\omega_q$，不会自动趋零。
因此“单纯形恢复”和“单纯形能隙趋零”是两个不同极限，不能在同一句话中
当作同义命题。

## Assumptions

1. $\mathcal J_k$、$\beta_3$、$j$ 和相位均为示意参数；脚本没有拟合 `78Br`、
   `130Cs` 或 `133Ce` 的数据。
2. $S_x=P R_x^{-1}(\pi)$ 是只有在 Hamiltonian 保持该复合操作时才是好量子数。
   反射不对称平均场可破缺 $P$，实验室宇称仍需投影。
3. $S(I)$ 使用整数自旋约定；半整数核应改用相应的交错相位和
   $r=\pm i$ 标记。
4. WKB gap 是四次势的指数代理，不是自洽 ATDHFB/GCM 惯量计算。
5. `delta_E_rot` 以 $\mathcal J_{\rm eff}$ 给出的刚性转动基线扣除，不能直接
   视为实验 recoil correction。

## Competing Explanations

- 旋称劈裂可以由三轴惯量、近邻低-$j$ 轨道、配对阻塞、组态交叉或单纯
  Coriolis attenuation 产生，不需要八极自由度。
- 异宇称 E1 网络可来自组态混合、八极声子或局域反射不对称，不能单独证明
  稳定 $\beta_3\ne0$。
- 近简并手征伙伴也可能是动态手征振动、$\gamma$-soft 涨落或带混合；绝对
  寿命、$B(M1)/B(E2)$、偏振和对齐信息才可能区分这些解释。
- “非对易拓扑”若实际指含时间反演的手征反幺正操作，应在具体 PRM/TAC
  表示中重新计算其项目相位；不能从 $P R_x^{-1}$ 的符号顺序推断。

## Transfer Conditions

转移到具体核至少需要逐自旋的带标签、宇称和 signature、绝对或相对寿命、
$B(E1)$/$B(M1)$/$B(E2)$、偏振/混合比、alignment，以及同一组态空间中同时
改变 $\gamma$、$\beta_3$、配对和 Coriolis attenuation 的 PRM、TAC 或
CDFT/GCM 计算。模型必须同时拟合能量和电磁矩阵元，不能只拟合 $S(I)$。

## Failure Conditions

- 把 $[R_x,S]\ne0$ 当作标准宇称—旋称代数的定理。
- 把四态 toy 基底写成 `78Br` 已实验确证的四重态。
- 把 $\Delta_s\to0$、$q_0\to0$ 和静态八极恢复混为同一极限。
- 把 Coriolis 干涉的 synthetic 分支数值报告为实测的 keV 劈裂。
- 忽略奇奇核整数自旋与奇质量核半整数自旋的 signature/simplex 本征值差异。

## Falsification or Reverse Tests

1. 用同一组态空间同时拟合两种宇称的 $S(I)$、partner-resolved $B(E2)$、
   $B(M1)$ 和 $B(E1)$；若必须为每个分支独立调相位，双调制模型失效。
2. 在 $\beta_3=0$、$t_{\chi3}=0$ 和 Coriolis attenuation 三个退化极限分别
   重跑脚本；若仍出现所谓八极特有分岔，则解释是模型实现伪影。
3. 对 $a(I)$ 改变符号扫描；验证深阱侧 $\log\Delta_s$ 与势垒/谐振能的
   指数关系，以及恢复侧 $q_0\propto|I-I_c|^{1/2}$。
4. 以半整数 $I$ 重新构造 $r=\pm i$ 和 $s=pr^{-1}$；若把 simplex 标签错误地
   保持为 $\pm1$，则分类失败。

## Open Questions

- `78Br` 是否存在逐自旋闭合的正负宇称四带、绝对 E1/M1/E2 和 partner-resolved
  寿命？
- `130Cs` 的旋称反转与三轴—八极耦合是否可由同一组态的 TAC/PRM 统一描述？
- `133Ce` 的半整数 simplex 标记和 `131Ba` 的整数 signature splitting 能否
  在同一投影规范下比较？
- 旋称劈裂、宇称劈裂和电磁矩阵元是否足以反演 $t_{\chi3}$，还是存在带混合
  导致的不可辨识谷？
- 含八极坐标的自洽 GCM 是否会把脚本中的幂律/指数标度显著重整化？

## Human Review

本页为 Codex self-audit 草稿，`review_status: unreviewed`。需要人工重点核对：
Frauendorf 2001 和 Butler--Nazarewicz 1996 原文的精确 locator；具体核素的
四态证据边界；以及含时间反演的手征反幺正操作在所选 SU(2) 相位规范下的
平方和项目表示。脚本输出仅作为模型审计工件，不作为实验数据源。

## Promotion or Rejection History

- 2026-10-29：保留“手性与八极双阱的张量积四态”作为条件性 toy 模型；不晋升
  为任何核素的实验四重态。
- 2026-10-29：拒绝“$P$、$R_x(\pi)$ 与 $S$ 必然非对易”的前提；标准空间群
  代数给出对易，非平凡反幺正项目结构需额外定义。
- 2026-10-29：保留 Coriolis 正负宇称反相干涉和双阱两种离心响应作为可检验
  机制假设；不把参数扫描当作微观自洽计算。

## Reproducible Worktree

脚本、CSV、JSON 和图表位于
`outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/octupole-chiral-simplex/`。
运行 `python3 octupole_chiral_simplex_model.py` 可重建全部工件。
