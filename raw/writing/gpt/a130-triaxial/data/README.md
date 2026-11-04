# 原始基准数据手册 (Primary Benchmark Ground-Truth Data Manual)

**存储目录**：`raw/writing/gpt/a130-triaxial/data/`
**核心铁律**：本目录专用于存放**不可修改的真实物理与实验基准数据 (Ground-Truth Data)**。数据直接源自经同行评议发表的实验论文、ENSDF 国际核结构数据库与理论基础哈密顿量参数，包含完整的物理测量误差（$1\sigma$ 标准偏差）。严禁在此处进行任何人为平滑、算法插值或挑选性修图。

---

## 1. 原始基准数据文件清单

| 文件名 | 物理对应 | 核心实验/理论观测量 | 原始文献出处 | 实验设施与大阵列 |
|---|---|---|---|---|
| `table1_135pr_experiment_benchmark.csv` | Figure 2 实验基准 | $a_2^{\text{exp}}, a_4^{\text{exp}}, P_{\text{exp}}$ 实测点及误差 | Matta 2015 PRL; Lv 2022 PLB | Argonne Gammasphere / JYFL JUROGAM-II |
| `table2_chiral_benchmark_135nd_134pr.csv` | Figure 3 实验基准 | 能级寿命 $\tau$、绝对 $B(M1), B(E2)$ 矩阵元及误差 | Zhu 2003 PRL; Tonev 2007 PRL | Gammasphere Plunger / LNL Legnaro GASP |
| `table3_ce131_ce133_experimental_levels.csv` | Figure 4 实验基准 | 激发能级 $E_x$、自旋宇称 $I^\pi$、单粒子组态 | Alwaleedi 2017 PRC; Ayangeakaa 2016 PRC | 中国原子能院 HI-13 / 南非 iThemba AFRODITE |
| `table4_zobel1983_pado_alignment_experiment.csv` | Figure 5 实验基准 | $\alpha_2, \alpha_4$ 实测衰减系数与高斯取向宽度 $\sigma/J$ | Zobel 1983 NIM 207, 389 (Table 1 & 2) | 科隆大学串列加速器核谱学终端 |
| `table5_triaxial_rotor_parameters.csv` | Figure 1 物理基准 | 三轴形变 $(\beta_2, \gamma)$、主轴水动力学惯量 $\mathcal{J}_k$ | 朗道《力学》§37–39; Raduta 2015 Ch. 4 | 经典欧拉刚体动力学解析参数 |

---

## 2. 字段定义与数据字典

### 2.1 Table 1: $^{135}\text{Pr}$ 角分布与线偏振测量基准
- `transition_energy_keV`: 跨带跃迁能量（$747.2, 812.6, 753.8, 594.1\text{ keV}$）；
- `spin_initial`, `parity_initial`, `spin_final`, `parity_final`: 初末态自旋与宇称；
- `a2_exp`, `sigma_a2`: 实测方向角分布勒让德展开二阶系数及 $1\sigma$ 实验不确定度（源自 Matta 2015 PRL）；
- `linear_polarization_P_exp`, `sigma_P`: 实测康普顿散射线偏振度及 $1\sigma$ 不确定度（源自 Lv 2022 PLB）。

### 2.2 Table 2: 手征标杆核绝对电磁跃迁几率基准
- `nucleus`: 标杆核素名（$^{135}\text{Nd}$ 与 $^{134}\text{Pr}$）；
- `spin_I`: 能级自旋量子数；
- `lifetime_tau_ps`, `sigma_tau_ps`: 通过反冲距离多普勒频移法（RDDS）测定的绝对寿命（皮秒）；
- `B_M1_in_band_muN2`, `sigma_B_M1`: 带内 $\Delta I=1$ 磁偶极跃迁几率（$\mu_N^2$）；
- `B_E2_in_band_e2b2`, `sigma_B_E2`: 带内 $\Delta I=2$ 电四极跃迁几率（$e^2\text{b}^2$）；
- `B_M1_interband_DeltaI0_muN2`: 孪生手征伙伴带间 $\Delta I=0$ 的跨带 $M1$ 跃迁几率。

### 2.3 Table 4: Zobel 1983 原始打靶取向实验表
- `reaction`: 打靶核反应道（$^{62}\text{Ni}(\alpha, p\gamma)^{65}\text{Cu}$ 与 $^{58}\text{Ni}(^{12}\text{C}, 2p\gamma)^{68}\text{Ge}$）；
- `E_lab_MeV`: 实验室系入射束流能量；
- `alpha_2_measured`, `sigma_alpha_2`: 实验测定的自旋取向张量衰减系数；
- `extracted_sigma_over_J`, `sigma_sigma_over_J`: 经由 Legendre 展开反演的亚磁能级高斯布居相对宽度 $\sigma/J$。

---

## 3. 与 `figures/made/data/` 目录的本质区别

- **`data/`（本目录）**：**不可修改的真实实验事实与物理原件点**。它是科学审稿与实验重复检验的第一现场；
- **`figures/made/data/`**：**特定插图渲染工程数据**。它是从本目录基准出发，通过特定算法模型（如高密度网格离散化、连续样条插值、卡方似然比扫描）运算产出的、专为 Matplotlib 绘图平滑显示所用的辅助数据。
