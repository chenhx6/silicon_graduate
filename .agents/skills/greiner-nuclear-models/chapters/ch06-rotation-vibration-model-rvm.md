# 第 6 章 (二)：Faessler-Greiner 转动振动模型 (RVM) 与黎曼度规量子化

**来源专著**：Walter Greiner & Joachim A. Maruhn《Nuclear Models》（Springer 1996）第 6 章 §6.5
**对应页码**：印刷 pp. 147–167 / 物理 PDF pp. 166–186，式 (6.175)–(6.220)

---

## 1. 核心理论推导与黎曼空间几何

### 1.1 曲线内禀坐标系与平衡形变微扰展开
A. Faessler 与 W. Greiner (1962) 建立了处理轴对称基态周围四极表面振动与转动相互作用的经典理论。
设原子核基态具有平衡长椭球形变 $(\beta_0 > 0, \gamma = 0)$。将五维集体运动变换到内禀系，坐标选取为：
- $\xi = a_0 - \beta_0$：描述沿对称轴方向的 $\beta$ 伸缩呼吸振动；
- $\eta = a_2 = a_{-2}$：描述破坏轴对称性的横向 $\gamma$ 形变振动（与形变角关系为 $\eta = \frac{1}{\sqrt{2}}\beta\sin\gamma \approx \frac{\beta_0}{\sqrt{2}}\gamma$）；
- $\theta_1, \theta_2, \theta_3$：描述核体空间取向的三个欧拉角。

### 1.2 Pauli-Podolsky 黎曼度规量子化算符
经典动能包含振动线速度与转动角速度的二次型：$T = \frac{1}{2} B (\dot{a}_0^2 + 2 \dot{a}_2^2) + \frac{1}{2} \sum_{k} \mathcal{J}_k \omega_k^2$。
在曲线坐标系下，五维度规张量为 $g_{\mu\nu}$，其行列式为：
$$g = \det(g_{\mu\nu}) = 16 B^5 (\beta_0 + \xi)^2 \eta^2 \sin^2(3\gamma) \sin^2\theta_2.$$
应用 Pauli-Podolsky 广义曲面动能量子化定理：
$$\hat{T} = -\frac{\hbar^2}{2} \sum_{\mu,\nu} \frac{1}{\sqrt{g}} \frac{\partial}{\partial q^\mu} \left( \sqrt{g} (g^{-1})^{\mu\nu} \frac{\partial}{\partial q^\nu} \right).$$
展开求导后，动能严格分解为纯振动项、对称转动项以及高阶离心与非对称耦合项（Greiner 式 6.206）：
$$\hat{T} = -\frac{\hbar^2}{2B} \left( \frac{\partial^2}{\partial \xi^2} + \frac{1}{2}\frac{\partial^2}{\partial \eta^2} + \frac{1}{2\eta} \frac{\partial}{\partial \eta} \right) + \sum_{k=1}^3 \frac{\hat{I}_k^2}{2\mathcal{J}_k(\xi, \eta)}.$$

---

## 2. RVM 解析能级谱与集体激发带

在简谐振动势 $V(\xi, \eta) = \frac{1}{2} C_\beta \xi^2 + C_\gamma \eta^2$ 近似下，零阶未微扰哈密顿量可完全解析对角化：
$$E(I, K, n_\beta, n_\gamma) = \left( n_\beta + \frac{1}{2} \right) \hbar\omega_\beta + \left( 2 n_\gamma + 1 + \frac{1}{2}|K| \right) \hbar\omega_\gamma + \frac{\hbar^2}{2\mathcal{J}_0} \left[ I(I+1) - K^2 \right],$$
其中 $\mathcal{J}_0 = 3 B \beta_0^2$ 为基态平衡转动惯量，固有频率 $\omega_\beta = \sqrt{C_\beta / B}, \omega_\gamma = \sqrt{C_\gamma / B}$。

### 集体能带微观分类：
1. **基态转动带 (Ground Band, $n_\beta=0, n_\gamma=0, K=0$)**：
   $$E_{\text{g.s.}}(I) = \frac{\hbar^2}{2\mathcal{J}_0} I(I+1), \quad I = 0^+, 2^+, 4^+, 6^+, \dots;$$
2. **$\beta$ 振动带 ($\beta$ Band, $n_\beta=1, n_\gamma=0, K=0$)**：
   带首为 $0_\beta^+$ 态，激发能量为 $\hbar\omega_\beta$，具有特征的单极跃迁 $E0(0_\beta^+ \to 0_{\text{g.s.}})$；
3. **$\gamma$ 振动带 ($\gamma$ Band, $n_\beta=0, n_\gamma=0, K=2$)**：
   带首为 $2_\gamma^+$ 态，激发能量为 $\hbar\omega_\gamma - \frac{2\hbar^2}{\mathcal{J}_0}$，允许自旋序列包含全部整数：$I = 2^+, 3^+, 4^+, 5^+, \dots$。

---

## 3. 离心拉伸修正与 Mikhailov 带间跃迁展开

转动项随自旋上升引入离心势能，迫使核表面向外拉伸（Centrifugal Stretching）：
$$\xi_{\text{eq}}(I) \approx \frac{\hbar^2 I(I+1)}{3 B \beta_0^3 \omega_\beta^2}.$$
代入转动能量导出高阶可变惯量修正（VMI 展开）：
$$E(I) = A I(I+1) - B [I(I+1)]^2,$$
微观证明转动带在高自旋下的回弯前能级压缩效应源自 $\beta$ 振动核芯的离心形变膨胀。同时，通过一阶微扰论给出带间 $E2$ 跃迁对经典 Alaga 定则的 Mikhailov 线性偏离参数。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/greiner-asymmetric-rotor-and-rvm-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`mariscotti-vmi` 子命令)
- **上游来源**：`knowledge/sources/book-greiner-nuclear-models.md`
