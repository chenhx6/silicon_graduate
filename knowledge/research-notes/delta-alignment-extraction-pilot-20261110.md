---
type: research-note
title: "Delta extraction and alignment treatment: 61Ni, 135Pr and 187Au pilot"
aliases: [delta alignment extraction pilot]
created: 2026-11-10
updated: 2026-11-11
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [wadsworth-1977-61ni-levels, lv-2022-evidence-against-wobbling-135pr, matta-2015-transverse-wobbling-135pr, guo-2022-low-spin-wobbling-187au, sensharma-2020-longitudinal-wobbling-187au]
created_from: "Bounded user-requested extraction-table pilot"
tags: [mixing-ratio, alignment, angular-distribution, evidence-matrix]
---

# Delta extraction and alignment treatment pilot

Current workbook: `raw/writing/pado/20261029_review_v1/mixing_ratio_sigma_I_pilot_20261111.xlsx`. It contains31 numerical E2/M1 records across6 references and4 nuclei. The39-row initial table below is retained as historical extraction evidence; non-E2/M1 and nonnumerical controls are excluded from the current workbook.

Revision: G22 is standard R_ADO and L22 is detector-group R_ADO; original Rac labels and exact angle groups remain recorded. Dataset and Settings now share one result-level dataset_id with exact reciprocal links. Both G22 and S20 are independent measurements, not repeated analysis of the same acquisition. [[mukherjee-2022-shape-coexistence-octupole-72se]] adds72Se;454.5-keV delta=-5(3) uses calibrated-and-fixed sigma/j=.3, while1136.1-keV delta=-.10(.24) has unresolved extraction origin.

## Research Trigger

The question is how reported gamma-transition mixing ratios depend on the treatment of laboratory spin alignment. This pilot covers five primary papers for three user-specified nuclei, with no date restriction. It is a spreadsheet-design trial, not a systematic prevalence estimate of whether analyses commonly fix sigma/I. Expansion awaits the user's review of the workbook format.

## Grounded Evidence

| Ref | Source | Exact methodological locator | Treatment supported by the inspected source |
|---|---|---|---|
| W77 | [[wadsworth-1977-61ni-levels]] | printed p.36, Sec.2; Table3 pp.40-41 | Joint minimization over delta and population parameters, with compound-nucleus alignment estimates entering residuals; no fixed single sigma/I. |
| L22 | [[lv-2022-evidence-against-wobbling-135pr]] | main Table1/Fig.2 p.3; Supplement p.4 | Central P/Rac match determines delta and sigma/I jointly; varying response curves propagates observable error boundaries. |
| M15 | [[matta-2015-transverse-wobbling-135pr]] | pp.2-4; Fig.2 and TableI | Delta from Gammasphere angular distributions; separate INGA asymmetries check electromagnetic character. Sigma/I handling not specified in inspected PRL. |
| G22 | [[guo-2022-low-spin-wobbling-187au]] | main p.3/Fig.3; Supplement pp.3-4/Fig.2 | Conditional fixed-sigma curves are combined over all allowed alignment values. Final reported range does not condition on one assumed sigma. No probability marginalization is described. |
| S20 | [[sensharma-2020-longitudinal-wobbling-187au]] | p.3; Fig.3 p.4 | Full angular-distribution fits; alignment details deferred to Ref.26. Unreported is not evidence of fixed-assumed sigma. |

## Extracted Transition Evidence

Values below retain the original article's sign. Errors are positive absolute offsets from the central value, not fractional errors. Multipole definitions marked inferred are not treated as author-explicit. Blank numeric delta indicates a non-numerical control rather than zero. Angular observables retain their reported uncertainty and source notation.

