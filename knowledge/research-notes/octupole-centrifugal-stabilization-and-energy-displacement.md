---
type: research-note
title: "离心力驱动八极形变稳定化与高自旋交错能级位移"
aliases: [centrifugal stabilization of octupole shapes, octupole high-spin parity displacement]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [butler-nazarewicz-1996-intrinsic-reflection-asymmetry, bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, gaffney-2013-pear-shaped-rn-ra, robledo-2010-bcp-d1s-octupole-ra-ba, nomura-2020-ra-th-gogny-d1m-octupole]
created_from: Day26 directed study of centrifugal stabilization and parity-displacement evolution
promotion_target: octupole-deformation
tags: [octupole, centrifugal-stabilization, high-spin, parity-doublet, energy-displacement, Ba144, Ba146, Ra224, Th226]
---

# 离心力驱动八极形变稳定化与高自旋交错能级位移

## Research Trigger

本课题追踪一个可检验的动力学链条：在低自旋时，$^{144,146}$Ba 的八极自由度主要表现为软振动，负宇称带头位于约 $0.74$–$0.76$ MeV，交错位移
$$
\delta E(I)=E(I^-)-\frac{E((I-1)^+)+E((I+1)^+)}{2}
$$
在 $I=1$ 为 $647$–$659$ keV；当自旋升高，转动能偏好增大的转动惯量，可能把最低点推向有限 $\beta_3$，并使相反宇称能级更接近。该现象需要同时检查微观势能面、转动惯量、零点能与实测能级，不能由单一大 $B(E3)$ 或单一势垒高度裁决。

## Grounded Evidence

### 理论来源与定位

1. Butler & Nazarewicz 的 RMP 综述指出，Egido–Robledo 在集体哈密顿量中加入 $I(I+1)/(2\mathcal J(q_3))$ 后，对高自旋 $^{146}$Ba 得到八极形变稳定化（*Rev. Mod. Phys.* **68**, 349–421 (1996), PDF p.390，讨论段）；同页还指出 $^{144,146}$Ba 在 $I\gtrsim12$ 出现 band crossing，具体走向取决于对齐与组态。
2. 同一综述在 PDF p.390 明确总结：Ra–Th 区域的总 Routhian 计算在中等自旋增大八极形变并使八极极小分离得更好；在较高自旋，$j_{15/2}$ 中子和 $i_{13/2}$ 质子四准粒子组态在约 $I\sim26$ 变为 yrast，并可能把形状推回反射对称。该段引用 Nazarewicz *et al.*, *Nucl. Phys. A* **467**, 437 (1987)。
3. RMP PDF p.390–391 还记录 Jolos 等的自旋依赖势 $V(\beta_3,I)=U(\beta_3)+A(\beta_3)I(I+1)$ 与 WKB 交错宇称劈裂处理，并指出临界自旋 $I_{\rm oct}$ 与 $E(3^-_1)/E(2^+_1)$ 存在经验关联。该段是本笔记把 $\delta E(I)$ 作为动力学响应量的理论出处，而非对所有核的普适定律。
4. RMP PDF p.363 的集体模型讨论说明转动哈密顿量包含转子、Coriolis 和离心项；PDF p.390–392 的 Fig.40 图注给出 Nazarewicz *et al.* (1987) 对 $^{220–228}$Th 的转动频率依赖总 Routhian 计算。该综述还指出 Egido–Robledo 对 $^{142–148}$Ba 的零自旋势垒不足以直接归为刚性八极形变（PDF p.363），说明“非零平均场极小”与“实验静态梨形”必须分层。
5. Garrote, Egido & Robledo, “A microscopic study of the octupole degree of freedom at high angular momentum,” *Phys. Lett. B* **410**, 86–94 (1997), DOI `10.1016/S0370-2693(97)00942-8`，以及其短文 “Theoretical description of the octupole phase transition in lanthanide nuclei at high spin,” *Nucl. Phys. A* **654**, 723c–726c (1999), DOI `10.1016/S0375-9474(00)88535-8`，是本课题的直接理论谱系。当前仓库未取得这两篇全文，故这里只记录书目信息和 RMP 的可定位转述，不把其具体图线或参数冒充已复核原件。

### 能级与电磁证据

