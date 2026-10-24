---
type: source
title: "Ayangeakaa2019：76Ge低自旋刚性三轴主张与高阶矩证据范围"
title_original: "Evidence for Rigid Triaxial Deformation in 76Ge from a Model-Independent Analysis"
aliases: [Ayangeakaa2019 Ge76 rigid triaxiality]
created: 2026-10-23
updated: 2026-10-23
status: ai-draft
review_status: unreviewed
source_type: experiment-and-structure-interpretation
reading_depth: read
authors: ["A. D. Ayangeakaa", "R. V. F. Janssens", "S. Zhu", "D. Little", "J. Henderson", "C. Y. Wu", "et al."]
year: 2019
journal: Physical Review Letters
volume: "123"
pages: "102501"
doi: "10.1103/PhysRevLett.123.102501"
citation_key: ""
canonical_source: "https://doi.org/10.1103/PhysRevLett.123.102501"
source_url: "https://link.aps.org/accepted/10.1103/PhysRevLett.123.102501"
raw_file: "raw/papers/day20-20261022/ayangeakaa-2019-rigid-triaxial-ge76.pdf"
raw_sha256: "fd549c59e62774b43690a8ae3b5c4bf638982f6c9b888dd0f0aba83b3993b733"
raw_storage_status: reserved-unpopulated-accepted-manuscript-staging-only
raw_archive_verified_at: 2026-10-23
analysis_status: public-staging-original-read-raw-archive-verified
public_staging_manifest: "tmp/day20-ge76-118/manifest.json"
nuclei: [76Ge, 208Pb]
reactions: ["208Pb(76Ge,76Ge*)208Pb"]
experiments: [ATLAS-GRETINA-CHICO2]
methods: [multistep-Coulomb-excitation, GOSIA, quadrupole-invariants]
observables: [E2-matrix-element, M1-matrix-element, quadrupole-dispersion, triaxiality]
tags: [rigidity, low-spin, convergence, covariance, ge76]
---

# 刚性主张的实际高阶证据与未提供输入

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

Ayangeakaa等，Physical Review Letters123，102501(2019)，DOI10.1103/PhysRevLett.123.102501，Crossref精确端点核发表2019-09-06。本session实际读取APS/CHORUS accepted manuscript，cover1页+正文/参考6页，共7页、1022508bytes，SHA256见frontmatter。首页Dated2019-07-26；下载metadata的publishedVersion标签不覆盖cover明确的accepted身份，未逐字核最终排版版本。

PDF在tmp，实际路径见public_staging_manifest；raw_file为未填归档槽，raw/PLAN/Bib未写，citation_key空白。SI沿auto配置关闭，不声称SI已读或不存在。本测量是新counts配合外源spectroscopic constraints，不能与这些旧约束无条件重复计独立证据。

## Scope and Reading Depth

primed-recall-118在lookup前冻结；已知Poves批评及76Se实验边界，非盲测。本session实际读PDF1–7全部正文/致谢/参考文献；视觉核PDF3–6的全部Figs1–5、TableI、形状转换与耦合/高spin限制段。未取得完整103矩阵元集、原yield/门效率数值、exact GOSIA job/producer/jointCov及Ref37全文；不从部分表重造Fig5误差或实际CI。

## Paper Question and Scientific Motivation

PDF2/3摘要及引言：以E2矩阵元和高阶不变量检验76Ge低spin刚性三轴，而非仅靠γ带能量交错。原文已列RHB动态软度、TPSM/SCCM刚性与无需γ形变的替代模型；不能把文章当无争议的模式标签。

## Method and Design Logic

PDF3/4：ATLAS两次实验、三束能304/291/317MeV；208Pb.5mg/cm²配Al/C层，GRETINA与CHICO2测粒子符合γ。三能量各分七角组，GOSIA联合新yield及旧寿命、branch、E2/M1混合比。103是E2和M1 reduced matrix elements合计，不能改写成103个E2或103次独立测量。TableI仅给相关E2子集，caption把完整集合指向Ref37的forthcoming publication。

## Key Evidence and Reasoning Chain

多步激发/角门yield与外源约束 → 带符号矩阵元 → q2与平均cos3δ → 高阶dispersion的不同耦合计算 → 作者对低spin三态刚性的判断。完整矩阵元/误差相关和高阶实现是复核最后两步所需的输入，不能用“有表/读完原文”替代。

## Summary

