---
type: source
title: "Behavior of the collective rotor in wobbling motion"
aliases: [Streck et al. 2018, collective rotor in wobbling]
created: 2026-07-15
updated: 2026-10-26
status: ai-draft
review_status: unreviewed
source_type: theory-article
reading_depth: deep-read
title_original: "Behavior of the collective rotor in wobbling motion"
authors: [E. Streck, Q. B. Chen, N. Kaiser, U.-G. Meissner]
journal: Physical Review C
year: 2018
volume: 98
pages: 044314
doi: 10.1103/PhysRevC.98.044314
arxiv:
language: en
canonical_source: doi:10.1103/PhysRevC.98.044314
zotero_item_key:
citation_key: streck_2018_Behaviorcollective
zotero_uri:
library_file:
raw_file: "raw/papers/2018_Streck et al_Behavior of the collective rotor in wobbling motion.pdf"
raw_sha256: E6816F64F08AFEBB4E0230EC418A5CCF13E19B30C38E5B6964DCCC7B564A2F9D
nuclei: [135pr]
reactions: []
experiments: []
models: [particle-rotor-model, tilted-axis-cranking]
observables: [wobbling-energy, moments-of-inertia, bm1-be2-ratio, interband-e2-strengths]
methods: [r-representation, k-representation, azimuthal-angular-momentum-plot]
tags: [wobbling, transverse-wobbling, longitudinal-wobbling, signature-partner, particle-rotor, angular-momentum-geometry]
---

# Streck et al. (2018): Behavior of the collective rotor in wobbling motion

## Bibliographic Record

E. Streck, Q. B. Chen, N. Kaiser and U.-G. Meissner, *Physical Review C* **98**, 044314 (2018), DOI `10.1103/PhysRevC.98.044314`. The BibTeX key is uniquely matched as `streck_2018_Behaviorcollective`.

## Scientific Question and Motivation

The paper asks how the collective rotor and the high-j proton share angular momentum in the `135Pr` wobbling bands. It aims to expose the wave-function geometry behind the reported decrease and subsequent increase of the wobbling frequency, and to provide a microscopic PRM distinction between wobbling and a signature-partner band.

## Scope and Reading Depth

Full ten-page article read. Covered: the PRM Hamiltonian, K-to-R basis transformation, azimuthal/R/KR probability distributions, energy and wobbling-frequency calculations with and without pairing, angular-momentum coupling schemes, signature-partner comparison and B(M1) limitation. Not covered: an independent remeasurement of the `135Pr` level scheme or a new experimental polarization analysis.

## Summary

The PRM wave-function transformation makes rotor-angular-momentum distributions visible in `135Pr`. The calculated low-spin transverse and high-spin longitudinal patterns, and the separate signature-partner alignment pattern, are model diagnostics rather than directly measured angular-momentum vectors.

## Method and Design Logic

