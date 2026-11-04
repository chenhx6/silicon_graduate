# Jouni Suhonen 微观核结构 5 大实操与代数推演范式

### Pattern 1: Wigner-Eckart 定理与电多极单粒子约化矩阵元计算
- **目标**：在球形壳模型中计算单粒子轨道 $|n_i l_i j_i\rangle \to |n_f l_f j_f\rangle$ 的绝对 $B(E\lambda)$ 跃迁概率。
- **推演步骤**：
  1. **宇称选择定则**：检验 $\Delta \pi = (-1)^{l_f + l_i + \lambda} = +1$；若不满足，矩阵元恒等于零；
  2. **三角角动量定则**：检验 $|j_i - j_f| \le \lambda \le j_i + j_f$；
  3. **计算几何 3j 符号**：
     $$J_0 = \begin{pmatrix} j_f & \lambda & j_i \\ 1/2 & 0 & -1/2 \end{pmatrix}$$
  4. **计算径向积分**：计算谐振子径向期望值 $I_{\text{rad}} = \int_0^\infty R_{n_f l_f}(r) r^\lambda R_{n_i l_i}(r) r^2 dr$；
  5. **组装约化矩阵元**：
     $$\langle j_f || \mathcal{M}(E\lambda) || j_i \rangle = \frac{e_{\text{eff}}}{\sqrt{4\pi}} (-1)^{j_i + \lambda - 1/2} \hat{j}_f \hat{j}_i \hat{\lambda} J_0 I_{\text{rad}}$$
  6. **提取 $B(E\lambda)$**：$B(E\lambda; j_i \to j_f) = \frac{1}{2j_i + 1} |\langle j_f || \mathcal{M}(E\lambda) || j_i \rangle|^2$。

---

### Pattern 2: BCS 单常数配对能隙方程自洽求解
- **目标**：给定一组单粒子能级 $\varepsilon_j$ 和简并度 $\Omega_j = (2j+1)/2$，求解配对能隙 $\Delta$ 与费米能级 $\lambda$。
- **推演步骤**：
  1. **初始化**：取试验化学势 $\lambda_0 = \varepsilon_{\text{Fermi}}$，试验能隙 $\Delta_0 = 12 / \sqrt{A}\text{ MeV}$；
  2. **计算准粒子能量**：$E_j = \sqrt{(\varepsilon_j - \lambda)^2 + \Delta^2}$；
  3. **更新占据几率**：$v_j^2 = \frac{1}{2} [1 - (\varepsilon_j - \lambda)/E_j]$；
  4. **检验粒子数守恒条件**：$f_N(\lambda, \Delta) \equiv \sum_j (2j+1) v_j^2 - N = 0$；
  5. **检验能隙方程自洽性**：$f_\Delta(\lambda, \Delta) \equiv \frac{G}{2} \sum_j \frac{2j+1}{2 E_j} - 1 = 0$；
  6. **二分/Newton-Raphson 联合迭代**：调整 $(\lambda, \Delta)$ 直至残差 $|f_N| < 10^{-6}$ 且 $|f_\Delta| < 10^{-6}$。

---

### Pattern 3: 表面 Delta 相互作用 (SDI) 双粒子矩阵元快速求解
- **目标**：在两个价核子轨道空间快速构建全反对称化剩余相互作用矩阵元。
- **推演步骤**：
  1. 提取轨道角动量 $l_a, l_b, l_c, l_d$ 与总自旋 $J$、同位旋 $T$；
  2. 遍历中间多极标量 $L$（满足三角定则）；
  3. 计算两个特殊 $3j$ 符号：
     $$A_L = \begin{pmatrix} j_a & j_c & L \\ 1/2 & -1/2 & 0 \end{pmatrix}, \quad B_L = \begin{pmatrix} j_b & j_d & L \\ 1/2 & -1/2 & 0 \end{pmatrix}$$
  4. 引入反对称化同位旋相位因子 $\eta_{JT} = [1 - (-1)^{J + T} (-1)^{j_c + j_d}]$；
  5. 求和提取矩阵元：$V_{abcd}^{JT} = -\frac{V_0}{2 \sqrt{(1+\delta_{ab})(1+\delta_{cd})}} (-1)^{l_a + l_c} \hat{j}_a \hat{j}_b \hat{j}_c \hat{j}_d \sum_L \hat{L}^2 A_L B_L \eta_{JT}$。

---

### Pattern 4: 准粒子跃迁相消与相加选择律诊断
- **目标**：判断特定核跃迁在 BCS 准粒子平均场下是增强还是受到剧烈配对相消。
- **推演步骤**：
  1. 判断跃迁多极性质 $\sigma\lambda$（$E\lambda$ 还是 $M\lambda$）；
  2. 提取初末态单粒子轨道的占据振幅 $u_i, v_i$ 与 $u_f, v_f$；
  3. **配对跃迁因子求值**：
     - 若为 $E\lambda$ 跃迁：计算因子 $F_{E\lambda} = u_i u_f - v_i v_f$；
       - 若初末态在费米面同一侧且深处或高处（即 $u_i \approx u_f, v_i \approx v_f$），则 $u_i u_f - v_i v_f \approx u_i^2 - v_i^2 \to 0$（在费米面附近 $u^2 \approx v^2 \a0.5$ 发生**剧烈电跃迁相消**）；
     - 若为 $M\lambda$ 跃迁：计算因子 $F_{M\lambda} = u_i u_f + v_i v_f$；
       - 因子恒为正且接近 1（**磁跃迁无相消，保持稳定**）；
  4. 给出最终 1qp 约化矩阵元：$\langle f || \mathcal{M} || i \rangle_{\text{1qp}} = F_{\sigma\lambda} \langle f || \mathcal{M} || i \rangle_{\text{sp}}$。

---

### Pattern 5: pnQRPA Ikeda 求和规则完备性与 $g_{\text{pp}}$ 稳定性校验
- **目标**：在质中电荷交换模型中校验 Gamow-Teller 强度分布的无偏性与超矩阵稳定性。
- **推演步骤**：
  1. 构建母核 $(N, Z)$ 的 BCS 质子与中子单粒子基矢及占据数 $u_p, v_p, u_n, v_n$；
  2. 求解 pnQRPA 本征值方程，获得所有正宇称 $1^+$ 本征态 $\omega$ 的前向振幅 $X_{pn}^\omega$ 与后向振幅 $Y_{pn}^\omega$；
  3. 计算 $\beta^-$ 衰变到子核 $(N-1, Z+1)$ 的总 Gamow-Teller 强度：
     $$S_- = \sum_\omega |\langle 1_\omega^+ || \beta^- || 0_{\text{gs}}^+ \rangle|^2$$
  4. 计算 $\beta^+$ 衰变到子核 $(N+1, Z-1)$ 的总 Gamow-Teller 强度：
     $$S_+ = \sum_{\omega'} |\langle 1_{\omega'}^+ || \beta^+ || 0_{\text{gs}}^+ \rangle|^2$$
  5. **绝对守恒判据**：严格计算差值 $\Delta S = S_- - S_+$，必须以高精度满足：
     $$|\Delta S - 3(N - Z)| < 10^{-4}$$
  6. **$g_{\text{pp}}$ 临界失稳预警**：扫描 $g_{\text{pp}}$，监测最低本征能量 $\hbar\omega_1$；当 $\hbar\omega_1 \to 0$ 时，表明系统进入质中超流破缺区，计算必须终止。
