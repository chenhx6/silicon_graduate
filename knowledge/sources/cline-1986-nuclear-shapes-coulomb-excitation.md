---
type: source
title: "Cline1986：多步库仑激发、形状不变量与有限求和边界"
title_original: "Nuclear Shapes Studied by Coulomb Excitation"
aliases: [Cline 1986 nuclear shapes, Cline rotational invariants]
created: 2026-10-23
updated: 2026-10-23
status: ai-draft
review_status: unreviewed
source_type: method-and-experimental-review
reading_depth: read
authors: ["Douglas Cline"]
year: 1986
journal: Annual Review of Nuclear and Particle Science
volume: "36"
pages: "683-716"
doi: "10.1146/annurev.ns.36.120186.003343"
citation_key: ""
canonical_source: "https://doi.org/10.1146/annurev.ns.36.120186.003343"
source_url: "https://www.pas.rochester.edu/~cline/Publications/annurev.ns.36.120186.pdf"
raw_file: "raw/papers/day20-20261022/cline-1986-nuclear-shapes-coulomb-excitation.pdf"
raw_sha256: "76d89a9bc5d603aa8dae104c0b6356271b7d152e0bff33e3cf78138861670113"
raw_storage_status: reserved-unpopulated-public-author-copy-staging-only
public_staging_file: "tmp/day20-cline148/PDFs/Nuclear_Shapes_Studied_by_Coulomb_Excitation.pdf"
analysis_status: original-review-mainline-and-key-evidence-read-raw-archive-deferred
source_independence: method-review-and-secondary-reports-not-new-independent-experiments
nuclei: [232Th, 168Er, 110Pd, 192Os, 194Pt, 104Ru]
methods: [Coulomb-excitation, rotational-invariants, nonlinear-least-squares]
models: [GOSIA, semiclassical-coupled-channels, rotor, IBM]
observables: [E2-matrix-elements, quadrupole-invariants, shape-fluctuations]
tags: [shape, triaxiality, covariance, convergence, source-lineage]
---

# 从多步产额到电四极分布：原方法综述与限制

## Bibliographic Record

Douglas Cline，Annual Review of Nuclear and Particle Science36，683–716(1986)，DOI见frontmatter。Crossref精确DOI与PDF首页的题名、页码一致。作者大学主页的1985–89列表把链接题名写作“Heavy Ion Coulomb Excitation and Nuclear Structure”、页码681–714；下载实际是本页题名/683–716，不用列表替换原件身份。

出版商PDF403、公开APS/Kumar入口403/401及OA查询失败均留在run的access记录。沿Rochester作者主页→Publications→1985–89的真实链接取得1930372bytes、35页PDF；前34页为683–716正文/参考，末页只有水印。文件有copyright与personal-use水印；公开作者副本可访问不等于开放再分发许可。只在tmp staging，raw归档deferred；不把PDF、Bib或PLAN带入Git。Kumar1972仍未获正文，本文Ref26不是代读。

## Scope and Reading Depth

checkpoint148的primed recall在lookup前冻结，已受HE20/PO20/AY23与147账本启发，非盲测。本session实际阅读PDF1–34全部主线/结论/参考，检查PDF35为水印页；视觉核全部Fig1–13及第695、698–700页关键误差/耦合公式，Fig4分母另放大。没有数值digitize全图、读完94项被引原文、运行原GOSIA或恢复任一实验的原产额/jointCov。

这是一篇方法与实验综述：其方法论文字是直接原读；所举核素的测量结果在本轮仍属于综述转述，不计为本任务新读的独立实验。

## Paper Question and Scientific Motivation

第683–686页：高Z多步库仑激发可布居更多态，但需要从许多耦合通道中提取矩阵元，再用不变量表达集体相关。关注点是测量的范围、精度、限制与结构信息，而非只用能级或一个大B(E2)给形状定名。

## Method and Design Logic

安全碰撞距离/半经典多通道 → 逐角、逐能量或逐projectile-Z产额与衰变 → 包含寿命、branch、mixing等外源约束的GOSIA非线性搜索 → 带符号矩阵元 → 不同阶/耦合路径的不变量 → 集体形状解释。有限探测器、靶能损、recoil与deorientation分别进入响应；低敏感参数及原误差算法不能由论文表值代替。

## Key Evidence and Reasoning Chain

第692–696页解释为什么产额同时依赖矩阵元模与相对符号，以及为什么多角度/多Z有价值。第697–700页给张量标量与中间态展开，随后直接讨论高阶缺失强度、对易性和低/高频分离条件。第700–712页以强形变、带交叉和过渡核说明单个成功模型拟合的局限；结论仍要求更精细的模型检验。

## Summary

