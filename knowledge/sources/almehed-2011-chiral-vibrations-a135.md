---
type: source
title: "Almehed2011：TAC+RPA手征振动的近谐适用域"
aliases: [Almehed 2011 chiral vibrations, A135 TAC RPA]
created: 2026-10-23
updated: 2026-10-26
status: ai-draft
review_status: unreviewed
source_type: theoretical-paper
reading_depth: deep-read
title_original: "Chiral vibrations in the A=135 region"
authors: [Daniel Almehed, Friedrich Dönau, Stefan Frauendorf]
journal: Physical Review C
year: 2011
volume: 83
pages: "054308"
doi: 10.1103/PhysRevC.83.054308
arxiv: 0709.0969v2
language: en
canonical_source: https://doi.org/10.1103/PhysRevC.83.054308
citation_key: ""
raw_file: raw/papers/2011_Almehed_ChiralVibrations_A135_arxiv07090969v2.pdf
raw_sha256: becba964421bb8860fa657865071df117622a492a2bbb2b23d661d235296f29b
raw_storage_status: public-staging-not-archived
nuclei: [135Nd, 134Pr]
models: [tilted-axis-cranking, random-phase-approximation]
observables: [transition-probability, band-energy-splitting]
methods: [small-amplitude-expansion, quadrupole-tensor]
tags: [chirality, RPA, model-validity, source-lineage]
---

# 近谐手征振动：模型的软化点不是实测相界

## Bibliographic Record

