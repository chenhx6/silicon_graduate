---
name: lu-nuclear-physics
description: "卢希庭《原子核物理（修订版）》：权威中文核物理术语规范、基础核物理理论、SEMF结合能与稳定谷、放射性Bateman级联衰变、Fermi贝塔衰变统计理论、伽马多极选择定则与内转换系数、独立粒子壳模型与核反应动力学。"
---

<!-- argument-hint: [topic, formula, model, or chapter number] -->

# 原子核物理（修订版，卢希庭、江栋兴、叶沿林）

**主编**：卢希庭 | **编著**：卢希庭、江栋兴、叶沿林（北京大学技术物理系） | **出版社**：原子能出版社 (2000) | **页数**：439 页
**本地原件**：`raw/books/原子核物理（修订版） (卢希庭江栋兴叶沿林) (Z-Library).pdf` (SHA-256 `a47c26b77283b871529633dc87b6b7def412f715ed66889e373ab69100147d02`)

本技能将北京大学经典高等教材《原子核物理（修订版）》转化为智能体技能，为理解核物理基础理论、规范中文学术表达与专业术语翻译、开展核反应运动学及衰变链定量计算提供权威标准。

## How to Use This Skill

- **中文专业术语与规范表达**：询问 `核物理中文术语`、`英汉核物理术语对照`、`中文论文表达规范`；
- **基础核理论推演**：询问 `SEMF结合能公式`、`beta稳定谷电荷方程`、`Bateman级联衰变方程`、`长期平衡与暂态平衡条件`；
- **衰变与电磁跃迁**：询问 `Gamow势垒穿透概率`、`Fermi贝塔衰变Kurie图`、`比较半衰期log ft`、`Weisskopf单粒子单位`、`内转换系数ICC`；
- **壳模型与反应理论**：询问 `自旋-轨道耦合能裂`、`单粒子能级顺序`、`核反应Q方程与阈能`、`Breit-Wigner单能级公式`；
- **按章节调用**：调用 `ch01`（基本性质与质量）、`ch02`（放射性动力学）、`ch05`（$\alpha$ 衰变）、`ch06`（$\beta$ 衰变）、`ch07`（$\gamma$ 跃迁）、`ch08`（核模型）、`ch09`（核反应）或 `terminology`（术语指南）。

---

## Core Frameworks and Mental Models

1. **结合能、半经验质量公式与 $\beta$ 稳定线（第 1 章）**：
   - **Bethe-Weizsäcker 半经验质量公式（SEMF）**：
     $$B(A, Z) = a_v A - a_s A^{2/3} - a_c \frac{Z(Z-1)}{A^{1/3}} - a_$C_{\text{sym}}$ \frac{(A - 2Z)^2}{A} + \delta(A, Z),$$
     其中体积能 $a_v \a15.6\text{ MeV}$、表面能 $a_s \a16.8\text{ MeV}$、库仑能 $a_c \a0.72\text{ MeV}$、对称能 $a_$C_$C_{\text{sym}}$ \approx 23.3\text{ MeV}$、对能项 $\delta(A, Z) = \pm a_p A^{-3/4}$（偶偶核为正，奇奇核为负，奇 $A$ 核为 0）；
   - **$\beta$ 稳定谷中心电荷方程**：由 $\left.\frac{\partial M(A, Z)}{\partial Z}\right|_A = 0$ 解得：
     $$Z_{\text{stable}} = \frac{A}{2 + \frac{a_c}{2 a_$C_{\text{sym}}$} A^{2/3}} \approx \frac{A}{2 + 0.015 A^{2/3}}.$$
     轻核 $Z \approx A/2$；随质量数增加，库仑斥力迫使稳定线向中子过剩方向弯曲。