| ID | Nucleus | Eg (keV) | Ji -> Jf | Definition | delta | left error | right error | angular data | P / asymmetry | Locator |
|---|---|---:|---|---|---:|---:|---:|---|---|---|
| W77-T01 | 61Ni | 908.3 | 5/2- -> 3/2- | E2/M1 | 0.18 | 0.05 | 0.05 | a2=-0.28 +/- 0.01; a4=-0.02 +/- 0.01 | P=-0.15 \pm 0.03; A=NR | Table 3, p. 40; Table 4, p. 42; Section 3.3, p. 39 |
| W77-T02 | 61Ni | 841 | 5/2- -> 5/2- | E2/M1 | -1.83 | 0.2 | 0.2 | a2=0.15 +/- 0.01; a4=0.02 +/- 0.02 | P=-0.17 \pm 0.06; A=NR | Table 3, p. 40; Table 4, p. 42; Section 3.3, p. 39 |
| W77-T03 | 61Ni | 1014.9 | 7/2- -> 3/2- | M3/E2 (inferred) | 0.03 | 0.03 | 0.03 | a2=0.27 +/- 0.01; a4=-0.09 +/- 0.01 | P=0.45 \pm 0.06; A=NR | Table 3, p. 40; Table 4, p. 42; Section 3.4, p. 39 |
| W77-T04 | 61Ni | 947.6 | 7/2- -> 5/2- | E2/M1 | -2.46 | 0.15 | 0.15 | a2=0.47 +/- 0.01; a4=0.13 +/- 0.01 | P=-0.10 \pm 0.03; A=NR | Table 3, p. 40; Table 4, p. 42; Section 3.4, p. 39; Fig. 5(a), p. 47 |
| W77-T05 | 61Ni | 816.7 | 3/2- -> 1/2- | E2/M1 | -0.23 | 0.07 | 0.07 | a2=-0.01 +/- 0.01; a4=0.0 +/- 0.01 | P=-0.12 \pm 0.07; A=NR | Table 3, p. 40; Section 3.5, p. 45 |
| W77-T06 | 61Ni | 1131.9 | 5/2- -> 3/2- | E2/M1 | 0.47 | 0.09 | 0.09 | a2=-0.44 +/- 0.01; a4=0.01 +/- 0.01 | P=-0.03 \pm 0.04; A=NR | Table 3, p. 40; Table 4, p. 42; Section 3.6, p. 45 |
| W77-T07 | 61Ni | 1064.6 | 5/2- -> 5/2- | E2/M1 | -0.14 | 0.12 | 0.12 | a2=0.21 +/- 0.01; a4=0.0 +/- 0.01 | P=0.16 \pm 0.08; A=NR | Table 3, p. 40; Table 4, p. 42; Section 3.6, p. 45 |
| W77-T08 | 61Ni | 1454.4 | 7/2- -> 3/2- | E2 | NR | NR | NR | a2=0.25 +/- 0.06; a4=-0.15 +/- 0.1 | P=0.50 \pm 0.06; A=NR | Table 3, p. 40; Table 4, p. 42; Section 3.7, p. 46 |
| W77-T09 | 61Ni | 1387.2 | 7/2- -> 5/2- | E2/M1 | -2.7 | 0.4 | 0.4 | a2=0.44 +/- 0.02; a4=0.15 +/- 0.03 | P=-0.05 \pm 0.17; A=NR | Table 3, p. 40; Table 4, p. 42; Section 3.7, p. 46 |
| W77-T10 | 61Ni | 1609.4 | 5/2- -> 3/2- | E2/M1 | 0.33 | 0.14 | 0.14 | a2=-0.4 +/- 0.01; a4=0.01 +/- 0.02 | P=-0.05 \pm 0.10; A=NR | Table 3, p. 40; Table 4, p. 42; Section 3.8, p. 46; Fig. 5(b), p. 47 |
| W77-T11 | 61Ni | 1541.7 | 5/2- -> 5/2- | E2/M1 | 0.07 | 0.05 | 0.05 | a2=0.16 +/- 0.01; a4=0.0 +/- 0.02 | P=0.35 \pm 0.10; A=NR | Table 3, p. 40; Table 4, p. 42; Section 3.8, p. 46 |
| W77-T12 | 61Ni | 1740.1 | 9/2- -> 5/2- | M3/E2 (inferred) | -0.01 | 0.03 | 0.03 | a2=0.36 +/- 0.01; a4=-0.1 +/- 0.01 | P=0.53 \pm 0.05; A=NR | Table 3, p. 41; Table 4, p. 42; Section 3.10, p. 49 |
| W77-T13 | 61Ni | 792.6 | 9/2- -> 7/2- | E2/M1 | -0.97 | 0.18 | 0.18 | a2=0.57 +/- 0.02; a4=0.06 +/- 0.02 | P=-0.62 \pm 0.12; A=NR | Table 3, p. 41; Table 4, p. 42; Section 3.10, p. 49 |
| W77-T14 | 61Ni | 1920.1 | 9/2- -> 5/2- | M3/E2 (inferred) | -0.02 | 0.03 | 0.03 | a2=0.36 +/- 0.01; a4=-0.1 +/- 0.01 | P=0.39 \pm 0.10; A=NR | Table 3, p. 41; Table 4, p. 42; Section 3.11, p. 49 |
| W77-T15 | 61Ni | 1079.3 | 9/2- -> 5/2- | M3/E2 (inferred) | -0.01 | 0.03 | 0.03 | a2=0.35 +/- 0.02; a4=-0.11 +/- 0.02 | P=0.38 \pm 0.11; A=NR | Table 3, p. 41; Table 4, p. 42; Section 3.11, p. 49 |
| W77-T16 | 61Ni | 972.5 | 9/2- -> 7/2- | E2/M1 | 0.7 | 0.23 | 0.23 | a2=-0.79 +/- 0.02; a4=0.06 +/- 0.03 | P=0.03 \pm 0.12; A=NR | Table 3, p. 41; Table 4, p. 42; Section 3.11, p. 49 |
| W77-T17 | 61Ni | 533.2 | 9/2- -> 7/2- | E2/M1 | -0.02 | 0.03 | 0.03 | a2=-0.18 +/- 0.01; a4=-0.03 +/- 0.02 | P=-0.39 \pm 0.07; A=NR | Table 3, p. 41; Table 4, p. 42; Section 3.11, p. 49 |
| W77-T18 | 61Ni | 1997.3 | 5/2- -> 3/2- | E2/M1 | 0.27 | 0.06 | 0.06 | a2=-0.43 +/- 0.01; a4=0.02 +/- 0.02 | P=-0.24 \pm 0.11; A=NR | Table 3, p. 41; Table 4, p. 42; Section 3.12, p. 49; Fig. 6(a), p. 48 |
| W77-T19 | 61Ni | 1950.6 | 7/2- -> 5/2- | E2/M1 | 0.02 | 0.02 | 0.07 | a2=-0.26 +/- 0.02; a4=-0.03 +/- 0.02 | P=-0.4 \pm 0.1; A=NR | Table 3, p. 41; Table 4, p. 42; Section 3.13, p. 50 |
| W77-T20 | 61Ni | 1106.2 | 9/2+ -> 7/2- | M2/E1 (inferred) | 0 | 0.03 | 0.03 | a2=-0.28 +/- 0.01; a4=0.03 +/- 0.01 | P=0.23 \pm 0.06; A=NR | Table 3, p. 41; Table 4, p. 42; Section 3.14, p. 50 |
| W77-T21 | 61Ni | 1113.6 | 11/2- -> 7/2- | M3/E2 (inferred) | 0.02 | 0.02 | 0.02 | a2=0.32 +/- 0.01; a4=-0.11 +/- 0.01 | P=0.44 \pm 0.04; A=NR | Table 3, p. 41; Table 4, p. 42; Section 3.16, p. 51; Fig. 6(b), p. 48 |
| L22-135PR-747 | 135Pr | 747.3 | 17/2- -> 15/2- | E2/M1 | -0.47 | 0.22 | 0.09 | Rac 0.37(4) | P=0.04(+0.08,-0.13); A=0.006(+0.012,-0.019) | PLB 824 (2022) 136840 Table 1 (p. 3), Fig. 2(b); Supp Mat Table 1 (p. 5) |
| L22-135PR-813 | 135Pr | 813.2 | 21/2- -> 19/2- | E2/M1 | -0.37 | 0.14 | 0.1 | Rac 0.48(6) | P=-0.03(+0.05,-0.12); A=-0.004(+0.007,-0.016) | PLB 824 (2022) 136840 Table 1 (p. 3), Fig. 2(d); Supp Mat Table 1 (p. 5) |
| L22-135PR-450 | 135Pr | 450.2 | 19/2- -> 17/2- | E2/M1 | -0.31 | 0.13 | 0.1 | Rac 0.49(4) | P=-0.07(+0.09,-0.10); A=-0.017(+0.022,-0.023) | PLB 824 (2022) 136840 Table 1 (p. 3), Fig. 2(f); Supp Mat Table 1 (p. 5) |
| L22-135PR-755 | 135Pr | 755.1 | 25/2- -> 23/2- | E2/M1 | NR | NR | NR | Rac 0.50(6) | P=NR; A=NR | PLB 824 (2022) 136840 Table 1 (p. 3), text p. 3; Supp Mat Table 1 (p. 5) |
| M15-135PR-747 | 135Pr | 747 | 17/2- -> 15/2- | E2/M1 | -1.24 | 0.13 | 0.13 |  NR | P=NR; A=0.047(12) | PRL 114, 082501 (2015) Table I (p. 4), Fig. 2 (p. 3), Fig. 3 (p. 4) |
| M15-135PR-813 | 135Pr | 812.8 | 21/2- -> 19/2- | E2/M1 | -1.54 | 0.09 | 0.09 |  NR | P=NR; A=0.054(34) | PRL 114, 082501 (2015) Table I (p. 4), Fig. 2 (p. 3), Fig. 3 (p. 4) |
| M15-135PR-755 | 135Pr | 754.6 | 25/2- -> 23/2- | E2/M1 | -2.38 | 0.37 | 0.37 |  NR | P=NR; A=NR | PRL 114, 082501 (2015) Table I (p. 4), Fig. 2 (p. 3) |
| M15-135PR-594 | 135Pr | 593.9 | 13/2- -> 11/2- | E2/M1 | -0.16 | 0.04 | 0.04 |  NR | P=NR; A=-0.092(23) | PRL 114, 082501 (2015) Table I (p. 4), Fig. 2 (p. 3), Fig. 3 (p. 4) |
| G22_376 | 187Au | 376 | 11/2- -> 9/2- | E2/M1 (reported sign; convention unconfirmed) | -0.26 | 0.15 | 0.11 | Rac 图示，未数字化 | P=图示，未数字化; A=NR | PLB 828 (2022) 137010, p. 3 Fig. 3(a); Supplement p. 3 Fig. 2 |
| G22_462 | 187Au | 462 | 15/2- -> 13/2- | E2/M1 (reported sign; convention unconfirmed) | -0.28 | 0.69 | 0.23 | Rac 图示，未数字化 | P=图示，未数字化; A=NR | PLB 828 (2022) 137010, p. 3 Fig. 3(b) |
| S20_376 | 187Au | 376.3 | 11/2- -> 9/2- | E2/M1 (reported sign; convention unconfirmed) | -2.67 | 0.07 | 0.07 | W(theta) shown in Fig.3; A2/A4 not tabulated | P=NR; A=NR | PRL 124, 052501 (2020) p. 4 Fig. 3(a) |
| S20_462 | 187Au | 461.8 | 15/2- -> 13/2- | E2/M1 (reported sign; convention unconfirmed) | -2.98 | 0.02 | 0.02 | W(theta) shown in Fig.3; A2/A4 not tabulated | P=NR; A=NR | PRL 124, 052501 (2020) p. 4 Fig. 3(b) |
| S20_544 | 187Au | 544.3 | 19/2- -> 17/2- | E2/M1 (reported sign; convention unconfirmed) | -3.44 | 0.03 | 0.03 | W(theta) shown in Fig.3; A2/A4 not tabulated | P=NR; A=NR | PRL 124, 052501 (2020) p. 4 Fig. 3(c) |
| S20_639 | 187Au | 639.3 | 23/2- -> 21/2- | E2/M1 (reported sign; convention unconfirmed) | -3.72 | 0.12 | 0.11 | W(theta) shown in Fig.3; A2/A4 not tabulated | P=NR; A=NR | PRL 124, 052501 (2020) p. 4 Fig. 3(d) |
| S20_265 | 187Au | 265.3 | 11/2- -> 9/2- | E2/M1 (reported sign; convention unconfirmed) | -0.06 | 0.01 | 0.01 | W(theta) shown in Fig.3; A2/A4 not tabulated | P=NR; A=NR | PRL 124, 052501 (2020) p. 4 Fig. 3(e) |
| S20_436 | 187Au | 436.5 | 15/2- -> 13/2- | E2/M1 (reported sign; convention unconfirmed) | -0.1 | 0.01 | 0.01 | W(theta) shown in Fig.3; A2/A4 not tabulated | P=NR; A=NR | PRL 124, 052501 (2020) p. 4 Fig. 3(f) |
| S20_333_CTRL | 187Au | 333.8 | 13/2- -> 9/2- | M3/E2 (inferred; control) | -0.04 | 0.01 | 0.01 | W(theta) shown in Fig.3; A2/A4 not tabulated | P=NR; A=NR | PRL 124, 052501 (2020) p. 3 left column and p. 4 Fig. 3(g) |
| S20_413_CTRL | 187Au | 413.7 | 17/2- -> 13/2- | M3/E2 (inferred; control) | -0.03 | 0.01 | 0.01 | W(theta) shown in Fig.3; A2/A4 not tabulated | P=NR; A=NR | PRL 124, 052501 (2020) p. 3 left column and p. 4 Fig. 3(h) |

