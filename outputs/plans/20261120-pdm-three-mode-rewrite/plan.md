---
title: "PDM：三模式物理核心、交互分析与 PyPI 发布执行计划"
date: "2026-11-20"
status: in_progress
implementation_authorized: true
goal_created: true
---

# PDM 执行计划与验收合同

**状态：用户已批准执行，实施 goal 已启动；发布仍须满足本合同的验收门。**

Agent 按批准的合同自主实现、测试、修复和维护报告。本目录 `plan.pdf` 是供用户阅读的计划；`plan.md` 是规格正文；`tasks.json` 是唯一任务状态账本。用户无需维护机器账本。三者直接保持一致，不追加逐轮修改说明。

## 1. 目标与交付物

本项目以 **PDM 密度映射核心**为中心，接入 `P_ADO`、`P_DCO`、`PDCO` 三个响应模块，提供简单 GUI、计算后即时四联图与区间统计、Notebook 分析和可复现科研报告。发布优先使用一套 PyPI Python 包，不把制作多个原生安装包作为本轮主任务。

| 对象 | 固定名称或路径 |
|---|---|
| GUI 窗口标题 | **PDM** |
| PyPI 发布包名 | `multipolePDM`（规范化项目键 `multipolepdm`），发布前再次检查名称可用性 |
| Python 导入名 | `multipolepdm` |
| 启动入口 | `pdm-gui`；备用 `python -m multipolepdm` |
| 内部模式标识 | `P_ADO`、`P_DCO`、`PDCO` |
| 代码根目录 | `raw/code/PDM/` |
| 推荐数据分析 | `raw/code/PDM/analysis/`，优先 Notebook |
| 整体开源项目 | `raw/code/PDM/`，包括 analysis、GUI、示例、测试与文档 |
| Python 包构建目录 | `raw/code/PDM/GUI/`，公共核心及 GUI |
| 秘书/可读科研报告 | `raw/writing/pado/20261029_review_v1/PDM/main.tex` 与唯一 `main.pdf` |
| 科学图及生成脚本 | `raw/writing/pado/20261029_review_v1/PDM/figures/` |

两个代码目录承载当前实现；实际完成状态与证据由任务账本记录。被用户删除的 `raw/writing/pado/Upload/p_ado_v1.0/` 不恢复、不作为构建依赖。剩余 `Upload/analysis/YAnalysis.py` 和 `YPlot.py` 只作方法与展示参考，不保留旧文件格式兼容层。

### 面向使用者的最短路径

1. 已有受支持 Python 的用户运行一次 `python -m pip install multipolePDM`。
2. 运行 `pdm-gui` 打开 PDM；提供示例、一键计算、结果目录入口以及可选桌面启动入口。
3. 不懂编程的使用者只需选模式、填实验量、点击计算；网格、缓存、归一化等有默认设置，高级参数折叠显示。

**PyPI 安装不等于无 Python 的解压免安装。** 本轮采用一次 pip 安装的简化交付路线；不再强制生成四个原生发行档。自己的包可以是纯 Python，但 Qt、NumPy、SciPy 等依赖由 pip 安装其兼容版本/平台 wheel；不承诺所有历史系统均可用。

## 2. 物理合同：三模式共用一个 PDM 核心

### 2.1 参数与参考态

- 主模型支持同宇称 M1/E2 及其纯分量。公式允许时支持 Delta I=0、1；Delta I=2 的禁 M1 情形走纯 E2 响应，不伪造自由混合比的二维 PDF。
- 核心参数为 `xi = arctan(delta)` 和 `sigma`。Gaussian 磁子态布居不改。
- `P_ADO` 的 Gaussian 放在目标发射态；`P_DCO`/`PDCO` 放在输入路径中先发观测光子发射前的参考态。
- 初始默认范围：正整数参考自旋 `sigma_min=0.15`，半整数 `0.20`，`sigma_max=I_ref`。这些是可测试优化的数值工作设置，不是物理先验真值。优化必须保存依据，不为了匹配文献值调参。
- 下游布居按给定跃迁传播，不重新拟合第二个 sigma。输出标明 `I_ref`；展示的 `sigma/I` 中 I 始终是这个参考态自旋，不能暗换成目标态。
- 不作方向选择的跃迁用精确 U_k 或等价传播；指定方向门保留完整关联，不默认所有 U_k=1。
- 门及中间跃迁的必要参数作为已给模型配置，不增加未知扫描轴。

### 2.2 三个模块

| 标识 | 理论观测量 | GUI 选择框下的英文短注释 |
|---|---|---|
| `P_ADO` | 单线 P + 单线角分布比 R_ADO | Single-line polarization + angular-distribution ratio. |
| `P_DCO` | 无方向门条件的单线 P + DCO | Single-line polarization + directional-correlation ratio. |
| `PDCO` | 保留指定门方向的条件 P + DCO | Direction-gated polarization + directional-correlation ratio. |

只测目标线自身的 P。单线 P 从同一联合强度对伴随方向求和后取偏振比；条件 P 在指定门方向取比；DCO 使用两种交换方向的联合符合强度比。实现可用解析传播代替逐网格球面积分，但必须证明与共同定义一致。

程序接收最终 P、R_ADO/R_DCO 及左右误差，不负责原始计数、效率、污染或实验门线真伪。检查数值格式、允许多极性和必需几何即可。NRF 入射束偏振、低温取向等不同源模型不能直接套入本合同。

观测误差按声明的分位数含义建模：对称误差使用Gaussian，非对称误差采用可核验分位数的模型并记录选择与归一化。只有左右误差而没有协方差时，明确沿用独立误差近似；不能从“无方向门”推断统计独立，也不新增相关系数拟合。

**本轮不加入 chi-square 拟合模块。** 三模式只是 PDM 的响应入口，不发展成三套互相分离的推断程序。

### 2.3 术语与不确定度来源

| 符号 | 英文 | 本项目中文名称 |
|---|---|---|
| R_ADO | Angular-distribution ratio | **角分布比** |
| R_DCO | DCO ratio; directional correlation from oriented states | **DCO 比（定向核的方向关联比）** |

R_ADO是单线角分布函数W在两个探测方向的比；R_DCO是保留门条件的联合符合强度之比。二者都不是两个角度数值的比。共同描述时写“角分布比或DCO比”，不使用含混的缩写称呼。

术语依据当前投稿稿的单线W之比定义，以及Krämer-Flecken等1989年原文p.334的DCO门控强度定义。对于数据准备，“不确定度来源”是指原文是否直接给出比值及左右误差，或需要由角分布/角关联系数及协方差换算；不是要求程序审核实验人员如何做实验。

### 2.4 P-DCO响应的必读实现合同

**P-DCO是本轮物理核的主要核验对象。实现者必须先完成下述共同强度模型和上下游测试，再接PDM、真实案例及GUI；不能先用简化替代公式把界面跑起来，再把它当作物理已完成。**

详细理论手册为 `raw/writing/pado/20261029_review_v1/PDM/main.tex`，阅读版为同目录 `main.pdf`。以下直接列出实现定义，并用TeX公式标签定位手册，避免页码/公式序号变化后失联。三种模式的核心区别必须在代码和测试中可见。

#### A. 唯一的参考初态

对输入路径中最早观测光子发射前的态，记自旋为I_ref。每个参数点只生成一份布居：

