---
type: source
title: "PDM 确定性报告修订的冻结输入、响应快照与诊断证据"
title_original: "PDM deterministic report revision: frozen jobs, response snapshots and diagnostics"
aliases: [PDM确定性报告修订数据20261124]
created: 2026-11-24
updated: 2026-11-24
status: ai-draft
review_status: unreviewed
source_type: research-code-and-data
reading_depth: read
year: 2026
canonical_source: "User-authorized local deterministic report revision of the frozen multipolePDM 0.1.1 jobs, 2026-11-24"
raw_file: "raw/writing/pado/20261029_review_v1/PDM/figures/data/report_revision/manifest.json"
raw_sha256: "9af8408c9c8b59c20a430f9283bdbb500b47c8e8cf6d6b2ccc10881242bde49c"
raw_storage_status: archived-local
archive_required: true
citation_key: PDMDeterministicReportRevision20261124
evidence_sources: [multipolepdm-20261120-v011-validation, multipolepdm-20261120-empirical-validation, pdm-20261120-error-geometry-grid-study, polarization-delta-collection-20261119-source]
tags: [pdm, deterministic-validation, response-grid, finite-domain, polarization]
---

# PDM 确定性报告修订：软件生成证据

## Bibliographic Record

这是用户授权的本地软件生成结果集合，用于重放冻结nominal job、保存响应数组并修订图文报告。它不是新采集实验、独立实验验证论文或文献δ真值表。`raw_file`指向最终集合manifest，登记179个实际文件及其SHA-256和大小，共816969691字节；包括90页canonical main.pdf、60个二维快照、64幅Python科学图、冻结输入及未改动的0.1.1实现依赖。

配套解释页为 [[pdm-deterministic-report-revision-20261124]]。本轮保留既有工作树和冻结输入，仅在报告层重放与归档，并将这两页接入knowledge/index。`review_status`只保存页面审核历史，不参与证据使用、置信度或任务完成判断。

## Scope and Reading Depth

### Covered scope

- 已读取两个0.1.1批次的完成结果、冻结几何快照及其manifest，核对模式、不同跃迁、混合与纯项分类、读图敏感性及来源依赖；旧结果不是本次重建已完成的证明。
- 已定位六篇文献原件及source，核对主文原件哈希；已定向读取构成0.1075误差工作点的五篇原件相应表格，确认132Ce印刷页码。
- 已读取本次`results.json`的30注入、30文献模型及9前向记录，全部12行`large_delta_diagnostics.csv`，并核对60个NPZ的共同字段。按`figures/revise_report.py`的`assert_frozen`、`diagnostics`及`main`函数定位断言、诊断与快照保存；主任务实际执行确定性重放与独立数值核对。`preview.json`不作为最终证据。

### Not covered

未重做原始计数、效率、Q校准、实验响应或独立阵列重放；未新增随机观测或测量。本页不据文献δ的接近程度选择几何、误差模型或自旋指认；报告的90页版式和60张四联图已逐页核查；该版式验收不替代实验响应验证。

## Summary

冻结证据与本次结果均保持15条不同混合跃迁、30个混合模型和9个纯项前向配置；两个Tl配置属于确定性读图敏感性。另有30个same-kernel确定性注入，未运行随机观测，60条二维记录的冻结统计匹配标记均为true，60套快照齐备。大|δ|诊断同时保留多分支与有限域限制；J与sigma积分均重排质量。0.1075来自十条最终P误差的经验中位数，132Ce定位为印刷第180页Table 2。最终manifest及其哈希已登记；软件仍为0.1.1，未发新版本。

## 六篇文献来源与实际使用位置

