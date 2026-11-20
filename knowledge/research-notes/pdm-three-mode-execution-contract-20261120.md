---
type: research-note
title: "PDM 三模式重写：验证、交互分析与发布合同"
aliases: [PDM三模式执行合同]
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "用户批准三模式重写、并行代理与自动实施"
evidence_sources: [polarization-delta-collection-20261119-source, droste-1996-pdco-formalism, book-hamilton-electromagnetic-interaction, kramer-flecken-1989-use-dco-ratios, pypi-pdm-packaging-20261120]
tags: [pdm, validation, pdco, polarization, benchmark-design, python-packaging]
---

# PDM 三模式重写：验证、交互分析与发布合同

## Research Trigger

用户要求从零实现PDM核心及三个响应模块、友好GUI和Notebook；提供四联图、ETI/HDI、独立测试、真实核素案例和Python图文报告，并优先经PyPI发布。0.1.0已完成并发布；E01--E03研究及U00--U09正式改造均已完成；multipolePDM0.1.1已发布，公开安装与三模式GUI回读通过。执行验收与限制见 [[multipolepdm-20261120-v011-validation]]。旧完成goal不代表新任务完成。规格位于 `outputs/plans/20261120-pdm-three-mode-rewrite/plan.md`，任务状态仅由同目录 `tasks.json` 维护。

## Grounded Evidence

- [[droste-1996-pdco-formalism]] p.522 Eqs.20–21和Figs.4–5区分方向条件P与全方向积分P。
- [[kramer-flecken-1989-use-dco-ratios]] p.334的门控联合强度比定义DCO；R_ADO则是单线W在两个方向的比。中文分别采用“角分布比”和“DCO比（定向核的方向关联比）”，不能将二者混称。
- [[book-hamilton-electromagnetic-interaction]] p.552 Eqs.12.209–12.213定义未观测传播；p.553 Eq.12.218不等同所有U_k=1。
- [[polarization-delta-collection-20261119-source]] 是本地论文原件索引。用户Excel作为候选表，行排序/列位置不是记录身份；数值与条件定义仍回原件。
- `raw/writing/pado/Upload/analysis/YAnalysis.py` 的compute_eq_summary默认采用q16/q50/q84，中位数q50为中心；compute_hdi使用密度阈值，可有多个区间。新程序按用户最新指示统一命名ETI/HDI，不保留EQ为界面名。
- `raw/writing/pado/Upload/analysis/YPlot.py` 的plot_projection1d使用axvspan；本项目不沿用满高色带，改为HDI区间内0到PDF的填色。其对折叠观测网格不能直接pcolormesh的警告应保留。
- [[pypi-pdm-packaging-20261120]] 记录官方wheel、entry point、上传与Qt依赖资料。pdm名称已有其他项目；multipolePDM实施前查询404只作历史记录；0.1.0现已实际发布，见交付回执。

## Provisional Reasoning

GUI名称PDM，模式标识P_ADO/P_DCO/PDCO。新代码分为 `raw/code/PDM/analysis/` 与 `raw/code/PDM/GUI/`；前者推荐Notebook，后者承载公共核心和GUI；用户授权整个raw/code/PDM项目开源，包括analysis、输出读取示例、测试和可公开案例。三模式分别有response模块和config，公共物理、统计和绘图共享。用户删除的p_ado_v1.0不恢复、不成为依赖。

响应实现必须优先核验P-DCO。计划第2.4/2.5节已将秘书理论标签与代码模块绑定：eq:population/B定义唯一源布居，eq:trace/nonadjacent定义完整联合强度，eq:dco/joint-ratio定义DCO，eq:common-joint-p定义单线与条件P，eq:uk-pure/mixed负责未观测传播。标签已从当前PDM/main.tex实际核对，不靠可能变化的公式序号。手册工程章节按最新计划同步，不能恢复旧打包或旧接口要求。

