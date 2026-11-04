---
type: method
title: "Jouni Suhonen 质子-中子准粒子无规相位近似（pnQRPA）与 Ikeda 求和规则方法合同"
aliases: [Suhonen-pnQRPA-contract, Ikeda-sum-rule-contract, Gamow-Teller-pnQRPA-contract]
created: 2026-11-04
updated: 2026-11-04
status: active
review_status: unreviewed
method_type: microscopic-model-contract
tags: [suhonen, pnqrpa, gamow-teller-resonance, ikeda-sum-rule, quasiparticle, beta-decay, charge-exchange, gpp-parameter]
topics: [suhonen, pnqrpa, gamow-teller, ikeda-sum-rule, beta-decay]
sources: [book-suhonen-from-nucleons-to-nucleus, book-bohr-mottelson-nuclear-structure-vol2, book-nuclear-shell-model-70-years]
---

# Jouni Suhonen 质子-中子准粒子无规相位近似（pnQRPA）与 Ikeda 求和规则方法合同

## Purpose

本方法合同严格绑定 Jouni Suhonen《From Nucleons to Nucleus: Concepts of Microscopic Nuclear Theory》（Springer 2007）第 17、18、19 章（印刷 pp. 523–626 / 物理 PDF pp. 533–636），
系统形式化开壳奇奇核激发的质子-中子准粒子塔姆-丹科夫近似（pnQTDA）与准粒子无规相位近似（pnQRPA）运动方程（式 19.1–19.8）、相关矩阵 $A, B$ 的两体相互作用矩阵元展开、
Gamow-Teller 跃迁算符在准粒子表象下的约化矩阵元，以及基于完备性代数严格证明模型无关的 **Ikeda 求和规则（Ikeda Sum Rule）**（式 19.74–19.79），
并定量分析粒子-粒子相互作用强度参数 $g_{\text{pp}}$ 对 $\beta^+$ 衰变与双贝塔衰变矩阵元的相消抑制机制，
为弱电相互作用电荷交换反应、超允许与禁戒 $\beta$ 衰变及无中微子双贝塔衰变微观核矩阵元（NME）提供严格微观计算规范。

## Inputs and Assumptions

1. **BCS 准粒子平均场基础**：质子与中子分别在球形或变形单粒子势阱中通过单极配对力建立 BCS 真空 $|\text{BCS}\rangle = |\text{BCS}\rangle_p \otimes |\text{BCS}\rangle_n$，占据振幅 $u_j, v_j$ 与准粒子能量 $E_j = \sqrt{(\epsilon_j - \lambda)^2 + \Delta^2}$ 已自洽收敛；
2. **电荷改变准粒子对算符**：定义创生质子-中子准粒子对的双费米子算符 $A_{pn}^\dagger(JM) = [a_p^\dagger a_n^\dagger]_{JM}$ 与时间反演湮灭算符 $\widetilde{A}_{pn}(JM) = (-)^{J-M} [a_p a_n]_{J,-M}$；
3. **准粒子无规相位近似假定（Quasiboson Approximation, QBA）**：假定两准粒子对算符满足准玻色子对易关系：
   $$[A_{pn}(JM), A_{p'n'}^\dagger(J'M')] \approx \delta_{JJ'} \delta_{MM'} \delta_{pp'} \delta_{nn'}$$
4. **两体残余相互作用（SDI 或 Bonn/Argonne 势）**：相互作用分解为粒子-空穴通道（通道强度 $g_{\text{ph}}$，主导巨共振相干推高）与粒子-粒子通道（通道强度 $g_{\text{pp}}$，主导低能准粒子相消）。

## What It Can Establish

1. **pnQRPA 矩阵本征方程（式 19.7）**：
   $$\begin{pmatrix} \mathbf{A} & \mathbf{B} \\ -\mathbf{B}^* & -\mathbf{A}^* \end{pmatrix} \begin{pmatrix} \vec{X}^\omega \\ \vec{Y}^\omega \end{pmatrix} = \hbar\omega \begin{pmatrix} \vec{X}^\omega \\ \vec{Y}^\omega \end{pmatrix}$$
   - 正确解出开壳奇奇核正负宇称激发态能谱（如 $^{24}\text{Na}, {}^{24}\text{Al}, {}^{66}\text{Ga}$），自然引入基态关联（向后传播振幅 $Y_{pn}^\omega$）；
   - 正交归一化条件：$\sum_{pn} (|X_{pn}^\omega|^2 - |Y_{pn}^\omega|^2) = 1$；
