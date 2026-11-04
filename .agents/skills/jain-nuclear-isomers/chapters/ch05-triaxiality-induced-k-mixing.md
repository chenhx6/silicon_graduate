# 第 5 章 (二)：三轴形变诱导 $K$-混合（$K$-Mixing）与阻碍度异常塌缩指纹

**来源专著**：Ashok Kumar Jain 等《Nuclear Isomers: A Primer》（Springer 2021）第 5 章 §5.4
**对应页码**：印刷 pp. 88–98 / 物理 PDF pp. 100–110

---

## 1. 核心理论推导与三轴对称性破缺

### 1.1 三轴形变破坏轴向旋转对称性
在理想轴对称核中，主对称轴具有旋转不变性，$K$ 是严格守恒的好量子数。
当原子核具备非轴对称三轴形变（$\gamma \ne 0^\circ$ 且 $\gamma \ne 60^\circ$）时：
1. 三个主轴长短各异，原子核绕主轴旋转不再对称；
2. **非对角张量耦合算符**：
   三轴刚性转子或三轴粒子-转子模型（PTRM）哈密顿量中显式包含 $\Delta K = \pm 2$ 的非对角耦合项：
   $$\hat{H}_{\text{triax}} = \frac{\hbar^2}{8} \left( \frac{1}{\mathcal{J}_1} - \frac{1}{\mathcal{J}_2} \right) (\hat{I}_+^2 + \hat{I}_-^2);$$
3. **波函数的全空间多重 $K$ 杂化展开**：
   本征波函数彻底丧失单值 $K$ 纯度，展开为一系列相距 $\Delta K = 2$ 的空间基底相干杂化混合：
   $$|\Psi_{IM}\rangle = \sum_{K = 0, 2, 4 \dots \le I} c_K |IMK\rangle.$$

---

## 2. “量子捷径”泄漏与折合阻碍度 $f_\nu$ 的异常暴跌

### 2.1 阻碍度塌缩机理 (Hindrance Collapse)
设名义上初始态为高 $K$ 态（如 $K_i = 8$），终态为低 $K$ 基态转动带（$K_f = 0$）：
- **轴对称图像的错误预言**：按照轴对称守恒律，跃迁经历 $|\Delta K| - \lambda = 8 - 2 = 6$ 级强禁戒，按照 $f_\nu \sim 100$ 规律，半衰期应被压低整整 $100^6 = 10^{12}$ 倍；
- **三轴 $K$-混合的真实跃迁路径**：
  由于三轴形变导致初态波函数中渗入了微量低 $K$ 组分（如即使包含仅 $1\% - 3\%$ 的 $K=2$ 杂质振幅）：
  $$\langle \text{Ground Band }(K_f=0) || \hat{M}(E2) || \Psi_{\text{isomer}} \rangle \approx c_2 \cdot \langle K_f=0 || \hat{M}(E2) || K=2 \rangle.$$
  此时跃迁通过该小振幅杂质路径发生**完全无禁戒的拉伸电四极跃迁（$\Delta K_{\text{eff}} = 2 = \lambda$）**！

### 2.2 阻碍度暴跌指标
尽管杂质振幅平方仅占百分之几，但相比于微扰禁戒的高阶惩罚，无禁戒通道的跃迁几率大数千倍，从而导致实测折合阻碍度发生断崖式暴跌：
$$f_\nu \ll 10 \quad (\text{通常降至 } f_\nu \approx 2 - 5)!$$

---

## 3. 在束谱学应用：$A \a$A \aA \a130$ 质量区三轴性独立判决
在核手征性与摆动运动直接关切的 $A \a$A \aA \a130$ 质量区（如 $\text{Cs}, \text{Ba}, \text{La}, \text{Ce}, \text{Nd}$ 同位素），核芯普遍具有强烈的三轴形变与 $\gamma$ 软性。

### 经典实验对账数据：
1. **$^{130}\text{Ba}$ 的 $8^-$ 异能态**（$T_{1/2} = 9.5\text{ ms}$）：
   退激到 $K=0$ 基带，名义禁戒度 $\nu = 6$；实测折合阻碍度仅为 **$f_\nu = 4.8 \ll 100$**；
2. **$^{134}\text{Nd}$ 的 $8^-$ 异能态**（$T_{1/2} = 410\ \mu\text{s}$）：
   名义禁戒度 $\nu = 6$；实测折合阻碍度仅为 **$f_\nu = 3.6 \ll 100$**；
3. **$^{128}\text{Cs}$ 的 $8^-$ 异能态**（$T_{1/2} = 2.2\ \mu\text{s}$）：
   名义禁戒度 $\nu = 5$；实测折合阻碍度仅为 **$f_\nu = 2.9 \ll 100$**。

**物理判决结论**：
在低自旋下普遍观测到的 $f_\nu \le 5$ 异常塌缩，排除了高转速 Coriolis 动力学混合的可能，排他性地证明了 $A \sim 130$ 质量区原子核具有**深刻的非轴对称三轴形变（$\gamma \approx 20^\circ - 30^\circ$）**，为该区域三轴手征双重带与摆动运动提供了无可辩驳的同核异能态侧翼宏观形变证据！

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/sources/book-jain-nuclear-isomers.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`k-isomer-hindrance` 子命令)
- **上游来源**：`knowledge/sources/book-jain-nuclear-isomers.md`
