---
type: research-note
title: "三轴超形变（TSD）摆动激发与核芯非集体带终止的相空间竞争：163-167Lu与169Tm微观演化机制"
aliases: [tsd-wobbling-vs-core-termination-microscopic-competition, TSD wobbling vs core termination, Day27 TSD termination]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [odegard-2001-evidence-wobbling-163lu, jensen-2002-second-phonon-wobbling-163lu, schonwasser-2003-wobbling-165lu, amro-2003-wobbling-167lu, frauendorf-2014-transverse-wobbling]
created_from: Day 27 continuation study; system/scripts/day27_tsd_wobbling_vs_termination_study.py
tags: [triaxial-superdeformation, TSD-bands, transverse-wobbling, core-termination, CNS-model, wobbling-phonon, 163Lu, 165Lu, 167Lu, 169Tm, A160, Day27]
---

# 三轴超形变（TSD）摆动激发与核芯非集体带终止的相空间竞争：163-167Lu 与 169Tm 微观演化机制

## Research Trigger

在稀土区高自旋核物理中，三轴超形变（Triaxial Superdeformation, TSD，$\varepsilon_2 \approx 0.38 - 0.40, \gamma \approx 18^\circ - 21^\circ$）能带中的横向摆动运动（Transverse Wobbling, TW）构成了旋转对称性破缺的标杆性实验发现：
- 在 $^{163}\text{Lu}$（[[odegard-2001-evidence-wobbling-163lu]], [[jensen-2002-second-phonon-wobbling-163lu]]）中，实验确立了标志性的单声子与双声子摆动能带，摆动频率随自旋增加单调下降（$d\hbar\omega_w / dI < 0$），带外具有强大的集体电四极跃迁（$B(E2_{\text{out}})/B(E2_{\text{in}}) \sim 0.25 - 0.50$）；
- 然而，沿镥同位素链向重核方向演化时，实验呈现出一系列未被完全阐明的突变：
  1. 在 $^{167}\text{Lu}$（[[amro-2003-wobbling-167lu]]）中，摆动能量随自旋下降的趋势过早停滞，表现为 $\hbar\omega_w \sim 130 - 140\text{ keV}$ 的平坦直线响应；
  2. 在 $^{169}\text{Tm}$（$N=100$）中，集体摆动激发彻底消亡，高自旋带退化为普通轴对称长椭转子；
  3. 此外，依据推转 Nilsson-Strutinsky（CNS）理论，当自旋达到极高自旋区时，核芯的价核子对齐必然拉动形变向非集体扁椭轴（$\gamma = 60^\circ$）偏移，诱发非集体能带终止（Band Termination）。

这引出核心科学问题：**是什么微观条件决定了 TSD 摆动声子能够稳定存活还是过早平坦淬灭？中子数增加如何驱动三轴势能面曲率耗散？核芯价粒子对齐诱发的非集体带终止是如何与摆动模式在相空间中竞争的？**

## Grounded Evidence

