# Triaxial Collective Excitations across the A≈130 Region: Resolving the Frontiers of Nuclear Chirality and Wobbling

**论文投稿源码包与全套衍生数据中枢**

- **论文题目**：*Triaxial Collective Excitations across the $A \approx 130$ Region: Resolving the Frontiers of Nuclear Chirality and Wobbling*
- **拟投期刊**：*Physical Review C* (Regular Article)
- **预印本文件**：[`main.pdf`](main.pdf) 与 [`paper.pdf`](paper.pdf)（4 页双栏排版，1.5 MB）
- **数据防作假溯源手册**：[`DATA_PROVENANCE.md`](DATA_PROVENANCE.md)

---

## 论文核心插图与数据预览 (Figures & Data Preview)

### Figure 1: 半经典三轴转子相空间能量曲面与分离线拓扑
基于朗道刚体欧拉方程与 Raduta 相干态分离线临界条件 $2E_{\text{crit}}\mathcal{J}_2 = I^2$。
- **对应数据文件**：[`data/fig1_separatrix_energy_surface.csv`](data/fig1_separatrix_energy_surface.csv)
- **矢量图文件**：[`figures/fig1_separatrix_rotor.pdf`](figures/fig1_separatrix_rotor.pdf)

![Figure 1: 相空间分离线](figures/fig1_separatrix_rotor.png)

---

### Figure 2: $^{135}\text{Pr}$ 角分布与线偏振双根破简并仲裁
实测 $a_2 = -0.32(4)$（Matta 2015）双根退化（$\delta_1 = -0.11$ vs $\delta_2 = -1.35$）。结合 JUROGAM-II Clover 康普顿散射线偏振实测值 $P = -0.18(6)$（Lv 2022），在 $>10.5\sigma$ 置信度下彻底证伪大模摆动根。
- **对应数据文件**：[`data/fig2_135pr_polarization_dual_roots.csv`](data/fig2_135pr_polarization_dual_roots.csv)
- **矢量图文件**：[`figures/fig2_135pr_dual_root_polarization.pdf`](figures/fig2_135pr_dual_root_polarization.pdf)

![Figure 2: 偏振双根仲裁](figures/fig2_135pr_dual_root_polarization.png)

---

### Figure 3: 手征双重带内带内 $B(M1)$ 同相奇偶交错与简并点极小
基于 $^{135}\text{Nd}$（Zhu 2003 PRL）与 $^{134}\text{Pr}$（Tonev 2007 PRL）绝对电磁跃迁几率，验证 Koike-Starosta-Hamamoto (KSH) 手征选择定则。双带内带内交错 $S_{M1}(I)$ 100% 同相吻合，简并点带间 $\Delta I=0$ 的 $M1$ 跃迁深极小（$<0.05\ \mu_N^2$）。
- **对应数据文件**：[`data/fig3_chiral_m1_staggering.csv`](data/fig3_chiral_m1_staggering.csv)
- **矢量图文件**：[`figures/fig3_chiral_m1_staggering_and_minima.pdf`](figures/fig3_chiral_m1_staggering_and_minima.pdf)

![Figure 3: 手征选择定则同相交错与极小](figures/fig3_chiral_m1_staggering_and_minima.png)

---

### Figure 4: $^{131}\text{Ce} \to {}^{133}\text{Ce}$ 中子费米面演化与摆动阻尼
基于推转 Nilsson-Strutinsky 模型对比 CIAE HI-13 $^{131}\text{Ce}$（Alwaleedi 2017）与 iThemba $^{133}\text{Ce}$（Ayangeakaa 2016）。中子费米面由中壳升至顶壳，引发高 $\Omega$ 轨道 Coriolis 阻尼。
- **对应数据文件**：[`data/fig4_ce_fermi_surface_evolution.csv`](data/fig4_ce_fermi_surface_evolution.csv)
- **矢量图文件**：[`figures/fig4_fermi_surface_evolution_ce.pdf`](figures/fig4_fermi_surface_evolution_ce.pdf)

![Figure 4: 铈同位素费米面演化](figures/fig4_fermi_surface_evolution_ce.png)

---

### Figure 5: P-ADO 取向参数跨反应迁移之束流族 Mahalanobis 剖面
基于科隆大学 Zobel 1983 NIM 实验数据，证明轻离子 $\alpha$ 束退取向随能量急剧破缺（$\tau = 2.16 > 1.0$），而重离子 $^{12}\text{C}$ 熔合蒸发注入稳态取向流（$\tau = 0.74 < 1.0$）。
- **对应数据文件**：[`data/fig5_pado_projectile_family_profile.csv`](data/fig5_pado_projectile_family_profile.csv)
- **矢量图文件**：[`figures/fig5_pado_projectile_families.pdf`](figures/fig5_pado_projectile_families.pdf)

![Figure 5: P-ADO 束流族剖面](figures/fig5_pado_projectile_families.png)

---

## 源码与复现说明

```bash
# 1. 重新生成全套矢量 PDF 与 300 DPI PNG 插图
cd figures/made
python3 generate_figures.py

# 2. 编译 Typst 双栏预印本
typst compile paper.typ main.pdf
```
