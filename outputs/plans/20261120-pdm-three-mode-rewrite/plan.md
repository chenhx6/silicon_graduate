---
title: "multipolePDM：当前报告修订合同"
date: "2026-11-20"
updated: "2026-11-24"
status: completed
phase: report_revision
report_update_authorized: true
goal_id: "01a20bbe-dfb1-77f3-a6a9-fd264a759483"
---

# PDM 报告修订计划与验收合同

本文件是当前规格，`tasks.json`是当前账本。目标为修订秘书报告的物理说明、全部确定性注入长表、全部文献四联图及大混合比诊断。**R00–R05全部完成：90页canonical报告、60张四联图、179文件定向归档及知识回写均通过验收。后续用户已授权整理并推送Git基线；原两处源码升级造成的四项大小／哈希错配已用精确历史快照解决，不再作为当前发布障碍，不发新软件版本。**历史E01–E03、U00–U09的完成与0.1.1发布事实保留，不能代替报告验收。

`plan.pdf`是**20261120历史阅读快照**，不再与本文件同步；当前以`plan.md`为准。本轮不生成额外计划PDF。

## 1. 范围、写域与交付

- 当前goal为`01a20bbe-dfb1-77f3-a6a9-fd264a759483`。本轮不重构GUI或共享物理/统计核，不新增发布，不读取发布凭据，不运行新随机测试，不添加卡方拟合。
- 主交付为`raw/writing/pado/20261029_review_v1/PDM/main.tex`与同目录唯一报告`main.pdf`；图表代码、数据引用与清单位于`figures/`。优先读取现有analysis结果，允许报告层确定性整理、诊断与重绘；缺二维数组时按冻结任务重建并逐项核对原统计，不重复改造或重新抽样。
- 报告阶段的计划侧审仅修改本目录`plan.md`、`tasks.json`，主代理负责报告与知识归档；该阶段已完成，无活动侧审写域。后续Git整理按用户新授权执行，不扩展为GUI重构或新软件发布。
- 不改实测P/R及左右误差、文献原件、既有结果或历史验收回执。编译中间物、全页预览与布局诊断留仓库`tmp/`；不另造第二份报告/计划PDF。
- R05由主代理按证据门回写知识及维护归档；只有计划改动时不得声称已完成报告、知识回写或归档收尾。

## 2. 物理定义与参数口径

三模式共用联合辐射模型和一个PDM核：

| 模式 | 偏振 | 比值 |
|---|---|---|
| `P_ADO` | 目标单线P | 单线角分布比R_ADO |
| `P_DCO` | 无伴随光子方向条件的目标单线P | 联合符合强度R_DCO |
| `PDCO` | 指定门方向条件下的目标P | 联合符合强度R_DCO |

目标电场平行/垂直强度记为C_parallel/C_perp，门偏振已求和。单线P先对伴随光子的全部方向积分两通道强度，再作差除以和；条件P保留门方向后取比。目标先发为POL–DIR，目标后发为DIR–POL。单线P不依赖DCO门探测角，但可依赖上游未观测传播。测一条线的P不自动证明无方向门；电场轴不能直接换成Compton散射计数标签。

R_DCO分子为目标A、门B组的联合强度，分母为目标B、门A组；不能用单线W之比或丢失门出现概率的归一化条件概率之比代替。R_ADO才用单线W之比。门身份、比值次序与发射顺序分开记录。

### 2.1 一个Gaussian源与传播

