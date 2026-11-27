---
type: source
title: "Leander–Larsson1975：静态PES、历史坐标与四极矩归一"
aliases: [Leander Larsson1975 N=Z potential energy surfaces, LL75]
created: 2026-10-27
updated: "2026-11-07"
status: ai-draft
review_status: unreviewed
source_type: theory-method-and-applications
reading_depth: deep-read
title_original: Potential-energy surfaces for the doubly even N = Z nuclei
authors: [G. Leander, S. E. Larsson]
year: 1975
journal: Nuclear Physics A
volume: 239
pages: 93–113
doi: 10.1016/0375-9474(75)91136-7
canonical_source: https://doi.org/10.1016/0375-9474(75)91136-7
citation_key: "leander_1975_12c-potential-energy"
raw_file: "raw/papers/1975_Leander_Larsson_PotentialEnergySurfaces_NequalsZ.pdf"
raw_sha256: 35ce50a080755f3a11dac48cfbe2e2041659694038bc6bcaf28b452d72da562d
raw_storage_status: "archived-local"
actual_body_file: tmp/day24-leander1975-039/attachment-object-response.pdf
nuclei: [12c, 16o, 20ne, 24mg, 28si, 32s, 36ar, 40ca, 44ti]
models: [modified-oscillator, macroscopic-microscopic, Strutinsky-shell-correction]
methods: [stretched-coordinates, deformation-minimization, intrinsic-moments]
tags: [133Ce-method-blueprint, shape-coexistence, operator-normalization, model-transfer]
archive_required: true
---

# Ref23原件已读：轴向同态Q不等完整三轴跃迁库


## Local archive reconciliation — 2026-11-07

Recovered/located original bytes at `raw/papers/1975_Leander_Larsson_PotentialEnergySurfaces_NequalsZ.pdf`; SHA-256 matches the previously recorded identity. Recovery manifest: `raw/reports/gpt/20261107-local-literature-recovery/manifest.json`. Local recovery time: 2026-11-07T06:49:26.680862+00:00. Earlier statements that raw was an unfilled slot describe the historical acquisition stage; the current frontmatter records the completed local archive. Reading scope, version attribution, claims and citation key are unchanged. The main-file recovery does not certify every supplementary artifact is present.

## Bibliographic Record

G. Leander和S. E. Larsson，Nuclear Physics A239(1975)93–113，DOI10.1016/0375-9474(75)91136-7，Crossref核题名、作者、卷页。首页received1974-08-22/revised1974-10-29；physicalPDF页+92=印刷页。它是[[larsson-1978-nuclear-core-quasiparticle-coupling]]的Ref23，不是133Ce实际代码附件。

实际21页PDF为1736708bytes，SHA见frontmatter。配置的出版商API先给90,802bytes的一页文章预览；另取FULL XML后，按其返回的确切MAIN attachment EID走标准Object Retrieval API，得到21页完整原件。正文完整性由题名/作者、首末页及页数另核，不把通用downloaded状态或PDF签名等同完整body。S3直链403、Scholar失败和OA索引空值保留为受检路线历史；正文来自配置的publisher API，不宣称开放许可证或PDF可再分发。SI获取未成功不等SI全无；未启动浏览器/宿主。完整原件、XML/OCR/整页图不进入本run发布清单。

## Scope and Reading Depth

044读PDF1–18全文科学主线和PDF20–21参考，视觉核全部Figs1–12/Tables1–2；043另连续深读PDF3–6/19–20方法/Appendix，核Table1表头/脚注及关键放大公式。两者覆盖全部21页主线、附录与参考入口，但没有逐篇重读所引实验/理论文献。root另读方法/物理判读关键文本，视觉核PDF4/7/10、PDF19–20的A1–A10及归一/表头。不是数值重现PES或恢复作者程序。

## Summary

这篇实际给出历史dimensionless坐标、角矩阵元CG归一、体积约定和忽略γ后的同态Q-like期望，关闭了此前Ref23的body/方法阅读缺口。一般angular ME确实存在；A8/A9则明确是轴向同一ν，不能把q2ν下标误当球张量μ，不能称完整三轴off-diagonal库已取得。PES主线还明确保留静态极小与物理态之间的投影、collective dynamics、ZPE和混合边界。

## Experimental or Theoretical Setup

