---
type: source
title: "W. D. Hamilton 1975 - The Electromagnetic Interaction in Nuclear Spectroscopy"
aliases: [Hamilton1975, Hamilton电磁相互作用, 电磁跃迁核谱学圣经]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: deep-read
title_original: "The Electromagnetic Interaction in Nuclear Spectroscopy"
authors: [W. D. Hamilton (editor)]
publisher: "North-Holland Publishing Company / American Elsevier"
year: 1975
pages: "956"
isbn: "0720402747"
canonical_source: "W. D. Hamilton (ed.), The Electromagnetic Interaction in Nuclear Spectroscopy, North-Holland (1975)"
library_file: "raw/books/The Electromagnetic Interaction In Nuclear Spectroscopy.pdf"
raw_file: "raw/books/The Electromagnetic Interaction In Nuclear Spectroscopy.pdf"
raw_sha256: "93b32a8debb66ad036229d860ad56f0434dc49b56edd32f1628af1d71a21ae00"
nuclei: []
reactions: [in-beam-gamma, coulomb-excitation, radioactive-decay]
experiments: []
models: [orientation-parameters, angular-distribution, directional-correlation, polarization-correlation]
topics: [bk-parameters, ak-coefficients, f-coefficients, u-coefficients, mixing-ratio-delta, dual-root-solution]
---

# W. D. Hamilton 1975 - The Electromagnetic Interaction in Nuclear Spectroscopy

## Key Results

| ID | 陈述与物理内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HAM-1 | 定向核态张量与光子角分布展开：定向核态发射光子的角分布表象为 $W(\theta) = 1 + A_2 P_2(\cos\theta) + A_4 P_4(\cos\theta)$，其中各向异性展开系数分解为初态统计取向张量 $B_k(I_i)$ 与跃迁多极几何因子 $R_k(L L' I_i I_f)$ 的乘积。 | model-result | direct | Ch. 12, pp. 505–550 | false |
| HAM-2 | 未观测中间级联去取向系数 $U_k$：经由未观测多极跃迁 $I_1 \xrightarrow{L} I_2$ 级联退激时，核取向张量严格按 Wigner $6j$ 符号衰减 $B_k(I_2) = B_k(I_1) U_k(I_1, I_2, L)$，其中 $U_k = (-1)^{I_1+I_2+L+k}\sqrt{(2I_1+1)(2I_2+1)}\{I_1 I_1 k; I_2 I_2 L\}$；严格满足总几率守恒 $U_0 \equiv 1$ 与各向异性衰减 $U_k < 1.0$。 | model-result | direct | Ch. 14, pp. 580–625 | false |
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
