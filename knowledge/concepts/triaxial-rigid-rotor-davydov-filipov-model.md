---
type: concept
title: "三轴刚性转子 Davydov-Filipov 模型解析解与跃迁比率推导"
aliases: [Davydov-Filipov模型, 三轴转子解析解, DF模型, 非对称转子能级推导]
created: 2026-11-01
updated: 2026-11-05
status: ai-draft
review_status: unreviewed
tags: [triaxiality, davydov-filipov-model, greiner-models, e2-branching-ratios, asymmetric-rotor]
---

# 三轴刚性转子 Davydov-Filipov 模型解析解与跃迁比率推导

## Definition

### 物理模型提出与学术价值

1958 年，苏联理论物理学家 A. S. Davydov 和 G. F. Filipov 在《Nuclear Physics》上发表了划时代的解析理论（Davydov-Filipov 模型，简称 DF 模型）。该模型在 Walter Greiner《Nuclear Models》（第 6 章）中得到了最为系统和优雅的数学展开。

DF 模型假定原子核在内禀系中具有**完全刚性的三轴椭球形变**，其形变参数 $(\beta, \gamma)$ 在旋转过程中保持固定。该模型是所有三轴转动动力学（包括摆动运动与粒子-转子耦合模型）的解析极限，也是通过实验低自旋能级比值直接提取原子核三轴非对称角 $\gamma$ 的标准标尺。

---

## Necessary Assumptions

### 汉密尔顿量与波函数基矢

### (1) 转动能量算符
设原子核三个主惯性轴为 $1, 2, 3$。根据水动力学转动惯量：
$$\mathcal{J}_k = 4 B \beta^2 \sin^2\left(\gamma - \frac{2\pi}{3} k\right) \quad (k = 1, 2, 3)$$
刚体转动汉密尔顿量表达为：
$$\hat{H} = \sum_{k=1}^3 \frac{\hat{I}_k^2}{2\mathcal{J}_k} = A_1 \hat{I}_1^2 + A_2 \hat{I}_2^2 + A_3 \hat{I}_3^2$$
其中旋转常数定义为 $A_k = \frac{\hbar^2}{2\mathcal{J}_k} = \frac{\hbar^2}{8 B \beta^2 \sin^2(\gamma - \frac{2\pi}{3} k)}$。

### (2) 空间定点转动群对称性（$D_2$ 对称性）
由于椭球表面在绕任何一个主轴旋转 $180^\circ$（即 $\mathcal{R}_k(\pi)$ 操作）下保持不变，系统的波函数必须属于四元群 $D_2$（Klein 四元群）的全对称不可约表示（$A$ 表示）。
自旋为 $I$ 的全对称态只能由具有偶数投影量子数 $K$ 的对称化 Wigner $D$ 矩阵构成：
|IMK\rangle = \sqrt{\frac{2I + 1}{16\pi^2(1 + \delta_{K,0})}} \left[ D_{MK}^I(\theta_i) + (-1)^I D_{M,-K}^I(\theta_i) \right] \quad (K = 0, 2, 4, \dots \le I)$$

---

## Discriminating Observables

### 特征谱学观测量

## Supporting Evidence

### $I=2^+$ 能级的严格矩阵对角化与能级公式

对于 $I=2$，基矢空间仅由两个正宇称正规化态张成：
$|2, 0\rangle \quad (K=0), \quad |2, 2\rangle \quad (K=2)$$

利用阶梯算符 $\hat{I}_\pm = \hat{I}_1 \mp i \hat{I}_2$，计算哈密顿量矩阵元：
$$H_{00} = \langle 2, 0 | \hat{H} | 2, 0 \rangle = 3 (A_1 + A_2)$$
$$H_{22} = \langle 2, 2 | \hat{H} | 2, 2 \rangle = A_1 + A_2 + 4 A_3$$
$$H_{02} = H_{20} = \langle 2, 0 | \hat{H} | 2, 2 \rangle = \sqrt{3} (A_1 - A_2)$$

代入 $A_k(\gamma)$ 的显式函数并对角化 $2\times 2$ 实对称矩阵，解出两个特征能量本征值：
$$E(2_1^+) = \frac{9 \hbar^2}{4 B \beta^2} \frac{1 - \sqrt{1 - \frac{8}{9}\sin^2(3\gamma)}}{\sin^2(3\gamma)}$$
$$E(2_2^+) = \frac{9 \hbar^2}{4 B \beta^2} \frac{1 + \sqrt{1 - \frac{8}{9}\sin^2(3\gamma)}}{\sin^2(3\gamma)}$$

### 能量比值定理（从能谱提取 $\gamma$ 核心公式）：
$$R_{22} \equiv \frac{E(2_2^+)}{E(2_1^+)} = \frac{1 + \sqrt{1 - \frac{8}{9}\sin^2(3\gamma)}}{1 - \sqrt{1 - \frac{8}{9}\sin^2(3\gamma)}}$$
- **当 $\gamma \to 0^\circ$（轴对称拉长）**：$\sin(3\gamma) \to 0$，分母为零，$E(2_2^+)/E(2_1^+) \to \infty$（非对称 $2_2^+$ 态被推向无穷远）；
- **当 $\gamma = 30^\circ$（最大三轴形变）**：$\sin(3\gamma) = 1$，$\sqrt{1 - 8/9} = 1/3$，代入得：
  $$\frac{E(2_2^+)}{E(2_1^+)} = \frac{1 + 1/3}{1 - 1/3} = 2.0$$
**条件反演**：该比值可在指定irrotational模型内给γ坐标；它不能独立确立静态γ或刚性。
130Ba的具体反例见[[ba129-core-and-pairing-validity]]：两2+能量与一个E2分支
可给看似合理的对应，但同一模型仍未描述3+候选及4_1能量。

---

## 4. 电四极跃迁几率与分支比定理

在 DF 模型中，内禀四极矩张量算符在内禀系中的非对角元引起强烈的跨带 $E2$ 跃迁。
从非对称态 $2_2^+$ 向基态 $0_1^+$ 与基带第一激发态 $2_1^+$ 的减缩电四极跃迁几率比值为：
令\(s=\sin^2(3\gamma),\,d=9-8s\)，在本页的irrotational惯量和集体E2合同下，
$$\frac{B(E2;2_2^+\to0_1^+)}{B(E2;2_2^+\to2_1^+)}
=\frac7{20}\frac{d-(3-2s)\sqrt d}{s}.$$
其γ→0极限为7/10，γ=30°时为0。旧的\((20/7)s/d\)式不满足这些极限，
已由独立D₂矩阵和CG张量核验替换；见[[ba129-core-and-pairing-validity]]。

同时，基带内部 $B(E2; 2_1^+ \to 0_1^+)$ 相对于轴对称刚体转子（$\gamma=0^\circ$）具有衰减因子：
$$B(E2; 2_1^+ \to 0_1^+) = \frac{1}{2} \left[ 1 + \frac{3 - 2\sin^2(3\gamma)}{\sqrt{9 - 8\sin^2(3\gamma)}} \right] \times B(E2)_{\text{axial}}$$

这套解析公式构成了三轴刚性模型（Rigid Triaxiality）与 $\gamma$ 软核（$\gamma$-soft Jean-Wilets 模型）竞争鉴别的第一道经典检验标尺。

## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。


## Sources

- [[book-greiner-nuclear-models]]：§6.4.3的能谱与基底；E2式按本任务明定算符独立推导。
- [[ba129-core-and-pairing-validity]]：公式、极限与128/130Ba输入核查。
- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
