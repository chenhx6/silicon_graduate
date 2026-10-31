---
type: source
title: "von der Werth et al. 1995 - Two Compton polarimeter constructions for modern standard gamma spectroscopy"
aliases: [von der Werth 1995 POLALI MINIPOLA]
created: 2026-09-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: method-paper
reading_depth: deep-read
title_original: "Two Compton polarimeter constructions for modern standard γ-spectroscopy"
authors: [A. von der Werth, F. Becker, J. Eberth, S. Freund, U. Hermkens, T. Mylaeus, S. Skoda, H. G. Thomas, W. Teichert]
journal: "Nuclear Instruments and Methods in Physics Research A"
year: 1995
volume: 357
pages: "458-466"
pii: "0168-9002(95)00025-9"
canonical_source: "von der Werth et al., NIM A 357, 458-466 (1995)"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1995_Von Der Werth et al_Two Compton polarimeter constructions for modern standard γ-spectroscopy.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1995_Von Der Werth et al_Two Compton polarimeter constructions for modern standard γ-spectroscopy.pdf"
raw_sha256: "54db57f926f99e069186e99a5b373ef5cb79f234eec43cc6ff84c82e80563021"
nuclei: [56Fe, 24Mg, 28Si, 66Zn, 67Zn]
reactions: [56Fe(p,pγ), 24Mg(p,pγ), 28Si(p,pγ), 66Zn(alpha,nγ), 67Zn(alpha,nγ)]
experiments: [cologne-polali-minipola]
models: [klein-nishina-response]
observables: [polarization-sensitivity, coincidence-efficiency, figure-of-merit, Compton-asymmetry]
methods: [compton-polarimetry, kinematic-Compton-gate]
tags: [POLALI, MINIPOLA, Compton, detector-response, Euroball]
---

# Two Compton polarimeter constructions for modern standard γ spectroscopy

## Bibliographic Record

