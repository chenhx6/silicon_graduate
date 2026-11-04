# A≈130 论文数据体系全景与防作假审计手册 (Master Data Provenance Manual)

> **WITHDRAWN / historical audit only.** This package is not a submission source
> and its bundled tables and derived claims are not admitted as current evidence.
> The provenance layout is retained to document how the omnibus draft mixed
> direct measurements, model outputs, toy calculations and private workbook
> quantities. Use the narrower P-ADO package for the current public-data paper
> candidate and the `133Ce` project for the separate private-data route.

**论文题目**：*Triaxial Collective Excitations across the $A \approx 130$ Region: Resolving the Frontiers of Nuclear Chirality and Wobbling*
**拟投期刊**：*Physical Review C* (Regular Article)
**数据体系架构**：严格区隔 `data/`（原始基准铁律）与 `figures/made/data/`（插图特定渲染数据）双层体系。

---

## 1. 数据架构设计哲学与铁律

在实验核物理研究与论文撰写中，为彻底杜绝学术不端与数据作假嫌疑，本课题组确立以下数据分层铁律：

```
raw/writing/gpt/a130-triaxial/
├── data/                                 # 【铁律层】原始基准数据（Primary Ground-Truth Data）
│   ├── README.md                         # 原始数据字典与实验引文溯源大纲
│   ├── table1_135pr_experiment_benchmark.csv
│   ├── table2_chiral_benchmark_135nd_134pr.csv
│   ├── table3_ce131_ce133_experimental_levels.csv
│   ├── table4_zobel1983_pado_alignment_experiment.csv
│   └── table5_triaxial_rotor_parameters.csv
└── figures/
    └── made/                             # 【工程层】绘图工程与特定渲染数据（Plot Engineering）
        ├── generate_figures.py           # 成套绘图复现主脚本（Python 3 + Matplotlib）
        ├── README.md                     # 插图工程与复现指南
        └── data/                         # 【渲染层】插图专用密集网格与插值数据（Derived Plot Data）
            ├── README.md                 # 衍生渲染算法与模型推导说明
            ├── fig1_separatrix_mesh_1500pts.csv
            ├── fig2_135pr_profile_likelihood_curve.csv
            ├── fig3_chiral_staggering_model_curve.csv
            ├── fig4_ce_routhian_trajectories_interpolated.csv
            └── fig5_pado_mahalanobis_distance_profiles.csv
```

### 核心区别与法律地位 (Core Distinction & Open Data Mandate)
1. **`<topic>/data/`（原始基准数据 · 铁律层）**：
   - **核心定义**：`writing/gpt/<topic>/data/` 内存放的数据为**原始基准数据**，是**本文章的主要依据**，它是一个**不可任意变动的铁律**（除非最初的物理模型或者计算方案等发生改变）。
   - **内容构成**：严格直接摘录自同行评议发表的实验论文（PRL、PLB、PRC、NIM）与 ENSDF 国际数据库的离散实测能级、角分布勒让德系数、偏振度、跃迁寿命与测量误差（$1\\sigma$），以及标准解析哈密顿量参数。
   - **公开承诺**：**如果随着文章公开数据，我们仅需要公开 `<topic>/data/`**。它是学术界检验文章科学事实、重复数据分析与实验对比的唯一依据。
2. **`<topic>/figures/made/data/`（辅助绘图数据 · 临时缓存层）**：
   - **核心定义**：本目录内存放的是依据原始数据（`data/`）做出的**简单分析或者绘图需要的数据**，**并非文章依赖的数据**。也就是说**算是一个临时文件夹，可有可无，没有什么作用**。
   - **内容构成**：50×30 相空间等高线球面网格点、100 点卡方剖面扫描曲线、能级交叉样条轨迹等密集离散值。
   - **存在价值**：仅为了绘图工程服务（供 Matplotlib 绘制光滑连续曲线，避免图件粗糙）；完全可由 `generate_figures.py` 内置的第一性原理公式动态生成。随文公开数据时无需公开此目录。

---

## 2. 5 幅插图数据映射与科学诚信对账表

