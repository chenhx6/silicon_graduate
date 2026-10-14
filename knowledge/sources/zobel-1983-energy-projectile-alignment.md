---
type: source
title: "Energy and projectile dependence of nuclear alignment in fusion-evaporation reactions"
aliases: [Zobel 1983 energy projectile alignment, Zobel 1983 nuclear alignment, projectile dependence of nuclear alignment]
created: 2026-07-08
updated: 2026-10-15
status: ai-draft
review_status: human-reviewed
source_type: experiment-method-article
reading_depth: deep-read
title_original: "Energy and Projectile Dependence of Nuclear Alignment in Fusion-Evaporation Reactions"
authors: [V. Zobel, L. Cleemann, J. Eberth, T. Heck, K. Hüsing, W. Neumann, M. Nolte]
journal: Nuclear Instruments and Methods in Physics Research
year: 1983
volume: 207
pages: 389--394
doi: 10.1016/0167-5087(83)90649-X
language: en
canonical_source: doi:10.1016/0167-5087(83)90649-X
citation_key: zobel_1983_Energyprojectile
raw_file: "raw/papers/1983_Zobel et al_Energy and projectile dependence of nuclear alignment in fusion-evaporation reactions.pdf"
raw_sha256: 60B0D4BC561B44D861E16490EFEC7BEBB8FBF1B8B30A7C7D81621A4057208759
nuclei: [67ga]
reactions: ["64Zn(alpha,p gamma)67Ga", "57Fe(12C,pn gamma)67Ga"]
observables: [attenuation-coefficient, angular-distribution-coefficient]
methods: [angular-distribution]
tags: [nuclear-alignment, projectile-dependence, energy-dependence, direct-feeding, cascade-feeding, pado-support]
---

# Zobel et al. (1983): Energy and Projectile Dependence of Nuclear Alignment

## Bibliographic Record

V. Zobel, L. Cleemann, J. Eberth, T. Heck, K. Hüsing, W. Neumann and M. Nolte, *Nuclear Instruments and Methods in Physics Research* **207**, 389--394 (1983), DOI `10.1016/0167-5087(83)90649-X`. The title, authors, year, DOI and file name uniquely match citation key `zobel_1983_Energyprojectile`.

## Scope and Reading Depth

Full text was read from the PDF text layer for pp.389--394. Key checks include Eqs.1--3, experimental methods for `64Zn(α,pγ)67Ga` and `57Fe(12C,pnγ)67Ga`, Table 1, Figs.1--5, and the conclusion. The table text layer is OCR-noisy in places, so this note does not depend on row-by-row table transcription beyond the broad trends and values stated in the authors' prose.

This is an `experiment-ingest + method-ingest + project-ingest` source. It directly supports the P-ADO project by showing that nuclear alignment attenuation coefficients vary with projectile, incident energy and feeding mechanism, and by warning against combining angular-distribution and linear-polarization data taken under different conditions without consistency checks.

## Summary

