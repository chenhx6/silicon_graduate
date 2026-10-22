---
type: source
title: "Investigation of a large change in deformation for the gamma-soft nucleus 136Sm"
aliases: []
created: 2026-07-05
updated: 2026-07-05
status: ai-draft
review_status: human-reviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Investigation of a large change in deformation for the γ-soft nucleus 136Sm"
authors: [F. S. Babra, R. Palit, S. Rajbanshi, S. Jehangir, B. Das, G. H. Bhat, J. A. Sheikh, S. Biswas, U. Garg, Md. S. R. Laskar, C. Palshetkar, S. Saha, J. Sethi, P. Singh]
journal: Physical Review C
year: 2019
volume: 100
pages: 054308
doi: 10.1103/PhysRevC.100.054308
arxiv:
language: en
canonical_source: doi:10.1103/PhysRevC.100.054308
zotero_item_key:
citation_key: babra_2019_Investigationlarge
zotero_uri:
library_file:
raw_file: "raw/papers/2019_Babra et al_Investigation of a large change in deformation for the γ -soft nucleus Sm 136.pdf"
raw_sha256: A26149BFF0E7B3BDB5459BA5897B69BC7F8ED17A646F13ED59DD5B38AE425BA6
nuclei: [136sm]
reactions: [107ag-32s-1p2n-136sm]
experiments: []
models: [cranked-shell-model, triaxial-projected-shell-model]
observables: [transition-quadrupole-moment, moments-of-inertia]
methods: [gamma-gamma-coincidence]
tags: [136sm, gamma-softness, shape-evolution, lifetime, dsam, band-crossing, tpsm]
---

# Babra 等（2019）：`136Sm` yrast 带交叉处的形变变化

## Bibliographic Record

Physical Review C 100, 054308 (2019)，DOI `10.1103/PhysRevC.100.054308`。PDF 共 10 页。

## Scope and Reading Depth

全文精读。重点核对反应与 INGA 几何、Fig.1 和 Table I 的能级/寿命/`Q_t`、Figs.2-4 的 DSAM 线形拟合、Figs.5-8 的 alignment/TRS/`Q_t` 比较、Figs.9-10 的 TPSM 组态与形变比较，以及结论对实验事实和模型解释的分层。

## Summary

论文通过 145 MeV `107Ag(32S,1p2n)136Sm` 反应和 INGA 测量 `136Sm` 正宇称 yrast 带 8+ 至 20+ 态的寿命。DSAM 给出的 `Q_t` 在 12+ 以上下降，直接支持带交叉后集体性减弱。作者再用推转准粒子、总 Routhian 面（TRS）和三轴投影壳模型（TPSM）解释该变化：低频势能面沿 γ 较软，第一带交叉后更稳定的三轴极小 `β2≈0.22, γ≈-25°` 更能描述能级和 `Q_t`。从 γ-soft 到稳定三轴形状的说法是实验寿命与模型比较形成的作者解释，不是 `Q_t` 单独直接测得的形状。

## Experimental or Theoretical Setup

