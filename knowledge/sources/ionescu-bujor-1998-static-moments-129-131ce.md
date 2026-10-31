---
type: source
title: "Static electromagnetic moments and nuclear shapes in 129,131Ce"
aliases: ["Ionescu-Bujor 1998 Ce moments", "129Ce 131Ce TDPAD shapes"]
created: 2026-09-20
updated: 2026-10-23
status: ai-draft
review_status: unreviewed
source_type: experiment
reading_depth: deep-read
title_original: "Static electromagnetic moments and nuclear shapes in 129,131Ce"
authors: ["M. Ionescu-Bujor", "A. Iordachescu", "F. Brandolini", "M. De Poli", "N. H. Medina", "P. Pavan", "M. N. Rao", "C. Rossi Alvarez"]
journal: "Nuclear Physics A"
year: 1998
volume: 633
pages: "459-478"
doi: "10.1016/S0375-9474(98)00157-2"
citation_key: Ionescu_Bujor_1998
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
language: en
canonical_source: "Ionescu-Bujor, M. et al. Static electromagnetic moments and nuclear shapes in 129,131Ce. Nucl. Phys. A 633, 459-478 (1998)."
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/形变/1998_Ionescu-Bujor et al_Static electromagnetic moments and nuclear shapes in 129,131Ce.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/形变/1998_Ionescu-Bujor et al_Static electromagnetic moments and nuclear shapes in 129,131Ce.pdf"
raw_sha256: "2735874b2be1116741f421a114ffa5995be93c99891ed284d962b53f0446484b"
nuclei: ["129Ce", "131Ce", "128Ce", "130Ce"]
reactions: ["116Sn(16O,3n)129Ce", "119Sn(16O,4n)131Ce"]
experiments: ["lnl-tpad-129-131ce-o16-70mev"]
models: ["particle-plus-triaxial-rotor-model", "BCS-pairing"]
observables: ["g-factor", "quadrupole-moment", "TDPAD", "signature-splitting", "level-energies", "alignment"]
methods: ["time-differential-perturbed-angular-distribution", "g-factor-measurement", "angular-distribution"]
tags: [129Ce, 131Ce, TDPAD, static-moments, triaxiality, shape-evolution, odd-mass]
---

# Static electromagnetic moments and nuclear shapes in 129,131Ce

## Day20本session实际原读：静态矩与模型依赖（checkpoint104）