本文研究12≤A≤44的doubly-even N=Z核。MO single-particle能级给Strutinsky shell correction，加macroscopic Coulomb与finite-range surface；不是2022 odd-A Ce的QTR/BCS job。所选κ=.08、μ=.10对所研究protons/neutrons相同，省略single-particle Coulomb贡献，连同time reversal形成此处四重简并；不能迁为N≠Z Ce的orbitals或组态。

deformed HO基含9–11 major shells、抑制ΔN>4 couplings；Gaussian平滑γs=1.6ℏω0及sixth-degree curvature correction；85点(ε,γ)网格上逐点最小化ε4，范围0–.24。surface的a1.4fm/r0=1.16fm与Table1 moments的charged-drop r0=1.2fm承担不同角色。各处ω0和带上置小圆圈的ω0°须按原页分别保留，不能靠OCR合并。

## Key Results

新claims全部needs_review:true。原模型结果、引用实验和任务归一推导分开。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LL75-D24-001 | 本篇是N=Z A12–44的static MO/Strutinsky+macro计算，κμ/p=n四重简并/空间与最小化均有具体条件，不是133Ce参数或actual producer。 | direct-model-scope-and-input | direct-original | PDF1–4 printed93–96; Eqs5–8 | true |
| LL75-D24-002 | A1明确定义dimensionless ξ/η/ζ，ω0无圈；A7的ω0°是另一符号，ω0/ω0°由含γ、ε4的体积积分给定，不能自动化为任意product-frequency处方或由ℏω≈8恢复Ce输入。 | coordinate-frequency-and-volume-contract | direct-original | PDF19–20 printed111–112 A1/A7 | true |
| LL75-D24-003 | A2/A3给general spinor-angular ME与CG相乘的rLL，不含radial HO积分/deformed coefficients。按声明的标准3j定义，Rstd=√(2j′+1)rLL是任务桥；double bars本身不能识别归一。 | original-angular-ME-plus-task-conversion | direct-original-and-labelled-algebra | PDF19 A2–A3 | true |
| LL75-D24-004 | A8/A9段首明确neglecting γ，bra/ket均同一ν无prime；A8 q2ν是√(16π/5)r²Y20的Q-like期望，含length²及+2ε/3〈ρ²〉。不是任意μ/ν′ν三轴transition matrix。 | direct-formula-domain-and-index-identity | direct-original-visual | PDF20 A8–A10及其前句 | true |
| LL75-D24-005 | Eq10 Q0为总proton Q-like sum，Eq11 Q40显式除Z且采用r⁴Y40；Table1为fm²/fm⁴的intrinsic moments，B(E2)列经rotational model推abs(Q0)而不独立给sign。 | moment-normalization-and-observable-boundary | direct-original | PDF6–7 printed98–99 Eqs10–12/Table1 | true |
| LL75-D24-006 | Table2 min与barrier两列都相对ground minimum，后者不是已减去各excited minimum的逃逸barrier；未见/空白/边界图还受空间截断与插值等合同。 | energy-reference-and-display-contract | direct-original | PDF8 §3.1; PDF10 Table2caption | true |
| LL75-D24-007 | 作者指出高阶shell-correction项、macro light-mass外推和surface softness可致数MeV系统差；plateau不消除此误差，a1.4fm或导致unphysical wiggles。 | author-model-error-boundary | direct-original | PDF4–6 §2.3 | true |
| LL75-D24-008 | static PES是最低可用轨道占据的intrinsic能，physical states仍需projection或adiabatic collective模型；ZPE、mixing与不同deformed bases非正交使minima高差只能粗估bandheads。 | direct-intrinsic-to-laboratory-boundary | direct-original | PDF8 printed100 §2.3末 | true |
| LL75-D24-009 | 24Mg反射非对称min在两surface选择中约6/17MeV；40Ca模型binding过多9–13MeV，另一参组prolate8p8h min在本图仅ledge。作者保留的失败/敏感性不能删掉后称所有形状都精确再现。 | direct-adverse-results-and-sensitivity | direct-original | PDF14–17 Results; Figs4/8 | true |
| LL75-D24-010 | near-Fermi轨道耦合与总macro代价可用于研究设计；整数HO比、allowed coupling、PES min或轻核quartet/cluster解释不直接认证实验shape、rotational band或Ce组态。 | source-model-plus-explicit-transfer-boundary | direct-original-and-task-synthesis | PDF2 Fig1; PDF9 §3.1; PDF12–18 Results | true |
| LL75-D24-011 | A1取γ0后，pointwise O20=2z²−x²−y²=ℓ0²/[(1+ε/3)(1−2ε/3)]·[Ot+2ερ²/3]，Ot=2ζ²−ξ²−η²，与042轴向恒等式一致；推广到任意bra/ket是任务代数，不冒A8原文已印off-diagonal库。 | explicit-source-to-coordinate-identity-bridge | direct-formula-plus-task-derivation | PDF19 A1; PDF20 A8; LLR78-D24-023/024 | true |
| LL75-D24-012 | 当前取得历史坐标/角ME/轴向期望定义，不等2022 κμ/频率/体积/BCS/basis/radial/signed数值输出已恢复；相同方法谱系不确定actual版本或单位零点。 | actual-producer-readiness-boundary | original-scope-and-explicit-task-audit | §2/Appendix; WK22 §3.4 | true |