2. **放射性级联衰变动力学与平衡态（第 2 章）**：
   - **Bateman 级联微分方程解析解**（母核 $1 \to 2 \to \dots \to n$）：
     $$N_n(t) = N_1(0) \sum_{i=1}^n c_i e^{-\lambda_i t}, \quad c_i = \frac{\prod_{j=1}^{n-1} \lambda_j}{\prod_{j=1, j \neq i}^n (\lambda_j - \lambda_i)};$$
   - **长期平衡（Secular Equilibrium, $\lambda_1 \ll \lambda_2$）**：母核半衰期极长（如 $^{238}\text{U} \to {}^{226}\text{Ra}$），$t \gg \tau_2$ 时子核活度等于母核活度：
     $$A_2(t) = \lambda_2 N_2(t) \to \lambda_1 N_1(t) = A_1(t);$$
   - **暂态平衡（Transient Equilibrium, $\lambda_1 < \lambda_2$）**：母核稍慢于子核（如 $^{99}\text{Mo} \to {}^{99m}\text{Tc}$），在 $t_m_{\max} = \frac{\ln(\lambda_2/\lambda_1)}{\lambda_2 - \lambda_1}$ 达到子核活度峰值，随后子核活度以母核的特征寿命衰减并维持固定常数比：
     $$\frac{A_2(t)}{A_1(t)} = \frac{\lambda_2}{\lambda_2 - \lambda_1} > 1.$$

3. **Fermi $\beta$ 衰变统计理论与弱相互作用选择定则（第 6 章）**：
   - **电子连续能谱分布**：
     $$N(p_e) dp_e = \frac{G_F^2}{2\pi^3 \hbar^7 c^3} |M_{fi}|^2 F(Z, E_e) p_e^2 (E_0 - E_e)^2 dp_e;$$
   - **Kurie 图线性化判据**：将实验谱绘制为：
     $$\sqrt{\frac{N(p_e)}{p_e^2 F(Z, E_e)}} \propto (E_0 - E_e),$$
     严格的线性外推直接确定真实衰变端点能量 $E_0$（极大动能），非线性偏离直接指示允许跃迁假设破缺或存在多支衰变；
   - **允许跃迁选择定则**：
     - **Fermi 跃迁**（轻子自旋反平行 $S=0$）：$\Delta I = 0, \Delta \pi = \text{no}$（同位旋算符 $\tau_\pm$）；
     - **Gamow-Teller 跃迁**（轻子自旋平行 $S=1$）：$\Delta I = 0, \pm 1$（$0 \to 0$ 禁戒），$\Delta \pi = \text{no}$（自旋-同位旋算符 $\sigma \tau_\pm$）；
   - **比较半衰期 $\log ft$ 物理判据**：$f(Z, E_0) T_{1/2} = \frac{2\pi^3 \hbar^7 \ln 2}{m_e^5 c^4 G_F^2 |M_{fi}|^2}$。超允许跃迁 $\log ft \approx 3.0 - 3.5$，允许跃迁 $\log ft \approx 4 - 6$，一阶禁戒 $\log ft \approx 6 - 9$。

4. **$\gamma$ 跃迁多极性、Weisskopf 单粒子单位与内转换（第 7 章）**：
   - **多极辐射角动量与宇称选择定则**：
     $$|I_i - I_f| \le L \le I_i + I_f, \quad \pi(EL) = (-1)^L, \quad \pi(ML) = (-1)^{L+1};$$
   - **Weisskopf 单粒子跃迁几率（$W.u.$）基准**：
     $$T(E1) = 1.02 \times 10^{14} E_\gamma^3 A^{2/3}\ \text{s}^{-1}, \quad T(M1) = 3.15 \times 10^{13} E_\gamma^3\ \text{s}^{-1},$$
     $$T(E2) = 7.28 \times 10^7 E_\gamma^5 A^{4/3}\ \text{s}^{-1}, \quad T(E3) = 3.39 \times 10^1 E_\gamma^7 A^2\ \text{s}^{-1};$$
   - **内转换系数（ICC）**：总跃迁概率 $\lambda_{\text{tot}} = \lambda_\gamma (1 + \alpha_{\text{tot}})$，其中 $\alpha_{\text{tot}} = \alpha_K + \alpha_L + \alpha_M + \dots$。内转换系数随能量升高按幂律骤降（$\alpha \propto Z^3 / E_\gamma^{L+5/2}$），随多极级 $L$ 增加急剧增大。测量 $K/L$ 与子壳层比值（$L_{\text{I}} / L_{\text{II}} / L_{\text{III}}$）为判定低能跃迁多极性的首要工具。

