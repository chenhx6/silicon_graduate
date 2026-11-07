---
type: research-note
created_from: "20261107 continuation primary-source study and parent audit"
title: "98Mo负宇称带绝对寿命与跃迁几率约束核查：态身份Ledger与E1/E3/E2机制可辨识性"
aliases: ["98Mo negative-parity absolute constraints ledger", "continuation-g17-mo98-absolute-constraints-20261107"]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
reasoning_status: provisional
evidence_sources: ["continuation-g17-chen-singh-2020-nds-98mo", "continuation-g17-thomas-2016-96-98mo-coexistence", "karmakar-2025-2026-98mo-octupole-preview", "karmakar-2024-100ru-enhanced-e1-lifetimes", "campaign-g13-iskra-2019-96zr-revised-e3", "mo98-ru100-same-parent-e1-e3-constraints-20261107", "octupole-orbital-eligibility-and-collectivity-boundary-20261107"]
tags: ["98mo", "level-lifetimes", "octupole-collectivity", "state-identity-ledger", "identifiability", "e3-transition"]
---

# 98Mo 负宇称带绝对寿命与跃迁几率约束核查：态身份 Ledger 与辨识性分析

## Research Trigger & Core Question

Karmakar et al.（Nucl. Phys. A 1066 (2026) 123265 出版全文 [[karmakar-2025-2026-98mo-octupole-preview]]）在 ${}^{98}\text{Mo}$ 中新指认了两条高能 $E3$ 跃迁（1833.3 keV $5^- \to 2^+$ 与 1585.8 keV $7^- \to 4^+$），并报道低自旋负宇称态的 $B(E3)/B(E2)$ 相对比值达到 ${}^{100}\text{Ru}$ 的约 4 倍，且在 $9^-$ 态观察到 $B(E1)/B(E2)$ 激增与宇称分裂指数 $S(I)$ 反转。
然而，该论文未进行激发态寿命测量，两条 $E3$ 弱线亦未提取出实验 DCO 比值或线偏振度。

本研究聚焦唯一核心问题：
**在本次取得的评价与谱学材料中，${}^{98}\text{Mo}$ 的 $5^-, 7^-, 9^-_1$ 负宇称能级是否已有独立于 Karmakar 2026 分支比测量的绝对寿命、绝对 $B(E2)$ 或绝对 $B(E3)$ 实验约束？当前数据能否在物理上分辨这是八极/电偶极跃迁矩阵元（$E3/E1$）的绝对增强，还是带内四极跃迁（$E2$）的减小与受阻？**

---

## 态身份 Ledger（State Identity Ledger）

本 Ledger 逐能级核查目标态、衰变支路、寿命测量与同态绝对跃迁几率导出资格。
**底线物理警示**：低激发 $3^-_1$ 态（2017.5 keV）的实测寿命属于该态本征性质，其衰变宽度不可外推或乘以 $5^-, 7^-$ 的分支比；将其与更高自旋态分支相乘构造“绝对 $B(E3)$”在量纲与物理上均属致命误用。下表中 $3^-_1$ 仅作为实验控制列与基准列，不参与任何交叉运算。

