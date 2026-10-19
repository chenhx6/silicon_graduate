---
type: source
title: "Bethge1966：厚靶反向散射、有效电荷与阻止测量的共同尺度"
title_original: "Energieverluste und Ladungszustände schwerer Ionen beim Durchgang durch Materie"
aliases: [Bethge1966 stopping and charge states, Bt1966 primary]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: read
authors: [K. Bethge, P. Sandner, H. Schmidt]
year: 1966
journal: Zeitschrift für Naturforschung A
volume: 21a
pages: 1052-1056
doi: 10.1515/zna-1966-0727
citation_key: ""
canonical_source: "Bethge Sandner Schmidt 1966 ZNaturforsch21a1052 DOI10.1515/zna-1966-0727"
source_url: https://doi.org/10.1515/zna-1966-0727
raw_file: raw/papers/day17-20261019/bethge-1966-stopping-charge-states.pdf
raw_sha256: 1b0d51590cd0341ac4fa3a496c81252572740d13ea66ee2612f6fbb6ac0ec6d6
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [11B, 14N, 16O, 32S]
methods: [stopping-power, Rutherford-backscattering, effective-charge]
tags: [DSAM-input, stopping, calibration, shared-systematics]
---

# 从原实验看阻止表的误差与对象

## Bibliographic Record

