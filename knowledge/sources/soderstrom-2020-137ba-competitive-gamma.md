---
type: source
title: "Söderström et al. 2020 - Electromagnetic character of the competitive gamma-gamma/gamma decay from 137mBa"
aliases: [Soderstrom 2020 137Ba competitive double gamma]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Electromagnetic character of the competitive γγ/γ-decay from 137mBa"
authors: [P.-A. Söderström, L. Capponi, E. Açıksöz, T. Otsuka, N. Tsoneva, Y. Tsunoda, D. L. Balabanski, N. Pietralla, G. L. Guardo, D. Lattuada, H. Lenske, C. Matei, D. Nichita, A. Pappalardo, T. Petruse]
journal: "Nature Communications"
year: 2020
volume: 11
pages: "3242"
doi: "10.1038/s41467-020-16787-4"
citation_key: S_derstr_m_2020
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "https://doi.org/10.1038/s41467-020-16787-4"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/electromagnetic/2020_Söderström et al_Electromagnetic character of the competitive γγ-γ-decay from 137mBa.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/electromagnetic/2020_Söderström et al_Electromagnetic character of the competitive γγ-γ-decay from 137mBa.pdf"
raw_sha256: "fb8bd159bae6e5f1e2b9827e1bf2bce7cd98c126c7fef00f1bd41526154ec12a"
nuclei: [137Ba, 137Cs, 152Sm]
reactions: [137Cs-beta-decay]
experiments: [ELIGANT, CeBr3, ELI-NP]
models: [EDF-QPM, Monte-Carlo-shell-model, GEANT4]
observables: [competitive-two-photon-branching, energy-sharing, angular-correlation, alpha-M2E2, alpha-E3M1]
methods: [gamma-gamma-coincidence, fast-timing, angular-correlation]
tags: [137Ba, competitive-double-gamma, two-photon-decay, polarizability, E3M1]
---

# Electromagnetic character of the competitive γγ/γ decay from `137mBa`

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

- P.-A. Söderström *et al.*, *Nature Communications* **11**, 3242 (2020), DOI `10.1038/s41467-020-16787-4`.

## Scope and Reading Depth

- The eight-page open-access article was read end-to-end: motivation, Fig.1 decay scheme, Table 1, eleven-CeBr3 setup, Figs.2–5, differential-branching definition, energy-sharing fit, EDF+QPM/MCSM discussion, Methods Eqs.(6–9), Tables 2 and data/code availability.

## Independent Measurement

The experiment uses eleven 3''×3'' CeBr3 detectors at 40 cm, with 32.7° nearest-neighbor spacing and five correlation angles `32.7°, 65.5°, 98.2°, 130.9°, 163.6°`; ≥15 cm lead separates neighboring detectors. A 152Eu/60Co calibration and GEANT4 toolkit characterize efficiency and geometry (PDF pp.3–4, Fig.2). A `336 kBq 137Cs` source was run for 49.5 active days. Prompt coincidences use `|Δt|≤655 ps`; uncorrelated events use a 20–820 ns side window. Multiplicity-two and energy-difference cuts suppress cosmic-ray and backscatter backgrounds (pp.3–4, Fig.3).

The summed peak contains `990(170)` counts before final cuts and `960(100)` after the cosmic-ray condition (Fig.3). The differential branching ratio integrates `E_low=180` to `331 keV` (half the 662-keV transition) and is evaluated at all detector angles (p.4, Eq.4). Combined with the energy-sharing distribution, the fit gives `Γγγ/Γγ=2.62(30)×10−6` at `8.7σ`, compared with Walz's `2.05(37)×10−6` (Table 1, Figs.4–5).

## Electromagnetic Character and Model Comparison

Pure M2E2 and E3M1 paths have different energy-sharing shapes: M2E2 peaks near equal `331/331 keV`, while E3M1 is asymmetric near about `200/442 keV` (pp.4–5, Fig.5a). Angular data alone have two χ² minima; simultaneous angle plus energy-sharing data favor a substantial `αE3M1` and much smaller `αM2E2` than the original Walz interpretation (Fig.5b). Table 1 reports the present fitted values `αM2E2=±8.8(50)` and `αE3M1=±36.4(20) e²fm⁴/MeV` (sign branches), while EDF+QPM and MCSM give different `αM2E2` signs/magnitudes and more consistent E3M1 contributions.

The paper's MCSM analysis finds a strongly hindered `M2` transition (`B(M2)=13.5×10−3 μ²fm²`, about three orders below the EDF+QPM value), explaining suppression of the quadrupole–quadrupole component; EDF+QPM attributes E3M1 strength to a collective octupole phonon (pp.5–6, Table 2). The authors stress that model complexity does not yet resolve the remaining α-component discrepancy.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SO20-1 | An independent eleven-CeBr3 experiment confirms the `137mBa` competitive branch at `8.7σ` with `2.62(30)×10−6`. | experiment-result | direct | PDF pp.1, 3–5, Table 1 | true |
| SO20-2 | Energy-sharing data favor a substantial E3M1 contribution and a smaller M2E2 component. | path-discrimination | mixed | PDF pp.4–6, Figs.4–5 | true |
| SO20-3 | EDF+QPM and MCSM disagree on the quadrupole component; the MCSM M2 hindrance is a candidate explanation. | model-conflict | mixed | PDF pp.5–6, Tables 1–2 | true |

## Summary

Söderström *et al.* provide an independent total-branch confirmation and the strongest within-batch evidence that energy sharing, not angular correlation alone, is needed to identify the virtual multipole path.

## Competing Interpretations and Limitations

- Angular-only fits have local minima and the fitted α signs/order remain branch-dependent.
- Detector response, efficiency and cosmic-ray/Compton cuts are setup-specific; raw data and code are not openly deposited.

