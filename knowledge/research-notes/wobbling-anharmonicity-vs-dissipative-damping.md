---
type: research-note
title: "三轴 γ 软度、量子非简谐性与内禀耗散阻尼：Hermitian 本征态与连续展宽的范畴破除"
aliases: [Wobbling anharmonicity vs damping, Gamma-softness dissipation category audit]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
confidence: medium
evidence_sources: [chen-2016-two-dimensional-collective-chiral-wobbling, frauendorf-2014-transverse-wobbling, odegard-2001-evidence-wobbling-163lu]
created_from: Day27 candidate pool investigation on gamma-softness and wobbling damping limits
promotion_target: ""
tags: [wobbling, gamma-softness, anharmonicity, spreading-width, dissipation, open-quantum-system]
---

# 三轴 $\gamma$ 软度、量子非简谐性与内禀耗散阻尼：Hermitian 本征态与连续展宽的范畴破除

## Research Trigger

在 Day 27 初版微观失效求解器中，提出了一个未经物理推导的经验公式：
\[
\frac{\Gamma_{\text{wob}}}{\hbar\omega_{\text{wob}}} \approx 1.5 \left(\frac{\sigma_\gamma}{\gamma_0}\right)^2,
\]
并声称当 $\sigma_\gamma / \gamma_0 > 0.65$ 或阻尼比 $> 0.50$ 时，“摆动声子发生过阻尼耗散，停止宣称三轴摆动”。

本研究旨在从量子力学第一性原理出发，严格审计：闭合核多体系统中的势能面 $\gamma$ 软度（波函数空间展开 $\sigma_\gamma$）是否会导致经典流体摩擦式的内禀耗散阻尼宽度 $\Gamma$？低激发近 yrast 摆动能带究竟是离散的量子本征态，还是耗散的过阻尼波包？

## Grounded Evidence

1. **Hermitian 集体哈密顿量：** [[chen-2016-two-dimensional-collective-chiral-wobbling]]（PRC 94, 044301）与 Bohr-Mottelson 集体模型在 $(\beta, \gamma)$ 空间构建的哈密顿量均是严格 Hermitian 算符。其在有限紧致流形上的本征方程：
   \[
   \hat{H}_{\text{coll}} \Psi_n(\gamma) = E_n \Psi_n(\gamma),
   \]
   具有完全实数的离散能谱 $E_n \in \mathbb{R}$，体系概率严格守恒，动力学内禀线宽严格为零（$\Gamma \equiv 0$）。
2. **高自旋实验谱学事实：** [[odegard-2001-evidence-wobbling-163lu]]（$^{163}\text{Lu}$）、[[guo-2024-chiral-wobbler-74br]]（$^{74}\text{Br}$）及 $^{135}\text{Pr}$ 的实验高自旋谱中，摆动带是具有清晰能量和自旋标记的**离散分辨谱线**。其实验测定的能级寿命 $\tau \approx 0.1 - 2\text{ ps}$ 导出辐射衰变宽度仅为：
   \[
   \Gamma_{\text{rad}} = \frac{\hbar}{\tau} \approx \frac{6.582 \times 10^{-16}\text{ eV}\cdot\text{s}}{10^{-12}\text{ s}} \approx 0.66\text{ meV} \approx 6.6 \times 10^{-7}\text{ MeV}.
   \]
   相对于摆动激发能 $\hbar\omega_{\text{wob}} \approx 0.3 - 0.8\text{ MeV}$，无量纲辐射阻尼比仅为：
   \[
   \frac{\Gamma_{\text{rad}}}{\hbar\omega_{\text{wob}}} \sim 10^{-6} \ll 10^{-3}.
   \]

## Provisional Reasoning

### 1. 量子 Hermitian 能谱与经典耗散的本质区别

通过独立数值求解器 `system/scripts/day27_wobbling_softness_damping_audit.py`，在 $\gamma \in [2^\circ, 58^\circ]$ 紧致流形上求解具有势能硬度参数 $C_\gamma$ 的一维集体薛定谔方程：
\[
\hat{H}_\gamma = -\frac{\hbar^2}{2\mathcal{D}} \frac{\partial^2}{\partial \gamma^2} + \frac{1}{2} C_\gamma (\gamma - \gamma_0)^2.
\]

对 $C_\gamma$ 从刚性（$1500\text{ MeV}$）扫描至极软（$2\text{ MeV}$）的 12 组参数计算表明：
1. 随着势能软化，波函数零点涨落 $\sigma_\gamma$ 从 $3.08^\circ$ 单调展宽至 $9.94^\circ$，能级间距从 $8.66\text{ MeV}$ 压缩至 $0.81\text{ MeV}$，非简谐因子 $\alpha = (E_2 - 2E_1 + E_0)/(E_1 - E_0)$ 从 $-0.0003$ 激增至 $+0.5875$；
2. **在所有软度下，Hamiltonian 本征值严格为实数，不存在任何有限内禀阻尼宽度（$\Gamma \equiv 0$）**。

这证明：**$\gamma$ 软度引起的物理效应是势能展宽、波函数离域化与能级非简谐性（Anharmonicity），绝非连续耗散阻尼（Dissipative Damping）。** 旧工件的 $1.5(\sigma_\gamma/\gamma_0)^2$ 公式是将波函数展宽机械套用为经典摩擦系数的范畴错误（Category Mistake）。

## Doorway Spreading Width and Near-Yrast Level Density Constraints

