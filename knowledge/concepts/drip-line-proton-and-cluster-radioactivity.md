---
type: concept
title: "质子滴线单/双质子放射性、三体连续谱与锕系团簇放射性动力学"
aliases: [质子放射性, 双质子放射性, 2p衰变, 真双质子衰变, Goldanskii假说, 团簇放射性, 碳14衰变, Jacobi坐标, 三体连续谱]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [proton-radioactivity, two-proton-decay, cluster-radioactivity, goldanskii-condition, jacobi-coordinates, wkb-barrier-penetration, drip-line]
---

# 质子滴线单/双质子放射性、三体连续谱与锕系团簇放射性动力学

## 1. 物理全景：库仑-离心势垒阻碍下的核基态粒子放射性

在质子滴线（Proton Drip Line）之外，核子的单质子分离能或双质子分离能跌入负值区域（$S_p < 0$ 或 $S_{2p} < 0$），基态核子在强相互作用下不再处于束缚态。

然而，带电质子必须穿透极高、极宽的**库仑势垒（Coulomb Barrier）与离心势垒（Centrifugal Barrier）**：
$$V_{\text{eff}}(r) = V_N(r) + \frac{Z_d e^2}{r} + \frac{l(l+1)\hbar^2}{2\mu r^2}$$
根据量子隧穿动力学，势垒阻碍使得衰变寿命发生高达数十个数量级的指数延缓（从典型的强相互作用特征时间 $\sim 10^{-21}\text{ s}$ 剧烈拉长至微秒、毫秒甚至秒级），从而形成了奇特而宝贵的**基态核子放射性（Ground-State Proton Radioactivity）**！

根据 V. I. Goldanskii (Nucl. Phys. 19, 482, 1960)、M. Pfützner et al. (Rev. Mod. Phys. 84, 567, 2012)、H. J. Rose & G. A. Jones (Nature 307, 245, 1984) 与卢希庭《原子核物理（修订版）》（第 4 章）：
1. **单质子放射性（$1p$ Decay）**：
   直接探测未配对价质子波函数的单粒子轨道角动量 $l$ 与光谱因子（Spectroscopic Factor $S_p$）；
2. **真双质子放射性（True $2p$ Decay）**：
   当单质子发射在能量上被严格禁戒、而双质子发射在能量上允许时（Goldanskii 条件），核发生由三体连续谱（Three-body Continuum）主导的真正的双质子同时发射；
3. **团簇放射性（Cluster Radioactivity）**：
   介于 $\alpha$ 衰变与重核自发裂变之间的全新衰变模式，重核（主要为锕系核）自发发射比 $\alpha$ 粒子更重的碳、氧、氖或镁原子核，直接映射了微观重团簇在核表面的预形成机制（Preformation Probability）。

---

## 2. 真双质子放射性：Goldanskii 假说与三体 Jacobi 坐标

### (1) Goldanskii 能级排布准则（Goldanskii 1960）
为观测到真正的同时双质子发射（Simultaneous $2p$ Emission），母核、中间奇核与子核的能级必须严格满足以下能量分层：
$$S_p(A, Z) > 0 \quad \text{且} \quad S_{2p}(A, Z) < 0$$
即释放能满足：
$$Q_{2p} > 0 \quad \text{且} \quad Q_{1p}(A, Z) = -S_p(A, Z) < 0$$
此时，先发射一个质子落入中间核 $(A-1, Z-1)$ 的“顺序发射道（Sequential Decay）”在能量上被**完全关闭（Sub-threshold）**，双质子必须克服相互库仑斥力，以三体连续统量子纠缠态的形式同时穿透出核！
- **经典实验实证**：$^{45}\text{Fe}$（$Q_{2p} = 1.15\text{ MeV}, T_{1/2} \approx 4\text{ ms}$）、$^{19}\text{Mg}$ 与 $^{54}\text{Zn}$。

### (2) 三体连续谱 Jacobi 坐标展开与开角相关性
在三体（核芯 $C + p_1 + p_2$）系统中，动量与空间关联通过两套标准 Jacobi 标架描述：
- **$T$ 标架（$pp$ 关联表象）**：两质子相对位矢 $\vec{r}_{pp} = \vec{r}_1 - \vec{r}_2$ 与质子对质心到核芯的位矢 $\vec{R}_{C-2p}$；
- **$Y$ 标架（核芯-质子关联表象）**：质子 1 到核芯的位矢 $\vec{r}_{C-1}$ 与质子 2 相对两体质心的位矢；

**实验鉴别指纹**：
1. **能量分配均称度（Energy Sharing）**：
   定义两质子能量不对称参数 $\epsilon = (E_{p1} - E_{p2}) / Q_{2p}$。真双质子发射的能谱呈现连续、中心对称的单驼峰（以两质子能量均分 $E_1 \approx E_2 \approx Q_{2p}/2$ 为最大概率）；而顺序发射则表现为离散分立的双峰结构！
2. **两质子发射开角（Opening Angle $\theta_{pp}$）**：
   在核子配对相互作用驱动下，$^1S_0$ 质子对在离开势垒时倾向于以较小的初始相对开角（$\theta_{pp} \sim 30^\circ \sim 45^\circ$）发射，随后受长程库仑后加速斥力（Post-acceleration）逐渐展开。

