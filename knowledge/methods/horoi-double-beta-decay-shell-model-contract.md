---
type: method
title: "Horoi：双贝塔衰变壳模型核矩阵元、闭合近似与 Lanczos 加速算法合同"
aliases: [Horoi double beta decay, 0vbb shell model NME, 2vbb Lanczos doorway algorithm, optimal closure energy, LNV mechanism discrimination]
method_type: "double-beta-decay-shell-model-calculation-contract"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Nuclear Shell Model 70 Years article 13, full main-text reading"
confidence: "high for formalisms and review comparisons; conditional for specific model parameters"
tags: [shell-model, double-beta-decay, 0vbb, 2vbb, nme, closure-approximation, lanczos-algorithm, ga-quenching, lnv-mechanisms]
sources: [book-nuclear-shell-model-70-years]
---

# Horoi：双贝塔衰变壳模型核矩阵元、闭合近似与 Lanczos 加速算法合同

## Purpose

这篇综述系统总结了相互作用壳模型（Interacting Shell Model, ISM）在双贝塔衰变
（包括无中微子双贝塔衰变 \(0\nu\beta\beta\) 和双中微子双贝塔衰变 \(2\nu\beta\beta\)）核矩阵元
（Nuclear Matrix Element, NME）计算中的理论方法、算法突破与物理分析框架。
核心关注点包括：

1. \(0\nu\beta\beta\) 衰变中多种轻子数破坏（LNV）机制（轻马约拉纳中微子交换、重右手中微子、超对称 \(R\) 宇称破缺、左右对称模型的 \(\lambda\) 与 \(\eta\) 机制）的有效哈密顿量与 NME 对应；
2. 闭合近似（Closure approximation）的有效性条件、误差尺度（典型约 10%）以及模型空间与有效相互作用特定的“最优闭合能量”（Optimal closure energies）；
3. 规避高维两体跃迁密度（TBTD）计算的 Lanczos 等位旋投影加速技巧；
4. \(2\nu\beta\beta\) 衰变中超越闭合近似的门态（Doorway-state）Lanczos 谱函数快速求和算法（相较于显式直接对角化中间核几百个 \(1^+\) 态，计算效率提高近 1000 倍）；
5. 利用多核素（如 \(^{76}\mathrm{Ge}, {}^{82}\mathrm{Se}, {}^{130}\mathrm{Te}, {}^{136}\mathrm{Xe}\)）半衰期比值与双电子能谱/角分布解耦不同 LNV 产生机制的分析蓝本；
6. 轴矢量弱荷 \(g_A\) 淬灭（Quenching）在 \(2\nu\beta\beta\)（需要 \(q\sim 0.6\)–\(0.74\)）与 \(0\nu\beta\beta\)（动量转移高，通常取无淬灭）中的物理区分。

## Inputs and Assumptions

### Generalized LNV decay rate formula

结合左右对称模型与 \(R\) 宇称破缺超对称模型，\(0\nu\beta\beta\) 半衰期可写为相空间因子（PSF）、LNV 参数与对应 NME 的综合表达式：

\[
\left[T_{1/2}^{0\nu}\right]^{-1}
= G_{01} g_A^4 \left| \eta_{0\nu} M^{0\nu} + \eta_{0N} M^{0N} + \eta_{\tilde q} M_{\tilde q} + \eta_{\lambda'} M_{\lambda'} + \eta_\lambda X_\lambda + \eta_\eta X_\eta \right|^2 ,
\]

其中 \(G_{01}\) 为考虑子核电荷分布有限尺寸效应的高精度相空间因子，\(g_A\) 为轴矢量耦合常数，\(\eta_{0\nu} = \langle m_{\beta\beta}\rangle / m_e\) 为有效马约拉纳中微子质量参数。
在单一主导机制假设下，若仅考虑标准的轻左手中微子交换机制（质量机制），半衰期公式简化为经典的：

