---
name: heyde-nuclear-physics
description: "Kris L. G. Heyde《Basic Ideas and Concepts in Nuclear Physics》（第二版）：微观壳模型与残余相互作用、相互作用玻色子模型 (IBM-1/IBM-2)、磁偶极剪刀模式 (Scissors Mode)、等矢巨偶极共振 (IVGDR) 双峰分裂、弱束缚晕核与软 E1 模、多重形状共存与反转岛。"
---

<!-- argument-hint: [model-name, concept, observable, or chapter topic] -->

# 核物理基本思想与概念（Kris L. G. Heyde）

**著者**：Kris L. G. Heyde（根特大学理论物理研究所） | **出版社**：Institute of Physics Publishing (IOP), Bristol and Philadelphia (1999, 2nd Edition) | **页数**：647 页
**本地原件**：`raw/books/Basic Ideas and Concepts in Nuclear Physics An Introductory Approach (Kris L.G. Heyde) (Z-Library).pdf` (SHA-256 `0490c8036be9cd8702cd8aec9c858ebb0e898e6c7b2b1056ce36e205f9f3c18a`)

本技能提炼 Kris Heyde 权威巨著《Basic Ideas and Concepts in Nuclear Physics（第二版）》的核心物理体系，架设从独立粒子微观壳模型、两体有效相互作用到代数相互作用玻色子模型（IBM）、质中剪刀振动模式（Scissors Mode）、宏观多极巨共振、弱束缚晕核与近闭壳多重形状共存的理论桥梁，为低能核结构相变、集体电磁跃迁与极端同位旋物理提供统一的理论指引。

## How to Use This Skill

- **相互作用玻色子模型 (IBM-1 / IBM-2)**：询问 `IBM动力学对称性`、`U(5)振动极限`、`SU(3)转动极限`、`O(6)软核极限`、`Casten三角形相变`；
- **磁偶极剪刀模式 (Scissors Mode)**：询问 `IBM-2剪刀模式`、`B(M1)减缩公式`、`价玻色子数依赖性`、`混合对称态MSS`、`质中相对角摆动`；
- **巨多极共振 (Giant Resonances)**：询问 `等标巨单极共振ISGMR`、`核不可压缩模量K_inf`、`等矢巨偶极共振IVGDR`、`形变双峰分裂1:2`、`TRK求和规则`；
- **极端稳定性与晕核 (Halo Nuclei)**：询问 `单中子/双中子晕核`、`物质半径发散`、`Borromean系统`、`软偶极共振Soft E1`、`反转岛Island of Inversion`；
- **多重形状共存 (Shape Coexistence)**：询问 `近闭壳核形状共存`、`186Pb三重0+态`、`E0单极跃迁`、`势能面多重极小`；
- **高自旋回弯与推转模型**：询问 `独宇称侵入轨道顺排`、`Coriolis解耦`、`回弯Backbending`、`超形变SD`。

---

## Core Frameworks and Mental Models

1. **两体有效残余相互作用与长程四极吸引（第 11 & 14 章）**：
   - 独立粒子哈密顿量产生球形平均场单粒子壳层（幻数 $2, 8, 20, 28, 50, 82, 126$）；
   - **短程配对力（$\delta$ 吸引力）**：主要作用于同类核子（$pp$ 或 $nn$），促使偶偶核基态形成 $J=0^+$ 凝聚，维持球形结构；
   - **长程四极-四极相互作用（$H_{QQ} = -\chi \hat{Q}_\pi \cdot \hat{Q}_\nu$）**：
     质子与中子在空间具有强烈的四极-四极吸引相互作用；
     当开壳价核子数足够多时，$H_{QQ}$ 的相干四极能超过球形壳缝与配对能，打破球对称性，自发诱发原子核发生宏观**四极长椭球或三轴形变**！