$$
p_m(\sigma)=\frac{\exp[-m^2/(2\sigma^2)]}
 {\sum_{m'=-I_{\rm ref}}^{I_{\rm ref}}\exp[-m'^2/(2\sigma^2)]},
\qquad
\rho_0(\sigma)=\sum_m p_m(\sigma)|I_{\rm ref}m\rangle\langle I_{\rm ref}m|.
$$

目标跃迁具有允许的M1/E2混合时，归一化振幅写为

$$T_t(\xi)=T_{M1}\cos\xi+T_{E2}\sin\xi,\qquad \delta=\tan\xi.$$

各纯多极振幅采用相同的全空间辐射概率归一化；delta为辐射振幅比，不把裸约化矩阵元比直接代入。相位、偏振电场基底与混合项符号必须按原文/勘误核定，不凭名称相同就认为一致。目标以外的跃迁参数由输入给定。单线角分布W有时按球面平均为1归一，而跃迁矩阵按全空间总概率为1归一；与原文或解析基准比较时必须显式对齐常数归一化，不能把它误判为物理差异，更不能改变M1/E2两分量的相对归一化。

#### B. 先构造两光子的联合强度

按实际发射顺序给跃迁编号1、2，不能把target/gate标签当成发射顺序。未观测中间光子对应全方向/偏振求和的传播映射U；相邻时U为恒等映射。U必须是线性、保迹的未观测传播：不能在每一步把未归一化的门条件强度偷偷归一化到1。使用U_k时遵守手册的统计张量归一化约定，不混用不同自旋下的原始张量定义。对于指定偏振通道，联合强度由

$$
C_{\lambda_1\lambda_2}=
\operatorname{Tr}\!\left[
T_2^{\lambda_2}\,\mathcal U\!\left(
T_1^{\lambda_1}\rho_0 T_1^{\lambda_1\dagger}
\right)T_2^{\lambda_2\dagger}\right]
$$

计算，方向自变量在这里省略但在程序中必须保留。DCO对两光子偏振求和；计算P时仅将目标光子投影到平行/垂直电场分析轴，门光子偏振仍求和。

平行/垂直指目标光子的电场分析轴，不是Compton散射计数标签；发射平面和角度端点的参考轴约定须明确，未分析偏振的总强度不能依赖任意偏振基底选择。

因此可以按target/gate身份统一得到 `C_parallel(Omega_t, Omega_g)`、`C_perp(Omega_t, Omega_g)`，以及 `C_0=C_parallel+C_perp`。三者来自同一rho_0和同一辐射模型。门方向选择后产生的相干项必须保留，中间U传播作用于完整密度矩阵/统计张量，不能无条件只传对角布居或B2/B4。

#### C. DCO的定义：保留门方向

$$
R_{\rm DCO}(\xi,\sigma)=
\frac{C_0(\Omega_t=\Omega_a,\Omega_g=\Omega_b)}
 {C_0(\Omega_t=\Omega_b,\Omega_g=\Omega_a)}.
$$

这是联合符合强度之比，不是单线 `W(theta_a)/W(theta_b)`，也不是分别归一化两个条件态后丢弃门出现概率的比。分母零强度必须标记定义域问题，不能加一个小常数伪造有限响应。

#### D. P-DCO的P：对门方向积分后再取偏振比

$$
P_{\rm single}(\xi,\sigma;\Omega_P)=
\frac{\int d\Omega_g\,[C_\parallel(\Omega_P,\Omega_g)-C_\perp(\Omega_P,\Omega_g)]}
 {\int d\Omega_g\,[C_\parallel(\Omega_P,\Omega_g)+C_\perp(\Omega_P,\Omega_g)]}.
$$

这是先分别加总强度再取比，不是对各门方向的条件P作均匀平均。实现可以用等价的解析传播/单线公式加速，不要求逐网格数值球面积分，但必须与联合强度积分的独立测试相符。

- **目标先发、门后发：**单线P直接使用目标初态rho_0；后发门完整求和后不能给P留下门角依赖。DCO仍使用两光子方向关联。
- **门先发、目标后发：**单线P先对上游门光子的全部方向/偏振求和，并传播所有中间跃迁，得到目标发射态；此布居一般不再严格Gaussian。应将其真实布居/张量交给单线P函数，不能重新调用一个以目标自旋为参考、使用同名sigma的Gaussian。

单线偏振底层函数应接收目标发射态的布居或统计张量，由模式入口负责生成/传播该布居；不能把同一个sigma数值当成适用于所有核态的Gaussian宽度。

两种路线中的sigma始终是同一参考初态的参数。既不引入独立的“门后sigma”，也不假设筛选前后的布居相同。P-DCO输入的P按约定已经对应这个无方向条件的单线观测量；程序不替实验方进行有限阵列或效率修正。

#### E. PDCO的P：在指定门方向取偏振比

$$
P_{\rm cond}(\xi,\sigma;\Omega_P,\Omega_g)=
\frac{C_\parallel(\Omega_P,\Omega_g)-C_\perp(\Omega_P,\Omega_g)}
 {C_\parallel(\Omega_P,\Omega_g)+C_\perp(\Omega_P,\Omega_g)}.
$$

目标先发使用POL-DIR的物理次序，目标后发使用DIR-POL；二者都保留方向条件。P的门几何与DCO几何可分别配置，不能自动认为完全相同。输入多个已给方向/路径权重时，先加相应强度再形成比值。

#### F. 三模式返回同一种响应对象

```text
P_ADO : (xi, sigma) -> (P_single, R_ADO)
P_DCO : (xi, sigma) -> (P_single, R_DCO)
PDCO  : (xi, sigma) -> (P_cond,   R_DCO)
```

P_ADO在目标态直接采用Gaussian；DCO两模式在共同参考态采用Gaussian。U_k只用于未作方向选择的传播，不是把“DCO的sigma”换算成“P的sigma”的修正系数。没有中间跃迁时中间传播为1，不意味着两条观测线没有关联。

目标振幅只出现一次、其他模型参数固定时，各联合强度可整理为

$$
C = K_{MM}\cos^2\xi + 2K_{ME}\sin\xi\cos\xi + K_{EE}\sin^2\xi,
$$

用于高效生成响应网格。K必须来自完整联合计算，不准套用单线角分布系数冒充联合系数。随后由唯一PDM核心评价观测密度、计算绝对Jacobian并边缘化；密度矩阵rho不是PDM参数PDF，不新增推断轴。

### 2.5 手册定位、原始依据与防误写测试

| 实现内容 | 手册TeX标签 | 对应代码 |
|---|---|---|
| Gaussian与统计取向 | `eq:population`、`eq:B` | `physics/populations.py` |
| 无条件传播与U_k | `eq:population-transfer`、`eq:propagate`、`eq:uk-pure`、`eq:uk-mixed` | `physics/propagation.py` |
| 联合强度和非相邻路径 | `eq:trace`、`eq:nonadjacent` | `physics/joint.py` |
| DCO分子分母及target/gate身份 | `eq:dco`、`eq:joint-ratio` | `models/p_dco.py`、`models/pdco.py` |
| 单线P及其目标态张量 | `eq:single-P`、`eq:single-P-tensors` | 单线偏振函数及P_DCO入口 |
| 同一联合模型的两种P | `eq:conditional-P`、`eq:common-joint-p` | P_DCO与PDCO入口 |
| 上下游偏振模式 | `eq:pol-dir`、`eq:dir-pol` | 物理次序与投影选择 |
| 混合角二次强度 | `eq:quadratic`、`eq:rational` | 网格系数预计算 |
| PDM映射 | `eq:pdm` | `pdm/mapping.py` |

