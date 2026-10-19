---
type: source
title: "Sun2023：31S的MCMC Bayesian DSAM与输入边界"
aliases: [Sun 2023 Bayesian DSAM, Sun 2022 arxiv2203.10336v2]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: experiment-and-method
reading_depth: deep-read
title_original: "First application of Markov chain Monte Carlo-based Bayesian data analysis to the Doppler-shift attenuation method"
authors: [L. J. Sun, C. Fry, B. Davids, N. Esker, C. Wrede, M. Alcorta, S. Bhattacharjee, M. Bowry, B. A. Brown, et-al]
journal: Physics Letters B
year: 2023
volume: 839
pages: 137801
doi: 10.1016/j.physletb.2023.137801
citation_key: ""
canonical_source: https://doi.org/10.1016/j.physletb.2023.137801
raw_file: raw/papers/2023_Sun_et_al_Bayesian_Doppler_shift_attenuation_method.pdf
raw_sha256: f19bb23761529d355efbe83e5a8063f4e99a9c43bd65cc906604d129aad55b34
nuclei: [31S, 31P]
reactions: [3He(32S,alpha)31S]
methods: [doppler-shift-attenuation-method, Bayesian-inference, MCMC, Gaussian-process-emulator]
tags: [DSAM, covariance, prior, lifetime, surrogate, 31S]
---

# Sun2023：Bayesian DSAM首先要问likelihood与prior合同

## Bibliographic Record

