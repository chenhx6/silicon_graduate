---
type: research-note
title: "奇 A 锕系宇称双重态直接 E3 跃迁的微观角动量耦合"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [odd-A actinide direct E3 angular coupling, 奇A锕系直接电八极跃迁, parity-doublet E3 geometry]
tags: [actinides, parity-doublets, be3, octupole-transitions, angular-coupling]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: Day26 directed study of odd-A actinide parity-doublet direct E3 transitions
evidence_sources: [butler-nazarewicz-1996-intrinsic-reflection-asymmetry, gaffney-2013-pear-shaped-rn-ra, nndc-2009-ra225-adopted-parity-doublet, nndc-2022-ac225-adopted-parity-doublet, nndc-2001-223ra-reference-and-2026-intensity-records]
---

# 奇 A 锕系宇称双重态直接 E3 跃迁的微观角动量耦合

## Research Trigger

本笔记研究轻锕系奇 A 核中相反宇称带之间的直接电八极跃迁
$B(E3;I_i^{\pi_i}\to I_f^{-\pi_i})$。目标是把反射不对称内禀八极矩、转动波函数的 Clebsch–Gordan（CG）几何因子、$K=1/2$ 的退耦干涉和高自旋 Coriolis 混合放在同一可复现框架中，并对照 $^{225}$Ra、$^{223}$Ra 与 $^{225,227}$Ac 的现有谱学证据。

这里必须先划定证据层：Butler–Nazarewicz 综述给出反射不对称、E1/E3 和奇 A 转动的理论框架；Gaffney 等给出偶偶 $^{220}$Rn/$^{224}$Ra 的直接 E1/E2/E3 矩阵元；ENSDF 给出 $^{225}$Ra/$^{225}$Ac 的评价能级与 E1。当前本地来源没有为奇 A 锕系建立绝对直接 E3 寿命/分支账本，因此本页的奇 A E3 网络是条件性强耦合模型结果，不是已发表奇 A 直接 $B(E3)$ 的替代品。

## Grounded Evidence

### 反射不对称与八极矩

Butler–Nazarewicz 的综述区分静态反射不对称、八极振动/软度、宇称投影和 E1/E3 观测。反射不对称平均场具有非零内禀 $Q_{30}$，而实验室宇称本征态仍需宇称与角动量恢复。轴向内禀坐标中保留 $\mu=0$ 分量时，电八极算符写为

$$
\mathcal M(E3,\mu)=\sqrt{\frac{7}{16\pi}}\,eQ_{30}D^{3*}_{\mu0}(\Omega).
$$

这一定义是算符约定；$Q_{30}$ 的符号依赖内禀 $\beta_3$ 相位，不能从单条实验 $B(E3)$ 取得。综述同时强调 E1 对质子—中子偶极相消敏感，E3 通常更接近集体八极探针，但单条 E3 仍不能排他地区分静态梨形与大振幅八极振动。[Butler–Nazarewicz 1996](../sources/butler-nazarewicz-1996-intrinsic-reflection-asymmetry.md)

Gaffney 等对偶偶 $^{220}$Rn/$^{224}$Ra 的库仑激发取得多条 E1/E2/E3 矩阵元；$^{224}$Ra 的 $Q_3$ 和 E3 图样比 $^{220}$Rn 更连贯，作者同时保留静态投影态与四极形状上的八极振动之间的边界。这个偶偶核结果可作为奇 A 粒子—核芯模型的核芯尺度参照，不能直接当作奇 A 的 $B(E3)$。[Gaffney 2013](../sources/gaffney-2013-pear-shaped-rn-ra.md)

### 奇 A 能级与分支约束

评价 $^{225}$Ra 的低能带包含 $K=1/2^+$ 的 $1/2^+,5/2^+,3/2^+,7/2^+$ 和 $K=1/2^-$ 的 $3/2^-,1/2^-,7/2^-,5/2^-$。同自旋 A/B 中心差 $E_- - E_+$ 为 $+55.16,-11.21,+94.95,-42.24$ keV（$I=1/2,3/2,5/2,7/2$）；31.50-keV $3/2^-→1/2^+$ E1 的评价强度为 $B(E1)=0.00081(20)$ W.u.。其中负宇称自旋部分带括号，数值是评价对象而非本轮重读原实验计数。[225Ra ENSDF](../sources/nndc-2009-ra225-adopted-parity-doublet.md)