原始依据：Droste 1996 pp.519–522 Eqs.3–8、12–21；Starosta 1999 p.17 footnote 1的磁项相位勘误；Hamilton编著第12章p.552 Eqs.12.209–12.213；Krämer-Flecken 1989 p.334的DCO门控定义。上述原件均在本库。必须记录“原文约定→本程序约定”的对应表，不把旧代码当唯一真值。

手册的物理定义与本节一起作为实现依据；目录、模式标识、xi(rad)、交互和PyPI发布按本计划的当前约定执行，不从手册尚待同步的工程章节恢复原生打包或旧接口。T15按实际实现同步手册。若直接原文或独立计算暴露物理矛盾，应指出证据、定位和影响，不能为让程序跑通而静默换掉响应。

以下必须成为有名称的测试，而不只是文字保证：

1. 固定源、跃迁和xi/sigma，仅改变DCO门方向，P_single不变；有方向敏感度的控制例中P_cond可以变化。
2. 门先发时，P_single等于完整联合强度的全方向边缘；不能用目标态重新Gaussian化的数值冒充。
3. DCO交换a/b得到倒数，target/gate标签与发射次序分别检验；归一化条件态不得丢掉门概率。
4. 相邻/非相邻传播、完整张量相干项与相对方位角依赖经独立参考核验；U的空乘积不删除观测线关联。
5. 纯项、正负混合项及电场偏振符号分别核定；只有单一分量允许时不生成伪二维混合比PDF。

## 3. 单位、网格与显示：xi 全链条使用弧度

### 3.1 xi 网格

混合角 xi 的输入、内部数组、三角函数、差分、保存及默认图轴统一使用 **rad**，轴标注 `xi (rad)`。不在这条链上来回换算度数。

初始供开发测试的网格为：

```text
xi_min = -1.56 rad
xi_max = +1.56 rad
xi_step = 0.001 rad
xi = [-1.56, -1.559, ..., 1.559, 1.56]
delta = tan(xi)
```

这是 3121 个 xi 点，避开正切在正负 pi/2 的奇点。sigma 初始用默认区间内的 201 个点。实际默认值由收敛与性能测试确定；用户主要操作界面不必理解这些参数。结果触及网格边界时明确提示、扩域检查，不能把截断区间当完整结论。

内部点用中心差分，边界用同阶单边差分；不把 sigma 的辅助网格扩展到负数。Jacobian近零诊断初始阈值为 `1e-12`，明确作用于 `(xi_rad, sigma)`；它不是布居截断或自动删点阈值，调整须有测试依据。纯 E2 的精确辐射极限单独计算，不用无穷 delta 做不稳定运算。

探测器的 `theta/phi` 与混合角 xi 是不同变量。为方便实验人员，探测器几何按度输入并显式标注 `deg`，在几何入口转换一次；配置字段用 `theta_deg`/`phi_deg`，禁止与 `xi_rad` 混用。

### 3.2 sigma 用于计算，sigma/I 用于分析和图示

计算密度以 `(xi_rad, sigma)` 为坐标；Notebook、四联图第二/第四面板及主要取向统计使用 `sigma/I_ref`。以下用 s 仅说明坐标转换，不增加程序的物理参数：

```text
s = sigma / I_ref
f_display(xi, s) = I_ref * f_core(xi, I_ref*s)
p_s(s) = I_ref * p_sigma(I_ref*s)
p_delta(delta) = p_xi(arctan(delta)) / (1 + delta^2)
```

这保证改变坐标后积分概率不变；不能只改刻度、不改 PDF 数值和积分步长。I_ref=0 不使用 sigma/I 扫描，而是独立的解析核态测试。

### 3.3 ETI 与 HDI

新界面、输出、图例与报告统一使用 **ETI**（Equal-Tailed Interval，等尾区间）和 **HDI**，不显示 EQ。

原 `YAnalysis.py` 的 `compute_eq_summary` 实际取 q16/q50/q84，是同一等尾方法的已有实现参考。默认68% ETI为 `[q16,q84]`，中心取中位数 q50；95%使用q2.5/q97.5。HDI采用密度阈值求区间集合，可有多个不相连的分支。

对 delta 和 sigma/I 分别计算 ETI、HDI。delta 的 HDI 必须在 delta PDF 上计算，不能把 xi-HDI 端点变换后当成 delta-HDI。多峰 HDI 报各段边界和质量，不用一个包络区间填平空隙。

## 4. 易维护的目录与职责

核心和 GUI 放在同一个可安装项目；Notebook 调用该项目的公共 API，不复制一份物理或统计内核。

```text
raw/code/PDM/
  README.md                  全项目安装/GUI/analysis入口
  LICENSE                    自有代码的统一许可
  analysis/
    01_results_and_intervals.ipynb
    02_benchmarks_and_comparison.ipynb
    03_report_figures.ipynb
    cases/                    可公开的规范化案例与排除规则
    examples/                 小型GUI输出样例，供Notebook直接读取
    scripts/audit_cases.py
    scripts/run_benchmarks.py
    README.md
  GUI/
    pyproject.toml
    README.md
    LICENSE
    src/multipolepdm/
      __main__.py             PDM 启动
      contracts.py            任务、响应和结果的数据结构
      examples/
        example.json          P_ADO单任务示例
        example_P_DCO.json
        example_PDCO.json
        example_batch.json
        README.md             各字段的填写说明
      models/
        registry.py           标识到模块的分派
        p_ado.py              P_ADO 响应
        p_dco.py              P_DCO 响应
        pdco.py               PDCO 响应
      config/
        common.py            通用参数与默认网格
        p_ado.py              P_ADO 字段/校验/短注释
        p_dco.py              P_DCO 字段/校验/短注释
        pdco.py               PDCO 字段/校验/短注释
      physics/
        populations.py       Gaussian 与张量
        amplitudes.py        归一化多极振幅/相位
        propagation.py       未观测传播与 U_k
        joint.py             共同两光子强度
      pdm/
        observations.py      观测误差密度
        mapping.py           网格/差分/密度转换
        statistics.py        边缘化、ETI、HDI
      plotting/
        style.py             四联图/单图统一样式
        overview.py          四联图、坐标和色标
        intervals.py         PDF 下方 HDI 填充/ETI线
        export.py            单图/整图保存
      io/input.py
      io/export.py
      jobs/manager.py
      jobs/workers.py
      gui/window.py
      gui/results.py
      cli.py
    tests/
      reference/angular_correlation.py
      fixtures/synthetic/
    scripts/build_release.py
    scripts/release.py
```

三个 `models` 文件负责不同观测定义，四个 `config` 文件分别负责共同和模式专属设置。共享计算留在 `physics/` 和 `pdm/`；避免巨型条件分支，也避免三套重复代码。实际拆分可适当调整，但这条职责边界不变。

主要接口：

```python
evaluate_response(job, xi_rad, sigma) -> ResponseGrid
map_density(job, response) -> MappingResult
summarize_density(result, masses=(0.68, 0.95)) -> Summary
make_preview(result, summary) -> PreviewData
load_jobs(path) -> tuple[JobRequest, ...]
submit(job) -> job_id
```

