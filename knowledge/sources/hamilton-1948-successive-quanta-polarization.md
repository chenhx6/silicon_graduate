---
type: source
title: "Hamilton 1948 - Polarization and direction of propagation of successive quanta"
aliases: [Hamilton 1948 direction-polarization correlation]
created: 2026-09-21
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: theory-method
reading_depth: deep-read
title_original: "Polarization and Direction of Propagation of Successive Quanta"
authors: [Donald R. Hamilton]
journal: "Physical Review"
year: 1948
volume: 74
pages: "782-788"
canonical_source: "Hamilton, Phys. Rev. 74, 782 (1948)"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/mixing ratio/1948_Hamilton_Polarization and Direction of Propagation of Successive Quanta.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/mixing ratio/1948_Hamilton_Polarization and Direction of Propagation of Successive Quanta.pdf"
raw_sha256: "f569db64c7e402558fd574839ba5c3da56bc8ecf1b37dab330be706118dc0879"
nuclei: [generic]
reactions: [successive-gamma-cascade, resonance-radiation]
experiments: [polarization-correlation-formalism]
models: [direction-polarization-correlation, statistical-substate-population]
observables: [linear-polarization, angular-correlation, relative-parity, multipole-order]
methods: [polarization-correlation, angular-correlation]
tags: [polarization, angular-correlation, historical-formalism, parity]
---

# Polarization and direction of propagation of successive quanta

## Bibliographic Record

- D. R. Hamilton, *Phys. Rev.* **74**, 782–788 (1948).

## Scope and Reading Depth

- The in-scope six-page article was read end-to-end, including Eqs.(1–15), the 16 dipole/quadrupole combinations, efficiency discussion, parity-group summary and magnetic-field boundary. The following scan page (pp.788 onward) is an unrelated H. C. Corben article and was excluded from this source.

## Formalism

With the first γ defining the quantization axis, Hamilton writes the second-γ polarization intensities along the local `eθ/eφ` axes in terms of `f_|Δm|` (dipole) and `g_|Δm|` (quadrupole) functions (PDF pp.783–784, Eq.1). Electric/magnetic radiation of a fixed multipole order has the same angular distribution but orthogonal polarization. The directional-correlation function is `W(θ)=1+a2 cos²θ+a4 cos⁴θ` (p.784, Eq.6).

For the case in which one detector is polarization insensitive, Eqs.(8a–b) give polarization intensities for each first/second multipole combination. Hamilton then generalizes to finite relative efficiencies `αAB` and `αBC` when either photon may enter either detector (pp.784–786, Eqs.9–15). The sum of the two polarization intensities recovers `W(θ)` independently of detector efficiency, while their ratio carries the parity/multipole information.

## What the Observable Can and Cannot Do

The sixteen dipole/quadrupole sequences collapse into identifiable groups. For same-order electric/magnetic combinations, the polarization-direction correlation can distinguish relative parity groups even when it cannot uniquely identify the multipole order. Mixed dipole–quadrupole cases are efficiency independent only in the electric–magnetic group; same-electric or same-magnetic cases retain efficiency factors (pp.786–787). With partial discrimination of which photon reaches the polarization-sensitive detector, the relative parities of the three levels can be uniquely assigned, but the paper explicitly says that multipole-order information is no better than a directional-correlation experiment alone (p.787).

Magnetic fields preserve the correlation only when parallel to the propagation direction of the unpolarized quantum; transverse fields can wash it out (p.788's final paragraph belongs to the same Hamilton article before the unrelated Corben page marker).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HAM48-1 | Direction–polarization correlations extend directional-correlation formalism to 16 dipole/quadrupole combinations. | method-result | direct | PDF pp.783–787, Eqs.1–15 | true |
| HAM48-2 | Relative parity can be grouped or uniquely assigned with partial first/second-photon discrimination. | parity-assignment-method | direct | PDF pp.786–787 | true |
| HAM48-3 | Detector efficiencies cancel only for specified mixed-multipole groups. | method-boundary | direct | PDF pp.785–787, Eqs.13–15 | true |

## Summary

Hamilton supplies the formal direction–polarization bridge that later Compton/PDCO experiments implement with detector-specific response functions.

## Competing Interpretations and Limitations

- Multipole order can remain grouped even when relative parity is determined.
- The formal results assume the stated substate/phasing conditions and do not substitute for modern calibration or finite-geometry simulation.

## Analytical Reconstruction and Self-Audit

| ID | Audit item | Agent judgment | Locator | Status |
|---|---|---|---|---|
| HAM48-AR-1 | Correlation chain | Direction of first quantum → statistical substates → `W(θ)` plus orthogonal polarization components; the sum remains the directional correlation. | PDF pp.783–787, Eqs.1–15 | self-checking |
| HAM48-AR-2 | Efficiency boundary | Some mixed-multipole groups cancel detector efficiencies, while same-electric/magnetic groups do not; calibration cannot be omitted generically. | PDF pp.785–787, Eqs.13–15 | self-checking |
| HAM48-AR-3 | Assignment scope | Relative parity is more robust than unique multipole order; the result is a formal method, not a modern detector calibration. | PDF p.787 | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[angular-correlation]], [[linear-polarization-asymmetry]] and the historical direction–polarization lineage behind HS-041, HS-072 and HS-092.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `HAM48-P0-1`: Keep the in-scope page boundary explicit; do not ingest the adjacent Corben article as part of Hamilton's nuclear-polarization source.

## Extracted Pages

- Methods: [[angular-correlation]], [[linear-polarization-asymmetry]]。


### Day16 原件与光子角色复核

