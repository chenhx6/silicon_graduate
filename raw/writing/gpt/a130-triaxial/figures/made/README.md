# 插图工程与复现指南 (Figure Engineering & Reproduction Manual)

本目录归档论文 5 幅出版级插图的绘图源码与辅助临时渲染数据。

---

## 目录结构

```
figures/
├── made/                  # 【绘图工程主目录】
│   ├── README.md          # 本说明书
│   ├── generate_figures.py# 成套绘图主脚本（Python 3 + Matplotlib）
│   └── data/              # 临时辅助渲染数据（临时缓存，可有可无，非文章依赖数据）
│       ├── README.md      # 临时渲染算法与透明性说明
│       ├── fig1_separatrix_mesh_1500pts.csv
│       ├── fig2_135pr_profile_likelihood_curve.csv
│       ├── fig3_chiral_staggering_model_curve.csv
│       ├── fig4_ce_routhian_trajectories_interpolated.csv
│       └── fig5_pado_mahalanobis_distance_profiles.csv
├── pdf/                   # 矢量 PDF 插图专用存储目录（供 LaTeX/RevTeX/Typst 排版）
└── png/                   # 300 DPI 高清预览图专用存储目录（供在线图文审阅）
```

---

## 核心数据规则与透明绘图流程

1. **唯一科学依据源 (`../../data/`)**：
   `generate_figures.py` 直接读取 `../../data/` 中的原始基准数据（`table1` 至 `table5`），绘制具有物理不确定度的真实实验离散测量点与物理哈密顿量基准。本文章的科学立论完全基于该目录；**如果随着文章公开数据，我们仅需要公开 `<topic>/data/`**。
2. **临时辅助数据 (`data/`)**：
   本目录下的 `data/` **算是一个临时文件夹，可有可无，没有什么独立作用，并非文章依赖的数据**。它仅用于缓存密集离散点（例如 1500 点相空间网格），即使将其全部清空，`generate_figures.py` 内置的第一性原理计算分支也能即时动态重新生成全部曲线。
3. **三端同步输出**：
   执行 `python3 generate_figures.py` 后，脚本会自动将最终图件同步输出至：
   - `../`：供当前目录双栏稿件相对路径直接引用；
   - `../pdf/`：包含出版级矢量 PDF 原件；
   - `../png/`：包含 300 DPI 高清位图，便于 Gitee Web UI 网页端直接内嵌与在线审阅。

---

## 一键复现命令

在当前目录下执行：
```bash
python3 generate_figures.py
```
终端将输出校验回执并刷新所有插图。