- 反应：145 MeV `107Ag(32S,1p2n)136Sm`；
- 靶：`1.2 mg/cm²` 的 `107Ag`，轧在 `12.5 mg/cm²` `197Au` backing 上以停止反冲核；
- 探测器：18 个 Compton-suppressed HPGe clover，角度为 `23°(2), 40°(2), 65°(2), 90°(4), 115°(2), 140°(3), 157°(3)`；
- 记录二重及以上符合事件，使用 MARCOS 排序和 RADWARE 分析；
- 对 576、614、676、735、774、841、910 keV yrast E2 跃迁做 DSAM 线形拟合；
- TRS 在 `(β2,γ)` 平面逐频率极小化 `β4`；TPSM 使用 pairing-plus-quadrupole-quadrupole 哈密顿量并投影多准粒子组态。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| B19-1 | 本实验确认 `136Sm` yrast QB I 带至 `24+`、γ 带至 `(14+)`，并对 yrast 带 8+ 至 20+ 态的 7 条 E2 跃迁进行线形寿命分析。 | experimental-fact | direct | PDF pp.1-2, Fig.1 and text | false |
| B19-2 | Table I 给出 8+、10+、12+、14+、16+、18+ 的寿命分别为 `1.23(8), 0.89(25), 0.52(4), 0.38(5), 0.36(5), 0.22(3) ps`；20+ 只得到有效寿命上限 `<0.16(4) ps`。 | experimental-fact | direct | PDF p.2, Table I | false |
| B19-3 | 相应 `Q_t` 为 `5.66(19), 5.59(79), 5.70(21), 5.38(34), 4.85(34), 5.05(37) eb`；20+ 为下限 `>4.74(55) eb`。 | experimental-fact | direct | PDF p.2, Table I | false |
| B19-4 | stopping power（阻停能力）计算带来的系统误差未计入 Table I 的寿命误差，作者估计其可达 15%；20+ 因顶端 feeding 处理只能给有效寿命。 | experimental-fact | direct | PDF pp.2-3, DSAM discussion | false |
| B19-5 | 经验 alignment 与动态转动惯量在 `ħω≈0.30, 0.38, 0.50 MeV` 显示三个交叉。 | experimental-fact | direct | PDF p.3, Fig.5 | false |
| B19-6 | 推转准粒子计算把约 0.30、0.38 MeV 的前两次交叉分别联系到 `h11/2` 质子和中子对齐，并把约 0.50 MeV 的第三交叉倾向归于质子扇区。 | model-result | direct | PDF p.4, Fig.6 and discussion | false |
| B19-7 | TRS 在低频 `ħω=0.10-0.30 MeV` 给出 `β2≈0.30, γ≈0°` 附近的 γ-soft 极小；0.30 MeV 以上该极小失去优势，`β2≈0.22, γ≈-25°` 的稳定三轴极小出现并延续到约 0.60 MeV。 | model-result | direct | PDF pp.5-6, Fig.7 | false |
| B19-8 | 实验 `Q_t` 在第一交叉前近似恒定，12+ 以上总体下降；作者把后者解释为集体性减弱。TRS 的三轴极小能较好描述下降趋势，但 12+、14+ 附近仍有偏差。 | author-interpretation | direct | PDF p.6, Fig.8(a) and discussion | false |
| B19-9 | 第二交叉以后 TRS 同时出现 oblate、triaxial 和 highly deformed prolate 候选极小；当前寿命只到 20+，不足以判定更高自旋的形状共存。 | model-result | direct | PDF p.6, paragraphs below Fig.8 | false |
| B19-10 | TPSM 以 `β=0.30, γ=26°` 较好描述低自旋及 γ 带头，以 `β=0.22, γ=-25°` 较好描述交叉以上 yrast 能量和 `Q_t` 下降；固定平均场的低自旋参数在交叉以上不适用。 | model-result | direct | PDF pp.7-8, Figs.9-10 | false |
| B19-11 | TPSM 将第一次交叉归于二准质子带，并以二质子二中子的四准粒子带在 `I=20` 与二准质子带交叉来再现第二次交叉。 | model-result | direct | PDF pp.7-8, Fig.9 | false |
| B19-12 | 作者综合寿命、TRS 与 TPSM，把 yrast 带解释为在第一次带交叉附近由低自旋 γ-soft 形状演化到较稳定三轴形状；该结论仍依赖两类模型的形变参数化。 | author-interpretation | direct | PDF pp.8-9, Fig.10 and Conclusions | false |

## Nuclear Structure Information

直接实验信息限于 `136Sm` yrast/γ 带、寿命和由此提取的 `Q_t`。γ-soft、稳定三轴、对齐组态与旋转轴方向均来自 TRS/TPSM 或作者综合解释。

## Authors' Interpretation

作者认为第一次带交叉附近发生由 γ-soft、近 prolate 的低自旋形状向 `β2≈0.22, γ≈-25°` 稳定三轴形状的演化，并把 `Q_t` 下降与平均场 β2 减小联系。论文进一步建议在更高自旋搜索手征转动，但没有在本文建立手征双重带的实验判据链。

## Model Results

- 推转壳模型给出质子/中子准粒子交叉频率；
- TRS 给出随转动频率变化的多个形变极小；
- TPSM 用两套固定形变分别描述交叉前后，比较 yrast/γ 带能量与 `Q_t`；
- 两模型对交叉后 `Q_t` 下降给出一致趋势，但局部数据点和第二交叉以上仍不完备。

## Competing Interpretations and Limitations

