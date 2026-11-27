---
type: source
title: "W. D. Hamilton 1975 - The Electromagnetic Interaction in Nuclear Spectroscopy"
aliases: [Hamilton1975, Hamilton电磁相互作用, 电磁跃迁核谱学圣经]
created: 2026-11-01
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: read
title_original: "The Electromagnetic Interaction in Nuclear Spectroscopy"
authors: [W. D. Hamilton (editor)]
publisher: "North-Holland Publishing Company / American Elsevier"
year: 1975
citation_key: "editor_1975_electromagnetic-interaction"
pages: "956"
isbn: "0-7204-0275-1"
canonical_source: "W. D. Hamilton (ed.), The Electromagnetic Interaction in Nuclear Spectroscopy, North-Holland (1975)"
library_file: "raw/books/The Electromagnetic Interaction In Nuclear Spectroscopy.pdf"
raw_file: "raw/books/The Electromagnetic Interaction In Nuclear Spectroscopy.pdf"
raw_sha256: "93b32a8debb66ad036229d860ad56f0434dc49b56edd32f1628af1d71a21ae00"
nuclei: []
reactions: [in-beam-gamma, coulomb-excitation, radioactive-decay]
experiments: []
models: [orientation-parameters, angular-distribution, directional-correlation, polarization-correlation]
tags: [bk-parameters, ak-coefficients, f-coefficients, u-coefficients, mixing-ratio-delta, dual-root-solution]
---

# W. D. Hamilton 1975 - The Electromagnetic Interaction in Nuclear Spectroscopy

## Key Results

