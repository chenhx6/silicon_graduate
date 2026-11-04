---
type: method
title: "Bohr & Mottelson Vol. II：集体振动正规模式、多极能量加权求和规则（EWSR）与 CAP 机制合同"
aliases: [BM2 collective vibrations, BM2 Chapter 6 normal modes, beta and gamma vibrations, EWSR sum rules TRK, Mottelson-Valatin CAP, Strutinsky shell correction BM2]
method_type: "collective-vibrations-and-sum-rules-contract"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Bohr & Mottelson Nuclear Structure Vol. II, Chapter 6 Section 6-3b (printed pp.361-365 / PDF pp.383-387), Section 6-4 (printed pp.399-415 / PDF pp.421-437), Section 4-3a (pp.42-43), and pp.598-634"
confidence: "high for analytical double-commutator sum rules, harmonic vibration group theory, and Strutinsky macro-microscopic energy surfaces"
tags: [bohr-mottelson, vol2, collective-vibrations, beta-vibration, gamma-vibration, ewsr, trk-sum-rule, cap-effect, strutinsky-method, fission-barrier]
sources: [book-bohr-mottelson-nuclear-structure-vol2]
---

# Bohr & Mottelson Vol. II：集体振动正规模式、多极能量加权求和规则（EWSR）与 CAP 机制合同

## Purpose

本方法合同基于 Aage Bohr 与 Ben R. Mottelson 的巨著《Nuclear Structure》第二卷第 6 章 §6-3、§6-4 以及第 4 章 §4-3a 的系统研究，
解决原子核在形变平衡态附近的微观集体振动分解、多声子激发多重态劈裂、宏观电磁多极强度的模型无关总和度规（EWSR）以及高自旋超流配对崩溃的理论与实验对账难题：
通过将核表面四极形变分解为沿内禀对称轴的保留轴对称模式（\(\beta\) 振动）与破缺轴对称模式（\(\gamma\) 振动），
严格证明两声子 \(\gamma\) 振动态分解为 \(K^\pi = 0^+\) 与 \(K^\pi = 4^+\) 双能带的几何定理，
基于海森堡对易子推导模型无关的经典电磁多极能量加权求和规则（EWSR，涵盖 \(E0, E1, E2, E3\)），
确立巨共振激发能量与核物质不可压缩模量 \(K_\infty\) 的直接关联，
并阐明 Mottelson–Valatin 科里奥利反配对（CAP）相变机制与 Strutinsky 宏观–微观壳修正双峰裂变势垒理论：

1. **球椭平衡态下的四极简谐正规模式（§6-3b、图 6-3）**：
   - \(\nu = 0\)（\(\beta\) 振动）：保持轴对称，\(K^\pi = 0^+\)；
   - \(\nu = \pm 2\)（\(\gamma\) 振动）：破坏轴对称，产生瞬时三轴椭球形变，\(K^\pi = 2^+\)；
   - **多声子劈裂定理**：单声子激发为 \(K^\pi = 2^+\)（\(n_\gamma=1\)），双声子态（\(n_\gamma=2\)）在玻色对称性下严格分裂为 \(K^\pi = 0^+\) 与 \(K^\pi = 4^+\) 两个独立的转动带头；
2. **模型无关的能量加权求和规则（EWSR，§6-4）**：
   利用双对易子定理 \(S(F) = \frac{1}{2}\langle 0  \vert [F^\dagger, [T, F]]  \vert 0 \rangle\)，严格推导仅依赖核基态单体密度分布的普适积分强度：
   - **\(E1\) 模式与 Thomas–Reiche–Kuhn（TRK）求和规则**：导出光核吸收积分截面 \(\sigma_{\rm int} = \int \sigma(E_\gamma)dE_\gamma \approx 60 \frac{NZ}{A}\text{ MeV}\cdot\text{mb}\)；
   - **等标巨四极共振（ISGQR）EWSR**：导出 \(S(E2, \text{IS}) \approx 25.7 Z A^{2/3}\text{ MeV}\cdot e^2\text{fm}^4\)，在 \(E_{\rm GQR} \approx 64 A^{-1/3}\text{ MeV}\) 处耗尽近 100% 强度；
   - **单极呼吸模（ISGMR）EWSR 与核物质不可压缩模量**：导出 \(S(E0, \text{IS}) = \frac{2\hbar^2}{M} Z \langle r^2  \rangle_p\)，实验能峰直接约束 \(K_\infty \approx 230\pm20\text{ MeV}\)；
   - **等标八极（ISGHR / LEOR）EWSR**：导出 \(S(E3, \text{IS}) \a106.6 Z A^{4/3}\text{ MeV}\cdot e^2\text{fm}^6\)；
