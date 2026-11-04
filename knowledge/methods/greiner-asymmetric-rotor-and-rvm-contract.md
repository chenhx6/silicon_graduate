---
type: method
title: "Walter Greiner 非轴对称转子与转动振动模型（RVM）解析方法合同"
aliases: [Greiner-RVM-contract, Davydov-Filippov-Greiner-contract, 转动振动模型合同]
created: 2026-11-04
updated: 2026-11-04
status: active
review_status: unreviewed
method_type: collective-model-contract
tags: [greiner-maruhn, asymmetric-rotor, davydov-filippov, rotation-vibration-model, bohr-hamiltonian, triaxiality, sum-rules]
topics: [asymmetric-rotor, davydov-filippov, rvm, bohr-hamiltonian, sum-rules]
sources: [book-greiner-nuclear-models, book-bohr-mottelson-nuclear-structure-vol2, book-heyde-nuclear-physics-concepts]
---

# Walter Greiner 非轴对称转子与转动振动模型（RVM）解析方法合同

## Purpose

本方法合同严格绑定 Walter Greiner & Joachim A. Maruhn《Nuclear Models》（Springer 1996）第 6 章第 6.4.3 节与第 6.5 节（印刷 pp. 145–167 / 物理 PDF pp. 164–186），
系统形式化经典非轴对称转子（Davydov-Filippov 模型）的 $D_2$ 对称性本征态构建、本征能量解析解、三态能量求和规则 $E(2_1^+) + E(2_2^+) = E(3_1^+)$、电四极跃迁分支比定理，
以及 Faessler-Greiner 转动振动模型（Rotation-Vibration Model, RVM）在弯曲内禀坐标系 $(\xi, \eta, \theta_i)$ 下的 Pauli-Podolsky 黎曼动能算符量子化，
为原子核三轴集体运动在低自旋区的刚性转子与转动振动混合提供解析标尺。

## Inputs and Assumptions

1. **内禀表面形变参数化**：原子核四极形变表面由长度拉伸 $\beta$ 与非轴对称偏角 $\gamma$ 唯一确定：
   $$a_0 = \beta \cos\gamma, \quad a_2 = a_{-2} = \frac{1}{\sqrt{2}} \beta \sin\gamma$$
2. **水动力学或微观主轴转动惯量**：
   $$\mathcal{J}_k = 4 B \beta^2 \sin^2\left(\gamma - \frac{2\pi}{3} k\right) \quad (k = 1, 2, 3)$$
3. **$D_2$ 四元群对称基矢展开**：由于内禀系三主轴不可分辨，物理波函数必须在旋转变换 $\mathcal{R}_k(\pi)$ 下具有正宇称：
   $$\vert IMK\rangle_$C_{\text{sym}}$ = \sqrt{\frac{2I+1}{16\pi^2 (1+\delta_{K0})}} \left[ D_{MK}^I(\theta) + (-1)^I D_{M,-K}^I(\theta) \right]$$
4. **小振幅振动展开（RVM 模型）**：围绕轴对称长椭基态平衡形变 $(\beta_0, \gamma=0)$ 将坐标展开为 $\xi = a_0 - \beta_0$ 与 $\eta = a_2$，假定回复势能为简谐形式 $V(\xi, \eta) = \frac{1}{2} C_\beta \xi^2 + C_\gamma \eta^2$。

## What It Can Establish

1. **$I=2^+$ 能级的严格二重分裂与比值单调定理**：
   $$E(2_1^+, 2_2^+) = \frac{9 \hbar^2}{4 B \beta^2} \frac{1 \mp \sqrt{1 - \frac{8}{9}\sin^2(3\gamma)}}{\sin^2(3\gamma)}$$
   - 随 $\gamma$ 从 $0^\circ$ 增大到 $30^\circ$，能量比 $E(2_2^+)/E(2_1^+)$ 从 $+\infty$ 严格单调下降至极限值 $2.00$；
   - 在最大三轴形变 $\gamma = 30^\circ$ 处，$R_{4/2} = E(4_1^+)/E(2_1^+) = 2.67$；
2. **三态能量求和守恒定理（Greiner 式 6.174）**：
   $$E(2_1^+) + E(2_2^+) \equiv E(3_1^+)$$
   该关系在三主轴转动惯量取任意有限实数值时严格恒等成立，成为无需指定任何惯量模型即可在实验上检验 Davydov-Filippov 刚性转子纯度的无参数检验基准；
3. **内禀电四极跃迁分支比定理**：
   $$\frac{B(E2; 2_2^+ \to 0_1^+)}{B(E2; 2_2^+ \to 2_1^+)} = \frac{20}{7} \frac{\sin^2(3\gamma)}{9 - 8\sin^2(3\gamma) + (9 - 8\sin^2(3\gamma))^{1/2}}$$
   在 $\gamma = 30^\circ$ 处达到最小值 $0.1750$（$7/40$），直接裁决原子核三轴非对称度；
4. **Pauli-Podolsky 黎曼度规量子化动能算符（Greiner 式 6.206）**：
   $$\hat{T} = -\frac{\hbar^2}{2B} \left( \frac{\partial^2}{\partial \xi^2} + \frac{1}{2}\frac{\partial^2}{\partial \eta^2} + \frac{1}{2\eta} \frac{\partial}{\partial \eta} \right) + \sum_{k=1}^3 \frac{\hat{I}_k^2}{2\mathcal{J}_k(\xi, \eta)}$$
   严格给出了转动能量与 $\beta/\gamma$ 振动耦合的微观动能矩阵元。

## What It Cannot Establish Alone

1. **不能单凭 $E(2_2^+)/E(2_1^+)$ 区分刚性三轴与 $\gamma$ 不稳定软核**：Wilets-Jean 完全 $\gamma$ 软核模型在谐振子势下同样预言 $E(2_2^+)/E(2_1^+) \approx 2.0 - 2.5$，必须结合更高阶交错指数 $S(J) = [E(J) - E(J-1)] / (2J)$ 的交错相位与多声子分支比联合判定；
2. **纯水动力学转动惯量的系统性低估**：实验测量的转动带转动惯量通常介于水动力学无旋流与刚体转动之间，必须引入 BCS 配对淬灭因子；
3. **高自旋回弯与准粒子对齐失效**：本模型为纯集体玻色核芯模型，未引入费米子自由度，无法描述在 $I \ge 10 - 14\hbar$ 处发生的单核子 Coriolis 顺排（RAL）与回弯现象。

## Sources

- [[book-greiner-nuclear-models]]：Chapter 6, §6.4.3 & §6.5 (印刷 pp. 145–167 / 物理 PDF pp. 164–186).
- [[book-bohr-mottelson-nuclear-structure-vol2]]：Chapter 4 §4-2 & §4-5.
- [[book-heyde-nuclear-physics-concepts]]：Chapter 8 集体转动与振动.
- A. S. Davydov & G. F. Filippov, Nucl. Phys. 8, 237 (1958).
- A. Faessler & W. Greiner, Z. Phys. 168, 425 (1962).
- [[davydov-filippov-triaxial-rotor-and-wobbling-dynamics]]：Davydov-Filippov 转子动力学.
- [[davydov-rostovsky-triaxial-band-mixing]]：非绝热转动-振动 Mikhailov 展开.
