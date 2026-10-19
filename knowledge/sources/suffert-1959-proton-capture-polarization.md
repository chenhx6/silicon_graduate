---
type: source
title: "Suffert, Endt & Hoogenboom 1959 - Polarization measurements of proton-capture gamma rays"
aliases: [Suffert 1959 proton capture polarization]
created: 2026-09-21
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: experiment-and-method
reading_depth: deep-read
title_original: "Polarization Measurements of Proton Capture Gamma Rays"
authors: [M. Suffert, P. M. Endt, A. M. Hoogenboom]
journal: Physica
year: 1959
volume: 25
pages: "659-670"
canonical_source: "Suffert, Endt & Hoogenboom, Physica 25, 659 (1959)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1959_Suffert et al_Polarization measurements of proton capture gamma rays.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1959_Suffert et al_Polarization measurements of proton capture gamma rays.pdf"
raw_sha256: "ea2742bd196d30497fc919839fb249dfd7e50a88411411831d981604b2016669"
nuclei: [25Al, 31P, 33Cl]
reactions: [24Mg-p-gamma, 30Si-p-gamma, 32S-p-gamma]
experiments: [utrecht-cockcroft-walton, nai-compton-polarimeter]
models: [angular-distribution-mixing-ratio]
observables: [linear-polarization, compton-asymmetry, E2-M1-mixing-ratio, spin-parity]
methods: [compton-polarimetry, angular-distribution, proton-capture]
tags: [polarization, proton-capture, historical-method, mixing-ratio]
---

# Polarization measurements of proton-capture γ rays

## Bibliographic Record

- M. Suffert, P. M. Endt & A. M. Hoogenboom, *Physica* **25**, 659–670 (1959).

## Scope and Reading Depth

- The 12-page article was read end-to-end, including Eqs.(1–9), Figs.1–4, Table I, corrections, discussion of all eight lines and references. The scan's page order was checked; no unrelated neighboring article is included in this source page.

## Experimental Design

Eight γ rays from resonances in `24Mg(p,γ)25Al`, `30Si(p,γ)31P` and `32S(p,γ)33Cl`, with energies `0.8–8.0 MeV`, were emitted at 90° to the proton beam. A 2-inch NaI scattering crystal and two 4-inch NaI counters at interchangeable azimuths measured the Compton counter ratio (PDF pp.659–664, Figs.1–3). A ratio `R=[(NB1/NA1)/(NB2/NA2)]^{1/2}` gives `P=(1/p)(R−1)/(R+1)` after eccentricity/background and solid-angle corrections (pp.664–667, Eq.9).

The paper derives the proton-capture direction–polarization correlation for mixed M1+E2 or E1+M2 transitions, including the sign of the `cos 2φ` term (pp.660–662, Eqs.1–7). The Compton analyzing power is the Klein–Nishina ratio `p(θ)`, and the shortest statistical run time maximizes `σ_c(θ)p²(θ)` (p.662, Eq.8). Corrections include finite scattering azimuth (about 12% reduction in `p`), scattering-angle (≤3%), solid angle (≤1.5%), target eccentricity and contaminant/off-resonance background (pp.665–667).

## Results

Table I resolves ambiguities left by angular distributions. The `2.85 MeV` and `2.86 MeV` levels in `33Cl` are assigned `5/2+` and `3/2−`; the `2.69`/`2.24 MeV` lines in `25Al` and `2.85 MeV` line in `33Cl` are predominantly M1, while the `8.04 MeV` `31P` line is predominantly E2 (abstract, Table I, pp.667–669). The `33Cl` 2.86-MeV parity conclusion uses combined runs 6/7; the high-energy `31P` polarization is acknowledged as statistically limited and potentially affected by pair production/bremsstrahlung (p.669).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SEH59-1 | Compton polarization resolves spin/parity or E2/M1 alternatives left by proton-capture angular distributions. | experiment-result | direct | PDF pp.659–669, Table I | true |
| SEH59-2 | Counter-ratio polarization requires geometry, eccentricity, background and analyzing-power corrections. | method-result | direct | PDF pp.661–667, Eqs.5–9 | true |
| SEH59-3 | The 8.04-MeV result retains a pair-production/bremsstrahlung and statistical limitation. | limitation | direct | PDF p.669 | true |

