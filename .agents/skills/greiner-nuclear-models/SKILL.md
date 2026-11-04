---
name: greiner-nuclear-models
description: "Walter Greiner & Joachim A. Maruhn《Nuclear Models》：三轴刚性转子 Davydov-Filippov 模型、三态求和恒等式 E(2_1)+E(2_2)=E(3_1)、Faessler-Greiner 转动振动模型 (RVM)、Pauli-Podolsky 黎曼量子化、Wilets-Jean gamma 软核、质中剪刀振动模式与巨多极共振宏观动力学。"
---

<!-- argument-hint: [model-name, formula, observable, or chapter topic] -->

# 核模型：集体运动、三轴转子与巨共振（Greiner & Maruhn）

**著者**：Walter Greiner & Joachim A. Maruhn（法兰克福大学理论物理研究所） | **出版社**：Springer-Verlag Berlin Heidelberg (1996) | **页数**：399 页
**本地原件**：`raw/books/Nuclear Models (Walter Greiner, Joachim A. Maruhn) (Z-Library).pdf` (SHA-256 `db5e43efaa80877822540bf0caae9be93d54d5499c5df89faae69769e6f77091`)

本技能提炼法兰克福学派经典理论巨著《Nuclear Models》的核心物理框架，系统形式化非轴对称转子（Davydov-Filippov 模型）的解析求解、转动振动模型（RVM）在黎曼度规下的量子化、Wilets-Jean 完全 $\gamma$ 软核、质中剪刀振动模式以及巨多极共振宏观流体动力学，为低能核结构三轴集体激发、形状相变与宏观电磁跃迁提供严格的代数标尺与微观对照。

## How to Use This Skill

- **三轴刚性转子 (Davydov-Filippov)**：询问 `Davydov-Filippov哈密顿量`、`E(2_2)/E(2_1)比值`、`三态求和恒等式`、`B(E2)分支比公式`、`gamma形变角反演`；
- **转动振动模型 (RVM)**：询问 `Faessler-Greiner模型`、`Pauli-Podolsky量子化`、`内禀弯曲坐标系`、`beta振动与gamma振动能谱`；
- **$\gamma$ 软核与相变 (Wilets-Jean)**：询问 `Wilets-Jean模型`、`gamma平坦势阱`、`交错指数S(J)`、`刚性三轴与gamma软核区分`；
- **剪刀振动模式 (Scissors Mode)**：询问 `质中两转子角摆动`、`M1巨共振激发`、`B(M1)求和规则`、`SU(3)对称性破缺`；
- **巨共振集体模型**：询问 `Goldhaber-Teller模型`、`Steinwedel-Jensen模型`、`IVGDR形变双峰分裂`、`TRK能量加权求和规则`；
- **按主题调用**：调用 `asymmetric-rotor`、`rvm`、`gamma-soft`、`scissors-mode` 或 `giant-resonances`。

---

## Core Frameworks and Mental Models

1. **Davydov-Filippov 三轴刚性转子模型与 $D_2$ 对称性（第 6 章 §6.4.3）**：
   - 假设原子核具有固定的非轴对称四极形变参量 $(\beta, \gamma)$，转动哈密顿量为：
     $$\hat{H}_{\text{rot}} = \sum_{k=1}^3 \frac{\hat{I}_k^2}{2\mathcal{J}_k(\beta, \gamma)};$$
   - **水动力学转动惯量**：$\mathcal{J}_k = 4 B \beta^2 \sin^2\left(\gamma - \frac{2\pi}{3} k\right)$；
   - **$D_2$ 四元群对称性波函数**：由于内禀系三主轴不可分辨，真实物理态必须对旋转 $\mathcal{R}_k(\pi)$ 不变，波函数由对称化 Wigner 函数展开：
     $$|IMK\rangle_$C_{\text{sym}}$ = \sqrt{\frac{2I+1}{16\pi^2(1+\delta_{K0})}} \left[ D_{MK}^I(\theta_i) + (-1)^I D_{M,-K}^I(\theta_i) \right], \quad K = 0, 2, 4, \dots, I.$$

