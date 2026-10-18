---
type: source
title: "223Ra官方reference：未知MR符号、多重放置与2026编译强度"
aliases: [NNDC223Ra reference records, Ra223 unsigned MR and multiplets]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: evaluated-and-unevaluated-nuclear-data-objects
reading_depth: skimmed
title_original: "223RA ADOPTED LEVELS GAMMAS / 227TH A DECAY / XUNDL-5"
authors: [E. Browne, E. A. McCutchan]
journal: Nuclear Data Sheets
year: 2001
volume: 93
pages: 763--1061
doi: "10.1006/ndsh.2001.0016"
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "NNDC223088001/003 base200110; 223088009 XUNDL202602"
data_version: "fullcut1-May-2001; Jpierr27-Mar-2003; alphaNRerr27-Aug-2012; XUNDLcompiled8-Jan-2026from2019Co05"
source_url: "https://www.nndc.bnl.gov/ensdf/"
raw_file: "raw/data/gpt/day16-20261018/ra223-adopted-691b1924ddb4.ens"
raw_sha256: "691b1924ddb45793d68f03b3aafe4c09c456a30f85e5c316bc316b69cb1fc090"
raw_storage_status: official-staging-verified-raw-archive-deferred
nuclei: [223Ra, 227Th]
reactions: [227Th-alpha-decay]
observables: [multipole-mixing-ratio, photon-intensity, conversion-coefficient, angular-correlation]
methods: [ENSDF-fixed-column, source-lineage, normalization-audit]
tags: [reference-identity, unsigned-MR, multiplets, shared-data, calibration]
---

# 记录的符号、placement与分母必须一起读

## Bibliographic Record

