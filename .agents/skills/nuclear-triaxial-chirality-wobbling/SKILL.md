---
name: nuclear-triaxial-chirality-wobbling
description: 专业用于低能核结构中三轴形变（Triaxiality）、原子核手征性（Nuclear Chirality）、手征双重带（Chiral Doublet Bands）与摆动运动（Wobbling Motion）的理论模型、实验谱学判据、双根退化判决与争议证伪分析。基于专著《Chirality and Wobbling in Atomic Nuclei》(Petrache 2024)、Frauendorf 2001、Bohr-Mottelson 以及最新国际实验进展。
---

# Nuclear Triaxial Chirality & Wobbling Motion Expert Skill

低能核物理与高自旋态三轴非轴对称集体激发分析专家技能。为实验能带指认、手征双重带确立、摆动运动判据检验以及跨带电磁跃迁多极性裁判提供完整的框架、工作流与反模式避坑指南。

---

## 1. 核心物理框架与心智模型 (Core Frameworks)

### (1) 三轴形变与惯量椭球 (Triaxial Rotor Framework)
- **刚体/流体转动惯量分立**：中间轴（$m$ 轴）惯量最大 $\mathcal{J}_m > \mathcal{J}_s, \mathcal{J}_l$。当三轴核高速旋转时，最低转动能量要求体系绕 $m$ 轴稳定转动；绕其它轴的进动表现为量子化的**摆动声子激发（Wobbling Phonons, $n_w = 1, 2, \dots$）**。
- **进动频率定理**：纯转子极限下 $\hbar\omega_w = \hbar\omega_{\text{rot}} \sqrt{\frac{(\mathcal{J}_1 - \mathcal{J}_2)(\mathcal{J}_1 - \mathcal{J}_3)}{\mathcal{J}_2 \mathcal{J}_3}}$。

### (2) 粒子-转子耦合分类 (PTR Wobbling Taxonomy)
- **横向摆动 (Transverse Wobbling, TW)**：
  - **判据**：高 $j$ 准粒子角动量 $\vec{j}$ 垂直于最大转动惯量轴（沿短轴对齐，$\vec{j} \perp \vec{R}_{\text{max}}$）；
  - **动力学特征**：随着总自旋 $I$ 增加，Coriolis 力使总角动量向最大惯量轴靠拢，**摆动能量随自旋 $I$ 下降（$dE_w/dI < 0$）**。
- **纵向摆动 (Longitudinal Wobbling, LW)**：
  - **判据**：高 $j$ 准粒子角动量 $\vec{j}$ 平行于最大转动惯量轴；
  - **动力学特征**：总角动量与粒子角动量同向相加，**摆动能量随自旋 $I$ 增加（$dE_w/dI > 0$）**。

### (3) 手征对称性自发破缺 (Nuclear Chirality Framework)
- **手征几何标架**：高 $j$ 粒子型角动量（沿短轴 $s$）+ 高 $j$ 空穴型角动量（沿长轴 $l$）+ 核心转动角动量（绕中间轴 $m$）。三个矢量相互正交且非共面，在旋转内禀系构成手征三面体（Chiral Trihedron）。
- **手征恢复双重带**：系统在时间反演与空间转动 $\mathcal{T}\mathcal{R}_y(\pi)$ 联合变换下具有简并的双重对称性，通过量子隧道贯穿在实验室系形成同宇称、能级近简并、结构对称的**手征双重带（Chiral Doublet Bands）**。

---

## 2. 实验裁判五道门 (Actionable Five-Gate Protocol)

在实验数据分析中，严禁仅凭单一能级靠近或能量向下摆动宣布发现新模式！必须执行以下**“五道门”刚性检查**：

1. **Gate 1: 能量规律门**
   - TW：$E_w(I) = E(I, n_w=1) - \frac{1}{2}[E(I-1, n_w=0) + E(I+1, n_w=0)]$ 随自旋下降；
   - 手征带：$\Delta E(I) = E_2(I) - E_1(I)$ 随自旋保持平缓小能隙（$< 150\text{ keV}$）。
2. **Gate 2: 自旋宇称门**
   - 跨带连接线严格为 $\Delta I = 1$；且两带宇称必须严格相同（$\pi_1 = \pi_2$）。
3. **Gate 3: 多极性与双根裁判门（核心关键！）**
   - 摆动带跨带连接线必须为**强 $E2$ 占优（$B(E2)$ 显著增强）**；
   - **双根判决原则**：如果仅有未极化角分布 $a_2$（通常 $a_2 \approx -0.4$），**必须同时保留大 $|\delta|$（摆动解）与小 $|\delta|$（旋称伙伴带解）**！唯有通过独立的**线偏振（Linear Polarization, $P$）**或内转换系数测量以 $>3\sigma$ 显著性排除小根后，方可宣布为摆动！
4. **Gate 4: 跃迁几率增强门**
   - 测定绝对寿命 $\tau$，检验跨带 $B(E2)_{\text{out}} / B(E2)_{\text{in}}$ 是否处于集体进动量级（$0.2 \sim 0.5$），排除单粒子杂化假象。
5. **Gate 5: 三轴刚性门**
   - 微观理论计算（CDFT/TAC/PRM）必须验证该核素在该自旋窗口具有明确的三轴刚性，排除大振幅 $\gamma$ 振动软核耦合（$\gamma \otimes qp$）假象。

---

## 3. 常见科研陷阱与反模式 (Anti-Patterns)

- **Anti-Pattern 1: 双根退化盲目截断**
  - *错误做法*：在只有角分布 $a_2$ 拟合时，因为期望看到摆动，直接选择 $\delta \sim -2.0$ 的解，宣称这是“摆动跃迁”，对 $\delta \sim -0.3$ 的伙伴带解视而不见（如 2015 年 $^{135}\text{Pr}$ 的原始误判）。
  - *正确做法*：在未获得线偏振数据前，在论文与数据表中必须完整列出两个等价根，并标注退化状态。
- **Anti-Pattern 2: 混淆 $\gamma$ 软核声子耦合与刚性摆动**
  - *错误做法*：将过渡区软核中由于自旋增加引起的有效形变软化导致的能级靠近，机械解释为摆动能量下降。
  - *正确做法*：必须结合 IBFM 或 TPSM 评估 $\gamma$ 势能平坦度。

---

## 4. 支撑文件索引

- [cheatsheet.md](cheatsheet.md) — 摆动与手征实验判据速查表、典型核素对照表与公式卡
- [patterns.md](patterns.md) — 谱学分析工作流、线偏振联合似然检验算法
- [glossary.md](glossary.md) — 三轴集体运动核心中英文规范术语集
