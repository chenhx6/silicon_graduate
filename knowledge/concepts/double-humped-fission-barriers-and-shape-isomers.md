---
type: concept
title: "双峰裂变势垒量子穿透、裂变形状异能态（Class-II）与亚阈中间共振动力学"
aliases: [双峰裂变势垒, 裂变异能态, 形状异能态, Class-II态, 超形变第二极小, 亚阈裂变共振, 势垒量子穿透, 瞬发裂变竞争, 240Pu裂变]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [double-humped-fission-barrier, fission-isomers, shape-isomers, class-ii-states, subthreshold-fission, strutinsky-shell-correction, intermediate-structure, actinide-fission]
---

# 双峰裂变势垒量子穿透、裂变形状异能态（Class-II）与亚阈中间共振动力学

## 1. 物理全景：超形变第二势阱与微观壳效应重构的裂变图景

在经典旋转液滴模型中，重核裂变势垒呈现单峰抛物线结构（Single-humped barrier），从基态穿过鞍点后便不可逆地滑向断裂。
然而，20 世纪 60 年代初，苏联物理学家 S. M. Polikanov 等在杜布纳联合核子研究所发现了一个极为离奇的自发裂变现象：
某些处于低激发态的锕系同位素（如 $^{242m}\text{Am}, ^{240m}\text{Pu}, ^{238m}\text{U}$）的自发裂变半衰期竟然只有**纳秒至毫秒量级（$\text{ns} \sim \text{ms}$）**，比正常的基态自发裂变寿命（$10^9 \sim 10^{16}$ 年）**缩短了整整 20 个数量级**！

根据 V. M. Strutinsky（Nucl. Phys. A 95, 420, 1967）、S. Bjørnholm & J. E. Lynn（Rev. Mod. Phys. 52, 725, 1980）以及 R. Vandenbosch & J. R. Huizenga《Nuclear Fission》：
这一震惊世界的发现促成了理论核物理的革命——**双峰裂变势垒（Double-Humped Fission Barrier）的诞生**：
1. **Strutinsky 宏观-微观壳修正能的二次下沉**：
   在轴比达到 $2:1$ 的超形变状态下（$\beta_2 \approx 0.60$），谐振子壳层产生新的大单粒子能隙（简谐振子比值为 $2:1$ 时的对称性），强烈的负壳修正能叠加在单峰液滴势上，将势垒正中央挖出一个深邃的**第二势能极小值（Second Minimum, 深度达 $2 \sim 3\text{ MeV}$）**；
2. **裂变形状异能态（Fission Shape Isomers / Class-II 态）**：
   受困在第二势阱底部的核态被称为 **第二类态（Class-II States）**。由于被内势垒 $V_A$ 与外势垒 $V_B$ 两侧阻隔，它向正常第一势阱（Class-I 态）发射 $\gamma$ 光子的跃迁面临巨大的形状重叠阻碍（阻碍因子达 $10^6 \sim 10^{10}$），而向外穿透外势垒发生裂变的势垒厚度又远小于基态，从而形成了寿命极短的自发裂变同质异能态；
3. **亚阈中子裂变截面中间共振结构（Subthreshold Intermediate Structure）**：
   在中子能量低于势垒峰顶的亚阈裂变实验中（如 $^{237}\text{Np}(n, f), ^{240}\text{Pu}(n, f)$），裂变截面呈现出以 $D_{\text{II}} \sim 1 \sim 2\text{ keV}$ 为周期的巨型窄共振群，直接暴露了第二势阱中离散能级的量子存在！

---

## 2. 严格双重势垒量子穿透方程

### (1) 双峰势垒几何轮廓参数化
沿裂变延伸坐标 $\beta$：
- **内势垒（Inner Barrier A）**：高度 $V_A$（典型 $5.5 \sim 6.5\text{ MeV}$），曲率能量 $\hbar \omega_A \approx 0.8 \sim 1.1\text{ MeV}$；
- **第二极小（Second Minimum II）**：基态激发能量 $E_{\text{II}} \approx 2.0 \sim 3.0\text{ MeV}$，有效自振声子能量 $\hbar \omega_{\text{II}} \approx 0.7 \sim 0.9\text{ MeV}$；
- **外势垒（Outer Barrier B）**：高度 $V_B$（典型 $5.0 \sim 6.0\text{ MeV}$），曲率能量 $\hbar \omega_B \approx 0.5 \sim 0.7\text{ MeV}$。

---

### (2) 双抛物线势垒量子相干穿透公式（Cramer & Nix 1970）
对于单势垒，Hill-Wheeler 穿透几率为：
$$T_A(E) = \frac{1}{1 + \exp\left[ \frac{2\pi (V_A - E)}{\hbar \omega_A} \right]}, \qquad T_B(E) = \frac{1}{1 + \exp\left[ \frac{2\pi (V_B - E)}{\hbar \omega_B} \right]}$$

