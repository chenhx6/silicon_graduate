---
type: source
title: "Demonstration of Nuclear Gamma-Ray Polarimetry Based on a Multi-Layer CdTe Compton Camera"
aliases: [Go 2024 CdTe Compton camera polarimetry, multi-layer CdTe nuclear gamma-ray polarimeter]
created: 2026-07-13
updated: 2026-07-13
status: active
review_status: human-reviewed
source_type: detector-method-experiment-article
reading_depth: deep-read
title_original: "Demonstration of Nuclear Gamma-Ray Polarimetry Based on a Multi-Layer CdTe Compton Camera"
authors: ["S. Go", "Y. Tsuzuki", "H. Yoneda", "Y. Ichikawa", "T. Ikeda", "et al."]
journal: Scientific Reports
year: 2024
volume: 14
number: 1
pages: 2573
doi: 10.1038/s41598-024-52692-2
language: en
canonical_source: doi:10.1038/s41598-024-52692-2
citation_key: go_2024_Demonstrationnuclear
raw_file: "raw/papers/2024_Go et al_Demonstration of nuclear gamma-ray polarimetry based on a multi-layer CdTe Compton camera.pdf"
raw_sha256: CB16B9B16E4932385CE027BF4AF56CAC72025FDD89F3ADC90384A9E48C0C78EA
nuclei: [56fe]
reactions: ["56Fe(p,p'gamma)"]
observables: [gamma-ray-linear-polarization, experimental-asymmetry, polarization-sensitivity, modulation-factor, detection-efficiency]
methods: [compton-polarimetry, modulation-curve, maximum-likelihood, detector-response-simulation]
tags: [cdte, compton-camera, nuclear-gamma-ray-polarimetry, klein-nishina, geant4]
---

# Go et al. (2024): Multi-Layer CdTe Compton-Camera Polarimetry

## Bibliographic Record

S. Go et al., *Scientific Reports* **14**, 2573 (2024), DOI `10.1038/s41598-024-52692-2`, citation key `go_2024_Demonstrationnuclear`.

The title, DOI, year and local PDF match the BibTeX record uniquely. The full nine-page article was read, including the abstract, Introduction, detector and reaction methods, Figs.2-6, Eqs.(1)-(7), Table 1 and the future-performance discussion.

## Scope and Reading Depth

This is a `detector-method-ingest + experiment-ingest` source. It demonstrates a multi-layer position-sensitive CdTe Compton camera with a known polarized 847-keV line. The paper characterizes one detector configuration and one calibration reaction; it is not a universal replacement for Clover or tracking-array polarimetry.

## Summary

The authors use a twenty-layer CdTe camera to record two-hit Compton events from the 847-keV `2+ -> 0+` transition in `56Fe`, produced by the `56Fe(p,p'gamma)` reaction. Measured azimuthal distributions are compared with Geant4/ComptonSoft detector simulations. Normalized detector-response and background terms are fitted with a Poisson maximum-likelihood procedure to infer the polarization and to obtain a modulation curve. The paper reports a detector sensitivity compatible with a finite, explicitly quantified efficiency, while emphasizing the sensitivity-efficiency trade-off.

## Experimental and Detector Setup