## Experimental Conditions

These descriptions are part of the reusable evidence contract. G22 and L22 Rac are classified as R_ADO, with their original single-angle or detector-group definitions retained. Full W(theta) data are not labeled as intensity ratios.

### W77-S1

- **ref_id**: W77
- **reaction_setup**: 58Fe(alpha,n gamma)61Ni reaction at alpha energies 7.8, 11.0, and 13.0 MeV. Target at 7.8 MeV: 1 mg/cm2, 71% enriched 58Fe on thick Au backing; targets at 11.0 and 13.0 MeV: 760 ug/cm2, 87% enriched 58Fe self-supporting.
- **angular_definition**: Linear polarization measured at 90 deg; angular distribution measured at multiple angles with escape-suppressed Ge(Li) spectrometer normalized to external singles monitor (full angle list not tabulated in text; a2, a4 corrected for solid-angle attenuation).
- **angles**: P at 90 deg; multi-angle AD; exact complete angle list not tabulated in the inspected methods.
- **gate**: Singles angular distribution in escape-suppressed spectrometer normalized to external singles monitor in polarimeter scatterer; separate gamma-gamma coincidence at 8.0, 8.5, 12.0 MeV with two Ge(Li) detectors at 90 deg used for level decay scheme.
- **polarization_calibration**: Three-Ge(Li) Compton polarimeter at 90 deg to beam axis; calibration and polarization sensitivity Q referenced to Butler et al. (1973) NIM 108, 497.
- **alignment_treatment**: CONSTRAINED_JOINT
- **curve_evaluation**: Joint sum of squared residuals combining compound-nucleus alignment predictions, angular distribution coefficients (a2, a4), and linear polarization P(90) minimized simultaneously over delta and alignment parameters (beta, x).
- **final_alignment_condition**: δ 与取向参数联合最小化；复合核模型预测参与残差约束。未采用一个固定 σ/I。
- **alignment_details**: p.36：以复合核统计模型估计取向，将取向参数、角分布与线偏振残差共同最小化，变量含 δ 及布居参数 β、x。不是假定单一 σ/I。原印布居公式有记号歧义，本表不擅自修正式子。
- **delta_convention**: Rose-Brink (1967)
- **uncertainty_model**: δ 误差引用 James et al. (1974) 方法；本篇未明确置信水平。0.1% 是自旋假设拒绝准则，不是 δ 区间水平。
- **locator**: p. 36, Section 2; Table 3, pp. 40-41; Table 4, p. 42

