# 044：Leander–Larsson1975 的完整 PES 主线及其 133Ce 迁移边界

本单元沿同一 Day24 的 133Ce formalism/参数谱系问题，直接读本篇 PDF1–18（printed93–110）全文主线及 PDF20–21 参考文献；视觉核全部 Figs1–12、Tables1–2、方法数值与作者自限段。PDF19–20 Appendix 的逐式深核由 043 负责，本单元不冒称独立复核了该附录。没有新网络、作者或未知 producer、旧114、模型拟合或数值复现。只写本 worker 与自己的 tmp 前缀，canonical/raw/Git/course/session 均不改。

## 本篇新增了什么

这篇不只是 L78 的 E2 参考文献占位：它完整展示了 MO single-particle 谱、Strutinsky/macroscopic surface、形变空间和 intrinsic static minima 之间的链条，并直接说明**为什么 static PES 的多个 minimum 还不是物理能级和实验形状结论**。对 133Ce 真正可迁移的是输入/算符/坐标与物理判读的合同，而非它为 doubly-even N=Z、A=12–44 选定的数值。

尤其应保留它的负结果与作者自己的限度：40Ca 的实验谱不能由本 PES 直接解释；一个他文的 prolate 8p–8h minimum 在本参数下只是 ledge；轻核 absolute/relative energies 可能有数 MeV 系统误差；有限程 surface 可把同一个 24Mg 反射非对称 minimum 从传统 surface 下约17MeV压到约6MeV。只摘抄 minima 或 triaxial 标签会丢失这一原文证据边界。

## 身份、文件和页码

- G. Leander and S. E. Larsson, “Potential-energy surfaces for the doubly even N=Z nuclei”, *Nuclear Physics A* **239** (1975)93–113，DOI `10.1016/0375-9474(75)91136-7`。
- 直接文件：`tmp/day24-leander1975-039/attachment-object-response.pdf`，21 pages，1,736,708 bytes，SHA256 `35ce50a080755f3a11dac48cfbe2e2041659694038bc6bcaf28b452d72da562d`。
- physical PDF页+92=printed页。本轮仅只读临时原件，不宣称该位置已经构成 canonical/raw 摄入。
- 本地文本/视觉产物：`tmp/day24-leander1975-pes-mainline-044/page01.txt` 至 `page21.txt`；科学主线 rendered `page02.png` 至 `page18.png`；Table2 另有 high render 与上下 crop。PDF有原扫描污损，OCR仅用于定位，本文采用的关键数字经图页复核。

## 实际计算合同：限本篇 N=Z 研究

