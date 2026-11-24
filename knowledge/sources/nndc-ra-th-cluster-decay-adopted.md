---
type: source
title: "NNDC Ra–Th团簇衰变评价：14C/20O分支、总半衰期与226Th通道边界"
aliases: [NNDC Ra Th cluster branching, Ra14C Th20O evaluated decay]
created: 2026-10-29
updated: 2026-11-22
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data
reading_depth: deep-read
canonical_source: "NNDC ENSDF Adopted 222Ra, 224Ra, 226Ra, 226Th, 228Th; acquired 2026-10-29"
raw_file: "raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/nndc-222ra-adopted-cluster-20261029.pdf"
raw_sha256: "3a681f65303cbaa9bba9541dfc439d5155c55f276256121d43652d8dc7004042"
title_original: "ENSDF Adopted Levels, Gammas: 222Ra, 224Ra, 226Ra, 226Th, 228Th"
authors: [NNDC ENSDF evaluators]
year: 2026
citation_key: "nndc_2026_222ra-ensdf-adopted"
source_url: "https://www.nndc.bnl.gov/ensnds/"
raw_storage_status: "official-pdf-archived-new-original"
retrieved: 2026-10-29
nuclei: [222Ra, 224Ra, 226Ra, 226Th, 228Th]
observables: [half-life, cluster-branching-fraction, partial-half-life]
methods: [ENSDF-evaluated-data]
tags: [cluster-radioactivity, branching-ratio, evaluated-data, percentage-conversion]
---

# Ra–Th团簇衰变评价数据

## Bibliographic Record

读取官方 `https://www.nndc.bnl.gov/ensnds/<A>/<Element>/adopted.pdf`，2026年是本页获取时间，不是所有数据的评价年份。222Ra/224Ra/226Ra/226Th/228Th的literature cutoff分别为2023-09-25、2022-03-08、1996-02-01、1996-02-01、2012-12-31。精确URL、文件签名、页数和SHA-256载于 `octupole-cluster-radioactivity-boundary.json`；五份PDF均已逐文件核验后以新增原件归档至raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/，主raw_file指向222Ra，其余路径和哈希见审计JSON。

## Scope and Reading Depth

读取各核基态总半衰期、团簇分支、来源NSR码及限值注释：222Ra PDF2，其余核PDF1。2026-11-22核对222Ra PDF1–11、224Ra PDF1–13、226Ra PDF1–8、226Th PDF1–5、228Th PDF1–46的评价历史、能级表、γ表及谱图。228Th PDF2–6为能级表及带指派，PDF7–24为γ表，PDF25–44为逐能级谱图，PDF45–46为带图。归一化、数据集代码和物理量溯源以相应数据表注释为准。226Th未列团簇分支应记为该评价中的缺项。

## Summary

归集Ra222/224/226的14C和Th228的20O评价分支，严格区分百分数、概率和部分半衰期；226Th未由本轮数据建立20O正测基准。

## Key Results

