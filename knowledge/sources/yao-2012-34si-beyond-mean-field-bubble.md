---
type: source
title: "Yao2012：34Si相关GCM、点质子与电荷密度边界"
title_original: "Beyond-mean-field study of the possible bubble structure of 34Si"
aliases: [Yao 2012 34Si bubble, 34Si GCM density]
created: 2026-10-23
updated: 2026-10-23
status: ai-draft
review_status: unreviewed
source_type: theoretical-model
reading_depth: deep-read
authors: [Jiang-Ming Yao, Simone Baroni, Michael Bender, Paul-Henri Heenen]
year: 2012
journal: Physical Review C
volume: "86"
pages: "014310"
doi: "10.1103/PhysRevC.86.014310"
arxiv: "1205.2262v1"
citation_key: Yao_2012
citation_key_origin: locally-assigned-from-verified-DOI
canonical_source: "https://doi.org/10.1103/PhysRevC.86.014310"
source_url: "https://arxiv.org/pdf/1205.2262v1"
raw_file: "raw/papers/day21-20261023/yao-2012-34si-beyond-mean-field-bubble.pdf"
raw_sha256: "a3e8765895514298dc2479dc935617ed9972af418fcf9acb28fe83b497c0a0d2"
raw_storage_status: existing-raw-read-only-verified-checkpoint124
public_staging_verified_at: 2026-10-23
public_staging_file: "tmp/day21/yao2012/PDFs/Beyond-mean-field_study_of_the_possible_bubble_structure_of_34Si.pdf"
source_independence: theoretical-SLy4-GCM-not-an-independent-density-measurement
nuclei: [34Si, 35Si, 36S, 37S]
models: [SLy4, HFB, Lipkin-Nogami, projected-GCM]
observables: [charge-density, E0-strength, E2-strength]
methods: [particle-number-projection, angular-momentum-projection, generator-coordinate-method]
tags: [a34, correlations, density, model-boundary]
---

# 相关与测量对象怎样改变密度亏空量

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

J.-M. Yao等，Phys. Rev. C **86**, 014310 (2012)。Crossref精确DOI核题名、卷/期、2012-07-09出版日期；实际阅读arXiv1205.2262v1九页，locator不混用期刊页。公开arXiv下载PDF/哈希已核，SI未检；较早预留槽描述由124纠正：该raw路径实际现存且hash与staging一致；本轮只读核验，不归本轮创建或改写，raw/Bib未写。

## Scope and Reading Depth

Day21实际读PDF1–9主线/公式/结论及参考入口，视觉核PDF5–7的Fig.4–7、Table I/II、Eq.(9)–(11)。未运行原GCM代码、取得未舍入密度/transition kernels，也未独立核参考中的实验原数据。Fig.1–3已按文本主线读其说明，本次未逐点数字化或声称所有图的独立复算。

## Summary

Yao等人采用基于SLy4 Skyrme泛函与表面配对相互作用的粒子数和角动量投影发生坐标方法（GCM），研究了关联效应对34Si中预言的质子气泡结构的影响。计算系统分析了球形HF、球形HFB+LN、粒子数投影态以及轴对称四极形变GCM基态在点质子密度与折叠电荷密度上的径向分布演化。结果表明：配对关联使质子2s1/2轨道产生部分占据，而基态的四极形状涨落强烈抹平了密度起伏；点质子密度的中心亏空因子从球形HF的Fmax=0.41下降到GCM基态的0.21，折叠进有限质子电荷半径后可测电荷密度的亏空因子进一步跌落至0.09。这显示该SLy4/GCM模型内关联与有限电荷尺度会改变所定义的亏空；不是实测亏空或实验上限。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| YA12-1 | 计算使用SLy4及surface pairing，HFB态作粒子数/角动量投影并混合不同轴向q；GCM的g(q)依赖离散化且其模方不能直接作找到变形q的概率。 | model-definition-and-coordinate-boundary | direct-original-theory | Eq.(6) | true |
| YA12-2 | Fmax=(ρmax,p−ρcent,p)/ρmax,p，针对点质子密度。Table I给HF/HFB+LN/N&Z/N&Z,J=0/GCM的Fmax为0.41/0.32/0.36/0.30/0.21；并非单调逐步增加相关就必定减小，LN与数投影的角色需分开。 | model-result-and-definition | direct-original-table | Table I | true |
| YA12-3 | 电荷密度由点质子密度同a=0.65 fm Gaussian形状因子卷积；Table II给上述五种状态的Fmax为0.21/0.16/0.18/0.14/0.09。点质子HF的0.41和折叠GCM电荷的0.09同时改变了相关处理和密度对象，不是同一observable的两次测量。 | model-result-and-observable-contract | direct-equation-and-table | Eq.(10) | true |
| YA12-4 | 作者另定Fsat=(ρsat−ρcent)/ρsat，ρsat,p=(14/34)×0.16 fm⁻³；Table I的总密度Fsat,t为负，模型的总中心密度未出现与质子相同的空洞。Fmax和Fsat参考密度不同，数值不可直接混并。 | model-definition-and-limitation | direct-original | Eq.(11) | true |
| YA12-5 | 模型过估ρ²(E0)：58.1×10⁻³对文中所引13.0(0.9)×10⁻³，B(E2;2₁→0₁)也过估，作者据此提示两最低0⁺混合过强；定量相关效应可能依赖泛函。这里实验数字仍是本文引用，非本轮独立原读。 | model-counter-evidence | direct-author-limitation-with-secondary-data | PDF p.5 | true |
| YA12-6 | 结论承认把转移的主碎片间隔当单粒子能量的比较有模型问题；比较35Si/37S需同类计算，近阈值p轨道还涉及continuum，超出本文。本文不能反向认证2017敲出响应或单独终结spin–orbit解释。 | theory-application-boundary | direct-author-caveat | PDF p.8 | true |