每个(xi,sigma)只有一份rho0。按物理发射次序的T1/T2及未观测传播U构造联合强度；不测偏振时求和，测P时只对目标投影到平行/垂直电场轴。C0=Cparallel+Cperp，DCO=C0(target@a,gate@b)/C0(target@b,gate@a)；单线P对门方向先分别积强度再取差和比，条件P在指定门方向直接取差和比。门先发时单线目标态来自全方向传播，不能重新设为目标态Gaussian。条件路径中的传播必须保留必要相干项，不能普遍只传对角布居/B2/B4。U不是sigma换算器；未观测映射须线性保迹，不能丢掉未归一化门条件态的权重。球面平均归一的单线W与全空间概率归一的振幅核需显式对齐常数，且统计张量规范不能混用。

独立测试必须区分单线P的门角不变性、条件P的门角响应、上下游角色、门概率保留、相对方位角相干及零强度定义域。原始相位依据包括Droste1996和Starosta1999已发表勘误；不能以旧代码或同源闭环代替这些核验。

核心使用xi(rad)、sigma。xi的网格、三角函数、差分、输出及默认图轴均为rad；探测器角度另标deg，在几何入口转换。对外分析/图轴标为sigma/I，去掉ref和dimensionless；内部I_ref仍记录共同Gaussian参考态，不因目标位于下游而改变身份。对外角轴写arctan(delta)，刻度使用0、正负pi/8、pi/4、3pi/8，内部仍按rad计算。此显示改造属于当前待实施合同，不是0.1.0已有行为。

固定I_ref时，s=sigma/I_ref，f(xi,s)=I_ref*f(xi,I_ref*s)，p_s(s)=I_ref*p_sigma(I_ref*s)；delta边缘由p_delta=p_xi(arctan(delta))/(1+delta^2)转换。不得只换轴标签。当前用户选定的报告约定是在arctan(delta) PDF上计算68%HDI、ETI、mode和mean/std，再将每个HDI区间内PDF最高点的横坐标mode、分位数和各段端点逐项tan转换来报告delta；不要求先对delta PDF重算HDI。sigma/I直接评估。README注明这是物理混合角口径；HDI可能不连续，不能跨低密度间隙填色。Mean使用PDF加权积分，tan(angle mean)不标作直接delta期望；mean±std不赋予68%覆盖意义，越域或越tan奇点须显式标识。

结果统计和四联图从内存快照产生，不等待完整CSV导出。新显示目标：图1为所有有效响应点所在完整R_ADO/R_DCO-P观测域，按观测密度着色并叠加输入点和误差棒；图2为arctan(delta)-sigma/I密度；图3为arctan(delta)边缘，图4为sigma/I边缘。C/D各画橙色CDF16/50/84三线，合用图例68% ETI (16%, 50%, 84%)；灰色mean和mean±std三线默认常显，无开关；每个HDI分段各有自己的mode，不能复制整条PDF的唯一全局峰；HDI蓝色仍填0到PDF，另画y=h阈值水平线。图下显示delta和sigma/I的HDI/ETI/Mean-based三类数值，支持滚动、平移、缩放和单图/整图保存。计算完成和保存完成分别显示，写盘失败不抹掉可用预览。

四联图按nature-figure的Python数据图规范采用固定2x2 quantitative grid，a/b为观测与联合参数密度，c/d为两个边缘；共享样式模块统一字体、色图和区间标记。报告导出初始183x150mm，轴标题9pt、刻度/图例8pt，最终字形不少于5pt；GUI采用较大字号预设。用户指定viridis用于两个二维密度面板，a/b测度不同不能强制共用数值色标；HDI蓝色填PDF下方，ETI用橙色虚线，中心CDF50%不再另立Median图例。开发/报告出图做1.5pt面板对齐、字体及碰撞检查，普通用户不依赖技能脚本或TeX。这是本项目采用的Nature-style规范，不是宣称符合某刊全部投稿条款。

JSON示例随wheel提供，位于包资源examples目录：example.json为P_ADO，另有example_P_DCO.json、example_PDCO.json和example_batch.json及字段说明。GUI能载入/导出示例、保存已填输入；analysis/examples提供同格式的小型GUI合成输出，Notebook可以直接运行再换用户文件。示例不是实验数据，正式交付前须实际运行。

