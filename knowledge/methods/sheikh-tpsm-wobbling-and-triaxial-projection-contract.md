---
type: method
title: "Sheikh 等：三轴投影壳模型（TPSM）摆动激发、3D 角动量投影与短轴量子化合同"
aliases: [Sheikh TPSM wobbling, TPSM wobbling contract, 3D angular momentum projection, short-axis quantization, TSD and ND wobbling systematics]
method_type: "triaxial-projected-shell-model-wobbling-contract"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Chirality and Wobbling in Atomic Nuclei Ch.12, PDF pp.256-274, full chapter reading"
confidence: "high for formalisms, calculated curves, and reported data; conditional for model parameter choices"
tags: [wobbling, transverse-wobbling, longitudinal-wobbling, tpsm, 3d-projection, hill-wheeler, short-axis-quantization, tsd-nuclei, normal-deformation]
sources: [book-petrache-chirality-and-wobbling]
---

# Sheikh 等：三轴投影壳模型（TPSM）摆动激发、3D 角动量投影与短轴量子化合同

## Purpose

本方法合同基于 J. A. Sheikh、S. Jehangir、G.-H. Bhat 在专著《Chirality and Wobbling in Atomic Nuclei》第 12 章的系统阐述，
解决低能核结构中摆动运动（Wobbling motion）与手征运动微观多体计算的核心难题：
通过三维严格角动量投影技术，从非轴对称形变 Nilsson+BCS 多准粒子基底中恢复实验室坐标系下的严格转动对称性，
在无需半经典推转（Cranking）近似与轴对称假定的条件下，统一描述实验室系中角动量完全守恒的离散能级谱、
波函数 \(K\) 组态混合以及绝对电磁跃迁几率，并在以下关键课题中确立微观分析合同：

1. **TPSM 理论三阶段流图与 Hill–Wheeler 广义本征方程**：三维角动量投影算符 \(\hat P^I_{MK}\) 的显式构造、配对加四极（P+Q）微观哈密顿量对角化，以及严格非正交基底上的电磁跃迁算符积分；
2. **短轴量子化与横向摆动几何的微观直视（图 12.10）**：通过三轴参数空间坐标系旋转（\(\gamma \to -120^\circ - \gamma\)），将量子化主轴从传统长轴转至短轴（\(s\) 轴），在微观波函数层面直观揭示 yrast 态（\(K=11/2\) 锁定于短轴）向一激发摆动带（\(K=7/2\) 偏离短轴）的转动轴倾斜进动物理本质；
3. **三轴超强形变（TSD）核横向摆动系统学（\(^{161,163,165,167}\mathrm{Lu}, {}^{167}\mathrm{Ta}\)）**：全面再现摆动能随自旋下降趋势、对齐角动量 \(i_x\) 与动态惯量 \(\mathcal{J}^{(2)}\) 的全同性，以及简谐摆动多声子特征选择定则（\(B(E2; n_\omega=2 \to 1) \approx 2 \times B(E2; n_\omega=1 \to 0)\)，而跨声子直跃被强烈压制）；
4. **正常形变（ND）10 核跨质量区普适演化（图 12.11–12.14）**：
   - TW 核：\(^{131}\mathrm{Cs}, {}^{135}\mathrm{Pr}, {}^{151}\mathrm{Eu}, {}^{183}\mathrm{Au}\)（负宇称）、\(^{133}\mathrm{Ba}, {}^{105}\mathrm{Pd}\)；
   - LW 核：\(^{133}\mathrm{La}, {}^{187}\mathrm{Au}\)（负宇称）、\(^{127}\mathrm{Xe}\)；
   - 拐点转变核：\(^{183}\mathrm{Au}\)（正宇称）；
5. **摆动带与单粒子旋称伙伴带（SP）的微观统一判据**：阐明在同一 TPSM 哈密顿量下，摆动带（核芯集体转动轴倾斜，强集体 \(E2\) 主导）与旋称伙伴带（价核子角动量倾斜，强 \(M1\) 主导）的内禀几何与跃迁指纹差异。

## Inputs and Assumptions

### Three-stage TPSM framework