primed-recall-104在本轮开原件前冻结，已明示用户摘要、旧085及本日模型反例的priming。本次实际读取20页全文（459–478，含references），全部11图与2表、Eq1–6均作page-level视觉检查；Fig7额外旋正。没有逐线digitize、重拟合events，亦未取得原PTR代码/fit Cov或所引校准primary全文。scope与指纹见本日run02/source-reading-scope-104.json。旧全文scope不代替本次阅读，本文仍是同一实验而非新增独立证据；原review/flags保持。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| IB98-D20-R104-1 | QI用厚116/119Sn多晶靶完全停止；MI用.6mg/cm²的116/119Sn蒸镀在厚Pb箔，外场14.6(4)/32.0(8)kG，每约10min翻转。束脉冲宽3ns、周期800ns、time resolution约11ns，不能混作寿命或调制周期。QI需CeSn室温EFG Ref14；MI需Ce/Pb室温local susceptibility1.40(2) Ref13。 | actual-host-and-calibration-lineage | direct-original-and-visual | printed460–461/PDF2–3 §2; printed463/PDF5; printed464/PDF6 Eq4/5 | true |
| IB98-D20-R104-2 | QI拟合给νQ129=52.6(14)、νQ131=36.4(16)MHz；129观察完整T0=456(12)ns，131只观察调制起始结构。Eq1 T0=2J(2J−1)/(3νQ)在J=9/2下为24/νQ。半衰期为60(2)/88(2)ns，平均寿命须另除ln2；QI取向relax约.2–.3µs。不是同一时间参数，也不把原两个χ²13.9/2.7重造p或CL。 | coupling-period-lifetime-relaxation-separation | direct-original-and-conditional | printed462/PDF4 Eq1–3; Figs1/2 PDF5/6 | true |
| IB98-D20-R104-3 | 原实测静态矩绝对值1.32(13)/.92(10)eb；|Q129|/|Q131|=1.44(7)由作者称独立于EFG标定。共享同一乘性标定时中心频率比可重现约1.445，不能凭两绝对误差独立传播就恢复原ratio Cov。QI的模值不独自测得正号或真实K。 | absolute-moment-and-ratio-calibration-boundary | direct-original-and-derived | printed463/PDF5; printed466/PDF8; Table1 printed472/PDF14 | true |
| IB98-D20-R104-4 | g129=−.185(10)、g131=−.189(7)来自MI的cos2(φ−ωLt)拟合与外场/local susceptibility；MI relax约100/250ns。作者说小负g支持h11/2中子描述，不是排他组态/几何测量；模型内不同K混合仍可给相近g。 | magnetic-moment-versus-configuration-inference | direct-original-and-visual | printed464–466/PDF6–8 Eq4/5 and Fig3; printed472/PDF14 | true |
| IB98-D20-R104-5 | PTR采用modified oscillator+BCS、hydrodynamic惯量、gs_eff=.6gs_free与gR=Z/A。Fig4的131Ce Q曲线在γ≈30°附近仍非零，正文称Q略随γ变化并依赖Coriolis ξ；否定旧085把cos3γ当本原文通用Qs压制。Table1同一实验131Ce分别以ξ=.7,ε2=.14,γ23°或ξ=1,ε2=.18,γ20°描述，K9/2与7/2混合随ξ改变；不是纯K9/2测定。 | actual-PTR-inputs-and-counterevidence-to-universal-Qs-law | direct-original-and-visual | printed466–469/PDF8–11 Fig4/5; printed472/PDF14 Table1 and wavefunction paragraph | true |
| IB98-D20-R104-6 | 129Ce负宇称模型需ε4≈.05–.08，Table1选.07、ε2=.24、γ12°、Ecore2=130keV；131Ce负宇称Ecore2=250keV。Table2正宇称131Ce给ξ1、Ecore2=200、ε2范围.18–.24、γ20°，且正文说尚无决定其g.s.带ε2的实验数据。129Ce g.s. Qt3.5(5)eb为Ref24外源，不是本次TDPAD独立新测量。 | band-specific-model-parameters-and-external-Qt-lineage | direct-original-and-visual | printed469/PDF11 Fig6; printed472/PDF14 Table1; printed473–475/PDF15–17 Table2; Ref24/PDF20 | true |
| IB98-D20-R104-7 | 作者在129Ce提出isomer上11.8keV处的新11/2−态，以重建signature次序；估94keV crossover/82keV主线比约.02，12keV M1可能数ns馈入低于约11ns时间分辨。新态/feeding是作者方案，不能把未分辨feeding当已实测寿命或排除其影响。 | proposed-level-and-unresolved-feeding | direct-original-and-visual | printed469–472/PDF11–14 Fig7/8; especially PDF14 first paragraph | true |
| IB98-D20-R104-8 | PDF9的χ²定义为Σ(Eexp−Ecalc)²，未含逐能量σ或原jointlikelihood；Table1的131Ce gcalc=−.23与exp−.189(7)及作者“agreement”保literal，不补出理论误差或新的联合显著性。PDF15称所引TRSγ的“rapid decrease”与本表129→131的γ12→20/23上升字面并存；未读Ref17完整原件，不静默裁决坐标或笔误。 | literal-model-fit-and-text-tension-boundary | direct-original-and-visual | printed467/PDF9 χ² definition; printed472/PDF14 Table1; printed473/PDF15 TRS sentence | true |

### Knowledge Impact and Learning Decision — Day20 checkpoint104

本次source原读支持static moment、spin-sensitive QI和作者PTR比较；撤回“相近g排他确定组态”“cos3γ64%通用压制”“纯K9/26/11投影是实际producer”及“0.92→2.58→7.30同一形变三相阶梯”。Qs异能态、Singh负宇称高spin逐态Qt、Petrache HD带Q0来自不同态/fit/参数角色，不能直接相除称β或B(E2)跳变。原实验/events、EFG和magnetic calibration primary与PTR producer仍缺；不认证实际CI、唯一形状或模式。

## Bibliographic Record