### L22-JUROGAM2-PRAC

- **ref_id**: L22
- **reaction_setup**: 100Mo(40Ar, 1p4n)135Pr at 152 MeV, self-supporting 0.5 mg/cm^2 enriched 100Mo target, JUROGAM II array (24 EUROGAM clovers + 15 EUROGAM Phase 1 tapered Ge detectors)
- **angular_definition**: Rac = I_gamma(157.6 deg + 133.6 deg, gated on all angles) / I_gamma(ca. 90 deg [75.5 deg + 104.5 deg], gated on all angles). Extracted from two gamma-gamma matrices: Phase 1 tapered detectors at (157.6, 133.6 deg) vs all detectors, and Clover detectors around 90 deg (75.5, 104.5 deg) vs all detectors. Same gate on all-detector axis.
- **angles**: [157.6, 133.6, 104.5, 75.5]
- **gate**: Same all-detector-axis coincidence gates. For polarization:747 uses450 gate;813 uses796 gate;450 uses747 gate. See Supplement pp.1,4.
- **polarization_calibration**: P=Ap/Q(E); a(E)=0.9844(21)+2(1)e-5 E(keV). Q(E) adopted from A. Herzan et al., PRC92,044310(2015), Supplement Ref.[6]; not Starosta1999. Clovers75.5/104.5 deg.
- **alignment_treatment**: FREE_JOINT
- **curve_evaluation**: Calculated response curves of P as a function of Rac for several sigma/I values in P-Rac plane for each delta
- **final_alignment_condition**: 中心值联合求解 δ 与 σ/I，区间通过响应曲线扫描传播观测误差；非单值预设，非概率边缘化。
- **alignment_details**: Supplement p.4：实验 P 和 Rac 中心值最佳匹配同时给出 δ 与 σ/I；再改变 σ/I，沿 P、Rac 实验误差边界确定 δ 上下限。这里的 FREE_JOINT 指中心值联合求解，未证明作者使用了特定二维优化算法；区间步骤另见说明。
- **delta_convention**: E2/M1 as reported; exact cross-paper phase/sign conversion not established in this pilot.
- **uncertainty_model**: 原文表列非对称误差；通过 P/Rac 误差边界传播。完整协方差与统一置信水平未给出。
- **locator**: PLB 824 (2022) 136840 p. 2-3, Fig. 2, Table 1; Supp Mat p. 1, 4, Table 1

