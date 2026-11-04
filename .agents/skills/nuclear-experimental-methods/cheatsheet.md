# Cheatsheet: 实验核物理与探测方法速查卡

实验常用物理常数、靶衬底材料参数、活时间公式与在束谱学机时预算速查。

---

## 1. 探测器物理基准参数卡

| 探测器类型 | 有效电离能 $\epsilon$ | Fano 因子 $F$ | 典型能量分辨率 ($\text{FWHM}$) | 典型时间分辨率 ($\text{FWHM}$) |
|---|---|---|---|---|
| **HPGe (高纯锗, 77 K)** | $2.96\text{ eV}$ | $0.08 - 0.12$ | $1.8 - 2.2\text{ keV}$ @ $1.33\text{ MeV}$ | $5 - 10\text{ ns}$ (同轴); $2 - 4\text{ ns}$ (平面) |
| **Si (硅表面垒/微条, 300 K)** | $3.62\text{ eV}$ | $0.11$ | $15 - 25\text{ keV}$ @ $5.5\text{ MeV}\ \alpha$ | $1 - 2\text{ ns}$ |
| **$\text{LaBr}_3\text{(Ce)}$ 闪烁体** | 光产额 $\sim 63\text{ ph/keV}$ | - | $2.8 - 3.2\%$ @ $662\text{ keV}$ | **$120 - 200\text{ ps}$** (极快) |
| **$\text{BGO}$ 反符合屏蔽套** | 光产额 $\sim 8\text{ ph/keV}$ | - | $10 - 15\%$ @ $662\text{ keV}$ | $10 - 20\text{ ns}$ (高光电截面 $\propto Z^5$) |

---

## 2. 常用靶材料与高 $Z$ 停阻衬底物理常数

| 材料 | 原子序数 $Z$ | 原子量 $A$ | 密度 $\rho\ (\text{g/cm}^3)$ | 熔点 ($^\circ\text{C}$) | 在束谱学应用角色 |
|---|---|---|---|---|---|
| **Au (金)** | 79 | 196.97 | 19.32 | 1064 | **标准厚衬底 (Backer)**：高阻止截面、晶格高度对称无磁矩，反冲核 $\sim 1\text{ ps}$ 阻停且无真空退取向 |
| **Pb (铅)** | 82 | 207.20 | 11.34 | 327 | 备选衬底（熔点低，强束流易烧损，需注意水冷） |
| **Ta (钽)** | 73 | 180.95 | 16.65 | 3017 | 超高熔点耐辐照衬底，用于高功率大束流在束实验 |
| **$^{12}\text{C}$ (天然碳箔)** | 6 | 12.01 | 2.26 | 3500 | 超薄自支撑衬底（$10 - 50\ \mu\text{g/cm}^2$），用于微小角散射与飞行核测量 |

---

## 3. 统计死时间与活时间计算公式

- **不可扩展型（非麻痹型）**：
  $$m = \frac{n}{1 - n \tau_N}, \quad f_{\text{live}} = 1 - n \tau_N.$$
- **可扩展型（麻痹型）**：
  $$n = m e^{-m \tau_P}, \quad f_{\text{live}} = e^{-m \tau_P}.$$
- **双源法测量死时间 $\tau$**：
  $$\tau \approx \frac{n_1 + n_2 - n_{12} - n_b}{n_{12}^2 - n_1^2 - n_2^2} \approx \frac{n_1 + n_2 - n_{12}}{2 n_1 n_2}.$$
- **在线脉冲发生器（Pulser）绝对活时间校正**：
  $$N_{\text{corr}} = \frac{N_{\text{meas}}}{f_{\text{live}}} = N_{\text{meas}} \cdot \frac{f_{\text{pulser}} \cdot T_{\text{real}}}{N_{\text{pulser,meas}}}.$$

---

## 4. 重离子在束反应实验机时预算通用速算表

1. **靶面原子密度 $N_t$**：
   $$N_t\ [\text{atoms/cm}^2] = \frac{d\ [\text{mg/cm}^2] \times 10^{-3}}{M_{\text{target}}\ [\text{g/mol}]} \times 6.022 \times 10^{23}.$$
2. **入射粒子流强 $I_p$**：
   $$I_p\ [\text{ions/s}] = \frac{I\ [\text{pnA}] \times 10^{-9}}{1.602 \times 10^{-19}} = I\ [\text{pnA}] \times 6.242 \times 10^9.$$
3. **目标核产生率 $R_{\text{prod}}$**：
   $$R_{\text{prod}}\ [\text{nuclei/s}] = I_p \cdot N_t \cdot \sigma\ [\text{cm}^2] = I_p \cdot N_t \cdot (\sigma\ [\text{mb}] \times 10^{-27}).$$
4. **有效二重 $\gamma-\gamma$ 符合率 $R_{\gamma\gamma}$**：
   $$R_{\gamma\gamma} \approx R_{\text{prod}} \cdot \langle M_\gamma \rangle (\langle M_\gamma \rangle - 1) \cdot \frac{\epsilon_{\text{tot}}^2}{2}.$$
5. **纯物理曝光机时 $T_{\text{beam}}$**：
   $$T_{\text{beam}}\ [\text{hours}] = \frac{N_{\text{events}}^{\text{req}}}{R_{\gamma\gamma} \times 3600}.$$
6. **总申请机时（含调束、刻度、死时间）**：
   $$T_{\text{total}} \a1.8 \times T_{\text{beam}}.$$
