---
type: concept
title: "两中子分离能系统学、核子配对能（Pairing Gap）与壳层闭合判据"
aliases: [两中子分离能, S2n系统学, 配对能, 配对能隙, 奇偶交错, OES, 壳层淬灭, 五点公式, 幻数判据]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [separation-energy, pairing-gap, odd-even-staggering, shell-closure, magic-numbers, mass-curvature, bcs-theory]
---

# 两中子分离能系统学、核子配对能（Pairing Gap）与壳层闭合判据

## 1. 物理全景：原子核质量曲面的一阶与二阶微商物理

原子核基态质量（或结合能 $B(N, Z)$）是核内所有单粒子动能、两体有效核力、表面张力、库仑排斥与短程配对相互作用在整个 $A$ 体多体系统中的总能量积分投影。

根据 A. Bohr & B. R. Mottelson《Nuclear Structure》Vol. I（第 2 章）、K. Heyde《Basic Ideas in Nuclear Physics》（第 7 章）与卢希庭《原子核物理（修订版）》（第 1–2 章）：
1. **结合能的一阶差分——核子分离能（Separation Energy）**：
   从原子核中剥离单个或一对核子所需的最小能量：
   $$S_n(N, Z) = B(N, Z) - B(N-1, Z)$$
   $$S_{2n}(N, Z) = B(N, Z) - B(N-2, Z) = M(N-2, Z) + 2 M_n - M(N, Z)$$
   两中子分离能 $S_{2n}$ 过滤掉了单个未配对价核子引起的奇偶起伏，直接反映了**费米面（Fermi Surface）单粒子结合能随同位素链中子填充的光滑演化斜率**；
2. **结合能的二阶差分——核子配对能隙（Pairing Gap, $\Delta$）与奇偶交错（OES）**：
   原子核普遍展现出偶偶核比相邻奇 $A$ 核结合更紧密、奇奇核结合最松散的现象，物理本质源于短程吸引核力在时间反演共轭轨道核子对（$|j, m\rangle$ 与 $|j, -m\rangle$）之间诱发强烈的 $J=0^+, T=1$ 准粒子配对关联（BCS Pairing Correlation）；
3. **结合能曲率异常——壳闭合与形状相变指纹**：
   $S_{2n}$ 曲线在传统幻数处的陡峭断崖反映了主壳层单粒子能级间隙；而 $S_{2n}$ 曲线的局域平坦乃至反常隆起，则是微观形变突然爆发（如 $N=88 \to 90$ 稀土区球形-大变形相变）带来的额外形变束缚能的直接热力学指纹！

---

## 2. 配对能隙微观公式：三点、四点与五点质量差分法典

为了从实测原子核质量谱中精确剥离核物质光滑宏观体积项与对称能曲率，国际物理界建立了多点有限差分指标：

### (1) 三点奇偶交错公式（Three-Point Formula, $\Delta^{(3)}$）
以中子配对隙为例，围绕奇数中子 $N$ 核素构造：
$$\Delta_n^{(3)}(N, Z) = \frac{(-1)^N}{2} \left[ M(N+1, Z) - 2 M(N, Z) + M(N-1, Z) \right]$$
- 当 $N$ 为奇数时，中间项为奇 $A$ 核，两端为偶偶核，$\Delta_n^{(3)}$ 直接度量最后一个未配对中子由于缺乏配对能所损失的束缚能；
- **局限性**：三点公式混杂了局域质量曲面的宏观对称能二次导数，导致提取的配对隙系统性偏高约 $10\% \sim 15\%$。

### (2) 五点平滑消除曲率公式（Five-Point Formula, $\Delta^{(5)}$，黄金标准）
为了彻底消除核质量曲面的线性能量漂移与一阶/二阶曲率偏置，Bohr & Mottelson 推荐了五点中心对称差分算符：
$$\Delta_n^{(5)}(N, Z) = \frac{(-1)^N}{8} \left[ M(N+2, Z) - 4 M(N+1, Z) + 6 M(N, Z) - 4 M(N-1, Z) + M(N-2, Z) \right]$$
该五点公式能够将光滑宏观背景抑制到三阶微商以上，是评估核内准粒子激发阈值（$2\Delta$）与高自旋转动带交叉阻尼最可靠的实验标尺！

### (3) 经验 BCS 配对能经验标度律
在整个核素图上，质子与中子配对能隙呈现高度稳定的质量数标度依赖：
$$\Delta_{\text{empirical}} \approx \frac{12}{\sqrt{A}}\text{ MeV} \quad \text{或} \quad \Delta_n \approx \frac{4.8}{A^{1/3}}\text{ MeV}$$
- 重核区（$A \sim 130$）：$\Delta_n \approx \frac{12}{\sqrt{130}} \approx 1.05\text{ MeV}$；
- 当原子核高速转动（高自旋）时，Coriolis 力使准粒子逐渐对齐，发生 Coriolis 反配对（CAP 效应），有效配对能隙在第一次能带交叉（Backbending）处显著萎缩至基态的 $50\% \sim 60\%$。

---

## 3. 两中子分离能 $S_{2n}$ 系统学与物理判定法则

在沿固定质子数 $Z$ 扫描同位素链时，$S_{2n}(N)$ 呈现出极具诊断价值的几何形态：