The particle-rotor model is solved in the strong-coupling K representation and transformed to the R representation, where rotor-angular-momentum probabilities can be summed. The authors use an azimuthal distribution P(theta,phi) for total angular momentum, an R plot for the rotor magnitude, and KR plots for its projections on the long, short and intermediate axes. These distributions are compared across yrast, one-phonon and signature-partner states to reconstruct the coupling geometry.

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ST18-1 | The PRM Hamiltonian separates a collective rotor term from a high-j single-particle intrinsic term; the rotor term is most naturally evaluated in the R representation, while the usual strong-coupling diagonalization uses the K representation. | method/formalism | direct | PDF pp. 2-3, Eqs. (2)-(5) and representation discussion | true |
| ST18-2 | The K-to-R transformation makes the rotor angular momentum explicit and permits probability distributions for R and its principal-axis projections; these are calculated quantities, not direct experimental observables. | method/formalism | direct | PDF pp. 2-4, Eqs. (6)-(22) | true |
| ST18-3 | With a pi(1h11/2) proton, beta = 0.17, gamma = -26 degrees and the adopted MoI, the PRM reproduces the reported `135Pr` yrast/wobbling energies and the decreasing-then-increasing wobbling-frequency trend qualitatively. | model-result / review-background | direct | PDF pp. 4-5, Fig. 1 and numerical details | true |
| ST18-4 | In the calculation, the wobbling frequency decreases for I <= 14.5 hbar and increases at higher spin, consistent with a calculated transverse-to-longitudinal change; the thresholds differ slightly between pairing choices and data. | model-result / author-interpretation | direct | PDF pp. 4-5, Fig. 1 and text below it | true |
| ST18-5 | The calculated proton angular-momentum components remain mainly aligned with the short axis at low spin and trend toward the intermediate axis above about I = 13.5 hbar, while the signature-partner components are qualitatively different. | model-result | direct | PDF pp. 5-6, Fig. 3 and discussion | true |
| ST18-6 | Azimuthal plots show principal-axis rotation about the short axis at low spin, a planar regime at intermediate spin, and a return toward intermediate-axis rotation at high spin; the one-phonon distributions have nodes/symmetry features distinct from the zero-phonon states. | model-result / angular-momentum criterion | direct | PDF pp. 6-7, Fig. 4 and Eq. (25) | true |
| ST18-7 | R and KR plots give different rotor-coupling patterns for the low-spin transverse region and the high-spin longitudinal region, including different changes of the short- and intermediate-axis rotor projections between yrast and wobbling states. | model-result / author-interpretation | direct | PDF pp. 7-9, Figs. 5-10 and coupling-scheme lists | true |
| ST18-8 | The PRM signature-partner state has a distinct single-particle alignment pattern from the yrast and wobbling states, so the authors propose the angular-momentum components as a model diagnostic for distinguishing the two modes. | model-result / experimental-criterion | direct | PDF pp. 5-6 and 8-9, Fig. 3 and Figs. 9-10 | true |
| ST18-9 | Pairing changes the calculated alignment and causes the transverse-wobbling branch to terminate earlier, but does not change the qualitative low-spin/high-spin evolution in the displayed calculation. | model-result / limitation | direct | PDF pp. 4-6, Figs. 1 and 3 | true |
| ST18-10 | Calculated B(M1) values remain larger than the experimental values by factors of roughly 3-10 even after pairing; the authors discuss a missing proton-neutron current (scissors-like) coupling as a possible source of the discrepancy, while energies and interband B(E2) are less affected. | model-result / limitation | direct | PDF p. 9-10, final discussion | true |

## Analytical Reconstruction

The source adds a wave-function-level layer to the energy-based transverse-wobbling argument. Its evidence chain is: PRM parameterization -> transformed wave functions -> azimuthal/R/KR distributions -> inferred rotor-particle coupling scheme. The transition from short-axis principal rotation through a planar region to intermediate-axis rotation is therefore a PRM reconstruction. The signature-partner distinction is also model based: different particle components and rotor projections are proposed as discriminants, not measured alignment vectors.

## Competing Interpretations and Limitations

- The PRM uses fixed deformation and selected moments of inertia; calculated topology is parameter dependent.
- Energy agreement does not validate every probability distribution, and the B(M1) overestimate remains unresolved.
- Signature-partner discrimination from angular-momentum components is a model criterion requiring experimental cross-checks.

## Assumptions, Limits and Reverse Tests

- The PRM uses a fixed triaxial deformation and selected moments of inertia; alternate parameter sets or a microscopic calculation are needed to test robustness.
- The reported energy agreement does not validate every wave-function probability distribution. A reverse test is to compare the same distributions and electromagnetic matrix elements with TAC, TPSM or a configuration-mixed PRM.
- The B(M1) overestimate is an explicit quantitative limitation. It weakens any inference based only on calculated M1 strengths and motivates proton-neutron current coupling beyond this PRM.
- The source does not provide new experimental transition measurements; all quoted `135Pr` data remain linked to the original spectroscopy papers.

## Related Knowledge and Project Relation

- Concepts: [[wobbling-motion]], [[transverse-wobbling]], [[longitudinal-wobbling]], [[signature-partner-bands]], [[angular-momentum-alignment]], [[triaxial-deformation]]
- Models: [[particle-rotor-model]], [[tilted-axis-cranking]], [[triaxial-particle-rotor-model]]
- Methods/observables: [[spin-coherent-state-map]], [[wobbling-energy]], [[interband-e2-strengths]], [[bm1-be2-ratio]], [[moments-of-inertia]]
- Projects/synthesis: [[low-spin-wobbling-controversies]], [[wobbling-vs-signature-partner]]

This is a model-comparison source that supports a detailed angular-momentum interpretation of `135Pr`; it does not replace experimental evidence or settle the low-spin wobbling controversy.

## Extracted Pages

