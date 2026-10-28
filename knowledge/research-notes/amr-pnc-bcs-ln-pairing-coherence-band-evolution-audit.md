---
type: research-note
title: "AMR中的PNC、BCS/LN与配对相干：粒子数、非对角项和能带演化审计"
aliases: [PNC BCS LN pairing fluctuations AMR, pairing coherence Cd Pd band evolution]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [zhang-2013-105106cd-pnc-superfluidity, zhang-2019-104pd-pnc-antimagnetic-rotation, wu-2011-pairing-rotation-blocking-pnc, sheikh-2002-number-projection-pairing-comparison]
created_from: Day26 delegated PNC pairing and band-evolution research
promotion_target: antimagnetic-rotation
tags: [antimagnetic-rotation, PNC-CSM, BCS, Lipkin-Nogami, pairing, band-crossing, 105Cd, 106Cd, 104Pd]
---

# AMR中的PNC、BCS/LN与配对相干

## Research Trigger

本页追问：有限核高转频下的配对减弱应怎样与BCS异常场锐崩溃区分？PNC-CSM究竟精确保存什么、仍近似什么？105/106Cd和104Pd的非对角项如何影响背弯、剪刀几何和B(E2)？

本轮发现两个必须先纠正的用语：**固定N态的异常平均〈aa〉严格为0，但配对关联可以非零；文中off-diagonal alignment也不是哈密顿量的off-diagonal pairing矩阵元。** 105Cd原文显示配对推迟中子交叉并使剪刀闭合更明显；104Pd显示先快后慢的两阶段闭合。因此不能预设“所有非对角配对项都延缓剪刀闭合”。

## Grounded Evidence

| 问题 | 原件/locator | 已支持的结果 | 证据边界 |
|---|---|---|---|
| BCS/HFB与固定N | [[wu-2011-pairing-rotation-blocking-pnc]] PDF pp2–5 Eqs1–12 | PNC在CMPC Fock空间对角化；粒子数固定、阻塞显式；关联能型gap与BCS异常场定义不同 | 不是全核精确解，不含实际AMR新实验 |
| LN、PAV和PHFB | [[sheikh-2002-number-projection-pairing-comparison]] PDF pp8–13 Figs1–6讨论 | 在其精确可解推转模型中，LN改善但弱配对时仍可能崩溃；PAV不自动修复无配对基态；PHFB的总能与对齐角动量与模型精确解吻合 | 具体0.45G阈值仅适用于该模型；不能外推所有核 |
| 105Cd背弯与几何 | [[zhang-2013-105106cd-pnc-superfluidity]] PDF pp7–10 Figs2–4 | 约0.4 MeV的νg7/2对齐；配对使几何图中的中子交叉推迟、对齐渐进，质子空穴闭合更明显 | 两支空穴的Jz用RMS近似，不是直接方向测量 |
| 106Cd背弯与E2 | 同上PDF pp7–9 | 约0.3 MeV有gd→h11/2占据改变；固定ε2不足，高频需0.14→0.12形变变化 | 配对和双剪刀不能独自解释全部B(E2) |
| 104Pd非对角对齐 | [[zhang-2019-104pd-pnc-antimagnetic-rotation]] PDF pp5–7 Figs4–7 | 低频质子非对角Jx贡献显著；π5/2+[422]—π7/2+[413]与π7/2+[413]—π9/2+[404]等干涉项参与渐进对齐；高频其贡献变小 | 这些是单体算符期望的干涉项，不能当作配对势矩阵元 |
| 104Pd高频E2 | 同上PDF p4 Fig3 | 配对改善总体比较，但固定ε2=0.18不能给出>0.6 MeV的快速E2下降；作者另拟合ε2向0变化 | 形变路径来自同一B(E2)拟合，不是独立验证 |

## Provisional Reasoning

### 1. BCS、LN与PNC在求什么

对给定推转哈密顿量

$$H'(\omega)=H_{\rm Nil}-\omega J_x-G\sum_{\xi\eta}P_\xi^\dagger P_\eta,\qquad P_\xi^\dagger=a_\xi^\dagger a_{\bar\xi}^\dagger,$$

