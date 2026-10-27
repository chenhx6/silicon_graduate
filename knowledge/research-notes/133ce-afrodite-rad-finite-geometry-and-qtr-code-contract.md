---
type: research-note
title: "133Ce AFRODITE 阵列几何、全探测器门 RAD 算符偏差与 QTR 代码链输入合同"
aliases: [133Ce AFRODITE RAD and QTR contract, AFRODITE有限角门与GAMPN-ASYMO-PROBMO合同]
created: 2026-10-27
updated: 2026-10-27
status: active
review_status: unreviewed
confidentiality: public
tags: [133ce, afrodite, rad, dco, qtr, gampn, asymo, probmo, analysis-blueprint]
---

# $^{133}\text{Ce}$ AFRODITE 阵列几何、全探测器门 $R_{AD}$ 算符偏差与 QTR 代码链输入合同

## 1. 核心问题与研究背景

在针对 $^{133}\text{Ce}$ 高自旋能带结构与三轴形变开展深入学习（[[133ce-thesis-analysis-blueprint]]、[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]]，WK22）的过程中，为了使学位论文方法真正转化为可迁移、可复现的专业数据分析能力，必须彻底厘清实验数据采集与理论模型输入两个层面的底层合同：
1. **探测器阵列几何与角分布比率**：AFRODITE 探测器阵列的实际 Clover 数量在同源文献中存在 8 个与 13 个的分歧；同时，实验采用的“全探测器门角分布比率”（$R_{AD}$）常被散文简化为“完全不依赖门跃迁多极性”，其实际有效性依赖于有限立体角积分的对称性近似。
2. **三轴粒子-转子模型（QTR）代码链输入合同**：基于 Ragnarsson–Semmes（RS88）谱系的 GAMPN $\to$ ASYMO $\to$ PROBMO 程序链，其形变参数存在 $\varepsilon_4 = 0.1$ 与 $0.01$ 的字面冲突；单粒子能量与化学势 $\lambda_F$ 存在跨主振子壳层（$N=4$ 与 $N=5$）的零点对齐机制，直接决定 BCS 配对与准粒子演化。

---

## 2. AFRODITE 探测器几何与实验 Run 配置同源分歧

### 2.1 文献报道的分歧对照

对于 $^{125}\text{Te}(^{12}\text{C}, 4n)^{133}\text{Ce}$（$E_{\text{beam}} = 57\text{ MeV}$，iThemba LABS 分离扇回旋加速器）实验：
- **Ding et al. 2021 (*Phys. Rev. C* 103, 034311)**：
  正文明确描述 AFRODITE 阵列由 **8 个 Compton-suppressed Clover 探测器** 组成，分别位于 $90^\circ$（4 个）和 $135^\circ$（4 个）；
- **Wakudyanaye 2022 学位论文**：
  - **第 4.5 节（通用阵列介绍，PDF 54）**：描述 AFRODITE 基本框架为“8 个 Clover（4@90°, 4@135°）外加 7 个 LEPS 探测器（2@45°, 3@90°, 2@135°）”，并注明“近期已升级至 17 个 Clover”；
  - **第 5.2.1 节（具体实验细节，PDF 61）**：明确写道：“...measured with the AFRODITE array which consists of **thirteen Compton-suppressed clover detectors arranged in three rings at $45^\circ$ (one clover), $90^\circ$ (eight clovers) and $135^\circ$ (four clovers)** with respect to the beam direction.”

### 2.2 事件计数与同源性线索

两篇文献报告的完全相同的统计量表明它们基于同一批物理数据：
- 双符合事件数：$2.8 \times 10^{10}$；
- 三重及更高阶符合事件数：$5.4 \times 10^9$。

**物理与离线排序审计**：
1. **活动探测器掩模（Active Detector Mask）**：在离线构建 $\gamma$-$\gamma$ 符合矩阵时，位于 $45^\circ$ 的单 Clover 探测器由于缺少对称环伙伴，其立体角较小且几何不对称；若分析人员未对 $45^\circ$ 探测器加门，仅将其作为辅助符合线，或在某些矩阵排序（sorting）中关闭了 $45^\circ$ 通道，则实际参与对称矩阵构建的有效阵列仍等效于特定子集；
2. **角响应不可跨阵列移植**：由于探测器环角设置（$45^\circ, 90^\circ, 135^\circ$）及各环 Clover 数目不同，本实验的峰位效率响应曲线、极化不对称度响应与角关联接收度完全特定于本次 iThemba LABS run，**绝对禁止将该阵列的比值阈值套用到 GALILEO、EUROBALL、Gammasphere 或 INGA 实验中**。