## Summary

Suffert *et al.* demonstrate how linear polarization supplies the missing observable for proton-capture spin/parity and mixing-ratio ambiguities, while preserving a detector-specific response chain.

## Competing Interpretations and Limitations

- High-energy attenuation and finite geometry can bias the polarization; the paper does not provide a modern response simulation.
- Angular-distribution alternatives depend on the external angular data and their own consistency, so polarization is not independent of those assumptions.

## Analytical Reconstruction and Self-Audit

| ID | Audit item | Agent judgment | Locator | Status |
|---|---|---|---|---|
| SEH59-AR-1 | Ambiguity resolution | Angular-distribution alternatives are separated by the sign/magnitude of Compton polarization, not by polarization alone detached from `R` and `p`. | PDF pp.660–669, Table I | self-checking |
| SEH59-AR-2 | Detector response | `p(θ)`, finite geometry, eccentricity and background corrections are setup-specific; no universal high-energy polarimeter sensitivity follows. | PDF pp.661–667, Eqs.5–9 | self-checking |
| SEH59-AR-3 | High-energy boundary | Pair production/bremsstrahlung may attenuate the 8.04-MeV result; the authors leave that discrepancy unresolved. | PDF p.669 | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[compton-polarimetry]], [[linear-polarization-asymmetry]], [[angular-distribution]] and the spin/parity evidence checklist; it supplies a proton-capture calibration lineage distinct from in-beam heavy-ion alignment.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `SEH59-P0-1`: Preserve the geometry/energy-specific Compton efficiency and the high-energy pair-production boundary before transferring the historical `P` values.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]], [[angular-distribution]]。


### 1959 原件复核：normal 轴与 plane 轴不是同一个 P

