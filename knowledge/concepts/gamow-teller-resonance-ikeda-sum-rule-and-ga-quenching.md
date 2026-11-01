---
type: concept
title: "伽莫夫-泰勒巨共振（GTGR）、Ikeda求和定则与轴矢量耦合常数gA淬灭动力学"
aliases: [伽莫夫泰勒巨共振, GTGR, Ikeda求和定则, gA淬灭, 同位旋类似态IAS, 双贝塔衰变核基质元]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [gamow-teller, ikeda-sum-rule, ga-quenching, isobaric-analog-state, charge-exchange, double-beta-decay]
---

# 伽莫夫-泰勒巨共振（GTGR）、Ikeda求和定则与轴矢量耦合常数gA淬灭动力学

## 1. 物理全景：强弱相互作用的同位旋统一视界

在原子核低能电弱物理与在束电荷交换核反应（如 $(p, n)$、$(^3\text{He}, t)$、$(d, {}^2\text{He})$）中，核子在空间发生自旋翻转与同位旋阶梯算符操作，将核素转变为相邻的同量异位素（Isobars）。

根据 A. Bohr & B. R. Mottelson《Nuclear Structure》Vol. I（第 3 章）、J. Suhonen《From Nucleons to Nucleus》（第 7–8 章）与 F. Osterfeld（Rev. Mod. Phys. 64, 861, 1992）：
1. **两类基本同位旋激发**：
   - **费米跃迁（Fermi Transition）**：由纯同位旋标量算符驱动（$\Delta S = 0, \Delta T = 1$），全部激发强度集中在极狭窄的**同位旋类似态（Isobaric Analog State, IAS）**；
   - **伽莫夫-泰勒跃迁（Gamow-Teller Transition, GT）**：由自旋-同位旋张量算符驱动（$\Delta S = 1, \Delta T = 1$），在激发能 $E_x \sim 10 \sim 25\text{ MeV}$ 形成宽广强烈的**伽莫夫-泰勒巨共振（GTGR）**；
2. **微观模型不依赖性**：由于同位旋对易关系的代数纯洁性，GT 跃迁满足严格的模式无关和定则——**Ikeda 求和定则（Ikeda Sum Rule）**；
3. **科学世纪之谜**：全球实验测得的 GT 强度普遍比 Ikeda 和定则低约 $40\%$，揭示了微观核介质中核子波函数与 $\Delta(1232)$ 共振态混合诱发的**有效轴矢量弱耦合常数淬灭（$g_A$ Quenching）**，直接制约了无中微子双贝塔衰变（$0\nu\beta\beta$）核基质元的精确预言！

---

## 2. 算符代数与 Ikeda 模型无关求和定则

### (1) 同位旋阶梯算符与基本跃迁算符
定义单核子同位旋下降算符 $t_-$（将中子变为质子：$t_- |n\rangle = |p\rangle$）与上升算符 $t_+$（将质子变为中子：$t_+ |p\rangle = |n\rangle$）。
- **Fermi 跃迁算符**：$\hat{O}_F^\pm = \sum_{k=1}^A t_\pm(k) = T_\pm$
- **Gamow-Teller 跃迁算符**：$\hat{O}_{GT}^\pm = \sum_{k=1}^A \vec{\sigma}(k) t_\pm(k)$

减缩跃迁强度定义为：
$$B(F_\pm) = \frac{1}{2I_i + 1} |\langle f || \sum_k t_\pm(k) || i \rangle|^2$$
$$B(GT_\pm) = \frac{1}{2I_i + 1} |\langle f || \sum_k \vec{\sigma}(k) t_\pm(k) || i \rangle|^2$$

