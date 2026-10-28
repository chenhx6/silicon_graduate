---
type: research-note
title: "Ra/Th与Ba/Sm八极双阱、隧穿和Schiff响应：可比量与反例"
aliases: [actinide-lanthanide-doublewell-schiff-boundary]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [robledo-2010-bcp-d1s-octupole-ra-ba, rodriguez-guzman-2012-sm-gd-quadrupole-octupole, nomura-2020-ra-th-gogny-d1m-octupole, bernard-2016-144ba-sccm-octupole, dobaczewski-2005-ra225-schiff, nndc-2009-ra225-adopted-parity-doublet]
created_from: Day26 delegated double-well and Schiff mechanism investigation
promotion_target: octupole-correlation
tags: [octupole, double-well, tunneling, Schiff-moment, EDM, microscopic-mechanism, evidence-boundary]
---

# Ra/Th与Ba/Sm八极双阱、隧穿和Schiff响应

## Research Trigger

核验“锕系普遍1–2 MeV深双阱而Ba/Sm普遍≤0.3 MeV浅阱”的前提，并推导225Ra低能伙伴如何进入Schiff响应。原文核验给出直接反例：Gogny-D1S的144Ba最小值深约0.7 MeV；Ra/Th链端点也不统一深。另有两处须校正：Schiff坐标算符本身T偶P奇；225Ra基态PT标量混合的同自旋分母是55.16 keV，31.56-keV的3/2−不能代入。

## Grounded Evidence

| 核素/范围 | 模型原文支持的PES或相关量 | 原件定位与限制 |
| --- | --- | --- |
| 220–228Ra | BCP1与D1S均有非零Q3极小值；该链最深222Ra约1.5 MeV | [[robledo-2010-bcp-d1s-octupole-ra-ba]] PDF4/Fig1；不是每核均1.5 MeV |
| 224Ra、226Th | D1M中N=136处八极最显著，β3≈0.15；作者仍称β3方向较软 | [[nomura-2020-ra-th-gogny-d1m-octupole]] PDF2/Fig1；未给可直接引用的逐核势垒表 |
| 220Th、222Th | 220Th位于近球形或弱变形端；222Th已有β3≈0.1非零极小值 | 同上；220Th不能笼统归为已认证深双阱 |
| 144Ba | D1S极小值深约0.7 MeV；BCP1则在Q3=0附近很平坦 | [[robledo-2010-bcp-d1s-octupole-ra-ba]] PDF10/Fig9；直接反驳全Ba≤0.3 MeV |
| 146,148Ba | D1S有非零极小值，深度不超过该组144Ba的0.7 MeV；BCP1没有非零最低点 | 同上；未从图估填逐核精确值 |
| 144Ba（另一实现） | D1S二维HFB最低点(β2,β3)=(0.2,±0.1)，β3∈[−0.2,0.2]较软 | [[bernard-2016-144ba-sccm-octupole]] PDF2–3/Fig1；0.5-MeV等高线间距不能当精确势垒 |
| 146Sm | D1S与D1M最低点均Q30=0 | [[rodriguez-guzman-2012-sm-gd-quadrupole-octupole]] PDF4/Table I；不是每个Sm都有双阱 |
| 148Sm | Q30=1.25(D1S)、0.75(D1M) b^(3/2) | 同上；仅有非零极小值坐标不足以给势垒 |
| 150Sm | 反射对称性破缺平均场能量增益204 keV(D1S)、105 keV(D1M)；Q30=1.50/1.25 b^(3/2) | 同上PDF4/Table I、PDF12；确实很软，却不能代表全部Ba/Sm |
| 225Ra | 1/2+基态的同自旋负宇称伙伴55.16(6) keV；31.56(3) keV态是3/2− | [[nndc-2009-ra225-adopted-parity-doublet]] 原始L行；1/2−指认带括号 |

同为D1S、上述两个不同核的最深量级之比1.5/0.7≈2.14；222Ra相对150Sm的1.5/0.204≈7.35。两项都只是明确模型输出的比值，不是实验深度比，且跨论文实现不同，不能把它们提升为普适区域常数。

## Provisional Reasoning

### 1. 势垒、相关能与物理劈裂是三种不同量

对轴向反射对称的HFB势能面，先定义绝热曲线

$$V_{\rm ad}(q_3)=\min_{q_2,\ldots}E_{\rm HFB}(q_2,q_3,\ldots),\qquad V_{\rm ad}(q_3)=V_{\rm ad}(-q_3).$$

若确有±q0两个最低点，反射对称点相对深度为V_ad(0)−V_ad(q0)。这等于该绝热路径下放开反射对称性的平均场能量增益；不等于完整多维最小作用量路径的势垒，更不是宇称恢复/GCM的相关能。加入零点修正后得到的动力学势V_eff也不一定与原始HFB曲线相同。

在指定集体坐标/测度下，一维示意Hamiltonian为

$$H_{\rm coll}=-\frac{\hbar^2}{2}\frac{d}{dq}\frac1{B(q)}\frac{d}{dq}+V_{\rm eff}(q).$$

