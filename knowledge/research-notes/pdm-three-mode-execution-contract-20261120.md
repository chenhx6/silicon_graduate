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

用户要求从零实现PDM核心及三个响应模块、友好GUI和Notebook；提供四联图、ETI/HDI、独立测试、真实核素案例和Python图文报告，并优先经PyPI发布。用户已明确批准执行，实施goal已启动。规格位于 `outputs/plans/20261120-pdm-three-mode-rewrite/plan.md`，任务状态仅由同目录 `tasks.json` 维护。

## Grounded Evidence

- [[droste-1996-pdco-formalism]] p.522 Eqs.20–21和Figs.4–5区分方向条件P与全方向积分P。
- [[kramer-flecken-1989-use-dco-ratios]] p.334的门控联合强度比定义DCO；R_ADO则是单线W在两个方向的比。中文分别采用“角分布比”和“DCO比（定向核的方向关联比）”，不能将二者混称。
- [[book-hamilton-electromagnetic-interaction]] p.552 Eqs.12.209–12.213定义未观测传播；p.553 Eq.12.218不等同所有U_k=1。
- [[polarization-delta-collection-20261119-source]] 是本地论文原件索引。用户Excel作为候选表，行排序/列位置不是记录身份；数值与条件定义仍回原件。
- `raw/writing/pado/Upload/analysis/YAnalysis.py` 的compute_eq_summary默认采用q16/q50/q84，中位数q50为中心；compute_hdi使用密度阈值，可有多个区间。新程序按用户最新指示统一命名ETI/HDI，不保留EQ为界面名。
- `raw/writing/pado/Upload/analysis/YPlot.py` 的plot_projection1d使用axvspan；本项目不沿用满高色带，改为HDI区间内0到PDF的填色。其对折叠观测网格不能直接pcolormesh的警告应保留。
- [[pypi-pdm-packaging-20261120]] 记录官方wheel、entry point、上传与Qt依赖资料。pdm名称已有其他项目；multipolePDM本次查询404，不代表预留成功。

## Provisional Reasoning

GUI名称PDM，模式标识P_ADO/P_DCO/PDCO。新代码分为 `raw/code/PDM/analysis/` 与 `raw/code/PDM/GUI/`；前者推荐Notebook，后者承载公共核心和GUI；用户授权整个raw/code/PDM项目开源，包括analysis、输出读取示例、测试和可公开案例。三模式分别有response模块和config，公共物理、统计和绘图共享。用户删除的p_ado_v1.0不恢复、不成为依赖。

响应实现必须优先核验P-DCO。计划第2.4/2.5节已将秘书理论标签与代码模块绑定：eq:population/B定义唯一源布居，eq:trace/nonadjacent定义完整联合强度，eq:dco/joint-ratio定义DCO，eq:common-joint-p定义单线与条件P，eq:uk-pure/mixed负责未观测传播。标签已从当前PDM/main.tex实际核对，不靠可能变化的公式序号。手册工程章节按最新计划同步，不能恢复旧打包或旧接口要求。

每个(xi,sigma)只有一份rho0。按物理发射次序的T1/T2及未观测传播U构造联合强度；不测偏振时求和，测P时只对目标投影到平行/垂直电场轴。C0=Cparallel+Cperp，DCO=C0(target@a,gate@b)/C0(target@b,gate@a)；单线P对门方向先分别积强度再取差和比，条件P在指定门方向直接取差和比。门先发时单线目标态来自全方向传播，不能重新设为目标态Gaussian。条件路径中的传播必须保留必要相干项，不能普遍只传对角布居/B2/B4。U不是sigma换算器；未观测映射须线性保迹，不能丢掉未归一化门条件态的权重。球面平均归一的单线W与全空间概率归一的振幅核需显式对齐常数，且统计张量规范不能混用。

独立测试必须区分单线P的门角不变性、条件P的门角响应、上下游角色、门概率保留、相对方位角相干及零强度定义域。原始相位依据包括Droste1996和Starosta1999已发表勘误；不能以旧代码或同源闭环代替这些核验。

核心使用xi(rad)、sigma。xi的网格、三角函数、差分、输出及默认图轴均为rad；探测器角度另标deg，在几何入口转换。分析、参数图和取向统计显示sigma/I_ref，I_ref为共同Gaussian参考态，不因目标位于下游而改变身份。

固定I_ref时，s=sigma/I_ref，f(xi,s)=I_ref*f(xi,I_ref*s)，p_s(s)=I_ref*p_sigma(I_ref*s)；delta边缘由p_delta=p_xi(arctan(delta))/(1+delta^2)转换。不得只换轴标签。ETI和HDI均在各自最终变量密度上计算；HDI可能不连续，不能跨低密度间隙填色。

