---
type: research-note
title: "135Pr MR 交叉、有限 j 重耦合与偏振判据的原件边界"
aliases: [135Pr shears crossing source boundary, MR Racah polarization boundary]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [garg-2015-135pr-magnetic-rotation, garg-2019-135pr-polarization-erratum, clark-2000-shears-mechanism, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]
created_from: Day26 independent primary-source and operator audit
promotion_target: magnetic-rotation
tags: [135Pr, magnetic-rotation, shears, band-crossing, Racah-algebra, polarization, evidence-boundary]
---

# 135Pr MR 交叉、有限 j 重耦合与偏振判据的原件边界

## Research Trigger

核验“135Pr 的交叉后比值反弹、i13/2 中子对齐、有限 j 零点能量、偏振排除 TW”这条因果链。以下逐项区分原件报告、模型推导与尚未测得的量；不能把成立的角动量代数移作实验模式的认证。

## Grounded Evidence

本轮直接读取 Garg 2015 PDF pp.2、6–8，Garg 2019 Erratum pp.1–2。2015 文件 SHA256 为 `c74e7c12614cf405861c639194e132f3096d5f46d22062b0164fa166282b9e88`、9页；2019 为 `c9fbed8bb0a1463c6d083f29e1331ff72102f5fb4edfdd96b76f3c5c0149db30`、2页。Clark 2000 的经典剪刀式沿用既有 [[fixed-j-quantum-shears-m1-boundary]] 的 p.15 Eqs.(5)–(7) 来源定位，不声称本轮新完整阅读该综述。

| ID | 陈述 | 分层与 locator | 边界 |
|---|---|---|---|
| MR-SB-1 | 低/高段 TAC 配置分别为 π(h11/2)¹⊗ν(h11/2)⁻²、π(h11/2)¹(g7/2)²⊗ν(h11/2)⁻² | 作者模型解释；Garg2015 p.7，与p.8结论一致 | 新增的是 g7/2 质子对；没有 ν(i13/2)²，也没有原文 g7/2/d5/2 混合配置 |
| MR-SB-2 | 交叉 ℏω≈0.37 MeV，I≈33/2−；27/2− 是3530-keV带低端 | 作者谱学报告；p.7–8；带低端身份TableI/p.7 | 不能把27/2称5qp交叉点 |
| MR-SB-3 | B(M1)/B(E2) 随自旋上升到约35/2−；高自旋 crossover 未观测，作者明确说不能从比值解释交叉后行为 | 直接原文范围；p.7末至p.8首、Figs5/7 | “交叉后反弹已实测”不是本文结论；该因果链不闭合 |
| MR-SB-4 | 未测该带寿命，不能给绝对B(M1)；未来寿命可帮助确认MR | 实验限制；p.7，p.8结论 | 仍有由同母态分支推出的相对B比，不应写成“没有强度信息” |
| MR-SB-5 | 813.3-keV Δ由−0.20(8)改为+0.04(3)，747.5由−0.05(3)改为+0.03(3)，两线仍列M1+E2 | 勘误直接报告；2019p.1 TableI | Δ是偏振不对称度，不是除过灵敏度Q后的P；未给δ区间 |
| MR-SB-6 | 813.3原DCO=0.22(2)，747.5原DCO=0.25(1)，均在四极门下 | 2015p.2 TableI；2019正文重申813值 | 不应换成0.98(5)；门型上标Q不能当灵敏度Q |
| MR-SB-7 | Band3是高自旋ΔI=1候选MR；Bands1/4的748/813-keV连接涉及另一组低自旋结构 | 2015p.6 Bands2/4/5与Band3分别讨论；p.7–8 | 同核不同带不能归并为“同一带MR与TW二选一” |

上述均是 Codex 定向 self-audit；页面仍 `review_status: unreviewed`。

## Provisional Reasoning

### 1. 经典剪刀：可推得的条件关系

先假设无芯、两可区分刚性角动量，I、jp、jn均以ℏ为单位，μ以μN为单位：

$$\mathbf I=\mathbf j_p+\mathbf j_n,\qquad c\equiv\cos\theta=\frac{I^2-j_p^2-j_n^2}{2j_pj_n}.$$

磁矩为 $\boldsymbol\mu=g_p\mathbf j_p+g_n\mathbf j_n$。横向磁矩的**模**满足

$$|\mu_\perp|=|g_p-g_n|\frac{j_pj_n\sin\theta}{I},\qquad B_{\rm cl}(M1)=\frac{3}{8\pi}(g_p-g_n)^2\frac{j_p^2j_n^2}{I^2}\sin^2\theta.$$

不能写向量 $\boldsymbol\mu_\perp=(g_p-g_n)(\mathbf j_p\times\mathbf j_n)/I$：叉积垂直叶片平面，真实磁矩在平面内；只有模相等。固定I、jn改变jp，