三种方法的核心区别如下：

| 方法 | 多体态/变分对象 | 粒子数和配对 | 主要边界 |
|---|---|---|---|
| BCS/HFB | 准粒子真空；BCS常用∏(u+vP†) | 固定〈N〉，通常Var(N)>0；Δ由κ=〈aa〉构成 | 单一平均场忽略重要有限体系关联；阻塞、约束与分支选取影响高频解 |
| Lipkin–Nogami | 在破数变分中采用二阶Kamlah展开的λ2近似数投影修正 | 改善粒子数问题，但通常不是严格N本征态 | 近似数投影/二阶展开；弱配对区不保证与严格投影相同 |
| PAV | 先得到HFB态，再作PN投影 | 投影后的态有固定N | 原HFB若已变成单一固定N行列式，仅作事后投影不能恢复被变分遗漏的配对混合 |
| 投影变分/PHFB | 优化投影后的能量 | 恢复粒子数且允许配对关联 | 依赖变分族、投影与实现；本页来源的成功是指定模型基准 |
| PNC-CSM | 固定N的CMPC线性组合直接对角化 | Var(N)=0；显式处理Pauli占据与阻塞，保留配对散射导致的组态混合 | 精确性限于给定哈密顿量和截断；不自动恢复总角动量，不自动自洽求形变 |

PNC与严格投影是不同的解法；PNC不是处理有限核配对的唯一途径。标准BCS/HFB加适当投影、GCM等关联，也能改善锐崩溃。LN在不少应用中可使下降更平滑，但Sheikh2002给出了其弱配对失效的直接模型反例，不能一概说LN与裸BCS完全相同，也不能说LN保证绝不崩溃。

### 2. 高频锐崩溃为何可能是变分伪相变

未转动BCS的示意gap方程为

$$1=G\sum_k{1\over2\sqrt{(\epsilon_k-\lambda)^2+|\Delta|^2}}.$$

转动后Coriolis分裂、准粒子占据及阻塞改变配对易感性；当线性化配对核不足以维持非零Δ，单一变分解会落到Δ=0分支。此时锐变可能反映变分族的分岔或分支跳转，而非有限核中所有两体配对关联突然严格为零。变形壳、配对相互作用及对角自能约定都会改变临界点，不能给核素无关的ωc。

这里“有限体系涨落洗掉锐热力学相变”有边界：**固定N不排除不同对称性或不同组态的真实能级交叉。** PNC仍可出现背弯、非解析的基态分支交换或有限空间完全极化后的关联消失；它没有“所有谱函数随ω严格光滑”的定理。

### 3. 固定N时，什么量还可以叫配对

对N本征态，aa将N改变2，故

$$\langle\Psi_N|a_ka_{\bar k}|\Psi_N\rangle=0.$$

这不意味着

$$\langle\Psi_N|P^\dagger P|\Psi_N\rangle=0.$$

可以报告〈HP〉、不同轨道的〈P†iPj〉、合适的连接关联函数、配对算符方差或N↔N±2的对转移振幅。Wu2011 Eq10采用

$$\widetilde\Delta=\sqrt{-G_0\langle H_P\rangle},$$

这种关联能型量是诊断定义；它不能不加说明就等同于BCS的Δ=G〈P〉。尤其〈P†P〉通常包含对角占据/自配对项；若想排除无关联基线，应在**同一相互作用、自能和减项约定下**定义，而不能看见非零〈HP〉便宣布集体配对全部幸存。

PNC所保留的“配对涨落”是固定N态中不同配对占据组态的量子混合，**不是粒子数涨落**，也不是已经求解了热涨落或实时间随机动力学。

### 4. 三种非对角项必须分栏

PNC态写为|Ψ〉=ΣαCα|α〉。对于固定CMPC基底：

1. **配对哈密顿量非对角项**：Vαβ=〈α|HP|β〉，直接在对角化矩阵中耦合组态，典型过程转移一对粒子。若基底随ω改变，必须声明所在基底。
2. **单体算符非对角干涉项**：

