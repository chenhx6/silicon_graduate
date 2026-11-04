# 原始基准数据手册 (Primary Ground-Truth Benchmark Manual)

**存储目录**：`raw/writing/gpt/a130-triaxial/data/`

---

## 核心铁律与数据定位 (The Iron Rule)

1. **原始数据与主要依据**：`writing/gpt/<topic>/data/` 内存放的数据为**原始基准数据 (Primary Ground-Truth Benchmark Data)**，是**本文章的主要依据**与学术立论的坚实物理根基。
2. **不可任意变动之铁律**：本目录内的数据是一条**不可任意变动的铁律**。严禁为了图件美观或迎合结论在此处进行任何人为挑选、平滑、修改或插值。只有当论文最初的物理模型、基本哈密顿量定义或实验计算方案本身发生根本性变革时，才允许对基准数据进行有据可依的版本迭代。
3. **论文随附公开范围 (Open Data Contract)**：如果随着文章发表在学术期刊（如 Physical Review C / Physical Review Letters）、Zenodo 或科学数据平台公开数据，**我们仅需要公开 `<topic>/data/`**。本目录包含了审稿人与科学共同体复核论文所需的全套独立实验基准点、误差棒与理论模型核心常数。

---

## 1. 原始基准数据文件清单

| 文件名 | 物理对应 | 核心实验/理论观测量 | 原始文献出处 | 实验设施与大阵列 |
|---|---|---|---|---|
| `table1_135pr_experiment_benchmark.csv` | Figure 2 实验基准 | $a_2^{\\text{exp}}, a_4^{\\text{exp}}, P_{\\text{exp}}$ 实测点及误差 | Matta 2015 PRL; Lv 2022 PLB | Argonne Gammasphere / JYFL JUROGAM-II |
| `table2_chiral_benchmark_135nd_134pr.csv` | Figure 3 实验基准 | 能级寿命 $\\tau$、绝对 $B(M1), B(E2)$ 矩阵元及误差 | Zhu 2003 PRL; Tonev 2007 PRL | Gammasphere Plunger / LNL Legnaro GASP |
| `table3_ce131_ce133_experimental_levels.csv` | Figure 4 实验基准 | 激发能级 $E_x$、自旋宇称 $I^\\pi$、单粒子组态 | Alwaleedi 2017 PRC; Ayangeakaa 2016 PRC | 中国原子能院 HI-13 / 南非 iThemba AFRODITE |
| `table4_zobel1983_pado_alignment_experiment.csv` | Figure 5 实验基准 | $\\alpha_2, \\alpha_4$ 实测衰减系数与高斯取向宽度 $\\sigma/J$ | Zobel 1983 NIM 207, 389 (Table 1 & 2) | 科隆大学串列加速器核谱学终端 |
| `table5_triaxial_rotor_parameters.csv` | Figure 1 物理基准 | 三轴形变 $(\\beta_2, \\gamma)$、主轴水动力学惯量 $\\mathcal{J}_k$ | 朗道《力学》§37–39; Raduta 2015 Ch. 4 | 经典欧拉刚体动力学解析参数 |

---

## 2. 字段定义与数据字典

### 2.1 Table 1: $^{135}\\text{Pr}$ 角分布与线偏振测量基准 (`table1_135pr_experiment_benchmark.csv`)
- `transition_energy_keV`: 跨带跃迁能量（$747.2, 812.6, 753.8, 594.1\\text{ keV}$）；
- `spin_initial`, `parity_initial`, `spin_final`, `parity_final`: 初末态自旋与宇称；
- `a2_exp`, `sigma_a2`: 实测方向角分布勒让德展开二阶系数及 $1\\sigma$ 实验不确定度（源自 Matta 2015 PRL）；
- `linear_polarization_P_exp`, `sigma_P`: 实测康普顿散射线偏振度及 $1\\sigma$ 不确定度（源自 Lv 2022 PLB）。

### 2.2 Table 2: 手征标杆核绝对电磁跃迁几率基准 (`table2_chiral_benchmark_135nd_134pr.csv`)
- `nucleus`: 标杆核素名（$^{135}\\text{Nd}$ 与 $^{134}\\text{Pr}$）；
- `spin_I`: 能级自旋量子数；
- `lifetime_tau_ps`, `sigma_tau_ps`: 通过反冲距离多普勒频移法（RDDS）测定的绝对寿命（皮秒）；
- `B_M1_in_band_muN2`, `sigma_B_M1`: 带内 $\\Delta I=1$ 磁偶极跃迁几率（$\\mu_N^2$）；
- `B_E2_in_band_e2b2`, `sigma_B_E2`: 带内 $\\Delta I=2$ 电四极跃迁几率（$e^2\\text{b}^2$）；
- `B_M1_interband_DeltaI0_muN2`: 孪生手征伙伴带间 $\\Delta I=0$ 的跨带 $M1$ 跃迁几率。

### 2.3 Table 3: 铈同位素能级与组态基准 (`table3_ce131_ce133_experimental_levels.csv`)
- `nucleus`: $^{131}\\text{Ce}$ 与 $^{133}\\text{Ce}$；
- `band_label`: 跃迁带标识；
- `spin_I`, `parity`: 能级自旋与宇称；
- `excitation_energy_keV`: 能级激发能量；
- `single_particle_orbital`: 对应的中子单粒子轨道。

### 2.4 Table 4: Zobel 1983 原始打靶取向实验表 (`table4_zobel1983_pado_alignment_experiment.csv`)
- `reaction`: 打靶核反应道（$^{62}\\text{Ni}(\\alpha, p\\gamma)^{65}\\text{Cu}$ 与 $^{58}\\text{Ni}(^{12}\\text{C}, 2p\\gamma)^{68}\\text{Ge}$）；
- `E_lab_MeV`: 实验室系入射束流能量；
- `alpha_2_measured`, `sigma_alpha_2`: 实验测定的自旋取向张量衰减系数；
- `extracted_sigma_over_J`, `sigma_sigma_over_J`: 经由 Legendre 展开反演的亚磁能级高斯布居相对宽度 $\\sigma/J$。

### 2.5 Table 5: 三轴转子哈密顿量解析基准 (`table5_triaxial_rotor_parameters.csv`)
- `beta2`, `gamma_deg`: Bohr-Mottelson 三轴形变参数；
- `J1`, `J2`, `J3`: 三主轴流体动力学转动惯量；
- `E_crit`: 鞍点分离线临界能量判据。

---

## 3. 本目录与 `figures/made/data/` 临时目录的本质对立

| 维度 | `<topic>/data/` (本目录) | `<topic>/figures/made/data/` (临时目录) |
|---|---|---|
| **法律地位** | **不可动铁律，文章核心依据** | **临时辅助缓存，可有可无，无独立科学作用** |
| **科学角色** | 真实的实验测量点、物理误差棒、原始理论参数 | 绘图脚本生成的密集网格、平滑曲线、临时计算表 |
| **存在依赖** | 独立存在，不可从零生成，是唯一的源头活水 | 完全派生自 `data/` 与理论方程，删除后可随时重构 |
| **对外公开发布** | **随文章发表公开的唯一必需数据集** | **无需公开发布**（纯属绘图工程内部临时产物） |
