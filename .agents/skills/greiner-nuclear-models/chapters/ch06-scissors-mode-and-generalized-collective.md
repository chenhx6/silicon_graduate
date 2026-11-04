# 第 6 章 (四)：广义集体模型与质中剪刀振动模式 (Scissors Mode)

**来源专著**：Walter Greiner & Joachim A. Maruhn《Nuclear Models》（Springer 1996）第 6 章 §6.7
**对应页码**：印刷 pp. 170–178 / 物理 PDF pp. 189–197，式 (6.229)–(6.255)

---

## 1. 核心理论推导与广义集体模型 (GCM)

### 1.1 法兰克福广义集体模型 (Frankfurt GCM)
为了克服纯刚性转子或纯谐振子模型的片面性，Greiner 等人提出了广义集体模型：
势能面采用表面四极张量不变量多项式展开：
$$V(\beta, \gamma) = C_{20} \beta^2 + C_{30} \beta^3 \cos(3\gamma) + C_{40} \beta^4 + C_{50} \beta^5 \cos(3\gamma) + C_{60} \beta^6 + D_{60} \beta^6 \cos^2(3\gamma),$$
其中只有两个旋转不变量参量：$I_2 = \beta^2$ 与 $I_3 = \beta^3 \cos(3\gamma)$。
- 通过微调唯象系数，GCM 可以平滑自洽描述球形振动核、轴对称长椭转子、扁椭转子、三轴刚性转子乃至大振幅形状共存与临界相变点。

---

## 2. 质中双转子剪刀振动模式 (Two-Rotor Scissors Mode)

### 2.1 物理几何图像与同位旋相对摆动
N. Lo Iudice 与 F. Palumbo (1978) 提出、Darmstadt 电子散射实验（Bohle 等，1984）确证的剪刀振动模式，是核物理集体电磁激发的重大发现。
- **双流体两转子几何**：
  将原子核看作由具有长椭四极形变 $\delta$ 的质子流体球（转动惯量 $\mathcal{J}_p$）与中子流体球（转动惯量 $\mathcal{J}_n$）构成的系统；
  两者的主对称轴彼此相对倾斜一个微小剪刀角 $\theta = \theta_p - \theta_n$；
- **角动量与速度反相耦合**：
  质子系统与中子系统绕两者对称平分线作反相相对角振荡：$\vec{I}_p = -\vec{I}_n$；由于总角动量为零（$\vec{I} = \vec{I}_p + \vec{I}_n = 0$），该模式在基态附近展示为无净角动量净转动的纯内禀振动；
- **对称能恢复力**：
  质子与中子流体在空间方向的相对剪刀错开，直接破坏了同位旋标量对称性，核力强大的体积对称能提供极强的角弹性回复力常数：
  $$C_\theta \approx 2 b_$C_{\text{sym}}$ \delta^2 \frac{Z N}{A}.$$

### 2.2 激发能量与 $B(M1)$ 强度求和
- **剪刀态本征激发能**：
  $$E_{\text{sc}} = \hbar\omega_{\text{sc}} \approx 66 \cdot \delta \cdot A^{-1/3}\text{ MeV}.$$
  在典型稀土形变区（$A \sim 150 - 180, \delta \a0.25$），剪刀模能量集中在 $E_x \sim 2.5 - 3.5\text{ MeV}$；
- **集体磁偶极跃迁几率 $B(M1)$ 增强**：
  由于质子具有轨道磁矩（$g_p \a1.0$）而中子不带电荷轨道磁矩为零（$g_n \approx 0$），质子流的宏观角反摆产生巨大的动态瞬态交变磁偶极矩：
  $$B(M1; 0^+ \to 1_{\text{sc}}^+) = \frac{3}{16\pi} \mathcal{J}_{\text{sc}} \omega_{\text{sc}} (g_p - g_n)^2 \a1.0 - 3.5\ \mu_N^2.$$
  其强度不仅远超普通单粒子态阻碍跃迁，且在 IBM-2 代数模型中完美对应为 $F$-旋矢量激发（$F = F_m_{\max} - 1$ 的混合对称态）。

---

## 3. 三轴形变核中的剪刀模式双模分裂
在非轴对称三轴形变核中，原子核具有两条相互正交的不同长度短轴：
1. 剪刀相对角摆动沿两个不同短轴方向具有不同的转动惯量与刚度恢复常数；
2. **三轴双模分裂**：经典的单 $1^+$ 剪刀共振峰精确分裂为两个不同激发能量的 $1_a^+$ 与 $1_b^+$ 态；
3. 双峰各自携带可观的集体 $B(M1)$ 跃迁强度，其分裂间距与分支比提供了检验原子核非轴对称刚性三轴性的全新磁偶极探针。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/greiner-asymmetric-rotor-and-rvm-contract.md`
- **代码实现**：`system/scripts/analysis/triaxial_two_rotor_scissors_mode_m1_solver.py`
- **上游来源**：`knowledge/sources/book-greiner-nuclear-models.md`