### (2) Ikeda 求和定则严格推导（K. Ikeda 1963）
利用同位旋自旋算符的标准对易关系：
$$[t_-(j), t_+(k)] = -2 t_z(j) \cdot \delta_{jk}$$
对闭合完全基矢系求和，计算 $GT_-$ 与 $GT_+$ 算符的对易子基态期望值：
$$S_-(GT) - S_+(GT) \equiv \sum_f B(GT_-; i \to f) - \sum_{f'} B(GT_+; i \to f') = \langle i | [\hat{O}_{GT}^+, \hat{O}_{GT}^-] | i \rangle$$
由于泡利自旋矩阵满足 $\sum_{\mu} \sigma_\mu^\dagger \sigma_\mu = 3$，代入得：
$$\langle i | \sum_{k=1}^A \vec{\sigma}(k)^2 [t_+(k), t_-(k)] | i \rangle = 3 \langle i | \sum_{k=1}^A 2 t_z(k) | i \rangle$$
因为单个核子同位旋分量 $t_z = +1/2$（中子）与 $-1/2$（质子），总核子求和直接给出：
$$S_-(GT) - S_+(GT) = 3(N - Z)$$

**绝对普适性**：
该求和定则**完全独立于核的形状（拉长、扁长或三轴）、配对强度以及二体相互作用的具体细节**，只要体系由单纯的质子与中子非相对论费米子构成，该和定则在数学上严格守恒！

---

## 3. 轴矢量弱电耦合常数 $g_A$ 淬灭微观机制

### (1) 实验强度缺失现象（Missing GT Strength）
自 1980 年代以来，全球利用高分辨 $(p, n)$ 与 $(^3\text{He}, t)$ 束内反应（如在大阪大学 RCNP 谱仪）对全核素图进行高精度测量，发现：
在整个激发能区（$E_x \le 30\text{ MeV}$，包括单粒子态、低能态与完整的 GTGR 巨共振峰），实验测得的积分总强度仅占 Ikeda 理论值的 $50\% \sim 60\%$：
$$\frac{[S_-(GT) - S_+(GT)]_{\text{exp}}}{3(N - Z)} \approx 0.55 \pm 0.05$$

### (2) 两大微观淬灭根源
1. **$\Delta(1232)$-空穴张量重整化（$\Delta\text{-}h$ Mixing）**：
   质子和中子是夸克复合粒子，在强相互作用下核子可以被自旋-同位旋算符激发为其激发态——$\Delta$ 共振态（$M_\Delta \approx 1232\text{ MeV}, J^\pi = 3/2^+, T=3/2$）。核力中强烈的张量力使得基态波函数混入微小的 $\Delta\text{-}h$ 组态，将近 $20\%$ 的 GT 跃迁强度推向了高达 $300\text{ MeV}$ 的超高激发能区；
2. **二体弱交换流（Two-Body Meson-Exchange Currents, 2BC）**：
   在手征有效场论（Chiral EFT）微观推导中，弱相互作用流不仅直接作用于单个核子，而且作用于正在交换 $\pi$ 介子与 $\rho$ 介子的核子对，使得单体轴矢量算符被重整化为有效单体算符。

由此在原子核有限多体介质中定义**有效轴矢量弱电耦合常数（$g_A^{\text{eff}}$）**：
$$g_A^{\text{eff}} = q \cdot g_A^{\text{free}} \quad (q \approx 0.75 \sim 0.85)$$
其中自由核子中子衰变测得的基准常数为 $g_A^{\text{free}} = 1.2754(13)$，在核介质中有效淬灭至 $g_A^{\text{eff}} \approx 0.95 \sim 1.05$。

---

## 4. 与 $A\approx 130$ 质量区双贝塔衰变的跨界前沿闭环

