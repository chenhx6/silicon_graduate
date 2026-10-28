# 四极—八极势能面拓扑边界研究回执

长期结论见 [[beta2-beta3-octupole-topology-boundary]]；本文件只记录本轮执行、证据定位和未决边界。

## 结论

“八极关联严格集中于 $\beta_2\approx0.15$–$0.20$”不能作为普适规律。Sm/Gd链的Gogny-D1M二维PES确实在 $N=86,88$ 显示八极方向软化，且最低点大致从 $\beta_2\sim0.1$ 向更大四极形变演化；Ba的反射不对称RMF则在 $^{148,150}$Ba 给出 $\beta_2\approx0.26$–$0.28$、$\beta_3\approx0.17$ 的强八极反例。U链的D1S/D1N/D1M/BCP1计算还显示，深长椭四极背景不自动淬灭八极极小：$^{222-230}$U仍有深度不超过约1.5 MeV的非零 $Q_3$ 极小。

机制上，四极形变通过Nilsson分裂改变异宇称、相同 $\Omega$ 轨道的近简并关系；八极响应还由矩阵元、占据因子、准粒子分母、配对和自洽重排共同决定。偶极相消则依赖质子—中子过渡密度和轨道占据，必须与 $E3$ 集体性分开检查。

## Evidence locators

- `tmp/1504.03243.pdf`, PDF pp.4–5 and Fig.1：Sm/Gd Gogny-D1M二维PES，$N=88$最软，$N\ge90$后八极方向变陡；D1S/D1M总体趋势相近。
- `tmp/1008.1888.pdf`, PDF p.4 Table 1, pp.4–6 Figs.2–3：Ba RMF的 $\beta_2,\beta_3$、$N=88/N=94/Z=56$能隙及 $f_{7/2}$–$i_{13/2}$、$d_{5/2}$–$h_{11/2}$驱动对。
- `knowledge/sources/rodriguez-guzman-2012-sm-gd-quadrupole-octupole.md`：D1S/D1M的 $^{146}$Sm 球形、$^{148,150}$Sm有限八极极小和浅能量增益。
- `knowledge/sources/bernard-2016-144ba-sccm-octupole.md`：$^{144}$Ba约 $(\beta_2,\beta_3)=(0.2,\pm0.1)$ 的软GCM基底及静态形状反演边界。
- `tmp/day26-octupole-doublewell/1209.0927.pdf`, PDF pp.3,7–9：深长椭四极背景、$^{222-230}$U非零八极极小、配对和$D_0$依赖。
- `knowledge/sources/nomura-2020-ra-th-gogny-d1m-octupole.md`：Ra/Th质量区八极集体性在 $^{224}$Ra、$^{226}$Th附近更显著。

## Reusable rule

报告新核时，先给二维PES的最低点与软度，再给费米面轨道和 $\chi_3$ 分项，最后将静态、动态和实验层分开。没有同一坐标归一化、配对处方和惯性定义时，不跨模型比较 $\beta_2/\beta_3$ 数值；没有质子—中子过渡密度分解时，不由小 $B(E1)$ 反推小八极强度。

## Status

本回执只对应一个独立研究工件；不创建session/run/deadline，不推进Day26学分，未运行全库lint，未提交或push。
