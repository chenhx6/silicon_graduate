---
type: research-note
title: "锕系与超重核区 β3–β4 耦合：裂变势垒与宇称双重态的微观重整化"
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [butler-2020-222-228ra-octupole-evolution, gaffney-2013-pear-shaped-rn-ra, nomura-2020-ra-th-gogny-d1m-octupole, warda-2011-actinide-cluster-radioactivity-gogny, butler-nazarewicz-1996-intrinsic-reflection-asymmetry, nndc-2022-ac225-adopted-parity-doublet, nndc-2009-ra225-adopted-parity-doublet]
aliases: [actinide beta3 beta4 coupling, octupole hexadecapole fission barrier, actinide-octupole-hexadecapole-coupling-fission-barrier]
tags: [octupole, hexadecapole, beta3-beta4-coupling, fission-barrier, parity-doublet, actinide, superheavy, WKB, evidence-boundary]
created_from: Day26 delegated beta3-beta4 coupling and fission-barrier study
promotion_target: octupole-correlation
outputs: ["outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/actinide-coupling/actinide-coupling-model.py", "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/actinide-coupling/results.json", "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/actinide-coupling/fission_path.csv", "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/actinide-coupling/parity_doublet_wkb.csv"]
---

# 锕系与超重核区 β3–β4 耦合研究笔记

## Research Trigger

本轮任务要求检查锕系 `220–228Th`、`222–228Ra`、`225Ac` 以及超重核中的八极、十六极和更高多极形变耦合，特别是对裂变势垒、非对称裂变谷和宇称双重态劈裂的影响。任务简报提出 `C234 β2β3²β4` 与 `C345 β3β4β5` 耦合项，并要求检验“β3>0 必然诱发正 β4”和“第二势垒普遍降低 1–3 MeV”的说法。

本笔记将后两项视为待证假设。现有来源支持高阶坐标会改变势能面和路径，但没有给出这两个普适结论的直接实验或 EDF 证明。

## Grounded Evidence

### 实验与低能八极证据

- Butler *et al.* 的 `222Ra`/`228Ra` 亚势垒多步库仑激发拟合给出 `Q3=3120(190) e fm^3` 与 `2230(290) e fm^3`；`222Ra` 的多条跃迁 `Q3` 近似一致，而 `228Ra` 的 `2+→3−` 链接为 `Q3=150^{+360}_{-500} e fm^3`，与零相容。作者把前者解释为更稳定的梨形八极形变，把后者解释为八极振动，同时明确保留转动模型约束和配对/振动替代解释（Butler *et al.*, *PRL* **124**, 042503 (2020), PDF pp.3–5, Table I, Fig.4；本库来源页 [[butler-2020-222-228ra-octupole-evolution]]）。
- Gaffney *et al.* 的 `220Rn`/`224Ra` 库仑激发同时测量 E1–E3 矩阵元；`224Ra` 的 `Q3` 和跨自旋一致性强于 `220Rn`，支持更强的梨形八极集体性，但作者指出这些矩阵元仍不能单独区分静态形变与八极振动（*Nature* **497**, 199–204 (2013), PDF pp.2–5, Figs.3–5；[[gaffney-2013-pear-shaped-rn-ra]])。
- `225Ac` 的 NNDC/ENSDF 评价列出约 `40.09 keV` 的 E1 和 `B(E1)=0.00171(15) W.u.`；`225Ra` 的 `K=1/2` 宇称带显示 Coriolis 解耦造成的交错差值。该资料约束实验能级和跃迁，但没有 β4、β5 或 β6 的独立测量（[[nndc-2022-ac225-adopted-parity-doublet]], [[nndc-2009-ra225-adopted-parity-doublet]]）。

### 微观势能面与裂变路径

