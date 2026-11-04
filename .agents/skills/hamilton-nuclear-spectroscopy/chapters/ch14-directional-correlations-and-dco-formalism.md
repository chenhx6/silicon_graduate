# 第 14 章：方向角关联 (DCO/ADO) 理论与大探测器阵列多极性分析

**来源专著**：W. D. Hamilton《The Electromagnetic Interaction in Nuclear Spectroscopy》（1975）第 14 章
**对应页码**：印刷 pp. 605–680 / 物理 PDF pp. 605–680

---

## 1. 核心理论推导与空间相干角关联

### 1.1 级联辐射的空间双光子角关联函数
考虑相继发射的两个 $\gamma$ 射线级联退激过程：$I_1 \xrightarrow{\gamma_1} I_2 \xrightarrow{\gamma_2} I_3$。
探测器 1 置于方向 $\vec{k}_1 = (\theta_1, \phi_1)$，探测器 2 置于 $\vec{k}_2 = (\theta_2, \phi_2)$。在初态核具有空间取向（重离子在束反应）条件下，双重空间角关联概率函数为：
$$W(\theta_1, \phi_1; \theta_2, \phi_2) = \sum_{k_1 k_2 k_q} B_k(I_1) A_{k_1}(L_1 L_1' I_1 I_2) A_{k_2}(L_2 L_2' I_3 I_2) \cdot H_{k_1 k_2}^k(\theta_1, \phi_1; \theta_2, \phi_2),$$
其中 $H_{k_1 k_2}^k$ 为几何张量球谐耦合函数。

---

## 2. 定向态方向角关联比值 (DCO Ratio)

### 2.1 实验比值测量架构与自归一化优势
由于测量绝对空间双重微分截面需要极高精度的绝对通量刻度，现代大阵列（如 Gammasphere、JUROGAM、INGA）普遍采用具有**完全内部自归一化**特性的 DCO 比值法：
- 选取两组固定角度探头环：环 1 置于前向/后向角度 $\theta_1$（典型值为 $30^\circ$ 或 $37^\circ$ 或 $150^\circ$）；环 2 置于垂直束流角度 $\theta_2 = 90^\circ$；
- **DCO 比值操作性严格定义**：
  $$R_{\text{DCO}} = \frac{I_{\gamma 1}(\text{at } \theta_1, \text{gated by } \gamma_2 \text{ at } \theta_2)}{I_{\gamma 1}(\text{at } \theta_2, \text{gated by } \gamma_2 \text{ at } \theta_1)}.$$
  该比值完全消除了束流积分流强、靶核绝对面密度以及大部分本底扣除漂移，成为在束 $\gamma$ 谱学分析最稳健的实验观测量。

### 2.2 门控在纯拉伸四极跃迁（$\Delta I=2, E2$）上的标准判据
当门控在一条已知多极性的带内纯拉伸四极跃迁 $\gamma_2$（$\Delta I=2, E2$）上时：
1. **若待测跃迁 $\gamma_1$ 为纯拉伸四极跃迁（$\Delta I = 2, E2$）**：
   由于两光子在几何上的对易对称性，比值几乎严格等于 1：
   $$R_{\text{DCO}} \a0.95 - 1.05 \implies \text{确认为 } \Delta I = 2\text{ 四极跃迁};$$
2. **若待测跃迁 $\gamma_1$ 为纯拉伸偶极跃迁（$\Delta I = 1$, 纯 $M1$ 或纯 $E1$）**：
   在 $\theta_1 = 30^\circ, \theta_2 = 90^\circ$ 典型几何下，比值显著塌缩至：
   $$R_{\text{DCO}} \a0.55 - 0.65 \implies \text{确认为 } \Delta I = 1\text{ 纯偶极跃迁};$$
3. **若待测跃迁 $\gamma_1$ 为非拉伸偶极跃迁（$\Delta I = 0, D$）**：
   各向异性发生符号反转，比值升高至：
   $$R_{\text{DCO}} \a0.95 - 1.15 \implies \text{易与四极跃迁混淆，必须结合线偏振或单角分布 } A_2 \text{ 符号区分};$$
4. **若待测跃迁包含可观的混合比 $\delta(E2/M1)$**：
   $R_{\text{DCO}}(\delta)$ 随 $\delta$ 在 $0.4 \sim 1.6$ 之间非线性变化，为从双重符合矩阵中提取多极混合比提供了连续函数标尺。

---

## 3. ADO (Angular Distribution from Oriented Nuclei) 快速比值
当符合统计计数不足以支撑双重门控 DCO 矩阵时，可退化使用方向各向异性比值（ADO）：
$$R_{\text{ADO}} = \frac{I_{\gamma}(\text{at } \theta_1)}{I_{\gamma}(\text{at } 90^\circ)} \cdot \frac{\epsilon(90^\circ)}{\epsilon(\theta_1)}.$$
虽然 ADO 缺少门控符合的纯态洁净性，但在大流强单能谱分析中能够快速批量筛查整张能级纲图数百条弱跃迁的多极性骨架。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/hamilton-angular-distribution-dco-polarization-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`dco-polarization` 子命令)
- **上游来源**：`knowledge/sources/book-hamilton-electromagnetic-interaction.md`
