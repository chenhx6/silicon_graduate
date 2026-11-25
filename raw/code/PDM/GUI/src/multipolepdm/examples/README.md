# 合成输入 JSON 示例

这些文件随 0.1.1 源码中的 `multipolepdm` 分发。示例使用相同的 $5\to4$ `M1 + E2` 目标跃迁，合成真值为 $\delta=0.5$、$\sigma/I=0.3$。DCO 两个模式另用下游 $4\to2$ 纯 E2 门。各例都采用未筛选方位的环平均和组内相对权重。

| 文件 | 模式 | $P$ | 角分布比或 DCO 比 |
| --- | --- | ---: | ---: |
| `example.json` | `P_ADO` | -0.7540775691 | 1.2222178307 |
| `example_P_DCO.json` | `P_DCO` | -0.7540775691 | 0.9258352809 |
| `example_PDCO.json` | `PDCO` | -0.7607141179 | 0.9258352809 |
| `example_batch.json` | 三个模式 | 各子任务分别给定 | 各子任务分别给定 |

示例的偏振误差幅度为 `max(0.1075, 0.8 * abs(P))`，角分布比或 DCO 比的误差幅度为 `0.1 * abs(R)`，两侧相同。实际测量请按各观测量分别填写 `value`、`err_minus`、`err_plus`，误差字段使用正数。

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

目标线若是纯 E2，例如选择定则禁止 M1 的 $4\to2$ 跃迁，令目标 `multipoles` 只含 `"E2"`，并使用 `multipolepdm my-input.json --forward`。此入口用于正向响应随 $\sigma$ 的标定。参考态自旋为零也只用于正向标定。

## English quick reference

结果读取应分别使用 `summary.delta_pdf` 和 `summary.tan_angle_statistics`。前者是真 δ 密度；后者的 `tan_mode`、`tan_mean` 与 `intervals[].tan_hdi_segments` 分别标作 `tan{mode[arctan(δ)]}`、`tan{mean[arctan(δ)]}`、`tan{HDI68%[arctan(δ)]}`。`tan_mean_std_endpoints` 只是一对转换端点。原示例输入和 68% 约定均未改变；旧快照不改写。

Run a packaged example with `--example MODE` or write its input with `--export-example PATH`. Grouped geometry uses detector-angle entries and explicit `mean` or `sum` weighting. JSON grid coordinates and steps are stored in radians and native sigma. Use `--forward` for pure transitions such as an E2-only $4\to2$ target.