2. **Gamow-Teller 跃迁强度的微观代数表达式（式 19.67–19.68）**：
   $$\langle 1_k^+ || \beta_{\text{GT}}^- || \text{pnQRPA} \rangle = \sum_{pn} \mathcal{M}_{\text{GT}}(pn) [ u_p v_n X_{pn}^k + v_p u_n Y_{pn}^k ]$$
   $$\langle 1_k^+ || \beta_{\text{GT}}^+ || \text{pnQRPA} \rangle = \sum_{pn} \mathcal{M}_{\text{GT}}(pn) [ v_p u_n X_{pn}^k + u_p v_n Y_{pn}^k ]$$
   微观单粒子矩阵元为 $\mathcal{M}_{\text{GT}}(pn) = \frac{1}{\sqrt{3}} \langle  p \vert| \vec{\sigma} |\vert  n \rangle$；
3. **基于 pnQRPA 完备性关系的 Ikeda 求和规则严格守恒定理（式 19.75–19.79）**：
   $$S_- - S_+ = \sum_{k} B(\text{GT}^-; 0^+ \to 1^+_k) - \sum_{k} B(\text{GT}^+; 0^+ \to 1^+_k) = 3(N - Z)$$
   Suhonen 利用双对易子与正交完备性 $\sum_k (X_{pn}^k X_{p'n'}^k - Y_{pn}^k Y_{p'n'}^k) = \delta_{pp'}\delta_{nn'}$ 证明：无论两体相互作用强度如何调节、基态关联多强，求和差值恒等于未配对中子数 $3(N-Z)$；
4. **$g_{\text{pp}}$ 诱发 $\beta^+$ 衰变相消与相变临界失稳**：
   - 证明增加吸引性粒子-粒子相互作用 $g_{\text{pp}}$ 会使 $B$ 矩阵元剧烈增加，导致 $X$ 与 $Y$ 振幅在低能态发生相消干涉，急剧压低 $\beta^+$ 强度与 $2\nu\beta\beta$ 矩阵元；
   - 给出当 $g_{\text{pp}} \to g_{\text{pp}}^n_{\text{crit}} \a1.1 - 1.3$ 时，第一激发态能量塌缩至零（$\hbar\omega \to 0$），标志着偶偶核基态发生向质子-中子超流态的相变。

## What It Cannot Establish Alone

1. **准玻色子近似（QBA）在临界点失效**：当 $g_{\text{pp}} \approx g_{\text{pp}}^n_{\text{crit}}$ 时，基态关联极度增强导致 $|Y|^2$ 显著偏离零，费米子反对易子破缺严重，经典 pnQRPA 给出虚频本征值，必须采用重整化 pnQRPA（RQRPA）或自洽投影壳模型；
2. **自由核子轴矢量耦合常数淬灭（$g_A$ Quenching）的微观溯源**：pnQRPA 能说明价空间组态混合的强度再分配，但无法自动包含高能 $\Delta(1232)$ 异构体激发与双体介子交换流（MEC）导致的全局淬灭（$g_A^{\text{eff}} \a1.0$ 或 $1.27$），需结合第一性原理手征 EFT 弱流算符；
3. **形变核中的轴对称/三轴角动量破缺**：标准球形 pnQRPA 不能直接处理强形变核（如稀土区或 $A\a$A \aA \a130$ 区）中的 $K$ 混合与内禀转动进动，需扩展为变形 pnQRPA（Deformed pnQRPA）。

## Sources

- [[book-suhonen-from-nucleons-to-nucleus]]：Chapters 17, 18, 19 (印刷 pp. 523–626 / PDF pp. 533–636).
- [[book-bohr-mottelson-nuclear-structure-vol2]]：Chapter 6 §6-5 粒子-振动耦合与 RPA 色散方程.
- [[book-nuclear-shell-model-70-years]]：Horoi 综述（双贝塔衰变微观核矩阵元）.
- K. Ikeda, S. Fujii, and J. I. Fujita, Phys. Lett. 3, 271 (1963).
- [[gamow-teller-resonance-ikeda-sum-rule-and-ga-quenching]]：GT 共振与 Ikeda 求和规则.
- [[neutrinoless-double-beta-decay-nmes-and-majorana-mass]]：无中微子双贝塔衰变矩阵元.