| 能级 $E_x$ (keV) | 自旋宇称 $J^\pi$ | Karmakar 2026 所属能带 | 论文/评价寿命 ($\tau$ 或 $T_{1/2}$) | 实验误差 / 上下界 | 直接实验或 Evaluation 引用及原文 Key | 目标退激支路 $E_\gamma$、多极性与混合比 $\delta$ | Source 依赖链 | 能否合法给出同态绝对 $B(E\lambda)$？ |
|---|---|---|---|---|---|---|---|---|
| **2017.53(3)**<br>*(控制列)* | $3^-_1$ | Band 2 奇自旋带头 | $T_{1/2} = 65(7)\text{ ps}$<br>($\tau = 93.8(101)\text{ ps}$) | $\pm 7\text{ ps}$ | NDS 164, 1 (2020) Adopted p.3, 15; 原实验 1972Ba90 (Can. J. Phys. 50, 295 Coulex) | 2017.46(10) keV $\to 0^+_1$ ($I_\gamma=18.7(12)$, [E3]);<br>1230.16(4) keV $\to 2^+_1$ ($I_\gamma=100(3)$, (E1));<br>258.99(4) keV $\to 2^+_3$ ($I_\gamma=25.8(7)$, (E1)) | [[continuation-g17-chen-singh-2020-nds-98mo]] [CS20-F1]; [[karmakar-2025-2026-98mo-octupole-preview]] [KM-F1] | **可以合法给出**：<br>$B(E3\downarrow; 3^-_1 \to 0^+_1) = 30^{+7}_{-5}\text{ W.u.}$;<br>$B(E1\downarrow; 3^-_1 \to 2^+_3) = 4.9^{+9}_{-7}\times 10^{-5}\text{ W.u.}$。<br>*仅限本态，绝不可外推至更高态。* |
| **2620.4(3)**<br>*(ENSDF: 2620.78(5))* | $5^-_1$ | Band 2 奇自旋负宇称带 | **本次检索范围未发现** | 无测量值，无实验上下界 | Karmakar 2026 NPA 1066 Table 1 p.4, Table 2 p.6; Thomas 2016 NPA 947 Table 2 p.211; Chen & Singh 2020 NDS 164 p.4, p.20 | 带内 $E2$: 603.1(2) keV $\to 3^-$ ($I_\gamma=8.94(45)$, $R_{\text{DCO}}=0.96(12)$, $\Delta_{i\text{PDCO}}=0.05(4)$);<br>带间 $E1$: 1110.8(3) keV $\to 4^+$ ($I_\gamma=10.33(55)$, $R_{\text{DCO}}=0.69(8)$, $\Delta_{i\text{PDCO}}=0.09(4)$);<br>跨带 $E3$: 1833.3(5) keV $\to 2^+$ ($I_\gamma=0.24(9)$, DCO/偏振未测，最低允许 $E3$) | [[karmakar-2025-2026-98mo-octupole-preview]] [KM-F1-F4]; [[continuation-g17-thomas-2016-96-98mo-coexistence]] [TH16-F1]; [[continuation-g17-chen-singh-2020-nds-98mo]] [CS20-F2] | **无法给出绝对尺度**。<br>总衰变宽度 $\Gamma_{\text{tot}} = \hbar/\tau$ 未知，仅知相对比值：<br>$B(E3)/B(E2) = 66.05(27.01)\text{ fm}^2$;<br>$B(E1)/B(E2) = 5.17(38)\times 10^{-8}\text{ fm}^{-2}$。<br>但同母态 $B(E1)/B(E3) = 7.83\times 10^{-10}\text{ fm}^{-4}$ 消去共同分母，提供不依赖寿命的相对结构约束（见 [[mo98-ru100-same-parent-e1-e3-constraints-20261107]]）。 |
| **3095.4(4)**<br>*(ENSDF: 3096.26(16))* | $7^-_1$ | Band 2 奇自旋负宇称带 | **本次检索范围未发现** | 无测量值，无实验上下界 | Karmakar 2026 Table 1 p.4, Table 2 p.6; Thomas 2016 Table 2 p.211, Sec. 2.2; Chen & Singh 2020 NDS 164 p.5, pp.24-25 | 带内 $E2$: 475.1(2) keV $\to 5^-$ ($I_\gamma=9.89(25)$, $R_{\text{DCO}}=1.02(10)$, $\Delta_{i\text{PDCO}}=0.09(4)$);<br>带间 $E1$: 752.4(3) keV $\to 6^+$ ($I_\gamma=8.52(40)$, $R_{\text{DCO}}=0.65(6)$, $\Delta_{i\text{PDCO}}=0.07(4)$);<br>跨带 $E3$: 1585.8(6) keV $\to 4^+$ ($I_\gamma=0.74(16)$, DCO/偏振未测，最低允许 $E3$) | [[karmakar-2025-2026-98mo-octupole-preview]] [KM-F1-F4]; [[continuation-g17-thomas-2016-96-98mo-coexistence]] [TH16-F2]; [[continuation-g17-chen-singh-2020-nds-98mo]] [CS20-F3] | **无法给出绝对尺度**。<br>总寿命未知，仅知相对比值：<br>$B(E3)/B(E2) = 153.81(33.31)\text{ fm}^2$;<br>$B(E1)/B(E2) = 3.76(21)\times 10^{-8}\text{ fm}^{-2}$。<br>同母态 $B(E1)/B(E3) = 2.44\times 10^{-10}\text{ fm}^{-4}$ 同样消去共同分母，显现相对演化（见 [[mo98-ru100-same-parent-e1-e3-constraints-20261107]]）。 |
| **3655.7(4)**<br>*(ENSDF: 3656.7(3))* | $9^-_1$ | Band 2 奇自旋负宇称带 | **本次检索范围未发现** | 无测量值，无实验上下界 | Karmakar 2026 Table 1 p.4, Table 3 p.7; Chen & Singh 2020 NDS 164 p.7, p.28 | 带内 $E2$: 560.3(3) keV $\to 7^-$ ($I_\gamma=4.17(42)$, $R_{\text{DCO}}=1.04(19)$, $Q$ 纯四极);<br>带间 $E1$: 384.5(3) keV $\to 8^+$ ($I_\gamma=3.62(29)$, $R_{\text{DCO}}=0.69(10)$, $D$ 纯偶极);<br>另支: 802.3(3) keV $\to 8^+_{2854}$ ($I_\gamma=5.54(58)$, E1) | [[karmakar-2025-2026-98mo-octupole-preview]] [KM-F6]; [[continuation-g17-chen-singh-2020-nds-98mo]] [CS20-F4] | **无法合法给出**。<br>$B(E1)/B(E2) = 64.52(8.30)\times 10^{-8}\text{ fm}^{-2}$ 激增 17 倍，但在无绝对寿命时，无法分辨是八极关联增强还是带交叉引起带内四极跃迁急剧衰减。 |
| **3767.5(4)**<br>*(竞争态隔离)* | $9^-_2$ | **Band 3** (奇自旋负宇称伴带) | **本次检索范围未发现** | 无测量值 | Karmakar 2026 Table 1 p.4, Fig. 1 p.3; Chen & Singh 2020 NDS 164 p.8, p.28 | 672.1(4) keV $\to 7^-_1$ (3095.4 keV) ($I_\gamma=6.25(24)$, $R_{\text{DCO}}=1.45(23)$, $\Delta_{i\text{PDCO}}=0.07(5)$, 纯 E2); 无带间 E1 跃迁 | [[continuation-g17-chen-singh-2020-nds-98mo]] [CS20-F5] | **严格区分**：归属 Band 3，非 Band 2 八极候选带成员，绝不可与 3655.7 keV $9^-_1$ 混淆。 |