## Historical Operator Dictionary

A1为ξ=√[(mω0/ℏ)b_x]x、η=√[(mω0/ℏ)b_y]y、ζ=√[(mω0/ℏ)b_z]z，b_x/y=1−2εcos(γ±2π/3)/3，b_z=1−2εcosγ/3。只有声明ω_i=ω0 b_i>0后，才与[[larsson-1978-nuclear-core-quasiparticle-coupling]]的任务dimensionless字典对应；dimensionful X_i=ℓ0ξ_i，ℓ0²=ℏ/(mω0)。A7另用ω0/ω0°的体积条件，包含γ与ε4的角积分；这里没有求实际Ce的ω0。

A2采用F=rLL·CG，未另乘1/√(2j′+1)。同CG相位下，标准3j的Rstd=√(2j′+1)rLL，故若某输出明确定义为这种CG-reduced字段，B=(2If+1)/(2Ii+1)abs(rCG)²。只有两个算符都用此约定、同一spin端点时，这个spin因子才在它们比中消去；不同普通分量ME仍有不同3j，不能混用。这里只举实际历史归一例，不宣称PROBMO采用它。

在A8的轴向范围，令p=1+ε/3、s=1−2ε/3，则

$$2z^2-x^2-y^2=\frac{\ell_0^2}{ps}
\left[(2\zeta^2-\xi^2-\eta^2)+\frac{2\varepsilon}{3}
(\xi^2+\eta^2+\zeta^2)\right].$$

对同一ν取期望正好给A8，原件下标是态ν，不是张量μ。ρ²=ξ²+η²+ζ²是普通stretched半径平方；其项不代表物理E0，完整physical算符仍是rank2。A9给同态r⁴Y40期望，不能只因同叫Q而把它与Q0归一或电荷/长度混合。完整三轴五分量pointwise表达仍为042任务推导，不倒填为本篇直接打印的式子。

## PES and Evidence Interpretation

全部Figs1–12给MO单粒子图、PES、变形耦合示例；Tables1/2分别为moments对照和static minima属性，不是实验逐伙伴τ/B表。Table1中24Mg Q0 microscopic/macroscopic64/64fm²与B(E2)推得64.2(1.1)相近，是源中真实比较；32S两min与admixture解释依模型，所引实验/散射/HF也不等多个独立新实验。

读Table2须连每行min位置/组态与同一能量零点，不能把GS-relative saddle高度直接当从该well出发的barrier或衰变寿命。更不能从static wells直接读出good-I partner splitting：作者要求投影/collective dynamics，保ZPE、mixed states和非正交。40Ca与24Mg的明确失败/敏感例说明这些限制有实际后果，不只是一般免责声明；本文没有计算Ce的shape模式胜负。

## Competing Interpretations and Limitations

作者认为部分topology/组态有用而relative energies常不准，结尾主动把直接PES解释收窄为speculative。不同single-particle potential、spin-orbit/orbit-orbit、填充、higher-multipole最小化和macro项须逐字段比较；允许耦合也不保证净能量降低。不能把N=Z p=n quartet、α结构或这里κμ搬到odd133Ce，也不由本篇shape例推全核chirality无效。

原扫描Eq8的第二系数及Fig12参数框部分损伤，043/044都未猜填。本篇未交付本轮所需的2022 input/header、完整signed eigenvectors、径向数值矩阵、EM output、实际detector response或Cov。原body取得和历史归一闭合是进展，不能以摄入/公式转录宣称133Ce分析工程结束。

## Extracted Pages

- [[133ce-thesis-analysis-blueprint]]：历史field与actual输入/单位/波函数分开。
- [[larsson-1978-nuclear-core-quasiparticle-coupling]]：Ref23方法范围及042/041字典的原件核验。
- [[chirality-shape-coexistence-companion-matrix]]：static PES、物理态与竞争解释的层次，非目标核替代fit。