Zobel et al. measured nuclear-alignment attenuation coefficients in `67Ga` using four pure E2 transitions populated through `64Zn(α,pγ)67Ga` and `57Fe(12C,pnγ)67Ga` over wide incident-energy ranges. For the heavy-ion `12C` reaction they observe only a slight decrease of alignment with incident energy, while the α-induced reaction shows strong energy dependence due to changing direct/cascade feeding. The authors conclude that Gaussian magnetic-substate population assumptions can be useful when direct feeding or cascade feeding dominates, but mixed direct/cascade feeding and cross-condition measurements require caution.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| Z83-1 | 作者将 normalized radiation intensity 写成 `W(θ)=1+A2expP2(cosθ)+A4expP4(cosθ)`，并将 experimental coefficients 分解为 alignment attenuation factor `αk` 与 maximum-alignment coefficient `Akmax(Ii,If,δ)`。 | method-formalism | direct | p.389, Eqs.1--2 | false |
| Z83-2 | 作者说明 angular-distribution coefficients depend not only on spins, multipolarities and mixing ratio, but also on the population distribution of the initial level。 | method-formalism | direct | p.389, Introduction | false |
| Z83-3 | 本文实验用 `64Zn(α,p)67Ga` at `Eα=9--22 MeV` 与 `57Fe(12C,pn)67Ga` at `E12C=32--48 MeV`，并分析 `67Ga` 中四条 well-known pure electric quadrupole transitions。 | observed-fact | direct | pp.390--391, Sec.2, Fig.1 | false |
| Z83-4 | 对 `57Fe+12C` heavy-ion reaction，四条 selected E2 transitions 的 attenuation coefficients 随 incident energy 只有 slight decrease；作者将其可能归因于 higher energy 时 statistical feeding cascades 中 multiplicity 增加。 | observed-fact / author-interpretation | direct | p.390, Fig.2 and paragraph below Fig.1 | false |
| Z83-5 | 对 α-induced reaction，alignment 不再近似线性随能量变化；3031.7 keV level 的 direct feeding 从 `Eα=11.3 MeV` 时超过 80% 变到 `Eα=22 MeV` 时低于 10%，并伴随 alignment 的强下降。 | observed-fact | direct | pp.391--392, Fig.3 and text | false |
| Z83-6 | 作者解释 light projectiles 下 direct feeding and cascade feeding 的相对强度变化可导致 strong descent of nuclear alignment with incident energy；intermediate energy region 是两类 feeding final substate populations 的 superposition。 | author-interpretation | direct | p.393, Discussion | false |
| Z83-7 | Heavy-ion `12C` reaction 的 `α2,α4` pairs 与 Gaussian substate-population hypothesis consistent within errors；α-induced reaction 的 points 可粗分为 high-energy lower-alignment group 与 direct-feeding-dominated upper group。 | observed-fact / author-interpretation | direct | pp.393--394, Figs.4--5 | false |
| Z83-8 | 当两个或多个 feeding components contribute and have different variances, their superposition can deviate from a single Gaussian shape; authors specifically mention direct feeding and γ-ray cascade feeding as such a case。 | method-formalism / author-interpretation | direct | p.393, Discussion | false |
| Z83-9 | 作者在结论中警告：angular distribution and linear polarization measurements combined for model-independent spin assignments and mixing ratios should be recorded at the same energy and with the same target, because alignment and effective beam energy conditions matter。 | method-formalism | direct | p.394, Conclusion | false |
| Z83-10 | 作者总结：heavy-ion-induced reactions 中 Gaussian hypothesis seems useful when `αK` consistency is achieved throughout the level scheme；light projectiles are more complicated due to strong alignment variation with incident energy。 | author-interpretation | direct | p.394, Conclusion | false |
| Z83-11 | Table1的958.0-keV、13/2+→9/2+列，alpha11.3MeV给alpha2=.973±.037、alpha4=.803±.090；alpha22MeV给.674±.036、.215±.087。C32/48MeV对应.793±.032/.595±.093与.756±.038/.413±.110。它们为作者拟合系数，非rawcounts；alpha9MeV该列空白。 | published-fit-result | direct | printed p.392 / PDFp.4，Table1 3032→2074列 | true |
| Z83-12 | Table1 caption将quotederrors限定为Eq1 angular-fit的statisticaluncertainties并采用delta=0；p393明确讨论alpha2/alpha4的statisticaldependence和error ellipse，未列数值Cov。因此本run不能以两个独立误差或矩形认证jointGaussian检验。后句为任务边界。 | method-and-boundary | mixed | printed p.392 Table1 caption；printed p.393，Fig5后右栏第一段 | true |
| Z83-13 | 四条selectedE2的delta在原Sec2注明由Ref4的angular distribution/linear polarization判为within-errors zero；Ref4为Zobel等NPA316,165(1979)，Ref5为Zobel等NIM171,223(1980)。当前scan数据、purity/structure输入和理论/方法引用不能全计成独立实验。 | source-lineage | direct | printed p.390 Sec2；printed p.394 References4/5 | true |
| Z83-14 | Fig3下面六个above-threshold ticks为1.44/3.60/4.26/7.09/9.91/13.67MeV，caption给4MeV阈值幅度及3031.7keV parent。本任务用mass-number CM64/68、lab9/11.3/12/15/18/22MeV扣4与3.0317MeV，最大差.00418MeV；后半是坐标cross-check，不认证作者精确mass/calibration或正反应Q。 | source-axis-and-task-inference | mixed | printed p.392 / PDFp.4，Fig3 lower-axis与caption | true |


