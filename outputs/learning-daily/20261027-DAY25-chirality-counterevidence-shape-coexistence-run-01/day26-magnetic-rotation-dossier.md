---
type: preview-dossier
graph-excluded: true
created: 2026-10-27
day_index: 25
preview_day_index: 26
status: uncredited-preview
title: "Day 26 磁转动与剪刀机构专项预习档案：135Pr 负宇称高自旋带、TAC 微观动力学与电磁跃迁解析"
tags: [magnetic-rotation, shears-mechanism, 135Pr, TAC, B(M1), high-spin, A130]
---

# Day 26 磁转动与剪刀机构专项预习档案：$^{135}\text{Pr}$ 负宇称高自旋带、TAC 微观动力学与电磁跃迁解析

> **执行身份与前置预习声明**：
> 本档案由 Day 26 专项预习 Subagent（`subagent_day26_mr`）独立构建，作为 Day 25 运行期间（距 15:00 硬截止充足）依据课程守卫规则展开的下一日课程卡（Day 26）无学分前置预习。
> 本预习严格遵守 Wiki 契约，保持今日 `day_index: 25`，列入 `partial_day_indices: [26]`，不提前索取 Day 26 正式学分，不将课程主线推进至 Day 27，不执行 `git commit` 或 `git push`。正式学分留待正式 Day 26 自身运行。

---

## 1. 核心研究对象与实验谱系：Garg 2015 $^{135}\text{Pr}$ 纲图

### 1.1 实验装置与采集身份
- **基准来源**：R. Garg *et al.*, *Phys. Rev. C* **92**, 054325 (2015), DOI: `10.1103/PhysRevC.92.054325`（原件存储于 `raw/papers/gpt/high-spin-20260920/纲图/2015_Garg et al_Negative-parity high-spin states and a possible magnetic rotation band in Pr 76.pdf`）；
- **核反应与靶系统**：在印度大学间加速器中心（IUAC, New Delhi）利用 15-UD Pelletron 加速器提供 $82\text{ MeV}$ 的 $^{16}\text{O}$ 束流，轰击自支撑 $^{123}\text{Sb}$ 靶（厚度 $800\,\mu\text{g/cm}^2$，背衬 $10\text{ mg/cm}^2$ 天然 Au），通过 $^{123}\text{Sb}(^{16}\text{O}, 4n)^{135}\text{Pr}$ 熔合蒸发反应布居高自旋态；
- **探测阵列（INGA）**：由 15 台四叶草高纯锗探测器（Clover HPGe）组成印第安国家 $\gamma$ 阵列（INGA），探测器分布在 5 个极角环：$32^\circ$ (3台)、$57^\circ$ (2台)、$90^\circ$ (4台)、$123^\circ$ (2台) 和 $148^\circ$ (4台)，靶点到晶体前表面距离为 $25\text{ cm}$。共记录约 $3 \times 10^8$ 个三重及更高重数（fold $\ge 3$）符合事件；
- **与 Matta 2015 采集的严格区分**：Matta 2015 实验基于 TIFR-Pelletron 的 $80\text{ MeV}$ $^{16}\text{O} + ^{123}\text{Sb}$ 反应，阵列构型与电子学响应不同；两者虽共享母核与反应类型，但属于完全独立的实验测量（见 `knowledge/sources/garg-2015-135pr-magnetic-rotation.md` GA15-4）。