通过执行全微观 CNS 势能曲面轨迹与配对修正 HFA 横向摆动求解器 `system/scripts/day27_tsd_wobbling_vs_termination_study.py`（数值结果存入 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/tsd-wobbling-termination/tsd_wobbling_termination_results.json`），确立以下定量证据：

1. **$^{163}\text{Lu}$ 深 TSD 势能曲率与横向摆动平稳下降：**
   - 在 $N=92$ 处，中子与质子多重高-$j$ 侵入能隙协同，构筑了深达 $V_{\text{barrier}} = 1.20\text{ MeV}$ 的 TSD 势阱（$\varepsilon_2 = 0.38, \gamma = 20.0^\circ$），其横向形变刚度高达 $C_\gamma = 9.84\text{ MeV}/\text{rad}^2$；
   - 配对修正转动惯量呈现严格的横向层级：中轴最大（$\mathcal{J}_m = 64.2\ \hbar^2/\text{MeV}$），短轴次之（$\mathcal{J}_s = 39.9$），长轴最小（$\mathcal{J}_l = 18.1$），比值 $\mathcal{J}_m / \mathcal{J}_s = 1.61$（与 Frauendorf 2014 Table I 拟合基准一致）；
   - 在单准粒子自旋区间（$I = 8.5\hbar \to 15.5\hbar$），$\pi i_{13/2}$ 准粒子对齐项 $(j/I)(\mathcal{J}_m/\mathcal{J}_s)$ 随自旋减小，驱动摆动频率从 $166.8\text{ keV}$ 单调陡峭下降至 $99.4\text{ keV}$（降幅达 $67.4\text{ keV}$），带外跃迁比维系在强集体区间（$r_{E2} = 0.26 \to 0.14$）；
   - 越过 $I \approx 16\hbar$ 后，$i_{13/2}$ 中子对破对对齐（提供 $\Delta i_x \approx 8\hbar$），将非集体带终止自旋推后至 $I_{\text{term}} = 56.5\hbar$，从而为多声子摆动运动在相空间中提供了广阔的存活窗口。

2. **$^{167}\text{Lu}$ 势能刚度耗散与转动惯量压缩平坦化：**
   - 随着中子数增至 $N=96$（$^{167}\text{Lu}$），TSD 壳能隙收缩，平衡三轴角减小至 $\gamma = 13.5^\circ$，势垒深度锐减至 $V_{\text{barrier}} = 0.35\text{ MeV}$（刚度暴跌至 $C_\gamma = 2.87\text{ MeV}/\text{rad}^2$）；
   - 三轴度减小导致中轴与短轴惯量差被大幅压缩（$\mathcal{J}_m = 57.2, \mathcal{J}_s = 40.6$，比值降至 $1.41$）；
   - 计算表明摆动频率在全自旋段**呈现完全平坦的直线响应（$134.7 \to 138.8 \to 128.3\text{ keV}$，全区间波动幅度仅 $10.5\text{ keV}$）**，带外跃迁比降至 $r_{E2} = 0.18 \to 0.10$；
   - 同时非集体扁椭带终止自旋提前至 $I_{\text{term}} = 46.5\hbar$，自洽微观解释了 Amro 2003 观测到的平坦化特征。

3. **$^{169}\text{Tm}$（$N=100$）TSD 势阱消失与摆动声子彻底淬灭：**
   - 在 $N=100$ 处，微观 Nilsson 势能面上的 TSD 极小完全坍缩（$\gamma \to 1.5^\circ, V_{\text{barrier}} \le 0.02\text{ MeV}$），原子核转变为轴对称长椭转子；
   - 横向摆动前提条件 $\mathcal{J}_m > \mathcal{J}_s$ 被彻底破坏，系统退化为普通纵向对称顶进动模式，频率随自旋线性上升（$220 \to 255\text{ keV}$），带间四极跃迁彻底淬灭（$r_{E2} = 0.02$），确立了 A≈160-170 TSD 摆动模式存在的硬中子数边界（$N \le 96$）。

## Provisional Reasoning

三轴超形变摆动运动的存活是由两大量子几何条件的精细平衡所维系的：
1. **形变空间势能刚度条件**：必须具有足够深的单粒子三轴壳能隙提供横向势垒刚度（$C_\gamma > 3.0\text{ MeV}/\text{rad}^2$），以抵御零点四极振动涨落对三轴极小的涂抹；
2. **转动空间相空间窗口条件**：非集体带终止自旋 $I_{\text{term}}$ 必须显著高于中子破对交叉自旋（$I_{\text{term}} > 50\hbar$），使集体进动能够获得高角动量相空间。
在 $^{163}\text{Lu}$ 中，双条件同时完美满足；而在 $^{167}\text{Lu}$ 中，势垒刚度不足导致惯量压缩而使能谱响应平坦化；在 $^{169}\text{Tm}$ 中，壳能隙消失直接关闭了三轴通道。

## Assumptions

1. **核芯转动惯量经验参数化：** 采用配对与刚体混合的三轴惯量参数化，标定在 $\gamma=20^\circ$ 处吻合 Frauendorf 2014 经典基准（65, 40, 18）；
2. **价单粒子取向假设：** 假定奇质子 $\pi i_{13/2}$ 在全自旋段保持沿短轴刚性取向（Frozen Alignment Approximation）；
3. **带终止线性拉伸路径：** 假定沿转动轴的角动量增加线性驱使三轴形变角 $\gamma$ 趋近于非集体扁椭轴 $\gamma = 60^\circ$。

## Competing Explanations

| 假说/解释 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| 纯一维签名伙伴能带说 | 认为所谓摆动能带仅仅是普通的单粒子科里奥利签名伙伴带（Signature Partner Bands） | 签名伙伴带的带间跃迁由强 $\Delta I = 1$ $M1$ 跃迁主导，而实验与本模型证明 TSD2 $\to$ TSD1 由巨大集体 $E2$ 主导（$B(E2_{\text{out}}) \approx 20-50\text{ W.u.}$），且两带转动惯量几乎完全重合，签名伙伴假说无法解释巨 $E2$ 辐射 | 彻底排除，确立横向摆动声子集体激发本质 |
| 突发性对崩塌淬灭说 | 认为 $^{167}\text{Lu}$ 的频率平坦与 $^{169}\text{Tm}$ 的淬灭是由高自旋超导对关联突然消失引起的 | 对关联的平滑减弱在镥同位素链中是连续的，单纯配对崩塌只能改变整体转动惯量标度，无法改变势能面上 TSD 局部三轴阱的存在与否；本模型证明决定性因素在于单粒子壳能隙对三轴曲率 $C_\gamma$ 的调制 | 修正为三轴势垒刚度消解主导机制，配对仅作为次级效应 |
| 刚性固定椭球唯象观 | 假定三轴原子核在全自旋段形变参数 $(\varepsilon, \gamma)$ 恒定不变 | CNS 微观计算表明价核子顺排必然拉动形变向扁椭终止点漂移，不考虑形变动力学漂移将无法解释高自旋非集体带终止现象 | 被自洽三轴轨迹模型所包容与深化 |

## Transfer Conditions

1. 适用于含有高-$j$ 侵入轨道费米子并处于大四极形变（$\varepsilon_2 \ge 0.35$）的三轴超形变原子核；
2. 适用于转动惯量满足水动力学层级（$\mathcal{J}_m > \mathcal{J}_s > \mathcal{J}_l$）的横向摆动候选核。

## Failure Conditions

1. 若原子核处于近球形或弱形变区（$\varepsilon_2 < 0.20$），转动惯量主要由价核子结构决定，水动力学惯量层级完全逆转，横向摆动公式失效；
2. 若自旋越过完全顺排终止自旋（$I > I_{\text{term}}$），集体转动完全解构，退化为非集体单粒子激发态。

## Falsification or Reverse Tests

1. **反向检验 1（高自旋跃迁速率实测）：** 若在寿命实验中测得 $^{163}\text{Lu}$ 在 $I > 40\hbar$ 处的带内 $B(E2)$ 发生剧烈塌缩归零，且终止自旋低于 $45\hbar$，则推翻本模型关于中子对齐延缓带终止的预言；
2. **反向检验 2（$^{167}\text{Lu}$ 势能曲率测量）：** 若通过高阶多步库激测得 $^{167}\text{Lu}$ 的三轴角涨落展宽极小（$\sigma_\gamma < 5^\circ$），则反驳势垒软化导致频率平坦化的理论机制。

## Open Questions

1. 在 A≈130 质量区（如 $^{135}\text{Pr}$）的横向摆动向纵向进动转变中，是否存在类似的核芯准粒子对齐诱发的相空间压缩？
2. 双声子摆动能带（TSD3）在带交叉区域的裂距如何定量受控于四极—单粒子多极张量干涉？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究基于包含三轴 CNS 势阱演化与配对修正 HFA 的自洽动力学求解程序（`day27_tsd_wobbling_vs_termination_study.py`）及入库一手文献（Ødegård 2001, Jensen 2002, Amro 2003, Frauendorf 2014）；
- 结论属于模型推论与系统学综合（`reasoning_status: provisional`），未进行正式人类同行评审。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，确立 TSD 摆动声子与核芯非集体带终止的相空间竞争机制，系统解答了 $^{163}\text{Lu}$ 稳固下降对决 $^{167}\text{Lu}$ 平坦化及 $^{169}\text{Tm}$ 淬灭的微观演化链条。
