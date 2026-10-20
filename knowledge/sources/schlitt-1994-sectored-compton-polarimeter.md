---
type: source
title: "Schlitt et al. 1994 - Sectored Ge Compton polarimeter for parity assignments"
aliases: [Schlitt 1994 sectored Ge polarimeter]
created: 2026-09-21
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: method-paper-and-application
reading_depth: deep-read
title_original: "A sectored Ge-Compton polarimeter for parity assignments in photon scattering experiments"
authors: [B. Schlitt, U. Maier, H. Friedrichs, S. Albers, J. Bauske, P. von Brentano, R. D. Heil, R.-D. Herzberg, U. Kneissl, J. Margraf, H. H. Pitz, C. Wesselborg, A. Zilges]
journal: "Nuclear Instruments and Methods in Physics Research A"
year: 1994
volume: 337
pages: "416-426"
pii: "0168-9002(94)91111-8"
canonical_source: "Schlitt et al., NIM A 337, 416-426 (1994)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1994_Schlitt et al_A sectored Ge-Compton polarimeter for parity assignments in photon scattering.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1994_Schlitt et al_A sectored Ge-Compton polarimeter for parity assignments in photon scattering.pdf"
raw_sha256: "d23380e6a8bea4be9e77c845ba125f3b934765744bad6a1f300a3301aae07684"
nuclei: [106Pd, 24Mg, 28Si, 12C, 162Dy]
reactions: [106Pd-gamma-gamma, 24Mg-p-p-gamma, 28Si-p-p-gamma, 12C-p-p-gamma, NRF]
experiments: [fourfold-sectored-Ge, Stuttgart-Dynamitron]
models: [Klein-Nishina, angular-correlation]
observables: [polarization, parity, Q, figure-of-merit, Compton-asymmetry]
methods: [Compton-polarimetry, photon-scattering]
tags: [sectored-Ge, Compton-polarimeter, parity, NRF, polarization]
---

# Sectored Ge Compton polarimeter for parity assignments

## Bibliographic Record

