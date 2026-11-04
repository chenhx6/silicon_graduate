# 第 8 章：准粒子微观费米子与 CSM 玻色子核芯自洽耦合理论

**来源专著**：A. A. Raduta《Nuclear Structure with Coherent States》（Springer 2016）第 8 章
**对应页码**：印刷 pp. 255–276 / 物理 PDF pp. 262–283

---

## 1. 核心理论推导与混合多体哈密顿量

### 1.1 费米子-玻色子杂化系统表象
为了描述奇 $A$ 核以及偶偶核高自旋破对两准粒子激发带，Raduta 建立了准粒子费米子算符与相干态玻色核芯自洽耦合的统一模型：
$$H = H_{\text{core}} + H_{\text{qp}} + H_{\text{coupl}}.$$
1. **玻色核芯项 $H_{\text{core}}$**：由四极玻色子创生湮灭算符展开，描述核芯的转动与表面微扰振动；
2. **费米子准粒子项 $H_{\text{qp}}$**：在球形或变形 Nilsson 单粒子基底上展开：
   $$H_{\text{qp}} = \sum_{jm} E_j c_{jm}^\dagger c_{jm},$$
   其中 $E_j = \sqrt{(\epsilon_j - \lambda)^2 + \Delta^2}$ 为 BCS 准粒子激发能量；
3. **粒子-核芯相互作用耦合项 $H_{\text{coupl}}$**：
   包含四极-四极粒子-玻色子吸引力：
   $$H_{\text{coupl}} = - \chi \sum_\mu \hat{q}_{2\mu} (b_{2\mu}^\dagger + (-1)^\mu b_{2,-\mu}), \quad \hat{q}_{2\mu} = \sum_{1, 2} \langle 1 | r^2 Y_{2\mu} | 2 \rangle c_1^\dagger c_2.$$

---

## 2. 复合系统三维角动量投影

未投影的内禀波函数由玻色子相干态 $|\psi_{\text{core}}(d)\rangle$ 与外层准粒子态相乘构成：
$$|\Phi(d)\rangle = |\psi_{\text{core}}(d)\rangle \otimes |j_1 j_2 \dots; J_f K_f\rangle.$$
应用全空间群角动量投影算符 $\hat{P}_{MK}^I$：
$$|\Psi_{IM}\rangle = \sum_K \mathcal{N}_{IK}(d) \hat{P}_{MK}^I |\Phi(d)\rangle.$$
- 投影积分核同时遍历核芯欧拉角与外层费米子自旋旋转；
- 自动消除了微观粒子-转子模型中人为假定核芯惯量与准粒子相互孤立割裂的经典近似，严格保持全核 Pauli 不相容原理与总角动量守恒。

---

## 3. 在束核谱学应用：独宇称轨道 Coriolis 退耦带微观构建
当外层准粒子占据高-$j$ 独宇称侵入轨道（如 $1h_{11/2}$ 或 $1i_{13/2}$）时：
1. Coriolis 力迫使准粒子角动量向旋转轴顺排，与相干玻色核芯解耦；
2. 投影模型解析导出了退耦带（Decoupled Bands）能级间距与偶偶核芯基带完全相同的微观物理图景（$E(I+2) - E(I) \approx E_{\text{core}}(2_1^+)$）；
3. 同时自洽给出了多准粒子高 $K$ 带首态的形成机制与微观能级排布。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/raduta-gcsm-chiral-and-triaxial-rotor-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`odd-a-coriolis-mixing` 子命令)
- **上游来源**：`knowledge/sources/book-raduta-coherent-states.md`