## Authors' Interpretation

- Alignment is controlled by projectile, incident energy, angular-momentum transfer and direct-vs-cascade feeding balance.
- Gaussian assumptions are useful in selected regimes, especially when direct feeding or cascade feeding dominates, but should not be adopted by principle when feeding components compete.

## Competing Interpretations and Limitations

- The source gives `67Ga` reaction-specific measurements; it does not define a universal `σ/I` prior for all P-ADO applications.

## Project Relation

For [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]], this source supplies the experimental argument that alignment is reaction-condition dependent. It is the clearest of the three sources for the warning that angular distribution and polarization information used together for `δ` extraction should be taken under consistent beam/projectile/target conditions or explicitly corrected.

## Extracted Pages

- Concepts: [[magnetic-substate-population]], [[spin-alignment]], [[sigma-over-i]]
- Methods: [[angular-distribution]]
- Observables: [[attenuation-coefficient]], [[angular-distribution-coefficient]], [[multipole-mixing-ratio]]
- Projects: [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]

## Personal Notes

User review on 2026-07-08 found no source-level problems; Z83-5, Z83-8 and Z83-9 are accepted as project-relevant evidence for feeding/projectile/energy dependence.

## Day14无学分预习：同parent条件迁移与统计边界

先冻结primed recall，再核Crossref exact DOI/title/207(3)/389–394/1983与raw SHA256；视觉读全六页mainline，覆盖Eq1–3、setup/fit、Fig1–5、Table1、讨论/结论/refs。Table1旋转为upright后视觉转录同一958.0-keV列全部10个nonemptyrows；只按匹配parent/spin/transition选择，未补alpha9MeV空白或静默删该列数据。旧OCR摘要不作为本次数值依据。

### Table1 958.0-keV：视觉核验转录

对应printed392/PDF4的3032→2074列，按beam-energy升序列出该parent全部非空行；alpha9MeV空白。这里的±仅保留原表quotedstatisticalerrors。

| projectile / lab E(MeV) | alpha2±error | alpha4±error |
| --- | --- | --- |
| alpha / 11.3 | .973±.037 | .803±.090 |
| alpha / 12 | .910±.037 | .810±.090 |
| alpha / 15 | .681±.036 | .419±.087 |
| alpha / 18 | .728±.036 | .263±.087 |
| alpha / 22 | .674±.036 | .215±.087 |
| 12C / 32 | .793±.032 | .595±.093 |
| 12C / 36 | .821±.016 | .569±.051 |
| 12C / 40 | .820±.020 | .569±.078 |
| 12C / 44 | .754±.033 | .573±.088 |
| 12C / 48 | .756±.038 | .413±.110 |

原frontmatter人审状态及Z83-1–10的false标记是2026-07-08继承记录，保持原范围；新Z83-11–14和本run模型/图为Codex自审，needs_review:true，不产生新人审事件。

实验输入层：Table1的coefficients是corrected intensity的LS fit outputs，quotederrors为statistical；GF的Gaussian+tail+step是谱线profile模型，与nuclear-substate Gaussian不是同一个假设。作者p393对quantitative feeding分析明确保留误差较大限制，并强调alpha pair相关性；数值Cov/raw spectra/完整response没有在本材料提供。

解释层：heavy-ion组Gaussian一致与轻粒子direct/cascade limiting groups一致是作者的有条件判断；Fig5中间能区feeding-superposition线与p394同energy/target警告限制固定alignment迁移，不等于全部Gaussian无效。Ref9 Ionescu的167Tm是比较引用；Ref4 purity/structure与Ref5 method依赖不认证当前所有点独立采集。

任务计算层：[[angular-distribution]]“Zobel1983：同parent反应条件与Gaussian诊断”保存原表10行、明确的独立stat差量、任务Gaussian标准差s、CG/Stevens独立核验、unknownCov敏感性、chosen mixture及Fig3坐标cross-check。38检查与图QA通过；不把alpha2-only s/J当原文实测sigma/I、不给Gaussian排除概率，不拟合用户P-ADO或193Bi。Day15仍只是partial15预习。
