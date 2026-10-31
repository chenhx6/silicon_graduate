---
type: source
title: "TAMU2006–2007原报告：23Al γ参考的采集谱系与分母边界"
title_original: "Selected 23Al reports, Cyclotron Institute Progress in Research 2005–2006 and 2006–2007"
aliases: [TAMU Al23 gamma reports, TA07 gamma reference lineage]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: institutional-research-reports
reading_depth: read
authors: [Y. Zhai, L. Trache, V. E. Iacob, et al.]
year: 2007
citation_key: ""
canonical_source: "TAMU2005–2006 I5–I10 plus2006–2007 I27–I28 selectedcompleteauthoredreports"
source_url: https://cyclotron.tamu.edu/publications/
raw_file: raw/reports/gpt/learning-daily/20261020-DAY18-dsam-lifetime-strength/cyclotron-progress2006.pdf
raw_sha256: e0602d7608a5307c917eb61426e87b7987d9cf777bac7a4930bf3d43ce531f48
raw_storage_status: verified-raw-archive
raw_archive_verified_at: 2026-10-23
nuclei: [23Al, 23Mg, 22Na]
reactions: [24Mg(p,2n)23Al, 23Al-beta-gamma-decay]
methods: [gamma-spectroscopy, absolute-normalization, source-lineage]
tags: [reference, Compton-background, lifetime-strength, covariance]
---

# 后续采集与同一source链的重复引用需要分别记录

## Bibliographic Record

实际读三篇独立署名的机构贡献，均非Iacob2006期刊正文或Zhai2007学位论文：

| 对象 | 署名/标题 | 原定位 |
| --- | --- | --- |
| 2005–2006结构报告 | Y. Zhai等，The Structure of 23Al and the Consequences on the 22Mg(p,γ)23Al Stellar Reaction Rate | annual PDF17–19 / I-5–I-7 |
| 2005–2006共振报告 | L. Trache等，Decay of 23Al and Resonances in 22Na(p,γ)23Mg at Astrophysically Relevant Energies | annual PDF20–22 / I-8–I-10 |
| 2006–2007后续报告 | Y. Zhai等，Further studies of β-decay of proton-rich nucleus 23Al | 单独PDF1–2 / I-27–I-28 |

