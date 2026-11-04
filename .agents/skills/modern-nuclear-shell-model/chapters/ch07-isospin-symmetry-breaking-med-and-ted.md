# 第 7 章：同位旋对称性破缺、镜像能级差 MED/TED 与超允许弱电修正

**来源专著**：M. A. Bentley & N. A. Smirnova《The Nuclear Shell Model 70 Years after Its Advent》（MDPI 2023）第 11、12 篇专论
**对应页码**：印刷 pp. 243–260, 272–301 / 物理 PDF pp. 254–271, 283–312

---

## 1. 核心理论推导与 Henley-Miller 四类核力分类

### 1.1 核力电荷对称性与电荷无关性破缺
在理想纯强相互作用下，核力满足同位旋旋转不变性（$SU(2)$ 同位旋对称性）。
E. M. Henley 与 G. A. Miller 建立了微观同位旋破坏（ISB）分类准则：
1. **Class I 核力（同位旋标量力）**：严格保持同位旋标量旋转不变，$[V_I, \vec{T}] = 0$；
2. **Class II 核力（电荷对称性破缺力, CSB）**：破坏同位旋守恒但在中子-质子反演（绕同位旋 $y$ 轴转 $\pi$）下保持对称：$V_{nn} \ne V_{pp}$（如 $\rho-\omega$ 介子混合与 $u-d$ 夸克质量差）；
3. **Class III 核力（电荷无关性破缺力, CIB）**：将中子-中子力与质子-质子力区别于质子-中子力：$V_{np}(T=1) \ne V_{pp}(T=1)$；
4. **库仑相互作用多极场**：包含单体电荷势、两体直接单极库仑排斥与多极库仑配对力。

---

## 2. 镜像能级差 (MED) 与三重能级差 (TED)

### 2.1 镜像能级差 (MED)
对于互为镜像的同位旋多重态核对（如 $T_z = -1/2$ 与 $T_z = +1/2$）：
$$\text{MED}(J) = E_x(J, T_z = -T) - E_x(J, T_z = +T).$$
- **微观构成**：$\text{MED}(J) = \Delta E_C^{\text{monopole}}(J) + \Delta E_C^{\text{multipole}}(J) + \Delta V_{\text{CSB}}(J)$；
- **单核子 Coriolis 顺排的灵敏探针**：
  当转动角动量上升至对齐区，高-$j$ 质子对在离心力下打破 $J=0^+$ 配对发生平行顺排；质子间空间重叠减小使库仑多极斥力瞬间衰减数十至数百 $\text{keV}$，使得 $\text{MED}(J)$ 曲线展现剧烈下凹的特征拐点，严格锁定了质子顺排发生时的临界自旋 $J_c$。

### 2.2 三重能级差 (TED)
在同位旋三重态（$T=1$，包含 $T_z = -1, 0, +1$ 三核）中构造二阶差分：
$$\text{TED}(J) = E_x(J, T_z = -1) + E_x(J, T_z = +1) - 2 E_x(J, T_z = 0).$$
- **完全抵消单体单极库仑势**：TED 在代数上完全严格消去了所有一阶单体库仑展开项与球形半径单极漂移项；
- **直接分离两体 CIB 核相互作用**：TED 纯粹直接测定了原子核两体库仑配对矩阵元与非微扰强相互作用电荷无关性破坏核力（CIB）的微观强度。

---

## 3. 超允许 $0^+ \to 0^+$ 费米 $\beta$ 衰变与 $\delta_C$ 内转换修正

纯超允许费米衰变比较半衰期 $\mathcal{F}t$ 值为常数：
$$\mathcal{F}t = ft (1 + \delta_R') (1 + \delta_{NS} - \delta_C) = \frac{K}{2 G_V^2 (1 + \Delta_R^V)} = \text{const}.$$
- **同位旋混合修正项 $\delta_C = \delta_{C1} + \delta_{C2}$**：
  1. **$\delta_{C1}$（价空间组态混合）**：库仑两体相互作用诱发同位旋纯态与邻近非完全同位旋态之间的微弱微扰混合（通常为 $0.05\% - 0.2\%$）；
  2. **$\delta_{C2}$（单粒子径向波函数失配）**：质子势阱包含库仑势壁，其径向波函数向外渐近衰减行为与纯中子波函数发生微观空间重叠失配。
通过大规模壳模型高精度计算 $\delta_C$（不确定度控制在 $< 0.1\%$ 以内），将电弱矢量耦合常数 $G_V$ 的测量精度提升至十万分之一，为检验弱电相互作用 CKM 矩阵首行么正性（$|V_{ud}|^2 + |V_{us}|^2 + |V_{ub}|^2 \equiv 1$）及寻找标准模型外新物理提供了最高精度基准。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/smirnova-isospin-symmetry-breaking-shell-model-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`isobaric-analog-state` 子命令)
- **上游来源**：`knowledge/sources/book-nuclear-shell-model-70-years.md`
