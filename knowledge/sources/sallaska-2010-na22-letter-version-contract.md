---
type: source
title: "Sallaska2010：Letter版本、Lab/CM公式与未得勘误正文"
title_original: "Direct measurements of 22Na(p,gamma)23Mg resonances and consequences for 22Na production in classical novae"
aliases: [Sallaska2010 Na22 Letter, S10 version frame contract]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: read
authors: [A. L. Sallaska, C. Wrede, A. García, et al.]
year: 2010
journal: Physical Review Letters
volume: 105
pages: 152501
doi: 10.1103/PhysRevLett.105.152501
citation_key: ""
canonical_source: "Sallaska PRL105152501 arxiv1008.4170v2 and targetedv1; officialerratum105209901 metadataonly"
source_url: https://arxiv.org/abs/1008.4170v2
raw_file: raw/papers/gpt/learning-daily/20261020-DAY18-dsam-lifetime-strength/sallaska-2010-letter-arxiv-v2.pdf
raw_sha256: e004080c48c26d3de6f6b611ddb7d121b655e9fa96477f9956e1c26c5ebbe090
raw_storage_status: verified-raw-archive
raw_archive_verified_at: 2026-10-23
nuclei: [22Na, 23Mg]
reactions: [22Na(p,gamma)23Mg]
methods: [resonance-strength, gamma-spectroscopy, frame-transformation]
tags: [version, reference-lineage, covariance, lifetime-companion]
---

# 版本相同表值不能代替分析程序或勘误正文

## Bibliographic Record