深阱且E0低于阱间势垒、作用量充分大时，最低双重态才可用

$$\Delta E\sim\frac{\hbar\omega}{\pi}\exp[-\mathcal S/\hbar],\qquad \mathcal S=\int_{q_a}^{q_b}dq\sqrt{2B(q)[V_{\rm eff}(q)-E_0]}$$

估计。劈裂同时取决于宽度、惯性、零点能与耦合路径。浅阱中E0可能接近/高于中间势垒，此时不能把WKB套成定量隧穿结论。完整投影GCM还可直接处理非局域核，不必先定义这一局域质量。由V_barrier单独给出ΔE不存在唯一映射。

偶偶Ra/Th/Ba的常见实验标志是偶J正宇称与奇J负宇称交错转动序列；0+与1−的差还含角动量贡献。它们不能无条件与奇A核同J异宇称的伙伴劈裂当成同一个“基态双重态”量。

### 2. 高j异宇称轨道使八极响应增大，但不能从轨道名称推出势阱深度

锕系的πf7/2↔i13/2、νg9/2↔j15/2，以及A≈144–150区的πd5/2↔h11/2、νf7/2↔i13/2，均具有Δl=Δj=3，允许强rank-3耦合。微扰地写h(q)=h0+qF3，占据/空态耦合带来负的二阶能移；其大小由矩阵元、能量距离与占据决定。配对体系还要用两准粒子能及相应相干因子。

精确谱表示的静态响应为

$$\chi_3(0)=2\sum_{n\ne0}\frac{|\langle n|Q_3|0\rangle|^2}{E_n-E_0}.$$

在示意可分离吸引作用−κQ3²/2的RPA中，1−κχ0接近零标志软化。把自洽势沿八极坐标作局部Landau展开：

$$V(q_3)=\frac12 Cq_3^2+\frac14 Dq_3^4,\quad D>0;\qquad C<0:\ q_0^2=-C/D,\quad V_{\rm barrier}=C^2/(4D).$$

这一Landau形式是条件模型，不是原文拟合。壳能增益与表面/宏观恢复力、配对、四极—八极耦合的竞争共同确定C和D。2012原文显示150Sm也有上述质子/中子驱动对与费米面壳隙，却仍只有204-keV的D1S平均场增益；2010原文显示Ba的D1S与BCP1对是否形成非零最低点都可不同。因此“锕系轨道多，所以必然1–2 MeV而稀土≤0.3 MeV”没有足够微观依据。

### 3. Schiff算符的归一化、微观矩阵元与离散对称性

采用点质子与常见最低阶有限核尺寸约定，恢复题面略去的e/10：

$$\hat S_z=\frac e{10}\sum_{p=1}^Z(r_p^2-\tfrac53\langle r^2_{\rm ch}\rangle)z_p,$$

单位为e fm³；坐标相对核质心。其球向量分量可定义为

$$S_{1q}=\frac e{10}\sqrt{\frac{4\pi}{3}}\sum_p[r_p^3-\tfrac53\langle r^2_{\rm ch}\rangle r_p]Y_{1q}(\hat r_p).$$

因此在任意已定相位的单粒子基中

$$S^{(z)}_{ab}=\frac e{10}\sum_\sigma\int d^3r\,\phi_a^*(\mathbf r,\sigma)[r^2-c]z\phi_b(\mathbf r,\sigma),\quad c=\tfrac53\langle r^2_{\rm ch}\rangle,$$

$$\langle f|S_z|i\rangle=\sum_{ab}S^{(z)}_{ab}\langle f|c_a^\dagger c_b|i\rangle.$$

径向积分含[r³−cr]而普通E1只有r；即使普通偶极矩相消，两个径向权重也无需同时相消。球形分量的角动量选择规则仍是rank1：异宇称且|j−j′|≤1；不能把Δj=3的八极驱动对直接当成Schiff的一体rank1矩阵元。

P使r→−r，所以S_z为P奇；T保持坐标不变，所以该电荷算符为T偶。T破缺来自使实验室静态矢量与自旋定向相关的PT奇相互作用；把算符本身称“T破缺算符”混淆了作用量与观测量。在宇称守恒的非简并核本征态中，⟨S_z⟩=0，即便内禀密度具有反射不对称形状。

### 4. 宇称混合与225Ra的正确分母

令W_PT是旋转标量且P、T均奇的小相互作用。一阶微扰给出

$$|\widetilde g\rangle=|g^+\rangle+\sum_n|n^-\rangle\frac{\langle n^-|W_{PT}|g^+\rangle}{E_g-E_n},$$

$$S_{\rm lab}=2\mathrm{Re}\sum_n\frac{\langle g^+|S_z|n^-\rangle\langle n^-|W_{PT}|g^+\rangle}{E_g-E_n}.$$

W_PT是标量，故中间态必须与基态具有相同J。对225Ra的J=1/2基态，低能分母为55.16 keV的1/2−伙伴。31.56-keV的3/2−不满足条件；既有解耦谱拟合约31.31-keV的截距也不是此式的实际能量分母。这个区分不依赖是否认同刚性八极模型。

