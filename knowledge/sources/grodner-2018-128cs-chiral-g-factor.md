---
type: source
title: "Grodner et al. 2018 - g factor of the 128Cs chiral-band isomer"
aliases: [Grodner 2018 128Cs g factor]
created: 2026-09-21
updated: 2026-10-09
status: ai-draft
review_status: unreviewed
source_type: experiment-and-PRM-CDFT
reading_depth: deep-read
title_original: "First Measurement of the g Factor in the Chiral Band: The Case of the 128Cs Isomeric State"
authors: [E. Grodner, J. Srebrny, Ch. Droste, L. Próchniak, S. G. Rohoziński, M. Kowalczyk, M. Ionescu-Bujor, C. A. Ur, K. Starosta, T. Ahn, M. Kisieliński, T. Marchlewski, S. Aydin, F. Recchia, G. Georgiev, R. Lozeva, E. Fiori, M. Zielińska, Q. B. Chen, S. Q. Zhang, L. F. Yu, P. W. Zhao, J. Meng]
journal: "Physical Review Letters"
year: 2018
volume: 120
pages: "022502"
doi: "10.1103/PhysRevLett.120.022502"
citation_key: Grodner_2018
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "Grodner et al., Phys. Rev. Lett. 120, 022502 (2018)"
library_file: "raw/papers/gpt/high-spin-20260920/g-factor/2018_Grodner et al_First Measurement of the g Factor in the Chiral Band.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/g-factor/2018_Grodner et al_First Measurement of the g Factor in the Chiral Band.pdf"
raw_sha256: "c71ec59160c444c34ab7f340db5f045c1f26456bc1741197ec62caea7f4efbf2"
nuclei: [128Cs, 128Xe]
reactions: [122Sn-10B-4n]
experiments: [TDPAD, GAMIPE, LEPS]
models: [particle-rotor, constrained-CDFT, angular-momentum-additivity]
observables: [g-factor, Larmor-precession, orientation-parameter, chiral-geometry]
methods: [time-differential-perturbed-angular-distribution]
tags: [128Cs, chirality, g-factor, TDPAD, planar-aplanar, particle-rotor]
---

# g factor of the `128Cs` chiral-band isomer

## Bibliographic Record

- E. Grodner *et al.*, *Phys. Rev. Lett.* **120**, 022502 (2018), DOI `10.1103/PhysRevLett.120.022502`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/g-factor/2018_Grodner et al_First Measurement of the g Factor in the Chiral Band.pdf`。

## Supporting Information Availability

The official APS article page was checked on 2026-10-09. The initial request returned HTTP 200 with no supplement or attachment link; a later metadata-only recheck timed out, so Crossref metadata was used to verify DOI/title identity. The APS supplemental resolver returned to the article record at `#supplemental`, and the standard supplemental-PDF endpoint returned HTTP 404. No SI file was found on these checked publisher routes; separately hosted author material is outside this check.

## Scope and Reading Depth

- PDF pp.022502-1–5 fully read: `122Sn(10B,4n)128Cs` production, TDPAD at two facilities, 56-ns isomer, Larmor fits/attenuation, angular-momentum additivity, generalized three-component g-factor equation, PRM+CDFT geometry and conclusions.
- Not covered: raw time spectra and full PRM/CDFT code.

## Key Results

- The `Iπ=9+`, `T1/2=56 ns` isomeric bandhead g factor is measured as `g=+0.59(1)` independently at Orsay and SUNY using TDPAD; `1/λ2≈300 ns` describes spin deorientation (PDF pp.1–3, Table I, Fig.2).
- A two-component `πh11/2⊗νh11/2^-1` additivity estimate gives `g≈0.50–0.52`, below experiment; the discrepancy requires nonzero even-even core rotation (`j_R=2,4,...`) and a three-vector g-factor relation (PDF pp.3–4, Eq.2, Table II).
- The generalized g factor depends on scalar products of `j_p`, `j_n`, and `j_R`; the normalized triple-product orientation `⟨(jp×jn)·jR⟩/sqrt(...)` is near zero for the fitted configuration. PRM+constrained-CDFT with `β≈0.23`, `γ≈23.8°` gives `g≈0.58` and an almost planar (`⟨ô⟩≈0.15`) bandhead rather than ideal chirality (PDF pp.4–5, Eqs.2–3, Fig.4).
- The result indicates a critical rotational frequency: characteristic chiral geometry may emerge only above a minimum spin/frequency, so low-spin bandheads with chiral-like transition patterns are not automatically static chiral configurations (PDF pp.1, 4–5).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GR18-1 | `128Cs` isomer g factor is `+0.59(1)` from two independent TDPAD measurements. | experiment-result | direct | PDF pp.1–3, Table I | true |
| GR18-2 | The measured g factor requires core-rotation admixtures beyond a two-vector proton–neutron additivity model. | structure-inference | mixed | PDF pp.3–4, Eq.2, Table II | true |
| GR18-3 | PRM+CDFT reproduces the g factor for an almost planar bandhead, not ideal aplanar chirality. | geometry-result | mixed | PDF pp.4–5, Fig.4 | true |
| GR18-4 | Chiral geometry can have a critical-spin/frequency onset; transition fingerprints alone are insufficient at low spin. | interpretation-boundary | mixed | PDF pp.1, 4–5 | false |
| GR18-5 | In the simplified classical vector construction with `j_p=j_n=11/2` and `j_R=2`, the two planar limiting alignments give `g=0.6` and `g=0.4`, while the aplanar geometry gives an intermediate value; these are model-specific limits, not a universal g-factor classifier. | model-result + evidence-boundary | indirect | single | printed 022502-3 / PDF p.3, Fig.3 caption | true |
| GR18-SI-1 | The official APS article page exposes no SI link; the supplemental resolver returns to the article record and the standard SI PDF endpoint returns HTTP 404. No SI file was found on the checked publisher routes. | evidence-boundary | direct | APS article `https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.120.022502`; resolver `https://link.aps.org/supplemental/10.1103/PhysRevLett.120.022502`; standard endpoint `https://journals.aps.org/prl/supplemental/10.1103/PhysRevLett.120.022502/PhysRevLett.120.022502.supplemental.pdf` | true |