---

## 3. 全探测器门 $R_{AD}$ 算符与有限阵列角关联偏差的解析推导

### 3.1 定向态角关联理论基础

在重离子熔合蒸发反应中，余核角动量高度取向于垂直束流轴（$z$ 轴）的平面内（高斯磁子能级分布 $P(m) \propto \exp[-m^2/(2\sigma^2)]$）。两连发级联跃迁 $\gamma_1 - \gamma_2$ 的符合角关联由五维几何与统计张量决定：
$$W(\theta_1, \theta_2, \phi) = \sum_{k_1, k_2, k} A_{k_1 k_2}^k \, P_{k_1}(\cos\theta_1) P_{k_2}(\cos\theta_2) + \text{干涉项}$$
其中 $\theta_1, \theta_2$ 分别为两光子相对于束流方向的极角，$\phi$ 为二者相对方位角。

### 3.2 理想 $4\pi$ 连续积分极限下的消去定理

若门跃迁 $\gamma_2$ 在整个 $4\pi$ 空间进行无偏均匀积分：
$$\int_{4\pi} W(\theta_1, \theta_2, \phi) \, d\Omega_2 = 4\pi \, W_1(\theta_1)$$
其中 $W_1(\theta_1) = A_0 [1 + a_2 P_2(\cos\theta_1) + a_4 P_4(\cos\theta_1)]$ 是未加门时单一光子 $\gamma_1$ 从定向核发射的纯粹角分布。

**理论推论**：
在连续 $4\pi$ 积分下，门跃迁 $\gamma_2$ 的多极性（无论是四极 $E2$、偶极 $M1$ 还是混合跃迁）其各向异性项在角积分中完全为零（$\int P_k(\cos\theta_2) d\Omega_2 = 0, \, k \ge 2$）。因此，理想“全空间门角分布比率”：
$$R_{AD}^{4\pi} \equiv \frac{W_1(135^\circ)}{W_1(90^\circ)} = \frac{1 + a_2 P_2(\cos 135^\circ) + a_4 P_4(\cos 135^\circ)}{1 + a_2 P_2(\cos 90^\circ) + a_4 P_4(\cos 90^\circ)}$$
该比值**严格独立于门跃迁 $\gamma_2$ 的多极性**，仅由观察跃迁 $\gamma_1$ 自身的多极性 $L$、混合比 $\delta$ 及初态取向程度 $\sigma/I$ 唯一决定。

### 3.3 有限离散探测器阵列的残余偏置

在实际实验中，“all-detectors gate”并非 $4\pi$ 积分，而是有限离散探测器的代数求和：
$$I_{\gamma_1}(\theta_1, \text{gate in all}) = \sum_{j \in \text{detectors}} \epsilon_j \, \Omega_j \, W(\theta_1, \theta_j, \phi_{1j})$$
此时角分布比率变为：
$$R_{AD}^{\text{finite}} = \frac{\sum_j \epsilon_j \Omega_j W(135^\circ, \theta_j, \phi_{1j})}{\sum_j \epsilon_j \Omega_j W(90^\circ, \theta_j, \phi_{1j})}$$

**离散残余偏差分析**：
1. **立体角权重失衡**：在 AFRODITE 阵列中，第 5.2.1 节报告 8 个 Clover 位于 $90^\circ$，仅 4 个 Clover 位于 $135^\circ$（数量比 2:1）。在全探测器门中，$90^\circ$ 探测器捕获的门事件占总门事件的 $\sim 60\%–70\%$；
2. **残余关联项**：
   $$R_{AD}^{\text{finite}} = R_{AD}^{4\pi} \left[ 1 + \Delta_{\text{geom}}(\gamma_2) \right]$$
   若门跃迁 $\gamma_2$ 是一条强烈各向异性的纯 $E2$ 跃迁（$a_2 \approx +0.3$），其在 $90^\circ$（$P_2(0) = -0.5$）的产额比 $135^\circ$（$P_2(-1/\sqrt{2}) = +0.25$）低约 $25\%$。由于 $90^\circ$ 探测器权重过大，导致求和中偶极分量与四极分量无法精确抵消，产生数个百分点的微观残余偏移 $\Delta_{\text{geom}}$；
3. **经验校准的有效性边界**：论文报告 $R_{AD} \sim 1.3$（stretched quadrupole）与 $R_{AD} \sim 0.8$（stretched dipole）。这两个经验数值已经吸收了 AFRODITE 特定有限阵列的有效几何因子，**可以作为本实验多极性粗分类的定性判据，但不能反向作为无模型误差的高精度 $\delta$ 拟合依据**。

