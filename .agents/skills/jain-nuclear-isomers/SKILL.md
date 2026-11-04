---
name: jain-nuclear-isomers
description: "Ashok Kumar Jain 等《Nuclear Isomers: A Primer》：同核异能态四大物理机制（自旋陷阱、Seniority 异能态、K 异能态、形状异能态）、单 j 壳层 Seniority 代数半满壳 B(E2) 相消定理、K 禁戒跃迁折合阻碍度幂律 f_nu 与三轴形变诱导 K 混合指纹。"
---

<!-- argument-hint: [isomer-type, nucleus, formula, or chapter topic] -->

# 原子核同核异能态：微观机制与前沿前沿（A. K. Jain 等）

**著者**：Ashok Kumar Jain, Bhoomika Maheshwari, Alpana Goel（IIT Roorkee / 萨格勒布大学 / Amity 大学） | **出版社**：Springer Nature Switzerland (2021) | **页数**：151 页
**本地原件**：`raw/books/nuclear isomer - A Prime.pdf` (SHA-256 `20f88b84240637e10a6086eca6b9f6e80a28813ad1ecf14a795144a4d5c2ac34`)

本技能提炼国际核异能态领军学者 A. K. Jain 教授经典专著《Nuclear Isomers: A Primer》的核心物理体系，系统形式化原子核长寿命激发态（$T_{1/2} \ge 1\text{ ns}$）的四大微观物理机制——自旋陷阱（Spin Traps）、Seniority 代数异能态（Seniority Isomers）、$K$-异能态（$K$-Isomers）与裂变形状异能态（Shape Isomers），深入推导单 $j$ 壳层半满壳 $B(E2)$ 粒子-空穴对称性相消定理、高阶 $K$-禁戒跃迁折合阻碍度幂律 $f_\nu = (F_W)^{1/\nu}$，以及非轴对称三轴形变破坏轴对称性诱导 $K$-混合（$K$-mixing）使得阻碍度异常塌缩的三轴指纹效应。

## How to Use This Skill

- **异能态分类学与判据**：询问 `同核异能态四大机制`、`自旋陷阱Spin Trap`、`长寿命激发态分类`、`同核异能比Isomeric Ratio`；
- **Seniority 异能态与半满壳相消**：询问 `Seniority量子数v`、`单j壳层E2矩阵元`、`半满壳相消定理`、`130Sn的10+异能态`、`210Po的8+异能态`；
- **$K$-同核异能态与阻碍度幂律**：询问 `K量子数选择定则`、`禁戒度nu`、`Weisskopf阻碍因子F_W`、`折合阻碍度f_nu`、`178Hf的16+超长寿命异能态`；
- **三轴形变与 $K$-混合指纹**：询问 `三轴形变诱导K混合`、`轴对称破缺`、`f_nu反常下降`、`A~130区K异能态退激`；
- **形状共存与裂变异能态**：询问 `形状异能态Shape Isomer`、`双峰裂变势垒`、`第二超形变极小`、`WKB作用量与穿透半衰期`。

---

## Core Frameworks and Mental Models

1. **原子核同核异能态四大微观机制分类学（第 1–5 章）**：
   根据造成跃迁几率急剧抑制（寿命延长至 $T_{1/2} \ge 1\text{ ns}$ 乃至年量级）的微观物理根源，全核图谱异能态严格划分为四大物理机制：
   1. **自旋陷阱 (Spin Traps)**：初态与终态自旋差 $\Delta I$ 巨大，而跃迁能量 $E_\gamma$ 极小，受相空间因子 $E_\gamma^{2L+1}$ 与多极阶数 $L$ 的急剧抑制（如 $^{212m}\text{Po}$ 的 $18^+$ 态）；
   2. **Seniority 异能态 (Seniority Isomers)**：在近球形核的高-$j$ 独宇称壳层（如 $1h_{11/2}, 1i_{13/2}, 1g_{9/2}$）中，相同 Seniority（$\Delta v = 0$）的跃迁电四极矩阵元在半满壳处发生代数相消；
   3. **$K$-同核异能态 ($K$-Isomers)**：在强轴对称形变核中，跃迁自旋投影差大于辐射多极阶数（$|\Delta K| > \lambda$），受到轴向对称性量子数强力禁戒；
   4. **形状异能态 (Shape Isomers)**：初态与终态处于完全不同的宏观形变势阱中（如正常形变基态与 $2:1$ 轴比超形变第二极小态），受极宽空间裂变势垒的量子隧穿压制。

