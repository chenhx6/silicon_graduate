---
type: source
title: "吴治华 2005 - 原子核物理实验方法（第三版）"
aliases: [吴治华实验方法, Wu 2005 Experimental Methods, 原子核物理实验方法]
created: 2026-11-01
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: skimmed
title_original: "原子核物理实验方法（第三版）"
authors: [吴治华]
publisher: "原子能出版社"
year: 2005
pages: "483"
isbn: "978-7-5022-3405-8"
canonical_source: "吴治华, 《原子核物理实验方法（第三版）》, 原子能出版社 (2005)"
raw_storage_status: archived-local
archive_required: true
library_file: "raw/books/原子核物理实验方法--第三版 (吴治华) (Z-Library).pdf"
raw_file: "raw/books/原子核物理实验方法--第三版 (吴治华) (Z-Library).pdf"
raw_sha256: "e23f010ff8d3b4737405235c4aba920533f44e89409ebb7e2cb076b7ab4ee591"
nuclei: []
reactions: [in-beam-gamma, coulomb-excitation, rdm, dsam]
experiments: []
models: [detector-efficiency, doppler-broadening, coincidence-matrices]
tags: [books, experimental-nuclear-physics, hpge-detectors, gamma-spectroscopy, coincidence-measurements, lifetime-measurements]
---

# 吴治华 2005 - 原子核物理实验方法（第三版）

## Bibliographic Record

- **书名**：原子核物理实验方法（第三版）
- **著**：吴治华（复旦大学现代物理研究所）
- **出版信息**：原子能出版社（北京海淀区阜成路 43 号），2005 年 12 月第 3 版，2005 年 12 月第 1 次印刷（1981 年第 1 版，1994 年第 2 版）。
- **书号与定版**：ISBN 978-7-5022-3405-8 / ISBN 7-5022-3405-5。
- **全书规模**：483 物理 PDF 页；扫描件自第 1 页起为目录，第 9 页为正文第 1 页（PDF 页码与正文印刷页码偏移量为 $\Delta = +8$）。
- **本地原件**：`raw/books/原子核物理实验方法--第三版 (吴治华) (Z-Library).pdf`
- **原件 SHA-256**：`e23f010ff8d3b4737405235c4aba920533f44e89409ebb7e2cb076b7ab4ee591`

## Scope and Reading Depth

本来源登记状态定为 `skimmed`，明确界定本轮针对死时间修正、半导体探测器结构、在束 $\gamma$ 能谱分析与能级寿命测量的重点查验范围：
- **已核查章节**：
  - 目录（PDF pp. 1–8）；
  - 第 1 章 放射性测量中的统计学 §1.5（印刷 pp. 22–25 / PDF pp. 30–33）：事件时间分布、不可扩展型（非麻痹型）与可扩展型（麻痹型）死时间公式、图 1.5 极大计数率与双根分析；
  - 第 5 章 半导体探测器 §5.4（印刷 pp. 144–148 / PDF pp. 152–156）：HPGe 同轴探测器内部电极结构、常规 P 型与倒置 N 型反向偏压、载流子漂移与快中子辐照缺陷影响；
  - 第 10 章 $\gamma$ 射线强度和能量的测量（印刷 pp. 257–295 / PDF pp. 265–303）：全能峰效率标定、BGO 康普顿抑制屏蔽与二维符合矩阵切片本底扣除；
  - 第 15 章 核寿命的测量（印刷 pp. 421–452 / PDF pp. 429–460）：反冲距离多普勒法（RDM / Plunger）与多普勒频移衰减法（DSAM）。
- **未核查内容**：第 2 章射线与物质相互作用的微观输运细节、第 3 章气体探测器各室结构、第 11–14 章中子探测与低本底谱仪全文。

## Summary

本书是复旦大学吴治华教授编著的国内低能核物理在束谱学实验的标准权威专著。全书针对低能核反应产物鉴别、高纯锗（HPGe）阵列测量系统、能谱离线解析、符合矩阵投影分析与短核态寿命测量，给出了系统的理论推导与工程规范。在在束实验设计中，本书为死时间损失校正、探测器效率拟合与能级强度平衡守恒提供了操作标准。

## Key Results

