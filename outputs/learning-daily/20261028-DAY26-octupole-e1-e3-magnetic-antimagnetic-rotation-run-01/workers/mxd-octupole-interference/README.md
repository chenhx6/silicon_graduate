# MχD 八极组态干涉求解器

本工件实现一个可复现的有效八带模型，基底为 `|c,chi,p>`，其中 `c=2qp,4qp`、`chi=L/R`、`p=+/-`。它用于检验不同准粒子组态在八极软势面上如何通过相干 E1 路径发生增强或相消，并追踪带内 `B(M1)/B(E2)` 的非简谐变化。

## Run

```bash
python3 mxd_octupole_interference_solver.py
```

输出 `mxd_octupole_interference_scan.csv`（140 个 `(I,beta3)` 点）、包含完整跃迁网络的 `mxd_octupole_interference_scan.json` 和 `mxd_octupole_interference.svg`。扫描自旋为 `I=8,10,12,14`，`beta3=-0.34...0.34`。

## Model

`V(beta3)=1.55 beta3^2/2+8 beta3^4/4-0.018 beta3` 是软势的示意参数化；`t_chi`、`t_par` 和 2qp–4qp 混合 `v_cfg` 依赖于 `beta3`。E1 同时包含同组态路径和相反相位的组态改变路径，因此矩阵元先相加再平方。M1 保持宇称并翻转手征标签，E2 保持宇称，E3 与 E1 同样翻转宇称。所有强度均为 relative units。

## Result snapshot

在本组参数下，`sum B(M1)/sum B(E2)` 随自旋和八极坐标显著偏离常数：扫描范围约为 0.00024–1.51 (`I=8`) 到 0.0051–9.99 (`I=14`)。E1 总强度在 `beta3≈-0.18` 附近达到局部峰值，说明组态混合相位可使 E1 网络不随 `|beta3|` 单调增加。该结果是机制演示，不能直接当作 78Br 或 134Pr 的实验 B 值。

## Reproducibility and limits

仅依赖 Python、NumPy 和可选 matplotlib。模型没有角动量投影、Clebsch–Gordan 系数、绝对寿命、内转换、真实 CDFT 势面或核素特定准粒子波函数；因此只能作为 PRM/GCM 参数扫描的诊断基线。要转为核素拟合，必须输入逐带自旋宇称、绝对 `B(E1/M1/E2)`、寿命和组态波函数。
