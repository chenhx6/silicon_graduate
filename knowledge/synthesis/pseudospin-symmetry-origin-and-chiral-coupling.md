---
type: synthesis
title: "原子核赝自旋对称性微观相对论起源及其与手征/八极前沿耦合专题"
aliases: [赝自旋对称性专题, pseudospin-symmetry-and-chiral-coupling, 赝自旋微观机制]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
scope: relativistic-pseudospin-symmetry-and-exotic-band-couplings
confidence: high
sources: [ding-2012-phd-thesis-127-128i-high-spin, wang-shouyu-2020-mchid-review]
tags: [pseudospin, pss, relativistic-mean-field, chirality, octupole, pcq]
---

# 原子核赝自旋对称性微观相对论起源及其与手征/八极前沿耦合专题

## 1. 概念提出与微观相对论起源

### 1.1 经验现象的发现
在原子核单粒子能级谱中，实验学者很早便注意到一个奇特的近简并现象：某些具有不同主量子数 $n$ 与轨道角动量 $l$ 的单粒子轨道，在能量上表现出异乎寻常的接近。例如：
- $(2d_{5/2}, 1g_{7/2})$ 能级差极小；
- $(3s_{1/2}, 2d_{3/2})$ 能级差极小；
- $(2f_{7/2}, 1h_{9/2})$ 能级差极小。

1969 年，K. T. Hecht、A. Adler 以及 A. Arima 等人独立提出了\term{赝自旋对称性}（Pseudospin Symmetry, PSS）的唯象概念。他们定义一组“赝”量子数：
\begin{equation}
    \tilde{n} = n - 1, \quad \tilde{l} = l + 1, \quad \tilde{s} = 1/2
\end{equation}
此时，这一对物理轨道恰好对应于同一个赝轨道角动量 $\tilde{l}$ 与赝自旋 $\tilde{s} = 1/2$ 相加所构成的赝自旋双重态（Pseudospin Doublet）：
\begin{equation}
    \tilde{j} = \tilde{l} \pm 1/2
\end{equation}
以 $(2d_{5/2}, 1g_{7/2})$ 为例，其对应的赝轨道为 $\tilde{l} = 3$（赝 $f$ 态，$\tilde{f}$），两个轨道分别对应 $\tilde{j} = \tilde{f}_{5/2}$ 与 $\tilde{f}_{7/2}$。两能级之间微小的能隙，被解释为微弱的“赝自旋-轨道耦合分裂”（Pseudo Spin-Orbit Splitting）。

### 1.2 相对论 Dirac 理论对 PSS 物理本质的解答
在长达近三十年的时间里，赝自旋对称性被普遍视为一种纯粹巧合的经验参数化。直到 1997 年，J. N. Ginocchio 以及孟杰（Meng et al., 1998, 1999）等人通过相对论性 Dirac 方程，才彻底揭示了\textbf{赝自旋对称性是原子核微观相对论动力学的内在严格对称性}。

核子在相对论平均场中服从 Dirac 方程：
\begin{equation}
    \left[ \vec{\alpha} \cdot \vec{p} + \beta(M + S(\vec{r})) + V(\vec{r}) \right] \psi = \epsilon \psi
    \label{eq:dirac_equation}
\end{equation}
其中 $S(\vec{r})$ 为深达 $-400\text{ MeV}$ 的巨标量吸引势，$V(\vec{r})$ 为高达 $+350\text{ MeV}$ 的巨矢量排斥势。

定义两势之和为绑定弱束缚势 $\Sigma(\vec{r}) = V(\vec{r}) + S(\vec{r}) \approx -50\text{ MeV}$。将 Dirac 旋量展开为大分量 $F(r)$ 与小分量 $G(r)$，小分量满足的薛定谔型二阶微分方程为：
\begin{equation}
    \left[ -\frac{d^2}{dr^2} + \frac{\tilde{l}(\tilde{l}+1)}{r^2} + 2M(\epsilon - M - \Sigma) + \frac{1}{\epsilon + M - \Delta} \frac{d\Delta}{dr} \left( \frac{d}{dr} + \frac{\kappa}{r} \right) \right] G(r) = 0
    \label{eq:lower_component_dirac}