| ID | 核素与评价字段 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| NCRT-1 | 222Ra：总T1/2=33.6(4) s；%14C=3.0(10)×10^-8，对应无量纲分支b=3.0(10)×10^-10；引用1985Pr01/1985Ho21/1991Hu02。 | evaluated-decay-data | official-evaluated-object | 222Ra Adopted PDF2 ground-state comments | true |
| NCRT-2 | 224Ra：总T1/2=3.6316(23) d；%14C=4.0(10)×10^-9，故b=4.0(10)×10^-11；评价采用1992Ar02并列其他结果。 | evaluated-decay-data | official-evaluated-object | 224Ra Adopted PDF1 ground-state comments | true |
| NCRT-3 | 226Ra：总T1/2=1600(7) y；%14C=3.2(16)×10^-9，故b=3.2(16)×10^-11；评价引用1985Ho21及另一上限。 | evaluated-decay-data | official-evaluated-object | 226Ra Adopted PDF1 ground-state comments | true |
| NCRT-4 | 228Th：总T1/2=1.9116(16) y；%20O=1.13(22)×10^-11，故b=1.13(22)×10^-13；引用1993Bo20。 | evaluated-decay-data | official-evaluated-object | 228Th Adopted PDF1 ground-state comments | true |
| NCRT-5 | 226Th当前取得的Adopted基态记录仅列alpha，不提供20O分支的正测值；不能据此建立已正测的226Th20O实验基准。 | acquired-dataset-boundary | official-evaluated-object | 226Th Adopted PDF1 | true |
| NCRT-6 | 用T_partial=T_total/b、1 y=365.25 d换算，222Ra/224Ra/226Ra的14C部分半衰期中心为1.120×10^11、7.844×10^15、1.578×10^21 s；228Th的20O为5.339×10^20 s。 | arithmetic-derived-from-evaluation | derived | NCRT1–4; source-keyed Python artifact | true |
| NCRT-7 | 222Ra团簇分支注释列出三个 \(I(^{14}\mathrm C)/I(\alpha)\) 测量值：\(3.7(6)\times10^{-10}\)、\(3.1(10)\times10^{-10}\)、\(2.3(3)\times10^{-10}\)，分别源自1985Pr01、1985Ho21、1991Hu02。1991Hu02对通往208Pb 2614 keV \(3^-\) 终态的分支给出 \(2\times10^{-10}\%\) 的上限。 | evaluated-decay-data | official-evaluated-object | 222Ra Adopted PDF2, 0 keV comments | true |
| NCRT-8 | 222Ra能级能量由 \(E_\gamma\) 最小二乘拟合。评价放大若干输入能量的不确定度后，约化 \(\chi^2\) 从4.9降至2.2。高于111.1 keV的表列寿命由库仑激发矩阵元和采纳的γ分支推导。评价说明表列 \(B(E1)\)、\(B(E2)\) 通常也由库仑激发矩阵元换算。 | evaluation-method | official-evaluated-object | 222Ra Adopted PDF2 preamble and PDF3 notes †, ‡ | true |
| NCRT-9 | 222Ra γ表的 \(E_\gamma,I_\gamma\) 默认来自222Fr β衰变，标注@的条目来自 \(^{232}\mathrm{Th}(^{136}\mathrm{Xe},X\gamma)\)。多极性默认来自226Th α衰变的转换电子数据，BrIcc的 \(\alpha\) 值通常由能量、指派的多极性与混合比计算。能级图的强度定义为各能级的相对光子分支。 | evaluated-observable-definition | official-evaluated-object | 222Ra Adopted PDF7 notes ‡, #, @, & and PDF8–10 legends | true |
| NCRT-10 | 224Ra的84.372(3) keV \(2^+\) 寿命采用值为0.748(19) ns，同一能级注释还列库仑激发所得 \(B(E2)\) 与 \(Q_2\) 并引用2013Ga23/2012GaZV。γ表多极性通常来自224Fr β衰变的转换电子数据。 | evaluation-method | official-evaluated-object | 224Ra Adopted PDF1, 84.372 keV entry, PDF8 note # | true |
| NCRT-11 | 226Ra的基态带和 \(K=0\) 八极振动带的自旋宇称沿用库仑激发工作；γ表的相对光子强度来自226Fr β衰变、230Th α衰变及重离子反应。226Th的基态带 \(J\geq 8\) 与八极带 \(J\geq 7\) 的指派依赖重离子反应数据；γ表的默认能量来源是230U α衰变和226Ac β衰变。 | evaluated-data-lineage | official-evaluated-object | 226Ra Adopted PDF3 note & and PDF4 notes †, ‡; 226Th Adopted PDF2 note @ and PDF3 notes †, ‡ | true |
| NCRT-12 | 228Th 的 \(2_1^+\) 和 \(4_1^+\) 总能级半衰期为 0.406(7) 和 0.164(4) ns，评价注明来自232U α衰变。表列相应带内 E2 强度为 167(6) 和 242(9) W.u.。\(K^\pi=0^-\) 带的 396.094(4) keV \(3^-\) 列有通往 \(2_1^+\)、\(4_1^+\) 的 E1 和通往 \(1_1^-\) 的带内 [E2] 上限。该能级行未列通往基态的 E3。 | evaluated-data-lineage | official-evaluated-object | 228Th Adopted PDF1–2 level entries and PDF7 gamma rows | true |
| NCRT-13 | 228Th 基态带在 3283.4? keV 有一个由 \(^{232}\mathrm{Th}(^{136}\mathrm{Xe},X\gamma)\) 支持的暂定 \((22^+)\) 成员。449 keV 连接的放置带有注记 k。 \(^{230}\mathrm{Th}(p,t)\) 的 \(L=0\) 转移支持 831.842、938.61、1119.7 keV 三个 \(0^+\) 能级，其中 1119.7 keV 的第三条 \(K^\pi=0^+\) 带头身份仍属评价推测。 | evaluated-assignment | official-evaluated-object | 228Th Adopted PDF1 dataset D, G; PDF2, PDF6, PDF23–24 | true |
| NCRT-14 | 228Th 的 911.204(4) keV \(2^+\to2^+\) 连接表列 `E2+M1`、\(\delta=+24(8)\) 和 \(\alpha=0.0120(2)\)。转换系数的默认方法为 BrIcc 冻结轨道近似，使用所指派的多极性和混合比。谱图按每个能级的相对光子分支标注。该表未随这行提供偏振测量及其误差。 | evaluated-observable-definition | official-evaluated-object | 228Th Adopted PDF8, E_i=968.984 keV; PDF24 note h; PDF25 legend | true |

## Source Dependencies

222Ra PDF1的评价截止为2023-09-25，历史栏指向 *Nuclear Data Sheets* **192**, 315 (2023)。PDF2的 `2020Bu01` 矩阵元回链实测 [[butler-2020-222-228ra-octupole-evolution]]。同一矩阵元、评价变换的 \(B(E\lambda)\) 与由此求得的寿命属于一条证据链。PDF1资料综述列出的 `2020No13` 是 [[nomura-2020-ra-th-gogny-d1m-octupole]] 的理论计算。逐线使用 \(I_\gamma\) 前应读PDF4–7的来源注释及归一化。总跃迁强度还受内转换影响，多步库仑激发产额另有布居与级联依赖。

## Competing Interpretations and Limitations

`%14C`或`%20O`是百分比；转换为概率必须除以100。总半衰期与罕见通道的部分半衰期不能混用。部分衰变记录与total T1/2评价年代相差较大，未取得完整协方差或原始计数似然；一阶误差传播只能作为标度估计。226Th的18O下限来自 [[warda-2011-actinide-cluster-radioactivity-gogny]] Table I的原实验引用链，不由该NNDC表新造出一个分支。

## Knowledge Impact and Learning Decision

为 [[octupole-cluster-radioactivity-preformation-boundary]] 提供真实实验评价锚点；不从分支比直接测得P0、beta3、beta5或beta7。

## Extracted Pages

- [[octupole-cluster-radioactivity-preformation-boundary]]

## Review Status

Codex source self-audit，所有新claim保留needs_review。