[PRL105152501 DOI](https://doi.org/10.1103/PhysRevLett.105.152501)的实际原件为[arXiv1008.4170v2](https://arxiv.org/abs/1008.4170v2)，24Sep2010，四页。另取得24Aug2010的v1作定向版本比较。v2正文May2018、v1正文May2019及生成metadata来自再生PDF，官方两版tex均`\date{\today}`，不计新采集。与[[sallaska-2011-na22-absolute-resonance-strength]]为同研究短报/详细文链。

另核[正式Erratum DOI10.1103/PhysRevLett.105.209901](https://doi.org/10.1103/PhysRevLett.105.209901)，Crossref出版9Nov2010；**未取得正文**。arXiv关联此DOI不表示Sep版已包含Nov正式更正。不得从本文公式差异猜测勘误更正对象。

[两版PDF/hash](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/sallaska2010-original-versions-download.json)、[源码包/成员hash](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/sallaska2010-versions-source-identity.json)、[勘误readiness](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/sallaska2010-erratum-primary-readiness.json)。缓存`tmp/day17-sallaska2010/`，raw不改。

## Scope and Reading Depth

承认2011原件和评价priming后冻结回忆，实际读v2四页完整主线/参考文献、Eq1、TableI、Fig1六panels/Fig2三panels；全页视觉核、PDF2公式放大。v1仅定向source/text/table/figure比较，不称另一次独立盲读；没有VoR、正式勘误body或原producer。源码与图片hash用于版本证据，不把同一图的重复出版计独立数据。

## Summary

v1/v2的Eq1、TableI源码相同，rate figure EPS逐字同；v2新增分支比较句、更新详细文引用，谱图EPS发生标签图形变化。2011保持四有限强度中心/误差，补更详细的输入链。Letter的λlab标签与详细文CM定义须经frame桥明确；缺失实际分析程序与勘误正文时，只能保存文字/推导边界。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| S10-1 | 原v2四页完整主线/1式/1表/2图全读，v1为定向版本比较；两版tex date-today使PDF2018/2019不是新实验。2011详细文自引此短报，采集不重复计数。 | identity-version-and-dependence | direct-original | v2 PDF1–4；both source date；S11-1 | true |
| S10-2 | 两版Eq1/TableI源码完全相同，reactionrate EPS hash同；v2新增“branches roughly agree”句/详细文引用状态，谱图EPS变。没有把更新日期或rate图重印当独立强度验证。 | actual-source-version-comparison | direct-source-diff | version-comparison-scope；frame-exercise version fields | true |
| S10-3 | LetterEq1字面为2π²λlab²(m+M)/M NTρb omega，prose称proton reduced wavelength；2011Eq4同factor但明确定义CM reduced wavelength。此字面差异真实存在，实际producer如何用λ未得。 | literal-equation-frame-boundary | direct-original | v2 PDF2 Eq1；source label main；S11 PDF2 Eq4 | true |
| S10-4 | 声明NR窄孤立BW及resonance处冻结λ，CM截面积分为2π²λcm²omega，Lab能量积分另乘r=(m+M)/M；λcm²=r²λlab²，故纯Lab写法为λlab²r³。是条件推导，不是论文实际实现重放。 | conditional-frame-derivation | task-derivation | frame-exercise NR_declared_control | true |
| S10-5 | 质量数m1/M22控制给r²1.092975，若其它量相同而误用字面Lab系数，推强度相差此因子。不是实际质量输入/原分析错误或实验重标，也不能解释2.4–3.2倍争议。 | declared-numerical-control | task-model | frame-exercise NR_declared_control | true |
| S10-6 | TableI有限2135.7(+1.6,−.9)、28839(8)、454166(22)、610591(+103,−74)与2011一致；213.4(1.4)/288.0(1.1)质子能量与后详细213.5/288.1保版本舍入/分析差，不能把同结果算独立测量或据.1keV判新态。 | actual-table-and-version | direct-original-and-companion | v2 PDF3 TableI；S11 TablesII/IV | true |
| S10-7 | 232上限脚注g字面将7350配66.4%、7801配30%，而2011TableIII为ground7802配66.4、7351配29.9；保各版文字/分支对象。正式erratum未读，不把此差异宣称其更正内容或改raw。 | branch-label-version-boundary | direct-original-comparison | v2 PDF3 TableI footnoteg；S11 PDF16 TableIII | true |
| S10-8 | Letter明确<约4MeVγ因radioactive背景不能测，有限强度/upper都需分支inventory；weakshape有stopping比伸缩，213还补10(5)%尾，与2011详细合同同源。不能从短报“absolute”读成无响应/无停止/完整观测。 | response-and-shared-input-boundary | direct-original | v2 PDF2–3 Eq1 paragraphs/TableI | true |
| S10-9 | arXiv标注正式erratum DOI，准确metadata出版9Nov2010；其body在APS401/403、ADS30s超时和当前Scholar/公开发现路线未得。不能据关联DOI/标题猜科学更正或把Sepv2当正式勘误。 | actual-access-readiness | metadata-and-failure-boundary | erratum-exact-metadata；erratum-primary-readiness | true |
| S10-10 | 短报关于22Na产额下降2–3再由SHIVA混合稀释约25%是作者模型/后续沟通，不是天文gamma检出、独立寿命或自旋测量；2011给具体hydrodynamic表仍同模型链。 | model-versus-experiment | direct-author-model | v2 PDF3–4 Fig2/modelparagraph；S11 TableVI | true |

## Analytical Reconstruction and Self-Audit

[推导前合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/sallaska2010-frame-exercise-before.md)、[hash合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/sallaska2010-frame-exercise-contract.json)、[程序](../../system/scripts/day17_sallaska2010_frame_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/sallaska2010-frame-exercise-result.json)。Lorentz积分用独立数值quad核π；它只验证声明推导的归一，不增加实验精度或认证完整BW/能变λ/producer。

采用`σ(Ecm)=πλcm² g ΓpΓγ/[(Ecm−Er)²+Γ²/4]`并定义`omega=g ΓpΓγ/Γ`，全数学实轴窄峰积分给`2π²λcm² omega`；因`dElab=r dEcm`，纯Lab波长应伴`r³`。物理阈值/能变partial widths、有限扫描/靶退化与效率另在原分析合同，不由这个局部公式消除。

## Competing Interpretations and Limitations

文字公式可能是标签/印刷问题，也可能只是采用了未写出的λ定义；缺实际producer与正式erratum，无法选择。两版TableI未变并不证明producer正确，也不证明其用了字面错误公式。本session没有按9.3%修改任何实测值或据之宣布历史争议解决。

Source diff表明版本变化局部，但谱图EPS的vector差不自动认证全部原event或每个点未变；未将图形hash相同升级成新的独立实验。正式erratum访问失败只关闭当前获取路线，不声称全网无正文或要求用户代取。

## Knowledge Impact and Learning Decision

`supports`按源版本/公式frame/数据依赖逐项匹配；`limits`metadataerratum、文字系数和重复表值对实际数据的保证。新增claim全needs_review，无human-reviewed或新实验强度/寿命/自旋/置信区间。Day17原窗口中仅Day18无学分预习。

## Extracted Pages

[[sallaska-2011-na22-absolute-resonance-strength]]、[[nndc-2021-mg23-lifetime-strength-reference]]、[[lifetime-strength-audit-165tm-136nd]]、[[doppler-shift-attenuation-method]]。
