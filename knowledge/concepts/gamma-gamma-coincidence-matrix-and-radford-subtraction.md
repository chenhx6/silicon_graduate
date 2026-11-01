---
type: concept
title: "在束γ-γ二维符合矩阵切片、Radford二维背景扣除算法与能级纲图级联判据"
aliases: [二维符合矩阵, gamma-gamma符合, Radford背景扣除, Radware算法, 峰门切片, 康普顿平原消除, 级联确认, 互斥分支]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [gamma-gamma-coincidence, radford-subtraction, radware, matrix-slicing, level-scheme-construction, in-beam-spectroscopy, peak-to-background]
---

# 在束γ-γ二维符合矩阵切片、Radford二维背景扣除算法与能级纲图级联判据

## 1. 物理全景：从庞杂全投影谱到清晰级联关系的二维解析

在束核物理实验中，重离子熔合蒸发反应产生的残核在极短时间内（飞秒至纳秒）发射密集的 $\gamma$ 射线瀑布。
如果仅仅使用单道谱仪记录一维全投影能谱（Total Projection Spectrum）：
由于数十条甚至上百条跃迁相互重叠，加上巨大的康普顿散射连续平原（Compton Continuum），微弱的低强度未知跃迁会被完全淹没，物理学家根本**无法直接判定哪两条 $\gamma$ 射线属于同一条转动带，更无法确定能级的先后级联次序**。

根据 D. C. Radford（Nucl. Instrum. Methods A 361, 297, 1995，Radware 软件套件与 ESCL8R 分析器）、M. A. Deleplanque 等（Phys. Rev. Lett. 43, 749, 1979）以及吴治华《原子核物理实验方法》（第三版）：
**解决这一困难的终极物理方案是构建二维对称符合矩阵（2D $\gamma-\gamma$ Coincidence Matrix, $M(E_1, E_2)$）**：
1. **符合事件的微观定义**：
   只有当两个不同的 HPGe 探头在纳秒级时间符合门（$\Delta t \le 50 \sim 100\text{ ns}$）内同时记录到光子时，事件才被作为一个点增量累加在矩阵道址 $(i, j)$ 与对称道址 $(j, i)$ 上；
2. **2D 背景的三重成分**：
   在二维空间中，任何一个门窗口不仅包含真实的“峰-峰（Peak-Peak）”符合，还充斥着“峰-康普顿（Peak-Compton）”、“康普顿-峰（Compton-Peak）”以及无所不在的“康普顿-康普顿（Compton-Compton）”偶然背景；
3. **Radford 2D 背景扣除黄金公式**：
   Radford 提出了革命性的闭合解析算法，通过全投影谱 $P_i$ 与其平滑背景 $B_i$ 的矩阵自洽乘积，**从第一性原理上彻底剥离掉假符合背景，使切片后的一维能谱只留下纯粹、平坦基线上的真符合峰**！

---

## 2. 严格数学推导与 Radford 扣除公式

### (1) 矩阵总计数与一维投影关系
设 $M_{ij}$ 为经过能量标定后的对称符合矩阵（$M_{ij} = M_{ji}$，道宽为 $\Delta E$）。
定义总一维投影谱（Total 1D Projection）：
$$P_i = \sum_j M_{ij}$$
矩阵全空间总计数为：
$$T = \sum_{i} P_i = \sum_{ij} M_{ij}$$
通过一维峰形拟合算法（如 Radware 中的 `gf3` 拟合），从全投影谱 $P_i$ 中剥离出平滑变化的康普顿背景谱 $B_i$。全投影中的纯净峰面积占空比为 $P_i - B_i$。

---

### (2) 传统相邻背景门扣除的局限性
在早期实验中，物理学家通常在待测跃迁能量 $E_{\text{gate}}$ 两侧各取一个背景门窗口 $BG_1, BG_2$：
$$S_i^{\text{trad}} = \sum_{j \in G} M_{ij} - \frac{W_G}{W_{BG}} \sum_{j \in BG} M_{ij}$$
这一做法存在致命缺陷：
当峰门 $G$ 内的康普顿背景自身包含共线散射时，传统扣除法会导致基线剧烈上下凹陷起伏，并在其他强峰位置产生虚假负峰（Negative Dips）！

---