$$\langle O\rangle=\sum_\alpha|C_\alpha|^2O_{\alpha\alpha}+2\operatorname{Re}\sum_{\alpha<\beta}C_\alpha^*C_\beta O_{\alpha\beta}.$$

对于O=Jx或Q20，Slater–Condon规则只允许相差一个单粒子占据的组态相连。文献Figs5–6中的off-diagonal alignment属于这一层；因子2是否已经吸收到jx(μν)须按各文Eq6约定。
3. **配对相干关联**：〈P†iPj〉是两体密度；不同于Oαβ，也不同于其贡献CαCβOαβ。

最小反例：两个组态分别是“低能轨道一整对”和“高能轨道一整对”。它们相差两个单粒子占据，配对势矩阵元可为−G，但任意单体O在这两个组态间的矩阵元均为0。它们仍可有显著〈P†1P2+h.c.〉。因此，“非对角配对增强”不能直接替换成“非对角Jx变大”，更不能从一个干涉项的正负推断配对强度或剪刀速率。

### 5. 配对如何推迟或平滑能带交叉

考虑两个相同对称性的有效构型A、B：

$$H_{AB}'=\begin{pmatrix}E_A(\omega)&W(\omega)\\W^*(\omega)&E_B(\omega)\end{pmatrix}.$$

固定W时，混合产生最小间隙2|W|，把突然的组态转换展宽。若EA=eA−JAω、EB=eB−JBω，混合中心仍在EA=EB处；**非对角W单独增大主要改变宽度，不自动把中心推到更高频率。**

若两构型的对角关联能为δEA、δEB，则

$$\omega_c={e_B-e_A+\delta E_B-\delta E_A\over J_B-J_A}.$$

低对齐构型A得到更大的负配对关联能时，可提高交叉频率。实际PNC里对角能、非对角混合、占据和单粒子轨道都随ω变，不能只用W一个数解释延迟。

对固定参数的推转本征值，Hellmann–Feynman关系给Jx=−dE′/dω。配对通过改变波函数与能量曲率调节对齐和惯量；它既能平滑/推迟某次中子交叉，也能在另一频段促进质子占据重排和更快的几何闭合。若形变或G显式随ω改变，上述导数还应审计相应参数导数。

### 6. 105Cd、106Cd：原件支持的是“交叉延迟”和“闭合更明显”

Zhang2013采用ε2=0.12/0.14，CMPC维数约1000（各质子/中子空间），Gp均0.45 MeV；105Cd的Gn=0.80、106Cd的Gn=0.45 MeV。作者依据105Cd惯量较小而选更大的有效中子配对强度。**因此不能把两核全部差异归给自动阻塞**，也不能把拟合后的G变化当作独立测量。

- **105Cd**：关掉配对会高估惯量；首背弯约0.4 MeV归于νg7/2中子对齐。Fig4无配对在0.5–0.6 MeV有中子对齐突增；加入配对后交叉推迟、对齐更渐进。两质子空穴仍朝中子合矢量闭合，且原文称闭合更明显。因此可说配对改变角动量在中子与质子间的分配，不能说它普遍抑制质子闭合。
- **106Cd**：约0.3 MeV交叉涉及(g7/2,d5/2)→h11/2占据转移；固定形变计算不能完整重现高频B(E2)，作者需ε2由0.14降至0.12。
- **E2**：两核不论有无配对都呈下降趋势。105Cd在0.45–0.75 MeV，配对计算〈Q20〉由0.55降至0.41 eb，B(E2)相应约剩55%；这是同一模型的结果，非实验直接测得内禀Q轨迹。
- **几何边界**：由于签名对称，〈Jz〉=0；Fig4用√〈Jz²〉画刃，不可把RMS矢量解释成每个空穴的直接定向期望。PNC也没有恢复实验室good-I波函数。

### 7. 104Pd：低频非对角对齐使四刃分解失效，高频E2仍需形变

Zhang2019采用Gp=0.5、Gn=0.8 MeV，截断CMPC各约1000；这些与Cd参数不同，不能直接把数值G当可跨空间比较的裸作用强度。其主要结果为：