JobRequest 不可变。GUI手动输入和JSON批文件最终生成同一对象。外部输入不执行Python配置代码。保留命名明确的数值/误差/路径/几何/网格字段，不使用含混的 P/R 数组槽位。

## 5. GUI：简单操作、即时评估、后台写盘

### 5.1 输入

- 窗口名 PDM；选择模式后刷新必要字段，下方只显示一行英文说明。
- 默认提供可直接运行的示例和合理网格设置；高级参数折叠。
- 手动输入与JSON批文件二选一。文件模式下手动输入区变灰、禁用，残留值不混入任务。
- 点击一次计算，冻结任务输入，立即允许修改并提交下一条。后台队列和多实例输出互不覆盖。

### 5.2 随包JSON示例：复制即可填，GUI也能生成

安装包内置以下文件，源码位置为 `GUI/src/multipolepdm/examples/`，通过标准资源接口读取，不依赖用户当前工作目录：

- `example.json`：P_ADO单任务。
- `example_P_DCO.json`：P_DCO，完整门线/路径/几何。
- `example_PDCO.json`：PDCO，额外明确偏振的方向门。
- `example_batch.json`：三种模式混合批任务。
- `README.md`：每个字段的含义、单位、左右误差均为正幅度、哪些字段可以留给默认值。

GUI提供“载入示例”“保存输入JSON”，用户可以先在面板填好再保存，不必从零学习JSON语法。可将示例导出到自己的文件夹，修改后选择“输入文件”计算。批文件由每条记录的mode决定模式，不能被面板残留设置覆盖。单任务文件是一个任务对象；批文件顶层含jobs数组，每项都是完整单任务对象。JSON本身不写注释，解释放在README中。

`example.json` 的最小填写示意如下。以下数值仅用于解释格式，不是实验数据；最终随包数值在实现后由通过验证的合成案例生成并实际运行。

```json
{
  "mode": "P_ADO",
  "label": "Synthetic example",
  "target": {
    "spin_initial": 5,
    "spin_final": 4,
    "multipoles": ["M1", "E2"]
  },
  "observations": {
    "P": {"value": -0.20, "err_minus": 0.05, "err_plus": 0.05},
    "R_ADO": {"value": 0.60, "err_minus": 0.04, "err_plus": 0.04}
  },
  "geometry": {
    "theta_P_deg": 90,
    "theta_a_deg": 26,
    "theta_b_deg": 90
  },
  "output": {"directory": "results"}
}
```

示例不填写待求的delta或sigma真值，网格省略时使用默认配置。P_DCO/PDCO示例的输出比值字段改为R_DCO，并给出可直接运行的门信息，不能只用“其余字段类似”代替实际文件。

### 5.3 结果就绪不必等待完整数据文件

```text
提交 -> 后台计算 -> 统计完成 -> 结果/四联图立即可看
                         -> 后台写数据 -> 写入完成
```

结果就绪时显示 `Results ready; saving data...`，同时给出目标目录；文件仍在写时不谎称“已全部保存”。成功关闭全部所选文件后显示 `Saved`；失败则保留可用的图和统计，显示 `Save failed` 并允许重试。

计算、完整导出和高分辨率图片保存均不在GUI主线程进行。预览读取内存中的结果快照，不等CSV落盘再读回来。完整结果和预览分开管理；显示网格可按概率守恒方式降采样，但边缘PDF、区间和科学输出必须来自原计算网格。

### 5.4 四联图与下方统计

| 面板 | 横轴 | 纵轴/内容 |
|---|---|---|
| 1 观测空间 | R_ADO 或 R_DCO | P；显示观测空间密度和测量位置/误差 |
| 2 参数空间 | xi (rad) | sigma/I_ref；正确换算后的二维密度 |
| 3 混合比边缘 | delta | delta 的归一化 PDF |
| 4 取向边缘 | sigma/I_ref | sigma/I_ref 的归一化 PDF |

面板1默认在规则观测网格上评价输入密度；可叠加响应覆盖点。参考 `YPlot.py` 的约束，不把发生折叠的参数网格强行用 pcolormesh 连成观测面，避免画出不存在的连接。

面板3、4使用虚线标记ETI端点、中位数等；HDI仅在被选区间内以 `fill_between(x, 0, pdf)` 填充，边界交点插值，**色带不超过PDF曲线，不使用铺满纵轴的 axvspan**。多段HDI各自填充，中间空隙不着色。图例和可选阈值线不遮挡曲线。

四图下方显示 delta 与 sigma/I 的 ETI/HDI 数值、概率质量和多分支；窗口可滚动、可调整分区尺寸，图可平移/缩放/复位。提供四联总览与单图放大，借鉴 Listcute++ 的交互便利性，不照搬其内部实现。

每个面板有独立保存按钮，另可保存整张四联图。优先支持PNG、PDF、SVG，其他格式按运行时Matplotlib后端能力提供；保存图像从数据重绘，不截屏裁切GUI。含透明度的格式兼容问题要有明确处理，不能静默损坏HDI含义。

### 5.5 四联图标准：统一的Nature-style科研图规范

采用 `nature-figure` 的Python数据图规范，固定为2×2 quantitative grid。科学问题是“给定观测的不确定度如何映射为混合比和取向的约束”：a展示观测输入，b展示联合参数密度，c/d展示两个边缘。保持用户指定的四个面板，不为套模板删改证据。

这里借用的是科学可读性、配色和输出质量规范，不表示本程序投稿Nature，也不把某期刊全部投稿要求强加给用户。

| 项目 | 统一规范 |
|---|---|
| 版式 | a–d按左上、右上、左下、右下排序；面板绘图区和间距对齐；色标使用独立位置，不挤压上排绘图区 |
| 背景与字体 | 白底、统一sans-serif；默认可用的DejaVu Sans，已有Arial/Helvetica可作统一预设；不要求用户另装字体或LaTeX |
| 投稿/报告导出 | 四联图默认宽183 mm、高约150 mm，单图导出默认宽89 mm；轴标题9 pt、刻度/图例8 pt、面板字母10 pt，最终可见字符不得小于5 pt |
| GUI预览 | 独立的较大显示字号预设，不能把论文小字号直接搬到屏幕；预览与导出共用数据、色彩和区间含义 |
| 二维密度 | 默认统一使用cividis感知均匀顺序色图，不用彩虹色；a/b密度测度不同，分别标注色标单位，不能强制共享数值色标 |
| 一维PDF | 深灰/黑曲线，线宽约1.2 pt；坐标轴约0.8 pt，避免重网格和装饰背景 |
| HDI | 色盲友好蓝色（#0072B2）、适度透明；只填0到PDF曲线之间的HDI各段 |
| ETI与中位数 | ETI端点用橙红色（#D55E00）虚线；中位数用明确的线型标记；不单靠颜色区分 |
| 标注 | 各图单位明确，概率质量/区间规则可查；图例与统计区放在不遮挡曲线的位置 |
| 文件 | PDF/SVG优先保留可编辑文本和矢量曲线；PNG/TIFF报告导出以600 dpi为默认；GUI保存对话框提供实际支持的格式 |

样式集中在 `plotting/style.py`，GUI、Notebook、报告和单图保存均调用同一预设，不分散硬编码。文本使用Matplotlib自身mathtext，普通用户无须安装TeX。