## 2026-11-27 — 馆藏原件与覆盖核对

- {"range": "物理 PDF 1–2", "sections": "首页书目信息及 §1 引言"}
- {"range": "物理 PDF 3–8", "sections": "§2 模型、数值步骤、方法适用性与本征能量的解释"}
- {"range": "物理 PDF 8–18", "sections": "§3 绘图约定、极小值、逐核结果与结语"}
- {"range": "物理 PDF 19–21", "sections": "致谢、附录 A1–A10、参考文献 1–53"}
- 本次获取的具体覆盖：逐页审读物理 PDF 1–21 的供给文本，涵盖引言、计算方法、逐核结果、附录及文献表，也读了可辨认的表注和图注。公式与图表的抽取有残缺，本次未查看原页图像。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A18-1 | 作者对 ¹²C 至 ⁴⁴Ti 的双偶 N=Z 核计算静态势能面，以修正振子能级的 Strutinsky 壳修正配合宏观库仑项和有限程表面项。所用 κ=0.08、μ=0.10 对质子和中子相同，单粒子势省略库仑贡献，文中将这两项约定与时间反演对称性联系到四重简并。 | 模型设定 | source-reported | 物理 PDF 1 §1、PDF 2 图1后正文、PDF 3–4 §2.1–2.2，式 (3)–(7)。 | true |
| A18-2 | 作者报告 ²⁴Mg 反射不对称极小值在有限程表面项下约高于基态极小值 6 MeV，采用常规液滴表面项时约为 17 MeV。对 ⁴⁰Ca，另一组参数得到的长轴 8p–8h 极小值在本计算中只表现为能量曲线上的台肩。 | 模型结果 | source-reported | 物理 PDF 5 §2.3、PDF 11 图4、PDF 15 图8及 PDF 16 §3.2。数值和台肩判定来自正文，图4与图8的曲线仍分别待查物理 PDF 11 与 15。 | true |
| A18-3 | 式 (10) 的 Q₀ 对质子贡献求和，式 (11) 的 Q₄₀ 采用 r⁴Y₄₀ 并除以 Z。表1把波函数计算与带电液滴计算分列，后者采用 r₀=1.2 fm。 | 模型与矩定义 | source-reported | 物理 PDF 6 式 (10)–(12)；PDF 7 表1及表注。公式字形、列归属和单位待查物理 PDF 6–7。 | true |
| A18-4 | 附录以 A1 定义无量纲伸缩坐标，A2–A3 给出角向矩阵元的 Clebsch–Gordan 约定，A7 用体积守恒约束频率比。A8–A9 在忽略 γ 后取同一单粒子态 ν 的期望值，q₂ν 的 ν 是态指标。 | 原文公式及适用域 | source-reported | 物理 PDF 19 A1–A6；PDF 20 A7–A10 及 A8 前导句。频率圈标、态下标与精确系数待查物理 PDF 19–20。 | true |

建议接受既有 Wiki 对这份同版完整主文的阅读覆盖。笔记所载 044 覆盖物理 PDF 1–18、20–21，043 补足 19–20，合计与本轮逐页文本范围吻合。原图核验仍采用待验状态，精确转录以原页复核为准。

- 将 Wiki 的 ε₄ 扫描范围 0–0.24 改为「在 85 个 (ε, γ) 格点上对 ε₄ 作最小化，扫描上下限与符号待核」。物理 PDF 4 §2.2 的范围句抽取不全，PDF 10 表2的 ²⁰Ne 行有疑似 −0.10 的 ε₄ 读数，须核列头和负号。
- 表2的极小值能量与最低鞍点高度均以基态极小值为零点。需要从某激发极小值出发的势垒时，应从对应的鞍点高度减去该极小值能量。用物理 PDF 9 §3.1 与 PDF 10 表2表注支持这一读法。
- 若保留 ⁴⁰Ca 过度束缚 9–13 MeV 的精确区间，应核物理 PDF 17 正文的下限字形。物理 PDF 4 式 (8) 的第二系数和 PDF 18 图12参数框及图注末端有残缺，保留待核标记。逐式引用时另查 PDF 1 式 (1)、PDF 3 式 (2)–(5)、PDF 5 式 (9) 及 PDF 19–20 附录，保留 A1 的 ω₀ 与 A7 的带圈频率符号之别。
