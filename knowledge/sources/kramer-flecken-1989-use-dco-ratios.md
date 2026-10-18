---
type: source
title: "Use of DCO Ratios for Spin Determination in gamma-gamma Coincidence Measurements"
aliases: [Kramer-Flecken 1989 DCO, Kramer-Flecken 1989 use of DCO ratios, DCO spin determination OSIRIS]
created: 2026-07-12
updated: 2026-10-18
status: ai-draft
review_status: human-reviewed
source_type: experiment-method-article
reading_depth: read
title_original: "Use of DCO Ratios for Spin Determination in gamma-gamma Coincidence Measurements"
authors: [A. Kramer-Flecken, T. Morek, R. M. Lieder, W. Gast, G. Hebbinghaus, H. M. Jager, W. Urban]
journal: Nuclear Instruments and Methods in Physics Research Section A
year: 1989
volume: 275
number: 2
pages: 333--339
doi: 10.1016/0168-9002(89)90706-7
language: en
canonical_source: doi:10.1016/0168-9002(89)90706-7
citation_key: kramer-flecken_1989_UseDCO
raw_file: "raw/papers/1989_Krämer-Flecken et al_Use of DCO ratios for spin determination in γ-γ coincidence measurements.pdf"
raw_sha256: 30CDF474DB5FBFAA6A27F6D2E0D11EA39BBB61A05C8153E740F2F3DCCA52220F
nuclei: []
reactions: []
observables: [multipole-mixing-ratio]
methods: [dco-ratio, angular-correlation, spin-parity-assignment]
tags: [dco, angular-correlation, spin-assignment, geometry, alignment, gamma-spectroscopy]
---

# Kramer-Flecken et al. (1989): Use of DCO Ratios

## 2026-10-17使用更正：实验DCO分式

**当前使用以KF89-9为准。** 原件printed334的理论式与实验式彼此一致；旧Wiki KF89-1把实验强度分式转写成了倒数。正确原式是`I_(theta1)^gamma2(Gate_(theta2)^gamma1) / I_(theta2)^gamma2(Gate_(theta1)^gamma1)`：gamma1为门、gamma2为待测线，W的第一角参数是门角。不能把原文只当一个无标签的theta交换式使用。

原有page级`human-reviewed`及KF89-1–8的flag/文字保留原审核历史，**不扩张到本次更正**；KF89-1的旧实验分式已被本节明确supersede，不能继续单独引用。新KF89-9–14及本节是Codex原件self-audit、`needs_review: true`，不是人审记录。原PDF身份/哈希不变。

同理，原件low-spin边界I≤6与旧摘要I<6、width措辞及generic mixed pair的适用条件分别由KF89-13/14注明；不要用旧审核标签抹掉本次明确的原件边界。

## Bibliographic Record

A. Kramer-Flecken et al., *Nuclear Instruments and Methods in Physics Research Section A* **275**(2), 333--339 (1989), DOI `10.1016/0168-9002(89)90706-7`, citation key `kramer-flecken_1989_UseDCO`.

The BibTeX key matches uniquely by title, year and DOI. Local file size is `450640` bytes; local timestamp `2025-01-09 10:22:20`; SHA-256 is recorded above.

## Scope and Reading Depth

The full seven-page article was read from the PDF text layer. Key checks covered the DCO formalism in Sec.2, geometry/systematics in Figs.1--4 and Table 1, the OSIRIS array description in Sec.3, and the `178W` spin-assignment application in Sec.4.

This is a `method-ingest + theory-ingest` source. It is both a method paper and an experimental demonstration on `178W`; for the current Wiki its main contribution is the DCO-ratio definition, geometry dependence, alignment dependence, and multi-solution boundary.

## Summary

The paper formalizes directional correlations from oriented states (DCO) as a practical reduction of gamma-gamma angular-correlation information in large detector arrays. It defines the gated intensity ratio, studies its dependence on detector geometry, alignment width, spins, multipolarities, and dipole-quadrupole mixing ratios, and shows with OSIRIS calculations that a single measured DCO ratio may map to several different spin/mixing-ratio solutions.

Its practical message is balanced: DCO is powerful for weak or unresolved transitions in multidetector arrays, but it does not uniquely determine spin or `delta` in all cases and should be combined with additional information such as intensities or angular distributions.

## Experimental or Theoretical Setup

