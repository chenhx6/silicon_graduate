---
type: concept
title: 核手征性
aliases: [nuclear chirality, nuclear rotational chirality, 核转动手征性]
created: 2026-07-13
updated: 2026-10-26
status: active
review_status: unreviewed
concept_type: rotational-symmetry
confidence: low
high_confirmed_by:
high_confirmed_date:
tags: [chirality, triaxiality, angular-momentum-geometry]
---

# 核手征性（Nuclear Chirality）

## Definition

在三轴核的经典图像中，高 `j` 粒子、集体芯转动和高 `j` 空穴可分别沿短、中、长主轴形成 aplanar 三角架。两种相反 handedness 在 body-fixed frame 中不能由普通空间转动互相变换；实验室系中的量子隧穿与对称性恢复可产生 [[chiral-doublet-bands]]。

## Necessary Assumptions

- 三个主轴方向均有重要角动量分量；
- 需要区分平均场的自发破缺与有限体系中的量子对称性恢复；
- 具体实验指认还需要组态、形变与电磁跃迁等多项约束。

## Discriminating Observables

同宇称近简并 `Delta I=1` 双带、`S(I)`、alignment 和 `B(M1)/B(E2)` 可作为候选信息，但 [[meng-2010-open-problems-nuclear-chirality]] 强调这些 fingerprints 均具有模型依赖，不能单项构成充分证明。

## Supporting Evidence

[[frauendorf-meng-1997-tilted-rotation-chirality]] 给出 aplanar TAC/PRM 奠基框架；[[meng-2010-open-problems-nuclear-chirality]] 总结其量子恢复和判据边界。

[[xiao-2022-chirality-octupole-correlations-74as]] 在 `74As` 建立正宇称 Bands 1/2 的五条连接和相近的能量/ratio fingerprints；拟合 TPRM 给出 aplanar total `I`。但中子角动量在三轴间显著混合，不符合最理想的 long-axis alignment，且无绝对 partner strengths，因此保留为 candidate evidence。

[[wang-2023-experimental-studies-nuclear-chirality-china]] 汇总中国团队在 23 个候选核上的工作，并以 A≈130、100、80 三个区域组织 fingerprint 与 lifetime 比较。它是二级证据地图；尤其 `106Ag` 的 absolute-strength 反例说明相似能谱/ratio 不能替代 partner-resolved electromagnetic tests。

[[bark-2024-investigations-nuclear-chirality-ithembalabs]] 进一步显示：realistic configuration mixing 下，少量 planar components 也可使 dominantly aplanar partners 明显不等；相反，多个相似 bands 也可能无法唯一分对。核手征判断因此同时需要 geometry、configuration 与 band-identity mapping，而不是逐项 fingerprint 打勾。

[[mukhopadhyay-2007-135nd-chiral-vibration-static]] adds a direct electromagnetic-strength reference: `135Nd` partner bands have near-identical intraband `B(E2)`/`B(M1)` from DSAM, while TAC+RPA connects a low-spin chiral-vibration regime to higher-spin static chirality. The source remains nucleus-specific and model-bound at the critical-spin transition.

[[grodner-2018-128cs-chiral-g-factor]] adds a direct geometry-sensitive counterexample: TDPAD gives `g=+0.59(1)` for the `128Cs` chiral-band head, while PRM+CDFT finds an almost planar rather than ideal aplanar configuration. This supports a spin/frequency onset boundary and warns against using low-spin fingerprints alone.

## Counter-evidence and Competing Interpretations

`gamma` vibration、shape coexistence、many-particle correlations、pseudospin partners、core polarization 和不同组态伙伴带可能产生相似结构。

## Our Current Position

核手征性是需要角动量几何、量子恢复和核素特定实验链共同支持的解释；近简并双带是候选入口而非充分证明。

Frauendorf 2001 adds a broader symmetry map: principal-axis, planar TAC and aplanar/chiral solutions are distinguished by the discrete operations left unbroken by the rotating mean field. The left/right TAC solutions are intrinsic mean-field states; same-parity partner bands arise only after laboratory-frame quantization and symmetry restoration. Magnetic rotation, antimagnetic rotation and reflection-asymmetric rotation are related rotating-nucleus cases, not interchangeable explanations for a chiral doublet.

## Sources

- [[frauendorf-meng-1997-tilted-rotation-chirality]]
- [[meng-2010-open-problems-nuclear-chirality]]
- [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]
- [[xiao-2022-chirality-octupole-correlations-74as]]
- [[wang-2023-experimental-studies-nuclear-chirality-china]]
- [[bark-2024-investigations-nuclear-chirality-ithembalabs]]

## Evolution Log

- 2026-07-13：由 Meng 2010 建立几何、对称性恢复和 fingerprint ambiguity 边界。
- 2026-08-11：加入 Xiao 2022 `74As` 五-link candidate 与 fitted-TPRM aplanar/nonideal-neutron geometry 边界。
- 2026-08-11：加入 Wang 2023 三质量区二级证据地图与 `106Ag` lifetime counterexample；不把 23-nucleus census 计为独立证据。
- 2026-08-11：加入 Bark 2024 realistic-mixing/planar-component 与 multiple-band mapping boundaries。

## Day23内的Day24无学分预习：反幺正手征操作不等于Kramers双带

本节是Day23原run中的恰好一张下一卡知识预习，**Day24未计正式学分、不开Day25**。来源为[[frauendorf-meng-1997-tilted-rotation-chirality]] FM97-D24P-001与[[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]] F01-D24P-001/002；新增推断needs_review:true，不改变原source人审历史。