---

## 4. QTR 三级程序链（GAMPN $\to$ ASYMO $\to$ PROBMO）输入合同与内部冲突

### 4.1 程序流与数据接口传递

依据 Ragnarsson & Semmes 1988（RS88）与 Larsson et al. 1978（LLR78）：
1. **GAMPN**：
   - 输入：核参数 $(Z, A)$，形变参数 $(\varepsilon_2, \gamma, \varepsilon_4)$，Nilsson 单粒子参数 $(\kappa, \mu)$，价核子单粒子空间（选取费米面近邻的 $N_p$ 个轨道）；
   - 求解：变形 Nilsson 势单粒子本征态 $|\nu\rangle$ 与单粒子能量 $\varepsilon_\nu$；
   - 输出：单粒子波函数展开系数（在 $|NLJ\Omega_l\rangle$ 基下）与单粒子矩阵元文件。
2. **ASYMO**：
   - 输入：GAMPN 输出文件，化学势 $\lambda_F$，配对能隙 $\Delta$，科里奥利衰减因子 $\xi$，转动惯量参数（Harris 参数 $J_0, J_1$ 或实验 $2_1^+$ 能量），芯转动能量谱；
   - 求解：对单粒子态执行 BCS 准粒子变换（$u_\nu, v_\nu$ 占有几率），通过将强耦合基（strong-coupling basis）重耦合到好芯角动量基（good-core-$R$ basis），求解非共面粒子-转子耦合哈密顿量：
     $$H = H_{\text{core}}(\vec{R}) + \sum_\nu \varepsilon_\nu a_\nu^\dagger a_\nu + H_{\text{pair}} - \sum_k \frac{\hbar^2}{\mathcal{J}_k} I_k j_k$$
   - 输出：核能级能谱 $E(I)$、旋称劈裂 $S(I)$ 与多组态混合波函数 $|\Psi_I\rangle$。
3. **PROBMO**：
   - 输入：GAMPN 的单粒子算符矩阵元、ASYMO 的态混合波函数、有效电荷 $(e_{\text{eff}})$ 与有效旋磁比 $(g_s^{\text{eff}}, g_R, g_l)$；
   - 求解：计算电四极跃迁几率 $B(E2)$、磁偶极跃迁几率 $B(M1)$、多极混合比 $\delta$ 与静态电磁矩（$Q, \mu$）。

### 4.2 正宇称形变参数 $\varepsilon_4$ 的字面冲突与谱系追溯

在 WK22 正宇称计算中：
- **Table 6.1（第 66 页，PDF 77）**：列出 $^{133}\text{Ce}$ $7/2^+$ 基态形变参数为：
  $$\varepsilon_2 = 0.185, \quad \gamma = 10^\circ, \quad \varepsilon_4 = 0.1$$
- **紧接正文散文（第 66 页，PDF 77）**：
  “Constrained potential energy surface (PES) calculations [22]... suggest a quadruple deformation of $\varepsilon_2 = 0.185$ and a hexadecapole deformation of **$\varepsilon_4 = 0.01$** for the $\nu g_{7/2}$ orbital... (see Table 6.1).”
- **同源文献 Ding 2021 (Ref. [22])**：正文使用 $\varepsilon_4 = 0.01$。

**物理与代数鉴别**：
1. 在 $A \approx 130$ 质量区，十六极形变参数的物理量级典型为 $|\varepsilon_4| \sim 0.01–0.03$；若取 $\varepsilon_4 = 0.1$，其十六极势阱深度将被夸大近一个数量级，会在低激发谱中引发虚假的轨道交叉；
2. 尽管物理上 $\varepsilon_4 = 0.01$ 具有压倒性的系统学合理性，但在缺少作者实际运行输入卡（actual input deck）的归档证据前，**严禁在代码复现中静默修改 Table 6.1 表值**，必须同时保留“表列值 0.1”与“正文/同源值 0.01”两套候选输入边界。

### 4.3 单粒子能量与化学势的谐振子壳层基准解耦

#### 1. 正宇称（$N=4$ 壳层）
在 Table 6.2 中，正宇称单粒子能量列为 $\varepsilon \approx 5.45–6.49\text{ MeV}$，而正文报告费米面为 $\lambda_F = 50.60\text{ MeV}$。
- $A=133$ 谐振子能级间隔：
  $$\hbar\omega_0 \approx 41 \, A^{-1/3}\text{ MeV} = 41 \times 133^{-1/3} \approx 8.0322\text{ MeV}$$
