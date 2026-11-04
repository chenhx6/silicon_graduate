# 插图工程与复现指南 (Figure Engineering & Reproduction Manual)

本目录归档论文 5 幅出版级插图的绘图源码与衍生渲染数据。

---

## 目录结构

```
figures/made/
├── README.md              # 本说明书
├── generate_figures.py    # 成套绘图主脚本（Python 3 + Matplotlib）
└── data/                  # 插图专用的密集渲染网格与插值数据
    ├── README.md          # 衍生算法与模型推导说明
    ├── fig1_separatrix_mesh_1500pts.csv
    ├── fig2_135pr_profile_likelihood_curve.csv
    ├── fig3_chiral_staggering_model_curve.csv
    ├── fig4_ce_routhian_trajectories_interpolated.csv
    └── fig5_pado_mahalanobis_distance_profiles.csv
```

---

## 数据双轨架构与可复现性

- **输入 1（原始基准层）**：直接读取 `../../data/` 目录下的原始实验与物理基准表格（`table1` 至 `table5`），绘制真实的实验数据点与误差棒；
- **输入 2（衍生渲染层）**：直接读取 `data/` 目录下的高密度模型曲线与曲面网格数据，绘制光滑的理论预测线与等高线；
- **输出目标**：绘制产物自动保存至上一级目录 `../`，包含矢量 PDF（供 LaTeX/RevTeX 编译）与 300 DPI 高清 PNG（供在线直接图文预览）。

运行复现命令：
```bash
python3 generate_figures.py
```
