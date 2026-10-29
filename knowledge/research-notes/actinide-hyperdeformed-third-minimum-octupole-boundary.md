---
type: research-note
title: "锕系超高形变第三势阱与深八极反射不对称：实验边界、WKB劈裂与可复现模型"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [actinide hyperdeformed third minimum, hyperdeformed third minimum octupole boundary, 锕系第三势阱八极不对称]
tags: [hyperdeformation, third-minimum, actinides, octupole, fission-barrier]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "2026-10-29 delegated investigation of hyperdeformed third minima and octupole asymmetry in 230-234Th and 232-236U"
evidence_sources: [butler-nazarewicz-1996-intrinsic-reflection-asymmetry, gaffney-2013-pear-shaped-rn-ra]
outputs: ["outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/hyperdeformed-actinides/hyperdeformed_actinides.py", "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/hyperdeformed-actinides/results.json", "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/hyperdeformed-actinides/pes_grid.csv", "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/hyperdeformed-actinides/parity_wkb.csv", "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/hyperdeformed-actinides/decay_competition.csv", "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/hyperdeformed-actinides/chart_data.json"]
---

# 锕系超高形变第三势阱与深八极反射不对称

## Research Trigger

本轮任务要求调查 `230,232Th` 与 `232,234,236U` 的超高形变第三势阱，检验亚势垒裂变共振、轴比约 `3:1`、`beta2≈0.8–0.9`、深八极 `beta3≈0.35–0.45`、宇称劈裂 `<1 keV` 及 `Q3≈12–16 e b^(3/2)` 等断言，并生成二维势能面与 WKB 工件。

检索后的工作结论是：轻锕系确有高形变裂变共振的强候选证据，但“深第三势阱”和“静态深八极极小”不是所有核素的同等事实。`232U` 的裂变概率数据支持第三势阱解释，`234,236U` 的传输共振与碎片角分布支持超高形变解释；`232Th` 的旧实验与现代八维宏观—微观计算指向浅第三极小；`230Th` 在本轮未找到可直接支持第三势阱的原始实验。宇称近简并和电多极矩数值还必须依赖集体惯性、坐标约定、投影方法及完整电磁矩阵元。

## Grounded Evidence

### 裂变共振与第三势阱

| 核素 | 直接来源与结果 | 证据性质与边界 |
|---|---|---|
| `232U` | `231Pa(3He,df)232U` 测量裂变概率，激发能分辨率 `11 keV`，覆盖 `E*=4.0–6.4 MeV`。摘要报告低于 `4.8 MeV` 的亚势垒共振、`hbar^2/(2Theta)=1.96(11) keV`，并由势垒参数分析得到 `EIII=3.2(2) MeV`。 | Csige et al., *Phys. Rev. C* **80**, 011301(R) (2009), DOI `10.1103/PhysRevC.80.011301`; 这是裂变概率/过渡态模型的间接结构证据，不是离散 gamma 带的直接观测。见 Csige et al. (2009)。 |
| `234,236U` | `235U(d,pf)236U` 的尖锐传输共振与早先 `234U` 数据联合分析；摘要给出 `hbar^2/(2Theta)=1.8^{+0.5}_{-0.7}` 和 `1.6^{+1.0}_{-0.4} keV`，并报告 `K=1,2,4` 的解释。 | Krasznahorkay et al., *Phys. Rev. Lett.* **80**, 2073 (1998), DOI `10.1103/PhysRevLett.80.2073`; 形变解释依赖共振拟合、角分布和转动模型，不能单独确定 `beta3`。见 Krasznahorkay et al. (1998)。 |
| `232Th` | Blons 等早期实验被后续计算概括为浅第三极小，深度不超过约 `0.5 MeV`。Jachimowicz–Kowal–Skalski 八维宏观—微观 Woods–Saxon 计算给出 `BIII−EIII≈0.36 MeV`，并建议用类似 U 实验的技术重做 `232Th`。 | Jachimowicz et al., *Phys. Rev. C* **87**, 044308 (2013), DOI `10.1103/PhysRevC.87.044308`, arXiv:1301.0713；这是理论与历史实验的对照，不是新的 `232Th` 共振测量。见 Jachimowicz et al. (2013)。 |
| `230Th` | 本轮未找到可直接核验的亚势垒裂变共振或第三势阱原始数据。 | 不把 `230Th` 写成已证实第三势阱；需要专门的高分辨裂变概率、光裂变或转移裂变实验。 |