- B. Schlitt *et al.*, *NIM A* **337**, 416–426 (1994), PII `0168-9002(94)91111-8`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1994_Schlitt et al_A sectored Ge-Compton polarimeter for parity assignments in photon scattering.pdf`。

## Scope and Reading Depth

- PDF pp.416–426 fully read: polarization formalism, fourfold single-crystal Ge design, `Q(E)` calibration with `106Pd`/`24Mg`/`28Si`/`12C`, figure of merit, NRF `162Dy` application and appendix two-detector proposal.
- Not covered: raw calibration spectra and later tracking-array implementations.

## Key Results

- A true coaxial p-type Ge crystal with four insulated outer sectors provides horizontal/vertical Compton coincidences while the core measures total incident energy; apparatus asymmetry is below about 1% at 2–4 MeV (PDF pp.417–420, Figs.5–6).
- 原150-keV门Table3的4438-keV Q为7.93(.31)%、Eq25拟合约7.954%；Table4总述约9.5%@4.4MeV未明同一threshold，不能合并成150keV值。原fit a=.304(.016)、b=8.9(.8)×10^-5keV^-1，Cov未给，见SC94-D17-5/6。
- 原coinceff约25%@3MeV/260keV门，分母是detectedcorefullpeakNs；merit另用绝对εcoinc(25cm)。Table4“total25%@1332”不等已给25cm绝对peakprobability，未在原件明确其reference标准，不拿它替merit分母。coreenergy直接给入射总能，见SC94-D17-2/3/8。
- NRF `162Dy` spectra demonstrate parity assignments: positive azimuthal asymmetry corresponds to M1/positive parity and negative to E1/negative parity, with weakly polarized lines suppressed in the difference spectrum (PDF pp.423–425, Figs.15–16).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SC94-1 | Fourfold sectored Ge provides a compact high-efficiency Compton polarimeter for NRF parity assignments. | method-result | direct | PDF pp.416–420, Table 4 | true |
| SC94-2 | `Q(E)` declines from ~20% at 0.5 MeV to ~9.5% at 4.4 MeV for the tested thresholds/geometry. | calibration-result | direct | PDF pp.421–423, Table 3, Fig.11 | true |
| SC94-3 | NRF `162Dy` parity signs are demonstrated with sum/difference spectra. | application-result | mixed | PDF pp.423–425, Figs.15–16 | true |

## Summary

Schlitt *et al.* establish a sectored-Ge polarimeter optimized for photon-scattering parity assignments. It trades some sensitivity against high coincidence efficiency and energy resolution, making detector geometry, thresholds and calibration central to any parity claim.

## Competing Interpretations and Limitations

- `Q(E)` and figure-of-merit values are geometry/threshold dependent; finite solid angle shifts the ideal Klein–Nishina analyzing power.
- Polarization sign determines parity only with known angular distribution/multipolarity and response correction.
- The NRF application is not equivalent to in-beam fusion-evaporation clover polarimetry; reaction-plane and alignment conventions differ.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| SC94-AR-1 | Response chain | Sectored Compton H/V events → asymmetry `ε=QP` with `a(E)` correction → parity sign. | PDF Eqs.1–17, pp.417–423 | self-checking |
| SC94-AR-2 | Performance chain | `Q² ε_coin` → figure of merit; compare only at common energy/threshold. | PDF Eqs.26, Table 4 | self-checking |
| SC94-AR-3 | Transfer condition | Recalibrate geometry, thresholds and reaction-plane convention for modern arrays. | PDF pp.423–426 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[compton-polarimetry]], [[linear-polarization-asymmetry]] and historical detector-response map.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `SC94-P0-1`: Preserve detector/threshold/NRF convention boundaries; do not transfer `Q` or parity sign directly to another geometry.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]]。


## Day17原件自审：实测校准的门与绝对效率分母

本session先冻primed回忆，新读完整11页/18图/4表/30式/33refs text+visual，hashd23380e6a8bea4be9e77c845ba125f3b934765744bad6a1f300a3301aae07684/868962bytes保持。旧SC94-1–3行/needs_reviewtrue与reviewunreviewed保持；新16条待审，不称human-reviewed，不以GR95重复引用新增实验。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SC94-D17-1 | 原polarimeter是truecoaxialpGe、fouroutersector+core，core直接给fullE；H/V Eqs18/19为指定两sector触发且另两否决的布尔组合，不是任意两扇区sum。原aV−H/sum式10、P=ε/Q的计数对象需sameeventselection。 | actual-count and hardware contract | direct | pp.419–420 Fig5/Eqs18–19 | true |
| SC94-D17-2 | relativecoinceff Eq22=(V+H)/Ns，Ns为无coinc条件的corefullpeakdetectedcounts；约25%@3MeV/260keV门，150/260/370各不同。它不是incidentphoton绝对概率，不能裸入F或与GR95ε同名便比较。 | efficiency-denominator correction | direct | pp.420–421 Eq22/Fig7 | true |
| SC94-D17-3 | meritEq26明确F=ε_abs_coinc Q²，Fig13数值用source距25cm/260keV门；ε_abs_coinc=ε_abs_corefullpeak×ε_relcoinc需同门。Table4总ε25%@1332未在原文详给reference标准，不能自动当25cmabsolutepeakfraction。 | absolute-merit input boundary | direct and algebra | pp.423–425 Eq26/Fig13/Table4 | true |
| SC94-D17-4 | unpolarized56Co测a=H/V=.9899±.0052，Fig6门260keV、energy/threshold内近常数；若漏a修正，按中心算rawnull A=(1−a)/(1+a)约.00508而非1−a。作者online可近a1是实用判断，不取消精密分析的共享校准Cov。 | actual-null and normalization boundary | direct plus arithmetic | p.420 Eqs20–21/Fig6 | true |
| SC94-D17-5 | Table3六点均150keV门，ε/P重算Q为21.2245/14.6263/11.7162/10.8485/7.9059/7.9293%，近印Q而不新拟合；作者ε/P/Q同chain非三份独立测量，rawfitCov未给。 | actual-calibration arithmetic | derived | p.423 Table3 | true |
| SC94-D17-6 | 原Eq25 a=.304±.016、b=8.9±.8×10^-5keV^-1仅150keV门，Eq16/17核4438nominalQ7.95364%，Table3为7.93(.31)%；Table4约9.5%@4.4未明同门。旧Wiki合并150门/9.5已纠，不改原总述或造curveCI。 | threshold-version correction | direct plus arithmetic | p.423 Eqs25/Table3; p.425 Table4 | true |
| SC94-D17-7 | 106Pd622tag→512probe的0–2–0在90°nominalP1；正文报ε/Q20.8(2.0)%，Table3实际用P98(1)%得Q21.2(2.0)%。180°difference近null且作者说明finiteNaIacceptance；本篇没有数值P98校正recipe，不能把nominal1和actualTableinput硬当同值。 | actual-reference gate and finite-geometry boundary | direct | pp.421–423 Fig8/Sec4.3.1/Table3 | true |
| SC94-D17-8 | 150门calibrationP部分引用B73 Ref27的Mg1368/C4438 AD/P，故装置测量独立但核偏振标尺共源；Si1778为不同p,p'energy/AD等，不能与B73/EW69同γlabel自动视同P。实际source/thesiscalibrationRefs25/26未取得body。 | source-independence and calibrator identity | direct | p.422 Table2; p.426 Refs25–27 | true |
| SC94-D17-9 | highersector门Q升但εrel降，实测Fig14F在此域近constant而非总更优；GR95用此实验作模拟比较仍须sameenergy/solidangle/absoluteε/门。原BGOshield在near future是预期而非本文已测新F增益。 | threshold and comparison counterevidence | direct | pp.423–425 Figs12–14/Summary | true |
| SC94-D17-10 | NRFTable1的E1/M1 sign只pureelastic0→1→0、unpolarizedincident、90°reactionplane及校准Q合同，E2 0→2→0也P+1但需已知L。DygroundM1positive/E1negative，不能移fusionPsign直接指定δ/Jπ/模式。 | necessary-NRF assumptions | direct | p.417 Table1; pp.424–425 Figs15–16 | true |
| SC94-D17-11 | Dy差谱27Al(P≈1.5%)消失、inelastic2+branch减弱，是低P/选择role而非无该线；Fig16caption把E1也印ε>0，与正文/图下面E1负号不闭合，保literal不改data或判实验矛盾。 | null-companion and caption-boundary | direct | pp.424–425 Figs15–16 | true |
| SC94-D17-12 | Appendix两detector方案是作者分析calibration后才提出，未在本次实验使用；R是AD强度比Wθ1/Wθ2，不是TW70polarimeterR或ComptonQ，Eq30是其近似函数，不能冒actual校准数据。 | proposal-versus-experiment and notation | direct | pp.425–426 Appendix/Eqs27–30 | true |
| SC94-D17-13 | 原Eq28印35(P+3)cos⁴θ−3(7P+35)cos²θ=0，无常数项；literalP0角0/90，P1角18.435/90，不能闭quoted23.5–28.6/66.5–68.9。原式保留不称officialerratum。 | source-literal formula failure | direct plus calculation | p.426 Eq28 | true |
| SC94-D17-14 | 新从Eq23/24或27对a2微分独立得同多项式+14=0，P0角23.4556/66.5444、P1角28.6475/68.8790且fixedP不同a2交点相同，内部闭合原quoted域。此derivedcandidate不是原producer/已建方法，formalWfamily不自动是实测正population。 | independent symbolic consistency test | derived | p.426 Eqs27–28 | true |
| SC94-D17-15 | derived交点的R在P.5为1.306667、P1为1.566727，对Eq30近似1.305525/1.5649有小差，保approx而不调角。声明54mmface/250mm距的solidanglefraction≈.002891只unituppercontrol，非本文absoluteeff；不由total25%造F。 | approximation and efficiency sanity control | derived conditional | p.419 Fig5; p.426 Eqs29–30 | true |
| SC94-D17-16 | fullsource新算术与附录核不替原counts/finitegeometrycalibration/Σ，未新测P/Q/merit/NRFparity或CI；source“Scissors/两phonon”解释与observedsign分层。 | readiness and knowledge-impact | synthesis of scopes | pp.423–426 applications/conclusion | true |

[六点/分母/附录输入](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/schlitt1994-calibration-contract.json)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/schlitt1994-calibration-result.json)，script `system/scripts/day17_schlitt1994_calibration_audit.py`。附录constant14由符号微分/固定P相交测试给出，不覆写raw Eq28；不把源打印failure当原实测校准全失效。

本次`revises`旧Wiki阈值/Q和eff分母合并，`limits`NRFsign迁移/同标尺重复信用/附录作已测结果；[[compton-polarimetry]]、[[linear-polarization-asymmetry]]、[[polarimetry-shared-calibration-count-design]]与[[garciaraffi-1995-nonorthogonal-compton-polarimeter]]保sameinput比较。