| 核素 | $\delta E(I=1)$ (keV) | 高自旋位移示例 (keV) | 证据层与定位 |
|---|---:|---:|---|
| $^{144}$Ba | $+659.2$ | $I=13$: $+168.5$ | Bucher *et al.*, PRL **116**, 112503 (2016), PDF pp.3–4/Table I；本轮脚本输入能级逐项重算 |
| $^{146}$Ba | $+647.4$ | $I=11$: $+78.1$ | Bucher *et al.*, PRL **118**, 152504 (2017), PDF pp.2–5/Fig.2/Table I；本轮脚本输入能级逐项重算 |
| $^{224}$Ra | $+173.8$ | $I=7$: $+20.2$，$I=11$: $-58.3$ | Gaffney *et al.*, Nature **497**, 199–204 (2013), PDF pp.200–203/Figs.3–5；符号反映所采用的局部正宇称参考带 |
| $^{226}$Th | $+194.3$ | $I=15$: $+0.8$，$I=19$: $-5.0$ | NNDC ENSDF Adopted Levels, `226Th`, PDF pp.1–3（1996 evaluation）；K=0+ 基带与 K=0− 八极振动带的评价能级 |

`144Ba` 与 `146Ba` 都有直接库仑激发的 $B(E3;3^-\to0^+)=48^{+25}_{-34}$ W.u. 与 $48^{+21}_{-29}$ W.u.（Bucher 2016/2017，PDF pp.3–4/Table I），但大 $B(E3)$ 本身只证明强八极集体性；$146$Ba 的 $E1$ 变化可由微观中子轨道占据与偶极相消改变，不能用作 $\beta_3$ 的唯一替代量。Gaffney *et al.* 对 $^{224}$Ra 与 $^{220}$Rn 的 Coulomb-excitation 结果在 Nature PDF pp.200–203、Figs.3–5 中将 $Q_2,Q_3$、能级和形状解释并列，且保留静态与振动解释的边界。$^{226}$Th 的 ENSDF PDF p.1 给出 $1^-$ 230.37、$3^-$ 307.5、$5^-$ 450.5、$7^-$ 657.9 keV，p.2 给出高自旋 $K=0^-$ 序列和与正宇称带的 E1 放置；该评价表没有负宇称寿命，不能从中独立反演绝对 $B(E1)$。

### 本轮可复现计算结果

脚本与结果位于 [`octupole-stabilization worker`](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/octupole-stabilization/centrifugal_octupole_model.py)。运行后生成 `centrifugal_octupole_results.json` 与 `parity_displacement_data.csv`。

- 模型采用 $x=\beta_3^2$、$\mathcal J(x)=\mathcal J_0(1+c_3x)$，并用 `V0= k2 x+k4 x²` 表示 Ba 的软单阱，用 $V_0=V_b(1-x/x_0)^2$ 表示 Ra/Th 的示意双阱。
- 在这组明确标注为示意的参数下，$^{144}$Ba 的有限 $\beta_3$ 极小从 $I=11$ 出现，$^{146}$Ba 从 $I=10$ 出现；至 $I=24$，模型最低点约为 $\beta_3=0.139,0.143$，中心势垒/能量增益约 $1.27,1.33$ MeV。
- $^{224}$Ra 和 $^{226}$Th 在 $I=0$ 已有有限极小，模型把其 $\beta_3$ 从 $0.140,0.150$ 推向 $0.163,0.185$（$I=24$），对应中心势垒从 $1.45,0.90$ MeV 增至 $3.35,2.94$ MeV。该数值是模型输入输出，不是实验势垒。
- 解析导数与中心差分在四个核的 $I=12,x=0.013$ 检验中最大绝对误差为 $7.7\times10^{-9}$ MeV，验证了脚本实现的微商。
- WKB-like `delta_model` 仅作趋势示意；它使 Ba 在低自旋保持约 $0.74$–$0.78$ MeV，并在高自旋向零收敛，使 Ra/Th 从约 $0.17$–$0.19$ MeV进一步下降。它不用于替代实验能级，也没有把 Ra/Th 实验负值位移强行改成正值。

## Provisional Reasoning

令 $x=\beta_3^2$，
$$
V_{\rm eff}(x;I)=V_0(x)+\frac{\hbar^2 I(I+1)}{2\mathcal J(x)},\qquad
\mathcal J(x)=\mathcal J_0(1+c_3x).
$$
对 $x$ 求导得到
$$
\frac{\partial V_{\rm eff}}{\partial x}=\frac{\partial V_0}{\partial x}
-\frac{\hbar^2 I(I+1)}{2\mathcal J(x)^2}\frac{\partial\mathcal J}{\partial x},
$$
并且 $\partial\mathcal J/\partial x=\mathcal J_0c_3>0$ 时，第二项严格为负。于是，在 $V_0$ 的斜率仍指向小 $x$ 的区域，离心项减小有效斜率、推动极小点外移；若 $V_0'(x)\le0$，总导数必然为负。更一般地，题设中“导数 $<0$”并非对任意 $x$ 自动成立：在裸势已经上升且 $V_0'(x)$ 足够大时，二者可抵消，极小点由 $V_\mathrm{eff}'=0$ 决定。

