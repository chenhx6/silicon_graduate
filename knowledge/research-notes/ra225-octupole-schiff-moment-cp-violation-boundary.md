---
type: research-note
title: "225Ra 与 223Ra 八极增强 Schiff 矩：T/P（CP）破坏机制与证据边界"
aliases: [ra225-octupole-schiff-moment-cp-violation-boundary]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [dobaczewski-2005-ra225-schiff, engel-2003-ra225-selfconsistent-schiff, nndc-2009-ra225-adopted-parity-doublet, nndc-2001-223ra-reference-and-2026-intensity-records, gaffney-2013-pear-shaped-rn-ra]
created_from: Day26 Ra225 octupole Schiff moment and CP violation study
promotion_target: octupole-correlation
tags: [225Ra, 223Ra, octupole, Schiff-moment, EDM, CP-violation, parity-doublet, model-sensitivity]
---

# 225Ra 与 223Ra 八极增强 Schiff 矩：T/P（CP）破坏机制与证据边界

## Research Trigger

本轮任务要求解释轻锕系 `225Ra (Z=88,N=137)` 与 `223Ra (N=135)` 中八极形变、宇称双重态和原子 EDM 灵敏度之间的微观链条，并给出可复现的能级分母与模型敏感性计算。重点是区分：核结构实验事实、PT-odd 模型结果、均匀密度几何估算和本笔记的推断。

## Grounded Evidence

### 1. 直接理论原件：一阶 PT 混合与 55 keV 分母

Dobaczewski–Engel, *Phys. Rev. Lett.* **94**, 232502 (2005), DOI `10.1103/PhysRevLett.94.232502`，原件 `raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/2005-dobaczewski-ra225-schiff.pdf`（PDF p.2，Eqs. (1)–(5)）给出

$$
S=\sum_{i\ne0}\frac{\langle\Psi_0|\hat S_z|\Psi_i\rangle\langle\Psi_i|\hat V_{PT}|\Psi_0\rangle}{E_0-E_i}+c.c.,
$$

其中 $\hat V_{PT}$ 同时破坏 P、T；$\hat S_z$ 是被原子电子屏蔽后仍能诱导原子 EDM 的核 Schiff 算符。论文指出 `225Ra` 的 `|1/2−⟩` 态约在 55 keV，因小分母主导求和；刚性内禀态近似下，PDF p.2 Eq. (4) 写成

$$
S\simeq-\frac{2}{3}\frac{\langle \hat S_z\rangle_{\rm intr}\langle \hat V_{PT}\rangle_{\rm intr}}{55\ {
m keV}}.
$$

这不是“55 keV 单独制造全部增强”：分子同时含集体 Schiff 矩和奇核自旋敏感的 $V_{PT}$ 矩阵元。

同一论文 PDF p.2 Eq. (2) 的常用点质子、有限核尺寸约定是

$$
\hat S_z=\frac e{10}\sum_{p=1}^Z\left(r_p^2-\frac53\langle r^2_{\rm ch}\rangle\right)z_p,
$$

即单位为 $e\,\mathrm{fm}^3$。写成球向量分量时包含 $[r^3-(5/3)\langle r^2\rangle_{\rm ch}r]Y_{1q}$。含显式质子/中子质心修正的形式与上述式子取决于坐标和密度约定，不能在未说明约定时把系数直接互换。

### 2. 225Ra 的核数据与八极形变

NNDC 225088001 Adopted 数据在 [225Ra source page](../sources/nndc-2009-ra225-adopted-parity-doublet.md:43) 的 NR225-1 记录 `1/2+` 基态与 `1/2−` 的 `55.16(6) keV` 伙伴；同表的 `31.56(3) keV` 态是 `3/2−`，不能代入 J=1/2 的旋转标量 $V_{PT}$ 分母。此处是评价数据，不等于新实验原始计数。

Engel *et al.*, *Phys. Rev. C* **68**, 025501 (2003), DOI `10.1103/PhysRevC.68.025501`，原件 `raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/2003-engel-ra225-schiff.pdf`：

| 原件定位 | 直接报告 | 证据层 |
| --- | --- | --- |
| PDF p.2 Eq. (2), p.2 Eq. (3) | 一阶 PT 响应和 Schiff 算符；225Ra 的同 J 伙伴能隙取 55 keV | 模型公式 |
| PDF p.4 Fig. 3 | 偶数 Ra 链中 $\beta_3$、$D_0$、内禀 $\langle S_z\rangle$ 的 Skyrme 预测 | 模型结果 |
| PDF p.6 | SkO′ 对 225Ra 给出 $\beta_2=0.190,\ \beta_3=0.146,\ \beta_4=0.136$ | 模型结果 |
| PDF p.8 Table I | SkO′、SIII、SkM*、SLy4 的内禀 $\langle S_z\rangle$ 和自旋/密度算符平均值；SkO′ 行 $\langle S_z\rangle=41.7\ e\,\mathrm{fm}^3$ | 模型结果 |
| PDF p.9 | 自洽计算相对早期粒子-转子估算通常小 1.5–3 倍；有限程、交换、投影和 T-odd 项仍是限制 | 模型限制 |