| 身份与DOI | source链接 | 本地原件与locator |
| --- | --- | --- |
| Biswas2026，80Se；10.1016/j.physletb.2026.140929 | [[biswas-2026-o6-like-80se-polarization-mixing]] | `raw/papers/gpt/query/20261119-pdm-delta-broad/10.1016_j.physletb.2026.140929.pdf`，PDF3–4 Figs.1–2及Table 1；`raw/papers/gpt/query/20261120-pdm-response-validation/Biswas2026_80Se_supplement.pdf`，Sec.II Eqs.(1)–(3) |
| Lv2022，135Pr；10.1016/j.physletb.2021.136840 | [[lv-2022-evidence-against-wobbling-135pr]] | `raw/papers/2022_Lv et al_Evidence against the wobbling nature of low-spin bands in 135Pr.pdf`，PDF3 Table 1；同名`supplementary.pdf`，PDF1、3–5的角组、门和误差传播说明 |
| Pal2026，185Au；10.1016/j.physletb.2026.140454 | [文献集合source R034](polarization-delta-collection-20261119-source.md#r034) | `raw/papers/gpt/query/20261119-polarization-delta-collection/10.1016_j.physletb.2026.140454.pdf`，PDF2–4 Figs.1、3–4及Table 1 |
| Susshma2025，154Tb；10.1016/j.nuclphysa.2025.123019 | [文献集合source R033](polarization-delta-collection-20261119-source.md#r033) | `raw/papers/gpt/query/20261119-polarization-delta-collection/10.1016_j.nuclphysa.2025.123019.pdf`，Eq.(1)、Figs.1–2、PDF8 Table 1 |
| Starosta1999，164Yb；10.1016/S0168-9002(98)01220-0 | [[starosta-1999-pdco-experimental-test]] | `raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/mixing ratio/1999_Starosta et al_Experimental test of the polarization direction correlation method (PDCO).pdf`，印刷Secs.4、6–7，Tables 2–4 |
| Pal2025，190Tl；10.1140/epja/s10050-025-01678-3 | [六核软件比较source中的Pal2025行](multipolepdm-20261120-empirical-validation.md#key-results) | `raw/papers/gpt/query/20261120-pdm-response-validation/Pal2025_190Tl.pdf`，PDF4 Table 1、PDF6 Fig.7(b)、Sec.4及Fig.8；最终P来自出版图 |

六篇主文身份、原件哈希与可取得的补充关系位于`raw/code/PDM/analysis/cases/results_v0_1_1/results.json:sources`及补充批次同名字段；复用原件不增加独立来源数。135Pr补充材料的完整文件名为`raw/papers/2022_Lv et al_Evidence against the wobbling nature of low-spin bands in 135Pr supplementary.pdf`。

## Key Results

| ID | claim_kind | evidence_level | locator | 内容与边界 |
| --- | --- | --- | --- | --- |
| DR24-1 | model-result | direct | `raw/code/PDM/analysis/cases/results_v0_1_1/results.json:cases`、`failed_runs` | 初始15个混合配置，覆盖10条不同跃迁；nominal及已有加密均记录完成 |
| DR24-2 | model-result | direct | `raw/code/PDM/analysis/cases/followup/results_v0_1_1/results.json:cases`、`kind`、`role` | 补充15混合配置、9纯项前向配置；与初始合计15条不同混合跃迁、30混合模型、9前向配置，不是39个独立实验 |
| DR24-3 | model-result | direct | 同上，`pal190tl-point-angle-jobs_01/07/08`的`input.observations.P`；新结果L28/L29/L30 | 原P=−0.351；−0.356和−0.346两配置的向下／向上误差均保持0.039／0.040，是确定性±0.005读图敏感性，共用同一实测线及DCO |
| DR24-4 | experimental-fact | direct | Starosta1999 Tables 2–4；补充结果的490-keV四个混合配置 | C/D共用R_DCO=0.96(2)，混合假设为14→14；另一个16→14纯E2假设只作前向比较，均不新增谱线 |
| DR24-5 | model-result | direct | 两批`reported_delta_used_in_inference=false`；各冻结`input`及`literature` | 报道δ只作事后对照；未知顺序与指认不因某个输出更接近报道值而被确认为实验事实 |
| DR24-6 | synthesis | direct | [[multipolepdm-20261120-v011-validation]]；本次`results.json:injections[].diagnostics`及`warnings` | 归一、重放一致和网格收敛与参数真值包含、重复实验覆盖率分开；保留全部HDI分支、边界质量与有限域限制 |
| DR24-7 | model-result | direct | 本次`results.json:injections`、`literature`、`forward_only_controls`、`random_draws_executed` | 30个same_kernel确定性注入、30个文献混合模型、9前向；60条二维记录均有冻结统计匹配标记；未新增随机观测 |
| DR24-8 | model-result | direct | `large_delta_diagnostics.csv` S01/S11/S21；`results.json`同ID | δ=−10时无J积分主峰经tan为−1.221761／−1.336728／−1.312688，PDM角边缘主峰经tan为+6.243209／+6.385866／−0.666917；去J曲线只作诊断 |
| DR24-9 | model-result | direct | 同表S10/S20/S30 | δ=+10时无J积分主峰经tan仍为−2.855552／−0.913125／−0.836130；不能把去J等同恢复注入值 |
| DR24-10 | model-result | direct | 同表S21；`statistics.arctan_delta.hdi_segments` | PDCO−10联合峰为(1.4451326206513047,0.225)，角边缘mode为−0.5881759579220891；两段HDI质量0.5780851497131829与0.10191485028681725，统计对象不同 |
| DR24-11 | synthesis | direct | `figures/revise_report.py:184–218`；同表12行与`results.json`完整分量 | 固定注入宽度切片、无J积分与PDM边缘的比较支持J与sigma积分均改变质量分配；不能作单因解释，不能据重放一致消除有限域限制 |

15条跃迁和完整case ID映射见配套研究笔记。纯项前向的九个配置为164Yb490纯E2四个、164Yb647纯E1四个及190Tl943.3纯E1一个；完整曲线在`raw/code/PDM/analysis/cases/followup/results_v0_1_1/forward_curves.csv`及`results.json:runs[].forward`。

初始与补充冻结job分别位于`raw/code/PDM/analysis/cases/grouped_geometry_v0_1_1/snapshot.json`和`raw/code/PDM/analysis/cases/followup/grouped_geometry_v0_1_1/snapshot.json`；同目录manifest登记其哈希。两批包含相同物理输入的几何替代，不能将它们或8次已有加密算作独立文献案例。合成的`Independent 9j`与`same_kernel`不进入文献计数；相同观测的不同生成器不成为两次独立实验。

## P误差工作点的独立定位索引

0.1075的十条样本、左右误差及逐线均值完整列于 [[pdm-deterministic-report-revision-20261124]]。原始冻结记录为`raw/code/PDM/analysis/research/grid_resolution/frozen_inputs.json:empirical_rows`；对应source为 [[pdm-20261120-error-geometry-grid-study]]。

- Biswas2026，PDF4 Table 1：80Se783.5的P=+0.18(3)、671.8的−0.55(20)、895.2的+0.11(7)。
- Lv2022，PDF3 Table 1：135Pr747.3的P=0.04（向下0.13、向上0.08），813.2的−0.03（向下0.12、向上0.05）。
- Susshma2025，PDF8 Table 1：154Tb244.6的P=−0.39(11)、204.7的+0.14(15)。
- Pal2026，PDF4 Table 1：185Au518.1的P=+0.21(15)、292.3的−0.34(12)。
- Paul1997，132Ce351.7的P=+0.03(5)。原件`raw/papers/gpt/query/20261119-polarization-delta-collection/10.1016_S0375-9474_97_00058-4.pdf`，**PDF4、印刷第180页Table 2**；[source R037](polarization-delta-collection-20261119-source.md#r037)。该原件SHA-256为`af48c3dfd17c367e03f8a5663f7b2faa8c882321088583c568a5dc80428f79b2`。冻结行的印刷182–183页locator不准确，本次不改冻结输入。

十条均值的中位数记录为0.1075，是合成研究的经验工作点。它不等于单台极化计系统误差下限，也不覆盖实测逐线误差。80Se同表1035.2的P=+0.37(2)，132Ce同表325.1的P=+0.18(2)，直接说明可报道小于0.1075的绝对误差。误差样本中的154Tb204.7、185Au292.3和132Ce351.7不是本批完成二维反演的额外案例。

## 本次工件、实际结论与归档待补项

集合目录为`raw/writing/pado/20261029_review_v1/PDM/figures/data/report_revision/`。

| 工件 | 角色 | 当前证据状态 |
| --- | --- | --- |
| `results.json` | 本次确定性注入及30文献模型的最终数值结果、冻结输入、统计标记和警告 | 已读取30S／30L／9前向，区间质量0.68，随机观测数0 |
| `large_delta_diagnostics.csv` | 大混合比逐例联合峰、边缘峰、无J积分峰、固定宽度切片峰、质量和包含标记 | 已读取全部12行，对应各模式δ=−10、−5、+5、+10 |
| `S01.npz`至`S30.npz`、`L01.npz`至`L30.npz` | 对应冻结job的响应、Jacobian、观测与参数密度 | 60个文件及共同字段齐全；最终四联图、90页PDF和64幅图形审计均已核验 |
| `manifest.json` | 本轮集合的最终路径、大小、哈希、来源和软件身份 | 未验证；待主代理完成并确认最终SHA-256 |

共同NPZ字段为`angle`、`sigma_over_i`、`parameter_density`、`response_P`、`response_R`、`observation_density`、`valid`、`jacobian`。参数密度保存为对`(ξ,sigma/I)`的密度，写盘时由对`(ξ,sigma)`的密度乘参考自旋I；Jacobian保留核心`(ξ,sigma)`定义。S快照另存`mapped_marginal`、`observation_integral`、`observation_truth_sigma_slice`、`mapped_truth_sigma_slice`及J积分／切片，支撑诊断图，不是新增测量。

实际`assert_frozen`逐坐标比较ETI端点、中位数、所有HDI端点，以及旧结果有记录时的mean/std，绝对和相对容差均为2×10⁻¹⁰；locator为`figures/revise_report.py:164–177`。本页只读核对60个true标记与断言范围，没有重跑断言，也不将其扩写为逐节点数组、各HDI质量／mode或实验物理已独立验证。

配套笔记保存全部12行的大|δ|主峰、各HDI分量质量及包含标记；精确端点和mode_ranges仍以`results.json`为准。S11／S20／S30各有三段，包含触下界的小质量分量。十二例均有角边界警告，S09仅角上界、其余十一例为两端；S09／S10另有sigma上界。所有质量按ξ∈[−89.9°,89.9°]、sigma/I∈[0.03,1]的有限域归一。全30注入的角ETI／HDI包含标记分别20／24，不能当作重复实验覆盖率；文献条目没有δ真值。

## Archive and verification boundary

`archive_required: true`持续有效。最终集合清单SHA-256为`9af8408c9c8b59c20a430f9283bdbb500b47c8e8cf6d6b2ccc10881242bde49c`，与frontmatter一致；每个登记项都有实际路径、大小及SHA-256。canonical报告SHA-256为`62d46bd0dea9bc2657c33889e0434efb10a8fd5fa3d714b451a762b53360ebd4`。早期草稿的空哈希与`source-missing`已由最终集合登记替代，不继续作为当前未完成项。

独立逐格积分核验60个快照的二维归一化、实际68% HDI质量、16/50/84%分位数CDF、所绘PDF的mean/std及角区间/局部mode的tan转换，容差2×10⁻¹²，实际通过记录为集合中的`numerical-validation.json`。相关物理/统计回归77项通过；64幅图的渲染遮挡审计为0 FAIL、0 WARN。90页全部目视，只有第18、19、20页的三张主表为A4横向，表字号8.5 pt，其余正文与四联图竖向。最终嵌入PDF最小有效字形约5.02 pt，无页外文字。

按实际文件和哈希判断归档状态，不使用`review_status`决定证据资格。最终source与179文件manifest的定向归档门实际通过（0失败），两页定向lint通过（0问题）；命令与结果写入原执行计划下的本轮验收回执。全库历史问题与本轮检查分开记录，不宣称全库已无错误。

另核实旧`analysis/benchmarks/manifest.json`对`run_benchmarks.py`、旧`analysis/research/manifest.json`对`pdm/statistics.py`各有大小及哈希错配，共四项；本轮未修改这两个被登记文件或覆盖旧清单。新集合登记的是本轮实际使用的依赖字节，冻结统计重放及独立积分检查通过，但不因此宣称旧清单已修复或当前依赖与历史发布包逐字节相同。此未隔离的旧归档问题阻止Git推送，报告保留本地。

## Competing Interpretations and Limitations

同一源观测的几何、自旋、误差模型或读图变体不构成独立实验；纯项前向和混合二维模型必须分开。统计重放一致只支持对声明软件结果的重现，不能消除有限域、多峰、端点质量、共享校准、未知实际接受度或文献δ提取条件差异。未取得的原始似然或协方差不由模型PDF代填。

## Extracted Pages

- [[pdm-deterministic-report-revision-20261124]]：去重清单、30／9配置、十条误差样本、正确locator与有限域解释。
- [[multipolepdm-20261120-v011-validation]]：已有0.1.1实现与合成控制证据入口，仅作历史依赖；本任务不修改该页。