- Nucleus: `135Pr` (PRM comparison; experimental source remains separate)
- Concepts: [[wobbling-motion]], [[transverse-wobbling]], [[longitudinal-wobbling]], [[signature-partner-bands]], [[angular-momentum-alignment]]
- Models/observables: [[particle-rotor-model]], [[tilted-axis-cranking]], [[wobbling-energy]], [[bm1-be2-ratio]]
- Project: [[low-spin-wobbling-controversies]]

## Human Review Triage

P0:

1. **ST18-3/ST18-4, PDF pp. 4-5, Fig. 1.** Verify the spin ranges, pairing labels and whether “evidence” is attributed to the calculated/experimental frequency trend rather than written as a direct wave-function observation.
2. **ST18-5/ST18-8, PDF pp. 5-6, Fig. 3.** Check the short-to-intermediate alignment language and the precise contrast with the signature-partner band.
3. **ST18-6/ST18-7, PDF pp. 6-9, Figs. 4-10.** Verify the azimuthal, R and KR distribution interpretation and the rotor-projection increments used in the two coupling schemes.

P1:

- ST18-1/ST18-2: check the K-to-R transformation terminology and normalization of P(theta,phi).
- ST18-9/ST18-10: verify the quantitative pairing and B(M1) limitation statements.

## Review Status

Page and all ST18 claims remain unreviewed with `needs_review: true`. Human review is deferred until use: perform targeted claim review when this content is used for paper writing, a key project decision, synthesis finalization or a paper-level evidence pool.


## Day23：实际基底、转子项与整模型readiness

本轮回读原PDF1–10完整主线/10页references，视觉核PDF2 Eq2–6、PDF3 Eq9–24与PDF4 numerical details；原SHA匹配，旧ST18-1–10及review状态不变。以下为Codex self-audit，needs_review:true。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ST18-D23-001 | Eq6的D2 strong基底保K−Ω非负偶数，差0时K=Ω>0；Eq9 weak基底取|I−j|≤R≤I+j、KR=0,2,…≤R，但oddR无KR0。因此R1完全不出现，R3等奇数R仍有允许分量；只有额外轴对称KR0限制时才仅evenR。Eq11带sqrt[(2R+1)/(2I+1)]、CG与sqrt(1+δKR0)，Eq12/13为正交，不能漏KR0因子或把R/KR标签混作声子数。 | basis-symmetry-and-normalization | direct-original | PDF2 Eq.6 and D2 paragraph; PDF3 Eqs.9–14 | true |
| ST18-D23-002 | Eq20的P_R,KR是先将d_KΩ与A相干求和后平方，不是K概率与|A|²的非相干乘积；Eq21全R/KR归一、Eq22/23分布是不同边缘化。Eq24只给R3²一个矩，不能据单一RMS反演全部P；这些是模型波函数分布，不是新实测j/R方向。 | probability-amplitude-and-observable-boundary | direct-original | PDF3 Eqs.20–23; PDF4 Eq.24 | true |
| ST18-D23-003 | SecIII用j=11/2、β.17/γ−26°，(s,i,l)惯量13/21/4；J1被改变至14/11以比较TW结束spin16.5/12.5，说明其临界spin是该参数模型的条件输出。无配对主讨论与Δ=12/sqrt(A)的PRM*分列，Eq5的C数值形式指Ref33 Wang/Qi/Zhang2009，本文没有完整列出它及电磁effective operators/参数，不能只见H形式就称原全文producer和B(M1/E2)都已复现。 | model-input-and-readiness-contract | direct-original | PDF2 Eq.5; PDF4 Sec.III and pairing discussion; PDF10 Ref.33 and B(M1) paragraph | true |
| ST18-D23-004 | 本文Fig3/R/KR/azimuthal图提供模型内SP与wobbling的不同耦合图像，但SP带头能量无/有pairing仍高估约900/500keV；p10称pairing可使M1小2–3倍而仍高估3–10，scissors-current缺失为其引用的解释。能谱拟合不能独立验证全部wavefunctions/模式，不能把缩g或单条小δ当唯一SP/TiP/剪刀识别。 | supporting-model-and-material-limitations | direct-author-model-and-attribution | PDF5 Fig.3/discussion; PDF10 final discussion | true |

