---
type: source
title: "Qi2009：135Nd全量子PRM、固定形变与版本参数边界"
aliases: [Qi 2009 Nd135 PRM, 135Nd particle rotor chirality]
created: 2026-10-23
updated: 2026-10-23
status: ai-draft
review_status: unreviewed
source_type: theoretical-paper
reading_depth: deep-read
title_original: "Chirality in odd-A nucleus 135Nd in particle rotor model"
authors: [B. Qi, S. Q. Zhang, J. Meng, S. Y. Wang, S. Frauendorf]
journal: Physics Letters B
year: 2009
volume: 675
pages: "175-180"
doi: 10.1016/j.physletb.2009.02.061
arxiv: 0812.4597v1
language: en
canonical_source: https://doi.org/10.1016/j.physletb.2009.02.061
citation_key: ""
raw_file: raw/papers/2009_Qi_135Nd_PRM_arxiv08124597v1.pdf
raw_sha256: 248546abd4a1d1597bf9ddf39cfffd5f09604802704204f0ff61647bbdb19346
raw_storage_status: public-staging-not-archived
nuclei: [135Nd]
models: [particle-rotor-model, tilted-axis-cranking, random-phase-approximation]
observables: [energy-levels, transition-probability]
methods: [angular-momentum-coupling, quantum-tunneling]
tags: [chirality, fixed-deformation, model-validity, version-boundary]
---

# 135Nd：量子隧穿的模型解释与可观测量分层

## Bibliographic Record