### 1.2 负宇称带 3（Band 3）能级与跃迁网络
Garg 2015 建立的负宇称高自旋带（Band 3）自旋从 $I^\pi = 27/2^-$ 延伸至 $(43/2^-)$，激发能跨度为 $3530.0\text{ keV}$ 至 $7110.4\text{ keV}$：
- **带头与低激发跃迁**：
  - $3530.0\text{ keV}$ ($27/2^-$) 态通过新发现的 $149.5\text{ keV}$ 纯偶极线（$R_{\text{DCO}} = 0.50(4)^Q$）退激至 $25/2^{(-)}$ 态；
  - $3863.0\text{ keV}$ ($29/2^-$) $\xrightarrow{332.9\text{ keV}} 27/2^-$：$I_\gamma = 13.1(3)$，$R_{\text{DCO}} = 0.47(3)^Q$，$\Delta = -0.03(8)$（确立为 $M1$）；
  - $4292.7\text{ keV}$ ($31/2^-$) $\xrightarrow{429.7\text{ keV}} 29/2^-$：$I_\gamma = 11.0(3)$，$R_{\text{DCO}} = 0.45(3)^Q$，$\Delta = -0.05(6)$（确立为 $M1$）；
  - $4704.1\text{ keV}$ ($33/2^-$) $\xrightarrow{410.8\text{ keV}} 31/2^-$：$I_\gamma = 7.60(24)$，$R_{\text{DCO}} = 0.51(7)^Q$，$\Delta = -0.16(10)$（确立为 $M1$）；
  - $5028.6\text{ keV}$ ($35/2^-$) $\xrightarrow{325.1\text{ keV}} 33/2^-$：$I_\gamma = 10.83(25)$，$R_{\text{DCO}} = 1.28(5)^D$，$\Delta = -0.12(6)$（确立为 $M1$）；
  - $5452.6\text{ keV}$ ($37/2^-$) $\xrightarrow{424.0\text{ keV}} 35/2^-$：$I_\gamma = 4.80(13)$，$R_{\text{DCO}} = 0.33(4)^Q$，$\Delta = -0.15(9)$（确立为 $M1$）；
  - $5951.1\text{ keV}$ ($39/2^-$) $\xrightarrow{498.5\text{ keV}} 37/2^-$：$I_\gamma = 4.88(16)$，$R_{\text{DCO}} = 0.83(4)^D$，$\Delta = -0.14(7)$（确立为 $M1$）；
  - $6506.4\text{ keV}$ ($41/2^{(-)}$) $\xrightarrow{555.3\text{ keV}} 39/2^-$：$I_\gamma = 1.7(2)$，$R_{\text{DCO}} = 0.87(14)^D$；
  - $7110.4\text{ keV}$ ($(43/2^-)$) $\xrightarrow{604.0\text{ keV}} 41/2^{(-)}$：暂定延伸线；
- **观测到的关键跨级 $\Delta I = 2$ 跃迁（$E2$ Crossovers）**：
  - $4292.7\text{ keV}$ ($31/2^-$) $\xrightarrow{762.7\text{ keV}} 27/2^-$：$I_\gamma = 1.58(8)$；
  - $4704.1\text{ keV}$ ($33/2^-$) $\xrightarrow{840.6\text{ keV}} 29/2^-$：$I_\gamma = 1.63(7)$；
  - $5028.6\text{ keV}$ ($35/2^-$) $\xrightarrow{735.9\text{ keV}} 31/2^-$：$I_\gamma = 0.50(3)$。
- **高自旋交叉缺失**：在 $I > 35/2^-$ 之上的更高自旋态，由于带交叉后分支极弱，全谱未观测到更高能的跨级 $E2$ 跃迁。

---

## 2. 倾斜轴推转（TAC）微观构型与角动量排布

### 2.1 质子颗粒与中子空穴的几何取向
$^{135}\text{Pr}$ 包含 $Z = 59$ 个质子与 $N = 76$ 个中子：
1. **质子费米面与短轴驱动**：
   - 质子数 $Z = 59$ 位于 $Z = 50$ 闭壳之上的 9 个质子，最后一个未配对奇质子占据侵入轨道 $h_{11/2}$ 的底部；
   - 在长椭球/弱三轴势阱中，低 $\Omega$ 轨道（如 $\Omega = 1/2^-, 3/2^-$）的波函数波包主要分布在赤道面，其单粒子轨道角动量矢量倾向于**沿核形状的短轴（short axis）** 对齐；
2. **中子费米面与长轴驱动**：
   - 中子数 $N = 76$ 距离 $N = 82$ 满壳缺少 6 个中子，属于准粒子空穴态（quasiparticle holes）；
   - 费米面切入中子 $h_{11/2}$ 壳层的高 $\Omega$ 区域（如 $\Omega = 9/2^-, 11/2^-$）；
   - 高 $\Omega$ 轨道中子空穴与长椭球核芯的相互作用驱动其单粒子角动量矢量倾向于**沿核形状的长轴（long axis）** 对齐；