在 $A\approx 130$ 质量区中：
1. **核心物理锚点**：$^{130}\text{Te} \to {}^{130}\text{Xe}$ 与 $^{136}\text{Xe} \to {}^{136}\text{Ba}$ 是国际寻找无中微子双贝塔衰变（$0\nu\beta\beta$）最核心的同位素体系；
2. **$g_A$ 的四次方敏感性**：
   $0\nu\beta\beta$ 的理论半衰期严格反比于 $g_A$ 的四次方：
   $$[T_{1/2}^{0\nu}]^{-1} \propto (g_A^{\text{eff}})^4 \cdot |M^{0\nu}|^2 \cdot \langle m_{\beta\beta} \rangle^2$$
   若 $g_A$ 发生微小的 $20\%$ 淬灭，半衰期将直接被拉长近 $3 \sim 4$ 倍，这直接决定了未来兆吨级深地下实验的物理探测灵敏度极限！

---

## 5. 实验电荷交换反应截面与微观跃迁强度 $B(GT)$ 标度转换

在束前角（$\theta \to 0^\circ$）中间能区（$E_{\text{lab}} \ge 100\text{ MeV/u}$）下，脉冲近似与程函近似（Eikonal Approximation）表明，电荷交换反应截面正比于微观自旋-同位旋跃迁强度：
$$\frac{d\sigma}{d\Omega}(q=0, \omega=0) = \hat{\sigma}_{GT} \cdot B(GT)$$
其中 $\hat{\sigma}_{GT}$ 为反应单位截面（Unit Cross Section），可通过已知 $\beta$ 衰变比较半衰期（$ft$ 值）的标准跃迁（如 $^{14}\text{C}(p, n)^{14}\text{N}$ 或 $^{12}\text{C}(^3\text{He}, t)^{12}\text{N}$）进行绝对实验定标。

通过对连续谱进行多极分解分析（Multipolarity Decomposition Analysis, MDA），扣除准自由散射（Quasifree Scattering, QFS）与高阶多极分量（$\Delta L = 1, 2$），即可获得纯净的 $\Delta L = 0$ 伽莫夫-泰勒跃迁强度分布。

---

## 6. Python 算法设计与实验分析器规范

本 Wiki 在 `system/scripts/analysis/gamow_teller_ikeda_quenching_calculator.py` 中实现了伽莫夫-泰勒求和定则与 $g_A$ 淬灭评估器：
1. **Ikeda 和定则理论值**：$S_{\text{Ikeda}} = 3(N - Z)$；
2. **实验求和与淬灭因子提取**：
   $$q = \sqrt{\frac{S_-(GT)_{\text{exp}} - S_+(GT)_{\text{exp}}}{3(N - Z)}}$$
3. **有效弱轴矢量常数**：$g_A^{\text{eff}} = q \cdot g_A^{\text{free}}$；
4. **$0\nu\beta\beta$ 半衰期修正因子**：
   $$R_{T_{1/2}} = \left(\frac{g_A^{\text{free}}}{g_A^{\text{eff}}}\right)^4 = \frac{1}{q^4}$$

---

## 7. 权威文献与理论溯源

1. **Bohr, A. & Mottelson, B. R.** (1969). *Nuclear Structure*, Vol. I (Single-Particle Motion), Chapter 3 (Collective Spin-Isospin Excitations). Benjamin, New York.
2. **Ikeda, K., Fujii, S., & Fujita, J. I.** (1963). The $(p, n)$ reactions and beta decays. *Phys. Lett.*, 3(6), 271-272.
3. **Osterfeld, F.** (1992). Nuclear spin and isospin excitations. *Rev. Mod. Phys.*, 64(4), 861-909.
4. **Suhonen, J.** (2007). *From Nucleons to Nucleus: Concepts of Microscopic Theory*, Chapters 7-8. Springer.
5. **Ejiri, H., Suhonen, J., & Zuber, K.** (2019). Neutrino-nuclear responses for astro-neutrinos, single beta decays and double beta decays. *Phys. Rep.*, 797, 1-102.
6. **卢希庭、江栋兴、叶沿林** (2000). 《原子核物理（修订版）》第 4 章：核衰变与弱相互作用选择定则. 原子能出版社.
7. **吴治华** (2006). 《原子核物理实验方法》（第三版）第 10 章：核辐射与核谱学测量. 原子能出版社.