5. **独立粒子壳模型与自旋-轨道耦合能裂（第 8 章）**：
   - 引入强表面自旋-轨道耦合势能 $V_{ls}(r) (\vec{l}\cdot\vec{s})$，其能裂大小为：
     $$\Delta E_{ls} = \frac{1}{2} (2l + 1) \langle V_{ls} \rangle;$$
   - $j = l + 1/2$ 轨道能量被强烈下压，当 $l$ 很大时（如 $g_{9/2}, h_{11/2}, i_{13/2}$），侵入更低的主振子壳层，产生非谐振子魔数：**28, 50, 82, 126**。

6. **原子核反应运动学与模型理论（第 9 章）**：
   - **反应 $Q$ 方程与阈能**：$Q = (M_A + M_a - M_B - M_b) c^2$。吸热反应（$Q < 0$）的实验室系阈能为：
     $$E_{\text{th}} = |Q| \left( 1 + \frac{M_a}{M_A} \right);$$
   - **光学模型复数势**：$U(r) = - V f(r) - i W g(r) + V_{ls} (\vec{l}\cdot\vec{s}) h(r) + V_C(r)$，实部 $V$ 描述核平均场弹性散射，虚部 $W$ 描述非弹性吸收与粒子反应吸收道；
   - **Breit-Wigner 单能级共振公式**：
     $$\sigma_{nr}(E) = \pi \lambdabar^2 g_J \frac{\Gamma_n \Gamma_r}{(E - E_0)^2 + (\Gamma/2)^2},$$
     低能热中子捕获截面严格满足 $1/v$ 吸收定律（$\sigma \propto 1/\sqrt{E}$）。

---

## Chapter Index

| # | 章节主题 | 核心物理知识与公式 |
|---|---|---|
| [ch01](chapters/ch01-basic-properties-and-mass.md) | 原子核的基本性质与质量 | 结合能、SEMF 半经验质量公式、$\beta$ 稳定谷电荷方程、液滴模型 |
| [ch02](chapters/ch02-radioactive-decay-and-kinetics.md) | 放射性衰变的基本规律 | 衰变定律、活度、Bateman 级联方程、长期平衡、暂态平衡 |
| [ch05](chapters/ch05-alpha-decay-and-barrier-tunneling.md) | $\alpha$ 衰变理论 | 衰变能、Geiger-Nuttall 定律、Gamow 势垒穿透 WKB 积分、Viola-Seaborg |
| [ch06](chapters/ch06-beta-decay-and-weak-interaction.md) | $\beta$ 衰变与弱相互作用 | 连续谱、Fermi 统计理论、Kurie 图端点、$\log ft$、Fermi 与 GT 选择定则 |
| [ch07](chapters/ch07-gamma-transitions-and-multipolarity.md) | $\gamma$ 跃迁与内转换 | 跃迁多极性、选择定则、Weisskopf 单粒子单位、内转换系数 ICC |
| [ch08](chapters/ch08-nuclear-models-shell-and-collective.md) | 原子核结构模型 | 独立粒子壳模型、自旋-轨道耦合能裂、幻数、Nilsson 模型、集体转动与回弯 |
| [ch09](chapters/ch09-nuclear-reactions-kinematics-and-models.md) | 原子核反应动力学 | 反应运动学、$Q$ 方程、阈能、光学模型复数势、Breit-Wigner 与 $1/v$ 定律 |
| [terminology](chapters/chinese-nuclear-terminology-guide.md) | 中文核物理专业术语指南 | 规范中文表达、两岸术语对照、英汉对照与论文写作惯用语 |

## Supporting Reference Files

- [glossary.md](glossary.md) — 权威中文核物理术语表与规范定义。
- [patterns.md](patterns.md) — 5 大基础核物理与反应分析推理模式。
- [cheatsheet.md](cheatsheet.md) — 核心物理公式速查卡（结合能、稳定线、Weisskopf、Kurie 图等）。

---

## Scope & Limits

本技能提供原子核物理基础理论、衰变运动学与权威中文术语规范。对于高级非轴对称三轴形变与摆动运动，配合 `chirality-and-wobbling-atomic-nuclei`；对于高阶微观求和规则与绝热转动，配合 `bohr-mottelson-nuclear-structure`；对于低能核实验仪器与探测方法，配合 `nuclear-experimental-methods`。