3. **初始垂直取向（Orthogonal Configuration）**：
   - 质子角动量 $\vec{j}_\pi$ 沿短轴，中子空穴角动量 $\vec{j}_\nu$ 沿长轴，两者在三维空间中形成接近 $90^\circ$ 的正交几何结构；
   - 这种正交各向异性导致了内禀磁偶极矢量的非零横向分量，构成了磁转动（剪刀机构）的内禀微观温床。

### 2.2 3-qp 与 5-qp 构型演化及带交叉动力学
Garg 2015 采用 Frauendorf 混合版 TAC 模型（Hybrid Tilted-Axis Cranking）对该带进行了自洽数值模拟：
- **交叉前低自旋区（3-qp 构型）**：
  $$\text{Configuration: } \pi(h_{11/2})^1 \otimes \nu(h_{11/2})^{-2}$$
  - 配对能隙取实验奇偶质量差的 80%：$\Delta_p = 1.08\text{ MeV}, \Delta_n = 0.764\text{ MeV}$；
  - 自洽极小能量点对应的势能形变参量为：$\varepsilon_2 = 0.14, \gamma = 62^\circ$；
  - 平均转动轴倾斜角为 $\theta = 31.6^\circ$（相对于长轴）。
- **交叉后高自旋区（5-qp 构型）**：
  $$\text{Configuration: } \pi(h_{11/2})^1(g_{7/2})^2 \otimes \nu(h_{11/2})^{-2}$$
  - 在角频率 $\hbar\omega \approx 0.37\text{ MeV}$（对应自旋 $I \approx 33/2^-\hbar$）处，质子壳层发生破对，一对 $(g_{7/2})$ 质子发生旋转对齐（alignment），形成 5-qp 构型；
  - 极小形变维持在 $\varepsilon_2 = 0.14, \gamma = 60^\circ$；
  - 倾斜角缩小为 $\theta = 26.9^\circ$。
- **与邻核 $^{137}\text{Pr}$ 的同位素系统学对比**：
  - 在 $^{137}\text{Pr}$ ($N=78$) 中，同类偶极带的交叉频率与自旋分别为 $\hbar\omega \approx 0.42\text{ MeV}, I \approx 35/2^-\hbar$；
  - 交叉自旋与频率的系统学延迟，反映了随着中子数从 $N=76$ 增加到 $N=78$，中子费米面进一步上升向 $N=82$ 闭壳靠近，占据不同 $\Omega$ 的 $h_{11/2}$ 轨道，从而改变了配对阻抗与对齐动力学。

---

## 3. 剪刀机构几何动力学严格推导

### 3.1 角动量闭合几何关系
设质子颗粒总角动量为 $\vec{j}_\pi$，中子空穴总角动量为 $\vec{j}_\nu$。在弱形变核中，核芯集体转动角动量 $\vec{R}$ 的贡献受到极大的转动惯量抑制（$\mathcal{J}_{\text{core}}$ 较小），总角动量主要由高 $j$ 准粒子的相对取向生成：
$$\vec{I} = \vec{j}_\pi + \vec{j}_\nu + \vec{R} \approx \vec{j}_\pi + \vec{j}_\nu$$

定义剪刀角（shears angle）$\theta_s$ 为两组单粒子角动量矢量的夹角：
$$\cos\theta_s = \frac{\vec{j}_\pi \cdot \vec{j}_\nu}{|\vec{j}_\pi||\vec{j}_\nu|}$$

总角动量的大小由余弦定理给出：
$$I^2 = j_\pi^2 + j_\nu^2 + 2 j_\pi j_\nu \cos\theta_s$$

在对称或近对称剪刀刃近似下（$j_\pi \approx j_\nu = j$）：
$$I^2 = 2 j^2 (1 + \cos\theta_s) = 4 j^2 \cos^2\left(\frac{\theta_s}{2}\right)$$
开方即得剪刀机构的核心运动学闭合公式：
$$I = 2 j \cos\left(\frac{\theta_s}{2}\right) = (j_\pi + j_\nu) \cos\left(\frac{\theta_s}{2}\right)$$