\[
\left[T_{1/2}^{0\nu}\right]^{-1}
= G_{01} g_A^4 \left(\frac{\langle m_{\beta\beta}\rangle}{m_e}\right)^2 |M^{0\nu}|^2 .
\]

### NME operator structure and intermediate state sum

对初态 \(|0_i^+\rangle\) 到末态 \(|0_f^+\rangle\) 的跃迁，NME 在理论上表示为对中间核 \((Z-1, N-1)\) 中间态 \(|\kappa\rangle = |J_\kappa^\pi\rangle\) 的显式求和：

\[
M_\alpha^{0\nu} = \sum_\kappa \sum_{1234} \langle 13 \vert O_\alpha \vert 24 \rangle \langle f \vert c_3^\dagger c_4 \vert \kappa \rangle \langle \kappa \vert c_1^\dagger c_2 \vert i\rangle ,
\]

其中 \(O_\alpha\)（\(\alpha = \text{GT}, \text{F}, \text{T}\)）包含中微子势 \(H_\alpha(r, E_\kappa)\)、自旋/同位旋算符以及有限核子尺寸（FNS）与短程关联（SRC，如 CD-Bonn 或 Argonne）修正。

### Closure approximation and optimal closure energy

由于虚中微子动量尺度高达 \(q \sim 100\)–\(200\text{ MeV}/c\)，远大于中间态核激发能（\(\sim 10\text{ MeV}\)），可用平均闭合能量 \(\langle E \rangle\) 替代各态能量 \(E_\kappa\)。
利用完全性条件 \(\sum_\kappa  \vert \kappa\rangle\langle \kappa \vert = 1\)，NME 简化为初末态两体跃迁密度（TBTD）与反对称两体矩阵元的乘积：

\[
M_\alpha^{0\nu} = \sum_{j_p j_p' j_n j_n' J^\pi} \text{TBTD}(j_p j_p', j_n j_n'; J^\pi) \langle j_p j_p'; J^\pi T \vert \tau_-^{(1)}\tau_-^{(2)} O_{12}^\alpha(\langle E  \rangle) | j_n j_n'; J^\pi T\rangle .
\]

闭合近似在 \(0\nu\beta\beta\) 中精度优于 10%，但对于 \(2\nu\beta\beta\) 衰变（动量转移极低，\(\sim \text{MeV}\)），闭合近似完全失效。

## What It Can Establish

### 1. 规避 TBTD 的 Lanczos 等位旋投影算法

传统大空间壳模型代码（如 J-scheme 或 M-scheme）直接生成高维两体跃迁密度（TBTD）非常耗时且占用巨大存储。
Horoi 提出的加速算法利用核相互作用的近似同位旋对称性：

1. 利用 Wigner–Eckart 定理，将引起同位旋跃迁 \(\Delta T_z = -2\) 的两体算符转换为保持球对称但破坏同位旋的等效哈密顿量分量 \(H_{\beta\beta}^\alpha\)；
2. 将高同位旋母核基态 \(|0_i^+ \langle T_>\rangle\rangle\) 的同位旋投影降低 2 个单位，使其成为子核同位旋多重态中的类似态（IAS）\(|0_i^+ \langle T_<\rangle\rangle\)（其中 \(T_< = T_> - 2\)）；
3. 将该态作为初始 Lanczos 向量，仅执行**一次** Lanczos 迭代：
   \[
   H_{\beta\beta}^\alpha |0_i^+ \langle T_<\rangle\rangle = a_1  \vert 0_i^+ \langle T_<\rangle\rangle + b_1  \vert L_1 \rangle ;
   \]
4. 跃迁矩阵元即简化为子核真实基态与新 Lanczos 矢量的重叠乘积：
   \[
   M_\alpha^{0\nu}(T_z = T_<) = b_1 \langle 0_f^+ T_<  \vert L_1\rangle ,
   \]
   最后通过同位旋 Clebsch–Gordan 系数还原真实矩阵元。

