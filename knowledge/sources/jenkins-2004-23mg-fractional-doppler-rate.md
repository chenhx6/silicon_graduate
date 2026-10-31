---
type: source
title: "Jenkins2004：23Mg分数Doppler寿命与混合来源的共振强度"
title_original: "Reevaluation of the 22Na(p,gamma) reaction rate: Implications for the detection of 22Na gamma rays from novae"
aliases: [Jenkins2004 Mg23, J04 fractional Doppler]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: read
authors: [D. G. Jenkins, C. J. Lister, R. V. F. Janssens, et al.]
year: 2004
journal: Physical Review Letters
volume: 92
pages: 031101
doi: 10.1103/PhysRevLett.92.031101
citation_key: ""
canonical_source: "Jenkins et al PRL92 031101 2004 arxivastro-ph0312404v1"
source_url: https://arxiv.org/abs/astro-ph/0312404v1
raw_file: raw/papers/gpt/learning-daily/20261020-DAY18-dsam-lifetime-strength/jenkins-2004-mg23-arxiv-v1.pdf
raw_sha256: d4c407ff4736dd9804498132fe526716726840ab818267a59793b203cfccbadd
raw_storage_status: verified-raw-archive
raw_archive_verified_at: 2026-10-23
nuclei: [23Mg, 23Na, 22Na]
reactions: [12C(12C,n)23Mg]
methods: [fractional-Doppler-shift, angular-correlation, gamma-gamma-coincidence, lifetime]
tags: [DSAM, lifetime, mixing-ratio, calibration, strength, covariance]
---

# 一张表中的新能谱、新寿命和旧强度不是同一类证据

## Bibliographic Record

