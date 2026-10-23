---
type: source
title: "Henderson2019：76Se Coulomb激发矩阵元与平均三轴性边界"
title_original: "Triaxiality in selenium-76"
aliases: [Henderson 76Se JANUS Coulomb excitation]
created: 2026-10-23
updated: 2026-10-23
status: ai-draft
review_status: unreviewed
source_type: experiment-and-model-comparison
reading_depth: read
authors: ["J. Henderson", "C. Y. Wu", "J. Ash", "B. A. Brown", "P. C. Bender", "R. Elder", "B. Elman", "A. Gade", "M. Grinder", "H. Iwasaki", "B. Longfellow", "T. Mijatović", "D. Rhodes", "M. Spieker", "D. Weisshaar"]
year: 2019
journal: Physical Review C
volume: "99"
pages: "054313"
doi: "10.1103/PhysRevC.99.054313"
citation_key: ""
canonical_source: "https://doi.org/10.1103/PhysRevC.99.054313"
source_url: "https://link.aps.org/accepted/10.1103/PhysRevC.99.054313"
raw_file: "raw/papers/day20-20261022/henderson-2019-triaxiality-selenium76.pdf"
raw_sha256: "a3327e0ee1eeb6aff8c6e0d49a3de2a281d5d005b0e5a58846b9bf0289d5b993"
raw_storage_status: reserved-unpopulated-accepted-manuscript-staging-only
raw_archive_verified_at: 2026-10-23
analysis_status: public-staging-original-read-raw-archive-verified
public_staging_file: "tmp/day20-henderson116/PDFs/Triaxiality_in_selenium-76.pdf"
nuclei: [76Se, 208Pb]
reactions: ["208Pb(76Se,76Se*)208Pb"]
experiments: [ReA3-JANUS-SeGA]
models: [GOSIA, Davydov-Filippov, JUN45, jj44b]
methods: [sub-barrier-Coulomb-excitation, quadrupole-invariants]
observables: [E2-matrix-element, spectroscopic-quadrupole-moment, average-triaxiality]
tags: [selenium, phase, reorientation, literature-constraint, rigidity-boundary]
---

# 平均三轴性与刚性的证据不是同一项

## Bibliographic Record

Henderson等，Physical Review C99，054313(2019)，DOI10.1103/PhysRevC.99.054313，Crossref精确端点核2019-05-13。实际下载为APS/CHORUS公开accepted manuscript，PDF首页明确如此标识：共10页，cover1页+正文/参考9页，2066061bytes，SHA256见frontmatter。downloader的oaEvidence把version标publishedVersion，但以PDF cover为准，不声称已核最终排版全文一致性。

PDF只在tmp公开staging；raw_file为未填归档槽，raw/PLAN/Bib未写。SI沿auto配置关闭，不断言不存在或已读。本文是新yield实验加旧文献约束；表中输出不能当与既有寿命/branch完全独立的第二测量。

## Scope and Reading Depth

primed-recall-116在lookup前冻结；事先读过Poves/Henderson2020与113/115条件反例，非盲测。本session实际读PDF1–10全部文字及参考文献，视觉核PDF3–8全部Fig1–7、TablesI–III与Eq1–4。未取得原event、17组产额全数值、完整GOSIA job/producer与jointCov，也未运行JUN45/jj44b的原输入。本文Ref24/25不代替Kumar/Cline原读。

## Paper Question and Scientific Motivation

PDF2/正文1摘要/引言：用更精确的E2矩阵元约束76Se低激发态的电荷形变，区分单一轴对称转子与显著三轴成分；与0ν2β形状重叠相关的讨论是动机，不是本文测得了0ν2β矩阵元。

## Method and Design Logic

PDF3–5/正文2–4：ReA3稳定76Se，4.07/3.55MeV/u分别24/72h，208Pb靶.92mg/cm²，JANUS两S3与16个SeGA。按beam/target粒子、角组与两能量给17组yield，同时用literature寿命/混合比/branch约束GOSIA；末结果为联合fit，不把分别检查相容的两能量当两套独立最终数据。

## Key Evidence and Reasoning Chain

