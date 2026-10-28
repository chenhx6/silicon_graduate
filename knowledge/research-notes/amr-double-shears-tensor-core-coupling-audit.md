---
type: research-note
title: "AMR双剪刀的磁矩、不可约四极张量与核芯耦合：条件代数和Cd/Pd原件审计"
aliases: [AMR T21 T22 algebra, AMR sin4 theta core coupling audit]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [roy-2011-cd110-systematics-antimagnetic, rather-2014-104pd-antimagnetic-first-page, zhang-2019-104pd-pnc-antimagnetic-rotation, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]
created_from: Day26 delegated AMR tensor and core-coupling research
promotion_target: antimagnetic-rotation
tags: [antimagnetic-rotation, 110Cd, 104Pd, tensor-algebra, symmetry, evidence-boundary]
---

# AMR双剪刀：哪些量严格相消，哪些结论仍需要动力学

## Research Trigger

本页回答三个相连但不同的问题：为何理想双剪刀有μ⊥=0；`T21=0、T22=2sin²θ`在哪个归一化下成立；核芯角动量是否必然使实验B(E2)保持平台。其前两项可以在定义明确的几何模型中证明，第三项须对照来源和具体参数。下列“严格”等式均限于明列模型，不是完整核的投影多体波函数结果，不认证历史013工件中的多核输入或≥100普适判据。

## Grounded Evidence

| 问题 | 原件依据 | 证据层 | 限制 |
|---|---|---|---|
| 对称两刃与sin⁴θ | [[rather-2014-104pd-antimagnetic-first-page]] RA14-EX-01，printed061303-1 Eqs.1–2；[[roy-2011-cd110-systematics-antimagnetic]] printed323 Eq.1 | 半经典模型定义 | Rather只取得1/5页，未读其数据表 |
| 110Cd寿命和强度 | Roy printed324 Table1 | 实验报告和由寿命导出的强度 | 表列误差不含可能约20%的stopping系统误差；保留分支/寿命换算边界 |
| core使剪刀闭合变慢 | Roy printed324 Eqs.3–5、printed325–326 Fig.4及讨论 | 给定粒子加转子模型下的作者解释 | 不能把literal方程计算冒称原Fig.4数值完全重现 |
| 104Pd高频下降 | [[zhang-2019-104pd-pnc-antimagnetic-rotation]] PDF p4 Fig.3、pp5–7 Figs.5–7 | PNC-CSM的模型结果/模型失败与拟合 | 正常对齐贡献增加，并不保证B(E2)缓降；形变路径是拟合输入 |

## Provisional Reasoning

### 1. 先定义双剪刀矢量

取总转动轴为z，两支等长、同有效磁g因子的空穴刃为

$$
\mathbf j_\pm=j_h(\pm\sin\theta\cos\phi,\;\pm\sin\theta\sin\phi,\;\cos\theta),
\qquad \mathbf j_n=(0,0,j_n).
$$

两支质子空穴刃共同朝中子合矢量闭合。这里“四刃”可以指两对particle–hole剪刀的示意，但代数自由度为两支对称空穴矢量和一个中子合矢量；不是假定任意核都有两个质子粒子与两个中子空穴。110Cd在Roy方案中恰好相反：π(g9/2)^−2空穴配ν(h11/2)^2粒子。

$$I_{\rm sh}=j_n+2j_h\cos\theta.$$

若磁矩写为`g_h j_+ + g_h j_- + g_n j_n`（角动量数值用ℏ为单位，磁矩用μN），则

$$
\mu_x=\mu_y=0,\qquad \mu_z=2g_hj_h\cos\theta+g_nj_n.
$$

所以“横向相消”与“总磁矩为零”不同。常用相对转子磁矩`Σ(g_a−g_R)j_a`在横向也给相同结论，因为总I的横向分量为零。有效电荷/核芯极化不由磁g因子决定。

若g或刃长度不等，

$$
\mu_\perp=|g_1j_1-g_2j_2|\sin\theta.
$$

取`g1=g(1+ε)、g2=g(1−ε)、j1=j2=j`，则μ⊥=2gjεsinθ，半经典带内M1强度随ε²恢复。它说明精确零来自等价刃对称条件，而非AMR标签给出的无条件算符恒等式。

### 2. Rz(π)、时间反演与平面对称不能混用

`Rz(π)`交换两刃、保中子轴不变；等价刃总密度在该操作下不变。对秩k张量有`Tkq→(−1)^qTkq`，因而理想内禀场中奇q分量为零。对磁偶极这是μ±1=0，对电四极这是Q2,±1=0。

