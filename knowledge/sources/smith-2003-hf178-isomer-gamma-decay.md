---
type: source
title: "Smith2003：178m2Hf直接M4/E5衰变、E3内转换主支与阻退度归一"
aliases: [Smith2003 Hf178m2 gamma decay, UCRL-JRNL-200315]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: read
title_original: "Gamma rays emitted in the decay of 31-yr 178m2Hf"
authors: [M. B. Smith, P. M. Walker, G. C. Ball, J. J. Carroll, P. E. Garrett, G. Hackman, R. Propri, F. Sarazin, H. C. Scraggs]
year: 2003
journal: Physical Review C
volume: "68"
pages: "031302"
doi: "10.1103/PhysRevC.68.031302"
citation_key: smith_2003_Gamma178m2Hf
canonical_source: "https://doi.org/10.1103/PhysRevC.68.031302"
source_url: "https://digital.library.unt.edu/ark%3A/67531/metadc1413376/m2/1/high_res_d/15013782.pdf"
raw_file: "raw/papers/day27-20261030/smith-2003-hf178-isomer-gamma-decay.pdf"
raw_sha256: "9d326f4ff38af434b8d299b293d1da6da2b33fd412435eb56584cf010ecccb11"
raw_storage_status: reserved-unpopulated-manuscript-staging-only
public_staging_manifest: "outputs/literature-acquisition/20261030-day27-smith2003-hf178.json"
analysis_status: public-staging-manuscript-visually-read
nuclei: [178Hf, 172Hf, 172Lu]
reactions: [isomeric-decay]
experiments: [TRIUMF-ISAC-8pi]
models: [K-forbidden-decay, two-band-mixing]
observables: [gamma-energy, relative-gamma-intensity, multipolarity, reduced-hindrance]
methods: [gamma-gamma-coincidence, absorber-control, conversion-electron-comparison]
tags: [k-isomer, parity, internal-conversion, radiative-partial-half-life, high-multipolarity, Day27]
---

# 178m2Hf直接γ衰变与支路归一

## Bibliographic Record

Smith等，Physical Review C **68**, 031302（2003），DOI见frontmatter。精确Crossref端点核对发表日期为2003-09-17；本轮读取的是UNT公开保存的2003-06-25作者稿UCRL-JRNL-200315，不声称逐字核最终期刊版。获取件为PDF、505873字节、7页：封面/声明2页及正文5页，SHA-256见frontmatter。

PDF实际在 `tmp/day27-k-isomer-repair-046/smith-2003-hf178-gamma-manuscript.pdf`。`raw_file`是未填归档槽，raw目录未改动；获取、指纹和阅读范围保存于public_staging_manifest。旧的模糊Crossref题名查询没有命中，随后精确DOI核验成功，两次结果分别保留，不用模糊检索自动认定身份。

## Scope and Reading Depth

实际视觉读正文PDF3–7/印刷1–5，包括Figs.1–4、Tables I–II、方法、讨论、限制和结论；封面/声明另读。正文嵌入字体使文字提取严重乱码，所以能量、Jπ、乘性和表头以渲染页回看为准。未重取参考文献原实验、事件数据、完整校准曲线或作者分析代码；未取得SI，不声称其存在或不存在。

## Paper Question and Scientific Motivation

31年异构态的主衰变高度内转换，直接γ弱支难见。论文要在复杂衰变源中确证从16⁺异构态直接出发的弱γ线，并用两个K=8⁻带之间的分支约束混合；它不是跨质量区fν–γ形变普适律的测量。

## Summary

本实验用γ–γ符合和吸收片控制确认从异构态直接出发的M4/E5弱γ支，并改善K=8带间分支信息。高度内转换的E3主支、若干归一和阻退度依赖既有输入；相对γ强度不等于绝对分支概率。当前研究将其用于纠正逐支乘性和部分γ半衰期合同，不从本篇推导全核区寿命或γ隧穿定律。

## Method and Design Logic

15 kBq异构态源放在TRIUMF-ISAC的8π谱仪中心。20个反康普顿n型HPGe给出符合关系；源含172Hf/172Lu杂质。作者分别无吸收片、铅片和铜片取数，用改变求和/串扰贡献的控制识别弱线。主要分析使用铜片条件的29天数据，而非把所有条件无区别相加。

## Key Evidence and Reasoning Chain