本session完整读原7页中Hamilton所有正文/脚注：782–787及788上半，视觉核Eq.8–15和788真正文章边界。Crossref核DOI [10.1103/PhysRev.74.782](https://doi.org/10.1103/PhysRev.74.782)、74(7)、1948、782–788，纠正旧页码/六页scope。原PDF含邻文片段的SHA不变；Corben题名之后内容不作本source科学证据。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| HAM48-4 | Hamilton实际延续到p788上半；该页runningheader H.C.Corben不是正文边界。Crossref给782–788，旧782–787/六页说明已修，原件未改。 | source-boundary-correction | original-and-Crossref | p788 above Corben title | true |
| HAM48-5 | 先令firstγ方向为z轴且不测其polarization，作者在其随机相位/成对m假设下将secondγ分成eθ/eφ的线偏振强度；这不是已测firstγ的EM性质或一般coherent密度。 | preparation-and-axis-contract | direct-theory | p783 SecII/Eq1 | true |
| HAM48-6 | W的α2/α4乘cos²θ/cos⁴θ，而polarization式8/12–15含cos(2θ)及sin²(2θ)。两者混读会破坏Iθ+Iφ∝W，原图已核；不是作者勘误。 | exact-transcription-and-sum-guard | original-and-symbolic-failure-control | pp784–786 Eq6/8/12–15 | true |
| HAM48-7 | αBC为first→unpolarized、second→polarization-sensitive的overallcoincidence效率，αAB为反向角色；原11b以这两个正权重线性合并polarization强度。α不是mixing amplitude，也不是完整现代Comptonφ响应。 | response-object-and-photon-roles | direct-theory | p785 Eq11a/11b前定义 | true |
| HAM48-8 | 按原16个pure E1/M1/E2/M2序列符号重放，8组的P不依两角色权重，8组依赖；全部sum归原W、collinear null与角色/权重同步互换恒等。16式是理论分类，不是16个实验。 | source-sequence-replay | actual-symbolic-calculation | pp785–787 Eq12–15/Discussion | true |
| HAM48-9 | 对原14/15的8个dependent组，αAB=αBC时Iθ=Iφ；这类零偏振可以来自未区分role的抵消，不能泛称该跃迁无electric/magnetic信息或用null作绝对Q校准。部分discrimination还需知道哪个权重更大。 | null-and-identifiability-boundary | direct-and-symbolic-limit | pp786–787 Eq14/15后讨论 | true |
| HAM48-10 | 作者p787用α4区分DD/DQ与QQ时须保留nonzero-rank4条件。另作选律推断：allowed pureE2路径2→1→2的中间态J=1只能有rank≤2，相关6j的rank4严格0；所以QQ不普遍保证α4≠0，未据此赋实际核态。 | necessary-condition-and-counterexample | selection-rule-inference | p787 step(i)；本页rank4推断 | true |
| HAM48-11 | 在其pureD/Q、已知directionalcoefficients、适当nondegeneracy及已知效率次序下，部分role discrimination可给relativeparity；multipoleorder仍可成组。未知α2/α4或响应时不能套摘要“unique”。 | source-assignment-conditions | direct-and-explicit-qualification | p787 steps(i)–(iv)/conclusion | true |
| HAM48-12 | 9/10中的CBA为同理论对transition/state顺序的inverse构造，用于交换被分析photon角色；不是观测到同核发生时间倒放或可把emission RME直接标作absorption。本文没有mixedδ的完整operator桥。 | inverse-role-and-phase-boundary | direct-and-limited-inference | p785 Eq9/10/11a | true |
| HAM48-13 | 末段指出本polarization–direction关联在足够强磁场平行未测polarization那条γ时才保留；交换发射先后不改这一陈述，不能据磁场效应识别first/second。 | perturbation-and-role-boundary | direct-theory | p788 final Hamilton paragraph | true |

令t=cos²θ，α2=a、α4=b。去掉同一归一因子后，dipole的electric强度为`dθ=1+a(2t−1)`、`dφ=1+a`；quadrupole为`qθ=1+a+b−2bt(1−t)`、`qφ=1+(a+b)(2t−1)`。它们的sum分别为`2(1+at)`与`2(1+at+bt²)`；磁项交换θ/φ。这些函数既说明原OCR的cos2θ为何不能读成cos²θ，也给负面控制：后者会留下与t相关的sum残差，无法靠overall归一修好。

本次复算只用这些原式的symboliccoefficients和正角色权重；没有选任意counts、alignment数值或新核素实验。αAB/αBC交换须与first/last角色一起交换；两EM全dual会交换eθ/eφ。role weights在原框架可作为两个常数，不等于真实array的energy/φ/position-response已恢复，不能由其取消省略Q/acceptance校准。

对rank4边界，`{2 2 4;1 1 2}=0`来自三角限制。它只证明“纯QQ必有非零α4”不是普遍定理，未把这个允许的spin-path当作已观察能级或新的δ双根；若真实体系有更高rank/coherence、混合多极或额外feeding，应回更一般formalism。

学习决定为`supports`纯序列的role/efficiency合同；`limits`以未分辨null、α4=0或已知能量直接作唯一multipole/parity赋值；`revises`旧页边界。保留旧needs_review，新claims全true，不增加独立实验或课程学分。原1940论文、BR/Fe55的operator定义及actualarrayresponse/Cov仍未恢复。

[符号复算程序](../../system/scripts/day16_hamilton1948_role_audit.py)实际exit0；[冻结输入与16行结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/hamilton1948-role-audit-result.json)。相关[[angular-correlation]]、[[linear-polarization-asymmetry]]、[[compton-polarimetry]]及[[high-spin-angular-polarization-mixing-ratio]]；[[fagg-hanna-1959-polarization-measurements]]转引本理论不算新增实验。