这不意味着单独时间反演T不破缺。T把所有角动量反号，非零总I变为−I，因此有定向自旋的cranked场不保持T。若刃在xz平面，反幺正`S=R_y(π)T`作用在角动量矢量上为

$$(J_x,J_y,J_z)\mapsto(J_x,-J_y,J_z),$$

于是保该平面几何。普通平面MR也可以保S；AMR额外的两刃交换对称与它不同。`Rz(π)`也不能推出好宇称；signature和parity为独立对称量。

若量子模型确实有同一离散算符U=Rz(π)，且态是其本征态`U|i〉=ri|i〉、U|f〉=rf|f〉`，则矩阵元满足

$$[1-r_f^*r_i(-1)^q]\langle f|T_{kq}|i\rangle=0.$$

因此同signature态间奇q分量确实为零；不同signature态间则可能允许。这个式子要求明确体轴、状态及对称算符，与实验室系只因选定M而得到的期望值相消不同。单个`|j=1,m=0〉`就有〈Jx〉=〈Jy〉=0而〈1,±1|J±|1,0〉≠0，给“期望零不能推出所有跃迁零”的最小量子反例。

实验室好I态中的横向算符期望本来就不能替代跃迁矩阵元。理想平均场的无横向旋转磁矩给出该模式的半经典M1辐射为零；需要离散对称量子化/投影进一步讨论具体态间选择定则。固定signature的ΔI=2序列没有自身的I−1成员，且两个相邻ΔI=2成员之间M1受一般三角选择规则禁戒；这些事实不禁止任意跨带M1。不存在从μ⊥期望为零推出全核所有B(M1)=0的步骤。

### 3. 显式推导不可约四极分量和归一化

定义单位方向`n=(x,y,z)`上的Racah归一化球谐函数

$$
C_{2m}(\hat n)=\sqrt{\frac{4\pi}{5}}Y_{2m}(\hat n),
$$

$$C_{20}=\frac12(3z^2-1),\qquad
C_{21}=-\sqrt{\frac32}z(x+iy),\qquad
C_{22}=\sqrt{\frac38}(x+iy)^2.$$

两支等权q的轴向四极张量相加，得

$$
Q_{20}=q(3\cos^2\theta-1),\quad Q_{21}=0,\quad
Q_{22}=2q\sqrt{\frac38}\sin^2\theta e^{2i\phi}.
$$

理由是C21对横向投影变号，为奇；C22是横向投影的平方，为偶。负m分量由厄米张量关系`Q2,−m=(−1)^m Q2m*`得到，同样Q2,−1=0。

若另定义纯角度张量

$$T_{2m}\equiv\frac{Q_{2m}}{q\sqrt{3/8}},$$

才得到题目指定的

$$\boxed{T_{21}=0,\qquad T_{22}=2\sin^2\theta e^{2i\phi}.}$$

选择刃平面φ=0时`T22=2sin²θ`为实数。这里T已按q及常数归一化，不能把系数2直接当物理e·b四极矩；实际换算必须保留所用张量、电荷及转子约定。

半经典转动辐射取关于转轴的m=±2振幅，其模平方给

$$\frac{B(E2;\theta)}{B(E2;90^\circ)}=\sin^4\theta.$$

Roy Eq.1的绝对尺度处方为

$$B(E2)=\frac{15}{32\pi}(eQ_{\rm eff})^2\sin^4\theta.$$

归一化角张量本身不能确定Qeff或这个绝对前因子。θ→0时m=±2趋零，m=0却可非零；“绕轴的四极辐射消失”不等于电荷四极形变全部消失。

| θ | T22（φ=0） | sin⁴θ | 相对90°强度下降倍数 |
|---|---:|---:|---:|
| 90° | 2.000000 | 1.000000 | 1 |
| 60° | 1.500000 | 0.562500 | 1.778 |
| 45° | 1.000000 | 0.250000 | 4 |
| 30° | 0.500000 | 0.062500 | 16 |
| 15° | 0.133975 | 0.004487 | 222.85 |

上述是固定q的几何计算，不是给Cd实际各核态测定的角度。旧“90°→15°只降20倍”算术错误；也不能用这段几何强行赋予实验完整角轨迹。单剪刀MR的E2也可有sin⁴型因子，并不存在MR普适sin²、AMR普适sin⁴的模式专属区分；见[[clark-2000-shears-mechanism]] CL00-D23-003。

### 4. 核芯角动量为何可以使几何闭合变慢

按Roy printed323 Eq.2的势能系数，写

$$E(I,\theta)=\frac{[I-I_{\rm sh}(\theta)]^2}{2\mathcal J_c}+V_{\rm sh}(\theta),$$

$$V_{\rm sh}=V_{\pi\nu}P_2(\cos\theta)
-\frac{V_{\pi\pi}}{n}[P_2(\cos2\theta)-1].$$

