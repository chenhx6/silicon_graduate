---
type: source
title: "Frauendorf 2015 - The low-energy quadrupole mode of nuclei"
aliases: [Frauendorf 2015 quadrupole mode, tidal wave TPSM review]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: review-theory
reading_depth: deep-read
title_original: "The low-energy quadrupole mode of nuclei"
authors: [S. Frauendorf]
journal: "International Journal of Modern Physics E"
year: 2015
volume: 24
article: 1541001
pages: "1-38"
doi: "10.1142/S0218301315410013"
citation_key: Frauendorf_2015
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "https://doi.org/10.1142/S0218301315410013"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/三轴/进动/理论/2015_Frauendorf_The low-energy quadrupole mode of nuclei.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/三轴/进动/理论/2015_Frauendorf_The low-energy quadrupole mode of nuclei.pdf"
raw_sha256: "6503190945574eb2a19dc10555f4abc8866340dc3b84e0ff72068fcb0d9010d5"
nuclei: [102Pd, 152Sm, 62Ni]
reactions: []
experiments: []
models: [Bohr-Hamiltonian, ATDMF, GCM, IBM, TPSM, tidal-wave]
observables: [quadrupole-vibration, gamma-softness, gamma-band-staggering, B(E2), tidal-wave]
methods: [collective-model, generator-coordinate, projected-shell-model]
tags: [quadrupole, triaxiality, gamma-soft, tidal-wave, TPSM, review]
---

# The low-energy quadrupole mode of nuclei

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

- S. Frauendorf, *International Journal of Modern Physics E* **24**, 1541001 (2015), DOI `10.1142/S0218301315410013`。
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/三轴/进动/理论/2015_Frauendorf_The low-energy quadrupole mode of nuclei.pdf`。
- 38-page review; chapter equations/figures and model limitations read.

## Scope and Reading Depth

- Full review read: Bohr Hamiltonian/γ signatures, microscopic ATDMF, GCM, IBM mapping, tidal-wave approach, triaxial projected shell model (TPSM), applications and critical assessment of adiabaticity/decoherence.
- Key concepts checked: 5D quadrupole coordinates, γ-soft/rigid regions, zero-point energy, `102Pd/152Sm/62Ni` examples, `B(E2)` patterns and nonadiabatic coupling.
- Not covered: re-running cited GCM/IBM/TPSM codes or all post-2015 applications.

## Key Results

- The Bohr Hamiltonian classifies quadrupole spectra by potential shape and zero-point fluctuations; γ-softness is a wave-function extent, not simply a nonzero triaxial minimum.
- Microscopic ATDMF, GCM and IBM mappings provide complementary parameter routes but inherit adiabatic assumptions; high-lying/multiphonon states decohere through quasiparticle coupling.
- Tidal-wave and TPSM approaches extend spectral calculations beyond the adiabatic region, linking yrast `B(E2)`/moments of inertia and angular-momentum projection to quadrupole collectivity.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| FR15-1 | Low-energy quadrupole structures require separating β/γ potential shape, zero-point fluctuations and quasiparticle decoherence. | review-framework | direct | PDF pp.1–8, Figs.1–3 | true |
| FR15-2 | Microscopic BH parameters can be derived via ATDMF/GCM and mapped to IBM, but model mappings are not direct experimental shape measurements. | model-framework | direct | PDF Secs.3–5 | true |
| FR15-3 | Tidal-wave and TPSM methods address nonadiabatic/high-spin quadrupole spectra beyond simple BH/IBM assumptions. | model-framework | direct | PDF Sec.6 | true |

## Summary

Frauendorf's review provides the quadrupole-mode counterpart to the rotating-mean-field review: γ-softness, triaxiality, vibrational collectivity, tidal waves and projected-shell-model spectra are organized with explicit adiabatic/decoherence limits.

## Competing Interpretations and Limitations

Energy ratios and `B(E2)` patterns are not unique shape classifiers; model parameters, zero-point fluctuations, pairing and quasiparticle coupling can alter γ-soft/rigid assignments. Tidal-wave/TPSM results remain model calculations rather than direct triaxial observables.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| FR15-AR-1 | Concept chain | 5D quadrupole potential → wave-function/ZPE → E2/energy observables → model comparison. | PDF Secs.2–6 | self-checking |
| FR15-AR-2 | Transfer condition | Cross-nucleus use needs matched potential, boson number, pairing and adiabaticity. | PDF Secs.3–7 | active-L3 |
| FR15-AR-3 | Independence | Review; `102Pd/152Sm/62Ni` examples are cited data/calculations, not new experiments. | Scope/Refs. | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[octupole-softness]]-style potential/wave-function separation, γ-softness diagnostics and [[tidal-wave]]/TPSM model map.
- Persistence: source/index and A≈130 collective-mode project relation.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `FR15-P0-1`: do not infer γ-rigid/γ-soft or direct triaxiality from one energy ratio or model fit.

## Extracted Pages

- Concepts: [[triaxial-deformation]], [[gamma-soft-deformation]], [[tidal-wave]]。
- Models: [[triaxial-projected-shell-model]]。

## Day21周考推断阶梯审计：四极潮汐波（Tidal Wave）转动与B(E2)离心拉伸证据门边界

依据独立审计程序 `system/scripts/day21_checkpoint014_tidal_wave_audit.py` 与审计产物 `outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/tidal-wave-audit-014.json`，确立本源在推断阶梯上的边界：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| FR15-D21-1 | Frauendorf 2015 综述确立低能四极潮汐波（Tidal Wave）转动推断阶梯边界：微观上弱形变 $\gamma$-软核（如 $^{102}	ext{Pd}$）的 yrast 角动量增长并非源于刚性经典旋转或多声子简谐激发，而是由四极形变振幅 $eta_2(I)$ 的离心拉伸主导；在 $^{102}	ext{Pd}$ 中，转动频率由 $2^+$ 的 $278.2	ext{ keV}$ 仅迟缓升至 $10^+$ 的 $490.0	ext{ keV}$（仅增 $1.76$ 倍，远低于刚性转子的 $5.0$ 倍），而实测带内 $B(E2)$ 由 $32(3)	ext{ W.u.}$ 激增至 $105(18)	ext{ W.u.}$（激增 $3.28$ 倍），大幅突破刚性转子的几何饱和极限（$1.69$ 倍），展现出与 $eta_2^2(I) \propto I$ 潮汐波行波模型的高度自洽。推断阶梯确立：严禁仅凭能级比值 $R_{4/2} pprox 2.0 - 2.4$ 断言简谐多声子态或刚性转子，确证潮汐波必须依赖绝对能级寿命测定 $B(E2) \propto I$ 线性伸展轨迹及转动频率迟滞。 | claim-boundary-audit | direct-and-derived | PDF Sec.6 pp.24-28 Figs.17-18; tidal-wave-audit-014.json | true |