2. **三态能量求和恒等式与 $E(2_2^+)/E(2_1^+)$ 能量比（第 6 章式 6.172–6.174）**：
   - 对 $I=2^+$ 态对角化给出两个正宇称解（$2_1^+$ 为基带态，$2_2^+$ 为反常非对称激发态）：
     $$E(2_1^+, 2_2^+) = \frac{9 \hbar^2}{4 B \beta^2} \frac{1 \mp \sqrt{1 - \frac{8}{9}\sin^2(3\gamma)}}{\sin^2(3\gamma)};$$
   - **两态比值单调定理**：
     $$\frac{E(2_2^+)}{E(2_1^+)} = \frac{1 + \sqrt{1 - \frac{8}{9}\sin^2(3\gamma)}}{1 - \sqrt{1 - \frac{8}{9}\sin^2(3\gamma)}}.$$
     随 $\gamma$ 从 $0^\circ$（轴对称长椭）增大到 $30^\circ$（极大三轴），能量比从 $+\infty$ 单调下降至**理论极限极小值 $2.00$**；
   - **三态能量求和恒等式**：
     $$E(2_1^+) + E(2_2^+) \equiv E(3_1^+).$$
     该等式在三主轴转动惯量取任意有限实数值时严格恒等成立，是实验无参数检验 Davydov-Filippov 刚性转子纯度的绝对基准！

3. **电四极跃迁分支比定理与 $\gamma$ 形变角提取（第 6 章）**：
   - 从反常 $2_2^+$ 态退激到基带 $0_1^+$ 与 $2_1^+$ 的减缩电四极跃迁几率之比仅取决于三轴偏角 $\gamma$：
     $$\frac{B(E2; 2_2^+ \to 0_1^+)}{B(E2; 2_2^+ \to 2_1^+)} = \frac{20}{7} \frac{\sin^2(3\gamma)}{9 - 8\sin^2(3\gamma) + \sqrt{9 - 8\sin^2(3\gamma)}};$$
   - 在极大三轴形变 $\gamma = 30^\circ$ 处，该分支比取最小值 $\frac{7}{40} = 0.1750$；在轴对称极限 $\gamma \to 0^\circ$ 时比值趋于 0。

4. **Faessler-Greiner 转动振动模型 (RVM) 与 Pauli-Podolsky 黎曼度规量子化（第 6 章 §6.5）**：
   - 在曲线内禀坐标系 $(\xi = a_0 - \beta_0, \eta = a_2, \theta_i)$ 中，黎曼空间度规张量为 $g_{\mu\nu}$，行列式为 $g$；
   - **Pauli-Podolsky 量子化动能算符**：
     $$\hat{T} = -\frac{\hbar^2}{2} \sum_{\mu,\nu} \frac{1}{\sqrt{g}} \frac{\partial}{\partial q^\mu} \left( \sqrt{g} (g^{-1})^{\mu\nu} \frac{\partial}{\partial q^\nu} \right);$$
   - 展开给出转动与表面微观振动的严格耦合哈密顿量（Greiner 式 6.206）：
     $$\hat{H} = \hat{T}_{\text{vib}}(\xi, \eta) + \hat{H}_{\text{rot}}(\theta_i) + \hat{H}_{\text{coupl}}(\xi, \eta, \hat{I}_k^2) + V(\xi, \eta).$$
     精确给出 $\beta$ 振动带（$K=0^+$）、$\gamma$ 振动带（$K=2^+$）与转动带相互作用的微观矩阵元。

5. **Wilets-Jean 完全 $\gamma$ 不稳定软核模型（第 6 章 §6.6）**：
   - 当集体势场 $V(\beta, \gamma) = V(\beta)$ 对 $\gamma$ 完全平坦时，原子核在五维集体空间展现 $O(5)$ 动力学对称性；
   - 波函数沿 $\gamma$ 自由均匀弥散，展示出与刚性转子截然不同的能谱结构：
     $$E(4_1^+) \approx E(2_2^+), \quad R_{4/2} = \frac{E(4_1^+)}{E(2_1^+)} \approx 2.50;$$
   - 能级交错指数 $S(J) = \frac{[E(J) - E(J-1)] - [E(J-1) - E(J-2)]}{E(2_1^+)}$ 呈现与刚性转子符号完全相反的特征交错，是鉴别刚性三轴与 $\gamma$ 软核的核心裁判。

