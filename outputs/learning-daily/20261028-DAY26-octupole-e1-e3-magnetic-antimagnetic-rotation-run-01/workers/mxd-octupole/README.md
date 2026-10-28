# MχD–八极 doorway toy model

这是一个可复现的诊断模型，不是 `133Ce`、`135Nd` 或 `137Nd` 的拟合。运行：

```bash
python3 mxd_octupole_spectrum.py
```

脚本使用四态基底 `|p,χ+⟩, |p,χ−⟩, |−p,χ+⟩, |−p,χ−⟩`，在每个自旋和 1qp/3qp/5qp family 上加入八极 doorway、`E_oct` 和 `v3`，生成：

- `mxd_octupole_spectrum.csv`：能谱与 parity expectation；
- `mxd_octupole_transitions.csv`：E2/M1/E1/E3 相对跃迁网络；
- `mxd_octupole_network_ratios.csv`：`M1/E2`、`E1/E2`、`E3/E2`；
- `mxd_octupole_summary.json`：输入和检查记录。

E1/E3 的数值是无量纲相对振幅平方，没有 Clebsch–Gordan、寿命、内转换或有效电荷归一化；不能与实验 W.u. 直接比较。参数和物理边界见 `knowledge/research-notes/mxd-multiple-chiral-doublets-octupole-coupling-boundary.md`。
