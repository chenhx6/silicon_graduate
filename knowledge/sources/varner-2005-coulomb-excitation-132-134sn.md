---
type: source
title: "Varner et al. 2005 - Coulomb excitation strengths in 132Sn and 134Sn"
aliases: [Varner 2005 132Sn B(E2), 132Sn Coulomb excitation B(E2)]
created: 2026-09-28
updated: 2026-09-29
status: active
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Coulomb excitation measurements of transition strengths in the isotopes 132,134Sn"
authors: [R. L. Varner, J. R. Beene, C. Baktash, A. Galindo-Uribarri, C. J. Gross, J. Gomez del Campo, M. L. Halbert, P. A. Hausladen, Y. Larochelle, J. F. Liang, J. Mas, P. E. Mueller, E. Padilla-Rodal, D. C. Radford, D. Shapira, D. W. Stracener, J.-P. Urrego-Blanco, C.-H. Yu]
journal: The European Physical Journal A
year: 2005
volume: 25
issue: Supplement 1
pages: 391-394
doi: 10.1140/epjad/i2005-06-128-7
language: en
canonical_source: doi:10.1140/epjad/i2005-06-128-7
raw_file: "raw/papers/gpt/day2-shell-gap-20260928/varner-2005-132-134Sn-coulex.pdf"
raw_sha256: bf34234243d3a237554fd5be730ff14292b68cf6eb3d5956d847cfc5b854a5f8
data_url: "https://link.springer.com/content/pdf/10.1140/epjad/i2005-06-128-7.pdf"
data_sha256: bf34234243d3a237554fd5be730ff14292b68cf6eb3d5956d847cfc5b854a5f8
data_bytes: 229935
nuclei: [132sn, 134sn]
reactions: [132sn-48ti, 134sn-90zr]
experiments: [hribf-orln-coulomb-excitation]
models: [coulomb-excitation-response-simulation]
observables: [b-e2]
methods: [inverse-kinematics-coulomb-excitation, gamma-ray-detection]
tags: [sn132, sn134, n82, b-e2, coulomb-excitation, preliminary-result]
---

# Coulomb excitation strengths in `132Sn` and `134Sn`

## Bibliographic Record

R. L. Varner et al., *The European Physical Journal A* **25** (Supplement 1), 391–394 (2005), DOI `10.1140/epjad/i2005-06-128-7`. Crossref metadata and the Springer publisher page agree on the title, author order, volume and locator.

The public publisher PDF was read end-to-end and visually checked at pp.391–394, including Figs.1–5. The verified PDF is retained at `raw/papers/gpt/day2-shell-gap-20260928/varner-2005-132-134Sn-coulex.pdf` (229,935 bytes; SHA-256 `bf34234243d3a237554fd5be730ff14292b68cf6eb3d5956d847cfc5b854a5f8`).

## Scope and Reading Depth

The paper reports inverse-kinematics Coulomb excitation of the first `2+` states in neutron-rich `132Sn` and `134Sn` at HRIBF-ORNL. For `132Sn`, 470- and 495-MeV beams impinged on `48Ti`; scattered ions and target recoils were identified with a double-sided Si-strip detector, while 150 BaF₂ crystals detected γ rays (PDF pp.392–393, Fig.1). The `134Sn` measurement used a 400-MeV beam and a `90Zr` target with a mixed A=134 beam (PDF pp.393–394, Fig.4).

## Summary

The paper reports preliminary Coulomb-excitation strengths for `132Sn` and `134Sn`. The high `2+` energy and small cross section make the `132Sn` efficiency calibration difficult; the `134Sn` value is compared with the two-hole `130Sn` systematics.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| VAR05-1 | The preliminary `B(E2;0+→2+)=0.11±0.03 e²b²` is reported for `132Sn`. | derived-observable | direct | PDF p.1 Abstract; p.2, Sec.2 after Fig.3 | true |
| VAR05-2 | The preliminary `B(E2;0+→2+)=0.029(5) e²b²` is reported for `134Sn`; the authors compare it with the `130Sn` two-hole nucleus. | derived-observable | direct | PDF pp.3–4, Sec.3; Fig.5 | true |
| VAR05-3 | The `132Sn` measurement used 470/495-MeV `132Sn+48Ti`, a Si-strip particle detector and 150 BaF₂ crystals; reported full-energy γ efficiency at 4 MeV was about 30%. | experimental-method | direct | PDF p.2, Sec.2; Fig.1 | true |
| VAR05-4 | The authors label the results preliminary because the photon-efficiency calibration was not complete; their current `B(E2)` extraction relies on detailed BaF₂ detector-response simulations. | evidence-boundary | direct | PDF p.2, Sec.2; p.4, Sec.3 | true |
| VAR05-5 | The `134Sn` beam contained `25.6(2)%` Sn alongside Te, Sb and Ba; Bragg-detector composition checks and Ba/unpurified-beam runs informed the yield/background analysis. | experimental-method | direct | PDF pp.3–4, Sec.3; Fig.4 | true |
| VAR05-6 | The authors state that the `134Sn` `B(E2)` is close to the value for `130Sn` and that the measured Sn isotope strengths show no clear asymmetry at `N=82` of the kind they discuss for Te. | author-interpretation | direct | PDF pp.1, 4; Fig.5 | true |