开发及报告图验收调用nature-figure的绘图源检查、渲染后面板对齐、PDF字体和碰撞检查；比较面板边界/尺寸/间隔默认容差1.5 pt。确认可见的每个面板和完整四联图，发现遮挡则修复。对齐/碰撞诊断只存临时验收目录，不额外塞给用户。

这些质量检查用于开发和报告交付，不要求普通用户安装skills目录，也不在每次拖动/缩放时运行重型PDF审计。正式公开程序使用自身的轻量布局逻辑和已验证样式。

## 6. Notebook 与科学报告

### 6.1 analysis 交付

三个 Notebook 分别负责：打开结果/查看ETI和HDI；合成与真实案例比较；复现论文报告图。推荐初学者从第一个运行，提供明确的输入文件选择和“运行全部”路径，不要求手动编辑底层代码。

analysis与GUI一起开源。`analysis/examples/` 提供由GUI实际生成的小型合成输出和说明，Notebook默认就能读取；用户只需换成自己的GUI输出文件即可做后续分析。示例必须与正式输出格式相同，不能另造只能在Notebook中使用的格式。

Notebook 和 GUI 使用同一统计/绘图API，分析坐标均为 sigma/I_ref 和 xi(rad)。Notebook可读取已经保存的数据，也可调用同一PDM核心生成结果。选择核素和能量即可定位案例，默认不显示内部溯源字段。

### 6.2 秘书成为图文并茂的报告

更新 `raw/writing/pado/20261029_review_v1/PDM/main.tex`，最终只交付该目录的一个 `main.pdf`。报告要解释：

1. 三种模式的物理区别、共同参考态和传播。
2. 公式如何对应具体模块/函数，以及单位和密度测度。
3. 可读的输入—计算—预览—导出操作流程。
4. 独立参考、注入恢复、真实案例和敏感性结果。
5. 包安装/启动方式、实际测过的平台及未解决边界。

所有科学图必须由 **Python + 实际计算/实验数据**绘制，不使用AI生成或手工编造的图像。模拟与实测图明确区分。图、生成脚本、数据来源/哈希、命令和必要随机种子写入 `PDM/figures/` 的图形清单；原始论文图不能冒称本程序计算图。

推荐图组包括：同一输入下三模式响应对照、上下游/传播示例、代表案例四联图、正负/大E2控制、覆盖率与区间比较、参数域敏感性及计算/写盘耗时。每张图必须有对应数据，不为凑“图文并茂”绘制无依据示意结果。

## 7. 数据源、排除规则与案例覆盖

### 7.1 稳定识别，不依赖排序

数据源：`raw/writing/pado/20261029_review_v1/polarization_delta_collection_20261119_final.xlsx`。

导入按表头名称识别“核素”“Eγ (keV)”等字段，不写死行号或能量列的位置。用户可排序、插入行或移动列。界面和候选表仅以 **核素 + 跃迁能量**标识；程序内部保留必要的来源/分支信息以避免同能量多解混并，但不要求用户查看这些冗余字段。

源文件SHA只用于记录本次输入快照，不作为永远不允许排序的限制。同核同能量确有不同物理跃迁时才提示选择，不能默默合并；同跃迁的多个delta解支仍属于同一条线。

### 7.2 排除与候选

本轮验证数据排除 **74Br**，并排除用户指定的 **SHU74** 来源/别名。当前References中未找到精确SHU74键；实施前按原件身份核定该排除对象，不猜测为另一篇论文，不将未确认的别名候选先运行。排除只作用于本轮验证集，不在通用程序中禁止这些核素。

初查候选如下；能量仅帮助用户识别，不硬编码进读取程序，不代表已经录用：

| 核素 | 核类 | 候选能量（keV） |
|---|---|---|
| 80Se | 偶偶 | 783.5、671.8 |
| 132Ce | 偶偶 | 351.7、197.5 |
| 154Tb | 奇奇 | 244.6、204.7 |
| 36Cl | 奇奇，替换候选 | 790、1170 |
| 185Au | 奇 A | 518.1、292.3 |
| 105Pd | 奇 A | 991、1034 |

36Cl目前表内主要是P和角系数，还需核定原文源取向、系数属于角分布还是角关联，以及是否能得到角分布比或DCO比及相应不确定度；不为了替换74Br而补造缺失的观测量。若不合适，继续查找其他奇奇核，包括但不限于112In等线索，并维持排除规则。SHU74若与任何候选同源，该候选也排除。

### 7.3 覆盖与来源准入

- 主集约8–12条、扩展约6条；总体尽量达到六核，偶偶/奇A/奇奇各两核。
- 每种模式优先至少两个不同核素的完整实测输入；跨模式使用同一条线不算两个独立实验。
- 正负delta各多个；按 E2 份额 `delta^2/(1+delta^2)` 选择低(<0.2)、中(0.2–0.8)、高(>0.8)案例。该划分只是选样规则。
- 最终名单在看PDM结果之前冻结。文献delta不进入反演输入或先验，不按“符合程度”换样。
- 核对P与偏振不对称度、入射束偏振、分析能力的区别；不能按IPDCO名称判定本项目PDCO。
- 门角、路径和多极性从原文获取，缺失不补零。只给角分布/角关联系数时，构造角分布比或DCO比需要明确几何和误差传播依据；若原文直接报告比值与误差则直接记录，缺协方差时不能悄悄假定独立。
- 图示数值优先查原表/补充材料；必要数字化须保存图源、标定和读数不确定度。
- 条件PDCO的两核实测覆盖尚未确认。继续检索补齐；不能用模拟补成实测配额，也不能将无取向放射源直接套成二维Gaussian源反演。

研究阶段的来源核对用于选出可计算案例，不把这些工作加成最终GUI的实验真实性审查。

## 8. 验证方案

### 8.1 独立物理与数值参考

生产核采用归一化跃迁振幅/密度矩阵；独立参考用原文广义角关联/统计张量组装。参考不得导入生产响应或其K系数构造，可共用基础Wigner符号库。核对已发表磁项相位勘误、纯多极极限、概率守恒、全方向积分、上下游和非相邻传播。

普通非零强度点初始比较目标为 `atol=1e-10, rtol=1e-8`；极小强度处分开比较强度与定义域，不用异常比值掩盖误差。

解析一一二维映射检验中心差分/边界单边差分；检验sigma到sigma/I的密度转换、xi(rad)到delta的转换与总概率。PDF积分误差目标 `1e-6`；代表普通案例加密网格后xi中位数变化目标不超过0.0035 rad，区间端点不超过0.0088 rad。边界/多峰例单独分析，不能静默放宽阈值。

### 8.2 注入—恢复与正负控制

固定真实 `(delta0,sigma0)`，生成P与角分布比或DCO比，再给观测量设误差；反演仍扫描sigma，不偷偷固定真值。确定性控制包括delta为0、正负0.1、正负1、正负10，配合低/中/高取向、整数/半整数自旋和三模式。

正负delta测试检验干涉和相位一致性，**不要求P整体反号**。同一函数生成再反演只能证明内部自洽，必须与独立参考生成分开记录。

重复观测抽样初始采用每模式6个代表条件、共18个条件，每条件300次，固定随机种子；报告偏差、区间宽度、经验覆盖率及其抽样误差，必要时有依据地增加重复数。先对称误差，再按定义明确的不对称分布抽样。标称68%区间不自动保证68%频率覆盖率。

### 8.3 图、统计与交互验收