秘书手册现位于 `raw/writing/pado/20261029_review_v1/PDM/main.tex`，唯一PDF同目录。所有科学图由Python根据记录数据生成并保存至其figures目录，不使用AI图像代替结果。Notebook和GUI调用同一核心，不复制互相漂移的算法。

实测选样排除74Br及用户指定SHU74；SHU74在当前References中未找到精确键，需按原件身份核定别名，不猜测归属。已完成的模型比较为80Se/164Yb、135Pr/185Au、154Tb/190Tl六核；PDCO仅164Yb，均不是完整阵列重放。当前图6改造保留冻结名单和全部几何边界，不重新按结果选样。候选展示只用核素+能量，内部保留必要来源与分支。读取按表头名称，不按固定行号/列号，排序不改变选择。

验证分独立物理参考、注入恢复/正负控制、实测与敏感性三层。P不要求随delta整体反号；同源生成反演不能作为独立验证。文献delta不进入反演输入，名单在看结果前冻结；不能用模拟凑实测配额。不加入chi-square拟合模块。

发布采用multipolePDM、导入multipolepdm、入口pdm-gui，一套纯Python wheel与sdist，依赖由pip处理。PyPI不是无Python解压免安装；平台有实际环境就做轻量安装/GUI检查，无环境如实标未测，不建立四个原生包工程。用户允许使用全局Python环境，不创建任务虚拟环境。pyproject.toml作为唯一依赖声明，pip安装普通依赖，analysis/dev为可选extra；若提供requirements则从同源定义生成。Agent自行处理普通下载、安装、调试，仅账号/API key/远端授权等本人必需操作请求用户协助。

当前环境是无桌面Docker，已发现Xvfb、xvfb-run、xauth。GUI默认用Qt offscreen和pytest-qt/QTest做真实控件/事件测试，必要时用Xvfb检查实际Qt布局、截图和保存；无需用户挂接桌面，不建立远程桌面工程。每模式须做小规模真实计算链，mock仅用于故障注入。全局环境已安装PySide6/pytest，三模式真实offscreen计算与逐图导出已有测试；原生Windows/macOS体验不因Docker测试而变成已验证。

用户允许对未尽细节自主研究：先由本库定位原件，再按需合法获取外部原文并归档；记录问题、locator、条件、采用方式和核验。不得借自主研究静默改变已确定的共同参考态、P-DCO单线P或DCO条件定义；证据冲突需显式说明并处理，不为凑可运行结果猜缺失参数。

## Detector Groups and Grid Controls

用户确认不筛phi的实验按环合并模型处理；它意味着先做方位强度平均，不是phi=0，也不是4pi。154Tb/190Tl未来主模型采用此约定。GUI默认不勾选方位选择，phi列灰化；勾选时可填degree单位(theta,phi)。各ADO/DCO组及偏振目标/门均可多行，带相对有效权重；不重新处理实验效率。默认明确组内加权平均，原始加权和作为另一个显式选项，不能暗中改变归一化。135Pr输入2:1组权重即可重现用户公式；P真实角75.5deg不随合成测试P90deg而改变。

网格GUI提供每坐标min/max/step和单位。角步长可用deg输入并仅换算一次为rad；sigma/I步长0.005在内部是I*0.005，不是sigma步长0.005。图仍显示arctan(delta)的pi分数刻度。研究推荐值只是有界样本下的稳定工作点，用户可改范围/步长，完整坐标/实际末段长度进入输出。

## Assumptions

- 旧0.1.0实施授权已经执行完毕；本轮E01--E03隔离研究已完成，U00--U09正式程序改造已获用户授权；新发布仍须完整验收。
- 上游共同Gaussian和已给路径参数保持二维反演；不能因都叫sigma就忽略参考态身份。
- 全域图不能静默裁去有效响应点；渲染优化不改变原网格统计和完整覆盖，概率测度必须保留。
- PyPI token仅在实际发布进程中读取与传入，不写文档/源码/日志；0.1.0已通过真实PyPI上传与公开元数据哈希回读；没有记录token值。

