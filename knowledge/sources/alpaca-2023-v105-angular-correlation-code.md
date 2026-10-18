---
type: source
title: "ALPACA 2023 v1.0.5固定代码：相位角色与观测对象执行核验"
aliases: [ALPACA fixed code object, ALPACA 1.0.5 phase-role benchmark]
created: 2026-10-18
updated: 2026-10-18
status: ai-draft
review_status: unreviewed
source_type: software
reading_depth: skimmed
title_original: "alpaca: a linearly-polarized angular-correlation application"
authors: [Udo Friman-Gayer]
year: 2023
version: "1.0.5 at fixed commit"
commit_date: "2023-03-17T18:04:55Z"
license: GPL-3.0-or-later
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "github:u-eff-gee/alpaca@f173c2d2e2fd855451e06446a2cfcce679c42d24"
source_url: "https://github.com/u-eff-gee/alpaca/tree/f173c2d2e2fd855451e06446a2cfcce679c42d24"
raw_file: "raw/software-reference/day16-20261018/alpaca-f173c2d2-81e377a81eaa.tar.gz"
raw_sha256: "81e377a81eaa9a289b2ee6e3b8879d30ad82faf490e40677923521f7c9824daf"
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [110Cd]
reactions: []
experiments: []
models: [Biedenharn-angular-correlation, photon-amplitude-trace]
methods: [angular-correlation, polarization-direction-correlation, phase-convention, code-crosscheck]
observables: [angular-correlation-coefficient, directional-probability-density]
tags: [software-reference, phase-convention, independent-implementation, not-independent-experiment]
---

# ALPACA固定公开代码对象：先辨认算的是什么

## Bibliographic Record

