---
type: source
title: "四极不变量与角动量通道指标：Nomura2016、Rouoof2025、Frauendorf2026及Lawrie–Orce2025原始先例集合"
aliases: [quadrupole invariant spin-channel precedents, finite-spin E2 proxy precedents]
created: 2026-11-06
updated: 2026-11-06
status: active
review_status: verified
source_type: primary-source-collection
reading_depth: skimmed
title_original: "Source collection: quadrupole moments, angular-channel diagnostics, and shape-conversion regimes"
authors: ["K. Nomura et al.", "S. P. Rouoof et al.", "S. Frauendorf et al.", "E. A. Lawrie and J. N. Orce"]
year: 2026
year_basis: "Collection-audit year; individual publication years are retained separately."
publication_years: [2016, 2025, 2026]
canonical_source: "collection:quadrupole-invariant-spin-channel-precedents"
citation_key: QuadrupoleSpinChannelPrecedentsCollection20261106
citation_key_origin: "Local collection key; cite the individual papers for their scientific results."
raw_file: "raw/papers/gpt/query/20261106-quadrupole-invariant-spin-channel-precedents-collection/manifest.json"
raw_sha256: "f0b7648dd1a8f17a738a8df8354c26c861dc58acb89b446a514e54ddfc10c021"
raw_storage_status: archived-local-collection-of-existing-originals
archive_required: true
source_independence: multiple-dependent
analysis_status: targeted-original-source-and-locator-audit
nuclei: [147Eu, 149Eu, 151Eu, 153Eu, 155Eu, 147Sm, 149Sm, 151Sm, 153Sm, 155Sm, 72Ge, 76Ge, 104Ru, 168Er, 186Os, 188Os, 190Os, 192Os, 194Pt]
application_anchor: "odd-A Ba, J=11/2; applicability comparison, not a source result for these Ba states"
models: [IBFM, TPSM, generalized-triaxial-rotor]
methods: [quadrupole-invariants, angular-momentum-channel-decomposition, Coulomb-excitation]
observables: [E2-matrix-elements, spectroscopic-quadrupole-moments, reduced-transition-strengths]
tags: [a130, odd-mass, finite-spin, quadrupole-invariants, source-dependence, interpretation-boundary]
---

# 四极不变量与角动量通道指标的原始先例

## Bibliographic Record

本页是四个原始来源的集合，不是一篇新发表论文。引用时使用对应论文及其实际 locator，不把集合年份、`citation_key` 或本页核验状态作为论文身份或科学准入。核验依据是原件、适用条件和来源依赖；这里没有人工批准要求，也不作优先权认证。

| ID | 原始来源与版本 | 归档原件 |
|---|---|---|
| N16 | K. Nomura, T. Nikšić, D. Vretenar, *Signatures of shape phase transitions in odd-mass nuclei*, PRC **94**, 064310 (2016), DOI `10.1103/PhysRevC.94.064310`；核查 author-preprint `arXiv:1610.00469`。 | [N16 PDF](../../raw/papers/gpt/query/20261106-spin-invariant-precedents/nomura2016-arxiv1610-00469.pdf) |
| R25 | S. P. Rouoof et al., *Microscopic investigation of E2 matrix elements in atomic nuclei*, PRC **111**, 054309 (2025), DOI `10.1103/PhysRevC.111.054309`；核查 author-preprint `arXiv:2502.18076`。 | [R25 PDF](../../raw/papers/gpt/query/20261106-spin-invariant-precedents/rouoof2025-e2-matrix-elements.pdf) |
| F26 | S. Frauendorf et al., *Systematic study of E2 matrix elements in the framework of the Triaxial Projected Shell Model*, `arXiv:2609.10431v1`；arXiv 记录为 **2026-09-09 16:43:36 UTC**。本次未建立期刊发表身份。 | [F26 PDF](../../raw/papers/gpt/query/20261106-spin-invariant-precedents/focused-sidecar/frauendorf2026-systematic-tpsm-2609.10431v1.pdf) |
| L25 | E. A. Lawrie, J. N. Orce, *Triaxial nuclear shapes from simple ratios of electric-quadrupole matrix elements*, ADND **164** (June 2025), 101730, DOI `10.1016/j.adt.2025.101730`；publisher PDF 在线日期 **2025-04-25**。 | [L25 PDF](../../raw/papers/gpt/query/20261106-spin-invariant-precedents/focused-sidecar/lawrie-orce2025-simple-ratios-publisher.pdf) |

集合清单引用上述四份 PDF 和 F26 arXiv 记录、L25 Crossref 记录，共六个既有原件。逐文件路径均相对于仓库根，保存 SHA-256、大小、原始 URL、原获取 UTC、访问范围和原清单来源。组装集合时没有复制、重新下载或修改原件，也没有修改原清单。L25 原件标示 CC BY-NC-ND 4.0；arXiv 公开访问不被扩写为任意再分发授权。

## Scope and Reading Depth