$^{225}$Ac 评价对象有 $3/2^-$ 基态、40.10-keV $3/2^+$ 伙伴和 40.09-keV E1，$B(E1)=0.00171(15)$ W.u.；但 $5/2$、$7/2$、$9/2$ 在多个带中重复出现，不能从能量窗自动定义唯一的宇称双重态序列。因而 $^{225}$Ac 的 $K=3/2$ 只适合检验“无一阶 $K=1/2$ 退耦项”的代数边界，不足以提供本页直接 E3 的实验归一。[225Ac ENSDF](../sources/nndc-2022-ac225-adopted-parity-doublet.md)

$^{223}$Ra 的评价/原实验链记录 $3/2^+$ 基态、约 50.128-keV $3/2^-$ E1 伙伴和 $B(E1)=0.00119(16)$ W.u.；角关联工作还显示多重放置、转换系数和混合比符号不能仅按 $E_\gamma$ 唯一恢复。故 $^{223}$Ra 可约束能级与 E1 分支层，不能被本工件写成已测奇 A $B(E3)$。[223Ra 官方记录](../sources/nndc-2001-223ra-reference-and-2026-intensity-records.md)；[Jones et al. 1998](../sources/jones-1998-ra223-alpha-gamma-correlations.md)

## Provisional Reasoning

### 1. 转动展开与矩阵元

取轴对称强耦合转动波函数（省略规范化相位）

$$
|IMK\rangle=\sqrt{\frac{2I+1}{16\pi^2}}
\left[D^{I*}_{MK}|\phi_K\rangle+(-1)^{I+K}D^{I*}_{M,-K}|\phi_{-K}\rangle\right].
$$

八极算符的 $D^{3*}_{\mu0}$ 分量给出 $\Delta K=0$ 的轴向几何项。对同一奇核子内禀组态的相反宇称投影，并采用本页的 reduced-matrix-element 顺序约定，可得

$$
\begin{aligned}
\langle I_iK\pi\Vert\mathcal M(E3)\Vert I_fK{-\pi}\rangle
={}&\sqrt{2I_i+1}\,\langle I_iK\;3\,0\mid I_fK\rangle\\
&\times\sqrt{\frac{7}{16\pi}}eQ_{30}
\left[1+(-1)^{I_f+1/2}p_{\rm oct}\,\delta_{K,1/2}\right].
\end{aligned}
$$

这里 $p_{\rm oct}=\pm1$ 是固定内禀相位约定下的八极反射/退耦标签。按照同一约定

$$
B(E3;I_i\to I_f)=\frac{\left|\langle I_iK\pi\Vert\mathcal M(E3)\Vert I_fK{-\pi}\rangle\right|^2}{2I_i+1}.
$$

因此网络的基础量为

$$
B(E3)=\frac{7}{16\pi}e^2Q_{30}^2
\left|\langle I_iK\;3\,0\mid I_fK\rangle\right|^2F_K(I_f,p_{\rm oct})^2,
$$

其中 $F_K=1+(-1)^{I_f+1/2}p_{\rm oct}$（$K=1/2$），而 $F_K=1$（$K>1/2$）。电八极跃迁改变宇称，三角条件允许 $\Delta I=0,\pm1,\pm2,\pm3$，但具体 CG 系数可能使某条支线为零。$\Delta I=\pm3$ 的角几何不能被笼统写成相等；固定 $I_i$ 的 $K=1/2$ 干涉因子对两方向相同，方向比首先由 CG 系数决定。

### 2. $K=1/2$ 退耦与交错

当 $K=1/2$ 时，$K\leftrightarrow-K$ 只相隔一个单位，Coriolis 算符 $-(I_+j_-+I_-j_+)/(2\mathcal J)$ 可在一阶连接两镜像分量。于是 $F_K$ 随 $I_f+1/2$ 奇偶交替。理想标签下，一支 $p_{\rm oct}$ 使偶数次幂相消（$F=0$），另一支使其相干相加（$F=2$），相对于无干涉强度分别是 0 与 4；实际波函数混合会把零抬高为有限值。这个“剧烈交错”是相位相干和 CG 几何的乘积，不等于每个实验核都具有精确零强度。

