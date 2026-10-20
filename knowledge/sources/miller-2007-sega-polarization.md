---
type: source
title: "Miller et al. 2007 - Linear polarization sensitivity of SeGA detectors"
aliases: [Miller 2007 SeGA polarization]
created: 2026-09-21
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: method-paper
reading_depth: deep-read
title_original: "Linear polarization sensitivity of SeGA detectors"
authors: [D. Miller, A. Chester, V. Moeller, K. Starosta, C. Vaman, D. Weisshaar]
journal: "Nuclear Instruments and Methods in Physics Research A"
year: 2007
volume: 581
pages: "713-718"
doi: "10.1016/j.nima.2007.07.141"
citation_key: Miller_2007
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "Miller et al., NIM A 581, 713-718 (2007)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/2007_Miller et al_Linear polarization sensitivity of SeGA detectors.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/2007_Miller et al_Linear polarization sensitivity of SeGA detectors.pdf"
raw_sha256: "a334ee35a84ded50f6a7937c037ee13d2d06b2f8406b0c68fac1a4245999acf3"
nuclei: [245Cm, 249Cf]
reactions: [249Cf-alpha-decay]
experiments: [SeGA, alpha-gamma-correlation]
models: [Klein-Nishina-response, pure-dipole-angular-distribution]
observables: [linear-polarization, asymmetry, Q, figure-of-merit]
methods: [Compton-polarimetry, alpha-gamma-correlation]
tags: [SeGA, polarization, Compton-polarimetry, detector-response]
---

# Linear polarization sensitivity of SeGA detectors

## Bibliographic Record

