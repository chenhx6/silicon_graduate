# Minimal proposed updates — text only

These passages are suggestions for the parent. This review has not edited the article or any knowledge page.

**Article insertion.** The natural location is immediately after the existing paragraph that distinguishes the 137Ba 19/2 isomer measurement from the missing 15/2→11/2 strength, before the conclusions.

> A separate frozen comparison with the tentative \(^{137}\)Ba \(19/2^-\) isomer limits the spectroscopic reach of this reconstruction. The primary \(19/2_1\to15/2_1\) prediction is 22.47 W.u. with a 1173.6-keV model spacing, compared with 0.46(3) W.u. at 120.1 keV. Although one conditional operator and an alternative predeclared daughter give 0.420 W.u., a much stronger modeled decay remains open. For the seven tested operators and two candidate parents, summing all open model E2 radiative rates gives conditional half-life upper bounds no larger than \(2.811\times10^{-4}\) ns, compared with 589(20) ns. These bounds assume the modeled spectrum and state identification; omitted conversion and other widths can only shorten the lifetime of that unchanged scheme. The measured strength and half-life share the same experimental origin and are not independent validation data. The tested transition lies outside the initial-\(11/2\) cubic loop, so this check does not directly refute the moment decomposition, but it prevents treating calibration or a selected-branch near-match as validation of the full scheme. Source-energy reconstruction fidelity remains under independent review.

Use the existing Vogt citation and add the frozen protocol/result identifiers to the reproducibility material. If space is limited, move the alternative-branch details to a supplement; retain the conditional failure and its scope in the main text.

**Conclusions adjustment.** Add one clause to the existing limitation sentence:

> The static-moment discrepancies and the conditional failure of the separate high-spin isomer check limit claims of spectroscopic validation; the present result concerns the explicitly defined finite-model mechanism.

Do not replace the 11/2 mechanism conclusion with a claim that all IBFM is falsified, and do not attribute the discrepancy to the original authors before reconstruction fidelity is settled.

**Minimum knowledge record to add later, under the parent's chosen owning page:**

| Field | Proposed content |
|---|---|
| claim_kind | model-result |
| Claim | The frozen 137Ba reconstruction, under its two candidate parent assignments and seven tested E2 operators, is incompatible with the tentative isomer half-life if its modeled decay scheme is adopted. A selected alternate B(E2) near the quoted value does not remove a dominant fast model decay. |
| Calculation locator | `outputs/l4/20261106-a130-next-evidence/isomer-benchmark/decay-width-results.json`, fourteen `rows`; detailed competing routes in `branches`. |
| Mapping/strength locator | `energy-mapping-frozen.json`; `results.json`, rows for `primary` and `Q136_plus_007_splus`, parent ordinal 0. |
| Experimental locator | Vogt et al., PRC95,024316; locators as registered in the frozen `protocol.json`. Tentative assignments retained. |
| Source dependence | The quoted B(E2) and 589(20)-ns half-life derive from the same measurement; not independent evidence entries for significance testing. |
| Applicability | Conditional on the model spectrum, amplitudes and mapping. Not a model-independent empirical bound or complete lifetime prediction. No direct falsification of the initial-11/2 q3 loop. |
| Fidelity boundary | Original-source 135/137Ba energy reconstruction is under separate review; no verdict about the original authors' calculation. |

**Next question, kept singular:** is the strong 19/2_1→15/2_1 escape route a faithful result of the intended fixed-input reconstruction, or does the independent energy replay identify a reconstruction/state-correspondence discrepancy?