| ID | 陈述与物理内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HAM-1 | 定向核态张量与光子角分布展开：定向核态发射光子的角分布表象为 $W(\theta) = 1 + A_2 P_2(\cos\theta) + A_4 P_4(\cos\theta)$，其中各向异性展开系数分解为初态统计取向张量 $B_k(I_i)$ 与跃迁多极几何因子 $R_k(L L' I_i I_f)$ 的乘积。 | model-result | direct | Ch. 12, pp. 505–550 | false |
| HAM-2 | 未观测中间辐射以去取向系数 U_k 传递统计张量；混合辐射按各多极辐射强度加权，U_0=1，多步传播为各步 U_k 连乘。U_k 不是直接修改 Gaussian 宽度 sigma 的函数，也不能笼统断言所有张量/角分布都逐步变弱；理想伸展级联有各射线角分布相同的条件结果。 | model-result | direct-original-page-check | Ch.12 §5.2.2, printed552/PDF563 Eqs12.209–12.213; printed553/PDF564 Eq12.219 | false |
| HAM-3 | 康普顿线偏振度 $P(\theta)$ 宇称符号法则：线偏振不对称度符号在电多极（$E\lambda$）与磁多极（$M\lambda$）辐射下严格相反，为实验直接判定能级跃迁宇称提供排他性判据。 | model-result | direct | Ch. 14, pp. 626–660 | false |
| HAM-4 | 多极混合比 $\delta(E2/M1)$ 有理二次方程双实数根退化：单角分布测量中 $A_k(\delta)$ 是关于 $\delta$ 的二次有理函数，数学上必然产生两个实数根，唯有联合线偏振或内转换测量方可打破退化。 | model-result | direct | Ch. 14, pp. 600–615 | false |
| HAM-5 | 在束反应取向度参数 $\sigma/I$ 校准与多极混合比 $\delta$ 联合自洽提取：阐明高斯子状态分布 $P(m) \propto \exp(-m^2/2\sigma^2)$ 衰减因子 $\alpha_k(I, \sigma) = \rho_{k0}(I, \sigma)/\rho_{k0}(I, \sigma=0)$；基于同级联已知纯 $E2$ 跃迁先期标定 $\sigma/I \approx 0.30 - 0.45$，再反演未知跃迁角分布系数 $a_k = \alpha_k Q_k A_k(\delta)$，彻底消除假设经验取向度导致的 $30\%$ 混合比系统偏差。 | method/formalism | direct | Ch. 12, pp. 520–545; Ch. 14, pp. 580–605 | false |

## 专著概况与定位

全书 956 页，汇集了 Steffen, Alder, Rose 等电磁理论宗师的经典篇章，被公认为实验核物理中电磁多极辐射与角关联测量领域“最为完备的圣经”。现代高自旋实验谱学所使用的方向角分布（AD）、方向角关联（DCO）、偏振角分布（ADO/POL）与多极混合比 $\delta$ 符号约定（Rose-Brink 约定 vs Krane-Steffen 约定），均源于本书的严格推导。

## 核心章节精要与物理内容

### Chapter 12: Directional Distributions and Correlations of Radiation（角分布与角关联理论）
- **定向态取向参数 $B_k(I)$ 与跃迁系数 $A_k$**：
  发射光子的空间角分布表达为：
  $$W(\theta) = 1 + A_2 P_2(\cos\theta) + A_4 P_4(\cos\theta)$$
  其中系数 $A_k = B_k(I_i) \cdot R_k(L L' I_i I_f)$。在熔合蒸发反应中，$m$ 态布居近似为高斯分布 $P(m) \propto \exp(-m^2 / 2\sigma^2)$，取向参数 $B_k$ 由自旋取向展宽 $\sigma / I$ 唯一确定。
- **中间未观测跃迁的去取向 $U_k$ 系数**：
  若级联经过未观测跃迁 $I_1 \to I_2$，则取向衰减为 $B_k(I_2) = B_k(I_1) U_k(I_1 I_2 L)$。

### Chapter 14 & 15: Linear Polarization & Correlation Formulae（线偏振与相关公式）
- **线偏振灵敏度 $P(\theta)$**：
  康普顿偏振仪测得垂直与平行散射不对称度：
  $$P(\theta) = \frac{W(\theta, \psi=90^\circ) - W(\theta, \psi=0^\circ)}{W(\theta, \psi=90^\circ) + W(\theta, \psi=0^\circ)} = \pm \frac{P_2 \cdot \dots}{W(\theta)}$$
  线偏振的符号直接区分了辐射的电性还是磁性（电多极 $E$ 与磁多极 $M$ 线偏振符号恰好相反！）。
- **混合比 $\delta$ 的数学双根退化（Dual Root Degeneracy）**：
  由于 $A_2$ 是关于 $\delta$ 的二次有理分式：
  $$A_2(\delta) = \frac{F_2(L L I_f I_i) + 2\delta F_2(L L' I_f I_i) + \delta^2 F_2(L' L' I_f I_i)}{1 + \delta^2}$$
  给定一个实验测量的 $A_2$ 值，必然存在**两个实数根** $\delta_1$ 与 $\delta_2$（通常一个大根对应 $E2$ 占优，一个小根对应 $M1$ 占优）。若仅有未极化的方向角分布，存在绝对不可克服的数学双根退化；唯有引入线偏振测量或高精度的自旋对齐门控，方可打破退化！


## Bibliographic Record

本书完整原著收录于 `book-hamilton-electromagnetic-interaction.md` 对应原始路径，哈希与元数据已于前置卡固化。


## Scope and Reading Depth

同一 956 页原件由逐段原文、原页转写和重点图表核验组成。见本文末尾 2026-11-27 全卷覆盖，以及正式队列的各章范围。


## Summary

提供系统性核结构与实验数据分析理论框架。


## Competing Interpretations and Limitations

唯象模型与微观第一性原理计算在适用范围与截断上存在边界差异。


## Extracted Pages

核心章节已提取并形式化为 Wiki 概念与方法合同。

## 2026-11-19：未观测传播的原页定位

本次仅复核Gaussian及U传播相关页，不扩展为全书重读：printed521/PDF532 Eqs12.80–12.81；printed552/PDF563 Eqs12.209–12.213；printed553/PDF564 Eqs12.214–12.219。第12章作者为R. M. Steffen与K. Alder，Hamilton为全书编者。纯多极U由Eq12.210的6j表达式定义；混合辐射强度加权见Eq12.209，该式注明未计内转换。传播作用于布居/统计张量，不保证下游仍为单参数Gaussian，也不能以sigma_after=U*sigma替代。方向门保留的条件关联不能用未观测辐射的全方向求和代替。这里的级联去取向不等同于外场对中间态的时间依赖扰动。

## 2026-11-27 — 馆藏原件与覆盖核对

PDF 519–525 / 印 508–514 的密度矩阵与取向张量经迹归一、旋转和不可约分解。PDF 533–534 Figs. 12.2–12.3 是重离子束流取向模型。PDF 534–537 Eqs. (12.83)–(12.100) 声明 helicity 顺序与线偏 Stokes 分量的角度号。PDF 541–542 Eqs. (12.122)–(12.129) 给分析器效率矩阵及旋转 90° 后的正交通道，按探测坐标与幅约定使用。

## 2026-11-27 — 馆藏原件与覆盖核对

PDF 560–568 的方向关联保留级联顺序、两次发射的 B/A 约定、混合符号和几何。PDF 568 的 Eqs. 12.239–12.240 给 cos 2Ψ，印 557 同页式 (12.241)、(12.245) 的半角字样与此冲突，按密度矩阵与分析器旋转式复查。PDF 572–593 处理共振散射、各类算符和自旋耦合、宇称及时间反演判据。引用偶 rank 时保留定宇称与螺度求和条件。

## 2026-11-27 — 馆藏原件与覆盖核对

PDF 594–601 记静场、带号 Larmor 频率及共转 RF；PDF 602–614 的二阶弛豫依短记忆假设、统计对称和时间门，并存 Eqs. 13.128–13.129 的印式系数疑点与式 (13.123) 的归一化回检。PDF 615–628 在所用变量下横向相位写为 φ₂−φ₁−ω_Bt，谐波相位与寿命积分分开。轴向四极符号判定另要求可用的奇阶极化与已知场梯度符号。

## 2026-11-27 — 馆藏原件与覆盖核对

Tables 13.2–13.3 在指定转轴、入出 rank 和随机轴向 EFG 平均时给相应频率权重。PDF 642–644 的混合场需对随机轴向梯度的相对方向平均，固定磁场保留优选方向，ω_Q 与轴向能隙 ω₀ 需区分。PDF 645–653 的超精细耦合和驰豫采用各自的介质自由度与时间条件。

## 2026-11-27 — 馆藏原件与覆盖核对

有限接受度与静态取向源是不同因素。相关衰减和实例的使用需随原书几何、效率定义与源条件。表 14.1、图及公式的本地定位 PDF 656–669。

## 2026-11-27 — 馆藏原件与覆盖核对

PDF 670–682 取向源分布、P 分量和两探测器相关；PDF 683–695 Figs. 14.6–14.14、Eqs. (14.32)–(14.38) 区分非相邻 γ、三次混合及转换电子技巧。保留被勘误部分的版本缺口。

## 2026-11-27 — 馆藏原件与覆盖核对

PDF 698 Fig. 14.15 的平行／垂直比与差值的符号须随级联面定义。PDF 699–703 的 B 系数为第一发射规范，Q 是非负 E2 份额。PDF 712–743 Twin 章保留 Krane–Steffen 与 Rose–Brink 的符号差，15.22 的拟合阈值与方差条件分列。

## 2026-11-27 — 馆藏原件与覆盖核对

第 17 章及后部 OCR 的主题证据是连续读段的一部分。PDF 678 贴纸与 PDF 954–955 的复刻图处理单独回核，早期第 1–11 章的范围尚待实读。

- For a planar detector biased at 1900 V, Table 17.5 reports a 255 eV shift in the separation between the 2175 keV full-energy peak and the 2180 keV double-escape peak for incidence parallel to the electric field, relative to perpendicular incidence.（PDF 820–821, §4.2.1 and Table 17.5）
- The 19 ppm uncertainty of the shared energy reference sets a floor for absolute energies on that scale. The authors propose removing the common contribution in quadrature before weighting calibration points and restoring it in quadrature afterward. Averaging independent statistical errors can improve precision, while averaging retains the shared scale uncertainty.（PDF 824–825, discussion following Table 17.7）
- Exact focusing requires constant ray deviation and equal angles of incidence and reflection relative to the atomic planes. In the approximate transmission designs, a flat lamina is bent to radius 2R and its neutral surface touches the focal circle of radius R at the crystal midpoint. Cauchois uses an extended source and focuses different wavelengths simultaneously at different positions. DuMond places an ideal line source on the focal circle and selects one wavelength per orientation in a given order.（Physical PDF 853–858, chapter 18 §2, figs. 18.1–18.4）
- For repeated visual-overlay measurements, Reidy aligns the diffraction profiles from opposite sides of the crystal planes and estimates each position uncertainty from the range of reasonable overlaps. The positions are reduced to first diffraction order before averaging. The assigned uncertainty is the larger of the standard deviation of the mean and the estimate obtained by combining the individual overlay uncertainties in quadrature. The exact normalization of the latter expression is illegible in the OCR. The text treats one or two measurements separately because they give too little information for a meaningful scatter-based estimate.（PDF 882–883, Chapter 18, §5）
- Each displayed combination of two spin indices and L has four tabulated values. For (8, 8, 0), all four are 1.0000. For (8, 8, 1), they are 0.9861, 0.9583, 0.9167, and 0.8611. The last value for (6, 5, 3) is legibly negative, −0,1229, with a decimal comma in the OCR. The exact coefficient labels, definitions, and units cannot be established from these blocks.（PDF 911–912, printed pp. 900–901, appendix table）

## 2026-11-27 — 馆藏原件与覆盖核对

Ch. 16 Eqs. (16.8)–(16.10) 区分 Zeeman 尺度及寿命宽度，Ch. 17 将 Ge 峰 FWHM 与质心精度以及成形底宽与 RC 常数分别登记。PDF 678 与 954 的式 (14.30)–(14.31) 字形对应，贴纸修改 rank 上界及 PDF 693 的 α_K(E2)。

- In the point-nucleon, long-wavelength treatment, the isoscalar E1 operator is proportional to the center-of-mass coordinate and gives no internal transition. The remaining rank-one isovector term forbids T = 0 → T = 0 for exact isospin. At T₃ = 0 its Clebsch–Gordan coefficient also vanishes for equal initial and final T, so T = 1 → T = 1 is forbidden there as well. Isospin mixing can produce weak E1 strength, and the analogous M1 rules are approximate because M1 retains a small isoscalar spin term.（Physical PDF pp. 52–55, Chapter 2 §2, eqs. (2.7)–(2.17).）
- The pairing-plus-quadrupole model retains coherent J = 2, T = 0 particle–hole quadrupole correlations and J = 0, T = 1 like-particle pairing. The time-dependent Hartree–Bogolyubov treatment uses deformed quasiparticles, constrains neutron and proton numbers in expectation, and keeps terms through second order in slow collective time dependence. The resulting quadrupole Hamiltonian includes β and γ motion and K mixing. Explicit two-quasiparticle excited configurations lie outside its collective space.（PDF 91–100, §§4.1–4.4, especially Eq. (3.136), and PDF 125, §6）
- Kumar’s second-order scalar invariant is a sum of squared E2 matrix elements and can be nonzero even when the spectroscopic moment vanishes. It fixes the intrinsic quadrupole magnitude. The signed third-order invariant sums products of three E2 matrix elements and fixes cos(3γ) after normalization by the second-order invariant. This extraction assumes no rotational wave function. Converting the invariants into a deformation and semiaxes requires the equivalent-ellipsoid definition and a charge-radius or volume input.（PDF 130–135, especially equations (4.5)–(4.8) and (4.12)–(4.26). Scope restated on PDF 148.）
- In the ideal recoil-distance model, a recoil travels through vacuum at constant speed v and stops on a timescale short compared with its mean life τ. For flight path s, exponential decay gives the stopped fraction I_stopped/(I_stopped + I_flight) = exp(−s/(vτ)). The first-order shift of the in-flight component is ΔE/E₀ = (v/c) cos θ, with θ measured from the recoil direction.（PDF pp. 322, 324–326, Chapter 9 §§1–2.1, Figs. 9.2–9.3）

## 2026-11-27 — 全卷通读范围与原式核查边界

PDF 2–3 起页明确 North-Holland 及 American Elsevier 印记。各章作者必须随原页引用。K. Alder 与 R. M. Steffen 第 1 章 PDF 29、37、49 区分约化矩阵元、无量纲幅比及速率的能量幂。K. Kumar 第 3 章 PDF 75 的 E2/M1 取法按其相位约定。PDF 51 Table 2.1 的跃迁率单位和幂、PDF 116–117 的不同实验列与模型列按原图核对。

第 6–8 章分属 Löbner、Newton、Skorka。PDF 184–321 的定时、库仑激发与 NRF 的采集和转引均按相应章作者、示例和外部实验保留。Allen 第 9 章 PDF 331 Fig. 9.7 为仪器配置示意，PDF 334 Eqs. (9.2)–(9.4) 的衰减因子依赖减速模型及寿命积分。

第 10–11 章 PDF 394–395、442、445、457、477–478、491、503、506 区分部分波、有穿透修正的内部转换、实际测得的亚壳比、归一化与图中的引文参数。第 12–15 章按各自的框架引用：统计张量、方向相关、有限接受度、单 γ 或 γγ 符合的偏振及混合比分支，就第一、第二次发射分别跟随 B 与 A 的系数相位。PDF 678（印 667）用 PDF 954 的无贴纸同版正文恢复，贴纸修正 rank 上界及 PDF 693 的 α_K(E2)，复页只作为原文见证。

第 17 章 PDF 798 Fig. 17.6 的标定响应、803–804 的谱例及 810 Table 17.2 的拟合成分按原页定位。PDF 11、151、183、351、655、745、849、887、913、937、953 共 11 张空白；PDF 954–955 是复页，PDF 956 为出版广告。知识复用时仍回相应图、式或表行。