Jachimowicz 等同时指出，`232–236U` 的实验解释给出 `EIII≥3 MeV`，而当时多数 Skyrme、Gogny 及现代宏观—微观结果不给出如此深的第三极小。这个“实验解释—理论计算冲突”本身是当前证据状态，不能通过把共振自动改写成静态形状而消除。该论文还显示，纳入 `beta10` 后第三鞍点可沿其路径降低约 `4.1 MeV`；这说明在大伸长、颈化和质量不对称区域，形状坐标截断会显著改变势垒，而不能把某一个 `beta3` 扫描当作全维裂变路径。

### 微观八极起源与形变证据

Butler–Nazarewicz 综述把锕系八极软化的微观来源归因于费米面附近相反宇称轨道的 `Delta l=Delta j=3` 耦合，例如质子 `f7/2–i13/2` 和中子 `g9/2–j15/2`。这解释了八极响应容易增强，但不决定第三势阱的绝对深度。第三势阱还受壳修正、表面能、四极—高阶多极耦合、配对、颈坐标、质量不对称和集体惯性共同控制。

反射不对称的实验判据必须分层：裂变共振和碎片角分布是过渡态/形状候选证据；交替宇称带和 E1/E3 是低能结构证据；离散 gamma 超高形变带才是更直接的谱学证据。Butler–Nazarewicz 明确区分静态八极平均场、八极软振动、宇称恢复和 GCM 劈裂；Gaffney 等在 `220Rn/224Ra` 的库仑激发中也强调，E2/E3 矩阵元本身不能唯一区分投影静态梨形与八极振动。故第三势阱裂变共振不能单独证明“深静态梨形双核分子态”。

### 本轮可复现二维模型结果

工件 `hyperdeformed_actinides.py` 使用透明的

$$V(\beta_2,\beta_3)=V_q(\beta_2)+\frac12a_3(\beta_2)\beta_3^2+35\beta_3^4,$$

其中 `Vq` 是三井路径诊断函数，`a3` 在 `beta2≈0.92` 附近变负；对 `beta3=0` 与放开 `beta3` 的路径分别求极小。它是敏感性模型，不是 EDF。输出结果为：

| 核素 | 放开路径 `beta2` | `beta3` | 八极放开能量增益 MeV | 几何 `Q3` (`e b^(3/2)`) |
|---|---:|---:|---:|---:|
| `230Th` | 0.92 | 0.316 | 0.350 | 2.70 |
| `232Th` | 0.92 | 0.378 | 0.714 | 3.26 |
| `232U` | 0.92 | 0.414 | 1.029 | 3.65 |
| `234U` | 0.92 | 0.431 | 1.207 | 3.83 |
| `236U` | 0.92 | 0.439 | 1.302 | 3.93 |

模型中的 `beta3=0` 路径在第三坐标附近没有局部极小，放开八极后出现两个 `+/-beta3` 对称极小；这是“坐标允许时会形成凹陷”的条件性演示，不是实验或自洽 EDF 结论。二维原始网格见 `pes_grid.csv`，汇总见 `results.json`，绘图数组见 `chart_data.json`。

### 宇称劈裂的 WKB 推导与边界

沿固定 `beta2` 的一维集体坐标，取

$$H_3=-\frac{\hbar^2}{2B_{33}}\frac{d^2}{d\beta_3^2}+V(\beta_3),\qquad V(\beta_3)=\frac{d_4}{4}(\beta_3^2-q_0^2)^2.$$

在井底能量近似下，穿过 `-q0` 到 `+q0` 的作用量为

$$\frac{S}{\hbar}=\frac{2\sqrt{2B_{33}d_4}}{3}q_0^3,$$

并有

$$\Delta E_{\rm parity}\simeq\frac{\hbar\omega_3}{\pi}e^{-S/\hbar},\qquad \hbar\omega_3=\sqrt{\frac{2d_4q_0^2}{B_{33}}}.$$

