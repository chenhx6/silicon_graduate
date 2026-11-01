---
type: method
title: "重离子核反应激发函数、靶内阻止积分与截面反演实战指南"
aliases: [激发函数分析指南, 反应截面反演, 靶内能量损失积分, 熔合蒸发产额计算, 束流靶厚优化]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [excitation-functions, cross-section-extraction, energy-loss, stopping-power, fusion-evaporation, beam-time-estimation]
---

# 重离子核反应激发函数、靶内阻止积分与截面反演实战指南

## 1. 物理测量视界：从宏观束流计数到微观反应截面

在低能重离子在束核物理实验中，目标核（如 $^{131}\text{Ce}$ 或 $^{133}\text{Ce}$）的布居几率强烈依赖于入射束流能量。
描述特定出射反应道（如 $3n, 4n, 5n$ 蒸发道）的生成截面随入射能量或复合核激发能演化的关系曲线，称为**激发函数（Excitation Function）**。

根据林承键《重离子核反应》（第 6 章）与吴治华《原子核物理实验方法》（第 13 章），加速器送出的单能束流在穿过有限厚度的物理靶箔时，会由于与靶原子的电离碰撞发生连续减速。实验上测得的特征 $\gamma$ 射线产额是反应截面在靶内能量展宽区间上的**厚靶加权积分**。

---

## 2. 核心数学积分方程与阻止本领修正

### (1) 产额-截面积分基本方程
设入射束流粒子数为 $N_p$，在实验室系入射能量为 $E_{\text{in}}$；靶核质量数为 $A_t$，靶面密度为 $\rho \Delta x$（单位：$\text{mg/cm}^2$）。
束流在靶内的出射能量降为 $E_{\text{out}} = E_{\text{in}} - \Delta E$。
实验测得的特定反应残核某条特征级联 $\gamma$ 射线的全能峰净面积 $N_\gamma$ 为：
$$N_\gamma = N_p \cdot \frac{N_A}{A_t \times 10^{-3}} \cdot \epsilon(E_\gamma) \cdot b_\gamma \int_{E_{\text{out}}}^{E_{\text{in}}} \frac{\sigma(E)}{S(E)} dE$$
其中：
- $N_A = 6.022 \times 10^{23}\text{ mol}^{-1}$ 为阿伏伽德罗常数；
- $\epsilon(E_\gamma)$ 为探测器阵列在该能量处的全能峰总效率；
- $b_\gamma$ 为该能级向下的光子发射分支比；
- $S(E) = -\frac{dE}{d(\rho x)}$ 为入射重离子在靶介质中的质量阻止本领（单位：$\text{MeV} \cdot \text{cm}^2/\text{mg}$）。

### (2) 薄靶近似（Thin Target Approximation）
在常规高自旋在束 $\gamma$ 谱学中，为了严格控制由于靶内减速带来的反冲速度发散与多普勒展宽，通常采用**自支撑薄靶（$\rho \Delta x \approx 0.5 \sim 1.5\text{ mg/cm}^2$）**。
此时靶内能量损失较小（$\Delta E \ll E_{\text{in}}$，通常 $\Delta E \approx 3 \sim 8\text{ MeV}$），截面 $\sigma(E)$ 在区间内可近似为常数，取在平均有效能量处：
$$E_{\text{eff}} = E_{\text{in}} - \frac{\Delta E}{2}$$
积分方程退化为代数乘积：
$$N_\gamma \approx N_p \cdot \left[ \frac{\rho \Delta x \cdot N_A}{A_t \times 10^{-3}} \right] \cdot \epsilon(E_\gamma) \cdot b_\gamma \cdot \sigma(E_{\text{eff}})$$

由此导出从实验实测计数直接提取微观绝对截面的核心反演公式：
$$\sigma(E_{\text{eff}}) = \frac{N_\gamma}{N_p \cdot N_{\text{target}} \cdot \epsilon(E_\gamma) \cdot b_\gamma} \times 10^{27}\text{ (mb)}$$

---

## 3. 束流流强积分与法拉第杯电荷换算

在加速器运行中，束流流强通常由法拉第杯（Faraday Cup）以电荷流形式测量（单位：粒子纳安 $\text{pnA}$ 或电荷微库仑 $\mu\text{C}$）。
设束流离子电荷态为 $q$（例如 $^{36}\text{S}^{10+}$，则 $q = 10$）：
1. **若记录的是粒子流强 $I_p$（$\text{pnA}$）与辐照时间 $t$（小时）**：
   $$N_p = \frac{I_p \times 10^{-9}\text{ A}}{1.602 \times 10^{-19}\text{ C}} \times (t \times 3600\text{ s}) = 2.247 \times 10^{13} \cdot I_p(\text{pnA}) \cdot t(\text{h})$$
2. **若记录的是法拉第杯积分总电荷 $Q_{\text{tot}}$（微库仑 $\mu\text{C}$）**：
   $$N_p = \frac{Q_{\text{tot}} \times 10^{-6}\text{ C}}{q \times 1.602 \times 10^{-19}\text{ C}} = \frac{6.242 \times 10^{12} \cdot Q_{\text{tot}}(\mu\text{C})}{q}$$

---

## 4. 激发函数拟合模型与最佳束流能量确定

在熔合蒸发反应中，$xn$ 反应道的微观截面随复合核激发能 $E^*$ 的演化呈现典型的非对称钟形曲线：

### 非对称共振参数化模型（Asymmetric Gaussian Model）：
$$\sigma_{xn}(E) = \sigma_{\max} \cdot \exp\left[ -\frac{(E - E_{\text{opt}})^2}{2 \Gamma^2(E)} \right]$$
其中宽度随能量发生轻微非对称展宽：
$$\Gamma(E) = \begin{cases} \Gamma_{\text{low}}, & E < E_{\text{opt}} \quad (\text{受库仑势垒穿透与中子分离能截断}) \\ \Gamma_{\text{high}}, & E \ge E_{\text{opt}} \quad (\text{受下一个蒸发道竞争与中子动能分布展宽}) \end{cases}$$

**实战应用**：
通过在 3–5 个不同能量点测量产额并拟合该模型，即可精确提取：
1. 最佳反应束流能量 $E_{\text{opt}}$；
2. 峰值最大产生截面 $\sigma_{\max}$；
3. 相邻蒸发道（如 $4n$ 杂质道对 $5n$ 目标道）的交叉污染比例，为离线谱学设定纯净选门提供坚实的反应动力学依据。
