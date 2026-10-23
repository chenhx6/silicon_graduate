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

## Day20定向原读与checkpoint004混合认证撤回

依据独立审计程序 `system/scripts/day20_band_mixing_qt_audit.py` 与基准输出 `outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02/band-mixing-result-005.json`，旧004声称严格认证，现撤回。此时本session实际新读范围仅PDF2的TableI/DSAM段与PDF3命中行，未完成新10页全文/关键图视觉。旧human-reviewed字段指旧审核事件，本次不借其扩大新scope，也不更改原flags。007只校正新引入的算术/归因错误：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| B19-D20-F01 | checkpoint007撤回004的精确混合认证：原005JSON在声明qg=5.675780、qs=4.95、theta14=26.5deg、theta12=0和零interband intrinsic元时，实际给5.079451eb，不是5.38或零残差；纯末态还使qs不进入此矩阵元。pre/post平均−.584eb与z≈−2.45只是独立、对称化误差的分段诊断，不是作者实验CI或机制判决。任意指定角可匹配一个中心，不证明136Sm真实混合，更不证明静态收缩已被排除。 | conditional-mixing-correction | task-derived-and-boundary | PDF2 Table I; mixing-response-result-007.json | true |

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
| B19-D18-2 | checkpoint039区分误差合同：六点中心与上下误差仍如原表；平均上下误差/已知独立Gaussian z−2.178812，全lower/upper为−2.258052/−2.105708。旧−2.721及−2.752/−2.693来自残差缩放未知共同尺度合同，应为Student统计量而非Gaussian z；本轮只复算平均误差的t(df4)，所有诊断非原实验CI。 | conditional-regression | derived-and-boundary | PDF2 TableI；新qt-systematics-boundary-result-049 | true |
| B19-D18-3 | 原文称12+后Qt逐渐下降、15% stopping-power误差未计入，并用TRS/TPSM解释跨越后形变变化；“15%”是模型系统误差量级，不能简单当每点独立±15%。若是共同乘性scale，斜率与斜率误差同乘、z不变；逐态独立包络则是另一个敏感性场景，不是CI。 | source-systematic-scope | direct-and-boundary | PDF3 p.3；PDF6–9 discussion/conclusion | true |
| B19-D18-4 | checkpoint039更正限值方向：20+ τ<.16(.04)ps是有效寿命上限，但Qt>4.74(.55)eb是下限，非第七有限点。原文支持Qt随spin/交叉变化及TRS/TPSM形变解释；未得完整Cov与响应，不能在形变演化、mixing、stopping/feeding之间作本任务排他判决。 | interpretation-boundary | direct-and-boundary | PDF2 TableI；PDF6–9 | true |

[新程序](../../system/scripts/day18_qt_boundary_controls.py)核两个raw hash、TableI/15%文字与9项条件检查；[结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/qt-systematics-boundary-result-049.json)不重拟合lineshape、无jointCov/CI。

## Day 20预习：带交叉处Qt衰减显著性与两带混合审计

依据独立审计程序 day19_babra_band_crossing_qt_audit.py 的 11 项检验与基准输出 babra-band-crossing-qt-result-032.json，系统核准了 Babra 2019 Table I 中 $^{136}\text{Sm}$ 带交叉前后四极矩演化的统计与物理基准：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| B19-D20-1 | checkpoint039保留声明独立对称化pre/post诊断：5.67578→5.09205、差−.583735±.238561eb、z−2.44690；已知误差全线z−2.178812与残差缩放t−2.721(df4)分开。原007已反驳精确混合重现5.38；统一stopping免疫/机制完全解释认证撤回。TRS/TPSM作者形变解释保留且有模型依赖。见B19-D20-R39-1/R39-2。 | band-crossing-qt-attenuation-contract | direct-original-and-derived | PDF2 Table1；PDF3 DSAM段；babra-band-crossing-qt-result-032.json | true |

## Day19量化审计：带交叉四极形变阶跃抑制与准粒子阻塞对比定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_a130_deformation_systematics_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/a130-deformation-systematics-result-075.json`，核准了针对 Babra 2019 与 A≈130 区域多核形变系统学的微观动力学审计：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| B19-D19-5 | superseded：旧3.925→2.550eb与z5.91没有TableI支持，继续撤回。新pre/post5.676/5.092eb及其误差只能作明确独立对称化控制，不能升级为原实验CI。004“20%混合精确重现5.38”又被007数值反证；原TableI/原review与原flags保持。 | task-correction | corrected-and-boundary | Table I; B19-D20-F01 | true |

### checkpoint039：跨带比较与统计合同原件纠正

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| B19-D20-R39-1 | 六有限点平均上下误差/独立已知Gaussian的全线斜率−.0716484±.0328842、z−2.178812；残差估共同尺度t≈−2.721(df4)，非Gaussian z。固定pre8–12/post14–18的均值差−.583735±.238561、z−2.44690仅条件诊断，非作者CI/因果判决；均值Qt比平方不是不同跃迁总B变化。 | declared-statistical-model-comparison | original-and-conditional | PDF2 TableI; task crossband-attribution-result-039.json | true |
| B19-D20-R39-2 | 20+ τ<.16(.04)ps而Qt>4.74(.55)eb：有效寿命上限、Qt下限。原top100%feeding/8+upper gate/higher25%与15%stopping预算保留；TRS/TPSM作者γ-soft至较稳定三轴解释不被任意混合反例排除，不能据此识别真实混合概率。 | literal-limits-and-model-boundary | original-and-conditional | PDF2 TableI/DSAM; PDF3 stopping paragraph; PDF6–9 models/conclusions | true |


## Day20量化审计：136Sm带交叉形变演化、两带混合与限值反转审计（checkpoint136）

> checkpoint146：本节科学认证撤回。旧文本与指纹保存在history-before-repair-146.json。先前原件纠错与原review/flags保留；passed不认证实际实验/结构结论。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| B19-D20-R136-1 | checkpoint146撤回旧认证；同态/分支/几何/单位与Cov未逐claim重审之前，不恢复旧数据及过强推论。 | withdrawn-task-certification | rejected-and-replaced | checkpoint146; history-before-repair-146.json | true |
