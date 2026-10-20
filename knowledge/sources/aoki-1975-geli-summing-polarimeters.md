---
type: source
title: "Aoki et al. 1975 - Ge(Li) summing spectrometers and multidirectional polarimeters"
aliases: [Aoki 1975 GeLi summing polarimeters]
created: 2026-09-21
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: method-paper
reading_depth: deep-read
title_original: "Ge(Li) Summing Spectrometers of Special Type"
authors: [T. Aoki, J.-Z. Ruan, A. Yoshimura, Y. Matsuyama]
journal: "Nuclear Instruments and Methods"
year: 1975
volume: 128
pages: "53-60"
pii: "0029-554X(75)90773-9"
canonical_source: "Aoki et al., Nucl. Instr. Meth. 128, 53-60 (1975)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1975_Aoki et al_Ge(Li) summing spectrometers of special type.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1975_Aoki et al_Ge(Li) summing spectrometers of special type.pdf"
raw_sha256: "b0a36fa350a078021212b8cd9a28fecc389baf1ebbbd8a60f79f025b68cc70a7"
nuclei: [generic]
reactions: [22Na-annihilation, 60Co, 137Cs, 152Eu]
experiments: [GeLi-summing-polarimeter, GeLi-GeLi-summing-spectrometer]
models: [Compton-scattering-response]
observables: [linear-polarization, Compton-background, full-energy-efficiency]
methods: [Compton-polarimetry, coincidence-summing]
tags: [GeLi, summing-spectrometer, Compton-polarimetry, polarization]
---

# Ge(Li) summing spectrometers of special type

## Bibliographic Record

