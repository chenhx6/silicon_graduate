---
type: source
title: "Bass et al. 1972 - Symmetrical two-crystal Compton polarimeter for gamma rays"
aliases: [Bass 1972 two-crystal polarimeter]
created: 2026-09-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: method-paper
reading_depth: deep-read
title_original: "Symmetrical two-crystal Compton polarimeter for gamma rays"
authors: [R. Bass, S. Brinkmann, C. von Charzewski, H. Hanle]
journal: "Nuclear Instruments and Methods"
year: 1972
volume: 104
pages: "33-43"
pii: "0029-554X(72)90293-5"
canonical_source: "Bass et al., Nucl. Instr. Methods 104, 33-43 (1972)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1972_Bass et al_Symmetrical two-crystal compton polarimeter for gamma rays.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1972_Bass et al_Symmetrical two-crystal compton polarimeter for gamma rays.pdf"
raw_sha256: "4f6bfed154b9c2dbe60bae672a2a998f3777b31879746ffeff5bd63040d3994d"
nuclei: [40Ar, 24Mg, 60Co]
reactions: [24Mg(p,p'γ), 56Fe(p,p'γ)]
experiments: [frankfurt-two-crystal-polarimeter]
models: [klein-nishina-scattering]
observables: [polarization-sensitivity, coincidence-efficiency, peak-to-compton]
methods: [compton-polarimetry]
tags: [Compton-polarimeter, two-crystal, detector-response, polarization]
---

# Symmetrical two-crystal Compton polarimeter for gamma rays

## Bibliographic Record

- R. Bass *et al.*, *Nuclear Instruments and Methods* **104**, 33–43 (1972), PII `0029-554X(72)90293-5`。
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1972_Bass et al_Symmetrical two-crystal compton polarimeter for gamma rays.pdf`。
- 11-page method paper; title/author/PII and NaI/Ge(Li) test geometry checked.

## Scope and Reading Depth

- PDF pp.33–43 fully read: symmetric two-crystal principle, threshold/angle acceptance, polarized-source production, NaI and Ge(Li) construction, Tables 1–3, Figs.1–7, coincidence/anticoincidence response and conclusions.
- Not covered: raw spectra, modern Monte Carlo response and later detector implementations.

## Method Logic and Key Evidence

- 两massivecrystal接触/转动，原p33–34明确`N(φ)=nco/(nco+nanti)`为fullpeak的coincidencefraction，非旧Wiki含混co/anti比；再Q=(N0−N90)/(N0+N90)=RP。R是本装置的分析能力，Nbar另有分母，见BA72-D17-1/2。
- Equal threshold `E_th` selects an effective Compton-angle range; lower thresholds raise efficiency but change `R`. The paper maps threshold versus accepted scattering angle (Fig.2).
- NaI tests cover 0.2–4.4 MeV; Ge(Li) tests use 28-cm³ coaxial crystals and thresholds 50–1500 keV. Coincidence operation improves peak-to-Compton and suppresses photoelectric/escape backgrounds.
- Detector-specific tables report efficiency ratio `N` and polarization sensitivity `R`; values vary strongly with energy and threshold (Tables 2–3), so they are not universal constants.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BA72-1 | Symmetric two-crystal coincidence/anticoincidence asymmetry measures incident linear polarization with efficiency `R`. | method-result | direct | PDF pp.33–35, Eqs./Figs.1–2 | false |
| BA72-2 | Threshold controls accepted Compton angles and the sensitivity–efficiency trade-off. | detector-response | direct | PDF pp.34–36, Fig.2, Tables 2–3 | false |
| BA72-3 | NaI/Ge(Li) tests achieve usable sensitivity over 0.2–4.4 MeV and improve peak-to-Compton compared with anticoincidence/singles. | method-validation | direct | PDF pp.35–43, Tables 1–3, Figs.6–7 | true |

## Summary

Bass *et al.* establish a compact symmetric two-crystal Compton polarimeter whose threshold-dependent coincidence asymmetry trades efficiency against polarization sensitivity and improves spectral background conditions.

## Competing Interpretations and Limitations

`R` depends on crystal geometry, threshold, energy, source distance and angular acceptance; alignment, gain matching, accidental coincidences and multiple scattering require calibration. Historical values should not be transferred to modern arrays without response simulation.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| BA72-AR-1 | Formula chain | Compton coincidence/anticoincidence counts → asymmetry `Q` → calibrated `R` → physical polarization `P`. | PDF pp.33–35 | self-checking |
| BA72-AR-2 | Transfer condition | Use only with matched threshold/geometry and detector-specific `R(E,E_th)`. | PDF Tables 2–3 | self-checking |
| BA72-AR-3 | Failure condition | Multiple scattering, background/gain mismatch and threshold-dependent angle acceptance can bias `R`. | PDF pp.34–43 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` detector-response lineage for [[compton-polarimetry]] and [[linear-polarization-asymmetry]].
- Persistence: add source to Compton method map; preserve `R`/efficiency separation.
- Review state: Codex self-audited; not `human-reviewed`.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[compton-polarimetry]] | Early symmetric two-crystal geometry and threshold-dependent `R`. |
| supports | [[linear-polarization-asymmetry]] | Detector-level asymmetry and response calibration. |

## Human Review Triage

### P0

- `BA72-P0-1`: quoted `R` values are detector/threshold-specific and cannot be used as modern universal calibration.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]]。


## Day17原件自审：coincidence分数与参考P误差

