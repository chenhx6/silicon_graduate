---
type: source
title: "IAEA阻止数据库：S/Au、O/Ta的实验覆盖与DSAM输入边界"
title_original: "Electronic Stopping Power of Matter for Ions — selected S/Au and O/Ta records"
aliases: [IAEA stopping S Au O Ta, 阻止截面覆盖核查]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: compiled-experimental-and-model-data
reading_depth: read
authors: [IAEA Nuclear Data Section]
year: 2026
citation_key: ""
canonical_source: "IAEA Stopping Power Database 2026-09 selected S-Au O-Ta download objects"
source_url: https://www-nds.iaea.org/stopping/
data_version: website-version-2026-09-selected-pairs-last-modified-2023-11-27
raw_file: raw/nuclear-data/day17-20261019/StoppingPower_tuple_S-Au.csv
raw_sha256: f5c169296c7d129cf74011e89a7772448a9f6da51c681c4cd651965fee85f43f
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [31S, 32S, 15O, 16O, 17O, 18O]
methods: [stopping-power, DSAM, unit-conversion, data-coverage]
tags: [DSAM, stopping, calibration, covariance, source-independence]
---

# 电子阻止数据能约束什么，尚缺什么

## Bibliographic Record

官方[首页](https://www-nds.iaea.org/stopping/)标示版本2026-09、发布日期25Sep2026；两条实际查询为[S/Au](https://www-nds.iaea.org/stopping/tuples?ion=S&target=Au)、[O/Ta](https://www-nds.iaea.org/stopping/tuples?ion=O&target=Ta)，pair页更新时间均27Nov2023。当前版本标签、抓取日期和具体实验年代分别记录。参考数据库论文 DOI [10.1016/j.nimb.2024.165336](https://doi.org/10.1016/j.nimb.2024.165336)只作身份入口，未读其正文。

全库数据ZIP实际下载成功，SHA256 `0813d4137aa571eb8d8d48e96ed7ca3dd2b7ef10e510d627e7d01029379ba01b`，内部CSV哈希 `dacc1c57e39a8187129d9b6593e5aa91276ca317a7f0c7530869446347f9af0c`。参考文献ZIP也取得。两个pair单独下载的CSV与全库筛选行逐字段完全相等，选中392行含63实验行和329条SRIM2013模型点，绝非392次实验。全库还含其它模型，不能把全库行数当首页的实验点总数。

可复算选中CSV：[S/Au](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/stopping-S-Au-frozen.csv)、[O/Ta](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/stopping-O-Ta-frozen.csv)。S/Au CSV哈希见frontmatter；O/Ta为`da298960651436e2c0d7eb8f0bf1262b86d76f4b61a5f19454c18488eb68596b`。这些是本任务分析输入的固定副本，raw归档槽仍未填，没有覆盖原证据。

## Scope and Reading Depth

先冻结已知DSAM priming，再读首页、API/description入口、两pair全部页面与392行选中CSV字段、对应reference行；未逐行阅读全库、未读各primary全文。API schema返回403，未绕过。Ward1979/Forster1976/Hu1999的Crossref身份核查仅metadata；Ward publisher403及OpenAlex无OA候选保留，不将摘要升级为body。另定向查询N/Ta全库行，仅作Schürmann引用surrogate的readiness检查，未摄入其primary。

## Summary

当前编译确实提供可追溯的S/Au、O/Ta实验值，能限定下一次校准该找哪条原实验。它尚不能直接替换Sun的Geant4阻止模型或10/20%先验，也不能覆盖Schürmann低能15O/Ta的完整速度投影历史。原因包括电子/核阻止对象、同位素、能区、材料状态、误差与共同来源依赖。

## Experimental or Method Setup

首页定义电子阻止截面S满足`−dE/dx=nS`，并明确核阻止已扣除或可忽略。选中行均solid、能量MeV/u、质量阻止单位MeV/(mg/cm²)，含projectile isotope、target mass/atom ratio、literal percentage_error、ref/DOI。模型行的error为空，不赋0。表中error没有给出统一置信定义或点间Cov；不能仅见4就认定相互独立的Gaussian1σ。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| ISP26-1 | 官网定义电子阻止截面与−dE/dx=nS，核阻止已扣除或可忽略；不含完整核散射角/速度投影响应。 | observable-definition-and-boundary | direct-database | homepage electronic-stopping definition | true |
| ISP26-2 | 版本2026-09与两pair lastmodified2023-11-27分开；全库ZIP/refs/pairCSV实际取得，pair与全库selected行相等；392行=63实验+329SRIM模型，不据全库行数宣称实验点数。 | identity-and-reproducibility | direct-data-and-task-check | pair pages Experimental/Theoretical Data；selected CSV header | true |
| ISP26-3 | S/Au六组39实验行均32S：Am1968五行、Bt1966十六、Fs1976十、Ou1995三、Sd1975三、Wr1979二；低能Wr只有.0168/.0251MeV/u两点，.0251–.15之间无这些实验行。 | actual-energy-isotope-coverage | direct-compilation | S-Au CSV refs Am1968/Bt1966/Fs1976/Ou1995/Sd1975/Wr1979 | true |
| ISP26-4 | O/Ta四组24实验行分别17O85MeV/u、16O24.58–90.83、18O9.27–9.34、16O.1167807–.2587359；没有15O行。不能由同元素标签补同位素/低能覆盖。 | counter-coverage-and-identity | direct-compilation | O-Ta CSV refs Bi1990/Ga1987/Hak2002/Hu1999 | true |
| ISP26-5 | literalerror含3、4、25、2.5–4.5等，模型为空；无统一σ定义/Σ。Fs1976与Wr1979作者Ward/Andrews/Mitchell重叠；不同年代/DOI不认证独立校准，SRIM也可能共享用于建模的数据，当前未核其训练谱系。 | error-semantics-and-dependence | direct-input-and-readiness | CSV percentage_error；reference rows Fs1976/Wr1979 | true |
| ISP26-6 | 选中同位素匹配的实验/当前SRIM2013点插值比仅作描述：Fs1976约.977–1.044，Wr1979约1.002–1.027，Bt1966约.962–1.928；不合并拟合或认旧实验/模型出错。初程序把17/18O也比16O模型，终稿已剔除并保留原失败对象。 | task-ratio-exercise-and-self-correction | derived | stopping-coverage-result pairs；stopping-analysis-correction | true |
| ISP26-7 | 用所列Au质量/atom比196.96657与精确SI N_A，Wr1979低点.58MeV/(mg/cm²)转换约189.701×10⁻¹⁵eV cm²/atom；不假设density或变长度停止程。 | task-unit-reconstruction | derived-from-compiled-input | S-Au CSV Wr1979 E.0168；stopping-coverage-result unit_example | true |
| ISP26-8 | Ep.318MeV与15u质量近似给capture后、减速前起点E/A≈.00142362MeV/u；把声明的总光子能量8MeV宽松上界加到反冲的宽松三角上界也仅.00250874。最低O/Ta实验点仍高约46.55倍；仅为覆盖诊断，不是实际cascade/碰撞重放。 | conditional-kinematic-coverage-bound | task-model | SCH08-2；stopping-coverage-result O_Ta_coverage_proxy | true |
| ISP26-9 | Sun原文的sp中心为Geant4所用database，10/20%为作者明确Gaussian1σ选择；此IAEA SRIM2013曲线不是其actualproducer。Schürmann使用SRIM2006及v(t)cosψ，当前电子表不替其多项式/Σ；N/Ta selected仅14N点也未恢复其Bister15N原输入。 | matched-response-readiness | primary-companion-and-boundary | SUN23-6；SCH08-9；N-Ta targeted CSV query | true |

## Analytical Reconstruction and Self-Audit

| pair / ref | 实验行数 | isotope | E/A范围 MeV/u | literal error % |
| --- | --- | --- | --- | --- |
| S/Au Am1968 | 5 | 32 | .625–1.25 | 4 |
| S/Au Bt1966 | 16 | 32 | .15725–.89226 | 25 |
| S/Au Fs1976 | 10 | 32 | .15–2.5 | 4 |
| S/Au Ou1995 | 3 | 32 | 1.669–1.885 | 3 |
| S/Au Sd1975 | 3 | 32 | .2848–.98834 | 2.5–4.5 |
| S/Au Wr1979 | 2 | 32 | .0168–.0251 | 4 |
| O/Ta Bi1990 | 1 | 17 | 85 | 2 |
| O/Ta Ga1987 | 8 | 16 | 24.58–90.83 | 1.6/2.3/2.5 |
| O/Ta Hak2002 | 3 | 18 | 9.27–9.34 | 7 |
| O/Ta Hu1999 | 12 | 16 | .1167807–.2587359 | 6 |

[程序](../../system/scripts/day17_stopping_database_coverage.py)、[合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/stopping-coverage-contract.json)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/stopping-coverage-result.json)逐一锁定CSV哈希/单位/role。模型只在相邻点内插，不外推；log–log插值为敏感性比较，不称独立软件验证。32S数据与32S模型、16O数据与16O模型才列比值；17/18O数值保存但不无声套16O模型。

