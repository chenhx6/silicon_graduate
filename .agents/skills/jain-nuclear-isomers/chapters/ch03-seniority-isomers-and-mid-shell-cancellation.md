# 第 3 章：Seniority 代数、粒子数抛物线与半满壳绝对相消定理

**来源专著**：Ashok Kumar Jain 等《Nuclear Isomers: A Primer》（Springer 2021）第 3 章
**对应页码**：印刷 pp. 31–52 / 物理 PDF pp. 43–64

---

## 1. 核心理论推导与 Seniority 准自旋代数

### 1.1 单 $j$ 壳层配对相互作用与 Seniority 量子数
G. Racah (1943) 与 I. Talmi (1962) 建立了单 $j$ 壳层纯配对力的准自旋代数形式：
$$H_{\text{pair}} = - G \hat{S}_+ \hat{S}_-, \quad \hat{S}_+ = \sum_{m > 0} (-1)^{j-m} a_{jm}^\dagger a_{j,-m}^\dagger.$$
- **壳容量与简并对数**：$\Omega = j + 1/2$，全满壳层粒子数为 $2j + 1 = 2\Omega$；
- **Seniority 量子数 ($v$)**：系统中未被配对算符 $\hat{S}_+$ 结合为 $J=0^+$ 对的单核子数目；
- **准自旋算符**：$\hat{S}_z = \frac{1}{2}(\hat{n} - \Omega)$，总准自旋量子数为 $S = \frac{1}{2}(\Omega - v)$。

### 1.2 单体电多极算符矩阵元的粒子数依赖性
电多极算符 $\hat{M}(E\lambda)$ 在准自旋空间是球张量算符：
1. **奇阶张量（如磁偶极 $M1$）**：为准自旋标量（$\Delta S = 0$），矩阵元与占据粒子数 $n$ 完全无关；
2. **偶阶张量（如电四极 $E2$）**：为准自旋矢量算符的零分量（$\Delta S = 1, \Delta S_z = 0$）。
应用 Wigner-Eckart 定理求粒子数依赖性因子，在**相同 Seniority 态之间（$\Delta v = 0$）**：
$$\langle j^n, v, J || \hat{M}(E2) || j^n, v, J' \rangle = \left( \frac{\Omega - n}{\Omega - v} \right) \langle j^v, v, J || \hat{M}(E2) || j^v, v, J' \rangle = \left( \frac{2j + 1 - 2n}{2j + 1 - 2v} \right) \langle j^v, v, J || \hat{M}(E2) || j^v, v, J' \rangle.$$

---

## 2. 半满壳绝对相消定理 (Mid-Shell Cancellation Theorem)

### 2.1 抛物线跃迁几率因式
将约化电四极跃迁几率表示为粒子数 $n$ 的函数：
$$B(E2; j^n, v \to v) = \left( \frac{2j + 1 - 2n}{2j + 1 - 2v} \right)^2 B(E2; j^v, v \to v).$$
- 当 $n = v$ 时，前置因子为 1；
- **半满壳绝对相消**：
  当单 $j$ 壳层填充达到正中间，即**半满壳（Half-Filled Shell）**：
  $$n = j + 1/2 = \Omega \implies 2j + 1 - 2n = 2\Omega - 2\Omega \equiv 0!$$
  理论跃迁几率严格为零：
  $$B(E2; j^{\Omega}, v \to v) \equiv 0.$$

### 2.2 物理本质：粒子-空穴严格时间反演共轭
在半满壳处，费米面正处于单粒子壳层的中心对称点：
- 此时在壳层中产生一个粒子激发与产生一个空穴激发在动力学上完全对称；
- 粒子态的电四极跃迁贡献与空穴态的电四极跃迁贡献大小完全相等、而代数符号严格相反；
- 导致总跃迁振幅在矩阵元层面发生**完全相消（Destructive Interference）**！

---

## 3. 标杆实验核素数据与微观对账

在真实原子核中，尽管邻近微弱的亚壳层组态混合会导致极微小的残余跃迁，但实测 $B(E2)$ 依然被压制数千倍：
1. **$^{130}\text{Sn}$ 的 $10^+$ 态（微观标杆）**：
   - 处于 $Z=50$ 质子闭壳与 $N=80$ 处；
   - 支配组态为中子独宇称轨道 $\nu (1h_{11/2})^{-2}$ 粒子-空穴态；对于 $1h_{11/2}$ 轨道，$\Omega = 11/2 + 1/2 = 6$；
   - 中子填充数恰好达到半满壳（$n=6$）；
   - 理论上 $10^+ \to 8^+$ 的带内 $E2$ 跃迁受到半满壳相消的极限制约，实测 $B(E2) = 0.038\text{ W.u.}$，寿命急剧延长至 **$T_{1/2} = 1.61\ \mu\text{s}$**！
2. **$^{214}\text{Rn}$ 的 $8^+$ 态**：
   - 质子数 $Z=86$（相对于 $Z=82$ 闭壳含 4 质子），支配轨道为质子 $\pi 1h_{9/2}$（$\Omega = 5$）；
   - 处于严格的质子半满壳（$n=5$），$8^+ \to 6^+$ 跃迁几乎完全相消，$B(E2) = 0.024\text{ W.u.}$，半衰期达 **$T_{1/2} = 6.4\ \mu\text{s}$**；
3. **$^{94}\text{Ru}$ 的 $8^+$ 态**：
   - 质子空穴 $\pi (1g_{9/2})^{-4}$ 构型，半衰期长达 **$71\ \mu\text{s}$**。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/sources/book-jain-nuclear-isomers.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`seniority-isomer` 子命令)
- **上游来源**：`knowledge/sources/book-jain-nuclear-isomers.md`
