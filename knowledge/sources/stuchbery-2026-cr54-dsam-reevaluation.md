---
type: source
title: "Stuchbery2026：54Cr DSAM旧数据重分析与停止模型边界"
aliases: [Stuchbery 2026 Cr54 DSAM, arxiv2608.28047v2]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: experimental-reanalysis-and-model
reading_depth: deep-read
title_original: "Doppler-shift attenuation method lifetimes in 54Cr: A reevaluation"
authors: [A. E. Stuchbery]
journal: Physical Review C
year: 2026
volume: 114
issue: 3
pages: "034322"
doi: 10.1103/gm4m-8wyn
citation_key: ""
canonical_source: https://doi.org/10.1103/gm4m-8wyn
raw_file: raw/papers/2026_Stuchbery_Cr54_Dsam_reevaluation.pdf
raw_sha256: 918ba5cb8a663bf57aedfef50f8106774a539f45454066079854bf425cfe1440
nuclei: [54Cr, 58Fe, 48Ca]
reactions: [51V(alpha,p-gamma)54Cr]
methods: [doppler-shift-attenuation-method, centroid-shift, stopping-power-reanalysis]
models: [shell-model, GXPF1A]
tags: [DSAM, 54Cr, stopping-power, lifetime, reanalysis, model-dependent-strength]
---

# 54Cr：停止曲线更新不是一项统一寿命百分数

## Bibliographic Record

