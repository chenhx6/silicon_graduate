---
type: method
title: "核激发态寿命测量全指南：DSAM、RDM活塞法与介质阻止本领反演"
aliases: [核寿命测量指南, DSAM多普勒衰减法, RDM活塞法, 介质阻止本领, 寿命线形反演]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [nuclear-lifetimes, dsam, rdm-plunger, stopping-power, srim, doppler-lineshape]
---

# 核激发态寿命测量全指南：DSAM、RDM活塞法与介质阻止本领反演

## 1. 物理测量视界与时间尺度分段

激发态寿命 $\tau$（或半衰期 $T_{1/2} = \tau \ln 2$）是直接提取核波函数内禀四极矩 $Q_t$、形变参量 $\beta_2$、减缩电磁跃迁几率 $B(E2)$ 和 $B(M1)$ 的最纯净物理可观测量。

根据吴治华《原子核物理实验方法》（第 15 章）与现代高自旋实验谱学，核态寿命横跨数十个数量级，必须针对不同时间窗口选取正交的实验技术：

```
  时间尺度 (Time Scale)          适用的实验测量技术 (Experimental Technique)
  ─────────────────────────────────────────────────────────────────────────────
  10 fs  ~  1 ps   (10^-14 ~ 10^-12 s)  --> 多普勒频移衰减法 (DSAM: Doppler Shift Attenuation)
  1 ps   ~  1 ns   (10^-12 ~ 10^-9  s)  --> 反冲距离多普勒法 (RDM / Plunger 活塞法)
  1 ns   ~  1 us   (10^-9  ~ 10^-6  s)  --> 电子学延迟符合法 (Delayed Coincidence, TAC/TDC/RF)
  > 1 us           (10^-6  s 以上)      --> 束流脉冲截断定时与活化放射性衰变测量
```

在研究三轴摆动带与手征双重带的高自旋态集体增强（$B(E2)_{\text{out}} \sim 20 \sim 100\text{ W.u.}$）时，能级寿命主要集中在 **$10\text{ fs} \sim 5\text{ ps}$ 的极短时间区间**，因此 **DSAM** 与 **RDM 活塞法**构成了检验集体进动性质的核心生命线。

---

## 2. 反冲距离多普勒法（RDM / Plunger 活塞法：$1\text{ ps} \sim 1\text{ ns}$）

### (1) 实验装置几何与物理原理
靶室由安装在超高精度压电驱动器（Piezoelectric controller）上的**自支撑薄靶箔（Thin Target）**和其后方的**重金属停阻箔（Stopper Foil, 如金或铅）**构成。
- 弹核在薄靶中发生完全熔合后，反冲核穿出薄靶，以恒定初速度 $v_0 = \beta c$（通常 $\beta \approx 1.5\% \sim 3.0\%$）在真空中自由飞行距离 $d$（微米级，通常 $5\text{ }\mu\text{m} \sim 5\text{ mm}$）；
- **飞行中衰变（In-flight component, 移位峰 $S$）**：若在飞行途中退激，受全多普勒频移：
  $$E_{\text{shifted}}(\theta) = E_0 [1 + \beta \cos\theta]$$
- **停阻后衰变（Stopped component, 未移位峰 $U$）**：若反冲核飞抵停阻箔被完全慢化停阻后再退激，其速度为零，在未移位标称能量 $E_0$ 处发射单能 $\gamma$ 射线。

### (2) 强度演化与寿命提取方程
定义飞行时间 $t = d / v_0$。未移位峰相对强度比随箔片间距 $d$ 的衰减规律为：
$$R_0(d) = \frac{I_{\text{stopped}}(d)}{I_{\text{stopped}}(d) + I_{\text{shifted}}(d)} = \exp\left( -\frac{d}{v_0 \tau} \right)$$
- **微分衰变曲线法（Differential Decay Curve Method, DDCM）**：
  现代分析普遍采用 DDCM，通过对实验测得的 $I_{\text{shifted}}(d)$ 与 $I_{\text{stopped}}(d)$ 曲线求导，消除了复杂母能级次级馈送（Side-feeding）引入的系统误差：
  $$\tau(d) = \frac{I_{\text{stopped}}(d)}{v_0 \cdot \frac{d}{dd} I_{\text{shifted}}(d)}$$

