# 第 12 章：假设检验、Wilks 定理与物理发现显著性

**来源专著**：朱永生《实验物理中的概率和统计（第二版）》（科学出版社 2006）
**对应页码**：印刷 pp. 461–520 / 扫描 PDF pp. 477–536

---

## 1. 核心理论推导与数学基础

### 1.1 统计假设检验的基本结构
在实验物理中，经常需要依据测量样本对两个竞争的物理模型作出仲裁决断：
- **原假设 / 零假设 ($H_0$)**：基准参考模型（如“纯单粒子进动带”、“无三轴形变”、“跃迁为纯 $M1$”）；
- **备择假设 ($H_1$)**：竞争新物理模型（如“三轴集体摆动带”、“手征双重带”、“存在 $E2$ 集体增强混合”）；
- **第一类错误率 ($\alpha$, 假阳性率 / 显著性水平)**：零假设 $H_0$ 为真时却被拒绝的概率；
- **第二类错误率 ($\beta$, 假阴性率 / 漏检率)**：零假设 $H_0$ 为假时却被接受的概率；
- **检验功效 (Power $1 - \beta$)**：当备择假设为真时正确拒绝零假设的概率。

### 1.2 Neyman-Pearson 引理（最有效检验定理）
对于简单假设检验（$H_0$ 与 $H_1$ 均无未知自由参数），设样本观测为 $\vec{x}$：
- **似然比检验统计量**：
  $$\lambda(\vec{x}) = \frac{L(\vec{x} \mid H_0)}{L(\vec{x} \mid H_1)};$$
- **拒绝域准则**：在给定显著性水平 $\alpha$ 下，拒绝域形式为 $W = \{ \vec{x} \mid \lambda(\vec{x}) \le c_\alpha \}$；
- **定理结论**：似然比检验是在所有假阳性率等于 $\alpha$ 的检验中，第二类错误率 $\beta$ 严格达到极小、功效 $1 - \beta$ 严格达到最大的**一致最优检验 (Uniformly Most Powerful, UMP)**。

### 1.3 广义似然比检验与复合假设
当模型包含待定未知参数时（$\vec{\theta} \in \Theta$ 为全参数空间，$\Theta_0 \subset \Theta$ 为 $H_0$ 约束子空间）：
$$\lambda = \frac{\sup_{\vec{\theta} \in \Theta_0} L(\vec{\theta})}{\sup_{\vec{\theta} \in \Theta} L(\vec{\theta})} = \frac{L(\hat{\vec{\theta}}_0)}{L(\hat{\vec{\theta}})}.$$
定义检验统计量：
$$q = -2 \ln \lambda = 2 [\ln L(\hat{\vec{\theta}}) - \ln L(\hat{\vec{\theta}}_0)] = \chi^2(H_0) - \chi^2(H_1) = \Delta\chi^2.$$

### 1.4 Wilks 定理（大样本渐近卡方分布）
**定理内容**：当原假设 $H_0$ 成立、两模型参数空间嵌套（$H_0$ 是 $H_1$ 的受限子空间）、真参数位于参数空间内部且样本量 $N \to \infty$ 时：
$$q = -2 \ln \lambda \xrightarrow{d} \chi^2(k),$$
其中自由度 $k = \dim(\Theta) - \dim(\Theta_0)$ 为两模型自由参数个数之差。
**适用边界与破缺条件**：若零假设参数位于参数空间边界上（例如新粒子产额振幅限制在 $S=0$ 边界），标准 Wilks 定理失效，检验统计量服从半高斯-半卡方混合分布（Chernoff 混合分布：$\frac{1}{2}\delta(0) + \frac{1}{2}\chi^2(1)$）。

---

## 2. $p$ 值与高斯等效显著性 $Z$

### 2.1 $p$ 值的严格定义
实验观测得到统计量数值 $q_{\text{obs}}$ 时，在 $H_0$ 假设下发生等于或大于该偏离的累积概率：
$$p = P(q \ge q_{\text{obs}} \mid H_0) = \int_{q_{\text{obs}}}^\infty f_{\chi^2}(x; k) dx = 1 - F_{\chi^2}(q_{\text{obs}}; k).$$

### 2.2 单参数 ($k=1$) 下的高斯显著性换算
将单侧 $p$ 值通过标准正态累积分布函数反演：
$$Z = \Phi^{-1}(1 - p) \approx \sqrt{q_{\text{obs}}} = \sqrt{\Delta\chi^2}.$$

### 2.3 物理学裁决门槛
1. **$Z \ge 3.0\sigma$ ($p \le 1.35 \times 10^{-3}$, $\Delta\chi^2 \ge 9.0$)**：
   物理学公认的“**观测证据 (Evidence)**”门槛，表明单纯由统计涨落产生该信号的几率小于千分之 1.35；
2. **$Z \ge 5.0\sigma$ ($p \le 2.87 \times 10^{-7}$, $\Delta\chi^2 \ge 25.0$)**：
   物理学公认的“**确证发现 (Discovery)**”黄金标准，将第一类假阳性几率压缩至千万分之二以下。

---

## 3. 核结构实战案例：$^{135}\text{Pr}$ 摆动运动假设之 $11.1\sigma$ 证伪

在奇 $A$ 核 $^{135}\text{Pr}$ 的高自旋态研究中，关于 Band 1 与 Band 2 的带间退激 $\Delta I=1$ 跃迁性质存在激烈争议：
- **假设 $H_0$ (摆动激发假说)**：带间跃迁主导多极性为电四极 $E2$（摆动声子退激），对应多极混合比解根 $\delta_2 \approx +2.5$；
- **假设 $H_1$ (倾斜进动 / 签名伙伴带假说)**：带间跃迁主导多极性为磁偶极 $M1$（单粒子进动），对应多极混合比解根 $\delta_1 \approx -0.1$；
- **角分布退化**：Gammasphere 实测方向角分布系数 $a_2 = -0.42(3)$，在两根处卡方完全重合：$\Delta\chi_{\text{ang}}^2 = 0.00$；
- **引入线偏振度 $P$ 仲裁**：JUROGAM II Clover 阵列测得康普顿散射不对称度给出 $P_{\text{exp}} = -0.21(4)$；
- **检验统计量**：
  $$\chi^2(\text{wobbling}) - \chi^2(\text{TiP}) = \Delta\chi^2 = 122.3.$$
代入高斯等效显著性：
$$Z = \sqrt{122.3} = 11.06\sigma \a11.1\sigma, \quad p = 2.0 \times 10^{-28}.$$
以超过 $11\sigma$ 的压倒性统计置信度坚决拒绝摆动假说，确证了多极混合比的唯一物理真解。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/zhu-advanced-statistics-and-parameter-estimation-contract.md`
- **研究笔记**：`knowledge/research-notes/pr135-gammasphere-vs-jurogam-joint-likelihood-audit-20261101.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`double-root` 子命令)
- **上游来源**：`knowledge/sources/book-zhu-probability-statistics-in-physics.md`