工件用 `d4=140` 和示意集体质量 `B33=140` 扫描：`beta3=0.35` 时 `S/hbar=5.66`、`Delta E≈0.55 keV`；`beta3=0.40` 时约 `0.039 keV`；`beta3=0.45` 时约 `0.0012 keV`。但将同一势换成 `B33=100` 时 `beta3=0.35` 的劈裂约 `1.56 keV`。因此“`Delta E<1 keV`”只能在给定势、惯性、零点能和路径的条件下成立，不能从 `beta3` 或势垒高度单独严格推出。对于偶偶核，更准确的语言是第三井内交替宇称带可能出现强烈近简并；它不自动等同于奇 A 核同自旋宇称双重态。

### `Q3`、`D0` 与单位核查

用轴向均匀密度的几何尺度

$$Q_3\simeq\frac{3}{4\pi}ZeR^3\beta_3,\qquad R=1.2A^{1/3}\ {\rm fm},$$

并采用 `1 b^(3/2)=1000 fm^3`，本轮模型得到 `Q3≈2.7–3.9 e b^(3/2)`。这与 Gaffney 2013 的 `220Rn/224Ra` `Q3≈2180/2520 e fm^3` 和 Butler 2020 的 `222Ra` 聚合 `Q3=3120(190) e fm^3` 同量级。题面提出的 `12–16 e b^(3/2)` 不能作为这些核素的通用结果；它需要未声明的归一化约定或远大于本模型的有效变形。

`D0` 对质子—中子内禀偶极相消极敏感。BN96 将 E1 视为相消敏感的等矢量量，将 E3 视为更集体的八极探针；因此大 E3、很小 E1 和非零平均场 `beta3` 可以同时出现。本工件的 `D0_proxy≈0.11–0.18 e fm` 只用于显示量级和敏感性，不能代替 GOSIA、寿命或完整 EDF 电荷密度计算。

### 裂变与 gamma 退激竞争

第三井态的总宽度应写成 `Gamma_tot=Gamma_f+Gamma_gamma+...`。`Gamma_f` 由外鞍点穿透、能级密度、质量张量和预形成因子控制；`Gamma_gamma` 由 E1/E2/E3 强度、终态密度和内转换控制。仅有第三井深度不能决定分支比。工件 `decay_competition.csv` 对外势垒作一维 WKB 传输代理：在模型第三井底部、外势垒仍存在时 `T_f` 很小，任何非零 gamma 宽度都可能竞争；激发能接近或越过外鞍点时裂变可以迅速占优。该表不提供绝对半衰期或分支比。实验上 U 共振正是通过裂变通道被看到，不能据此反推所有第三井态都具有相同的裂变主导性。

## Provisional Reasoning

1. 最保守的综合是：U 同位素存在重复的亚势垒裂变共振和转动参数，支持超高形变过渡态或第三井解释；`232Th` 的浅极小与 U 的深极小形成未解决的理论—实验张力；`230Th` 仍是证据空白。
2. 八极反射不对称是合理的微观自由度，但“第三井=深静态梨形”不是由 `Delta l=Delta j=3` 或一次裂变共振唯一推出的。
3. 当集体质量足够大、八极双井作用量足够大时，宇称劈裂可进入 keV 甚至更低；该量级是动力学量，不是 `beta3` 的单值函数。
4. 本模型显示 `beta3≈0.35–0.44` 可作为参数扫描窗口，但模型 `Q3` 仅约 `3–4 e b^(3/2)`，因此拒绝把 `12–16 e b^(3/2)` 作为通用预测。

## Assumptions

- `beta2,beta3` 为无量纲轴向形变坐标；真实文献中的 `Qλ`、`βλ` 和表面参数化不能直接互换。
- `Vq`、`a3`、`d4`、`B33` 和外势垒宽度均为公开的敏感性输入，不是某个 EDF 的拟合参数。
- 一维 WKB 忽略三轴性、`beta4–beta6`、颈、质量不对称、随坐标变化的惯性和零点修正。
- `Q3` 公式是均匀密度几何尺度；`D0_proxy` 是显示相消敏感性的占位量。

## Competing Explanations

