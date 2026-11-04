# 第 6 章：$^{100}\text{Sn}$ 闭壳近区高自旋谱学、Seniority 异能态与超允许 $\beta$ 衰变

**来源专著**：M. Górska《The Nuclear Shell Model 70 Years after Its Advent》（MDPI 2023）第 10 篇专论
**对应页码**：印刷 pp. 223–242 / 物理 PDF pp. 234–253

---

## 1. 核心理论推导与 $^{100}\text{Sn}$ 双闭壳坚硬度

### 1.1 全核素图最重自共轭自对偶双幻核
$^{100}\text{Sn}$（$Z=50, N=50$）是全核图谱中质子数与中子数严格相等（$N=Z$）且抵抗粒子衰变的最重双闭壳核（Double-Magic Nucleus）：
- **双壳隙硬度**：其质子与中子同时处于完全充满的 $1g_{9/2}$ 闭壳下方，与上方的 $2d_{5/2}, 1g_{7/2}$ 壳层之间具有高达 **$6.5\text{ MeV}$** 的巨型闭壳能隙；
- **超允许巨加莫夫-泰勒衰变（Superallowed GT Decay）**：
  由于质子与中子占据完全相同的单粒子空间波函数轨道，纯质子空穴向纯中子空穴的弱跃迁展示全核图谱最大的相干加莫夫-泰勒强度：
  $$B(\text{GT}; ^{100}\text{Sn} \to {}^{100}\text{In}) \approx 9.1 \pm 3.0,$$
  成为高精度检验轴矢量弱相互作用耦合常数核介质淬灭因子（$g_A$ Quenching）的世界最高灵敏度物理实验室。

---

## 2. $g_{9/2}$ 壳层高自旋 Seniority 异能态动力学

M. Górska 系统解构了 $^{100}\text{Sn}$ 邻近核素（如 $^{98}\text{Cd}, {}^{96}\text{Pd}, {}^{94}\text{Ru}, {}^{95}\text{Rh}$）中的高自旋异能态图谱：

### 2.1 Seniority $v=2$ 与 $v=4$ 异能态阶梯
在纯 $\pi(1g_{9/2})^{-n}$ 质子空穴构型中：
1. **$8^+$ Seniority 异能态**：
   一对质子空穴全顺排耦合为最大可能自旋 $J_m_{\max} = 2j - 1 = 2(9/2) - 1 = 8^+$；
   由于 $8^+ \to 6^+$ 属于带内相同 Seniority（$v=2 \to v=2$）电四极跃迁，受单 $j$ 壳层配对相消因式 $(2j+1-2n)$ 抑制，在 $^{98}\text{Cd}$ 与 $^{96}\text{Pd}$ 中形成微秒级长寿命态；
2. **$^{96}\text{Cd}$ 的 $16^+$ 自旋隙异能态（Spin-Gap Isomer）**：
   四质子空穴组态耦合为最高自旋 $16^+$ 时，由于四体单极势能压低，该态能量反常低于下方的全部中间自旋态（出现能隙陷阱），其主要通过直接发射超强质子衰变退激！

---

## 3. 在束谱学应用：反冲衰变标记 (RDT) 极端微弱通道探测
在合成 $^{100}\text{Sn}$ 邻近极缺中子核实验中：
- 熔合蒸发截面极其微弱（通常仅有微靶 $\mu\text{b}$ 乃至纳靶 $\text{nb}$ 量级）；
- 采用重离子大阵列结合反冲质量分离器（FMA/VAMOS）与反冲衰变标记技术（Recoil Decay Tagging, RDT）：
  将反冲进入焦平面的残核与微秒后发射的特征 $\alpha$ 衰变或高自旋异能态延迟 $\gamma$ 射线建立微秒空间点-时间关联，彻底消除高达数亿倍的强杂质反应本底，成功重构出双闭壳 $^{100}\text{Sn}$ 邻区的完整高自旋核能谱。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/sn100-region-highspin-spectroscopy-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`seniority-isomer` 子命令)
- **上游来源**：`knowledge/sources/book-nuclear-shell-model-70-years.md`