- 核心坐标为xi=arctan(delta)（rad）和sigma。源态p_m正比exp[-m²/(2 sigma²)]，在合法离散m归一。sigma是指数宽度，不是方差，也不普遍等于有限离散布居的实际rms；方差为sum(m² p_m)，等布居极限为I(I+1)/3。sigma=I不是严格无取向极限。
- P_ADO源态为目标初态；DCO两模式为路径最上游被观测光子发射前的共同源态。sigma/I的I始终为此源自旋，不暗换成下游目标自旋。
- 每点只生成一份源Gaussian。未观测跃迁按完整密度矩阵映射或等价U_k传播；混合跃迁按辐射强度加权，U_0=1，多步相乘。下游/方向条件态一般非Gaussian，不拟合第二个独立sigma，不写sigma_after=U sigma。
- 默认数值工作下限为整数sigma=0.15、半整数0.20，上限I；相邻磁子态布居比约10^-12的判据与Jacobian近零警告不同。
- 保留KS/Droste辐射振幅比及Starosta带撇磁项勘误，不因恢复结果改相位。禁M1的纯E2只作前向控制；允许混合跃迁的纯E2注入为端点诊断，无有限delta真值。

### 2.2 几何与权重

未选择phi时，在固定theta锥面上平均原始强度；不是phi=0或4pi积分。PDCO仍保留门theta。DCO与偏振门的方位条件分别遵守冻结输入。全部组先分别合并平行、垂直或联合强度，再形成P/R；不平均角度、P或R。默认组内归一权重与原始加权和不静默互换；有效权重模型不等于完整效率重放。

- 合成：比值A125度/B90度，P90度，PDCO偏振门125度，未选择phi。
- 135Pr：R_ADO=[2W(157.6度)+W(133.6度)]/[3W(75.5度)]，P75.5度；不退回145.6/90代表角。
- 154Tb、190Tl主场景为已声明的无phi筛选理想环；旧点方位只留历史敏感性。
- 其余实测沿用各自冻结几何，不把合成P90度套到文献；185Au比值顺序、164Yb门及自旋假设逐项标记，不算新增独立实验。
- 80Se原文P+DCO固定宽度与本库P+ADO扫描宽度的路线不同，文献比较保留该条件。

### 2.3 Jacobian与测度

保留f_map(xi,sigma)正比f_obs(P,R)|det d(P,R)/d(xi,sigma)|并在声明有限域归一。实际坐标（含较短末格）用于差分和积分；P/R交换只改变有符号det符号。

固定I、同物理域下，s=sigma/I满足J_(xi,sigma)=J_(xi,s)/I、f_(xi,sigma)=f_(xi,s)/I，展示密度f_(xi,s)=I f_(xi,sigma)。delta变换满足J_(xi,sigma)=(1+delta²)J_(delta,sigma)、p_delta=p_xi/(1+delta²)。degree/rad换算同时作用于导数与密度。

Jacobian<=10^-12仅为坐标相关诊断，不裁小正质量；恒等响应det=0不得归一成二维PDF。R03解释多对一映射、分支重数与|J|权重，区分观测密度、似然与参数密度；不把该权重写成常数参数先验，不称局部det非零保证全局唯一。本轮诊断不替换推断核。

实现定位（相对`raw/code/PDM/GUI/`）：`docs/response-reference.md`、`src/multipolepdm/physics/{populations,propagation,joint}.py`、`models/registry.py`、`pdm/mapping.py`。手册用`eq:population`、`eq:B`、`eq:propagate`、`eq:common-joint-p`、`eq:joint-ratio`、`eq:pdm`定位。原件回链Droste 1996 Eq.19与pp.519–524、Hamilton第12章Eqs.12.80–12.81/12.209–12.219、Starosta 1999 p.17 footnote 1。

## 3. 统计、表图合同

- 精确68% ETI/HDI先在完整xi边缘密度评估，再逐端点、q50和各段mode取tan报告delta；不改成按delta密度重新排序HDI。
- 每个HDI连通段保留lower、mode或并列峰范围、upper、分段质量；质量总和0.68。不得用全局mode替代其他段中心或用最外端点包络替代不连通集合。
- ETI为完整PDF的q16/q50/q84；Mean用积分权重求角mu/SD，再显示tan(mu)与有效tan(mu±SD)。后者不是E[delta]/delta标准差或68%区间，越域/正切奇点明确标记，不静默裁切。
- sigma/I在自身完整边缘密度评估同样三类统计，不取tan。文献误差照原报，置信水平缺失标as reported；固定、提取和未报道宽度区分。
- 输入误差沿用中位数分侧正态变换：每侧半概率、端点Phi(-1)/Phi(1)，不等误差中心密度跳跃；与精确q16/q84略有差别。P/R乘积密度为独立误差近似，不由单线定义推出。E01比较结果留后台；正文保留现行误差定义，不从三个数字唯一确定分布或宣布光滑模型最优。

