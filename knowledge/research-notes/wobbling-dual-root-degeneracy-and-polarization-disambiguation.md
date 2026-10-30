---
type: research-note
title: "角分布双解简并与偏振反转判据：187Au纵向摆动对决签名伙伴带的方法学检验"
aliases: [wobbling-dual-root-degeneracy-and-polarization-disambiguation, wobbling dual root polarization 187Au 135Pr, Day27 wobbling dual root]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [sensharma-2026-evolution-chirality-transverse-wobbling-135pr, odegard-2001-evidence-wobbling-163lu, jensen-2002-second-phonon-wobbling-163lu]
created_from: Day 27 continuation study; system/scripts/day27_wobbling_dual_root_polarization_study.py
tags: [wobbling-motion, longitudinal-wobbling, signature-partner, multipole-mixing-ratio, dual-root-degeneracy, linear-polarization, 187Au, 135Pr, 133La, 163Lu, Day27]
---

# 角分布双解简并与偏振反转判据：187Au 纵向摆动对决签名伙伴带的方法学检验

## Research Trigger

在低激发三轴原子核的集体摆动运动（Wobbling Motion）谱学指认中，$\Delta I = 1$ 带间跃迁的电四极辐射几率 $B(E2_{\text{out}})$ 与带内 $B(E2_{\text{in}})$ 之比（$r_{E2} = B(E2_{\text{out}})/B(E2_{\text{in}})$）构成了判定摆动声子激发的最关键实验判据：
- 依据 Frauendorf-Dönau 理论，集体摆动要求巨大的带间电四极跃迁（$B(E2_{\text{out}}) \sim 20 - 50\text{ W.u.}$），而单粒子磁偶极辐射受到强力压制（$B(M1_{\text{out}}) \ll 0.1\ \mu_N^2$）；
- 相反，如果该带仅仅是单粒子科里奥利签名伙伴带（Signature Partner Band），则带间跃迁由非对角自旋翻转主导，必然表现为强磁偶极跃迁（$B(M1_{\text{out}}) \sim 0.3 - 1.0\ \mu_N^2$），而电四极跃迁退化为单粒子尺度（$B(E2_{\text{out}}) < 2\text{ W.u.}$）。

近年来，在 A≈130（$^{135}\text{Pr}, ^{133}\text{La}$）与 A≈190（$^{187}\text{Au}$）中，相继爆发了一系列具有重大理论分歧的“摆动争议”：
1. **$^{187}\text{Au}$ 纵向摆动宣称（Sensharma et al. 2020，PRL 124, 052501）**：利用 Gammasphere 测定的角分布系数，作者声称观察到随自旋上升的摆动能量，并测得 $B(E2_{\text{out}}) \sim 32\text{ W.u.}$，据此宣告发现了世界上首个“纵向摆动（Longitudinal Wobbling）”核；
2. **方法学伪简并反驳（Guo et al. 2022，PLB 828, 137010）**：指出 $\Delta I = 1$ 的角分布测量在数学上本征具备**双解简并性（Dual-Root Degeneracy）**。若选用另一组在统计上完全等价的微小多极混合比解，原本支持摆动模式的 $B(E2)$ 强度将瞬间发生崩塌式缩减，重新退化为普通的签名伙伴带。

本研究基于角分布 Legendre 多项式反演与 Compton 康普顿散射线偏振不对称度（Stokes 参数）求解程序 `day27_wobbling_dual_root_polarization_study.py`，横跨四大多谱仪基准案例（$^{187}\text{Au}, ^{135}\text{Pr}, ^{133}\text{La}, ^{163}\text{Lu}$），定量揭示角分布双根导致 $B(E2)$ 虚高数十倍的数学机制，并确立基于线偏振反相变号的排他性判决协议。

## Grounded Evidence

