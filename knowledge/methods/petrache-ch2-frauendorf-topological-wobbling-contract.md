---
type: method
title: "Petrache Ch.2/Frauendorf：三轴转子拓扑摆动、TW–FM–LW 与实验边界"
aliases: [Frauendorf topological wobbling, TR separatrix classification, TW FM LW contract]
method_type: "topological-wobbling-and-ptr"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Petrache ed. Chirality and Wobbling in Atomic Nuclei Ch.2, PDF pp.43-80"
confidence: "high for selected equations/topology; conditional for experimental interpretation"
tags: [petrache, frauendorf, wobbling, flip-mode, transverse-wobbling, longitudinal-wobbling, ptr, qtr]
sources: [book-petrache-chirality-and-wobbling, book-bohr-mottelson-nuclear-structure-vol2]
---

# Petrache Ch.2/Frauendorf：三轴转子拓扑摆动、TW–FM–LW 与实验边界

## Purpose

把 Frauendorf 章节中三个容易混淆的层次分开：

1. 偶偶纯三轴转子的经典轨道拓扑；
2. 奇 A 粒子–三轴转子 PTR/QTR 的准粒子响应；
3. 实验上由能量、\(B(E2)\)、\(B(M1)\)、混合比和寿命共同约束的模式解释。

## Inputs and Assumptions

- 三轴转子哈密顿量
  \[
  H_{\mathrm{TR}}=\sum_i A_iJ_i^2,\qquad A_i=\frac{1}{2\mathcal J_i};
  \]
- 主轴命名为短轴 \(s\)、中轴 \(m\)、长轴 \(l\)，并满足
  \[
  \mathcal J_m>\mathcal J_s>\mathcal J_l;
  \]
- \(\kappa\) 按章节数字轴约定 \(A_2\le A_1\le A_3\) 定义：
  \[
  \kappa=\frac{2A_1-A_2-A_3}{A_2-A_3}.
  \]
  将它转换到 Wiki 的 \(A_m,A_s,A_l\) 命名时必须显式换轴；
- PTR/QTR 还需要单粒子势、组态、配对、转动惯量和 \(D_2\) 对称化基底；
- 经典 adiabatic energy 近似要求粒子内禀能量尺度足够大，使准粒子能跟随总
  角动量取向变化。

## What It Can Establish

### Pure triaxial rotor topology

在固定 \(I\) 下，角动量轨道由能量椭球与
\[
R^2=I(I+1)
\]
的交线决定。由 separatrix 分隔：

- separatrix 内侧：角动量围绕最大惯量 \(m\) 轴进动，可标记为 W-m；
- separatrix 外侧：角动量围绕最小惯量 \(l\) 轴进动，可标记为 W-l；
- separatrix 附近：轨道靠近不稳定的 \(s\) 轴，出现 flip mode；
- 低能最低态在足够高自旋下近似椭圆轨道，才接近 BM-II 的谐声子极限。

作者明确提出：wobbling 的名称可以按轨道拓扑使用，椭圆小振幅只是其中的谐特例；
Lawrie 将非椭圆倾斜进动全部另命名为 TiP，是另一套术语立场，不能伪装成唯一
实验定义。flip 与 wobbling 之间也没有普适的锐利边界。

### PTR/QTR and HFA

高 \(j\) 粒子–转子模型的简化高自旋接口为
\[
H_{\mathrm{HFA}}
=A_1(J_3-j)^2+A_2J_1^2+A_3J_2^2,
\]
\[
\bar A_1=A_1(1-j/I),
\qquad
\hbar\omega_w
=2I\sqrt{(A_2-\bar A_1)(A_3-\bar A_1)}.
\]

当粒子沿短轴、而总角动量进动轴与最大惯量中轴正交时，称为 TW；当粒子随
中轴方向的集体转动对齐时，HFA 对应 LW。沿长轴取向的高 \(j\) 空穴也可以产生
TW 型下降趋势。

HFA 临界角动量满足
\[
I_c=\frac{j\mathcal J_2}{\mathcal J_2-\mathcal J_1}
\]
（章节数字轴约定），此时 \(\omega_w=0\)，HFA 失效。这个点不是实验上必然
进入 TiP 的证明。

### Beyond HFA: TW–FM–LW

作者使用随粒子取向反应的经典绝热能量
\[
E_{\mathrm{ad}}(\theta,\phi)
=\min_{\vartheta,\varphi}
E_{\mathrm{class}}(\theta,\phi,\vartheta,\varphi)
\]
描述 HFA 失效后的连续演化：

1. 低自旋：总角动量绕短轴，TW；
2. 接近临界点：短轴极小失稳，出现两个倾斜极小，进入 flip mode；
3. 更高自旋：轨道围绕中轴，进入 LW 拓扑。

其诊断表是模型参考而不是自动分类器：

| 模式 | \(J\) 进动轴 | \(j\) 进动轴 | \(E_w(I)\) | 跨带 E2 |
| --- | --- | --- | --- | --- |
| TW | 短轴或长轴 | 短轴或长轴 | 通常下降，低 \(I\) 可有小幅上升 | order one |
| LW | 中轴 | 短轴、长轴或倾斜 | 通常上升 | order one |
| FM | 倾斜轴 | 倾斜轴 | 近似平坦 | order one |
| SP | 轴向单粒子伙伴 | 轴向单粒子伙伴 | 上升 | small |

### 135Pr and mixing-ratio controversy

第 2 章记录了 \(^{135}\mathrm{Pr}\) 的两条实验解释路线：

- 大 \(|\delta|\) 分支：支持较强跨带 E2、TW；
- 小 \(|\delta|\) 分支：支持较小跨带 E2，并把低自旋带重解释为 signature partner。

两者来自角分布拟合的不同 \(\chi^2\) 极小值选择。作者倾向 TW，但明确认为需要
新的实验确定 \(\delta\)。因此本 Wiki 必须保留全部可容许根、响应协方差和替代解释。

## What It Cannot Establish Alone

- \(E_w(I)\) 下降或上升不能单独确定 TW 或 LW；
- HFA 的 \(I_c\) 不能自动确认 TiP、flip mode 或 QTR 后续分支；
- 大跨带 E2、非零偏振或单个 \(\delta\) 根不能独立证明模式；
- \(B(E2)\) 比值、\(B(M1)\) 比值和能级趋势必须在共同组态、寿命、feeding 和
  实验响应合同下比较；
- \(\gamma\)-soft 核、TPSM、RPA、PTR/QTR 和 signature partner 可以在部分观测量
  上互相模拟。

## Evidence and Locators

- PDF pp.43–47 / printed pp.24–28：三轴转子、\(\kappa\)、D2、separatrix 和
  wobbling/flip 拓扑；
- PDF pp.50–55 / printed pp.31–36：PTR/QTR、HFA、式 (2.18)–(2.21)；
- PDF pp.56–58 / printed pp.37–39：\(^{135}\mathrm{Pr}\)、\(\delta\) 双根争议和
  \(B(E2)\) 竞争解释；
- PDF pp.61–66 / printed pp.42–47：PTR 经典绝热能量、TW–FM–LW 拓扑和分类表；
- PDF pp.75–80 / printed pp.56–61：RPA、TPSM 和 \(\gamma\)-soft 核边界。

## Sources

- [[book-petrache-chirality-and-wobbling]]
- [[book-bohr-mottelson-nuclear-structure-vol2]]
- [[wobbling-model-common-input-and-evidence-boundary]]
- [[wobbling-mixing-ratio-phase-and-transition-diagnostics]]