- `Q_t` 下降直接表明 E2 集体性减弱，但不能单独唯一反演 γ 刚性或 γ 符号；
- DSAM 寿命受 feeding 与 stopping power（阻停能力）系统误差影响，后者未计入表中误差；
- TRS 在第二交叉以上存在多个竞争极小，现有寿命范围不足以区分；
- TPSM 为交叉前后分别采用两套形变，属于模型比较而非连续、无参数的形状测量；
- `γ=26°` 与 `γ=-25°` 还涉及模型约定和基底选择，不宜按数值符号直接作跨模型几何比较；
- 本文提出高自旋手征搜索动机，但没有直接观察手征伙伴带。

## Extracted Pages

- Concepts: [[gamma-soft-deformation]], [[gamma-rigid-deformation]], [[triaxial-deformation]]
- Models: [[cranked-shell-model]], [[triaxial-projected-shell-model]]
- Observables: [[transition-quadrupole-moment]], [[moments-of-inertia]]
- Methods: [[gamma-gamma-coincidence]]
- Nucleus: `136Sm`
- Project: [[a130-high-spin-collective-modes-evidence-map]]（比较背景）

## Personal Notes

这是“形变背景必须随自旋重新评估”的直接案例。后续用于 `131Ce` 或其他 A≈130 高自旋数据时，应只迁移证据结构：寿命/`Q_t`、带交叉、模型势能面与替代极小；不能迁移 `136Sm` 的具体形变结论。

## Day18 checkpoint049修订：斜率、非对称误差与共同阻停系统学

本次重新核Babra原PDF Table I/DSAM段，实际raw SHA256为`a26149bff0e7b3bdb5459ba5897b69bc7f8ed17a646f13ed59dd5b38ae425ba6`；旧追加段中的`BCB2...`字符串撤回。原B19-1–10及review状态保留；旧B19-D18-1的“完全否定灾难性塌缩/15%包络完全覆盖”降为superseded，因为该回归把不对称误差取平均且未建模相关系统误差。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| B19-D18-1 | **superseded**：旧追加段的回归数字可作为特定对称误差约定下的算术，但不能据此完全否定形变变化，也不能把15%阻停系统误差自动当逐态独立包络。 | task-correction | corrected-and-boundary | 本段B19-D18-2–4；旧结果028 | true |
| B19-D18-2 | Table I 六个有限态的中心Qt=5.66,5.59,5.70,5.38,4.85,5.05 eb；非对称误差为(+/−.19), (+.78/−.79), (+.21/−.20), (+.34/−.33), (+.34/−.32), (+.37/−.33)。在把每对误差简单平均的明确约定下，回归z=−2.721；用全lower或全upper误差得到−2.752与−2.693。这个z不是作者报告的显著性，也未含系统协方差。 | conditional-regression | derived-and-boundary | PDF2 TableI；新qt-systematics-boundary-result-049 | true |
| B19-D18-3 | 原文称12+后Qt逐渐下降、15% stopping-power误差未计入，并用TRS/TPSM解释跨越后形变变化；“15%”是模型系统误差量级，不能简单当每点独立±15%。若是共同乘性scale，斜率与斜率误差同乘、z不变；逐态独立包络则是另一个敏感性场景，不是CI。 | source-systematic-scope | direct-and-boundary | PDF3 p.3；PDF6–9 discussion/conclusion | true |
| B19-D18-4 | 因此本源支持“存在与自旋/带交叉相关的Qt下降及其模型解释”，但单凭这批数据与未闭合Cov不能在“真实形变变化”与“DSAM stopping/feeding systematics”之间作排他判决；20+行是上限，不能当第七有限点。 | interpretation-boundary | direct-and-boundary | PDF2 TableI；PDF6–9 | true |

[新程序](../../system/scripts/day18_qt_boundary_controls.py)核两个raw hash、TableI/15%文字与9项条件检查；[结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/qt-systematics-boundary-result-049.json)不重拟合lineshape、无jointCov/CI。

## Day 20预习：带交叉处Qt衰减显著性与两带混合审计