D. Almehed、F. Dönau、S. Frauendorf，*Physical Review C* **83**, 054308 (2011)，DOI [10.1103/PhysRevC.83.054308](https://doi.org/10.1103/PhysRevC.83.054308)。Crossref元数据已核；实际正文为公开[arXiv:0709.0969v2](https://arxiv.org/abs/0709.0969v2)，并未核对VoR正文。PDF边栏31 Jan 2011，题头却印Dated December 1, 2018，保留此版本日期差异，不把期刊年份改成2018。

公开暂存：`tmp/day21-checkpoint051/almehed-2011-arxiv07090969v2.pdf`，18页、487253 bytes，SHA256 `becba964421bb8860fa657865071df117622a492a2bbb2b23d661d235296f29b`。frontmatter的raw_file是尚未写入的归档槽，hash对应实际公开暂存；raw未写入，暂存可能丢失，复核时按URL/版本/hash重新取得。获取记录在Day21 run的`source-retrieval-051.json`。

## Scope and Reading Depth

- 实际阅读18页全文文字，包括Appendix A与refs；视觉核PDF pp.3–18的全部14图、两表及关键公式。p.1–2为文字读取，未宣称逐页视觉核。
- source前回忆为已受MU07等priming的回忆，已冻结，不作盲测。
- 无原TAC/RPA代码或实际job，未重跑本征问题，未核VoR与预印本逐字一致。

## Paper Question and Scientific Motivation

作者要在微观TAC均场之上描述手征左右运动及带劈裂，避免仅依赖刚性转子/无旋惯量等核心假设。作者明确大振幅从振动到隧穿的完整过渡超出本文范围（PDF p.2）。

## Method and Design Logic

TAC自洽均场加残余QQ相互作用的RPA。n=4、5振子壳，BK修正B=.5；κ在SCTAC势能面极小值满足自洽条件，配对隙取邻核奇偶质量差80%（pp.2–3、Table I、Eqs.1–5）。这些是模型选择/校准，不是实验测得的形状刚性。

RPA给带间率，带内率取TAC（p.7）。p.10 Eqs.15–16采用有效电荷ep=1+Z/A、en=Z/A及自由spin g的.7；排印公式已视觉核，但未据此重算实际B。p.11 Eq.18在本文半经典/声子约定下连接跃迁振幅与率，不用它替换实验约化矩阵元定义。

## Key Evidence and Reasoning Chain

均场平面解 → 小振幅RPA声子 → 能量/跃迁率与实验比较 → 再以四极张量分量分析形状和取向振幅。作者明确能量与率本身不直接给出声子性质（p.11 Sec.IV），因此“拟合率”不是排他身份判据。

## Summary

本文为135Nd原解释提供了真实方法后续及近谐失效条件，但没有补出该核逐行参数、原实验分支或联合Cov。主要计算表图属于奇奇邻核；不能将这些数值移植到135Nd。作者支持部分区域以取向为主的手征振动，同时承认大振幅非谐性、某些spin趋势失败及不存在通用onset跃迁模式。

## Experimental or Theoretical Setup

理论研究复用公开实验作比较，不新增采集。Table I/II的八核参数与Figs.1–14需按各自核素阅读。135Nd在p.2明确交由Ref.13，p.8写“not shown here”；Ref.13仅印Mukhopadhyay et al., PRL (2007)，未给卷页。此引用关系不是第二套独立135Nd电磁测量。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AL11-D21-R51-1 | 本文方法已用于Ref.13的135Nd，但135Nd结果不在本文图表展示；Table I/II主要列奇奇邻核，不能补本核逐行参数/branch。 | source-lineage-and-scope | direct-original | PDF p.2 Introduction；p.8 Sec.III；p.18 Ref.13 | true |
| AL11-D21-R51-2 | 近谐RPA仅在劈裂足够大时合理；声子能量到零表征方法/均场转变，需大振幅非谐处理；静态左右TAC解在当前方法下零劈裂，隧穿高阶项未完整求解。 | author-model-limitation | direct-original | PDF p.2；p.4 Fig.1前后；p.15 Conclusions | true |
| AL11-D21-R51-3 | QQ/BK模型的壳空间、B=.5、κ自洽校准和80%配对隙为计算输入；两转动spurious modes的稳定解耦由作者报告，本文任务未复现。 | model-input-and-numerical-claim | direct-original | PDF pp.2–3 Eqs.1–5/Table I；p.7 | true |
| AL11-D21-R51-4 | 带间率取RPA，带内率取TAC；某些向更高spin的分量因过低或负Eγ不可观测。二者不是两套独立实验验证。 | model-observable-contract | direct-original-and-scope | PDF p.7；pp.10–11 Eqs.15–18 | true |
| AL11-D21-R51-5 | 声子性质需形状/取向振幅分析；多数所算案例取向振幅主导，角振幅约30–40度起步并在失稳附近发散；134La有较强混合，未给135Nd的本核同类数值。 | author-model-result | direct-original | PDF pp.11–16 Sec.IV/Figs.11–14 | true |
| AL11-D21-R51-6 | 作者承认部分角动量趋势未再现；不同ΔI带间率比随N/Z快变，未发现通用的手征onset模式。 | author-limitation | direct-original | PDF p.16 Conclusions | true |
| AL11-D21-R51-7 | Eqs.21–26及Appendix A是线性振幅分解；角坐标反演含取向/形状相关分母，退化轴或形变消失时不能无条件反演。 | model-formula-and-derived-domain | direct-original-and-algebra | PDF p.13 Eqs.19–22；p.14 Eqs.23–26；pp.17–18 A3–A17 | true |

## Nuclear Structure Information

普通手征伙伴为同宇称；有限系统的精确本征态不是固定的左/右经典构型（p.1）。这里讨论的均场静态构型与有限核实验伙伴态之间仍有量子涨落和隧穿，不能把均场临界频率直接登记为实验相变点。

## Authors' Interpretation

N=75附近部分模型解以取向振动为主；接近壳闭合或非谐区时性质改变。作者提出需超越谐近似，不以一个固定B比模式覆盖所有核（pp.15–16）。

## Model Results

两类转动spurious modes分别为E=0和E=ℏω（p.7）；模型自洽/解耦是本征解的必要数值检查。我们没有程序和实际输出，故只能记录作者报告，不认证重现。Table II横线与RPA失效域保留，不能作为缺失的实验误差条。

## Competing Interpretations and Limitations

原文p.2保留134Pr形状与取向耦合和非手征解释。本文近谐假设并未排除这些竞争解释，也没有用邻核成功拟合排除135Nd其它组态/混合可能。未得135Nd预测参数域Θ、原branch/job/response/jointCov，不能计算真实排他检验或新CI。

## Analytical Reconstruction

本任务仅作两个有限运动学练习：由A3–A6验证形状微分反演；冻结其它自由度，选R3=e^(−iφJ3)约定，将Eq.A10的线性2φ与精确sin(2φ)比较。它们不运行TAC/RPA，不给135Nd改正因子，不把文中的声子角振幅直接当经典摆幅误差。计算记录`small-amplitude-domain-051.json`，长期公式边界同时见[[day21-135nd-same-input-falsification-design]]。

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: [[mukhopadhyay-2007-135nd-chiral-vibration-static]]已有近临界失效声明，但详细方法/本核参数尚缺。
- Effect: limits；真实后续核实了模型域，未补实验输入。
- Persistence: 本source与现有暂定设计页；不新增邻核实体/案例，不扩展课程卡。
- Review state: unreviewed，全部新claim保持needs_review true。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[mukhopadhyay-2007-135nd-chiral-vibration-static]] | 原135Nd解释的方法后续；共享实验，不计独立复测。 |
| limits | [[day21-135nd-same-input-falsification-design]] | 要检验近谐预测，须先取得本核参数和有效域；不能填邻核表值。 |
| foundational-background | [[frauendorf-meng-1997-tilted-rotation-chirality]] | 有限系统、TAC与左右运动的关系。 |