独立响应与合成反演的归档数据见 [[multipolepdm-20261120-synthetic-validation]]；其中600次反演只对应三个工况各100个独立噪声向量经两种生成器成对处理，不能计作600个独立实验。

## Current Planned Validation and Reporting

下列U00--U09是整体实现合同；本轮已授权并完成的E01--E03研究另有原始数据，不用其完成状态替代GUI接入。完整规格在原plan和tasks。

- 注入主矩阵：三模式乘delta=-10,-5,-1,-0.5,-0.1,+0.1,+0.5,+1,+5,+10；用户的sigma_yy=0.3按上下文理解为sigma/I=0.3，源sigma=0.3*I，反演仍扫描宽度。
- 误差策略已按用户更新：80%/10%不作固定教条；本轮研究从10条已核主层P误差取得绝对下限0.1075，取max(0.1075,0.8abs(P0))并以R10%为基线。主矩阵在研究后冻结策略，不借旧配置结果冒充已测。30条独立9j生成主记录、30条同核自洽对照；另外三个代表工况各100独立噪声向量、两生成器成对处理，保留依赖关系。
- 真值/恢复图和详细表必须同时交付：列注入delta、sigma/I、自旋/门/几何、P/R及误差、每个HDI区间的mode与边界、ETI三分位数、mean/std、真值包含、偏差、分支和边界警告。只画PDF而不标真值或只说测试通过不合格。
- 公式(6)的2->0纯E2、m=0、W(45deg)=15/8、P(45deg)=+1需直接断言；可混合模型的纯E2端点恢复与选择定则禁止M1的纯项前向控制分开。两者当前不以旧纯项对照统称完成。
- 图6四面板：A为delta对谱线，B为sigma/I对谱线，C为delta对目标初态自旋，D为sigma/I对目标初态自旋。A/C用tan转换后的delta，不用角坐标。四图都有HDI68%、ETI68%和文献点图例；C/D以小横向offset避免同自旋估计重叠，自旋数据本身不改。文献固定采用宽度与提取值分开。
- 默认主报告/GUI只展示68%ETI/HDI；历史95%数据不删除、不混入新默认展示。原文未声明误差置信水平时不补写68%。
- 用户已确认图题为Full Range Marginalization; Constant Weight。数值含义是完整扫描域、常数附加权重，绝不是固定sigma。
- analysis是Notebook/脚本目录，不是第二个必装包；pip安装共享核心一次，[analysis]只补Jupyter等可选依赖，不自动下载Notebook。教程应写清下载Notebook、打开示例、换输出路径及三评估的读法。

## Geometry and Numerical-Setting Audit

已有只读核查之后，本轮又完成实际隔离研究；新原始数据与结果见 [[pdm-20261120-error-geometry-grid-study]]。这些研究使用0.1.0基线；正式改造已启动，新增功能的验收须另看当前账本。来源定位：`raw/code/PDM/analysis/benchmarks/synthetic_benchmarks.json` 的settings/convergence；`analysis/cases/point_angle_ado_jobs.json`、`point_angle_dco_scenarios.json`及followup各job；`GUI/src/multipolepdm/pdm/observations.py`、mapping.py、statistics.py、models/registry.py、contracts.py。