本原件支持把矩阵元网络、原非线性误差、不同阶求和及形状解释分层。它没有把“model independent”扩展为无截断、无实验响应误差或任意模型算符满足相同对易恒等式。该文的历史精度/成功案例不可移植为Ce/Nd或现代Ge的统一认证。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| CL86-D20-1 | 实际PDF题名Nuclear Shapes Studied by Coulomb Excitation、683–716；大学列表另题名/681–714属入口元数据差异。35PDF页中34页正文/参考、末页水印。 | source-identity | direct-cover-and-author-index | PDF1/p683; Rochester Pub8589列表; PDF35 | true |
| CL86-D20-2 | 产额对模与相对符号是耦合、非线性响应；多角度/不同projectile-Z可移动高敏感fall-off区。简单相邻产额比敏感性法会损失部分信息，不能通用于强耦合过渡核。 | original-method-and-failure-boundary | direct-review-method | PDF10–12/pp692–694; Fig3 | true |
| CL86-D20-3 | 作者在强非线性/交叉相关问题中批评局部抛物曲率近似，并描述以参数空间概率积分取68.3%限的做法。这是1986方法说明，不证明2023具体producer、所有现代GOSIA版本或本任务的Gaussian重拟合等价。 | nonlinear-uncertainty-method | direct-original-text-and-visual | PDF13/p695 | true |
| CL86-D20-4 | Rochester做法为每个态固定一个矩阵元符号以选波函数相位，再以不同随机初值采样干涉符号；强branch约束可能把搜索锁在初始干涉符号。相位规范与物理环符号不能混为同一不确定性。 | relative-phase-search-contract | direct-original-method | PDF13–14/pp695–696 | true |
| CL86-D20-5 | 主轴E20=Qcosδ、E2±2=Qsinδ/√2；二、三、四、五、六阶零耦合项分别涉及Q²、Q³cos3δ、Q⁴、Q⁵cos3δ、Q⁶与Q⁶cos²3δ。中间态展开要求相对符号和模，不能仅用B模。 | original-tensor-definition | direct-original-equations-and-visual | PDF16/p698六行耦合式及6j展开 | true |
| CL86-D20-6 | 缺失强度影响随不变量阶数/复杂性增强；不同中间spin耦合可给自洽检查，但相关恒等式依赖E2对易性质。作者明确部分模型（例IBM）算符不满足这些恒等式；不同耦合结果不是独立重复实验。 | completeness-and-operator-boundary | direct-original-text | PDF17–18/pp699–700; Fig11/13 caption | true |
| CL86-D20-7 | 作者区别能量加权与非能量加权强度；所述低能非加权90–95%是强形变情形的综述量级。忽略高频巨共振只有在两模式分离、弱耦合且高频涨落相对小时才合理，不是全部真实空间已穷尽。 | low-high-frequency-separation-assumption | direct-author-limitation | PDF18/p700 | true |
| CL86-D20-8 | Fig4宽度最后一项实际印[⟨Q³cos3δ⟩/⟨Q³⟩]²，不是HE20 Eq27的分母⟨Q²⟩³；图中cos3δ的centroid行只印未归一的⟨s|Q³cos3δ|s⟩。保留字面/归一歧义，不擅自修为同一公式或据此判定作者代码。 | literal-formula-version-boundary | direct-original-and-enlarged-visual | PDF17/p699 Fig4; enlarged formula crop | true |
| CL86-D20-9 | 综述以232Th的Qt近常数而惯量随spin变讨论Coriolis anti-pairing，认为单纯离心伸长解释不合该组数据。Fig5来自多个已引实验与模型，不建立所有核中Qt/惯量唯一因果关系。 | reviewed-example-and-author-interpretation | secondary-experimental-report-plus-model-comparison | PDF19–21/pp701–703 Fig5 | true |
| CL86-D20-10 | 168Er一组带内矩阵元可被多个模型较好重现，跨带元素更敏感；作者还说γ≈9°附近所比数据对γ-softness相对不敏感。拟合均值/带内模式与刚性宽度是不同问题。 | reviewed-model-discrimination-limit | secondary-review-of-experimental-comparison | PDF23–24/pp705–706 Figs7/8 | true |
| CL86-D20-11 | 110Pd的近“两声子”0⁺/2⁺/4⁺能量聚组并未固定振动解释；综述所述89个E2矩阵元支持不同变形带/软度。此处只用作能量聚组的反例路径，不把模型标签推广为A≈130通用阈值。 | reviewed-competing-interpretation | secondary-review-and-figures | PDF28–30/pp710–712 Figs12/13 | true |
| CL86-D20-12 | 文中转述110Pd八个低态的recoil-distance与CoulEx寿命比较，weighted mean差2.2±3.5%；支持所述案例的相容性，不证明跨方法零共同系统误差或任一现代实验的CI。 | reviewed-cross-method-check | secondary-experimental-report | PDF14/p696; Refs48/52 | true |

## Competing Interpretations and Limitations

