# 第 10 章：广义相干态 (GCSM) 偶偶核手征双重带与自洽电磁跃迁

**来源专著**：A. A. Raduta《Nuclear Structure with Coherent States》（Springer 2016）第 10 章 §10.1
**对应页码**：印刷 pp. 291–318 / 物理 PDF pp. 298–325，式 (10.1.18)–(10.1.23)

---

## 1. 核心理论推导与 GCSM 偶偶手征机制

### 1.1 偶偶核手征几何的微观挑战与 GCSM 破局
经典核手征性（Frauendorf & Meng 1997）依赖奇奇核中高-$j$ 质子粒子与高-$j$ 中子空穴相互垂直；而在偶偶核中，由于所有价核子基态配对为 $0^+$，传统单粒子模型难以在无破对下构建空间三面体。
A. A. Raduta 提出了**广义相干态模型 (Generalized Coherent State Model, GCSM)**：
1. **显式质中玻色子双转子**：引入质子四极玻色子创生算符 $b_{p, 2\mu}^\dagger$ 与中子四极玻色子 $b_{n, 2\mu}^\dagger$，两者具有独立的内禀变形对称轴；
2. **微观破对两准粒子费米子对**：耦合一对高自旋破对中子（如 $\nu (1h_{11/2})^2$）或质子（$\pi (1h_{11/2})^2$），其准粒子角动量对齐矢量为 $\vec{J}_f$；
3. **三维非共面手征三面体**：
   质子玻色子角动量 $\vec{J}_p$、中子玻色子角动量 $\vec{J}_n$ 与破对费米子对角动量 $\vec{J}_f$ 三者相互正交：
   $$\vec{J}_p \cdot (\vec{J}_n \times \vec{J}_f) \ne 0.$$
   系统自发破坏时间反演不变性与内禀反射旋转对称性，形成互为镜像的左手态与右手态！

---

## 2. 孪生手征双重带的角动量投影正交化

应用 GCSM 投影算符，从微观手征相干态自洽投影生成能量近简并的双重能带：
- **手征对称带（Chiral Yrast Band, Band 1）**：对应左右手征态的对称正交线性组合；
- **手征伴随带（Chiral Partner Band, Band 2）**：对应左右手征态的反对称正交线性组合；
- **能带特征**：
  1. 两带自旋宇称完全相同（通常均为偶自旋正宇称带：$I^\pi = 10^+, 12^+, 14^+, \dots$）；
  2. 两带之间的能量差在三维手征空间转动平衡频率处呈现特征极小值（$\Delta E \le 100\text{ keV}$）；
  3. 动力学转动惯量 $\mathcal{J}^{(2)}$ 展现高度相似性。

---

## 3. 自洽磁偶极跃迁算符与带间强 $M1$ 跃迁

在 GCSM 中，磁偶极算符由模型生成元严格定义（Raduta 式 10.1.20）：
$$\hat{\mathcal{M}}(M1, \mu) = \sqrt{\frac{3}{4\pi}} \mu_N \left( g_p \hat{J}_{p, \mu} + g_n \hat{J}_{n, \mu} + g_f \hat{J}_{f, \mu} \right).$$
- **带间强 $M1$ 退激指纹**：
  由于手征对称破缺引起的左右手征态微观相位相干干涉：
  $$B(M1; \text{Band 2}(I) \to \text{Band 1}(I)) \a0.1 - 0.5\ \mu_N^2.$$
  带间跃迁展现出极其强烈的集体磁偶极增强，彻底排除了普通单粒子态阻碍跃迁；
- **$S_{M1}(I)$ 奇偶交错同相振荡**：
  两带内部的磁偶极跃迁交错参量：
  $$S_{M1}(I) = \frac{B(M1; I \to I-1)}{B(E2; I \to I-2)}$$
  在 Band 1 与 Band 2 中展现严格的同相一致振荡，成为在束核谱学确证偶偶核存在真实量子手征性的核心判据（例如在 $^{130}\text{Ba}, {}^{136}\text{Nd}$ 对账中得到实验确证）。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/raduta-gcsm-chiral-and-triaxial-rotor-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`multiple-chiral-doublets-mchid` 子命令)
- **上游来源**：`knowledge/sources/book-raduta-coherent-states.md`