### 3. 223Ra 的对应能隙和八极证据

NNDC `223088001,223RA ADOPTED LEVELS, GAMMAS` 的固定栏原件 `raw/data/gpt/day16-20261018/ra223-adopted-691b1924ddb4.ens` 在 source page [N223 records](../sources/nndc-2001-223ra-reference-and-2026-intensity-records.md:43) 所记录的行号中给出：

- L48–58：`0.0 keV, 3/2+` 基态，且激光谱学与含八极形变的磁矩解释被记录在评价注释中；
- L89–106：`50.128(9) keV, 3/2−`，有 E1 到 `3/2+`，评价给 `B(E1)=0.00119(16) W.u.`（该量是评价跃迁强度，不是 Schiff 矩）；
- 原件注释 L9–18：记录 K=3/2、5/2、1/2 的宇称双重带、约 100 倍于其它 E1 的双重带内 E1、相近磁矩和八极形变解释。

因此 `223Ra` 可用同 J `3/2−` 的 `50.128 keV` 做分母尺度；不能把 223Ra 的 E1 强度直接等同于 PT-odd Schiff 响应，也不能把评价注释升级为新的静态形变测量。

### 4. 原子 EDM 实验层

Parker *et al.*, *Phys. Rev. Lett.* **114**, 233002 (2015), DOI `10.1103/PhysRevLett.114.233002`，开放原件 `tmp/ra225-schiff-external/parker2015-arxiv.pdf`（arXiv:1504.07477v2，PDF p.1 摘要和引言）报告首次 225Ra 原子 EDM 原理验证，95% C.L. 上限 `|d(225Ra)|<5.0×10^-22 e cm`；引言同时说核结构计算结合原子结构给出相对 199Hg 的 `2–3` 个数量级预期增强。它是原子实验限值，不是核 Schiff 矩的直接测量。

Bishof *et al.*, *Phys. Rev. C* **94**, 025501 (2016), DOI `10.1103/PhysRevC.94.025501`，开放原件 `tmp/ra225-schiff-external/bishof2016-arxiv.pdf`（arXiv:1606.04931v1，PDF p.1 摘要/引言，p.2 和 p.8 Eq. (3)）把上限改进到 `1.4×10^-23 e cm`（95% C.L.，约 36 倍改进），并把八极形变相对 199Hg 的预期提升表述为超过两个数量级。实验读出的是原子自旋进动相位，不能单独反演核内 $S$、$\bar g_0$、$\bar g_1$、$\bar g_2$。

## Provisional Reasoning

### 微观增强链

1. **P、T/CP 结构**：在 CPT 假设下，永久 EDM 同时破坏 P 和 T，等价地指向 CP 破坏。$\hat S_z$ 本身是 P-odd、T-even 的电荷算符；T 破缺来自 $V_{PT}$，不能把算符本身称为 T-odd。
2. **宇称混合**：$V_{PT}$ 为旋转标量时，中间态必须与基态同 J、异宇称。225Ra 用 `1/2−, 55.16 keV`；223Ra 用 `3/2−, 50.128 keV`。错误使用 225Ra 的 `31.56-keV, 3/2−` 会违反选择规则。
3. **集体分子**：八极形变使同一内禀态的正、负宇称投影具有大的 $\langle +|S_z|−\rangle$；四极—八极耦合和质心修正使其尺度近似正比于 $e ZR^3\beta_2\beta_3$。
4. **奇核 PT 矩阵元**：$\langle V_{PT}\rangle$ 取决于末粒子轨道、核芯极化、交换、有限程、短程关联及 T-odd EDF 项。它不是由 `β3` 或 E3 强度唯一决定。
5. **原子层**：$d_{\rm atom}=k_S S_{\rm lab}$，其中 $k_S$ 由电子结构决定；Dobaczewski–Engel 2005 引述 Ra/Hg 电子结构额外约 3 倍，但这不是核理论普适常数。

### β2β3 几何推导与约定

在均匀尖锐表面

$$R(\theta)=R_0[1+\beta_1Y_{10}+\beta_2Y_{20}+\beta_3Y_{30}],$$

并令质心为零，保留 $\beta_2\beta_3$ 阶，归一化球谐给出

$$\beta_1\sqrt{4\pi/3}+\frac9{\sqrt{35}}\beta_2\beta_3=0,$$
$$S_{\rm intr}=\frac9{20\pi\sqrt{35}}eZR_0^3\beta_2\beta_3+O(\beta^3).$$