| 字段 | 本篇直接报告 | locator 与迁移边界 |
|---|---|---|
| 问题与能量 | 12C–44Ti doubly-even N=Z 的形变依赖 static energy；MO 谱给 Strutinsky shell correction，加 macroscopic Coulomb+surface | PDF1/3，printed93/95；不是 odd-A Ce 的 quasiparticle-rotor job |
| surface | Krappe–Nix finite-range Yukawa folding，sharp homogeneous mass distribution；shape-independent 大 volume 项扣去 | PDF3 Eqs2–4；surface选择会改变结果，不可视作与其它 liquid-drop PES 等价 |
| 数值 | `a=1.4fm`、sharp `r0=1.16fm`；`as=24.7MeV`、`κs=4.0` | PDF3 Eqs3–4；这些来自所引 barrier/electron-scattering/macroscopic体系，不是本篇对Ce的拟合 |
| single-particle | deformed harmonic-oscillator basis，9–11 major shells；suppress coupling with `ΔN>4` | PDF4 §2.2；应保留截断条件，不能把“11 shells”表成整个空间已收敛证明 |
| κ/μ | 所研究全部核、protons/neutrons 都取 `κ=.08, μ=.10` | PDF4 Eq6、PDF5末–6首；作者说是球形/形变谱 fits 的 compromise，且可看作 Strutinsky 参数；不是通用参数或Ce input |
| smoothing | Gaussian，`γs=1.6ℏω0`，sixth-degree curvature-correction polynomial | PDF4 Eq7；本篇 plateau 声明不认证任何后来 producer |
| grid/minimization | `(ε,γ)` triangular lattice 85 points；逐点令 `ε4` 在0–.24内变化并最小化能量；`(ε,ε3)` 类似 | PDF4 §2.2；已消元的 higher multipoles、范围及网格都属于 PES 定义 |
| odd multipoles | ε5按 Eq8 选取以使 macroscopic energy 最小；ε1 调整抵消 P3/P5 的质心位移；特定 minima 进一步研究 higher multipoles | PDF4 Eq8；扫描第二系数本单元不作可靠数字转录，043独立核；不能从显示平面误断全部其它形变固定为0 |
| axis/stretched | Eq5 以 stretched coordinates；`γ>30°` 时 P3/P4/P5 绕 y 轴转 `π/2`，使 hexadecapole 对 prolate tips/oblate rim 的作用一致 | PDF3末–4首、PDF8–9 §3.1；同符号 ε4 不保证与其它 convention 同一物理形状 |
| proton/neutron谱 | 省略 single-particle potential 中的 Coulomb contribution，κ/μ相同；time reversal 加p/n相同使每level四重degenerate | PDF2 Fig1后；这解释 quartet 组态记号，不能搬到 N≠Z/odd-A Ce |
| moments尺度 | Table1 microscopic `ℏω0=41 A^(−1/3)MeV`；macroscopic charged liquid drop `r0=1.2fm` | PDF7 Table1 caption；这个1.2与surface的1.16承担不同角色，不得悄悄统一 |

主线没有提供可据以认证2022 GAMPN/ASYMO/PROBMO版本、完整矩阵库或实际 Ce 输出的执行清单。本篇的 explicit single-particle 潜势/shape方法不等于其后来所有应用都采用相同 pairing、g、effective charge、κμ、truncation 或 input 文件。

## 全部图表检查：图像内容和证据类型

| 图表 | physical PDF / printed | 视觉核对的内容 | 证据边界 |
|---|---|---|---|
| Fig1 | 2 /94 | MO neutron(or proton) single-particle energies vs ε，`κ=.08 μ=.10 γ=0 ε4=.08`；某些 nonzero-ε4 导致的 avoided crossings 被有意忽略 | 模型单粒子图，不是实验 many-body level scheme；pure-HO 整数frequency ratio并不保证MO shell gap，作者举3:1处12核子gap被spin-orbit趋于关闭 |
| Fig2 | 6 /98 | spherical MO 与16O/40Ca附近引用实验single-neutron levels、Woods–Saxon levels比较；每组gap中点置零 | 引用实验而非本文新测量；不取作跨核绝对能量基准。作者说MO shell correction为用实验谱所得值的O约80%、Ca约60%，不是“预测精度80/60%” |
| Table1 | 7 /99 | 本文microscopic/macroscopic Q0、Q40，与HF SIII/F1以及由B(E2)、(e,e′)、(α,α′)分析推得的值比较；32S第二min数据用括号 | 模型/模型依赖实验推断分栏；B(E2)给|Q0|、不独立给shape sign；24Mg/32S minima先投到prolate axis；不是triaxial laboratory moment的直接逐点测量 |
| Fig3 | 9 /101 | 20Ne `(ε,γ)` triangle及边界向reflection-asymmetric plane扩展，prolate ground及高形变minima | static model surface；向ground的最低通路可离开reflection-symmetric平面 |
| Table2 | 10 /102 | 全部九核 minima：ε、ε3、ε4、γ、shell-dominated occupation、HO frequency ratio、GS-relative min与barrier能量 | 配置 `(N)^p/(N)^−h`是N oscillator quanta主导level上的粒子/空穴数；两能量列都相对ground min，后一列不能读为已扣除各minimum能量的decay barrier |
| Fig4 | 11 /103 | 24Mg interior ground min、large oblate/triaxial minima，reflection-asymmetric extension | 0–±形变图的多个well不是几条已测band；原文特别指出surface敏感性 |
| Fig5 | 12 /104 | 28Si oblate/prolate低min、higher minima与reflection-asymmetric plane | 作者称其为本篇唯一在oblate/prolate minima间有barrier的核；不外推“所有shape coexistence都要此图拓扑” |
| Fig6 | 13 /105 | 32S弱变形低min与prolate min及higher minima，reflection extension | 原文认为promote quartet到N=3使单sd shell不足；这是作者对模型/旧解释的判断 |
| Fig7 | 14 /106 | 36Ar oblate ground、较高shape-isomeric min及空白/截断区域 | 没画reflection plane按§3.1是对该自由度稳定的作者判断，不是没有研究或实验已禁止 |
| Fig8 | 15 /107 | 40Ca spherical ground、较软oblate side和weak shadow min；大deformation topography | 与单纯prolate8p–8h最低态解释有张力，保留失败 |
| Fig9 | 16 /108 | 44Ti prolate ground、triaxial low minimum及higher regions | 文中仅说low 4p–4h triaxial min可能解释引用1.9MeV0+ |
| Fig10 | 17 /109 | strongly-oblate `ε=1.23 ε4=.24 γ=60°` 的Y33 distortion对MO levels，横轴ε33 | 模型orbital coupling演示；不是直接测得的clustering密度或Ce E2 matrix element |
| Fig11 | 17 /109 | strongly-prolate `ε=1.00 ε4=.10` 的octupole distortion对MO levels，横轴ε3及联动ε5 | N=1耦合在24Mg附近可开gap；不能拿这里slope当Ce actual single-particle matrix |
| Fig12 | 18 /110 | moderately-large quadrupole shape随γ的MO levels；24Mg、40Ca、44Ti相关gap/coupling | γ变化不是实验旋转频率轨迹；框内部分ε/ε4扫描残损，本单元未认证其精确数字，不用邻近PES minima代填 |

