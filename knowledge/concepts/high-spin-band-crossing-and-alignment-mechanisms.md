---
type: concept
title: "高自旋能带交叉、准粒子对解耦对齐与带端终止动力学"
aliases: [高自旋带交叉与回弯, 回弯微观机理, Alignment机制, 带端终止理论, 旋称反转动力学]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [high-spin-physics, backbending, band-crossing, alignment, band-termination, signature-inversion]
---

# 高自旋能带交叉、准粒子对解耦对齐与带端终止动力学

## 1. 物理源头：高角动量下的核多体旋转重构

当原子核被重离子反应注入极高角动量（$I \ge 20 \sim 60\hbar$）并在转动频率 $\hbar\omega \ge 0.3\text{ MeV}$ 下高速推转旋转时，微观单核子受到强烈的经典惯性离心力与**科里奥利力（Coriolis force: $-2\vec{\omega} \times \vec{v}$）**。

根据 A. Bohr & B. R. Mottelson《Nuclear Structure》Vol. II 与 Stefan Frauendorf《Spontaneous symmetry breaking in rotating nuclei》（RMP 2001），Coriolis 相互作用具有反时间反演性，它强烈瓦解基态核子间的 BCS $s$-波配对（Pairing correlation），迫使占据高 $j$ 闯入轨道（Intruder orbits, 如 $h_{11/2}, i_{13/2}$）的核子对自发解耦并沿旋转轴平行对齐，在宏观上表现为著名的**转动回弯（Backbending）与能带交叉（Band Crossing）**。

---

## 2. 回弯机制的理论统一视界：CAP vs Stephens-Simon

### (1) Mottelson-Valatin Coriolis 反配对假说（CAP Effect, 1960）
假定随角速度 $\omega$ 增加，Coriolis 力连续弱化单粒子能态间的对关联能隙 $\Delta$，直到在临界角速度 $\omega_c$ 处配对能隙完全塌缩（$\Delta \to 0$），转动惯量从超流转动惯量 $\mathcal{J}_{\text{pair}} \approx 0.4 \sim 0.5 \mathcal{J}_{\text{rigid}}$ 突变为全刚体惯量 $\mathcal{J}_{\text{rigid}}$。

### (2) Stephens & Simon 准粒子对解耦对齐模型（Alignment, 1972）
现代微观实验谱学证实：回弯不是全核超流配对的平滑消失，而是**个别特定高 $j$、低 $\Omega$ 轨道上的单对准粒子发生离散的突变解耦对齐**：
1. 在基态带（$g$-band）中，全体核子配对为时间反演共轭态（$J^\pi = 0^+$）；
2. 当转动频率 $\hbar\omega$ 达到约 $0.25 \sim 0.35\text{ MeV}$ 时，占据高 $j$ 轨道（如稀土区的 $\nu i_{13/2}$ 或 $A\approx 130$ 区的 $\pi h_{11/2}$）的一对核子被 Coriolis 力拉开；
3. 这一对准粒子迅速沿旋转轴 $x$ 平行对齐，贡献高达 $i_x = 2j - 1$（如 $i_{13/2}$ 贡献 $12\hbar$，$h_{11/2}$ 贡献 $10\hbar$）的内禀角动量；
4. 解对后形成的“解耦带（$s$-band, Superband）”能量显著低于原基带，两条带在临界频率发生**带交叉（Band crossing）**。若二者相互作用矩阵元 $V_{\text{int}}$ 很小，在 $I$ vs $\hbar\omega$ 图像上便呈现出急剧向后折返的“回弯”。

---

## 3. Harris 三参数展开与角动量对齐量 $i_x$ 提取算法

在数据分析中，为从宏观总自旋中分离出解耦准粒子的真实内禀贡献，必须扣除纯集体核心转动的平滑基线：

### (1) Harris 两参数/三参数可变转动惯量公式
定义集体核芯转动惯量展开：
$$\mathcal{J}_{\text{core}}(\omega) = \mathcal{J}_0 + \mathcal{J}_1 \omega^2$$
核芯参考角动量为积分结果：
$$I_{\text{ref}}(\omega) = \int_0^\omega \mathcal{J}_{\text{core}}(\omega') d\omega' = \mathcal{J}_0 \omega + \frac{1}{3} \mathcal{J}_1 \omega^3$$
对于 $A\approx 130$ 质量区偶偶核芯（如 $^{132}\text{Ce}, {}^{134}\text{Nd}$），典型 Harris 参数通常拟合为：
$$\mathcal{J}_0 \approx 12 \sim 18\text{ }\hbar^2\text{MeV}^{-1}, \quad \mathcal{J}_1 \approx 25 \sim 40\text{ }\hbar^4\text{MeV}^{-3}$$

### (2) 准粒子对齐量 $i_x$ 与 Routhian 能量提取
对于给定的实验转动能级序列 $E(I)$：
1. **实验转动角速度**：$\hbar\omega = \frac{E(I+1) - E(I-1)}{I_x(I+1) - I_x(I-1)} \approx \frac{E_\gamma}{2}$；
2. **总角动量在转动轴上的投影**：$I_x = \sqrt{(I + 1/2)^2 - K^2}$；
3. **准粒子角动量对齐量（Alignment）**：
   $$i_x(\omega) = I_x(\omega) - I_{\text{ref}}(\omega)$$
4. **旋转坐标系准粒子能量（Routhian Energy）**：
   $$e'(\omega) = E(I) - \omega I_x(I) - E_{\text{ref}}(\omega)$$
通过绘制 $i_x$ vs $\hbar\omega$ 曲线，对齐平台的高度直接暴露出回弯解对的微观轨道轨道角动量（单粒子指纹）！

---

## 4. 旋称反转（Signature Inversion）与带端终止（Band Termination）

### (1) 旋称反转微观动力学
在奇奇核与强三轴核中，正常情况下有利旋称态（Favored signature $\alpha_f$）能量低于不利旋称态（Unfavored $\alpha_u$）。
然而在 $A\approx 130$ 区（如 $^{126,128}\text{Cs}, {}^{130,132}\text{La}$），低自旋下常常观察到不利旋称态能量反而低于有利旋称态（旋称反转）。微观 TAC 与 PRM 模型表明：**这是三轴形变（$\gamma \approx 30^\circ$）与质子-中子残余相互作用（$V_{pn}$）在低转动频率下协同打破常规 Coriolis 排序的独有物理解释**。

### (2) 能带平滑终止（Smooth Band Termination）
当能带自旋继续上升至极端高自旋极限时，外层价核子的全部独立轨道角动量被 Coriolis 力完全拉向转动轴（$M = \sum j_i = I_{\text{max}}$）。
此时，**已不再有剩余的微观单粒子自由度可供集体转动**，系统由大四极形变的集体转动光滑演化为沿对称轴取向的非集体扁椭球态（Oblate state with $\gamma = 60^\circ$）。在谱线上表现为能级间距骤增、转动惯量断崖式下跌，集体跃迁 $B(E2)$ 彻底淬灭（消失至单粒子极限以下）。
