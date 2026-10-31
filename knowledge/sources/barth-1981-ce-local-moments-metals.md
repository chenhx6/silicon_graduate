---
type: source
title: "Barth1981：Ce局域磁场、核g的Curie标定与两类松弛"
title_original: "Local moment studies of isolated Ce ions in liquid and solid metals"
aliases: [Barth1981 CeSn CePb, Ce local susceptibility calibration]
created: 2026-10-23
updated: 2026-10-23
status: ai-draft
review_status: unreviewed
source_type: experiment-and-method
reading_depth: read
authors: ["H. J. Barth", "G. Netz", "K. Nishiyama", "D. Riegel"]
year: 1981
journal: Hyperfine Interactions
volume: 10
pages: "811-820"
doi: "10.1007/BF01022015"
citation_key: ""
canonical_source: "https://doi.org/10.1007/BF01022015"
source_url: "http://link.springer.com/content/pdf/10.1007/BF01022015.pdf"
raw_file: "raw/papers/gpt/learning-daily/20261022-DAY20-be2-qt-deformation-systematics/barth-1981-ce-local-moments.pdf"
raw_sha256: "dff4d09add2aeeb91302ca1b222cc0e3e7e7b280fe0095e097a2585e7b60cb15"
raw_storage_status: reserved-unpopulated-public-publisher-pdf-only
raw_archive_verified_at: 2026-10-23
analysis_status: public-staging-original-read-raw-archive-verified
public_staging_file: "tmp/day20-barth107/PDFs/Local_moment_studies_of_isolated_Ce_IONS_in_liquid_and_solid_metals.pdf"
license: not-established-from-tdm-metadata
nuclei: [136Ce]
methods: [TDPAD, magnetic-hyperfine-interaction]
observables: [g-factor, local-field-enhancement, nuclear-alignment-relaxation, electronic-spin-relaxation]
tags: [calibration, ce-pb, ce-sn, source-lineage, magnetic-moment]
---

# 温度扫描的局域场标定仍有模型条件

## Bibliographic Record

H. J. Barth、G. Netz、K. Nishiyama、D. Riegel，*Hyperfine Interactions*10(1981)811–820，DOI10.1007/BF01022015；刊头、四作者与题名在PDF1实际核对。

公开publisher PDF为440322bytes、10页，SHA256见frontmatter。nature-downloader的TDM metadata不确立开放再分发许可；SI按本轮auto配置关闭。raw_file为未填归档槽，实际只读public staging，未改raw/PLAN/Bib；下载身份与实际scope107在本日run02中。

## Scope and Reading Depth

在primed-recall-107冻结后，实际读PDF1–10全部文字及参考文献，视觉核十页，涵盖Figs1–5、Eqs1–8及未编号的Curie式、最后两页会议讨论。没有独立数值table。未取得原事件、温度/场标定Cov或确切fit producer；所引1980 PRL正文仍未得。

## Summary

用136Ce(10+)核探针观察液态Sn/固态Pb中的Ce电子局域磁矩。温度扫描拟合给g_N和局域磁场增强，核取向松弛则在额外动力学假设下约束电子4f自旋速率。后续[[ionescu-bujor-1998-static-moments-129-131ce]]的g标定和[[dafni-1983-ce-isomers-tin-quadrupole]]的relaxation参考与本组工作相关，但不是对同一核态/宿主/谱形的无条件复制。

## Extracted Pages

PDF1/811实验身份和装置；PDF2/812 Figs1–3；PDF3/813 Curie式、Fig4与g/B(0)；PDF4/814 Eq1与Fig5；PDF5/815 Eqs2–7及交换假设；PDF6/816 Eq8、两种拟合及方法局限；PDF7–8/817–818全部参考文献；PDF9–10/819–820会议问答及作者承认的模型限制。

## Method and Evidence Chain