### (3) Radford 2D 背景扣除严格闭合公式
Radford 指出，二维背景事件强度 $B_{ij}$ 在概率论上严格等于两个一维背景在相空间中的归一化直积：
$$B_{ij} \approx \frac{1}{T} \left( P_i B_j + B_i P_j - B_i B_j \right)$$
对选定的峰门 $G$（积分通道为 $j \in [j_{\text{min}}, j_{\text{max}}]$，总投影为 $P_G = \sum_{j \in G} P_j$，背景投影为 $B_G = \sum_{j \in G} B_j$）：
扣除全部背景后的**真符合一维切片能谱 $S_i$ 的最终形式为**：
$$S_i = \sum_{j \in G} M_{ij} - \frac{W_G}{W_{BG}} \sum_{j \in BG} M_{ij} - \frac{P_G - B_G}{T} B_i$$
- 第一项：门内的总实测计数；
- 第二项：消除与门内康普顿背景相关的“峰-康普顿”与“康普顿-康普顿”事件；
- 第三项：**Radford 核心补偿项**，扣除与门内真实光电峰相关的其他道址连续康普顿背景 $B_i$！

---

### (4) 能级纲图的逻辑裁决法则
利用扣除背景后的切片能谱 $S(E)$，核谱学家执行三大刚性裁判逻辑：
1. **级联充要条件（In Cascade）**：
   若跃迁 $\gamma_A$ 与 $\gamma_B$ 属于同一条转动带中的上下级联：
   - 在 $\gamma_A$ 门谱中必须清晰出现 $\gamma_B$ 峰；
   - 在 $\gamma_B$ 门谱中必须以对称几率出现 $\gamma_A$ 峰；
2. **互斥分支判据（Parallel Branching）**：
   若 $\gamma_A$ 与 $\gamma_B$ 是同一能级分叉发射的两条平行退激道，或者属于互不交叠的独立带：
   - 在 $\gamma_A$ 门谱中，$\gamma_B$ 能量处**必须严格表现为统计平坦的零基线**；
3. **同质异能态阻断（Isomer Interruption）**：
   若级联中间存在一个寿命长于符合时间门（如 $\tau > 100\text{ ns}$）的同质异能态：
   - 异能态上方的跃迁与异能态下方的跃迁之间的**符合联系被彻底切断**，证明中间存在长寿命结构陷阱！

---

## 3. 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/gamma_gamma_matrix_slicer_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `gslice` 命令。

### 运行示范（模拟典型在束转动带级联矩阵在 $350.0\text{ keV}$ 处的峰门切片）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py gslice -G 350.0 -W 12.0 --json
```

### 计算输出核心物理特征：
1. **矩阵规模与总事件**：$100 \times 100$ 道，总积累计数达 $8.60 \times 10^5$；
2. **切片门参数**：
   - 峰门设定在 $350.0\text{ keV}$（通道 $[34, 36]$），峰总计数 $39000$，背景计数 $24000$；
   - 峰背比达到 $P/B = 0.62$；
3. **级联峰自动识别与强度守恒**：
   - 经过 Radford 算法扣除后，平坦基线上清晰析出 3 个真符合峰：
     - $200.0\text{ keV}$ 跃迁：净峰面积为 $5000.0$；
     - $500.0\text{ keV}$ 跃迁：净峰面积为 $5000.0$；
     - $650.0\text{ keV}$ 跃迁：净峰面积为 $5000.0$；
   - 全部标记为 `In_Cascade_Confirmed`，严格证实了 $200 \to 350 \to 500 \to 650\text{ keV}$ 四条射线完全处于同一个级联转动带中，彻底复现了 Radware 在束建纲图的经典分析流程！

---

## 4. 与相关前沿概念的交叉引用
- [[coincidence-intensity-and-level-scheme-balancing]]：此处提取的真符合峰面积 $A_{\text{coinc}}$ 直接充当能级进出流强平衡守恒检验的原始输入；
- [[hpge-digital-pulse-processing-pzc-and-ballistic-deficit]]：高质量的数字脉冲梯形滤波确保光电峰不发生弹道拖尾，是实现高信噪比 2D 矩阵切片的前提；
- [[side-feeding-dynamics-and-doppler-lineshape-deconvolution]]：在符合矩阵中设置顶门（Top-gate）切片，是彻底排除慢侧馈送延迟的物理黄金方案。