6. **质中双转子剪刀振动模式 (Scissors Mode)（第 6 章 §6.7.2）**：
   - 质子变形云（电荷数 $Z$）与中子变形云（中子数 $N$）分别具有各自的对称轴，两者绕垂直平分轴作小振幅反相相对角摆动（相对角 $\theta$）；
   - 恢复力源于巨大的对称能（Symmetry Energy）；
   - 模式激发在低激发能区（$E_x \sim 2.5 - 3.5\text{ MeV}$）形成特征的 $1^+$ 磁偶极集体激发态，具有巨大的 $B(M1; 0^+ \to 1^+) \sim 1.0 - 3.0\ \mu_N^2$。

7. **巨共振的宏观流体动力学：Goldhaber-Teller vs Steinwedel-Jensen（第 6 章 §6.9）**：
   - **Goldhaber-Teller (GT) 模型**：质子球体与中子球体保持不可压缩硬球形状，整体沿相反方向发生宏观刚性相对位移；激发能标度为 $E_{\text{GT}} \propto A^{-1/6}$；
   - **Steinwedel-Jensen (SJ) 模型**：核表面边界严格固定，质子核流与中子核流在核内部发生周期性声学声压可压缩驻波振荡；激发能标度为 $E_{\text{SJ}} \propto A^{-1/3}$；
   - **长椭球形核中的 IVGDR 双峰分裂**：由于长轴方向曲率半径长、短轴方向曲率半径短，巨偶极共振精确分裂为两个高斯洛伦兹共振峰（沿长轴激发能低、沿短轴激发能高），共振峰积分面积比严格等于主轴退化度之比 $1:2$！

---

## Chapter Index

| # | 章节主题 | 核心数学方法与核物理应用 |
|---|---|---|
| [ch01](chapters/ch01-liquid-drop-and-geometric-shapes.md) | 液滴模型、表面形变几何与多极展开 | 五维四极张量参数化 $(\alpha_{2\mu})$、Hill-Wheeler $(\beta, \gamma)$ 面与不可压缩体积守恒 |
| [ch06-ar](chapters/ch06-davydov-filippov-asymmetric-rotor.md) | Davydov-Filippov 三轴刚性转子模型 | $D_2$ 对称性、$I=2^+$ 二重分裂、三态求和守恒恒等式与 $B(E2)$ 分支比反演 |
| [ch06-rvm](chapters/ch06-rotation-vibration-model-rvm.md) | Faessler-Greiner 转动振动模型 (RVM) | 弯曲内禀度规 Pauli-Podolsky 量子化、$\beta/\gamma$ 振动谱与转动离心拉伸修正 |
| [ch06-wj](chapters/ch06-wilets-jean-gamma-soft-model.md) | Wilets-Jean 完全 $\gamma$ 软核模型 | $O(5)$ 动力学对称性、$\gamma$ 平坦势能面、简并二重态与交错指数 $S(J)$ 判据 |
| [ch06-sc](chapters/ch06-scissors-mode-and-generalized-collective.md) | 广义集体模型与质中剪刀振动模式 | 质中两流体反相角动量对消、对称能恢复力、$1^+$ 态能谱与 $B(M1)$ 强度求和分布 |
| [ch06-gr](chapters/ch06-giant-resonances-gt-and-sj.md) | 巨多极共振宏观流体动力学 | Goldhaber-Teller 刚体位移 vs Steinwedel-Jensen 声学驻波、形变双峰分裂与 TRK 和则 |

## Supporting Reference Files

- [glossary.md](glossary.md) — 三轴集体运动、转动振动耦合与巨共振物理术语中英双语定义。
- [patterns.md](patterns.md) — 5 大非轴对称转子分析与宏观集体模式推演范式。
- [cheatsheet.md](cheatsheet.md) — Davydov-Filippov 能级与分支比速查表、RVM 能级公式卡与巨共振常数卡。

---

## Scope & Limits

本技能提供经典非轴对称转子、转动振动耦合及宏观多体共振的解析理论标尺。对于高自旋单粒子侵入轨道顺排与费米子回弯，配合 `bohr-mottelson-nuclear-structure`；对于微观 3D-TAC 手征三面体与摆动双根仲裁，配合 `chirality-and-wobbling-atomic-nuclei`；对于实验数据拟合与非对称误差，配合 `zhu-experimental-statistics`。