- 作者：M. Ionescu-Bujor 等；*Nuclear Physics A* 633, 459-478 (1998)。DOI：`10.1016/S0375-9474(98)00157-2`。
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/形变/1998_Ionescu-Bujor et al_Static electromagnetic moments and nuclear shapes in 129,131Ce.pdf`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: PDF pp.459-478 全文；TDPAD QI/MI setup, lifetime/ratio fitting, g/Q extraction, `129,131Ce` spin/parity revision, PTR Hamiltonian/parameters, negative/positive-parity bands, figures/tables and conclusions all read.
- Not covered: cited spectroscopy papers and later lifetime/shape calculations.
- Coverage caveats: deformation parameters are PTR-model optima constrained by measured moments and spectra; they are not direct shape images。

## Paper Question and Scientific Motivation

The paper measures static electromagnetic moments of low-lying `9/2−` isomers in neutron-deficient `129,131Ce`, then uses particle-plus-triaxial-rotor calculations to determine how the odd neutron polarizes the core and how shape changes across two neutrons.

## Experimental and Theoretical Setup

- Reactions: `116Sn(16O,3n)129Ce` and `119Sn(16O,4n)131Ce`, 70-MeV pulsed `16O`, 3-ns pulses every 800 ns.
- TDPAD: quadrupole interaction in polycrystalline Sn foils; magnetic interaction in Sn evaporated on Pb foils with 14.6/32.0 kG external field; planar HPGe at 0°/90°/±135°; time resolution about 11 ns。
- PTR: modified oscillator single-particle space, BCS pairing, hydrodynamic moments of inertia, variable Coriolis attenuation `ξ`, `ε2`, `ε4`, `γ` and core `E(2+)`。

## Key Evidence and Reasoning Chain

1. QI modulation of 108-keV (`129Ce`) and 162-keV (`131Ce`) isomers gives half-lives 60(2) ns and 88(2) ns and strongly favors `J=9/2` over previous `J=7/2` for `129Ce` (`χ²=2.7` vs `13.9`) (PDF pp.461-464, Figs.1-2).
2. QI calibration yields `|Q(129Ce,9−)|=1.32(13) eb` and `|Q(131Ce,9−)|=0.92(10) eb`; MI gives `g(129Ce,9−)=−0.185(10)` and `g(131Ce,9−)=−0.189(7)` (PDF pp.463-465, Table 1).
3. E1 decay from `9/2−` isomers fixes ground states as `7/2+`; this changes earlier `129Ce` ground/isomer assignments and shifts spins in its negative-parity band (PDF p.466).
4. PTR optimum parameters: `131Ce` small `ε2≈0.14-0.18`, `γ≈20-23°`, with `ξ≈0.7-1`; `129Ce` larger `ε2≈0.24`, `γ≈12-14°`, and `ε4≈0.07` needed to reproduce Q and negative-parity structure (PDF pp.466-477, Tables 1-2, Figs.4-11).
5. The Q ratio `Q(129Ce)/Q(131Ce)=1.44(7)` supports a pronounced shape change across two neutrons, but its numerical decomposition into `ε2/γ/ε4` remains PTR-model dependent (PDF pp.466-477).

## Summary

TDPAD moments provide direct spin-sensitive electromagnetic observables for `129,131Ce`. The measurements establish `J=9/2−` isomers, revise the `129Ce` ground-state spin assignment, and show a large quadrupole-moment difference. PTR fits associate `131Ce` with smaller quadrupole deformation and larger triaxiality, while `129Ce` needs larger `ε2`, smaller `γ` and nonzero hexadecapole deformation. This source materially strengthens the `131Ce` shape/systematics context but does not by itself identify the collective mode of its high-spin bands.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| IB98-1 | QI patterns strongly support `J=9/2` for the `129,131Ce` isomers; `129Ce` spin-7/2 fit is substantially worse. | experimental-result | direct | PDF pp.461-464, Figs.1-2 | false |
| IB98-2 | 作者报告经CeSn EFG校准的Q模=1.32(13)/.92(10)eb及MI的g=−.185(10)/−.189(7)；106沿引用链追到上游理论参考矩归一，绝对标尺不宜称无模型，具体实际校准producer/Cov仍未得。 | calibrated-observable-and-source-lineage | direct-report-and-primary-lineage | printed463/465; printed472 Table1; IB98-D20-R104-1/3/4; DA83-D20-3 | false |
| IB98-3 | PTR optimum shapes differ strongly: `131Ce` `ε2≈0.14-0.18, γ≈20°-23°`; `129Ce` `ε2≈0.24, γ≈12°-14°, ε4≈0.07`. | model-result | direct | PDF pp.466-477, Tables 1-2 | true |
| IB98-4 | The two-neutron isotope change produces a large Q-moment ratio `1.44(7)` and a pronounced shape-evolution candidate. | experimental-result/author-interpretation | direct | PDF p.466, Conclusions | true |

## Competing Interpretations and Limitations

- QI/MI moments are direct observables, but mapping them to `ε2`, `γ`, and `ε4` depends on PTR single-particle space, pairing, Coriolis attenuation and core `E(2+)`。
- The rapid shape change is a model-constrained inference; the source does not provide independent lifetimes for every positive/negative band or a model-independent triaxiality measurement。
- `129Ce` level-spin revision changes comparisons to earlier source pages; source lineage must be preserved rather than silently overwriting old assignments。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-IB98-1 | Core reconstruction | TDPAD QI/MI closes a direct moment→spin/parity chain, while PTR converts moments/energies into shape parameters. | PDF pp.461-477 | self-checking |
| AR-IB98-2 | Transfer conditions | Moment evidence transfers to neighboring odd-mass Ce only with matched lattice calibration and TDPAD response; PTR shapes require model re-fit. | PDF §§2-4 | provisional |
| AR-IB98-3 | Failure conditions | Alternative Coriolis attenuation, ε4, core inertia or band assignments can change the extracted shape ranking. | PDF pp.466-477 | active-L3 |
| AR-IB98-4 | Research-question decision | Add to `131Ce`/A≈130 shape evidence map and a candidate L3 comparison of moments versus high-spin collective modes. | Full paper | candidate-L3 |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: `131Ce` pages emphasize high-spin band structures, lifetimes and γ-soft/triaxial competition; this source adds static moments, firm isomer spin evidence and a two-neutron shape-evolution anchor。
- Effect of this source: `supports` and `revises`。
- Persistence decision: update `131Ce` shape project/source links; retain PTR parameters as model results, not direct facts。
- Review state: `unreviewed`; claims self-audited by Codex, not human-reviewed。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[131ce-collective-mode-discrimination]] | Static moments constrain shape inputs for the 131Ce competing-mode map。 |
| methodological-bridge | [[time-differential-perturbed-angular-distribution]]、[[recoil-distance-doppler-shift]]、[[lifetime-method-selection-response-contract]] | TDPAD QI/MI gives direct moment and spin evidence。 |
| supports | [[gamma-soft-vs-gamma-rigid-diagnostics]] | Provides A≈130 odd-mass Ce shape-systematics context, with PTR model boundary。 |

## Human Review Triage

### P0

- IB98-P0-1：`J=9/2` and moment values are direct TDPAD results; `ε2/γ/ε4` are PTR-dependent and must remain separated。

### P1

- IB98-P1-1：`129Ce` spin revision changes historical level labels; cross-source use must preserve old/new assignment lineage。

### P2/P3

- DOI, reaction and page metadata are aligned; no new independent L4 input is present。

## Extracted Pages

- Nuclei: update [[131ce]]/`129Ce` related context only if existing pages support it。
- Bands: no new band page。
- Concepts: [[triaxial-deformation]], [[gamma-soft-deformation]], [[angular-momentum-alignment]]。
- Methods: [[time-differential-perturbed-angular-distribution]]、[[recoil-distance-doppler-shift]]、[[lifetime-method-selection-response-contract]], [[g-factor-measurement]]。


## Day19新原读：半整数自旋与host校准

本session新读PDF1–20完整文本主线，实际视觉核PDF3–8及14：装置、Eqs1–5、Figs1–3、spin/ratio正文与Table1。未把其余模型图算成新视觉复核。原Wiki漏写分母的9−/J9/J7已订为9/2−/J9/2/J7/2；旧review与claim needs_review标志原样保留，不认证其旧审核正确。准备文本/旧方法矩阵的“Cd晶格/液态靶”没有此原文支持，本实验是Sn QI与Sn/Pb MI。raw hash保持2735874b2be1116741f421a114ffa5995be93c99891ed284d962b53f0446484b。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| IB98-D19-1 | 129,131Ce异能态为9/2−，129Ce旧候选为7/2−，地态为7/2+；129Ce QI的7/2与9/2试探χ²为13.9/2.7。后续band spin重排含作者提议的近邻11/2−，不能把该新level当此TDPAD直接观测。 | assignment-and-lineage | direct-original-and-author-inference | PDF4–8 Figs1–3及Sec4；PDF12–14 Fig7/Table1 | true |
| IB98-D19-2 | QI使用厚多晶金属116,119Sn靶，反冲在Sn内停止；MI使用.6mg/cm²Sn蒸镀于厚Pb，14.6(4)/32.0(8)kG外场，每约10min反向。脉冲宽3ns、周期800ns，time resolution约11ns。不是Cd晶格或液体。 | apparatus-fact | direct-original | PDF2–3 Sec2 | true |
| IB98-D19-3 | QI的T0=[2J(2J−1)/3]/νQ，νQ=QVzz/h，随机轴对称EFG的多频pattern用于spin拟合。J9/2因子24；52.6(14)/36.4(16)MHz给周期456.274/659.341ns，前者与原456(12)ns相容。比值给1.44505；仅独立frequency errors控制传播为.07426，与原EFG-free Q比1.44(7)相容。不是新fit。 | frequency-and-reconstruction | direct-and-task-derived | PDF4 Eqs1–3、末段；PDF8 Sec4 Qratio段 | true |
| IB98-D19-4 | 两绝对|Q|为1.32(13)/.92(10)eb，依赖CeSn EFG参考；MI的g为−.185(10)/−.189(7)，使用Ce在Pb的local susceptibility1.40(2)。QI弛豫约.2–.3μs；MI约100/250ns；不同于人口half-life60(2)/88(2)ns。辐射损伤解释是作者推断，旧参考本轮未读。 | calibration-and-distinct-times | direct-original-and-author-interpretation | PDF4–7 Eqs3/5、Figs1–3；PDF14 Table1 | true |
| IB98-D19-5 | 本文νQ约束QVzz，外场进动约束gB_eff，缺EFG/local-field/time-scale不能仅靠高统计给绝对矩。共同EFG在同J同host的ratio中可消，但两绝对Q误差不能当完全独立来重造ratio CI。Qs不等transition Qt，PTR的ε/γ是模型输出。 | calibration-readiness | direct-and-synthesis | PDF4–8；PDF14 Table1；PDF19结论 | true |

Knowledge Impact and Learning Decision：revises整数自旋误录与Cd/液态host误记；supports population lifetime、relaxation、frequency及共用EFG校准分层。与[[grodner-2018-128cs-chiral-g-factor]]为不同核/host/数据的companion；两者不是同level寿命重复测量。[[time-differential-perturbed-angular-distribution]]、[[recoil-distance-doppler-shift]]、[[lifetime-method-selection-response-contract]]与[[lifetime-method-selection-response-contract]]给新响应设计；保留未取得原events、EFG/reference原件和jointCov的边界。

## Day19电四极进动周期与同晶格EFG对消审计

依据独立审计程序 day19_ionescu_bujor_tdpad_audit.py 的 17 项检验与基准输出 ionescu-bujor-tdpad-result-028.json，核准了 Ionescu-Bujor 1998 中四极相互作用（QI）与磁相互作用（MI）测量的定量响应：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| IB98-D19-6 | checkpoint108撤回旧普适平面/Schmidt锁定/EFG完全消除等科学认证。新直接原读及条件边界见IB98-D19-8；原result字节保留，不以算术通过恢复科学结论。 | superseded-certification | corrected-and-boundary | IB98-D19-8 | true |

## Day19量化审计：TDPAD四极微扰因子G22微积分展开、晶格对称性解耦与矩演化定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_tdpad_hyperfine_decoupling_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/tdpad-hyperfine-decoupling-result-071.json`，核准了针对 Ionescu-Bujor 1998 多晶电四极相互作用与晶格微扰的动力学审计：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| IB98-D19-7 | checkpoint108撤回旧普适平面/Schmidt锁定/EFG完全消除等科学认证。新直接原读及条件边界见IB98-D19-8；原result字节保留，不以算术通过恢复科学结论。 | superseded-certification | corrected-and-boundary | IB98-D19-8 | true |