- delta及sigma/I的ETI/HDI均可从同一结果复算，图上着色积分与报告质量一致。
- 多峰HDI没有跨空隙填色；任何着色上边界不高于PDF，端点插值准确。
- 每个面板及四联图可保存PNG/PDF/SVG；其他格式按后端能力验证。
- 改变窗口大小、滚动、缩放和平移不会遮住曲线或统计表；复位操作明确。
- 模拟慢盘时结果/四联图在完整导出结束前出现；编辑和提交下一任务不等待写盘。
- 实测计算、统计、渲染、序列化、压缩和写盘耗时；输入事件延迟p95以200 ms为初始目标，记录硬件条件，不把它当跨所有机器保证。
- Notebook“运行全部”与GUI使用相同数据给出相同区间；科学图脚本可从记录的数据重新生成。

### 8.4 Docker无桌面环境的GUI验证

当前为Docker、没有连接桌面显示。本轮只读检测已发现Xvfb、xvfb-run和xauth；PySide6及pytest尚需在实施时按实际环境安装。不存在必须让用户挂接GUI或另找桌面机器才能推进的前置条件。

采用轻量分层验证：

1. **Qt offscreen为默认功能测试。** 在无显示环境创建真实Qt控件和Matplotlib Qt画布，用pytest-qt/QTest触发模式切换、输入、提交和保存等事件，检查信号、状态、四联图与统计表。
2. **Xvfb用于需要虚拟屏幕的代表流程。** 如offscreen不能覆盖窗口布局或Qt后端行为，使用现有Xvfb运行；不建立VNC/RDP或浏览器桌面工程。
3. **保存可检查证据。** Qt窗口截图、绘图区渲染、导出的PNG/PDF/SVG及任务事件时间线均由实际程序产生。至少每模式运行一条小规模真实计算链；仅对慢盘、磁盘满等故障注入使用mock，不把mock响应算作物理验收。
4. **边界如实记录。** Docker虚拟显示可以验证应用行为和布局，但不能证明Windows/macOS原生窗口、系统菜单、显示缩放和驱动均已实测。无需用户现在提供真实GUI；虚拟环境仍不能覆盖的项列为“未实测”，不伪装成通过，也不让它阻塞物理主线。

计划使用的验证命令为：

```bash
QT_QPA_PLATFORM=offscreen python -m pytest tests/test_gui.py -q
xvfb-run -a -s "-screen 0 1600x1000x24 -nolisten tcp" python -m pytest tests/test_gui.py -q
```

执行者选择适合的命令，不要求两种环境重复所有测试。测试依赖属于dev extra，Xvfb是开发验证工具，不成为普通PyPI用户的运行依赖。实际GUI验证环境和命令证据由任务账本与秘书报告记录。

### 8.5 Reviewer 2 的证据范围

三核类和大E2案例直接补充覆盖范围；合成覆盖率与文献中心值一致性分开报告。对代表案例做网格、sigma下限/上限和明确边缘权重的敏感性分析，不能声称“不固定sigma”就不依赖模型。

本轮不加入二维chi-square比较，不宣称覆盖扩展已证明优越性或完全回应审稿人的所有意见。秘书报告保留不符结果和剩余问题。

## 9. 环境、PyPI 与开源

### 9.1 简化环境和包结构

允许在当前全局Python环境安装/调整所需包，不创建任务专用虚拟环境。记录版本与依赖变更，不无理由全量升级其他项目依赖。

初始评估NumPy、SciPy、SymPy、Matplotlib与PySide6-Essentials；仅需QtCore/QtGui/QtWidgets时避免引入不必要的WebEngine等组件。依赖版本按实际测试确定，不直接将“最新版本”当稳定默认。Notebook需要的JupyterLab、pandas、openpyxl等设为可选analysis依赖。

使用 `pyproject.toml` 构建一套 `py3-none-any.whl` 及sdist；如使用build工具，采用已安装构建依赖和 `--no-isolation`，不另建任务环境。核心不得硬编码Wiki绝对路径。

依赖以 `GUI/pyproject.toml` 为唯一主声明：普通用户执行 `python -m pip install multipolePDM` 自动安装运行依赖；需要Notebook时执行 `python -m pip install "multipolePDM[analysis]"`。开发测试/构建工具单列dev可选依赖，不强塞给普通用户。若提供requirements文件，须从同一依赖定义生成或直接引用项目extra，不维护相互矛盾的两套版本清单。

采用“满足功能的最简单可维护方案”：不建立不必要的环境管理、原生包矩阵或自定义安装器；下载、安装、调试由Agent完成。用户只需完成正常安装/启动、填写数据等简单操作；只有申请账号/API key、授权或创建远端等本人必须操作的事情才请用户协助。权限或资源确实缺失时，一次说明具体需要，不让用户代替Agent排查普通代码问题。

### 9.2 发布名称与凭据

PyPI已有名为pdm的其他项目；本项目采用 **multipolePDM**。本轮公开JSON查询返回404，只表示当时未找到同名项目，不是名称预留；上传前再检查。

凭据来自 `raw/personal/.env` 的 `PYPI_API_KEY`。本轮只确认存在且有正常前缀，未发送凭据、未上传、未证明发布权限。实现验收后的真实发布使用进程内环境变量交给Twine：用户名为 `__token__`，密码为读取的token。不得写入源码、Notebook、计划、日志、命令行参数或公共配置。

发布前先执行 `python -m build --no-isolation` 与 `python -m twine check`。后者只检查制品元数据，不是token鉴权。用验收合格的实际项目制品完成合法首次发布及pip安装回读，不发无意义占位包，也不为“试token”发布垃圾版本。生产PyPI凭据不发送到TestPyPI。

### 9.3 平台检查与公开边界

主交付是一套包及Windows/Linux/macOS使用说明，pip处理依赖平台选择，不建立四个原生安装包工程。

本轮默认在Docker中通过offscreen或Xvfb做安装、启动、三模式示例与保存的轻量检查，不要求用户接入桌面。Windows/macOS保持兼容实现与安装说明，未实际运行则明确标注；不将Linux虚拟显示通过写成其他平台已测。本轮验收不以真实桌面或额外多架构机器为硬条件，无法覆盖的原生体验项目如实记录；主要精力用于响应函数、PDM和数据验证。

用户授权整个 `raw/code/PDM/` 作为开源项目，包括GUI、核心、analysis Notebook、输出读取示例、可公开的规范化案例、合成测试和文档。根README串联安装、GUI使用和Notebook分析，统一自有代码许可，建议MIT。

Git发布根目录是 `raw/code/PDM/`，而不是只有GUI子目录，也不是整个Wiki。PyPI发布可安装的GUI/核心包并内置JSON示例；Git仓库提供完整analysis和GUI输出样例，README给出直接入口。只有API key等凭据和不具再分发许可的第三方原件不进入公开包；不将整本书、出版社PDF或受限图片顺手复制进项目。

已有授权且可写的指定远端才执行push；若远端需用户创建或授权，说明所需一步操作，其余发布工作自行完成。未具备远端时可先交付PyPI和完整可公开源码包，明确Git发布状态，不能伪称push成功。

技术依据及原件归档见 `knowledge/sources/pypi-pdm-packaging-20261120.md`。

## 10. 实施任务与验收

任务按依赖推进；当前状态、实测证据和剩余项由 `tasks.json` 记录。命令在 `raw/code/PDM/GUI/` 执行；analysis脚本从其目录执行。运行时由账本建立唯一 `PDM_RUN_DIR`，并明确设置源Excel、冻结案例清单、报告图目录等路径，不能使用共享固定结果文件。