- 已完成旧合成矩阵是目标3->2、E2门2->0，比值90/38deg，P81deg，DCO方位18deg；PDCO偏振门47deg、目标/门方位13/61deg。新主矩阵采用5->4->2、125/90deg、P90deg和phi强度平均；本轮已跑9个寻优与6个留出工况，正式30工况尚未全部执行，不能混用描述。
- 0.1.0的135Pr145.6/90deg只是代表角近似。用户提供的原程序实际为[2W157.6+W133.6]/[3W75.5]，P角75.5deg；本轮54点振幅核对照已复算到约1e-14，不能用平均角替代。185Au保留两个顺序假设，164Yb是理想环模型。所有几何假设都不能通过调成更接近文献或注入值来“优化”。详细来源与边界见 [[multipolepdm-20261120-empirical-validation]]。
- 新程序没有偏态正态拟合接受门；对称输入为Gaussian，不对称输入为左右尺度正态变换、中心两侧各1/2概率，中心一般有密度跳跃。旧Upload/p_ado/pdf/fitters.py才有skew-normal量化匹配及接受/回退。模型选择与数值收敛是不同问题，不能宣称旧阈值已经在新程序优化。
- Jacobian1e-12只作警告，不裁小正值；Gaussian布居没有用1e-12作硬截断。64倍机器epsilon用于无可分辨sigma变化的拒绝；models/registry.py另有1e-12物理范围舍入容差。三者用途不可混同。
- 已有3121x201到6241x401的36项delta区间检查通过，最大角中位数移动3.34944e-5rad、端点1.39665e-4rad，属于所选工况而非全局最优证明。本轮又实测9种网格、9个初始工况及6个留出工况，推荐候选0.1deg/.005通过，.1deg/.01初始仅6/9；J警告阈值不改PDF，机器epsilon阈值只影响近退化控制。不能以吻合真值挑参数，三个初始delta=-10工况的68%HDI仍不含真值。

## Implemented Response Evidence

生产核在 `raw/code/PDM/GUI/src/multipolepdm/physics/`，独立参考在 `raw/code/PDM/GUI/tests/reference/`，两者分别使用显式光子振幅矩阵和广义9j统计张量。详尽推导及原文locator保存在公开代码的 `GUI/docs/response-reference.md` 与秘书手册 `raw/writing/pado/20261029_review_v1/PDM/main.tex`，不依赖任务输出目录保存科学结论。

- 输入混合比采用KS/Droste辐射振幅约定；当前CG/D-star基底需要逐多极乘 `(-1)^L`，M1/E2的相对符号不能靠纯分量检查确认。Starosta1999 p.17 footnote1将D96 Eq4的磁项作用于带撇项，是独立于基底桥的勘误。依据为 [[droste-1996-pdco-formalism]] pp.519–520 Eqs3–8、[[starosta-1999-pdco-experimental-test]]、[[krane-steffen-1970-cd110-mixing-ratios]] p.727 Eqs4–5/9。
- 本任务独立参考24测试和生产桥接7测试实际通过；覆盖两个偏振原始通道、两种发射次序、半整数及非相邻路径/非零方位差。属于独立代数组装，不是独立实验或原作者软件重放。
- D96 Fig7的5->4->2、sigma1.5、xi=-70deg点模型给P_single=.273255、POL-DIR=.437181、DIR-POL=.173583、R_DCO=.362034。程序xi存储仍为rad；上述数值是计算，不是图读实验点。Kramer-FleckenTable1四个所选非伸展条目与点模型仍有残差，未隐去，也不将其归因于实验错误。
- 初步数值审查发现：极稀疏tan(xi)网格的点值密度不能直接当成质量守恒直方图。因此完整CSV另存原生积分权重/节点概率，delta边缘用自适应细化的独立坐标；异步结果数组置只读，避免图形消费者改变正在导出的快照。后续网格及边界敏感性依然必要。

文献六核实测比较与测量定义见 [[multipolepdm-20261120-empirical-validation]]。其中PDCO只覆盖164Yb一个核，六核不等于六次完整阵列重放。

当前模型还显式保留解析对称性：相同或互补极角给常量比值1，轴上单线P为0，但轴上条件P遇轴外门不能据此置0。相邻共线两光子且源/末态自旋和小于2时，未分析门螺旋度使目标线偏振为0；中间出现未观测光子时此选择规则不再成立。由已定义振幅与旋转/螺旋度选择规则推得，属于本任务实现控制；不把浮点舍入产生的非零Jacobian当可用二维信息。

## Failure Conditions

以旧0.1.0完成状态勾选本轮新任务、对delta重新求HDI代替用户指定角空间口径、只画实验附近遗漏有效响应点、灰色mean引导线需要开关才能出现、CDF50%另设Median图例、图上没有三评估数值、把负P生成负误差幅度、用旧误差的注入结果冒充新矩阵、用EQ作为新界面名、xi混用deg/rad、仅换sigma/I轴而不换密度、HDI铺满纵轴或跨空隙、必须等大文件写完才显示结果、把IPDCO名称当模式证明、把74Br重新算进覆盖、固定Excel行/列定位、发布凭据或未授权第三方原件，均不符合当前合同。

