---
type: concept
title: "复合核退激多步γ光子级联量能学、多重数谱仪与在束反应通道分选法典"
aliases: [伽马级联量能学, 多重数谱仪, 总能谱, 反应通道分选, 入口态分布, 统计E1冷却, 集体E2瀑布, BGO球, 4pi量能器]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [gamma-cascade, calorimetry, multiplicity-filter, entry-state-distribution, statistical-e1, collective-e2, bgo-ball, channel-selection, nuclear-instrumentation]
---

# 复合核退激多步γ光子级联量能学、多重数谱仪与在束反应通道分选法典

## 1. 物理全景：从准连续态入口点到高自旋基态能带的光子瀑布

在重离子熔合蒸发反应中，当复合核发射完最后一个热化中子后，残余原子核落在一个由热激发能与旋转角动量张成的相空间中：**入口态（Entry States, $(E_{\text{entry}}^*, I_{\text{entry}})$）**。
此时，激发能已低于所有带电粒子与中子的结合能阈值，强相互作用通道被彻底冻结，**原子核唯一合法的退激手段便是发射密集的 $\gamma$ 光子瀑布（$\gamma$-Cascade）**。

根据 F. S. Stephens（Rev. Mod. Phys. 47, 43, 1975）、M. Jääskeläinen 等（NIM 204, 385, 1983，自旋谱仪 Spin Spectrometer）以及吴治华《原子核物理实验方法》（第三版）：
在配备高立体角覆盖的 $4\pi$ 闪烁体量能球（如 BGO 晶体球、$\text{BaF}_2$ 晶体球或大立体角滤波阵列）中，实验物理学家通过全阵列事件记录，可同时测量两个宏观参量：
1. **总发射 $\gamma$ 能量（Total Cascade Sum Energy, $E_{\text{sum}}$）**；
2. **符合触发晶体探头重数（Coincident Detector Fold, $k$），反映真实光子多重数 $M_\gamma$**。

这两大参量构成了核物理实验中极其强大的物理透镜：
- **两阶段光子退激解耦**：统计 $E1$ 冷却光子负责带走绝大部分内禀热能，而集体延伸 $E2$ 转动光子负责卸掉庞大的旋转角动量；
- **二维 $(E_{\text{sum}}, M_\gamma)$ 反符合门通道分选（Channel Triage）**：由于不同中子蒸发通道（如 $3n, 4n, 5n$）在入口态平面上具有清晰分离的质心岛，通过二维多重数能窗门，**无需使用复杂的带电粒子望远镜或反冲分离器，即可物理提纯极弱的目标出射通道**！

---

## 2. 严格物理模型与量能器仪器响应

### (1) 入口态空间边界与 Yrast 能量线
入口态在 $(E^*, I)$ 平面上的几何分布边界为：
- **下边界：Yrast 能级线**（特定自旋下的最低可能能态）：
  $$E_{\text{yrast}}(I) = \frac{\hbar^2}{2\mathcal{J}_{\text{eff}}} I (I + 1)$$
  其中有效转动惯量在中高自旋下接近刚体转动惯量（$\mathcal{J}_{\text{eff}} \approx 0.85 \mathcal{J}_{\text{rigid}}$）；
- **上边界：中子分离能截断面**：$E_{\text{upper}}(I) = E_{\text{yrast}}(I) + S_n$（高于此能量则继续发射中子）。
残余核入口态分布在 Yrast 线之上 $0 \sim S_n$（典型 $0 \sim 8\text{ MeV}$）的狭窄带状区域中。

---

### (2) 级联两阶段解耦微观动力学
整个退激瀑布由两个物理机制截然不同的阶段串联构成：
1. **第一阶段：准连续区统计 $E1$ 冷却瀑布（Statistical Cooling Cascade）**：
   在入口态刚形成的高能级密度区，原子核主要通过巨偶极共振（GDR）低能尾部发射统计偶极光子。
   - 单光子平均能量较高：$\langle E_{\gamma, \text{stat}} \rangle \approx 1.5 \sim 2.5\text{ MeV}$；
   - 转移角动量极小：偶极跃迁只带走 $\Delta I = 0, \pm 1\hbar$（平均转移 $\approx 0.5\hbar$）；
   - 统计光子多重数估算：
     $$M_{\text{stat}} \approx \frac{E_{\text{entry}}^* - E_{\text{yrast}}(I)}{\langle E_{\gamma, \text{stat}} \rangle} \approx 3 \sim 4\text{ 颗}$$
   此阶段的作用是**将原子核近乎垂直向下“冷却”至靠近 Yrast 线的冷核转动带上**；