### T00：建立新项目、基线和全局依赖

- 依赖：无。必读本计划第2.4/2.5节及其指向的秘书公式，核对标签和原件；再读取YAnalysis/YPlot、Excel及排除要求。
- 产出：两个目录的职责、原始输入哈希、全局依赖版本记录、包名与凭据存在性记录；不读取输出token值，不恢复删除的程序。
- 验收：原始Excel/手册/参考脚本保持不变；开发环境可导入必需模块。
- 验证：记录逐模块import和版本；此步不能写成PDM已通过。

### T01：公共合同、独立模式配置与注册表

- 依赖：T00。文件：`contracts.py`、`models/registry.py`、`config/common.py`及三个模式config；`tests/test_contracts.py`。
- 产出：不可变JobRequest、三个大写模式标识、字段描述和英文短注释；共同参考态/相位/target-gate角色/手册公式到模块的对应表。
- 验收：模式字段正确、共同字段不复制、自旋/多极判定正确；xi(rad)、探测角(deg)、sigma明确分开。
- 命令：`python -m pytest tests/test_contracts.py -q`。

### T02：Gaussian、振幅与未观测传播

- 依赖：T01。文件：`physics/populations.py`、`amplitudes.py`、`propagation.py`；`tests/test_physics.py`。
- 实现说明：在秘书手册明确写出振幅矩阵元的CG系数、Wigner-D角函数、电/磁相位和总辐射归一化，以及由完整联合强度提取K系数的方法；逐项关联原始来源和代码函数，不能让T或K停留在未定义的符号占位。
- 验收：归一化、纯项/混合项、整数/半整数、U_0=1及空路径；保留联合关联所需张量/相干信息，不套用单线截断。
- 命令：`python -m pytest tests/test_physics.py -q`。

### T03：三个响应模块

- 依赖：T02。文件：`physics/joint.py`、`models/p_ado.py`、`p_dco.py`、`pdco.py`；`tests/test_responses.py`。
- 接口：`evaluate_response(job, xi_rad, sigma)`。
- 验收：以第2.4节共同强度定义为准，优先完成P_DCO；第2.5节五项防误写测试全部落地。单线/条件偏振、上下游目标、非相邻传播和相干项正确，零强度不伪造比值。
- 命令：`python -m pytest tests/test_responses.py -q`，至少含 `test_p_dco_single_p_gate_angle_invariant`、`test_target_second_singles_matches_transfer`、`test_dco_joint_gate_weight_preserved`、`test_pdco_fixed_gate_polarization`、`test_nonadjacent_relative_azimuth`。

### T04：独立参考与相位验证

- 依赖：T01，可与T02/T03在独立测试路径并行。
- 文件：`tests/reference/angular_correlation.py`、`tests/test_independent_reference.py`。
- 验收：不导入生产响应，按第2.5节原始来源和勘误独立组装；核定正负混合、纯极限、全方向边缘和两种次序。物理定义有冲突时定位和处理，不用数值近似掩盖。
- 命令：`python -m pytest tests/test_independent_reference.py -q`。

### T05：PDM、坐标转换、ETI与HDI

- 依赖：T03、T04。文件：`pdm/observations.py`、`mapping.py`、`statistics.py`及对应测试。
- 验收：xi全链条rad，sigma/I展示密度保持概率，中心/单边差分正确；归一化、非对称误差、delta和sigma/I边缘、ETI及不连通HDI可复算。
- 命令：`python -m pytest tests/test_mapping.py tests/test_statistics.py -q`。

### T06：文件输入、CLI和导出

- 依赖：T05。文件：`io/input.py`、`io/export.py`、`cli.py`、`src/multipolepdm/examples/`中的四个JSON及说明、`tests/test_io.py`。
- 验收：四个随包示例均实际运行；包资源接口在非源码工作目录也可载入/导出示例，wheel安装后的回读由T16/T17复验；GUI可保存输入JSON；手动/文件生成同一任务，批文件逐条模式有效；表头、单位、参考态和关闭状态明确，不兼容旧列名。
- 命令：`python -m pytest tests/test_io.py -q`；`python -m multipolepdm.cli --example P_ADO --output-dir "$PDM_RUN_DIR"`。

### T07：后台计算、即时结果和写盘队列

- 依赖：T06。文件：`jobs/manager.py`、`jobs/workers.py`、`tests/test_jobs.py`。
- 验收：结果就绪通知先于完整写盘完成；输入快照不可变，内存/队列有界，取消/磁盘满/重复提交无误报；支持连续任务与多实例。
- 命令：`python -m pytest tests/test_jobs.py -q`。

### T08：共享四联图、HDI填色与图片保存

- 依赖：T05。文件：`plotting/style.py`、`overview.py`、`intervals.py`、`export.py`、`tests/test_plotting.py`。
- 验收：执行第5.5节统一样式；四轴/单位/独立色标正确，HDI只填PDF下方且无跨段着色，ETI虚线准确；导出通过面板对齐、字体和碰撞检查，且逐面板视觉复核；普通用户无额外skills/TeX依赖。
- 命令：`python -m pytest tests/test_plotting.py -q`；开发制图使用nature-figure的 `validate_figure.py`、`require_matplotlib_panel_alignment()`、`audit_pdf_text.py`、`audit_figure_collisions.py`；逐图检查积分和渲染。技能脚本路径在执行时发现，不写死到公开程序。

### T09：PDM GUI与结果浏览

- 依赖：T01、T07、T08。文件：`gui/window.py`、`gui/results.py`、`__main__.py`、`tests/test_gui.py`。
- 验收：简短英文模式说明、灰化文件模式、一键载入示例/保存输入/计算、后台保存期间可看四图和双变量ETI/HDI、滚动/平移/缩放/复位/单图保存；统计表不遮挡曲线。
- 命令：按第8.4节用 `QT_QPA_PLATFORM=offscreen` 或 `xvfb-run` 执行 `python -m pytest tests/test_gui.py -q`，保存实际Qt渲染及事件证据；不要求用户提供桌面。

### T10：推荐Notebook与报告图生成链

- 依赖：T05、T06、T08；数据充分后持续更新。
- 文件：三个公开analysis Notebook、analysis README、`analysis/examples/` 的小型GUI输出样例；秘书 `figures/` 下的Python生成脚本和图形清单。
- 验收：从公开仓库下载analysis即可读取随附GUI输出示例，“运行全部”可复现，再换成用户文件同样可用；调用同一API/统一样式，图有来源/参数/单位，sigma/I和xi(rad)正确。
- 命令：`jupyter nbconvert --to notebook --execute` 对三个Notebook分别执行并保存带结果的交付副本；输出目录由账本指定。

### T11：排除、排序无关导入与案例冻结

- 依赖：T01。文件：analysis中的 `cases/`、`scripts/audit_cases.py`；GUI不得内置研究排除名单。
- 验收：按表头而非固定列/行读取；行排序、列移动不改变案例识别；核素+能量是用户展示标识；排除74Br/SHU74，同源排除身份核定；冻结主/扩展/缺口清单，不按结果换样。
- 命令：对人工重排的Excel内存副本做导入一致性测试，不修改原Excel；运行审计脚本输出覆盖矩阵。

### T12：注入恢复、正负控制和覆盖率