与[[henderson-2019-triaxiality-selenium76]]只报实验平均三轴性不同，本文明确声称76Ge最低0₁/2₁/2₂态刚性三轴。作者以较小的高阶dispersion及耦合方案相容性支持；本短文未列全部矩阵元与原Cov，且不展示高spin软度。保留原主张及其范围，同时追踪[[poves-2020-limits-assigning-nuclear-shape]]的竞争模型结果，不提前裁决实际实验精度。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| AY19-D20-1 | 三束能量各七角组与旧spectroscopic constraints进入GOSIA；作者报告103个E2/M1的模和符号。TableI明确只列部分E2，完整集合待Ref37；目前不能只据本表重建全部高阶矩或jointCov。 | experiment-and-published-input-scope | direct-original-and-visual | PDF3/4 experiment/analysis; PDF4 TableI caption; PDF7 Ref37 | true |
| AY19-D20-2 | TableI ground到2₁–2₅的RME分别.526(2)、.089(3)、.061(3)、.054(4)、.023(6)eb，2₁对角−.24(2)eb、2₂对角+.26(+.02/−.05)eb。这些带号矩阵元是fit输出，不是B模或不受旧约束影响的独立实验量。 | literal-reported-matrix-elements | direct-table-and-visual | PDF4/正文3 TableI | true |
| AY19-D20-3 | Fig3的q2在两带约.30e²b²，对应按R=1.2A^(1/3)fm电荷形状转换β≈.28；Fig4平均cos3δ约.15/.24，对应约27/25°。这是作者的有限网络/形状参数解释，不直接测mass deformation或任意态静态Qs。 | reported-invariant-and-shape-interpretation | direct-original-and-visual | PDF5 Figs3/4 and conversion paragraphs | true |
| AY19-D20-4 | Fig5以最低0₁、2₁、2₂态的σ⟨cos3δ⟩比较三个耦合方案，作者据较接近0及方案相容称刚性三轴。图文另给harmonic≈.6、soft≈1作参考；本任务不把这些推广成所有模型/核素通用硬阈值。图没有逐点数字表，未digitize误差/重新给CI。 | author-rigidity-inference | direct-original-and-visual | PDF5 discussion leading toFig5; PDF6 Fig5 and following paragraph | true |
| AY19-D20-5 | 高spin的dispersion数据未展示，作者说随J增加的可用集合不完备会降低判断确定性。不得用两带平均β/γ相容去宣称所有高spin态刚性已经测全。 | explicit-spin-and-completeness-boundary | direct-author-limitation | PDF5 last paragraph; PDF6 opening paragraph | true |
| AY19-D20-6 | 作者把不同J=0/2/4 coupling结果称independent，并把相容性作为convergence证据；这些函数来自同一矩阵元拟合集合。数学耦合不同不自动意味着统计独立的新实验/误差源，需实际Jacobian与原jointCov才能判联合信息。 | author-convergence-criterion-versus-task-statistical-boundary | direct-text-plus-explicit-task-inference | PDF5 Figs3/4 discussion; PDF6 Fig5 discussion | true |
| AY19-D20-7 | 原文明确76Se已有显著三轴成分，但其rigidity未定；Se较软是由交错模式提出的可能。Ge刚性主张不能自动外推Se、A≈130或其0νββ NME数值。 | cross-nucleus-inference-boundary | direct-author-comparison | PDF6 discussion beforeConclusion | true |

## Competing Interpretations and Limitations

[[poves-2020-limits-assigning-nuclear-shape]] PO20-D20-6的76Ge宽γ来自选定CI模型，高阶方法/质量-电荷定义、数据截断和参数传播均要对齐。原文Fig5支持方的低spin实验主张确实存在；不能因76Se未测rigidity而抹去Ge的主张，也不能凭作者结论或后来的模型标题替代比较。完整103集合、producer与Cov未得，保留P1复核路线。

## Analytical Reconstruction

AY19-D20-6只作统计层面的任务推断：若三个coupling结果均是同一RME向量m的函数fₐ(m)，则一阶Cov(fₐ,fᵦ)=Jₐ Cov(m) Jᵦᵀ；off-diagonal没有因函数表达不同而自动为零。这不指控作者实际采用独立误差，也不估其真实CI。是否遗漏相同高态strength，需完整输入与收敛设计，不能由图中相容点数直接决定。

## Knowledge Impact and Learning Decision

revises：争议矩阵应保留Ge实验高阶刚性主张、Se实验仅平均三轴性、Poves竞争模型软度三种不同对象。supports：[[day20-quadrupole-collectivity-systematics-synthesis]]和[[transition-quadrupole-moment]]对完整网络、符号/Cov及原producer的要求。下一追Ref37的实际后续完整论文；不因短文未列全就断言完整数据永不可得，不对原实验作置信认证。

## Related Knowledge and Project Relations

- competing-interpretation：[[poves-2020-limits-assigning-nuclear-shape]]，同76Ge的宽γ模型解释。
- limits：[[henderson-2019-triaxiality-selenium76]]，不同核和不同高阶可达性不能并成一个实验主张。
- methodological-bridge：[[henderson-2020-quadrupole-invariant-convergence]]，高阶有限网络收敛需求。
- supports：[[day20-quadrupole-collectivity-systematics-synthesis]]、[[transition-quadrupole-moment]]，实验/模型/数学合同分层。