- Method context: unpolarized heavy-ion beam, detectors insensitive to gamma polarization, so the full angular-correlation formalism can be simplified for DCO use.
- Initial-state magnetic-substate population is modeled as a Gaussian centered at `m=0` with a width parameter written in the paper as `sigma`; the paper states that `sigma/I` is approximately constant over a wide spin range, but that this empirical rule deviates in the low-spin region `I < 6`.
- Calculations were performed with the DCOMAP code for arbitrary detector geometries and for varying spins/multipolarities/mixing ratios.
- Experimental demonstration uses the OSIRIS array (12 Compton-suppressed Ge detectors) and delayed cascades in `178W`.

## Key Results

KF89-1–8是原2026-07-12审核记录；其中KF89-1的实验分式有上述转写错误。其当前更正见同表KF89-9及页首使用说明，原件没有该上下倒置问题。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KF89-1 | 本文先把理论 DCO ratio 定义为 `R_DCO = W(theta_2,theta_1,phi) / W(theta_1,theta_2,phi)`，并紧接着给出实验上对应的 `R_DCO = I_{theta_2}(Gate_{theta_1}) / I_{theta_1}(Gate_{theta_2})`；交换角度或交换 gate 与被观察跃迁会把 DCO ratio 取倒数。 | method-formalism | direct | p.334, Sec.2 around the definition of `R_DCO` | false |
| KF89-2 | 作者采用以 `m=0` 为中心的 Gaussian magnetic-substate population 描述初态取向，并指出 `sigma/I` 在较宽自旋区间内近似常数，但在低自旋 `I < 6` 区域会偏离这一经验规律。 | method-boundary | direct | p.334, Sec.2 first paragraph | false |
| KF89-3 | DCO 对几何强烈依赖：区分不同 cascades 的效果在一个探测器接近 `0°/180°`、另一个接近 `90°` 时最大；对大阵列，应选择能放大该差异的 detector combinations。 | experimental-criterion | direct | pp.334--335, Fig.2 and text below | false |
| KF89-4 | 实验 DCO ratios 需要做相对效率修正；推荐用能量相近、已知 multipolarity 与 spin 的 cascades 来标定平均修正因子。 | experimental-practice | direct | p.335, Sec.2 paragraph below Fig.2 | false |
| KF89-5 | DCO 依赖初态 alignment：当 `a/I` 很大时，DCO ratio 会趋近 `1`，与放射源无取向情形相符。 | method-boundary | direct | p.335, Fig.3 and surrounding text | false |
| KF89-6 | 在允许 dipole-quadrupole mixing 的情况下，同一个实验 DCO ratio 可对应若干不同的自旋或 mixing-ratio 解；一般而言 `Delta I = ±1` 不能仅靠 DCO 唯一区分，因此单靠 DCO 不能总是给出无歧义自旋指定。 | method-boundary | direct | p.337, top paragraph; Fig.4 discussion | false |
| KF89-7 | 作者总结 DCO method 相对角分布的三项实践优势是：可研究弱跃迁、可处理 multiplets、且不需要 beam-charge normalization。 | author-interpretation | direct | p.337, paragraph below Fig.4 | false |
| KF89-8 | 在 `178W` 的 OSIRIS 示例中，作者结合多条 cascade 的 DCO ratios 与强度信息，把 `3527 keV`、`35 ns` isomer 的自旋定为 `I=14`。 | observed-fact | direct | pp.338--339, Sec.4 and Fig.8 discussion | false |
| KF89-9 | 原文W(theta1,theta2,phi)指在detector1的theta1角用gamma1开门、在detector2的theta2角观测gamma2；故R=W(theta2,theta1)/W(theta1,theta2)=I_theta1^gamma2(Gate_theta2^gamma1)/I_theta2^gamma2(Gate_theta1^gamma1)。旧KF89-1的实验I分式是Wiki倒置转写，本条优先。 | source-transcription-correction | direct-and-self-audit | printed334 Sec2，W定义段与紧接的两个R公式 | true |
| KF89-10 | 本文公式中的gamma1/gamma2是gate/observed标签；Table1又明确各例gating transition为物理级联第二条。两套标签不能不经映射等同“第一/第二次发射”。 | convention-boundary | direct | printed334 Sec2定义段、Table1图注 | true |
| KF89-11 | “两条同L则R=1”不能脱离spin路径：Table1在相同geometry/width下给10→8→7的L2/L2为.66、10→8→8的L2/L2为.57，而stretched10→8→6为1。Fig2的陈述有L=Ii−If的stretched前提。 | calibration-transfer-boundary | direct-and-self-audit | printed334 Table1与Fig2图注；printed335首段 | true |
| KF89-12 | 178W例假设35ns异构体不强烈改变width/I；DCO容许isomer I12或14，作者另用decay-pattern/intensity偏好14。不能把其最终采用值说成一项DCO直接唯一测量，本文未给未见弱branch的完整upper-limit/Cov输入。 | author-assignment-and-boundary | direct-and-self-audit | printed337 Sec4末段；printed339 isomer讨论 | true |
| KF89-13 | 原文称Gaussian的half width sigma，未在本文写明指数式；printed334低spin边界印为I≤6。表中sigma/I值不能仅凭同字母自动转成HWHM或D96Eq19的std。 | width-convention-boundary | direct-and-self-audit | printed334 Sec2首段 | true |
| KF89-14 | 182-keV例以E1/小M2解释generic dipole/quadrupole ratio；不能把本文所有delta都当E2/M1或把平方份额无条件称为E2份额。 | multipole-pair-boundary | direct-and-self-audit | printed339 182-keV讨论 | true |
| KF89-15 | 对采用I=11的3055-keV态，921(G)–306给RDCO=.66±.10，921–169(G)给.47±.15；Fig7c/d分别是11→10→8及11→10→9。作者仍报告921的delta1=.07±.10或delta1>85两支。第一行gate在物理第一条，第二行gate在物理第二条，不能当同方向target比。 | experimental-summary-and-multisolution | direct | printed338 Sec4，Fig7c/d及正文；printed337 Fig6的920.9-keV标记 | true |
| KF89-16 | 原文用Igamma(1090)/Igamma(921)=1.2±.2对照pure-quadrupole预期2.3来偏好921小混合支；本7页方法文没有给2.3的完整模型推导/误差，也没有两DCO与强度的联合Cov。不能将偏好改写为DCO独自唯一确定delta。 | author-branch-preference-and-boundary | direct-and-self-audit | printed338末段–printed339首段 | true |
| KF89-17 | 137/169-keV参考导入平均mixing parameter delta=−1.9，正文归给Dors et al.[3]的angular distributions/branching；但Ref3实际是Gast待发表，Dors1979在Ref2。本文未显式定义其operator ratio，未经primary不能认证该delta与D96/KS70数值坐标相同。 | reference-provenance-and-convention-boundary | direct-and-self-audit | printed338首段；printed339 Refs2/3 | true |
| KF89-18 | 本文给OSIRIS十二台Ge但DCO实际选择六台，角组90/38度、phi18度，要求相对效率修正；sigma/I=.3及35ns异构体不强改width是假设，缺实际pair响应、feeding、producer和Cov。条件点模型不能凭这些文字自称重放原分析。 | experimental-response-readiness | direct-and-self-audit | printed335效率段；printed337 Sec3/4；printed338 Fig7图注 | true |
| KF89-19 | Ref2的Dors NPA314,61(1979)由Crossref/SemanticScholar定位为六作者的High-spin rotational levels in178W populated in177Hf(alpha,3ngamma)，DOI10.1016/0375-9474(79)90555-4、pages61–79；只核metadata，未得全文，不能由此填169/137的delta算符/误差或消除Ref2/3编号边界。 | external-reference-identity | verified-metadata-only | printed339 Ref2；Crossref DOI10.1016/0375-9474(79)90555-4 retrieved2026-10-18 | true |
| KF89-20 | 后续Purry1997 primary用290KICC和prompt/低能符合将原约3525态改为13-、T1/2<1ns，旧35ns移至上方3654态约30ns；这是原方法示例的真实反证/后续修订，KF89原I14历史结论不改写为已包含该修订，也不据此量化921delta变化。 | later-primary-counter-evidence | direct-later-source-and-self-audit | KF89 printed337/339原假设/采用值；Purry1997 printed52–54 Sec4.2.3–4.2.5 | true |

