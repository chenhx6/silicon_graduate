---
type: source
title: "Twin, Olsen & Sheppard 1970 - Polarization and angular correlation measurements following the 40Ar(p,nγ)40K reaction"
aliases: [Twin 1970 40K polarization, 40Ar p n gamma 40K angular correlations]
created: 2026-09-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-method
reading_depth: deep-read
title_original: "Polarization and angular correlation measurements following the 40Ar(p,nγ)40K reaction"
authors: [P. J. Twin, W. C. Olsen, D. M. Sheppard]
journal: "Nuclear Physics A"
year: 1970
citation_key: twin_1970_Polarization
volume: 143
pages: "481-496"
pii: "0375-9474(70)90543-9"
canonical_source: "Twin, Olsen & Sheppard, Nucl. Phys. A 143, 481-496 (1970)"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1970_Twin et al_Polarization and angular correlation measurements following the 40Ar(p, nγ)40K reaction.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1970_Twin et al_Polarization and angular correlation measurements following the 40Ar(p, nγ)40K reaction.pdf"
raw_sha256: "40cb4df52b26f0eabc9c86eba136fb68bc2da99d123a72276583483cc64dfd11"
nuclei: [40K, 40Ar, 40Ca]
reactions: [40Ar(p,nγ)40K]
experiments: [alberta-vande-graaff-gamma-polarimeter]
models: [compound-nuclear-statistical-model, rotation-vibration-context]
observables: [gamma-ray-angular-distribution, gamma-ray-polarization, gamma-gamma-angular-correlation, multipole-mixing-ratio]
methods: [angular-distribution, linear-polarization-asymmetry, compton-polarimetry]
tags: [40K, polarization, angular-correlation, mixing-ratio, historical-method]
---

# Polarization and angular-correlation measurements following the 40Ar(p,nγ)40K reaction

## Bibliographic Record

