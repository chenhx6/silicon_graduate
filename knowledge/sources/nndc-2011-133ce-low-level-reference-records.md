---
type: source
title: "NNDC2011评估快照：133Ce基态、低异能态与参考能量"
title_original: "133Ce ADOPTED LEVELS, GAMMAS (ENSDF record 133058001)"
aliases: [133Ce adopted low levels 2011, ENSDF133058001 low reference]
created: 2026-10-27
updated: 2026-10-27
status: ai-draft
review_status: unreviewed
source_type: evaluated-database-record
reading_depth: skimmed
authors: [Yu. Khazov, A. Rodionov, F. G. Kondev]
year: 2011
evaluation_citation: Nuclear Data Sheets 112, 855 (2011)
evaluation_header: 11NDS 201104
publication_cutoff: 31-Oct-2010
record_id: 133058001
companion_record_id: 133058014
retrieved_local: 2026-10-27
canonical_source: https://www.nndc.bnl.gov/nudat3/getdataset.jsp?nucleus=133Ce&unc=nds
citation_key: ""
raw_file: raw/database-records/133ce-2011-adopted-133058001.ensdf
raw_sha256: 4ac09f19661a52dd6061c8797cd3daeeadb869ca5be67d4423bc35040da4bced
raw_storage_status: public-staging-not-archived
actual_body_file: tmp/day24-ce133-evaluated-zero-entry-069/adopted.ensdf
nuclei: [133Ce]
methods: [evaluated-level-record, atomic-beam-magnetic-resonance-lineage, gamma-energy-least-squares]
observables: [level-energy, spin-parity, half-life, isomer-reference]
tags: [historical-zero, evaluation-version, covariance-boundary, 133Ce-analysis-blueprint]
---

# 服务当前返回的评估版本与历史实验身份分别保存

## Bibliographic Record

本轮2026-10-27北京时间通过NNDC公开端点实际取得133Ce `ADOPTED LEVELS, GAMMAS` record133058001，以及`120SN(16O,3NG)` record133058014。两header为11NDS/201104，Khazov/Rodionov/Kondev，NDS112,855(2011)、cutoff31-Oct-2010；是服务在检索时返回的2011评估，不宣称包含2026新实验或全部后续文献。

正式原文获取流程为ENSDF DatasetFetchServlet quick search，再EnsdfDispatcherServlet的`ENSDF text format`只读POST；adopted文本1043行，SHA见frontmatter；reaction文本171行，SHA f30e85c96003b0359f6a1cfdb8dffd66f6fa30b144f5cd7a7a8d25c2ab2a2bae。NuDat HTML和IAEA levels CSV另取，同源评估不是独立实验。IAEA URL为https://nds.iaea.org/relnsd/v0/data?fields=levels&nuclides=133ce，CSV SHA98de2d45e8f746334aeeed8ec8d4a524e41e8e63c5c08b156152ff191e27df32。

原快照在tmp，raw未归档；旧式mass URL一次404后转正常dispatcher，未重复撞失败端点、未改配置。正式request参数/响应类型/哈希另有access receipt，不能把HTML wrapper哈希混成ENSDF正文哈希。

## Scope and Reading Depth

069定向读adopted低态及comments、反应低态/历史说明、两个official reference pages和NuDat/IAEA对应字段，非1043行全核结构精读。root复核adopted原行1–105、reaction1–171全部文本及CSV首两态的定宽/列语义；未原读2011评价论文全文或NSR列出的每篇primary，未从band字母推现代带。

## Summary

此adopted快照给ground0、1/2+、97(4)min；低9/2−异能态37.2(7)keV、5.1(3)h。它提供了独立于Wiki能差算术的实际评估记录，和[[gizon-1974-deformed-states-cerium-neodymium]]当年ground/isomer尚未知的陈述可以同时成立。反应子记录另保37.3(6)/4.9(4)、固定anchor且称from adopted，不能平均或假定各record实时同步。

## Key Results