旧评价为E. Browne，*Nuclear Data Sheets* **93**,763–1061(2001)，DOI[10.1006/ndsh.2001.0016](https://doi.org/10.1006/ndsh.2001.0016)，完整题名*Nuclear Data Sheets for A=215,219,223,227,231*；ENSDF选定A223章节引页846。Crossref还给NDS96,391(2002)、DOI10.1006/ndsh.2002.0013的更正记录元数据；未读该期刊正文，不由引用推断全部更改。

XUNDL由E.A. McCutchan于2026-01-08编译（unevaluated），原实验是Collins等*Applied Radiation and Isotopes*145,251–257(2019)，DOI[10.1016/j.apradiso.2018.10.023](https://doi.org/10.1016/j.apradiso.2018.10.023)、NSR2019Co05。2026是编译日期，不是新采集年。

官方[ENSDF](https://www.nndc.bnl.gov/ensdf/) `DatasetFetchServlet(nuc=223RA,searchType=quick,datasource=ensdf)`实际列出对象，再POST `EnsdfDispatcherServlet`。旧对象用`chooseit=ENSDF text format`；XUNDL表单实际submit名为`postButton`，不能照搬旧参数。初错参数HTTP500已保留，纠正后200得到真实143行，不以空响应当数据。

| 精确datasetcheck | 读取范围/原文本位置 | SHA-256 |
| --- | --- | --- |
| 223088001,223RA Adopted，641行 | general1–170、selected246–270/291–309/358–378及L280.182块；`tmp/day16-ra223-reference/adopted.ens` | `691b1924ddb45793d68f03b3aafe4c09c456a30f85e5c316bc316b69cb1fc090` |
| 223088003,223RA 227Thα，865行 | general1–170、selected227–275/490–518/551–594/653–676；`tmp/day16-ra223-reference/th227alpha.ens` | `782c225e071facafce81f60c6a56b08d752ea2733dab3101d073c12aa8e655fc` |
| 223088009,223RA XUNDL-5，143行 | 全部143行；`tmp/day16-ra223-reference/xundl2026-v2.ens` | `30a38a663859a9df19fd75ff58eef143b52f13b962464f2d60a8f0c7330b329f` |

原件在repo tmp、raw槽未归档，不修改raw/Bib。来源作者Browne为旧评价者、McCutchan为新编译者，不把两者写成2019实验作者。

## Scope and Reading Depth

本页是选定对象/字段与格式审核，不是整质量链评价通读。旧两对象只定向读上表范围；新XUNDL完整读。另视觉复核[[tuli-2001-ensdf-format-manual]] printed28/PDF34，核MR显式号、col77 `&/@`与RI语义。新primary Collins2019只有NNDC/Crossref书目及仓储发现，本文写回时未读其正文，不补其标定或Cov。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| N223-1 | 旧对象基版200110/fullcut1-May-2001，另有27-Mar-2003 Jπ修改、信件fromJones注；α对象还记27-Aug-2012 normalization更正。列表月份不穷尽字段修改史，信件正文未取得。 | object-version-boundary | direct-object | 223088001 H2–5；223088003 H2–12 | true |
| N223-2 | target在L342.654(21)、J=(9/2)+的G62.45(5)，MR token为无显式号0.29(5)。按TU01规则sign未知，不能用float正值宣称评价已测正δ，也不能用Adopted与α两对象重复转录修复J98原表非闭合。 | unsigned-MR-and-conditional-spin | direct-fixed-field-and-format | 223088001 L342.654/G62.45；223088003 lines490–495；TU01printed28 | true |
| N223-3 | α对象target MR注引用1998Jo08的A2=.29(.06)/A4=−.07(.08)，与J98同实验；相邻212.70显式−.4(.1)另有“sign is from1998Jo08”注。字段有号/无号、统计误差与primaryphase是不同层。 | sign-and-field-provenance | direct-object | 223088003 G62.45 M,MR494–495；G212.70 MR507–510 | true |
| N223-4 | XUNDL202602实际编译2019Co05；声明用semi-planar HPGe测绝对Iγ，Eγ/level/J来自Adopted，全部MR空。它不提供新δ、偏振或原α门，也不是2026独立实验。 | postcutoff-object-identity | direct-XUNDL | 223088009 header/comments2–18；allG MR fields | true |
| N223-5 | XUNDL两113.1均RI=.8026(.0038)、两314.9均.4754(.0010)，col77为&：一个未分区强度复制到两个placement。不能相加成1.6052/.9508或默认每条独立测量/各自同强度。 | shared-undivided-intensity | direct-object-and-format | 223088009 L174.6两G113.1；L376.3/L445.1 G314.9；TU01col77 | true |
| N223-6 | 旧α对象两113.11为@：已分配RI4.2/1.2，CC.362/5.78，LC.0611/4.00、MC.0147/1.09；两处RI均注明1971Br29并列另项1993强度。不同版本/门的数据不能静默并作同一次角fit。 | divided-intensity-and-provenance | direct-object | 223088003 lines251–270 | true |
| N223-7 | 只在旧分区/同响应条件下，E2份额photon=.2222、total=.5872、L电子=.9493、M电子=.9549。此算术说明electron选择可增强E2，不是1998实测门份额或独立验证；不以αT替subshell系数。 | conditional-companion-weight-check | fixed-field-arithmetic | 223088003 G113.11 RI/CC/LC/MC；本页权重公式 | true |
| N223-8 | 旧α NR=.129(.011)，两113.11总光子central为(4.2+1.2)NR=.6966 per100decays；新XUNDL NR=1且同组总I=.8026(.0038)。旧RI分区误差/共同norm、两来源响应不全，未作独立差异z检验或将其强配原角系数。 | normalization-and-comparison-boundary | direct-field-and-arithmetic | 223088003 N62/comments64–65；223088009 N19/G113.1 | true |
| N223-9 | 两旧314.85分别位于L376.296 E1与L445.071 M1，α对象RI同3.8(.3)且&未分区；α能记录为5668.0(15)/5600.6(18)。相隔67.4keV与原约25keVα分辨只给尺度，未恢复实际窗口/尾部/背景或污染。 | gate-and-reference-readiness | direct-object-and-primary-crosswalk | 223088003 L376.296/A5668.0/G314.85；L445.071/A5600.6/G314.85 | true |
| N223-10 | 62.45分支的能量相容终态候选为L280.182：342.654−280.182−62.45=.022keV；把终态误认61.424会差218.78keV。G62.45没有显式FL，G281.42才有FL61.424。初冻结回忆误认已纠正并保留，未改原数据/正确J9/2→7/2模型。 | Codex-recall-correction-and-energy-identity | source-record-and-arithmetic-control | 223088001 L280.182/L342.654/G62.45/G281.42 FL61.424 | true |

## 符号未知、物理两候选与相位变换

[[tuli-2001-ensdf-format-manual]] TU01-1规定已知sign须显式写。这里`MR="0.29"`保留unsigned状态；两候选δRB=±.29是未决符号的条件输入，不是将评价改成两次测量。相同9/2→7/2 pointα布居模型给：

| 假定δRB | a2 | a4 | P90 |
| --- | --- | --- | --- |
| −.29 | .245184 | .048359 | −.786070 |
| +.29 | −.856775 | .048359 | −.105756 |

每个物理候选内部的native/RB同步operator桥残差0；两个候选observable不同。不能把约定转换误叫第二个物理解，也不能以其它primary/sign label替代实际reference/response/Σ。原[[jones-1998-ra223-alpha-gamma-correlations]] J98-12的printed δ/theory不闭合仍保留；本评价不独立解决它。

## 多重放置与分母

col77 `&`表示intensity **not divided**，`@`表示intensity **suitably divided**。这不是普通文本脚注：去掉flag会改变观测单位。XUNDL的113.1和314.9各有两个parent placement，重复的RI/误差代表一个组总量，分量权重未识别。只以E=174.6或342.6选level也会遇到不同J的重复；程序拒绝单能量唯一选择。

旧113.11两@给的分区可以作明确的条件算术：

`wγ,i=RIi`，`wtotal,i=RIi(1+CCi)`，`wL,i=RIi αL,i`，`wM,i=RIi αM,i`。

E2份额由相应`w2/(w1+w2)`得到。95%左右的L/M份额只限此旧输入/同接受响应，不能当原1998α门的实测纯度；旧分区本身含来源/模型依赖，算术回代不新增独立电子证据。XUNDL不分区的总量则无法单凭总强度唯一确定P_eff，仍需matching parent门或别的分量观测。

## 回忆误认的纠正

初active recall把342.84的62.45写到61.431终态，后来对照fixed-column与能量闭合识别错误：该母态另有281.42/FL61.424，62.45的相容候选为280.182。冻结文件/hash保持原样，[纠正记录](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ra223-recall-correction.json)另存；所有47行point输入使用的是正确Ji/Jf，未用错误Ef能量，故既有角计算数值不变。新脚本保存energy guard；.1keV只是候选搜索阈值，不是已知Cov下的置信判决，没有显式FL时仍保留candidate措辞。

## Summary

官方对象补齐版本/符号状态和多重放置语义。它保留了原δ符号/producer与分量权重缺口，不能因为字段有数字或日期新，就授予独立选根或偏振校准能力。

## Competing Interpretations and Limitations

- 2003Jones信件未得，不能由Jπ更新注释补出MR修订。XUNDL借Adopted的E/J而新报RI，两层依赖不同。
- 2019Collins正文尚未读；当前只XUNDL/NSR/Crossref及仓储发现，不据metadata补efficiency/TCS/ingrowth Cov。NPL机构记录新路线可继续核；不从publisher403/429或验证页写原文结论。
- 原J98具体α能窗、peak area、完整response/Σ仍缺；不以Gaussian尾部toy制造真实crossfeed。
- 新数据请求中短暂DNS/429和一次错误submit500各有回执，未改DNS/凭据，未把网络错误当空科学结果。

## Knowledge Impact and Learning Decision

`supports`source身份/字段语义与必要companion权重分层；`revises`裸解析unsignedMR和重复placement RI的做法，也纠正本run回忆的终态误认；`limits`以评价/新编译强度代替独立phase/P/Q。新claims全部needs_review，formal16一次、partial17，不开18。

## Extracted Pages

- [[tuli-2001-ensdf-format-manual]]：col77与MR符号的原格式规则。
- [[jones-1998-ra223-alpha-gamma-correlations]]：原source与评价复制/新版绝对I的依赖。
- [[compton-polarimetry]]、[[multipole-mixing-ratio]]：matching reference不能丢sign、parent或placement。
- [[internal-conversion-analysis]]：photon/total/subshell权重与真实响应边界。

## Reproducibility

[fixed-column/flags脚本](../../system/scripts/day16_ra223_reference_audit.py)实际exit0；[合同](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ra223-official-analysis-contract.json)与[结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ra223-official-audit-result.json)固定三文件hash。v1结果/源码snapshot保留，v2仅补能量identity guard；不改物理数据或review状态。执行输出不替本页原子claim/原文locator。
