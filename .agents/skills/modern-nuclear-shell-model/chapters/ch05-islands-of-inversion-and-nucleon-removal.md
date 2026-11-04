# 第 5 章：极端丰中子反转岛与单核子敲出反应动力学

**来源专著**：A. Gade《The Nuclear Shell Model 70 Years after Its Advent》（MDPI 2023）第 9 篇专论
**对应页码**：印刷 pp. 211–222 / 物理 PDF pp. 222–233

---

## 1. 核心理论推导与 $N=40$ 反转岛微观机制

### 1.1 传统次壳闭合向形变反转岛的跃迁
在近稳定线核中，$N=40$ 对应 $2p_{1/2}$ 满壳与上方的 $1g_{9/2}$ 独宇称轨道之间的次壳闭合（如 $^{68}\text{Ni}$ 具有极高 $E(2_1^+) = 2.03\text{ MeV}$，表现出强球形刚性）；
然而当沿 $N=40$ 同中子素链向质子缺乏的极端丰中子区推进（从 $\text{Ni}(Z=28)$ 走向 $\text{Fe}(Z=26)$ 与 $\text{Cr}(Z=24)$）：
1. **质子单极吸引减弱**：$1f_{7/2}$ 质子的移除使得中子 $1g_{9/2}$ 与 $2d_{5/2}$ 轨道大幅向下扎入；
2. **多粒子-多空穴侵入态跨壳凝聚**：中子极易跨越 $N=40$ 壳隙被激发到 $1g_{9/2}$ 轨道形成 $2p-2h$ 甚至 $4p-4h$ 侵入组态；
3. **反转岛爆发（Island of Inversion）**：
   在 $^{64}\text{Cr}$（$Z=24, N=40$）与 $^{62}\text{Cr}$ 中，第一激发能急剧断崖式塌缩至 $E(2_1^+) \approx 420\text{ keV}$，$B(E2)$ 爆发式增长，证实球形基态彻底被强形变侵入基态反转取缔！

---

## 2. 单核子敲出反应与平行运动量分布

A. Gade 系统形式化了在中高能重离子碰撞（$E_{\text{beam}} \sim 80 - 250\text{ MeV/u}$）下利用单核子去除反应（Knockout Reactions）测定弱束缚核波函数组态的方法：

### 2.1 程函近似与核心-旁观者模型 (Eikonal Theory)
高能入射弹核在掠碰轻靶（如 $^{9}\text{Be}$ 或 $^{12}\text{C}$）时，单个价核子被靶核通过核相互作用与库仑作用瞬间剥离，其余残留核心作为旁观者（Spectator）自由飞出：
- **总敲出反应截面**：
  $$\sigma_{-1N}^{\text{th}} = \sum_{nlj} S(nlj) \cdot \sigma_{\text{sp}}(nlj, S_N^{\text{eff}}),$$
  其中 $S(nlj)$ 为微观壳模型波函数单粒子光谱因子，$\sigma_{\text{sp}}$ 为单粒子程函吸收截面。

### 2.2 出射残核平行运动量分布 $p_\parallel$
残核在束流方向的纵向动量分布半高全宽（FWHM）完全直接反映被剥离核子在母核内的空间波函数动量分布（由角动量 $l$ 唯一决定）：
- 若剥离的是 $s$ 轨道核子（$l=0$）：动量分布极其狭窄（$\text{FWHM} \sim 50\text{ MeV}/c$）；
- 若剥离的是 $p$ 轨道或 $d$ 轨道核子（$l=1, 2$）：动量分布显著拓宽（$\text{FWHM} \sim 150 - 250\text{ MeV}/c$）；
- 实验测定 $p_\parallel$ 线形，可完全无歧义锁定参与组态混合的微观单粒子轨道量子数。

---

## 3. 在束谱学应用：光谱因子淬灭因子 $R_s$ 普适系统学
实验测得敲出截面与理论壳模型截面之比定义为淬灭因子：$R_s \equiv \sigma_{\text{exp}} / \sigma_{\text{th}}$。
- Gade 等人确立了 $R_s$ 随核子结合能不对称度 $\Delta S = S_n - S_p$（或 $S_p - S_n$）的强相关衰减规律；
- 在极度不对称的深度束缚价核子去除中，短程排斥关联与张量力促使 $R_s$ 下降至 $\sim 0.3 - 0.5$；而在极弱束缚价核子去除中 $R_s \to 1.0$，为检验滴线外反转岛侵入纯度提供了普适微观判据。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/n40-island-nucleon-removal-shell-model-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`halo-breakup` 子命令)
- **上游来源**：`knowledge/sources/book-nuclear-shell-model-70-years.md`
