# PDM 界面与输入手册

## 安装和启动

PDM 用实验测得的线偏振度和角分布比或 DCO 比估计多极混合比及取向宽度。请先安装 Python 3.10 或以上版本。打开终端，在 Windows 上可以用 PowerShell。

```sh
python -m pip install --upgrade multipolePDM
python -m multipolepdm
```

如果系统用 `py` 或 `python3` 启动 Python，将命令开头的 `python` 换成相应名称。也可用 `pdm-gui` 打开窗口。

本手册对应 0.1.2。若包索引尚未提供该版本，可从相同版本的完整源码包安装。若已解压该源码包，在其中含 `pyproject.toml` 的 `GUI/` 目录运行 `python -m pip install .`，再用同样的启动命令。第一次操作可以在模式下拉框选择 `P_ADO`，点击 **Load example**，指定输出目录后点击 **Calculate**。

## 按测量方式选择模式

| 界面模式 | 填入的偏振度 $P$ | 填入的比值 |
| --- | --- | --- |
| `P_ADO` | 目标线的单线偏振 | $R_{\mathrm{ADO}}$ |
| `P_DCO` | 目标线的单线偏振，或等效于没有方向选择的偏振 | $R_{\mathrm{DCO}}$ |
| `PDCO` | 在门跃迁方向选择条件下得到的目标线偏振 | $R_{\mathrm{DCO}}$ |

填写目标跃迁的初态、末态自旋和多极性。两个 DCO 模式还需要门跃迁、多极性和已知混合比、级联顺序及中间跃迁。按所用实验定义核对 $P$ 的正负号和混合比相位。偏振输入用校正后的 $P$，百分数需要换成小数，例如 `-20%` 填 `-0.20`。角分布比或 DCO 比的输入按下文所列的 A、B 组次序填写。

目标混合比 $\delta$ 是反演参数，输入目标跃迁时不填已知真值。门和未观测中间跃迁的混合比则是已知输入。`target_first: true` 表示目标在上游、门在下游；`false` 表示上游门馈入下游目标。中间跃迁按衰变顺序列出，初末态自旋必须依次衔接。合成示例标签中的注入值只说明如何产生观测中心，计算不会从标签取得参数。

填写每个观测量的中心值 $x$、正的下误差 $e_-$ 和正的上误差 $e_+$。默认模型从标准正态变量 $Z$ 出发，左侧用 $x+e_-Z$，右侧用 $x+e_+Z$。因此中心是中位数，两侧各占一半概率，两个误差端点对应 $\Phi(-1)\approx0.158655$ 和 $\Phi(+1)\approx0.841345$。误差不等时中心密度有左右跳变。程序按输入的左右尺度直接构造密度，无自动偏态正态拟合。联合误差将偏振度与所用的角分布比或 DCO 比视为独立。结果的 68% ETI 用 `q16` 和 `q84`，与输入端点的上述正态分位约定略有差别。

纯 E2 目标跃迁可用命令行的 `--forward` 做正向标定。若选择定则禁止 M1，例如 $4\to2$，请在输入中只选 `E2`。此时无待估的 M1/E2 混合比，计算给出随取向宽度变化的正向响应。允许 M1/E2 的跃迁才可使用相应双多极性反演。

## 按实验分组录入探测器

每个探测器组由多行 `theta`、`phi`、`weight` 组成。`theta` 是相对取向轴的极角，`phi` 是方位角，均用度。用 **+ Detector** 和 **- Selected** 增删条目。

- **Select ratio azimuth (otherwise average full rings)** 控制比值 A/B 组的 `phi` 输入。`P_ADO` 和 `P_DCO` 的偏振目标组输入也跟随这个开关。勾选后，相应条目可输入 `theta` 和 `phi`。
- `PDCO` 单独显示 **Select PDCO polarization azimuth (target and gate)**，控制偏振目标组和偏振门组的 `phi` 输入。两个开关默认均未勾选，可分别设置。例如 DCO 比采用指定方位、条件偏振按环平均，也可以采用相反的组合。
- 未勾选时，相应组的 `phi` 列灰化并按每行的 `theta` 做整圈强度平均。整圈保留该极角条件，与取 `phi=0` 或对全部 $4\pi$ 方向积分不同。`PDCO` 仍在指定的偏振门极角上选门。
- 默认 **Relative weighted mean** 将组内权重归一到总和为 `1`，例如 `2:1` 实际用 `2/3:1/3`。高级用法 **Raw weighted sum** 直接按输入权重求和，改变组的总权重会改变相应的强度比。权重须非负且每组总和为正。零权重行的贡献为零。
- 权重表示已经提取的观测量所用的有效组权重。程序先分别合成强度，再计算比值或偏振。对角度取平均会改变响应。权重和组定义应与实验处理一致，输入本身不会估算探测效率。

**上下组顺序**可用公式核对。ADO 分子取 A 组强度，分母取 B 组。DCO 分子取目标 A、门 B 的联合强度，分母取目标 B、门 A 的联合强度。`PDCO` 另外使用目标偏振组与偏振门组计算条件偏振。

