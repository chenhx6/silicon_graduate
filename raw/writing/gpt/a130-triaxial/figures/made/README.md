# A≈130 三轴形变与集体激发模式论文插图说明书与数据溯源

本目录归档 Physical Review C 投稿论文《Triaxial Collective Excitations across the $A \approx 130$ Region: Resolving the Frontiers of Nuclear Chirality and Wobbling》中使用的全部 5 幅核心插图的生成源码、衍生数据与溯源说明。

---

## 1. 目录架构

```
raw/writing/gpt/a130-triaxial/figures/
├── made/
│   ├── README.md               # 本说明书
│   ├── generate_figures.py     # 独立完整绘图源码（纯 Python 3 + Matplotlib）
│   └── data/                   # 绘图所用的衍生数据文件（CSV 格式）
│       ├── fig1_separatrix_energy_surface.csv
│       ├── fig2_135pr_polarization_dual_roots.csv
│       ├── fig3_chiral_m1_staggering.csv
│       ├── fig4_ce_fermi_surface_evolution.csv
│       └── fig5_pado_projectile_family_profile.csv
├── pdf/                        # 矢量图格式（用于 LaTeX/RevTeX 排版编译）
│   ├── fig1_separatrix_rotor.pdf
│   ├── fig2_135pr_dual_root_polarization.pdf
│   ├── fig3_chiral_m1_staggering_and_minima.pdf
│   ├── fig4_fermi_surface_evolution_ce.pdf
│   └── fig5_pado_projectile_families.pdf
└── png/                        # 高清光栅图格式（300 DPI，用于预览与快速查看）
    ├── fig1_separatrix_rotor.png
    ├── fig2_135pr_dual_root_polarization.png
    ├── fig3_chiral_m1_staggering_and_minima.png
    ├── fig4_fermi_surface_evolution_ce.png
    └── fig5_pado_projectile_families.png
```

---

## 2. 插图物理内涵与数据来源

### Figure 1: 半经典三轴刚性转子相空间极值与分离线拓扑
- **图件路径**：`pdf/fig1_separatrix_rotor.pdf`、`png/fig1_separatrix_rotor.png`
- **数据文件**：`data/fig1_separatrix_energy_surface.csv`
- **物理内涵**：展示非对称转子在单位角动量球面 $M^2 = 1$ 上的能量等值面。中间惯量主轴对应双曲鞍点，不稳定相轨道构成相空间分离线（Separatrix），拓扑区隔了小振幅局部进动（量子摆动模式）与跨鞍点大循环环流（静态手征转动相）。
- **理论来源**：
  - 朗道《力学》刚体欧拉运动方程与 Jacobi 椭圆函数解；
  - A. A. Raduta《Nuclear Structure with Coherent States》第 4 章分离线临界能量公式 $2E_{\text{crit}}\mathcal{J}_2 = I^2$。

### Figure 2: $^{135}\text{Pr}$ 角分布与线偏振双根破简并仲裁
- **图件路径**：`pdf/fig2_135pr_dual_root_polarization.pdf`、`png/fig2_135pr_dual_root_polarization.png`
- **数据文件**：`data/fig2_135pr_polarization_dual_roots.csv`
- **物理内涵**：针对 $^{135}\text{Pr}$ 关键 $747\text{ keV}$ 跃迁，展示角分布 $a_2(\delta)$ 二次有理方程的双实数根（小模解 $\delta_1 \approx -0.11$ vs 大模解 $\delta_2 \approx -1.35$）。引入欧洲 JUROGAM 与 Gammasphere 实测 Clover 康普顿线偏振度 $P = -0.18(6)$，以 $\Delta\chi^2 = 111.4$（$>10\sigma$ 统计置信度）彻底排除了大模摆动根，证实其为单粒子旋称伙伴跃迁。
- **数据来源**：
  - ENSDF $^{135}\text{Pr}$ 实验采用能级纲图；
  - Matta et al., Phys. Rev. Lett. 114, 082501 (2015) 原始角分布数据；
  - Lv et al., Phys. Lett. B 834, 137446 (2022) 康普顿线偏振度测量。