## Competing Interpretations and Limitations

1. 作者把34Si模型结果称为质子中心密度凹陷而非总核密度bubble，并没有计算到中心密度为零。总核子密度在中心反而是平坦甚至由于中子中心隆起而略有升高。
2. 本文早于Mutschler 2017实验，不是对其数据的直接反拟合；模型过高估计了ρ²(E0)与B(E2; 2₁→0₁)，暗示其可能高估了四极形状混合的幅度，因而Fmax=0.09或0.21不能作为确凿的实验上限。

## Extracted Pages

- Nuclei: [[experimental-claim-boundaries]]、[[high-spin-lifetime-strength-deformation]]。
- Methods: [[experimental-claim-boundaries]]。
- Synthesis: [[high-spin-lifetime-strength-deformation]]。

## Day21 checkpoint108：超越平均场点质子与电荷密度演化边界审计（124纠正）

108的“已冻结source前回忆/原刊全部9页新原读”认证撤回：该轮实际是arXiv稿的定向文本读取，未留下相应新全文/视觉证据。124实际读取arXiv PDF5–7文字、视觉PDF7两表；原51等其它阅读记录不因本次说明而扩大。raw只读hash a3e8765895514298dc2479dc935617ed9972af418fcf9acb28fe83b497c0a0d2，未重跑GCM。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| YA12-D21-R108-1 | superseded：分开Table I/II与物理对象，改用R124-1/2。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
| YA12-D21-R108-2 | superseded：作者说might indicate而非证明过度平滑，改用R124-3。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
| YA12-D21-R108-3 | superseded：总密度Fsat包含−.06，旧−.08至−.07遗漏N&Z行，改用R124-1。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
| YA12-D21-R108-4 | superseded：后于本文的2017实验比较是任务综合，不可归为2012作者原句。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
| YA12-D21-R124-1 | Table I点质子Fmax按HF/HFB+LN/N&Z/N&Z,J0/GCM为.41/.32/.36/.30/.21，非单调；总密度Fsat为−.08/−.08/−.06/−.07/−.07，均属模型计算而非真实物质密度测量。 | model-table | direct-arxiv-table-and-visual | arXiv v1 PDF p.7 Table I | true |
| YA12-D21-R124-2 | Table II折叠电荷Fmax为.21/.16/.18/.14/.09；HF点质子.41到GCM电荷.09同时改变关联处理和密度对象，不能当同一量的实验差或统一上限。 | model-table-and-object-identity | direct-arxiv-table-and-visual | arXiv v1 PDF p.7 Table II | true |
| YA12-D21-R124-3 | 作者列ρ²(E0)计算58.1×10⁻³/引用实验13.0(0.9)×10⁻³、B(E2)60.5/16.6e²fm⁴，称差异might indicate两最低0⁺态混合过强；中心比4.469/3.645是任务算术，不证明真实混合参数或亏空修正值，实验原引用本轮未独立原读。 | author-caveat-and-conditional-arithmetic | direct-arxiv-text | arXiv v1 PDF p.5 Section III continuation | true |
| YA12-D21-R124-4 | Eq10在给定Gaussian质子形状因子下折叠点质子密度；这是该模型电荷密度合同，不是从一个占据数唯一重建密度的公式。 | model-definition | direct-arxiv-equation | arXiv v1 PDF p.6 Eq.10 | true |

### 124打印舍入控制

Table I的GCM密度打印.057/.073给1−.057/.073=.219178，与打印Fmax=.21不精确相等。若声明密度按最近.001、F按最近.01舍入，则密度舍入区间映射为[.206897,.231293]，与F的打印区间[.205,.215]相交；不应改表强制一致，也不能把该区间当实验CI。四个HF/GCM点质子/电荷控制均按这一合同相容。代码system/scripts/day21_checkpoint124_literal_rounding_scope.py；没有恢复未舍入密度或原GCM代码。