B. Qi等，*Physics Letters B* **675**, 175–180 (2009)，DOI [10.1016/j.physletb.2009.02.061](https://doi.org/10.1016/j.physletb.2009.02.061)。本次Crossref核作者、题名、卷页；arXiv API关联[0812.4597v1](https://arxiv.org/abs/0812.4597v1)，2008-12-25上传。实际读v1，不声称VoR逐字一致。

PDF16页、376923 bytes，实际暂存`tmp/day21-checkpoint053/qi-2009-0812.4597v1.pdf`；SHA256见frontmatter。raw_file是未写入的归档槽，hash对应实际公开暂存；raw未改。题头有November 9, 2018编译日期，与arXiv上传/期刊年份分开记录，不由此改年份。

## Scope and Reading Depth

- 实际读v1全16页文字：正文pp.1–9、refs pp.9–11、五图pp.12–16；视觉核pp.5–8及所有五图/图注。
- 先冻结已受Lv2019等priming的回忆，不作盲测。
- 未取得原PRM代码、波函数系数、数值job、拟合参数不确定域或VoR全文；不声称重现作者模型。

## Paper Question and Scientific Motivation

作者将PRM扩展到多价粒子/空穴，处理135Nd的πh11/2²⊗νh11/2⁻¹组态。全量子PRM保好角动量，能够处理近谐RPA不能连续描述的振动到隧穿过渡；代价是固定形变转子假设（pp.2–3）。

## Method and Design Logic

H=Hcoll+Hintr，Hcoll=Σ(Ik−Jk)²/(2𝓙k)，无旋惯量𝓙k=𝓙0sin²(γ−2πk/3)（pp.3–4 Eqs.1–3）；D2对称的强耦合基与单j壳形变势（pp.4–5 Eqs.4–8）。电磁算符细节转给Ref.26，本文没有列完整实现。

本v1 p.5给β=.235、γ=22.4度、Cp=.323/Cn=−.323MeV、Q0=4.0eb、gR=.44、gp=1.21、gn=−.21；𝓙0数值29.0按实验能谱调整。原页把其单位印为MeV/ℏ²，而Eq.2要求惯量单位为ℏ²/MeV。此维度边界保留，不静默改原文字或声称已核原job。Eq.8的粒子/空穴±号与Cn符号也应按实际实现核，不能在复现时重复施加符号。

## Key Evidence and Reasoning Chain

固定组态/形变与能谱校准 → 比较能量和电磁率 → 用模型RMS分量与投影概率解释手征几何及spin演化。后两者是波函数输出，并非直接测得的核内矢量。Fig.1/2实验数据来自Zhu2003/Mukhopadhyay2007，无新增采集。

## Summary

作者给出近39/2最接近静态手征、其前后为不同振动的模型图像。本任务得到了一组本核实际参数点及明确的固定形变前提，未得到参数域Θ或原实验分支。该v1参数与Lv2019转述/采用数值有差别，必须按版本分别记录；未核VoR时不宣布期刊原文错误。

## Experimental or Theoretical Setup

三准粒子耦合刚性三轴转子，单j壳Hamiltonian；𝓙0拟合能谱，Q0/g为采用的电磁输入。PRM与TAC+RPA对比重用同一组135Nd实验强度，理论方法不同不构成第二套独立电磁实验。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| QI09-D21-R53-1 | 全量子PRM能处理固定形变条件下振动到隧穿的过渡，角动量为好量子数；它仍假设形变固定，作者对γ软/形状耦合保留讨论。 | author-method-and-limitation | direct-original | PDF pp.2–3；p.4 Eqs.2–3 | true |
| QI09-D21-R53-2 | v1本核参数为β=.235、γ22.4度、Cp/Cn=±.323MeV、Q0=4.0eb与采用g；𝓙0数值29.0按能谱调整，打印单位与Eq.2维度不符，原job未得。 | model-input-and-version-boundary | direct-original-and-dimensional-check | PDF p.5参数段/Eq.8；p.4 Eq.2 | true |
| QI09-D21-R53-3 | Figs.1–2对照的实验来自Zhu2003与MU07；p.6承认带外E2被PRM/TAC计算低估，带内/带外率比对过渡细节敏感。摘要“excellent”不抹去此具体偏差。 | model-comparison-and-data-lineage | direct-original | PDF p.6；pp.12–13 Figs.1–2；p.10 Ref.20 | true |
| QI09-D21-R53-4 | 39/2处最接近静态、模型给剩余76keV劈裂且较好隧穿域仅限此spin；之后又出现不同振动。此为模型波函数/概率解释，不是直接测得静态构型或普适临界自旋。 | author-model-interpretation | direct-original | PDF pp.7–9；pp.15–16 Figs.4–5 | true |
| QI09-D21-R53-5 | Figs.3–4箭头/分量来自sqrt〈Jk²〉；它们不保符号，不等于〈Jk〉或同时确定的经典矢量，单靠三轴RMS非零不能排他推出手征。作者另用了Fig.5投影概率。 | model-output-and-our-boundary | direct-original-and-angular-momentum-algebra | PDF p.6定义；p.7 Eq.9；pp.14–16 Figs.3–5 | true |
| QI09-D21-R53-6 | Fig.2仅标in/out和B(M1)/B(E2)，未给γ能量/逐线成分表；它没有为MU07每个E2点补唯一初末态/分支。 | evidence-scope | direct-original | PDF p.6；p.13 Fig.2 | true |

## Nuclear Structure Information

同一固定组三准粒子PRM给出随spin变化的波函数取向分布。原文39/2的模型判断与作者关于有限核量子隧穿的解释绑定；不得用“rigid core”这一模型输入反过来认证真实核γ刚性。

## Authors' Interpretation

低spin绕s-l面的手征振动、39/2附近减弱的左右隧穿、较高spin向l-i面的另一振动；作者称手征为transient现象（pp.7–9）。这支持保留动态边界，不能把所有可疑双带套进同一个spin阈值。

## Model Results

γ22.4度给无旋惯量比约6.8:2.6:1（p.6）。重新代公式得6.7659:2.5636:1，仅核模型几何/舍入，不测真实惯量。图中R/Jp/Jn是模型RMS，未得带符号的原波函数系数或联合取向分布。

## Competing Interpretations and Limitations

固定形变、单j空间、电磁算符输入与𝓙0拟合限制外推。p.6的带外E2低估是具体剩余张力，不被整体能谱再现解除；未得联合Cov、模型误差合同，不能给其统计显著性。本文不提供MU07原branch/response。

版本差异：本v1(.235,22.4,29.0)与[[lv-2019-chirality-135nd-reexamined]]所述(.24,22.2，2019再用20.2/23.5)分开；需VoR或实际原job解释差别，不能直接拼成一个参数域。

原文p.7–8用P(Ki=0)/P(Ks=0)解释节点，但该核I为半整数、Eq.6/9基的K为离散半整数；未得作图网格/平滑约定时，不把图文“0”当作精确离散K=0本征投影概率。这是待核的表述/实现边界，不据此否定原模型。

## Analytical Reconstruction

声明L2角动量反例：一般自旋态|j,m=j〉有〈Jx〉=〈Jy〉=0，〈Jz〉=j，但sqrt〈Jx²〉=sqrt〈Jy²〉=sqrt(j/2)>0，sqrt〈Jz²〉=j。三轴RMS均非零仍不能确定三轴平均取向或手性。j=19.5只是运动学示例，非135Nd实际PRM态；不据此声称作者模型无手征。代码`day21_checkpoint053_prm_geometry_scope.py`同时给矩阵/解析恒等式与惯量比，实际波函数/CI字段null。

## Knowledge Impact and Learning Decision

- supports：本核具体参数点及作者超越近谐的模型解释真实存在。
- limits：固定形变、校准/版本和几何可观测性，参数点不等置信域Θ。
- persistence：source、既有暂定设计/方法；不新建其它核素案例。
- review：全部新claim needs_review true，未发生用户审阅。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[mukhopadhyay-2007-135nd-chiral-vibration-static]] | 同核实验的全量子PRM解释，非新数据。 |
| limits | [[almehed-2011-chiral-vibrations-a135]] | 比较近谐RPA与固定形变PRM；方法优势不消除各自假设。 |
| methodological-bridge | [[day21-135nd-same-input-falsification-design]] | 从缺参数缩小到版本参数点已得、job/Θ仍缺。 |

