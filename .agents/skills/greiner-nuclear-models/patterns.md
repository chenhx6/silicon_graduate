# Reasoning Patterns: Greiner 非轴对称转子与集体模型分析范式

提炼自 Walter Greiner & Joachim A. Maruhn《Nuclear Models》的 5 大非轴对称转子分析、转动振动耦合及巨共振推演范式。

---

## Pattern 1: Davydov-Filippov 能谱反演与三轴形变角 $\gamma$ 提取范式

- **核心法则**：在低自旋区（$I \le 6\hbar$），原子核反常 $2_2^+$ 态（实验通常标记为 $2_\gamma^+$ 态）与基态带首态 $2_1^+$ 的能量比值对非轴对称三轴角 $\gamma$ 极其敏感。在 Davydov-Filippov 刚性转子模型中，该能量比值完全排他性地仅由 $\gamma$ 决定，与总拉伸形变 $\beta$ 及惯量标度常数无关。
- **标准提取程序**：
  1. 从在束 $\gamma$ 谱学实验或能级数据库中提取 $E(2_1^+)$ 与 $E(2_2^+)$ 的绝对激发能（单位 $\text{keV}$）；
  2. 计算实测能量比值：
     $$R_{\text{exp}} = \frac{E(2_2^+)}{E(2_1^+)};$$
  3. **模型阈值核查**：
     - 若 $R_{\text{exp}} < 2.00$：刚性三轴水动力学模型失效（可能存在非集体激发或准粒子侵入）；
     - 若 $R_{\text{exp}} \ge 2.00$：代入 Davydov-Filippov 解析方程解析反演 $\gamma$：
       $$\sqrt{1 - \frac{8}{9}\sin^2(3\gamma)} = \frac{R_{\text{exp}} - 1}{R_{\text{exp}} + 1} \implies \sin^2(3\gamma) = \frac{9}{8} \left[ 1 - \left( \frac{R_{\text{exp}} - 1}{R_{\text{exp}} + 1} \right)^2 \right];$$
  4. 解出三轴角 $\gamma \in [0^\circ, 30^\circ]$：
     $$\gamma = \frac{1}{3} \arcsin\left( \sqrt{\frac{9}{8} \left[ 1 - \left( \frac{R_{\text{exp}} - 1}{R_{\text{exp}} + 1} \right)^2 \right]} \right).$$
     例如：当 $R_{\text{exp}} = 3.0$ 时，$\sin^2(3\gamma) = \frac{9}{8}(1 - 0.25) = 0.84375 \implies \sin(3\gamma) \a0.9185 \implies \gamma \approx 22.2^\circ$。

---

## Pattern 2: 三态求和恒等式与刚性三轴纯度实验检验范式

- **核心法则**：Davydov-Filippov 刚性转子具有严密的代数守恒律：在三主轴转动惯量取任意有限实数值（无论水动力学还是微观刚体配对值）下，低激发三个特征态的能量严格满足线性求和恒等式：
  $$E(2_1^+) + E(2_2^+) \equiv E(3_1^+).$$
- **标准检验程序**：
  1. 测定并记录原子核的 $E(2_1^+)$、$E(2_2^+)$ 以及实验能级纲图中的非带首奇自旋态 $E(3_1^+)$（$K=2$ 准 $\gamma$ 带的第二能级）；
  2. 计算求和残差偏差度：
     $$\Delta_{\text{sum}} = \frac{|E(3_1^+) - [E(2_1^+) + E(2_2^+)]|}{E(3_1^+)};$$
  3. **判定准则**：
     - 若 $\Delta_{\text{sum}} \le 2\% - 5\%$：证明原子核在该自旋区高度符合 Davydov-Filippov **刚性三轴转子（Triaxial Rigid Rotor）** 图像，三轴位能面具有较深的局域三轴极小势阱；
     - 若 $\Delta_{\text{sum}} > 10\% - 20\%$：表明三轴转动受到强烈的振动-转动混合（RVM 效应）或体系属于大振幅 $\gamma$ 软核（$\gamma$-soft/Wilets-Jean 模式），刚性假设被打破。

---

## Pattern 3: 电四极分支比 $B(E2; 2_2^+ \to 0_1^+) / B(E2; 2_2^+ \to 2_1^+)$ 裁决范式