[原年报PDF](https://cyclotron.tamu.edu/progress-reports/2005-2006/cyclotron_progress2006.pdf)共205页，缓存`tmp/day17-iacob2006/progress2006.pdf`，hash见frontmatter；[后续两页原PDF](https://cyclotron.tamu.edu/progress-reports/2006-2007/1%20Nuclear%20Structure,%20%20Fundamental%20Interactions,%20and%20Astrophysics/I_27_further%20studies%20of%20betal.pdf) SHA256`9796fab52a78e5f3304fed9d6d34469e8cd67c5e60911dd187c10df8652facbf`。后者PDFmetadata错误沿用10B反应题名，实际页标题/作者/正文/引用均为23Al；不以模板metadata冒新科学对象，也不覆盖raw。

## Scope and Reading Depth

先冻来源前/选页前回忆，再读上述三篇各自完整主线/全部图/refs，共8页，全部视觉核。未读205页其它内容（尤其未开启I-11寿命专项），不称年报全文。2006期刊[DOI10.1103/PhysRevC.74.045810](https://doi.org/10.1103/PhysRevC.74.045810)原body当前仍未得，APS401/403、TAMUrepository403、arXiv exactDOI0/作者查询只另篇会议文、HAL与部分lab页TLS失败；来源发现失败均留档。[期刊readiness](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/iacob2006-primary-readiness-boundary.json)。

## Summary

原报告明确区分2005年的采集及2006年Sep/Nov两次后续采集：后者改进高能统计、24Al能量/效率标定并加入BGO Compton屏蔽。不能将所有论文/thesis/进展报告一概认同一批事件；也不能将新采集自动当完全独立response/reference。三报告给γ支路比例和旧强度推断链，却仍未提供当前FR20 adopted绝对γ馈入3.95(.37)%的完整原表/Σ。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| TA07-1 | 实际三篇机构报告完整8页/图refs已读，年报205页其它内容未读；IacobPRC/Zhai thesis未取得。机构报告为作者primary但不是它们的全文替身或独立重复实验。 | identity-and-reading-scope | direct-report | I5–I10/I27–I28；reading-scope | true |
| TA07-2 | 结构报告2005样品用48AMeV24Mg/MARS约4000pps、tape1s收集/177ms转移/3.2s计数，HPGe4.9cm与βBC4043mm；24Alγ用于4–9MeV标定，高能约20h。不是后续2s计数或不同source可共用效率。 | actual-setup-and-normalization-context | direct-report | I-5；I-6 | true |
| TA07-3 | I-6把BGO与更多高能统计列未来计划；I-27/28明确2006Sep/Nov新实验已做，Sep>4MeV统计约2倍、Nov加BGO。相同组/同技术不等同一eventdataset，计划与结果按原时点分列。 | actual-dataset-version-bridge | direct-report | I-6 futureplan；I-27/28 | true |
| TA07-4 | 后续报告48AMeV/MARS/tape、1s收集/177ms转移/2s计数，与2005结构报告3.2s计数不同；还重测24Al高能能量/效率。新run不自动独立于同校准知识或全旧数据。 | changed-run-and-shared-reference | direct-report | I-27/28 | true |
| TA07-5 | 共振报告以ft2042(120)s接近所引Fermi2048(.5)s识别7803IAS，另7787强β馈入；γ/ft支持作者identity，原ft表/绝对馈入误差构造未给完整，不能据一幅scheme复原3.95。 | direct-result-and-readiness | reported-result | I-8/I-9 Fig1 | true |
| TA07-6 | 共振报告IAS三γ相对100/45(5)/5.5(2.1)，7787三γ相对3.8(2.5)/100/20(5)，是各母态光子归一，非绝对β馈入或pγ总branch。两组不可无母态迁用。 | actual-photon-ratio-roles | direct-report | I-9 Fig1/prose | true |
| TA07-7 | 7787三γ名义归一给3.069/80.775/16.155%，与S11转列Iacob旧参考3.1/80.8/16.2打印近合；仍不提供absoluteI451/throughstate3.95或fullCov。 | actual-table-crosscheck | task-derivation | exercise three_listed_photon_fractions；S11 TableIII | true |
| TA07-8 | 旧报告r=Γp/Γγ=.080(.017)来自Tighe相对p与Peräjärvi高能pγ参考的混合，非新直接测Bp；换为Bp=r/(1+r)=.074074，不能将.080当Γp/Γ。 | mixed-source-and-denominator | direct-report-and-reconstruction | I-10；exercise daughter_Bp_from_r | true |
| TA07-9 | I-10字面称T1/2=10(3)fs而引用J04；配mean10与r/J7/2，本任务得omega2.5797近报2.6，若按literalhalf10则1.7881。只保存label/条件算术不闭合，不改原J04mean、不宣称正式勘误/新寿命。 | literal-time-label-and-conditional-check | direct-label-and-task-derivation | I-10；J04-7；exercise omega fields | true |
| TA07-10 | 作者把强p/近IAS的mixing/γpattern用于偏好7/2，仍是含动力学/旧p输入的解释；与SA11/当前Adopted候选分列，不能作纯选择律或新的独立spin测定。 | author-spin-interpretation | direct-author-interpretation | I-9；SA11-9；M23-4 | true |
| TA07-11 | 后续BGO图显示高能γ背景改善并识别弱线，作者称confirm旧βγbranches但未列完整absolute数值/误差/Cov；效果不等零Compton、通用Q或独立绝对标定。 | Compton-companion-and-scope | direct-and-author-summary | I-28 Fig1/prose | true |
| TA07-12 | 这些报告收窄run/version/相对γ角色，仍未闭合FR20的3.95(.37)%绝对γ馈入与SA11打印两支和；缺原PRC/thesis/fullinventory/Σ。应保存readiness而不是用报告比例倒填新绝对数值。 | verified-boundary-and-next-input | synthesis-with-source-boundary | TA07-2/3/6/7；FR20-15 | true |

## Analytical Reconstruction and Self-Audit

[量化前合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/tamu2006-2007-report-exercise-before.md)、[输入hash](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/tamu2006-2007-report-exercise-contract.json)、[程序](../../system/scripts/day17_tamu_report_ratio_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/tamu2006-2007-report-exercise-result.json)。r→Bp的局部尺度仅r误差条件传播，未与旧τ/γ/归一Σ组成新实验CI。

一个声称“确认旧支路”的后续run可能共用旧效率/强度基准，还可能新增event；两层必须同时保留。确认相对γ比和确认绝对馈入不是同一个交付。后续查询应返回原absolutebranch表及定义，不能由图上能量标签/日志日期或publicationyear推断。

## Competing Interpretations and Limitations

Iacob2006原件和Zhai2007thesis均未取得，不能从TAMU进展报告补其原表、未舍入数字、误差或共同Cov。r与lifetime标签的字面问题不自动解释其它实验分歧，更不能作为当下推荐branch输入。原p实验/数据未独立查，不把作者归因旧peak或mixing升级成事实裁决。

## Knowledge Impact and Learning Decision

`supports`实际run谱系/高能Compton背景companion/母态分开的光子比例；`revises`报告转载=同event、或相对比=绝对branch；`limits`当前获取路线对3.95分母和完整联合CI的保证。新claim均needs_review，无human-reviewed或新实验τ/branch/spin。仍为Day17原窗口Day18无学分知识preview。

## Extracted Pages

[[friedman-2020-gadget-al23-proton-branch]]、[[saastamoinen-2011-thesis-al23-proton-response]]、[[sallaska-2011-na22-absolute-resonance-strength]]、[[lifetime-strength-audit-165tm-136nd]]、[[linear-polarization-asymmetry]]。