---

## 3. 多普勒频移衰减法（DSAM：$10\text{ fs} \sim 1\text{ ps}$）

### (1) 介质阻止本领（Stopping Power）微观物理
在 DSAM 实验中，采用在薄靶背面直接蒸镀厚金属衬底（厚度足以完全停阻反冲核，通常 $>10\text{ mg/cm}^2$ 的 Au, Pb 或 Ta）的“带衬靶”。
反冲核进入厚衬底后，在数皮秒（通常 $\sim 1\text{ ps}$）内通过两类基本能量损失机制迅速减速：
$$-\frac{dE}{dx} = \left( -\frac{dE}{dx} \right)_{\text{electronic}} + \left( -\frac{dE}{dx} \right)_{\text{nuclear}}$$
1. **电子阻止本领（Electronic Stopping Power, $(-dE/dx)_e$）**：
   反冲核与衬底靶原子的核外束缚电子发生非弹性散射激发电离。根据 Bethe-Bloch 与 Lindhard 理论，在低速区（$v \le v_0 = c/137$），电子阻止本领正比于速度：
   $$\left( -\frac{dE}{dx} \right)_e = k_e \cdot \sqrt{E} \propto v$$
2. **核阻止本领（Nuclear Stopping Power, $(-dE/dx)_n$）**：
   反冲核与衬底原子核发生近碰撞库仑散射。在速度极低时占主导，伴随明显的多重角散射展宽（Multiple scattering）。

现代精确分析必须调用 Ziegler SRIM-2013 程序库生成的微观阻止本领数值表，建立反冲速度随时间的精确减速函数 $v(t)$。

### (2) 多普勒线形分析（Doppler Lineshape Analysis）
若激发态寿命 $\tau$ 与减速特征时间 $\alpha$ 处于同一量级（$10\sim 500\text{ fs}$），反冲核将在减速过程中一边飞行一边发射 $\gamma$ 射线。
在探测角 $\theta$ 处观测到的发射光子能量为：
$$E_\gamma(t, \theta) = E_0 \left[ 1 + \frac{v(t)}{c} \cos\theta \right]$$
宏观能谱表现为从全移位能量向未移位能量连续延展的**不对称多普勒拖尾能谱（Lineshape）**。
利用连续衰变卷积方程对 HPGe 实验能谱进行逐通道拟合，即可反演提取出激发态能级寿命 $\tau$ 以及上游能级的慢侧馈送时间（Side-feeding time $\tau_{\text{sf}}$）。

---

## 4. 绝对减缩跃迁几率与内禀四极矩解算

当通过 DSAM 或 RDM 精确获得能级寿命 $\tau$（单位：ps）以及分支比 $b_\gamma$、混合比 $\delta$ 和总内转换系数 $\alpha_{\text{tot}}$ 后，绝对跃迁几率由标准公式解算：

$$B(E2; I \to I-2) = \frac{0.08156 \cdot b_\gamma}{\tau(\text{ps}) \cdot E_\gamma^5(\text{MeV}) \cdot (1 + \alpha_{\text{tot}})}\text{ (e}^2\text{b}^2\text{)}$$
$$B(M1; I \to I-1) = \frac{0.05679 \cdot b_\gamma}{\tau(\text{ps}) \cdot E_\gamma^3(\text{MeV}) \cdot (1 + \alpha_{\text{tot}})} \cdot \frac{1}{1 + \delta^2}\text{ (}\mu_N^2\text{)}$$

在转动带内部，内禀四极矩 $Q_t$ 由轴对称或三轴转动投影公式给出：
$$B(E2; I \to I-2) = \frac{5}{16\pi} e^2 Q_t^2 \cdot (C_{I K 2 0}^{I-2, K})^2$$
由此解出的 $Q_t$ 直接决定了原子核的真实宏观四极形变 $\beta_2 \approx \frac{\sqrt{5\pi}}{3 Z R_0^2} Q_t$，完成了从在束微观能谱测量到原子核几何形貌的终极闭环！