$$\left.\frac{\partial c}{\partial j_p}\right|_{I,j_n}=-\frac{I^2+j_p^2-j_n^2}{2j_p^2j_n}.$$

在分子为正且新旧三角形均允许的区域，增加jp会令θ增大。这是“重新张开”的一种允许几何，不能脱离芯角动量、配置和g因子确定性地推出B(M1)反弹。

定义 $R=B(M1)/B(E2)$，在单一光滑支上

$$\frac{d\ln R}{dI}=\frac{d\ln B(M1)}{dI}-\frac{d\ln B(E2)}{dI}.$$

R上升只要求分子相对分母下降更慢或上升更快；分子本身仍可下降。跨配置时叶片长度、有效g、四极核与混合均改变，不能把R反弹自动等同于M1强度重增。没有一般MR定理要求E2在3qp/5qp交叉处为零；E2是幅度矩阵元，可能有干涉，但没有原件或对称性支持普适零点。

同母态纯E2 crossover与混合M1+E2 dipole的效率校正光子强度可给条件比值

$$R\simeq0.697\,\frac{E_{\gamma,E2}^{5}}{E_{\gamma,M1}^{3}}\frac{I_{\gamma,\mathrm{dip}}}{I_{\gamma,\mathrm{cross}}(1+\delta^2)},$$

能量MeV，R单位μN²/(e²b²)，δ按E2/M1辐射幅度定义。若输入为含内转换的总跃迁强度，需要先回到光子分支或一致加入转换系数。缺失crossover时不能从“未见”任意填一个强度；可建立上限须有实际灵敏度、背景和效率，不等同于精确B(E2)=0。

两同壳h11/2中子空穴反对称化后Jn最大10，两个g7/2质子Jpair最大6。因此“最大耦合”的无芯算例有3qp Imax=11/2+10=31/2，5qp Imax=11/2+6+10=43/2。真实TAC不是固定good-j两叶片模型，观测交叉≈33/2已超出这个3qp刚性算例的端点；这说明直接把实际自旋代入无芯闭式并声称重现交叉是越界，不否定带芯与准粒子平均场的TAC解释。11.5只是最大质子合成角动量，不是该核实测叶片长度。

### 2. 有限j：精确Racah式与能量声明的区别

对两个可区分固定角动量j1,j2，$\mathbf I=\mathbf j_1+\mathbf j_2$，且磁矩只含 $g_1\mathbf j_1+g_2\mathbf j_2$。因总I生成元不连接不同I，跨I的M1只含Δg=g1−g2。Wigner–Eckart重耦合给

$$|\langle I-1\Vert j_1\Vert I\rangle|^2=(2I-1)(2I+1)j_1(j_1+1)(2j_1+1)\left\{\begin{matrix}j_1&I-1&j_2\\I&j_1&1\end{matrix}\right\}^2.$$

采用 $T(M1)=\sqrt{3/(4\pi)}\boldsymbol\mu$ 并除初态简并2I+1，得

$$B(M1;I\to I-1)=\frac{3}{4\pi}(\Delta g)^2\frac{[(j_1+j_2+1)^2-I^2][I^2-(j_1-j_2)^2]}{4I(2I+1)}\,\mu_N^2.$$

在允许下级存在时，端点Imax=j1+j2有

$$B(M1;I_{\max}\to I_{\max}-1)=\frac{3}{4\pi}(\Delta g)^2\frac{j_1j_2}{j_1+j_2}\,\mu_N^2.$$

有限j端点不必为零；Δg=0时整条跨I M1严格为零。经典端点零值不能当普适量子选择定则。精确公式的既有独立矩阵验证见 [[fixed-j-quantum-shears-m1-boundary]]；本轮不再次把示例jp=11/2、jn=10、Δg=1.42称为135Pr的实验参数，也不把计算强度当实测。

这说明有限角动量横向分量与量子重耦合的重要性，**不产生一个已确定的零点能量**。当前模型没有能量哈密顿量。更强的反例：若选旋转标量 $H=f(I^2)$，每个good-I态都是精确能量本征态、Var(H)=0，而上述端点M1仍可非零。因此“端点M1残留=能量零点涨落”不成立。若构造真正集体角坐标哈密顿量 $H=p_\theta^2/(2\mathcal M_\theta)+V(\theta)$，在稳定极小值谐近似才有 $E_{zp}=\hbar\sqrt{V''/\mathcal M_\theta}/2$；其曲率、惯量及边界均需来源或独立计算。

组态交叉须扩展到至少两配置空间。若 $|I,\alpha\rangle=\sum_a C_a^{(I,\alpha)}|I,a\rangle$，则