### 3.1 全部四联图

每个nominal文献二维声明模型均给出完整四联图和数值，不以汇总图替代：

| 面板 | 内容 |
|---|---|
| A | R_ADO/R_DCO横轴、P纵轴；全部有限有效响应与完整实验左右误差棒；色值为观测密度 |
| B | arctan(delta)横轴、sigma/I纵轴；正确变换的二维参数密度 |
| C | 完整角边缘PDF与delta三类数值 |
| D | 完整sigma/I边缘PDF与该坐标三类数值 |

A/B为viridis、独立色标；不只显示实验附近±5误差、不按95%包络裁域、不强连折叠网格。角轴写arctan(delta)、用pi分数刻度，计算仍为rad；宽度轴写sigma/I，无ref/dimensionless赘词。

C/D黑色PDF；橙色q16/q50/q84合用`68% ETI (16%, 50%, 84%)`图例；灰色mean及mean±SD合用`Mean +/- SD`且默认可见；蓝色HDI从0填到各段PDF、保留间隙，水平虚线为68%HDI密度阈值。附全部HDI分段、ETI和Mean-based数值。标题沿用`Full Range Marginalization; Constant Weight`，解释全域边缘化与常数附加权重。

### 3.2 输入—输出表与文献索引

三模式各一张10行主表，每个案例连接唯一四联图编号。每行给出mode、注入delta与arctan(delta)、P/R及左右误差、角HDI各段及mode、直接tan后的delta表示、角与delta的ETI(q16,q50,q84)，以及恢复sigma/I的HDI/ETI。目标自旋、注入sigma/I、源态身份、门线/次序、比值分子分母角度/权重、P角及phi条件在紧邻公共设置中明确，不重复I_ref、sigma0字段。各段质量、mean/std及全部精度由同一PDF/JSON保留。

文献使用全部30个nominal二维模型的输入索引和对应四联图；15条不同跃迁、共用输入与两个历史确定性读图平移分开计数。原来的18模型“图6”及其它汇总展示留后台，不作为本轮新增必做图，也不替代全部案例。文献报道值始终是比较值。

## 4. 确定性注入：30条主记录

主报告`primary_records=30`，固定选`same_kernel`。三模式各10个delta：[-10,-5,-1,-0.5,-0.1,+0.1,+0.5,+1,+5,+10]。独立9j另30条只留后台核对，不重复进主表/主图，不称60个主案例或独立实验。

目标5->4 M1/E2；DCO目标先发、门4->2纯E2。I_ref=5，sigma/I真值0.3即sigma=1.5；反演仍扫描sigma全域。P90度、R125/90度、PDCO门125度，未选择phi。

先生成无附加噪声P0/R0，再赋对称Gaussian一标准差：DeltaP=max(0.1075,0.8|P0|)、DeltaR=0.1|R0|。floor是十条已核主层谱线左右P误差均值的跨线中位数，样本/locator见`analysis/research/grid_resolution/frozen_inputs.json`；是合成工作点，不是通用实验下限，不改真实误差。近零P不赋零宽误差，误差棒越[-1,1]不裁短。

主网格xi±89.9度、步长0.1度；sigma/I域[0.03,1]、步长0.005，即sigma[0.15,5]、步长0.025；实际末格和节点数保留。既有加密、±89.99度扩域、纯E2端点仅作诊断，不增加主案例计数。

每模式主表完整放在一页A4横页，共三页；字号8.5 pt。角量为rad，默认小数点后两位，小于0.005的非零值用科学计数法；扫描设置保留还原网格所需精度。其余正文、短表、四联图均为A4竖版。