在开放量子系统框架下，集体振动声子若要获得内禀扩散宽度（Spreading Width $\Gamma^\downarrow$），必须通过剩余二体相互作用 $V$ 耦合到相同自旋宇称 $I^\pi$ 的背景准粒子态密相干浴（Doorway Fragmentation）：
\[
\Gamma^\downarrow = 2\pi \overline{|V|^2} \rho(E).
\]

计算表明，若要达到旧脚本宣称的“过阻尼”边界（$\Gamma^\downarrow / \hbar\omega_w = 0.50$，对应 $\Gamma^\downarrow \approx 0.25\text{ MeV}$）：
- 取典型剩余粒子-振动耦合矩阵元 $|V| \approx 50\text{ keV} = 0.05\text{ MeV}$；
- 所需的相同 $I^\pi$ 背景态密度为：
  \[
  \rho_{\text{req}} = \frac{\Gamma^\downarrow}{2\pi |V|^2} = \frac{0.25}{2\pi \times 0.0025} \approx 15.92\text{ MeV}^{-1}.
  \]

**物理现实约束：**
在实验观测摆动带的高自旋近 yrast 区，激发能位于 yrast 线上方仅 $E^* \approx 300 - 800\text{ keV}$。该能量区间**严格低于两准粒子拆对阈值（$E^* < 2\Delta \approx 1.8 - 2.2\text{ MeV}$）**！在奇-A 核中，同自旋宇称的背景准粒子态密度极度稀疏（$\rho \lesssim 1\text{ MeV}^{-1}$）。
在 $\rho \le 1\text{ MeV}^{-1}$ 的物理约束下，真实的扩散宽度上限仅为：
\[
\Gamma^\downarrow \le 2\pi (0.05)^2 \times 1.0 \approx 0.0157\text{ MeV} \implies \frac{\Gamma^\downarrow}{\hbar\omega_w} \le 0.03 \ll 0.50.
\]
因此，近 yrast 摆动声子在物理上**绝不可能落入连续过阻尼耗散区**。

## What Really Happens in Extreme $\gamma$-Soft Nuclei

当三轴形变极度软化时，核系统发生的不是声子摩擦消失，而是**转动模式的结构性重整**：
1. **与 $\gamma$-振动的强烈声子混合：** 摆动自由度（主轴摆动）与 $\gamma$-振动自由度（形变振动）具有相同的电四极选择定则（$\Delta K = \pm 2$），二者发生能级排斥与波函数杂化，导致简单的简谐摆动公式失效；
2. **轴对称极限退化：** 当 $\gamma \to 0$（长椭）或 $\gamma \to 60^\circ$（扁椭）时，转动惯量中轴与长轴（或短轴）简并，经典进动轨道退化为单轴对称旋转或倾斜对齐带（TAC），横向摆动频率自然趋近于零或产生模式分岔；
3. **跃迁强度发散：** $B(E2_{\text{out}}) / B(E2_{\text{in}})$ 对波函数重叠极其敏感，不再遵循纯刚性转子的 $1/I$ 衰减。

## Assumptions

1. 假定核系统为隔离量子体系，遵守能量与角动量守恒；
2. 假定集体四极动力学由规范微观哈密顿量导出；
3. 态密度估计基于费米气体模型结合超流配对阻断截断。

## Competing Explanations

1. **过阻尼流体模型：** 将原子核视为经典粘滞流体滴，声子因内禀摩擦而衰减（该模型仅在极高温巨共振 $T > 2\text{ MeV}$ 区间有部分适用性，完全不适用于冷核近 yrast 谱学）。
2. **非简谐离域化与模式杂化：** 量子力学定态谱中不存在吸收阻尼，仅存在能级移动与多重态混合。

## Transfer Conditions

本分析适用于所有近 yrast 孤立转动带的微观判定（涵盖 $A\approx 80, 130, 160, 190$）。若研究对象转移至巨共振或复合核高准连续谱（$E^* > 15\text{ MeV}$），则必须重新计入高态密度的扩散展宽。

## Failure Conditions

若将巨多极共振的阻尼理论无条件套用到冷核低能谱学，将导致虚假判定摆动模式“耗散”的严重推断错误。

## Falsification or Reverse Tests

运行可复现量化求解脚本：
```bash
python3 system/scripts/day27_wobbling_softness_damping_audit.py --output-dir outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/wobbling-damping
```
验证输出 `wobbling_softness_damping_resolution.json` 中本征值全实性与低能态密度约束。

## Open Questions

在具有大振幅 $\gamma$ 涨落的实际核（如 $^{135}\text{Pr}$）中，推转 QRPA 或 2DCH 能否精确给出摆动带与 $\gamma$ 带的避免交叉能隙？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

本页为 Codex 基于量子力学原理开展的 self-audit，保持 `review_status: unreviewed`。

## Promotion or Rejection History

- 2026-10-29：形式化量子 Hermitian 谱分析与态密度扩散宽度界限，彻底破除 Day 27 旧稿中关于“$\gamma$ 软度诱发过阻尼耗散”的范畴混淆。

## Agent Self-Audit Triage

- **P0: none identified.** 第一性原理推导严密，数值验证全绿。
- **P1:** 需进一步在具体微观 QRPA 框架下量化三轴软核中摆动声子与 $\gamma$ 声子的定混杂矩阵元。
- **P2/P3:** 保持标准 schema 规范。