结果统计和四联图从内存快照产生，不等待完整CSV导出。图1为R_ADO/R_DCO对P的观测密度，图2为xi(rad)对sigma/I的参数密度，图3为delta边缘，图4为sigma/I边缘。下方显示两变量的ETI/HDI，允许滚动、平移、缩放及单图/整图保存。计算完成和保存完成分别显示，写盘失败不抹掉可用预览。

四联图按nature-figure的Python数据图规范采用固定2x2 quantitative grid，a/b为观测与联合参数密度，c/d为两个边缘；共享样式模块统一字体、色图和区间标记。报告导出初始183x150mm，轴标题9pt、刻度/图例8pt，最终字形不少于5pt；GUI采用较大字号预设。cividis等顺序色图用于密度，a/b测度不同不能强制共用数值色标；HDI蓝色填PDF下方，ETI用橙红虚线。开发/报告出图做1.5pt面板对齐、字体及碰撞检查，普通用户不依赖技能脚本或TeX。这是本项目采用的Nature-style规范，不是宣称符合某刊全部投稿条款。

JSON示例随wheel提供，位于包资源examples目录：example.json为P_ADO，另有example_P_DCO.json、example_PDCO.json和example_batch.json及字段说明。GUI能载入/导出示例、保存已填输入；analysis/examples提供同格式的小型GUI合成输出，Notebook可以直接运行再换用户文件。示例不是实验数据，正式交付前须实际运行。

秘书手册现位于 `raw/writing/pado/20261029_review_v1/PDM/main.tex`，唯一PDF同目录。所有科学图由Python根据记录数据生成并保存至其figures目录，不使用AI图像代替结果。Notebook和GUI调用同一核心，不复制互相漂移的算法。

实测选样排除74Br及用户指定SHU74；SHU74在当前References中未找到精确键，需按原件身份核定别名，不猜测归属。36Cl的790/1170keV为替换奇奇核的待核线索，但表中主要给P与角系数，尚未证明适用和输入完整。候选展示只用核素+能量，内部保留必要来源与分支。读取按表头名称，不按固定行号/列号，排序不改变选择。

验证分独立物理参考、注入恢复/正负控制、实测与敏感性三层。P不要求随delta整体反号；同源生成反演不能作为独立验证。文献delta不进入反演输入，名单在看结果前冻结；不能用模拟凑实测配额。不加入chi-square拟合模块。

发布采用multipolePDM、导入multipolepdm、入口pdm-gui，一套纯Python wheel与sdist，依赖由pip处理。PyPI不是无Python解压免安装；平台有实际环境就做轻量安装/GUI检查，无环境如实标未测，不建立四个原生包工程。用户允许使用全局Python环境，不创建任务虚拟环境。pyproject.toml作为唯一依赖声明，pip安装普通依赖，analysis/dev为可选extra；若提供requirements则从同源定义生成。Agent自行处理普通下载、安装、调试，仅账号/API key/远端授权等本人必需操作请求用户协助。

当前环境是无桌面Docker，已发现Xvfb、xvfb-run、xauth。GUI默认用Qt offscreen和pytest-qt/QTest做真实控件/事件测试，必要时用Xvfb检查实际Qt布局、截图和保存；无需用户挂接桌面，不建立远程桌面工程。每模式须做小规模真实计算链，mock仅用于故障注入。全局环境已安装PySide6/pytest，三模式真实offscreen计算与逐图导出已有测试；原生Windows/macOS体验不因Docker测试而变成已验证。

用户允许对未尽细节自主研究：先由本库定位原件，再按需合法获取外部原文并归档；记录问题、locator、条件、采用方式和核验。不得借自主研究静默改变已确定的共同参考态、P-DCO单线P或DCO条件定义；证据冲突需显式说明并处理，不为凑可运行结果猜缺失参数。

## Assumptions

- 实施已获批准；软件发布仍以完整科学与制品验收为条件，不提前上传占位版本。
- 上游共同Gaussian和已给路径参数保持二维反演；不能因都叫sigma就忽略参考态身份。
- 图的显示降采样不得改变基于完整网格计算的统计；概率测度必须保留。
- PyPI token仅在实际发布进程中读取与传入，不写文档/源码/日志；0.1.0已通过真实PyPI上传与公开元数据哈希回读；没有记录token值。

独立响应与合成反演的归档数据见 [[multipolepdm-20261120-synthetic-validation]]；其中600次反演只对应三个工况各100个独立噪声向量经两种生成器成对处理，不能计作600个独立实验。

## Implemented Response Evidence