```text
S_2n (MeV)
 ^
 |    \
 |     \       <-- 壳内正常线性平缓下降 (斜率由平均对称能与排斥力主导)
 |      \
 |       *  N = 82 (传统主壳层)
 |        |
 |        |  <-- 跨越幻数断崖：\Delta S_{2n} 剧跌 2 ~ 4 MeV (Shell Gap)
 |        |
 |        *  N = 84
 |          |          \__  <-- 突发大形变区 (额外形变能补偿结合能，曲线出现反常隆起/拐点)
 +-----------------------------------------> 中子数 N
```

### (1) 壳层闭合（Shell Closure）的断崖突变判据
当沿同位素链从中子数 $N_{\text{magic}}$ 跨越至 $N_{\text{magic}} + 2$ 时，两中子必须填入高一个主壳层的单粒子轨道：
$$\delta_{2n}(N_{\text{magic}}) \equiv S_{2n}(N_{\text{magic}}, Z) - S_{2n}(N_{\text{magic}} + 2, Z)$$
- 在双幻核（如 $^{132}\text{Sn}$ 的 $N=82$、$^{208}\text{Pb}$ 的 $N=126$）处，$\delta_{2n}$ 跃升至 **$3 \sim 5\text{ MeV}$** 的巨型断崖；
- **壳层淬灭（Shell Quenching）**：在极丰中子滴线区，由于自旋-轨道耦合弱化与连续态耦合，$\delta_{2n}$ 断崖高度显著萎缩，直接证实传统幻数的消融。

### (2) 形状相变（Shape Phase Transition）的平坦反常判据
在球形向大四极变形过渡区（如稀土区 Sm, Nd 的 $N=88 \to 90$ 以及 $A\approx 100$ 的 Zr 同位素）：
- 正常情况下由于对称能增加，$S_{2n}$ 随 $N$ 单调线性下降（每增加 2 个中子约下降 $1.0 \sim 1.5\text{ MeV}$）；
- 但当体系从球形突然跃入大变形时，形变带来的结合能收益 $\Delta E_{\text{def}} = \frac{1}{2} C \beta_2^2$ 强力补偿了分离能损失，**导致 $S_{2n}(N=90) \approx S_{2n}(N=88)$ 出现异常的平坦平台甚至反向抬升**！

---

## 4. 与在束高自旋态谱学及 A≈130 质量区的交叉闭环

在博士课题直接相关的 $A\approx 130$（如 $^{131}\text{Ba}, {}^{132,133}\text{Ce}, {}^{135}\text{Nd}$）中：
1. **基态配对隙与高自旋交叉频率解耦**：
   AME2020 测定的基态质量三点配对能 $\Delta_n^{(3)} \approx 1.17\text{ MeV}$ 提供了基态核芯配对强的静态标尺；而在高自旋转动带中，通过 Routhian 角动量对齐反演的带交叉频率 $\hbar\omega_c \approx 0.35\text{ MeV}$，则由局域准粒子能隙与 Coriolis 耦合矩阵元共同决定，不能将静态基态配对能直接等同于高自旋配对能；
2. **手征带头配对弱化与三维手征涌现**：
   在奇奇核（如 $^{128}\text{Cs}$）中，质子与中子各自占据单个准粒子轨道，导致核系统质子配对与中子配对双重弱化，阻止了对关联对三轴形变核心的硬化束缚，为手征双重带的高速柔性进动扫清了微观阻碍。

---

## 5. Python 算法设计与实验分析器规范

本 Wiki 在 `system/scripts/analysis/pairing_gap_separation_energy_calculator.py` 中实现了完整的质量曲率与配对分离能分析器：
1. **分离能自动求解器**：输入同位素链结合能或原子质量，自动计算 $S_n, S_{2n}, S_p, S_{2p}$；
2. **三点与五点配对能隙计算器**：实现 $\Delta^{(3)}$ 与 $\Delta^{(5)}$ 的精确计算，输出与经验 $\frac{12}{\sqrt{A}}$ 的偏差比率；
3. **主壳层断崖与壳能隙量化器**：自动扫描同位素链，诊断幻数断崖 $\delta_{2n}$ 与壳淬灭程度；
4. **形状相变隆起/平坦异常检测器**：对 $S_{2n}$ 斜率的一阶导数做平滑拟合，自动识别形状相变拐点。

---

## 6. 权威文献与理论溯源

1. **Bohr, A. & Mottelson, B. R.** (1969). *Nuclear Structure*, Vol. I (Single-Particle Motion), Chapter 2 (Nuclear masses and separation energies). Benjamin, New York.
2. **Heyde, K.** (2004). *Basic Ideas and Concepts in Nuclear Physics* (3rd Edition), Chapter 7 (Two-neutron separation energies and pairing). CRC Press.
3. **Wang, M. et al.** (2021). The AME 2020 atomic mass evaluation. *Chin. Phys. C*, 45(3), 030003.
4. **Bender, M., Rutz, K., Reinhard, P.-G., & Maruhn, J. A.** (2000). Pairing gaps from nuclear mean-field models. *Eur. Phys. J. A*, 8(1), 59-75.
5. **卢希庭、江栋兴、叶沿林** (2000). 《原子核物理（修订版）》第 1–2 章：结合能系统学与核子配对相互作用. 原子能出版社.