$$\langle I_f,\beta\Vert T_\lambda\Vert I_i,\alpha\rangle=\sum_{ab} C_a^{(I_f,\beta)*}C_b^{(I_i,\alpha)}\langle I_f,a\Vert T_\lambda\Vert I_i,b\rangle.$$

未知混合系数和跨配置电磁核时，单一6j公式不足以预测交叉后的B或其比值；不存在一个只乘有限j因子就完成的真实核“严格反弹推导”。

### 3. 偏振、多极混合与TW/MR的对象边界

勘误定义中的几何校准a与偏振灵敏度Q是不同量：

$$\Delta=\frac{aN_\perp-N_\parallel}{aN_\perp+N_\parallel},\qquad P=\Delta/Q.$$

2019 TableI给的是Δ。a(Eγ)=1.01229+1.17083×10⁻⁶Eγ（keV），来自三只90°clover，不能替代Q。即使已知Q，P(δ)仍依赖初末自旋、取向/退取向张量、观察角和探测器积分；与DCO的角相关响应有共同参数及多支解。仅Δ=0.04(3)不能推出δ∈[0.10,0.19]，更不能推出M1纯度≥96.5%。δ约定下辐射分数为fE2=δ²/(1+δ²)，这个换算式成立，δ数值仍须测量或联合响应反演。

| 问题 | 所需证据 | 本两篇原件能否完成 |
|---|---|---|
| 高自旋Band3是否候选MR | 带内ΔI=1磁性、配置与TAC、能谱、寿命强度 | 前三项有支持；绝对寿命缺，作者保留possible |
| 低自旋Band4→Band1的E2辐射分量多大 | 定标角相关+偏振，δ分支，必要的绝对/相对E2 | 勘误保留M1+E2，没有给δ数值 |
| 候选带是否TW | 对同一物理带系核验跨带E2、配置与惯量、摆动能量及竞争解释 | 不能用Band3的M1/E2替代Band4问题 |
| wobbling能量上升能否自动排除TW | 明确的带伙伴身份及适用哈密顿量稳定区 | 不成立为普适硬门；交叉混合也改变谱差 |

$E_{wob}(I)=E_1(I)-[E_0(I-1)+E_0(I+1)]/2$ 只有两列确实对应同一配置下的相关带时才是模式诊断。任取Band3与yrast相减可产生数字，却不构成已确认wobbling声子能。2015原文将Band3与Band4分开；2019是Garg自身实验校准更正，不能写成它修改了Matta实验数据。完整当前TW争论需逐篇核对各实验的实际响应与带身份，本轮不作排他判决。

## Assumptions

经典式假设固定叶片无芯；量子闭式假设两个可区分good-j直积、单一M1算符、允许末态。真实准粒子组态、Pauli反对称、配对、芯转动和混合另行处理。光子强度公式假定正确母态配对与多极分解。

## Competing Explanations

R上升可能来自E2减小、M1增大、混合/形状变化或分支检测偏差；本原件不足以唯一分解。有限j修正影响量子强度而不决定能谱。低自旋TW与高自旋MR可涉及不同配置，彼此不是自动排斥的全核标签。

## Transfer Conditions

把本推导用于具体核前，须给出相同带系的身份、配置、有效算符、实际响应、强度/寿命及误差；跨配置必须提供混合核。不能从谱学交叉的位置单独标定几何剪刀角。

## Failure Conditions

未知芯角动量、good-j空间不成立、跨配置电磁核缺失、crossover未见无检测上限、δ反演缺响应，都会阻止数值归因。不得用任意Q、惯量、形变或叶片长度填补为“定量重现”。

## Falsification or Reverse Tests

最直接的新证据是同带交叉前后的寿命与分支测量：同时重建绝对B(M1)、B(E2)及其相关误差，才能检查重新张开模型。若几何模型预测M1增而实测只是E2降，该模型的因果解释应撤回。偏振问题需公布足以重建多支δ似然的响应信息。

## Open Questions

真实TAC的质子g7/2对齐中，有多少角动量由芯承担？形状与配对的改变分别贡献多少M1和E2？如何在不误认带身份的前提下连接低自旋摆动与高自旋准粒子重排？当前两份原件不足以回答。

## Human Review

Codex原件定向self-audit和显式假设推导，保留 `review_status: unreviewed`，不代表用户审核。

## Promotion or Rejection History

2026-10-29：建立原件边界，`revises` [[pr135-shears-dynamics-bandcrossing-rebound]] 中交叉后实测反弹与固定叶片拟合的过强措辞，`revises` [[pr135-wobbling-vs-shears-discrimination]] 中同带二选一、δ纯度及排他结论。只以本页核验范围为准；不提升其它页状态，不删除历史证据。
