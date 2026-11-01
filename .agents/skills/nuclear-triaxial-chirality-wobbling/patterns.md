---
title: "Chirality & Wobbling Motion Research Patterns"
---

# 三轴核手征性与摆动运动研究范式与工作流

## 1. 实验识别与证伪全流程工作流 (Identification Workflow)

```
[阶段 1: 束内符合矩阵与纲图初建]
   ├── 建立 gamma-gamma 对称符合矩阵，设定关键门
   ├── 寻找平行能带与跨带连接跃迁 (Delta I = 1, 2)
   └── 计算动态转动惯量 J^(2)(omega) 与能级差 Delta E(I)

[阶段 2: 角分布与多极性提取]
   ├── 提取不同角度 HPGe 探测器的能量探测效率归一化全能峰面积
   ├── 执行加权最小二乘法拟合 W(theta) -> 获得 a2, a4 及协方差矩阵
   └── 解析求解关于混合比 delta 的一元二次方程 -> 获得双根 (delta_1, delta_2)

[阶段 3: 双根退化破除与偏振联合似然]
   ├── 提取复合锗探测器 (如 Clover 探测器) 的垂直/平行散射计数
   ├── 计算实验线偏振度 P_exp 并与理论曲线 P_theo(delta) 对比
   ├── 扫描联合似然 Delta-chi^2(delta) = chi^2_AD + chi^2_POL
   └── 计算排除统计显著性: sqrt(Delta-chi^2) -> 若 > 3-sigma 则判决确立

[阶段 4: 激发态寿命与绝对电磁跃迁几率]
   ├── 运行 DSAM (薄靶+衬底) 或 RDM (活塞法) 测定能级寿命 tau
   ├── 解算绝对跃迁强度: B(E2) = 0.08156 / [tau(ps) * E_gamma^5(MeV) * (1 + alpha_tot)] * [delta^2 / (1+delta^2)]
   └── 检验 B(E2)_out / B(E2)_in 比值是否满足集体增强

[阶段 5: 微观自洽理论校验]
   ├── 运行 CDFT / TAC / PRM / TPSM 势能曲面计算
   └── 检查在对应自旋下势能面是否存在稳定三轴极小值 (gamma_min ~ 20-30 deg)
```

---

## 2. 核心数学模型计算模式

### Pattern 1: 摆动能量提取公式
对于给定的能带序列：
$$E_w(I) = E(I, n_w=1) - \frac{1}{2} [ E(I-1, n_w=0) + E(I+1, n_w=0) ]$$
若基带中 $I-1$ 或 $I+1$ 能级因回弯未知，可采用局部多项式惯量内插：
$$E_w(I) \approx E(I, n_w=1) - E_{\text{ref}}(I, n_w=0)$$

### Pattern 2: 偏振联合卡方判决模式
当评估竞争假设 $H_{\text{wobbling}}$（解 1）与 $H_{\text{partner}}$（解 2）时：
$$\Delta\chi^2 = \chi^2(H_{\text{wobbling}}) - \chi^2(H_{\text{partner}})$$
- 若 $\Delta\chi^2 > 9.0$：以 $> 3\sigma$ 置信度排除摆动解；
- 若 $\Delta\chi^2 > 25.0$：以 $> 5\sigma$ 置信度彻底证伪摆动解。
