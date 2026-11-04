# 第 12 章 (一)：方向角分布理论、统计取向张量与几何 $F_k$ 系数

**来源专著**：W. D. Hamilton《The Electromagnetic Interaction in Nuclear Spectroscopy》（1975）第 12 章
**对应页码**：印刷 pp. 505–550 / 物理 PDF pp. 505–550

---

## 1. 核心理论推导与统计取向张量

### 1.1 密度矩阵与统计取向张量 $\rho_{kq}(I)$
激发核系综的宏观空间取向状态由密度矩阵 $\rho_{m m'}$ 完备描述。在不可约球张量基底上展开：
$$\rho_{kq}(I) = \sum_{m, m'} (-1)^{I-m'} \langle I m I -m' | k q \rangle \rho_{m m'}.$$
- **轴对称反应系统的退化**：
  在重离子熔合蒸发或库仑激发反应中，由于绕束流轴具有柱对称性且时间反演守恒：
  1. 非对角相干项严格为零：$\rho_{kq \ne 0} \equiv 0$；
  2. 奇数阶张量严格为零：$\rho_{1, 0} = \rho_{3, 0} = \dots = 0$；
  3. 引入标准无量纲**轴对称取向参数 (Orientation Parameter $B_k(I)$)**：
     $$B_k(I) = \sqrt{2I+1} \sum_{m=-I}^I (-1)^{I-m} \langle I m I -m | k 0 \rangle P(m), \quad B_0(I) \equiv 1.$$

### 1.2 高斯磁子态布居与自旋取向参数 $\sigma/I$
熔合反应中转移的大角动量垂直于反应平面，形成以 $m=0$ 为中心的对称高斯磁子态布居：
$$P(m) = \frac{\exp(-m^2 / 2\sigma^2)}{\sum_{m'=-I}^I \exp(-m'^2 / 2\sigma^2)}.$$
- 重离子熔合反应典型实测取向参数为：$\sigma/I \a0.28 - 0.35$；
- 随自旋 $I$ 增大，高斯布居越来越尖锐，统计张量 $B_2(I)$ 与 $B_4(I)$ 随之单调升高并趋近于完全对齐理论上限 $B_k^m_{\max}(I)$。

---

## 2. 方向角分布函数 $W(\theta)$ 与 $F_k$ 系数分解

### 2.1 勒让德多项式展开与因子化定理
对齐核发射光子在相对于束流轴角 $\theta$ 处的方向角分布函数为：
$$W(\theta) = 1 + A_2 P_2(\cos\theta) + A_4 P_4(\cos\theta),$$
其中各项异性系数严格因子化为初始核态取向度与电磁跃迁几何因子的乘积：
$$A_k(I_i \to I_f) = B_k(I_i) \cdot R_k(L, L', I_i, I_f).$$

### 2.2 Ferentz-Rosenzweig 几何 $F_k$ 系数
电磁跃迁几何因子 $R_k$ 由 Wigner $3j$ 与 Racah $W$ 系数完全确定：
$$F_k(L L' I_f I_i) = (-1)^{I_f - I_i - 1} \sqrt{(2I_i+1)(2L+1)(2L'+1)} \langle L 1 L' -1 | k 0 \rangle W(I_i I_i L L'; k I_f).$$
- **混合多极跃迁解析展开**（如 $M1+E2$ 跃迁，带入多极混合比 $\delta$）：
  $$R_k(L L' I_i I_f) = \frac{F_k(L L I_f I_i) + 2 \delta F_k(L L' I_f I_i) + \delta^2 F_k(L' L' I_f I_i)}{1 + \delta^2}.$$
  此式是核谱学根据实验各向异性系数 $A_2, A_4$ 提取多极混合比 $\delta$ 的第一性基本方程。

---

## 3. 在束谱学应用：探头有限立体角衰减因子 $Q_k$
实际 HPGe 探测器晶体具有有限正面半径与吸收深度，不能视作几何质点。实际测得的实验角分布系数被平滑衰减：
$$A_k^{\text{meas}} = Q_k(E_\gamma) \cdot A_k^{\text{true}},$$
其中衰减因子 $Q_k \in [0, 1]$：
$$Q_k = \frac{\int_0^{\alpha_m_{\max}} P_k(\cos\alpha) \epsilon(\alpha) \sin\alpha d\alpha}{\int_0^{\alpha_m_{\max}} \epsilon(\alpha) \sin\alpha d\alpha}.$$
对于距靶 $15\text{ cm}$ 的同轴 HPGe 晶体，典型衰减因子为 $Q_2 \a0.96 - 0.98$，$Q_4 \a0.88 - 0.93$，在提取物理混合比 $\delta$ 前必须首先执行严格的几何去卷积校正。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/hamilton-angular-distribution-dco-polarization-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`angular-distribution` 子命令)
- **上游来源**：`knowledge/sources/book-hamilton-electromagnetic-interaction.md`