若进一步采用两宇称态来自同一刚性轴向内禀组态、K=M=J=1/2的强耦合近似，方向投影因子为KM/[J(J+1)]=1/3，因而

$$S_{\rm lab}\simeq-\frac23\frac{S_{\rm intr}\langle W_{PT}\rangle_{\rm intr}}{\Delta E}.$$

这对应[[dobaczewski-2005-ra225-schiff]] Eq4的近似；不是完全投影SCCM的严格恒等式。缺少PT耦合常数或内禀W矩阵元时，不能由ΔE和E3独自给出实测Schiff矩。

### 5. 用质心修正均匀密度推导β2β3集体尺度

作为可检查的几何极限，令质子、质量密度具有同一均匀表面R(θ)=R[1+β1Y10+β2Y20+β3Y30]，密度ρe=3Ze/(4πR³)。保留β2β3阶，用

$$\int d\Omega\cos\theta Y_{10}=\sqrt{4\pi/3},\qquad \int d\Omega\cos\theta Y_{20}Y_{30}=3/\sqrt{35}$$

可得质心约束

$$\beta_1\sqrt{4\pi/3}+\frac9{\sqrt{35}}\beta_2\beta_3=0,$$

即β1≈−0.74330β2β3。此时普通偶极为零，而r²加权的矩不消失：

$$S_{\rm intr}=\frac9{20\pi\sqrt{35}}eZR^3\beta_2\beta_3+O(\beta^3).$$

取A=225、Z=88、R=1.2A^(1/3) fm，并**仅作示例**设β2=0.18、β3=0.10，得到R=7.29864 fm、S_intr=14.9111 e fm³。这是均匀密度几何尺度，不是225Ra的实验Schiff矩，也不是生产EDF重算；真实表面扩散、质子/中子密度与高阶形变会改变结果。

### 6. “几个数量级”来自多个因子，不能只归因于低能分母

把55.16-keV分母与示例1、5、10 MeV非集体尺度比较，单是分母因子只有18.13、90.65、181.29。完整增强还来自内禀集体S及PT相互作用矩阵元；原子EDM满足d_atom=k_atom S_lab，另需电子结构系数。

2005原文的特定模型系数为S_Ra=g(−1.5ḡ0+6.0ḡ1−4.0ḡ2) e fm³；其引述的199Hg RPA系数为g(0.0004ḡ0+0.055ḡ1+0.009ḡ2) e fm³。逐一通道的绝对比约3750、109、444，表明在该模型比较下可出现2–3个数量级乃至更大的差别；它们属于不同方法的理论比较，存在耦合常数与通道相消依赖。原文还估计电子结构约再带来因子3，并保留核理论因子2–3的不确定性。不能给任意球形核承诺统一EDM灵敏度提升，也不能把这些比值作为已测核响应。

## Assumptions

PES数值按论文的EDF、路径与读图精度解释；不插值不存在的逐核势垒表。WKB只限深阱。Schiff式为常见最低阶点质子约定，精密原子有限尺寸/其它多极修正不在此推导中；强耦合方向因子、均匀密度β2β3公式及PT微扰均各有独立近似。

## Competing Explanations

强E3与非零平均场最低点可同时出现在软集体动力学中；势阱“静态/动态”分类不能靠统一势垒阈值。偶偶交错带与奇A同J双重态需要分别判断。Schiff响应还依赖PT相互作用和time-odd密度，不能把普通E1相消或大E3当充分判据。

## Transfer Conditions

可迁移的是响应函数、对称性选择规则、作用量依赖与矩阵元分层；不能迁移具体势垒、惯性、奇核组态、EDM电子系数或未知耦合常数。

## Failure Conditions

若无V_eff、B(q)与零点能，不能从势垒唯一算ΔE；若中间态J不同，不能代入标量PT混合分母；若把e/10略去，Schiff数值比较相差10倍且缺失电荷单位。

## Falsification or Reverse Tests

在同一EDF、同一基底和同一投影近似下输出各核二维PES及惯性，再比较实验多跃迁E3与谱；不能先按区域规定势垒。225Ra需同J伙伴和PT核自洽计算，独立检验刚性投影近似；将E1接近零的模型与非零Schiff径向矩同时对账，检验“共享相消点”的错误假设。

## Open Questions

各核可重算PES/惯性网格、220–226Th逐核数值势垒、blocked225Ra的同EDF投影及time-odd耦合敏感性尚缺；当前不填这些数字。

## Human Review

Codex source self-audit；未转为human-reviewed。

## Promotion or Rejection History

2026-10-29：不采纳“所有锕系1–2 MeV/所有Ba–Sm≤0.3 MeV”、31-keV可直接作为225Ra基态PT分母、Schiff坐标算符本身T奇三项预设。

## Next Actions

先取得生产网格/惯性再比较隧穿；新PDF仅暂存tmp，指纹、阅读覆盖和示例算术在同名工件。保持Day26证据研学边界，不计额外课程信用。