## Human Review Triage

### P0

P0: none identified。版本日期不一致、未核VoR和缺本核producer已显式隔离，不以它们作排他科学认证。

### P1

AL11-D21-R51-1/2/5/7：重要风险是将方法普适性当135Nd实证，或将大振幅运动学示例当实际RPA误差。后续写作应核各自精确locator与本核预测；目前保留未审。原件读到的理论结果、Agent代数域与未得实际job分别记录。

### P2/P3

书目、版本/hash和索引导航已核；raw归档deferred，citation key未取得，不改本地Bib。

## Extracted Pages

沿用既有方法与主案例页面；不创建邻核实体页，理由是当前任务只需主案例推断边界。

## Non-source Notes and Follow-up

最高信息输入仍是135Nd本核branch/成分与原模型job；若只取得其它核参数或文稿图，不将“可运行”说成原结果可复现。

## Day21 checkpoint113：TAC+RPA小振幅谐振子近似破缺与软化点推断边界

124定向纠正：用AL11-D21-R51-2/7；2phi与sin2phi是冻结自由度的运动学示例，不给实际声子非谐误差或20/45度普适阈值；软化可表征均场失稳，不能称纯伪影。本节旧全文与脚本保留为历史，不恢复原件阅读/科学认证。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AL11-D21-R113-1 | superseded：124撤回本条过强科学认证；用AL11-D21-R51-2/7；2phi与sin2phi是冻结自由度的运动学示例，不给实际声子非谐误差或20/45度普适阈值；软化可表征均场失稳，不能称纯伪影；旧全文保存在superseded-124。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
| AL11-D21-R113-2 | superseded：124撤回本条过强科学认证；用AL11-D21-R51-2/7；2phi与sin2phi是冻结自由度的运动学示例，不给实际声子非谐误差或20/45度普适阈值；软化可表征均场失稳，不能称纯伪影；旧全文保存在superseded-124。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |

## Day23内的Day24无学分预习：m分量与实际γ身份

本轮只定向回读原arXivv2 PDF7/8/10/11的RPA/TAC角色、135Nd not-shown范围和Eqs15–18；fresh视觉PDF11及关键式，实际暂存PDF SHA becba964421bb8860fa657865071df117622a492a2bbb2b23d661d235296f29b相符。未新称重读18页或重跑TAC/RPA，raw归档槽仍deferred、旧flags保留。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AL11-D24P-001 | Eq17把P-frame算符旋转到L-frame，m明确对应I→I−m；Eq18分别给这些component的B。E2可含m0/±1/±2，M1可含m0/±1；正B矩阵元不保证某I→I+1/+2支路能放光，作者说明低/负Eγ会使其不见。本文135Nd结果not shown here，不能由邻核不同m曲线给MU07某marker补Eγ/Jf，亦不能将同图M1/E2自动当同一混合γ的两个分量。 | original-RPA-component-and-identity-boundary | direct-original-and-bounded-inference | arXiv0709.0969v2 PDF10 Eqs.15–17; PDF11 Eq.18 and following paragraphs; PDF8 final paragraph | true |
| AL11-D24P-002 | Eq18的振幅平方是该近谐模型约定的transition strength，不是对选中γ出口归一的photon branch。把B接到光子率仍需能量的Eγ^(2L+1)和相同母态/方向；RPA波函数/quasiboson归一、全衰变分支和选样条件概率是不同归一。这个区分是本任务结合率定义的推论，不认证135Nd实际producer。 | model-strength-versus-selection-normalization | source-formula-plus-task-inference | arXiv0709.0969v2 PDF7 RPA amplitudes; PDF11 Eq.18; LKH82 printed121 Eq.2.2 | true |

实际率定义回链[[lange-kumar-hamilton-1982-multipole-admixtures]]；[[mukhopadhyay-2007-135nd-chiral-vibration-static]]的新归一诊断仅是明确compound binding hypothesis，不能由本文“not shown”缺口填成原数据或完整模型重现。

## Day24主线核验：共同转频、有限窗口与模身份

