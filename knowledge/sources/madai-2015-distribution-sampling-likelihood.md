---
type: source
title: "MADAI2015公开内核：covariance、likelihood与两条API的合同"
title_original: "MADAI DistributionSampling Model and sampler call path"
aliases: [MADAI 2015 likelihood kernel, DistributionSampling likelihood component]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: software-code
reading_depth: read
authors: [MADAI project contributors]
year: 2015
data_version: 9f9ee0dac704d77492d9905b4d90a57746201912
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: https://github.com/MADAI/DistributionSampling/tree/9f9ee0dac704d77492d9905b4d90a57746201912
source_url: https://github.com/MADAI/DistributionSampling/tree/9f9ee0dac704d77492d9905b4d90a57746201912
raw_file: raw/software-reference/day17-20261019/MADAI-Model-9f9ee0da.cxx
raw_sha256: 1784476b861fd4d74cd0d747d41c57541cac897965947b1e89aa116e8642882f
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: []
reactions: []
models: [Gaussian-likelihood, Gaussian-process-emulator, MCMC]
methods: [fixed-code-component-execution, likelihood-contract-audit]
tags: [software, covariance, Bayesian-inference, likelihood, DSAM]
---

# MADAI公开likelihood核与paperproducer是两个对象

## Bibliographic Record