- 依赖：T04、T05、T06。文件：analysis `scripts/run_benchmarks.py` 的synthetic套件。
- 验收：确定性及重复观测抽样、独立与同核生成分开；正负P不设反号断言；真值包含、偏差、区间宽度、多解和经验覆盖率均报告。
- 命令：从analysis执行 `python scripts/run_benchmarks.py --suite synthetic --output "$PDM_RUN_DIR"`。

### T13：真实案例及范围/权重敏感性

- 依赖：T11、T12。消费：冻结实测案例；文献delta仅用于结果对照。
- 验收：覆盖矩阵按真实完成数填写，保留不符/不可计算案例；代表案例的网格、sigma范围和明示权重影响分开；不加入chi-square拟合。
- 命令：基准脚本分别运行 `--suite empirical` 与 `--suite sensitivity`，清单由账本指定。

### T14：大结果与快速预览整合

- 依赖：T09、T13。消费：代表性完整输出和模拟慢盘任务。
- 验收：不等CSV落盘即可显示四图/ETI/HDI；同时写盘、编辑、提交、保存单图无串任务；记录计算、绘图与I/O耗时及峰值内存，不默减科学精度。
- 命令：基准脚本运行 `--suite io-gui`；记录事件时间线和实际输出规模。

### T15：图文秘书报告

- 依赖：T03起持续更新，定稿依赖T10、T12、T13、T14。
- 文件：新位置 `PDM/main.tex`、唯一 `main.pdf` 与 `figures/`。
- 验收：可读叙述、公式、模块对应、四联图、数据/测试与限制齐全；所有科学图由Python和记录数据生成；没有旧路径、旧模式名和未实现冒充完成。
- 命令：XeLaTeX两遍，临时文件进tmp；检查引用、溢出和逐页视觉布局。

### T16：通用wheel、启动入口与开源清单

- 依赖：T06、T09。文件：根README/LICENSE、GUI的 `pyproject.toml`、包README/许可、构建脚本及随包示例清单。
- 验收：multipolePDM与multipolepdm命名一致，安装生成pdm-gui；一套纯Python wheel和sdist，运行依赖自动安装，analysis/dev可选依赖清楚，核心不硬编码Wiki路径；内置示例完整，包内无凭据或未授权第三方原件。
- 命令：`python -m build --no-isolation`；`python -m twine check dist/*`；检查压缩包文件清单及秘密。

### T17：Docker安装、虚拟显示与平台边界检查

- 依赖：T14、T16。
- 验收：Docker中安装wheel并通过offscreen/Xvfb运行三模式示例、四图与保存；明确虚拟显示已测和各原生平台未测项目，不以缺少桌面为物理工作的阻塞，也不创建原生打包/桌面转发工程。
- 命令：安装wheel后执行 `QT_QPA_PLATFORM=offscreen pdm-gui --self-test --report "$PDM_PLATFORM_REPORT"`；必要时在 `xvfb-run -a` 下运行相同入口。使用实际包内合成示例，记录截图/输出，不宣称真人桌面体验已验证。

### T18：验收后PyPI发布与公开源码

- 依赖：T04、T05、T15、T16、T17。
- 验收：发布的是通过验收的真实制品；token仅通过进程环境传入，无公开日志泄漏；PyPI版本元数据和pip安装回读一致；以README准确声明平台实测边界。
- 操作：GUI发布脚本从环境获取凭据后上传；执行 `python -m pip install --upgrade multipolePDM` 验证真实安装。首次正式版本拟为0.1.0，发布前按实际状态确定，不用空包探测权限。
- Git：在指定远端就绪且有权限时，push整个 `raw/code/PDM/` 项目，包含analysis和GUI；验证公开Notebook示例能读取随附GUI输出。没有远端时交付完整源码包并明确缺少哪一步授权，不擅自公开整个Wiki。

### T19：总验收与交付

- 依赖：T01–T18。
- 验收：响应/统计/图形/交互/发布的证据齐全；候选覆盖和缺口如实；两个代码目录职责清楚；公开Notebook示例与秘书PDF可复现；发布清单无凭据或未授权第三方原件。
- 命令：全测试、定向diff检查、来源归档门、图形/包/报告manifest核对；没有数据或平台实测不能冒称已验证。

## 11. Goal追踪与完成规则

实施goal已按用户批准创建；未指定token预算，不自行设置。`tasks.json` 记录ID、依赖、状态、实际命令、退出码、证据路径、未解决项和下一步。多任务仅在读写路径独立时并行，主Agent负责整合，单文件单写者。

任务初始 `awaiting_user_approval`；实施后可为pending/running/passed/failed/evidence_gap。任务标签不自动改变goal系统状态。每项passed必须有实际证据。

总体交付应包含：

1. 三个响应模块和唯一PDM核心，通过独立物理及密度/统计测试。
2. 友好的GUI、即时四联图、双变量ETI/HDI、后台导出和保存功能。
3. 三个可公开运行的Notebook、随包JSON示例及GUI输出样例、统一Nature-style Python科学图与唯一图文秘书PDF。
4. 冻结选择的真实案例、模拟控制、覆盖矩阵与敏感性结果；缺乏实测模式配额时先继续补齐，无法补齐则明确提交调整，不用模拟冒充。
5. 一套PyPI包及实际上传/安装证据，准确平台状态表；整个PDM项目（含analysis）的源码发布状态。

不以未达到的四平台原生包为完成条件，也不把未测平台说成已测。不能因代码写完、图看起来合理或技能迭代次数用完就宣称科学目标完成。遇到凭据权限或证据缺失，先完成可推进的部分，再按事实记录所需外部条件。

### 11.1 未尽细节的自主研究规则

用户授权Agent补充未讨论充分的细节。优先使用本库知识定位原始文献和公式；不足时可自行检索、阅读并按主题归档合法获得的外部原件，不需要用户逐篇指定。知识页/skill作为检索入口，关键相位、归一化、条件定义回到原件核对。

每项影响结果的新选择记录“问题、来源及页码/公式、适用条件、采用方式、独立核验、残余不确定性”，同步到秘书手册与可复用知识页。可自主完善数值实现、积分方法、缓存、额外校准例、候选文献和界面细节；不得为了实现方便悄悄改变P-DCO的单线P、共同参考态、方向门定义或加入本轮排除的chi-square路线。

若直接证据与已约定的物理定义冲突，明确指出证据和影响，单独处理该问题，同时推进不受影响的工作；缺失的门角、多极性或数据不是可以任意猜测的自由度。自由发挥应增加可验证的正确性，而不是增加没有依据的模型或工程负担。

## 12. 当前准备状态与审核入口

已建立两个空代码目录；Docker无桌面且已有Xvfb工具，GUI验证方案采用offscreen/虚拟显示；已核对秘书手册的物理公式标签，并阅读YAnalysis/YPlot及nature-figure规范，统一ETI、PDF下方HDI填色和四联图样式，确认角分布比与DCO比应分别命名；已核对PyPI官方资料并归档。multipolePDM名称本次查询404；本地API key存在且前缀正常，但尚未进行上传鉴权。

**本轮没有创建实施goal，没有安装程序依赖，没有写响应/GUI代码，没有修改Excel、YAnalysis/YPlot或新秘书手册，没有上传PyPI或push软件。**

用户审核本计划后可直接回复“按此执行”。本计划是完整的当前规格，不要求下一位执行者结合历史修改记录推断需求。