---

## 检索范围与文献证据链审查

为核查本次取得材料中是否已含 ${}^{98}\text{Mo}$ 负宇称态能级寿命数据，对以下数据库与原始文献群开展了核实：

1. **官方核结构与衰变数据评价库（ENSDF / NuDat 3 / NDS 164, 1 (2020)）**：
   - 逐页检索 Jun Chen, Balraj Singh 的 A=98 评价底本 [[continuation-g17-chen-singh-2020-nds-98mo]]（截止 2020 年 2 月，含 2021 年 5 月修改）；
   - 核查了 6 个核心反应数据集：Adopted Levels/Gammas、Coulomb Excitation（2002Zi06, 1972Ba90）、$^{96}\text{Zr}(\alpha, 2n\gamma)$（2016Th01, 1971Le19）、$^{98}\text{Mo}(n, n'\gamma)$（1984Me04, 1971McZG）、$^{168}\text{Er}(^{30}\text{Si}, X\gamma)$（2007La03）与 $^{98}\text{Nb}$ $\beta^-$ 衰变（51.1 min）；
   - **核查结论**：在 2017.5 keV $3^-_1$ 态之外，${}^{98}\text{Mo}$ 的 $5^-_1$（2620.8 keV）、$7^-_1$（3096.3 keV）、$9^-_1$（3656.7 keV）与 $9^-_2$（3768.7 keV）在评价底本 Adopted Levels 中半衰期 $T_{1/2}$ 与平均寿命 $\tau$ 均为空白。所有测出皮秒/飞秒寿命的激发态（2206, 2333, 2525, 2700, 2871, 2905, 2916, 2976, 3050, 3229, 3557 keV）全部为正宇称态（主要是形状共存或质中混合对称态）。

2. **高精度 Clover 阵列 DSAM 实验（Thomas et al., Nucl. Phys. A 947 (2016) 203 [[continuation-g17-thomas-2016-96-98mo-coexistence]]）**：
   - 该工作在耶鲁大学 WNSL 利用 YRAST Ball 阵列（10 台 Clover）与 $^{96}\text{Zr}(\alpha, 2n)$ 反应开展 DSAM 多普勒线形分析；
   - 提取了大量正宇称态的有效亚皮秒寿命（如 2206 keV $2^+$ $\tau_{\text{eff}} < 0.26\text{ ps}$、2871 keV $2^+,3$ $\tau_{\text{eff}} < 0.50\text{ ps}$ 等）；
   - 但在其完整数据表 Table 2（p.211）中，2620.56 keV $5^-$ 与 3095.74 keV $7^-$ 态的 $\tau$ 列明确留空；正文第 2.2 节详述了 $7^-$ 态 752 keV 分支强度的争议，但明确指出未提取线形寿命。

3. **重离子高自旋谱学（Lalkovski et al., Phys. Rev. C 75, 014314 (2007)）**：
   - 利用 EUROBALL-III 阵列通过 $^{168}\text{Er}(^{30}\text{Si}, X\gamma)$ 深度扩展了 ${}^{98}\text{Mo}$ 负宇称能带至 $15^-$；
   - 但该实验采用薄靶金衬底，未进行线形分析或反冲距离寿命测量，未提供任何激发态寿命。

4. **Web of Science Starter API 检索（2000–2026 全库追踪）**：
   - 检索式 `TI=("98Mo" OR "98-Mo" OR "Mo-98" OR "Molybdenum-98") AND PY=(2000-2026)` 命中 50 篇文献，覆盖库仑激发（2002Zi06）、双光子衰变（2014He04）、形状共存（2013Th05, 2016Th01）、FIPPS $(n, \gamma)$ 谱学（2018Wi02）等；
   - 在已核实文献范围内，除已知正宇称态与低激 $3^-_1$ 态外，未见针对负宇称带 $5^-, 7^-, 9^-_1$ 能级的直接寿命测量；这表明在掌握的主流与评价文献中该数据缺失，不应断言全历史所有文献均已绝对穷尽。

---

## 物理机制可辨识性：E1/E3 绝对增强 vs E2 受阻减小

在缺乏能级寿命的前提下，Karmakar 2026 报告的相对跃迁强度比率表达为：
$$\frac{B(E3; I^- \to (I-3)^+)}{B(E2; I^- \to (I-2)^-)} = \frac{I_\gamma(E3)}{I_\gamma(E2)} \cdot \frac{E_\gamma(E2)^5}{E_\gamma(E3)^7} \cdot \frac{1.223 \times 10^8}{1.590 \times 10^3} \quad [\text{fm}^2]$$
$$\frac{B(E1; I^- \to (I-1)^+)}{B(E2; I^- \to (I-2)^-)} = \frac{I_\gamma(E1)}{I_\gamma(E2)} \cdot \frac{E_\gamma(E2)^5}{E_\gamma(E1)^3} \cdot \frac{1.071 \times 10^{13}}{1.590 \times 10^3} \quad [\text{fm}^{-2}]$$

这两个比值均以带内四极跃迁几率 $B(E2)$ 作为分母。因此，比值的增大具有双重物理诱因：
1. **解释 A（八极关联增强假说）**：内禀反射不对称性增强导致八极跃迁矩阵元 $M(E3)$ 与电偶极跃迁矩阵元 $M(E1)$ 增大；
2. **解释 B（带内四极重叠减小/组态重排假说）**：能级受到形状共存、波函数重叠减小或准粒子顺排/带交叉影响，使得带内四极矩阵元减小。形状变化并不必然导致 $B(E2)$ 减小，但在多组态竞争区，四极强度的受阻是可能与八极增强并存的竞争机制。

此外，如 [[mo98-ru100-same-parent-e1-e3-constraints-20261107]] 所揭示，同母态的 $B(E1)/B(E3)$ 比值消去了共同的 $B(E2)$ 分母与能级寿命，构建了仅依赖光子分支比与能量的直接比值 $S_i$。98Mo 的 $S_7/S_5 \approx 0.31$ 与 100Ru 的 $S_7/S_5 \approx 1.56$ 存在明确差异，表明相对分支测量并非毫无物理区分力；它能够有效检验不同核的相对跃迁结构演化，只是仍不能单独固定绝对跃迁尺度。

### 条件不等式分析

若假定未来的高灵敏度反冲距离实验（RDM）或厚靶 DSAM 给出 $5^-$ 或 $7^-$ 态的平均寿命上限 $\tau < \tau_{\text{upper}}$（例如典型皮秒窗口 $\tau_{\text{upper}} = 1.0\text{ ps}$），则利用总跃迁几率 $1/\tau = \sum_f \lambda_f = \lambda_{E2}(1 + \alpha_{E2}) + \lambda_{E1}(1 + \alpha_{E1}) + \lambda_{E3}(1 + \alpha_{E3}) + \dots$，可建立条件不等式：
$$B(E2) > \frac{1}{\tau_{\text{upper}} \cdot \left[ 1.223\times 10^9 E_\gamma(E2)^5 + 1.590\times 10^{15} \frac{I_\gamma(E1)}{I_\gamma(E2)} E_\gamma(E2)^5 + \dots \right]}$$
仅有τ仍需完整支路/多极分量及转换约定。若b_tot,λ为该多极支路含转换占全部母态衰变的份额，则光子率λγ=b_tot,λ/[τ(1+αλ)]；若输入本身已是相对总衰变的光子份额，不再重复除1+α。所有实际开放通道须纳入归一。

---

## 同位素与同中子素比较：控制边界与反泛化

本研究选取同中子素 ${}^{96}\text{Zr}$ ($Z=40, N=56$)、${}^{100}\text{Ru}$ ($Z=44, N=56$) 与同位素 ${}^{96}\text{Mo}$ ($N=54$) 进行对比：

1. **同中子素 ${}^{96}\text{Zr}$ ($Z=40, N=56$)**：
   - ${}^{96}\text{Zr}$ 的 $3^-_1$ 态（1897.2 keV）绝对跃迁几率在 Iskra et al. 2019 PLB 788, 396 ([[campaign-g13-iskra-2019-96zr-revised-e3]]) 中采用 Horen 1993 的 $T_{1/2} = 67.8(43)\text{ ps}$，结合Gammasphere修正的1897.2/1750.4-keV光子相对强度12.8(3):100（不是总分支12.8%），修订为向下 $B(E3; 3^- \to 0^+) = 42(3)\text{ W.u.}$ ($23(2)\times 10^3\text{ }e^2\text{fm}^6$)。历史文献（Mach 1990 [[mach-1990-96zr]]）报告的 $T_{1/2} = 50(7)\text{ ps}$ 对应于旧的 $B(E3) = 65(10)\text{ W.u.}$ 评价，不能把 Mach 1990 的 50(7) ps 误配给 Iskra 2019 的 42(3) W.u. 修订值。其它态的寿命本页未据Iskra原文另行认证。
   - 球形单粒子rank3下p1/2↔g9/2因Δj4为零；p3/2↔g9/2及d5/2↔h11/2可角向允许。允许性不证明实际核的占据、径向重叠或相干集体性，见[[octupole-orbital-eligibility-and-collectivity-boundary-20261107]]。

2. **同中子素 ${}^{100}\text{Ru}$ ($Z=44, N=56$)**：
   - Karmakar et al. (PRC 110, L051302 (2024) [[karmakar-2024-100ru-enhanced-e1-lifetimes]]) 仅在高自旋端（$13^-, 15^-, 17^-$ 与 $14^+, 16^+, 18^+$）通过厚靶 DSAM 测出皮秒寿命；
   - 其低自旋 $5^-_1$（2527 keV）与 $7^-_1$（2952 keV）态同样缺乏直接寿命！Karmakar 2026 Table 2 所列 ${}^{100}\text{Ru}$ 的 $B(E3)/B(E2)$ 同样是基于薄靶实验相对分支比计算得出的导出量。

3. **反泛化科学判据**：
   - **不能泛称“$N=56$ 是八极集体性的充分条件”**。
   - $N=56$ 确实为中子体系提供了相干的 $\Delta l=\Delta j=3$ 轨道对（$\nu 2d_{5/2} \leftrightarrow \nu 1h_{11/2}$），构成了八极跃迁矩阵元的基础。
   - 不同Z的占据、配对与形状可能不同，需要逐态实际数据和模型；不把Zr→Mo→Ru整链写成已测得的单一形状演化。
   - 在此过渡区，能级波函数的多组态混合使得带内 $B(E2)$ 极易受到局部退相干抑制。因此，不具备绝对寿命的相对比值增强绝不可等同于反射不对称静态形变的充分确证。

---

## 结论与最有信息量下一测量

1. **核心结论**：在本次取得与核验的 NDS 2020 评价底本与 Thomas 2016、Karmakar 2026 等文献中，**${}^{98}\text{Mo}$ 的 $5^-_1, 7^-_1, 9^-_1$ 负宇称态均未见直接能级寿命或同态绝对跃迁几率记录**。在缺乏绝对寿命时，相对比值 $B(E3)/B(E2)$ 无法独立区分 $E3$ 绝对增强与带内 $E2$ 减小；但同母态 $B(E1)/B(E3)$ 比值消去共同分母，提供了不依赖寿命的相对结构约束（[[mo98-ru100-same-parent-e1-e3-constraints-20261107]]）。
2. **最有信息量下一测量（Most Informative Next Measurement）**：
   - **反应方案**：利用变能量回旋加速器或串列加速器，通过重离子熔合蒸发反应（如 $^{94}\text{Zr}(^7\text{Li}, 3n)^{98}\text{Nb}(\beta^-)$ 或 $^{96}\text{Zr}(\alpha, 2n)^{98}\text{Mo}$ 在富集靶厚衬底上），开展**反冲距离多普勒频移法（RDM / Plunger）**或**厚靶低能反冲核 DSAM 线形拟合**；
   - **首要测量目标**：针对 $2620.4\text{ keV}$ $5^-$ 态与 $3095.4\text{ keV}$ $7^-$ 态，针对 Thomas 2016 薄靶 DSAM（有效寿命上限亚皮秒）未测出寿命的情况，通过拓展时间测量窗口尝试提取其本征寿命；
   - **配套多极性辅助判定**：采用高统计 Clover 阵列配备数字获取系统，对 1833.3 keV 与 1585.8 keV 两条弱 $\gamma$ 线开展高灵敏度康普顿线偏振度（$\Delta_{i\text{PDCO}}$）与角分布定向相关（DCO）测量。需注意偏振测量主要辅助判别电/磁跃迁特征（宇称改变），不能单独确证跃迁为纯 $E3$；确证多极性仍须结合自旋序列、混合比界限及跃迁速率单粒子上限综合判定。


## Research Trigger

98Mo目标5−/7−/9−是否有可匹配的绝对量。


## Grounded Evidence

直接证据、实际版本和页码见本页来源段；证据入口为[[continuation-g17-chen-singh-2020-nds-98mo]], [[continuation-g17-thomas-2016-96-98mo-coexistence]], [[karmakar-2025-2026-98mo-octupole-preview]], [[karmakar-2024-100ru-enhanced-e1-lifetimes]], [[campaign-g13-iskra-2019-96zr-revised-e3]], [[mo98-ru100-same-parent-e1-e3-constraints-20261107]], [[octupole-orbital-eligibility-and-collectivity-boundary-20261107]]。


## Provisional Reasoning

本页比较从原表/算符到条件结论的推断；这些推断与作者实验报告分别标注，不视作新的独立测量。


## Assumptions

采用本页声明的态对应、单位、多极/旋转规范和所用模型范围；未给的联合Cov、原始响应或作者实现不补造。


## Competing Explanations

所选机制须与组态混合、占据变化及实际实验/有效算符依赖比较；与名义数据相容不等于唯一解释。


## Transfer Conditions

迁移到另一核素/核区前，重新核对同态身份、占据/配对、形状动力学和探针算符；仅质量数或名词相同不满足合同。


## Failure Conditions

若原件/态映射/算符规范改变、或必要响应未恢复，重新计算并收窄结论；不得以缺失伴随信号代替有灵敏度的排除。


## Falsification or Reverse Tests

逐态核对评价的寿命空白和2026分支；不同母态不得代用。 本页没有未执行的真实核模型排他认证。


## Open Questions

目标态寿命、完整支路及实际测量灵敏度。


## Human Review

本任务未发生用户逐项审核；记录的是Agent原件自审，未伪装human-reviewed。审核标注不作为检索或使用资格门。


## Promotion or Rejection History

本批根据直接原件与独立核查修订worker草案，撤回无源数值/普适断言；本页保持provisional。具体触发证据和仍存边界见正文，不以结构检查替代物理核验。