- D. Miller *et al.*, *NIM A* **581**, 713–718 (2007), DOI `10.1016/j.nima.2007.07.141`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/2007_Miller et al_Linear polarization sensitivity of SeGA detectors.pdf`。

## Scope and Reading Depth

- PDF pp.713–718 fully read: SeGA side irradiation/segmentation, `P/A/Q` formalism, `249Cf→245Cm` α–γ calibration, angular distribution, geometric asymmetry, sensitivity, figure-of-merit comparison and outlook.
- Not covered: in-beam pure-transition calibration and raw waveforms.

## Key Results

- SeGA detectors have four quadrants and eight axial slices (32 segments) and are irradiated from the side for fast-beam Doppler correction. The paper measures the previously untested side-irradiated Compton response (PDF pp.713–714, Figs.1–2).
- `249Cf` α–γ correlations provide opposite-sign pure E1 polarizations at 333 and 388 keV. Angular-distribution coefficients are `a2=−0.29(2)` and `+0.17(1)` (PDF pp.714–716, Eqs.7–12, Figs.3–5).
- Geometric asymmetries from unpolarized lines are `a(333)=0.126(7)` and `a(388)=0.128(7)`. After correction, the relative sensitivity is `Qrel=0.18(2)`, corresponding to `Q≈0.14(2)` near 350 keV (PDF pp.716–717, Fig.8, Table 1).
- The single-detector polarization coincidence efficiency is about `2.99×10^-4`, giving a figure of merit `FM≈5.9×10^-6`, comparable within an order of magnitude to other arrays but lower than Clover sensitivity (PDF pp.717–718, Eqs.13–14, Table 1).
- The authors estimate `ΔP≈0.3` with 5000 photopeak counts and emphasize that in-beam calibration at higher energies and tracking improvements remain necessary (PDF p.718).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MI07-1 | Side-irradiated SeGA acts as a usable Compton polarimeter with `Q≈0.14(2)` near 350 keV. | calibration-result | direct | PDF pp.713–717, Fig.8, Table 1 | true |
| MI07-2 | Detector geometry, unpolarized asymmetry correction and finite-angle averaging are explicit response inputs. | method-boundary | direct | PDF pp.714–717, Eqs.1–6 | false |
| MI07-3 | SeGA's efficiency–sensitivity tradeoff gives `FM≈5.9×10^-6` for the tested setup. | performance-result | direct | PDF pp.717–718, Table 1 | true |
| MI07-4 | The calibration is a source/energy/geometry test, not an in-beam parity assignment. | limitation | direct | PDF pp.717–718 | false |


### Day17原件新增自审

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MI07-D17-1 | 侧入射32segment是4quadrant×8slice；standardfig18units与本实验实际15units分开：6在37°、9在90°，距source24cm，不把8+10layout当本run数。 | experimental-setup | direct-and-self-audit | printed714 Fig1–2; printed715 Sec3.2 | true |
| MI07-D17-2 | 249Cf约1µCi，经alpha衰变245Cm388.3keV9/2−同parent的333→54.8 9/2+和388→0 7/2+均E1；oppositeP由不同branch/AD而非E/M相反。Si厚400µm距11cm，2milPt停重离子。 | reference-identity | direct-and-self-audit | printed715 Fig3 Sec3.1–3.2 | true |
| MI07-D17-3 | singles concurrent downscale125，333每detector约25000singles/7000coinc/100h，388约4倍counts；Eq9–12的Nd/Ns消Ge效率而保alphaε和finiteangleWav，samecounts层仍可能共享Cov。 | normalization-and-independence | direct-and-self-audit | printed715 Eq9–11; printed716 Eq12 | true |
| MI07-D17-4 | a=Uperp/Uparallel，A=(Nperp−aNparallel)/(Nperp+aNparallel)，a333=.126(.007)/a388=.128(.007)，不同ST99倒数约定；weighted平均σ多来自unitdifference，sample std .009，不自动作独立共同calibrationσ。 | response-convention | direct-and-self-audit | printed714 Eq5–6; printed716 Sec4.2 | true |
| MI07-D17-5 | only2segments/photopeak选择的parallel/perp约占25%/3%，其geometry空间不同；approx fractions ratio .12不等精确a=.126，可是rounding范围，不改原a强配。原未给实际persegment数值阈值/ordering核，不补producer。 | selection-and-readiness | direct-and-self-audit | printed716 Fig6 Sec4.2 | true |
| MI07-D17-6 | 同E1 a2(388)=+.17(.01)、a2(333)=−.29(.02)由AD fit；Eq8/finiteangle推P，故knownE1不单独给数值P。原文字388两P−.267(.007)/−.13(.02)及333+.24(.02)/+.37(.02)顺序保留。 | experimental-fit-and-input | direct-and-self-audit | printed715 Eq8; printed716 Fig5 Sec4.3 | true |
| MI07-D17-7 | 原388P文字与nominalforward/back order、裸37/90pointEq8不直接闭合：point388−.08570/−.27869、333+.18160/+.37991。fullgamma/alphaacceptance和平均recipe未得，不能据此改Q/调角或判实验错。 | bounded-summary-replay | direct-and-self-audit | printed715 Sec3.2 Eq8; printed716 Sec4.3 | true |
| MI07-D17-8 | 在commonE1 integratedStokes模型，printedP反推S=<sin²>：388 .96690/.52785，333 .51543/.95858；全在物理0–1，仅为接受moment合同诊断，不认证actualgeometry/交换原标记或证明finiteangleproducer。 | task-calculation | direct-and-self-audit | printed715 Eq7–8; printed716 Sec4.3 | true |
| MI07-D17-9 | 四group相对A为−.08(.03)/−.02(.03)/+.04(.04)/+.10(.04)，claimedQrel=.18(.02)。只用summary在fixedQrel作残差均约1.1所印σ以内，不能重放原逐detectorfit或恢复完整Σ。 | reported-result-and-summary-control | direct-and-self-audit | printed717 Fig8 Sec4.3 | true |
| MI07-D17-10 | Eq14 εc=(Nparallel+Nperp)/(2Ntot) εphoto；singleεphoto≈.00212，roundedfraction给εc.0002968/FM5.8173e−6近原2.99e−4/5.9e−6。平均方向效率非裸selectedsum，也非整15array效率。 | efficiency-denominator-and-calculation | direct-and-self-audit | printed717 Eq13–14 | true |
| MI07-D17-11 | 设计Npeak5000/nullP/Q.14、按原rounded3%/25%独立primitivecounts且knowna=.12，sigmaP≈.308607，闭合Outlook约.3的计数量级；不是5000selected事件或actualCI。若另假设σa .007独立，仅该nuisance可贡献.2083，但实际unitspread/Cov不允许如此直接合成。 | conditional-count-design | direct-and-self-audit | printed716 Sec4.2; printed718 Outlook | true |
| MI07-D17-12 | Table1其它POLALI/Clover/Gammasphere的Q用文献外推至约350keV、absoluteeff从图估；FM表误差只availableQuncert，含effestimate整体认为30%。不是四套独立同beamtime正面实验ranking。 | shared-reference-and-comparison-boundary | direct-and-self-audit | printed717 Table1 Sec5.2; printed718 Sec5.2 | true |
| MI07-D17-13 | 作者要求higherenergy/inbeam pureD/Q标定；tracking是future改善，原SeGA模拟fastbeam potential不等已测31/33Mg parity或newdigitalorderingresponse。 | readiness-and-proposal-boundary | direct-and-self-audit | printed718 Outlook | true |
| MI07-D17-14 | Eq4的Q0=(1+α)/(1+α+α²)精确是singleCompton90°reference；一般Eq3最大θ在α>0略小于90。333/388理论max角84.936/83.889、qmax.807179/.769044，相比q90 .795473/.753179高约1.47/2.11%；不把sourcecurve重新归一或改publishedQrel。 | cross-source-analytic-scope | derived-and-matching-definition | printed714 Eq4; MI07-D17-4; GR97-D17-2 | true |
| MI07-D17-15 | 若把本文limitedtoQ0措辞理解为任何Compton角的严格上界，general-angle核给反例；本任务只限制该字面外推，不指认原SeGA测量失败。maxpointq不等fullmultipletransport bound或最优FOM，actualSeGA阈值未给不从别器件移。 | interpretation-and-transfer-boundary | source-plus-task-counterexample | printed714 Eq4 paragraph; printed718 Outlook | true |
| MI07-D17-16 | 当前202305官方Cm245对象给同388.170母态的333.37/388.15均(E1)/MR空，并保1977混合幅度及2015 anomalousE1 ICC解释。它限制将本文pureE1假定跨版本当独立测得δ0，不证明本实验Q失败，也不从electronanomaly直接重标gammaP。 | evaluated-reference-companion-boundary | cross-source-synthesis | N245-2; N245-3; N245-4; N245-5; printed715 Sec3.1 | true |

## Summary

Miller *et al.* establish a practical side-irradiated SeGA polarization calibration for fast-beam spectroscopy. It confirms that segmented arrays can access parity-sensitive polarization while preserving Doppler capability, but the `Q` and figure-of-merit values remain detector-, energy- and geometry-specific.

## Competing Interpretations and Limitations

- The 333/388-keV `249Cf` calibration uses pure E1 transitions and source-specific angular distributions; response at higher energies and in-beam backgrounds remains untested here.
- The 30% figure-of-merit uncertainty includes estimated photopeak efficiency; it is not a universal SeGA constant.
- A measured polarization sign still requires known multipolarity/angular distribution before assigning electric or magnetic character.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| MI07-AR-1 | Response chain | α–γ known `P` → segment counts/asymmetry `A` with geometric `a` correction → `Q=A/P`; finite detector angle averaged. | PDF Eqs.1–12, pp.714–717 | self-checking |
| MI07-AR-2 | Performance chain | `Q²` times coincidence efficiency → figure of merit; compare only after equal energy/geometry definitions. | PDF Eqs.13–14, Table 1 | self-checking |
| MI07-AR-3 | Transfer condition | Recalibrate `a`, `Q`, thresholds, scattering selection and background for any fast-beam in-beam use. | PDF pp.716–718 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[compton-polarimetry]], [[linear-polarization-asymmetry]] and the detector-response lineage from Jones/Starosta/Schmid.
- New reusable rule: side irradiation changes response geometry; retain detector orientation when comparing `Q` or parity sensitivity.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `MI07-P0-1`: Do not transfer `Q≈0.14` or `FM≈5.9×10^-6` outside the tested SeGA side-irradiated setup without recalibration.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]]。

## Day17原件复核：侧入射a合同与5000全峰计数

先冻miller2007-before/exercise、声明旧摘要priming后，原6页713–718完整text/visual、Eq1–14/Fig1–8/Table1/15refs新读；371472bytes/hash `a334ee35a84ded50f6a7937c037ee13d2d06b2f8406b0c68fac1a4245999acf3`保持。旧MI07-1–4/flags/citationkeyverified metadata保，13新待审。回忆中怀疑a是offset已由原Eq5排除：它确是方向计数ratio，且反ST99；不把a≪1当误转或物理P。

[[polarimetry-shared-calibration-count-design]]“SeGA2007：a的倒数约定与5000全峰计数”保存actualfractions/σ设计、eff分母与ADreference readiness。knowna/Q的计数控制支持作者约.3量级，不认证原实际CI；σa多来自unitspread，sample .009不能直接独立加到每target。四groupP/finiteangle/388顺序边界原样保；本session未取得fullacceptance/persegmentcut/ordering/fitCov，未自由改Q或重拟合source。

决定`supports`实际sidegeometry可以polarimetry、`limits`跨energy/inbeam/array和Table1裸merit转用。sameparent两E1 oppositeP是sourcecontrol，不是两独立标定谱系；与Jones2002/Falk1970方法/历史参考须保依赖。没有新核Jπ/δ/P实验测量或现代fastbeam响应认证。

新pointQ上界问题的定向primarycompanion为[[garciaraffi-1997-monte-carlo-compton-polarimeters]] GR97-D17-1–4（本session只新读462/466两页），新推导在[[compton-polarimetry]]“90度点参考不是全角最大分析能力”；本MI07完整6页scope和实际标定值不变。

### Cm245官方参考的新输入

[[nndc-2023-cm245-cf249-polarization-reference]] N245-1–15是本session新获取的202305评价两个完整对象，不是本篇2007实验的独立Q验证。保当前(E1)/空MR、旧无显式号MR评论、分壳转换异常与BrIccmodel列；未取得2015/1977primarybody/phase/实际SeGAΣ，不能据此给新的P/Q修正或作parity重裁。
