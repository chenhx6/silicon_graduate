---
type: research-note
title: "PDM five-nuclide survey: quantitative P-joint extraction and alignment reporting"
aliases: [PDM five-nuclide P-required survey]
created: 2026-11-18
updated: 2026-11-18
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [wadsworth-1977-61ni-levels, lv-2022-evidence-against-wobbling-135pr, guo-2022-low-spin-wobbling-187au, mukherjee-2022-shape-coexistence-octupole-72se, lv-2022-transverse-wobbling-136nd]
created_from: "User-requested nuclide-level survey redesign"
tags: [pdm, mixing-ratio, linear-polarization, alignment]
---

# Five-nuclide PDM literature survey

## Research Trigger

The user subsequently requested a data-only `Data` sheet. The current combined workbook is `raw/writing/pado/20261029_review_v1/pdm_nuclide_survey_20261118_with_data.xlsx`: the same five-row Nuclide summary plus22 reported transition records, G22 Fig.3(a,b), and SE22 TableII/Fig.6. The data sheet has no assessment, recommendation or model-result columns. It reuses the earlier audited originals; plotted-only G22 inputs link to the original figure rather than invented numerical transcription.

The added136Nd numerical row follows the primary paper's body and Fig.3: P=0.02(+0.04,-0.05), Rac=0.55(5), AP=0.03(+0.06,-0.07), and delta=-0.48(+0.13,-0.14). These are author-reported values, not a new fit. The source remains [[lv-2022-transverse-wobbling-136nd]].

The user needs a readable nuclide-level survey for two purposes: establish how literature reports and handles sigma/I for reviewer correspondence, and identify P plus angular-observable inputs for future PDM analysis. The active workbook is `raw/writing/pado/20261029_review_v1/pdm_nuclide_survey_20261118.xlsx`, with five rows and no transition/delta table.

## Grounded Evidence

Inclusion requires physical linear polarization P to participate in quantitative joint extraction of E2/M1 delta. Measured asymmetry plus documented Q calibration is acceptable where the original analysis uses it as P. A sign-only electromagnetic-character check is insufficient.

| Nuclide | Source | Joint inference | Numerical sigma/I reporting | PDM preparation | Locator |
|---|---|---|---|---|---|
| 61Ni | [[wadsworth-1977-61ni-levels]] | 角分布系数＋P联合拟合，并加入复合核模型取向约束。 | 未给σ/I；使用其他布居参数。 未给σ/I | 由a₂/a₄重建R_ADO并传播系数误差；核对布居模型。 | p. 36, Section 2; Table 3, pp. 40-41; Table 4, p. 42 |
| 135Pr | [[lv-2022-evidence-against-wobbling-135pr]] | P–Rac联合求中心值，再沿观测误差边界扫描求区间。 | 说明了求解方式，未列最终σ/I数值。 未列最终值 | 已有P和Rac；需按实际分组角度及探测器权重计算响应。 | 主文Table 1/Fig.2；补充材料pp.1、4–5。 |
| 187Au | [[guo-2022-low-spin-wobbling-187au]] | P–Rac联合允许区间：逐取向计算曲线，合并允许解。 | 有不同取值曲线；不指定最终单值。 例：0.2、0.3（图示） | 需取得P/Rac原始数值，或数字化图点；已有用户转录可回核。 | 主文Fig.3、p.3；补充材料pp.1–4/Fig.2。 |
| 72Se | [[mukherjee-2022-shape-coexistence-octupole-72se]] | ANGCOR计算响应，P–DCO联合χ²拟合。 | 明确给出σ/j=0.3。 0.3 | 先用Δ/Q换算P；使用DCO门条件和响应，检查ΔI=0支持。 | Table I、II；方法p.7；Fig.7、p.8。 |
| 136Nd | [[lv-2022-transverse-wobbling-136nd]] | P–Rac响应曲线与实验点联合提取。 | 主文未明确给出σ/I数值。 未给出 | P和Rac有数值；需补角度、门定义，再确定PDM积分域与权重。 | 主文Sec.II–III、Fig.3；实验方法Ref.[38]。 |

## Provisional Reasoning

- The Nd isotope is136Nd, DOI10.1103/PhysRevC.105.034302. The primary paper explicitly says a combined linear polarization P and Rac method extracts the connecting-transition mixing ratio. P and Rac numerical inputs are available in the body; precise geometry is referred to earlier experimental work, Ref38. The inspected primary text does not give a numerical sigma/I value. This does not establish what the cited full analysis assumed.
- W77 uses population parameters beta and x with model-estimated alignment constraints. Lack of a numerical sigma/I in that parametrization is not evidence for a prior-free analysis.
- L22 jointly solves central parameters and scans response boundaries; G22 combines conditional curves over allowed alignment. Their final inference is not a single fixed-sigma result.
- SE22 uses sigma/j=.3 calibrated from same-experiment E1 transitions and then fixed. Physical P requires Delta/Q conversion, and its DCO and spin-change response must be matched before PDM use.
- M15's separate polarimetry character check and S20's absence of polarimetry do not satisfy this active quantitative P-joint inclusion rule. They remain historical evidence, not rows in this workbook.
- Existing user-transcribed G22 inputs do not become primary numerical table entries without reconciliation against original points/errors.

## Assumptions

Each row represents one selected study for a nuclide, not every paper or transition ever reported for that nuclide. The original measurement definitions and uncertainty/calibration dependencies remain necessary for future replay.

## Competing Explanations

Unreported sigma/I can reflect other population parameters or deferred method descriptions. It is not automatically fixed, freely fitted, or absent from the calculation. Fixed experimental calibration and an unsupported assumed constant are different categories.

## Transfer Conditions

Reconstruct a ratio from W77 coefficients with their errors and covariance when available. Recover G22 numerical graph inputs. Use actual detector-group responses for L22. Convert asymmetry with Q and include the DCO gate for SE22. Obtain referenced geometry for136Nd and state PDM integration bounds and weights rather than imposing a single fixed alignment solely because the paper omitted it.

## Failure Conditions

Do not treat raw asymmetry as calibrated P, treat sign-only polarization as a numerical joint fit, substitute DCO for ADO, or use these five selected papers to estimate the prevalence of fixed alignment across the field.

## Falsification or Reverse Tests

Check the exact original methods/figures and cited experimental papers. A documented numerical alignment or different detector/gate definition in those references can update the reporting and replay-readiness fields without changing what the short primary paper itself states.

## Open Questions

- Exact136Nd detector groups and Rac gate convention from Ref38.
- PDM input recovery/conversion and response support, then study-specific replay.
- Whether the five-row workbook is readable for the user's review.

## Human Review

User will inspect the workbook format and its methodological summaries. No user scientific review or new PDM fitting has been claimed.

## Promotion or Rejection History

| Date | event | previous state | new state | reason | target |
|---|---|---|---|---|---|
|2026-11-18|Survey scope clarified|Transition-level pilot|Five-nuclide P-joint summary|Review alignment reporting and prepare PDM inputs|Nuclide workbook|