该技巧将原本需要完整计算和存储庞大 TBTD 的重型操作，降阶为一个单次 Lanczos 迭代与简单波函数内积，在大型模型空间中极大地提升了数值可行性。

### 2. 有效相互作用特定的最优闭合能量（Optimal Closure Energies）

不同模型空间与有效相互作用对平均能量敏感度不同。文章核定并推荐了两套国际主流方案的最优闭合能量：

- **CMU 组推荐参数**：
  - \(^{48}\mathrm{Ca}\)（pf 壳，GXPF1A）：\(\langle E\rangle = 0.5\text{ MeV}\)；
  - \(^{76}\mathrm{Ge}, {}^{82}\mathrm{Se}\)（jj44 空间，JUN45）：\(\langle E\rangle = 3.4\text{ MeV}\)；
  - \(^{124}\mathrm{Sn}, {}^{130}\mathrm{Te}, {}^{136}\mathrm{Xe}\)（jj55 空间，SVD）：\(\langle E\rangle = 3.5\text{ MeV}\)。
- **Strasbourg–Madrid 组推荐参数**：
  - \(^{48}\mathrm{Ca}\)（KB3G）：\(\langle E\rangle = 2.5\text{ MeV}\)；
  - \(^{76}\mathrm{Ge}, {}^{82}\mathrm{Se}\)（GCN.28-50）：\(\langle E\rangle = 10\text{ MeV}\)；
  - \(^{130}\mathrm{Te}, {}^{136}\mathrm{Xe}\)（GCN.50-82）：\(\langle E\rangle = 12\text{ MeV}\)。

这一对比直接证明：即使在同一壳模型框架内，闭合能量的选取也与有效相互作用的单极项和单粒子轨道能级紧密绑定，不能将 \(\langle E \rangle = 8\text{ MeV}\) 作为普适常量套用。

### 3. \(2\nu\beta\beta\) 门态 Lanczos 快速求和算法（1000 倍加速）

标准模型允许的 \(2\nu\beta\beta\) 衰变必须超越闭合近似，其 Gamow–Teller 矩阵元为：

\[
M_{2\nu} = \sum_k \frac{\langle 0_f^+ || \sigma\tau^- || 1_k^+\rangle \langle 1_k^+ || \sigma\tau^- || 0_i^+\rangle}{E_k + E_0} .
\]

对于重核（如 \(^{48}\mathrm{Ca}\) 涉及 2\(\hbar\omega\) 空间或 \(^{136}\mathrm{Xe}\)），中间核 \(1^+\) 态维数超亿，直接对角化几百个态完全不可行。
Horoi 提出的快速算法如下：

1. 以 Gamow–Teller 算符作用于初态或末态构造“门态”（Doorway states）：
   \[
   |\sigma\tau^- 0_i^+\rangle = c_- \vert dw_-\rangle \equiv c_- |L_1^-\rangle , \quad
   |\sigma\tau^+ 0_f^+\rangle = c_+ \vert dw_+\rangle \equiv c_+ |L_1^+\rangle ,
   \]
   其中 \(c_\pm\) 为 GT 和规则的平方根；
2. 从门态出发进行 Lanczos 迭代，生成 Krylov 基矢 \(\vert L_m\rangle\)；
3. 仅需约 \(N \sim 20\) 次迭代即可获得高精度收敛矩阵元：
   \[
   M_{2\nu} \approx 3 c_+ c_- \sum_m g_m^- \langle dw_+  \vert L_m^- \rangle , \quad
   g_m^- = \sum_{k=1}^N \frac{V_{1k}^- V_{mk}^-}{E_{L_k}^N(1^+) - E_{\rm g.s.} + E_0} .
   \]

该方法相较于对角化 300–500 个中间态需要 5000–10000 次迭代的传统直接求和法，计算速度提升约 **1000 倍**，且可在 M-scheme 代码中通用执行。