对 $\Delta I=+3$ 与 $-3$，同一 $I_i$ 的 $F_K^2$ 相同，故 $K=1/2$ 项本身不产生方向不对称；脚本的 `delta3_direction_comparison.csv` 给出 CG² 比值。例如 $I_i=7/2$、$K=1/2$ 时，$|C_{+3}|^2/|C_{-3}|^2=2.8555$，$I_i=11/2$ 时为 1.7560，并随自旋向高自旋趋近 1。若实验将 $+3$ 和 $-3$ 支线的显著差异归因于退耦项，必须同时核对初态简并、能量五次方/八次方的计数约定、带混合与相位选择；单靠 $F_K$ 不能解释同一初态两方向的 CG 比。

### 3. Coriolis 非绝热重整

有限转动频率下，$H_C$ 会把目标 $K$ 与 $K\pm1$ 组态混合。用 $a_{K\to K'}(I)$ 表示一阶混合振幅，E3 振幅应写为

$$
M_{fi}=\sum_{K_iK_f}c^{(f)*}_{K_f}(I_f)c^{(i)}_{K_i}(I_i)
\,C(I_iK_i\;3\,0\mid I_fK_f)\,m_3Q_{K_iK_f},
$$

并保留不同 $K$ 通道的相对相位。二阶修正进入能量和强度：$\delta E_I\sim\sum_{K'\ne K}|H_C|^2/(E_K-E_{K'})$，而强度含有与主通道相干的 $2\operatorname{Re}(M_0^*\delta M)$。在高自旋，$I_\pm$ 矩阵元增大、带交叉和配对削弱使这一重整可能达到与静态 $Q_{30}$ 变化同量级。因而应逐自旋拟合 E3 分支、E1/E2 竞争、带交叉和寿命，不能仅以低自旋 $Q_{30}$ 固定外推。

现有 $^{225}$Ra 评价的交错 A/B 能级差与 31.50-keV E1 证明了一个适合检验 Coriolis/宇称投影的谱学环境；它没有给出直接 E3 寿命。$^{223}$Ra 的多重放置与未定混合比符号进一步说明，分支比必须保留内转换和 placement 语义。$^{225}$Ac 的 $K=3/2$ 对照显示一阶对角 $K=1/2$ 退耦项不适用，但二阶跨 $K$ 混合仍可存在。

## Assumptions

- 内禀核芯采用轴向反射不对称的单一 $Q_{30}$，并用宇称投影恢复实验室宇称。
- 主跃迁满足 $\Delta K=0$；跨 $K$ 的 Coriolis 项只作为非绝热重整的条件讨论。
- reduced matrix element、$B(E3)$ 初态简并和 CG 相位都按本页公式统一；不同文献的 bra–ket 顺序不能直接拼接。
- 工件采用 $Q_{30}=1000\ e\,\mathrm{fm}^3$ 的演示输入；这不是 $^{223,225}$Ra 或 $^{225,227}$Ac 的测量值。
- $p_{\rm oct}$ 是相位标签，不是独立可观测量；相位变换必须同时变换内禀态和算符。

## Competing Explanations

1. **静态反射不对称**：稳定的 $\pm\beta_3$ 双阱产生相干 E3、低宇称劈裂和较平滑的 $Q_3$。
2. **八极振动/软度**：宇称投影态可有强 E3，但 $\langle\beta_3\rangle$ 不必非零；能量、带间强度和高阶矩会随自旋变化。
3. **奇粒子组态混合**：邻近 $K$ 轨道、阻塞和带交叉可产生交错能级与 E3 强度重排，不要求静态梨形。
4. **偶然近简并或 placement 混淆**：评价 Jπ 带括号、多重放置和未测寿命会模拟双重态或异常分支。

## Transfer Conditions