## Human Review Triage

按ingest-strategies的Agent self-audit定义，review保持unreviewed。P0: none identified。P1：AY19-D20-1/4/6的完整集合、原高阶程序/Cov及耦合相容性与遗漏strength关系待核；AY19-D20-5的spin边界与PO20-D20-6模型比较须保持。P2/P3：accepted版本身份优先、raw deferred、103混合总数和图示参考值不作硬阈值。

## Extracted Pages

PDF1：CHORUSaccepted cover；2/正文1：摘要/动机与作者；3/正文2：竞争模型/方法与Fig1；4/正文3：分析、Fig2/TableI及不变量定义；5/正文4：Figs3/4、参数转换、高阶/高spin限制；6/正文5：Fig5、刚性/Se比较、结论/致谢/Refs1–16；7/正文6：Refs16–45与Ref37/44原读后续入口。

## Day21 checkpoint005旧认证撤回（047定向原件复核）

005把Henderson样本统计改成76Ge伪刚性证明，以及宣称103个RME必有强非对角病态协方差，均超出当前原件证据。旧段逐字存本run `superseded-047/ayangeakaa-2019-rigid-triaxial-ge76-day21-before-047.txt`。原实验结果、作者刚性解释和review/flags保持；不把撤回本任务认证写成撤回论文。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AY19-D21-1 | superseded：005由模型平均截断低估直接判76Ge刚性假象的认证撤回；本任务未取完整高阶网络/producer/jointCov，不能确定真实截断偏差大小/方向或强相关程度。 | withdrawn-task-certification | rejected-and-replaced | checkpoint047 original-source audit | true |

## Day21 checkpoint047：保留低自旋刚性主张与实际复核缺口

冻结primed回忆后新读实际accepted manuscript全7页（含CHORUS封面及参考），视觉核PDF4–6全部表/图2–5；实际raw存在且SHA256 `fd549c59e62774b43690a8ae3b5c4bf638982f6c9b888dd0f0aba83b3993b733`匹配。未核VoR逐字一致性，未运行GOSIA；早先staging记录保历史，原review/flags不变。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AY19-D21-R47-1 | 文章报告GOSIA拟合103个E2/M1 RME，Table I只列E2子集，完整集合当时指Ref.37 forthcoming。新yield与旧寿命/branch/δ共入拟合，因此这些RME是有约束拟合结果，不是103次独立观测或直接测内禀坐标。 | extraction-and-input-scope | direct-original | PDF p.4 Table I | true |
| AY19-D21-R47-2 | Fig5与正文以0₁、2₁、2₂的较小角度dispersion及不同coupling相容支持低自旋刚性三轴；高spin数据因不完备增加而不展示，不能将全部已观测态都认证刚性。作者确有rigid主张，本任务没有用Henderson模型结果推翻它。 | author-rigidity-interpretation-and-spin-boundary | direct-original | PDF p.6 Fig.5 | true |
| AY19-D21-R47-3 | 原文把coupling结果称independent并用相容作收敛证据；它们均由同一拟合RME集计算，统计独立性需实际Jacobian与jointCov核验。未得原jointCov时既不能默认独立，也不能量化强非对角相关、病态程度或新CI。 | statistical-independence-task-boundary | source-plus-explicit-task-inference | PDF p.5 coupling-convergence paragraphs | true |

[[henderson-2020-quadrupole-invariant-convergence]]的HE20-D21-R47-1明确四阶σ(Q²)与需六阶的角度宽度不可混写；其sd/pf样本不包括76Ge实际误差模型，也没计算本测量巨共振遗漏贡献。可以说高阶完备性与误差传播需独立检查；不能说已经证明本核其实γ软或σ≈0必为假象。下一步沿Ref.37的实际后续全文/输入集核版本、全部高阶路径与jointCov，再做逐态、逐coupling稳定性与遗漏强度界；缺少这些输入时保作者解释与待检验边界并列。


### Checkpoint048：Ref37已定位，不把后续输入继续写成不存在

实际后续为[[ayangeakaa-2023-ge76-coulomb-excitation-full]]（PRC107,044314），其正文明称follow-up并以Ref27回指本PRL。AY23-D21-R48-1至4新核作者误差更正、表列/态编号与相关性合同：81为E1/E2/E3/M1总数，与本短文103 E2/M1不同口径，不能只由两数断定参数删减或完备性。完整长表已可读；原job、联合Cov及未列高阶子块仍未取得。旧TableI的2₅相关行/2₁→4₂误差必须带版本使用，不与后续表按下标拼接。原review/flags及047撤回保持。