### Figure 3: 手征双重带内带内 $B(M1)$ 同相奇偶交错与简并点极小
- **图件路径**：`pdf/fig3_chiral_m1_staggering_and_minima.pdf`、`png/fig3_chiral_m1_staggering_and_minima.png`
- **数据文件**：`data/fig3_chiral_m1_staggering.csv`
- **物理内涵**：系统展示 Koike-Starosta-Hamamoto (KSH) 手征电磁选择定则。两个伴随带的双带内带内 $B(M1)$ 奇偶交错参数 $S_{M1}(I) = (-1)^I [B(M1)/B(E2)]$ 呈现 $100\%$ 同相咬合，且在能级能量近简并点（$I = 14.5\hbar$ 处），带间 $\Delta I=0$ 的 $M1$ 跃迁呈现近乎零的深极小（$< 0.05\ \mu_N^2$），符合自发手征对称性恢复的无公度选择定则。
- **数据来源**：
  - Zhu et al., Phys. Rev. Lett. 91, 132501 (2003)（$^{135}\text{Nd}$ 绝对电磁矩阵）；
  - Tonev et al., Phys. Rev. Lett. 98, 232501 (2007)（$^{134}\text{Pr}$ 绝对寿命与跃迁矩阵）。

### Figure 4: $^{131}\text{Ce} \to {}^{133}\text{Ce}$ 中子费米面演化与摆动阻尼
- **图件路径**：`pdf/fig4_fermi_surface_evolution_ce.pdf`、`png/fig4_fermi_surface_evolution_ce.png`
- **数据文件**：`data/fig4_ce_fermi_surface_evolution.csv`
- **物理内涵**：展示从 $N=73$（$^{131}\text{Ce}$）到 $N=75$（$^{133}\text{Ce}$）中子费米面跨越独宇称 $h_{11/2}$ 壳层的微观推转 Routhian 轨迹演化。在 $^{131}\text{Ce}$ 中，费米面位于壳层中部偏下，未占据轨道间距大（$\Delta e' \approx 400\text{ keV}$），维持稳定的大振幅进动；在 $^{133}\text{Ce}$ 中，费米面升高接近壳顶，高 $\Omega$ 组态重叠增强粒子-转子 Coriolis 阻尼，自然诱发向非手征对齐带演化。
- **理论来源**：
  - Nilsson-Strutinsky 推转模型单粒子本征方程；
  - Alwaleedi et al., Phys. Rev. C 95, 014316 (2017) 实验能谱能级。

### Figure 5: P-ADO 取向参数跨反应迁移之束流族 Mahalanobis 剖面
- **图件路径**：`pdf/fig5_pado_projectile_families.pdf`、`png/fig5_pado_projectile_families.png`
- **数据文件**：`data/fig5_pado_projectile_family_profile.csv`
- **物理内涵**：检验跨反应共享核自旋取向参数 $\sigma/J$ 的零假说。轻离子 $\alpha$ 束（$11.3 - 22.0\text{ MeV}$）因统计级联去取向效应随能量急剧增大而彻底破除共享假说（$\tau_{\text{req}} = 2.16 > 1.0$）；相反，重离子 $^{12}\text{C}$ 熔合蒸发族（$32.0 - 48.0\text{ MeV}$）形成注入高角动量的稳态热化级联，完全相容于单一取向参数 $r = 0.2824$（$\tau_{\text{req}} = 0.74 < 1.0$）。
- **数据来源**：
  - Zobel et al., Nucl. Instrum. Methods 207, 389 (1983) 原始实验取向衰减测量表。

---

## 3. 复现与重绘说明

在当前目录下直接运行以下命令即可重新读取 `data/` 中的数据并生成全套矢量 PDF 与高清 PNG 图片：

```bash
python3 generate_figures.py
```

绘图环境依赖仅为标准 Python 3、NumPy 与 Matplotlib，无任何额外闭源库。