**Covered scope：** N16 的 Eq.(8)、Fig.10 及耦合方式讨论；R25 Sec.IV C 与结论中的网络截断、组态混合比较；F26 六页正文和参考文献依赖；L25 正文方法、适用条件、Fig.3 比较及 Table1 的来源说明。N16 Fig.10、F26 p.4 和 L25 p.3 的关键页面已视觉核对。下列页码均针对上表实际归档版本。

**Not covered：** 没有重跑这些作者的代码、重新拟合 Coulomb-excitation 数据、逐项重分析 L25 的全部核素表，或独立读取它们引用的每一篇实验原文。N16/R25 未逐字对照 publisher 最终版。集合的 `skimmed` 记录限定阅读范围，不是对已定位主张的可信度排序。

本页只固化文献先例与可复用解释边界，不把本任务 odd-Ba 数值结果、角度、静态矩或实验可行性当作上述论文的结论。

## Summary

N16 已在奇质量核中展示不同角动量跃迁通道的结构敏感性；R25 已比较较大微观 E2 网络与实验可达子集；F26 延续同一 TPSM 研究并讨论微观混合导致的诊断差异；L25 展示有限矩阵元比值在明确转动条件下与 Kumar–Cline 结果相容的情形。因此，“有限通道”“微观混合”或“effective 比值”本身都不能被直接当成新方法或错误公式的证据。

这些工作没有在本次核查段落中给出固定 \(J=11/2\) odd-Ba 链的完整通道、静态／非弹性份额和有符号三次环分解。该定位差异只界定已读先例覆盖了什么，不证明相关研究在全领域不存在。

## Key Results

| ID | 有来源支持的陈述 | claim_kind | evidence_level | source_independence | locator |
|---|---|---|---|---|---|
| QSC-N16-1 | Eq.(8) 定义五个向带头衰变的平均 \(B(E2;J_0+\Delta J\to J_0)\)，分别取 \(\Delta J=1,2\)。Fig.10 中 odd-Sm 负宇称带的两种指标呈现不同质量数趋势，作者将其联系到弱／强耦合结构。 | author-interpretation | direct | single | N16 PDF p.9 Eq.(8)；p.10 Fig.9 下方讨论；p.11 Fig.10(a–d) 与 caption |
| QSC-R25-1 | 对每核四条带、到 \(I=10\) 的 187 个计算 E2 元素，作者比较较大网络与具有实验对应元素的子集；对 \(^{76}\)Ge，施加实验子集限制可使计算涨落减小。 | model-result | direct | single | R25 PDF pp.12–13 Sec.IV C，p.13 Fig.13 下首段；p.16 conclusion item 2 |
| QSC-R25-2 | 作者把多准粒子混合与固定三轴平均场之上出现的不同形状特征联系起来，并指出 E2 不变量与 gamma-band 能量 staggering 的集体模型对应关系可失效。 | author-interpretation | direct | single | R25 PDF p.13；pp.16–17 conclusions items 1–3,7–8 |
| QSC-F26-1 | F26 展示一般自旋的二、三阶不变量表达式及微观混合／staggering 比较；其图与计算明确回引既有 TPSM 系列，不能计作 R25 的独立重复验证。 | author-interpretation | direct | multiple-dependent | F26 PDF pp.4–5 Sec.4，Eqs.(10)–(14)、Figs.7–10；p.6 Refs.8–10 |
| QSC-F26-2 | F26 p.5 把所讨论 Os 情形标为 gamma rigid，而 R25 p.16 描述 moderate gamma softness。此处保留原文标签差异，未调和其判据，也不据此判断作者代码或实际核形状。 | synthesis | direct | multiple-dependent | F26 PDF p.5 Fig.10 周围文字；R25 PDF p.16 conclusion item 3 |
| QSC-L25-1 | L25 的四矩阵元关系分开 E2 张量的 \(\gamma\) 与惯量不对称参数 \(\Gamma\)；两矩阵元简化再使用 Eq.(11) 的经验 \(\Gamma(\gamma)\) 关系。作者对选定偶偶转动 \(2^+\) 态与 KC／generalized-rotor 结果进行比较，且讨论混合相关的偏离。 | author-interpretation | direct | single | L25 publisher pp.2–3 Eqs.(5)–(13)、Fig.1；pp.4–5 Eqs.(14)–(15)、Fig.3；Table1 |

## Competing Interpretations and Limitations

**来源依赖。** F26 Ref.9 是 R25；Ref.8 是先前 \(^{104}\)Ru TPSM 研究，Ref.10 是同系列后续工作。重复图与共同模型结果不能增加独立证据计数。R25 的实验比较仍依赖其引用的 Coulomb-excitation 数据；本页未将这些实验全部重新认证。N16 与 L25 是不同研究，但这种区别也不自动构成对同一 odd-Ba 主张的独立验证。