## checkpoint108：身份、频率与校准的直接原读纠正

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| IB98-D19-8 | 本轮实际文本读2–8、视觉4/5/7。QI厚多晶Sn、MI Sn/Pb，half60(2)/88(2)ns；129Ce T0约456ns，131Ce约659ns且只见pattern起始，人口tau并不须大于完整周期。ratio1.44(7)按源独立于共同EFG绝对校准，不能断言所有site/温度/损伤系统全消。MI g使用local susceptibility1.40(2)，作者用缺陷四极相互作用解释MI较短弛豫，fcc Pb不保证实际EFG严格0；近g不证明Schmidt锁定。Qs与另一stateQt不能构造直接shape阶梯。 | direct-scope-and-correction | direct-original-and-bounded-arithmetic | PDF2–8; PDF4–7 Eqs1–5/Figs1–3; PDF8 Qratio | true |

## checkpoint110：完整原件主线与PTR输入、未分辨feeding范围

本轮实际文本补读PDF1、9–20，与108的PDF2–8组成该20页原件的完整文字阅读。当前视觉累计PDF4–7、9–14、16–19，覆盖Figs1–11、Tables1–2、Eqs1–6与Fig7的原/建议能级图（旋转核对）。全scope见source-reading-scope-110.json；没有复跑PTR代码或原TDPAD fit，也不把20页已读当所有历史primary已读。旧review/needs_review保持。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| IB98-D19-9 | Table1给131Ce的两套PTR输入：xi.7、E2core250keV、epsilon2.14、gamma23deg、Qcal+.91eb；xi1、epsilon2.18、gamma20deg、Qcal+.93eb；两者gcal均−.23，而gexp−.189(7)、absQexp.92(10)保原。文中xi1含K9/2与7/2近等幅，减弱Coriolis增K9/2幅而增Q；129Ce需epsilon4.07并改变K混合得到Qcal1.34。故不能将pureK轴对称Qs->Q0换算当作者实测内禀矩，也不把拟合shape坐标当直接观测。 | model-input-and-state-boundary | direct-original-model | PDF9–14 Figs4–8/Table1 | true |
| IB98-D19-10 | Fig7b为作者建议的129Ce新11/2−，在9/2− isomer上方11.8keV，用近12keV成对线和signature重排作支持。PDF14估计12keV M1单粒子half.14ns、plausible为数ns，并称约11ns时间分辨下未辨这段feeding；94keV crossover约2%是估计，不是新TDPAD直接发现或新寿命测量。 | proposed-level-and-response-limit | direct-original-author-inference | PDF12–14 Fig7 and first paragraph PDF14 | true |
| IB98-D19-11 | Eq6的S(J)为相邻/跨二级能量差乘转子spin因子再减1，不是任意其他页S432定义；pureE=A J(J+1)+const时该S精确为0。Table2中131Ce positivegs epsilon2=.18–.24、gamma20deg，正文称缺该gs能确定epsilon2的实验数据；结论.14–.18概括与表中角色分开保留。PDF15称TRS的gamma decrease，Table1/结论为129约12deg、131约20deg；保字面，不猜erratum或改上游来源。 | diagnostic-definition-and-literal-boundary | direct-original-and-task-algebra | PDF9 Eq6; PDF15–19 Table2/Figs9–11/Conclusions | true |