粒子/角组门与Doppler谱 → 处理邻近线和γγ效率 → GOSIA加TableI外源约束 → 19个E2矩阵元与静态矩 → 有限E2环的不变量 → 平均三轴性解释。高阶刚性只在后续CI模型分支讨论，没有从本次实验有限网络直接提取完整软度。

## Summary

作者测得更精确的部分矩阵元并支持显著、非最大三轴成分，明确说实验不变量只约束平均三轴性，不约束其刚性。0₂⁺尤其受未测2₃⁺对角元素和求和收敛影响，误差条未含后者；与后来的软度批评应对准具体模型分支而非把实验原话升级为rigid证明。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| HE19-D20-1 | 两能量/角门与Doppler处理后用17组yield拟合；target-like大于40°/ring13起因dead layer排除，低能上游检测也排除。有限几何/门决定分析对象，不能把所有检测角作为独立等价点。 | experiment-gating-response | direct-original-and-visual | PDF3/正文2 SecII–III, Fig1/2; PDF4 Figs3/4 | true |
| HE19-D20-2 | 559/563keV邻线在downstream不可分，借γγcoincidence并用152Eu及backward谱两种经验效率校准作weighted correction。TableI给外源寿命/δ/branch，部分非对称误差先对称化；E0用虚构1+态的M1通道表示且受branch约束，该虚构态不是新能级。TableII明确结果与literature不独立。 | response-and-input-lineage | direct-original-and-visual | PDF4/5 SecIII; PDF5 TableI; PDF6 TableII caption | true |
| HE19-D20-3 | TableII ground0₁到前三2态RME为.647(5)/.110(2)/.040(1)eb；2₁→2₃为−.093(+.007/−.006)eb；对角2₁/2₂为−.463(+.052/−.053)/+.245(+.057/−.060)eb。Qs(2₁)=−.35(4)eb，Qs(2₂)=+.19(4)eb。保留RME符号与初末态，不只抄B模。 | reported-fit-matrix-elements | direct-table-and-visual | PDF6/正文5 TableII | true |
| HE19-D20-4 | 0₂与前三2态的RME为.285(+.026/−.027)/.182(+.033/−.047)/.532(+.021/−.018)eb。2₃对角矩未测，作者明确其对0₂的不变量可能显著、该态角度值可能未收敛；ground因.040较小而预期贡献小，不给未测元素通用数值上界。 | missing-companion-matrix-element | direct-table-and-author-boundary | PDF6 TableII; PDF7/正文6 discussion; PDF9 conclusion | true |
| HE19-D20-5 | Eq4明确以近似号假定mean cos3δ≈q3/q2^(3/2)。PDF7明确实验不变量只对平均三轴程度敏感，不对rigidity敏感；更高阶需更大矩阵元集合。Fig6/7误差只含矩阵元误差，不含convergence不确定度。 | mean-angle-and-rigidity-boundary | direct-original-and-visual | PDF6 Eq2–4; PDF7 text and Fig6 caption; PDF8 Fig7 caption | true |
| HE19-D20-6 | CI采用jj44空间与JUN45/jj44b、TableIII eπ=1.8/eν=.8。本文只用到2₅的模型矩阵元增加收敛信心；称jj44b很δ-soft、JUN45更rigid是模型分支结论。它不是实验测得了JUN45刚性或所有软度已收敛。 | model-comparison-and-softness-interpretation | direct-model-discussion | PDF7/8 SecIVA; PDF8 TableIII/Fig7 | true |
| HE19-D20-7 | TableII注明B↑，0₁→2₁为4190(+60/−70)e²fm⁴，而TableIII的2₁→0₁为838(14)e²fm⁴；上/下行需按实际初末态及详细平衡处理。↑不意味着每行spin都增大，例如2₁→0₂是向更高激发能的跃迁。 | strength-direction-and-units | direct-tables-and-level-scheme | PDF3 Fig2; PDF6 TableII; PDF8 TableIII | true |

## Competing Interpretations and Limitations