- Gogny-D1M 映射的轻锕系势能面把最强八极关联定位在 `224Ra` 与 `226Th` 附近（模型 `β3≈0.15`），而 `220Th` 处于较软、较弱八极的边界；这说明 `220–228Th`/`222–228Ra` 不应被当成一个固定深双阱链（Nomura *et al.*, *PRC* **102**, 064326 (2020), arXiv:2008.08870v2, PDF pp.2–4, Fig.1；[[nomura-2020-ra-th-gogny-d1m-octupole]])。
- Warda–Robledo 的 Gogny-D1S HFB 计算把 `Q20`、`Q30`、颈约束和 WKB/ATDHFB 惯性联合用于 `222,224,226Ra` 与 `226Th` 的团簇裂变通道；`224Ra` 基态附近给出约 `β2=0.18`、`β3=0.14`，而大 `Q30` 颈缩通道不能与低能八极振动混同（*PRC* **84**, 044608 (2011), PDF pp.3–5, 10–13；[[warda-2011-actinide-cluster-radioactivity-gogny]])。
- Warda *et al.* 对 Fm 区的自洽 Gogny-D1S 计算显式约束 `Q20/Q30/Q40`。`256Fm` 的紧致与伸长裂变谷在 `Q30` 和 `Q40` 上都不同，允许非对称形变会改变相关势垒；但降低量依赖核素、路径和约束，论文没有给出普适的 `β3β4` 系数或固定 `1–3 MeV` 规则（Warda *et al.*, *PRC* **66**, 014310 (2002), [arXiv:nucl-th/0203057](https://arxiv.org/abs/nucl-th/0203057), PDF pp.4,7–13）。
- Giuliani *et al.* 在 BCPM-EDF 的超重区计算中沿 `Q20` 路径探索 `Q30` 与 `Q40`，并将势垒剖面和集体惯性同时带入自发裂变寿命；作者明确指出势垒和寿命对 EDF、形变空间和惯性方案敏感（Giuliani *et al.*, *PRC* **97**, 034323 (2018), [arXiv:1704.00554](https://arxiv.org/abs/1704.00554), PDF pp.1,3–11）。

### 对称性与证据边界

反射变换要求偶多极 `β2,β4,β6` 不变、奇多极 `β3,β5` 变号。因此 `β2β3²β4` 和 `β3β4β5` 是允许项，但对称性不决定系数符号，也不决定平衡 `β4` 的正负。Butler–Nazarewicz 综述还强调 E1 对质子—中子位移相消敏感，E3 更接近集体八极观测；交替宇称带和 E1/E3 不能单独证明稳定静态极小（*RMP* **68**, 349–421 (1996), PDF Secs.II–VII；[[butler-nazarewicz-1996-intrinsic-reflection-asymmetry]])。

## Provisional Reasoning

### 1. 允许的低阶能量泛函

采用无量纲形变坐标的最小模型

\[
 E=E_0+\frac12C_2\beta_2^2+\frac12C_3\beta_3^2+\frac12C_4\beta_4^2+\frac12C_5\beta_5^2+\frac12C_6\beta_6^2
 +\frac14u_3\beta_3^4+\frac14u_4\beta_4^4+\frac14u_5\beta_5^4
 +C_{234}\beta_2\beta_3^2\beta_4+C_{345}\beta_3\beta_4\beta_5+\cdots .
\]

`β3β4` 线性项被反射对称性禁止；`β2β3²β4` 与 `β3β4β5` 允许，但系数须由自洽 EDF 或宏观—微观 PES 拟合，不能由 Butler、Gaffney 或 Warda 的实验量直接读出。

固定 `β2,β3` 且暂取 `β5=0` 时，局部极小满足

\[
 \beta_4^*\simeq -\frac{C_{234}}{C_4}\beta_2\beta_3^2,
 \qquad
 u_{3,\mathrm{eff}}=u_3-\frac{2C_{234}^2\beta_2^2}{C_4}.
\]

因此，`β3>0` 不推出 `β4>0`：在 `β2>0,C4>0` 的 convention 下，符号由 `−C234` 决定；当 `β5` 允许响应时，`C345β3β4β5` 还会使局部极小依赖 `β5` 的符号和软度。模型的这一步是解析推导与可证伪假设，不是某篇论文的直接测量结果。

### 2. 裂变势垒重整化

脚本以一个双峰参考 `V0(q)` 加上 `β4,β5` 局部极小能量，分别计算 `C234=C345=0` 和耦合开启的路径。运行结果为：

| 路径峰 | 无耦合 | 耦合 | `耦合−无耦合` |
|---|---:|---:|---:|
| 第一峰 | `10.137 MeV` (`q=0.3025`) | `9.669 MeV` (`q=0.2950`) | `−0.468 MeV` |
| 第二峰 | `8.264 MeV` (`q=0.7000`) | `6.872 MeV` (`q=0.7175`) | `−1.392 MeV` |

这组数值只说明一组透明系数下高阶耦合可以把路径峰降低约 `0.5–1.4 MeV`；它不是 `236U` 的预测，也不是对所有锕系的 `1–3 MeV` 证明。Warda 2002 的直接结论是 `Q30/Q40` 会改变 Fm 区裂变谷和势垒，Giuliani 2018 的直接结论是超重区势垒还必须与集体惯性一起解释（上述论文 locators）。`236U→140Xe+96Sr` 的质量分布需要完整的质量非对称坐标、惯性、颈断裂和产物形成模型；本轮证据不足以把它归因于一个局部 `β3β4` 项。

### 3. 宇称双重态的有效势与 WKB 灵敏度

把 `β3=x` 作为反射双阱坐标，取

\[
 U(x)=\frac12a_3x^2+\frac14u_{3,\mathrm{eff}}x^4+\frac16d_3x^6,
 \quad
 S/\hbar=2\sqrt{2B}\int_0^{x_0}\sqrt{U(x)-U(x_0)}\,dx .
\]

`x0` 是非零极小，`B` 是有效八极惯性。脚本使用无量纲 `B=38`，输出 `S` 和 `A exp(−S)` 作为劈裂灵敏度，而不是 keV 级实验能级。对 `N=130–142` 的示例输入，耦合让 `u3_eff` 从 `10` 降到约 `8.60–9.00`，`S` 在中点由 `0.662` 增至 `0.752`，相应无量纲劈裂比约 `0.914`；两端趋近 `1`。该非单调形状来自输入的 `a3(N),β2(N)` 与耦合共同作用，不是 Ra/Th 同位素链的拟合。

这个推导给出可检验的机制：β4 耦合可以改变八极势垒的有效四次项、双阱位置与作用量；实际劈裂还取决于惯性、零点能、宇称投影、角动量投影、奇核阻塞和 Coriolis 解耦。`225Ac`/`225Ra` 的现有低能数据只能约束这些因素的组合，不能单独反演 `C234`。

## Assumptions

- `βλ` 为同一形状参数化下的无量纲轴对称质量多极坐标；不同论文的 `Qλ`、`βλ`、半径和体积守恒 convention 未强行互换。
- `C234,C345,C4,C5` 是示例系数，不能当作 Skyrme、Gogny 或 RMF 的已标定参数。
- 裂变路径用标量 `q` 表示，参考势 `V0(q)` 是数值诊断用的双峰函数；没有声称它复现某个核素的真实 PES。
- WKB 只使用一维 `β3` 有效势和固定无量纲惯性；真实计算应使用多维作用量和随坐标变化的惯性张量。
- `β6` 在脚本中没有独立求解，仅在泛函中保留为对称性允许的更高阶背景自由度；本轮文献没有给出足够数据拟合 `β5/β6` 的独立贡献。

## Competing Explanations

- 低能宇称双重态可能来自八极软振动、宇称投影和组态混合，不要求稳定反射不对称平均场；Butler 2020 对 `228Ra` 的八极振动解释与 Butler–Nazarewicz 综述均保留这一替代路径。
- E1 小值可能由质子—中子偶极相消造成，不能当作 β3 或 β4 小的直接证据；`224Ra` 的强 E3 与小 E1 正是需要分层解释的例子（Gaffney 2013；Butler–Nazarewicz 1996）。
- 裂变势垒的主要重整化可能来自三轴形变、配对、壳修正、颈自由度或惯性，而非 `β3β4` 局部项；Warda 2002、Giuliani 2018 都把路径和惯性列为模型组成部分。
- 在奇 A 核中，轨道阻塞、Coriolis 解耦和带混合可以产生非平滑宇称位移；现有 `225Ac/225Ra` 评价不能把所有劈裂演化归为 β4。

## Transfer Conditions

只有同时满足以下条件时，模型结果才可迁移到具体锕系或超重核：

1. 用同一 EDF、配对方案、体积约束和多极归一化计算至少 `β2,β3,β4,β5,β6` 的二维或多维 PES；
2. 在同一坐标上提取反射对称与反射破缺路径的能量差，并报告局部曲率和 `β4` 符号 convention；
3. 用 ATDHFB/GCM 或等价方法计算惯性张量，比较势垒高度、路径作用量和零点修正；
4. 对 `Ra/Th/Ac` 同时检查 E1、E3、交替宇称能级、解耦参数和绝对寿命；
5. 将裂变片段质量非对称和颈密度作为独立输出，不能由低能宇称双重态直接外推。

## Failure Conditions

- 反射对称性或体积/质心约束未保持，导致 `β4` 符号和 `C234` 拟合不可比；
- `u3_eff≤0` 或高阶稳定项不足，局部多项式失稳，不能使用一维 WKB；
- 只用一个 E1 或一个 `0+→3−` E3 矩阵元宣称静态八极形变；
- 只比较势垒高度而省略惯性、零点修正和路径重优化；
- 将 Fm、Ra、Th 或 U 的质量非对称裂变结果跨核素直接迁移；
- 将脚本的无量纲劈裂比例写成 `keV`，或把示例系数写成 EDF/实验拟合结果。

## Falsification or Reverse Tests

1. **符号反演：** 固定 `β2,|β3|`，改变 `C234` 符号；若 `β4*` 不按 `−C234` 翻转，检查实现或坐标 convention。
2. **解耦极限：** 设 `C234=C345=0`，应恢复 `β4*=β5*=0`、原始势垒和基线 WKB 表。
3. **路径重优化：** 在 `(β2,β3,β4,β5)` 网格上重新寻找最小作用路径；若固定 `q` 的峰降低消失，说明标量路径结论不能迁移。
4. **惯性反检：** 把 `B` 扫描一倍和一半；若劈裂趋势比势垒项更敏感，应优先归因于惯性不确定度。
5. **EDF 反例：** 对 `220Th`、`228Ra` 和一个超重核分别运行 Skyrme、Gogny、RMF；若 β4 符号、耦合能量或势垒顺序不稳定，拒绝“普适正 β4/固定 1–3 MeV”命题。
6. **实验反检：** 检查奇核阻塞后 parity-doublet 位移是否仍与同一 `C234` 拟合；若 `225Ac` 与 `225Ra` 需要相反或高度自旋依赖的参数，拒绝把 β4 当作唯一控制量。

## Open Questions

1. 是否有同一套 Skyrme/Gogny/RMF 计算在 `220–228Th` 与 `222–228Ra` 上同时输出 `Q30,Q40,Q50,Q60`、惯性张量和最小作用路径？
2. `C234` 和 `C345` 能否从多维 EDF PES 的局部导数稳定提取，并在不同能量密度泛函之间比较？
3. `225Ac` 的奇核阻塞是否改变 β4 曲率足以解释 parity-doublet 的自旋依赖，还是主要是 Coriolis 解耦？
4. `236U` 的 `140Xe+96Sr` 质量分布需要怎样的质量非对称坐标和 scission 处理，才能测试八极—十六极协同是否有增量解释力？
5. 在 `Z≈120,N≈184`，高阶形变、三轴性和壳效应的相对贡献是否能用同一作用量审计区分？

## Human Review

本页为 Codex source self-audit，尚未人工审核。实验事实、作者解释、模型结果和本轮 reduced-model 推断已分开；`needs_review` 不因脚本算术通过而清除。

## Promotion or Rejection History

2026-10-29：创建本研究笔记。接受“高阶坐标可重整化裂变路径和八极有效势”的条件性工作假设；拒绝将“β3>0 必然诱发正 β4”“第二势垒普遍降低 1–3 MeV”写成已证实结论。脚本首次运行输出保存在 `workers/actinide-coupling/`，第一峰变化 `−0.468 MeV`、第二峰变化 `−1.392 MeV`，仅作为模型敏感性结果。