**有限自旋不等于同一物理适用域。** N16 使用多条带的带头指标，没有把其 Fig.10 定义为统一固定 \(J=11/2\) 的完整矩比较。R25/F26 所核示例是偶偶 TPSM 核；R25 的较大网络是声明的带与自旋范围，不是完整物理 Hilbert 空间。L25 的条件是相关偶偶 \(2^+\) 态具有转动性质，并在两元素版本中采用经验 \(\Gamma(\gamma)\) 关系；这不是混合 odd-A \(11/2\) 态的通用形状反演。

**观测量与形状解释。** 通道受限 RME 函数可以是合法的旋转不变标量；它与标准完整电荷多项式矩不同，并不独立构成代数错误。固定 J 跨同位素的强度重分配可以反映真实粒子—核心结构。把某个 effective 坐标解释为内禀 beta/gamma，还需验证耦合、算符和状态条件；单一平均角不能判定 gamma 软度或刚性。这是由上述来源作出的限定综合，不是作者对本任务模型的认证。

**方向和归一约定。** 对这些先例进行数值比较前，必须注明采用向外激发还是反向衰变的 \(B(E2)\)。按标准约化矩阵元定义，
\[
(2J_i+1)B(E2;i\to f)=(2J_f+1)B(E2;f\to i).
\]
因此同一 \(11/2\leftrightarrow15/2\) 态对满足 \(B_\uparrow=(4/3)B_\downarrow\)。N16 的平均向下强度不能直接当作向上强度和；比值分母若改用衰变方向，其对应数值也须改变。这是定义层面的比较规则，不是新不变量理论。

对静态—跃迁比值，须进一步分开
\[
R_{\rm stat}=\frac{D_0}{\sum_\nu B(E2;J\to(J+2)_\nu)},\qquad
R_{\rm stat}^{(1)}=\frac{D_0}{B(E2;J\to(J+2)_1)},\qquad
D_0=\frac{|\langle J\Vert T(E2)\Vert J\rangle|^2}{2J+1}.
\]
前者用声明范围内的通道总和，后者只用已识别的第一态。若另定义直接以反向衰变强度作分母的 \(R_{\rm stat,\downarrow}^{(1)}\)，则
\[
R_{\rm stat,\uparrow}^{(1)}
=\frac{2J+1}{2J+5}R_{\rm stat,\downarrow}^{(1)}
=\frac34 R_{\rm stat,\downarrow}^{(1)}
\quad(J=11/2).
\]
对相同 \(J+2\) 态集合的求和也适用这一因子。同自旋非弹性跃迁的正反 \(B(E2)\) 相同。静态 \(D_0\) 不是零能 gamma 衰变；这些关系要求同一态对、同一 E2 分量与一致单位，不能替代实际能级映射或实验覆盖核查。

**核物理推断边界。** 完整有限模型闭合、核心单个 \(0\to2\) 校准和奇核静态／非对角矩阵元的物理检验是不同问题。数据不完整时，应比较相同已测子集并评估遗漏路径，不能从少量无符号 \(B(E2)\) 重建有符号三次环，或把一个通道的饱和冒充完整矩阵元覆盖。

**恢复后的三源直接对照。** 2026-11-06再次读取N16 PDF2–3、9–11，R25 PDF2–3、12–13、16–17，以及L25 PDF1–5，并核对N16 Eq.8、R25 PDF13和L25 PDF3页图。L25 Eq.12的比值显式同时依赖电荷gamma与惯量Gamma，因此几何／动力学分离本身已经是直接先例，不是当前稿的新原理。当前候选增量限于指定全J+2诊断的严格电荷几何控制和具体模型的静态／带符号路径响应。详细边界见[[odd-ba-novelty-overlap-and-contribution-boundary]]；三源对照没有升级为全球优先权证明。

**优先权边界。** 本页不是系统性综述、作者程序认证或论文新颖性证书。它给出已核查的直接先例与适用条件；检索未命中和“所读段落未展示某比较”都不推出不存在先例。历史审核标注不替代原件证据，也不触发人工批准。

## Extracted Pages

- **N16：** PDF p.9 Eq.(8)；p.10 耦合方式与两类通道的相反趋势；p.11 Fig.10(a–d) 与 caption。原文短摘录定位为 “depends on whether a band exhibits a weak-coupling or strong-coupling systematics.”
- **R25：** PDF pp.12–13 Sec.IV C；p.13 实验可达网络限制；p.16 conclusion item 2 的较小涨落结果，item 3 的 Os 描述；p.17 同系列后续工作与解释边界。
- **F26：** PDF pp.4–5 Sec.4、Eqs.(10)–(14)、Figs.7–10；p.6 Refs.8–10 与数据／计算依赖。arXiv 版本日期由集合中的原始记录核定。
- **L25：** publisher pp.2–3 的转动适用条件、Eqs.(5)–(13) 和 Fig.1；pp.4–5 的 Eqs.(14)–(15)、Fig.3 与混合例外；Table1 pp.7–9 的输入和来源说明。未重算全部表项。

原始摘录和页面图像仅在临时证据目录保存；本页回链到未修改的原件及哈希集合，不以审计输出代替论文来源。