3. **Mottelson–Valatin 科里奥利反配对（CAP）二级相变（§4-3a，pp. 42–43）**：转动科里奥利力向时间反演配对施加相反力矩，驱动配对能隙随转速单调衰减 \(\Delta(\omega) = \Delta_0 \sqrt{1 - (\omega/\omega_{\rm crit})^2}\)，并在临界自旋 \(I_{\rm CAP}\) 发生向正常费米气体的超流相变；
4. **Strutinsky 壳修正与双峰裂变势垒（§6-3c，pp. 598–634）**：将液滴模型形变能与平滑单粒子壳修正相结合（\(E_{\rm tot} = E_{\rm LDM} + \delta U + \delta P\)），解释双峰裂变势垒（\(E_A, E_B\)）、形状异能态（如 \(^{241}\mathrm{Pu}\) 异能态）及超重核稳定岛机理。

---

## Inputs and Assumptions

### 1. 简谐形变自由度展开

核半径在内禀主轴系下按球谐函数展开：
\[
R(\theta, \phi) = R_0 \left[ 1 + \alpha_{20} Y_{20}(\theta, \phi) + \alpha_{22} (Y_{22} + Y_{2,-2}) \right]
\]
在极小振动近似下，\(\alpha_{20} = \beta\cos\gamma \approx \beta_0 + (\beta - \beta_0)\)，\(\alpha_{22} = \frac{1}{\sqrt{2}}\beta\sin\gamma \approx \frac{1}{\sqrt{2}}\beta_0 \gamma\)。

### 2. 双对易子求和规则条件

电磁跃迁算符 \(F\) 假定仅依赖于核子空间坐标 \(\vec r_k\)，与动量无关；两体核力势能项 \(V(\vec r_1, \dots, \vec r_A)\) 假定与速度无关（对于含交换力或速度依赖力的情况，TRK 给出经典求和下限，实际强度可获得 \(20\% - 40\%\) 的增强）。

---

## What It Can Establish

### 1. 球椭形变核四极正规振动模式分类（式 6-90、图 6-3）

- **\(\beta\) 振动模（\(\nu=0, K^\pi = 0^+\)）**：
  波函数保留轴对称，对应长轴的拉伸与赤道平面的反相收缩；基带与 \(\beta\) 振动带头之间的跃迁为纯电单极 \(E0\) 与电四极 \(E2\)；
- **\(\gamma\) 振动模（\(\nu=\pm 2, K^\pi = 2^+\)）**：
  波函数破坏轴对称，对应赤道平面截面由圆形向椭圆形的往复振荡；
- **双声子激发谱结构**：
  - \(n_\beta = 2, n_\gamma = 0 \implies K^\pi = 0^+\)；
  - \(n_\beta = 1, n_\gamma = 1 \implies K^\pi = 2^+\)；
  - \(n_\beta = 0, n_\gamma = 2 \implies K^\pi = 0^+\) 与 \(K^\pi = 4^+\)（双能带分裂！）；
- 实验测得的 \(\beta\) 与 \(\gamma\) 振动带到基带的电四极跃迁几率约为 \(B(E2) \sim 5 - 10\text{ W.u.}\)，反映相对较少核子参与的小振幅集体相干性（振动振幅 \(\Delta\beta \sim \beta_0 \gamma \sim 0.05\)）。

### 2. 模型无关的电磁能量加权求和规则（EWSR）（式 6-171–6-174）

应用双对易子定理：
\[
[F_\lambda, [T, F_\lambda^\dagger]] = \frac{\hbar^2}{M} \sum_k |\vec\nabla_k F_\lambda|^2
\]
导出任意阶多极场的通用加权求和：
\[
S(F_\lambda) \equiv \sum_a (E_a - E_0) B(F_\lambda; 0 \to a) = \frac{\lambda(2\lambda+1)^2}{4\pi} \frac{\hbar^2}{2M} \int \rho(\vec r) r^{2\lambda-2} d\tau
\]
常用巨共振模式的显式数值标度律：
1. **等标巨四极共振（ISGQR, \(\lambda=2\)）**：
   \[
   S(E2, \text{IS}) = \frac{5}{4\pi} \frac{\hbar^2 e^2}{2M} Z \langle r^2 \rangle_p \approx 25.7 Z A^{2/3} \quad [\text{MeV}\cdot e^2\text{fm}^4]
   \]
   共振峰能量位于 \(E_{\rm GQR} \approx 64 A^{-1/3}\text{ MeV}\)，在所有稳定重核中几乎穷尽 100% 的 EWSR；
2. **等标巨单极共振（ISGMR, 呼吸模, \(E0\)）**：
   \[
   S(E0, \text{IS}) = \frac{2\hbar^2 e^2}{M} Z \langle r^2 \rangle_p \approx 41.1 Z A^{2/3} \quad [\text{MeV}\cdot e^2\text{fm}^4]
   \]
   共振频率直接决定核物质压缩系数 \(K_A = M \langle r^2 \rangle \omega_0^2 \implies K_\infty \approx 230\text{ MeV}\)；