当体系处于带头（bandhead）时，两叶剪刀处于初始近正交状态（$\theta_s \approx 90^\circ$），角动量为：
$$I_{\text{bandhead}} \approx \sqrt{j_\pi^2 + j_\nu^2} \approx \sqrt{2} j$$
随着转动激发能量注入体系，角动量的增加**并非**依靠核芯加速旋转（$\omega$ 增大），而是通过剩余两体相互作用克服有效摩擦力，驱动 $\vec{j}_\pi$ 与 $\vec{j}_\nu$ 逐步向总角动量 $\vec{I}$ 方向靠拢闭合。当 $\theta_s \to 0^\circ$ 时，剪刀完全闭合，达到带终止自旋：
$$I_{\text{max}} = j_\pi + j_\nu$$

---

## 4. 电磁跃迁几率解析推导：$B(M1)$ 随自旋的单调陡降

### 4.1 内禀磁偶极矩及其空间正交分解
原子核的总磁偶极算符由质子和中子的有效回转比（有效 $g$ 因子）线性组合给出：
$$\vec{\mu} = g_\pi \vec{j}_\pi + g_\nu \vec{j}_\nu + g_R \vec{R}$$
忽略微弱的核芯项（$g_R \vec{R} \approx 0$），将磁偶极矩沿总角动量方向的单位矢量 $\vec{e}_I = \vec{I}/I$ 进行正交投影分解：
$$\vec{\mu} = \vec{\mu}_\parallel + \vec{\mu}_\perp$$
其中：
$$\vec{\mu}_\parallel = (\vec{\mu} \cdot \vec{e}_I) \vec{e}_I$$
$$\vec{\mu}_\perp = \vec{\mu} - (\vec{\mu} \cdot \vec{e}_I) \vec{e}_I$$

#### 物理含义剖析：
- **平行分量 $\vec{\mu}_\parallel$**：在经典转动参考系中与转动轴重合，对空间静态取向贡献静态磁偶极矩 $\mu_{\text{static}} = \langle I, M=I | \mu_z | I, M=I \rangle$。根据电磁跃迁选择定则，静态分量对 $\Delta I = 1$ 的辐射跃迁矩阵元没有贡献；
- **垂直分量 $\vec{\mu}_\perp$**：在核转动过程中绕总角动量 $\vec{I}$ 快速进动，破坏了空间对称性，构成了旋转磁偶极电流辐射源。**所有 $\Delta I = 1$ 的磁偶极跃迁强度 $B(M1)$ 均完全由 $\vec{\mu}_\perp$ 的模长平方决定**。

### 4.2 垂直偶极分量 $\mu_\perp$ 的严格代数推导
由几何关系，$\vec{j}_\pi$ 与 $\vec{j}_\nu$ 到 $\vec{I}$ 垂直方向的投影大小分别为：
$$j_{\pi,\perp} = j_\pi \sin\theta_\pi, \quad j_{\nu,\perp} = j_\nu \sin\theta_\nu$$
根据矢量闭合条件 $\vec{I} = \vec{j}_\pi + \vec{j}_\nu$，在垂直于 $\vec{I}$ 的方向上两投影大小必须严格相等且反向：
$$j_{\pi,\perp} = j_{\nu,\perp} \implies j_\pi \sin\theta_\pi = j_\nu \sin\theta_\nu$$
利用正弦定理：
$$\frac{\sin\theta_\pi}{j_\nu} = \frac{\sin\theta_\nu}{j_\pi} = \frac{\sin\theta_s}{I}$$
因此垂直分量的大小为：
$$j_{\perp} = \frac{j_\pi j_\nu}{I} \sin\theta_s$$

代入磁偶极矩算符表达式，由于质子与中子在垂直方向反向排列：
$$\vec{\mu}_\perp = g_\pi \vec{j}_{\pi,\perp} + g_\nu \vec{j}_{\nu,\perp} = (g_\pi - g_\nu) \vec{j}_{\pi,\perp}$$
取其绝对模长：
$$\mu_\perp = |g_\pi - g_\nu| \frac{j_\pi j_\nu}{I} \sin\theta_s$$