### M15-GS-AD

- **ref_id**: M15
- **reaction_setup**: 123Sb(16O,4n)135Pr,80 MeV. AD:ATLAS Gammasphere,634 ug/cm2 Sb +15 ug/cm2 Al. Polarimetry:separate TIFR-BARC INGA run,630 ug/cm2 Sb between15 ug/cm2 Al and20 mg/cm2 Au (p.2).
- **angular_definition**: Angular distributions from Gammasphere, fitted with function cited as Yamazaki1967 (p.3); numerical a2/a4 not tabulated. Not a measured two-angle ratio.
- **angles**: Gammasphere multi-angle AD (Fig.2); exact ring list not supplied in the inspected text. INGA asymmetry from separate experiment.
- **gate**: Coincidence gated Gammasphere spectra
- **polarization_calibration**: Fig.3 reports (a*N_perp-N_parallel)/(a*N_perp+N_parallel), i.e. geometrical asymmetry correction a is included. Table I lists asymmetry, not sensitivity-corrected P. Q(E) not supplied here; details referred to Ref.[24].
- **alignment_treatment**: UNREPORTED
- **curve_evaluation**: Angular-distribution fit and comparison curves (Fig.2). Numerical sigma/I and whether it was held fixed are not stated in this PRL.
- **final_alignment_condition**: Not reported in PRL text or Table I; fitting was performed using Gammasphere data without specifying fixed sigma/I value or prior distribution in the paper.
- **alignment_details**: PRL 114, 082501 (2015) p. 3 states angular distributions were fitted with the function given in Yamazaki (1967), but does not report the numerical value of sigma/I, whether sigma/I was fixed or varied, or alignment parameters.
- **delta_convention**: E2/M1 as reported; precise phase convention/normalization not independently reconciled.
- **uncertainty_model**: Symmetric errors as printed in Table I; exact interval construction/confidence not stated in inspected text.
- **locator**: PRL 114, 082501 (2015) p. 2-4, Fig. 2, Table I

