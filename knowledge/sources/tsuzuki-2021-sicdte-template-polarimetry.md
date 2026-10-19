---
type: source
title: "Si/CdTe模板偏振：16个空间分区、独立零偏振控制与排序能区"
aliases: [Tsuzuki2021 EBIT Compton camera, SiCdTe spatial template polarimetry]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: detector-method-experiment-article
reading_depth: deep-read
title_original: "An application of a Si/CdTe Compton camera for the polarization measurement of hard x rays from highly charged heavy ions"
authors: [Yutaka Tsuzuki, Shin Watanabe, Shimpei Oishi, Nobuyuki Nakamura, Naoki Numadate, Hirokazu Odaka, Yuusuke Uchida, Hiroki Yoneda, Tadayuki Takahashi]
journal: Review of Scientific Instruments
year: 2021
volume: 92
pages: "063101"
doi: "10.1063/5.0050826"
arxiv: "2105.14236v1"
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "arXiv2105.14236v1, 29-May-2021; publisherVoRnotobtained"
source_url: "https://arxiv.org/abs/2105.14236"
raw_file: "raw/papers/gpt/day16-20261018/tsuzuki2021-2105-14236v1-f2c69bdb5ec1.pdf"
raw_sha256: "f2c69bdb5ec135a8334ee977e198a79250b3a1b1322703b7277db8fcdc1f218d"
raw_storage_status: arxiv-staging-verified-raw-archive-deferred
nuclei: []
reactions: []
observables: [linear-polarization, azimuthal-modulation, energy-spectrum, interaction-position]
methods: [Compton-polarimetry, response-template, energy-calibration, event-ordering]
tags: [EBIT, SiCdTe, normalization, domain-boundary, shared-data, systematics]
---

# 空间归一和能区排序都需要实际响应身份

## Bibliographic Record

