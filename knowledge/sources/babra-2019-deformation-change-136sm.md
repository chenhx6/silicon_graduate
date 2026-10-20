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

## Day18定量审计：高自旋Qt拟合斜率显著性与15%阻停系统误差带

在Day18正式学习中对本文Table I中136Sm yrast带8+至18+态的DSAM寿命与跃迁四极矩Qt进行加权回归与系统误差包络审计，raw SHA256 `BCB2D8534C15A7091B87EE496DAFE59DC5D1EB4ED627340D83B094CC2088FE37`已核。原B19-1–10各claim及`human-reviewed`状态完全保留；新B19-D18-1待审。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| B19-D18-1 | 本文Table I报告136Sm基态带8+至18+态的Qt从5.66(19) eb演化至5.05(37) eb。定量审计证实：(1) 六个有限态的加权平均Qt为5.483(112) eb，常数Qt模型的卡方chi2/dof仅为7.31/5 = 1.46，完全否定了早期文献宣称的形变灾难性塌缩至beta2 ~ 0.14（Qt ~ 3.2 eb）的猜想；(2) 线性回归斜率为dQt/dI = -0.0716(263) eb/hbar，显著性仅为-2.72sigma，属于温和下降；(3) 正文p.3估计未计入的阻停本领系统误差达15%（对应+/-0.822 eb包络），该系统误差带完全覆盖了高自旋Qt的微弱变动。因此，136Sm在第一与第二交叉区间总体保持了高四极集体性，未发生剧烈形状猝灭。 | task-rate-decomposition-audit | derived-and-boundary | PDF p.2 Table I；新babra19-singh16-qt-result-028 | true |

新[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/babra19-singh16-qt-contract-028.json)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/babra19-singh16-qt-result-028.json)4项检查全过。