三轴投影壳模型计算包含三个严格阶段：

1. **形变基底构造**：求解具有真实轴对称形变 \(\epsilon\)（或 \(\beta\)）与非轴对称形变 \(\epsilon'\)（或 \(\gamma\)）的三轴 Nilsson 势，随后执行标准 BCS 配对过程；
2. **三维角动量投影（3D Projection）**：
   利用三维投影算符从三轴多准粒子基底中抽取好角动量 \(I\) 和好 \(K\) 的量子基矢：
   \[
   \hat P^I_{MK} = \frac{2I+1}{8\pi^2} \int d\Omega D^{I*}_{MK}(\Omega) \hat R(\Omega) , \quad
   \hat R(\Omega) = e^{-i\alpha \hat J_z} e^{-i\beta \hat J_y} e^{-i\gamma \hat J_z} ;
   \]
   针对奇 \(A\) 核，构建由 1 准粒子、3 准粒子（如 1 质子 + 2 中子，或 3 质子）、5 准粒子张成的非正交多粒子空间；
3. **配对加四极（P+Q）哈密顿量对角化**：
   微观哈密顿量包含球形单粒子能量、自洽自旋四极力、单极配对和四极配对：
   \[
   \hat H = \hat H_0 - \frac{1}{2}\chi \sum_\mu \hat Q_{2\mu}^\dagger \hat Q_{2\mu} - G_M \hat P^\dagger \hat P - G_Q \sum_\mu \hat P_{2\mu}^\dagger \hat P_{2\mu} .
   \]

在非正交投影基底上求解 Hill–Wheeler 广义本征方程：

\[
\sum_{\kappa' K'} \left( H^I_{\kappa K, \kappa' K'} - E_\sigma^I N^I_{\kappa K, \kappa' K'} \right) f^\sigma_{I, \kappa' K'} = 0 ,
\]

其中哈密顿核与重叠核为：

\[
H^I_{\kappa K, \kappa' K'} = \langle \Phi_\kappa  \vert \hat H \hat P^I_{K K'}  \vert \Phi_{\kappa'} \rangle , \quad
N^I_{\kappa K, \kappa' K'} = \langle \Phi_\kappa  \vert \hat P^I_{K K'}  \vert \Phi_{\kappa'} \rangle .
\]

波函数由变分展开系数 \(f^\sigma_{I, \kappa K}\) 决定，直接用于计算跃迁算符在欧拉角积分下的严格折合跃迁几率 \(B(EL)\) 与 \(B(ML)\)。

## What It Can Establish

### 1. 短轴量子化（Short-Axis Quantization）与横向摆动微观图像（图 12.10）

传统 TPSM 计算通常采用长轴（\(l\) 轴）作为量子化主轴。然而在横向摆动（TW）动力学中，奇准粒子角动量主要沿短轴（\(s\) 轴）取向。
Sheikh 等人通过等效坐标扇区变换（\(\gamma \to -120^\circ - \gamma\)），将量子化主轴旋转至短轴：

- 物理可观测量（能级谱与跃迁几率）在坐标变换下保持完全不变；
- 投影 \(K\) 组态能谱直观显示：\(^{163}\mathrm{Lu}\) 的 yrast 双带（TSD1 与 TSD2）基底完全由 \(K=11/2\) 占据主导，严格证明奇质子角动量紧密锁定于短轴（\(s\) 轴）；
- 激发摆动带 TSD3 与 TSD4 的主要成分跃迁为 \(K=7/2\)，直接证明了集体转动轴从短轴发生离轴进动的物理图景。

### 2. TSD 质量区（A≈160）横向摆动的严格简谐性检验（图 12.1–12.9）

在 \(^{161,163,165,167}\mathrm{Lu}\) 与 \(^{167}\mathrm{Ta}\) 中，TPSM 给出高度自洽的理论再现：

- **摆动能量随自旋下降**：\(E_{\rm wob}(I) = E(n_\omega=1, I) - \frac{1}{2}[E(n_\omega=0, I+1) + E(n_\omega=0, I-1)]\) 随自旋升高呈现特征性下降；
- **对齐量与转动惯量全同性**：TSD1 与 TSD2 的对齐角动量 \(i_x\) 和动态惯量 \(\mathcal{J}^{(2)}\) 完全重合，证实两者共享相同的内禀单粒子基底；
- **简谐多声子跃迁选择定则**：
  - 跨带连接跃迁强度 \(B(E2; TSD3 \to TSD2)\) 约为 \(B(E2; TSD2 \to TSD1)\) 的 **2 倍**；
  - 跨两声子的直跃 \(B(E2; TSD4 \to TSD1)\) 与 \(B(E2; TSD3 \to TSD1)\) 受到强烈压制（近似禁戒）；
  - 理论计算与 \(^{163}\mathrm{Lu}\) 实验测得的跨带强化比 \(B(E2)_{\rm out}/B(E2)_{\rm in}\) 和微小 \(B(M1)_{\rm out}/B(E2)_{\rm in}\) 高度符合。

### 3. 正常形变（ND）10 核系统的 TW 与 LW 分类（图 12.11–12.14）

TPSM 将分析推广至正常形变核，成功解释了跨质量区的 10 个代表性摆动候选带：

1. **横向摆动（TW）**：\(^{131}\mathrm{Cs}, {}^{135}\mathrm{Pr}, {}^{151}\mathrm{Eu}, {}^{183}\mathrm{Au}\)（负宇称）、\(^{133}\mathrm{Ba}, {}^{105}\mathrm{Pd}\) 展现出频率随自旋下降；
2. **纵向摆动（LW）**：\(^{133}\mathrm{La}, {}^{187}\mathrm{Au}\)（负宇称）、\(^{127}\mathrm{Xe}\) 表现出频率随自旋单调升高；
3. **拐点与失稳相变**：\(^{183}\mathrm{Au}\)（正宇称）频率呈现先增后减的特征拐点，预言负宇称带在 \(I > 33/2\hbar\) 处频率将拐弯上升；
4. **电磁指纹一致性**：所有 10 个核实测与理论跨带 \(B(E2)_{\rm out}/B(E2)_{\rm in}\) 均达到与带内相近的量级，而 \(B(M1)\) 相对比值极小，支持了摆动运动的电磁集体性假说。

### 4. 摆动带与单粒子旋称伙伴带（SP）的微观解耦

传统推转模型往往难以自然区分旋称伙伴带与摆动带。TPSM 证明两者具有完全不同的几何拓扑：

- **单粒子旋称伙伴带（SP）**：转动轴仍在主轴旋转，奇准粒子角动量矢量发生局部倾斜，跃迁以强磁偶极 \(B(M1)\) 为特征；
- **摆动激发带（Wobbling）**：核芯集体电荷转动轴发生立体倾斜进动，跃迁以强集体四极 \(B(E2)\) 为主导；
- TPSM 能够在同一个模型空间与相互作用下自然共存并清晰区分这两种机制。

## Experimental and Spectroscopic Analysis Contract

在采用 TPSM 分析在束 \(\gamma\) 谱学实验中的摆动候选带时，必须遵循以下合同：

1. **参数设定透明度**：必须明确列出三轴 Nilsson 势形变参数 \((\epsilon, \epsilon')\)（或 \(\beta, \gamma\)）以及配对强度 \(G_M, G_Q\)，禁止利用未标明的参数调整来强行配合实验能级；
2. **区分主轴取向与 K 组态标记**：报告投影基底 \(K\) 分量时，必须声明量子化轴是传统的长轴还是变换后的短轴；
3. **多观测量联立检验**：
   - 确立横向摆动必须同时具备：(i) \(\hbar\omega_w\) 随自旋下降；(ii) 跨带跃迁 \(B(E2)_{\rm out}/B(E2)_{\rm in} \sim 0.2\)–\(1.0\)；(iii) 极小 \(B(M1)_{\rm out}/B(E2)_{\rm in}\)；(iv) 伙伴带具有完全重合的对齐量 \(i_x\)；
   - 实验上若仅发现能级差下降而缺乏强集体 \(E2\) 跨带，不能排他排除组态交叉或转动惯量变化；
4. **多声子简谐判据**：对于多声子摆动候选，必须验证两声子带向单声子带的 \(B(E2)\) 强化（理论接近 2 倍）以及跨两声子向基态带的直跃抑制比（\(B(E2; 2\to 0)/B(E2; 2\to 1) \ll 0.1\)）。

## What It Cannot Establish Alone

- TPSM 使用配对加四极（P+Q）的可分离两体相互作用，未显式包含高阶多极或自洽相对论单极力；
- 相互作用强度 \(\chi\) 与形变 \(\epsilon\) 通过自洽 HFB 关系绑定，不能自由变化，但基底形变仍需作为输入输入；
- 尽管 TPSM 计算的 \(B(E2)\) 与能谱与 \(^{135}\mathrm{Pr}\) 早期大混合比数据吻合，但它无法直接解决后续高统计量实验（如 Lv et al.）测得小混合比 \(|\delta| < 1\) 所引发的实验争议，争议裁决仍依赖多实验组独立高精度符合谱学；
- 偶偶核中 \(\gamma\) 刚性带（奇自旋分支反常偏低）与两准粒子摆动的深层边界仍需全微观多体与形变自由度结合检验。

## Knowledge Impact and Learning Decision

Sheikh 等人的第 12 章确立了当前核微观理论中三维投影壳模型（TPSM）处理非轴对称高自旋物理的权威标杆：
它将角动量完全守恒的量子化多体对角化与直观的短轴几何旋转结合起来，
在同一理论基底下完美涵盖了超强形变 Lu/Ta 链与中重核 ND 10 核链的横向/纵向摆动，
为 Wiki 建立了统一对比 PRM、CDFT、TAC 与投影壳模型的最高层微观谱学桥梁。

本单元完成第 12 章全文、公式推导、表 12.1 及图 12.1–12.14 的全面精读与核验。

## Evidence and Locators

- Ch.12 pp.237–239 / physical PDF pp.256–258：三轴形变背景、手征与摆动模式物理概念、Bohr–Mottelson 谐振子量子数 \(n_\omega\)；
- Ch.12 pp.239–241 / physical PDF pp.258–260：摆动模式分类（TW 与 LW）、实验历史与争议核素汇总；
- Ch.12 pp.241–243 / physical PDF pp.260–262：TPSM 理论框架、3D 投影算符式 (12.8)–(12.9)、多准粒子基底式 (12.10)–(12.11)、P+Q 哈密顿量式 (12.12)–(12.14)、Hill–Wheeler 广义本征方程式 (12.15)–(12.16)、电磁矩阵元式 (12.17) 与表 12.1（15 核模型形变参数）；
- Ch.12 pp.243–248 / physical PDF pp.262–267：TSD Lu 与 Ta 核计算能谱（图 12.1–12.5）、摆动频率随自旋下降式 (12.18)（图 12.6）、对齐量与动态惯量（图 12.7）、在带与跨带 \(B(E2)\)（图 12.8）；
- Ch.12 pp.248–250 / physical PDF pp.267–269：跨带跃迁比率（图 12.9）、短轴量子化与 \(K\) 组态直视（图 12.10）；
- Ch.12 pp.250–253 / physical PDF pp.269–272：正常形变 10 核能级谱与 TW/LW 频率对比（图 12.11）、转动频率（图 12.12）、对齐量（图 12.13）、\(B(E2)_{\rm out}/B(E2)_{\rm in}\) 与 \(B(M1)_{\rm out}/B(E2)_{\rm in}\)（图 12.14）；
- Ch.12 pp.253–255 / physical PDF pp.272–274：总结与前沿展望；
- 已渲染核对 PDF pp.261、264、267、268、269、271。

## Sources

- [[book-petrache-chirality-and-wobbling]]
- [[chen-cdft-prm-wobbling-and-fermi-surface-contract]]
- [[petrache-ch2-frauendorf-topological-wobbling-contract]]
- [[lawrie-tip-wobbling-discrimination]]
- [[odd-a-wobbling-mode-stability-and-bifurcation]]
- [[multiphonon-wobbling-and-anharmonicity-dynamics]]
- [[shimizu-shell-model-mcsm-qvsm-computational-contract]]
