---
type: source
title: "223Ra原α角关联：校准reference身份、混合比相位与重叠分量"
aliases: [Jones1998 Ra223 alpha gamma, 223Ra alpha electron reference]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: experimental-structure-article
reading_depth: deep-read
title_original: "A study of 223Ra populated by alpha-decay"
authors: [G. D. Jones, P. A. Butler, T. H. Hoare, P. M. Jones]
journal: European Physical Journal A
year: 1998
volume: 2
pages: 129--141
doi: "10.1007/s100500050101"
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "doi:10.1007/s100500050101 publisherPDF"
source_url: "https://link.springer.com/content/pdf/10.1007/s100500050101.pdf"
raw_file: "raw/papers/gpt/day16-20261018/jones1998-223ra-alpha-19d50c6b0b8b.pdf"
raw_sha256: "19d50c6b0b8bf558839253cedb766a758fed89102bd95f9a9420484092dc164d"
raw_storage_status: publisher-staging-verified-raw-archive-deferred
nuclei: [223Ra, 227Th, 227Ac]
reactions: [227Th-alpha-decay]
observables: [alpha-gamma-angular-correlation, alpha-electron-angular-correlation, multipole-mixing-ratio, conversion-coefficient, magnetic-moment]
methods: [Legendre-fit, Rose-Brink-convention, reference-identity, source-lineage]
tags: [calibration, conditional-spin, overlapping-transitions, finite-solid-angle, covariance]
---

# 先识别α门、母态与粒子通道，再谈偏振reference

## Bibliographic Record