原势能前因子不能擅加3；以下取导数可直接回核Eq.4。固定I的平衡条件给

$$R=I-I_{\rm sh}=\mathcal J_c\frac{dV_{\rm sh}/d\theta}{dI_{\rm sh}/d\theta}
=\mathcal J_c\omega_{\rm sh},$$

$$\omega_{\rm sh}=\frac{1.5V_{\pi\nu}}{j_h}\cos\theta
-\frac{6V_{\pi\pi}}{nj_h}\cos2\theta\cos\theta.$$

令c=cosθ、K=15(eQeff)²/(32π)。纯剪刀有`dI/dc=2jh`，耦合后

$$\frac{dI}{dc}=2j_h+\mathcal J_c\frac{d\omega_{\rm sh}}{dc},\qquad
\frac{dB}{dI}=\frac{-4Kc(1-c^2)}{2j_h+\mathcal J_c\,d\omega_{\rm sh}/dc}.$$

当所用分支`dωsh/dc>0`且稳定时，核心响应扩大分母，在相同θ处使B随I下降更慢。这是有条件的动力学推论。若存在组态交叉、不同响应符号、Qeff随I变化，结论需重新求解。

核心角动量与核心电四极振幅是不同输入。若核心自身具有绕转轴的m=2振幅，须计算

$$B(E2)\propto|A_{\rm sh}(\theta)+A_{\rm core}(I)|^2,$$

含相干交叉项；不能简单把“R增加”写成“B必然增加”，也不能任意相加两个B值。

### 5. 按Roy打印方程直接求根：机制成立不等于曲线已复现

取原文参数`jh=4.5、jn=10、Jc=19.5 ℏ²/MeV、Vpn=1.2 MeV、Vππ=0.15 MeV、n=4、eQeff=1.1 eb`，严格解Eq.3得到下表。未添加源文未明确写入Eq.3的spin offset。

| I | θ（度） | R（ℏ） | R/I | B(E2)按Eq.1+3（e²b²） | 原Table1报告B(E2)（e²b²） |
|---:|---:|---:|---:|---:|---:|
| 16 | 70.005 | 2.92255 | 18.27% | 0.14079 | 0.14(1) |
| 18 | 62.561 | 3.85276 | 21.40% | 0.11201 | 0.12(2) |
| 20 | 54.233 | 4.73955 | 23.70% | 0.07826 | 0.11(2) |
| 22 | 44.337 | 5.56278 | 25.29% | 0.04307 | 0.09(3) |
| 24 | 31.066 | 6.29087 | 26.21% | 0.01280 | 0.06(2) |

原寿命数据是0.36(3)、0.23(3)、0.17(3)、0.21(7)、0.27(7) ps；Eγ为1075、1224、1323、1314、1358 keV。此处保留原表报告值，未用寿命常数重写B；分支/归一化问题参见[[cd110-branch-normalization-boundary]]。

这里R/I为总自旋比例。16→24的增量比例是

$$\frac{\Delta R}{\Delta I}=\frac{6.29087-2.92255}{8}=42.10\%,$$

不能把18%–26%说成“自旋增益分担比例”。同一参数下24态计算0.01280与报告0.06不一致，故不能称“完美再现平台”。源文另假定12ℏ带头，并在Fig.4讨论不同bandhead/总自旋域；仍需作者计算或明确的spin映射才能把打印Eq.3与整条图曲线逐点对应。这里保留这个复现缺口，不靠未说明的shift调成吻合。

固定该经典刃长度时，纯剪刀`Imax=10+9=19`，耦合打印式最大25.825；这只是经典有效向量上界。相同g9/2壳中两个相同空穴受Pauli限制，精确最大耦合J=8；再加冻结中子对J=10，显式四准粒子子空间最多18。19不是完整量子核的严格终止定理。Roy printed326还明确认为最高28⁺不由该AMR机制产生，不能把观察到28⁺写成模型已解释至28⁺。

### 6. Pd微观模型提供反向检验：normal rotation不必带来平台

[[zhang-2019-104pd-pnc-antimagnetic-rotation]] ZH19-PD-03/06/07给出比“核芯使E2变平”更细的结果：

- PNC-CSM中，约0.45–0.55 MeV质子对齐增益较快，更高频率中子(g7/2,d5/2)对齐增益较快；作者称两阶段AMR。此处normal-rotation贡献不是另加独立inert core，不能直接套用Roy的Jc和R百分比。
- 固定ε2=0.18模型虽有双剪刀及配对，仍不能重现ℏω>0.6 MeV的B(E2)快速下降。作者通过拟合令ε2逐渐减小，在约0.75 MeV趋零以追踪数据；该路径不是独立测得的形变演化。
- 两阶段几何中低频off-diagonal配对贡献使四刃长度分解不唯一；高频忽略较小off-diagonal项才近似画独立刃；横向刃取sqrt〈Jz²〉，不是直接定向期望〈Jz〉。