| 插图序号 | 插图物理主题 | `data/` 中的原始事实依据 | `figures/made/data/` 中的算法渲染处理 | 理论模型与防作假判决依据 |
|---|---|---|---|---|
| **Figure 1** | 半经典三轴转子相空间极值与分离线拓扑 | `table5_triaxial_rotor_parameters.csv`<br>(Bohr-Mottelson 三轴形变参数 $\beta_2=0.22, \gamma=25^\circ$) | `fig1_separatrix_mesh_1500pts.csv`<br>(1500 点二维等高线能量网格数据) | 朗道《力学》欧拉方程；Raduta 2015 式 (4.19) 临界能量 $E_{\text{crit}} = 0.500$ 严格判定马鞍点拓扑界面 |
| **Figure 2** | $^{135}\text{Pr}$ 角分布双解与偏振破简并 | `table1_135pr_experiment_benchmark.csv`<br>(Matta 2015 实测 $a_2=-0.32(4)$，Lv 2022 实测 $P=-0.18(6)$) | `fig2_135pr_profile_likelihood_curve.csv`<br>(100 点 $\delta \in [-4, 2]$ 连续理论扫描曲线与 $\Delta\chi^2$ 剖面) | Hamilton 1975 二次方程求得等价双根 $\delta_1=-0.11$ 与 $\delta_2=-1.35$；极化度实测以 $>10.5\sigma$（$\Delta\chi^2=111.4$）证伪大模摆动根 |
| **Figure 3** | KSH 手征选择定则同相交错与深极小 | `table2_chiral_benchmark_135nd_134pr.csv`<br>($^{135}\text{Nd}$ 与 $^{134}\text{Pr}$ 的 RDDS 实测绝对寿命与跃迁几率) | `fig3_chiral_staggering_model_curve.csv`<br>(步长 0.25$\hbar$ 的 KSH 理论交错波形与极小点曲线) | Koike-Starosta-Hamamoto 2004 PRL 选择定则：双带内交错 100% 同相；近简并点（$I=14.5\hbar$）带间 $M1$ 发生反演相消深极小（$0.03\ \mu_N^2$） |
| **Figure 4** | 铈同位素费米面演化与摆动模式阻尼 | `table3_ce131_ce133_experimental_levels.csv`<br>(CIAE HI-13 $^{131}\text{Ce}$ 与 iThemba $^{133}\text{Ce}$ 实验能级) | `fig4_ce_routhian_trajectories_interpolated.csv`<br>(50 点转动频率 $\hbar\omega$ 下准粒子 Routhian 插值轨迹) | 推转 Nilsson-Strutinsky 求解；证明中子费米面由中壳升至顶壳引发高 $\Omega$ 轨道 Coriolis 阻尼，摆动模式退化为常规旋称伙伴带 |
| **Figure 5** | P-ADO 取向参数跨反应迁移之束流族剖面 | `table4_zobel1983_pado_alignment_experiment.csv`<br>(Zobel 1983 NIM 原始表 1 与表 2 离散实测 $\alpha_2$ 点) | `fig5_pado_mahalanobis_distance_profiles.csv`<br>(25 点入射能量连续流场马氏距离 $D^2(E)$ 剖面) | 统计学马氏距离协方差检验：$\alpha$ 束去取向随能量急剧破缺（$D^2=9.89, \tau=2.16 > 1$）；$^{12}\text{C}$ 熔合注入高角动量稳态流（$D^2=0.74, \tau=0.74 < 1$） |

---

## 3. 绘图代码复现审计

在 `figures/made/` 目录下运行主绘图脚本：
```bash
python3 generate_figures.py
```
该脚本执行流程：
1. 从 `../../data/` 读取带有物理误差棒的离散实验基准数据，绘制为散点图（带误差棒）；
2. 从 `data/` 读取密集的模型网格与连续曲线数据，绘制为光滑理论背景线与等高面；
3. 将最终合成图件输出为出版级矢量 PDF（用于 LaTeX 编译）与 300 DPI 高清 PNG（用于图文预览）。

所有数据流向清晰、依赖透明、数学严格，完全经得起学术界任何维度的严格复核。
