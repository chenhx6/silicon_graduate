---
type: source
title: "ROOT直方图比较：LL未消费、自动权重与原表达式边界"
title_original: "ROOT TH1::Chi2Test and Chi2TestX source, v6-24-06 and v6-40-04"
aliases: [ROOT Chi2Test LL contract, RCT26 histogram homogeneity]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: public-software-repository
reading_depth: skimmed
authors: [ROOT collaboration]
year: 2026
citation_key: ""
canonical_source: "root-project/root 1211eda93010f26710eafd527d1e66921bffdf8e and 3b796f86a30e274053669931a24d77a3d36c8f18 hist/hist/src/TH1.cxx"
source_url: https://github.com/root-project/root/blob/1211eda93010f26710eafd527d1e66921bffdf8e/hist/hist/src/TH1.cxx
raw_file: raw/code/day17-20261020/ROOT-v64004-TH1.cxx
raw_sha256: 5c354dc674055d4c246942af5e51b4a89be7f7edab03da7a063ccd6d4de2c79d
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [23Mg]
methods: [histogram-analysis, likelihood, covariance, software-component-audit]
tags: [ROOT, DSAM, fit-statistic, empty-bins, software-provenance]
---

# 统计量由实际接口、误差状态与分析域共同定义

## Bibliographic Record