### 4. 实验半衰期下限与物理参数约束（表 1 实验对账）

文章汇总了当时最先进深地实验给出的关键同位素实测与限制基准（表 1）：

- \(^{48}\mathrm{Ca}\)：\(Q_{\beta\beta}=4.268\text{ MeV}\)，\(T_{1/2}^{2\nu}=5.3\times10^{19}\text{ y}\)，\(T_{1/2}^{0\nu} > 2.0\times10^{22}\text{ y}\)；
- \(^{76}\mathrm{Ge}\)：\(Q_{\beta\beta}=2.039\text{ MeV}\)，\(T_{1/2}^{2\nu}=1.9\times10^{21}\text{ y}\)，\(T_{1/2}^{0\nu} > 8.0\times10^{25}\text{ y}\)（GERDA）；
- \(^{82}\mathrm{Se}\)：\(Q_{\beta\beta}=2.998\text{ MeV}\)，\(T_{1/2}^{2\nu}=8.7\times10^{19}\text{ y}\)，\(T_{1/2}^{0\nu} > 2.5\times10^{23}\text{ y}\)；
- \(^{124}\mathrm{Sn}\)：\(Q_{\beta\beta}=2.291\text{ MeV}\)，\(T_{1/2}^{2\nu}>1.0\times10^{19}\text{ y}\)，\(T_{1/2}^{0\nu} > 1.0\times10^{21}\text{ y}\)；
- \(^{130}\mathrm{Te}\)：\(Q_{\beta\beta}=2.528\text{ MeV}\)，\(T_{1/2}^{2\nu}=7.9\times10^{20}\text{ y}\)，\(T_{1/2}^{0\nu} > 4.0\times10^{24}\text{ y}\)（CUORE）；
- \(^{136}\mathrm{Xe}\)：\(Q_{\beta\beta}=2.458\text{ MeV}\)，\(T_{1/2}^{2\nu}=2.2\times10^{21}\text{ y}\)，\(T_{1/2}^{0\nu} > 1.1\times10^{26}\text{ y}\)（KamLAND-Zen）。

### 5. 多核素比值解耦 LNV 机制

单核素的 \(T_{1/2}^{0\nu}\) 测量只能约束综合参数乘积，无法区分是微小中微子质量驱动，还是右手中微子、超对称或接触项导致。
利用不同核素在不同算符下 NME 的特征比值（例如 \(M_{0\nu}(^{76}\mathrm{Ge})/M_{0\nu}(^{136}\mathrm{Xe})\) 与 \(M_{0N}(^{76}\mathrm{Ge})/M_{0N}(^{136}\mathrm{Xe})\) 存在显著差异），
结合两个或多个核素的实验半衰期比值，原则上可以排除特定机制，确立轻子数破坏的主导通道。

## Experimental and LNV Analysis Contract

在进行双贝塔衰变数据分析与理论比较时，必须遵守以下合同规则：

1. **相空间因子（PSF）版本一致性**：必须采用考虑子核真实有限尺寸电荷畸变（屏蔽因子 \(\sim 92\)–\(94.5\)）计算的现代 PSF（如 \(G_{01}\)），不得使用点电荷近似旧表；
2. **明确有效相互作用与闭合能量绑定**：报告闭合近似 \(M^{0\nu}\) 时，必须注明所用的有效哈密顿量与对应的 optimal \(\langle E\rangle\)；
3. **\(g_A\) 淬灭假设公开**：
   - \(2\nu\beta\beta\) 衰变：由于低动量转移，必须考虑 Gamow–Teller 算符淬灭（有效因子 \(q \a0.6\)–\(0.74\)），需标明采用的淬灭系数；
   - \(0\nu\beta\beta\) 衰变：由于中微子交换涉及 \(q \sim 100\)–\(200\text{ MeV}\)，高动量多极算符受两体流（2BC）与接触算符影响，禁止未经说明地把 \(2\nu\beta\beta\) 的强淬灭直接套用于 \(0\nu\beta\beta\)；
