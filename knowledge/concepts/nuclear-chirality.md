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

## Day23内的Day24无学分预习：三种归一必须分开

当前135Nd partner map进一步区分：量子/准玻色波函数的归一、同一母态全部衰变的绝对branch归一、对某组已选γ出口的条件归一。后者即使加到1，也不表示那组出口耗尽真实total width。模型振幅/图中B若尚未与母态和normalizer绑定，不能直接充当同一inventory中的绝对分量。

[[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-D24P-006/007在一组明确candidate binding中得到out-only q约.98，而in+out超过1；这是可证伪的输入组合诊断，**不是认定作者使用了某种归一或paper错误**。[[almehed-2011-chiral-vibrations-a135]] AL11-D24P-001/002与[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-D24P-001锁定m、B与γ率定义。必要伴随输入变成具体问题：每个图点的parent/Jf/γ、是absolute还是selected-channel quantity、所用total/partialτ及branch/IC normalization是什么？没有ledger就保留多种解释，不拟新δ/τ/CI/g或机时。仍仅同一个Day24无学分preview。

## Day23内的Day24无学分预习：哪些强度关系来自额外动力学

[[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]] F01-D24P-003与[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-D24P-002/003在完整good-I多重态中扩展017逻辑。这里H在每个I、multiplicity上为一个标量乘identity，所以与所有转动、T和C相容；不同multiplicity的能量仍可不等。真正半整数T/Kramers和M简并在各自irrep内，不因此强迫两条不同的谱学序列。

构造遵守

$$\langle I_fM_f,\beta|T_{\lambda\mu}|I_iM_i,\alpha\rangle=
\frac{\langle I_iM_i,\lambda\mu|I_fM_f\rangle}{\sqrt{2I_f+1}}
R_{\lambda;\beta\alpha},$$

并以反向RME/Hermitian phase闭合全部μ分量。两套声明的real RME满足rank1磁time-odd、rank2电time-even变换及C covariance，仍可让两组in-sequence强度不等；所选三步in/cross强度的第二差分符号也可相同或相反。47个旋转/adjoint/time/C/CG与bound控制通过，最大tensor残差约3.4e−15。

这个模型没有核素、intrinsic三角架或局域化波函数；real RME是抽象设计、未知tensor尺度已因子化，**不等于实际one-body M1/E2可以任意取值**。两case改变了数学tensor，因此不是本卡要求的固定H/operator只换configuration，也不是对135Nd的拟合或真实反例。它只阻止把“纯C对称”当成partner B相等/通用staggering的完整证明；实核dynamics仍可能给强而可检验的预报。

在一个额外受限的实L/R kernel中，若M=aI+bσx，B±正比(a±b)²。于是

$$\frac{B_+-B_-}{B_++B_-}=\frac{2ab}{a^2+b^2},\qquad
|b/a|\le\epsilon\le1\ \Longrightarrow\
\left|\frac{B_+-B_-}{B_++B_-}\right|\le\frac{2\epsilon}{1+\epsilon^2}.$$

等强在这里依赖小EM cross-kernel这一额外条件，不能只由能谱小gap为ε赋数。没有真实operator/局域化/混合及Cov，就不把该界转成Qt形变1% CI、physicalg equality gate或模式排他认证。[[mukhopadhyay-2007-135nd-chiral-vibration-static]]的特定强度图样与具体TAC/RPA一致仍是支持链；这个数学边界既不抹掉它，也不验证其原γ/normalizer ledger。仍只有Day24无学分预习。

## Day23内的Day24无学分预习：只换标签、物理混合与矩阵完整性

[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-D24P-004/005将三种动作分开：普通基底变换同时变H、T和态坐标，不改物理矩阵元；固定非简并H的energy-eigenstate relabel只容phases/permutation，不能任意旋混；固定T的真实态混合则要给改变的H，即使能谱被构造为isospectral。不能把一个矩阵旋转自动当成只改configuration assignment已解释同一数据。

固定完整Ii/If子空间时，R→Uf†RUi保Frobenius和singular values、保ΣB的unweighted trace；但只观察两带不证明封闭projector，混入第三态会改变选定块。[[bark-2024-investigations-nuclear-chirality-ithembalabs]] BK24-D24P-001的多带模型只是相关背景，不能当实际135Nd封闭性证据。不同Eγ/parent的率要分别加权，不能把B trace当总光子宽度恒等式。

即使四个B模齐备，相对loop phase仍可能使det/singular values不同；R=((1,2),(3,±4))是确切dimensionless例。它只是数据类型需求，不给实核operator或测得phase。[[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-D24P-008还发现候选完整M1块的反向跨带单元缺数据，其中首个direct transition为上跃；不能设B0凑块。下一检验须同时有正确projector、endpoint/component/normalizer与足够相干信息。特定135Nd手征支持与竞争解释继续并列，不形成统一排他gate；Day24仍无正式信用。

## Day23内的Day24无学分预习：能消单位，不能消身份

[[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-D24P-009/010将同parent、同多极、同核素的WU比保在一个明确范围内：WU/共同τ可相消，Iγ-E³/E⁵比也可作中央算术核对；这些量来自同一adopted评价链，不因此构成独立复测或原分析认证。第一mixed648缺B_M1不填0/δ。

与作者图点/TableI构成的conditional ratio不相同，优先追parent/Jf/component/absolute-vs-selected normalizer及参考版本；不先归因paper错、也不把derived比值当新实测强度。actualmissingEMblock、relativephase和Cov缺口保持。这个检验只提高输入readiness，不给静态手征阈值或g/Qt CI；仍同一个Day24无学分preview。

## Day23内的Day24无学分预习：配对与模型fingerprint的范围

[[qi-2009-135nd-particle-rotor-chirality]] ZH07-D24P-001–004现在接入其Ref26的实际2007 qpPRM原文。M1的uu′+vv′矩阵因子、coreE2取法和单j/BCS模拟多空穴的近似均已按原公式列出；它支持量子PRM对γ/费米面敏感性的模型研究，不等新135Nd/Au实验或原producer复现。

该模型的B(M1)/B(E2)staggering并非跨参数不变，ratio接近也可能掩盖分子/分母各自差异。因而本Day24预习的partner-resolved evidence map仍分开直接能谱/绝对强度、采用的Q0/g/配对、以及模型几何；不能仅按staggering打勾或以derivedratio代两个绝对观测。[[signature-tip-shears-discrimination-contract]]保算符/定标/数据谱系，Day24仍无正式学分、不打开Day25。新增needs_review:true。

## Day23内的Day24无学分预习：配对占据与EM比较的必要输入

[[qi-2009-135nd-particle-rotor-chirality]] ZH07-D24P-005/006以实际方法文参数作单j/BCS组件，显示M1的uu′+vv′是轨道对矩阵而非普遍共同尺度。Δ0/ε=λ还需blocking/占据约定；源pureparticle条件须另保留，不任意填半占据。

这不提供新核带或实际g/B，不能用组件factor范围推partner强度比。partner-resolved map需要完整EM算符、占据、相干/rotor波函数及定标/实验账本，见[[signature-tip-shears-discrimination-contract]]。本节仍Day24无学分预习，新增needs_review:true。

## Day23内的Day24无学分预习：投影闭合与手征证据分层

[[qi-2009-135nd-particle-rotor-chirality]] ZH07-D24P-007用精确四mode Fock例核源BCS的时间奇plus因子；在同约定的时间偶单体算符则得到minus因子。遗漏3qp扇区可携带剩余范数，完整Fock闭合与截断1qp闭合不同，但均不是实验γ分支库存。

这个toy不指定实际核Hamiltonian/EM多极或真实态，不给手征/Kramers双带新认证；T²与C²的既有区别保持。[[signature-tip-shears-discrimination-contract]]承接算符/截断审计，源coreE2不因toy时间偶单体例而自动添加minusfactor。Day24仍无学分，新增needs_review:true。

## Day23内的Day24无学分预习：固定H的有限I谱与几何分层

[[qi-2009-135nd-particle-rotor-chirality]] ZH07-D24P-008/009给一个实际源公式定义的无配对1p+1hole有限I解，D2基/自由转子与solver闭环均已检查。固定参数下最低ordinal gap由I9的约381keV降到I14约37.7再到I18约87.3；它是模型随I变化的谱，不直接对应实际核/模式名。

full-space平方范数给RMS而非带符号平均矢量，低gap/RMS相近也不单独认证左右手局域化、隧穿机制或实验静态手征。后续需同H的概率/EM与其适用条件，见[[signature-tip-shears-discrimination-contract]]；不以某个gap或g阈值建立普遍硬门。Day24仍不授分，新增needs_review:true。

## Day23内的Day24无学分预习：三个边缘概率不是三轴联合取向

[[qi-2009-135nd-particle-rotor-chirality]] ZH07-D24P-010在固定源variant中，将full wavefunction求迹后分别投影到三轴I分量。它比只看RMS多保留了分布形状，但三轴算符不对易，三个峰不能组成唯一经典三维矢量，单轴分布近合也不恢复左右手相干/phase。

该模型I14的中轴分布比另两轴更近；I18能隙更大，部分边缘分布却更近。这里不据此选择实际核模式，只限制把“最小gap/RMS近合”直接当完整geometry结论。[[signature-tip-shears-discrimination-contract]]保model/data与概率/相干矩阵区别，Day24仍不正式计卡，新增needs_review:true。

## Day23内的Day24无学分预习：EM矩阵还需出口与配置标签

[[qi-2009-135nd-particle-rotor-chirality]] ZH07-D24P-011–013在已固定H上补source采用尺度的EM矩阵和独立自由/张量检查；它比marginals多保留了相干算符信息，仍不是实测partner强度或作者pairedproducer。

特殊参数下某些E2近0、强M1在ordinal通道之间变化，不能直接称普遍手征/旋称判据。形式矩阵元可对应向上连接，固定If完整角空间也不等完整γ出口；不同If的M1与E2不能合成某条δ。[[signature-tip-shears-discrimination-contract]]保这些输入身份，新增needs_review:true，Day24无学分。

## Day23内的Day24无学分预习：额外unitary S不等于手征C

[[qi-2009-135nd-particle-rotor-chirality]] ZH07-D24P-014/015的S是特殊H的交换/旋转unitary对称，物理D2扇区内S²=1；它与antiunitaryC的操作类型、以及Kramers T²保护分别处理，不能只看平方或±标签。S分扇区不强迫谱简并，也不单独认证左右手构型。

S-even/odd的modelEM零与强弱关系有明确γ/惯量/谱/配对/算符条件。[[signature-partner-bands]]和[[signature-tip-shears-discrimination-contract]]承接分类与迁移边界，原Pr/Au及其它核正支持链不由此一概否决。新增needs_review:true，Day24仍不授分。

## Day23内的Day24无学分预习：特殊对称性与量子态连续跟踪

[[qi-2009-135nd-particle-rotor-chirality]] ZH07-D24P-016/017给额外S的受控惯量破缺。以overlap连续匹配而非能量排序定义同一个模型态，±ε由S关联，原forbiddenE2随smallε²打开；该结果不提供实际核隧穿率、静态手征分数或实验禁戒显著性。

S被破后不能把其期待值当精确量子数，源模型选择关系也不能升级为普遍fingerprint。[[signature-partner-bands]]和[[signature-tip-shears-discrimination-contract]]区分这个改H实验与configuration-only解释；Day24仍无学分，新needs_review:true。