对软 Ba 参数化，$I=0$ 的 $V_0'(0)=k_2>0$；离心项使原点失稳的连续分岔近似满足
$$
k_2-\frac{\hbar^2 I(I+1)}{2\mathcal J_0}c_3=0.
$$
这给出一个模型临界 $I$，而不是普适实验阈值。对已经存在双阱的 Ra/Th，$\beta_3\neq0$ 在低自旋就存在，离心项主要增大有限 $\beta_3$ 极小相对于中心区域的能量差。若用集体质量 $B_{33}(\beta_3)$ 和二维势能面 $V(\beta_2,\beta_3)$，应把一维势替换为
$$
H_I=-\frac{\hbar^2}{2}\sqrt{G^{-1}}\partial_a\sqrt{G^{-1}}G^{ab}\partial_b+V(\beta_2,\beta_3)+E_{\rm rot}(\beta_2,\beta_3;I),
$$
其中 $a,b\in\{\beta_2,\beta_3\}$，并对每个 $I$ 做 parity projection/GCM 或集体 Schrödinger 求解。只有这样才能同时处理 $\beta_2$–$\beta_3$ 耦合、坐标依赖惯性和宇称隧穿。

交错位移趋零的动力学图像是：随 $I$ 增大，$\mathcal J(\beta_3)$ 增大使转动能下降，有限 $\beta_3$ 区域相对中心区域降低；当有效双阱的作用量 $S_I/\hbar$ 增大，宇称隧穿劈裂近似按 $\exp(-S_I/\hbar)$ 减小。这个方向与 RMP p.390–391 所述自旋依赖势和 WKB 处理一致，但“势垒超过零点能”只是有用的尺度判据，不能单独推出相变或唯一的刚性标签。

## Assumptions

- $\mathcal J(\beta_3)$ 在研究区间可用 $\mathcal J_0(1+c_3\beta_3^2)$ 近似，且 $c_3>0$；真实 cranked EDF 可能有非单调响应、配对坍塌与 band crossing。
- 一维示意模型忽略 $\beta_2$、$\gamma$、高阶 $\beta_4$ 和 time-odd 场；二维方程只作为应升级的形式化框架。
- 能级输入按每个核的正宇称带逐自旋配对；当带混合或 spin assignment 不稳时，$\delta E$ 不能被解释为纯八极隧穿劈裂。
- 结果 JSON 中的势垒、零点能和 WKB 参数都是可复现的示意输入，不能替代 EDF/GCM 的自洽输出。

## Competing Explanations

1. **离心稳定化**：有限 $\beta_3$ 区域的转动惯量增长足够大，$E_{\rm rot}$ 使该区域随自旋下降，低能交替宇称带逐渐形成。
2. **对齐驱动的反射对称恢复**：RMP p.390 记录 Xe–Sm 区域在约 $I\sim12$ 的反射对称转变和 $^{144,146}$Ba 的高自旋 band crossing；aligned $h_{11/2}$ 质子/中子可能让八极形变减弱，方向与简单单调稳定化相反。
3. **组态交叉/带混合**：交错位移变化可能来自不同准粒子构型的交叉、重新标记或混合，不必等于同一集体势阱的隧穿变化。
4. **八极声子—转动耦合**：Ba 的大低自旋位移和较高 $3^-$ 能量可由软八极声子耦合解释；强 $B(E3)$ 不足以排除该动态图像。
5. **惯性和零点修正**：坐标依赖 $B_{33}$、配对、宇称投影和二维路径可改变势垒—劈裂映射，使同一 $V_b$ 不对应同一 $\delta E$。

## Transfer Conditions

- 将离心项外推到另一核素，至少需要相同定义下的 $\beta_2,\beta_3$、转动惯量、配对方案、能级带身份和自洽 cranking 频率；不能仅以质量数或 $B(E3)$ 缩放。
- $\delta E(I)$ 可跨核比较的前提是同一公式、同一正宇称参考带、可靠的 spin/parity assignment，并记录带交叉和未观测的高自旋成员。
- 将 Ba 的高自旋稳定化图像迁移到 Ra/Th 只能作为假设；Ra/Th 的初始双阱与 Ba 的软单阱不是同一动力学初值。
- 静态形变判定必须与 E3/Q3、E1、parity band、寿命和势能面联合；$E1$ 受质子—中子偶极相消影响，不能单独作否定或确证门。