Y. Tsuzuki等，*Review of Scientific Instruments* **92**,063101(2021)，DOI[10.1063/5.0050826](https://doi.org/10.1063/5.0050826)。Crossref核作者、题名、article number。实际读的是[arXiv2105.14236v1](https://arxiv.org/abs/2105.14236)，submission29-May-2021、PDF首页dated1-Jun-2021；两日期角色不同。AIP给出的VoR PDF请求403，未读VoR，不冒称逐字相同。

[实际arXiv PDF](https://arxiv.org/pdf/2105.14236v1)HTTP200、11页，SHA256见frontmatter；当前在`tmp/day16-tsuzuki2021/arxiv-pdf.pdf`。raw槽未归档，未改raw/Bib。

## Scope and Reading Depth

本session完整读11页SectionsI–VI、References及Dataavailability，视觉核Figs.1–15和Eqs.(1)–(8)及likelihood flow，本文无数据表。其原子Kr radiative-recombination x射线实验仅用于补[[go-2024-demonstration-nuclear-gamma-ray-polarimetry-cdte]] Ref37的response/normalization方法；不把原子偏振当核γ reference，不另开原子结构或Day18课程。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| T21-1 | 实读arXivv1/11页而非未得VoR。Tokyo-EBIT Kr recombination约75keV与Go2024 RIKEN56Fe847是不同source/geometry/energy；共同作者/ComptonSoft方法不认证同一producer或独立系统误差。 | source-version-and-transfer | direct | PDF1；SecIII；G24Ref37 | true |
| T21-2 | EBIT-CC含32层600µm Si、8层bottomCdTe及4×2 sideCdTe，pixel3.2mm，Si总厚1.92cm；约50%是75keV Compton作用概率，不是本选择后的绝对polarimetry效率。 | detector-and-denominator | direct | PDF3SecIIB/Fig2 | true |
| T21-3 | source至camera约500mm、Si阈约8keV，bottomCdTe触发关闭；选择Si–Si或Si–sideCdTe。对侧Ge用于能谱，提供两Kr分量/能标检查，不是另一项独立偏振测量。 | acquisition-and-companion-identity | direct | PDF3–4SecIII；PDF7–8Fig10/VA1 | true |
| T21-4 | 在73–77.5keV窗，94%已记录Compton事件为twohit；Eq3用2E<mec²推ES<EA，因此取minenergy为scatterer。该过程假设单Compton散射加完整吸收，不能无条件迁到847keV。 | ordering-domain | direct-and-kinematic-audit | PDF5SecIVA/Eq3 | true |
| T21-5 | MC按first-hit的xy位置分16个12.8mm×12.8mm区域，νj由各区域能谱fit；不是16个φbins任意free scale。φ模板同样加权；不自动认证Go2024实际division也为这16区。 | spatial-normalization-identity | direct | PDF6SecIVD/Eq4；PDF7–8Eq5–7 | true |
| T21-6 | θK由能量运动学Eq2、θG由source/interaction几何，ARM=θK−θG。criterion3文字称“Geometrical”却写θK，Fig4亦是θK；保留这个preprint字词/符号边界，不据此静默将真实cut改为θG。 | angle-and-version-boundary | direct-visual | PDF5Eq2/Fig4；PDF6criterion3 | true |
| T21-7 | 选择还含73–77.5keV、ARM±60°、指定firsthit圆区；Fig5低能tail不闭合被作者推测为未模拟CdTe谱失真，Fig6坏region/disabledlayers在data/MC都需处理。不能由整体谱相容认证所有selection响应。 | response-counter-evidence | direct-and-author-interpretation | PDF6criteria/Fig5；PDF7Fig6 | true |
| T21-8 | 独立133Ba源81keV的energy/φ/modulation控制用于验证response；残留modulationQ=.010，在假定Q100≈.7下映成ΔΠ≈.015并作sys估计。它与同Krdata的两种P分析分开。 | independent-null-companion | direct | PDF6–8Figs7–9；PDF8VB | true |
| T21-9 | νj能谱fit后，innerPoisson likelihood固定ν并迭代Π，Fig12给完整flow。MLEΠ=.962（.953–.970，1σ），modulationfit=.968±.010使用同Kr events，不是两次独立确认。未给实际νCov/finiteMC/联合hist文件。 | inference-and-shared-data-boundary | direct | PDF8Eq5–8；PDF9Fig12；PDF10Figs13–15 | true |
| T21-10 | 最终作者报Π=.962±.008(stat)±.015(sys)，合成写±.023；算术为线性相加，独立quadrature才为.017。保留作者结果/两层误差，不自行换成更小误差或宣称恢复原CI。 | reported-uncertainty-layer | direct-and-arithmetic | PDF9VB/VI；PDF10Dataavailability之前 | true |
| T21-11 | 自由静止电子/一次散射模型给全角minenergy排序阈E<255.5keV；847的ES=EA在66.628°，两种energy顺序均有physicalcos从35.114°起。Go40–120°跨越排序界，需实际position/ARM/response算法，未测错序率或归罪Go producer。 | conditional-transfer-control | analytic-kinematics | 本页排序公式；T21Eq3；G24scatteringcut | true |
| T21-12 | 同pointsource互换两hit会令scatterplane法向反号；同一共同轴下cos2φ不变。不能概括“错序必翻偏振号”；错序仍可通过incomingaxis、θK/θG、ARM及门选择改变实际observable。 | geometric-failure-control | symbolic-plane-and-spin2-identity | 本页normal/cos2公式；Fig2/Eq2–3 | true |
| T21-13 | 数据声明为向作者reasonable request；3.8e7registered中约4.3e4selected的.113%不是absoluteefficiency。当前未得events/templates/νledger/codeversion/Σ，未联系作者或做experimentalL4refit。 | data-and-readiness-boundary | direct-and-central-arithmetic | PDF6VA；PDF10Dataavailability | true |

## 归一、零控制与shared dataset

16个region以first-hit位置在−25.6…25.6mm的xy平面划4×4网格；原文推测各处非均匀可含source角强度与detector响应。νj由能谱获得，并传入φhist模型；文中采用isotropic source MC后再做这种校正。这里的分区定义不能仅因Go引用此文就填进Go实际producer。

Eq5–7分别是energy template与φPoisson模型，含实测background按observationtime归一。innerlikelihood固定ν；Fig12明确每次更新Π再回energyfit。没有原事件/有限MC与calibrationCov时，不能把“inner fixed”读成整体ν无不确定度，也不能直接说每个φbin都自由归一而完全失辨识。[[modulation-curve]]的signal-only profile/Schur是另声明设计，非本producer认证。

Ba source提供独立于Kr线的零偏振response控制；对侧Ge提供两条RR线的能量/谱身份。Kr的energy fit、MLE、modulation ratio和Π回代则共享同一采集。共同geometry/energycalibration/MC也可带共同系统误差，不按图数加独立样本。

原Ge两峰75.35±.03/75.99±.03keV以.640keV间隔拟合，weightedenergy75.68±.02与CC75.5±.2相容；这不是本run测量或核γ reference P。原子近满Π不能借作不同核跃迁的已知偏振。

## 两hit排序的适用域与失败控制

在一次Compton散射后完整吸收，`EA=E/[1+(E/m)(1−cosθ)]`、`ES=E−EA`，其中`m=mec²`。最小`EA−ES=E(m−2E)/(m+2E)`，所以E<255.5keV才对所有角保证ES<EA。原73–77.5keV窗满足该域；8keV理想阈在E75对应θK≈79.253°，与作者约80°说法量级相符，不据此拟实际ASIC阈值。

对847，equal-deposit角由`cosθ=1−m/E`得到66.628°。反次序也有physicalθK的条件是`cosθ≤1−m²/(2E²)`，阈35.114°。在声明例中：

| 真实θ/deg | ES/keV | EA/keV | 反序也有physicalθK/deg |
| --- | --- | --- | --- |
| 60 | 383.846 | 463.154 | 74.214 |
| 90 | 528.284 | 318.716 | 50.504 |
| 120 | 604.049 | 242.951 | 40.769 |

90/120°时minenergy会选到实际absorber；这些是指定能量/角的运动学演示，没有生成实验counts或错序率。物理cos条件与真实ARM、位置/threshold、事件cut不同，部分反序也可能被后续选择排除。Go实际采用何排序需实际代码/response，本文不能证明其用错了低能规则。

另一方面，pointsource设r1/r2，`nf=(r1−S)×(r2−r1)`，`nr=(r2−S)×(r1−r2)=−nf`；共同轴下`cos2(φ+π)=cos2φ`。仅法向反号不导致cos2符号翻转。实际错误的incoming direction/referenceplane与kinematics/selection仍可改变响应，必须保存完整angle合同。

## Q符号与误差分层

此文Eq8的Q是**modulation factor**，`Π=Q/Q100`；Go的对应量叫Q′，Go的Q是full-polarization sensitivity。Morse已读UNCpreprint又用`A0=Q_M Pbar/2`。同字母Q跨三篇不是同对象，转换须同时匹配harmonic/P/axis/response。

Ba残差`.010/.7=.01429`与作者sys≈.015保留原舍入。最终`.008+.015=.023`不是不知Cov时可自动quadrature缩成.017的授权；较早似然区间/同data另一fit也不组成独立平均。这里未构造新CI，也未将reported sys等同测得Gaussianσ。

## Summary

原件补齐空间分区、独立null与排序能区三个重要细节。支持template polarimetry的方法链，限制其到847核γ的裸迁移与同data多次计证据；原producer/response/Σ仍未恢复。

## Competing Interpretations and Limitations

- 全文来自arXivv1，publisherVoR403；criterion3等字词问题仅对已读版保留，不称正式勘误。
- 模拟未捕捉的CdTe低能tail与firsthitmap失配是作者明确的模型边界，不以总体拟合成功抹掉。
- 8keV/255.5keV规则是声明过程的理想值，bound-electron Doppler、能量误差、multiple scatters与eventclustering会改变实际重建；未估真实mistag。
- RR/DR/QED的物理动机只作原source背景，未以此新增核结构或其它课程结论。相同软件/技术不等于相同数据或原实验版本。
- 未取得实际分区输入/背景/模板/νfit/Cov；原图像不能冒充raw，合理请求声明未触发对外联系。

## Knowledge Impact and Learning Decision

`supports`空间归一、独立零偏振companion与response自检；`limits`低能排序迁移、Q名称互换、同Krdata重复确认和未定义误差组合。当前Day16正式一次、Day17无学分preview；新claims needs_review，无human review或newexperimentalfit。

## Extracted Pages

- [[go-2024-demonstration-nuclear-gamma-ray-polarimetry-cdte]]：Ref37的方法上游与核γ迁移输入。
- [[compton-polarimetry]]、[[modulation-curve]]：空间分区、Q/ν/共有数据与null-control。
- [[linear-polarization-asymmetry]]：同平面法向反号不等于cos2谐波翻号。

## Reproducibility

[运动学/几何程序](../../system/scripts/day16_tsuzuki2021_ordering_audit.py)实际exit0，输入为原文窗/阈及Go847/40–120°，只用解析式与符号控制，未造eventhist。[合同/结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/tsuzuki2021-ordering-audit-result.json)、11页/15图阅读与sourcehash在同run回执。下载PDF/原图/第三方代码仅在tmp，不stage原件。

### 后续finitegeometry companion

[[bizzeti-2015-agata-triple-cluster-polarimetry]] B15-5/15原读给两hit/source同时退化的更强条件sinθcr=m/E−sin(α/2)。本T21的两个energyorders有physicalcos并未使用这个额外几何约束，故不能把energy规则的域外直接等同actualtracking不可解。新增来源还明确ε分母/角cut/packedhit响应，未改变本source原输入或reportedΠ。