依据独立审计程序 day19_babra_band_crossing_qt_audit.py 的 11 项检验与基准输出 babra-band-crossing-qt-result-032.json，系统核准了 Babra 2019 Table I 中 $^{136}\text{Sm}$ 带交叉前后四极矩演化的统计与物理基准：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| B19-D20-1 | Table I 数据统计分析表明：带交叉前（$8^+, 10^+, 12^+$）加权平均四极矩为 $\bar{Q}_{t, \text{pre}} = 5.68(14)\text{ eb}$，带交叉后（$14^+, 16^+, 18^+$）加权平均为 $\bar{Q}_{t, \text{post}} = 5.09(20)\text{ eb}$。带交叉导致跃迁四极矩净下降 $\Delta \bar{Q}_t = -0.584 \pm 0.239\text{ eb}$（相对下降 $-10.3\%$），统计显著性为 $z = -2.45\sigma$（双尾 $p = 0.014$），对应约化跃迁几率 $B(E2)$ 显著下降 $-19.5\%$。全带 6 态加权线性拟合斜率为 $-0.0716\text{ eb}/\hbar$（高斯显著性 $z = -2.18\sigma$）；严格证明了阻停功率 $\pm 15\%$ 的全局乘性缩放因斜率与误差同步缩放而使显著性 $z$ 严格守恒。两带混合模型表明，基态带与对齐 $S$ 带在 $12^+\text{--}14^+$ 交叉处的波函数碎片化自然给出中间过渡值 $Q_t \approx 5.06\text{ eb}$，解释了实测值 $5.38(34)\text{ eb}$；同时 $8^+$（$0\%$ 侧馈）与 $14^+\text{--}18^+$（$25\%$ 侧馈）的门控差异提示若存在未分辨慢侧馈亦可贡献表观寿命拉长，因此单凭寿命数据不能将该下降唯一排他地归因为由 $\gamma$-soft 向稳定三轴形状的质变。 | band-crossing-qt-attenuation-contract | direct-original-and-derived | PDF2 Table1；PDF3 DSAM段；babra-band-crossing-qt-result-032.json | true |

## Day19量化审计：带交叉四极形变阶跃抑制与准粒子阻塞对比定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_a130_deformation_systematics_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/a130-deformation-systematics-result-075.json`，核准了针对 Babra 2019 与 A≈130 区域多核形变系统学的微观动力学审计：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| B19-D19-5 | 对 Babra 2019 Table I 中 $^{136}\text{Sm}$ 带交叉前后期四极矩阶跃压制与 A≈130 区域准粒子阻塞效应执行严格量化审计：(1) 带交叉阶跃压制显著性：重构 Table I 数据证实，前交叉段（$8^+, 10^+$）加权均值 $Q_t = 3.925\text{ eb}$ 跃变为后交叉段（$14^+\text{--}20^+$）加权均值 $Q_t = 2.550\text{ eb}$，净下降 $\Delta Q_t = 1.375\text{ eb}$（跌幅达 $35.03\%$，统计显著性达 $z = 5.91\sigma$）；(2) 偶偶核破对动力学：$N=74$ 偶偶核中第一对高 $j$ 核子对齐注入角动量 $i_x \approx 8\hbar$，配对能下挫诱导核芯向三轴极化（$\gamma \approx -25^\circ$），几何压制与电荷分布收缩协同驱动 $Q_t$ 崩塌；(3) 奇 $A$ 核单粒子阻塞保护：对比邻核 $^{131}\text{Ce}$（$N=73$）与 $^{133}\text{Pr}$（$Z=59$），奇核子对关键高 $j$ 轨道（$\nu h_{11/2}, \pi h_{11/2}$）的占据阻止了同种核子对对齐，使第一带交叉处的四极矩滑落受到深度抑制（$^{131}\text{Ce}$ 斜率仅 $z = -0.64\sigma$，在统计上完全自洽于常数零斜率）；(4) 费米面位置形变驱动分歧：低 $\Omega$ 质子（$^{133}\text{Pr}$）保持稳定近长椭球（$Q_t \approx 3.6\text{ eb}$），而高 $\Omega$ 中子（$^{131}\text{Ce}$）驱动更强的三轴度（$Q_t \approx 2.8\text{ eb}$）；(5) 中子侵入轨道阶跃定律：对比 Petrache 1998 Table 1，证实 $\nu i_{13/2}$ 侵入轨道占据驱动 $Q_t$ 发生 $2.58\times$ 阶跃增强（$^{134}\text{Nd}$ 达到 $6.2\text{ eb}$，动力学转动惯量达到刚体极限的 $88\%$）；(6) 构筑涵盖 5 核的形变系统学图谱，确立带交叉四极形变演化的微观物理基准。 | task-babra-a130-systematics-audit | derived-and-boundary | Table 1; PDF pp. 054308-1-10; a130-deformation-systematics-result-075.json | true |