因此，Cd/Pd核中的角动量重分配、几何闭合、配对、形变演化和电四极相干幅度应分别求解。110Cd原作者的core缓降解释有明确对象，不是覆盖所有Pd同位素的恒定平台定律。

## Reproducible Artifacts

工件目录：`outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-tensor-core-20261029/`。

- `amr_tensor_core_audit.py`：标准库实现矢量与球张量、对称性网格残差、破缺参数扫描、Roy Eq.3二分求根及势能导数回核。
- `amr_tensor_core_audit.json`：来源签名/哈希/阅读覆盖、边界、计算结果及APS401失败记录。
- `angular_tensor_table.csv`：固定张角的归一化张量与sin⁴强度。
- `roy_literal_core_comparison.csv`：报告实验值与打印方程条件输出逐列分开。

181个θ、31个φ共5611组计算中，μ⊥和C21残差为0，T22恒等式最大绝对残差8.96×10⁻¹⁶，Rz(π)四极总张量不变性最大残差2.64×10⁻¹⁵，势能导数与Eq.4残差5.56×10⁻¹⁷。二分求根的spin残差<10⁻¹²。这些残差认证代数实现；不认证EDF、自洽占据、实际实验角或全多体跃迁。

## Assumptions

等价刃、相同磁权重和电四极权重、共同θ与φ、固定q/Qeff、已定义的总转轴；半经典辐射处方与Roy固定参数。有限壳层Pauli上界与经典向量长度使用不同模型对象。

## Competing Explanations

低E2和高J²/B也可能涉及弱集体性、对齐/交叉、终止、形状演化与寿命分支输入。104Pd结果表明几何/normal alignment不能唯一决定E2形状。J^(2)/B(E2)有量纲，≥100不是无条件排他门；1323→1314 keV的负有限差分不能为美化曲线而删除。

## Transfer Conditions

可迁移的是张量变换律、明确定义下的奇q相消、相干振幅求和及动力学求导方法；不可迁移的是固定Qeff、Jc、R/I、ΔR/ΔI、形变路径、完整多核阈值或特定签名r=+1。奇A签名可能为±i。

## Failure Conditions

刃不等价、三维不对称、不同磁/电权重或重要配置混合时，精确相消须重算。若无明确归一化直接宣称物理T22=2sin²θ，若把μ⊥=0写成所有磁矩/所有跨带M1为零，或用拟合形变宣布独立实验验证，均越过本页证据。

## Falsification or Reverse Tests

让磁权重失配ε，检查M1强度以ε²恢复；让电权重失配，检查Q21以ε恢复；保μ⊥=0但改变Qeff(I)，可得到不同B(E2)趋势；保双剪刀几何但改变核芯响应，则dB/dI不必相同。上述受控反向例可区分哪些结论来自离散对称，哪些来自动力学输入。

## Open Questions

Roy Eq.3与Fig.4的bandhead/spin映射能否获得原始代码确认？用同一投影/配对方案能否同时预测Cd/Pd的绝对E2和弱带间M1？如何以独立寿命或静态四极矩约束104Pd拟合形变，而非继续从同一B(E2)反演？

## Knowledge Impact and Learning Decision

`supports` 对称双剪刀的横向磁矩与奇q相消、固定几何sin⁴律和有条件核芯缓降机制；`revises` MR/AMR幂次独占区分、18%–26%增益措辞、19ℏ量子硬上界及完美平台复现；`limits` 从Rz推好宇称、从反幺正平面对称推单独T对称和跨Pd普适平台。与[[day26-quantitative-claim-corrections]]一致，未恢复013历史认证。

## Sources

- [[roy-2011-cd110-systematics-antimagnetic]]
- [[rather-2014-104pd-antimagnetic-first-page]]
- [[zhang-2019-104pd-pnc-antimagnetic-rotation]]
- [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]
- [[clark-2000-shears-mechanism]]

## Human Review

Codex source/claim self-audit；未升级`human-reviewed`，原学分、撤回与人工审核边界保留。

## Review Status

保持provisional/unreviewed。代数数值自检已完成；核模型本征态、论文级原Fig.4逐点复现和Rather剩余4页仍未完成。

## Promotion or Rejection History

2026-10-29：新增条件张量推导、Roy literal求根和104Pd PNC-CSM原件反向检验，保留缺页及复现差异，不发放额外课程学分。