按模式的恢复对照图逐案例显示ETI中位数、全部HDI分支与局部mode及注入菱形；delta图使用对称对数轴完整容纳远端分支，宽度图标出0.30。所有30张四联图的C/D面板已经包含完整角/宽度PDF，不再增加仅“代表性”案例的重复图。

本次重放核实角ETI含真值20/30、HDI24/30；负5与负10在三模式均不在68%角HDI。确定性包含计数不是频率覆盖。历史随机结果保留在原始后台，不进入当前报告主线或当前验收。

## 5. 全部文献：30二维声明模型 + 9前向控制

`analysis/cases/results_v0_1_1/results.json`含15个初始二维模型；`analysis/cases/followup/results_v0_1_1/results.json`含15个后续二维模型及9个纯项前向控制。按nominal记录计数；加密run不重复计案例，同一测量的不同几何/自旋假设不称独立实验。

- R02逐一呈现30个nominal二维模型的身份、观测误差、声明几何、完整四联图、三类统计和文献对照；六核数据依赖、读图误差、固定宽度及缺值保留。
- 9个前向控制单列纯跃迁、输入、响应与原文对照；无自由delta时不造二维PDF/混合比区间。
- 加密run附对应nominal案例，仅作收敛核对，与15+15二维及9前向分开计数。
- 主报告以30同核注入和nominal文献为主；独立核、旧0.1.0、历史随机覆盖/几何敏感性置方法依据或附录，不重复占主案例。

## 6. 大delta诊断与横页排版

R03解释正负5、10的恢复、分支质量、真值包含和端点依赖；优先读已有角边缘、加密/扩域证据。新增工作限必要的确定性诊断，不调整误差、角度、源态、核或区间坐标来逼近真值。

结合实际Jacobian、折叠/多解、有限sigma/xi域、观测误差和近纯E2饱和，区分数值收敛、可辨识性、确定性包含与历史覆盖。局部det非零不证明全局一一；区间偏离不能单独证明唯一根因。±pi/2是同一纯E2极限，有限delta区间不能称包含无穷。记录开放问题、证据缺口、停止原因和下一步。

只有三张宽主表所在页采用A4横向（最终第18、19、20页），每模式10例完整一页；正文、短表与全部四联图保持A4竖版。未整体缩小主表，实际8.5 pt；不得把旧软件阶段或skill默认横板解释成用户要求整份横向。图表、公式、脚注、页眉不遮挡/越界/截断；图表均有单位、观测/生成器/模型身份、误差及来源说明。

正文保留本轮需要的误差定义、组权重、纯E2校准与扫描域；既有比较研究和使用说明在后台保留；清理“30矩阵尚未执行”“仅sigma输入/输出”等冲突旧句。软件发布历史独立表述；历史225项测试和PyPI发布不代替本轮全页QA。

## 7. R00–R05任务与验收

| ID | 当前状态 | 依赖 | 消费、交付与验收 |
|---|---|---|---|
| R00 现场/数据核对 | completed | 无 | 核main/figures现场、sigma/Jacobian、冻结输入/哈希、30同核、15+15二维/9前向/加密计数；交缺项与复用路径，须主代理接收核对证据 |
| R01 30注入与长表 | completed | R00 | 读deterministic/angle_marginals的same_kernel30条；交全部输入/恢复长表、主图和分段检查，独立9j留后台 |
| R02 全部文献四联图 | completed | R00 | 交30nominal模型完整四联图/三类数值、9前向单表与索引；加密不重复计数 |
| R03 大delta诊断 | completed | R00、R01 | 用大delta边缘、Jacobian/分支、已有加密扩域证据，交机制对照、局限/开放问题；无新随机/卡方 |
| R04 报告编译全页QA | completed | R01、R02、R03 | 整理仅三张长表横向的main.tex，核图表数值，XeLaTeX至少两遍至引用稳定；渲染并目视每页，修溢出/遮挡/不可读，留实际页数与QA证据 |
| R05 知识归档收尾 | completed | R04 | 主代理核来源/图表清单与哈希、回写knowledge和必要handoff；验新旧状态分离/唯一main.pdf及定向归档，说明科学未决项；不发新软件版本，Git后续按用户授权整理发布 |