§3.1（PDF8–9/100–101）是读图必需合同：cross-hatching 标每minimum周围低区；dashed circles标shallow min准确位置；near saddle/min标的MeV相对ground min。右下角大prolate deformation的basis-truncation严重，较重核该区域留白；边界的mismatch是grid interpolation效应。`ε=1.5,γ=0°`为infinite prolate，`ε=1.5,γ=60°`却仅轴比4:4:1，infinite oblate需`ε=3,γ=60°`。因此这套ε不是可以任意当作β2或轴比的无条件数值。

## 核素逐项主线：模型结果与实验联结分开

以下 Table2 数值只是本篇 static model，单位MeV的能量均相对ground minimum。只列主线所需低minimum，未把高形变每个row转录为新数据集。Table2原扫描保留高分辨crop；任何未选取的详细configuration/ratio请回原表，不能用OCR自动生产全表。

| 核 | 视觉核实的 Table2 低minimum字段 `(ε,ε3,ε4,γ)` | 本文解释及引用实验的范围 |
|---|---|---|
| 12C | ground `(.83,0,.20,60°)`；prolate excited `(1.11,0,.24,0°)` | PDF11/14：熟知oblate ground/prolate excited；PES未画。作者将3:1构型同约8MeV谱联系（Refs39/40的链），不是本文实验形状测量 |
| 16O | ground `(0,0,0,0°)`；triaxial `(1.04,0,.24,43°)`；prolate `(1.2,0,.24,0°)` | PDF11：本计算比所引Ref26激发形变更大、能量更低，归因modified-surface softness；PDF14把4:1构型与约17MeV联结；physical-state/ZPE问题尤其重要 |
| 20Ne | ground `(.40,0,−.10,0°)`；large triaxial `(1.17,0,.24,50°)`，min9/barrier14 | PDF11–12：prolate ground；highly-deformed8p–4h被认为关联引用`0+7.20MeV`，believed-to-be不能改成已确定assignment；lowest path可走reflection-asymmetric形状 |
| 24Mg | ground `(.45,0,.08,20°)`；reflection `(1.0,.3,.20,0°)` min约6/barrier12.5；oblate `(1.23,0,.24,60°)`；triaxial `(1.26,0,.24,42°)` | PDF14–15：interior ground与HF一致；其余low isomeric min是计算。oblate对Y33仅slightly unstable，加入macro代价后weak ternary min，只提出六α平面三角构型的可能性 |
| 28Si | ground `(.49,0,.06,60°)`；prolate `(.45,0,.16,0°)` min1/barrier1.5 | PDF15：oblate略低与引用实验一致；其余min需多quartet intershell excitation且较高；作者引用sd-shell模型声称复现到10MeV |
| 32S | ground `(.21,0,.08,20°)`；prolate `(.68,0,.08,0°)` min.1/barrier4.5 | PDF16：prolate需quartet进N=3，作者据此反对仅sd-shell足够的旧解释，并认为可解释coexistence phenomenology的相对成功；PDF7–8称ground Q与约8% core-excited admixture consistent，是模型依赖推断 |
| 36Ar | ground `(.29,0,.16,60°)`；excited `(.74,0,.16,7°)` min9/barrier11 | PDF16：较高shape-isomeric min；引用7MeV以下positive-parity spectrum可由sd模型解释，以及HFB解释I(I+1)偏离；均不是本文独立实验或新HFB计算 |
| 40Ca | ground `(0,0,0,0°)`；shadow/triaxial `(.45,0,.16,50°)` min9/barrier10.5 | PDF16–17：本PES不能现成解释谱。Ref49选另一κ/μ得到的prolate8p–8h minimum，在此仅为ε=.55的ledge；oblate软并加largeε4/γ才有shadow min。model binding比实验过多`9–13MeV`（依mass formula），作者借大ZPE来讨论与引用0+3.35MeV的关联；3He/(p,t)的结构证据只由其引Refs50/51，本轮未独立读 |
| 44Ti | ground `(.18,0,0,0°)`；triaxial `(.52,0,.16,38°)` min3/barrier5.5 | PDF18：low4p–4h triaxial min“possible explanation”引用core-excited0+1.9MeV（Refs52/53）；模型3MeV不改写为实验1.9MeV的预测精确符合 |

