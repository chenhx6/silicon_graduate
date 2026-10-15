---
type: concept
title: 三轴形变
aliases: [triaxial deformation, gamma deformation, γ deformation, non-axial deformation]
created: 2026-07-01
updated: 2026-10-15
status: active
review_status: unreviewed
concept_type: nuclear-shape
confidence: medium
high_confirmed_by:
high_confirmed_date:
tags: [deformation, collective-motion]
---

# 三轴形变（Triaxial Deformation）

## Definition

核的三个主轴不再具有轴对称性，通常以 β、γ 描述。三轴性可以是静态/刚性的，也可以表现为 γ 方向的大幅量子涨落。

## Necessary Assumptions

γ 数值依赖 Copenhagen/Lund 等约定和轴排序；跨论文比较前必须统一约定。

## Discriminating Observables

γ 带 staggering、signature splitting、手征或 wobbling 候选带、E2/M1 跃迁模式以及微观势能面都可提供信息，但没有一个单独观测量普遍充分。

## Supporting Evidence

[[chakraborty-2023-131xe-wobbling-origin]] 用较大 signature splitting 和 TPRM 拟合支持 `131Xe` 三轴形变，但同时没有观察到 wobbling。[[ayangeakaa-2016-133ce-in-beam]] 的多组态 CNS/TAC-CDFT 与 [[petrache-2020-137nd-multiple-chiral-bands]] 的 CDFT/PRM 也给出中高自旋三轴解。

非 A≈130 参照 [[domscheit-1999-triaxial-superdeformation-163lu]] 在 `163Lu` 的大形变 UC/PES 中给出 `γ≈+20.6°` 与 `-15.0°` 极小值。实验的带连接、转动惯量和大四极矩支持超形变转动结构，但 γ 数值和符号来自模型。

## Counter-evidence and Competing Interpretations

带混合、γ-softness 和模型参数相关性可能模拟部分三轴信号。[[ding-2021-131ba-133ce-signature-splitting]] 进一步表明，signature splitting 还可由近邻低-j 轨道的 Coriolis mixing 显著贡献，不能把 S(I) 当作 γ 的单值测量。

`163Lu` SD1 的平均四极矩不能区分 UC 的正、负 γ 组态；SD2 又缺少连接跃迁和多极性。因此“大形变 + 相近转动惯量”不能单独证明稳定三轴性或 wobbling。

## 形状张量、轴置换与signedγ分开

[[lv-2025-136pr-tac-covariant-density-functional]] LV25-33提供具体校准：模型TableII的D4/D6为`(.17,35°)`/`(.19,39°)`，Fig16显示γ0–60°扇区；另一个alternative解释才使用D4负γ/medium axis与D6正γ/short axis。没有实际轴映射，不把图上的γ自行改号，也不把替代解释写成实测形状共存。

### 声明的四极normal form

为拆清几何，本任务**选定**无量纲对角四极张量：

`qx=βcos(γ+120°)`，`qy=βcos(γ−120°)`，`qz=βcosγ`，`Q=diag(qx,qy,qz)`。

这不是已核作者代码的坐标定义。由三角/多项式恒等式得

`TrQ=0`，`TrQ²=3β²/2`，`TrQ³=3β³cos(3γ)/4`。

γ变号交换x/y特征值；同时翻z可令这个变换为det=+1的proper rotation。γ加120°则循环置换三轴。因此相同β的±γ具有相同unordered四极特征值与二/三阶不变量；它们单凭符号不是两个不同四极形状。**这不证明完整核密度、占据、流或波函数相同**，也不为带间shape identity作充分认证。

把表中rounded模型参数代入本normal form，D4的`TrQ²≈.04335, cos3γ≈−.258819`，D6为`.05415, −.453990`。这些是声明参数化下的确定性变换，不是实验E2 invariants、测量误差或作者未报告的更多精度；也不能仅凭这些符号重判其prolate-triaxial/oblate-triaxial术语。

### 相对转轴需要独立保留