在对称剪刀近似下（$j_\pi \approx j_\nu = j, I = 2j \cos(\theta_s/2)$）：
$$\mu_\perp = |g_\pi - g_\nu| \frac{j^2}{2j \cos(\theta_s/2)} \cdot 2 \sin\left(\frac{\theta_s}{2}\right) \cos\left(\frac{\theta_s}{2}\right) = |g_\pi - g_\nu| j \sin\left(\frac{\theta_s}{2}\right)$$

### 4.3 约化跃迁几率 $B(M1)$ 的解析表达式与熄灭行为
在半经典推转几何极限下（Frauendorf 1993, 2001; Clark & Macchiavelli 2000）：
$$B(M1; I \to I-1) = \frac{3}{8\pi} \mu_\perp^2$$
代入上式即得经典剪刀跃迁强度定理：
$$B(M1; I \to I-1) = \frac{3}{8\pi} (g_\pi - g_\nu)^2 j^2 \sin^2\left(\frac{\theta_s}{2}\right)$$

利用几何闭合关系 $\cos(\theta_s/2) = I / (2j) = I / I_{\text{max}}$，可将角度完全消去，表达为总自旋 $I$ 的显式函数：
$$\sin^2\left(\frac{\theta_s}{2}\right) = 1 - \cos^2\left(\frac{\theta_s}{2}\right) = 1 - \frac{I^2}{I_{\text{max}}^2}$$
从而得到标志性的解析熄灭抛物线方程：
$$B(M1; I \to I-1) = \frac{3}{8\pi} (g_\pi - g_\nu)^2 j^2 \left( 1 - \frac{I^2}{I_{\text{max}}^2} \right)$$

#### 物理性质总结：
1. **陡峭单调下降**：当自旋 $I$ 较小时（带头区），剪刀角张开较大，$\sin^2(\theta_s/2)$ 接近 $0.5$，$B(M1)$ 达到极大值（通常可达数个 $\mu_N^2$）；随着自旋 $I$ 增加，剪刀刃不断闭合，$\sin^2(\theta_s/2)$ 单调下降，导致 $B(M1)$ 呈现特征性的剧烈暴跌；
2. **带终止零点**：在剪刀完全对齐时（$I = I_{\text{max}}$），$\mu_\perp$ 完全消失为零，$B(M1) \to 0$，磁辐射通道被几何严格熄灭；
3. **电四极跃迁 $B(E2)$ 的惰性**：由于核芯四极形变弱（$\varepsilon_2 \approx 0.14$）且集体四极流未沿主对称轴旋转，带内 $\Delta I = 2$ 的 $B(E2)$ 极为微弱（通常只有几个 W.u.，远小于正常转动带的上百 W.u.）；
4. **电磁跃迁比 $B(M1)/B(E2)$ 的演化**：
   $$\frac{B(M1)}{B(E2)} \propto \frac{(g_\pi - g_\nu)^2 \left(1 - \frac{I^2}{I_{\text{max}}^2}\right)}{Q_0^2 \cos^2\left(\frac{\theta_s}{2} + \gamma\right)}$$
   在低激发区比值高达 $10–50\,\mu_N^2/(e^2\text{b}^2)$，并随自旋增加剧烈下跌，构成了实验上搜寻剪刀机构的重要判据。

---

## 5. A≈130 质量区高自旋四类模式全面鉴别矩阵

为了消除文献中长期存在的概念混淆，建立磁转动（MR）、反磁转动（AMR）、晃动运动（Wobbling）与手征双重带（Chirality）的系统鉴别矩阵：

