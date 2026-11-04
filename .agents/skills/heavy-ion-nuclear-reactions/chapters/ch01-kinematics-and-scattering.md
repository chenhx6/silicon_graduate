# 第 1 章：重离子碰撞运动学、坐标变换与弹性散射

**来源专著**：林承键《重离子核反应》（科学出版社 2017）第 1、3 章 & Bertulani《Introduction to Nuclear Reactions》（2021）第 1、2 章
**对应页码**：林书印刷 pp. 1–17, 37–68 / 物理 PDF pp. 11–27, 47–78；Bertulani PDF pp. 12–79

---

## 1. 核心理论推导与运动学体系

### 1.1 实验室系与质心系非相对论性严格变换
设入射重离子（弹核）质量为 $M_p$（核子数 $A_p$），在实验室系中具有动能 $E_{\text{lab}}$，轰击静止靶核 $M_t$（核子数 $A_t$）。
- **质心速度**：
  $$\vec{V}_{\text{c.m.}} = \frac{M_p \vec{v}_p}{M_p + M_t} = \frac{\sqrt{2 M_p E_{\text{lab}}}}{M_p + M_t} \hat{z};$$
- **质心系有效可用动能**：
  $$E_{\text{c.m.}} = \frac{1}{2}\mu v_{\text{rel}}^2 = \frac{M_t}{M_p + M_t} E_{\text{lab}} = \frac{A_t}{A_p + A_t} E_{\text{lab}},$$
  其中约化质量 $\mu = \frac{M_p M_t}{M_p + M_t}$；
- **散射角坐标变换关系**：
  设质心系中出射角为 $\theta_{\text{c.m.}}$，出射粒子在实验室系中角度为 $\theta_{\text{lab}}$：
  $$\tan\theta_{\text{lab}} = \frac{\sin\theta_{\text{c.m.}}}{\cos\theta_{\text{c.m.}} + \gamma_v}, \quad \gamma_v = \frac{V_{\text{c.m.}}}{v_3'}=\sqrt{\frac{M_p M_3}{M_t M_4} \frac{E_{\text{c.m.}}}{E_{\text{c.m.}} + Q}}.$$
  对于弹性散射（$M_3 = M_p, M_4 = M_t, Q = 0$）：$\gamma_v = M_p / M_t = A_p / A_t$。
  - 若 $A_p < A_t$（反向反应学或轻弹核轰击重靶）：$\gamma_v < 1$，$\theta_{\text{lab}}$ 覆盖完整 $0^\circ \to 180^\circ$；
  - 若 $A_p > A_t$（重弹核轰击轻靶）：$\gamma_v > 1$，实验室系中存在最大前向出射角 $\theta_{\text{lab}}^m_{\max} = \arcsin(A_t / A_p)$。

### 1.2 复合核反冲初动能与多普勒初速
当发生完全熔合时，弹核与靶核合二为一，质心相对动能全部转化为复合核内禀激发能，系统整体沿束流方向平移：
$$E_{\text{recoil}} = E_{\text{lab}} - E_{\text{c.m.}} = \frac{A_p}{A_p + A_t} E_{\text{c.m.}} = \frac{A_p A_t}{(A_p + A_t)^2} E_{\text{lab}}.$$
反冲初速度比率：
$$\beta = \frac{v_{\text{recoil}}}{c} \approx \sqrt{\frac{2 E_{\text{recoil}}}{M_{\text{CN}} c^2}} = \frac{\sqrt{2 A_p u E_{\text{lab}}}}{(A_p + A_t) u c} \a0.04635 \frac{\sqrt{A_p E_{\text{lab}} [\text{MeV}]}}{A_p + A_t}.$$
在束 $\gamma$ 谱学测量中，$\beta$ 决定了运动发射源的多普勒频移：$E_\gamma(\theta) = E_{\gamma 0} \frac{\sqrt{1-\beta^2}}{1 - \beta\cos\theta_{\text{det}}} \approx E_{\gamma 0} (1 + \beta\cos\theta_{\text{det}})$。

---

## 2. 重离子弹性散射与菲涅耳衍射动力学

### 2.1 索末菲参数与强库仑散射
重离子碰撞的显著特征是体系携带大量正电荷，库仑势极为强大：
$$\eta = \frac{Z_p Z_t e^2}{\hbar v} = 0.1574 Z_p Z_t \sqrt{\frac{A_{\text{red}}}{E_{\text{c.m.}} [\text{MeV}]}} \gg 1.$$
当 $\eta \gg 1$ 时，系统运动呈现鲜明的半经典轨道特征：
- 经典掠射距离：$R_{\text{gr}} = R_p + R_t = r_0 (A_p^{1/3} + A_t^{1/3})$；
- 对应掠射角（Grazing angle）：
  $$\sin\left(\frac{\theta_{\text{gr}}}{2}\right) = \frac{\eta}{k R_{\text{gr}} - \eta}.$$

### 2.2 菲涅耳衍射与 1/4 截面点强吸收定理
当重离子在强吸收势下碰撞时，分波 $S$ 矩阵模值从远距的 $|S_l| = 1$（完全反射）过渡到核表面内的 $|S_l| = 0$（完全吸收）。角分布展示出特征的菲涅耳衍射图样：
- 在小散射角区 $\theta < \theta_{\text{gr}}$，微分截面围绕纯 Rutherford 截面振荡；
- 当散射角继续增大并跨越掠射角时，截面迅速向下跌落；
- **Frahn 强吸收定理**：在比值降为四分之一处：
  $$\left. \frac{d\sigma_{\text{el}}}{d\sigma_R} \right|_{\theta = \theta_{1/4}} = 0.250.$$
  通过测定实验角分布中的 $\theta_{1/4}$，可严格直接反推核相互作用接触半径 $R_{\text{int}}$，完全不依赖唯象势场参数假设。

---

## 3. 在束谱学应用：反应道运动学与探头布局控制
在 $^{16}\text{O} (E_{\text{lab}} = 80\text{ MeV}) + {}^{120}\text{Sn}$ 熔合蒸发反应中：
- $A_p = 16, A_t = 120, A_{\text{CN}} = 136$；
- $E_{\text{c.m.}} = \frac{120}{136} \times 80 = 70.59\text{ MeV}$；
- 反冲核 $^{136}\text{Ce}^*$ 初始动能：$E_{\text{recoil}} = \frac{16}{136} \times 70.59 = 8.30\text{ MeV}$；
- 反冲初速比：$\beta = 0.04635 \frac{\sqrt{16 \times 80}}{136} = 0.0122 = 1.22\% c$；
- 阵列角度为 $30^\circ$ 与 $150^\circ$ 处的相反多普勒移动为 $\Delta E / E_0 \approx \pm 1.06\%$，为在束 DSAM 寿命反演与 Doppler-Correction 提供了明确的运动学校准基线。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/lin-heavy-ion-fusion-and-barrier-distribution-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`kinematics` 子命令)
- **上游来源**：`knowledge/sources/book-lin-heavy-ion-reactions.md`
