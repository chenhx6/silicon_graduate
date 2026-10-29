# 锕系奇-A核八极增强原子 Schiff 矩微观微扰求和规则工件

本目录包含奇-A反射不对称变形锕系核（$^{223,225}\text{Ra}, ^{225,227}\text{Ac}$）对比近球形参考核（$^{199}\text{Hg}$）的微观微扰求和规则、内禀电荷几何尺度、介子交换通道响应系数矩阵及相消盲区可复现计算工件。

## 目录清单

- `actinide_schiff_sumrules.py`：核心数值求解与系统学账本生成脚本，求解宇称双重态能量差标度、四核唯象与微观几何尺度、各同位旋介子交换通道响应系数以及相消盲区超平面扫描。
- `actinide_schiff_sumrules.csv`：五核（$^{225}\text{Ra}, ^{223}\text{Ra}, ^{225}\text{Ac}, ^{227}\text{Ac}, ^{199}\text{Hg}$）形变、同自旋宇称伙伴能隙、分母增益、内禀与实验室 Schiff 矩、介子响应系数矩阵及相对 $^{199}\text{Hg}$ 的核结构与原子 EDM 放大倍数汇总表。
- `actinide_schiff_sumrules.json`：包含完整元数据、WKB 隧穿双阱能隙随 $\beta_3$ 演化、Skyrme 泛函敏感性扫描与核素账本的 JSON 结构化数据。
- `actinide_schiff_cancellation_map.csv`：两体介子交换参数空间 $(\bar{g}_1/\bar{g}_0, \bar{g}_2/\bar{g}_0) \in [-2, 2] \times [-2, 2]$ 网格上的核 Schiff 矩响应与相消盲区判定。
- `README.md`：本说明文件。

## 运行与复现命令

在仓库根目录下运行：

```bash
python3 outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/actinide-schiff-sumrules/actinide_schiff_sumrules.py
```

## 关键物理公式与约定

1. **核 Schiff 矩算符与宇称双重态一阶微扰**：
   $$\hat{S}_z = \frac{e}{10} \sum_{i=1}^Z \left( r_i^2 - \frac{5}{3} \langle r^2 \rangle_{\text{ch}} \right) z_i$$
   $$S = 2 \frac{\langle + | \hat{S}_z | - \rangle \langle - | \hat{V}_{\text{PT}} | + \rangle}{E_+ - E_-}$$
2. **内禀几何过渡矩阵元与实验室投影**：
   $$S_{\text{intr}}^{\text{exact}} = \frac{9}{20\pi\sqrt{35}} Z e R_0^3 \beta_2 \beta_3, \qquad S_{\text{intr}}^{\text{compact}} = \frac{3}{20\pi} Z e R_0^3 \beta_2 \beta_3$$
   $$S_{\text{lab}} = \frac{J}{J+1} S_{\text{intr}} \quad (K=J)$$
3. **介子交换展开与相消盲区条件**：
   $$S = a_0 g \bar{g}_0 + a_1 g \bar{g}_1 + a_2 g \bar{g}_2$$
   相消盲平面方程：
   $$\frac{\bar{g}_1}{\bar{g}_0} = - \frac{a_0}{a_1} - \frac{a_2}{a_1} \frac{\bar{g}_2}{\bar{g}_0}$$
   奇中子 $^{225}\text{Ra}$（斜率 $0.667$，截距 $0.250$）与奇质子 $^{225}\text{Ac}$（斜率 $0.521$，截距 $-0.250$）及球形 $^{199}\text{Hg}$（斜率 $-0.164$，截距 $-0.007$）法向量非共线，构成完全正交的互补实验约束网。