- 中子ν1/2−[550]在约0.4 MeV占据从约0.4跃至2，gd占据相应减少；h11/2中子对齐导致背弯。
- 约0.4–0.55 MeV，质子g9/2占据重排显著，π5/2+[422]—π7/2+[413]和π7/2+[413]—π9/2+[404]等非对角Jx项参与渐进对齐。
- 约0.45–0.60 MeV，质子刃闭合较快且刃长变化；配对带来的非对角贡献使单根空穴角动量难以唯一分开。
- 约0.60–0.75 MeV，非对角Jx贡献较小，对应四个g9/2空穴的单粒子态占据接近0，才可近似分成独立刃；闭合转为较慢、平稳，同时gd中子对齐继续增长。
- 固定ε2=0.18即使保留配对，也无法重现>0.6 MeV的快速B(E2)下降。作者把ε2拟合到约0.75 MeV趋0；这是反演形变输入，不是PNC自动预言的独立实验形变。

这条证据链不支持“低频非对角配对只会延缓闭合”：在该模型，配对与占据重排反而使低频闭合更快、不同于无配对TAC的近等长平稳刃。它支持的是两阶段重组，以及单体干涉项显著时经典刃分解有边界。

### 8. 三个可复算的有限模型控制

#### A. 同一哈密顿量下，BCS gap可归零而固定N的配对相干仍在

取两个时间反演轨道对、N=2、ε1=−ε、ε2=ε，明确去掉i=j对角自配对项：

$$H=\sum_i\epsilon_iN_i-G(P_1^\dagger P_2+P_2^\dagger P_1).$$

固定N的一对空间矩阵为

$$H_{N=2,v=0}=\begin{pmatrix}-2\epsilon&-G\\-G&2\epsilon\end{pmatrix},\quad E_0=-\sqrt{4\epsilon^2+G^2}.$$

精确的对转移相干为

$$C_{12}=\langle P_1^\dagger P_2+P_2^\dagger P_1\rangle={G\over\sqrt{4\epsilon^2+G^2}}.$$

对同一H采用对称BCS变分、〈N〉=2，令v1²=x、v2²=1−x，则

$$E_{\rm BCS}=2\epsilon(1-2x)-2Gx(1-x),\quad x=\min(1,\tfrac12+\epsilon/G),$$

$$\Delta_{\rm BCS}=G\sqrt{x(1-x)}.$$

在ε=G/2处Δ归0，固定N的C12仍为1/√2。G=0.8 MeV时该点ε=0.4 MeV，Eexact=−1.13137 MeV，EBCS=−0.8 MeV，C12=0.707107，Var(N)exact=0；与此同时两种态的异常平均定义不能混用。这是**壳间距控制的有限变分反例**，不是把ε伪装成实际Cd/Pd的ω。

#### B. 非对角混合展宽并不自动延迟

取EB−EA=−6(ω−0.4)、W=0/0.02/0.10 MeV。W>0的混合曲线在ω=0.4具有相同50%构型权重；W=0时该点简并，不能指定唯一混合权重；最小间隙与典型宽度分别为2W、2W/6。这定量区分了“平滑”与“中心移动”。真实核延迟仍需不同对角关联能等输入。

#### C. 固定N仍允许真实转动交叉

对控制A加−ωJ，令两个正签名单粒子各有j=+1/2、负者各−1/2。一对态J=0；占两个正态的阻塞态J=1，配对作用为0。固定N基态能量为

$$E_0(\omega)=\min[-\sqrt{4\epsilon^2+G^2},-\omega].$$

ε=0.2、G=0.8 MeV时在ωc=0.894427 MeV/ℏ有不同守恒J扇区的真实交叉；J从0跳到1。这不违反PNC，也不是热力学配对相变。它防止把“固定N”误宣传为普遍平滑保证。

## Reproducible Artifacts

目录：`outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-pnc-bcs-pairing-20261029/`。