- A natural-iron foil of thickness 10 micrometers was irradiated with a 3.0-MeV proton beam at the RIKEN Pelletron. The CdTe camera was at approximately 90 degrees to the beam, 18.0 cm from the target; a segmented Ge CNS-GRAPE detector monitored the opposite direction (p.3, Fig.3 and methods text).
- The camera used twenty stacked CdTe layers, 8 x 8 pixels per sensor, 3.2-mm position resolution, 0.75-mm layer thickness and 15.0-mm total active thickness. Cooling and high-voltage operation were part of the detector characterization (p.3, Fig.2).
- The reference transition is the 847-keV first `2+ -> 0+` line in `56Fe`; the paper uses its known near-50% polarization as the calibration input. The measured peak resolution was 1.3% FWHM (p.3-4, Fig.4).

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| G24-1 | The paper presents a multi-layer position-sensitive CdTe Compton camera as a possible nuclear gamma-ray polarimeter, motivated by the limited efficiency of earlier linear-polarization systems. | author-interpretation | direct | Abstract; p.2, Introduction | false |
| G24-2 | The Klein-Nishina differential cross section (Eq.1) and its analyzing power `A(theta,Egamma)` (Eq.2) provide the photon-polarization dependence of the Compton-scattering plane. | method/formalism | direct | p.2, Eqs.(1)-(2) | false |
| G24-3 | The Introduction places the CdTe camera alongside Clover Ge and tracking arrays: Clover offers a compact Compton-polarimetry implementation, while GRETINA/AGATA provide fine interaction-position information; the CdTe design targets high position sensitivity and sub-MeV efficiency. | method-boundary | direct | p.2, Introduction | false |
| G24-4 | The measured detector is a twenty-layer, pixelated CdTe camera with 3.2-mm uniform position resolution and 15.0-mm total sensor thickness. | detector-characterization | direct | p.3, Fig.2 and detector-method subsection | false |
| G24-5 | The 3.0-MeV `56Fe(p,p'gamma)` reaction and detector geometry were chosen to produce a strongly polarized 847-keV line near 90 degrees; the paper uses CNS-GRAPE as an opposite-side intensity/asymmetry monitor. | observed-fact | direct | p.3, Fig.3 and production subsection | false |
| G24-6 | Two-hit events containing the 847-keV full-energy peak were selected for the polarimetry analysis; the paper reports relative full-energy-peak efficiencies of 63.8(3)% for two-hit and 7.6(1)% for three-hit events relative to the single-hit reference. | detector-characterization | direct | p.4, Fig.4 and paragraph below it | false |
| G24-7 | For each division of the azimuthal histogram, detector responses are normalized using measured energy spectra and a simulated mixture of unpolarized, 100%-polarized and background components: `e^(model)(P)=nu_j[(1-P)e(0)+P e(100)]+e(bg)`, where `j` indexes the division (Eq.3). | method/formalism | direct | pp.4-5, Eqs.(3)-(5) | false |
| G24-8 | ComptonSoft, using the Geant4 framework, supplies the detector-response and physics simulations; the degree of polarization is iterated with a Poisson maximum-likelihood function until the likelihood is maximized. | simulation-result/method | direct | p.5, azimuthal-distribution subsection, Eqs.(4)-(5) | false |
| G24-9 | Restricting the polar scattering angle to `40 degrees <= theta <= 120 degrees` increased polarization sensitivity at the cost of detection efficiency; the paper treats this as an event-selection optimization for this setup. | detector-characterization | direct | p.5, text below Eq.(5); Fig.5 caption | false |
| G24-10 | The measured azimuthal distribution gives an inferred degree of polarization `P=0.57(4)` for the 847-keV line, with the positive sign convention identified with electric character. | observed-fact/inferred-observable | direct | p.5, Fig.5 discussion | false |
| G24-11 | The modulation curve is defined as the measured-minus-background azimuthal distribution divided by the unpolarized simulation (Eq.6), and is fitted by `A(1+Q' cos(2(phi-phi0)))`; the paper reports `A=1.004(6)`, `Q'=0.203(8)` and `phi0=0.06(3)` (Fig.6). | detector-characterization | direct | pp.5-6, Eq.(6), Fig.6 | false |
| G24-12 | Dividing the modulation factor by the inferred polarization gives `Q=0.35(4)` at 847 keV. The paper explicitly distinguishes this sensitivity from detection efficiency and defines a figure of merit `F=epsilon Q^2`. | method/formalism/detector-characterization | direct | p.6, Eq.(7) and comparison text | false |
| G24-13 | A narrower `60 degrees <= theta <= 100 degrees` selection raises the quoted sensitivity to `Q=0.40(4)` but loses about 65% of the detection efficiency; the adopted setup estimates `epsilon` near `1.9 x 10^-5` and `F` near `2.4 x 10^-6`. | detector-characterization | direct | p.6, figure-of-merit discussion | false |
| G24-14 | Table 1 compares the CdTe result with Clover, GRETINA, Gammasphere, POLALI and other polarimeters; the comparison is configuration- and energy-specific and does not establish a universal ranking of detector technologies. | author-interpretation/method-boundary | direct | pp.6-7, Table 1 | false |
| G24-15 | The future discussion proposes side sensors, closer target placement and finer CdTe position resolution to improve coverage and efficiency; it presents these as development directions, not as already demonstrated nuclear-spectroscopy standards. | future-proposal | direct | p.7, Possible future gamma-ray polarimetry | false |

## Evidence Boundaries

