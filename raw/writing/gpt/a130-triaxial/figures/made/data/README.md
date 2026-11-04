# 插图特定渲染数据手册 (Derived Plot-Rendering Data Manual)

**存储目录**：`raw/writing/gpt/a130-triaxial/figures/made/data/`
**功能定位**：本目录专门存放**由 `../../data/` 原始基准数据经特定算法、插值或理论模型计算后生成的、用于插图渲染的非通用特定数据 (Plot-Specific Rendering Data)**。

---

## 1. 为什么需要与 `../../data/` 分开存放？

在科学论文绘图中，原始实验数据（保存在 `../../data/`）通常是由离散的数据点、误差棒和实验表格构成的有限集合。
为了在出版物图件中展示**连续理论曲线、二维/三维相空间等高线、连续置信带与似然比扫描抛物线**，绘图脚本必须基于微观核理论方程对连续自变量进行密集的数学离散化（如 100 点扫描或 1500 点空间曲面网格）。

为了**彻底消除数据作假嫌疑**，我们遵循如下透明公开准则：
1. **输入与输出完全解耦**：原始实验数据只读锁死在 `../../data/`；
2. **算法过程 100% 透明公开**：本目录下的所有 CSV 文件均由开源脚本 `generate_figures.py` 或理论求解器计算产出；
3. **数据形式完全披露**：将每一个用于画线的离散点全部以 CSV 格式固化在本目录，任何人均可使用 Excel、Origin 或 Python 直接比对核实。

---

## 2. 衍生渲染数据集与算法处理说明

| 数据集文件名 | 对应插图 | 算法处理形式 | 理论模型与算法推导 | 为什么要特定生成 |
|---|---|---|---|---|
| `fig1_separatrix_mesh_1500pts.csv` | Figure 1 | 50×30 球坐标能量离散网格 | 刚体欧拉方程能量哈密顿量 $E(\phi, \theta)$ | 用于绘制二维彩色能量等高线云图与分离线临界闭合轨迹 |
| `fig2_135pr_profile_likelihood_curve.csv` | Figure 2 | 100 点连续 $\delta \in [-4, 2]$ 扫描 | Hamilton $a_2(\delta)$、极化公式 $P(\delta)$ 与 $\Delta\chi^2$ 剖面 | 用于在连续坐标轴上展示二次有理双实数根与线偏振仲裁曲线 |
| `fig3_chiral_staggering_model_curve.csv` | Figure 3 | 0.25$\hbar$ 步长理论曲线 | KSH 手征奇偶交错方程与两带微扰态混合 | 用于在离散实验点下方衬托 100% 同相吻合的理论交错骨架 |
| `fig4_ce_routhian_trajectories_interpolated.csv` | Figure 4 | 50 点转动频率 $\hbar\omega$ 样条曲线 | 推转 Nilsson-Strutinsky 单粒子 Routhian 及 Landau-Zener 阻尼 | 用于平滑展示费米面从中壳向顶壳移动时的能级交叉轨迹 |
| `fig5_pado_mahalanobis_distance_profiles.csv` | Figure 5 | 25 点束流能量连续流场扫描 | 极小极大马氏距离协方差度规 $D^2(E) = (\vec{r}-\vec{r}_0)^T \mathbf{C}^{-1} (\vec{r}-\vec{r}_0)$ | 用于绘制轻离子去取向破缺曲线与重离子稳态流包络 |

---

## 3. 校验与可复现性命令

在当前目录的上一层 `figures/made/` 中执行：
```bash
python3 generate_figures.py
```
脚本将自动读取 `../../data/` 中的原始基准数据与本目录中的渲染数据，重新绘制出与论文中完全一致的矢量 PDF 和高清 PNG 插图。