只在假设的小形变irrotational law下，取任意共同标度的`ℑx=(qy−qz)²/3=β²sin²(γ+120°)`，其余循环。若Q、惯量张量和转轴一起换轴，`ωᵀℑω`不变；若固定cranking axis而只变γ号，相对取向可以改变。

声明控制`β=1,γ=±20°`的unordered四极形状相同，固定x轴的惯量分别为`.413176`与`.969846`；轴也同步交换后回到`.413176`。此处共同标度任意，不是136Pr实测MOI；没有把D4表列+35°改成−35°。TAC总角动量还有准粒子与配对贡献，不能将该hydrodynamic公式直接当作实际`I/ω`或唯一γ反演。

### 验证与观测边界

[day14_pr136_gamma_axis_audit.py](../../system/scripts/day14_pr136_gamma_axis_audit.py)及[50-check回执](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/pr136-gamma-axis-audit.json)读取实际TableII十行并校核上述性质。环境无SymPy的首次import失败已保留；随后用标准库Fraction在`Q(sqrt3)`中做精确算术。各恒等式对c/s逐变量次数至多3，在4×4不同有理点网格精确成立，结合多项式唯一性证明恒等；不是用有限浮点抽样冒充符号证明。另以浮点控制核source参数与同步转轴结果。

区分实际结构仍需作者逐态tensor/axis map及相对取向、完整E2矩阵元链（含必要的相位/分支）和独立形状敏感观测。单一寿命、相对γ强度、E2未观测或一个模型极小值不补这些材料；不同模型βγ也不直接证明实验形状共存。Decision: limits γ号到形状/模式的直接跳步，保留当前解释竞争。

### Nd系统学的直接伴随源

[[petrache-2015-nd-exotic-rotations-triaxiality]] PT15-5是Lv2025 Ref.[48]的实际语境：其calculated负γ/正γ分别关联中间/短轴转动；PT15-6却明确要求后续寿命测量检验这种轴变化是否真实。它支持保留relative-axis信息，不提供136Pr实际frame或新的shape实证。

该文J^(2)的51/23两组量级是选定Nd系统学总结。PT15-4将逐核选带、均值的interaction/频率范围与低组图示删点分开；缺完整输入/筛选mask，不能把图上的gap当无条件的γ或形状分类器。这个限制与上面的几何必要条件相容，不证明作者处理错误，也不改变D4/D6竞争解释。

## Related Nuclei and Bands

- [[131xe]]
- [[131ba]]
- [[133ce]]
- [[137nd]]
- [[163lu]]（非 A≈130 比较参照）
- A≈130 Xe-Ba-Ce-Nd 区域

## Our Current Position

“triaxial”是形状层面的判断；“wobbling”“chiral”“γ-rigid”是更强、需要额外判据的结构解释。

## Sources

- [[petrache-2015-nd-exotic-rotations-triaxiality]] PT15-4–PT15-8：signedγ的模型相对轴语境、J^(2)筛选与必要寿命观测，不是Pr136独立实证。
- [[lv-2025-136pr-tac-covariant-density-functional]] LV25-33：模型TableII/Fig16与alternative γ/axis场景；上述normal form与计算为本任务条件推导。
- [[zamfir-casten-1991-gamma-softness-triaxiality]]
- [[frauendorf-meng-1997-tilted-rotation-chirality]]
- [[chakraborty-2023-131xe-wobbling-origin]]
- [[frauendorf-2024-wobbling-review]]
- [[ayangeakaa-2016-133ce-in-beam]]
- [[petrache-2020-137nd-multiple-chiral-bands]]
- [[ding-2021-131ba-133ce-signature-splitting]]
- [[domscheit-1999-triaxial-superdeformation-163lu]]

## Evolution Log

- 2026-10-15：补136Pr模型γ/替代转轴场景和50-check四极张量必要条件；不认证作者frame或实验共存。
- 2026-07-01（7 sources）：加入 Ce-Nd 多组态与 signature-splitting 的模型非唯一性。
- 2026-07-03（8 sources）：加入 `163Lu` 非 A≈130 三轴超形变参照，明确四极矩与转动惯量不能直接确定 γ。