## Summary

Grodner *et al.* provide a direct magnetic-moment geometry test of a proposed chiral band. The measured `g=0.59(1)` demonstrates the importance of core rotation and shifts the `128Cs` bandhead away from ideal static chirality; it is a strong counterexample to assigning low-spin chirality from near-degenerate bands and E2/M1 fingerprints alone.

## Competing Interpretations and Limitations

- The g-factor geometry inference relies on particle-rotor/CDFT configurations, core `g_R`, deformation and model-space choices.
- A near-planar bandhead does not rule out chiral geometry at higher spin; the conclusion is about spin-dependent onset, not the entire band.
- TDPAD attenuation, field calibration and spin assignment (`9+`) are experimental inputs; unobserved converted transitions in the level scheme remain a boundary.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| GR18-AR-1 | TDPAD chain | Magnetic precession modulation `R(t)` → Larmor frequency → g factor with attenuation correction. | PDF Eq.1, Table I, Fig.2 | self-checking |
| GR18-AR-2 | Geometry chain | Three-vector g relation → scalar products/triple product → planar/aplanar orientation ranking. | PDF Eq.2–3, Fig.3 | self-checking |
| GR18-AR-3 | Transfer condition | Compare only with nucleus-specific PRM/CDFT and spin/frequency; g factor is a companion observable, not a universal chirality threshold. | PDF pp.3–5 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[nuclear-chirality]]、[[recoil-distance-doppler-shift]]、[[lifetime-method-selection-response-contract]], [[tilted-axis-cranking]], [[g-factor-measurement]], [[time-differential-perturbed-angular-distribution]] and the counter-evidence map for chiral fingerprints.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `GR18-P0-1`: Preserve the distinction between measured g factor and model-inferred geometry; do not promote `g=0.59` into a universal planar/aplanar classifier.

## Extracted Pages

- Concepts/methods: [[nuclear-chirality]]、[[recoil-distance-doppler-shift]]、[[lifetime-method-selection-response-contract]], [[tilted-axis-cranking]], [[g-factor-measurement]]。


## Day19新原读：进动频率、人口寿命与校准桥