只有R00–R05逐项有实际证据且全部验收，报告任务才可completed。数据已存在、计划已改或旧U07已完成均不足以勾选本轮任务。当前goal_id关联现行账本，不重建/关闭其他goal。

### 7.0 后续Git基线整理（2026-11-24）

用户明确要求“归类下push，整理git基线”。维护源码仍在`raw/code/PDM/{GUI,analysis}/`，按精确白名单跟踪源码、测试、公开示例、说明与无输出Notebook；证据、结果、历史快照、dist及缓存留本地。两个旧版本从0.1.0源码包精确恢复，不回退0.1.1；三个集合共57项代码／文档引用改绑55份去重快照，保留全部历史预期哈希和三个原清单字节。报告仍为179项、816969691登记字节，PDF未变。迁移清单为`raw/code/PDM/archives/20261124-code-inputs/manifest.json`；Git检查与最终推送结果统一记录于`delivery/git-baseline-20261124.json`。历史`final-not-pushed`回执记录当时事实，不改写为已推送。

### 7.1 可直接复用的输入与脚本

路径相对`raw/code/PDM/`：

- `analysis/benchmarks/sigma03_relP80_relR10/`：`frozen-policy.json`、`frozen-job.json`、`deterministic.json/csv`、`angle_marginals.npz`、`grid_and_endpoint_sensitivity.json/csv`、`generator_agreement.json`、`provenance.json`、`run.log`、历史`repeated_coverage.json`。
- `analysis/scripts/benchmark_u04.py`是真实冻结矩阵；`run_benchmarks.py --suite synthetic`转入该模块。旧默认常数属于legacy分支，不能据此误判U04；本轮不执行重计算命令。
- `analysis/scripts/plot_benchmark_u04.py`读取保存摘要/曲线；报告端筛选same_kernel30条，不调用benchmark run触发重算。
- `analysis/cases/results_v0_1_1/`、`analysis/cases/followup/results_v0_1_1/`及对应`grouped_geometry_v0_1_1/`快照保存nominal/附属run、区间与文献表。
- `analysis/research/grid_resolution/frozen_inputs.json`、`results.json`、`heldout.json`、`threshold_audit.json`给实验P误差样本、网格/阈值/留出证据；E01与E03使用原集合。
- `GUI/src/multipolepdm/pdm/statistics.py`、`plotting/`及报告`figures/generate_figures.py`提供现有摘要/出图，当前只在报告端组合与排版。

U04运行生产/参考脚本哈希可逐项对provenance；理论手册起止哈希不同，不能将运行后main.tex反称冻结输入。历史清单错配需按实际定向哈希结果解释，不沿用过时“仍阻塞”或未检查的全仓通过表述。

## 8. 历史已完成工作

以下保留已完成事实；原始specification、evidence、commands_run、changed_paths、unresolved_items、worker与旧scope仍在`tasks.json`。历史字段里的“本轮/未来/发布授权”描述当时阶段，不覆盖第1节。