## Nuclear Structure Information

The `178W` application is included as a worked method example rather than a full `178W` structure ingest. The current Wiki uses it mainly to anchor DCO practice and its ambiguities.

## Authors' Interpretation

- DCO ratios are well suited to multidetector-array spectroscopy of weak transitions.
- They can determine spins and dipole-quadrupole mixing ratios in favorable cases.
- They still require complementary information when several calculated branches overlap the same measured ratio.

## Model Results

- DCOMAP calculations quantify the dependence of `R_DCO` on geometry, alignment width, spin sequence, and the mixing ratios of both transitions in a cascade.
- For the OSIRIS geometry `theta_1=90°`, `theta_2=38°`, `phi=18°`, the paper tabulates limiting DCO values for several pure cascades and shows broad multi-solution regions for mixed cascades.

## Competing Interpretations and Limitations

- This paper should not be reduced to the heuristic "`R_DCO ~ 1` quadrupole / `~0.5` dipole"; those numbers are geometry-, gate-, and alignment-dependent.
- The low-spin `sigma/I` deviation is explicitly flagged, so later low-spin work should not inherit a single near-constant alignment-width heuristic without caution.
- The `178W` case uses intensities in addition to DCO; the source itself does not claim that DCO alone always solves the problem.

## Extracted Pages