## checkpoint033：观测量身份与形状约定原读纠正

本次为定向原文/表图self-audit，非新增独立实验或全文认证；原review和claim flags保持。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| IB98-D20-R33-1 | 绝对|Qs|129/131Ce1.32(13)/.92(10)eb依共同CeSn EFG；PDF8给不依该绝对EFG的矩比1.44(7)。不能将两个绝对Q误差当独立以认证同一ratio精度；旧018的.207匹配.07断言撤回。9/2−的静态矩不同于高spin转变Qt。 | calibration-and-observable-boundary | direct-original | PDF5 absoluteQ paragraph; PDF8 Sec4 ratio paragraph | true |
| IB98-D20-R33-2 | PDF9 Fig4/正文表明131Ce9/2−的PTR Q依ε2、γ和Coriolisξ；PDF14 Table1两套ξ=.7/1、ε2=.14/.18、γ23/20度给Qcal+.91/+.93eb。不能把pureK1/2轴对称候选Q0=2.53eb说成作者实测内禀矩，也不把2.57894eb加权常数诊断叫Singh RDM单点。 | PTR-versus-axial-conversion | direct-original-and-visual | PDF9 Fig4/Sec4.2.1; PDF14 Table1; SI16-D20-R33-2 | true |


### checkpoint105：校准编译与primary身份