本session实际新读五页全文文本；视觉核PDF2–5的全部Figs1–4、TablesI–II、Eqs1–3和结果/限制。raw hash仍c71ec59160c444c34ab7f340db5f045c1f26456bc1741197ec62caea7f4efbf2。各转移gamma同源于此isomer，不算九项独立g实验；Orsay与Stony为不同采集，核素/反应及部分物理输入仍相同。原needs_review/review flags不变。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| GR18-D19-1 | R(t)=Dexp(−λ2t)sin(φ−2ωLt)，ωL=−gBμN/ℏ。114keV行|ωL|=.0625(1)×10^9s⁻¹；rank2 modulation周期50.265ns，Larmor旋转周期100.531ns。56ns是half-life、mean80.791ns；约300ns是alignment弛豫尺度。 | distinct-clock-and-factor-two | direct-and-task-derived | PDF2 Eq1/TableI/Figs1–2；PDF3第一段 | true |
| GR18-D19-2 | Orsay使用55MeV10B、22mg/cm²Sn靶作stopper、1ns pulse/400ns周期、外场21450±10G与±45°LEPS；低能级纲图含未见强转换支路，9+按systematics采用。去背景time spectra与下游快gamma保留同进动是提取前提。 | experiment-and-gate-boundary | direct-original | PDF2 Sec实验/Fig1caption/TableI | true |
| GR18-D19-3 | Stony独立47MeV采集用Sn/Pb、212ns周期、±135°LEPS与Hallprobe外场14000(+200/−500)G，ωL=41.3(2)×10^6s⁻¹、g=.59(+.01/−.02)。Orsay文中g=.59(1)保原值；不能将两实验/多gamma行自动当共同输入全独立。 | independent-acquisition-and-calibration | direct-original | PDF3第一栏 | true |
| GR18-D19-4 | 仅把打印外场和频率代入|g|=|ωL|/(BμN/ℏ)，用约4.789×10^7s⁻¹T⁻¹得Orsay .6084、Stony .6160，不精确重建打印.59。本文未在这些段给出完整effective-local-field/calibration桥；当前不补造修正因子、不称原结果被推翻。 | literal-calibration-reproduction-boundary | task-derived-from-printed-inputs | PDF2 Eq1、外场段/TableI；PDF3 Stony段；tdpad-response-contract-result-014.json | true |
| GR18-D19-5 | PRM/CDFT在β.23、γ23.8°、gR.41及指定组态下给g约.58和较小orientation约.15；这与测得g不同层，不能由.59给普适平面判据。作者指出高自旋ps态需不同g测量技术，不能把ns-isomer TDPAD直接移植。 | model-and-transfer-boundary | direct-original-model-result | PDF3 Eq2/TableII/Fig3；PDF4 Eq3/Fig4；PDF5结论末段 | true |

Knowledge Impact and Learning Decision：limits把R(t)振幅衰减当人口寿命、把2ωL当ωL、把外场当自动已知B_eff的用法；supports与[[ionescu-bujor-1998-static-moments-129-131ce]]的distinct-data hyperfine校准对比。[[time-differential-perturbed-angular-distribution]]与[[lifetime-method-selection-response-contract]]给causal response设计；不以本算术重新发布g或实验CI。

## Day19三矢量g因子相加与手征序参量审计

依据独立审计程序 day19_grodner_three_vector_gfactor_audit.py 的 16 项检验与基准输出 grodner-three-vector-gfactor-result-027.json，系统核准了 Grodner 2018 中三矢量磁矩几何与 TDPAD 实验测量间的定量对应：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| GR18-D19-6 | checkpoint108撤回旧普适平面/Schmidt锁定/EFG完全消除等科学认证。新直接原读及条件边界见GR18-D19-8；原result字节保留，不以算术通过恢复科学结论。 | superseded-certification | corrected-and-boundary | GR18-D19-8 | true |

## Day19量化审计：TDPAD双倍拉莫尔进动周期、四重时间对象与三矢量共面判限定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_tdpad_hyperfine_decoupling_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/tdpad-hyperfine-decoupling-result-071.json`，核准了针对 Grodner 2018 磁相互作用与手征几何判据的微观动力学审计：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| GR18-D19-7 | checkpoint108撤回旧普适平面/Schmidt锁定/EFG完全消除等科学认证。新直接原读及条件边界见GR18-D19-8；原result字节保留，不以算术通过恢复科学结论。 | superseded-certification | corrected-and-boundary | GR18-D19-8 | true |


## checkpoint108：身份、频率与校准的直接原读纠正

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| GR18-D19-8 | 实际全文文本再读1–5，视觉2–3。TableI114keV的|omegaL|=.0625(1)e9 rad/s，普通fL=omegaL/(2pi)约9.947MHz，R(t)含2omegaL故调制周期约50.265ns；不是62.5MHz普通频率。56ns为half、mean约80.79ns，alignment约300ns另列。g+.59(1)保作者结果，外场/表频率简单代入尚不完全复现，缺localfield/fit桥不补造。g→近planar/orientation.15依赖PRM/CDFT的组态/g参数，不是跨核普适阈值或高spin已直接测量。 | direct-scope-and-correction | direct-original-and-bounded-arithmetic | PDF1–5; PDF2 Eq1/TableI; PDF3 Eq2/Fig3; PDF4–5 Fig4 | true |

## checkpoint110：三矢量模型图的实际视觉与输入依赖

本轮实际视觉核PDF4 Eq3/Fig4，加108的PDF2–3已核全部关键4图/2表/3式；108已完整文字读1–5。这里仍不等原event或PRM/CDFT job已复现。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| GR18-D19-9 | Fig4的A/B/C为不同configuration-fixedCDFT输入后PRM扫gamma0–60deg所得g–orientation曲线，固定beta.23、gR.41（来自128Xe2+）和Jcore12hbar²/MeV，gs取.6free。作者配置A取gamma23.8deg得g约.58、orientation约.15；图上实验g为单一黑线，orientation是模型输出。高spinps态没有在本文用同一TDPAD技术新测g，结论明确需新技术。 | actual-visual-and-model-domain | direct-original-model | PDF4 Eq3/Fig4 and parameters; PDF5 conclusion | true |