本session先冻primed回忆，新读完整11页/10图/3表/未编号公式及6refs text+visual，hash4f6bfed154b9c2dbe60bae672a2a998f3777b31879746ffeff5bd63040d3994d/820544bytes保持。旧BA72-1–3行/false false trueflags及reviewunreviewed保持，新13条待审，不称human-reviewed。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BA72-D17-1 | 原Nφ=nco/(nco+nanti)，是coincidence占同时fullenergysumpeak的分数，再Q=(N0−N90)/(N0+N90)=RP；P明确unpol0/fullpol±1。后表prose“co/anti”简称不能把总和分母改为nanti，旧Wiki措辞已纠。 | observable-definition correction | direct | pp.33–34 N/Q definitions | true |
| BA72-D17-2 | 两Ge整体转四个90°位置，nominal0/180与90/270各平均以降misalignment；actualsimultaneousco/anti避免另monitor，不等所有曝光/背景/geometrysystematics自动抵消。原sourceconfiguration/threshold定义R与Nbar，不迁SG98/CloverQ。 | rotation and normalization contract | direct | pp.34/38 Sec4 | true |
| BA72-D17-3 | 校准Table1 P来自sameactualtarget/resonance/AD及pureE2point式；F198/Ag414–423由Coulombexcitation，Fe/Mg/Si/C由p,p'。MgEp2.01/P.87、C P.80不同B73同γP.99等，sameEg不共享population标尺。 | actual-knownP identity | direct | pp.35–36 Table1 | true |
| BA72-D17-4 | DoubleCompton校准用Co1333经70±10°NaI散射成450–500keV、triplesum窗/三重coinc及samegeometryMg1368检查，reportedPmeas .38(.03)/calc.40(.03)。作者将1.33/1.37差视小的假设保，非无模型/无共同标尺的独立Ptrue测量。 | companion-reference and shared-assumption | direct | pp.35–36 Sec2/Table1 | true |
| BA72-D17-5 | Tables2/3的Rerror明确countstatonly，不含Table1Perror。新独立P条件下Ge198R.61/P.21(.06)的P-onlysigmaR=.1743，另有印statsigma.08；不拼成原fullCI或称作者漏报（source已声明排它）。 | actual-uncertainty layer | direct plus conditional propagation | p.37 after Table2; p.38 Table3 | true |
| BA72-D17-6 | 新Table3全部20行actualGe Nbar/R/%/threshold核，p41source相对merit为R sqrt(Nbar)，其平方才同NbarR²，不是absoluteεQ²。central各energy离散阈值最大为19850/42050/847300/1368200/1780400/4430200keV，只有限采样central，不全域最佳门或显著ranking。 | actual-table exercise and merit convention | derived | pp.38/41 Table3 and relative-merit discussion | true |
| BA72-D17-7 | 原R随门有非单调及N降，作者明言点数/精度不足准确定optimum、>500keV浅max约200–300；对不含<800γ用200为折衷，低能200γ约只56keV电子转移。不能把“门越高越好”或200普适硬切。 | threshold counterevidence | direct | pp.41–42 Fig9/Sec5 | true |
| BA72-D17-8 | 新按原fraction给fixedP q=RP、f±=fbar(1±q)代数核。若误换odds C/anti，则Qodds=q/(1−fbar+fbarq²)，与原linearR并非同响应；只是定义反例，不认原实验用了错分母或恢复原counts。 | normalization-counterexample | derived | p.34 definition; p.38 Table3 | true |
| BA72-D17-9 | 条件独立primitivePoisson C/A下Var[C/(C+A)]=f(1−f)/(C+A)，而Cov(C,C+A)=VarC不能省；原backgroundfit/rotation/exposure/Pref共享Σ未得，不拿新代数当其实际fullerror。 | covariance and statistical scope | derived from observable | pp.33–34 definitions | true |
| BA72-D17-10 | equalenergythreshold只在singleCompton近似给Fig2角域；multiple scatter/largeNaIgeometry会破能角一一映射，paircreation511/Eγ−511峰不敏感P。原sumcoinc电子模式可一次测threshold依赖但要求cleanmonochromatic、不代表每threshold独立事件。 | event-selection and independence | direct | pp.34–37 Fig2/Sec3 | true |
| BA72-D17-11 | 原Ge每crystal28cm³/3.2keVresolution、5%相对7.5×7.5NaI@25cm；sum4.5keV、Co1.33peak/Compton从anti12到co18。relativeeff/peakbackgrounddefinition不同absoluteNbar，不能比裸效率或称所有谱固定提升。 | actual-performance denominator | direct | pp.37–40 Table3/Figs4–7 | true |
| BA72-D17-12 | p42数字eventbysum/gainstabilization/511veto及fourcrystalQprime/Qdoubleprime模式均为proposedimprovements，无本文实测该producer/器件；原两crystaldata不认证现代四foldselection/response。 | proposal-versus-data | direct | p.42 Sec6/Fig10 | true |
| BA72-D17-13 | 新actualtable/方差countercheck与已有EW69等共享knownE2/方法祖先但仪器实验独立；不新测P/R/Jπ/δ/CI、不由Rstatonly或原co/anti简称判source错误。 | readiness and knowledge-impact | synthesis | pp.33–43 full scope | true |

[原Ge20行/参考P输入](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/bass1972-Ge-contract.json)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/bass1972-Ge-result.json)，script `system/scripts/day17_bass1972_fraction_audit.py`。sourceNbar不是原count数，f±回代仅同点代数；源Rerror预算与Pref/跨threshold共用误差必须分层，不反向补actualΣ。

本次`revises`旧WikiN分母含混，`supports`partition共享事件与statonlycalibration分层，`limits`threshold优化/双Comptonreference与fourcrystalproposal移用。关联[[polarimetry-shared-calibration-count-design]]、[[compton-polarimetry]]、[[linear-polarization-asymmetry]]。