公开[MADAI/DistributionSampling](https://github.com/MADAI/DistributionSampling/tree/9f9ee0dac704d77492d9905b4d90a57746201912)，固定commit `9f9ee0dac704d77492d9905b4d90a57746201912`，commitdate2015-03-25。LICENSE为UNC/MADAI的BSD式条款。官方项目站重定向后的证书过期，未关闭TLS验证；公开GitHub source/tree/blob另经HTTPS取得，所有所选源与tree Gitblob/SHA256核。缓存`tmp/day17-madai/original/`，raw槽未填。

[[sun-2023-bayesian-dsam-31s]] SUN23-8/15只说tailoredMADAI与项目Ref76，没有给papercommit/config或修改；本公开对象不能冒称其2022/2023 exactproducer。

## Scope and Reading Depth

完整读Model.cxx、GaussianProcessEmulatedModel.cxx、MetropolisHastingsSampler.cxx、README与LICENSE；定向读Model.h API、Sampler SetModel/Initialize、SamplerCSVWriter GenerateSamplesAndSaveToFile、madai_generate_trace应用与Defaults.cxx的covflag、GPtest的flag对照。未通读整个repo/GP内部PCA算法，也未执行完整MCMC/GP或Sun数据。

实际原样编译Model.cxx、Parameter.cxx、Distribution.cxx、UniformDistribution.cxx四文件，另加声明fixture；Eigen固定3.3.7(commitcf794d3b741a6278df169e58461f8529f43bce5d)只作为本组件依赖。源码文件未patch/旧sourcehash保持，两个Model API均实际执行。完整项目CMake先因Boost头/iostreams缺失exit1；不装系统包，采用必要四文件组件，不把组件成功改写成fullprojectbuild。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| MDA15-1 | 固定2015publicrepo原件/日期/选定blob/hash已核；Sun只给tailored框架名和站点，无papercommit/config/原counts。公开kernel执行不认证其实际分析。 | identity-and-producer-boundary | direct-code-and-primary-scope | commit9f9ee0da；SUN23-15；source-scope receipt | true |
| MDA15-2 | Model两API组合同一observedconstantCov与可选modelCov，然后返回−½rᵀΣ⁻¹r+logPrior，没有variablelogdet项；GetScalarOutputsAndLogLikelihood的返回值已经含prior，不能外层再无条件加一遍。 | code-likelihood-contract | direct-code-and-native-component | Model.cxx GetScalarOutputsAndLogLikelihood；GetScalarOutputsAndLogLikelihoodAndLikelihoodErrorGradient | true |
| MDA15-3 | declaredresidual=1、totalvariance从1到4时，native logratio+.375(比1.45499)，完整Gaussian中随参数的normalizer给−.318147(比.727496)，排序反转。相同零残差两variance native均0；这是所声明组件反例，不是31S实际CI偏差。 | native-component-normalizer-counterexample | executed-original-code-and-derivation | madai-likelihood-result varying_covariance_contrast | true |
| MDA15-4 | 固定Σ、只改变mean时，省logdet是同一个常数，不改相对likelihood；因此不能从printedEq3或出现quadratic就断言所有应用错。组件用同variance4的两个残差核此必要反证。 | constant-covariance-companion-control | executed-original-code-and-derivation | madai-likelihood-result checks constant_cov_mean_ratio_control | true |
| MDA15-5 | 基类defaultUseModelCov=false；应用Defaults::MCMC_USE_MODEL_ERROR亦false，但可由settings传给SamplerCSVWritersetter。PCA_USE_MODEL_ERROR是另一flag。当前default不证明Sun实际配置，实际paper说σ含emulator时尤须匹配。 | flag-consumption-and-version-boundary | direct-code-and-native-component | Model.cxx constructor；Defaults.cxx69；madai_generate_trace117；SamplerCSVWriter42 | true |
| MDA15-6 | ordinaryAPI识别名为log_likelihood的output并直接用它+prior；另一gradient-output API没有同分支。声明customfixture两者约−.818147与−.0836706。publicMH Initialize调用ordinary，NextSample却调用gradient-output，故ordinaryescape不能未经核验当完整MCMC修复。 | two-API-callpath-counterexample | direct-code-and-native-component | Model.cxx368；Model.cxx GetScalarOutputsAndLogLikelihoodAndLikelihoodErrorGradient；MetropolisHastingsSampler.cxx63/109 | true |
| MDA15-7 | 显式uniformprior范围外返回−inf的正控制成立；显式invalidnegative总Cov则两API仍返回finite+.5。源码QR前PSD/singular检查仅FIXME/comment。负Cov是故意的非物理控制，不声称作者/真实GP产生它。 | prior-positive-and-domain-failure-controls | executed-original-code-and-boundary | madai-likelihood-result rows finite_uniform_prior/out_of_prior/invalid_negative_totalcov | true |
| MDA15-8 | 四文件native编译/运行均exit0且所声明behaviourchecks通过；这是验证观测到的行为/反例，不是Gaussian统计合同或原fullapp全通过。全项目Boost失败、初只ordinary组件与后补双API版本都留档；未得Sun训练/priors/SI/patch，不能作其实验重拟。 | reproducibility-and-scope | direct-artifact | madai-likelihood-result；sun2023-madai-fullbuild-initial-boundary | true |

## Summary

本对象具体说明“likelihood函数名/开关存在”不等于实际消费了误差，原样组件能把Σ依赖与API分支变成可检验问题。它没有把Sun原文Eq3的一项疑问变成对其实验的定案：actualpaperimplementation、settings和数据仍缺。

## 变量Cov的统计合同

对正定Σ(x)，完整Gaussian的loglikelihood除固定2π项外为

\[
\ell(x)=-\frac12r(x)^T\Sigma(x)^{-1}r(x)-\frac12\log\det\Sigma(x).
\]

若Σ固定，末项对参数是常数，可在likelihoodratio中取消；若Σ变化，则不能仅因它写在“误差”中就删除。本组件的variance1/4只是新声明输入，不是从Sun后验图反解其Σ，更未用ratio1.45499重标原寿命。

Model函数名LogLikelihood含logPrior，customoutputescape也再加prior。使用外部sampler时需明确返回的是likelihood还是posterior；本页没有执行完整sampler，sourcecallpath仅作为必要伴随输入。

## Competing Interpretations and Limitations

- Sun可能采用fixedΣ、修改过的核或另一调用路径；没有papercommit/actualsettings，不能从2015publiccode决定其2022分析。
- ordinaryAPI可自给log_likelihood是必要反证，但原MH下一步改用另一API，不能只跑ordinarycontrol便宣称fullpipeline可绕过。
- flagfalse对所声明fixeduncertainty模型可以是明确设计；本文只揭示必须记录flag，不宣称所有用户都需打开。
- 负Σ和singular域要由数据/GP产生机制及调用方约束；本故意invalidcontrol不证明真实GP失败。

## Reproducibility

[来源前问题冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/sun2023-madai-before-code-freeze.json)、[源码scope/blobhash](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/madai-likelihood-source-scope.json)、[合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/madai-likelihood-contract.json)、[fixture](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/madai-likelihood-fixture.cpp)、[程序](../../system/scripts/day17_madai_likelihood_component.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/madai-likelihood-result.json)保存实际输入/两API/编译stderr与binaryhash。

运行`python3 system/scripts/day17_madai_likelihood_component.py`。需要按已记录pin恢复repo/Eigencache；本程序先核所有frozenhash，不自动取任意新版或写系统目录。firstcomponent的contract/fixture/script/result保留；补核两API没有覆盖首次版本。所有物理/统计结论只限声明组件，非原MCMC chain复现。

## Analytical Reconstruction and Self-Audit

两API的scalarlogvalue均原样执行；Metropolis完整文件只读、未编译完整sampler。第二API不含custombranch的控制纠正了初只测ordinary时可能产生的过宽推断；没有把最初ordinarycontrol延伸为paperMCMC保证。新增claims全needs_review，未改原Sun/其它sourceflags。

## Knowledge Impact and Learning Decision

`supports`实际输入消费/完整callpath比公式名字更有信息；`limits`把variableemulatorerror自动视为正确Gaussian、或把publicrepo当paperproducer。数学合同与公开代码行为可核，实验归因仍readiness；本Day17内恰好无学分Day18方法preview，不授新卡。

## Human Review Triage

P1：若以后引用为具体论文uncertainty失效的证据，先取得该论文的actualversion/config/训练与data；当前只作条件反例和下一输入，不输出原实验错误判决。

## Extracted Pages

[[sun-2023-bayesian-dsam-31s]]、[[doppler-shift-attenuation-method]]、[[lifetime-strength-audit-165tm-136nd]]。