## Failure Conditions

- 若在已确认的同一交替宇称带中，$I$ 增加时 $\mathcal J$ 下降或 $\partial\mathcal J/\partial\beta_3^2<0$，本课题采用的离心外移方向失效。
- 若经直接带交叉核查后，Ba 的高自旋 $\delta E$ 仍不收敛且 $\beta_3$、$B(E3)$ 与 $B_{33}$ 均不变，说明当前 WKB surrogate 或配对规则不适用。
- 若 226Th 的 ENSDF 负宇称带被后续评价重标号，或取得寿命显示其并非同一 K=0− 结构，当前 226Th 曲线只能保留为历史评价基线。
- 若二维 projected-GCM 计算显示低自旋 Ba 已有深双阱且零点能低于势垒，单纯软振动解释需修订；反之，若势垒始终低于零点能，不能把有限平均场 $\beta_3$ 写成静态梨形。

## Falsification or Reverse Tests

1. 用同一 EDF（如 Gogny-D1S/D1M 或 PC-PK1）在 $I=0$ 到高自旋做约束 $(\beta_2,\beta_3)$ cranking，直接检查 $\partial\mathcal J/\partial\beta_3^2$ 的符号、$V_b(I)$ 和 pairing collapse；将模型输出与本脚本的趋势表分开。
2. 对每个 $I$ 做二维 $\beta_2$–$\beta_3$ 集体 Schrödinger/GCM，比较 parity-projected $\delta E(I)$ 与未经投影的平均场极小；若只改变投影就反转趋势，说明一维势阱论证不足。
3. 对 Ba 的 $I\gtrsim10$ 逐线重建正负宇称能级、alignment、交叉和绝对 E3/E1/E2 强度；若位移收敛只在带交叉后出现，必须把它归入组态重排的竞争解释。
4. 在 $^{226}$Th 取得负宇称带寿命并抽取绝对 $B(E1)$，同时检查 $B(E3)$、$Q_t$ 与高自旋延伸；这可区分 K=0− 八极振动和稳定反射不对称转子。
5. 重跑：
   `python3 outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/octupole-stabilization/centrifugal_octupole_model.py`
   然后检查 JSON 中四个核的 `derivative_check.absolute_error_MeV < 1e-7`，并检查 CSV 的 `source_or_model` 列没有把两类数据混写。

## Open Questions

- Garrote–Egido–Robledo 1997 原文图线中，$^{146}$Ba 的高自旋 $\beta_3(I)$、势垒和集体惯性具体数值是多少？当前只有 RMP 的页级转述和 DOI 元数据。
- 144/146Ba 在 $I\approx10$–$15$ 的 parity displacement、alignment 与 band crossing 是否来自同一组态演化？需要原始高自旋能带论文和逐线 lifetime/E3 数据。
- 226Th 的 $\delta E$ 收敛比 224Ra 慢，究竟主要由较低有效势垒、不同 $B_{33}$、带混合还是评价能级偏差决定？
- 在二维 $(\beta_2,\beta_3)$ GCM 中，离心稳定化是否通过四极形变增大间接改变 $\mathcal J_3$，以及该效应能否在同一核素内被 E2/E3 联合观测区分？
- “$V_b>E_{\rm ZPE}$”作为静态形变阈值的适用范围应如何由 projected-GCM 的 parity splitting 和 wave-function localization 定量校准？

## Human Review

本页为 Codex self-audit 研究笔记，`review_status: unreviewed`。Garrote 1997/1999 全文与具体参数尚未取得；本轮不把 RMP 转述升级为 Garrote 原文核验，也不把示意势垒写成实验事实。用户后续若将具体数值用于论文，应对原始高自旋论文、ENSDF 版本和位移配对逐项复核。

## Promotion or Rejection History

2026-10-29：建立本研究笔记与可复现 worker。保留“离心项可外移有限 $\beta_3$ 极小、提高有效中心势垒并使宇称劈裂收敛”的条件性推断；同时记录对齐、带交叉、二维惯性和投影可能产生相反趋势。未将一维模型或旧审计中的“排他性”措辞晋升为正式知识。