- `pairing_finite_number_controls.py`：三个有限模型闭式计算，不宣称实际核的PNC对角化。
- `bcs_exact_shellgap_control.csv`：121个控制点，保留BCS gap、精确相干、粒子数方差与配对算符方差。
- `effective_avoided_crossing.csv`：21个有效混合点。
- `exact_N_genuine_cranking_crossing.csv`：真实不同对称扇区交叉控制。
- `pairing_model_summary.json`：方程、参数、临界点及不可外推边界。
- `plot_pairing_controls.py`、`pairing_finite_number_controls.png/.pdf`：三面板独立科研图。图中特别注明ΔBCS与精确相干是不同诊断量。
- `provenance.json`：PDF签名、页数、哈希与实际阅读覆盖；Crossref回包单列。

## Assumptions

Cd/Pd结论限于来源给定Nilsson势、单极配对和截断；Wu来源还讨论四极配对，不与Cd/Pd单极模型混同。自建控制模型去掉对角自配对项，以便相同H下比较BCS与固定N；其G和阈值不外推到核素。量子组态相干不是热涨落。

## Competing Explanations

背弯与E2变化还可来自准粒子对齐、占据交叉、形变收缩、固定N变分族以外的相关、side-feeding/stopping和分支归一。配对模型改善拟合不等于已唯一识别某个off-diagonal pairing矩阵元，也不排除其它残余作用。

## Transfer Conditions

可迁移的是粒子数/异常平均的代数、Slater–Condon规则、相干与单体干涉分栏、同一H比较和混合宽度/中心区分。不可迁移的是Gn=0.8、具体ω交叉、ε2拟合路径、某个单j阈值或PNC截断维数带来的核素预测。

## Failure Conditions

把PNC中的〈aa〉说成非零；把配对涨落说成粒子数涨落；把off-diagonal Jx改名为off-diagonal pairing；把平滑等同延迟；把PNC说成所有转频永不崩溃；把B(E2)形变反演当独立预测，均使推论失效。

## Falsification or Reverse Tests

固定H和截断，分别保留/去掉HP的非对角CMPC矩阵元，检查占据、相干、Jx和Q20；同时更换单粒子基底检验“对角/非对角份额”的基底依赖。在相同H中比较PNC、BCS、LN、PAV、VAP，并分别报告〈HP〉、减基线关联、Var(N)与对转移。只改W而不改对角能，应展宽而不移动交叉中心。

## Open Questions

能否取得Cd/Pd原始CMPC权重和一/两体密度，逐项提取HP而非仅Jx非对角项？同一Hamiltonian下LN/VAP与PNC对AMR的绝对B(E2)分歧多大？若固定形变和配对参数，PNC能否预测独立holdout寿命与弱跨带M1？

## Sources

- [[zhang-2013-105106cd-pnc-superfluidity]]
- [[zhang-2019-104pd-pnc-antimagnetic-rotation]]
- [[wu-2011-pairing-rotation-blocking-pnc]]
- [[sheikh-2002-number-projection-pairing-comparison]]
- [[amr-cd-isotopes-quantum-termination-odda-signature-audit]]
- [[amr-pd-four-hole-geometry-evolution-audit]]
- [[amr-vpinu-neutron-number-core-polarization-audit]]

## Human Review

Codex source/claim self-audit；保持`unreviewed`。没有改写既有撤回、人工审核或课程信用。

## Review Status

Cd/Pd配对和几何原件已重读；新增PNC方法与数投影基准来源已定向阅读；三个有限控制模型已闭式生成。没有运行实际Cd/Pd的完整PNC或LN/VAP重算。

## Promotion or Rejection History

2026-10-29：建立PNC/BCS/LN分层笔记；拒绝“配对一定延缓所有剪刀闭合”“固定N保证所有曲线平滑”“off-diagonal alignment就是配对矩阵元”的预设。

## Continuation Handoff

若继续，先寻找原作者CMPC密度与配对矩阵输出；在相同Hamiltonian、单粒子势、变形和截断下比较多方法。先确定异常平均、关联能减项与频率约定，再讨论高频“配对幸存”的定量幅度。
