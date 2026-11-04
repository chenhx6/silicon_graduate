# 第 4 章：准弹性散射、DWBA 多核子转移反应与光谱因子提取

**来源专著**：林承键《重离子核反应》（科学出版社 2017）第 4 章 & Bertulani《Introduction to Nuclear Reactions》（2021）第 6 章
**对应页码**：林书印刷 pp. 88–109 / 物理 PDF pp. 98–119；Bertulani PDF pp. 214–265

---

## 1. 核心理论推导与准弹性物理图像

### 1.1 准弹性散射定义与外围碰撞机制
准弹性散射（Quasi-Elastic Scattering, QEL）是指在掠射碰撞距离附近（$r \approx R_{\text{int}} = R_1 + R_2$）发生的外围直接过程总和：
$$\sigma_{\text{qel}} = \sigma_{\text{el}} + \sigma_{\text{inel}} + \sigma_{\text{transfer}}.$$
- 碰撞特征：相互作用时间极短（$\sim 10^{-22}\text{ s}$），无显著动能损失，两核核芯未发生深度重叠；
- **角分布特征**：主要集中在掠射角 $\theta_{\text{gr}}$ 附近，随角度增大迅速衰减。

### 1.2 准弹性势垒分布反演定理 (Timmers 法则)
由于核相互作用发生吸收损失，在背散射大角度（如 $\theta_{\text{lab}} = 160^\circ - 170^\circ$）下，准弹性散射与纯库仑 Rutherford 截面之比随入射能量上升而急剧跌落（通量转移至熔合道）。
- **准弹性势垒分布定义**：
  $$D_{\text{qel}}(E_{\text{eff}}) \equiv - \frac{d}{d E_{\text{eff}}} \left[ \frac{\sigma_{\text{qel}}(E, \theta)}{\sigma_R(E, \theta)} \right],$$
  其中离心势垒修正后的有效能量为：
  $$E_{\text{eff}} = \frac{2 E_{\text{c.m.}}}{1 + \csc(\theta_{\text{c.m.}}/2)}.$$
- **物理等价性**：$D_{\text{qel}}(E)$ 与 Rowley 熔合势垒分布 $D_{\text{fus}}(E)$ 在数学上严格互补，且测量准弹性背散射仅需单探测器监测，无需复杂的气体探测器分离反冲残核，是实验获取稀有束流与不稳定核势垒分布的最强手段。

---

## 2. 转移反应运动学与最优 Q 匹配法则

在重离子转移反应 $A(a, b)B$（其中 $a = b + x$ 为转移核子团簇）中，由于强库仑场主导，两核必须在接触点处同时满足空间距离与轨道速度切向连续。
- **最优 Q 值公式 ($Q_{\text{opt}}$)**：
  $$Q_{\text{opt}} \approx \left( \frac{Z_b Z_B}{Z_a Z_A} - 1 \right) E_{\text{c.m.}} + \frac{\hbar^2 (l_i^2 - l_f^2)}{2 \mu R^2}.$$
  - 若出射通道电荷数减小（如质子从弹核转移至靶核，$Z_b < Z_a$），出射库仑势垒降低，因而 $Q_{\text{opt}} < 0$（要求吸能反应）；
  - **物理启示**：实际转移截面强烈集中在以 $Q_{\text{opt}}$ 为中心、宽度仅数 $\text{MeV}$ 的“$Q$ 窗口”内；偏离 $Q_{\text{opt}}$ 的末态能级布居截面被压低数个数量级！

---

## 3. DWBA 形式理论与微观光谱因子反演

### 3.1 扭曲波玻恩近似 (DWBA) 跃迁振幅
在弹核与靶核光学模型扭曲波 $\chi_i^{(+)}(\vec{r}_i)$ 与 $\chi_f^{(-)}(\vec{r}_f)$ 构成的基底上：
$$T_{fi} = \int d\vec{r}_i \int d\vec{r}_f \chi_f^{(-)*}(\vec{r}_f) \langle \psi_B \psi_b | V_{\text{trans}} | \psi_A \psi_a \rangle \chi_i^{(+)}(\vec{r}_i).$$

### 3.2 角分布形状与转移角动量 $\Delta l$
转移微分截面的前向主峰角位 $\theta_{\text{peak}}$ 严格由动量转移矢量大小与相互作用半径满足的乘积法则控制：
$$q = |\vec{k}_i - \vec{k}_f| \approx \frac{\Delta l}{R_{\text{int}}}.$$
- 通过拟合实验测定的微分截面主峰角位，可无歧义确定被转移核子进入靶核轨道的轨道角动量 $\Delta l$（如区别进入中子 $1g_{9/2}$、$2d_{5/2}$ 还是 $1h_{11/2}$ 轨道）；
- **光谱因子提取**：
  $$\left( \frac{d\sigma}{d\Omega} \right)_{\text{exp}} = S_{lj} \cdot \left( \frac{d\sigma}{d\Omega} \right)_{\text{DWBA}}.$$
  $S_{lj} \in [0, 1]$ 直接测定核态中单粒子组态的纯度，揭示长程集体振动对单粒子运动的微观极化与破缺。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/bertulani-reaction-mechanisms-and-hauser-feshbach-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`transfer-qopt` 子命令)
- **上游来源**：`knowledge/sources/book-bertulani-nuclear-reactions.md`