### G22_HIRFL_RAC_POL

- **ref_id**: G22
- **reaction_setup**: 175Lu(18O,6n)187Au at 108 MeV, two self-supported natural Lu targets (0.7 mg/cm2 each), array of 8 segmented clover HPGe detectors at 90 deg and 16 coaxial HPGe detectors at 26, 51, 129, 154 deg relative to beam
- **angular_definition**: Two-point angular correlation ratio Rac = I_gamma(154 deg) / I_gamma(90 deg) normalized by detector efficiencies at these two angles, gated on transitions observed in all detectors
- **angles**: [90.0, 154.0]
- **gate**: For 376 keV: sum of 7 cleanest coincidence gates (316, 319, 400, 417, 471, 565, 625 keV). For 462 keV: gated on 316 and 400 keV, with lower/clean gate on left part of 316 keV (313 keV) to avoid 463/465 keV contamination.
- **polarization_calibration**: A = (a*N_perp - N_par)/(a*N_perp + N_par), a(E_gamma) = 0.975(24) + 7.6(379)e-6 * E_gamma (keV) calibrated with 152Eu, 133Ba, 60Co. P = A/Q using sensitivity Q curve from Zheng et al. PRC 87, 044328 (2013) for same clover type.
- **alignment_treatment**: SCAN_COMBINE
- **curve_evaluation**: Yes: fixed-sigma/I conditional P-Rac curves, repeated across different sigma/I values.
- **final_alignment_condition**: All allowed curves through experimental uncertainty box; authors explicitly state sigma/I not restricted. No single final fixed value; no probability marginalization specified.
- **alignment_details**: Main p.3 and Supplement pp.3-4：逐 σ/I 绘制条件曲线，将所有穿过实验误差矩形的允许解综合为 δ 范围。图示0.2/0.3等不是报告的扫描上下限；完整数值扫描域未公开。
- **delta_convention**: E2/M1 as reported; exact phase convention and conversion between sources not established.
- **uncertainty_model**: Experimental (Rac, P) rectangular uncertainty box combining statistical and 5% systematic detector error, mapped to delta envelope over unrestricted sigma/I scan.
- **locator**: PLB 828 (2022) 137010, pp. 2-3; Supplement pp. 1-4, Figs. 1-2

