# 合成输入 JSON 示例

这些文件随源码中的 `multipolepdm` 分发。示例使用相同的 $5\to4$ `M1 + E2` 目标跃迁，合成真值为 $\delta=0.5$、$\sigma/I=0.30$。注入值只写在标签中；目标对象没有 `delta` 真值字段。DCO 两个模式另用下游 $4\to2$ 纯 E2 门，门的已知 `delta` 为0、`target_first` 为 `true`。所有探测器行省略 `phi_deg`，采用极角环强度平均和组内相对权重。

ADO 分子/分母分别为26°/90°。DCO 分子为目标26°、门90°的联合强度，分母为目标90°、门26°的联合强度。三模式的目标偏振极角均为90°，`PDCO` 的偏振方向门极角也为90°。

| 文件 | 模式 | $P$ | 角分布比或 DCO 比 |
| --- | --- | ---: | ---: |
| `example.json` | `P_ADO` | -0.7540775691 | 1.6668268541 |
| `example_P_DCO.json` | `P_DCO` | -0.7540775691 | 1.0677658910 |
| `example_PDCO.json` | `PDCO` | -0.7322177521 | 1.0677658910 |
| `example_batch.json` | 三个模式 | 各子任务分别给定 | 各子任务分别给定 |

示例的偏振误差幅度为 `max(0.1075, 0.8 * abs(P))`，角分布比或 DCO 比的误差幅度为 `0.1 * abs(R)`，两侧相同。实际测量请按各观测量分别填写 `value`、`err_minus`、`err_plus`，误差字段使用正数。

观测中心由正式 `multipolepdm.models.registry.evaluate_response` 在 `xi=atan(0.5)`、`sigma=0.30*I_ref=1.5` 处生成，无随机扰动。`P_ADO` 是单线 P 加 ADO 比；`P_DCO` 是单线 P 加 DCO 比；`PDCO` 是方向门条件偏振加 DCO 比。

每个示例的顶层 `_help` 对象说明模式、目标/门、自旋、多极性、上下游、误差、角组、权重和网格；批量根层另有自己的 `_help`。说明不参与计算，可以整块删除。仅这些层级允许 `_help`；其它未知字段仍报错。文件必须是严格 JSON，不得写注释、尾逗号、NaN、Infinity 或重复键。

## 运行和修改

在终端执行 `multipolepdm --example P_ADO --output-dir pdm-results` 可直接运行。使用下面的命令导出一份可编辑的输入，并将其作为新任务提交。

```sh
multipolepdm --example P_ADO --export-example my-input.json
multipolepdm my-input.json --output-dir my-results
```

把 `P_ADO` 换为 `P_DCO`、`PDCO` 或 `batch` 可取得其它示例。也可在 GUI 选择单个模式并点 **Load example**，或在文件输入栏选择单任务或批量 JSON。

`geometry` 中的 `ratio_group_a`、`ratio_group_b`、`polarization_group` 及 `PDCO` 所用的 `polarization_gate_group` 保存各组的 `directions`。每行填写 `theta_deg`、可选的 `phi_deg` 和 `weight`。`select_azimuth: false` 表示在每个指定极角做环强度平均，此时忽略条目中的 `phi_deg`。对指定方位的设置填 `true` 并为各适用条目提供方位角。组的 `normalization` 用 `mean` 时按组内总权重归一，用 `sum` 时按原始权重求和。

`PDCO` 可以对 DCO 比和条件偏振分别选择方位。若其中任一项采用指定方位，设 `select_azimuth: true`，再用 `ratio_azimuth_average` 和 `polarization_gate_azimuth_average` 指定各自是否做环平均。例如逐点计算 DCO 比、按环平均计算条件偏振时，分别设为 `false` 和 `true`。

JSON 网格中的 `xi_min_rad`、`xi_max_rad`、`xi_step_rad` 是弧度，`sigma_min`、`sigma_max`、`sigma_step` 是内部 $\sigma$。`xi_input_unit`、`sigma_input_unit` 记录界面使用的单位。手改 JSON 时需自行换算，例如 $I=5$ 时，界面步长 `0.005 sigma/I` 对应 `sigma_step: 0.025`。

示例从共享 `recommend_grid(I_ref)` 取得推荐网格：`arctan(delta)` 范围±89°（±1.5533430342749532 rad）、步长0.1°（0.0017453292519943296 rad），内部 `sigma` 范围0.15至5、步长0.025。整数源自旋的默认宽度下限为0.15、半整数为0.20，上限为源自旋，宽度步长为 `0.005*I_ref`。GUI 推荐模式自动跟随源自旋；手动模式可编辑网格。JSON 省略 `grid` 或使用空对象时采用推荐值；非空显式旧网格保持原输入。

两项观测共用源态布居：目标在上游时 $I_\mathrm{ref}$ 是目标初态自旋；门在上游（`target_first:false`）时则是门初态自旋。上游门改成 $7\to5$ E2、目标仍为 $5\to4$ 时，`sigma/I=0.30` 应换为源 `sigma=2.1`，不是1.5；中间态布居由级联传递计算。

GUI 的 **Save input** 导出带说明的当前单任务，文件入口可读带或不带说明的单任务及批量 JSON。自定义 `_help` 不保存为计算状态，再导出时生成标准说明。以下命令在含 `pyproject.toml` 的 `GUI/` 目录重生成四份示例，观测中心重新调用正式物理接口，网格重新读取共享默认：

```sh
PYTHONPATH=src python src/multipolepdm/examples/regenerate_examples.py
QT_QPA_PLATFORM=offscreen python -m pytest -q tests/test_json_help.py
```

目标线若是纯 E2，例如选择定则禁止 M1 的 $4\to2$ 跃迁，令目标 `multipoles` 只含 `"E2"`，并使用 `multipolepdm my-input.json --forward`。此入口用于正向响应随 $\sigma$ 的标定。参考态自旋为零也只用于正向标定。

## English quick reference

结果读取应分别使用 `summary.delta_pdf` 和 `summary.tan_angle_statistics`。前者是真 δ 密度；后者的 `tan_mode`、`tan_mean` 与 `intervals[].tan_hdi_segments` 分别标作 `tan{mode[arctan(δ)]}`、`tan{mean[arctan(δ)]}`、`tan{HDI68%[arctan(δ)]}`。`tan_mean_std_endpoints` 只是一对转换端点。此次示例更新几何、观测中心和推荐网格；68% 约定保持，旧快照不改写。

Run a packaged example with `--example MODE` or write its input with `--export-example PATH`. Grouped geometry uses detector-angle entries and explicit `mean` or `sum` weighting. JSON grid coordinates and steps are stored in radians and native sigma. Use `--forward` for pure transitions such as an E2-only $4\to2$ target.