本轮回读arXiv0709.0969v2全部18页主线文本，fresh contact sheet PDF3–18覆盖14图/两表；另以单页分辨率核PDF5/7/14/15/16的TableII、Fig3、Eqs24–26及交叉/结论段。实际使用仍为`tmp/day21-checkpoint051/almehed-2011-arxiv07090969v2.pdf`，SHA与页首一致；原raw归档槽不存在，未创建或改raw，也未声称已核VoR。本文没有提供135Nd逐行job或实验branch，故该缺口在本轮可核范围已确认，后续不再为此机械回读。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AL11-D24-001 | Fig3图注明确实验比较量是共同ℏω网格上插值所得的两条experimental routhians之差；PDF7正文也把RPA splitting定义在给定ω。它不能未经Legendre/自旋映射直接替换为同I的EB(I)−EA(I)。本文Fig4–10还须保留各自核素与ΔI分量，不能给未展示的135Nd补具体值。 | model-data-comparison-coordinate | direct-original-and-bounded-inference | PDF7 Fig3caption and precedingparagraph; PDF9 Fig4caption | true |
| AL11-D24-002 | PDF4明确两种失稳：φ0平面进入aplanar、再由aplanar退出至absφ90平面；136Pm TableII的φ在ℏω=.10/.15为0，.20/.25/.30/.35为20/38/52/77度，.40/.45/.50为90度。中间四行RPA列是横线，不是测得零能；返回平面后Ω列为.15/.33/.42。它是该2qp模型的有限chirality窗口，不是135Nd实验临界值或任意更高spin都更静态的定理。 | model-phase-window-and-missing-value-identity | direct-original | PDF4 firstthreeparagraphs; PDF5 TableII 136Pm; PDF8 Results | true |
| AL11-D24-003 | PDF15将134La若干振幅曲线大跳变归因第一/第二RPA模交叉，并认为该模型的134La最低模不能再视为纯chiral vibration；不是全核实验模式否定。PDF7另列Jz诱发的E0与J+诱发的ℏω两个转动spurious modes，作者报告与physical模解耦。故跟踪最低ordinal/看到零频本身不足以判模身份；实际分量、norm/解耦与跨ω连续性仍需producer才能重验。 | mode-identity-and-numerical-readiness | direct-original-and-explicit-task-design | PDF15 134Laparagraph; PDF7 spuriousparagraph; PDF9 Fig4 | true |
| AL11-D24-004 | 形状/取向反演用Eq2的BK修正QQ张量（正文省略BK下标），而Eq15的physical E2算符采用ep=1+Z/A、en=Z/A；二者不因同写Q就当同一观测张量。本文Eq1邻奇奇核计算gap取80%奇偶质量差，不覆盖MU07给135Nd质子50%/中子80%的特定输入；同方法谱系不等同actual input完全相同。 | operator-and-parameter-lineage-boundary | direct-original-and-cross-source-comparison | PDF2 Eq1; PDF3 Eq2/BKparagraph; PDF10 Eq15; MU07 printed172501-3 pairingparagraph | true |
| AL11-D24-005 | 从A10/A15/A17构造φ0局部Jacobian，并独立用Cartesian traceless tensor旋转微分检验：TableII共55行中30个φ0行的normalized orientation condition number约2.712–6.678；脚本共157个有限数学控制通过，最大微分残差约1.34e−10。此欧氏坐标条件数不是模式权重/CI/质量张量；显示所选几何未被迫处在坐标奇点，不把真实软化一概归为坐标伪影。φ90/aplanar行未用本chart反演，球形/轴对称/Euler极限分别检查。 | source-grounded-local-coordinate-exercise | declared-Jacobian-and-independent-Cartesian-check | PDF14 Eqs24–26; PDF17–18 A10/A15/A17; PDF5 TableII | true |

`system/scripts/day24_al11_tensor_conditioning.py`读取实际PDF5，不执行论文代码。所有数学推导、spin/routhian坐标区分和有限窗口跨来源REFLECT固化在[[135nd-chiral-partner-resolved-evidence-map]]；数值不补135Nd输入、RPA振幅或新寿命/δ/g。原review flags保持，新增needs_review:true。

### Day24 checkpoint002 Agent self-audit triage

P0: none identified（本次新增范围）。P1：AL11-D24-001/002的frame/核素/横线身份原件已核；AL11-D24-003的ordinal/零模区分仍缺原producer而明确隔离；AL11-D24-004不把BK模型tensor升格为实测电荷形状；AL11-D24-005的Cartesian检查只核局部运动学。后续论文/关键问答需逐claim回这些locator，不以自审改为human-reviewed。