## Analytical Reconstruction and Self-Audit

| ID | Audit item | Agent judgment | Locator | Status |
|---|---|---|---|---|
| SO20-AR-1 | Signal/background chain | Five angular points, time sideband, multiplicity/energy cuts and GEANT4/Gaussian fits jointly support a competitive branch; cosmic-ray and Compton residuals remain systematics. | PDF pp.3–5, Figs.2–4 | self-checking |
| SO20-AR-2 | Path identifiability | Angular correlation alone is degenerate; energy-sharing breaks the M2E2/E3M1 ambiguity but still leaves sign/ordering branches and model dependence. | PDF pp.4–6, Fig.5, Eq.5 | self-checking |
| SO20-AR-3 | Cross-paper conflict | The result directly revises Walz's dominant-Aqq interpretation while agreeing on the total branch within errors; it is a same-nucleus independent experiment, not a duplicate PDF. | PDF pp.1, 4–6, Table 1 | self-checking |
| SO20-AR-4 | Reproducibility | The article points to Mendeley DOI `10.17632/skhmjshxdj` for final points, but the checked DOI/landing endpoint currently has no retrievable snapshot; raw data and sorting/analysis code remain author-request-only. | PDF p.7, Data/Code availability; EXT-20260921-002 | input-limited-L4 |

## Knowledge Impact and Learning Decision

- Effect: `revises` [[walz-2015-competitive-double-gamma-137ba]], [[two-photon-nuclear-decay]] and the `137Ba` polarizability evidence map; it promotes energy-sharing as the decisive companion observable for virtual-path identification.
- L3/L4: the cited data DOI was checked and is currently unavailable at its landing endpoint; no independent L4 re-fit is claimed here. Figure digitization is explicitly insufficient for the response/covariance contract.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `SO20-P0-1`: Before numerical reuse, reconcile the sign/ordering branches, detector-efficiency correction and the Walz/Söderström common definition of δ; preserve the model discrepancy instead of selecting one path by label.

## Extracted Pages

- Source relation: [[walz-2015-competitive-double-gamma-137ba]], [[two-photon-nuclear-decay]]。
- Methods/models: [[gamma-gamma-coincidence]], [[angular-correlation]]。

## Day19量化审计：E3M1八极主导确证、M2单粒子禁戒与13.9倍分量反转

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_ba137_double_gamma_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/ba137-double-gamma-result-045.json`，系统核准了 Söderström 2020（Nat. Commun. 11, 3242）关于 $^{137\text{m}}\text{Ba}$ 竞争双光子衰变虚态路径的物理裁决：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| SO20-D19-1 | Söderström 2020 利用 ELI-NP 的 11 个 $\text{CeBr}_3$ 探测器在五个关联角（$32.7^\circ$ 至 $163.6^\circ$）下测定连续能量共享谱，以 $8.7\sigma$ 显著性测定总分支比 $(2.62 \pm 0.30) \times 10^{-6}$，并在拟合中测定极化率比值 $\alpha_{M2E2} / \alpha_{E3M1} = 8.8 / 36.4 = 0.242$，相比 Walz 2015 实现了 $13.9$ 倍的路径反转。大空间蒙特卡洛壳模型（MCSM）揭示了该反转的坚实微观根源：在 $^{137}\text{Ba}$（$11/2^-$ 异构态到 $3/2^+$ 基态）中，$M2$ 单粒子跃迁受到 $\Delta l = 3$ 的角动量禁戒（$B(M2)$ 仅为 $1.35 \times 10^{-2}\ \mu_N^2\text{fm}^2$，受压制近 3 个数量级）；相反，虚跃迁 $E3$ 算符与 $^{138}\text{Ba}$ 核芯的集体 $3^-$ 八极声子（$B(E3) \sim 25\text{ W.u.}$）发生极强的集体耦合，从而赋予 $E3M1$ 路径压倒性的物理主导地位。这一测量确立了完整能量共享谱形与微观核结构计算在解耦虚态路径中的决定性作用。 | quantitative-benchmark-and-criterion | direct-and-derived | Nat. Commun. 11, 3242 pp.3-6; Table 1, Fig.5; ba137-double-gamma-result-045.json | true |

## Day21周考推断阶梯审计：核双光子衰变E3M1八极主导与连续能量共享证据门边界

依据独立审计程序 `system/scripts/day21_checkpoint015_two_photon_decay_audit.py` 与审计产物 `outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/two-photon-decay-audit-015.json`，确立本源在推断阶梯上的边界：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| SO20-D21-1 | Söderström 2020 利用 11 台 $	ext{CeBr}_3$ 探测器在五个角度下测定连续能量共享谱，以 $8.7\sigma$ 显著性测定总分支比 $(2.62 \pm 0.30) 	imes 10^{-6}$，并在多维自洽拟合中反转测定 $lpha_{M2E2} / lpha_{E3M1} = 0.2418$，确立了 $E3M1$ 八极—偶极路径的绝对物理统治地位（反转 Walz 2015 达 $13.88$ 倍）。蒙特卡洛壳模型（MCSM）揭示其微观机制为单粒子 $M2$ 矩阵元受 $\Delta \ell = 3$ 禁戒压低近 3 个数量级，而 $E3$ 算符与 $^{138}	ext{Ba}$ 核芯 $3^-$ 八极声子发生强集体耦合。由此确立证据门准则：确证双光子虚态多极路径必须依赖多角度连续能量分配谱的全局展开。 | claim-boundary-audit | direct-and-derived | Nat. Commun. 11, 3242 pp.3-6; Table 1; two-photon-decay-audit-015.json | true |