### S20_ATLAS_AD

- **ref_id**: S20
- **reaction_setup**: 174Yb(19F,6n)187Au at 105 MeV (57 Compton-suppressed Ge) and 115 MeV (73 Ge), enriched 174Yb target (13 mg/cm2 with 33 mg/cm2 208Pb backing), Gammasphere in triple-coincidence mode (1.08e9 events)
- **angular_definition**: Full angular distributions measured and fitted (p.3, Fig.3), not a two-angle ratio; numerical A2/A4 not tabulated.
- **angles**: 17 Gammasphere angular rings mentioned (p.3); exact complete angle list not given. Fig.3 shows angular distributions; do not infer a two-angle ratio.
- **gate**: Coincidence gated matrices and cubes (details stated in text to be provided in Ref. [26])
- **polarization_calibration**: NA: no linear-polarization result reported for this experiment.
- **alignment_treatment**: UNREPORTED
- **curve_evaluation**: Angular-distribution fits; no documented numerical sigma/I or fixed/free choice in this paper.
- **final_alignment_condition**: UNREPORTED. Alignment and attenuation details deferred to Ref.[26]. This cannot be counted as confirmed fixed sigma/I.
- **alignment_details**: PRL 2020 p. 3 states: "Further details, including a discussion of the various factors that might affect the extraction of final results—efficiency corrections, spin alignment, attenuation coefficients etc.—will be provided in Ref. [26]". Numeric sigma/I and attenuation treatment were not reported in S20 PRL text.
- **delta_convention**: E2/M1 for Delta I=1 links as reported; stretched-E2 controls carry a separate unresolved higher-multipole interpretation.
- **uncertainty_model**: Fit errors quoted on delta and E2 percentage in Fig. 3(a)-(h)
- **locator**: PRL 124, 052501 (2020) pp. 3-4, Figs. 2-3

