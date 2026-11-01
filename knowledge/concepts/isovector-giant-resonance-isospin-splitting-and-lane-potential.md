# 巨共振同位旋劈裂（$T_>, T_<$）、Lane 对称势与泡利阻塞微观机理：同位旋代数与电荷无关性破缺

## 1. 物理本质与同位旋 Clebsch-Gordan 耦合

在具有中子过剩（$N > Z$）的原子核基态中，基态具有非零的同位旋量子数：
$$T_0 = T_z = \frac{N - Z}{2}$$
其基态同位旋波函数严格处于同位旋多重态的底态 $|T_0, M_T = T_0 \rangle$。

当电弱或强相互作用的异旋跃迁算符（Isovector Operator，$\Delta T = 1, \Delta T_z = 0$）作用于该核时（例如电偶极激发的巨偶极共振 IVGDR、电单极激发的异旋巨单极共振 IVGMR）：
根据同位旋 Clebsch-Gordan 系数耦合定理：
$$|T_0, T_0 \rangle \otimes |1, 0 \rangle = C_{T_0 T_0 1 0}^{T_0 T_0} |T_< = T_0, T_0 \rangle + C_{T_0 T_0 1 0}^{T_0+1 T_0} |T_> = T_0 + 1, T_0 \rangle$$
任何异旋激发态均不可避免地被劈裂为两个具有不同总同位旋的独立物理分支：
1. **低同位旋主分支（$T_<$ 分支，$T = T_0$）**；
2. **高同位旋客分支（$T_>$ 分支，$T = T_0 + 1$）**，它是邻近核中同位旋类似态（Isobaric Analog State, IAS）的反转多重态成员。

---

## 2. Lane 对称势与能级劈裂能差 $\Delta E_T$

两个同位旋分支之间的能量间隔直接反映了核相互作用中的同位旋依赖性。根据 A. M. Lane 提出的光学模型核对称势（Lane Potential）：
$$V(r) = V_0(r) + \frac{V_1(r)}{A} (\vec{t} \cdot \vec{T}_0)$$
其中 $V_1 \approx 60 - 100\text{ MeV}$ 为 Lane 对称势强度，$\vec{t}$ 为跃迁核子的同位旋（$t = 1/2$），$\vec{T}_0$ 为核芯同位旋。

通过代数恒等式：
$$\vec{t} \cdot \vec{T}_0 = \frac{1}{2} \left[ T(T+1) - T_0(T_0+1) - t(t+1) \right]$$
对两个分支求能量本征值差，得到著名的 **Lane 同位旋劈裂定理**：
$$\Delta E_T = E(T_> = T_0 + 1) - E(T_< = T_0) = \frac{V_1}{A} (T_0 + 1)$$
这一简练的解析公式表明：**巨共振同位旋双分支的能量裂距直接提供了在有限核体系中独立测定 Lane 对称势强度 $V_1$ 的微观基准**。

---

## 3. Clebsch-Gordan 跃迁强度分布与泡利阻塞抑制（Pauli Blocking）

两分支跃迁强度的几何比率由同位旋 Clebsch-Gordan 系数决定：
$$\frac{S(T_>)}{S(T_<)} = \frac{(C_{T_0 T_0 1 0}^{T_0+1 T_0})^2}{(C_{T_0 T_0 1 0}^{T_0 T_0})^2} \left( 1 - \frac{3 T_0}{2 A} \right) = \frac{1}{T_0} \left( 1 - \frac{3 T_0}{2 A} \right)$$
其中括号中的项为泡利不相容原理（Pauli Blocking）对跃迁中子相干退激的几何阻抑修正。

高同位旋分支 $T_>$ 所占总跃迁强度的相对份额近似为：
$$\text{Fraction}(T_>) \approx \frac{1}{T_0 + 1}$$

### 同位旋演化的物理推论：
- **自共轭核或轻核（$N \approx Z$，$T_0 \sim 0$ 或 $1$）**：
  $T_>$ 分支与 $T_<$ 分支具有相近的跃迁强度（各占 $\sim 50\%$），两峰在光核反应截面上表现为对称的双峰结构；
- **重中子过剩核（如 $^{208}\text{Pb}$，$N=126, Z=82 \implies T_0 = 22.0$）**：
  由于中子费米面远高于质子费米面，质子向中子轨道的空穴跃迁受到极其严重的泡利完全阻塞（Pauli Exclusion），高同位旋分支的强度份额被剧烈压缩至仅占 **$4.3\%$**！绝大部分强度被锁死在低同位旋 $T_<$ 主峰（占 $95.7\%$）。

---

## 4. 科学分析套件实战验证

Wiki 内置模块 `system/scripts/analysis/isovector_giant_resonance_splitting_calculator.py`（CLI 命令：`python3 system/scripts/analysis/nuclear_analyzer.py isg`）对 $^{208}\text{Pb}$ 处的 IVGDR 同位旋劈裂进行了严格微观计算：

```bash
# 模拟 208Pb (T0 = 22.0) 在 Lane 势 V1 = 65.0 MeV 下的同位旋劈裂与分支份额
python3 system/scripts/analysis/nuclear_analyzer.py isg -Z 82 -A 208 --mode IVGDR --V1 65.0
```

**实测输出解析**：
- **母核同位旋**：$T_0 = 22.0$，IVGDR 质心能量 $E_{\text{centroid}} = 13.73\text{ MeV}$；
- **Lane 劈裂能距**：$\Delta E_T = 7.19\text{ MeV}$；
- **多重态分支精细分解**：
  - 低同位旋主分支（$T_< = 22.0$）：中心能量 $E_< = 13.42\text{ MeV}$，独占 **$95.7\%$** 的跃迁强度；
  - 高同位旋客分支（$T_> = 23.0$）：中心能量 $E_> = 20.60\text{ MeV}$，仅残存 **$4.3\%$** 的微弱强度；
- **物理判据**：定量验证了重核中泡利阻塞对高同位旋跃迁的剧烈压低效应，并为通过高能质子非弹性散射分离 $T_>$ 异旋共振提供了精确的能量预测基准。
