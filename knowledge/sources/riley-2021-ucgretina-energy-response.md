---
type: source
title: "Riley2021：GRETINA有效被动层、能谱响应与偏振迁移边界"
aliases: [Riley2021 UCGretina response, GRETINA effective passive germanium layers]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: read
title_original: "UCGretina GEANT4 Simulation of the GRETINA Gamma-Ray Energy Tracking Array"
authors: [L. A. Riley, D. Weisshaar, H. L. Crawford, M. L. Agiorgousis, C. M. Campbell, M. Cromaz, P. Fallon, A. Gade, S. D. Gregory, E. B. Haldeman, L. R. Jarvis, E. D. Lawson-John, B. Roberts, B. V. Sadler, C. G. Stine]
year: 2021
journal: Nuclear Instruments and Methods in Physics Research A
volume: 1003
pages: "165305"
doi: "10.1016/j.nima.2021.165305"
arxiv: "2104.09986v1"
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "arXiv2104.09986v1 actual26pagePDF, CrossrefDOI metadata"
source_url: "https://arxiv.org/abs/2104.09986v1"
raw_file: "raw/papers/gpt/day16-20261018/riley-2021-ucgretina-2104.09986v1.pdf"
raw_sha256: "68644a73a5bb0ecb66ee504d162e0acdefa6a1e5b7c8dc44e846c322264364d1"
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [137Cs, 22Na, 57Co, 133Ba, 152Eu, 241Am, 56Co, 226Ra, 60Co, 88Y]
reactions: []
experiments: [LBNL-GRETINA-pencil-beam-source, NSCL-GRETINA-12quad-flood-source]
models: [Geant4, effective-passive-germanium-layers]
methods: [photopeak-efficiency-calibration, pencil-beam-scan, Compton-continuum-comparison]
observables: [gamma-ray-energy-spectrum, photopeak-efficiency]
tags: [instrument-response, geometry, calibration, polarimetry-readiness]
---

# 能谱匹配的有效参数与偏振响应需要分别验证

## Bibliographic Record