- The measured modulation is a detector-level azimuthal response. The inferred `P` depends on the simulated response, normalization, background treatment, event selection and the known calibration reaction.
- A large `Q` is not the same as a large absolute efficiency. The paper's `F=epsilon Q^2` and event-selection examples make that trade-off explicit.
- The CdTe demonstration should be compared with Clover and GRETINA through the reported energy, geometry, event cuts and figure of merit. It should not be written as a mature universal replacement for in-beam HPGe arrays.
- Geant4/ComptonSoft outputs characterize detector response. They are not nuclear-structure model predictions.

## Competing Interpretations and Limitations

- The paper's inferred polarization is conditional on the simulated response, normalization, background model and event-selection cuts.
- A high sensitivity in one angular window can reduce efficiency; the reported figure of merit is setup-specific.
- The CdTe result is a detector demonstration and comparison point, not evidence that CdTe has replaced Clover or tracking arrays for all in-beam work.

## Extracted Pages

- Pages 1-2: motivation, Klein-Nishina cross section and analyzing power.
- Page 3: twenty-layer CdTe camera and `56Fe(p,p'gamma)` geometry.
- Pages 4-5: energy spectra, two-hit event selection, response normalization and likelihood polarization fit.
- Pages 5-7: modulation curve, sensitivity, efficiency/figure of merit and detector comparison.

## Related Wiki Pages

- Concepts: [[gamma-ray-linear-polarization]]; the Klein-Nishina formula is included in this source's method formalism.
- Methods: [[compton-polarimetry]], [[modulation-curve]], [[linear-polarization-asymmetry]], [[tracking-array]]
- Observables: [[experimental-asymmetry]], [[polarization-sensitivity]], [[detection-efficiency]]
- Calibration nucleus: `56Fe` (no separate structure page created in this method-only ingest).
- Project: [[gamma-ray-linear-polarization-in-nuclear-spectroscopy]]

## Human Review Triage

P0 review completed: G24-2 (Eqs.1-2), G24-7/G24-8 (normalization, background and likelihood equations), G24-10 (inferred `P=0.57(4)` and sign convention), and G24-11/G24-12 (modulation-factor and `Q` definitions) were checked as the core links between detector modulation and physical polarization inference.

The user-reviewed source has no remaining claim-level `needs_review: true` items. The detector numbers, Eq.3 division-index notation, likelihood chain, modulation/sensitivity values and Table 1 comparison boundary were checked against the cited pages.

## Project Relation

This source is the detector-demonstration branch of [[gamma-ray-linear-polarization-in-nuclear-spectroscopy]]. It supplies a concrete CdTe response, normalization and likelihood chain that can be compared with Jones's calibration formalism and Longfellow's GRETINA in-beam treatment without conflating detector simulation with nuclear-structure evidence.


## 2026-10-19 Codex追加：归一、似然与跨探测器Q定义

本session重新完整读九页文字主线/References，视觉核Figs.1–6、Table1及Eqs.(1)–(7)；另取当前publisher HTML及独立Table1页面HTTP200。原localPDF与全旧human-reviewed前缀逐字节保留；以下为新self-audit，均needs_review，不继承旧人审。

