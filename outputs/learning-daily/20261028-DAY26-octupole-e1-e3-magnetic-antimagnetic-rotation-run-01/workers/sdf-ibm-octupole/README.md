# sdf-IBM 八极玻色子凝聚工件

本工件把 `s,d,f` 玻色子相干态映射成可计算的有限玻色子数模型。运行环境只需要
Python 3 和 NumPy：

```bash
python3 sdf_ibm_octupole.py
```

脚本会生成 `potential_surface.csv`（`N=7` 的二维势能面切片）、
`order_parameter_scan.csv`（扫描 `κ3` 后的最低点和 `β3` 序参量）、
`transition_scaling.csv`（`N=2..20` 的跃迁强度标度）和 `results.json`。

## 模型

玻色子空间是 `s†(L=0,+)`, `d†_μ(L=2,+)`, `f†_μ(L=3,-)`。使用

\[
 H=\epsilon_d n_d+\epsilon_f n_f-\kappa_2 Q_2\cdot Q_2-
 \kappa_3 Q_3\cdot Q_3+\kappa_L L\cdot L,
\]

其中

\[
 Q_2=s^\dagger\tilde d+d^\dagger\tilde s+
 \chi_d[d^\dagger\times\tilde d]^{(2)}+
 \chi_f[f^\dagger\times\tilde f]^{(2)},
\]

\[
 Q_3=s^\dagger\tilde f+f^\dagger\tilde s+
 \chi_{df}([d^\dagger\times\tilde f]^{(3)}+
 [f^\dagger\times\tilde d]^{(3)}).
\]

`Q2` 为宇称偶、`Q3` 为宇称奇，因此 `Q3·Q3` 宇称偶；球张量点积对所有磁分量求和，
保证旋转标量。内禀态为

\[
 |N;\beta_2,\beta_3\rangle={1\over\sqrt{N!}}
 \left({s^\dagger+\beta_2d_0^\dagger+\beta_3f_0^\dagger\over
 \sqrt{1+\beta_2^2+\beta_3^2}}\right)^N|0\rangle .
\]

代码直接构造 13 维单玻色子矩阵，并使用精确的有限 `N` 恒等式

\[
 \langle Q_\lambda\cdot Q_\lambda\rangle_N=
 N(N-1)\,\bar q_\lambda\cdot\bar q_\lambda+N\langle q_\lambda\cdot q_\lambda\rangle_1.
\]

因此在固定内禀幅度下，经典 `N²` 近似遗漏一个 `O(N)` 自身项；只保留两体项时的
相对因子是 `(N-1)/N`。这与单个 `f` 声子衰变的振幅 `∝√N`、几率 `∝N` 是不同
的物理极限，不能把两种 `N` 标度混写。

强耦合轴对称约定给出

\[
 B(E2;2^+\to0^+)={5\over16\pi}Q_{20}^2,
 \qquad B(E3;3^-\to0^+)={7\over16\pi}Q_{30}^2,
\]

其中 `Qλ0=N⟨qλ0⟩`，`Qλ0` 的单位由有效电荷/玻色子电荷固定。它是转子极限的
代数缩放关系，不是对实验绝对 `e² fm^(2λ)` 数值的无参数拟合。

## 实验对账边界

工件保留直接库仑激发的 `144Ba: B(E3;3−→0+)=48^{+25}_{−34} W.u.` 和
`146Ba: 48^{+21}_{−29} W.u.`（Bucher 2016/2017）。采用 50/82 核芯的 IBM-1
计数时，三者的示意玻色子数分别为 `N=6,7,8`。`148Ce` 的 NNDC ENSDF（2026-01
评价）列出 `3−` 候选能级 `841.41(5) keV`，但没有 `B(E3)` 字段；因此 JSON 将
`148Ce` 标成缺失，脚本不填入猜测值。不能把 148Ce 的能级/交替宇称带观测冒充直接
`B(E3)` 测量。

有限数效应的可复核量在 `transition_scaling.csv`：`(N−1)/N` 对 `N=6,7,8`
分别为 `0.8333, 0.8571, 0.8750`。这是相对 `N²` 内禀二体项的抑制；若研究
`3−→0+` 单声子衰变，应使用 `N` 标度并重新构造角动量投影态。

## 适用范围

这是 IBM 相干态/势能面基准，不是自洽 EDF、GCM 或完整角动量投影计算。`β2`、`β3`
网格和相互作用参数均为示意输入；相变扫描显示 `κ3` 增大时 `β3=0` 极小可分岔为
`±β3` 简并极小，但临界点会随 `N`、`κ2`、`χ`、零点能和投影改变。实验静态梨形、
八极软振动和组态混合仍需联合能级、E1/E3、寿命和微观 PES 判别。