## Human Review Triage

### P0

P0: none identified；单位、版本/离散K表述边界已隔离，不用于声称复现或排他实验认证。

### P1

QI09-D21-R53-2：VoR/原job需核𝓙0数值/单位、Cp/Cn符号以及与2019版本差别；按已知数值独立建模也只能标本任务模型。QI09-D21-R53-4/5：RMS箭头与Fig.5概率不能转成实验观察的带符号构型；半整数K的“零点”需实际网格定义。QI09-D21-R53-6：具体E2成分绑定仍缺，后续应取原实验输入而非重复抄图。

### P2/P3

Crossref/arXiv身份、版本/hash与索引已核；raw归档deferred，citation key未取得，不改本地Bib。

## Extracted Pages

沿用135Nd及现有模型/方法关联，不建立重复模型/核素页。

## Non-source Notes and Follow-up

下一有界路线为VoR或作者最终版参数/公式核对；未取得时不以预印本与后文差异反判作者错误。原实验成分、response/jointCov仍是独立输入缺口。

## Day21 checkpoint112：PRM流体转动惯量比、手征几何与跨带E2低估审计

124定向纠正：用QI09-D21-R53-1至6；实际文件是arXiv v1，非已核VoR；三轴主要取向不等精确正交经典矢量，RMS是非负而非普遍严格正。本节旧全文与脚本保留为历史，不恢复原件阅读/科学认证。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| QI09-D21-R112-1 | superseded：124撤回本条过强科学认证；用QI09-D21-R53-1至6；实际文件是arXiv v1，非已核VoR；三轴主要取向不等精确正交经典矢量，RMS是非负而非普遍严格正；旧全文保存在superseded-124。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
| QI09-D21-R112-2 | superseded：124撤回本条过强科学认证；用QI09-D21-R53-1至6；实际文件是arXiv v1，非已核VoR；三轴主要取向不等精确正交经典矢量，RMS是非负而非普遍严格正；旧全文保存在superseded-124。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |


## Day21 checkpoint125：正式版本访问边界的实际复核

source前primed回忆已在本轮网络请求之前冻结。Crossref精确DOI返回期刊VoR的TDM链接与PII S0370269309003979。实际API XML HTTP200只有coredata，没有正文、公式或参数；ScienceDirect PDF路由HTTP403返回HTML，无PDF签名。因此没有取得VoR科学正文，不能比较参数或宣称预印本单位错误在正式版仍存。当前可用的科学locator仍是arXiv v1与R53，原job/Θ未得。请求/响应hash见本run source-retrieval-125.json；未写raw/Bib、未改变凭据或发送消息。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| QI09-D21-R125-1 | 2026-10-24实际Elsevier API对PII S0370269309003979返回HTTP200 XML，但根节点只有coredata，无正文；出版商PDF路由返回403 HTML。这个200只核书目身份，不证明可访问VoR全文，不改变R53参数版本边界。 | source-access-and-version-boundary | direct-response-inspection | https://api.elsevier.com/content/article/PII:S0370269309003979?httpAccept=text/xml | true |