2. **Seniority 代数 scheme 与半满壳粒子-空穴对称性相消定理（第 3 章）**：
   - 在单 $j$ 轨道纯配对力哈密顿量下，系统由 Seniority 量子数 $v$（未成对单粒子数）标记；
   - **相同 Seniority（$\Delta v = 0$）偶多极单体算符（如电四极 $E2$）矩阵元展开**：
     $$\langle j^n, v, \alpha, J || \hat{M}(E2) || j^n, v, \alpha', J' \rangle = \left( \frac{2j + 1 - 2n}{2j + 1 - 2v} \right) \langle j^v, v, \alpha, J || \hat{M}(E2) || j^v, v, \alpha', J' \rangle;$$
   - **跃迁几率对粒子数 $n$ 的抛物线展开**：
     $$B(E2; j^n, v \to v) = \left( \frac{2j + 1 - 2n}{2j + 1 - 2v} \right)^2 B(E2; j^v, v \to v);$$
   - **半满壳绝对相消定理 (Mid-Shell Cancellation Theorem)**：
     当轨道填充达到**半满壳（Half-Filled Shell, $n = j + 1/2$）**时：
     $$2j + 1 - 2n = 2j + 1 - 2(j + 1/2) \equiv 0 \implies B(E2) \equiv 0!$$
     由于单 $j$ 壳层粒子-空穴严格时间反演共轭对称性，电四极跃迁振幅严格相消为零！在现实核中仅残存极微弱的微扰非对角混合，从而在半满壳核素（如中子半满壳 $^{130}\text{Sn}$ 的 $10^+$ 态、质子半满壳 $^{210}\text{Po}$ 的 $8^+$ 态与 $^{94}\text{Ru}$ 的 $8^+$ 态）中产生毫秒乃至微秒级的长寿命 Seniority 异能态！

3. **$K$-异能态选择定则、禁戒度 $\nu$ 与折合阻碍度幂律（第 5 章）**：
   - 在具有良好轴对称形变的原子核中，总角动量沿内禀对称轴的投影 $K = \sum_i \Omega_i$ 为守恒量子数；
   - **$K$-选择定则**：电磁辐射多极阶数 $\lambda$ 必须满足三角不等式：
     $$|\Delta K| = |K_i - K_f| \le \lambda;$$
   - **$K$-禁戒度 (Degree of $K$-Forbiddenness $\nu$)**：
     $$\nu \equiv |\Delta K| - \lambda;$$
     当 $|\Delta K| > \lambda$（$\nu > 0$）时，单步多极跃迁在对称轴投影守恒下一阶禁戒；
   - **Weisskopf 阻碍因子与折合阻碍度幂律 (Reduced Hindrance $f_\nu$)**：
     $$F_W \equiv \frac{T_{1/2}^{\text{exp}}}{T_{1/2}^W} = \frac{B_W(\sigma\lambda)}{B(\sigma\lambda)_{\text{exp}}}, \quad f_\nu \equiv (F_W)^{1/\nu} = \left( \frac{T_{1/2}^{\text{exp}}}{T_{1/2}^W} \right)^{1/(|\Delta K| - \lambda)}.$$
     实验经验规律表明：对于良好的轴对称变形核，$f_\nu$ 表现出惊人的常数聚集性：
     $$f_\nu \a30 - 100 \implies \text{每增加一级 } K \text{-禁戒，跃迁几率约降低两个数量级（阻碍 } 100 \text{ 倍）}！$$
     例如著名的超长寿命同核异能态 $^{178m2}\text{Hf}$（$K^\pi = 16^+, T_{1/2} = 31\text{ 年}$），退激至 $K=8$ 带首经历了 $\nu = 8$ 级高阶禁戒。