| ID | 新核查陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| G24-16 | 847已知约50%偏振是选择反应的动机，作者的P=.57(.04)由本实验模板似然推断，并非把.50固定后另独立拟Q。CNS-GRAPE在对侧同beam同步监测强度/不对称，本文未给可组合的独立P/联合Cov。 | calibration-input-and-dependence | direct-mainline | PDF3 production；PDF5 Pparagraph；Fig3 | true |
| G24-17 | νj来自各division的能谱Eq3拟合；Eq4明确innerlikelihood固定νj并迭代P，Fig5说明归一先于40–120°选择。不能把它简化成每φbin任意free scale，也不能在缺原energy–φ/eventledger/νCov时认证jointprofile或原CI。 | normalization-and-likelihood-readiness | direct | PDF4Eq3；PDF5Eq4–5/Fig5caption | true |
| G24-18 | 作者说P=.57(.04)误差主要为不同eventselection的systematic，rotation系统项由模拟估为较小；它不是已知纯Poissonσ。0.1%能量校准、坏pixel、背景live-time/实际threshold与位置/选择响应仍需匹配。 | reported-error-layer | direct-author-assessment | PDF3energyparagraph；PDF4noisepixels；PDF5Puncertainty | true |
| G24-19 | 正文Q′=.203(.009)，Fig6caption=.203(.008)，当前HTML也保留两值。Q=Q′/P的共同count/selection/模板Cov未给；不能用独立误差代数把报告Q=.35(.04)重新定义为新校准。 | printing-and-covariance-boundary | direct-PDF-and-current-HTML | PDF5Qprimeparagraph；PDF6Fig6caption；currentHTMLsameanchors | true |
| G24-20 | Table1 Clover847标b、GRETINA847标c，但b注给Morse参数/c注给Kojima参数；p6正文对应相反。Eq7复算Morse参数得.199759、Kojima得.228589，支持正文/数值归属。原PDF及当前Table1均保留错配，非本run正式corrigendum。 | isolated-footnote-crosswalk | visual-PDF-current-table-and-arithmetic | PDF6Eq7/text；PDF7Table1b/c；publisherTable1 | true |
| G24-21 | εcoin=3e−5、选后ε≈1.9e−5为ComptonSoft估计，含badpixel，beamduct/refrigerator未计。40–120°Q提高1.5/eff留.64给条件F增1.44；若窄门所说65% loss相对adopted门，则F比≈.457。baseline/完整systematics未给，不据此保证真实beamtime最优。 | response-and-cut-design-boundary | direct-and-conditional-arithmetic | PDF6FOMparagraph；Eq7附近cuttext | true |
| G24-22 | Go定义Q′=Q_G P，而Morse2022已读UNC author-preprint定义A0=Q_M Pbar/2。只有sameharmonic/相同P与response对象时Q_G=Q_M/2、同ε时F_G=F_M/4。Table1裸Q/不同能区、门、布居与模拟曲线不能直接当统一技术排名；本run不重标实际实验Q。 | normalization-transfer-boundary | two-primary-definitions-and-algebra | G24PDF5Eq6/拟合式；M22UNCpreprint PDF3Eq7–9 | true |
| G24-23 | 另声明singlehist/positive signal-only Poisson模型μi=νsi(P)时，νprofile=D/S，shape likelihood等价于条件multinomial；Fisher有效信息为ν[Σs′²/s−(Σs′)²/S]。纯scale变化时信息0，S′=0时profile/fixedscale信息相等；不是对原Eq3–5实际输入的拟合。 | conditional-statistical-derivation | symbolic-identity-and-failure-controls | 本追加profile公式；原PDF4–5Eq3–5为触发 | true |
| G24-24 | Dataavailability为向correspondingauthor reasonable request；当前publisher页面未提供本实验count/response/partition/code的明确下载入口。未联系作者、未造hist/templates；experimentalL4refit仍notready，公开toolkit名不等于exactproducer。 | data-and-producer-readiness | direct-statement-and-bounded-link-audit | PDF7Dataavailability；currentpublisherHTML；PDF4ComptonSoft/Ref48 | true |
| G24-25 | p6正文称GRETA、Table1的847行却标GRETINA；上游Morse Eq13实际拟合四个GRETA模拟能量并沿用position tuning，不是GRETINA847的独立实测Q。当前算术input沿用被核原表label，producer/model身份另列；不因curve数值重放而认证实际response。 | curve-provenance-and-version-boundary | upstream-primary-and-source-crosswalk | G24PDF6Eq7text/PDF7Table1；M22PDF10Sec4.4/PDF11Eq13 | true |

### 归一式没有提供完整联合误差

原文定义i为φbin、j为division，νj从能谱中获得；内层Poisson mean为νj[(1−P)d0ij+P d100ij]+dbgij。background取实测并按live time缩放，noisypixel在data/simulation两边处理。没有原division划分、能量–φ event交叉表、finiteMC模板与backgroundCov时，既不能重放P=.57，也不能断言所有ν是不受约束的free parameters。

作为可复用推导，单组signal-only `ni~Pois[νsi(P)]`、`si>0`、`D=Σni>0`、`S=Σsi` 时：

`νhat=D/S`，`ℓprofile=Σni ln(si/S)+D lnD−D+constant`。

`Ieff=ν[Σ(s′i)²/si−(Σs′i)²/S]=ν/S Σi<j si sj(s′i/si−s′j/sj)²`。