单个collective model能拟合部分产额不等于唯一解释：第692页举Pt误模型也曾拟合成功；第709页说γ-soft模型较成功但各模型只重现部分矩阵元。1986关于计算能力、可得束流和误差量级的陈述带历史范围，不包装为现代装置极限。

原文“几乎完整低能集”“typical experiments”与“model independent”的用语，须与第699–700页明确限制一起引用。完整有限张量网络也不自动等同于全部物理价空间或电荷坐标实现；从电磁Q/δ到质量β/γ仍有模型关系。

## Analytical Reconstruction

CL86-D20-8只认证印刷差异。若另声明可交换正幅度Q与C=cos3δ相互独立，则使用⟨Q³⟩的图4宽度比可约去幅度矩；HE20的⟨Q²⟩^(3/2)分母一般留下幅度因子。这个条件代数不代表本文实际代码/数据采用了独立分布，也不将图中缺失归一自行补齐。进一步推导与scalar endpoint审计见[[day20-quadrupole-collectivity-systematics-synthesis]]；不是原实验CI恢复。

## Knowledge Impact and Learning Decision

revises：此前Cline1986的metadata-only状态变为本session实际原读；Kumar1972仍仅metadata。supports：高阶缺失路径、相位规范与干涉符号、原非线性误差、算符对易和低高频分离的边界。limits：把Qt常数/能量聚组/模型拟合直接升级为γ刚性或唯一模式。

本日[[singh-2016-lifetime-131ce-133pr]]与[[petrache-1998-highly-deformed-lifetimes-131ce-nd]]仍为不同实验及fit角色；本综述没有补出它们的原Cov、producer或真实K。原撤回状态不因新增经典来源而恢复。

## Related Knowledge and Project Relations

- foundational-method：[[coulomb-excitation]]、[[transition-quadrupole-moment]]。
- source-convention-comparison：[[henderson-2020-quadrupole-invariant-convergence]]，按实际Fig4/Eq27分母区分。
- operator-and-model-space-boundary：[[poves-2020-limits-assigning-nuclear-shape]]。
- later-experimental-implementation：[[ayangeakaa-2023-ge76-coulomb-excitation-full]]，历史方法不能识别其实际producer。
- supports-and-limits：[[day20-quadrupole-collectivity-systematics-synthesis]]。

## Human Review Triage

这是Codex source self-audit，不是human-reviewed。P0：PDF只留公开staging，不再分发。P1：Fig4归一字面歧义、有限网络/对易/高频省略条件、历史方法与现代具体fit的区分。P2：作者列表错题名/页码、raw deferred及空citation_key。needs_review保持true，后续论文使用再按具体claim核验。

## Extracted Pages

PDF1–4/683–686：动机、历史与范围；4–7/686–689：安全距离、半经典响应、deorientation；8–10/690–692：装置、Fig1/2与分析入口；10–14/692–696：非线性fit、Fig3、原误差/相位与交叉方法检查；15–18/697–700：形状不变量、Fig4、缺失强度/对易/低高频边界；19–22/701–704：232Th Fig5及odd-A谱Fig6/带交叉；23–24/705–706：168Er Figs7/8；25–27/707–709：Os/Pt Figs9–11；28–30/710–712：110Pd Figs12/13及Cd/Ru/Ge/Kr对照；31/713：前景；32/714：结论/致谢/参考开头；33–34/715–716：余下参考；35：无正文水印页。没有表，未编造表审计。

## checkpoint150：有限矩不唯一识别分布（任务推导）

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| CL86-D20-R150-1 | 原文p698“in principle all invariants”与一个有限二至六阶矩集合须分开。明示正Q、C=cos3δ的可交换五点分布，可构造二/三/四/五/六阶六个标量矩完全相同而meanC、VarC和mean/SDδ不同的两个正概率模型。它反驳有限六标量一般唯一决定完整分布，不反驳原文的全矩原则，也不声称真实Ge的完整矩阵元数据无法区分它们。 | task-derived-finite-moment-nonidentifiability | exact-rational-nullspace-and-positive-distributions | CL86-D20-5/8; day20_finite_moment_identifiability150.py; canonical note checkpoint150 | true |

完整模型与比较表写入[[day20-quadrupole-collectivity-systematics-synthesis]]。两模型刻意具有强Q–C相关；不满足独立假设，不用它们否定该假设下的公式。没有原events、实验Cov、波函数或GOSIA输入，不能据本反例推翻作者的某个具体实验拟合。有限矩/分布参数化这一层，仍应与矩阵元网络的可测性和截断完整性分别审计。


### checkpoint151：可得后续实现

[[gosia-2012-manual-sigma-invariants]] GM12-D20-1–3给出2012手册/公开源码的奇次正幅度矩插值与误差近似。它说明一种具体实现的约定，仍不证明Cline1986或AY23实际采用相同producer，也不修订Fig4字面。