固定[2023-03-17 commit](https://github.com/u-eff-gee/alpaca/commit/f173c2d2e2fd855451e06446a2cfcce679c42d24)，top-level CMake写version1.0.5，COPYING/README为GPLv3或later。这里的2023是commit时间，不是声称v1.0.5的正式发布日期，也不是2026最新版。2026-10-18实际从[固定codeload archive](https://codeload.github.com/u-eff-gee/alpaca/tar.gz/f173c2d2e2fd855451e06446a2cfcce679c42d24)取得126406bytes，SHA-256见frontmatter；GitHub tree非truncated、113个regular blobs均验证Git blobSHA-1和SHA-256，构建/运行后113份源文件仍完全不变。

实际来源archive和源树在`tmp/day16-alpaca-code/`，编译也在其中；raw_file是**未填充的归档槽**，没有raw写入、系统安装或第三方实现进入Wiki Git。程序属GPL参考依赖，Wiki仅保存原创核验harness、数值、版本/构建/依赖证明；没有替换程序许可证。无唯一本地Bib条目，key留空。

## Scope and Reading Depth

这是selected subsystem的定向code审计，whole113blobs不称全部精读。已读完整README主线/Conventions、top/source/python/test CMake；核心W_dir_dir/Av/F/Uv、W_pol_dir/Alphav以及AngularCorrelation的constructor/dispatch/selection/CABI，相关headers和8项selected upstream tests。未完整审计所有sampler、rotation、Python绘图/inversion或全软件测试集，不据113份hash宣称113份内容全读。

实际CMake3.28.3/GNU13.3、GSL2.7.1。系统原已有libgsl27/libgslcblas0；缺devheaders时从Ubuntu公开archive取**匹配2.7.1+dfsg-6ubuntu2的libgsl-dev**，核deb元数据后只解压到repo tmp。没有apt安装/改配置或运行setup.py；GNU同版本tar也下载但未用于构建。该依赖验证是版本/hash/HTTPS来源核验，未假称做GPG认证。配置、所选build targets、8项ctest和本任务CABI benchmark均实际exit0。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| AC23-1 | 固定commit的version为1.0.5、GPL3+，方向/偏振方向correlation以首和末光子为observed，中间unobserved；AngularCorrelation的输入不包含任意beam-oriented初态ρ或sigma/I。本次可核的无取向/首光子条件关联不当作KF89 DCOMAP。 | software-identity-and-domain | direct-code | CMakeLists.txt project；README Sec1/4/5；include/AngularCorrelation.hh | true |
| AC23-2 | W_dir_dir将首/末Av与各Uv乘积相连，normalization对每一步乘1/(1+delta²)；其角函数平均1、球积分4pi。Av常/线性/二次项和GSL3j/6j可直接定位，first/last Biedenharn坐标须按角色映射。 | software-formalism-and-convention | direct-code | source/W_dir_dir.cc calculate_expansion_coefficients_Av/calculate_expansion_coefficients_Uv/calculate_normalization_factor；source/AvCoefficient.cc；source/FCoefficient.cc | true |
| AC23-3 | 程序constructor直接以first em_char是否unknown选择W_dir_dir或W_pol_dir；填写相同spin/δ的EM类型会选择不同观测对象，不只是标签补全。以声明的3→2→0/δKS=−.55例，theta135时dir=.89954143、pol(phi0)=.92027694、pol(phi90)=.87880592；两pol平均回dir。 | API-observable-selection-and-control | direct-code-and-task-execution | source/AngularCorrelation.cc constructor；source/W_pol_dir.cc operator()；本任务API_observable_switch | true |
| AC23-4 | 从未改C++源码构建的shared library导出create/evaluate/free CABI，但固定Pythonwrapper导入时索取未导出的evaluate_angular_correlation_rotated而失败。本任务改用现有CABI执行，不修改upstream source，不声称Python/rotation接口已ready。 | execution-boundary | direct-execution-and-symbol-audit | python/alpaca/angular_correlation.py rotated binding；source/AngularCorrelation.cc extern C末段 | true |
| AC23-5 | 固定phase映射dBfirst=−dKS、dBlast=dKS，及16pi²/32pi²归一后，两条1505角色、764–687–818未观测路径、两个polarized controls与独立photon trace最大差1.12e−15；这是独立C++/GSL实现对本任务CG路线的同模型核验，不增加独立实验或认证旧paper exactproducer。 | bounded-independent-code-crosscheck | task-execution | source/W_dir_dir.cc；source/W_pol_dir.cc；冻结DAY16-ALPACA-FIXED-CODE-ROLE-PHASE-01及本任务result | true |
| AC23-6 | 只故意错first δ映射，mixed网格W最大差.6608114，而pure端点差约1e−15；未观测middle δ反号W差0。仅pure/δ²限制不能验证干涉符号或识别middle sign；这些是冻结失败控制，不是实测误差。 | convention-and-unobserved-failure-control | task-execution | source/AvCoefficient.cc operator()；source/UvCoefficient.cc；本任务wrong_first_sign/unobserved controls | true |

## Summary

本次把旧的“README/blob已核但未执行”边界推进到固定C++实现的实际执行与匹配核验。它支持KS70/D96的已声明发射坐标和同target两角色计算；TableI/II印刷输入的未闭合仍须原response/Σ处理，不能用一份program agreement消除。ALPACA基于同一formalism、README自述和IF21同理论谱系；**算法核验独立于本任务代码，实验采集并未增加**。

## Reproducibility and Source Locators

原创[核验harness](../../system/scripts/day16_alpaca_code_crosscheck.py)、[冻结输入](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/alpaca-comparison-input.json)、[结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/alpaca-comparison-result.json)与[113blobs/构建核验](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/alpaca-execution-verification.json)保存依赖、hash、实际运行范围和失败。首Pythonwrapper错误另留alpaca-first-wrapper-failure.json与harness初版snapshot，不悄然换代码声称原包装成功。

冻结输入SHA-256`dd5b433246a1255640e8ce45a32106bfbe716396104ac7ae8cca674d93cacd80`；实际binary SHA-256`5b983b807d356db313f573c52400291b89a58a3ecf7c239ad7f6f8c4dd7051fe`。binaryhash依构建环境，不要求跨机器bitwise一致。8项upstream测试为Av/Alphav/F/Uv、W_dir_dir/W_pol_dir、unobserved及AngularCorrelation；不是全包/所有samplers测试。

## Competing Interpretations and Limitations

- dB=±dKS映射来自已读[[krane-steffen-1970-cd110-mixing-ratios]]与[[iliadis-friman-gayer-2021-polarization-direction-correlations]]，不是从输出调号。纯E2用primaryL2/delta0输入，避免Infinity造成0×Infinity。
- polarized-first固定方向、电场轴与“只观测方向”是不同conditional对象；本例90度处两者近乎相同，不能只拿90度验证接口对象。程序输出不是仪器asymmetry A或P/Q校准。
- 中间单路propagation须完整photon marginal；多branch合并需额外的条件pathweights。没有把KS70764/658三路径随意选一条。
- 未核RU09 actualproducer、2022review footnote2或2023corrigendum正文；README对此的描述仍只是公开software作者说法，不替代缺失原件。

## Knowledge Impact and Learning Decision

`supports`旧phase桥及1505参考角色的数值实现；`revises`公开程序只要填EM标签就仍计算unpolarized correlation的直觉；`limits`旧Pythonwrapper直接可用、pure checks充分、同理论实现重复等于独立实验的说法。所有新claims true、page unreviewed；不扩展任何旧人审或实测δ/Jpi结论。

## Extracted Pages

- [[dco-pdco-ambiguity-worksheet]]：同target上下游reference与独立代码核验。
- [[krane-steffen-1970-cd110-mixing-ratios]]、[[iliadis-friman-gayer-2021-polarization-direction-correlations]]：公式/定义谱系与actualproducer边界。
- [[angular-correlation]]、[[linear-polarization-asymmetry]]：correlation对象、归一与测量响应分层。