L. J. Sun等，*Physics Letters B*839,137801(2023)，DOI[10.1016/j.physletb.2023.137801](https://doi.org/10.1016/j.physletb.2023.137801)。Crossref题名/DOI/卷/文章号已核；实际原读为[arxiv2203.10336v2](https://arxiv.org/abs/2203.10336v2)，页首9Nov2022、稿内dated10Nov2022，十页。不能将其当已取得2023VoR body；作者列表版本差异也保留。上方raw路径为保留归档槽，未写入raw或protectedBib。

实际PDF位于`tmp/day17-sun2023/PDFs/First_application_of_Markov_chain_Monte_Carlo-based_Bayesian_data_analysis_to_the_Doppler-shift_attenuation_method.pdf`，SHA256 `f19bb23761529d355efbe83e5a8063f4e99a9c43bd65cc906604d129aad55b34`。官方arxivsrc包SHA256 `8c1a995e1b4dc65d67e168ec1d030aaae44ccafaf697a4dfbbc6a081aec357fb`，只含maintex和六EPS，不含补充材料。

## Scope and Reading Depth

本session先冻承认Wang2023二级review/metadata priming的主动回忆，再取得原件。实际读十页全部主线/参考，五图(Figs1–5)、一表(TableI)、三式(Eqs1–3)，PDF2/4/5/6/7关键原图视觉核；maintex相关literalpriors/likelihood补核。初始v2摄入时未读SupplementalMaterial；后续新入口已取得并完整原读publisherSI五页/十三图，见本页SUN23-17–22。仍未取得原counts/训练网格/response/posteriordraws或作者tailoredMADAI。网络/下载/正文scope见本run[sun2023-download-identity](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/sun2023-download-identity.json)及后续readingscope；不从review的赞许替代原件。

## Summary

31S的transfer粒子tag与单clover addback谱提供不同于高spin多γbelowgates的DSAM输入。作者以GEANT4/旧fs模拟、PCA+GP surrogate和MCMC求寿命后验，报告两有限τ与四项90thpercentile上限，同时明确nuisancepriors会强烈影响后验。方法提供了joint参数讨论，但没有消除模型/校准/likelihood选择依赖，也没有让同data的frequentist比较变成独立实验。

## Experimental or Theoretical Setup

128MeV32S7+轰击3He implantedAu，以3He(32S,α)31S制备；87µm/1mm硅望远镜、aperture<13°，clover位于0°/距靶78mm，四晶addback谱。2MeVα窗对应约1MeV激发窗；其transferkinematicgating用于压制竞争反应与间接feeding，不能无对象套到Jensen/MU08的多步sidefeeding模型。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| SUN23-1 | 本页期刊metadata为PLB839137801(2023)，实际body是2022arxivv2十页；官方src仅maintex/6EPS。未得2023VoR/SI，不把这些版本算独立实验。 | identity-and-version | direct-metadata-and-original | PDF1；arxiv2203.10336v2；officialsrc manifest | true |
| SUN23-2 | 128MeV32S+3He implantedAu、αtag硅87µm/1mm/<13°、0°clover78mm与addback谱，非GRIFFIN全阵列Compton数据。 | experimental-setup | direct | PDF2 SecII；Fig1 | true |
| SUN23-3 | α窗宽2MeV约对应1MeV激发窗；transferkinematics门用于压制间接feeding，γ谱用2keVbins。near6390的5141线可能含6392.5态的5143.1，选择4156线作较唯一身份尝试；不能按近能量合并母态。 | selection-and-identity-boundary | direct | PDF2末段；PDF3 SecIII | true |
| SUN23-4 | 新GEANT4用于ps、旧MonteCarlo用于fs；反应点3He implantationprofile由SRIM，beamspread.2%FWHM；α在lab先取isotropic，小aperture下anisotropic替代影响小是作者/上游估计，非普遍定理。 | response-model-and-author-control | direct-and-author-boundary | PDF3 SecIII | true |
| SUN23-5 | EMG detectorresponse的width/decay由多条unshifted279–6129keV线表征；runbyrun用279/2814标准，6129作高能校验。列出的四nuisance是Eγ、bkg、sp、A2，不能由流程图responsebox自行认定所有EMG参数都进入joint采样。 | response-calibration-and-parameter-boundary | direct | PDF2 SecII；PDF3 SecIII；PDF4 SecIV/Fig3 | true |
| SUN23-6 | lifetimeprior字面constant于τ>0、负域0；Eγ与bkg为Gaussian，sp短/长态分别10%/20%Gaussian，A2在[−1,1]uniform且A4固定0；两long-lived态省A2。finiteτ上限/完整训练范围需实际SI/config，不能只凭正半轴文字认证tail。 | prior-and-domain-contract | direct-and-boundary | PDF4 Eqs1–2及SecIV | true |
| SUN23-7 | Eq3字面L≈exp[−Σ(residual²/2σi²)]，σ含experimental/theoretical及emulatorpredictiveuncertainty，均作Gaussian。若Σ依参数变化，规范Gaussian另需logdetΣ；是否固定Σ/actualtailoredcode如何实现未得，不将printedapprox直接判实验/代码错误。 | likelihood-literal-and-conditional-inference | direct-and-derived | PDF4 Eq3；PDF5首段 | true |
| SUN23-8 | hundredsfactorialdesignpoints跑fullDSAM，outputs作PCA后GPsurrogate；50kburnin后1millionsteps。作者称除4156链外几千iterations足够convergence，未在所取body报告Rhat/ESS/完整holdout或papercode，不把step数当普遍收敛证书。 | emulator-and-sampling-scope | direct-and-boundary | PDF5 SecIV；Fig4 | true |
| SUN23-9 | 作者明确Eγ/bkg/sp的restrictivepriors强烈影响posterior；两long-lived态τ–sp负相关，短态称无同样相关。posteriorpredictive窄/贴data是作者的约束证据，不是全部模型误差已被验证。 | author-stated-prior-dependence | direct | PDF5 SecIV；Fig4 | true |
| SUN23-10 | 有限τ用16/50/84percentile给1120(180)fs(1248)与250(80)fs(2234)；四更高态用90thpercentile上限<11/<16/<7/<15fs。原文称confidence，实际构造是所声明posteriorquantile，不补frequentistcoverage保证。 | reported-posterior-result-and-semantics | direct-and-boundary | PDF5 SecV；PDF7 TableI | true |
| SUN23-11 | 6390态4156线受低统计限制，正文说不能给finiteconstraint、posterior相对prior在20fs以下favored；随后τ<20fs→Γ>33meV/ωγ>5.5µeV是条件影响链，不是TableI四项90%上限中的第五项。SI Fig13未得，不补90%概率。 | counter-evidence-and-limit-status | direct-and-boundary | PDF6 SecV；Fig5；PDF7 TableI | true |
| SUN23-12 | 作者以USDB的E2partialτ6.9ps修正1248实测总τ，得到M1partialτ1.33(26)ps、B(M1).022(.004)µN²、RME.30(.03)µN。标签experimental仍含modelE2扣除，不等独立测得δ/纯M1。 | reported-model-assisted-extraction | direct | PDF6 SecV | true |
| SUN23-13 | 本任务用1/τM1=1/τ−1/τE2复算约1.33702ps，固定model时local误差.25652ps，现代单位/roundedE给B≈.021883、RME≈.295858。同输入/同model算术不是新测量、原posterior或completeCI。 | conditional-rate-reconstruction | derived | PDF6 SecV；sun2023-rate-result | true |
| SUN23-14 | 作者另报同data标准frequentist提取相合，非第二实验；本次1248寿命1120(180)与既往624(32)的差异仍保留，未重审其primary或合并为新worldaverage。五Hamiltonian共享sdspace/有效算符/能量缩放，不算五次测量。 | independence-and-counter-input | direct-and-boundary | PDF5–6 SecV；PDF7 TableI | true |
| SUN23-15 | 所取v2/src未给actualcountfiles/training/PCA/GPstates/posteriordraws或tailoredMADAIcommit；项目公开repo2015对象只是下一待核上游软件，不能把它冒作paperexactproducer。publisherFULL401、discovery无candidate，未绕过或原样重试。 | reproducibility-and-access-readiness | direct-provenance-boundary | PDF5/10 Ref76；sun2023-source-si-discovery；sun2023-publisher-full-attempt | true |

| SUN23-16 | 公开MADAI2015的原样四文件组件已实际执行两API，variableCov的quadratic-only与customoutput分支差异见MDA15-2–8；这些是公开上游的条件反例。Sun实际tailoredcode/config/Σ仍未知，不把它归因为本文实验CI错误或声称paper已重放。 | upstream-component-and-attribution-boundary | indirect-code-companion | MDA15-2；MDA15-6；MDA15-8 | true |

| SUN23-17 | 之后经官方publisherCDN精确PII取得mmc1.pdf，五页/十三图/technicaltext完整原读与视觉核，sha630d45a82229a3e45cc1a712b88a0c00c8fd6512398ac9d01843a9aed5c0d0aa。旧未得SI为008历史；v2源码包确实不含它，API401未被改写。publisherSI不是已得VoRmainbody或独立实验。 | new-primary-SI-identity-and-scope | direct-publisher-SI | SI PDF1 title；SI Fig1–13；si-reading-scope | true |
| SUN23-18 | SI给35keV3He implanted入25µmAu、arealdensity6×10^17cm−2和冷却/beamcollimator；DAQ为GRIFFIN Ge/GRIF16、GRIFC/GRIFClk、modifiedMIDAS及GRSISortunpacking。它不提供polarimetryselector/calibrationQ或Sun tailoredbayesianproducer。 | experimental-input-and-software-role | direct-SI-and-boundary | SI PDF1 Sec1.2/1.3；SI PDF2 Fig1 | true |
| SUN23-19 | SI Fig2–7的αgate中心依次47/46/45/42/42/39MeV，对2234/3076/3435/4971/5156/6390态；3435经2186支、6390经4156支。图中addbackprior/posterior曲线仍为原data/model，不是新增actualbinfiles或独立数据。 | state-gate-role-ledger | direct-SI | SI PDF2–3 Fig2–7 | true |
| SUN23-20 | SI Fig8的2234长态为4参数无A2，Fig9–13短态为5参数含A2；Fig9/12caption明确3076/5156为1/2+。A2的物理spin-density/帧或phenomenologicalresponse角色仍须核，不能将这些posterior视为已测核alignment/δ。 | angular-nuisance-and-state-boundary | direct-SI-and-open-interpretation | SI PDF4 Fig8/9；SI PDF5 Fig12/13 | true |
| SUN23-21 | Fig13确有6390的τ先验/后验和nuisancepanels；它不另给90thpercentile数值、完整τsupport/训练config或posterior draws。不能只按图轴范围认证hardpriorcut，或凭posterior高于prior处就给90%probability。 | posterior-figure-and-quantile-boundary | direct-SI-and-statistical-boundary | SI PDF5 Fig13；v2 PDF6 SecV | true |
| SUN23-22 | 此SI只技术说明/图及refs，没有原histogram/GRIFTevents、GP训练/PCAstate/likelihoodpatch/config或drawfiles；actualinputreadiness仍缺。获得SI消除的是来源读取缺口，不认证2015publickernel为本文producer。 | data-and-producer-readiness | direct-SI-scope-boundary | SI PDF1–5；MDA15-1 | true |

## Nuclear Structure Information

31S低位与31P mirrorlifetimes作核结构benchmark；4971负宇称态未在sd-only计算匹配，因模型不含crossshellexcitation。六项DSAM结果和6390的弱线/条件应用分列，未给新的Jπ/δ或三轴性判断。

## Authors' Interpretation

作者认为Bayesian框架更有利于处理多维相关参数，并把本次结果视为未来完全实验约束30P(p,γ)31S rate的一步；他们同时承认6390统计不足。综述的“reliableuncertainty”评价必须带入本文priors/likelihood/model与收敛/输入边界，不能只保留赞词。

## Model Results

NuShellX/五sdHamiltonian、有效M1/E2算符与实验能量E^(2L+1)缩放用于比较；USDB E2部分寿命进入M1提取。若把该理论部分的uncertainty忽略，派生M1误差就仍条件于该理论值；没有为其捏造modelσ。

## Competing Interpretations and Limitations

- Eq3的σ/Σ是否随参数变化、是否含完整binCov、normalizer/PCA截断和finiteMC如何进入，需actualtailoredimplementation；目前不从print疑问推实验失败。
- τ>0的uniform与actual有限training/support区间不是同一个完整prior说明；source当前未提供tailrange配置。不能据未见数据给posteriorimproper定论，也不把1millionsteps当消除了prior依赖。
- αtag的feeding压制与MU08/Jensenbelowgate不是相同实验；不裸迁10/20%sp priors给高spin研究。
- 本页不是Bayesian优于所有profilelikelihood的普遍证明；作者用同data频率学方法相合是方法对照，非source独立性。

## Analytical Reconstruction and Self-Audit

令t=τ、e=τE2，条件M1partialτ为te/(e−t)，必须0<t<e；∂τM/∂t=1/(1−t/e)²，∂τM/∂e=−t²/(e−t)²。实际Var需两输入Var和Cov；只固定e=6.9ps、以.18ps作local尺度时σ≈.25652ps，不等原posterior非线性变换。源E2centralrate占总rate约16.232%，所以“dominantM1”不意味着modelE2可无条件删除。

[新合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/sun2023-rate-contract.json)/[程序](../../system/scripts/day17_sun2023_rate_boundary.py)/[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/sun2023-rate-result.json)核PDF/maintexhash、exact1932/1445ps与rateconservation。20fs给Γ=ℏ/τ≈32.9106meV仅作条件单位检查，不发明6390的90%upperlimit。现代C_M1来自[[lange-kumar-hamilton-1982-multipole-admixtures]]的LKH82率公式的既有单位重构，不称该数字直接印在Sun正文。

## Knowledge Impact and Learning Decision

`supports`joint参数/priors显式化的价值；`revises`只按方法名字就称完整uncertainty、将model-subtractedB当独立测量的习惯；`limits`6390的20fs/反应率下限和同data方法对照的证据地位。新claims全needs_review，原review不升级；仅Day17内无学分Day18方法preview。

## Human Review Triage

P1：若用于正式31S寿命/反应率或DSAM精度裁决，先定向核SI/实际support/likelihood与producer；当前缺口由Codex自审追踪，不自动变成用户待办。

## Extracted Pages

[[doppler-shift-attenuation-method]]、[[lifetime-strength-audit-165tm-136nd]]、[[high-spin-lifetime-strength-deformation]]；上游二级入口[[wang-2023-experimental-studies-nuclear-chirality-china]]与本primary谱系明确，不重复计source。

固定公开软件的实际执行/版本与调用边界见[[madai-2015-distribution-sampling-likelihood]]；它补充SUN23-7的下一输入问题，不替本source actualpaperproducer。

## 后续正式SI原读与状态修订

[新下载/identity](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/sun2023-si-cdn-attempt.json)、[全读前问题冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/sun2023-before-full-si-freeze.json)与[actualscope](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/sun2023-si-reading-scope.json)保存新入口，不重复原失败URL或关闭TLS。SUN23-1–16的“未读/未得SI”属于008/原公开代码摄入阶段的历史readiness，最新为17–22；oldclaimflags原样保留，不从新scope清掉needs_review。

下一高信息问题是Fig9/12的1/2+状态与A2 nuisance对象：需把明确帧/条件密度的核rank允许域和emulatorphenomenologicalresponse区分；目前只冻结为开放问题，不输出原fit错误或τbias。
