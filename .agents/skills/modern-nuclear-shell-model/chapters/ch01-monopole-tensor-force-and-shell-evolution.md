# 第 1 章：单极相互作用分解、张量力对偶性与微观壳演化机制

**来源专著**：T. Otsuka & Y. Utsuno《The Nuclear Shell Model 70 Years after Its Advent》（MDPI 2023）第 3、8 篇专论
**对应页码**：印刷 pp. 87–114, 193–207 / 物理 PDF pp. 98–125, 204–218

---

## 1. 核心理论推导与有效两体力单极分解

### 1.1 单极矩阵元标量定义
在给定的单粒子模型空间中，两体有效相互作用算符 $V$ 可以严格做转动标量分解。
单极相互作用矩阵元（Monopole Matrix Element）定义为关于总角动量 $J$ 的自旋加权统计平均值（Otsuka 式 1）：
$$V_{j_1 j_2}^{\text{mono}} \equiv \frac{\sum_J (2J+1) \langle j_1 j_2 J | V | j_1 j_2 J \rangle}{\sum_J (2J+1)}.$$
- **物理意义**：消除了特定空间相对取向产生的多极形变扰动，纯粹描述了当轨道 $j_2$ 每增加一个价核子时，轨道 $j_1$ 感受到的平均单体势阱深度移动；
- **有效单粒子能量 (ESPE) 漂移方程**：
  $$\epsilon_{\text{eff}}(j_1) = \epsilon_{\text{bare}}(j_1) + \sum_{j_2} V_{j_1 j_2}^{\text{mono}} \cdot \langle \hat{n}(j_2) \rangle.$$

---

## 2. 张量力 (Tensor Force) 的微观对偶性定理

### 2.1 介子交换与自旋-轨道耦合依赖
真实的核子-核子相互作用包含强大的非中心张量力（主要源自单 $\pi$ 介子与 $\rho$ 介子交换）：
$$\hat{V}_T = V_T(r) \left[ 3 (\vec{\sigma}_1 \cdot \hat{r})(\vec{\sigma}_2 \cdot \hat{r}) - \vec{\sigma}_1 \cdot \vec{\sigma}_2 \right] \cdot (\vec{\tau}_1 \cdot \vec{\tau}_2).$$
T. Otsuka 等人严格证明了单极张量力对偶定理：
1. **自旋-轨道同向轨道 ($j_> = l + 1/2$) 与反向轨道 ($j'_< = l' - 1/2$)**：
   两者自旋方向反平行，两核子空间相对波函数波腹发生重叠，张量力表现为**强烈吸引 ($V_T^{\text{mono}} < 0$)**；
2. **自旋-轨道同向对 ($j_>, j'_>$) 或反向对 ($j_<, j'_<$)**：
   两者自旋方向平行，受动量空间排斥，张量力表现为**强排斥 ($V_T^{\text{mono}} > 0$)**。

### 2.2 Utsuno SDPF-MU 力分解验证
Y. Utsuno 等人将 SDPF-MU 跨壳有效相互作用严格正交分解为：中心力（Central）、自旋-轨道力（Two-body LS）与张量力（Tensor）。
- 在 Ca 同位素链（$Z=20$）中，随着中子向 $1f_{7/2}$（$j_{n>}$）填充，通过张量力对质子 $1d_{3/2}$（$j_{p<}$）施加强烈吸引，使得质子 $d$ 壳层自旋-轨道劈裂 $\Delta_{\text{SO}} = \epsilon(1d_{3/2}) - \epsilon(1d_{5/2})$ 剧烈减小达 **$2.0\text{ MeV}$**；
- 实验上由单质子敲出反应（Knockout Reactions）测得的光谱因子分布直接证实了该自旋-轨道能隙的塌缩。

---

## 3. 新幻数的出现与传统闭壳的淬灭

在极端丰中子区，张量力驱动的壳演化彻底重塑了核结构版图：
1. **$N=16$ 全新中子幻数确立（$^{24}\text{O}$ 稳定边界）**：
   在氧同位素中，由于质子完全中空（无 $1d_{5/2}$ 质子），中子 $1d_{3/2}$ 失去了来自质子的张量吸引，能级被大幅推高并抛入连续谱，在充满中子 $2s_{1/2}$ 的 $N=16$ 处留下了高达 **$4.8\text{ MeV}$** 的巨型闭壳能隙，确立 $N=16$ 为全新闭壳；
2. **$N=20$ 传统闭壳淬灭与 $^{28}\text{O}$ 连续态破裂**：
   在 $^{28}\text{O}$ 中，$N=20$ 无法维持闭壳，基态处于粒子结合能以上，成为自发发射 4 个中子的宽共振态；
3. **$N=34$ 新幻数确立（$^{54}\text{Ca}$）**：
   中子 $2p_{1/2}$ 与 $1f_{5/2}$ 之间由于张量单极演化拉开高达 $2.5\text{ MeV}$ 的坚硬子壳能隙，为 RIBF 与 FRIB 放射性束流实验所完全确证。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/otsuka-shell-evolution-monopole-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`shell-evolution-monopole` 子命令)
- **上游来源**：`knowledge/sources/book-nuclear-shell-model-70-years.md`