\end{equation}
其中 $\Delta(\vec{r}) = V(\vec{r}) - S(\vec{r}) \approx 750\text{ MeV}$ 为极深排斥差势。

**Ginocchio 与孟杰的里程碑结论**：
当巨势阱满足以下相对论条件时：
\begin{equation}
    \frac{d(V + S)}{dr} = \frac{d\Sigma}{dr} \approx 0 \quad \text{或} \quad \Sigma(\vec{r}) = V(\vec{r}) + S(\vec{r}) \to 0
\end{equation}
方程~(\ref{eq:lower_component_dirac})中破坏赝自旋对易不变性的赝自旋-轨道耦合势完全消失！**Dirac 旋量的小分量 $G(r)$ 在严格相对论意义下具备精确的 $SU(2)$ 赝自旋守恒对称性**。原子核微观中观察到的微弱能隙分裂，正是真实核介质中表面附近 $d\Sigma/dr$ 有限小梯度引起的轻度破缺。

---

## 2. 变形场中的赝自旋对称性与 Nilsson 渐近量子数映射

在四极形变平均场中，单粒子轨道由渐近量子数 $[N n_z \Lambda]\Omega$ 描述。经表象变换，一对赝自旋伙伴态在渐近基底下的量子数具有确定的一一映射法则：
\begin{equation}
    [N, n_z, \Lambda] \Omega = \Lambda + 1/2 \quad \longleftrightarrow \quad [N, n_z, \Lambda+2] \Omega' = (\Lambda+2) - 1/2
\end{equation}
定义\term{赝渐近量子数}：
\begin{equation}
    [\tilde{N} = N-1, \, \tilde{n}_z = n_z, \, \tilde{\Lambda} = \Lambda+1] \tilde{\Omega} = \Omega
\end{equation}
在形变场中，虽然轴对称长椭形变导致单粒子轨道产生强烈能量倾斜，但这一对赝自旋伙伴轨道的能量随 $\beta_2$ 与三轴角 $\gamma$ 的变化斜率完全平行！这使得赝自旋简并度在中高自旋转动态下依然表现出极高的鲁棒性（Robustness）。

---

## 3. 赝自旋与手征转动/八极关联的前沿耦合

### 3.1 赝自旋-手征多重带（PCQ）与三重态能谱（王守宇 2020 CPC 综述）
在 $A \approx 100$ 与 $A \approx 130$ 质量区的奇 $A$ 核与奇奇核中，当中子费米面跨越赝自旋伙伴态（如 $^{105}\text{Ag}$ 中的 $\pi g_{9/2}^{-1} \otimes \nu h_{11/2}(d_{5/2}/g_{7/2})$ 构型）时，微观投影粒子-转子模型（MPRM）预测并证实了多能带相干耦合：
1. **近简并三重带（Triplet Bands）**：最低能带与第二带构成严格的\term{赝自旋双重带}；而第二带与第三带则由于角动量非平面进动构成了典型的\term{手征双重带}；
2. **电磁选择定则**：赝自旋带伙伴之间受 $\Delta\tilde{s} = 1$ 选择定则主导，主要通过特定的单粒子磁偶极跃迁解耦；而手征伙伴带之间则保持经典的 $\Delta I = 1$ $M1+E2$ 强混合跃迁；
3. **四重带预言（PCQ）**：在三轴度更充分的奇 A 铈（$^{131,133}\text{Ce}$）高自旋端，赝自旋与手征三脚架的正交对称性将完全相乘，在同一核内激发出具有完全相同宇称的两对手征双重带（共 4 条平行能带）。

### 3.2 赝自旋对称性破缺对反射不对称八极形变的影响
微观研究指出，八极相干跃迁矩阵元 $\langle j || r^3 Y_3 || j' \rangle$ 对参与核子波函数的自旋-轨道重叠极其敏感。当赝自旋对称性较好时，两对伙伴轨道对单极电偶极矩的贡献相互干涉；而当自旋-轨道耦合导致 PSS 明显破缺时，单向八极矩阵元显著增强，直接催化了交替宇称带与内禀偶极矩 $|D_0|$ 的形成。

这一专题不仅彻底澄清了“假自旋”历史口语的学术不规范性，将其统一归一为具有严谨相对论基石的“赝自旋”，更为博士学位论文深入探讨微观对称性交织提供了前沿理论制高点。