4. **短程关联（SRC）标明**：必须标明采用的是 CD-Bonn、Argonne 还是自洽 \(\chi\text{EFT}\) 接触项，不同 SRC 对 NME 造成 10%–20% 的系统性差异；
5. **末态自旋宇称**：默认讨论 \(0_i^+ \to 0_f^+\) 基态跃迁；对激发态（如 \(2_1^+\) 或 \(0_2^+\)）跃迁，由于相空间大幅压低且算符可能非标量，必须采用中间态显式求和或非标量 TBTD 处理。

## What It Cannot Establish Alone

- 单个同位素的 \(0\nu\beta\beta\) 半衰期下限不能独立确定马约拉纳中微子质量，质量提取严格受制于各理论模型间 2–3 倍的 NME 分散度；
- 闭合近似计算的 \(M^{0\nu}\) 无法自动延伸至 \(2\nu\beta\beta\) 衰变；
- 壳模型虽然最完整地保留了费米面附近的组态混合与许多体对称性，但在超大模型空间中受限于价空间截断，对高动量短程核子关联的描述必须依赖外加参数化（SRC）；
- 多核素比值识别机制的方法前提是至少有两个以上不同核素测得非零的 \(0\nu\beta\beta\) 衰变率；在仅有半衰期下限的现状下，该方法只能给出排除边界，无法确立机制。

## Knowledge Impact and Learning Decision

Horoi 的文章将双贝塔衰变微观物理与实际多体算法推进到前沿工程级别：
它提出的单次 Lanczos 等位旋投影算法极大简化了 \(0\nu\beta\beta\) NME 求解，
门态 Lanczos 快速算法解决了 \(2\nu\beta\beta\) 衰变中中间核大空间直接求和的百年难题，
并且确立了各有效相互作用专属的“最优闭合能量”。
该成果为 Wiki 建立了规范的 \(0\nu\beta\beta\) 与 \(2\nu\beta\beta\) 实验分析与核矩阵元对比标准。

本单元完成 Horoi 综述主文本、公式、表 1 与图 1–2 的有界核读；生产级 ISM 代码（如 NuShellX/KSHELL）的实际二进制和多核素大规模数据未独立重新计算。

## Evidence and Locators

- Article pp.1135–1137 / physical PDF pp.302–304：\(0\nu\beta\beta\) 物理意义、黑匣子定理、EFT 理论框架与 Feynman 衰变图（图 1–2）、表 1 实验数据汇总；
- Article pp.1137–1139 / physical PDF pp.304–306：广义 LNV 半衰期式 (1)、轻马约拉纳质量机制式 (2)、相空间因子计算；
- Article pp.1139–1141 / physical PDF pp.306–308：中间态求和式 (5)、闭合近似式 (6)、TBTD 分解式 (7)；
- Article pp.1141–1143 / physical PDF pp.308–310：Lanczos 等位旋投影加速算法式 (8)–(11)、最优闭合能量定义与各组相互作用参数；
- Article pp.1143–1145 / physical PDF pp.310–312：\(2\nu\beta\beta\) 衰变式 (12)–(13)、门态 Lanczos 快速求和算法式 (14)–(18)（1000 倍加速）、\(g_A\) 淬灭讨论；
- Article pp.1145–1146 / physical PDF pp.312–313：结论与未来前沿；
- 已渲染核对 PDF pp.302、303、305、307、309、310。

## Sources

- [[book-nuclear-shell-model-70-years]]
- [[neutrinoless-double-beta-decay-nmes-and-majorana-mass]]
- [[beta-decay-phase-space-log-ft-and-cvc-unitarity]]
- [[shimizu-shell-model-mcsm-qvsm-computational-contract]]
- [[smirnova-isospin-symmetry-breaking-shell-model-contract]]
