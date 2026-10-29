# 140–150Ba 双声子八极多重态扫描

运行：

```bash
python3 ba_two_phonon_solver.py --out-dir .
```

输出 `ba_two_phonon_scan.csv/json` 和（matplotlib 可用时）`ba_two_phonon_scan.svg`。扫描包含偶数质量数 `140–150Ba`、`J=0,2,4,6` 非简谐能量、Pauli 振幅淬灭、4p–4h 混合、doorway spreading 宽度，以及八极路径与有效 IVGDR 路径的相干相消。

## 证据边界

`144Ba` 和 `146Ba` 的 Bucher 直接实验基准分别为 `B(E3;3−→0+) = 48(+25/−34)` 和 `48(+21/−29) W.u.`；这两项是输入的实验锚点，脚本没有把它们外推成两声子数据。脚本中的 `E3`、背景态密度、`sigma_V`、4p–4h 混合和 GDR 有效振幅都是可修改的示意输入，输出不是 GOSIA 拟合、ENSDF 能级或已发表的 `Q` 因子。

定义 `Q_amplitude = exp[-0.62*overlap - 0.78*v4]`，`Q_B = Q_amplitude²`，所以实际相对单声子强度为 `2 Q_B`。`Gamma_down = 2π sigma_V² rho` 是 Fermi 黄金律 doorway 估计。库仑激发相消使用 `|A_oct + A_gdr cos(phi)|²/|A_oct|²`；只有共同末态和相干相位成立时才可作物理解释。