- A. von der Werth *et al.*, *NIM A* **357**, 458–466 (1995), PII `0168-9002(95)00025-9`。
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1995_Von Der Werth et al_Two Compton polarimeter constructions for modern standard γ-spectroscopy.pdf`。
- 9-page method paper; title/PII, POLALI/MINIPOLA schematics, technical tables and calibration figures checked.

## Scope and Reading Depth

- PDF pp.458–466 fully read: five-detector POLALI, four-segment planar MINIPOLA, Klein–Nishina/asymmetry formalism, kinematic gate Eq.(8), Tables 1–3, Figs.1–10 and conclusions.
- Not covered: raw calibration matrices and modern Monte Carlo response.

## Method Logic and Key Evidence

- POLALI: a low-efficiency central HPGe scatterer plus four analyzers parallel/perpendicular to the reaction plane; list-mode `E_s,E_c` data are summed and gated by Compton kinematics (`θ∈70°–110°`) to reject multiple-scatter/background events.
- MINIPOLA: four-segment planar Ge in an anti-Compton shield; high coincidence efficiency but no unique scatterer/absorber ordering, so the full kinematic gate cannot be applied.
- Calibration uses known E2/E1/M1-E2 transitions (56Fe/24Mg/28Si and reactions on66/67Zn producing69/70Ge, as Table3/Fig8 specify) to derive `Q=A/P`, geometric asymmetry and coincidence efficiency. Figure of merit is `F=Q²ε` (paper's notation).
- The paper reports POLALI high `Q` with lower efficiency and MINIPOLA lower `Q` with compact high efficiency; both are designed as modular devices for OSIRIS/NORDBALL/EUROBALL-era arrays.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| VW95-1 | POLALI and MINIPOLA implement complementary sensitivity–efficiency compromises for modern γ arrays. | method-result | direct | PDF pp.458–462, Figs.1–5, Tables 1–2 | true |
| VW95-2 | POLALI's Compton-kinematic gate (`70°–110°`) suppresses multiple-scatter/background and raises sensitivity. | detector-response | direct | PDF pp.461–462, Eq.(8), Fig.6 | false |
| VW95-3 | `Q`, efficiency and `F=Q²ε` are calibrated across 0.18–2.5 MeV with known-polarization reactions and remain geometry/threshold specific. | method-validation | direct | PDF pp.462–466, Tables 2–3, Fig.10 | true |

## Summary

The POLALI/MINIPOLA paper is a practical detector-design bridge between historical Ge(Li) polarimeters and modern segmented arrays, explicitly separating sensitivity, efficiency, kinematic gating and figure of merit.

## Competing Interpretations and Limitations

POLALI's response depends on geometry, gate, threshold and gain matching; MINIPOLA's segmentation loses scatter-order information. Calibration lines and quoted `Q/F` values cannot be transplanted to another array without response simulation.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| VW95-AR-1 | Response chain | Compton energies → kinematic angle gate → coincidence asymmetry → `Q/P` and `F`. | PDF pp.461–466 | self-checking |
| VW95-AR-2 | Transfer condition | Detector-specific `Q(E)`, efficiency and gate; modern use requires geometry and multiple-scatter audit. | Tables 1–3/Fig.10 | self-checking |
| VW95-AR-3 | Failure condition | Unordered MINIPOLA scatter, crosstalk, thresholds and background can bias asymmetry. | PDF pp.460–463 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[compton-polarimetry]] and historical detector-response lineage with Garcia-Raffi 1995/1997 and Bass 1972.
- Persistence: update Compton method map and modern-array response protocol.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `VW95-P0-1`: POLALI/MINIPOLA `Q`, efficiency and `F` are device-specific; no universal calibration.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]]。


## Day17原件自审：ordering、信号通道与校准核身份

本session先冻primed回忆，新读完整9页/14图/3表/19式/12refs text+visual，hash54db57f926f99e069186e99a5b373ef5cb79f234eec43cc6ff84c82e80563021/839074bytes保。旧VW95-1–3行/true false trueflags和reviewunreviewed保，新14待审。候选池已排Zheng/Simpson旧检查重复；本篇不替两者实际response。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| VW95-D17-1 | POLALI中央scatterer3.9%relativeeff、30mm径/50mm长/10mmhole、四Geabsorber和80mmPb，Table1给source距130mm/solidangle.4%4π。relativeeff不是absolutepeakεa或Comptoncoincεc，不能按标称35%等替F分母。 | hardware and efficiency roles | direct | p.459 Table1/Figs1–2 | true |
| VW95-D17-2 | MINIPOLA16×54×48mm、四p+segments/60–70µmslots，共Li-contact给totalE、sectorpreamps只timing。不能由其actualrecord默认获得每段energy；原不做Eq8gate除orderingunknown外还需实际读出合同，不把新算法补成已存信息。 | actual-signal readiness | direct | pp.460–462 Figs3–5 and Sec3/5 | true |
| VW95-D17-3 | 原137Cs662fullpeakgate/其它segments10cmPb屏蔽，falsecoinc上界10^-6接random背景，验证特定electronicscrosstalkcontrol；不是所有inbeam能量/位置/threshold共享零crosstalk或实验P无系统量。 | failure-control scope | direct | p.460 Sec3 | true |
| VW95-D17-4 | POLALI实际listmode已知Es/E′，Eq8算Comptonθ并取70–110；作者称消约70%peakbelowbackground、Q提高约10%，未给原每cutcount/Cov。它不是计数retention70%、Q=.10或通用效率增益，MINIPOLA不应用同gate。 | actual-gate observable and boundary | direct | pp.461–462 Eq8/Fig6 | true |
| VW95-D17-5 | a(E)以target位置unpolarized226Ra定：POLALI a=(N2+N4)/(N1+N3)，MINIPOLA a=(N12+N34)/(N13+N24)。Q=Aexp/Ptheor另由knownEM/核calibration给，不能用Ra null给Q，也不把samea或pairgroup裸迁clover。 | independent-null and grouped-count dictionary | direct | pp.462–463 Eqs9–12 | true |
| VW95-D17-6 | Table3实际66Zn(α,nγ)69Ge、67Zn(α,nγ)70Ge，p463prose称residual66/67Zn与reactiontable/Fig8不闭；按质量/电荷及Fig8产品辨身份。Table287.2/952.6属69Ge，Fig8 288.0/250.1/357.4属70Ge，不因近能量迁MR或E/M。 | source-identity correction and countercontrol | direct and conservation | pp.462–463 Table3/Fig8 | true |
| VW95-D17-7 | Qfit=Q0(mE+b)，E用MeV，printedPOLALI m7.80(11)×10^-2/MeV,b.79(17)；MINIPOLA m−7.60(13)×10^-2/MeV,b.23(1)，门about60keV。本文只给plotpoints非rawcalA/P/Cov，本session只核centralcurve与units不造CI。 | fit-identity and error boundary | direct | pp.463–464 Eqs12–16/Fig10 | true |
| VW95-D17-8 | 数值apertureintegration把POLALI Δθ70–110/Δφ55与MINIPOLA Δθ60–140/Δφ约120配曲线；作者固定Δθ而调Δφ拟Q，不是完全独立验证response。planeanglewidth对Q影响不能当已测fullkernel/actualeventselection。 | model-input and shared-fit dependence | direct | p.464 Eq17 discussion | true |
| VW95-D17-9 | 原εc Eq18=[(Nparallel+Nperp)/(2Ns)]εa，unpolarizedRa数据；Ns分别scatterersingles或MINIPOLAwholecrystal，εa为absolutepeak而非标称relativeeff。原文字在1.33MeV用Co emittedquanta定义εa，能量曲线recipe未完整给，不补其数值。 | merit-efficiency denominator | direct | pp.464–465 Eq18/Fig11 | true |
| VW95-D17-10 | 本session对九actualEg与70/90/110点由Eq8正反核，swapenergy显示不同解/不物理只是角色反证；不是实际MINIPOLAordering或cutretention。symbolicPhi=Ns/εa时εc=Nsum/(2Phi)仅同source曝光/归一，不自动给inbeam4πrate或countF。 | Codex actual-input kinematic exercise | derived | p.461 Eq8; p.464 Eq18 | true |
| VW95-D17-11 | Sec7.3称MINIPOLA F不及POLALI1/3、Summary又称200keV处twicebetter并另称wholeenergyPOLALIhigher，literal有冲突；Fig12支持scope需逐点核。本session未digitize/强选一段作全能区实测rank，保background/geometry/Σ缺。 | ranking-counterevidence and text-boundary | direct | pp.464–466 Fig12/Sec7.3/Summary | true |
| VW95-D17-12 | neutronexposure前后MINIPOLAresolution变差，Co扫描显示holepath越长FWHM越差，作者解释为holetrapping。response随runstate可变，初Table2resolution不能自动作整个采集恒定response或解释新Pbias。 | actual-response drift | direct and author-interpretation | p.465 Figs13–14/Sec7.4 | true |
| VW95-D17-13 | 原Q/ε/F共同calibrationdata派生，Refs8/9/10提供核EM/P输入；本source引用同CJP1970伴随条目但未body核作者ratio命名，不将引用当取证。实验装置独立于GR95MC，commonknownP/理论不增独立实验信用。 | source-independence and readiness | direct and synthesis | pp.462–466 calibration/references | true |
| VW95-D17-14 | 原低能约180界含CFD/aluminiumabsorption，actual门about60/宽角接受与能量gain有域；本次无原counts/sorter/波形/responseΣ，noactualMC或新P/Q/merit/CI/核δ/Jπ。 | limits and knowledge-impact | synthesis | pp.458–466 full scope | true |

[实际线/运动学合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/vonderwerth1995-gate-contract.json)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/vonderwerth1995-gate-result.json)，script `system/scripts/day17_vw95_gate_audit.py`。九个calibrationγ能量来自原Table3，knownorderpointkinematics只核单位/EsE′角色，不把原近阈值响应点换理想pointQ。

本次`revises`旧Znresidual含混、`limits`ordering算法能补未记录energy/merit全能排行与单次crosstalkcontrol迁移，`supports`actualsignal-first门合同。关联[[compton-polarimetry]]、[[linear-polarization-asymmetry]]、[[polarimetry-shared-calibration-count-design]]及[[schlitt-1994-sectored-compton-polarimeter]]。
