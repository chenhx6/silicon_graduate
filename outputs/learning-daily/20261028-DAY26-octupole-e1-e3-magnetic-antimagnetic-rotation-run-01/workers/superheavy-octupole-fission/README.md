# 超重核八极形变—裂变势垒—WKB 工件

本目录的脚本是一个透明的响应模型，用于展示 `beta2-beta3-beta4` 势能面中反射不对称谷如何改变外裂变鞍点和最小作用量。它不是自洽 Skyrme、Gogny 或 CDFT 计算，不能替代带约束 HFB/RHB、集体惯量和宇称投影的核素预测。

## 运行

```bash
python3 octupole_fission_wkb.py
```

运行后生成：

- `results.json`：Z=114–126、N=170–190 的系统学表，以及 Z=120,N=184 的八极驱动灵敏度；
- `systematics.csv`：每个 Z/N 网格点的内外鞍点、最优 `beta3/beta4`、作用量和 `log10(T_SF/s)`；
- `sensitivity.csv`：八极壳驱动从 0 到 1.25 的响应；
- `octupole_wkb_sensitivity.png`：势能切面与半衰期灵敏度图。

## 模型合同

基准势能含一个 `beta2≈0.55` 内鞍和 `beta2≈0.95` 外鞍；八极刚度在外区由一个靠近 `(Z,N)=(120,184)` 的高斯壳代理降低，并保留 `C234 beta2 beta3^2 beta4` 耦合。`beta4` 在固定 `beta2,beta3` 下解析极小化。WKB 使用

`S/hbar = integral ds sqrt(2 M_eff(s) [V(s)-E0])`，

`T_SF = 2.86e-21 s * (1 + exp(2 S/hbar))`。

脚本采用 `E0=0.70 MeV` 和无量纲有效质量标度 `M=2000`，以便清楚显示势垒变化如何放大到对数寿命；绝对 `T_SF` 仅有模型示意意义。结果中的 `delta_log10_Tsf_vs_no_octupole` 和 `delta_barrier_II_MeV_vs_no_octupole` 才是可迁移的灵敏度诊断。

在代表点 Z=120,N=184，八极驱动尺度 0→1.0 使外鞍约降低 1.75 MeV，toy WKB 的 `log10(T_SF/s)` 下降约 4.52；尺度 1.25 时外鞍降低约 2.86 MeV，下降约 9.06。后一数值说明指数敏感性，不能解读为真实核素半衰期的精度。