4. **三轴形变诱导 $K$-混合与阻碍度异常塌缩（第 5 章 §5.4）**：
   - 当原子核具有非轴对称三轴形变（$\gamma \ne 0^\circ$ 且 $\gamma \ne 60^\circ$）时，三主轴长短各不相同，轴对称旋转群 $SO(2)$ 被彻底破坏；
   - **$K$-混合（$K$-Mixing）微观机制**：
     波函数不再是单值纯 $K$ 态，而是不同 $K$ 分量的空间相干杂化混合：
     $$|\Psi\rangle = \sum_{K = 0, 2, 4 \dots} a_K |I M K\rangle;$$
   - **三轴实验指纹**：由于初态与终态波函数中杂化渗入了相同或相近的中间 $K$ 成分，使得原本名义上高 $\nu$ 禁戒的跃迁能够通过波函数中微小的 $K$ 杂质分量无禁戒地快速退激；
   - **折合阻碍度断崖式暴跌**：
     $$f_\nu \ll 10 \quad (\text{甚至降至 } f_\nu \sim 1 - 3);$$
     在 $A \a$A \aA \a130$ 质量区（如 $\text{Cs}, \text{Ba}, \text{La}, \text{Nd}$ 的奇奇核与多准粒子态）观测到 $f_\nu$ 的异常超常塌缩，是实验裁决原子核具备**真实非轴对称三轴形变**的核心谱学证据！

5. **裂变双峰势垒与超形变形状异能态（第 4 章）**：
   - 在微观-宏观 Strutinsky 壳修正下，重核（铀、钚、镅同位素）在四极形变空间形成双峰裂变势垒；
   - **第二极小超形变深阱（Shape Isomers / Fission Isomers）**：
     在两主轴比达 $2:1$ 的巨大拉伸超形变处，存在第二个亚稳局域能量深阱，其基态寿命长达微秒至毫秒；
     穿透退激半衰期由 WKB 量子穿隧积分严格决定：
     $$T_{1/2} \propto \exp\left( \frac{2}{\hbar} \int_{a}^{b} \sqrt{2 B(s) [V(s) - E]} \, ds \right).$$

---

## Chapter Index

| # | 章节主题 | 核心数学方法与核结构物理应用 |
|---|---|---|
| [ch01](chapters/ch01-isomers-classification-and-spin-traps.md) | 同核异能态分类学与自旋陷阱机制 | 四大物理机制分类、相空间因子 $E_\gamma^{2L+1}$ 压制、高自旋与在束延迟符合 |
| [ch03](chapters/ch03-seniority-isomers-and-mid-shell-cancellation.md) | Seniority 代数 scheme 与半满壳相消定理 | Racah 母权展开、粒子数抛物线因式、半满壳 $B(E2) \equiv 0$ 与 $^{130}\text{Sn}, {}^{210}\text{Po}$ |
| [ch04](chapters/ch04-shape-isomers-and-double-humped-fission.md) | 形状异能态与双峰裂变势垒动力学 | Strutinsky 壳修正、第二超形变极小态、WKB 穿透作用量与超形变谱学 |
| [ch05-k](chapters/ch05-k-isomers-and-hindrance-systematics.md) | $K$-同核异能态、选择定则与折合阻碍度 | 轴向自旋投影守恒、禁戒度 $\nu = |\Delta K| - \lambda$、经验幂律 $f_\nu \a100$ 与 $^{178}\text{Hf}$ |
| [ch05-mix](chapters/ch05-triaxiality-induced-k-mixing.md) | 三轴形变诱导 $K$-混合与阻碍度塌缩指纹 | 轴对称破坏、波函数多 $K$ 空间杂化、$f_\nu < 10$ 异常塌缩与 $A\sim 130$ 三轴判定 |

## Supporting Reference Files

- [glossary.md](glossary.md) — 同核异能态四大机制、Seniority 代数、$K$ 禁戒度与形状共存专业术语中英双语定义。
- [patterns.md](patterns.md) — 5 大同核异能态物理机制识别、半满壳相消反演与三轴 $K$ 混合分析范式。
- [cheatsheet.md](cheatsheet.md) — 典型 Seniority 异能态核素数据表、$K$ 异能态阻碍度经验表与双峰裂变常数卡。

---

## Scope & Limits

本技能提供单 $j$ 壳层配对相消代数、轴向 $K$ 禁戒度与三轴 $K$ 混合的物理判定法典。对于具体高自旋在束符合矩阵提取与时间晃动滤波，配合 `nuclear-experimental-methods`；对于非轴对称三轴转子 Davydov-Filippov 模型求解，配合 `greiner-nuclear-models`；对于多极混合比 $\delta$ 统计双根裁决，配合 `zhu-experimental-statistics`。