[[vianden-1987-electric-field-gradients-metals]] VI87-D20-1–4实际定向读Ref14的定义页、Ce/Sn三行及其Ref371：134/136/138Ce均为同一Dafni1983引用，非三份独立EFG标定；原νQ绝对值与Q参考、293K/(T)列语义分开。IB98模值比的共同EFG相消保留条件，但实际频率/Cov/relaxation输入不由编译表恢复。磁校准Ref13 Barth1980目前仅metadata，官方正文获取403/401，不能声称已读。


### checkpoint106：known EFG的可见参考链含模型锚

[[dafni-1983-ce-isomers-tin-quadrupole]] DA83-D20-1/3/7实际全文明确：数据本身不能定绝对Q或符号，138Ce77e·fm²及e_eff1.87为模型归一且跨质量区迁移需谨慎。经Vianden Ref371可追到此上游；所以当前可见CeSn绝对标尺含模型输入，不能把本页Q模称完全无模型形变图像。只给定ν13830.6MHz/Q138.77eb即可条件重现本页两中心约1.32359/.91595eb，但不唯一识别本文采用标定/原producer、不恢复CI或宣称实验失效。相同host/标尺下的129/131模值比仍是不同层次约束。原IB98-1/2历史false flags保留，不代表本次自审晋升human-reviewed。