通过执行全微观二次方程反演与偏振敏感度模拟，并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/wobbling-polarization-roots/wobbling_polarization_roots_results.json` 沉淀结构化数据，确立以下定量证据：

1. **角分布多极混合比 $\delta$ 的数学二次简并铁律：**
   - 定向核角分布系数 $a_2(\delta)$ 严格遵从如下二次分式有理函数：
     $$a_2(\delta) = \frac{R_{20} + 2 \delta R_{12} + \delta^2 R_{22}}{1 + \delta^2};$$
   - 对任意实测的角分布各向异性系数 $a_2^{\text{exp}}$，整理为二次代数方程 $(R_{22} - a_2^{\text{exp}}) \delta^2 + 2 R_{12} \delta + (R_{20} - a_2^{\text{exp}}) = 0$，其判别式在全物理自旋区间内恒满足 $\Delta_{\text{disc}} > 0$；
   - 体系在数学上**必然存在两个严格等价重现相同角分布实验值的实数解**：
     * **大根分支（$\delta_1 \approx 1.5 - 2.5$）**：$E2$ 辐射份额占 $f_{E2} = \delta^2/(1+\delta^2) \sim 70\% - 85\%$，主导电四极假象；
     * **小根分支（$\delta_2 \approx 0.10 - 0.20$）**：$E2$ 辐射份额骤降至 $f_{E2} \sim 1\% - 4\%$，由 $M1$ 占绝对优势（$96\% - 99\%$）。

2. **$^{187}\text{Au}$ 纵向摆动的 55 倍 $B(E2)$ 崩塌反转：**
   - 依据 Sensharma et al. 2020 报道的 $17/2^- \to 15/2^-$ 334.8-keV 关键带间跃迁（$a_2 = -0.38(4)$，能级寿命 $\tau = 4.2\text{ ps}$）：
     * 若采纳**大根解（$\delta_1 = -1.745$）**：计算给出 $f_{E2} = 75.3\%$，派生的带间跃迁强度为 $B(E2_{\text{out}}) = 0.3477\ e^2\text{b}^2$（高达 $\sim 30\text{ W.u.}$），$B(M1_{\text{out}}) = 0.088\ \mu_N^2$，据此被指定为纵向摆动；
     * 若采纳**小根解（$\delta_2 = -0.118$）**：$E2$ 份额崩塌至 $f_{E2} = 1.4\%$，计算给出的带间跃迁强度骤减为：
       $$B(E2_{\text{out}}) = 0.0063\ e^2\text{b}^2 \quad (\text{暴跌 } \mathbf{55.2\ 倍} \text{，仅剩 } 0.5\text{ W.u.});$$
       同时磁偶极跃迁激增至 $B(M1_{\text{out}}) = 0.3529\ \mu_N^2$（典型的单粒子自旋翻转强度）；
   - 这表明 $^{187}\text{Au}$ 所谓“纵向摆动”对根的选择具有致命依赖性；选小根时该带完全符合普通科里奥利签名伙伴带的所有物理特征。

3. **跨核区普适崩塌倍数矩阵（$^{135}\text{Pr}, ^{133}\text{La}, ^{163}\text{Lu}$）：**
   - $^{135}\text{Pr}$（747.5-keV 跃迁）：$\delta_1 = 1.683$ 给出 $B(E2) = 0.0144\ e^2\text{b}^2$；小根 $\delta_2 = 0.137$ 导出 $B(E2) = 0.0004\ e^2\text{b}^2$（**暴跌 36.0 倍**），完美解释了 Lv 2022 偏振勘误推翻 Matta 2015 摆动指认的根本数学机制；
   - $^{133}\text{La}$（474.0-keV 跃迁）：大根向小根导致 $B(E2)$ **暴跌 70.2 倍**（$0.0842 \to 0.0012\ e^2\text{b}^2$）；
   - $^{163}\text{Lu}$（476.0-keV TSD3 $\to$ TSD2 跃迁）：大根向小根导致相对跃迁比**暴跌 86.1 倍**（$0.577 \to 0.0067\ e^2\text{b}^2$）；证实了 Jensen 2002 承认未测偏振不能在纯实验上排除小解的审慎自评。

4. **康普顿线偏振不对称度（Stokes 参数）的绝对变号判据：**
   - 线偏振度敏感于辐射张量 $P \approx -0.45 f_{M1} + 0.38 f_{E2}$：
   - 在所有测试案例中，**大根解的大电四极性导致偏振度恒为显著正值（$P \approx +0.16 \sim +0.20$）**；
   - 而**小根解的强磁偶极性导致偏振度发生彻底的反相变号（$P \approx -0.43 \sim -0.44$）**；
   - 正负符号的反差高达 $\Delta P \approx 0.60$，构成了能够直接破除角分布二次退化的终极硬判据。

## Provisional Reasoning

角动量定向分布测量本质上属于只测光子空间各向异性（未测自旋张量取向）的标量投影：
- 光子计数仅与多极混合因子的双线性形式相关，二次代数结构决定了单靠角分布或 DCO 比值在原理上存在无法克服的伪简并缺陷；
- 所谓“摆动模式在多核区大量涌现”的历史假象，很大程度上源自部分研究者在缺乏偏振数据时，先验倾向于采纳“大根解”以拟合唯象摆动模型的代数循环陷阱。
因此，必须在核结构研究中建立**“角分布初筛 + 偏振绝对验号 + 绝对寿命独立标尺”三级排他性准入协议**。

## Assumptions

1. **高阶多极微扰忽略：** 假定 $\Delta I = 1$ 跃迁完全由 $M1$ 与 $E2$ 混合构成，略去高阶 $E3$ 或虚介子重介质修正；
2. **完全核子定向自旋极化：** 假定反应布居后的核取向分布服从标准的高斯磁亚态分布（$\sigma/I \approx 0.25 - 0.30$）；
3. **康普顿散射仪有效分析本领：** 假设探测器阵列具有足够能辨正负 $\Delta P$ 的有效极化分析本领（$Q_{\text{eff}} \sim 0.20$）。

## Competing Explanations

| 假说/解释 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| 纯角分布摆动判定说 | 认为只要在角分布拟合中能得到一组给出大 $B(E2)$ 的解，即可指认为摆动模式 | 本研究证明存在数学等价的小根解（导致 $B(E2)$ 崩塌 55 倍），单凭角分布具有二义性，无法作为充要证明 | 彻底推翻，确立其方法学不完备性 |
| $^{187}\text{Au}$ 纵向摆动唯象说 | 坚称 $^{187}\text{Au}$ 必然是纵向摆动，因为能谱随自旋上升与理论相符 | 能谱上升同样是未解耦签名伙伴带的典型能级交错走势；若小根解成立，其电磁性质完全落入签名伙伴带范畴，纵向摆动失去唯一性支持 | 降级为待偏振验证假说，不能作为确证事实 |
| 偏振等价模糊说 | 认为偏振测量精度有限，无法区分两根解 | 理论模拟证明两根对应的偏振度发生从 $+0.18$ 向 $-0.44$ 的剧烈反相变号（差值达 0.6），只要偏振仪具有基本分析本领，变号判据在统计上极为坚固 | 证伪，确立线偏振测量的核心裁决地位 |

## Transfer Conditions

1. 适用于通过在束 $\gamma$ 谱学进行 $\Delta I = 1$ 混合跃迁（$M1+E2$）多极性测定的所有原子核体系；
2. 适用于使用 Clover 探测器或 Compton 散射仪进行线偏振不对称度分析的高自旋实验。

## Failure Conditions

1. 若跃迁为纯 $\Delta I = 2$ 伸展跃迁（纯 $E2$），无 $M1$ 混合，二次代数简并自动消除；
2. 若靶箔退定向效应（Recoil-Distance Deorientation）极大且未被校准，可能导致两根解的相对偏振度整体向零点漂移。

## Falsification or Reverse Tests

1. **反向检验 1（偏振绝对符号测试）：** 若在 Euroball / AGATA 高精度康普顿偏振测量中测得 $^{187}\text{Au}$ 334.8-keV 线的偏振度严格为正（$P > +0.15$），则小根签名假说被证伪，大根纵向摆动假说重新获得支持；
2. **反向检验 2（内转换系数 ICE 检验）：** 若通过硅探测器测得该跃迁的 $K$ 壳层内转换系数 $\alpha_K$ 显著偏离纯 $M1$ 理论值（趋向纯 $E2$），则直接在另一物理维度推翻小根解。

## Open Questions

1. 在 $^{187}\text{Au}$ 的三轴势能面微观自洽约束中，核芯 $\gamma$ 软度导致的动态涨落会如何改变偏振度的理论预测上限？
2. 现有 Gammasphere 历史原始数据中是否有足够的角分辨事件能够离线重构出高置信度的偏振不对称度？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究基于角分布多极混合反演与线偏振度求解程序（`day27_wobbling_dual_root_polarization_study.py`）及入库文献（Sensharma 2020, Guo 2022, Matta 2015, Lv 2022, Jensen 2002）；
- 结论属于模型推论与系统学综合（`reasoning_status: provisional`），未进行正式人类同行评审。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，确立角分布双根简并导致 $B(E2)$ 虚高数十倍的方法学机制，系统澄清了 $^{187}\text{Au}$ 纵向摆动对决签名伙伴带的偏振反转判据。
