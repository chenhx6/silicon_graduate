# MR–Chirality–SD 三维 Routhian 扫描

这是一个可复现的示例性 phenomenological 模型，把平面磁转动（MR）、非共面手征极小和超形变（SD）放在同一组生成坐标
`(beta2, theta, phi)` 中。`beta2` 区分弱形变 ND (`~0.12`) 与 SD (`~0.60`)；`theta` 是剪刀张角；`phi` 是出平面手征角。

## 方程与数值方法

求解器使用

`R(beta,theta,phi;omega) = V_shape(beta;omega) + V_shear(theta;omega) + a_phi(beta,omega) phi^2 + b_phi phi^4 + V_coupling`。

SD 井的旋转增益由 `-1/2 DeltaJ omega^2` 表示，`a_phi` 的符号变换给出 Landau 型平面到非平面分岔。每个频率先在固定形变井内放松角坐标，再在 31×31×31 网格上用 minimax Dijkstra 找两个极小之间的最低瓶颈。WKB 输出采用
`S/hbar = 1.25 sqrt(2 M) barrier^(3/2)`，其中 `M=18 hbar^2/MeV` 是显式示例质量参数；它不是实验提取值，路径长度因子是无量纲代理。

运行：

```bash
python3 mr_chiral_sd_multivalley.py
```

输出 `scan.csv`、`scan.json`、`energy_minima.svg/png` 和 `wkb_actions.svg/png`。缺失的极小表示该局部分支在本模型扫描区间内已失稳或没有被识别；空值不是零势垒。

## 结果边界

在本组参数下，MR 在低频率存在；约 `omega≈0.45–0.50 MeV/hbar` 后平面极小向 `±phi` 手征极小分岔。SD 分支一直可追踪，并随频率降低能量，在约 `omega≈0.3–0.4 MeV/hbar` 与 ND/MR 能量竞争。MR→Chirality 与 MR→SD 的势垒和作用量随分岔/交叉快速下降，分支比由 `exp(-2S/hbar)` 权重给出。

这些是模型结果，不能当作 `106Ag`、`194Pb` 或其它核素的实测临界频率、绝对隧穿寿命或实验分支比。真实预测需要自洽 TAC/PRM、频率依赖惯量、配对和组态混合，并用带间寿命与连接跃迁校验。