2026-10-19 同一 Day16 session 重新完整读 12 页 Sections 1–5、参考文献及 Eqs.(1–9)，核 Figs.1–4 与旋转后的 Table I。原 PDF SHA256 保持；旧三条 claim 的 review 标记保持。Crossref 另外核得 DOI [10.1016/S0031-8914(59)96977-0](https://doi.org/10.1016/S0031-8914(59)96977-0)，题名、三作者、Physica 25、659–670 与原件一致；直接 API DNS 失败、publisher 403 另存，不把访问失败当成未读本地原件。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| SEH59-4 | Eq.(2) 的电场角 φ 从 beam–γ 平面的法线量起，Eq.(3) 的 P 为 normal 减 plane 的电场强度。B15文字把角从 plane 量起；同一物理辐射应有 P_SU=−P_plane，不能因 B15称 following Suffert 就同号替换。 | explicit-axis-crosswalk | original-and-exact-algebra | p661 Eq.(2)后定义及Eq.(3) | true |
| SEH59-5 | Fig.3 的位置1中 B 沿 beam 投影、A 沿法线，位置2交换两类散射方向。其 R=sqrt[(NB1/NA1)/(NB2/NA2)] 对应 N_scatter,plane/N_scatter,normal；Eq.(9) 正号与 normal-axis P 一致。 | count-role-and-sign-contract | original-geometry-and-algebra | p664 Fig.3/Eq.(9) | true |
| SEH59-6 | 固定两个 detector 各自效率和每位置曝光时，四计数比可约去这些乘法量；跨位置相对效率漂移仍留下 sqrt[(εB1/εA1)/(εB2/εA2)]。原件另校 eccentricity/background，不能把位置交换当作所有系统项都已消除。 | conditional-cancellation-and-failure | exact-design-derivation | p664 counter-ratio定义；p665 eccentricityparagraph | true |
| SEH59-7 | 用 Table I 的八组 corrected R、p 作 Eq.(9) 重算，P约为 .1053/.6974/−.5925/−.3772/.5411/.9444/−.5930/−.04082；与 final P 最大差 .01560。原表还含未提供逐行数值的 θ 接受角修正和舍入，未宣称逐位闭合。 | printed-input-arithmetic | actual-computation | p667 Table I cols6–8/footnote c | true |
| SEH59-8 | 两项 unpolarized control 的 R=1.032(.023)、1.029(.016) 若独立加权得1.029978(.013134)，与作者采用1.030(.013)相容。它们校 eccentricity，不校所有能量的 p；共同 Re 的误差在各行P间产生条件 rank-one Cov，不能重复加入原表误差。 | control-and-shared-nuisance | original-and-conditional-propagation | p668 four-eccentricity-runsparagraph | true |
| SEH59-9 | 25Al 的2.69MeV线 Table I 用一套外部AD给 x=.35(.10)/11(6)、预测P=.01(.02)/.39(.05)；实测P=.11(.14)。这是一套有数据身份的双候选，不是两个独立偏振实验。 | same-transition-companion-candidates | original-experiment-and-imported-AD | p667 Table I run1 | true |
| SEH59-10 | 作者另讨论 Varma–Jack 的AD系数−.75(.04)，得 x=.72/2.3、预测P=0/.19，并明确若该AD正确，run1不能裁决2.69MeV混合比。这限制摘要和旧笔记“已解决歧义”的无条件措辞；不同AD候选不能合并成一次四根拟合。 | author-counter-evidence-and-source-dependence | direct | p669 Runs1and2paragraph | true |
| SEH59-11 | 8.04MeV偏振与大mixing分支预测仍近2σ有差，作者无法区分统计与pair/bremsstrahlung衰减；2.37MeV谱的高能尾被当作两位置相等背景，原事件未得，未认证该假设。 | unresolved-companion-and-background | direct | p669 Run4；p666 Fig.4后背景paragraph | true |
| SEH59-12 | Eq.(1)称x为E2/M1 amplitude mixing ratio，未在本文给出足以跨到KS/RB的完整operator/reduced-ME与state-order合同。本次只转换P的坐标，不将历史x的数值或正负号自动换成现代δ。 | phase-readiness-boundary | original-definition-and-limited-inference | p661 Eq.(1)后x定义；Ref8/9 | true |

以 beam–γ 平面为共同散射方位零点 χ，原装置给 `N(χ)∝1+p P_SU cos(2χ)`；若另定义 `P_plane=−P_SU`，则同一个 observable 写成 `1−p P_plane cos(2χ)`。两式恒等，实际 Fig.3 计数比无需变化。B15 的 operational `As_fit=a2/a0` 若沿同一零点，就与 `p P_SU` 同号；其文字 endpoint `N90−N0` 与 fit coefficient 的区别仍要保留。本次原读明确了一条上游坐标桥，未取得 B15 actual producer，未将其 literal 公式边界改写为真实数据错误。

Table I 的 `σP_R=2σR/[p(1+R)^2]` 只从 quoted corrected R 传播。八组实际值与原 σP 的差均小于 .02，但 p、背景、最终 θ 修正及其 Cov 未恢复，因此不是完整误差预算。若 correctedR=Rnet/Re，固定 Rnet、p 时 `∂P/∂Re=−2R/[p Re(1+R)^2]`；原 Re=.013 的误差单独给八行 σP 约 .0302/.0257/.0289/.0769/.0315/.0308/.0245/.0126。这个共同分量不能在不知道作者误差组成时再加一次。

对 run1 只作显式条件的 Gaussian point-likelihood 诊断：固定原候选预测P、只用σobs=.14，第一套候选的 χ² 为 .510/4.000，L_small/L_large≈5.73；另一套 AD 候选 χ² 为 .617/.327，比值≈.865。它们不是 Bayes factor、排除置信度或新δ拟合；缺预测误差/AD Cov也不把这些数冒充统计裁决。原作者保留的后者多解比任何“偏振必能唯一选根”的口诀更有约束力。

阅读决策为 `revises`：对这一条2.69MeV线，偏振的判别力依所采用AD数据和几何合同；`supports` position-exchange及normal-axis符号链；`limits` 把原x、原p或原实验结论直接迁入B15/现代DCO。新claims均needs_review，未增加独立实验或课程学分。

复算：[原表/符号脚本](../../system/scripts/day16_suffert1959_convention_audit.py)，[固定合同与结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/suffert1959-convention-audit-result.json)。原计数、逐行修正、外部AD原表及联合Cov仍缺；没有制造原实验事件。

相关页：[[bizzeti-2015-agata-triple-cluster-polarimetry]]、[[compton-polarimetry]]、[[linear-polarization-asymmetry]]、[[multipole-mixing-ratio]]。