生产核在 `raw/code/PDM/GUI/src/multipolepdm/physics/`，独立参考在 `raw/code/PDM/GUI/tests/reference/`，两者分别使用显式光子振幅矩阵和广义9j统计张量。详尽推导及原文locator保存在公开代码的 `GUI/docs/response-reference.md` 与秘书手册 `raw/writing/pado/20261029_review_v1/PDM/main.tex`，不依赖任务输出目录保存科学结论。

- 输入混合比采用KS/Droste辐射振幅约定；当前CG/D-star基底需要逐多极乘 `(-1)^L`，M1/E2的相对符号不能靠纯分量检查确认。Starosta1999 p.17 footnote1将D96 Eq4的磁项作用于带撇项，是独立于基底桥的勘误。依据为 [[droste-1996-pdco-formalism]] pp.519–520 Eqs3–8、[[starosta-1999-pdco-experimental-test]]、[[krane-steffen-1970-cd110-mixing-ratios]] p.727 Eqs4–5/9。
- 本任务独立参考24测试和生产桥接7测试实际通过；覆盖两个偏振原始通道、两种发射次序、半整数及非相邻路径/非零方位差。属于独立代数组装，不是独立实验或原作者软件重放。
- D96 Fig7的5->4->2、sigma1.5、xi=-70deg点模型给P_single=.273255、POL-DIR=.437181、DIR-POL=.173583、R_DCO=.362034。程序xi存储仍为rad；上述数值是计算，不是图读实验点。Kramer-FleckenTable1四个所选非伸展条目与点模型仍有残差，未隐去，也不将其归因于实验错误。
- 初步数值审查发现：极稀疏tan(xi)网格的点值密度不能直接当成质量守恒直方图。因此完整CSV另存原生积分权重/节点概率，delta边缘用自适应细化的独立坐标；异步结果数组置只读，避免图形消费者改变正在导出的快照。后续网格及边界敏感性依然必要。

文献六核实测比较与测量定义见 [[multipolepdm-20261120-empirical-validation]]。其中PDCO只覆盖164Yb一个核，六核不等于六次完整阵列重放。

当前模型还显式保留解析对称性：相同或互补极角给常量比值1，轴上单线P为0，但轴上条件P遇轴外门不能据此置0。相邻共线两光子且源/末态自旋和小于2时，未分析门螺旋度使目标线偏振为0；中间出现未观测光子时此选择规则不再成立。由已定义振幅与旋转/螺旋度选择规则推得，属于本任务实现控制；不把浮点舍入产生的非零Jacobian当可用二维信息。

## Failure Conditions

用EQ作为新界面名、xi混用deg/rad、仅换sigma/I轴而不换密度、HDI铺满纵轴或跨空隙、必须等大文件写完才显示结果、把IPDCO名称当模式证明、把74Br重新算进覆盖、固定Excel行/列定位、发布凭据或未授权第三方原件，均不符合当前合同。

## Competing Explanations

文献与PDM不符可能来自观测定义、相位、参考态、误差、范围/权重或代码缺陷，不预先归因于文献错误。PyPI通用wheel只减少本项目原生打包工作，不证明Qt及科学依赖在任意系统可用。

## Transfer Conditions

三模式共享计算核，但保留各自测量条件；Notebook、GUI和报告共享统计/绘图。整个raw/code/PDM的自有代码、Notebook、示例、测试及可公开数据可以一起发布；Git仓库根选PDM而非只选GUI。PyPI发布可安装包并附JSON示例，Git提供完整analysis；不把整个Wiki、API key或无再分发许可的出版社原件打包进去。

## Falsification or Reverse Tests

执行阶段验证独立角关联系数核对振幅核、纯分量、全方向积分、U传播、解析二维映射、坐标概率守恒、ETI/多峰HDI和图下填色积分。加入Excel排序/列移动一致性、慢盘提前预览、单图矢量保存、Notebook运行全部及真实PyPI安装回读。当前153项回归通过；当前wheel安装、offscreen/Xvfb真实GUI、三个Notebook均运行。独立与同核合成重复观测、六核文献模型比较及PyPI制品回读分别留有记录，不混计证据。

## Open Questions

方向条件PDCO只有164Yb一个实测核，第二核配对测量仍缺；190Tl补足第二奇奇核，但其单线P代理、方位几何和低能校准外推边界保留。SHU74别名未确定。Docker虚拟显示为当前GUI基线，Windows/macOS原生未测；未指定独立软件Git远端，因此交付完整源码包而不推送整个Wiki作为软件。

## Human Review

用户明确指令开始自动实施并授权代理协作；这是执行授权，不是人工逐条核验科学结论。multipolePDM 0.1.0已发布到PyPI；这是软件交付，不代表用户逐条审核科学结论。

## Promotion or Rejection History

2026-11-20：保留当前完整执行合同。计划状态由tasks.json追踪，本页不追加对话式修改流水，也不把候选盘点当已完成研究。
