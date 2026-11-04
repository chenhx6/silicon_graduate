# 插图渲染辅助数据说明 (Plot-Rendering Auxiliary Scratchpad)

**存储目录**：`raw/writing/gpt/a130-triaxial/figures/made/data/`

---

## 目录性质与定位 (Nature & Role of this Directory)

1. **临时辅助性质 (Ephemeral Scratchpad)**：
   本目录内存放的是依据原始基准数据（`../../data/`）做出的简单分析或者绘图需要的辅助数据。**它也就是说算是一个临时文件夹，可有可无，没有什么独立作用**。
2. **并非文章依赖的数据**：
   本目录中的所有文件**并非文章结论所依赖的实质性科学数据**。文章的核心依据全部锁死在上一级的 `../../data/` 中。即使将本目录完全清空或删除，主绘图脚本 `generate_figures.py` 内部内置的模型解析求解器也能动态计算并绘制出完全一致的出版级插图。
3. **数据公开发布标准 (Open Data Policy)**：
   **如果随着文章公开数据，我们仅需要公开 `<topic>/data/`**，本目录作为绘图工程过程中的临时辅助产物，无需随文公开发布。
4. **保留本目录的唯一目的**：
   将绘图时生成的密集网格与扫描曲线固化为明文 CSV，是为了**彻底排除学术不端与黑箱作假嫌疑**，使同行评审人员和读者能够透明地看到绘图曲线上每一个插值点的来龙去脉。

---

## 临时渲染文件清单与简单分析算法

| 临时文件名 | 对应插图 | 数据形式 | 算法与简单分析逻辑 | 为什么仅是绘图辅助 |
|---|---|---|---|---|
| `fig1_separatrix_mesh_1500pts.csv` | Figure 1 | 50×30 球坐标网格 (1500点) | 刚体欧拉方程能量哈密顿量离散求解 | 仅用于 Matplotlib 渲染彩色等高面，真实物理参数已在 `data/table5` |
| `fig2_135pr_profile_likelihood_curve.csv` | Figure 2 | 100 点连续 $\\delta$ 扫描曲线 | Hamilton 勒让德展开 $a_2(\\delta)$ 与线偏振 $P(\\delta)$ 理论扫描 | 仅用于绘制平滑的理论双根抛物线，真实实测点在 `data/table1` |
| `fig3_chiral_staggering_model_curve.csv` | Figure 3 | 0.25$\\hbar$ 步长模型交错线 | Koike-Starosta-Hamamoto 选择定则波形与相消深极小解析函数 | 仅用于衬托手征双重带同相交错趋势，真实能级寿命在 `data/table2` |
| `fig4_ce_routhian_trajectories_interpolated.csv` | Figure 4 | 50 点频率 $\\hbar\\omega$ 样条轨迹 | 推转单粒子 Routhian 能级交叉插值与 Fermi 面 Coriolis 阻尼因子 | 仅用于平滑展示交叉演化，真实激发能级在 `data/table3` |
| `fig5_pado_mahalanobis_distance_profiles.csv` | Figure 5 | 25 点束流能量连续剖面 | 极小极大马氏距离协方差流场计算 | 仅用于展示取向衰减包络线，真实打靶测量在 `data/table4` |

---

## 可复现性验证与重构

若要重构或清理本临时目录，只需在 `../` 目录运行：
```bash
python3 generate_figures.py
```
即使缺少本目录中的任何文件，脚本也会自动以第一性原理理论公式动态计算并补齐所有画线数据。
