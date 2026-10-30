# Joss 1998：¹³³Ce 高自旋三轴带寿命（078）

本单元取得并完整阅读 APS 正式4页正文，逐页核看全部图表。Joss 等的研究是 Gammasphere + DSAM/多普勒展宽线形（DBLS），与 Emediato 1997 的低自旋 RDDS 分开；不能用 1997 的低态时钟或 ENSDF 带字母替换本篇高自旋带的具体 (E_\gamma,J_i	o J_f,	au) 映射。

来源：D. T. Joss et al., *Lifetime measurements of a triaxial band in ¹³³Ce*, Physical Review C **58**(6), 3219–3222 (1998), DOI [10.1103/PhysRevC.58.3219](https://doi.org/10.1103/PhysRevC.58.3219)。Crossref、ENSDF 1998JO16 和 PDF 首页身份一致。PDF 4页、120,604 bytes，SHA256 `81b6ace5d9ee867220c5425e7f3d9ae4f5074d9484f7063fd04fd137b0deea0a`；物理页+3218=印刷页。原文、页文本和渲染图在 `tmp/day24-joss1998-133ce-triaxial-lifetime-078/`；本 worker 只写分配目录。

## 实验与 DBLS 合同

¹³³Ce 来自 ¹⁰⁰Mo(³⁶S,xn) A≈132 Ce 融合蒸发。约 (9	imes10^8) 个 fold>5 prompt coincidence events 记录5天，但3n ¹³³Ce 通道比 4n ¹³²Ce 和5n ¹³¹Ce弱，估计相对布居 5:4:1。数据按 422、488、643、888 keV 带内线门控，谱按前向31.7–37.4°、90°、后向142.6–148.3°组分出。

方法是 DSAM 的 Doppler-broadened line-shape analysis，由 LINESHAPE 用 Currie Monte Carlo 模拟反冲轨迹和速度方向历史；每步生成5000条 recoil history，步长0.001 ps，电子/核阻停分别用 Ziegler stopping powers 和 Monte Carlo。线形依赖目标态、观测线及未观测 side feeding 的寿命。side-feeding 强度由本数据带内相对强度得到，并与薄靶数据相符后固定；side feeding 用固定惯量 (I_{SF}=48\hbar^2\,\mathrm{MeV}^{-1}) 的五态旋转带表示。Qt、QSF、污染峰、背景和归一化因子共同拟合，前/后/90°谱同时最小二乘，MINOS 求误差，低于测量值8%的误差上调到8%下限。

作者没有给原始计数、完整速度/阻停核、逐线系统协方差、producer/job 或 side-feeding 原始独立计数。公式和参数应作为条件模型输入，不把 DBLS 输出写成与 response/feed 无关的直接 τ。

## Table I：四条带内寿命和 (Q_t)

|跃迁|Eγ (keV)|(Q_t) (eb)|平均寿命 τ (ps)|side-feed τSF (ps)|
|---|---:|---:|---:|---:|
|(43/2⁻→39/2⁻)|887.4|1.94(10)|1.11(13)|0.48(11)|
|(47/2⁻→43/2⁻)|999.3|2.65(16)|0.33(4)|0.49(1)|
|(51/2⁻→47/2⁻)|1097.6|2.66(21)|0.20(2)|0.37(4)|
|(55/2⁻→51/2⁻)|1188.1|2.15(15)|0.21(2)|0.34(4)|

这些是 (	au)（平均寿命），不是 (T_{1/2})。作者给 (Q_t) 加权平均约 (2.2(1)\,eb)，并称随估计角动量近似恒定。用表中四点按 (1/\sigma^2) 作内部核算得到 (2.199(70)\,eb)，四舍五入支持2.2；这只是表算术核查，不能重建作者含约10–15%阻停系统误差的最终不确定度。

(T(E2)) 与 (Q_t) 的公式用 (E_\gamma)（MeV）五次方和 Clebsch–Gordan 因子；未观测 side-feeding 能量由固定 (I_{SF}) 假设计算，side-feeding τ由拟合 QSF 推回。因此 side-feed 表列不是直接测出的独立寿命网络。

## 形变、TRS 与跨论文谱系

作者将带解释为高自旋、负宇称、旋转对齐的上半壳层 νh₁₁/₂ 构型，并报告大 γ 变形下的三轴结构。TRS 计算给单准中子 νh₁₁/₂ 低频率最小值约 β₂=.19、γ≈−30°，另有 ((
u h_{11/2})^3) 在 γ≈−73° 的低频率最小值；Fig.3(b) 高自旋面还显示 γ≈−83° 三轴最小值与 β₂≈.4 的超形变轴对称极小值共存。它们是模型势面结果，不是独立测得的静态 γ 或波函数组态。

用 (Q_t=Q_{20}\cos(\gamma+30°)/\cos30°)，作者在假设 γ=−83° 下得到 (Q_{20}=3.2(1)\,eb)，再在无六极形变假设下给 β₂=.186(7)。这一步依赖理论 γ 和形变截断，不能升级为独立刚性/三轴测量。Table II 的当前带 (Q_t=2.2(1)\,eb) 与 ¹³²Ce SD1 (7.4(3)\,eb) 的对比利用共同反冲阻停条件，支持相对 collectivity 判断；绝对值仍有阻停知识导致的约10–15%不确定度。

Fig.4 的顶态 (F(	au)) 略低于 (Q_t=2.2\) 的计算曲线，作者认为可能是低能带内门增强 side feeding 后形成的有效寿命。这提醒不能把四个 Table I 点都当成无 feeding 的纯带内时钟。作者估计本带 (T(E2)pprox35\) W.u.，远低于 ¹³²Ce SD 约490 W.u.、正常基带约100 W.u.；这是基于寿命/模型约定的集体性比较，不是独立形状观测。

Emediato 1997 只在讨论末被引用为低自旋 νh₁₁/₂ 带 (T(E2)pprox50) W.u.（TRS 的 β₂≈.19、γ≈−30°最小值），不能与 Joss 的高自旋 Table I 逐态合并。Joss 还引用先前 ¹³²/¹³³Ce SD 的 target-thickness Doppler broadening；Table II 的 SD 行不是全都来自本次同一采集。

## 组态和映射边界

Table I 的高自旋 (J^\pi) 采用括号标签，正文明确 side-feeding 与三轴带自旋是估计值，因为尚无连到已知低能带的 linking transitions。ENSDF 的带字母、现代 band F 等不能脱离具体 (E_i,J_i	o J_f,E_\gamma) 和时钟映射，直接当作独立实测组态证明。本文测的是这四条具体 DBLS 线；它没有覆盖 ¹³³Ce 所有高自旋态，也没有给 chiral partner 的相对/绝对 EM 网络、signed phase 或隧穿证据。

本单元已完整读完4页及 Fig.1–4/Table I–II，未运行 LINESHAPE、TRS 或其它作者程序，未取代原数据/协方差。逐条证据见 `claim-ledger.json`；表格与加权均值核查包含在末条 claim。APS 获取、SI 和路线边界见 `access-manifest.json`；来源自审不是 human-reviewed。