Table1 另给出较接近ground-state collectivity的比较，而非纯拓扑：24Mg的Q0 microscopic/macroscopic均64fm²，引用B(E2)推得64.2±1.1fm²；20Ne为52/54与56.4±2.7；32S主min43/42、第二min(192)/(193)，所引B(E2)推得54.3±1.2。作者用32S这一差别讨论admixture，而不是说每个minimum单独等于实验ground state。散射与B(E2)列有不同模型、误差、sign信息和引用来源，不能并成多份独立直接Q测量。Q40还有本篇Eq11的`1/Z`定义，须先保完整字典再与其它文献同名Q比较。

## orbital coupling 的可复用机制及不能外推的部分

PDF12–15/104–107 将形状不稳定性与near-Fermi orbital coupling联系：reflection-asymmetric轴向项耦合`[N nz Λ Ω]`到`[N+1,nz+1,Λ,Ω]`；triaxial项耦合`[N nz Λ Ω]`到`[N,nz,Λ+2,Ω+2]`；Y33项耦合`[N nz Λ Ω]`到`[N+1,nz,Λ+3,Ω+3]`。能否获shell energy取决于实际orbitals间距和Fermi位置，不只是selection rule允许。

例如同样的octupole机制在24Mg比20Ne强，作者归因ε3=0处levels更接近；Y33在prolate低N轨道影响小，在large-oblate时ω⊥变小、相关orbitals靠近才可能有效。将α-like density/potential maxima与cluster构型联结时，作者自己指出若把α-clustering定义为repulsive p-state force的后果，这些MO maxima可能部分是coincidence。故可以迁移“必须查near-Fermi level位置/耦合/总macro代价”的研究判据，不能把轻核α cluster、这几个Nilsson标号、frequency ratios或minima直接当作Ce结构。

