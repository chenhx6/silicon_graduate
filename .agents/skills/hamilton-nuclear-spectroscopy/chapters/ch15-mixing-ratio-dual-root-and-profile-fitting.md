# 第 15 章 (二)：多极混合比 $\delta$ 双根退化二次方程与网格似然反演

**来源专著**：W. D. Hamilton《The Electromagnetic Interaction in Nuclear Spectroscopy》（1975）第 15 章 §15.6
**对应页码**：印刷 pp. 733–737 / 物理 PDF pp. 733–737，式 (15.17)–(15.22)

---

## 1. 核心理论推导与非线性拟合陷阱

### 1.1 混合比无界性与传统非线性拟合的缺陷
多极混合比 $\delta(L'/L)$ 在纯四极（$E2$）跃迁极限下趋于 $\pm \infty$。
直接将 $\delta$ 作为自由参数输入标准高斯-牛顿或 Levenberg-Marquardt 极小化程序时：
1. **梯度死锁与数值溢出**：在发散端附近，一阶导数 $\frac{\partial \chi^2}{\partial \delta}$ 趋近于零或产生数值震荡，导致求解器过早陷入鞍点停滞；
2. **双根多解漏判**：非线性优化器只能收敛到距离初值最近的单一局部极小点，完全无法察觉在参数空间中并存的另一个具有相同卡方的等价解根，造成严重的结论漏判。

### 1.2 Hamilton $\arctan\delta$ 紧致网格扫描法 (Hamilton 式 15.22)
Hamilton 在第 15 章 §6.2 明确指出：**对多极混合比最稳健严密的实验拟合策略，是采用紧致周期性角度参数化**：
$$\phi \equiv \arctan\delta \in [-90^\circ, +90^\circ].$$
- $\delta = 0$ 对应 $\phi = 0^\circ$（纯最低多极 $M1$）；
- $\delta = \pm 1$ 对应 $\phi = \pm 45^\circ$（$50/50$ 电磁等强混合）；
- $\delta = \pm \infty$ 对应 $\phi = \pm 90^\circ$（纯高阶多极 $E2$）。
全参数空间被严格投影为有界闭区间，消除了无穷大奇点。

---

## 2. 轮廓似然网格扫描与双根全景成像

### 2.1 轮廓极小化算法流程
1. 在 $[-90^\circ, +90^\circ]$ 角度区间上建立均匀密集网格点集 $\phi_k = -90^\circ, -89.5^\circ, \dots, +90^\circ$（共 361 点）；
2. 对每一个固定的网格点 $\phi_k$（此时 $\delta_k = \tan\phi_k$ 视为已知定值）：
   - 目标函数关于总束流归一化参数 $A_0$ 与取向参数退化为线性代数方程；
   - 解析线性求解最优条件参数，并记录此时的最小卡方值：
     $$\chi_{\text{prof}}^2(\phi_k) = \min_{A_0, \sigma/I} \sum_{i=1}^{N_{\text{angles}}} \frac{\left[ A_0 W(\theta_i; \phi_k, \sigma/I) - Y_i \right]^2}{\sigma_i^2};$$
3. 绘制全景轮廓似然曲线 $\chi^2(\phi)$。

### 2.2 双谷底拓扑与真双根呈现
- 在曲线图上清晰展示出两个深浅相近的极小深谷 $\phi_1$ 与 $\phi_2$；
- **判别式条件**：当角分布二次代数方程判别式 $\Delta > 0$ 时，两谷底深度几乎完全重合（$\Delta\chi^2 \a0.00$），直观揭示角分布本征双根退化的几何根源；
- **MINOS 非对称置信区间提取**：在最低深谷底部向上取 $\chi^2 = \chi_{\min}^2 + 1.00$ 切割线，直接截取非对称角度置信限 $[\phi^-, \phi^+]$，再通过正切变换映射回具有真实非对称误差的物理混合比：
  $$\delta = \tan\phi^*, \quad \Delta\delta^+ = \tan\phi^+ - \tan\phi^*, \quad \Delta\delta^- = \tan\phi^* - \tan\phi^-.$$

---

## 3. 联合似然破除双根简并

引入康普顿线偏振度 $P_{\text{exp}}$ 或 $K$ 壳层内转换系数 $\alpha_K$ 作为正交观测项：
$$\chi_{\text{joint}}^2(\phi) = \chi_{\text{ang}}^2(\phi) + \frac{[P_{\text{theo}}(\phi) - P_{\text{exp}}]^2}{\sigma_P^2} + \frac{[\alpha_K^{\text{theo}}(\phi) - \alpha_K^{\text{exp}}]^2}{\sigma_\alpha^2}.$$
- 由于偏振度与转换系数对混合比具有单调或反号干涉响应，其中一个假根处的卡方将被急剧抬升（$\Delta\chi^2 \ge 25.0$），而真实物理根处的卡方保持在全局极小；
- 以超过 $5\sigma$ 的压倒性统计置信度破除双根歧义，输出唯一可靠的核谱学跃迁性质判定。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/hamilton-angular-distribution-dco-polarization-contract.md`
- **代码实现**：`system/scripts/analysis/double_root_dco_polarization_statistical_arbitrator.py`
- **上游来源**：`knowledge/sources/book-hamilton-electromagnetic-interaction.md`