质量阻止转截面：`S15=S_mass×A_target×10^24/N_A`，这里S15以10⁻¹⁵eV cm²/atom表示。初动量近似`p=sqrt(2m_p E_p)`，`(E/A)_0=p²/(2·15u·15)`；宽松光子界把p换为p+8MeV/c（覆盖7.556MeV激发加初始动能），忽略细小质量修正/热运动，是声明的覆盖控制。它不计算F(τ)、新τ或先验的后验校准。

## Competing Interpretations and Limitations

- 旧点与SRIM比值不同可能涉及原实验靶厚度/核阻止扣除/转换及共同模型输入。没有primarybody，不以一个描述性比值裁决。
- 32S在固定E/u与31S近似同速仍不是已经认证的同位素/charge-state/target transfer；更不能把高能16O表迁给低能15O。
- 原percentage_error不提供共享尺度/点间Cov，不能按行数压缩系统误差；shared-author也不证明一定共用同一event。
- IAEA电子表不足以替DSAM所需的`v(t)·n`、角散射、implantation材料和feeding。需matching原输入再判断constant sp先验是否合适。

## Knowledge Impact and Learning Decision

`supports`有源停止本领候选与可复算单位/能区清单；`limits`直接把编译误差或SRIM比值升级为Sun sp先验/Schürmann响应；`revises`以同元素、同DOI数量或下载行数替代匹配与独立性的做法。没有新实验τ/B/δ/CI。新增claims全needs_review，Day18仍只是Day17窗口内的无学分预习。

## Extracted Pages

[[doppler-shift-attenuation-method]]、[[lifetime-strength-audit-165tm-136nd]]、[[sun-2023-bayesian-dsam-31s]]、[[schuermann-2008-15o-6792-dsam]]。
