---
type: method
method_type: experimental-analysis-contract
title: "国际核结构与衰变数据网 ENSDF 格式语义与能级纲图自动对账指南"
aliases: [ENSDF格式指南, NNDC核数据规范, XUNDL解析方法, 能级纲图跨平台对账, 核谱学数据格式]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [ensdf, nndc, level-scheme, nuclear-data-formats, spectroscopy-crosswalk, gamma-rays]
---

# 国际核结构与衰变数据网 ENSDF 格式语义与能级纲图自动对账指南

## Purpose

### 国际核数据基础设施全景

在低能实验核物理与核谱学分析中，由国际原子能机构（IAEA）协调、美国布鲁克海文国家实验室国家核数据中心（NNDC）主导维护的**评估核结构数据文件（Evaluated Nuclear Structure Data File, ENSDF）**与**在束编译核数据文件（XUNDL）**，是全球学术界公认的最权威能级结构与衰变性质基准数据库。

在处理独立实验数据（如 $^{131}\text{Ce}$ 或 $^{133}\text{Ce}$）时，研究者必须将实测的新峰位、符合关系和跃迁分支比与 ENSDF 既有评估纲图进行严格的**逐行自动对账（Crosswalk Alignment）**，以快速识别已知基底带、标记新跃迁、排查杂质污染。

---

## Inputs and Assumptions

### ENSDF 80 列固定宽度（Fixed-Width）格式规范

ENSDF 文件采用经典的 80 列 ASCII 纯文本格式组织，每一行代表一个特定的物理实体。

### (1) 能级记录（Level Record，第 8 列为 'L' 或空格）
```
 1-5   6-7  8  9   10-19       20-21  22-39       40-49       ...
 131CE  L           0.0                 (7/2+)      10.2 M
 131CE  L         161.8               1 (11/2-)     4.8 PS
```
- **1–5 列**：核素标识符（如 `131CE`，左对齐）；
- **第 8 列**：记录类型标识符 `L`；
- **10–19 列**：能级激发能量（keV，相对基态）；
- **20–21 列**：能量不确定度；
- **22–39 列**：评估的自旋和宇称 $J^\pi$（若存疑带括号，如 `(11/2-)`）；
- **40–49 列**：能级半衰期 $T_{1/2}$ 或共振宽度 $\Gamma$（单位：`PS`, `NS`, `US`, `MS`, `S`, `M`, `H`, `D`, `Y`）。

### (2) 辐射跃迁记录（Gamma Record，第 8 列为 'G'）
紧随母能级记录之后，列出从该能级向下退激的所有 $\gamma$ 射线：
```
 1-5   6-7  8  9   10-19       20-21  22-29     30-31  32-41     42-49     ... 56-62
 131CE  G         161.8       1      100              M2+E3     -0.15          0.235
 131CE  G         450.2       2       45.2      12    (E2)                     0.021
```
- **10–19 列**：$\gamma$ 射线能量 $E_\gamma$（keV）；
- **20–21 列**：$E_\gamma$ 不确定度；
- **22–29 列**：相对发射光子强度 $I_\gamma$；
- **30–31 列**：$I_\gamma$ 不确定度；
- **32–41 列**：电磁多极性（Multipolarity，如 `E2`, `M1+E2`, `[E1]`）；
- **42–49 列**：多极混合比 $\delta$（遵循 Krane-Steffen 符号约定！）；
- **56–62 列**：总内转换系数 $\alpha_{\text{tot}}$。

---

## What It Can Establish

### 理论判据与可观测量

## What It Cannot Establish Alone

### 自动化能级纲图对账工作流（Crosswalk Protocol）

编写数据对账程序时，必须遵循以下容差匹配与判定法则：

1. **能量窗口容差匹配（Energy Matching Tolerance）**：
   - 对高纯锗（HPGe）在束谱仪，实测峰位与 ENSDF 评估值之间的能量容差通常设定为 $\Delta E_\gamma \le 1.0\text{ keV}$；
   - 若在容差内匹配成功，继承其评估自旋宇称与已知多极性；
2. **分支比拓扑检验（Branching Consistency）**：
   - 从同一能级退激的多条分支线，其实测强度比值 $I_{\gamma 1} / I_{\gamma 2}$ 必须在 $3\sigma$ 统计误差内与 ENSDF 符合；
   - 若强度比发生严重畸变，提示存在未分辨的能量重叠双峰（Unresolved doublet）或该能级受高自旋转动带强力布居导致的级联重配；
3. **新跃迁确认规则（New Transition Candidate）**：
   - 若某条强符合线在 $\pm 2.0\text{ keV}$ 内无任何 ENSDF 对应记录，且满足与已知能带的门控符合关系，标记为新发现候选跃迁，记录为独立研究增益。


## Sources

- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