3. **等标巨八极共振（ISGOR, \(\lambda=3\)）**：
   \[
   S(E3, \text{IS}) = \frac{21}{8\pi} \frac{\hbar^2 e^2}{2M} Z \langle r^4 \rangle_p \a106.6 Z A^{4/3} \quad [\text{MeV}\cdot e^2\text{fm}^6]
   \]
   低能八极态（LEOR，如 \(3_1^-\)）通常消耗约 \(15\% - 25\%\) 的总八极求和，其余分布于高能 HEOR。

### 3. Mottelson–Valatin 科里奥利反配对（CAP）微观理论（式 4-42 邻文）

在转动频率 \(\omega\) 下，核子对受到的反向科里奥利力矩为 \(-2\omega j_x\)：
- 在低转速下，自旋二次微扰重整化转动惯量；
- 随转速上升，单极配对能隙遭受单调非线性淬灭：
  \[
  \Delta(\omega) = \Delta_0 \sqrt{1 - \left(\frac{\omega}{\omega_{\rm crit}}\right)^2}
  \]
- 在临界自旋 \(I_{\rm CAP} \a30 \sim 40\hbar\) 处，能隙彻底降为零，系统从 BCS 超流态经历二级相变跃迁为正常刚体费米转子，转动惯量饱和至刚体转动惯量 \(\mathcal{J}_{\rm rig}\)。

### 4. Strutinsky 宏观–微观势能面与裂变同核异能态（式 6-52 邻文、图 6-52）

通过宏观液滴模型（LDM）形变能与 Strutinsky 壳修正 \(\delta U = \sum \epsilon_i - \int \tilde g(\epsilon)\epsilon d\epsilon\) 的叠加：
- 在重核（\(Z \ge 90\)）区，由于高 \(j\) 侵入轨道形成的能级疏密波动，在基态长椭阱（\(\beta \sim 0.25\)）之外形成具有更大形变（\(\beta \sim 0.60\)，轴比 2:1）的第二势能深阱；
- 第二深阱内的转动带构成了寿命在 \(\text{ns} \sim \mu\text{s}\) 量级的自发裂变形状同核异能态（Fission Isomers，如 \(^{241}\mathrm{Pu}\)）；
- 量化了超重核稳定岛（\(Z=114, 120, 126; N=184\)）借助微观壳修正势垒 \(\Delta E_{\rm shell} \sim 6 - 8\text{ MeV}\) 克服液滴模型自发裂变崩溃（\(x \ge 1\)）而稳定存在的机制。

---

## What It Cannot Establish Alone

1. **EWSR 求和规则不给出共振峰的具体展宽与衰变宽度**：
   双对易子积分给出全能量区间的加权积分上限，无法预测巨共振的朗道阻尼（Landau damping）、粒子发射逃逸宽度 \(\Gamma^\uparrow\) 与多粒子–多空穴扩展宽度 \(\Gamma^\downarrow\)；
2. **宏观振动模型无法替代微观 RPA/QRPA 组态解析**：
   简谐振子假定各振动模式相互正交，但在具有显著 \(\gamma\) 软度的过渡核中，\(\beta\) 与 \(\gamma\) 振动发生强烈大振幅耦合，需采用 5D 玻尔哈密顿量或代数 IBM 模型；
3. **CAP 机制中连续相变被单粒子能带交叉掩盖**：
   在真实中重核中，往往是少数高 \(j\) 侵入轨道（如 \(i_{13/2}\) 中子对）在临界自旋处发生急剧的回弯带交叉（Backbending），先于整体宏观 CAP 配对淬灭发生。

---

## Sources

- [[bm2-particle-vibration-coupling-and-rpa-contract]]：Bohr & Mottelson Vol. II §6-5 粒子–振动耦合微观机制与 RPA 色散方程合同。
- [[book-bohr-mottelson-nuclear-structure-vol2]]：A. Bohr & B. R. Mottelson, *Nuclear Structure*, Vol. II: *Nuclear Deformations*, Chapter 6 §6-3 (pp. 361–398), §6-4 (pp. 399–415), §4-3a (pp. 42–43), and pp. 598–634.
- [[giant-resonances-and-deformation-splitting]]：巨共振唯象模型、形变劈裂与 TRK 求和规则法典。
- [[strutinsky-shell-correction-and-plateau-condition]]：Strutinsky 壳修正能平滑方法与台阶条件判定。
- [[coriolis-anti-pairing-and-moment-of-inertia-expansion]]：科里奥利反配对（CAP）与转动惯量非线性膨胀动力学。