G.D. Jones、P.A. Butler、T.H. Hoare、P.M. Jones，*European Physical Journal A* **2**,129–141(1998)，DOI[10.1007/s100500050101](https://doi.org/10.1007/s100500050101)。Crossref核题名/作者/卷页；原PDF由[出版商实际链接](https://link.springer.com/content/pdf/10.1007/s100500050101.pdf)HTTP200取得，13页、%PDF及身份/hash核准。当前原件在`tmp/day16-ni60-reference/jones1998-discovery/publisher-pdf.pdf`，raw槽尚未归档，不修改原材料/Bib。

此文是[[jones-2002-calibration-compton-polarimeters]] Table1/Ref12的原α–γ数据源；2002新增理论P列不构成第二次独立采集。1998又称1990Ref15为本工作的早期short report/装置说明，尚未凭此确认exactevent overlap。

## Scope and Reading Depth

本session读完整13页Sections1–6和References，视觉核9图、3表及影响判断的公式/partial level schemes。主线为旧spin假设问题→α/γ/e装置→solid-angle与phase fit→逐level/重叠峰→magnetic observables及rotor/Woods–Saxon解释→局限与结论。

本轮用途限定在Day16混合比/相位、matching companion与Day17校准知识预习。读到结构解释不等于另开形变/寿命课程；没有重测Jπ、δ、g因子或β3。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| J98-1 | 源为约10µCi227Ac、4mm直径spot蒸发于厚Au；建立secular equilibrium后，227Ac β−→227Th α→223Ra。不是无门单γsource的普遍已知P。 | acquisition-identity | direct | p130 Sec2 | true |
| J98-2 | Be-window低能HPGe测γ，100mm²/3mm厚Si(Li)测电子；5个8mm孔PIN测α，角180/155/135/115/90°相对Ge，距离Ge/SiLi/PIN=9/5.5/3cm。α分辨率约25keV、低于250keVγ约1keV、electron150keV附近约2.5keV，未给逐峰门/完整response。 | geometry-and-readiness | direct | p130 Sec2；Ref15 | true |
| J98-3 | 初fit W=ΣAk Qk Pk，Qk是solid-angle correction，experimental a2/a4=Ak/A0不依赖spin假设；theoretical列来自指定J1/J2/δ的fit，二者不是两个独立实验observable。Qk不等于Compton sensitivity Q。 | coefficient-layer-and-fit-object | direct | p130 Sec3；Table1 caption | true |
| J98-4 | 取227Th ground J=1/2、223Ra ground J=3/2的外测spin，并按systematics假定两ground parity正。spin0α的pureL使daughterpoint布居m±1/2等分；γ混合式采用Rose–Brink Ref17，作者明确δ符号可能异于部分γγ分析。spin/EM/phase/order须整体保存。 | source-state-and-convention | direct-and-Codex-CG-check | p130–131 Sec3；Ref17；本页point布居式 | true |
| J98-5 | pure multipole fit仅scale、4df；mixed另fitδ、3df。文中0.1%阈值S²=18.47/16.27用于fit拒绝，不是1σ δ范围；标准误差程序指Ref18/JT74。没有实际jointCov/峰面积不能重建原CI。 | fit-and-error-procedure | direct | p131 Sec3；Ref18 | true |
| J98-6 | 同314.78keV两原角关联分别是376.278(7/2−)→61.431(7/2+) E1与445.00(9/2+)→130.172(9/2+) M1；Fig8分别plot/fitted，非只靠Eγ匹配。Point理论P90分别−15/16/+.96，2002表舍入为−.94/+.96。原α能窗口数值仍缺。 | matched-reference-identity | direct-and-point-calculation | p135 Sec4.6；p139 Fig8；Table1两314.78 | true |
| J98-7 | 113.159峰由174.58→61.431 E1和174.62→61.431 E2组成，母态差.04keV远小于约25keVα分辨。γ a2=−.18(.01)、a4=−.035(.015)为composite；不能当单纯transition求δ。 | actual-unresolved-companion | direct | p132 Table1双星行；p133–134 Sec4.2；Fig3 | true |
| J98-8 | 旧αT(E1)=.362、αT(E2)=5.78使等总分支时E1光子约为E2的4.98倍。作者用四角α–eL/eM及L/M强度相容性判断E2电子分量主导，再在忽略E1电子贡献的条件下赋174.62为11/2+。该companion是另一particle选择，不是同γ数据四种处理。 | conversion-companion-and-weights | direct-and-conditional-arithmetic | p133–134 Sec4.2；p131四electron角；Fig3 | true |
| J98-9 | 用印刷pure系数同层mixing、固定理论时，由a2/a4分别得E2光子份额.1923/.1458，字面marginal±1σ区间重叠；法向残差.0087小于任意允许Cov下σ下界.0093。此为条件相容性诊断，非actual联合fit/CI、真实分支份额或新Jπ。 | conditional-mixture-design | printed-input-calculation | Table1 composite113.159行；本页mixture公式 | true |
| J98-10 | 342.84的J9/2+是rotational systematics favoured，原角关联只排5/2、未唯一排7/2；其δ据假设J列出。Table2只有29.858/31.58的δ符号由当前α–γ研究支持，其余统一正号取自物理gR选择，不能称六项独立实测符号。 | conditional-spin-and-sign-boundary | direct | p135 Sec4.5；p138–139 Table2前后 | true |
| J98-11 | 47行point模型的Racah/helicity两路线误差≤7.92e−15；native/RB连operator转换0差。36行2002对应a2/a4和P都在声明的两位小数舍入cell内；1998中央理论有8行不闭合，允许δ中央舍入cell后剩6行，保留输入/程序/版本边界，不称原实验被否定。 | printed-theory-replay-and-boundary | two-mathematical-routes-and-source-crosswalk | p132 Table1；J02p457Table1；本页对照/舍入规则 | true |
| J98-12 | 342.84/G62.45原Table1写δRB=+.29、theorya2=.24；当前同假设point模型给−.8568，而oppositeδcontrol给+.2452，a4均.04836。不能擅改原δ号或凭控制修复实验；J非唯一、actualfit/producer缺失亦需保留。 | isolated-sign-sensitive-nonclosure | visual-source-and-failure-control | p132 Table1 parent342.84/G62.45；p135Sec4.5；roundingcontrol | true |
| J98-13 | β3≈.05、gK相近与octupole支持来自rotor/constantQ0、选定δ符号与Woods–Saxon模型链。作者同时指出14%负宇称bandheadµ误差不足以强约束。不是由角关联单独直接观测八极形状。 | author-interpretation-and-model-boundary | direct-author-limit | pp137–140 Sec5；Tables2–3/Fig9；Sec6 | true |

## 原装置与phase合同

α方向作为z、parent unpolarized1/2、α自旋0且单L时，`C(Jm,L0;1/2,M)`要求`m=M=±1/2`。独立CG对J=1/2…11/2的两个允许L均给这组归一density；只有parity/triangle选L后才对应原衰变。真实finite source/PIN/γ接受角不能由point布居自动认证。

原γ式的interference为`2δ Rk(L,L+1,J1,J2)`。本run用RB δ并与native相邻M1/E2振幅`δ_native=−δ_RB`同步转换operator，相同W/Q/P；仅换δ符号/仅换EM标签会改observable，属于失败控制。原文没有给每条actualproducer的矩阵/δ扫描文件。

仅按point source、PIN孔半径4mm、距离30mm作uniformcap设计，半角7.5946°，参考轴attenuation component `Q2=.9868803`、`Q4=.9567137`。该量来自`Qk=∫c^1Pk(x)dx/(1−c)`，不包括4mm源spot、Ge固体角、门/散射/材料；不是已恢复原完整Qk，更不是polarimeter Q。

## 113.159：光子、总衰变与电子的分母

设f为同一corrected photon coefficient层的E2角平均A0份额：

`a2=(1−f)(−.33)+f(.45)`，`a4=(1−f)0+f(−.24)`。

从印刷central得到`.1923077/.1458333`，固定theory的marginalσ为`.0128205/.0625`，字面区间重叠`.17949… .20513`；它不是联合置信集。法向`n=(.24,.78)`的residual `.0087`，任意满足两给定marginalσ的PSD Cov使其σ在`.0093… .0141`；不能因两个central份额不同就判模型冲突，也不能据此恢复actualfit。

在声明同响应/branch条件下，总E2份额为

`Ftotal=f(1+α2)/[f(1+α2)+(1−f)(1+α1)]`。

两central分别映到`.5424/.4594`，说明“较小光子份额”并不等于“较小总衰变”。等总分量时`Iγ(E1)/Iγ(E2)=(1+5.78)/(1+.362)=4.97797`。原L/M选择还需各subshell系数/效率与背景，本文没有列可重拟的L/M峰面积；不把αT总系数直接替代αL/αM，亦不把角平均f借作任意单角探测count权重。

## 原表与2002理论列

两表的experimental角系数是同源转录。2002列出36个本次对应行，已重新列部分theory与新增理论P；不是36次独立偏振测量。

| identity：母态/Eγ keV | 1998 theory a2/a4 | 2002 theory a2/a4 | 当前point中央值 |
| --- | --- | --- | --- |
| 334.38/272.93，δRB8.5 | −.14/0 | −.17/.11 | −.171877/.107358 |
| 342.84/212.65，δRB−.35 | .60/0 | .61/−.06 | .605875/−.059526 |
| 376.28/296.51，δRB−.16 | .01/.02 | −.02/.02 | −.024426/.016301 |
| 445.00/383.52，δRB−.46 | .49/.10 | .51/.11 | .510660/.108870 |

“不闭合”只指声明point/phase/spin、印刷δcentral与±.005系数cell的数值合同。初47行中央有8项；再解δ最后一位半宽（两位小数±.005、一位±.05）与a2/a4同时cell交集后，250.35/201.60可被中央舍入解释，其余205.03、272.93、212.65、342.84的62.45、296.51、383.52仍不闭合。显示为0的列也按声明±.005诊断；原作者的truncation规则/未舍入fit未得，不能把这个自设representation门当source正式精度或统计拒绝。

尤其342.84/G62.45的相反号control不能据此“修正”为−.29。原J本身附条件，source table/phase解释和actualprogram需要独立核；此处只保留可复现的强sign敏感反证。

## Summary

原件支持确切的reference母态、源布居与α–γ/α–electron companion链，限制只凭γ能/标签/单值阈值选择混合比或校准P。理论重放不是原event/response拟合，也不将2002同表算成独立实验。

## Competing Interpretations and Limitations

- 1990装置/shortreport是同工作谱系入口，尚未取得其正文/逐门ledger；不能仅按年代或同作者判exactevent全部共享，也不能宣称独立重复。
- 0.1% S²拒绝门、标准误差和printedcentral舍入各是不同对象；缺原jointCov/Qk与数值δscan，未重建置信域。
- 113.159的electron选择提供不同响应的companion；原L/M强度比未以可重拟数字给出。纯电子E2近似是作者条件，不能转换成“γ峰纯E2”。
- 两314.78原Fig8确实分列differentparent fits；本页不主张实际γ谱无法分离或原α门错配。具体α能窗和背景仍未恢复。
- 342.84/G62.45的非闭合已隔离，不更改PDF/旧spin/δ，也不由此否定整篇实验。所有新claims needs_review，非human-reviewed。

## Knowledge Impact and Learning Decision

`supports`matching reference/gate/particle对象及相位整体转换；`revises`“仅有2002校准表、原α–γ数据未读”的缺口；`limits`literaltheory列、附条件spin/δ符号与模型解释的实验化。当前仍Day16正式一次、Day17无学分preview，不开Day18。

## Extracted Pages

- [[jones-2002-calibration-compton-polarimeters]]：原数据谱系、理论P与source版本分层。
- [[compton-polarimetry]]：同能标不同母态、光子/电子选择与reference纯度。
- [[multipole-mixing-ratio]]：RB/native桥与附条件spin/sign赋值。
- [[internal-conversion-analysis]]：total/γ/subshell权重不可混用。

## Reproducibility

[原表/phase程序](../../system/scripts/day16_jones1998_reference_audit.py)、[舍入交集程序](../../system/scripts/day16_jones1998_rounding_audit.py)，实际exit0。输入v1的46行人工清单保留；v2在完整分析前补329.86/300.00及2002首行对应，47条以parent/Eγ复合键区分。依赖为已有repo SymPy1.14.0，原PDF/J02raw不变。

[完整主线/视觉记录](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/jones1998-full-mainline-reading.json)、[结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/jones1998-reference-audit-result.json)与[舍入结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/jones1998-rounding-audit-result.json)仅证明本run执行。长期可引用的版本、条件、数与反证保存在本页原子claims。

### 后续官方对象与回忆纠正

[[nndc-2001-223ra-reference-and-2026-intensity-records]] N223-1–10已核旧评价2003Jπ/2012NR修改与2026编译的不同层。旧MR62.45 unsigned0.29(5)不认证正号；新XUNDL只有2019绝对Iγ且全部MR空。&未分/ @已分的两版强度保留，不用其RI强配本实验α门或解释全部theory非闭合。

主动回忆曾误写该62.45终态为61.431，已用官方能量记录纠正：342.654到280.182为相容候选，281.42才带FL61.424；冻结回忆不覆写。47行算符原输入为正确Ji9/2/Jf7/2且不含错误Ef，既有角数不变。这一错误未进入本source原子claim的终态赋值；后续identity guard仍保留没有显式FL的界限。