文献/任务中常见的简写 `3/(20π) e Z R0^3 β2β3` 对应另一种表面多极归一化。脚本同时输出两个约定，避免把约 `1.97` 的系数差误判为理论不确定度。用 Engel 2003 SkO′ 的 `β2=0.190, β3=0.146`、`R0=1.2A^(1/3)=7.299 fm`，均匀密度尺度为 `22.98 e fm³`（归一化/质心修正）或 `45.32 e fm³`（紧凑简写）；它与 SkO′ 自洽内禀 `41.7 e fm³` 同量级，但不是实验 Schiff 矩。

### 为什么可到 100–1000 倍

Dobaczewski–Engel 2005 PDF p.4 的 Eq. (8) 给出 199Hg 的系数 `(0.0004, 0.055, 0.009) e fm³`；同文 PDF p.3–4 Table I 的有限程+短程关联+交换 SkO′ 行给 225Ra `(-1.5, 6.0, -4.0) e fm³`。逐个 $\bar g_i$ 通道的核系数绝对比为约 `3750, 109, 444`。脚本把这些作为同一文献中的模型比较，且另列“等耦合”情况：因 Ra 系数相加为 `0.5` 而 Hg 为 `0.0644`，等耦合总和只有约 `7.8` 倍，显示通道相消和 CP 来源依赖。

因此“100–1000 倍”是三个因素的乘积/竞争：

- 内禀 $S$ 的集体 $ZR^3\beta_2\beta_3$ 尺度；
- `50–55 keV` 同 J 宇称双重态分母，相对 1–5 MeV 非集体激发只给约 `18–100` 倍；
- 225Ra 与 199Hg 的 $V_{PT}$ 通道系数不同，尤其 Hg 的等标量通道异常小；再乘原子电子结构系数约 3，可使某些通道到 `10^3` 量级。

这里的“共振”是低能分母增强的微扰响应说法，不是已观测的核巨共振；若 $V_{PT}$ 足够大使微扰失效，公式本身需要重新对角化。

### 静态刚性与大振幅八极涨落

刚性梨形模型把 $\pm\beta_3$ 两个内禀态视作同一形状的宇称投影，令 $S_{\rm intr}$ 大且相干；它最清楚地解释“大的矩阵元 × 小能隙”。大振幅/GCM 或八极振动模型中，宇称本征态的静态平均 $\langle\beta_3\rangle$ 可为零，但 $\langle +|S_z|−\rangle$、跃迁 E3 和低能响应仍可很大；响应取决于波函数重叠、集体惯性、势垒、零点能和 PT 算符。

Gaffney *et al.* Nature **497**, 199 (2013), DOI `10.1038/nature12073`，source page [GA13](../sources/gaffney-2013-pear-shaped-rn-ra.md:50) 的 PDF pp.2–5、Figs.3–5/Table 1 显示 224Ra 比 220Rn 有更强、较连贯的 E3/Q3，但作者明确指出这些矩阵元不能单独区分静态梨形宇称投影与四极形状上的八极振动（同页 GA13-6）。这个边界同样适用于 225/223Ra：E3 或非零平均场 $\beta_3$ 不是 Schiff 响应的充分判据。

## Assumptions

- 采用一阶 PT 微扰，且 $V_{PT}$ 足够小；所有能量分母写成同 J 异宇称伙伴能差。
- `R0=1.2A^(1/3) fm` 和均匀尖锐表面只用于量纲/尺度控制，不替代有限表面、质子/中子不同密度或 EDF 计算。
- 225Ra 的 `β2, β3` 采用 Engel 2003 SkO′ 模型值；223Ra 未把评价 E1 反演成 β3，也未假造其 $S_{intr}$。
- 225Ra/Hg 的系数比来自不同核的模型计算与引用结果；CP 耦合组合未知，不能给单一普适增强因子。
- `β3_rms` 与 coherence 的 dynamic envelope 是透明 toy 参数扫描，不是 GCM/SCCM 计算或实验后验。

## Competing Explanations

- “低能分母”与“刚性梨形”不是互相替代的解释：动态八极关联也能给大跃迁矩阵元，但其 PT 响应需波函数重叠与惯性。
- 225Ra 评价中同自旋能差随自旋交替变号；Coriolis 解耦、不同转动惯量和组态混合会改变带间差，不能把每一个 A/B 差都当成同一隧穿劈裂。
- 大 E1、E3 或静态 $\beta_3$ 只能约束普通电磁结构；$V_{PT}$ 的 time-odd 核芯极化、交换和短程关联仍可改变 Schiff 响应的大小和符号。
- Skyrme、Gogny、相对论 EDF 之间的差异不能从单个 225Ra 系数直接外推；当前直接原件中明确量化的主要是 Skyrme/SkO′、SIII、SkM*、SLy4，Gogny/相对论结果需另行取得原始网格后比较。