2. **相互作用玻色子模型（IBM-1 / IBM-2）与动力学对称性（第 13 章 §13.3）**：
   - 将价质子对与价中子对映射为自旋为 $0$ 的标量玻色子（$s$ 玻色子）与自旋为 $2$ 的四极玻色子（$d$ 玻色子），构成六维生成元代数 $U(6)$；
   - **Casten 三角形的三大动力学对称极限**：
     1. **$U(5)$ 振动极限**：对应球形核微扰简谐四极表面振动，$R_{4/2} \approx 2.00$；
     2. **$SU(3)$ 转动极限**：对应强变形轴对称长椭刚体转子，$R_{4/2} = 3.333$；
     3. **$O(6)$ $\gamma$ 软核极限**：对应完全 $\gamma$ 独立不稳定核（Wilets-Jean 对应），$R_{4/2} = 2.500$。

3. **IBM-2 质中混合对称态与磁偶极剪刀模式（第 13 章 Box 13b）**：
   - 显式区分质子玻色子（$N_\pi$）与中子玻色子（$N_\nu$），引入 $F$-旋（$F = \frac{1}{2}(N_\pi + N_\nu)$ 为全对称标量态，$F = F_m_{\max}-1$ 为质中混合对称态 MSS）；
   - **剪刀振动模式 $B(M1)$ 强度减缩公式（Heyde 式 13b.1）**：
     $$B(M1; 0_1^+ \to 1_1^+) = \frac{3}{4\pi} \frac{8 N_\pi N_\nu}{2N - 1} (g_\pi - g_\nu)^2\ \mu_N^2, \quad (N = N_\pi + N_\nu);$$
   - **物理突破**：微观阐明了剪刀模式强度严格受限于**价壳层内价玻色子参与数目**，完美解释了为什么稀土区 $^{156}\text{Gd}$（$N_\pi=7, N_\nu=5, N=12$）实测强度 $1.3 \pm 0.2\ \mu_N^2$ 相较纯宏观全核参与双转子模型（预言 $\sim 15\ \mu_N^2$）减缩近一个数量级！

4. **巨多极共振与长椭核中的 IVGDR 双峰分裂（第 13 章 §13.1）**：
   - **等标巨单极共振（ISGMR）**：全核核子做球对称径向呼吸振动，激发能 $E_{\text{GMR}} \a80 A^{-1/3}\text{ MeV}$，直接反演核物质无限大体积对称不可压缩系数 $K_\infty \approx 240 \pm 20\text{ MeV}$；
   - **等矢巨偶极共振（IVGDR）在长椭变形核中的几何分裂**：
     核子沿长轴（$z$ 轴，曲率半径长，恢复力小）与短轴（$x, y$ 轴，曲率半径短，恢复力大）振荡频率不同；
     共振峰精确分裂为能量不同的双峰 $E_a < E_b$，且共振曲线下积分截面面积比严格满足两垂直短轴空间简并度：
     $$\frac{\int \sigma_a(E) dE}{\int \sigma_b(E) dE} \equiv \frac{1}{2}.$$

5. **极端同位旋与弱束缚晕核物理（第 15 章 §15.1）**：
   - 在中子滴线极区，最外层价中子分离能极其微小（$S_n \le 0.5 - 1.0\text{ MeV}$）；
   - **离心势垒缺乏与空间长尾隧穿**：当中子占据低轨道角动量（$l=0$ 的 $2s_{1/2}$ 轨道或 $l=1$ 的 $2p_{1/2}$ 轨道）时，离心势垒 $\propto l(l+1)/r^2$ 消失或极低，中子波函数以极其缓慢的指数形式弥散渗入经典禁戒区数百飞米；
   - **特征观测现象**：
     1. 均方根物质半径呈现阶跃式反常发散（如 $^{11}\text{Li}$ 物质半径相当于 $^{208}\text{Pb}$ 的大小）；
     2. **Borromean 三体系统**：核心与两个价中子构成的三体系统，任意两体均不能束缚，唯有三体共同形成稳定态；
     3. **低能软偶极共振（Soft $E1$ Mode）**：晕中子相对于致密紧束缚核心发生大振幅低频偶极角摇摆，在 $E_x \sim 1 - 2\text{ MeV}$ 产生显著的电偶极相干激发强度。