所有新claim needs_review:true；以下为评估字段和来源链，不是本轮新测量。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| N133CE11-D24-001 | 当前检索所载adopted为2011评估、201104 header、cutoff2010-10-31；NuDat/IAEA同源，不计成两次独立实验。 | actual-evaluation-metadata-and-lineage | direct-record | adopted.ensdf line2; line3; line4; IAEA CSV metadata columns | true |
| N133CE11-D24-002 | adopted L行给ground0、1/2+、97 M 4；其J引用1973In04 atomicbeam，T引用1967Ge08。不是从WK22反造的ground。 | evaluated-ground-with-primary-attribution | direct-record | adopted.ensdf line62; line64; line65 | true |
| N133CE11-D24-003 | adopted低态37.2 7、9/2−、5.1 H 3且M标志；5.1(3)h为1976Ge10的4.9(4)h与1967Ge08的5.4(5)h加权，J同1973In04。 | evaluated-isomer-and-shared-input | direct-record | adopted.ensdf line67; line69; line70 | true |
| N133CE11-D24-004 | 同评估一般能量来自γ能least-squares；37.2(7)/207.4(7)与直接170.2(2)γ有共享fit/anchor。未给Cov，不能假定两level误差独立或倒推唯一Cov。 | precision-and-covariance-boundary | direct-record-plus-inference | adopted.ensdf line18; line67; line79; line83 | true |
| N133CE11-D24-005 | 原行%EC+%B+ LT100、%IT=?；没有据此观测到37.2keV IT γ。IAEA aggregate100不替ENSDF的branch缺口，也不从levelgap造线/BR/ICC。 | explicit-decay-branch-boundary | direct-record | adopted.ensdf line68; IAEA CSV low-isomer row | true |
| N133CE11-D24-006 | 同201104 reaction记录另给37.3(6)keV/4.9(4)h，energy held fixed且E/T from adopted。保两个record版本，不平均、不当第二独立absolute测量、不擅修原表。 | cross-dataset-version-and-fixed-anchor | direct-record | sn120-reaction.ensdf line84; line85; line86 | true |
| N133CE11-D24-007 | reaction comments称1974Gi01建谱基于5.4h9/2态，后1995Ra12/后续研究扩充；不由2011 adopted身份倒写1974作者当时已知ground顺序。 | historical-scheme-lineage | direct-record-and-original-comparison | sn120-reaction.ensdf line11; line12; line13; line14; line18 | true |
| N133CE11-D24-008 | reaction开头首L之前仍列817.3/582.2/624.8/464.6等unplaced γ；本快照未把它们绑定现代582母态或817.7 reference。评价给的I/E误差由其一般规则赋，不当原实验逐线独立误差实测。 | evaluated-unplaced-peak-and-error-provenance | direct-record | sn120-reaction.ensdf line20; line24; line55; line64; line66; line73; line82 | true |

## Low-State Reference and Precision

|record/状态|E keV|Jπ|T1/2|定义/依赖|
|---|---|---|---|---|
|adopted ground|0.0|1/2+|97(4)min|line62；J/T来自先前实验引用|
|adopted低异能态|37.2(7)|9/2−|5.1(3)h|line67；加权寿命含旧5.4h输入|
|reaction固定低态|37.3(6)|9/2−|4.9(4)h|line84–86；from adopted且held fixed|
|adopted带内相连态|207.4(7)|11/2−|本窄问题不转录其clock为primary|line79；170.2(2)连接γ见line83|

所有T均为记录的half-life，不能改称meanτ。97(4)min对应5820(240)s、5.1(3)h对应18360(1080)s只是单位换算，不产生新precision。IAEA CSV有两个同名`unc_hl`列：原单位digits与秒数误差，必须按位置/相邻unit区分，不能用普通dict覆盖。数值0.7keV、0.3h、4min不被本页另称Gaussian CI或指定confidence level。

WK22的37.2此前是由207.4−170.2/592.1−554.9派生的decimal；本次中心数相同，不能把该旧行追溯性改成当时已读评估，也不自动给它赋本记录.7误差。评估能量fit的共同Cov未交，不能把共享reference offset误差独立加到每条能级/跃迁。

## Primary Lineage and Unresolved Absolute Anchor

- 1967Ge08：Gerschel/Albouy，Compt.Rend.264B183(1967)，*Isomerism in 133Ce*；本轮只读official reference record。
- 1973In04：Ingelman/Ekström/Olsmats/Wannberg，Phys.Scr.7,24(1973)，*Nuclear Spins of Neutron-Deficient Lanthanum and Cerium Isotopes*；两态J的atomicbeam来源，本轮未原读。
- 1976Ge10：Gehrke/Helmer，J.Inorg.Nucl.Chem.38,1929(1976)，DOI10.1016/0022-1902(76)80440-X；4.9h输入来源，未原读。
- 1974Gi01：[[gizon-1974-deformed-states-cerium-neodymium]]，本轮另有直接原读；source使用当年9/2参考和未定ground身份，保原叙述。
- 1995Ra12：Rab，NDS75,491(1995)，DOI10.1006/ndsh.1995.1030；后评价扩充层，不是一次新采集。

NuDat称能量来自120Sn反应表，而该表低态又标from adopted/held fixed；仅凭本次comments尚未唯一闭合两正负宇称基底相对激发能最初如何测定。当前adopted字段可如实引用；首次absolute anchor的实验路径仍是具体来源问题，不能把循环注释当独立测量已闭合。该未解也不取消公开adopted数值本身。

## Competing Interpretations and Limitations

评价不是模式证明。2011 band字母/configuration可能与1974/现代论文不同；本轮不将它们搬成WK22、A13或高spin3qp band身份。reaction中可能有后续RDDS/其它实验输入；若接入寿命网络须按Ei/Jπ/branch、原文clock定义、采集/方法谱系核，不直接把数据库T列冒原论文meanτ。

current服务版本与历史知情状态、同源UI与实验独立性、levelgap与observedγ、evaluated不确定度与实际Cov分别处理。supports的是低态参考现在有实际public记录；revises的是“现代zero只有Wiki算术入口”的知识缺口；limits的是把它当新独立实验、首次测定链已闭合或582分母/程序零点已解决。

## Extracted Pages

- [[133ce-thesis-analysis-blueprint]]：历史/现代zero、误差/分母与actual程序输入分开。
- [[wakudyanaye-2022-triaxiality-rotational-bands-133ce]]：派生37.2与后来查得adopted记录分层。
- [[gizon-1974-deformed-states-cerium-neodymium]]：保1974当年ground身份未知，不回改原实验。


Day24 evaluation link: [[nndc-2011-133ce-low-level-reference-records]]