pure HO的整数ratio只是shell结构动机：本篇PDF2已提醒spin-orbit会改变甚至关gap；PDF9说HO还预测许多根本未在MO PES出现的minima。跨paper比较要分别检查potential、spin-orbit/orbit-orbit、deformation coordinates、填充、higher-multipole minimization和macro项，不以“同MO谱系”替代actual参数。

## 作者自己的可靠性/collectivity限制，必须随结论保留

1. **模型误差不是只剩网格误差。** PDF4–5 §2.3：40Ca的HF信息提示，一阶density fluctuation shell correction之外的二阶/高阶贡献相当大；Strutinsky忽略可造成数MeV误差。本篇宣称所有考虑形变满足plateau，并用pure-HO解析shell correction作部分检验；但很大prolate deformation有差别，作者归因可能的truncation。plateau不消除宏观/平均场系统误差。
2. **重核校准的macro项不能自动保证轻核能量。** PDF5：liquid-drop参数原拟合ground masses/heavy fission barriers，能否准确给light-nucleus deformation energy仍待HF检验；远隔形变的minima相对高差尤其可有严重系统偏差。finite-range a=1.4fm可能过大，使lightest nuclei过软、高multipoles过量并出现unphysical wiggles；large-prolate时更严重。24Mg6→17MeV的surface对比是明确敏感性例，不是统计error bar。
3. **“topology probably correct”是作者评估。** PDF4–6：作者认为minima可能对应正确single-particle configurations和大致正确deformations，relative heights却在许多情形不准。这不是实验验证所有minima存在，也不是本任务授予高置信度。
4. **static intrinsic energy不等于Jπ-resolved spectrum。** PDF8：PES画核子占据最低可用orbitals的intrinsic static energy；physical states须projection或假设adiabaticity并采用collective rotations/vibrations。collective theory在light nuclei不足以作详细描述，作者只认为较低spin、尤其bandheads可能仍有部分有效性。其“低spin”没有提供适用于Ce的通用数值阈值。
5. **bandhead高差只能粗估。** 同页列三点：PES固有误差；collective zero-point energy可能很大（16O/40Ca spherical wells尤其）；states非pure，0p–0h与4p–4h可经更高2p–2h由two-body operators连接，且不同deformed bases可能略non-orthogonal。不能把每个minimum视作自动正交的观察态，也不能由well图直接恢复mixing matrix或lifetime。
6. **结尾主动收窄。** PDF18/110最后段明确称对计算PES作任何直接解释都相当speculative，价值是确认若干熟知结果并提示更详细计算的方向。本报告保留其模型/引用实验/作者解释标签，不将这种历史讨论改成2026已裁决结论。

## 给 133Ce formalism/参数谱系的最小写回建议

可把本篇新增source定位为：L78所指的single-particle算符/shape方法原件，同时拥有自己N=Z轻核PES应用；043另提供Appendix的可恢复算符合同。本单元建议只提升三个长期知识增量：

- 同一历史MO方法引用链不确定actual2022 producer：κμ、space、smoothing、finite-range macro、higher-multipole minimization、轴/坐标、moment convention和占据须逐字段核。
- static PES minima的物理判读须projection/collective dynamics、ZPE与mixing；地形topology、intrinsic configuration和experimental band/shape证据分层，保留40Ca失败与24Mg surface敏感例。
- 跨mass transfer可以迁移orbitals-near-Fermi/coupling与total-energy-cost的检验逻辑，不迁移A12–44的κ=.08/μ=.10、quartet/p=n degeneracy、α结构、minima数值或light-mass collectivity假设到odd133Ce。

本单元 self-audit 后关键claims均有原页locator，未独立核引用实验/其它模型原件，扫描残损的Eq8系数和Fig12框内数值保留needs_review而非猜填。停止原因：分配的mainline与全部图表已读完，进一步actual Ce判断需要另一证据对象；不制造toy/test或开启新课。父任务可按最小增量写回canonical并与043逐式报告衔接。