- Nuclei:
- Bands:
- Concepts:
- Methods: [[dco-ratio]], [[angular-correlation]], [[spin-parity-assignment]]
- Observables: [[multipole-mixing-ratio]]
- Projects: [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]

## Personal Notes

This is one of the clearest sources for the sentence "DCO is compressed angular-correlation information, not a geometry-free universal classifier." It also gives a concrete early warning that low-spin behavior and multi-solution branches can spoil naive reuse of standard thresholds.

## 本次原件核验范围与角色映射

本session的Day16整体primed回忆先于source/raw；补充的Ref1专门预测在读过既有source摘要后、打开raw前冻结，不能称盲测。raw SHA-256重新匹配`30cdf474db5fbfaa6a27f6d2e0d11ea39bbb61a05c8153e740f2f3dcca52220f`；完整读7页text主线，放大printed334公式及printed335多解图。原有`reading_depth: read`/human-review范围不改，额外声明不等于DCOMAP代码取得或本session人审。

令按物理发射先后记为a（上游）、b（下游），联合函数写`W_ab(theta_a,theta_b)`。[[dco-pdco-ambiguity-worksheet]]自己定义的`R*=W_ab(0,90)/W_ab(90,0)`可映射为：

| KF的detector标签 | 待测/门 | 对应比 |
| --- | --- | --- |
| theta1=0、theta2=90 | obs=a、gate=b | R* |
| theta1=90、theta2=0 | obs=a、gate=b | 1/R* |
| theta1=90、theta2=0 | obs=b、gate=a | R* |
| theta1=0、theta2=90 | obs=b、gate=a | 1/R* |

这是原定义的代数标签映射，要求同一corrected joint cells/selection/normalization；不同门后密度或不同pair cuts不能当作机械互反。D96 Fig7只列0/90角组，不在图注重写上述全部gate/detector标签，故数值约.4本身不认证唯一的标签解释；保留worksheet的显式R*定义。

新的corrected source入口已同步到[[dco-ratio]]；本页旧实验转写不再作为该方法的操作定义。KF89-2旧I<6摘要与原件I≤6的差别、half-width用语和generic delta的多极子类型分别保留在KF89-13/14，不能靠字母相同填入原文没有的定义。

## 2026-10-18独立Day16复核：921-keV实测双候选

本session在带priming声明的主动回忆冻结后重新读完7页主线，原图核printed334的定义/Table1、337的Fig6、338的Fig7与两候选、339的companion/References。原SHA-256按hex大小写归一后完全匹配；首个提取器只因大小写敏感比较而退出，未改raw。Crossref按DOI重新核题名、七作者、1989/275/333–339，metadata不作为图表数值证据。

新KF89-15–18及[[w178-921-dco-gate-double-solutions]]是本session的Codex self-audit，均needs_review:true；原page human-reviewed及KF89-1–14的文字/flags不扩大、不清除。新note把两实测gate角色、作者支、相同目标比的倒数及误差像与本任务条件点模型分开。额外的D96 tensor/photon一致性不代表DCOMAP已重放；部分Table1点值和作者大delta支未复现，保留原因未决。