实际读取[公开arXiv v1 PDF](https://arxiv.org/pdf/2104.09986v1)，26页/806,228bytes，SHA256如frontmatter。Crossref DOI/题名/作者及arXiv版本元数据均HTTP200核准，PDF实际身份页相符。期刊记录为*NIM A*1003,165305(2021)，DOI10.1016/j.nima.2021.165305；未取得publisher VoR正文，不主张两版本逐字节相同。

PDF与渲染图放repo `tmp/day16-ucgretina/riley2021/`，raw归档槽尚未填。下载使用公开OA路径；SI检索对direct PDF无landing而未找到，不能据此认定作者没有补充材料。此前代码页对本论文的README引用不替代本页原读。

## Scope and Reading Depth

已沿完整主线读PDF1–23：物理/几何、LBNL pencil-beam、NSCL flood-source、单晶和全阵列有效层、photopeak与Compton continuum、限制及展望；24–26页参考文献核对其方法谱系，没有声称读完被引文献。12幅图全部在本地实际渲染并逐图查看，Table1/2和Eq.(1)回核。主动回忆在取得正文前冻结，明示已接触公开代码/Eu2012数据/Morse及源MC的priming。

本论文主线是NSCL标准12quad（2019–2020配置）及单晶扫描；[[ucgretina-2012-eu152-public-calibration-data]]是另一份2012七quad源数据。初始回忆问题把两者联系到一起，原件要求收窄这个预期。当前[[ucgretina-2024-geant4-11-source-replay]]也有不同SDK/几何/源recipe，不能由同仓库名称认证exact producer。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| R21-1 | 主线全阵列为NSCL12quad，4个在58°、8个在90°；另有LBNL type-A单晶pencil-beam采集。两类装置/观测分开，不能把公开2012七quad例称本论文同采集。 | apparatus-and-data-identity | direct-experiment-description | PDFpp5/7–8；Sec3–4；Fig2–3 | true |
| R21-2 | 原文代码使用Geant4版本写为4.10.05、EM option4；PhotonEvaporation/RadioactiveDecay由ENSDF衍生，支持用户level文件。版本/数据包关系不认证当前11.4.2 binary或原polarimeter。 | software-and-data-version | direct-method | PDFpp3–4；Sec2 | true |
| R21-3 | pencil-beam为1mCi137Cs、Hevimet1mm孔/87mm长、11mrad开角；5scan共100点，靠近central contact步长2mm，其余4mm。图4是同一组扫描的多条路径。 | measured-calibration-design | direct-apparatus-and-figure | PDFpp7–8；Sec3；Fig4 | true |
| R21-4 | 已知activity的22Na/57Co/133Ba/152Eu/241Am给absolute efficiencies；56Co/226Ra relative值缩放到1836keV以下的absolute数据，延至3548keV。共享缩放需保留，不能逐能峰当独立绝对校准。 | normalization-and-lineage | direct-experiment-method | PDFp8；Sec4 | true |
| R21-5 | 60Co/88Y与上游LaBr3:Ce coincidence另做absolute校验；continuum对象为GRETINA的1172-keV（文中另写1173）γ，gate在LaBr3的1332γ。这个target/gate角色不同于L25的1333target/1173gate。 | gated-response-identity | direct-experiment-selection | PDFp8；Sec4；Fig11–12 | true |
| R21-6 | Eq.(1)用Neymanχ²=Σ(Ni−Nsim_i)²/Ni，声明independent observations；此式没有显式finite-MC方差/共同归一Cov。continuum残差阴影另将data与sim的逐bin统计误差平方相加，不能混成同一fitΣ。 | fit-and-error-definition | direct-equation-and-text | PDFp9 Eq1；PDFp21 Sec6.3 | true |
| R21-7 | Table2按coaxial/back/outer列出单晶(2.09,2.8,.40)、全阵列I(3.0,2.0,.40)、II(1.5,2.5,.90)mm；两全阵列解来自同flood数据的不同能区选择，不是两次独立实验。 | fitted-effective-model | direct-table-and-method | PDFp15 Table2；Sec6.1 | true |
| R21-8 | 单晶coax fit还调Yoffset.9mm/rotation1°，随后5scans共用一个scale；2.091mm的quoted95% interval为.012mm。作者强调它只含限定模型空间的统计不确定度，不代表真实被动层测量精度。 | fit-nuisance-and-uncertainty | author-explicit-boundary | PDFp11 Sec5.1；Fig4 | true |
| R21-9 | back-layer由344–3548keV的17能量back-slice观测约束，低能点因难到back被排除；单晶back2.8mm的quoted95% interval .4mm同样是模型内统计范围。 | companion-observable-and-fit | direct-selection-and-quoted-model | PDFp12 Sec5.2；Fig5 | true |
| R21-10 | 12%效率差的替代检查：额外约6mm Al才能补1MeV处差别，与已知总3.7mm/tolerances不符；将前侧/前表面多面体缩至96%导致全晶体体积少5.3%，不符尺寸/质量。作者据此转向outer effective layer，仍是模型解释。 | counter-evidence-and-alternative | author-explicit-comparison | PDFp13 Sec5.2 | true |
| R21-11 | Table1的back1–6/step.25、coax0–5/.25、outer0–1.2/.1构成5733点，36能量53–3548keV。事前typed表用有理数端点重算21×21×13=5733闭合；模拟网格不是实验样本量。 | actual-table-crosscheck | direct-table-and-reproducible-arithmetic | PDFp14 Table1；Sec6.1 | true |
| R21-12 | Fig7/8显示back/coax valley与coax/outer相关；(e)分别固定back2.0/2.5mm的平面，色阶/68%与95%contours来自插值。原χ²grid、Ndf/阈值及联合Cov未取得，不将固定平面自动当完整3D profile。 | identifiability-and-confidence-scope | direct-figure-and-limited-inference | PDFpp15–17；Fig7e/Fig8e | true |
| R21-13 | I外层.40mm在100–300keV效率可高估至15%，II的.90mm改善至约100keV却低估100keV以下效率；作者明确一组参数不能复现全部方面。拟合有效层并非真实surface detector physics模型。 | counter-evidence-and-model-domain | author-explicit-limit | PDFpp3/22–23；Fig9 | true |
| R21-14 | 最小装置模型在300keV以下continuum明显不足，加入邻接/后方被动材料后改善；I在150keV以下仍可高估10%。1000keV以上近photopeak残差被暂归partial charge collection，作者要求今后polarimetry/tracking加入现实segmentation/partial collection。 | response-companion-and-author-interpretation | direct-residual-and-qualified-interpretation | PDFpp20–23；Fig11–12；Sec7 | true |
| R21-15 | I能区Table2/图注常写53–3548keV，Sec6.1正文写58–3548、总结另写58–3549；1172/1173标签也并存。保留版本文字边界，不自选一个输入重放原拟合。 | literal-version-boundary | direct-source-crosscheck | PDFp15 Table2/text；PDFp23；Fig11–12 | true |
| R21-16 | Fig7/8(d)图注称coaxial-vs-outer，但实际轴和p15正文为back-vs-coaxial；不把(d)误用于outer厚度相关性，(e)才是outer/coax平面。 | figure-locator-boundary | actual-image-and-text | PDFpp16–17 Fig7d/Fig8d；PDFp15 | true |
| R21-17 | 原文称back fraction为至少一IP在back slice的photopeak子类，图5/10轴标(%)；本run没有unrounded counts/归一producer，保留原称谓，不仅凭图形量级把它静默改成absolute效率或重拟合其分母。 | normalization-readiness | direct-source-and-missing-input | PDFp12 Sec5.2；Fig5/Fig10 | true |
| R21-18 | 声明free stationary electron模型，1172/1173keV的180°backscattered photon为209.769/209.801keV，recoil edge为962.231/963.199keV；与Fig11约210keV背散射结构作定性机制核验，未数字化图counts或标Q。 | quantitative-mechanism-design | stated-kinematics-and-source-comparison | Fig11；本页Compton公式/response-exercise | true |

## Summary

作者用位置扫描、photopeak效率与coincidence continuum共同约束有效响应，清楚保留了参数退化、低能失败和physical-model边界。它加强“需要matching response”的证据，也直接限制由能谱吻合推出偏振Q已认证的结论。

## 表格与实际输入的复核

| Table2对象 | coax/mm | back/mm | outer/mm | 本run处理 |
| --- | --- | --- | --- | --- |
| TypeA单晶 | 2.09 | 2.8 | .40 | fitted effective参数，不作物理层测量 |
| 全阵列I | 3.0 | 2.0 | .40 | 保留53/58文字差别 |
| 全阵列II | 1.5 | 2.5 | .90 | 仅对该能区和响应方面有效 |

II/I的三个厚度比为.5/1.25/2.25。这是相同数据选择下模型optimum的变化，不是显著性检验。Table1按inclusive端点给21×21×13=5733；36能量的nominal网格组合数206388也不是206388个独立观测。

[[ucgretina-2024-geant4-11-source-replay]] UG24-18另核当前100k源MC的实际asolid：shape0/1均为coax1.5/back2.5/outer.9mm。文件、format doc、parser及usePassive默认true一致，恰对应Table2 II数值。当前模型仍为七quad和11.4.2，三厚度相同不能认证2019–2020十二quad实验、全部周边材料、源门或paper exact producer。

对free stationary electron，`E_back=Eγ/[1+2Eγ/(m_e c²)]`，`E_edge=Eγ−E_back`。以`m_ec²=510.99895keV`计算，1172/1173标签差只使背散射能量变.0320keV，远小于图的4keV bin；该小差不消除原文标签边界，也不解释完整残差。式子仅核约210keV背散射机制，材料分布/束缚电子/多次散射/阈值仍需实际response。

可复现[交叉核验脚本](../../system/scripts/day16_riley2021_response_crosscheck.py)，冻结typed表、源file/hash、单位和假设后实际exit0，PDF和原输入hash保持；`riley2021-response-exercise-contract/result.json`、`riley2021-mainline-reading-audit.json`和逐图render index位于本Day16 run目录。未从raster图读取高精度峰面积或重建原χ²grid。

## Competing Interpretations and Limitations

[[lauritsen-2025-gamma-angular-formalism-tracking-arrays]] L25-30的source reference是1333target/1173gate；本页Sec4的target/gate相反。两者即使来自同一60Co cascade，也须分别核γ角色、reference方向与响应定义，不能共享一个未经转换的P/Q输入。

- 有效层厚度、missing passive material、晶体体积与partial charge collection是不同层的竞争解释；原作者以尺寸/质量反证排除两种简单替代，仍不宣称effective layer代表真实电场边界。
- Eq1、逐bin residual误差带、quoted95% intervals与固定平面contours各有条件；原event/计数归一、finite-MC/fullCov、producer和未插值grid未取得，不能重放联合CI。
- 原文明确source参数受能区和observable选择影响。门控continuum、source singles效率、偏振harmonic与DCO reference是不同对象，迁移时必须再核角色/选区/响应。
- 图与正文的小冲突保存为locator/输入边界，不据此宣判实验无效；back fraction的确切原始分母也不由图的量级补写。
- I/II与多图共用flood measurements，LBNL单晶是另一装置路线；本run没有以论文数、图数、模型或公开代码版本数增加独立实验计数。

## Knowledge Impact and Learning Decision

`supports`用source效率＋位置/空间子类＋continuum反证约束能谱响应；`revises`公开七quad例即Riley2021主体数据的初始预期；`limits`将默认参数/能谱吻合/极小模型stat interval提升为真实被动层精度或偏振Q验证。当前仍为Day16下partial17知识预习，全部新claims needs_review。

## Extracted Pages

- [[gretina-eu152-source-response-replay]]：实际默认II参数、不同数据/配置及source-window模型的迁移边界。
- [[compton-polarimetry]]：能谱和偏振响应的必要companion与partial collection限制。
- [[ucgretina-2012-eu152-public-calibration-data]]：2012七quad独立身份。
- [[ucgretina-2024-geant4-11-source-replay]]：代码/当前输入与原论文的显式crosswalk。