在声明的普通spin表示中，K是|I,mz〉基底的复共轭，Ry(π)=exp(−iπJy)，T=Ry(π)K。由于时间反演与普通物理旋转相容，

$$T^2=(-1)^{2I},\quad R_y(\pi)^2=(-1)^{2I},\quad
C=R_y(\pi)T,\quad C^2=+1.$$

所以C不具半整数T²=−1导致Kramers正交伙伴的前提。这里选y为坐标平面的法向，只定义数学表示，不新指派某个核的中/短/长轴。C保Jx/Jz而反Jy，表达左右反射；真实同I磁子态的简并，也不等于两条不同intrinsic构型的partner bands。

反幺正标签还有phase边界：若Cψ=λψ，ψ→exp(iα)ψ会令λ→exp(−2iα)λ。因此不能把“C=±1”直接当成parity/signature那样的相位不变量子数。源文所说左右构型的对称/反对称组合是选定phase的构造，不能由此把所有实际split bands赋一个额外可测C奇偶。

两态数学模型令|L〉和|R〉由C=σxK互换，H=E0I+tσx，χ=σz。任何实t均保持C，能隙2|t|，非简并本征态有〈χ〉=0但〈χ²〉=1；这说明有限体系对称恢复后signed mean为0，不单独排除intrinsic手征图像。反过来，一个模型非零fluctuation也不证明实际手征。toy中t=.01/1只是dimensionless设计，不是核隧穿matrixelement、能量或误差上限。

同模型的C-even算符O=O0I+O1σx，对localized左右态均有对角O0，对两个stationary eigenstates却为O0±O1。**同一反幺正对称性不强制不同能级的任意标量相等**。若讨论physical g，必须先有实际电磁算符、组态与matrix elements；该toy不填任何g0/g1，更不把g相同/不同做成手征充分/普适排除判据。

新脚本`system/scripts/day24_preview_chiral_antiunitary.py`在I1/2、1、3/2、5/2、4表示及两态toy共59项控制通过，spin矩阵最大误差约2.0e−14。选定Csymmetry非简并spin矩阵只是对“该反幺正代数必强制双重简并”的数学反例，**不是rotationally invariant实验室核Hamiltonian**。验证到这里为止，不给真实核态、三维χ/g数据、Qt CI或机时，也未运行隔离的Day22 producer。

## Day23内的Day24无学分预习：135Nd逐伙伴观测矩阵

本矩阵只作当前Day24知识预习、不计正式信用。[[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-D24P-001–003及[[zhu-2003-135nd-composite-chiral-pair]] ZH03-D24P-001区分原实验、评价端点和模型；新推断needs_review:true。

| 量/层 | Band A与Band B实际可用证据 | 依赖/当前输入边界 |
|---|---|---|
| same-I能量 | 声明historical family对应下，snapshot在31/2…39/2的E_B−E_A中心为356.8/280.8/184.1/118.1/95.2keV | 外部cutoff2008 adopted中心，不是额外测量/CI或静态手征阈值；4006.7与4008.1keV虽近却分别31/2与33/2，不能配作same-I伙伴 |
| 寿命 | MU07 TableI meanτ两band分列，前四配对B约2倍A，39/2接近 | APIhalf_life须除ln2，不与meanτ裸比；相近derivedB不等τ相同，branch/Eγ/IC和Cov仍需原输入 |
| B(M1)、B(E2) | MU07表/图报告的inband强度在误差内相近；interband图点另有源身份 | 这是一条DSAM/branch/derivation链，TableI无逐行Eγ/finalspin；APIRTPW为W.u.而非μN²/e²b²，不能混单位或重复计票 |
| 角动量几何 | 原PQTAC/RPA解释低spin振动、随spin趋静态的model演化 | 实测τ/B不直接测三轴分量；RPA零频、TAC破缺和实测最小split分别检验，不指定一条model-independent临界spin |
| g因子 | 当前此对135Nd未获得可绑定的双partner g观测向量 | 128Cs bandhead的g属于另一核/态，不能迁入135Nd；017 C-even算符数学也不提供physicalg |

snapshot的648/649.2和590/591为实际不同endpoints/ΔI例，说明partner-resolved evidence map必须同时锁定parent、daughter、Jπ和component。所有字段为原文/导出已有量或声明中央算术，不新增核态/机时、不给Qt代理置信区间，也不恢复225.8 P正号排他方案。原2003建纲图与2007新DSAM各自有采集贡献，evaluation整理与重复引述不加独立实验票；真正共享哪些branch/assignment输入仍须reference notes与event/analysis ledger。

## Day23内的Day24无学分预习：表示精度不能补足物理量身份

[[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-D24P-004/005取得官方作者TeX/矢量图，原TableI版本相符，绘制坐标与误差棒可纯文本重建；这比仅从raster图手工读值更可复核，但仍是同一论文的表示层。

当前135Nd partner map把三件事分开：**图点画在哪里**可由作者vector source缩小转录误差；**图点对应哪条γ/component/parent**仍缺逐线ledger；**由这些量支持哪种手征动力学**还需完整模型和独立伴随观测。19项解析控制不把后两项自动补齐。用TableI denominator构造out/in仍需同母态/组件条件，也不把rounding或errorbar端点包络称CI。无新实验、physicalg或核态/机时；仅同一Day24无学分预习。