实际联网取得TH1.cxx的[6.40.04固定commit](https://github.com/root-project/root/blob/1211eda93010f26710eafd527d1e66921bffdf8e/hist/hist/src/TH1.cxx)与[6.24.06固定commit](https://github.com/root-project/root/blob/3b796f86a30e274053669931a24d77a3d36c8f18/hist/hist/src/TH1.cxx)。annotatedtags分别解析到上述commit，两个文件的computedGitblob与公开文件API一致；6.24.06 SHA256为`88b7ee394a342f2ac7e4a576f99ef67797a9eb1766db91b72b64387c07d41091`。[下载hash](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/root-chi2-ll-source-manifest.json)、[tag/blob身份](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/root-chi2-ll-exact-tag-identity.json)。本机实际ROOT6.40.04/GetGitCommit v6-40-04；未知thesis实际ROOT版，不以2021tag时间近冒matchingproducer。

## Scope and Reading Depth

先冻结已知Ch6与publicCodeA字符串/旧5.22grep的priming，再读6.40.04 Chi2Test文档完整理论主线、Chi2Test/Chi2TestX全部body及Chisquare的L选项companion。6.24.06两body逐差核，差异为residual数组index及末端doc，不改变LL/比较分支。本轮未读整个ROOT或原作者job。[范围](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/root-chi2-ll-reading-scope.json)。

同时通读publicEVASIONS CodeA_gamma.C，Tools.C两个统计函数body；发现LL与manual调用所在42–141为整段blockcomment。这是对先前grep候选的收窄，不能说release正常运行进入了它。原代码34文件不改。

## Summary

Chi2Test的LL不是likelihood开关。它比较两个histogram是否同形，按内容及Sumw2状态自动选UU/UW/WW；内部估计共同bin概率使用MLE，不等fixed-template的Poisson deviance。另一个方法Chisquare(TF1,"L")有明确L功能，接口不能移植选项。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| RCT26-1 | 两tag已解析固定commit且TH1.cxx下载hash/Gitblob匹配；installed6.40.04确认，原thesis版本/job未知。不是原paperproducer或两个独立实验。 | software-identity-and-scope | direct-code-and-native | exact-tag-identity；reading-scope | true |
| RCT26-2 | Chi2Test wrapper只识别P/CHI2/NDF输出选项，Chi2TestX识别UU/UW/WW/NORM/OF/UF，不消费LL或L；两个固定版本相同。unknownLL静默不触发likelihood。 | actual-option-parser | direct-code | v640 TH1.cxx L2043–2211；v624 L2007–2175 | true |
| RCT26-3 | 未显式UU/UW/WW时由sumcontent与effectiveentries=sumw²/sumw2比较自动选型；同contents的errorhistory可换统计量，nosw2/Scale/Add历史需实际保存。 | error-state-and-statistic | direct-code | v640 TH1.cxx L2195–2223 | true |
| RCT26-4 | UU按两hist和共同bin概率的同质性Pearson式，UW/WW另计模板对角误差；内部共同概率MLE不等fixedexpectedPoissondeviance。不能从文档maximumlikelihood字样推数值函数等价。 | actual-test-definition | direct-code | v640 TH1.cxx L1760–2039/L2287–2525 | true |
| RCT26-5 | 范围来自firsthist axisrange，normalization用所选bin；ndf先selectedbins−1、jointempty再减，不自动扣物理τ/E0拟合自由度。reducedχ²及其p值不是两参数profilecoverage认证。 | domain-normalization-and-ndf | direct-code | v640 TH1.cxx L2150–2183/L2260–2276/L2312 | true |
| RCT26-6 | 独立方法TH1::Chisquare(TF1,"L")明确使用Poissonlikelihoodratio，Fit的L亦为不同接口；这不能赋予Chi2Test的LL新语义。 | companion-interface-boundary | direct-code | v640 TH1.cxx L2529–2551 | true |
| RCT26-7 | 声明D0/5/20/0/7/0与M3/10/15/0/4/0的nativeLL与空选项都给6.199134；设置模型variance=M/10后均为UW8.783184。contents相同结果不同只是声明组件反证，不是实验MC误差估计。 | native-component-control | task-native-ROOT | exercise native_cases base/stored | true |
| RCT26-8 | publicCodeA_gamma.C L42–141整个LL/handlikelihood/本地input/legend示例被blockcomment，extract_width1分支空；不能把字符串存在写成实际paperfit已调用或据此裁τ偏差。 | producer-callpath-revision | direct-release-code | EVASIONS CodeA_gamma.C L38–141 | true |
| RCT26-9 | publicTools.C log_likelihood只在o>0且s>0累2(s−o+o log(o/s))，o0分支被注释；故o0s>0缺2s，o>0s0也被略而不是∞。摘取原body原样用installedROOT编译运行，仅组件非原job。 | actual-expression-zero-domain | direct-code-and-native | EVASIONS Tools.C L66–86 | true |
| RCT26-10 | 原函数nativebase给6.410432，而同范围fixedmodeldeviance12.410432，差6来自o0/m3；positiveo2/m0仍finite6.410432而properdeviance∞。不以这些自设counts量化paperCI。 | native-counterexample | task-native-component | exercise native_cases base/positive-zero | true |
| RCT26-11 | manual循环i<FindBin(high)排high所在bin；axisrange到high则含该bin。high2.5在第三bin时manual只bin1/2，而Chi2Test所选含bin3；两函数即使同range数字也不一定同domain。 | exact-endpoint-control | direct-code-and-native | EVASIONS Tools.C L71–73；exercise endpoint | true |
| RCT26-12 | 原helper chi2_ndf_1D也有不同合同：i<Nbins排最后bin、只o>0、分母ero²+ers²及nbins−1−numberfitparam。与Chi2Test/rawdeviance不能混称同χ²；原job缺不代选。 | alternative-statistic-contract | direct-release-code | EVASIONS Tools.C L48–64 | true |
| RCT26-13 | API/test输入、Sumw2/scale、mask/bin、MCstats/共享Cov和fit参数rank必须整套匹配；本轮只建立新接口边界，未修producer/重fitτ/BR/CI或判实验错误。 | readiness-and-use-gate | synthesis-with-code | RCT26-2/3/5/8/9 | true |
| RCT26-14 | 后续用F23原公开25display点做native查询，展示Sumw2/normalizer/配套variance合同改变结果；fallback41.6546、zero模板110.1959及一致UW缩放47.9398均条件合同，不鉴定原paperMC/fitstatistic。 | actual-public-graph-companion | direct-data-and-native | F23-24/25/26/27/28 | true |

## Analytical Reconstruction and Self-Audit

[读取前冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/root-chi2-ll-before-source.md)、[native前设计](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/root-chi2-ll-native-before.md)、[原表达式hash/行](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/root-chi2-ll-expression-manifest.json)、[组件输入](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/root-chi2-ll-exercise-contract.json)、[程序](../../system/scripts/day17_root_chi2_ll_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/root-chi2-ll-exercise-result.json)。

native原表达式通过Cling编译，没有运行有uninitializedinput的fullMC。ROOT低counts/错误UU指定的warnings有意保留，[stderr](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/root-chi2-ll-native-stderr.txt)。它们提示适用域，不能以exit0抹成coverage已通过。无histcounts属于实验，原raw/code/ROOT配置不改。

## Competing Interpretations and Limitations

thesis“maximumlikelihood option”可能指另一个实际job或共同概率估计术语，当前不足唯一解释；当前public示例是inactive，不能从它建立papercallpath。公开F23 source-data曲线/errors也不提供Sumw2原历史、mask、原τjob或共同Cov。旧5.22源码仅另说明API历史，不计独立实验。

## Knowledge Impact and Learning Decision

`revises`把LL字符串视为已经运行的likelihood实现；`limits`以名字替统计合同和未知errorhistory的模板比较；`supports`记录实际API/range/normalizer/zero域。没有新τ/BR/spin/CI，所有新增claims needs_review，仅Day18无学分preview。

## Extracted Pages

[[fougeres-2022-thesis-evasions-response-contract]]、[[evasions-2023-public-release-native-readiness]]、[[lifetime-strength-audit-165tm-136nd]]、[[root-2008-v522-background-error-contract]]。