低阶电荷形状平均、γ刚性、charge-versus-mass映射与模型拟合质量必须分开。[[poves-2020-limits-assigning-nuclear-shape]]对高阶计算的批评不能被简写成这篇实验声称rigidity后被整体证伪；本实验已明示该边界。其原jointCov/producer与更高态网络未得，TableII边际误差不能自动拼成独立Gaussian实验CI。

## Analytical Reconstruction

HE19-D20-4给出一个可算的下一问题：在前三2态截断内，未知2₃对角元素进入0态三阶环时带其连接RME的平方；可用两0态的打印中心值对比灵敏度。此处尚未赋未知元素的值/范围或重现作者Fig6误差，须以条件导数和缺失strength边界呈现。

## Knowledge Impact and Learning Decision

revises：112/114反证综合不能把“平均三轴性”误写成实验刚性主张。supports：[[transition-quadrupole-moment]]需要signed矩阵元、初末态、文献约束谱系和有限网络门。[[day20-quadrupole-collectivity-systematics-synthesis]]记录实际实验和模型解释的分支；不建立普适γ阈值或新的A≈130实验精度认证。

## Related Knowledge and Project Relations

- methodological-bridge：[[henderson-2020-quadrupole-invariant-convergence]]，原有限网络的截断缺口与后来的收敛问题。
- competing-interpretation：[[poves-2020-limits-assigning-nuclear-shape]]，针对高阶模型软度，实验低阶边界应保持。
- supports：[[day20-quadrupole-collectivity-systematics-synthesis]]、[[transition-quadrupole-moment]]，完整观测量与推断层次。

## Human Review Triage

按ingest-strategies的Agent self-audit定义；无用户审核事件。P0: none identified。P1：HE19-D20-4未测2₃对角与高态strength/收敛界；HE19-D20-2共享旧约束与原jointCov未得；HE19-D20-5/6平均/rigidity和实验/模型分支不可混写。P2/P3：accepted/PDFcover优先于downloader版本标签，raw deferred、↑/初末态与单位维护。

## Extracted Pages

PDF1：CHORUSaccepted cover；2/正文1：摘要/动机；3/正文2：方法/门与Fig1/2；4/正文3：Fig3/4谱与邻峰；5/正文4：γγ效率、TableI约束、模型比较引入；6/正文5：TableII、Eq2–4；7/正文6：Fig5/6与不变量rigidity/收敛边界；8/正文7：TableIII/Fig7、模型高阶与结论起；9/正文8：结论/致谢/Refs1–21；10/正文9：Refs21–30。

## Day20 checkpoint117：未测对角元素的条件权重

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| HE19-D20-R117-1 | 只纳入前三2+并固定TableII中心值/符号时，令d33为未测2₃对角RME：q3=−sqrt(7/10)aᵀDa，q2=aᵀa。ground q2=.432309eb²，q3=.08555848−.001338656d33；0₂ q2=.397373eb²，q3=−.04972794−.236794867d33，d33以eb计。常数项只是d33=0的多项式截距，不是采用真实零矩。 | literal-source-conditional-sensitivity | source-central-values-plus-independent-tensor-contraction | HE19-D20-3/4; PDF6 TableII/Eq2/3; day20_se76_missing_diagonal117.py | true |
| HE19-D20-R117-2 | 未知d33的q3系数模之比由(.532/.040)²=176.89给出；对R=q3/q2^(3/2)，导数ground−.00470953/eb、0₂−.94531109/eb，比例200.723。此有限截断中0₂对缺失元素更敏感，不给d33范围或其真实误差，也不以ground小系数证明误差绝对可忽略。 | conditional-comparative-missing-element-weight | exact-central-input-contract | HE19-D20-R117-1; HE19-D20-4 missing-companion boundary | true |

16维完整multiplet张量的直接球分量收缩与三态二次型相容；检查Hermiticity、整体态相位和自由d33仿射系数。11项控制仅核该投影模型与原件/输入/code指纹，没有原GOSIA重拟合、jointCov、全高态closure或实验CI。TableII打印.647给B↑4186.09而打印4190，反向按spin因子为837.218而打印838；保留字面舍入残差，不放宽容差后宣称producer已复现。
