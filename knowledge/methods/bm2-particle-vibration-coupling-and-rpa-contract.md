---
type: method
title: "Bohr & Mottelson Vol. II：粒子–振动耦合微观机制、有效电荷极化与 RPA 色散关系合同"
aliases: [BM2 particle-vibration coupling, BM2 Section 6-5 RPA, microscopic effective charge polarizability, phonon-mediated interaction, RPA dispersion relation]
method_type: "particle-vibration-coupling-rpa-contract"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Bohr & Mottelson Nuclear Structure Vol. II, Chapter 6 Section 6-5 (printed pp.416-435 / PDF pp.438-457), Eqs. 6-204 to 6-276, and Figures 6-7 to 6-8"
confidence: "high for analytical particle-vibration Hamiltonians, polarizability derivations, and RPA dispersion relations"
tags: [bohr-mottelson, vol2, particle-vibration, polarizability, effective-charge, rpa, qrpa, phonon-coupling, dispersion-relation]
sources: [book-bohr-mottelson-nuclear-structure-vol2]
---

# Bohr & Mottelson Vol. II：粒子–振动耦合微观机制、有效电荷极化与 RPA 色散关系合同

## Purpose

本方法合同基于 Aage Bohr 与 Ben R. Mottelson 的巨著《Nuclear Structure》第二卷第 6 章 §6-5 的系统研究，
解决原子核多体物理中单粒子运动与宏观集体振动之间的微扰耦合、有效电荷微观起源、声子媒介残余核力以及微观无规相位近似（RPA）集体色散方程的理论难题：
通过将核表面四极/八极振动场作为粒子–空穴激发的相干势场，
严格推导一阶粒子–振动耦合矩阵元（含表面形状因子 \(k_\lambda(r) = -R_0 \partial V_0/\partial r\)）、单粒子跃迁算符的有效极化常数 \(\chi_F\)，
导出声子媒介诱发的长程四极–四极（\(Q \cdot Q\)）与单极配对有效两体相互作用，
并由自洽场响应理论解析推导包含向后传播 \(Y\) 振幅（基态关联）的微观 **RPA 色散关系方程**，
为超流核集体振动与高自旋退激提供自洽的微观基础：