Bethge、Sandner、Schmidt，*Z. Naturforschg.*21a，1052–1056(1966)，3Mar1966收稿；DOI [10.1515/zna-1966-0727](https://doi.org/10.1515/zna-1966-0727)。这是[[iaea-2026-stopping-s-au-o-ta-records]] 中 Bt1966 的原实验，不是新的独立测量。

publisher旧OA入口重定向后仅202空响应，未认作PDF。旧ZfN地址现跳至Max Planck公开档案[10.17617/3.GRUJYR](https://doi.org/10.17617/3.GRUJYR)，档案`Reihe_A.zip`为50086033062字节。只通过合法HTTP Range读取ZIP目录及唯一成员`21/ZNA-1966-21a-1052.pdf`；共5639636网络字节，解压PDF4260488字节，ZIP CRC32核通过，SHA256见frontmatter。未下载全档案、未声称全档案MD5验证。原PDF保存在`tmp/day17-bethge1966/bethge1966-archive.pdf`，raw归档与Bib未写。

[原件取得回执](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/bethge1966-archive-member-receipt.json)、[范围读取程序](../../system/scripts/day17_bethge_archive_member.py)记录每个实际206 range及哈希；PDF第一页题名、作者、期刊、页码与Crossref相符。档案2023发布、PDF2013数字化字样都不是1966实验的新增采集。

## Scope and Reading Depth

先冻结已暴露IAEA比值、25%误差与metadata/abstract的priming，再读完整五页主线/参考文献；Figs1–6、Eqs1–4及全部页面实际视觉核，无表。Fig3断轴、归一字样、Eq3另作高分辨率检查。未恢复原谱bin、逐次beam charge、charge-state效率、完整Cov或编译digitization；Fig3到IAEA16行的全部坐标/符号归属桥仍未闭合，不称全图复现。

## Summary

论文以厚靶Rutherford反向散射测直接能损，再由磁分析的电荷态分布与同速质子阻止值计算能损作比较。作者明确报告直接值整体较高，并归因于束管较差真空中的换电荷使束流粒子数计量偏高。原文为IAEA误差字段提供了具体物理来源，不能将这些点无条件当成独立Gaussian样本。

## Experimental or Method Setup

Heidelberg Tandem Van de Graaff，11B/14N/16O/32S入射Au/Ag/Ni，1mm厚、表面研磨至约.1–1µm粗糙度。厚靶谱sharp edge由表面弹性散射运动学决定，内层散射粒子能量进一步降低；用能量bin计数、Rutherford截面和几何推回深度与能损。另一方法将厚靶90°散射离子用磁铁按电荷分开，五个半导体探测器测分量；同探测器固定E/n关系，利用电荷平衡假设计算有效电荷。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| B66-1 | 原五页题名/作者/1966卷页与DOI匹配；合法档案唯一成员PDF/CRC/hash已核。2013数字化和2023archive发布非新实验，未验证整个50GB ZIP的MD5。 | identity-provenance | direct-original-and-receipt | printed1052；archive member receipt | true |
| B66-2 | 厚靶Rutherford谱的surface edge与连续内层能损由Eq3联系N0/N(E1)、NsσRΔΩ和几何；11B/14N/16O/32S与Au/Ag/Ni、1mm靶/表面粗糙度实际报告。 | experimental-observable | direct | printed1052–1053 Sec1；Fig1；Eq3 | true |
| B66-3 | 方法条件含经典轨道/点电荷、低于Coulomb阈排核势散射、K壳内散射免未知屏蔽，以及入/出能损近似相同且随能量弱变。不能把这些条件当任意低能DSAM collision的认证。 | applicability-and-counter-condition | direct | printed1053 conditions a–d | true |
| B66-4 | 厚靶90°散射后磁分析电荷、五个半导体探测器；作者借约100原子层达平衡及约.1µm取样深度，用Eq4有效电荷平方ΣΦn n²，再经同速质子阻止与Eq2计算。不是单测meancharge即直接测S。 | companion-observable-and-model-input | direct-and-author-assumption | printed1052 Eq2；printed1053 Sec2/Eq4 | true |
| B66-5 | 直接测量整体高于charge-derived值；作者归因于束管差真空中较高电荷态使入射粒子数N0被高估，Eq3因而给高S。B/N效应较小；误差分别B/N12%、O15%、S25%。未给共同Σ或统一Gaussian置信定义。 | author-stated-systematic-and-error | direct-and-author-interpretation | printed1055 Sec3 firsttwo paragraphs；Fig3 | true |
| B66-6 | Fig3分直接散射符号与charge-derived符号，S实线是charge-derived均值连接；Northcliffe的O半经验线与S连接线不是同类预测。Fig2/6另有上游质子/文献与universality输入，两个方法不是完全无共享理论/装置的独立校准。 | figure-role-and-independence | direct-and-boundary | printed1054 Fig2；printed1055 Fig3 caption；printed1056 Fig6 | true |
| B66-7 | 作者称与Northcliffe及其它作者在误差内相合，同时明确S没有同类比较资料，仅与Betz气靶charge分布相合；不把综括excellentagreement当独立32S/Au阻止复测或当前SRIM验证。 | counter-evidence-and-author-interpretation | direct | printed1056 Sec4；Refs6/15/16 | true |
| B66-8 | 当前IAEA Bt1966的16行与此文同源；原Fig3有断轴、局部归一与多类符号，全部16行到原符号/电子核扣除的生产合同未得。旧.962–1.928比值只描述编译/当前SRIM，不等原实验矛盾或已证明转录错。 | compilation-primary-bridge-boundary | direct-source-and-task-inference | ISP26-6；printed1055 Fig3/normalization paragraph | true |
| B66-9 | 固定原local K与g=sinφ/sin(ψ−φ)>0，区分两路径Si/So后所识别的是Seff=(KSi+gSo)/(K+g)。方向(ΔSi,ΔSo)=(t,−Kt/g)不可由单Seff区分；仅为conditiond的局部推广，不是原拟合或任意强能变轨道定理。 | conditional-method-derivation | task-model | printed1053 Eq3/conditiond；bethge1966-exercise-result | true |
| B66-10 | 在同N0尺度模型下N0估计乘b使S估计也乘b，给Covscale=Var(b)TTᵀ的条件rank1结构；原25%不被自动指定为Var(b)。Eq4二阶电荷矩不同于meancharge平方，差为chargevariance，需分量和效率而非单平均。 | conditional-systematic-and-moment-derivation | task-model | printed1053 Eq3/4；printed1055 Sec3；bethge1966-exercise-result | true |

## Authors' Interpretation

作者把直接与电荷态推算方法的相合、与Northcliffe的比较、有效电荷对Papineau曲线的近似符合视为方法支持。原文同时点出束流计量偏移、元素相关误差和S比较资料缺失。前者是作者解释与上游模型比较，后者限制其独立验证范围；本任务未据此给现代阻止先验新的概率覆盖。

## Analytical Reconstruction and Self-Audit

[问题冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/bethge1966-exercise-before.md)、[符号程序](../../system/scripts/day17_bethge_stopping_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/bethge1966-exercise-result.json)以原PDF哈希为前提。固定局部运动学/几何，入、出路径损失贡献分别正比KSi与gSo；Eq3在Si=So时还原原式，g→0/∞给两极限。单谱bin确定一个加权量，不能分别校准两路径。共同尺度外积仅在固定真实向量T、随机共同b条件下成立，无原Cov恢复。

Eq4的物理量为二阶矩。若只有相邻两电荷态n/n+1、fraction为f，则`E[n²]−E[n]²=f(1−f)`；这是代数控制，未赋Fig4/5实际f或新误差。原程序初运行因缺SymPy退出1，后复用仓库内已存在依赖运行通过；不是新独立软件。Fig3初目视把O段标记套到S段的猜想已被高分辨率反证并留档，未改原数据/宣称勘误。literal κ归一与编译完整桥仍partial。

## Competing Interpretations and Limitations

- Eq1/2的有效电荷与同速质子映射有模型条件；电荷平衡是作者假设，非对所有靶/速度的实测定理。
- 图中相合可含共享设备、质子阻止表、模型或同一次测量的依赖；论文、IAEA转载与本任务算术不增独立证据。
- 未见可独立重放的逐bin计数、归一效率、原图数字化规则、完整Σ或电子/核扣除生产流程。不给Sun sp新先验，也不填Schürmann15O/15N低能响应缺口。

## Knowledge Impact and Learning Decision

`supports`以actualprimary定位阻止误差的物理来源和必要charge companion；`revises`把编译25%当16个独立点误差、把两个方法标签当完全独立校准；`limits`当前SRIM比值对原实验的裁决，以及从一个局部谱反推完整速度历史的能力。新增claims均needs_review，没有新实验S/τ/δ/B/CI。

## Extracted Pages

[[iaea-2026-stopping-s-au-o-ta-records]]、[[doppler-shift-attenuation-method]]、[[lifetime-strength-audit-165tm-136nd]]。当前仍为Day17原窗口内恰好Day18无学分预习，不增加课程卡信用。