CG 几何、$B(E3)$ 的初态简并因子和 $K=1/2$ 退耦结构可迁移到其它轴对称奇 A 核；需要重新输入每个核的 $K$、相位、带归属、$Q_{30}$、转动惯量和邻近组态。偶偶核的直接 E3 只可作为核芯参照。跨核比较必须统一 $e\,\mathrm{fm}^3$ 与 W.u.、跃迁方向、内转换和寿命归一，不能把评价 E1 当作直接 E3 证据。

## Failure Conditions

- 核心组态不是单一 $K$，或三轴性与强带交叉使 $K$ 不守恒时，单通道公式不足。
- 将 `p_oct` 的相位标签当作测得的八极矩符号，或把 $F=0$ 当作所有真实核的严格禁戒，会夸大交错。
- 不区分 $B(E3;I_i\to I_f)$ 与反向方向，或把不同初态的矩阵元平方相加，会破坏简并因子和闭合关系。
- 以 $^{225}$Ra/$^{223}$Ra 的 E1 评价值、偶偶 $^{224}$Ra 的 E3 或模型 $Q_{30}$ 冒充奇 A 锕系直接 E3 测量。

## Falsification or Reverse Tests

1. 对同一奇 A 核测量相反宇称带的逐线寿命、分支、内转换与多极性，检查 CG²、$F_K^2$ 和高自旋剩余是否同时成立。
2. 以完整粒子—转子 Hamiltonian 加入 $K\pm1$ 通道，比较 $H_C=0$ 与有限 $H_C$ 的 E3 网络；若无法同时重现能级交错和 E3 交替，单一退耦解释应降级。
3. 对 $K=3/2$ 对照核检查是否仍出现 $(-1)^{I+1/2}$ 的一阶模式；若出现，应寻找组态混合、三轴性或带标记错误。
4. 释放 GOSIA/库仑激发拟合中的星号耦合和协方差，检验由偶偶核推定的静态 $Q_3$ 是否保持；若不保持，不能把恒定 $Q_3$ 作为刚性证据。

## Open Questions

- $^{225}$Ra 和 $^{223}$Ra 是否存在可归属于同一宇称双重带的绝对 E3 寿命和高自旋分支？
- $^{225,227}$Ac 的 $K$ 组态、阻塞平均场和跨 $K$ Coriolis 混合能否在同一投影 GCM 或 blocked QRPA 中计算？
- 实验上如何从 E3/E1/E2 联合网络区分静态梨形、八极软振动和奇粒子组态混合？
- 高自旋的 $\Delta I=+3/-3$ 方向比是否受未观测分支、内转换和初态布居影响到足以遮蔽 CG 几何？

## Human Review

本页为 Codex source self-audit 形成的 AI 草稿，`review_status: unreviewed`。优先人工复核 reduced-matrix-element 的 bra–ket 约定、$K=1/2$ 相位规范、奇 A 直接 E3 原始实验来源和 $^{223}$Ra 多重放置/混合比的逐线 provenance；未将模型网络写成 `human-reviewed`。

## Promotion or Rejection History

- 2026-10-29：创建 provisional research note；建立 $Q_{30}$、CG、$K=1/2$ 干涉和 Coriolis 非绝热重整的统一计算合同。
- 2026-10-29：保留奇 A 直接 E3 实验缺口；拒绝把 $^{225}$Ra/$^{223}$Ra E1 或偶偶 $^{224}$Ra E3 当作奇 A $B(E3)$ 的直接测量。

## Reproducibility

可复现目录：`outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/actinide-direct-e3/`。

- `direct_e3_angular_coupling.py`：无外部 Python 包依赖的 CG、E3 网络和 $K=1/2$ 曲线计算；
- `direct_e3_network.csv`：$^{223,225}$Ra、$^{225,227}$Ac、$K=1/2$ 与 $K=3/2$ 的转移网络；
- `cg_geometry_matrix.csv`：CG 与 CG² 矩阵；
- `delta3_direction_comparison.csv`：$\Delta I=+3/-3$ 方向几何比；
- `khalf_interference_curve.csv`：交错干涉因子；
- `direct_e3_results.json`：参数、证据边界和全部结果。

运行命令：

```bash
python3 direct_e3_angular_coupling.py
```