| 鉴别维度 | 磁转动 (MR) | 反磁转动 (AMR) | 晃动运动 (Wobbling) | 手征双重带 (Chirality) |
|---|---|---|---|---|
| **角动量空间拓扑** | 平面单剪刀：质子颗粒与中子空穴在同一转动平面内非对称闭合 | 对称双剪刀：两对相反质子/中子在平面内向总自旋对称双向闭合 | 三轴刚体主轴微振动：总角动量绕最大惯量轴进动晃动 | 非共面三脚架：核心、质子、中子角动量互不共面，破坏空间手征反演 |
| **典型微观配态** | $\pi h_{11/2} \otimes \nu h_{11/2}^{-2}$（奇奇核或奇核多准粒子） | $\pi (h_{11/2})^2 \otimes \nu (h_{11/2})^{-2}$（偶偶或近球形奇 $A$ 核） | $\pi h_{11/2} \otimes \mathcal{R}_{\text{triaxial}}$（单准粒子三轴奇核） | $\pi h_{11/2} \otimes \nu h_{11/2}^{-1} \otimes \mathcal{R}$（奇奇核三轴高自旋） |
| **典型案例核素** | $^{135}\text{Pr}$ (Band 3), $^{137}\text{Pr}$, $^{142}\text{Gd}$, $^{198}\text{Pb}$ | $^{105}\text{Cd}$, $^{106}\text{Cd}$, $^{108}\text{Cd}$, $^{110}\text{In}$ | $^{135}\text{Pr}$ (Band 4 争议), $^{130}\text{Ba}$, $^{187}\text{Au}$ | $^{134}\text{Pr}$, $^{135}\text{Nd}$, $^{136}\text{Nd}$, $^{106}\text{Ag}$ |
| **$\Delta I = 1$ 跃迁电磁性质** | 极强磁偶极 $M1$（纯度近 $100\%$），$\Delta I=1$ 阶梯占据绝对支配地位 | **严格禁戒/相消**：对称双剪刀横向磁偶极矩 $\vec{\mu}_\perp$ 恒等于零 | 弱 $M1$、强 $E2$ 混合（带间 $M1$ 受到结构抑制，跨带 $E2$ 增强） | 强 $M1$ 与 $E2$ 共存：两手征伙伴带之间存在强跨带 $M1$ 和 $E2$ 连接 |
| **$\Delta I = 2$ 跃迁电磁性质** | 极弱或实验不可测（$1–10\text{ W.u.}$），无核芯集体增强 | 规则强 $E2$ 阶梯：带内全部为连续的 $\Delta I = 2$ 跃迁 | 强集体带内 $E2$（典型值 $50–200\text{ W.u.}$），保持转子阶梯 | 双重带内均具有完全对称的高集体性 $\Delta I=2$ $E2$ 阶梯 |
| **跃迁几率自旋演化** | $B(M1)$ 随自旋剧烈单调下降；$B(E2)$ 维持小常数或微弱变化 | $B(E2)$ 随自旋单调下降（双剪刀闭合使电荷多极流动减弱） | $B(E2_{\text{out}})/B(E2_{\text{in}}) \propto 1/I$（随自旋特征性下降） | $B(M1)$ 与 $B(E2)$ 在两带间呈现近简并或交错演化 |
| **特征能量学标志** | 转动惯量比 $\mathcal{J}^{(2)}/B(E2)$ 极大（可超数百 $\hbar^2\text{MeV}^{-1}(eb)^{-2}$） | 规则转动抛物线 $E(I) - E_0 \propto I(I+1)$，动力学惯量随自旋下降 | 晃动频率 $E_{\text{wob}}(I) = E_n(I) - E_{n-1}(I-1)$ 呈特征上升或下降 | 双重带能谱近简并：$\Delta E(I) = E_2(I) - E_1(I) \to 0$ 且具有相同转动惯量 |
| **自发对称性破缺** | 空间旋转对称性被内禀各向异性磁流破坏，但保持磁参考平面对称 | 保持中心反演对称性（$\mathcal{P}$），横向磁偶极被相消恢复 | 空间三主轴旋转对称性破缺，角动量形成离轴进动极化 | 空间手征对称性破缺：内禀系具有左手/右手对应手征手性 |

---

## 6. $^{135}\text{Pr}$ 实验边界：缺乏绝对寿命时磁转动判据的降级规范