- P. J. Twin, W. C. Olsen and D. M. Sheppard, *Nuclear Physics A* **143**, 481–496 (1970), PII `0375-9474(70)90543-9`。
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1970_Twin et al_Polarization and angular correlation measurements following the 40Ar(p, nγ)40K reaction.pdf`。
- 16-page historical experiment/method paper; HS-033 and HS-034 are exact duplicate rows of this same PDF and will be audited without rereading.

## Scope and Reading Depth

- PDF pp.481–496 fully read: reaction/target, angular distributions, γγ correlations, Compton polarimeter and Rose–Brink polarization formalism Eqs.(1–3), efficiency factor `R`, compound-statistical-model grid search, Table 1/2, Figs.1–9 and conclusions.
- Figure/table audit: polarimeter geometry, χ²/mixing-ratio plots, spectra at 0°/90° analyzer, Legendre-coefficient maps, and all state/mixing-ratio rows in Table 2.
- Not covered: raw spectra/matrices, original MANDY code, modern response simulations and later 40K evaluations.

## Paper Question and Experimental Logic

The experiment identifies low-lying `40K` levels and multipole mixing ratios by combining near-threshold `40Ar(p,nγ)` angular distributions, γγ angular correlations and Compton polarization. Near threshold suppresses outgoing-neutron `l=1` transmission and stabilizes compound-population predictions.

1. Record Ge(Li) γ spectra at 0°, 30°, 45°, 60° and 90°; fit even Legendre coefficients `a2/a4` and compare with MANDY compound-nuclear predictions.
2. Measure γγ angular correlations with two NaI detectors and use grid-search χ² fits in population parameters and mixing ratios.
3. Use a Ge(Li)+two NaI Compton polarimeter with Compton scattering angle `ψ=82°` and emission angles `θ=0–90°`; normalize analyzer efficiencies at `θ=0°`, compute polarization efficiency `R` with Klein–Nishina/solid-angle correction, and fit polarization simultaneously with angular distributions.

## Key Evidence and Reasoning Chain

- The paper assigns `40K` states at 1.959 (`2+`), 2.047 (`2−`), 2.070 (`3−`), 2.103 (`1−`), 2.261 (`3+`), 2.290 (`1+`), 2.291 (`4` or `3`), 2.419 (`2`/`3`), 2.575 (`2`/`4`) and 2.625 (`0−`) MeV, with branching and δ values in Table 2.
- The `0.800-MeV` `2−→3−` 770-keV transition has an angular-distribution ambiguity; γγ correlation with a pure-quadrupole 844-keV reference resolves it as pure M1.
- The 1.959-MeV level is assigned `2+`: simultaneous angular distributions establish spin 2, while 1159-keV polarization selects positive parity and δ(1929 keV)≈−0.10(4).
- The 2.261-MeV level is assigned `3+` from angular distributions plus `−0.57±0.30` polarization; the paper explicitly shows polarization alone can fit `2−`, `3+` or `4−`, so spin information is required first.
- Negative-parity `p3/2 d3/2−1` states receive mixed E2/M1 ratios; positive-parity states at 1.644, 1.959, 2.261 and 2.290 MeV are identified as likely multi-particle configurations but no modern structure calculation is supplied.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| TW70-1 | Combined angular distributions, γγ correlations and polarization assign spins/parities and mixing ratios for low-lying `40K` states. | experimental-method-result | direct | PDF pp.481–496, Table 2 | true |
| TW70-2 | The 770-keV `2−→3−` line is pure M1 after γγ-correlation resolution of the angular-distribution ambiguity. | experimental-result | direct | PDF pp.487–488, Fig.2 | true |
| TW70-3 | The 1.959-MeV state is `2+`; 1159-keV polarization and 1929-keV angular distribution/mixing support the assignment. | experimental-assignment | direct | PDF pp.489–490, Figs.3–4 | true |
| TW70-4 | The 2.261-MeV state is `3+`; polarization alone is non-unique and must be combined with angular distributions. | experimental-assignment/limitation | direct | PDF pp.491–492, Fig.6 | false |
| TW70-5 | Table 2 contains multiple δ solutions/uncertainties, including unresolved 2.291-MeV spin 3/4 and 2.419-MeV spin 2/3 cases. | ambiguity | direct | PDF pp.487–495, Table 2 | false |

## Summary

Twin *et al.* demonstrate a historical joint-analysis chain in which angular distributions constrain spin/population, γγ correlations resolve mixing-ratio branches and Compton polarization supplies parity/multipole information. The method's strongest lesson is complementarity: polarization alone is often non-unique.

## Competing Interpretations and Limitations

MANDY compound-statistical populations, Biedenharn versus Rose–Brink sign conventions, finite polarimeter efficiency `R`, near-threshold assumptions and limited detector response all affect δ. Several states retain alternative spin assignments or δ branches; positive-parity configuration language is qualitative and predates modern shell-model/DFT calculations.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| TW70-AR-1 | Observable chain | `a2/a4` angular distributions → γγ correlation → polarization `P=R^{-1}R_exp` → joint χ² δ/spin/parity. | PDF pp.482–487 | self-checking |
| TW70-AR-2 | Convention | MANDY uses Biedenharn δ sign; paper's formalism uses Rose–Brink, yielding opposite dipole–quadrupole sign. | PDF p.482 | self-checking |
| TW70-AR-3 | Transfer condition | 原R=.21(.02)属于2231-keV线(p492)；1.5MeV仅Ar1460参考检查几何计算within5%(p485)。ψ82是Compton角不是θ，数值不迁现代Q。 | PDF pp.484–485/492; Day17 correction | self-checking |
| TW70-AR-4 | Failure condition | Polarization-only parity fits can be degenerate; population priors and `a2/a4` uncertainties can reorder spin/δ solutions. | PDF pp.491–492 | active-L3 |
| TW70-AR-5 | Duplicate lineage | HS-033/HS-034 are exact SHA-256 duplicates; no new source/experiment count. | Ledger identity | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` the joint angular-distribution/polarization method map and `limits` single-observable spin/parity assignments.
- Persistence: update [[angular-distribution]], [[linear-polarization-asymmetry]], [[compton-polarimetry]] and [[multipole-mixing-ratio]].
- Review state: Codex self-audited; not `human-reviewed`.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[angular-distribution]] | Near-threshold population control and `a2/a4` grid search. |
| methodological-bridge | [[linear-polarization-asymmetry]] | Compton polarimeter efficiency and parity/multipole complement. |
| supports | [[multipole-mixing-ratio]] | Historical multi-observable δ extraction with explicit branch ambiguity. |