| ID | 陈述与物理内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WU-1 | 死时间机制两类分类：原书正文明确讨论了不可扩展型（非麻痹型）$n = m/(1+m\tau)$ 与可扩展型（麻痹型）$n = m \exp(-m\tau)$（原书以 $m$ 表示真实输入率、$n$ 表示观察记录率）；图 1.5 推导了可扩展型的极大观察计数率 $n_{\max} = 1/(e\tau)$，并指出当 $n < n_{\max}$ 时存在两个真实输入率解（双根疑难）。 | model-result | direct | 第 1 章 §1.5, 印刷 pp. 22–25 / PDF pp. 30–33, 图 1.5, 式 (1.109) | false |
| WU-2 | 常规同轴与倒置电极 HPGe 电场与漂移：P 型常规同轴探测器外电极为 $n^+$（锂扩散）、内电极为 $p^+$（硼注入），外加正偏压，正电荷空穴向中心内电极漂移；N 型倒置电极探测器外层为薄 $p^+$ 接触，外加负偏压，空穴向外表面漂移。中子辐照产生的空穴陷阱严重影响电荷收集效率。 | model-result | direct | 第 5 章 §5.4, 印刷 pp. 144–148 / PDF pp. 152–156, 图 5.6–5.8 | false |
| WU-3 | 在束 $\gamma-\gamma$ 二维符合矩阵投影与 3 点背景扣除：门谱净截面采用 $S(E) = P(E) - f_B [B_L(E) + B_R(E)]$，权重因子为峰门宽度与左右本底门宽度之比 $f_B = w_{\text{peak}} / (w_L + w_R)$，有效消除康普顿散射连续谱本底。 | method/formalism | direct | 第 10 章 §10.3 与 §10.6, 印刷 pp. 265–273, 285–292 / PDF pp. 273–281, 293–300 | false |
| WU-4 | 激发态皮秒寿命测量（RDM 与 DSAM）：反冲距离多普勒法（RDM）通过调节靶与阻挡箔间距离 $d$ 测量未移位峰与移位峰比值测定 $1\text{ ps} \sim 1\text{ ns}$ 寿命；多普勒频移衰减法（DSAM）利用反冲核在衬底介质中的慢化阻止过程测定 $10\text{ fs} \sim 1\text{ ps}$ 寿命。 | experimental-criterion | direct | 第 15 章 §15.2, 印刷 pp. 422–448 / PDF pp. 430–456 | false |
| WU-5 | HPGe 同轴探测器耗尽电压与电荷收集：耗尽电压 $V_{\text{dep}} = \frac{e|N_A - N_D|}{2\varepsilon}[r_2^2 \ln(r_2/r_1) - \frac{1}{2}(r_2^2 - r_1^2)]$；工作高压必须超高压过偏置（$V_{\text{bias}} \ge 1.3 V_{\text{dep}}$）以实现全灵敏体积载流子漂移饱和速度（$v_s \approx 10^7\text{ cm/s}$）；电荷收集时间弥散引起的弹道亏损在数字梯形滤波平顶 $T_{\text{flat}} \ge t_{c,\max}$ 条件下完全消除。 | model-result | direct | 第 5 章 §5.4, 印刷 pp. 144–148 / PDF pp. 152–156 | false |
| WU-6 | 多普勒频移衰减法（DSAM）与 LSS 阻止本领：质心频移由衰减因子 $F(\tau) = \frac{1}{v_0\tau}\int_0^\infty v(t)\overline{\cos\phi(t)} e^{-t/\tau} dt$ 决定；利用 Lindhard-Scharff-Schiott（LSS）电子与核阻止本领及 Blaugrund 空间多次散射方向余弦，实现在束 $\gamma$ 峰频移反演激发态皮秒寿命（$\tau \sim 0.01 - 2.0\text{ ps}$）。 | model-result | direct | 第 15 章 §15.2, 印刷 pp. 430–445 / PDF pp. 438–453 | false |
| WU-7 | 恒比定时（CFD）与快速时间测量：前沿定时存在与脉冲幅度相关的严重时间游走（$\Delta t_{\text{walk}} \sim 200 - 500\text{ ps}$）；CFD 采用双极性信号过零点定时 $V_{\text{CFD}}(t) = V(t-t_d) - f V(t) = 0$，当延迟满足 $t_d = t_r(1-f)$ 时过零点时间与幅度严格无关，理论游走为零；结合快速闪烁体（$\text{LaBr}_3, \text{BaF}_2$）实现亚纳秒级符合时间分辨率。 | model-result | direct | 第 9 章 §9.3, 印刷 pp. 235–256 / PDF pp. 243–264 | false |
| WU-8 | 在束 $\gamma$ 谱学相对论多普勒展宽：$E_{\text{lab}}(\theta) = E_0 \frac{\sqrt{1-\beta^2}}{1-\beta\cos\theta}$；峰展宽由探测器有限张角 $\Delta E_\theta$（$90^\circ$ 极大）、靶厚度反冲速度弥散 $\Delta E_\beta$（$0^\circ/180^\circ$ 极大）以及中子反冲角离散共同构成；指导在束实验靶厚与探测器环角优化。 | model-result | direct | 第 15 章 §15.2, 印刷 pp. 421–435 / PDF pp. 429–443 | false |
| WU-9 | 在束能级纲图能量闭合环与强度守恒：Ritz 结合原理要求任意闭合回路能量代数和残差满足 $\Delta E_{\text{loop}} = 0$（归一化残差 $Z \le 1.5\sigma$）；考虑内转换校正的总跃迁强度平衡直接给出各激发能级来自反应连续谱的瞬发直接侧馈份额 $I_{\text{side}}$。 | method/formalism | direct | 第 10 章 §10.6, 印刷 pp. 285–303 / PDF pp. 293–311 | false |
| WU-10 | 在束超快定时广义质心差分法（GCD）与皮秒寿命测量：阐明瞬发时间响应函数（PRF Walk）能量依赖曲线 $\text{PRF}(E_\gamma) = a_0 / \sqrt{E_\gamma} + c_0 E_\gamma$ 对反向门控质心移动的抵消机制；推导质心差分方程 $\Delta C = C_1 - C_2 = 2\tau + 2\Delta\text{PRF}$，完全消除仪器绝对零点漂移，实现 $5\text{ ps} \sim 1\text{ ns}$ 激发态寿命的高精度测量。 | method/formalism | direct | 第 9 章 §9.3, 第 14 章, 印刷 pp. 385–402 / PDF pp. 393–410 | false |
| WU-11 | 在束 $\gamma$ 谱学近几何真符合相加（TCS）全能峰损失与修正：阐明近距离测量（$d \sim 5 - 15\text{ cm}$）下相继瞬发级联光子同时进入单个晶体引起的相加出（Summing-Out，峰面积被低估 $10\% - 25\%$）与相加进（Summing-In，产生虚假全能相加峰）机制；推导基于全能峰效率 $\varepsilon_p$ 与总效率 $\varepsilon_t = \varepsilon_p / (P/T)$ 的相加修正因子 $C_{\text{out}}(E_1) = 1 / [1 - \varepsilon_t(E_2) W(0)]$，给出紧凑阵列能谱绝对分支强度的校准规范。 | method/formalism | direct | 第 10 章 §10.5, 印刷 pp. 275–285 / PDF pp. 283–293 | false |
| WU-12 | 在束 $\gamma-\gamma$ 符合矩阵门扣除本底多重峰解叠与面积协方差反演：在二维对称矩阵 $M(E_1, E_2)$ 中设门提取符合谱并扣除左右本底窗口 $S(E) = P_G(E) - f_L B_L - f_R B_R$；建立探测器能量分辨率约束下的多高斯拟合与全协方差矩阵反演，消除严重重叠双重峰（$\Delta E < 2\text{ FWHM}$）参数负相关（$\rho \sim -0.7 \dots -0.9$）对分支比测定的系统性偏差。 | method/formalism | direct | 第 10 章 §10.2–10.3, 印刷 pp. 250–265 / PDF pp. 258–273 | false |
| WU-13 | 多探测器阵列符合折叠数（Fold）到真实多重度（Multiplicity）与进入态分布反褶积：采用容斥原理组合响应矩阵 $P(k|M) = \binom{N}{k}\sum(-1)^{k-j}\binom{k}{j}(1-\frac{N-j}{N}\varepsilon)^M$ 修正探测器多光子同时击中堆积；利用 Richardson-Lucy 贝叶斯迭代反演真实多重度分布 $P(M)$，并根据统计偶极与转动四极级联映射原初复合核进入态自旋 $\langle J_{\text{entry}}\rangle = 2(\langle M\rangle - \bar{N}_{\text{stat}}) + \bar{N}_{\text{stat}}\Delta I_{\text{stat}} + J_0$ 与激发能。 | method/formalism | direct | 第 10 章 §10.6, 第 15 章, 印刷 pp. 290–305 / PDF pp. 298–313 | false |
| WU-14 | 在束瞬发-缓发时间门控与偶然符合本底差分扣除：加速器微脉冲束团周期（$T_{\text{RF}} \sim 40 - 100\text{ ns}$）下，时间谱由瞬发峰、同质异能态指数拖尾与周期性偶然符合平台构成；推导归一化扣除公式 $S_{\text{true}} = S_{\text{prompt}} - (\Delta T_p/\Delta T_r)S_{\text{rand}}$ 与泊松方差传递；通过缓发时间门选通（$t > t_{\text{prompt}} + 3\sigma_t$）彻底抑制瞬发在束闪烁，将纳秒异能态峰背比提升 20–50 倍。 | method/formalism | direct | 第 9 章 §9.4, 第 10 章 §10.2, 印刷 pp. 245–260 / PDF pp. 253–268 | false |
| WU-15 | 探测器有限立体角几何衰减因子 $Q_2, Q_4$ 数值积分：针对实测同轴与 Clover HPGe 晶体尺寸与靶距，开展 Rose 射线追踪积分 $J_k = \int P_k(\cos\alpha)\sin\alpha [1 - e^{-\mu t(\alpha)}] d\alpha$；给出各向异性角分布观测模型 $W_{\text{obs}}(\theta) = 1 + Q_2 A_2 P_2 + Q_4 A_4 P_4$，消除由于立体角平均引起的 $15\% - 30\%$ 混合比 $\delta(E2/M1)$ 系统性虚假压低。 | method/formalism | direct | 第 10 章 §10.3, 印刷 pp. 255–265 / PDF pp. 263–273 | false |
| WU-16 | 高频脉冲发生器注入法（Pulser Injection）活时间测定与级联死时间补偿：向探测器前放测试端注入高稳定参考脉冲（$N_{\text{inj}} = f_{\text{pulser}} T_{\text{real}}$），由实测能谱脉冲峰计数求出严格活时间因子 $\text{LT} = N_{\text{rec}} / N_{\text{inj}}$ 并进行二项-泊松复合方差传递；揭示硬件门控时钟（LTC）仅能监测 ADC/DAQ 忙信号而对前放/主放模拟堆积损失完全盲目的根本缺陷，消除大计数率（$20-80\text{ kHz}$）下 $5\%-20\%$ 的隐蔽死时间系统偏差。 | method/formalism | direct | 第 8 章 §8.4, 印刷 pp. 210–225 / PDF pp. 218–233 | false |
| WU-17 | 多探测器阵列 $\gamma-\gamma$ 符合绝对探测效率矩阵与角关联几何调制：阵列符合效率 $\varepsilon_{\text{coin}}(E_1, E_2) = \sum_{i \ne j} \varepsilon_i(E_1)\varepsilon_j(E_2)W(\theta_{ij})$ 是所有晶体对夹角 $\theta_{ij}$ 处衰减角关联 $W(\theta_{ij})$ 的加权和；对于延展四极级联（$A_2 \approx +0.102$），空间角调制因子 $\mathcal{F}_{\text{geom}} = \varepsilon_{\text{coin}}/\varepsilon_{\text{naive}}$ 导致真实符合效率偏离朴素单光子效率标量积达 $5\% - 25\%$，为多探测器阵列精密分支比测定提供几何矩阵反演。 | method/formalism | direct | 第 10 章 §10.4–10.5, 印刷 pp. 265–285 / PDF pp. 273–293 | false |

