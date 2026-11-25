# PDM Notebook 使用指南

下载并解压与 0.1.1 候选版配套的源码包。打开终端，进入含本 README 和三个 `.ipynb` 的 `analysis/` 目录。安装共享核心与 Jupyter 依赖，再启动 JupyterLab。

```sh
python -m pip install "../GUI[analysis]"
python -m jupyter lab
```

默认依赖已包含 GUI 所需的 PySide6。`analysis` 是 `multipolePDM` 的可选依赖组，只添加分析依赖。Notebook、数据和脚本随源码包取得，`analysis/` 中的程序直接导入 `multipolepdm`。PyPI 已发布的 0.1.0 可用于其配套文档和示例。

## 第一次打开 Notebook

在 JupyterLab 左栏双击文件，选择安装了候选源码的 Python 内核，再从 **Run** 菜单选 **Run All Cells**。三个 Notebook 可分别运行。

1. [01_results_and_intervals.ipynb](01_results_and_intervals.ipynb) 默认计算一个内置 `P_ADO` 合成例，显示四联图，并逐段输出 68% HDI。已有保存好的 GUI 或 CLI 结果时，将 `result_dir = None` 改为 `result_dir = Path("你的结果目录")`。选择包含 `manifest.json` 和 `density.npz` 的那一级目录。
2. [02_benchmarks_and_comparisons.ipynb](02_benchmarks_and_comparisons.ipynb) 对三种模式分别注入正负混合比，列出输入真值、观测量、区间各段和真值是否落入区间。生成与反演共享同一个核心，适合检查流程与符号。重复含噪实验有独立的覆盖率问题，文献对照也需核对几何和标定条件。
3. [03_report_figures.ipynb](03_report_figures.ipynb) 用同一绘图 API 输出 PDF、PNG 四联图和四张 SVG 单图。默认在 `generated_figures/` 写合成示例图。换自己的图时，填写 `result_dir`，并选择输出目录和文件名前缀。

## 从输出定位输入与统计

`manifest.json` 记录任务输入、源态、自旋、单位和警告，`density.npz` 保存内部混合角弧度与 $\sigma$ 网格及密度。`load_result` 从快照重建结果，`summarize_density` 在当前规则下重算摘要。运行新实验时请保留快照及相应的软件版本。对于早期结果，以当前版本重算的角区间仍受早期输入、几何和扫描域约束。

`Summary.arctan_delta` 是混合角的统计来源。`Summary.tan_angle_statistics` 将角统计转换值明确命名为 `tan_mode`、`tan_median`、`tan_mean`，图表分别写作 `tan{mode[arctan(δ)]}`、`tan{q50[arctan(δ)]}`、`tan{mean[arctan(δ)]}`，不称为 δ PDF 自身的峰或算术均值。每个 `intervals` 条目的 `tan_hdi_segments` 是 `tan{HDI68%[arctan(δ)]}` 的全部分支，各段给出 `bounds`、`mass` 与转换后的局部 `mode_ranges`，质量相加为 `0.68`。`tan_eti` 给出角 q16/q84 的正切。`tan_mean_std_endpoints` 只称转换端点，不称 δ 标准差；越界看 `mean_bound_flags`。角均值与标准差从 `Summary.arctan_delta` 读取。`Summary.sigma_over_i` 直接在源态归一的 $\sigma/I$ 密度上统计。旧 `Summary.delta` 混合对象仅为旧调用兼容保留。

完整网格 CSV 可按需导出。节点概率质量用 `parameter_node_probability` 汇总。`Summary.delta_pdf` 与 `marginal_delta.csv` 保存真正的 $p_\delta=p_\xi/(1+\delta^2)$，不是只换横轴；等角步长取正切后非均匀，δ PDF 可能使用加密坐标，积分必须使用对应坐标权重。角 HDI 阈值仅适用于角密度，不可直接用作 δ PDF 的水平阈值。新 v3 `summary.json` 分开 `delta_pdf` 与 `tan_angle_statistics`，读取仍兼容 v1/v2，旧快照不改写。此为未另发版本的工作源码订正，不改原输入或数值。文献混合比仅用于独立对照，缺失的门条件或原文未注明的误差类型保留在比较记录中。

## English quick reference

Install `../GUI[analysis]` and open these notebooks from the matching source archive. Use `result_dir` to read a completed GUI or CLI snapshot. The core evaluates 68% HDI and ETI in angle space. `Summary.delta_pdf` is the actual transformed density; `Summary.tan_angle_statistics` separately reports tan of angle estimates, not delta-PDF mode, HDI or arithmetic mean. Mean +/- std transformations are endpoints only. Figure export uses the same plotting API as the GUI. The current source writes result schema v3 and reads v1/v2/v3 without changing old snapshots; no new software version is published.

## 研究用验证脚本

在 `analysis/` 目录运行。文献计算指定 `grouped_geometry_v0_1_1` 输入快照，每次复算为 `--output` 选一个新目录。

```sh
python scripts/run_benchmarks.py --suite synthetic --check-xi-bounds --output benchmarks/my-validation
python scripts/run_literature_cases.py --input cases/grouped_geometry_v0_1_1 --output cases/my-grouped-results --project-root ..
python scripts/run_followup_cases.py --input cases/followup/grouped_geometry_v0_1_1 --output cases/followup/my-grouped-results --project-root ..
```

程序化验证与上面的短 Notebook 示例各有独立配置。研究批次请保留实际运行的输入、网格、误差策略和程序版本。使用跨生成器配对噪声时，按独立观测的数量解释覆盖率。

文献算例按记录采用点角或理想环几何，实际阵列的效率及方向条件以来源为准。初始集合包括九条 `P_ADO` 线，以及同一条 185Au `P_DCO` 线的六种几何设置。后续算例加入 154Tb、185Au 518.1 keV、190Tl 的结果及 164Yb 的条件 `PDCO` 测量。同一实测输入的不同几何为敏感性比较，只计为同一测量。纯跃迁使用正向标定。相关设置见 [后续算例说明](cases/followup/README.md)。

80Se 文献用 $P$、$R_{\mathrm{DCO}}$ 和固定宽度 `sigma/j=0.35` 提取混合比。本库的 `P_ADO` 算例用实测角分布比并扫描宽度，比较时需保留两套条件。
190Tl 采用可复现的原文最终 $P$ 图读值，读数不确定性和来源限制单列。

如需审计已有的研究工作簿，可以使用以下命令。常规 GUI 和 Notebook 使用 JSON 或已保存的结果。

```sh
python scripts/audit_cases.py --workbook YOUR_WORKBOOK.xlsx --source-root YOUR_SOURCE_ROOT --out-dir audit-output
```

工作簿脚本按表头读取，在内存副本上检查行列重排。`cases/source_evidence.json` 保存核对用的来源清单。完整核对需要自行准备可访问的论文原件及工作簿。

三个公开 Notebook 及0.1.1 benchmark/reference 流程使用源码包中的 `GUI/` 和 `analysis/`。`analysis/research/` 中的历史 E01/E03 探针另有可选的旧实现依赖，复跑这些探针需要原工作区的 `raw/writing/pado/Upload`。源码包内保留的历史证据可独立阅读，公开 Notebook 和0.1.1 验证无需安装该旧实现。