### checkpoint107：磁场增强的相关原读与两类松弛

[[barth-1981-ce-local-moments-metals]] BA81-D20-1–7新读10页，136Ce(10+)温度扫描在Curie模型下同时给g_N与B(0)，298K/Pb条件计算β≈1.401与本页1.40相容；不是已识别本1998实际标定producer或Cov。原会议讨论承认温度无关项未纳入，不能视为实测零。核态half-life、核取向τ_N、电子τ_J保持不同；原PRL1980正文仍未得，1981相关account不计独立实验。
### checkpoint145：轴对称转子角动量投影、同核静态矩对决转动四极矩闭合核验

> checkpoint146：本节121–145批次的科学认证已撤回。旧文本/输入与指纹保存在本run的history-before-repair-146.json；原始原件与既有review/flags保留。自设数值或flag的passed只验证算术，不识别实际producer、共同Cov、实验CI或唯一模式。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| IB98-D20-R145-1 | checkpoint146撤回旧认证；不据此恢复错误表值、跨态强度阶梯、硬阈值或完全闭合。请使用本页较早原件纠错与checkpoint146。 | withdrawn-task-certification | rejected-and-replaced | checkpoint146; history-before-repair-146.json | true |

## checkpoint146：原件身份与推断边界更正

本轮为Codex定向self-audit；已有review_status与原claim flags不变。121–145旧认证撤回；实际新阅读范围见source-reading-scope-146.json，引用较早纠错不冒称新全文阅读。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| IB98-D20-R146-1 | 本轮定向原件文字/视觉确认：131Ce的9/2−异构态abs(Qs)=0.92(10)eb，129Ce为1.32(13)eb。Table1的+1.34eb是129Ce的Qcal模型值，不是131Ce实测1.34(20)。145输入错误，Z=.320及静转闭环认证撤回。 | direct-original-correction | source-and-bounded-self-audit | PDF5/printed463; PDF14/printed472 Table1 | true |
| IB98-D20-R146-2 | 131Ce的PTR含K=9/2与7/2混合；两套ξ=.7/1、ε2=.14/.18、γ23/20度均列于原表。纯K=I=9/2的6/11仅条件轴对称几何，不能替代此模型，亦不能将异构态Qs、另一高spin带Qt和HD带fit Q0相除平方成实测B(E2)阶梯。 | model-and-observable-boundary | source-and-bounded-self-audit | PDF14 Table1及其后wavefunction段; IB98-D20-R104-5 | true |