- $N=4$ 主振子壳层基准能量：
  $$E_0(N=4) = \left(4 + \frac{3}{2}\right)\hbar\omega_0 = 5.5 \times 8.0322\text{ MeV} \approx 44.1770\text{ MeV}$$
- 叠加相对单粒子能量（费米面附近轨道 18–20，$\varepsilon \approx 6.4230\text{ MeV}$）：
  $$E_0(N=4) + \varepsilon \approx 44.1770 + 6.4230 = 50.6000\text{ MeV} \equiv \lambda_F$$
  **精确证明 $\lambda_F = 50.6\text{ MeV}$ 是以三维谐振子零点为绝对基准的单粒子化学势**。

#### 2. 负宇称（$N=5$ 壳层）的跨壳隔离红线
负宇称 $h_{11/2}$ 轨道属于 $N=5$ 主振子壳层：
- $N=5$ 基准能量：
  $$E_0(N=5) = \left(5 + \frac{3}{2}\right)\hbar\omega_0 = 6.5 \times 8.0322\text{ MeV} \approx 52.2091\text{ MeV}$$
- 壳基准跃迁差值：
  $$\Delta E_0 = E_0(N=5) - E_0(N=4) = 1.0 \, \hbar\omega_0 \approx 8.0322\text{ MeV}$$
- **致命物理陷阱**：
  在 WK22 第 6.3.2 节负宇称计算中，作者**完全未在正文中记录负宇称使用的 $\lambda_{F,-}$ 数值**。
  若后续研究者误将正宇称的 $\lambda_F = 50.60\text{ MeV}$ 直接代入负宇称计算，由于 $N=5$ 单粒子绝对能量高出 $\sim 8\text{ MeV}$，单粒子能减化学势将出现：
  $$E_\nu - \lambda_F \approx 58.2\text{ MeV} - 50.6\text{ MeV} \approx +7.6\text{ MeV}$$
  该差值远大于配对能隙（$\Delta \approx 0.9–1.0\text{ MeV}$），将导致准粒子激发能暴增为 $\sim 8\text{ MeV}$，BCS 占有几率发生极端畸变（$v^2 \to 0$），彻底摧毁负宇称能带的科里奥利混合。
  **结论**：负宇称必须使用自身的绝对费米能（$\lambda_{F,-} \approx 58.2\text{ MeV}$ 或重置相对基准后的 $\varepsilon - \lambda_{F,-}^{\text{rel}} \approx 0$）。

---

## 5. 结论与分析蓝本规范总结

| 分析维度 | 已核实事实 / 原文字面 | 物理机制与代数结论 | 分析蓝本规范红线 |
|---|---|---|---|
| **AFRODITE 探测器数** | Ding 2021 写 8 Clover；WK22 §4.5 写 8 Clover，§5.2.1 写 13 Clover（1@45°, 8@90°, 4@135°）。 | 双符合 $2.8 \times 10^{10}$ 与高阶符合 $5.4 \times 10^9$ 完全重合，属同一实验事件流的离线排序差异。 | 保留探测器掩模缺口，禁止断言“两文实验不同”或“完全相同几何”。 |
| **全探测器门 $R_{AD}$** | WK22 Eq 4.6 采用 all-detectors 门，正文称不依赖门线多极性（四极 $\sim 1.3$，偶极 $\sim 0.8$）。 | $4\pi$ 连续角积分下门线多极性严格相消；有限离散阵列因立体角不对称（8@90° vs 4@135°）存在残余偏置。 | $R_{AD}$ 为该阵列粗分多极性的经验基准，**严禁跨阵列移植套用**。 |
| **正宇称 $\varepsilon_4$ 冲突** | Table 6.1 列 $\varepsilon_4 = 0.1$；紧接正文写 $\varepsilon_4 = 0.01$；Ding 2021 写 0.01。 | $\varepsilon_4 = 0.1$ 夸大十六极效应近 10 倍，物理合理值为 0.01；但表列值未授权改写。 | 两套参数均予以保留，标记为待实际输入卡闭合的不一致性。 |
| **化学势 $\lambda_F$ 壳偏置** | 正宇称 $\lambda_F = 50.6\text{ MeV}$，单粒子能 $\varepsilon \approx 5.45–6.49\text{ MeV}$；负宇称 $\lambda_{F,-}$ 未显式记录。 | 差值 $44.18\text{ MeV}$ 精确对应 $N=4$ 壳基准 $5.5\hbar\omega_0$；$N=5$ 负宇称基准高出 $\sim 8.03\text{ MeV}$。 | **建立跨壳隔离红线**：严禁在负宇称计算中直接混用正宇称 $\lambda_F = 50.6\text{ MeV}$。 |