- T. Aoki *et al.*, *Nucl. Instr. Meth.* **128**, 53–60 (1975), PII `0029-554X(75)90773-9`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1975_Aoki et al_Ge(Li) summing spectrometers of special type.pdf`。

## Scope and Reading Depth

- PDF pp.53–60 fully read: six-sector and multi-directional single-crystal Ge(Li) polarimeter, annihilation-photon test, two-analyzer variant, Ge(Li)–Ge(Li) backscatter summing spectrometer, spectra/efficiency/background figures and conclusions.
- Not covered: raw electronics traces and later segmented-detector designs.

## Key Results

- A machined planar Ge(Li) crystal contains a central scatterer, four 30° analyzers (`φ=0°,30°,60°,90°`) and a rejector. All azimuths are measured simultaneously without rotating the polarimeter (PDF pp.53–56, Fig.1).
- Majority anticoincidence suppresses rescattered/Compton background by about a factor of four in the summed spectrum. The annihilation-photon test gives reported ratio `2.47±0.30`, compared with the predicted 2.50 after finite-solid-angle effects; the text calls this I0/I90 but Fig.6 has I90>I0, so the ratio direction remains unresolved (PDF pp.55–57, Figs.2,5–6).
- An improved two-analyzer version (`φ=0°` and `90°`) reduces the need for multiple rotations and shortens measurement time by about a factor of four, at the cost of detector-specific efficiency/geometry tradeoffs (PDF pp.56–57, Fig.7).
- A ring-plus-reflector Ge(Li) summing Compton spectrometer reduces continuous background by about a factor of 20; the summed full-energy efficiency above 500 keV is about one-tenth of the reflector singles efficiency (abstract/text; Fig.11 says less than one-tenth above 500 keV), and the practical lower energy threshold is about 300 keV for a flat background (PDF pp.57–60, Figs.8–12).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AO75-1 | Simultaneous four-angle Ge(Li) analyzers can measure polarization azimuths without rotating the detector. | method-result | direct | PDF pp.53–57, Figs.1,5–7 | true |
| AO75-2 | The annihilation test reproduces the finite-solid-angle intensity ratio within uncertainty. | method-validation | direct | PDF pp.56–57, Fig.6 | true |
| AO75-3 | Summing spectrometers trade efficiency for strong Compton-background reduction and a practical energy threshold. | detector-tradeoff | direct | PDF pp.57–60, Figs.9–12 | false |


### Day17原件新增自审

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AO75-D17-1 | 前polarimeter六segments=center+四30°sector+240°rejector，四方位0/30/60/90同时进四分PHA；另一Fig7两0/两90是不同实际布局，不是四方位轮转。 | experimental-setup | direct-and-self-audit | printed53 Sec2.1; printed54 Fig1; printed57 Fig7 | true |
| AO75-D17-2 | five-sector majorityanticoinc在任意两或更多sector同时时veto；Fig2约4倍背景改善是与scatterer单谱的relative比较，不是独立测得absoluteeff/FOM。 | selection-and-denominator | direct-and-self-audit | printed54 Fig2; printed55 Sec2.1 | true |
| AO75-D17-3 | 原Fig3实测未biassectors时scatterer效率随bias异常增，等bias时近定；作者要求allunit samebias，sector角宽比例只在3%countstat范围内。无旋转不能消掉读出/效率系统。 | experimental-counterevidence | direct-and-self-audit | printed55 Fig3 andtext | true |
| AO75-D17-4 | Fig4一个analyzer的summing全峰eff约scatterersingle的1/40；这属于前polarimeter，不是后ringreflector的1/10。 | efficiency-denominator | direct-and-self-audit | printed55 Fig4 | true |
| AO75-D17-5 | 22Na约20µCi置Pb准直器间，NaI scatterer20mm直径×20mm/absorber38×38，另端Ge；NaI summed511门tag，Ge四方位同时记录。不是无条件P=1单beam标定。 | calibration-input-identity | direct-and-self-audit | printed56 Sec2.2 Fig5–6 | true |
| AO75-D17-6 | 正文称ratio I0/I90=2.47±.30、pred2.50，Fig6却I90>I0；保原方向不闭边界，仅大小可转κ幅度=.423631±.049830局部传播，未认证原fitCov。 | source-internal-ratio-boundary | direct-and-self-audit | printed56 Sec2.2 Fig6 | true |
| AO75-D17-7 | prediction包含两套polarimeter finiteangle、引Snyder1948；本test约束共同geometry/tag/analysis响应，未另报独立knownPtag或GeQ。不能把pred2.50直接作任意GeQ或核P校准。 | independence-and-response-boundary | direct-and-self-audit | printed56 Sec2.2; printed60 Ref18 | true |
| AO75-D17-8 | Fig7两0/两90布局作者称相对usualoneanalyzer缩短4倍且测试相似；未给time/error/eff完整ledger，非通用跨装置beamtime merit定律。 | author-result-and-boundary | direct-and-self-audit | printed56 Sec2.3; printed57 Fig7 | true |
| AO75-D17-9 | 后ringreflectorspectrometer是另一装置：scatter150–170°/全azimuth、ring与reflector相距20mm；usualring100–250、reflector约100–2000keV，Fig10/11用160–240，Fig12降70–240。 | experimental-setup-and-gates | direct-and-self-audit | printed57 Fig8; printed58 Fig10; printed59 Fig11–12 | true |
| AO75-D17-10 | 原abstract约1/10、正文E>400约1/10、Fig11caption E>500 less1/10，旧Wiki1/4撤回；original不同能域保留，不从此取得absoluteε。 | Wiki-transcription-correction | direct-and-self-audit | printed53 Abstract; printed58–59 Fig11 | true |
| AO75-D17-11 | Fig9用1332全峰先归一再比较连续背景，约20倍是peaknormalizedshape，不是固定曝光的绝对background下降。不能与不同gate Fig11eff裸拼真实F/time收益。 | normalization-and-merit-boundary | direct-and-self-audit | printed58 Fig9 andtext | true |
| AO75-D17-12 | 原point singleCompton E′=E/[1+(E/511)(1−cosθ)]在1332/150–170给227.146–215.754keV，故正文below200不能作严格界；160–240仍容此point过程。不是actualdetector spectrum/refit或作者实验矛盾。 | task-calculation-and-approximation-boundary | direct-and-self-audit | printed57 Sec3; printed58 Fig10 | true |
| AO75-D17-13 | 降ring门70后122/244峰出现但弱线埋复杂tail，practical下限约300与7keV FWHM@1333为本谱仪条件；不移作前polarimeter阈值/Q或普适低能限。 | experimental-tradeoff-and-transfer-boundary | direct-and-self-audit | printed59 Fig12 andtext | true |

## Summary

Aoki *et al.* demonstrate an early high-resolution, multidirectional Ge(Li) polarimeter and a ring-reflector summing spectrometer. The source supplies a historical detector-response baseline: simultaneous azimuthal coverage is valuable, but anti-coincidence, biasing, window setting, efficiency and energy threshold define the actual sensitivity.

## Competing Interpretations and Limitations

- The 2.47 ratio is an annihilation-photon benchmark, not a universal polarization sensitivity; finite solid angle and analyzer geometry are specific.
- Embedded-detector biasing can create anomalous efficiency; all sectors must be biased consistently.
- Background reduction in the summing spectrometer comes with severe efficiency loss and a threshold/Compton-tail tradeoff.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AO75-AR-1 | Polarimeter chain | Scatterer → azimuth analyzers/rejector → summed peak counts → polarization ratio; simultaneous angles avoid rotation systematic. | PDF Secs.2.1–2.3 | self-checking |
| AO75-AR-2 | Spectrometer chain | Backscatter reflector + ring detector coincidence → flat Compton background → weak-line visibility with efficiency/threshold cost. | PDF Sec.3, Figs.8–12 | self-checking |
| AO75-AR-3 | Transfer condition | Detector bias/window/geometry must be recalibrated before comparing with modern `Q` or figure-of-merit values. | PDF pp.54–60 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[compton-polarimetry]], [[linear-polarization-asymmetry]] and historical detector-response lineage.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `AO75-P0-1`: Preserve simultaneous-angle geometry, bias/window settings and efficiency/background tradeoff; do not treat the annihilation ratio as a universal calibration.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]]。

## Day17原件复核：双光子ratio方向与两套效率分母

先冻aoki1975-before/exercise并声明旧摘要priming，原8页53–60完整text/visual、Fig1–12、20refs与未编号A+Bcos2φ拟式全核；535001bytes/hash `b0a36fa350a078021212b8cd9a28fecc389baf1ebbbd8a60f79f025b68cc70a7`保持。旧AO75-1–3/flags不改，13新待审。旧prose quarter/ratio方向已按原件修/显式限制，不把source内文字–图方向歧义静默裁掉。

[[ppco-joint-response-and-information]]“Aoki1975：实际tagged湮没基准与ratio方向”保存原fourangle/sharedtag、方向冲突、|κ|转换和响应识别边界；[[compton-polarimetry]]保存两装置/eff背景分母。原ratio的误差来自fourpointfit，未得actualcounts/cov，不能逆推jointP或单GeQ。原Snyderfinitegeometry计算在此是作者引用，尚未独立读该Ref18，不算新body。

script `system/scripts/day17_aoki1975_response_audit.py`实际核ratio倒数与singleCompton energy/window逆；不是geant或fullgeometryMC，窗口是否接受point单过程不代真实效率/背景。决定`revises`旧1/4与无方向限定ratio摘要，`limits`直接从doubleanalyzer反推singleQ/跨门FOM。无现代核P/Q/δ/CI或新模式指认。