124Sn(16O,4n)136Ce，85MeV，1ns脉冲、10000ns重复周期，NaI(Tl)探测。136Ce核探针I=10、半衰期2000ns；电子Ce³⁺的4f态则用J=5/2、g_J=6/7，不能把两种角动量或两类g混同。时间谱的振荡频率约束核g与局域磁场的乘积；温度扫描与Curie假设进一步分解两者。包络松弛τ_N与核态衰变寿命不同，电子τ_J又经Eq1额外反演。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| BA81-D20-1 | 核探针为136Ce(10+)，T1/2=2000ns；液态Sn例Fig2为504K/19.80kG、552keV线，固态Pb例Fig3为298K。Pb样品由.7mg/cm²的124Sn蒸镀于Pb并植入；不等于1998的129/131Ce或.6mg/cm²样品。 | probe-host-and-measurement-identity | direct-original-and-visual | PDF1/811 setup; PDF2/812 Figs1–3 | true |
| BA81-D20-2 | ωL=(g_N μ_N/ℏ)β(T)B_ext；β=1+g_J μ_B(J+1)B(0)/(3k_BT)，使用Ce³⁺ J=5/2、g_J=6/7。拟合给B(0)=1.78(4)MG/CeSn、1.78(6)MG/CePb及g_N136=−.180(2)。它是温度扫描与此模型下的同时提取，不应改写成先假定核g的独立场测量或完整Cov已知。 | Curie-calibration-and-joint-parameter-extraction | direct-original-and-visual | PDF3/813 temperature paragraph and Fig4 | true |
| BA81-D20-3 | 在上述Curie式中g_J(J+1)/3=1；以Pb B(0)=178T、T=298K算β≈1.401，与后续采用1.40相容。这是明确给定原模型/温度的条件核对，不恢复IB98原producer、1.40(2)的联合误差预算或其样品实际局域场。 | conditional-room-temperature-transfer | task-derived-from-original | BA81-D20-2; IB98-D20-R104-1 | true |
| BA81-D20-4 | Eq1把核取向松弛τ_N与电子4f松弛τ_J相连，要求ω_Jτ_J≪1且没有额外贡献τ_N的通道；电子速率约10^13s^−1是该反演/动力学框架下的量，不是核E2衰变率或其寿命。液态Sn中忽略EFG松弛的论据不能直接认证固态Sn辐照缺陷无影响。 | distinct-relaxation-identities-and-inverse-model | direct-original-and-visual | PDF4/814 Eq1 and text; PDF6/816 limitation iii | true |
| BA81-D20-5 | 电子交换/CEF假设下Eq7单参数Kondo拟合给TK=2.3K，Eq8另以明确交换通道/简并因子给解释。会议讨论承认Eq7简化的不确定性，并指向新增Eq8；“曲线相合”不确定唯一交换机制或普适实验时间阈值。 | competing-electronic-dynamics-models | direct-original-and-visual | PDF5–6/815–816 Eqs2–8; PDF10/820 final discussion | true |
| BA81-D20-6 | PDF9问答中Mahnke指出可能有温度无关Knight/orbital项，Riegel明确承认未纳入，并称Knight项预期较小、可能与diamagnetic shift部分相消。不是实测这些项严格为零；有无额外常数影响温度截距与核g的可辨识性。 | explicit-author-assumption-and-counterquestion | direct-original-and-visual | PDF9/819 Mahnke–Riegel discussion | true |
| BA81-D20-7 | Ref7为相同四作者的PRL“in print”；与IB98所引1980 PRL的作者/主题相连，但本次未取得该PRL正文，不能声称两版完整逐点对照或两份独立实验。Dafni1983明确Ref5引本1981文章，故引用次数不增加独立校准次数。 | related-account-and-reference-dependency | direct-original-and-metadata | PDF7/817 Ref7; DA83 PDF4 Ref5; IB98 Ref13 | true |

## Day20条件常数项反例（checkpoint108）

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| BA81-D20-8 | 另声明β=1+K0+C/T、C∝B0时，gN→a gN、B0→B0/a、1+K0→(1+K0)/a保持gNβ与gNB0不变。故选定原Eq1快涨落形式的relax及构造的多温度/双外场符号期望曲线可相同。11项仅检该声明观测映射；±.2%是chosen witness，未估原K0大小/CI，未抽样事件/核等待或恢复producer，也不否定作者采用K0=0模型下的报告。 | declared-observation-map-identifiability | task-derived-not-experimental-CI | BA81-D20-2/4/6; printed813/814/819; curie-offset-contract-result-108.json in Day20 run02 | true |

## Competing Interpretations and Limitations

局域场来自电子态与交换作用，核g来自另一层；二者的同时拟合仍依赖温度/常数项/价态模型。会议对温度无关项、交换通道、辐照损伤及“可测电子速率上限”的质疑应与作者答复一起保留，不把概念上的敏感范围当实测精度证明。

## Knowledge Impact and Learning Decision

当前补足的是磁校准的相关原文模型与反证：[[ionescu-bujor-1998-static-moments-129-131ce]]的室温1.40因子可在明确Curie参数下核对，不能据此清除其真实场/拟合Cov缺口，也不替代1980 PRL正文。[[day20-quadrupole-collectivity-systematics-synthesis]]继续把核寿命、核取向relax和电子τ_J分开；核形变判断仍需各自矩阵元与状态身份。