D. G. Jenkins等，*Phys. Rev. Lett.*92，031101(2004)，DOI [10.1103/PhysRevLett.92.031101](https://doi.org/10.1103/PhysRevLett.92.031101)。实际原件为[arXiv astro-ph/0312404v1](https://arxiv.org/abs/astro-ph/0312404v1)，16Dec2003提交、四页；未取得VoR。PDF日期13Nov2018与源码`novaletter.tex`的`\date{\today}`对应，不是2018新测量。

原PDF缓存`tmp/day17-jenkins2004/jenkins2004-arxiv-v1.pdf`，hash见frontmatter；官方source包SHA256`d756a890c05522a1bac364e65f27577dcb46aa650ea96c191bde7faff30df22d`，白名单tex SHA256`a5a8a2b46ef9f1e3cf3ee5e37bbea6dba09971feeb80fb27bae8c1534fc3016e`。raw/Bib不改。[实际身份/下载](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/jenkins2004-download-identity.json)与[reading scope](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/jenkins2004-reading-scope.json)保存版本、图表及未闭合边界。

## Scope and Reading Depth

先冻结已知K16转引τ10(3)/J7/2的strongpriming，再读四页完整主线/参考文献、TableI、Fig1两rate panel及两条coincidence-spectrum inset，全部四页视觉核；无编号公式。TableI九个parent对象中八个本次观察、7801为未观察的引用输入，不能填成新测量。旧实验分支、模型Γp、adoptedωγ与新gamma/τ分列。

未取得七角原centroids/联合Σ、实际最大位移/停止模型参数、feeding ledger或本数据的完整分析程序。Ref17称将另报详细谱学，本轮尚未核2013详细文与此数据的确切谱系。没有重拟合或复现原寿命置信区间。

## Summary

独立于TRIUMF24Mg+3He采集，这篇ANL12C+12C实验用gamma coincidences识别23Mg支路，以七角centroid的分数Doppler位移配模型提取寿命。表中7784.6态τ10(3)fs是本次报告，而其ωγ1.8(.7)meV明确adopted from Angulo；不能把两者读成此次实验给出的两个独立测量。本文还说明旧pγ阈值会漏掉新发现态的低能分支，使yield上限需要响应合同。

## Experimental or Method Setup

ATLAS22MeV、10pnA12C束打40µg/cm²12C薄靶，Gammasphere约100只Ge，gamma-gamma矩阵和gamma-gamma-gamma cube用于识别支路。高能量线需非线性和recoil校正；源Eu152/Co56共25线，并借7.5MeV质子非弹散射11B向高能扩展校验。

DCO比较all-angle gate下的90°与32°/37°分组，实测参照pure dipole约.9(.1)、pure quadrupole约1.7(.2)。Letter未写出一个带明确分子/分母顺序及全response的公式，不借通常DCO常数补它。分数Doppler用未校正gamma谱七角32/50/80/90/100/130/148°centroid，除以给定beam/target的最大位移，再经Ref16模型映射τ；高unbound态feeding direct为作者假设。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| J04-1 | 实际body四页arxivv1(2003)，期刊metadata2004；源码date-today解释PDF2018，未得VoR。TableI/Fig1完整主线已读，非新增2018实验。 | identity-and-reading-scope | direct-original | PDF1；source date；reading-scope | true |
| J04-2 | 本次22MeV12C/40µgcm−2C/Gammasphere100Ge，以gamma coincidences选23Mg；与K16的75MeV24Mg/3HeAu是不同采集。仍不能因此认所有后续rate输入/模型误差都独立。 | independent-acquisition-and-boundary | direct | PDF2 setup/matrices | true |
| J04-3 | 作者说已作非线性与finite-recoil校正，Eu/Co25线加p+11B高能扩展，并报cascade/crossover校正后约.5–1keV闭合。实际曲线/centroidCov未给；与K16“旧Ex似未校recoil”的二级解释须匹配photon/gap定义后再裁决。 | calibration-and-source-counterstatement | direct-and-readiness | PDF2 calibration；K16 PDF2 Jenkins comparison | true |
| J04-4 | DCO为all-axis gate、90与32/37组比较，pureD约.9(.1)/pureQ约1.7(.2)，混M1/E2依δ变；Letter缺明确ratio顺序/eff与完整alignment合同，不能迁ST99/SG98或用比值单独定δ/Jπ。 | angular-observable-contract | direct | PDF2 DCO paragraph；TableI | true |
| J04-5 | τ来自七角无Doppler校正centroid→fractionalshift→最大位移→模型；高unbound态directfeeding是作者认为可合理假设，不是实测feeding已闭合。没有完整stopping/feeding/fitΣ，τ误差不能由Letter认证模型无关。 | reported-lifetime-inference-chain | direct-and-author-assumption | PDF2 fractional-Doppler paragraph；Ref16 | true |
| J04-6 | TableI新近态7769.2、7779.9与7784.6靠不同gamma branches/coincidence gates区分；Fig1两insets是新态的支路证据。近能母态不能只按energy合并成一条旧resonance。 | level-and-branch-identity | direct-and-author-association | PDF3 TableI/text；PDF4 Fig1 insets | true |
| J04-7 | 7784.6(1.1)态报告tau10(3)fs、RDCO.89(.05)、观测7333.7(1.1)到5/2+支100；omega_gamma1.8(.7)有footnoteb为Angulo adopted，不是从此次τ新提取。未观测弱支不能据100列认全decayinventory精确单支。 | new-versus-adopted-and-branch-boundary | direct | PDF3 TableI row7784.6/footnoteb；text | true |
| J04-8 | Gamma_p前两低共振来自旧22Na(3He,d) spectroscopicfactor结合新energy/J；7779的括号估计还假l=2/原s_l=.04，其它多项omega_gamma引用旧direct/evaluation，7801未观察。混合来源表不是九项新强度测量。 | hybrid-input-lineage | direct-and-author-model | PDF3 TableI footnotesa–d；rate-evaluation paragraph | true |
| J04-9 | 7769的5054.8/2316.9支为58(8)/42(7)%，旧direct装置对<3MeV gamma不敏感；作者结合resenergy等给保守4meV强度上限，无此Letter中的明确CL构造。不能当由单gamma计数直接得到的通用界。 | detector-threshold-counter-evidence | direct-and-author-interpretation | PDF3 TableI/text | true |
| J04-10 | 作者把7623 J9/2+称firm，结合旧transferL4、quadrupole-DCO、已知finalspin及mirror/decay；仅E2三角选择律本身仍允许7/2→5/2。需matching stretched/nonstretched/angular合同，不据简写否定作者，也不把它变无条件DCO定spin规则。 | author-assignment-and-necessary-companion | direct-and-general-selection-boundary | PDF2–3 spin discussion；TableI | true |
| J04-11 | 用原Qp7579.6(1.4)和NR质量数23/22回算九个printedEp中心均在.05keV内；sigmaEx/Q独立的名义quadrature不完全复现printederrors，不调Q/error强配。共同Q若独立于Ex给2.14223keV²乘11ᵀ分量，不是实际完整Σ。 | actual-table-crosscheck-and-conditional-covariance | task-derivation | exercise-result parent_rows/commonQ | true |
| J04-12 | 固定τ10fs给总宽65.8212meV；再固定adoptedomega1.8/J7/2/仅pγ两通道，Bp代数两根约.05040/.94960。只是条件中心值说明branch companion必要，不是新Bp测量/置信区间或新原data组合fit。 | conditional-strength-branch-exercise | task-model | exercise-result tau_width/Bp_roots | true |
| J04-13 | 声明3MeV理想step detector、取原58/42中心，visiblefraction=.58、total/visible≈1.72414；它只核inventory/threshold效应，不复现真实ε或作者4meV保守界。quotedbrancherrors/联合Cov不被强制重归一。 | explicit-design-exercise | task-model-from-real-input | exercise-result threshold_inventory | true |
| J04-14 | Fig1 rate上下界混合新谱学/旧强度/模型输入，未给可据图重建的联合CL；后续nova22Na yield与detectdistance是作者hydrodynamic model，不是天文gamma检出或新实验fact。 | model-result-and-boundary | direct-author-model | PDF3–4 rate evaluation；Fig1；hydrodynamic paragraphs | true |
| J04-15 | 新官方202101编译将2004/2013同列研究链，但160µg靶与J04原40µg不同；7785reaction7/2(+)与Adopted3/2+,5/2+分列。7852/5138在详细版缺失的未确认沟通属于评价注释，不当正式勘误或删除本v1数据。 | evaluated-companion-and-counter-evidence | direct-evaluation-companion | M23-2/4/10 | true |

## Analytical Reconstruction and Self-Audit

[问题冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/jenkins2004-exercise-before.md)、[输入](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/jenkins2004-exercise-contract.json)、[程序](../../system/scripts/day17_jenkins2004_contract.py)与[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/jenkins2004-exercise-result.json)锁定原PDF和打印量。Ep复核只用`Ep≈(23/22)(Ex−Qp)`，不以现代质量或更多位数改原表。独立quadrature控制只条件地把括号数作为SD尺度；Letter未给完整误差/CL构造。若Q与Ex共享输入，完整Cov还含交叉项；不能只把上述common-Q外积加上去就称恢复实际Σ。

| parent Ex keV | 本次状态 | printed Ep lab keV | reportedτ fs | 强度输入角色 |
| --- | --- | --- | --- | --- |
| 7623.4(.9) | observed | 45.8(1.6) | 4(2) | Γp模型/旧spectroscopicfactor；ωγ约1.1×10⁻¹³meV |
| 7646.9(2.6) | observed | 70.4(3.0) | 未给 | Γp模型/旧spectroscopicfactor；ωγ约6.8×10⁻¹⁰meV |
| 7769.2(1.0) | observed | 198.2(1.9) | 2(1) | 保守ωγ≤4meV角色，无本Letter明确CL |
| 7779.9(.9) | observed | 209.4(1.7) | <1，未给CL | 假l=2/原s_l=.04的括号估计ωγ约.05meV，s_l命名不擅自改为C²S |
| 7784.6(1.1) | observed | 214.3(1.8) | 10(3) | ωγ1.8(.7)meV adoptedAngulo |
| 7801(2)，旧Endt输入 | unobserved | 231.5(2.4) | 未给 | ωγ2.2(1.0)meV取Perajarvi |
| 7851.5(1.4) | observed | 284.3(2.0) | 未给 | ωγ15.8(3.4)meV adoptedAngulo |
| 8015.3(1.7) | observed | 455.5(2.3) | 未给 | ωγ68(20)meV adoptedAngulo |
| 8159.7(2.0) | observed | 606.5(2.5) | 未给 | ωγ235(33)meV adoptedAngulo |

τ给Γtotal仍不足以单独给Γgamma或B(EM)：两通道中心练习有互补Bp根，须独立particle/radiative branch与spin。表中1.8(.7)adopted与新τ也不能被当作此次实验两个独立确认。旧threshold的visiblefraction示例是声明设计，不用它反解作者原yield或补置信水平。

## Competing Interpretations and Limitations

- K16重测与此融合蒸发采集不同，但K16引用本文不增加第三次寿命测量；2004/2013谱系要原详细文确认。
- directfeeding、angular response、最大Doppler位移和模型 prescription都在τ链上；没有原centroids/Σ不能将表的括号误差升级为完整统计保证。
- 原finite-recoil校正声明与K16的secondarycomment存在定义/版本待核，不用gamma+roundedfinallevel简单相加裁决谁错。
- v1把单alpha蒸发残核写20Na；简单A/Z守恒给A20/Z10，提示文字label边界。原文保留，不借此改23Mg实验对象或建立新核素观测。
- 并无linear-polarization测量，RDCO/τ不能替P/A/Q、实验δ或模式判定。

## Knowledge Impact and Learning Decision

`supports`独立采集的branch-tagged fractional-Doppler寿命链；`revises`把混合来源TableI当成新强度测量表；`limits`裸RDCO/E2标签、观测branch100与τ对唯一Jπ/δ/Γgamma的保证。新增claim均needs_review，没有human-reviewed或新的实验率/寿命/置信区间。

## Extracted Pages

[[kirsebom-2016-23mg-dsam-lifetimes]]、[[lifetime-strength-audit-165tm-136nd]]、[[doppler-shift-attenuation-method]]、[[linear-polarization-asymmetry]]。Day17原窗口内仅Day18无学分知识预习。

## 官方后续：保留不同自旋与未决身份

[[nndc-2021-mg23-lifetime-strength-reference]] M23-2/4/8/9/10原读五对象。Adopted并未无条件沿用J04的7785 J7/2；capture第二gamma支和新强度也使本v1输入不能直接作完整现代率。7852/5138的2019未确认沟通只按评价注释保存，不补成2013原文已读/正式erratum或改写本页旧claims。