### 6.1 Garg 2015 实验覆盖度与局限性
Garg *et al.* (2015) 依靠高质量的 INGA Clover 阵列完成了扎实的能谱学观测：
1. **已证实验事实**：
   - 建立了包含 9 个能级、能量延伸至 $7110\text{ keV}$ 的规则 $\Delta I = 1$ 负宇称能带（Band 3）；
   - 通过 RDCO 与 IPDCO 线性极化不对称度 $\Delta$，明确测定了 6 条带内跃迁的磁偶极（$M1$）性质；
   - 测得了 3 条跨级 $\Delta I = 2$ 的 $E2$ 交叉跃迁（736, 763, 841 keV），证实了高 $B(M1)/B(E2)$ 现象。
2. **关键缺失观测量（Fatal Missing Observables）**：
   - **无皮秒/飞秒寿命测量**：由于轻离子反应（$^{16}\text{O}$）动量转移有限，加之厚金衬底靶设计，未实施多普勒频移衰减法（DSAM）或反冲距离多普勒平移法（RDDS）测量；
   - **绝对 $B(M1)$ 与 $B(E2)$ 全面缺失**：实验无法提供任何一个态的绝对跃迁几率数值；
   - **带交叉后比值断裂**：在 $I > 35/2^-$ 的高自旋区，由于跨级 $E2$ 计数极低，连相对比值 $B(M1)/B(E2)$ 都无法继续提取。

### 6.2 混淆风险与伪剪刀假说
仅凭“强 $M1$ 阶梯”与“高 $B(M1)/B(E2)$ 比值”绝不足以作为磁转动的充要判据，存在以下难以排除的竞争解释：
1. **大 $K$ 准粒子轨道与旋称混合（Signature Mixing）**：
   当奇核或奇奇核处于大 $K$ 尼尔森轨道（如高 $\Omega$ 组态）时，较强的内禀非轴对称或科里奥利力混合能够引发极强的带内 $\Delta I = 1$ $M1$ 跃迁，同时微弱的四极集体形变亦会导致较小的 $B(E2)$，从而伪造出类似剪刀带的强偶极阶梯；
2. **分母驱动的比值单调下降**：
   实验测得的 $B(M1)/B(E2)$ 随自旋下降，在数学上包含两种独立机制：
   - 分子 $B(M1)$ 下降（剪刀闭合，真实磁转动）；
   - 分母 $B(E2)$ 增加（形状随转动被离心驱动伸长，常规转子行为）。
   在缺乏绝对寿命的情况下，无法判定下降趋势究竟来自于剪刀闭合还是核形变演化；
3. **TAC 拟合的非唯一性**：
   TAC 模型中引入的 3-qp/5-qp 构型、形变参数（$\varepsilon_2 = 0.14, \gamma \approx 60^\circ$）以及平均倾斜角 $\theta$，均带有显著的唯象参数依赖性。能级和推转频率的吻合不能直接等同于微观剪刀闭合机制的物理证实。

### 6.3 科学结论降级与证据准则
依据 Wiki 严格的证据分层契约：
- **禁止过度推断**：不得将 Garg 2015 报告的“a *possible* magnetic rotation band”升格为“确立的磁转动带（established MR band）”；
- **定级规范**：$^{135}\text{Pr}$ 的 Band 3 必须严格保留在 **“候选磁转动带（Candidate / Possible Magnetic Rotation Band）”** 级别；
- **终审准据**：只有在未来完成高质量薄靶反冲实验，测得皮秒级能级寿命 $\tau(I)$，并确证 **绝对 $B(M1)$ 随自旋呈现单调陡峭下降** 且 **绝对 $B(E2) \sim \text{few W.u.}$ 保持极微弱** 时，方可完成向确立磁转动的科学升格。

---

## 7. 档案交付与可追溯索引
- **文档路径**：`outputs/learning-daily/20261027-DAY25-chirality-counterevidence-shape-coexistence-run-01/day26-magnetic-rotation-dossier.md`；
- **关联来源**：
  - [[garg-2015-135pr-magnetic-rotation]]（GA15-1 至 GA15-14）；
  - [[magnetic-rotation]]；
  - [[antimagnetic-rotation]]；
  - [[tilted-axis-cranking]]；
  - [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]；
  - [[hubel-2005-magnetic-rotation-review]]。