## Human Review Triage

### P0

- `TW70-P0-1`: map Biedenharn/MANDY signs to Rose–Brink before cross-source δ comparison; preserve unresolved states.

### P1

- `TW70-P1-1`: `R` and analyzer geometry are historical detector-specific values; modern response simulation is required for reuse.
- `TW70-P1-2`: qualitative positive-parity configuration labels are not direct modern structure assignments.

## Extracted Pages

- Nuclei: `40K` (source-level only).
- Methods: [[angular-distribution]], [[linear-polarization-asymmetry]], [[compton-polarimetry]]。

## L3/L4 Follow-up

- L3 question: quantify how much joint `a2/a4`+γγ+polarization reduces δ/spin branch ambiguity under modern detector-response and convention mapping. No L4 inputs/code are available.


## Day17原件自审：三角角色、R能量与独立参照

本session先冻primed回忆，再新读完整16页/9图/2表/3编号式及未编号KN、P纯/混合式、18refs；hash40cb4df52b26f0eabc9c86eba136fb68bc2da99d123a72276583483cc64dfd11/754194bytes保持。旧TW70-1–5行与truetruetruefalsefalseflags保持，reviewunreviewed，新14claims待审。HS033/034同PDF不算两个experiment。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| TW70-D17-1 | 原ψ82°是Compton散射角，φ0/90是analyser方位；emissionθ为束流与incidentγ夹角、整个装置可由θ90移到0，实际P还测45。旧Wikiθ≈82误读已纠，不把beamangle代scatterKN。 | angle-identity correction | direct | pp.483–485 Fig1 and Sec2.3 | true |
| TW70-D17-2 | 45cm³GeLi距target20cm、2个7.6×7.6cmNaI距scatterer12cm/15cmPb；N取sumcoincidencefullpeak。relativeanalyzereff由θ0的unpolarizedγyield归一，不是R或absoluteP校准；null需原axisymmetry/选择条件。 | actual-count and null-calibration | direct | p.484 Sec2.3 | true |
| TW70-D17-3 | 原plane-axisPt式3与Pe=−[Nφ0−Nφ90]/[R(Nφ0+Nφ90)]相连，R由perp/parallelCompton截面差定义，KN包含ψ。此R为polarizationefficiency，不是Eq1/2核角Qk，亦不移B73/clover数值。 | formal-response dictionary | direct | pp.484–485 Eq3 and response equations | true |
| TW70-D17-4 | 原采用Ferguson有限solidangle算R；约1.5MeV以Ar1460的2+→0+AD/P检查within5%，实际采用nominal10%Rerror。R=.21±.02是在2231-keV偏振测量给的，旧Wiki挂到1.5MeV错，已纠；全文未给R1500具体值。 | calibration-energy correction | direct | p.485 Sec2.3; p.492 Sec3.4 | true |
| TW70-D17-5 | 新pointKN核1500keV的Rψ82=.346537、ψ90=.313526，2231为.245904/.219668；原R2231 .21对point82比.853992只geometry诊断，非完整有限接受重放/新的Q或可迁通用factor。 | Codex source-geometry calculation | derived conditional | p.485 KN expression | true |
| TW70-D17-6 | AD用0/30/45/60/90重复测，bombarding>4.5MeV以1614(0+)line作monitor否则totalNaI；systemisotropy用1614检查。CNRpopulationprior来自threshold到+200keV，实际beam在阈值100keV内以抑l1/l0<10%，不是自由populationfit。 | selection and inference-input contract | direct | pp.482–483 Sec2.1 | true |
| TW70-D17-7 | MANDY的Biedenharn与本文RB对dipolequadrupole混合δ反号，原声明只该对象；p486pureM1/M2/E1/E2的P符号与uppermultipole电磁性和核Qk一并进入。不能给所有rank/现代nativeδ统一乘−1。 | phase and multipolarity boundary | direct | p.482 Sec2.1; pp.484/486 equations | true |
| TW70-D17-8 | 770的AD有两个δ根；以1644(0+)→800(2−)的844 pureM2（L2）作γγcompanion排歧。未分析偏振的purequadrupole角关联仅需L2，不把reference误叫E2或把该门移给任意singlesP。 | actual-companion observable | direct | pp.487–488 Table2 and Fig2 | true |
| TW70-D17-9 | 1959的1159/1929两AD联合约束J2、δ1159=0后δ1929=−.10(.04)，再45/90的1159P选2+；770–1159γγ则作者明言不增信息，因为其唯一大项同ADa2。测更多correlation不自动提供独立判别。 | information-gain counterevidence | direct | pp.489–490 Figs3–4 | true |
| TW70-D17-10 | 2261的2231P=−.57(.30)单独可容2−/3+/4−，需2231/2261两AD先约束J3才选3+。以Tablea2=.41的pureE1 limit算pointP90=−.773585只是条件对照，R×印P=−.1197为派生A非原rawcounts/其CI。 | nonunique-P and conditional source replay | direct and derived | pp.491–492 Sec3.4/Fig6 | true |
| TW70-D17-11 | 2261→800的1461支被Ar1460强线遮，作者用770gate未见1461给<5%limit；没有同gateeff/background/CL原data，不能把未见转绝对无支或用别gatelimit。 | unresolved-line and negative-evidence boundary | direct | p.491 Sec3.4 | true |
| TW70-D17-12 | 2290/2291为twolevels：646+1490归2290，2291groundγ归2291，2261γ主要归2261level不塞两新态。2290 1+偏好依paritydependentCNRpopulationlimits，2291J4仍J3可容、2419J2仍J3可容、2575J2/4保。 | parent-identity and model-dependent alternatives | direct | pp.493–495 Figs7–9 and Table2 | true |
| TW70-D17-13 | 新9条Ei−Ef光子identity核含844/1614/770/1159/1929/2231/646/1490/2291，残差只表列MeV/keV算术，不当实验energy精度或全levelscheme重拟。Tablebranch约±3%、levelerror<1.5keV是作者报告，原counts/Σ缺。 | Codex table-crosscheck scope | direct plus arithmetic | p.487 Table2 | true |
| TW70-D17-14 | 本实验Alberta与B73/WA77的Liverpool不同装置/data，但有作者与共同RB/MANDY/FH/Suffert方法祖先，不把实现/理论当完全独立。positiveparity多p-h组态是作者定性interpretation，未本核量化计算；无actualevent/response/Cov/producer，未重测Jπ/δ/P/R或CI。 | independence and model-readiness | direct and synthesis | pp.481–483 methods; pp.495–496 conclusions/references | true |

[角/能量合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/twin1970-response-contract.json)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/twin1970-response-result.json)，script `system/scripts/day17_twin1970_response_audit.py`。0/180°ComptonR零、低能90°Thomson极限核作为componentcontrol，不认证原geometry。原R约.21与B73的B.84近似factor不能由数值接近视共响应。

本次`revises`旧角度/R能量转录、`supports`θ0null相对eff和分层R校准的独立实验例，`limits`Ponly/所有γγ自动高信息与自由phase迁移。关联[[butler-1973-three-geli-compton-polarimeter]]、[[compton-polarimetry]]、[[linear-polarization-asymmetry]]与[[polarimetry-shared-calibration-count-design]]。θ0null的现实axisymmetry/有限接受仍为仪器合同，不替实际无偏振source证据。