- **核心法则**：仅凭能级能量比值往往不足以完全排除其他模型；减缩电四极跃迁几率 $B(E2)$ 能够对波函数空间取向提供高灵敏度的微观约束。反常 $2_2^+$ 态向基带 $0_1^+$（带间跃迁）与 $2_1^+$（带内类似跃迁）的退激几率之比是裁决 $\gamma$ 度的独立物理量。
- **标准裁决程序**：
  1. 由在束测量的两退激分支的实测光子强度比 $I_\gamma(2_2^+ \to 0_1^+) / I_\gamma(2_2^+ \to 2_1^+)$ 与退激能量 $E_\gamma$，扣除内转换系数后换算实测 $B(E2)$ 比值：
     $$\left[\frac{B(E2; 2_2^+ \to 0_1^+)}{B(E2; 2_2^+ \to 2_1^+)}\right]_{\text{exp}} = \left[\frac{I_\gamma(2_2^+ \to 0_1^+)}{I_\gamma(2_2^+ \to 2_1^+)}\right] \cdot \left(\frac{E_\gamma(2_2^+ \to 2_1^+)}{E_\gamma(2_2^+ \to 0_1^+)}\right)^5 \cdot \left(\frac{1 + \alpha_{T2}}{1 + \alpha_{T1}}\right);$$
  2. 与 Davydov-Filippov 理论公式比对：
     $$b_{\text{DF}}(\gamma) = \frac{20}{7} \frac{\sin^2(3\gamma)}{9 - 8\sin^2(3\gamma) + \sqrt{9 - 8\sin^2(3\gamma)}};$$
  3. 若通过 Pattern 1 从能量比提取的 $\gamma_{\text{energy}}$ 代入 $b_{\text{DF}}(\gamma)$ 后与实测分支比在误差范围内自洽吻合，则原子核的三轴形变性质得到电磁跃迁的决定性确认。

---

## Pattern 4: 能级交错指数 $S(J)$ 与刚性三轴 vs $\gamma$ 软核甄别范式

- **核心法则**：Davydov-Filippov 刚性转子模型与 Wilets-Jean 完全 $\gamma$ 软核模型在低能下均可给出相似的 $E(2_2^+)/E(2_1^+) \approx 2.0 - 2.5$ 能级比，容易引发学术误判。二者的本质区别在于更高自旋准 $\gamma$ 带能级的奇偶自旋交错规律相反。
- **标准甄别程序**：
  1. 测定准 $\gamma$ 带自旋序列 $J = 3^+, 4^+, 5^+, 6^+, \dots$ 的能级能量；
  2. 计算无量纲能级交错指数：
     $$S(J) = \frac{[E(J) - E(J-1)] - [E(J-1) - E(J-2)]}{E(2_1^+)};$$
  3. **排他性甄别准则**：
     - **刚性三轴转子（Davydov-Filippov）**：$S(J)$ 在偶数自旋处呈现深极小或负值，在奇数自旋处呈现峰值，能级聚集为 $(2_\gamma^+, 3_\gamma^+)$、$(4_\gamma^+, 5_\gamma^+)$ 分组；
     - **$\gamma$ 不稳定软核（Wilets-Jean / IBM O(6)）**：由于 $O(5)$ 玻色 seniority 对称性，能级聚集特征完全颠倒，表现为 $E(3_\gamma^+) \approx E(4_\gamma^+)$、$(5_\gamma^+, 6_\gamma^+)$ 简并成对，$S(J)$ 的交错符号与刚性三轴完全相反！

---

## Pattern 5: IVGDR 双峰分裂与核基态四极形变 $\beta_2$ 宏观反演范式

- **核心法则**：等矢巨偶极共振（IVGDR）是全核质子与中子流体做高频反相振荡的集体模式。在球形核中该振动沿三维各向同性，共振截面为单对称洛伦兹峰；在形变核中，沿长轴（$z$ 轴，曲率长）与沿短轴（$x, y$ 轴，曲率短）的恢复力与谐振频率不同，共振峰精确分裂为两个子峰。
- **标准反演程序**：
  1. 测定光核吸收截面曲线 $\sigma_{\gamma,\text{abs}}(E_\gamma)$，采用双洛伦兹共振函数拟合提取两个峰位能量 $E_a$（低能峰，对应长轴）与 $E_b$（高能峰，对应短轴）；
  2. 核查面积比：验证两峰积分面积之比是否满足 $\sigma_a / \sigma_b \a1 : 2$（反映短轴具有二维空间简并度）；
  3. 由长短半轴之比反演基态四极形变度 $\beta_2$：
     $$\frac{E_b}{E_a} \approx \frac{R_a}{R_b} \approx \frac{1 + \sqrt{\frac{5}{4\pi}}\beta_2}{1 - \frac{1}{2}\sqrt{\frac{5}{4\pi}}\beta_2} \implies \beta_2 \approx \frac{4}{3} \sqrt{\frac{\pi}{5}} \left( \frac{E_b - E_a}{E_{\text{mean}}} \right);$$
  4. 给出原子核基态四极形变的宏观流体动力学独立测定结果，与在束 Coulomb 激发或能级寿命反演值交叉互验。