Knowledge Impact and Learning Decision：supports可追溯的K↔R及转子Hcoll组件实现，limits将组件控制扩张为完整模型/真实核态/实验验证。按[[signature-tip-shears-discrimination-contract]]分开C、pairing和EMoperator缺口；新变换/转子代码`system/scripts/day23_prm_basis_rotor.py`为本任务独立实现，非原作者producer，未生成实验δ/Q/τ或最终模式。


### Day23：Ref33的正文追溯与C处方

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ST18-D23-005 | Ref33为Wang/Qi/Zhang, “Coupling Parameter in the Single-j Shell Model”, CPL26,052102(2009), DOI10.1088/0256-307X/26/5/052102；journal自身公开页面的PDF入口成功取得4页%PDF，SHA dbdb64a8c116287015a062b80a4cf18f98fa190c4e2210f3dae7765bf856db96。实际读完整4页并视觉核p2 Eq11/Table1。其旧Eq3为C=195 A^(−1/3)β/[j(j+1)]，新Eq11为C=(123/8)sqrt(5/π)(2N+3)A^(−1/3)β/[j(j+1)]，MeV；N是HO主壳层量子数。ST18只说采用Ref33的form，具体实现/数值仍应明确，不把已取得该文公式称原作者code复现。 | external-direct-source-formula-and-implementation-boundary | directly-read-cited-paper-with-archival-boundary | ST18 PDF10 Ref.33; https://cpl.iphy.ac.cn/en/article/pdf/preview/10.1088/0256-307X/26/5/052102.pdf pp1–2 Eqs.3/11 | true |

这份Ref33完整PDF目前仅tmp公开staging、正式raw归档deferred，不新增/覆盖原ST18 raw。IOP DOI入口的HTTP200实际是verification页面，不能当取得全文；真正body来自期刊自身公开PDF，未读取凭据或绕过挑战。实际公开可读不等于已核开放许可证。

若明确采用Wang Eq11、N5、A135、j11/2、ST18 β.17，条件C=.233738451MeV；若采用旧Eq3则.180757460MeV，二者比1.29310542。这里只是定义/输入敏感性，没拟合实测谱，也不把处方差认证为ST18实际曾算错。该正文解除C处方的一个readiness缺口，pairing/完整EMoperators/原producer及实际response缺口仍独立保留。


## Day23：固定H任务variant的数值范围

以下是本任务基于已读source定义的模型实验，**不是ST18作者新报告或实际核态命名**。新claims needs_review:true。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ST18-D23-006 | 本任务指定无pairing单j particle+ H，A135/N5/j11/2/β.17/γ−26、MoI13/21/4，显式选Wang2009 Eq11得C=.233738451MeV，对14个I=11/2至37/2的完整D2空间求解。87项有限矩阵Hermitian/D2closure、两basis谱、零C rotor、Casimir与归一控制通过，max eigen residual约7.2e−14MeV。只对源定义及实现做控制，不给原authorproducer、完整E2/M1或实验模式认证。 | declared-task-model-and-validation-scope | source-defined-conditional-numerics | source premises PDF2 Eqs.2–6, PDF4 Sec.III; ST18-D23-005; task model-contract-009 | true |
| ST18-D23-007 | 上述固定variant最低两态在I17/2、21/2的间隔841.203/839.717keV；仅交换ordinal0/1与两实测序列的mapping会翻E3−E2的号，不改变幅度，因而两mapping都不能重现L22-D23-001的44.0/44.5keV中央差。只诊断这一H/这两候选mapping，不据此排除其它本征态、参数、模型或原实验；未给modelerror/Cov或p值，不叫统计证伪。 | fixed-model-mapping-diagnostic | task-numerics-and-primary-level-input | ST18-D23-006 premises; L22-D23-001; fixed-state-mapping-009 | true |
| ST18-D23-008 | 在单j/core磁矩μ=gR R+gj j假设下，本任务由R²和Casimir计算a=〈I·j〉/[I(I+1)]，所以g=gR+(gj−gR)a。I17/2两ordinal的a=.565133/.504198，差.060935；I27/2为.387731/.383045，差.004686，同时其j(s,i,l)RMS分别约(4.985,2.958,1.465)/(4.588,3.519,1.522)。a是条件几何系数，非实测或已校准物理g；gj/gR未给，近a不独立证明相同body图像。 | conditional-companion-observable-coefficient | task-Casimir-derivation-and-model | ST18-D23-006/007; source Eq.4 and R representation; task static-g derivation | true |

