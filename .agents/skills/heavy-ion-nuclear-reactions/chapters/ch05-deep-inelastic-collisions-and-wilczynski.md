# 第 5 章：深部非弹性散射 (DIC)、Wilczynski 图谱与耗散动力学

**来源专著**：林承键《重离子核反应》（科学出版社 2017）第 5 章 & Bertulani《Introduction to Nuclear Reactions》（2021）第 5 章
**对应页码**：林书印刷 pp. 110–133 / 物理 PDF pp. 120–143；Bertulani PDF pp. 172–213

---

## 1. 核心理论推导与物理图像

### 1.1 深部非弹性碰撞 (DIC) 的物理特征与碰撞区间
深部非弹性碰撞（Deep Inelastic Collisions, DIC，亦称强阻尼碰撞）发生在碰撞参数介于准弹性外围掠射与完全熔合之间的大角动量区域：
$$\ell_n_{\text{crit}} < l \le \ell_{\text{grazing}}.$$
- **微观时间尺度与弛豫层次**：
  1. **能量完全阻尼（$\sim 10^{-22}\text{ s}$ 最快）**：初始动能迅速耗散为内部热能，出射动能降至两形变核在断裂点处的纯相互库仑排斥能；
  2. **电荷-质量比平衡（$N/Z$ 均一化，$\sim 10^{-21}\text{ s}$）**：中子与质子在颈部窗口快速扩散，达到与基态对称能匹配的电荷平衡；
  3. **角动量耗散与核子数质量漂移（$\sim 10^{-20}\text{ s}$）**：轨道角动量向内禀自旋转移，体系发生非对称向对称的缓慢质量演化。

### 1.2 轨道角动量耗散与刚体粘滞极限 (Sticking Limit)
当两核在接触面发生强烈相对滑动与转动阻尼时，核表面强摩擦力迫使系统逐渐达到刚体共转（Sticking）：
- 接触双核体系的内禀主轴转动惯量为 $\mathcal{J}_1 + \mathcal{J}_2$；
- 相对轨道转动惯量为 $\mu R_{\text{int}}^2$；
- **转移到碎片内禀自旋的总角动量比例（刚体粘滞极限）**：
  $$\frac{\Delta l_{\text{int}}}{l_i} = \frac{\mathcal{J}_1 + \mathcal{J}_2}{\mathcal{J}_1 + \mathcal{J}_2 + \mu R_{\text{int}}^2} \approx \frac{\frac{2}{5} A_1 R_1^2 + \frac{2}{5} A_2 R_2^2}{\frac{2}{5} A_1 R_1^2 + \frac{2}{5} A_2 R_2^2 + \frac{A_1 A_2}{A_1 + A_2}(R_1 + R_2)^2} \a0.28 - 0.35.$$
对于入射角动量 $l_i \sim 100 - 150\hbar$ 的重核碰撞，单次碰撞即可向两碎片分别注入 $I_1 \sim 20 - 30\hbar$ 与 $I_2 \sim 20 - 30\hbar$ 的巨额自旋！

---

## 2. Wilczynski 能量-角度二维关联图谱

Jan Wilczynski (1973) 提出将实验测得的双重微分截面 $\frac{d^2\sigma}{d\Omega \cdot dE}$ 在质心散射角 $\theta_{\text{c.m.}}$ 与总动能（TKE）或总动能损失（TKEL）构成的平面上绘制等高线：
1. **准弹性峰 (Quasi-Elastic Peak)**：位于掠射角 $\theta_{\text{gr}}$ 附近，能量损失 $\text{TKEL} \approx 0$；
2. **深部非弹性脊线（强阻尼分枝）**：随能量损失持续增加，两核接触时间延长，体系绕质心继续转动，散射角向小角度偏转并穿过 $0^\circ$ 延伸至负偏转角（Negative Angles）；
3. **特征“鸟嘴”（Bird-Beak）形态**：等高线从准弹性极值点向下弯曲并向内收拢，在全弛豫动能线（$E \approx V_C$）处收敛，直观证明核碰撞经历了经典轨道连续偏转与渐进摩擦耗散过程。

---

## 3. 在束谱学应用：丰中子区高自旋同核异能态布居
常规熔合蒸发反应仅能合成缺中子或近稳定线核素（因为熔合后必须靠发射数个中子冷却）；而对于丰中子稀土区与重核区，熔合蒸发完全无法涉足。
- **深部非弹厚靶谱学技术**：
  采用高能量重离子轰击厚靶（如 $^{136}\text{Xe} (850\text{ MeV}) + {}^{208}\text{Pb}$ 或 $^{136}\text{Xe} + {}^{198}\text{Pt}$），利用深部多核子转移将大量中子注入靶核，同时注入 $I \sim 20 - 40\hbar$ 的高自旋；
- 反冲核完全阻滞在厚靶中，消除了高速飞行带来的多普勒展宽，利用 HPGe 大阵列的多重 $\gamma-\gamma-\gamma$ 空间符合矩阵，成功解析出一批丰中子核（如 $^{132,134}\text{Sn}$ 邻近同位素）的高自旋同核异能态与集体带。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/lin-heavy-ion-fusion-and-barrier-distribution-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`wilczynski-energy` 子命令)
- **上游来源**：`knowledge/sources/book-lin-heavy-ion-reactions.md`