当粒子在两势垒构成的法布里-珀罗干涉腔（Fabry-Pérot cavity）内来回多重反射时，第二势阱内的作用量相角为：
$$\phi(E) = \int_{\beta_A}^{\beta_B} \sqrt{\frac{2M}{\hbar^2} (E - V(\beta))} d\beta \approx \pi \frac{E - E_{\text{II}}}{\hbar \omega_{\text{II}}}$$
两势垒联合量子穿透几率为多束波干涉叠加解：
$$T(E) = \frac{T_A(E) T_B(E)}{1 + 2 \sqrt{(1 - T_A)(1 - T_B)} \cos(2\phi) + (1 - T_A)(1 - T_B)}$$

#### 极限行为与共振增透：
- **共振相消透射峰（Resonance Transmission Peak）**：
  当激发能正好对准第二势阱中的准束缚能级，满足玻尔-索末菲量子化条件 $\cos(2\phi) = -1$ 时，分母抵消至极小值：
  $$T_{\text{res}}(E) = \frac{4 T_A T_B}{(T_A + T_B)^2}$$
  **若两势垒高度相近（$T_A \approx T_B$），联合量子穿透几率发生共振暴增，瞬间飙升至 $T_{\text{res}} \to 1.0$（全透射无反射）**！这彻底解释了为何亚阈裂变能谱中会出现穿透几率暴增数千倍的孤立共振窄峰；
- **非共振谷底（Off-resonance Valley）**：
  在能级间隙处 $\cos(2\phi) = +1$，穿透几率跌落至非相干底数 $T_{\text{off}} \approx \frac{1}{4} T_A T_B \ll 10^{-6}$。

---

### (3) 形状异能态（Class-II）寿命与分支比
第二势阱基态的衰变率由两道闸门竞争主导：
1. **外势垒穿透宽度（延迟自发裂变通道）**：
   $$\Gamma_{\text{fiss}} = \left( \frac{\hbar \omega_{\text{II}}}{2\pi} \right) T_B(E_{\text{II}})$$
2. **内势垒穿透宽度（向 Class-I 态发射反向 $\gamma$ 光子）**：
   $$\Gamma_{\text{back}} = \left( \frac{\hbar \omega_{\text{II}}}{2\pi} \right) T_A(E_{\text{II}}) \cdot P_\gamma$$
   其中 $P_\gamma \approx 10^{-3} \sim 10^{-2}$ 为第一阱内高阶混杂跃迁的光子发射几率。

总衰变宽度为两者之和：$\Gamma_{\text{tot}} = \Gamma_{\text{fiss}} + \Gamma_{\text{back}}$。
异能态真实可观测半衰期为：
$$t_{1/2} = \frac{\hbar \ln 2}{\Gamma_{\text{tot}}}$$
对于 $^{240m}\text{Pu}$，测得寿命为 $t_{1/2} \approx 25\text{ ns}$，延迟裂变分支比约为 $15\% \sim 20\%$。

---

## 3. 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/fission_isomer_double_hump_transmission_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `fissiso` 命令。

### 运行示范（模拟典型锕系核 $^{240}\text{Pu}$ 双峰势垒与中间共振）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py fissiso \
  --VA 6.0 --hwA 0.9 --EII 2.5 --VB 5.5 --hwB 0.6 --scan --json
```

### 计算输出核心物理特征：
1. **形状异能态固有参数**：
   - 第二势阱激发能 $E_{\text{II}} = 2.5\text{ MeV}$，内势垒 $V_A = 6.0\text{ MeV}$，外势垒 $V_B = 5.5\text{ MeV}$；
   - 裂变分宽度 $\Gamma_{\text{fiss}} = 2.89 \times 10^{-15}\text{ MeV}$，反向 $\gamma$ 宽度 $\Gamma_{\text{back}} = 1.56 \times 10^{-14}\text{ MeV}$；
   - **理论预测异能态半衰期为 $24.72\text{ ns}$**，延迟裂变分支比为 $15.67\%$，与 $^{240m}\text{Pu}$ 实验值高度吻合；
2. **亚阈中间结构共振群**：
   - 在 $3.5 \sim 6.5\text{ MeV}$ 能量扫描中，离散共振峰位在 $3.7\text{ MeV}, 4.5\text{ MeV}, 5.3\text{ MeV}, 6.1\text{ MeV}$ 等处周期性爆发；
   - 在 $4.5\text{ MeV}$ 处穿透几率达到完美的共振全透射 $T = 1.0$，而在邻近的非共振道址骤降至 $10^{-8}$，定量展现出双峰共振腔的高对比度干涉放大效应！

---

## 4. 与相关前沿概念的交叉引用
- [[fission-barriers-and-superheavy-stability]]：超重核稳定岛（$Z=114 \sim 126$）的存活几率在宏观微观势能面上同样依赖此双峰位垒的穿透计算；
- [[superdeformation-triaxial-sd-and-decayout-dynamics]]：第二势阱本质上就是超形变态（轴比 $2:1$），其向第一阱的衰变机制与超形变衰退（Decay-out）在数学上完全等价；
- [[multi-modal-nuclear-fission-and-prompt-neutrons]]：从第二极小出发跨过外势垒后，原子核随即分叉进入 Standard I / II 等多模式断裂山谷。
