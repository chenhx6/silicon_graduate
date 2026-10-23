---
type: source
title: "Zhao等2015：配对对核自旋取向的影响"
aliases: [Zhao 2015 pairing spin orientation, TAC-RHB blocking 2015]
created: 2026-10-15
updated: 2026-10-15
status: ai-draft
review_status: unreviewed
source_type: journal-article-theory-and-method
reading_depth: deep-read
title_original: "Impact of pairing correlations on the orientation of the nuclear spin"
authors: [P. W. Zhao, S. Q. Zhang, J. Meng]
journal: Physical Review C
year: 2015
volume: 92
pages: 034319
doi: 10.1103/PhysRevC.92.034319
arxiv: 1506.08340v2
language: en
canonical_source: "https://doi.org/10.1103/PhysRevC.92.034319"
citation_key: ""
raw_file: "raw/papers/2015-Zhao-pairing-spin-orientation-TAC.pdf"
raw_sha256: ce3c7672420b07e9bbe7d7a869049771c5cef9aa64f4dffce5dfd18bcb0b3c21
raw_storage_status: verified-raw-archive
raw_archive_verified_at: 2026-10-23
nuclei: [135Nd]
reactions: []
models: [tilted-axis-cranking, covariant-density-functional-theory, relativistic-Hartree-Bogoliubov]
observables: [excitation-energy, angular-momentum, B(M1), B(E2)]
methods: [monopole-pairing, quasiparticle-blocking, overlap-following]
tags: [a130, pairing, tac-cdft, blocking, reproducibility]
---

# Zhao等（2015）：配对对核自旋取向的影响

## Bibliographic Record