## Day21 checkpoint126：公开机构元数据与正文不能混同

OpenAlex与Semantic Scholar的精确DOI记录均把可读OA指向已有arXiv稿。OpenAlex另给SUNScholar handle 10019.1/12355；实际机构页面题名、作者与2009年匹配，但没有下载链接。其公开DSpace item bed0e4c3-0a22-429e-a3e6-5c2fe95a4922的bundles API实际HTTP200、totalElements=0，未取得正文。仅限所查公开响应，不证明所有机构或正式版不存在。没有下载新PDF或SI、未用机构登录/凭据；125原VoR参数缺口保持。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| QI09-D21-R126-1 | 2026-10-24实际SUNScholar公开item的bundles清单返回HTTP200和totalElements=0；该同题同作者书目页不能当正式版PDF或独立模型复现。 | source-access-and-repository-identity | direct-public-metadata-response | https://scholar.sun.ac.za/server/api/core/items/bed0e4c3-0a22-429e-a3e6-5c2fe95a4922/bundles | true |

## Day23内的Day24无学分预习：Ref26准粒子PRM算符原件

本节独立标识本页Ref26的2007方法文，不将其当Qi2009的新数据或改本页元数据。S.Q. Zhang, B. Qi, S.Y. Wang, J. Meng，*Chiral bands for quasi-proton and quasi-neutron coupling with a triaxial rotor*，arXiv[nucl-th/0703047v1](https://arxiv.org/abs/nucl-th/0703047v1)，对应PRC75,044307(2007)、DOI[10.1103/PhysRevC.75.044307](https://doi.org/10.1103/PhysRevC.75.044307)。v1实际PDF200、738205bytes、25页、SHA256 601b90ca7163d90493d6288b5e031ed00ea7e350f06461f36b80b6551ce90aa8；tmp/day23-originals/zhang2007-qpprm-041.pdf，正式raw归档deferred。arXiv上传2007-03-15与文头June29,2018编译日期分开，不称已核VoR或改年份。

本次读完v1主线正文1–16页及公式、refs16–18与全部图注；视觉核pp6–8的BCS/EM公式、p19Fig1、p22Figs4/5、p23Figs6/7，其余图仅按文本/图注读，不宣全部数值点已精确核。属于Day23内已打开的唯一Day24无学分预习，completed仍[]、partial[23,24]、next23，未开Day25。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ZH07-D24P-001 | 原Eq8给BCS变换u²+v²=1，Eq10/11给准粒子能量sqrt[(ε−λ)²+Δ²]与v²=[1−(ε−λ)/ε′]/2。Hamiltonian单粒子矩阵及M1 Eq18明确采用f=uu′+vv′，M1算符在Eq16/18按(gp−gR)jp+(gn−gR)jn与各自pairing factor组合。只给常数g而没有逐轨道ε/λ/Δ/幅与相位，不能复现完整准粒子磁矩。 | original-BCS-and-M1-operator | direct-new-method-primary | v1PDF6 Eqs8/10/11; PDF7Eq16/17; PDF8Eq18 | true |
| ZH07-D24P-002 | Eq14/15的E2采用lab旋转intrinsicQ与Q0、γ及相同内禀标签的波函数重叠，另加时间反演sector的Term2；它没有列出粒子跨轨道r²C2矩阵或给这一E2式普遍乘uu′−vv′。不能把一般粒子E2的其它约定擅补到本文core tensor，也不能把单j qpPRM自动当Guo实际h/f多轨道QTR producer。 | original-E2-truncation-and-transfer-boundary | direct-new-method-primary-plus-bounded-synthesis | v1PDF7 Eqs13–15 and Term2 explanation | true |
| ZH07-D24P-003 | 本文固定纯h11/2质子、以BCS neutronλ从ε6到ε1模拟费米面/多空穴变化，例采用C=.3MeV、J=30MeV−1、Δn=1MeV、Q0=3.5eb和gp−gR=.7/gn−gR=−.6；Fig1另用固定λ1.227MeV。它是模型参数扫描，不是135Nd三准粒子实际谱的同H重跑或新实验。结论明确BCS真空中其它粒子对惯量贡献的近似，要求未来显式多proton/neutron和更真实single-particle potential。 | model-design-and-author-stated-limit | direct-new-method-primary | v1PDF8–9 SecIII A/B; PDF15–16 Conclusion; Fig1captionPDF19 | true |
| ZH07-D24P-004 | 作者模型中B(M1)/B(E2)两带接近可伴随两种绝对B各自差异；staggering随γ与Fermiλ强变，结论说它可能不是所有手征带的一般特征。λn=ε1的M1变小归于质子/中子取向和相反g贡献抵消，是本参数模型解释，不给任意核统一staggering/δ/B硬门，也不把ratio近合当两份独立absolute-strength观测。 | model-electromagnetic-pattern-and-limitation | direct-new-method-primary | v1PDF11–12 SecIIIC; PDF15Conclusion4/5; PDF22Figs4/5; PDF23Fig6 | true |

文中定义的RMS几何仍属模型波函数；不新增此前QI09已记录的RMS/半整数K反例充进度。本次新增信息是实际算符/pairing层与作者适用条件。[[nuclear-chirality]]和[[signature-tip-shears-discrimination-contract]]接续这些条件，[[guo-2022-low-spin-wobbling-187au]] GU22-D23-012/021的实际h/f含量仍需完整多轨道/径向/占据，未由本单j方法文自动补齐。新claims均needs_review:true，原QI09范围/其它人审flags不变。

## Day23内的Day24无学分预习：源BCS因子的矩阵组件

复用041实际读过的ZH07 Eq4/8/10/11/18，不新称完整PRM对角化或作者producer重放。以下均为任务数学/组件层，needs_review:true。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ZH07-D24P-005 | 在声明实非负u/v gauge下，Fμν=uμuν+vμvν是两列(u,v)的Gram矩阵，diag1、PSD、rank≤2，且0≤F≤1；不是所有轨道对同一常数。按原singlej j11/2/C=.3、fixedλ1.227/Δ1MeV，γ0/30/60三个组件点，在非零barej offdiagonal支持上的F范围分别约[.8854,1]/[.4626,1]/[.9583,1]，只说明配对因子矩阵非共同标量，不是核带M1抑制量或physicalB预报。 | source-parameter-BCS-matrix-component | original-equations-plus-declared-task-calculation | ZH07v1PDF5Eq4/PDF6Eq11/PDF8Eq18; Fig1PDF19; task input-contract042 | true |
| ZH07-D24P-006 | 对对称ξ=±x，plusfactor为Δ/sqrt(x²+Δ²)；Δ→0且ξ≠0时，同occupancy类factor1、异类0。若Δ=0且ε=λ，Eq11出现0/0，需要另给blocking/占据约定，程序保未定义而不填.5。源pureproton是另明确的配置条件，不能把这个数学边界当作者实验/模型错误。 | analytic-limit-and-occupation-boundary | source-definition-plus-task-algebra | ZH07v1PDF6Eq10/11; PDF9pure-proton conditions; task input-contract042 | true |

`system/scripts/day23_qp_pairing_factor.py`十二项源SHA、bareH解析/对称、BCS canonical/gap、Gram与极限控制通过，最大谱Kramers差1.8e−15MeV、Gram小负特征值浮点幅≤4.7e−15。bareH的Casimir检查只用于裸j；没有要求截断1qp算符在遗漏pair-changing sectors时独自实现完整生成元代数。未算rotor耦合核态、actualg/B/E2/δ、实验CI或机时。[[signature-tip-shears-discrimination-contract]]与[[nuclear-chirality]]保仅下一卡无学分预习及算符迁移边界。

## Day23内的Day24无学分预习：1qp因子与遗漏扇区的Fock检查

本节沿ZH07-D24P-001的Bogoliubov约定另作声明四mode数学例，不是该文核态或原PRMproducer；needs_review:true。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ZH07-D24P-007 | 在两Kramers对(A,barA,B,barB)的16维Fock空间、实u/v与源Eq8约定下，时间奇hopping的1qp A↔B块为uu′+vv′，时间偶同体hopping为uu′−vv′。完整odd sector由4个1qp和4个3qp态组成，算符作用的范数包含两者；plus²+(uAvB−vAuB)²=1、minus²+(uAvB+vAuB)²=1在声明例中成立。投影到1qp丢失的范数不代表实测γ强度丢失，也不能用它强判源模型生成元错误。 | declared-exact-Fock-projection-identity | source-convention-plus-task-algebra | ZH07v1PDF6Eq8/PDF8Eq18; task input-contract043 | true |

25个声明u/v设计点、十项CAR/BCS真空/时间宇称/投影/完整odd扇区检查通过，最大误差4.5e−16。所选θA=.2、θB=1的数学例中，时间奇1qp/3qp范数约.4854/.5146，时间偶约.1313/.8687；未赋核态能量、multipole、physicalg/B。toy T²=(−1)^N只校准此fermion约定，不将其误作手征C²或真实Kramers双带证据。[[nuclear-chirality]]和[[signature-tip-shears-discrimination-contract]]保Day24无学分与coreE2适用边界。

## Day23内的Day24无学分预习：明确无配对PRM的有限I闭环

本节求解ZH07源H的声明无配对p+hole极限：jproton=jneutron=11/2、C=.3MeV、γ30°、J0=30ħ²/MeV，惯量(1i,2s,3l)=(30,7.5,7.5)，Hintr=hsp,p−hsp,n。纯粒子/空穴的费米常量只移能量零点，在这里丢去；未重现源Δn=1的配对曲线，也未将整数I态映射为135Nd实际三准粒子/Pr/Au能级。原producer/实际EM和实验参数域仍缺。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ZH07-D24P-008 | 按源Eq6/7构D2强耦合基，K−Ωp−Ωn为偶数，反号对称phase=(−1)^(I−jp−jn)，维数D=(2I+1)(2jp+1)(2jn+1)/4；bodyI用anomalous分量(Jx,−Jy,Jz)，particle j正常。完整product H投影无扇区泄漏，两个小j自由转子解析谱与数值一致，有限I9/14/18的D为684/1044/1332。 | declared-finiteI-Hamiltonian-and-basis-implementation | source-formula-plus-task-quantum-model | ZH07v1PDF4–6 Eqs1/2/4/6/7; PDF9unpairedlimit; task input-contract044 | true |
| ZH07-D24P-009 | 上述固定无配对H的最低两个ordinal态在I9/14/18间隔约381.261/37.659/87.342keV；八项basis/自由极限/残差/不同seed-tol-ncv/Casimir/能量重建控制过，最大eigen残差1.6e−11MeV、重复谱差2e−14MeV。这些为任务模型能谱，不是实测level、全sourcepairedcurve重现或chirality终审。RMS用完整O Eψ范数，未将(E†O E)²当E†O²E；RMS非零仍不保符号或证明handedness。 | declared-model-spectrum-and-numerical-boundary | exactfinitebasis-plus-controlled-eigensolve | task input-contract044/unpaired-ph-prm044; sourceHlocators asZH07-D24P-008 | true |

`system/scripts/day23_unpaired_ph_prm.py`给固定H/embedding/solver/diagnostics分层。小j1/2+1/2、C0、各惯量30的I1谱[0,.1,.1]MeV和I2谱[.1,.1,.1,.1,.2]MeV对应允许自由coreR，最大差1.2e−16MeV；未通过调参匹配这些极限。目标I的Hcoll与Hintr重建、总I/裸jp/jn平方和从full-space作用核对，数值误差不是实验CI或modelerror预算。[[nuclear-chirality]]与[[signature-tip-shears-discrimination-contract]]承接有限体系的模式解释边界；仍只Day24无学分预习，新needs_review:true。

## Day23内的Day24无学分预习：同H的轴投影边缘分布

沿044完全相同的源无配对H，直接重算状态、对intrinsic Ωp/Ωn求迹得总I的ρK，再分别作I1/I2/I3的谱投影。不是原135Nd波函数或直接实验几何；该variant的I为整数，m=0在谱中，未转用原奇A半整数K“0点”字面。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ZH07-D24P-010 | 同H最低两ordinal态的各轴marginal距离不同：I14的TV(axis1)=.07143，TV(axis2/3)=.39553；I18 gap更大，却有TV(axis1)=.05755、TV(axis2/3)=.19361。TV只是该模型两个概率分布的描述量；小能隙、某轴分布/RMS近合不强制所有轴分布同样接近，更不提供handedness/相对phase或静态chirality认证。 | declared-sameH-quantum-marginal-diagnostic | finiteI-model-wavefunction-and-spectral-projection | task input-contract045/sameH044; QI09v1PDF7Eq9 probability premise | true |

`system/scripts/day23_prm_axis_marginals.py`七项ρHermiticity/trace/PSD、各轴P正归一、D2反射/一阶矩、二阶矩full-operator与直接K检查通过；最大二阶矩差1.2e−13ħ²。三个轴不对易，只能称各自边缘分布，不能把三个峰值拼成同时确定的经典矢量；概率接近也没有补足相干RME或完整几何。没有实验角度/概率、newδ/g/B/Q/τ/CI或机时。[[nuclear-chirality]]和[[signature-tip-shears-discrimination-contract]]保此范围，新增needs_review:true，Day24继续无学分。

## Day23内的Day24无学分预习：同H的EM约化矩阵

本节沿044无配对H和实际源ZH07 Eq15–18的coreE2/particleM1，先核张量归一/自由极限，再计算低ordinal态的模型矩阵。Q0=3.5eb、gp−gR=.7/gn−gR=−.6为原方法文采用的模型输入，不是新实验或实际135Nd/Au参数；它们不是detector Q(E)。未加particleE2、配对或未知径向量，未重现作者paired/multiqp producer。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ZH07-D24P-011 | 任务以Afi=Ef†Σν[CG(IiKi,λν;IfKf)⊗tν]Ei构约化角矩阵，RME=√(2Ii+1)A、B=|A|²乘源prefactor。coreE2 t0=cosγ、t±2=sinγ/√2；M1 tν=.7jpν−.6jnν。scalar identity、freeR0 proton-vector triplet→singlet normalizedB=.25、total-j interI0、complete vector .75/coreC2 1等十门通过，并核Hermitian reverse/D2映射。角闭合含formal upward/sameI，并非γ出口完整性；同I benchmark为声明向量而非包含gR I的完整静态磁矩。 | declared-source-operator-and-reduced-matrix-implementation | source-formula-plus-task-angular-model | ZH07v1PDF7Eq15–17/PDF8Eq18; task input-contract046 | true |
| ZH07-D24P-012 | 固定variant中，M1 Ii14→13的低2×2模型B约((2.01683,.002904),(.003114,2.21550))μN²，E2 Ii14→12约((数值近0,.140290),(.177171,数值近0))e²b²，行final/列initial均为ordinal0/1。I18时强M1转到offdiagonal而coreE2以diagonal为主。这些矩阵只描述特殊γ30无配对模型和能量排序；未赋实际band归属，不把近0当实测禁戒或普遍selectionrule。 | declared-fixedH-model-EM-matrix | finiteI-wavefunction-plus-fixed-source-operator | task prm-em-tensors046 rowsIi14/Ii18; sourceparams/operators asZH07-D24P-011 | true |
| ZH07-D24P-013 | 形式RME与开放γ出口须分：I9 ordinal0→If7 ordinal1的模型E2 B约.014488e²b²，但该fixedH中Einitial−Efinal≈−.416448MeV，是向上连接。所有固定If终态的形式强度范数也可含这种项，不能乘它作开放γ宽度/缺失branch或新机时。这里M1计算If=Ii−1、E2计算If=Ii−2，不是同一混合跃迁的两分量，未由二者反演δ。 | model-kinematic-outlet-and-mixing-identity-boundary | declared-H-energies-and-formal-RME | task prm-em-tensors046 Ii9/If7 rowfinal1/columninitial0; input-contract046 | true |

`system/scripts/day23_prm_em_tensors.py`十项门通过，最大矩阵reverse差1.8e−15、eigen残差2.6e−12MeV；两低final态只占固定If形式总强度的一部分，不能据低2×2表宣称projector封闭。[[nuclear-chirality]]和[[signature-tip-shears-discrimination-contract]]分别保model/probability/EM/experimental层次与唯一Day24无学分范围；新needs_review:true，无新measuredB/g/Q/δ/τ/CI或设施率/机时。