`system/scripts/day23_prm_fixed_state_mapping.py`强制CLI显式选择C处方。旧Wang Eq3作为另一个固定variant给C=.180757460MeV，同两个I的最低态间隔715.129/723.189keV，同样未闭合44keV中央差；这是两种有来源的处方敏感性，不是任意调参或作者旧模型已证错误。原parameter可能早已用能谱定标，当前能量对照不是独立盲测；将来physicalg/电磁holdout还需确定mapping和算符。


## Day23：固定H上的条件core-E2连接向量

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ST18-D23-009 | 本任务在009的同H本征态上声明normalized core-only E2，电荷轴1s/2i/3l、γE=γH=−26°、q0=cosγE、q±2=sinγE/sqrt2；未知S因子化。精确finite-I CG投影与独立Wigner-d积分核对、轴对称CG/closure/reverse等每处方25项控制通过；它们只验证该明示operator实现，电荷γ与H相同/省略单粒子E2不是实测或本文给出的完整EM定标。 | declared-task-electromagnetic-operator | conditional-numerical-implementation | ST18-D23-006 premises; H02-D23-001; task model-contract-010 | true |
| ST18-D23-010 | 指定跨spin恒定ordinal映射A(B3=0/B2=1)或B(B3=1/B2=0)，Eq11处方下形式矩阵元r747/526为137.3196或.0299216，r813/726为.505399或.00349706；但A的526候选ΔE=−.506395MeV为上跃，不能作为自发γ出口比（输出null）。旧Eq3的形式对应22.2669/.0165857与.500773/.00113266，A的526也为上跃ΔE−.356500MeV。两分母分别是另一band outlet和同band I−2，不互换；非零upward B不等于退激存在。均不报显著性/实际Q/δ/τ或唯一模式，009能量mapping问题保留。 | conditional-fixed-operator-vector-and-energy-direction | task-predictions-with-identity-boundaries | ST18-D23-009; L22-D22-001/002; task core-e2-010 | true |

这里operator closure包括upward及diagonal/elastic矩阵元，不是实际γ分支或计数总和。模型B/S²只有相对scale意义，不给绝对W.u.；physicalM1算符/混合相位未提供，所以不从E2比值补造δ。原source作者的PRM与scissors解释范围亦不由本数值练习改写。

## Day23：同H的particle-j张量与相对磁强度

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ST18-D23-011 | 在ST18 Eq7的lab耦合基底，j的rank1算符保持R/KR，通过m/MR的CG相干和求矩阵元，再用Eq11转回强基底。本任务同009 H的single-j投影中，跨I M1可写SM j_lab，未知SM=sqrt(3/4π)(gj−gR)μN。每处方32检查通过：freeR0、rank1 triangle、两个labM、Hermitian reverse/详细平衡、完整j closure=j(j+1)、j+R生成元及对角Casimir。最大closure误差3.6e−14ℏ²；与009能量、010 E2差0。控制仅核本实现，j-only closure含elastic/upward，不是full μ或实验γbranch sum。 | declared-task-normalized-M1-operator | conditional-source-defined-numerics | PDF3 Eq.7 and Eq.11; H02-D23-003; task model-contract-011 | true |
| ST18-D23-012 | 同010两mapping的747/813候选线，Eq11下A的B(M1)/SM²为1.661094/1.311946，B为.00839147/.00987035；相应normalized E2/j振幅比A为−.279323/−.285530，B为+.317974/+.285737。未知SE/SM未校准，均非physicalδ。共同scale与辐射常数在跨线(δ747/E747)/(δ813/E813)中消去时，A/B条件值为.978261/1.112823，旧C为.968807/1.140861；这个消去要求相同operator与spin-independent尺度，不能修复009/010能量问题。 | conditional-operator-mapping-and-scale-cancellation | task-derivation-and-frozen-H-numerics | ST18-D23-011; task particle-m1-011 and mixing-readiness-011 | true |

μ的对角gR项不能遗漏；SM在gj=gR时为0，非零j矩阵元并不保证物理M1非零。没有借用Lu或另一模型的effectiveg给Pr补数。不同态rephasing会同改E2/M1振幅，其比不变；改变物理operator/约定或使尺度随spin变动则是另一假设。旧C仅显式处方敏感性，不代表作者实际调参史。

算符投影前提另见[[hamamoto-2002-wobbling-excitations-odd-a-high-j-aligned-particles]] H02-D23-003。