| ID | 状态 | 历史工作 | 证据指针 |
|---|---|---|---|
| E01 | 已完成（历史） | 不对称误差的处理方案 | `raw/code/PDM/analysis/research/asymmetric_errors/results.json`；`raw/code/PDM/analysis/research/asymmetric_errors/acceptance_aware_results.json`；`raw/code/PDM/analysis/research/asymmetric_errors/README.md` |
| E02 | 已完成（历史） | 网格与数值阈值有界寻优 | `raw/code/PDM/analysis/research/grid_resolution/results.json`；`raw/code/PDM/analysis/research/grid_resolution/heldout.json`；`raw/code/PDM/analysis/research/grid_resolution/threshold_audit.json` |
| E03 | 已完成（历史） | 多组权重与方位平均核验 | `raw/code/PDM/analysis/research/geometry/results.json`；`raw/code/PDM/analysis/research/geometry/weighted_groups.py` |
| U00 | 已完成（历史） | 冻结本轮输入和基线 | `tmp/pdm-upgrade-011/baseline-files.json`；`tmp/pdm-upgrade-011/baseline-tests.log`；`tmp/pdm-upgrade-011/frozen-policy.json` |
| U01 | 已完成（历史） | 角空间统计及tan报告 | `tmp/pdm-upgrade-011/statistics/stats-worker.md`；`tmp/pdm-upgrade-011/statistics/targeted-final.log` |
| U02 | 已完成（历史） | 四联图与完整响应域 | `tmp/pdm-upgrade-011/statistics/stats-worker.md`；`tmp/pdm-upgrade-011/statistics/targeted-final.log` |
| U03 | 已完成（历史） | GUI、输出与异步回归 | `tmp/pdm-upgrade-011/gui-final-repair-worker.md`；`tmp/pdm-upgrade-011/full-regression-release.log`；`tmp/pdm-upgrade-011/independent-review.md` |
| U04 | 已完成（历史） | 指定注入矩阵与缺失校准 | `tmp/pdm-upgrade-011/benchmark/benchmark-worker.md`；`raw/code/PDM/analysis/benchmarks/sigma03_relP80_relR10/provenance.json`；`tmp/pdm-upgrade-011/benchmark/final-symmetry-comparison.log` |
| U05 | 已完成（历史） | 图6与文献比较 | `tmp/pdm-upgrade-011/literature/literature-worker.md`；`raw/code/PDM/analysis/cases/results_v0_1_1/results.json`；`raw/code/PDM/analysis/cases/followup/results_v0_1_1/results.json` |
| U06 | 已完成（历史） | Notebook与使用教程 | `tmp/pdm-upgrade-011/docs/docs-worker.md`；`tmp/pdm-upgrade-011/docs/archive-replay.IvnGHW/kernel-imports.jsonl` |
| U07 | 已完成（历史） | 秘书报告与数据图表 | `tmp/pdm-upgrade-011/report-worker.md`；`raw/writing/pado/20261029_review_v1/PDM/figures/manifest.json` |
| U08 | 已完成（历史） | 整体回归与发布候选 | `delivery/0.1.1/acceptance.json` |
| U09 | 已完成（历史） | 发布、归档和逐项总验收 | `delivery/0.1.1/acceptance.json`；`delivery/0.1.1/source-verification.json`；`raw/code/PDM/analysis/validation_v0_1_1/publication/verification.json` |

0.1.0证据为`delivery/acceptance.json`和`delivery/0.1.0-task-ledger.json`；0.1.1整体验收、源码核对与公开发布分别为`delivery/0.1.1/acceptance.json`、`delivery/0.1.1/source-verification.json`、`raw/code/PDM/analysis/validation_v0_1_1/publication/verification.json`。不据此授权本轮重发或认证当前报告全页。

已有知识回链：`knowledge/sources/multipolepdm-20261120-v011-validation.md`、`knowledge/sources/pdm-20261120-error-geometry-grid-study.md`、`knowledge/research-notes/pdco-pdm-response-contract-20261118.md`。R05由主代理将新知识同步到相应页面，计划不成为第二知识库。

## 9. 本轮完成证据

- canonical `main.pdf`：90页，30注入+30文献声明模型的60张四联图；15条不同文献跃迁与9前向配置明确区分。三张主表仅第18、19、20页横向，8.5 pt；其余竖向。
- 实际60套快照独立积分/分位数/PDF矩/tan核对容差2e-12通过，77项回归通过，64图遮挡审计0 FAIL/0 WARN，90页全部目视，最终编译无溢出/缺字/未定义引用。
- 179文件集合与新source定向归档0失败，两页定向lint0问题，路径边界通过。全库原有130项结构错误另列；两份旧PDM清单有四项大小/哈希错配，未修改被登记原件或重写其历史身份，因此不推送。
- 详细回执：`delivery/report-revision-20261124.json`；精确Git提交身份仅保存本轮local回执。科学开放边界见知识页与报告正文，不作为本轮缺项或用户待审核事项。