## 设置网格并保存结果

| 网格行 | 填写项 | 单位 |
| --- | --- | --- |
| 混合角 $\arctan(\delta)$ | 最小值、最大值、步长 | `deg` 或 `rad`，默认 `deg` |
| 取向宽度 | 最小值、最大值、步长 | `sigma/I` 或 `sigma`，默认 `sigma/I` |

角范围须严格位于 $(-\pi/2,\pi/2)$。宽度须为正。$I$ 是设置高斯布居的源态自旋。用 `sigma/I` 输入时，范围与步长都乘以这个 $I$ 进入内部 `sigma` 网格。最大值保留为网格终点。若范围不能被步长整除，最后一格更短，例如从 `0.03` 到 `1`、步长 `0.02` 时，最后一格从 `0.99` 到 `1`。差分和积分使用实际坐标及末格宽度。

推荐网格与示例共用 `multipolepdm.grid.recommend_grid(I_ref)`：混合角范围为 ±89°（JSON 中 ±1.5533430342749532 rad），步长 0.1°（0.0017453292519943296 rad）；内部 $\sigma$ 下限在整数源自旋时为 0.15、半整数源自旋时为 0.20，上限为 $I_\mathrm{ref}$，步长为 $0.005 I_\mathrm{ref}$。推荐模式会随源自旋更新，取消推荐后可手动改范围和步长。

两项观测共用同一个源态布居。`P_ADO` 和目标在上游的 DCO 任务，以目标初态自旋为 $I_\mathrm{ref}$；门在上游时，以门初态自旋为 $I_\mathrm{ref}$。例如 $I_\mathrm{ref}=5$，`sigma/I=0.30` 对应内部 `sigma=1.5`，`0.005 sigma/I` 的步长对应 `sigma_step=0.025`。上游门改变共同源态后，应按新的源自旋换算，不能把源宽度直接当作下游目标态宽度。零源自旋只作正向响应。

可先用默认精度预览，再用更细的步长核对峰位和各区间是否稳定。边缘概率堆积于扫描边界时，核对范围和结果警告。角轴用 π 分数显示，扫描输入可以继续使用度。

在 **Output folder** 选择路径后，单击 **Calculate**。计算完成后程序自动请求打开预览。若另一张图正在导出，预览等绘图锁释放后显示，输入、计算和数据写盘照常进行。保存完成后可从任务列表重开，也可用源码包 `analysis/` 目录中的 Notebook 读取。图件按需从结果窗口另存。手动表单和 JSON 输入是两种入口。若选了 JSON 文件，科学参数来自该文件，输出目录使用界面所选路径。

图中 68% HDI 和 ETI 表示归一化映射密度的概率质量。重复实验能否覆盖真值取决于工况。`PDCO` 合成对照在真值 $\delta=-10$ 时，100 次重复中 ETI 覆盖 0 次，HDI 覆盖 6 次。详见源码包 `analysis/benchmarks/sigma03_relP80_relR10/README.md`。

## JSON 说明、导入和导出

输入使用严格合法 JSON：双引号、无注释和尾逗号，不接受 `NaN`、`Infinity` 或重复键。单任务顶层可以有 `_help` 对象；批量输入的根层和每个任务顶层也可以分别有 `_help`。对象中的文字或结构仅供阅读，完全不参与物理输入和计算。其它未知字段仍严格报错；不能在 `target`、`geometry`、`grid` 等计算对象内部插入 `_help`。

GUI 的 **Save input** 会写入当前任务和 `_help`；**Input JSON file** 可读取带说明或不带说明的单任务及批量文件。旧 JSON 继续兼容。自定义说明在读取后不会成为任务状态；再次保存会生成当前版本的字段说明。计算结果快照继续只保存规范物理输入。

```sh
# 从源码使用时，先在含 pyproject.toml 的 GUI 目录执行安装
python -m pip install -e .
python -m multipolepdm

# 导出带字段说明的单任务或批量输入，编辑后运行
multipolepdm --example P_ADO --export-example my-input.json
multipolepdm my-input.json --output-dir my-results
multipolepdm --example batch --export-example my-batch.json
multipolepdm my-batch.json --output-dir batch-results

# 也可直接运行 P_ADO、P_DCO 或 PDCO 示例
multipolepdm --example PDCO --output-dir pdco-results
```

批量根层只接受非空任务数组 `jobs` 和可选 `_help` 对象，不向子任务继承物理字段。完整可运行文件见 [examples/README.md](src/multipolepdm/examples/README.md)。

JSON 中的 `xi_min_rad`、`xi_max_rad`、`xi_step_rad` 始终是弧度，`sigma_min`、`sigma_max`、`sigma_step` 始终是内部 $\sigma$。`xi_input_unit` 和 `sigma_input_unit` 只记录 GUI 显示单位，不会转换文件中的数字。未提供 `grid` 或写 `grid: {}` 时按共同源自旋采用共享推荐网格；非空显式旧网格（包括 `xi_points`、`sigma_points`）按原输入保留。