弱线峰 → 与既有级联的符合及吸收片控制 → decay placement → 与先前能级/电子证据及选择定则相容的多极性 → 采用相应部分γ半衰期、转换系数与Weisskopf约定得到报告fν。最后一步并非单靠总31年寿命或相对峰高测得。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| SM03-D27-1 | 20台HPGe；426-keV处绝对峰效率4%、FWHM 1.6 keV。数据总42天，8天无片、5天铅片、29天铜片，符合时间差不超过20 ns；弱线还受逃逸峰、求和、对侧散射及杂质影响。 | experimental-setup-and-response | direct-manuscript-and-visual | PDF4/printed2, left column and Fig.1 caption | true |
| SM03-D27-2 | Table I把约309.5(1)-keV支列为16⁺→12⁻ M4，587.0(1)-keV支列为16⁺→11⁻ E5。Figs.2–3及讨论用符合支持其从异构态直接出发；作者此前的conversion证据与本次γ确证有谱系依赖，不能当完全独立Jπ测量。 | measured-gamma-lines-and-assignment | direct-manuscript-with-prior-constraints | PDF4–6/printed2–4, Fig.2, Fig.3 and Table I | true |
| SM03-D27-3 | Table I列12.7-keV的16⁺→13⁻ E3与fν=66(1)；正文说明该主支高度内转换，未被直接探测到γ。printed5对该fν采用转换系数1.4×10⁷；这是有既有输入的报告量，不是本轮独立重提取。 | adopted-branch-and-derived-strength | direct-manuscript-with-dependent-input | PDF3/printed1 right column; PDF5 Table I; PDF7/printed5 left column | true |
| SM03-D27-4 | Table I强度以325.5(1)-keV线设100.0(17)归一；309.5和587.0线分别为0.015(1)与0.0062(5)。这些是相对γ强度，不是每次母核衰变的绝对γ概率；不得直接当作bγ或总分支。 | relative-intensity-and-normalization | direct-table-and-visual | PDF4/printed2 right column, normalization paragraph; PDF5/printed3 Table I | true |
| SM03-D27-5 | 作者给M4和E5的ΔK=8、ν=4和3，Table I报告fν=72(2)、165(5)；用部分γ半衰期与Weisskopf半衰期定义fν。不同多极、不同ν的数据不能沿用同一个ν=6指数。 | nominal-forbiddenness-and-reported-hindrance | direct-manuscript-and-visual | PDF5/printed3 Table I; PDF6/printed4 right column | true |
| SM03-D27-6 | 515-keV的8⁻→6⁺支未被确证；作者借铅吸收片抑制89/426求和给强度上限，Table I列M2及fν>160。正文还说M2/E3混合未知。不能把“未见”改写成E2支已测或完整模式排除。 | expected-but-not-established-and-limit | direct-manuscript-and-visual | PDF5/printed3 left column and Table I; PDF7/printed5 first column | true |
| SM03-D27-7 | 作者认为同一核素的若干阻退度有一致性，但明确比较其它核素中很低fν，要求模型解释不同核素的差异；Table II的E2带混合比来自本次符合强度与既有分支约束。 | author-interpretation-and-dependence | direct-manuscript-and-bounded | PDF6/printed4 Table II and mixing discussion; PDF7/printed5 discussion/conclusion | true |

## Assumptions and Scientific Boundaries

异构态31年寿命、若干Jπ/K、多极性及转换系数包含既有信息；新γ计数不独立测量所有这些量。13-keV E3主要为转换电子通道，不能用图上γ弱线强度直接重建主支。以不同吸收片作控制不自动消除未知响应或统计相关；没有原事件与峰拟合协方差，不给新的置信区间。

## Competing Interpretations and Limitations

弱峰备择包括杂质、求和及探测器间散射。作者用门、伴随级联及吸收片条件减弱这些备择；对未定位微弱线仍保留不明来源。515-keV支的物理存在性与可见产额必须分开。论文讨论K混合，不提供“低fν唯一来自γ隧穿”的排他证明。

## Knowledge Impact and Learning Decision

`revises` [[k-isomer-triaxial-tunneling-and-hindrance-collapse]] 的Hf错误E2基准与“同一ν=6”指数；`supports` [[walker-dracoulis-2001-exotic-isomers]] 中E3主支和部分γ半衰期定义，并补上M4/E5一手实验层。E3/fν66沿用既有信息不计新独立测量。当前保留source及修订研究note，不另造新的Hf整体能级库或装置页面；本轮证据价值是逐支身份和归一合同。QMD/overview批量更新deferred至主题纠错完成。

## Related Knowledge and Project Relations

- methodological-bridge：[[k-isomer-triaxial-tunneling-and-hindrance-collapse]]，分支/转换/乘性与阻退度反演。
- supports：[[walker-dracoulis-2001-exotic-isomers]]，2001综述与2003弱γ实验的来源谱系区分。

## Extracted Pages

- [[k-isomer-triaxial-tunneling-and-hindrance-collapse]]：逐支选择定则、绝对分支和内转换合同；旧八核表不再作为实测系统学。
- [[walker-dracoulis-2001-exotic-isomers]]：与综述E3参考支互链，保留直接弱γ数据与既有转换输入的依赖关系。

## Human Review Triage

本页为Codex定向source self-audit，非human-reviewed。P0身份/文件签名/哈希已核；P1为M2/E3未定混合、13-keV主支的依赖输入、缺原始事件/响应/协方差。已核内容不替代对最终期刊版本或不同核素分支的逐条核验。