A. E. Stuchbery，*Phys. Rev. C* **114**(3),034322(2026)，DOI[10.1103/gm4m-8wyn](https://doi.org/10.1103/gm4m-8wyn)。Crossref实际给出版日2026-09-16及article-number034322；本次实际原读为[arXiv2608.28047v2](https://arxiv.org/abs/2608.28047v2)，上传16Sep，PDF dated17Sep2026，11页。**未取得VoR正文，不将arXiv与期刊metadata当两份独立证据。**

原PDF实际保存在`tmp/day18-20261020/stuchbery54cr/stuchbery54cr-v2.pdf`，SHA256见frontmatter。上方raw_file是未写入的归档槽；本次保护raw/PLAN/Bib，raw归档deferred。官方arXiv源码包hash为`51d117309a0b38c3c23191a23243c04089f0d6ebae7c5608579832ee5481ad26`；九成员为tex/bib/bbl/README及五图，不含本文重建的DSAM分析程序或原logbook。这个有限包清单不是穷尽所有合法公开代码路线。

## Scope and Reading Depth

独立Day18先冻结primed回忆并完成Jensen/MU08首交付；之后以新候选问题取得本原件。此次完整原读11页主线/参考，五图(Figs1–5)、五表(TablesI–V)、五式(Eqs1–5)；PDF2–10关键图/表/式视觉核。Ta15条和Mo8条printed F输入另逐行复算；不是全部原谱/代码/Σ重建。

未读原1980测量论文、Nathan1978、Lieb1988/Kuronen1992/Devlin1999的正文，也未运行作者OCR重建的原DSAM程序或NuShellX。本文对这些工作的论述保留为本作者报告/二级谱系；不用参考文献列表预填原始阅读。

## Paper Question and Scientific Motivation

检查早期采用LSS停止功率的54Cr DSAM寿命，是否受更新电子停止功率影响，进而改变E2强度、壳模型比较和部分自旋候选。本文是1980数据的重分析；作者明确有原分析logbook，而不是又采集一次同样事件。

## Summary

本次实际原读的2026arxivv2重新分析1980的54Cr双靶DSAM数据。主要改变电子停止曲线，核停止和散射仍需分开处理，所得寿命变化依能级而异。新强度有助壳模型比较，但部分“experimental”B使用模型δ，所提Jπ仍受DCO反证限制。旧data、新程序和派生τ/B不是独立重复实验；本任务未取得作者实际分析代码或logbook。

## Experimental or Theoretical Setup

原测量为10MeVα+51V(α,pγ)54Cr，半靶/全靶相隔15.28cm，同一Ge(Li)看约26°/154°的双向shift；两SSB接受153°–174°质子。作者修正文献抄录的粒子开角和“β=.0068”角色：初始平均β约.0078，.0068是投影平均。能量分组的proton-γ符合用于选择直接布居，和Jensen/MU08的多γbelowgate不是同一种feeding控制。

靶为V/O化合物，RBS比V:O=1:(1.4±.1)，Ta/Mo两backing。PDF2靶厚单位字面印为µm/cm²；未自行改成µg/cm²或用它重建实际材料。25µmTa foil是粒子探测器挡α的另一对象，不能借来补靶厚。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| SC26-1 | 期刊身份为PRC114034322/DOIgm4m-8wyn，实际body为2026arxivv2十一页；原源码包九成员只给文稿/参考/五图，未提供本次DSAM重建程序或logbook。实际全文阅读不等原程序执行或VoRbody核验。 | identity-version-and-input-scope | direct-metadata-and-original | arxiv2608.28047v2首页/abs；Crossref DOI记录；官方src成员清单 | true |
| SC26-2 | 本文重用1980数据/原logbook；OCR原listing重建后先重现旧分析，再改停止曲线。修正energyloss/平均散射角的两处原代码错误及逐态F曲线均被作者报告为对旧寿命影响小，主要变化来自新stopping；本任务未独立运行该原程序。 | author-reported-reanalysis-procedure | direct-report-and-boundary | PDF4 Eq5后四段 | true |
| SC26-3 | 双靶同Ge/两proton-gates给up/down质心差；β=.0078与投影.0068分开，粒子开角153–174°而非旧抄录。作者称选直接布居的proton组排除上级feeding；该条件不自动迁移到其它reaction/γgate。 | source-experimental-selection | direct-report | PDF2 Fig1/SecII/Eqs1–2 | true |
| SC26-4 | Eq1/5的F由实测ΔEγ除E0Δ〈βcosθ〉；后者要反应运动学/接受角，Eq3省略空间平均和散射仅为简式。Eq4把时间、速度、距离与totalstop相连，核停止还影响散射方向。故只改电子停止不等整个velocity/scattering生成元统一scale。 | source-forward-model-and-inference | direct-and-derived | PDF2 Eq1/2；PDF3 Eq3；PDF4 Eq4/5及邻段 | true |
| SC26-5 | Fig2/SecIII的54Cr/Ta适用能域中SRIM电子停止约为LSS的60%，核停止接近；约10fs后核停止占主导。作者报告寿命通常增16–27%，取决于τ/两项贡献；不是任意核/材料的一项统一修正或精确共模关系。 | author-stopping-model-result | direct-and-boundary | PDF4 Fig2；PDF5 SecIII；PDF10–11 Summary | true |
| SC26-6 | TablesI–II寿命主误差来自ΔEγ；末两列分别展示电子±5%与核±10%变化效应，不是各态独立原Σ。TableIII用V.AveLib WeightedAverage合Ta/Mo并含stop估计；Mo旧run被加速器故障截短，原两backing未能充分检验LSS。 | reported-uncertainty-and-combination | direct-report | PDF3 TableIcaption；PDF5 TablesII–III/footnotes；PDF6 TableIII后段 | true |
| SC26-7 | TableIV旧Ref9列为原Ta结果，而Revised采用TableIII的Ta/Mo组合；例如4+1旧Ta3.5ps、新Ta4.2ps、组合3.8ps。19.3–26.8%的本次七行Ta中心变化与8.57%的3.8/3.5混合角色对照必须分开，不将所有比值叫stopping-only或独立显著性。 | source-input-and-task-role-audit | direct-and-derived | PDF3 TableI；PDF5 TableIII；PDF6 TableIVcaption与对应行 | true |
| SC26-8 | 作者指Nathan1978另一DSAM也用LSS/Ta，不能以其数值相合消共同模型风险；Kuronen1992是Lieb1988同GRID测量的再分析。2.620态新DSAM.185(.025)与GRID再分析.122(.022)仍不合，作者偏好DSAM的灵敏域理由是解释，不把全部comparisons写成一致。 | reported-lineage-and-counterevidence | direct-report-of-comparison | PDF6 TableIV/SecIVA；PDF7首三段 | true |
| SC26-9 | TableV的4043→3222 B(E2)88项明确用模型δ=+.05，4043→1824及所议(6)+身份也依模型/branch输入；作者承认新6+建议与原DCO相反，需新spectroscopy。3.786的5+也为基于longτ与壳模型的tentative建议，不是新实测Jπ。 | model-conditioned-extraction-and-counterevidence | direct-and-boundary | PDF8 TableVfootnoted/SecIVB1；PDF9前半 | true |
| SC26-10 | SM1/SM2共用GXPF1A/fullfp和波函数框架，只换effectivecharges(1.5,.5)到(1.3,.45)；径向HO常数也影响B，本文给45/A^(1/3)−25/A^(2/3)。54Cr偏好新charges而58Fe对照偏好旧值，作者称两例不足普遍定论；0+缺态与模型空间缺陷为竞争解释。 | source-model-scope-and-counterevidence | direct-model-report | PDF7–8 TableV；PDF9–10 0+讨论/Fig5 | true |
| SC26-11 | 新复算23条Ta/Mo printed输入按Eq5得F中心最大残差.000769；在另设独立F误差条件下，两条3160线加权给Ta.332181/.023122、Mo.380722/.050897，与printed均值相近但不认证原estimator/Σ。保留原F=1.002不clip观测，不据打印残差更正实验。 | task-published-input-arithmetic | derived-and-boundary | PDF3 TableI、PDF5 TableII/平均F；新stuchbery54cr-input-result-001 | true |
| SC26-12 | 固定绝对photonprobability/τ/E的声明chart中，δ=.05→.025/.10令该E2分量分别乘.250468/3.970297；88对应22.041/349.386e²fm4只为条件控制。没有原branch/ICC/δΣ，不能当新实验B/CI或以同模型δ生成的B反过来独立验证模型。 | task-mixing-sensitivity-and-dependency | derived-and-boundary | PDF8 TableVfootnoted；PDF8–9 SecIVB1；新inputcontract/result | true |

## Analytical Reconstruction and Self-Audit

观测层是双靶的质心差和粒子组选择，F分母也有运动学模型；总meanτ再经材料/停止/散射F曲线得到。换停止库不要求重新测量ΔEγ，但也不产生独立新data。两backing是原采集的不同子集；再分析后的同源数据与独立GRID必须按原measurement谱系分开。

本次[合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/stuchbery54cr-input-contract-001.json)、[新程序](../../system/scripts/day18_cr54_published_input_audit.py)/[结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/stuchbery54cr-input-result-001.json)给30项检查：23F行、同母态候选均值、七行Ta/adopted角色、δ分量和径向scale。检查数不等新测量或原profile重放。

同γ-only/pγ1/pureE2控制给4+1→2+1 B≈227.004、6+1→4+1 B≈230.762e²fm4，对原228/233的打印中心差分别−.437%/−.960%；不借匹配反认原支路/ICC。固定无量纲HO波函数时B∝ω^−2，A54的两ω约10.1556/10.8472MeV，条件B比.876545；这不重现Seidlitz的原NuShellX计算，本文的“about11%”也不能由这个控制单独裁错。

## Competing Interpretations and Limitations

- 更换停止库揭示旧systematic可被低估，但SRIM与模型贴合并非完全独立的停止功率实验校准。
- 同data新code/新τ/新B不作为三项独立证据；原sourcecode/logbook/计数/response/Σ未取得。
- 对4043态，“experimental”B部分使用候选模型δ，不能反过来当模型无条件外部验证；新Jπ保tentative并保DCO反证。
- 两材料结果相合不等全部共同停止/几何风险消除；本文另DSAM和GRID比较有共同模型及同data重分析层。
- 原文µm/cm²单位、GXPF1A/GXFP1A/GX1PFA等少数拼写按原位置保留，不自行修原件/推更正通知。

## Knowledge Impact and Learning Decision

`supports`[[doppler-shift-attenuation-method]]中只在声明整体生成元scale域讨论clock对称；`limits`把电子停止库切换简化成全部τ同一乘数。真实例子补到[[lifetime-strength-audit-165tm-136nd]]：partialrate、branch/δ和模型判别需保持依赖链。当前source有新原件/locator及定量反证，值得长期保存；不新增54Cr核素页以免只复制本source。

## Related Knowledge and Project Relations

[[jensen-2001-165tm-h9-2-configuration]]与[[mukhopadhyay-2008-136nd-transition-rates]]是主Day18案例，本source只提供不同核/反应的停止与模型依赖对照，不迁其数值。[[sun-2023-bayesian-dsam-31s]]的prior/模型扣除同样要求输入谱系；三者不是本54Cr的独立寿命复测。

## Extracted Pages

- 方法：[[doppler-shift-attenuation-method]]，新增电子/核停止变化与全生成元时钟缩放的区别。
- 可复用审计：[[lifetime-strength-audit-165tm-136nd]]的54Cr段，保Ta/组合、F/τ/B及模型δ依赖。
- 来源导航：[[index]]。核素与GXPF1A独立模型页未创建；当前证据由本source承载，未把本次模型比较扩写为普遍有效电荷结论。

## Human Review Triage

P0 self-audit：SC26-5不迁停止百分数、SC26-7不混Ta与组合结果、SC26-9/12保模型δ和DCO反证。P1：SC26-8的其它measurement谱系来自本文而非原件，SC26-1的v2与VoR/公开code边界。所有claim为needs_review，source unreviewed；Codex自审不写human-reviewed。

## Reproducibility and Evidence Gaps

原PDF/arxivabs/src hash、Crossref metadata和源表合同位于本Day18 run；本地raw槽未填，protectedraw/Bib未写。真实重拟合还需OCR重建代码、旧listing/logbook、逐靶proton-gatedcentroids与calibration/接受/材料/Σ、SRIM实际版本表及NuShellX波函数/径向参数。当前只有已发表参数审计和公开原文，不生成实验τ/δ/Jπ/CI。