P. W. Zhao, S. Q. Zhang, J. Meng, Physical Review C **92**, 034319 (2015)，DOI [10.1103/PhysRevC.92.034319](https://doi.org/10.1103/PhysRevC.92.034319)。Crossref核到题名、三作者和2015-09-18；arXiv精确DOI命中[1506.08340v2](https://arxiv.org/abs/1506.08340v2)，其API题名少最后一个“spin”，而所读[公开PDF](https://arxiv.org/pdf/1506.08340v2)首页完整题名/作者与Crossref一致，边栏日期20 Sep 2015。当前locator均为此13页预印本，不冒充正式排版核验。

本次按daily-learning授权保存来源证据，**未完成raw归档摄入**。`raw_file`是不存在的保留槽；实际只读输入为`tmp/day14-20261014/tac2015/PDFs/Impact_of_pairing_correlations_on_the_orientation_of_the_nuclear_spin.pdf`，323292 bytes，SHA256如frontmatter。独立检查PDF magic/hash/首页身份，保留下载manifest、metadata和阅读回执。citation key未在本地Bib匹配，留空；raw/Bib均未改。

## Scope and Reading Depth

- **Covered scope**：全文13页；Introduction与动机、TAC-RHB框架、数值设置、p.5轨道追踪/阻塞段、Results、Summary和参考文献；视觉核p.4–5的公式/方法及Figs.1–5。没有独立table或appendix；所有影响判断的输入与图例已读。未请求SI。
- **Not covered**：实际RHB代码、U/V文件、λ/ω迭代步长、轨道追踪日志、相位和tie等实现约定、实验事件/响应/联合误差。上游实验原文未在本次重新全文读取；既有[[mukhopadhyay-2007-135nd-chiral-vibration-static]]只作为Wiki已存伴随证据校准，不增加新实验。
- 来源前回忆受Wang2017 Ref.[31]及既有HFB知识priming，量化前另冻结预测。全部ZT15 claims仍`needs_review: true`，本页`unreviewed`。

## Summary

论文把配对加入自洽TAC-CDFT/RHB，用135Nd的1qp与3qp yrast段检验配对如何改变角动量大小和取向。它给出了分别最大化O1/O2的准粒子追踪/阻塞规则，是Wang2017回指的直接方法来源。计算仅允许平面推转、回弯区结果省略；配对改善部分比较，但模型曲线和外部实验、既有chirality解释仍须分层。方法公式没有提供136Pr的真实阻塞清单。

## Problem, Motivation and Method

核心问题是：在倾斜转轴下，配对不仅改变集体惯量，还可能通过改变占据和单粒子混合重定向自旋。旋转系RHB方程同时处理正常场、配对场和`−ω·J`；作者用PC-PK1与由odd–even质量差确定的常数monopole配对，比较开/关配对。全文的“无额外参数”指这套选定计算，不能将其解释为不存在泛函、基空间、配对强度或电磁算符输入。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| ZT15-1 | TAC-RHB以hD−λ、推转项和Δ构成准粒子矩阵，自洽求正常/配对场；以`⟨J⟩·⟨J⟩=I(I+1)`作半经典I对应。 | theoretical-method | direct | PDF p.4 Eq.(1) | true |
| ZT15-2 | 135Nd采用νh11/2的1qp及耦合两πh11/2的3qp，PC-PK1、10主壳；monopole强度源文印Gn=.12、Gp=.13 MeV fm³，来自odd–even质量差。其定义不同于Wang2017的有限程G，不能直接比数值。 | model-input-and-scope | direct-and-contextual | PDF p.4 numerical-setting paragraph | true |
| ZT15-3 | 源文先以`ψu=U/sqrt(UᵀU)`、`ψv=V/sqrt(VᵀV)`分别归一，再分别最大化`O1=〈ψu,ψu′〉+〈ψv,ψv′〉`与`O2=〈ψu,ψv′〉+〈ψv,ψu′〉`，两者可选不同previous k′。 | theoretical-method | direct | PDF p.5 O1/O2 paragraph | true |
| ZT15-4 | 作者说明O1较大时取previous k1′的blocked状态；O2较大时按previous k2′的unblocked状态决定当前blocked，即交换分量分支需反转标记。 | theoretical-method | direct | PDF p.5 final blocking sentence | true |
| ZT15-5 | Fig.1给出声明频率下1qp/3qp Routhian的θ极小值，1qp偏l–i、3qp偏l–s；γ约22°和转轴方向均为模型结果。 | model-result | direct | PDF p.6 Fig.1 | true |
| ZT15-6 | I约10–14ℏ回弯区计算结果省略；3qp中proton pairing很弱，neutron gap从ω=.2时1.25 MeV降至ω=.6时1.14 MeV。 | model-result-and-failure | direct | PDF p.7 Fig.2 discussion | true |
| ZT15-7 | 配对既减小质子/中子角动量大小，又使两方向靠拢，后者可抵消前者对总J的影响；因此固定ω下J变化不宜只按单一惯量缩小理解。 | model-result-and-interpretation | direct | PDF p.8 Fig.3 discussion | true |
| ZT15-8 | Fig.4按N82参考分解135Nd的7个neutron holes为3个h11/2与4个gds；作者区分全valence hole贡献、一个unpaired h11/2 hole及canonical mixing，不能把qp简称当全部valence清单。 | model-result-and-input-boundary | direct-and-derived | PDF p.9 Fig.4 | true |
| ZT15-9 | 作者称135Nd配对后不再需过去统一.3的B(M1)衰减；Fig.5的配对B(M1)曲线仍高于若干高自旋实验点。未给联合χ²/Cov，不能把“good agreement”改写为逐点误差内吻合或通用无缩放结论。 | author-interpretation-and-plot-boundary | direct-and-derived | PDF p.10 Fig.5 | true |
| ZT15-10 | 本计算只允许xz平面转轴；p.8的chiral-vibration解释回引既有Ref.[10]。因此本文的l–i/l–s变化不构成直接算出的三维aplanar静态手征解或partner splitting。 | method-domain-and-author-interpretation | direct-and-derived | PDF p.4 xz-plane restriction | true |
| ZT15-11 | 公开O1/O2段未给可逐位重放的phase/magnitude、相等/并列最大值、零分量norm分支与迭代日志。本任务43-check实canonical/BdG控制说明这些约定影响字面following；不判实际作者实现错误。 | our-inference-and-readiness-boundary | derived | PDF p.5 O1/O2 paragraph | true |
| ZT15-12 | Fig.2能谱点回引Zhu2003 PRL91,132501，Fig.5强度点回引Mukhopadhyay2007 PRL99,172501；本工作是模型重用实验，不提供Pr136新采集或新增独立寿命证据。 | source-lineage | direct | PDF p.12 Ref.[15] | true |

## Competing Interpretations and Limitations

作者把1qp的集体转动与3qp的既有chiral-vibration解释联系起来；同时明确3qp矢量图也有shears-like外观。判定不能只看矢量靠拢：此处平面平均场不包含左右手量子隧穿或完整partner谱。既有[[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-6将实测band-resolved强度、TAC带内曲线和RPA带间曲线分开，本页不合并这些层级。

对“配对后无ad hoc因子”的限制包括选定核素/配对/算符与未给统计拟合；Wang2017另对109Ag讨论Dirac项修正，不能把两篇写成普遍矛盾或普遍无缩放。回弯区被省略、缺少代码和实际轨道日志，也阻止独立复跑或沿模型选择反推唯一组态。

## Counter-Evidence and Missing Companion Observables

必要伴随材料是actual U/V、occupied/blocked/reference、λ/ω路径与步长、相位及近简并处理、收敛与基空间检查，和被比较电磁量的具体跃迁/误差链。缺这些时，O1/O2只能定义方法框架。本文的135Nd valence/unpaired分层提供了一个明确例子，但不能填Pr136 Q1/Q1*的spectator。

若要讨论chirality，需独立partner-resolved强度、带间跃迁、能级关系和可计算波函数/波动；单一平面θ极小值不补这些实验与量子信息。

## Analytical Reconstruction

[[configuration-occupation-audit]]“O1/O2阻塞追踪的可重放契约”记录本任务43-check控制。声明`U=sqrt(.7)I`、`V=sqrt(.3)J`，J的两行分别为`(0,−1)`和`(1,0)`，满足canonical Bogoliubov条件，并构造E=±1的简并实BdG矩阵验证eigenbasis；same-state/O2交换分支可复现。整体qp符号改变保持ρ、κ和blocked广义密度，但按源式的signed字面读法会产生需要相位约定的结果；45°混合有并列最大值，零V使分开归一未定义。此处不是源实际旋转谱。

另外展示的abs-score与first-argmax都明确是本任务控制。abs可以解除这个符号反例，却不能唯一解45°近简并；不是已核作者算法或通用修复。没有从这些控制给实际核素定新blocking、number sector或程序错误。

## Related Knowledge and Project Relations

- `methodological-bridge` → [[configuration-occupation-audit]]：实际following所需输入/约定与组态简称分开。
- `foundational-background` → [[wang-2017-109ag-tac-separable-pairing]]：该文Ref.[31]的直接blocking定义来源；方法依赖不算独立Pr136实验。
- `limits` → [[tilted-axis-cranking]]：平面、半经典I、回弯和数据/模型层级边界。
- `not-direct-evidence` → [[a130-model-choice-card]]：改善replay contract，不增加Pr136真实输入或PSM/TPSM覆盖。

## Knowledge Impact and Learning Decision

Decision: **supports** 必须追踪准粒子身份、区分valence与unpaired；**revises** 把“largest overlap”当完整可复跑输入的读法。固化到本source、现有occupation/TAC页与model-choice卡；原Q1清单和263/405历史原因仍开放。没有新核素页、研究note或原始实验重分析。overview update deferred：当前补的是同一输入证据链，不需另建全库结论地图。

## Agent self-audit triage

- **P0: none identified**。公开源身份/hash已核，raw未归档明示。
- **P1 / ZT15-3、4、11**：p.5规则已回到原文；43-check只对声明实canonical/BdG控制和字面式成立。实际phase/tie/near-zero实现未得，不可称作者程序有误。
- **P1 / ZT15-9**：保留作者“good agreement”与Fig.5可见残差，不编χ²或误差覆盖。
- **P1 / ZT15-10、12**：xz限制、chiral-vibration上游解释和模型重用实验分开，不能把平面矢量图计新静态手征实证。
- **P2**：空citation key与raw保留槽随lint报告；不改Bib/凭据。

## Extracted Pages

- Methods: [[configuration-occupation-audit]]
- Models: [[tilted-axis-cranking]]
- Projects: [[a130-model-choice-card]]

## Provenance

- [Crossref](https://api.crossref.org/works/10.1103/PhysRevC.92.034319)及[arXiv PDF](https://arxiv.org/pdf/1506.08340v2)：metadata与本页科学locator。
- [阅读回执](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/tac2015-reading-audit.json)、[43-check量化](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/tac2015-blocking-following.json)、[程序](../../system/scripts/day14_tac_blocking_following.py)。