## Competing Explanations

文献与PDM不符可能来自观测定义、相位、参考态、误差、范围/权重或代码缺陷，不预先归因于文献错误。PyPI通用wheel只减少本项目原生打包工作，不证明Qt及科学依赖在任意系统可用。

## Transfer Conditions

三模式共享计算核，但保留各自测量条件；Notebook、GUI和报告共享统计/绘图。整个raw/code/PDM的自有代码、Notebook、示例、测试及可公开数据可以一起发布；Git仓库根选PDM而非只选GUI。PyPI发布可安装包并附JSON示例，Git提供完整analysis；不把整个Wiki、API key或无再分发许可的出版社原件打包进去。

## Falsification or Reverse Tests

执行阶段验证独立角关联系数核对振幅核、纯分量、全方向积分、U传播、解析二维映射、坐标概率守恒、ETI/多峰HDI和图下填色积分。加入Excel排序/列移动一致性、慢盘提前预览、单图矢量保存、Notebook运行全部及真实PyPI安装回读。0.1.0基线的153项回归通过；该版本wheel安装、offscreen/Xvfb真实GUI、三个Notebook均运行。独立与同核合成重复观测、六核文献模型比较及PyPI制品回读分别留有记录，不混计证据。

## Open Questions

本轮不对称误差/几何/网格研究已完成，整体GUI接入仍待实施；标题Weight与逐HDI区间mode固定。方向条件PDCO只有164Yb一个实测核，第二核配对测量仍缺；190Tl补足第二奇奇核，但其单线P代理、方位几何和低能校准外推边界保留。SHU74别名未确定。Docker虚拟显示为当前GUI基线，Windows/macOS原生未测；未指定独立软件Git远端，因此交付完整源码包而不推送整个Wiki作为软件。

## Human Review

用户曾批准0.1.0自动实施并授权代理协作；当前已明确授权E01--E03研究与报告及U00--U09正式改造；不能沿用0.1.0的完成状态认定新增GUI功能已完成。执行授权不是人工逐条核验科学结论。multipolePDM 0.1.0已发布到PyPI；这是软件交付，不代表用户逐条审核科学结论。

## Promotion or Rejection History

2026-11-20：保留当前完整执行合同。计划状态由tasks.json追踪，本页不追加对话式修改流水，也不把候选盘点当已完成研究。

## 正式实现的观测误差策略

依据 [[pdm-20261120-error-geometry-grid-study]] 的E01对照，正式实现保留显式的中位数分侧高斯变换：输入中心是中位数、左右误差端点按正态Phi(-1)/Phi(1)解释，各侧质量1/2，对称时还原Gaussian，不对称时中心密度跳跃如实说明。输出ETI/HDI仍使用精确68%，不把输入一标准差的68.2689%混同输出68%。不自动拟合skew-normal再静默回退成中心为众数的split-normal；若实验误差另有似然或分位定义，需声明模型再作敏感性比较。研究中平滑替代族未获得真值层面的优越性证据，不能仅因曲线光滑而更换默认误差语义。这是有条件的建模约定，不是对原实验误差条含义的重新认证。

## 正式实现的验证证据

[[multipolepdm-20261120-v011-validation]] 保存0.1.1分组响应、角空间逐段HDI、正负及大混合比注入、纯E2解析检查和39项文献声明模型的实际结果。60条确定性记录与600次重复反演已执行；两个生成器共用300个独立噪声对，不能计为600个独立实验。大混合比PDCO的低包含率保留为明确方法边界，不因前向一致、单位测试或网格收敛而消失。程序交互修复、制品安装及发布已分别验收：225项完整回归通过，独立审查发现的问题关闭，公开包与源码哈希一致。Windows/macOS原生GUI仍未测，不把科学数值运行完毕等同于所有平台行为正确。