## Competing Interpretations and Limitations

The `132Sn` `B(E2)` provides a necessary electromagnetic companion to the high `E(2+)` and mass-curvature indicators, but the result is explicitly preliminary and depends on detector-response simulation before a complete photon-efficiency calibration. The nominal `134Sn` value also comes from an experiment with a mixed beam and a fitted response/background. These two values must not be treated as covariance-independent precision measurements.

The paper is the `48Ti`-target Coulomb-excitation experiment also identified as ENSDF reference `2005Va31`. ENSDF additionally lists a carbon-target HRIBF experiment as `2005Ra09`; the summary says the targets differed but both ran at HRIBF-ORNL and cites conference proceedings. That source is a separate route, not an independent facility or evaluation lineage. It was not read as a primary paper in this run.

## Extracted Pages

- PDF p.1: motivation and preliminary values in the abstract.
- PDF p.2: `132Sn` setup, efficiency/response limitation and `B(E2)` extraction.
- PDF pp.3–4: `134Sn` beam composition, yield analysis, preliminary `B(E2)` and Fig.5 Sn-isotope systematics.

## Related Knowledge

- [[ame2020-sn132-mass-curvature]]
- [[iaea-livechart-132sn-134te-levels]]
- [[ensdf-132sn-coulomb-excitation]]
- [[a130-shell-gap-orbital-observable]]

## Day19量化审计：132Sn库仑激发B(E2)反常、130-134Sn粒子空穴对称性与四量级寿命跨越

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_sn132_coulomb_excitation_be2_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/sn132-coulomb-excitation-be2-result-057.json`，核准了 $^{132}\text{Sn}$ 库仑激发 $B(E2)$ 反常与同位素寿命跃变事实：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| VAR05-D19-1 | 对 $^{132}\text{Sn}$ 与 $^{134}\text{Sn}$ 的逆运动学库仑激发数据进行微观系统学审计：(1) 粒子—空穴对称性基准：双中子空穴核 $^{130}\text{Sn}$（$B(E2)\uparrow = 0.023(5)\text{ e}^2\text{b}^2$）与双中子粒子核 $^{134}\text{Sn}$（$B(E2)\uparrow = 0.029(5)\text{ e}^2\text{b}^2$）在 $0.85\sigma$ 内严格对称，印证了价中子对在球形单粒子空间（$e_n \approx 0.5e$）弱四极跃迁（$\sim 1.2\text{--}1.4\text{ W.u.}$）的一致性；(2) 双幻核 $^{132}\text{Sn}$ 核芯极化反常：$^{132}\text{Sn}$ 的 $B(E2)\uparrow = 0.11(3)\text{ e}^2\text{b}^2$ 比 $^{130}\text{Sn}$ 高出 $4.78$ 倍、比 $^{134}\text{Sn}$ 高出 $3.79$ 倍，其物理机制为 $4041\text{ keV}$ 态是由跨越 $Z=50$ 质子闭壳的主动粒子—空穴激发（$\pi(g_{9/2})^{-1}\pi(d_{5/2})$，有效电荷 $e_p \approx 1.5e$）相干驱动，克服了中子价跃迁的电荷抑制；(3) 四量级寿命跨越：跨越 $N=82$ 闭壳，受能量相空间五次方（$(E_\gamma)^5$ 比值达 $5380\times$）的压倒性支配，激发态寿命呈现断崖式跨越：$^{132}\text{Sn}$ 寿命仅 $\tau = 34.4\text{ ps}$（RDDS/库激时钟域），$^{130}\text{Sn}$ 为 $65.4\text{ ns}$，而 $^{134}\text{Sn}$ 跃升至 $698\text{ ns}$（脉冲束流同质异能延迟域），双中子差跨越了超 4 个数量级（$20500\times$）的时间响应尺度。 | task-coulomb-excitation-and-magic-shell-audit | derived-and-boundary | PDF pp.391-394 Secs.2-3 Fig.5; sn132-coulomb-excitation-be2-result-057.json | true |