## Transfer Conditions

可迁移：一阶响应的选择规则、$1/\Delta E$ 灵敏度、$S_{\rm intr}$ 的 $ZR^3\beta_2\beta_3$ 尺度、以及“E3/静态形变不等于 PT-Schiff”边界。

不可直接迁移：具体 $\Delta E$、β2/β3、$\langle V_{PT}\rangle$、EDF 系数、原子电子系数、刚性方向投影因子和任意跨核的 100–1000 倍数值。

## Failure Conditions

- 中间态 J 与基态不同，不能代入旋转标量 $V_{PT}$ 的分母；225Ra 的 31.56-keV `3/2−` 是明确反例。
- 缺失 PT 耦合常数或核内 $V_{PT}$ 矩阵元时，不能由能级差和 E3 直接得到实验 $S$。
- 把紧凑 `3/(20π)` 公式与归一化球谐公式混用会产生约 1.97 倍归一化差；缺失 `e/10` 更会造成数量级错误。
- 使用普通 E1 的相消点替代 Schiff 算符的 $r^3$/质心修正权重，会误判符号和大小。
- 用 223Ra 的评价 E1、或 225Ra 的偶核 β3，直接声称奇核 PT 响应已被实验测量，属于证据层越界。

## Falsification or Reverse Tests

1. 在同一 EDF、同一 blocked 奇核组态和同一宇称/角动量投影下，同时计算 223/225Ra 的 $\Delta E$、$S_{\rm intr}$ 和 $\langle V_{PT}\rangle$；若去掉低能伙伴仍得到相同实验响应，说明分母主导解释不足。
2. 对同一核固定 $\beta_2\beta_3$，改变 PT 通道、有限程、交换和 time-odd 参数；若模型系数符号/通道相消改变，说明“统一增强因子”不可用。
3. 用多条 E3、E1、E2 和同 J 宇称伙伴的联合拟合比较刚性转子与 GCM/振动模型；只靠一条 E3 或一条 E1 不得判静态梨形。
4. 以 199Hg 的同一 $V_{PT}$、电子结构和符号约定重做比值；若将耦合从等标量改为等矢量后比值从 7.8 变为 109，正是通道依赖而非算术错误的反证测试。

## Open Questions

- 需要同一微观框架下 223Ra blocked 计算，特别是 `3/2+`/`3/2−` 的投影、Coriolis 和 time-odd 芯极化；当前没有对应的生产网格。
- 需要对 223/225Ra 做 Gogny 与相对论 EDF 的同口径 $S_{\rm intr}$、$V_{PT}$ 和不确定度比较；当前直接原件主要覆盖 Skyrme。
- 需要把 223Ra 的多条 E1/E2/E3、宇称伙伴和寿命输入放入 GCM/SCCM 或集体 Hamiltonian，量化 `β3_rms × coherence` 而不是用 toy envelope。
- 需要把 Parker/Bishof 原子 EDM 统计限值与最新原子电子结构 $k_S$、核系数协方差联合传播；当前笔记只记录实验上限和理论关系。

## Human Review

本笔记完成 Codex source self-audit；没有人工逐 claim 审核，不标记为 `human-reviewed`。优先人工复核：Schiff 算符质心/球谐归一化、225Ra 评价负宇称指认、Dobaczewski–Engel 的跨通道比较，以及 223Ra 评价注释中“约 100 倍 E1”的原实验依赖。

## Promotion or Rejection History

- 2026-10-29：采纳一阶 PT 响应、同 J 分母、Engel 2003 SkO′ 形变/内禀矩、Dobaczewski–Engel 2005 系数表、Parker/Bishof 原子 EDM 上限。
- 2026-10-29：拒绝把 `31.56 keV (3/2−)` 当作 225Ra 基态分母；拒绝把低能分母单独写成 100–1000 倍；拒绝把 223Ra 评价 E1 当作 Schiff 矩直接测量；拒绝把 toy dynamic envelope 当作 GCM 结果。

## Reproducibility and Handoff

脚本与 JSON 结果：

- `outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/ra225-schiff/schiff_moment_amplification.py`
- `outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/ra225-schiff/schiff_moment_amplification.json`

运行命令：

```bash
python3 outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/ra225-schiff/schiff_moment_amplification.py
```

脚本结果的关键控制是：225Ra/223Ra 在 1 MeV 参考尺度下分母因子分别 `18.129`/`19.949`；在 5 MeV 下为 `90.645`/`99.745`；225Ra SkO′ 几何尺度 `22.980 e fm³`；同文献通道比 `3750/109/444`，而等耦合总和仅 `7.764`。这些结果是可复现的模型/尺度计算，不能替代实验或生产 EDF。