## Provisional Reasoning

- Evaluating each forward response at specified parameter values is computational conditioning; it is not evidence that the final inference fixes one of those values.
- Scanning allowed regions, joint parameter estimation and probability marginalization remain different statistical procedures. Do not collapse them into either fixed-single-value or prior-free labels.
- W77 is a 1977 paper, not a 1960s paper. Its original benchmark-corresponding delta signs are +0.18(5), -2.46(15) and -0.02(3). A sign conversion must be derived before comparison with other conventions; this pilot performs no such conversion.
- W77 Table3 uses uncertainty0.15 for the947.6-keV transition whereas text/Table4 use0.16. This pilot uses Table3 and retains the discrepancy.
- G22 Fig.3 prints delta/error labels but plots P/Rac without a numerical table. No precision is invented by visual reading. Existing user transcriptions are not reclassified as primary table entries.
- The L22 polarization-sensitivity source is Herzan et al., PRC92,044310(2015), Supplement Ref.6; it is not the general Starosta1999 method citation.

## Assumptions

Parent assignments of inferred multipoles use the lowest two allowed radiative multipoles only. Those labels remain explicitly inferred. Original errors do not automatically share the same confidence definition. Derived final-state energies used for identity do not acquire independent measurement status.

## Competing Explanations

Missing sigma/I reporting may reflect fixed parameters, calibration, a fit, use of another population parameterization, or omitted documentation. A positive polarization asymmetry is not by itself a quantitative large-delta determination. Conflicting Au/Pr results retain their separate experiments and source-specific interpretations.

## Transfer Conditions

Preserve full angle-group and gating definitions, asymmetry versus P, Q calibration, phase convention and independent data lineage before any PADO replay. The original bibliography is linked through the source pages above and all seven original files were hash-checked locally.

## Failure Conditions

Do not infer the frequency of fixed alignment from this selected pilot, count each transition as an independent method, substitute DCO for ADO, turn illustrative sigma ticks into scan limits, or equate quoted delta interval mass with demonstrated coverage.

## Falsification or Reverse Tests

Inspect each cited page and the author-explicit method statements. A full-text or SI statement documenting fixed/free alignment would revise UNREPORTED. An explicit sign-convention derivation can resolve the W77 sign correspondence without changing the original records.

## Open Questions

- User evaluation of workbook fields, five-column error convention and navigation.
- Exact phase-convention reconciliation across papers.
- Numerical digitization or primary numeric input for G22 P/Rac, with explicit extraction uncertainty.
- Later supporting publications for the M15/S20 deferred experimental methods.
- A future broadly collected corpus and explicit independent-experiment denominator for the word commonly.

## Human Review

The user has requested an initial workbook-format review before expansion. This is a workflow scope boundary, not a scientific evidence eligibility rule. No human review has been claimed.

## Promotion or Rejection History

| Date | event | previous state | new state | reason | target |
|---|---|---|---|---|---|
| 2026-11-10 | Parent primary-source audit of Gemini extractions | worker draft | bounded pilot | Corrected calibration, unsupported angles/scan limits, uncertainty interpretation and provenance | local workbook; no large-scale collection |

## Artifacts

- Workbook: `raw/writing/pado/20261029_review_v1/mixing_ratio_sigma_I_pilot_20261110.xlsx` (local trial; original template retained).
- Audited machine export: `outputs/literature-acquisition/20261110-pado-delta-pilot/audited-extraction.json`.
- Raw worker drafts and parent correction list remain in the same output directory for audit only; use this knowledge note and primary sources for reusable claims.