1. **一阶粒子–振动耦合哈密顿量（式 6-204–6-213、图 6-7）**：建立单粒子在振动态发射与吸收声子的微扰算符 \(H' = -\sum_\mu \alpha_{\lambda\mu} k_\lambda(r) Y_{\lambda\mu}^*(\theta, \phi)\)，导出单核子跃迁矩阵元与 BCS 准粒子因子（\(\Delta\pi=(-1)^\lambda\)）；
2. **有效电荷与微观极化常数（式 6-215–6-216、图 6-8）**：解析证明单粒子电磁多极算符经由高能巨共振虚激发产生的相干屏蔽，重整化为有效算符 \(\mathcal{M}_{\rm eff} = (1 + \chi_F) \mathcal{M}_{\rm bare}\)，微观奠定 \(e_{\rm eff}(p) \a1.5e\) 与 \(e_{\rm eff}(n) \a0.5e\)；
3. **声子媒介有效两体相互作用（式 6-258–6-261）**：证明粒子与核表面振动交换虚声子诱发粒子间的吸引相互作用（核物理中的声子媒介 Cooper 配对机制），直接推导出有效四极–四极（\(Q \cdot Q\)）力；
4. **微观 RPA 色散方程严格推导（式 6-28–6-30、6-276）**：通过自洽极化响应推导包含向前（\(X\)）与向后（\(Y\)）时间双向传播的 RPA 本征方程：
   \[
   \frac{1}{\kappa} = \sum_{p h} \left[ \frac{|\langle p  \vert F  \vert h  \rangle|^2}{\varepsilon_p - \varepsilon_h - \hbar\omega} + \frac{|\langle p  \vert F  \vert h  \rangle|^2}{\varepsilon_p - \varepsilon_h + \hbar\omega} \right]
   \]
   阐明基态量子关联使最低集体态能量压低至非相干单粒子间距（\(2\Delta\)）之下，同时电多极跃迁振幅获得 \((X+Y)\) 相干极大放大的物理机制。

---

## Inputs and Assumptions

### 1. 表面形变形状因子与微扰小振幅假定

假定平衡势为伍德–萨克森（Woods-Saxon）或谐振子势 \(V_0(r)\)，核半径随多极振动发生微小动态伸缩：
\[
\delta V(r, \theta, \phi) = - R_0 \frac{\partial V_0}{\partial r} \sum_{\lambda\mu} \alpha_{\lambda\mu} Y_{\lambda\mu}^*(\theta, \phi) \equiv k_\lambda(r) \sum_\mu \alpha_{\lambda\mu} Y_{\lambda\mu}^*
\]
零点振动振幅满足 \(\alpha_0 = \sqrt{\frac{\hbar\omega_\lambda}{2C_\lambda}} \ll 1\)，使得粒子–振动耦合可在一阶微扰框架下展开。

### 2. 玻色子换算与准粒子因子

声子算符满足标准玻色子对易关系 \([b_{\lambda\mu}, b_{\lambda'\mu'}^\dagger] = \delta_{\lambda\lambda'} \delta_{\mu\mu'}\)。
在开壳超流核中，单粒子算符通过 Bogoliubov 变换引入 BCS 因子：
- 对自旋无关电多极跃迁（如 \(E2, E3\)）：引入因子 \((u_1 v_2 - v_1 u_2)\)（粒子–空穴对产生）或 \((u_1 u_2 - v_1 v_2)\)（准粒子散射）；
- 对磁多极跃迁（如 \(M1\)）：引入因子 \((u_1 u_2 + v_1 v_2)\)。

---

## What It Can Establish

### 1. 粒子–振动耦合矩阵元解析解（式 6-208–6-213）

单核子态 \(\vert j_1 m_1\rangle\) 散射到 \(\vert j_2 m_2\rangle\) 并激发一个 \(\lambda\) 极性声子的微扰矩阵元为：
\[
\langle j_2, n_\lambda=1; I=j_1  \vert H'  \vert j_1, n_\lambda=0  \rangle = \frac{\alpha_0}{\sqrt{2j_1 + 1}} \langle  j_2 \vert| k_\lambda(r) Y_\lambda |\vert  j_1 \rangle
\]
其中约化矩阵元严格满足几何因式分解：
\[
\langle  j_2 \vert| k_\lambda(r) Y_\lambda |\vert  j_1 \rangle = (-1)^{j_1 + 1/2} \sqrt{\frac{(2j_1+1)(2j_2+1)(2\lambda+1)}{4\pi}} \begin{pmatrix} j_1 & \lambda & j_2 \\ 1/2 & 0 & -1/2 \end{pmatrix} \langle j_2  \vert k_\lambda(r)  \vert j_1  \rangle
\]
**自旋翻转禁戒定则**：当 \(j_1, j_2 \gg \lambda\) 时，Wigner \(3j\) 符号在 \(\Delta j = \Delta l\)（无自旋翻转）时具有最大值，而在自旋翻转（\(\Delta j \ne \Delta l\)）时受到显著代数压制。

### 2. 微观有效电荷与极化系数（式 6-215–6-216）

价核子在核芯外运动时，通过虚激发高能等标巨四极共振（\(2\hbar\omega_0 \sim 80 A^{-1/3}\text{ MeV}\)）与等矢量巨四极共振（\(E_{\rm IVGQR} \sim 130 A^{-1/3}\text{ MeV}\)），
驱动核芯全部质子发生同相集体极化，其穿衣粒子（Clothed particle）有效跃迁算符为：
\[
\mathcal{M}_{\rm eff}(E\lambda) = e_i r^\lambda Y_{\lambda\mu} + \sum_{\text{phonons}} \frac{\langle 0  \vert H'  \vert \text{phonon}  \rangle \langle \text{phonon}  \vert \mathcal{M}  \vert 0  \rangle}{\Delta E_{\rm phonon}} = e_i (1 + \chi_F) r^\lambda Y_{\lambda\mu}
\]
微观极化系数满足：
\[
\chi_F = \frac{\kappa_\lambda \alpha_{0\lambda}^2}{\hbar\omega_\lambda - \Delta E}
\]
定量给出长程引力极化导致中子获得感生有效电荷 \(e_{\rm pol}(n) \a0.5e\)，质子有效电荷增强至 \(e_{\rm eff}(p) \a1.5e\)。

### 3. 声子媒介诱发有效两体核力（式 6-258–6-261）

两个价核子通过与同一核芯集体振动模交换虚声子，导出能量依赖的有效两体相互作用势：
\[
V_{\rm eff}(\vec r_1, \vec r_2) = - \sum_{\lambda\mu} \frac{\alpha_{0\lambda}^2}{\hbar\omega_\lambda} k_\lambda(r_1) k_\lambda(r_2) Y_{\lambda\mu}^*(\Omega_1) Y_{\lambda\mu}(\Omega_2)
\]
在四极通道（\(\lambda=2\)）下，这正是长程有效四极–四极相互作用（\(-\chi_Q Q \cdot Q\)）的微观物理起源；
在单极对振动通道下，导出有效吸引配对相互作用（\(-G P^\dagger P\)）。

### 4. 微观自洽 RPA 色散关系方程（式 6-28–6-30、6-276）

考虑粒子–空穴相互作用强度 \(\kappa\)，体系对多极激发场 \(F\) 的动态响应极点满足自洽分散方程：
\[
\frac{1}{\kappa} = \chi_0(\omega) = \sum_{p h}  \vert \langle p  \vert F  \vert h   \rangle|^2 \left[ \frac{1}{\varepsilon_p - \varepsilon_h - \hbar\omega} + \frac{1}{\varepsilon_p - \varepsilon_h + \hbar\omega} \right]
\]
- **向前振幅 \(X_{ph}\)** 与 **向后振幅 \(Y_{ph}\)** 满足微观耦合方程组：
  \[
  \begin{pmatrix} A & B \\ -B^* & -A^* \end{pmatrix} \begin{pmatrix} X \\ Y \end{pmatrix} = \hbar\omega \begin{pmatrix} X \\ Y \end{pmatrix}
  \]
- **跃迁几率的相干放大机制**：电多极跃迁矩阵元正比于 \(\sum_{ph} (X_{ph} + Y_{ph}) \langle  p \vert| \mathcal{M} |\vert  h \rangle\)；
  由于 \(X\) 与 \(Y\) 振幅同相叠加，其跃迁几率与 \((X+Y)^2\) 成正比，微观阐明了低激发 \(2_1^+\) 态 \(B(E2)\) 超越单粒子 Weisskopf 单位数十至数百倍的巨大集体相干起源。

---

## What It Cannot Establish Alone

1. **简谐 RPA 在相变点附近发散**：
   当两体相互作用强度 \(\kappa\) 逼近临界失稳值时，最低能根 \(\hbar\omega \to 0\)，RPA 运动方程矩阵出现虚本征值，表明基态球形真空崩溃，系统发生自发破缺转向静态形变转子（需采用玻尔 5D 势能面或角动量投影 AMP）；
2. **忽略了多声子非简谐声子散射**：
   一阶粒子–振动耦合模型只保留单声子交换过程，在高激发能区或大振幅四极振动中，声子–声子两体相互作用引起声子劈裂与阻尼，需采用粒子–振动耦合扩展网络（NFT 或 QPM）；
3. **有效形状因子 \(k(r)\) 依赖微观平均场自洽性**：
   简单的表面导数形式 \(-R_0 \partial V/\partial r\) 忽略了中子皮（Neutron skin）与核芯各向同性密度的微观径向收缩，高精度分析需结合基于 Skyrme 或相对论点耦合泛函的自洽微观 QRPA 计算。

---

## Sources

- [[book-bohr-mottelson-nuclear-structure-vol2]]：A. Bohr & B. R. Mottelson, *Nuclear Structure*, Vol. II: *Nuclear Deformations*, Chapter 6 §6-5 (pp. 416–435), Eqs. 6-204 to 6-276.
- [[quasiparticle-random-phase-approximation-qrpa-dynamics]]：准粒子无规相位近似（QRPA）、基态关联与多体集体振动动力学。
- [[bm2-collective-vibrations-and-sum-rules-contract]]：Bohr & Mottelson Vol. II 第 6 章正规振动模式、求和规则与 CAP 机制合同。
- [[book-suhonen-from-nucleons-to-nucleus]]：J. Suhonen, *From Nucleons to Nucleus*, Springer (2007), Chapters 13–18.
