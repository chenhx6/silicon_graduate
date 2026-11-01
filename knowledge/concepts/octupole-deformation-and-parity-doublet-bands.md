---
type: concept
title: "原子核八极形变、反射不对称性与宇称双重带动力学"
aliases: [八极形变, 梨形核, 宇称双重带, 内禀电偶极矩D0, 反射不对称性, Octupole Deformation]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [octupole-deformation, parity-doublets, reflection-asymmetry, intrinsic-dipole-moment, e1-transitions, pear-shaped-nuclei]
---

# 原子核八极形变、反射不对称性与宇称双重带动力学

## 1. 物理全景：空间反演对称性（$\mathcal{P}$）的宏观自发破缺

在低能核物理中，绝大多数偶偶核的基态具有正宇称（$J^\pi = 0^+$），且在内禀系中具有反演中心（$\mathcal{P} \vec{r} = -\vec{r}$，四极形变满足 $\beta_2$ 对称性）。然而，在特定的质子数和中子数孤岛中，核表面会自发发生**反射不对称的八极形变（Octupole Deformation: $\beta_3 \ne 0$）**，原子核宏观上呈现两端粗细不一的**梨形（Pear shape）**。

根据 P. A. Butler & W. Nazarewicz（Rev. Mod. Phys. 68, 349, 1996）与 A. Bohr & B. R. Mottelson《Nuclear Structure》Vol. II：
1. **微观驱动机制（$\Delta j = \Delta l = 3$ 轨道耦合）**：
   当费米面附近同时存在一对满足选择定则 $\langle j_1 l_1 || Y_3 || j_2 l_2 \rangle \ne 0$（即 $\Delta j = 3, \Delta l = 3$ 且初末态宇称相反）的入侵高 $j$ 轨道与正常壳层轨道时，长程八极相互作用克服单粒子能隙，诱发自发反射对称性破缺；
2. **四大特征质量区**：
   - 轻核区：$Z, N \approx 10$（如 $^{20}\text{Ne}$）；
   - $A\approx 80$ 质量区：$Z, N \approx 34 \sim 38$（$\pi(p_{3/2}, g_{9/2})$ 与 $\nu(p_{3/2}, g_{9/2})$，如 $^{78}\text{Br}, {}^{74}\text{As}$）；
   - **$A\approx 144$ 质量区（本 Wiki 紧邻核区！）**：$Z \approx 56 \sim 58, N \approx 88 \sim 90$（$\pi(d_{5/2}, h_{11/2})$ 与 $\nu(f_{7/2}, i_{13/2})$，如 $^{144}\text{Ba}, {}^{146}\text{Ce}, {}^{148}\text{Nd}$）；
   - 锕系区：$Z \approx 88 \sim 90, N \approx 134 \sim 136$（如 $^{224}\text{Ra}, {}^{226}\text{Th}$）。

---

## 2. 宇称双重带（Parity Doublets）与单极量子数（Simplex）

### (1) 双势阱隧道穿透与正负宇称交错带
在反射不对称八极形变势下，内禀系存在两个互为镜像的定态 $|\Phi_+\rangle$（梨尖朝上）与 $|\Phi_-\rangle$（梨尖朝下），由有限八极势垒阻隔。
在旋转坐标系中，镜像态通过势垒发生微观量子隧道穿透，对称性恢复，在实验室系投影为**两条交错的正负宇称伴随能带**：
- 正宇称序列：$0^+, 2^+, 4^+, 6^+, \dots$
- 负宇称序列：$1^-, 3^-, 5^-, 7^-, \dots$

定义**宇称能隙位移参量（Parity Splitting Displacement）**：
$$\delta E(I) = E(I^-) - \frac{1}{2}[E((I-1)^+) + E((I+1)^+)]$$
随转动自旋增加，转动离心力压制了八极势垒，$\delta E(I) \to 0$，正负宇称能态演化为严格等间距交错的单一转动序列！

### (2) 单极量子数（Simplex Quantum Number, $s$）
定义绕对称轴旋转 $180^\circ$ 与空间反演的复合操作 $\mathcal{S} = \mathcal{P} \mathcal{R}_y^{-1}(\pi)$。其特征本征值为：
$$s = p \cdot e^{-i\pi I} = \pm 1 \quad (\text{偶偶核}) \quad \text{或} \quad \pm i \quad (\text{奇} A \text{核})$$
在刚性八极形变核中，正负宇称带共享同一个单极量子数 $s=+1$ 或 $s=-1$。

---

## 3. 内禀电偶极矩 $D_0$ 与超强交错 $E1$ 跃迁

### (1) 质心-电荷中心分离与内禀偶极矩 $D_0$
在轴对称拉长四极核中，电荷中心与质量中心重合，宏观内禀电偶极矩严格为零（$D_0 \equiv 0$）。
但在具有八极形变（$\beta_3$）的梨形核中，由于质子电荷流与中子质量流在非对称边界下的不对称极化，原子核产生巨大的**内禀静态电偶极矩（Intrinsic Dipole Moment, $D_0$）**：
$$D_0 \approx C_{\text{dipole}} \cdot A Z e \cdot \beta_2 \beta_3 \quad (\text{典型数值高达 } D_0 \approx 0.1 \sim 0.4\text{ e}\cdot\text{fm})$$

### (2) 增强 $E1$ 跃迁几率与 $B(E1)/B(E2)$ 分支比
巨大的内禀 $D_0$ 使得正负宇称带之间的跨带交错跃迁呈现出极度反常的**超强电偶极辐射（Enhanced $E1$）**：
$$B(E1; I \to I-1) = \frac{3}{4\pi} e^2 D_0^2 \cdot (C_{I 0 1 0}^{I-1, 0})^2 \approx 10^{-3} \sim 10^{-2}\text{ W.u.}$$
（比常规单粒子跃迁阻碍 $10^{-6}\text{ W.u.}$ 强数千倍！）。

在实验能谱中，通过测量跨带 $E1$ 射线与带内四极 $E2$ 射线的发射强度比，直接提取无量纲分支比：
$$\frac{B(E1; I \to I-1)}{B(E2; I \to I-2)} = 0.77 \frac{E_\gamma^5(E2)}{E_\gamma^3(E1)} \frac{I_\gamma(E1)}{I_\gamma(E2)} \times 10^{-6}\text{ (fm}^{-2}\text{)}$$
并由转动模型反演绝对内禀偶极矩：
$$|D_0| = \sqrt{ \frac{5}{16} \frac{B(E1)/B(E2)}{Q_t^2} } \cdot \frac{C_{I 0 2 0}^{I-2, 0}}{C_{I 0 1 0}^{I-1, 0}}$$

---

## 4. 八极形变与三轴手征性的交叉判据

在紧邻 $A\approx 130$ 的过渡区核中：
1. **八极与手征的复合**：当三轴形变（$\gamma \approx 30^\circ$）与八极形变（$\beta_3 \ne 0$）共存时，时间反演与空间反演联合对称性破缺，形成手征-八极宇称四重带（Chiral-Parity Quartets）；
2. **伪八极带排除法规**：若在实验中仅观察到负宇称带靠近正宇称带，但未测得增强的 $B(E1)$ 跃迁（$D_0 < 0.05\text{ e}\cdot\text{fm}$），绝不能宣布为八极形变，只能归为常规的单粒子八极声子八极振动耦合！