2. **第二阶段：集体转动 $E2$ 阶梯瀑布（Collective Yrast Cascade）**：
   当原子核落入转动能带后，系统通过强集体四极跃迁（$\Delta I = 2$ 延伸 $E2$）沿着转动带逐步退激至基态：
   $$M_{\text{coll}} \approx \frac{I_{\text{entry}} - I_{\text{bandhead}}}{2}$$
   单光子能量平缓排列在 $E_\gamma = \frac{\hbar^2}{2\mathcal{J}}(4I - 2) \sim 0.2 \sim 1.2\text{ MeV}$。
   总真实光子多重数为两者之和：
   $$M_\gamma = M_{\text{stat}} + M_{\text{coll}}$$
   总积分跃迁能量即为入口态总激发能：$E_{\text{sum}} = E_{\text{entry}}^*$。

---

### (3) $4\pi$ 闪烁量能器二项式折叠响应（Calorimeter Response）
由 $N_{\text{det}}$ 块独立探测器构成的晶体球对单光子具有平均综合效率 $\Omega_{\text{eff}}$（典型 $0.70 \sim 0.90$）与能量吸收几率 $f_{\text{abs}}$（典型 $0.80 \sim 0.90$）。
测量得到的探头触发重数（Fold, $k$）服从二项分布：
$$P(k | M_\gamma) = \binom{M_\gamma}{k} \Omega_{\text{eff}}^k (1 - \Omega_{\text{eff}})^{M_\gamma - k}$$
平均实测探头重数：
$$\langle k \rangle = \Omega_{\text{eff}} \cdot M_\gamma$$
实测总吸收能量：
$$\langle H \rangle = f_{\text{abs}} \cdot E_{\text{sum}}$$
通过逆响应矩阵（Unfolding Matrix），能够从测量的二维直方图 $(H, k)$ 严格反演初态分布 $(E^*, I)$。

---

## 3. 在束实验 $(E_{\text{sum}}, k)$ 反应通道分选准则

在熔合反应中，由于每多蒸发一个中子必然多消耗 $S_n + 2T \approx 11\text{ MeV}$ 的总能量以及约 $1.5\hbar$ 的角动量：
- **$3n$ 残核通道**：保留了最高的激发能与最高的入口自旋，在 $(E_{\text{sum}}, k)$ 平面上位于**右上角**；
- **$4n$ 残核通道**：位于中间主流区；
- **$5n$ 残核通道**：由于过度蒸发中子，残核几乎贴近冷态基态，位于**左下角**。
实验中，只需在采集系统中划定一个多边形多重数-总能滤窗，便可将信噪比提升一个数量级以上！

---

## 4. 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/gamma_cascade_calorimetry_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `calorim` 命令。

### 运行示范（模拟典型入口态 $E^* = 24\text{ MeV}, I = 22\hbar$ 及多通道分选）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py calorim -E 24.0 -I 22.0 -A 130 --cn-e 58.0 --json
```

### 计算输出核心物理特征：
1. **单状态级联微观分解**：
   - 处于 $A=130, I=22\hbar$ 时，Yrast 能级能量为 $6.42\text{ MeV}$，热激发能为 $17.58\text{ MeV}$；
   - 统计冷却发射 $M_{\text{stat}} = 8.8$ 颗 $E1$ 连续光子，集体转动发射 $M_{\text{coll}} = 11.0$ 颗 $E2$ 光子；
   - 总真实多重数达 $M_\gamma = 19.8$，在效率 $80\%$ 量能器上实测平均触发探头重数 $\langle k \rangle = 15.8$，实测总能 $\langle H \rangle = 20.4\text{ MeV}$；
2. **多通道二维分选坐标质心**：
   - $3n$ 通道：入口能量 $25.0\text{ MeV}$，自旋 $30.5\hbar$，实测重数 $\langle k \rangle = 17.4$；
   - $4n$ 通道：入口能量 $14.0\text{ MeV}$，自旋 $29.0\hbar$，实测重数 $\langle k \rangle = 12.8$；
   - $5n$ 通道：入口能量急剧萎缩至 $3.0\text{ MeV}$，自旋 $27.5\hbar$，实测重数降至 $\langle k \rangle = 11.0$；
   - 各通道质心分离达 $10\text{ MeV}$ 以上，为无粒子探测器条件下的纯纯通道标记提供了严谨的数值物理方案！

---

## 5. 与相关前沿概念的交叉引用
- [[heavy-ion-fusion-evaporation-and-statistical-decay]]：粒子蒸发阶段输出的残核能量正是此处 $\gamma$ 级联的初始入口条件；
- [[hpge-digital-pulse-processing-pzc-and-ballistic-deficit]]：量能球的高效率多重数门通常用于为主力 HPGe 阵列提供高选择性符合选通信号。