- 裂变共振可能由过渡态共振、通道耦合或形状共振解释，而非可分辨的第三井转动带。
- 深 U 第三极小的实验反演可能受势垒参数、能级密度、角分布和共振重叠影响；Jachimowicz 等指出其与多数自洽计算冲突。
- 大 E3 或小 E1 可来自八极软振动、投影组态混合和质子—中子偶极相消；它们不是静态梨形的充分判据。
- 宇称近简并也可来自 GCM 非局域核和软势，而不要求单一平均场双井。

## Transfer Conditions

要把本模型转移到具体核素，至少需要同一 EDF、同一体积/质心约束下的多维 `beta2,beta3,beta4,beta5,beta6` PES、ATDHFB/GCM 惯性、零点修正、宇称和角动量恢复，以及 E1/E2/E3 过渡矩阵元。只有这些条件同时满足，才能把 WKB 量级与实验共振或交替宇称带逐项比较。

## Failure Conditions

- 以 `beta3=0` 的局部曲率或第三井深度单独宣称 `Delta E<1 keV`。
- 将 U 的裂变共振解释复制到 `230Th` 或 `232Th` 而不检查独立实验。
- 把 `e fm^3`、`e b^(3/2)` 和转子约定的 `Q3` 混写；`1 b^(3/2)=1000 fm^3` 必须显式处理。
- 将 reduced-model 的 `Q3`、`D0`、势垒和传输代理写成实验测量或 EDF 结果。
- 用一个 E1/E3 矩阵元或一个裂变分支排除八极振动、通道耦合或势垒参数替代解释。

## Falsification or Reverse Tests

1. 在同一 EDF 和同一网格上比较 `beta3=0`、允许 `beta3`、允许 `beta10` 以及完整高阶多极；若第三井位置或深度随坐标截断大幅变化，则拒绝单坐标结论。
2. 对 `232Th` 重做与 U 实验同分辨率的裂变概率和碎片角分布；若没有与第三井相容的共振群，浅井解释应优先。
3. 对 U 共振群同时拟合 `K` 分布、角分布、共振间距、裂变宽度和 gamma 退激；若转动参数不能稳定跨通道复现，降低 HD 解释置信度。
4. 扫描 `B33`、零点能和路径曲率；若 `<1 keV` 只在窄参数区出现，则拒绝“严格趋零”表述。
5. 测量多条 E3、E1 与交替宇称能级；静态形变应给出跨自旋较一致的内禀矩，而软振动允许矩阵元随自旋和通道显著变化。
6. 用 `Q3` 单位换算反检 `12–16 e b^(3/2)`：若原始论文实际报告的是 `e fm^3` 或约 `1–4 e b^(3/2)`，则撤回题面数值。

## Open Questions

- `230Th` 是否存在可分辨的第三势阱共振，尤其是高分辨光裂变或转移裂变测量？
- `232Th` 的浅第三极小与 `232–236U` 的深第三井反演能否在相同实验与相同多维模型中同时解释？
- 是否存在包含 `beta1–beta6`、质量不对称和 ATDHFB 惯性的统一轻锕系势能面？
- U 共振是否有可检出的第三井 gamma 退激或仅通过裂变宽度可见？
- `E1/E3`、角分布、共振间距和寿命能否联合区分深八极静态形状与通道耦合？

## Human Review

本页由 Codex 完成 source self-audit；当前 `review_status: unreviewed`。Jachimowicz、Csige 和 Krasznahorkay 的原始论文在本轮以公开摘要/预印本为主核验，完整实验表格、共振逐条 locator 和原始拟合协方差仍需人工复核。不得写成 `human-reviewed`。

## Promotion or Rejection History

- `2026-10-29`: 接受“U 同位素有超高形变裂变共振候选证据、232Th 浅第三极小和理论—实验冲突、八极自由度可使大伸长势面重整化”的条件性结论。
- `2026-10-29`: 拒绝“230–234Th、232–236U 均已证实深第三势阱”“放开 beta3 必然得到深静态梨形”“宇称劈裂严格 <1 keV”“Q3 普遍为 12–16 e b^(3/2)”四项无条件断言。
- `2026-10-29`: reduced-model 工件运行完成；数值仅作为透明敏感性与反证测试，不提升为实验或 EDF 结果。