探测器组的 `theta_deg` 必填，`phi_deg` 可省略（存储缺省为 0），`weight` 可省略（缺省 1）。推荐使用显式探测器组、`select_azimuth: false` 并省略 `phi_deg`，此时按极角环平均强度，存储的缺省方位不代表选定 `phi=0`。旧标量 `geometry` 输入保持旧接口语义；若需环平均，请使用示例中的组形式。

所有新示例使用目标 $5\to4$ M1/E2 和标签注入 $\delta=0.5$、$\sigma/I=0.30$；DCO 使用下游 $4\to2$ 纯 E2 门。ADO 的比值为目标 26°/90°；DCO 的分子为目标26°、门90°，分母为目标90°、门26°。偏振目标为90°，`PDCO` 的偏振方向门也为90°，全部采用无 `phi` 的环平均。观测中心由正式 `evaluate_response` 生成，误差为 `errP=max(0.1075,0.8*abs(P))`、`errR=0.1*abs(R)`，两侧相同。它们是合成演示，实际测量需替换观测中心及左右误差。

## 角统计的正切表示与真正的δ密度

令 $\xi=\arctan(\delta)$。GUI 和角边缘图将报告值显式标为 `tan{mode[arctan(δ)]}`、`tan{HDI68%[arctan(δ)]}`、`tan{mean[arctan(δ)]}`，各 HDI 分支的局部峰也逐一取正切。这些不是 δ 密度自身的峰、HDI 或算术均值。`tan(mu - std)` 与 `tan(mu + std)` 只称转换端点，`mu`、`std` 来自角 PDF；不能称作 δ 的均值加减标准差。

`marginal_delta.csv` 则是真正的密度变换 $p_\delta(\delta)=p_\xi(\arctan\delta)/(1+\delta^2)$，经过原有加密和数值归一，并非只把角 PDF 的横轴换成 δ。角 HDI 的水平密度阈值属于 $p_\xi$，不可直接画到 $p_\delta$ 上。

当前工作源码的 `multipolepdm-result-v3` 输出在 `summary.json` 中分开 `delta_pdf`（仅坐标与密度）和 `tan_angle_statistics`（带显式名称的角统计转换值）。Python 对应 `summary.delta_pdf` 和 `summary.tan_angle_statistics`；旧 `summary.delta` 仅为兼容旧调用保留，不能按其字段名称推断 δ PDF 自身的统计。读取支持 v1、v2、v3，不改写旧快照。上述命名订正与本手册的 JSON 输入说明纳入 0.1.2；已安装旧版的用户需升级到对应版本才能使用。

## 常见问题

| 遇到的问题 | 处理方法 |
| --- | --- |
| 终端找不到 `pdm-gui` | 启动脚本可能未加入 `PATH`。用安装 PDM 的同一个 Python 运行 `python -m multipolepdm`。 |
| 模式和手动表单变灰 | 勾选 **Input JSON file** 后，模式和参数由 JSON 文件提供。取消勾选即可回到手动输入。 |
| 结果无法写入 | 在 **Output folder** 选有写权限的目录。若计算已完成，点结果窗口的 **Retry data save...** 另选目录。 |
| 选择定则禁止 M1 | 例如 $4\to2$ 的纯 E2 目标，在 JSON 中只选 `E2`，用 `multipolepdm input.json --forward` 做正向标定。 |
| Jacobian 为零 | 该处两项观测无法局部独立约束两个参数。对称角组可能使整个网格退化，得不到二维概率密度。核对实际角组与比值定义，保留实验观测点。 |
| Docker 无图形桌面，`DISPLAY` 未设置 | 在无屏容器中可用 `QT_QPA_PLATFORM=offscreen` 做自动验证。鼠标操作需要有图形会话的桌面环境。 |
| Linux 的 Qt `xcb` 插件无法加载 | 先确认 X11 显示可用，再检查缺失的系统库。Debian/Ubuntu 的常见运行库包有 `libxcb-cursor0`、`libxkbcommon-x11-0`、`libxcb-xkb1` 和 `libx11-xcb1`。按错误中缺失的库安装对应包。 |

## English quick reference

Detector tables contain polar angle, azimuth and weight. Detector angles are in degrees. With azimuth selection off, PDM averages intensities around each selected polar ring. Group weights default to normalized weighted means. Raw weighted sums are available for observables defined by that convention. Enter grid minimum, maximum and step. The endpoint is retained and the final cell can be shorter. Completion requests a preview automatically. An ongoing figure export can defer rendering while input, computation and snapshot writing continue.

保存失败的计算快照仅在本次程序会话中保留。即使其预览被较新任务替换，仍可在任务列表选择它，点 **Open selected result**，再换目录重试保存，无需重算。最多两份未成功保存的结果会占住计算缓冲；重试成功或取消失败任务后队列继续。关闭程序前请处理需要保留的失败结果。