6. **近闭壳核的多重形状共存（第 13 章 Box 13c）**：
   - 在幻数或半幻数壳闭壳附近（如铅同位素 $Z=82$），质子闭壳提供强球形驱动；然而由于中子处于中壳填充区，质中四极吸引能强烈压低质子 $2p-2h$ 与 $4p-4h$ 激发组态的形变能量；
   - **标杆案例 $^{186}\text{Pb}$**：在低激发能区（$< 700\text{ keV}$）同时并存三个不同宏观几何的 $0^+$ 态：
     - 基态 $0_1^+$：纯球形驱动态；
     - 第一激发态 $0_2^+$（$532\text{ keV}$）：扁椭形变极小态；
     - 第二激发态 $0_3^+$（$650\text{ keV}$）：长椭形变极小态。
   - 三个构型之间伴随着极强的无光子电单极内转换 $E0$ 跃迁，直接证实微观势能曲面存在多个共存的宏观拓扑极小。

---

## Chapter Index

| # | 章节主题 | 核心数学方法与核物理应用 |
|---|---|---|
| [ch11](chapters/ch11-residual-interactions-and-multipoles.md) | 两体残余相互作用与长程四极力 | 短程配对力、多极展开、$H_{QQ} = -\chi Q_\pi \cdot Q_\nu$ 驱动宏观四极形变机制 |
| [ch13-gr](chapters/ch13-collective-vibrations-and-giant-resonances.md) | 表面集体振动与多极巨共振 | ISGMR 核物质不可压缩系数 $K_\infty$、IVGDR 形变双峰 $1:2$ 分裂与 TRK 求和规则 |
| [ch13-ibm](chapters/ch13-interacting-boson-model-and-scissors-mode.md) | 相互作用玻色子模型 (IBM) 与剪刀模式 | $U(5)/SU(3)/O(6)$ 极限、Casten 三角形、IBM-2 剪刀模 $B(M1)$ 价玻色子缩放律 |
| [ch13-sc](chapters/ch13-nuclear-shape-coexistence.md) | 多重形状共存与多极小势能面 | 近闭壳核粒子-空穴激发侵入、$^{186}\text{Pb}$ 三重 $0^+$ 态共存与 $E0$ 跃迁指纹 |
| [ch14](chapters/ch14-deformed-shell-model-and-backbending.md) | Nilsson 变形壳模型与高自旋回弯 | 独宇称高-$j$ 侵入轨道顺排 (RAL)、Coriolis 解耦、转动回弯与超形变能面 |
| [ch15](chapters/ch15-extremes-of-stability-and-halo-nuclei.md) | 极端稳定性边界、晕核与软偶极模 | 弱结合与低离心势垒空间长尾、Borromean 系统、软 $E1$ 共振与反转岛 |

## Supporting Reference Files

- [glossary.md](glossary.md) — 相互作用玻色子模型、巨共振、晕核与形状共存专业术语中英双语定义。
- [patterns.md](patterns.md) — 5 大微观与代数核结构模型推演范式。
- [cheatsheet.md](cheatsheet.md) — IBM 对称性极限特征表、剪刀模式实验参数表与典型晕核常数卡。

---

## Scope & Limits

本技能提供从微观有效相互作用到代数模型（IBM）与多极巨共振的体系化物理直觉与解析标尺。对于严格微观 3D 空间倾斜轴推转与手征几何，配合 `chirality-and-wobbling-atomic-nuclei`；对于大样本在束能谱拟合与双根似然比仲裁，配合 `zhu-experimental-statistics`；对于重离子束能激发函数与熔合势垒穿透，配合 `heavy-ion-nuclear-reactions`。