该非负平方和表明shape相同、仅总率随P改变时P与scale不可辨；S′=0时profile不自动损失相对于固定scale的P信息。不是所有data-driven归一都造成完全失辨识。已用符号表达式验证profile/Schur、pure-scale及zero-sumshape极限，没有生成替代实验计数。

若能谱与φ谱是同一批Poisson二维cells的marginals，则`Cov(Ee,Dφ)=μeφ`；将两个marginal likelihood直接相乘通常需要额外条件。原文并未把二者独立乘入一个联合式，本run也不据此指认作者doublecount；需要原producer/事件账本来决定实际统计模型。含background、有限MC和选择系统项时，以上纯信号式须扩展。

### 报告误差、印刷差与Q定义

舍入central Q′/P=.35614，保留原报.35(.04)。固定两marginal误差作一阶敏感度，text .009给独立σQ=.02956、任意Cov范围.00920–.04078；caption .008给.02866和.01096–.03903。它们不是原systematic decomposition或CI，也不用于宣布报告误差矛盾。两个observable共享data与selection，原Cov必须保持缺口。

当前p6正文的Morse `a=3.25e−4/keV,b=.131`与Kojima `a=1.470e−4/keV,b=.3404`分别给847的.199759/.228589；Table1行值与正文相符，b/c脚注映射则相反。只隔离这个具体版本问题，不更改原file或扩大成实验错误。

同字母Q的另一边界来自[[morse-2022-gretina-polarization-sensitivity]] M22-5：Wc=b(1−A0cos2ξ)、A0=Q_M Pbar/2，而这里modulation factor Q′=Q_G P。旋转/EM符号可以改变相位但不消除幅度因子；only在同harmonic/P合同下才有Q_G=Q_M/2。真实θ平均、event selection、效率分母及arrayresponse不同仍要分别核，不能仅做factor2换算就认证detector迁移。

### 效率、F与可重放输入

`.64×1.5²=1.44`复现40–120°选择的名义F收益；按ε≈1.9e−5/Q=.35得F≈2.3275e−6，与作者约2.4e−6的粗摘要分开保留。60–100°的effloss参照和实际系统项需要逐cut ledger，不用更高Q自动决定更优F。近距离/side sensor/250µm等仍是发展建议。

原Dataavailability不等于数据已公开。下一实际可复算P需要完整dexp/dbg/d0/d100、ej各分区、νfit/误差及eventcuts/finiteMC/rotationgeometry；当前不从曲线图像补伪rawcounts，不把reportedP与同data的modulationfit当两个独立实验。

`supports`独立56Fe/CdTe实验对P/response分层的价值；`limits`exactfit、无条件技术排名与跨normalization裸迁Q；新条目保持needs_review。相关[脚本](../../system/scripts/day16_go2024_calibration_audit.py)/[结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/go2024-calibration-audit-result.json)为印刷summary算术及解析设计，不重放原experimentalproducer。[[compton-polarimetry]]、[[modulation-curve]]保存使用合同。

当前原表把Morse曲线标成GRETINA847，而其上游Eq13明确是GRETA四点模拟/position tuning；这与b/c脚注错配是两个分别保留的对象边界。回放输入的`Morse2022_GRETINA`键只镜像原表label，不据此升级为GRETINA独立标定。

Morse上游的实际原件版本是UNC author-preprint（M22-1），其Eq8/13已核，VoR正文尚未取得。以上半因子与GRETAcurve crosswalk限于这些已读式/版本，不宣称VoR仍逐字同式，也不据此断言Go实际producer使用了错误归一。


### Ref37原方法读后的适用域

| ID | 新核查陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| G24-26 | Ref37实际已读arXivv1：16个归一division是first-hit xy空间区，不是16个φbins；其75keV的ES=minenergy规则借助2E<mec²。该域不能裸迁本847keV；也不能因sharedtoolkit自动认定本experiment采用相同16区或低能排序。 | upstream-method-and-transfer-domain | direct-upstream-plus-kinematic-check | Ref37/T21PDF5Eq3/PDF6Eq4；本PDF4–5Eq3–5 | true |

[[tsuzuki-2021-sicdte-template-polarimetry]] T21-1–13补齐独立Ba null、Kr likelihood/modulation共享data、ν空间区/threshold/ARM和arXiv/VoR边界。原子近满P不能填成本核γreference；Goactualproducer/分区/energy ordering/response仍需实际版本，不据T21演示判Go实际错序。此新追加needs_review，原全部humanprefix保留。