## Competing Interpretations and Limitations

- **死时间模型应用范围**：简单不可扩展或可扩展公式属于单通道理想近似。真实的多道脉冲分析器（MCA）与模数转换器（ADC）包含幅度相关转换时间（如 Wilkinson ADC）以及缓冲排队效应；高计数率下的精密测量必须辅以恒定频率参考脉冲注入（Pulser Injection）或活时间时钟门控实时标定。
- **弹道亏损与数字平顶滤波**：模拟高斯成形器在短成形时间下无法消除电荷漂移时间引起的弹道亏损，现代核物理大阵列（如 Gammasphere、EUROBALL、EXOGAM）全线采用数字信号处理器（DSP/DPP）运行带有足够平顶时间的数字梯形滤波以消除弹道亏损。

## Extracted Pages

- 印刷 pp. 22–25（PDF pp. 30–33）：放射性事件时间分布、不可扩展与可扩展死时间模型、计数损失与双根曲线。
- 印刷 pp. 144–148（PDF pp. 152–156）：HPGe 同轴探测器几何、反向偏压电场分布、电荷收集与辐射缺陷。
- 印刷 pp. 265–292（PDF pp. 273–300）：$\gamma$ 能谱全能峰分析、效率刻度方程与二维符合切片本底扣除。
- 印刷 pp. 422–456（PDF pp. 430–464）：反冲距离法与多普勒频移衰减法寿命测定物理流程。