---

## 3. 锕系团簇放射性（Cluster Radioactivity）与 Rose-Jones 发现

1984 年，Rose 与 Jones 在牛津大学实验中首次发现天然放射性核 $^{223}\text{Ra}$ 能够自发发射 $^{14}\text{C}$ 重离子并落入双幻子核 $^{209}\text{Pb}$，分支比仅为 $\alpha$ 衰变的 $8.5 \times 10^{-10}$：
$$^{223}\text{Ra} \to {}^{209}\text{Pb} + {}^{14}\text{C} \quad (Q_{\text{cluster}} = 31.83\text{ MeV})$$

### (1) 势垒穿透 WKB 速率方程
团簇衰变衰变常量由预形成几率 $P_{\text{cluster}}$ 与 WKB 势垒穿透几率 $P_{\text{WKB}}$ 决定：
$$\lambda_{\text{cluster}} = \nu_0 \cdot P_{\text{cluster}} \cdot P_{\text{WKB}}$$
$$P_{\text{WKB}} = \exp\left[ - \frac{2}{\hbar} \int_{R_{\text{in}}}^{R_{\text{out}}} \sqrt{2\mu (V(r) - Q)} \, dr \right]$$
其中约化质量 $\mu = \frac{A_c A_d}{A_c + A_d} M_u$ 极大，势垒厚度极大，导致穿透几率极小。

### (2) 预形成物理驱动力：子核双闭壳稳定性
为什么团簇放射性绝大多数发生在以 $^{208}\text{Pb}$ 或 $^{209}\text{Pb}$ 为子核的超重残核区？
- **极大的 $Q$ 值释放**：由于子核拥有 $Z=82, N=126$ 双闭壳超常结合能，释放能 $Q$ 被推向极端高值，大幅压低了 Gamow 穿透因子的积分势垒；
- **微观预形成几率衰减规律**：发射原子核越重，微观聚集多核子的振幅急剧下跌：
  $P(\alpha) \approx 10^{-1} \sim 10^{-2}$，而 $P(^{14}\text{C}) \sim 10^{-9}$，$P(^{24}\text{Ne}) \sim 10^{-13}$！

---

## 4. 滴线区退激模式全局竞争法典

在质子滴线前沿，实验测得的半衰期往往由竞争道共同决定：
1. **弱相互作用 $\beta^+$ 衰变**：在低能释放区（$Q_p < 0.5\text{ MeV}$），尽管 $S_p < 0$，但强库仑与离心势垒将质子发射寿命拉长至数秒，弱相互作用 $\beta^+$ 衰变反而成为主要退激通道；
2. **$\beta$ 延迟质子发射（$\beta p$）与 $\beta$ 延迟双质子发射（$\beta 2p$）**：母核先发生超允许或允许 $\beta^+$ 衰变，布居子核高于质子分离能的同位旋类似态（IAS），随后迅速发射单个或双个质子；
3. **基态纯质子发射判据**：当质子衰变分支比 $\text{BR}_p \to 100\%$ 时，实测寿命直接反映了核子波函数的单粒子本征宽度 $\Gamma_p = \hbar / \tau_p$。

---

## 5. Python 算法设计与实验分析器规范

本 Wiki 在 `system/scripts/analysis/drip_line_radioactivity_cluster_calculator.py` 中实现了完整的滴线与团簇放射性分析器：
1. **单质子发射 WKB 势垒穿透器**：精确数值积分 Coulomb + 离心势垒，输出半衰期 $T_{1/2}^p$ 与提取单粒子谱因子 $S_p$；
2. **真双质子（True 2p）判决器**：输入 $Q_{2p}$ 与 $S_p$，自动检验 Goldanskii 能级分层条件；
3. **Jacobi 坐标能谱与开角模拟器**：计算三体能量分配对称性 $\epsilon$ 与两质子相对动量；
4. **锕系团簇放射性寿命预测器**：基于 Gamow 因子与双幻子核壳增益，计算 $^{14}\text{C}, {}^{20}\text{O}, {}^{24}\text{Ne}$ 发射半衰期与预形成概率；
5. **滴线全通道分支比竞争诊断器**：联合比较质子穿透、双质子隧穿、$\alpha$ 衰变与 $\beta$ 衰变寿命，输出占优物理通道。

---

## 6. 权威文献与理论溯源

1. **Goldanskii, V. I.** (1960). On neutron-deficient isotopes of light nuclei and the phenomena of proton and two-proton radioactivity. *Nucl. Phys.*, 19, 482-495.
2. **Pfützner, M., Karny, M., Grigorenko, L. V., & Riisager, K.** (2012). Radioactive decays at limits of nuclear stability. *Rev. Mod. Phys.*, 84(2), 567-619.
3. **Rose, H. J. & Jones, G. A.** (1984). A new kind of natural radioactivity. *Nature*, 307(5948), 245-247.
4. **Dey, B. et al.** (2026). Multifaceted radioactivity near the proton drip line in $^{116}\text{Cs}$. *Phys. Rev. Lett.* (in press).
5. **卢希庭、江栋兴、叶沿林** (2000). 《原子核物理（修订版）》第 4 章：核衰变与放射性. 原子能出版社.