本轮决定supports多解性，revises不分gate角色直接联合比值的做法，limits强度prior和偏振符号的唯一赋值。下一原件是169/137参考的primary及完整response；printed338的Dors[3]与文末Ref2/3冲突仍开放，不把参考标签自动改成已取得的独立实验。

KF89-19只解决文献身份，网页入口[DOI](https://doi.org/10.1016/0375-9474(79)90555-4)。OA-only下载得到oa_not_found，public publisher discovery无候选、S2没有OA URL，Scholar一次timeout；没有取得或新归档Dors PDF。下载器的TDM license/confirmed_oa标签与Unpaywall is_oa:false不一致，本任务按未取全文保留边界，不把TDM许可当开放全文。另对[[bargholtz-1987-high-spin-gamma-gamma-directional-correlations]]原件/两近似作固定检查后，KF89 Table1差异仍未解释，见[[angular-correlation]]。

本session随后实际取得[[nndc-2009-178w-dco-reference-records]]的178074004/006：前者明确1989KR01、后者1979DO02并列137/169的AD；MR栏仍空，CC不能搬作delta。adopted对象默认E/RI另来自170Er(13C,5n)，其M1+E2/11-标签不算本原实验的新独立确认。新的same-parent诊断不替换本篇−1.9 reference输入或原921两支，完整边界见[[w178-921-dco-gate-double-solutions]]。

新KF89-20链接[[purry-1997-phd-w178-multiparticle-structure]] P97-8/9：后续实验确实改变约3525能级和35ns归属，不能只引用本篇abstract“established14”便声称无后续反证。原page人审历史/KF89-1–19均保留；新条只为Codex self-audit。旧DCO两候选、spin/feeding/width与必要观测的使用门进一步得到现实例子支持，未自造原921重新拟合结果。

## 1988原学位论文的目录取证与未读边界

2026-10-18用户恢复Day16原学习窗口后，以Purry printed101的Kr88为线索，新查德国国家图书馆SRU。DNB记录[881391638](https://d-nb.info/881391638)的MARC088明确`Jül-Spez 458`，245题名为*Untersuchung zum Zerfall von Hochspin-Isomeren in den W- und Os-Isotopen und Entwicklung von Programmen zur Steuerung der Experimentlogik und der Datenerfassung*，100作者Andreas Krämer-Flecken，264出版1988，300为123页，502为Bonn大学学位论文。另一个[890076413](https://d-nb.info/890076413)题名用复数*Untersuchungen*、300为123Bl.，同为Bonn1988；保留目录版本差别，不补ISBN/DOI。

两条856明确标为**Inhaltsverzeichnis**。实际取得[881391638目录PDF](https://d-nb.info/881391638/04)和[890076413目录PDF](https://d-nb.info/890076413/04)，均只有两页，SHA-256分别`e7efc704bd296289a6f99566140784c01a4bce95d779f5c17df18020aaa0fd37`、`366628ce2d21d6249565ef93f69334fde80d905c4a5f966e73b59ecdc11a07d7`。原图核目录第一、二页：Sec3为178W实验，printed38；Sec3.2“Bestimmung der Spins mit Hilfe von DCO-Verhältnissen”从printed46开始；下一Sec3.3时间分析从printed58开始；Anhang93、Referenzliste95。这里只确认原件的可定位章节，**尚未读其DCO正文、Gaussian指数、DCOMAP输入或代码**。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| KF89-21 | Purry的Kr88可由DNB881391638的Jül-Spez458/作者/1988/Bonn论文记录定位；公开下载是两页目录，Sec3.2 DCO从printed46开始、Sec3.3从58开始。目录未提供其正文/宽度约定或producer，不算新独立DCO实验。 | external-reference-identity-and-availability | direct-catalog-and-original-contents | DNB881391638 MARC088/100/245/264/300/502；881391638/04 PDF1 Sec3.2 | true |

本批原件/元数据只在repo tmp隔离，未修改raw或Bib。Jülich公开检索返回fast-challenge shell，未绕过；Bonn repository精确题名/authorfilter均无match；DataCite特定query零结果。Scholar超时、若干外部目录网络失败，不据此宣称全球无全文。决定`supports`较高信息的原producer追源，`limits`将目录PDF当整本论文。下一精确目标为该论文printed46的Sec3.2正文；不自由调σ解释KF89印表。所有旧人审/claim flags保持。
