---
type: research-note
title: "反磁转动四叶片中质子-质子库仑排斥与剪刀闭合非对称性"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: ["AMR proton-blade Coulomb repulsion", "AMR shears closing asymmetry", "四叶片质子库仑排斥"]
tags: [antimagnetic-rotation, coulomb-repulsion, proton-blades, shears-asymmetry, cadmium110]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "Day26 doctoral research task: proton-proton Coulomb repulsion and non-axial AMR shears"
evidence_sources: [roy-2011-cd110-systematics-antimagnetic, rather-2014-104pd-antimagnetic-first-page, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]
promotion_target: amr-double-shears-core-coupling-and-b-e2-plateau
---

# 反磁转动四叶片中质子-质子库仑排斥与剪刀闭合非对称性

## Research Trigger

本任务要求检验一个具体假设：在 $^{110}$Cd 和 $^{104}$Pd 的四叶片反磁转动（antimagnetic rotation, AMR）图像中，两个 $\pi g_{9/2}^{-1}$ 质子空穴叶片的直接库仑排斥会不会在带终止附近阻止质子剪刀完全闭合，从而产生 $\theta_p-\theta_n\neq0$ 及 $B(E2)$ 残余平台。已有实验/唯象基线把 $^{110}$Cd 的组态写成两个质子空穴与两个高-$j$ 中子粒子，并以粒子—空穴四极相互作用、剪刀闭合和核芯转动解释寿命与 $B(E2)$ 演化；但这些来源没有给出质子—质子库仑项的微观矩阵元，也没有测得独立的质子和中子叶片角。

因此本笔记把问题分成三层：来源直接报告的实验和模型输入；可从有限密度两体矩阵元推出的物理边界；以及一个可复现、参数透明的两角 Routhian 诊断模型。模型只用于检验机制敏感性，不能冒充自洽 HFB、PNC-CSM 或第一性原理计算。

## Grounded Evidence

| 证据 | 直接内容 | 定位与边界 |
|---|---|---|
| Roy et al. 2011 | $^{110}$Cd 的 $16^+$ 至 $24^+$ 带内寿命对应 $B(E2)=0.14(1),0.12(2),0.11(2),0.09(3),0.06(2)\ e^2\mathrm b^2$；作者用双剪刀与核芯转动解释平缓下降。 | [[roy-2011-cd110-systematics-antimagnetic]]，p.324 Table 1；原页标记 `RO11-1/2/3`，寿命含 stopping-power 系统边界。 |
| Roy 模型参数 | 两个 $g_{9/2}$ 质子空穴与两个 $h_{11/2}$ 中子粒子构成有效双剪刀；$V_{\pi\nu}=1.2$ MeV，$^{110}$Cd 的核芯惯量取 $\Im_m=19.5\ \hbar^2$/MeV。 | [[roy-2011-cd110-systematics-antimagnetic]]，pp.325–326，Eqs. 3–6；原模型是经典粒子加转子。 |
| Rather et al. 2014 | $^{104}$Pd 的有效构型为 $\pi g_{9/2}^{-2}\otimes\nu[h_{11/2}^2,(g_{7/2}/d_{5/2})^2]$；模型使用 $V_{\pi\nu}=1.2$ MeV、$V_{\pi\pi}=0.2$ MeV、$\Im=5\ \hbar^2$/MeV，并给出 $B(E2)$ 从 0.26(2) 降到 0.02(1)\ e^2\mathrm b^2$。 | [[rather-2014-104pd-antimagnetic-arxiv-full]]，pp.4–5、p.10 Table 1；不是四个显式空穴的同一 PNC 波函数。 |
| AMR 几何 | 对称双剪刀的两叶横向磁矩相消；理想几何中的 $B(E2)$ 具有 $\sin^4\theta$ 依赖，反映非轴向四极张量分量。 | [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]，PDF pp.487–490，F01-10/F01-11 与 F01-D26-004；综述明确这是条件模型。 |

实验上可以支持“带端仍有有限 $B(E2)$”这一事实，但上述来源没有把它归因于质子—质子库仑排斥。该归因在本页只能作为可检验的 provisional reasoning。

## Provisional Reasoning

### 1. 有限密度库仑项，而不是字面点粒子发散

若把两质子空穴错误地当作两个点电荷，几何距离为

$$d_p(\theta_p)=2r_p\sin\theta_p,$$

则

$$V_C^{\rm point}(\theta_p)=\frac{e^2}{d_p(\theta_p)}\xrightarrow[\theta_p\to0]{}+\infty.$$

这只能说明点粒子模型在闭合端点是奇异的。量子核结构中的准粒子是有限空间波包；直接矩阵元应写成

$$V_C^{\rm dir}=e^2\!\int d^3r_1d^3r_2\,
 \frac{\rho_{p1}(\mathbf r_1)\rho_{p2}(\mathbf r_2)}{|\mathbf r_1-\mathbf r_2|},$$

并含交换、反对称化、轨道占据与核芯屏蔽。对于两个宽度为 $a$ 的平滑密度，本页用

$$V_C^{\rm reg}(\theta_p)=\kappa\frac{e^2}{\sqrt{a^2+[2r_p\sin\theta_p]^2}}.$$

当 $a\to0$ 时恢复点粒子极限；只要 $a>0$，$V_C^{\rm reg}(0)=\kappa e^2/a$ 有限。因此，“波函数重叠使库仑排斥发散”不能作为微观事实写入结论；可保留的表述是：闭合使直接矩阵元快速增大，且其大小由径向密度、交换和有效屏蔽决定。

### 2. 两角 Routhian 与非对称闭合

把质子和中子叶片分别放在 $\pm\theta_p$、$\pm\theta_n$，采用与来源几何一致的镜像约束。可复现诊断的 Routhian 为

$$\begin{aligned}
 \mathcal R(\theta_p,\theta_n;\omega)=&V_{\pi\nu}
 [P_2(\cos(\theta_p-\theta_n))+P_2(\cos(\theta_p+\theta_n))]\\
 &+V_{\nu\nu}P_2(\cos2\theta_n)+V_C^{\rm reg}(\theta_p)
 -\omega[2j_p\cos\theta_p+2j_n\cos\theta_n+\Im_c\omega].
\end{aligned}$$

其中 $j_p=9/2$、$j_n=11/2$，$P_2(x)=(3x^2-1)/2$。第一项让低频构型保留剪刀张角，Routhian 的 $-\omega I$ 项推动闭合；库仑项只作用于质子叶片。参数 $V_{\pi\nu}=0.55$ MeV、$V_{\nu\nu}=0.50$ MeV、$\Im_c=19.5\ \mathrm{MeV}^{-1}$、$r_p=4.6$ fm、$a=2.0$ fm 是模型演示输入，不能当作 Roy 或 Rather 的拟合参数。

在 $\hbar\omega=0.20$–$1.00$ MeV 的示例扫描中，加入有限密度库仑项后，模型端点为 $\theta_p=11.75^\circ$、$\theta_n=0^\circ$；去掉库仑项则两角均为 $0^\circ$。在 $\omega=0.85$–$1.00$ MeV，质子角为 $14.0^\circ$–$11.75^\circ$，而中子角已经落到零。这个 10–15° 窗口是本组参数产生的模型输出，不是实验提取值，也不是普适定理。

### 3. $T_{22}$、$B(E2)$ 和角度差

为显示可观测量如何响应，定义一个含核芯代理项的示意四极振幅

$$T_{22}=T_{22}^{\rm core}+q_p\sin^2\theta_p+q_n\sin^2\theta_n,$$

并取 $B(E2)=|T_{22}|^2$。$T_{22}^{\rm core}=\sqrt{0.06}\ e\mathrm b$ 是与 Roy 带端量级相同的外加核芯项；$q_p=0.40\ e\mathrm b$、$q_n=0.10\ e\mathrm b$ 只用于敏感性展示。由此，含库仑模型的 $B(E2)$ 从 0.127 到 0.0684 $e^2\mathrm b^2$ 下降；无库仑端点是 0.060 $e^2\mathrm b^2$。这能重现“有限平台”的数量级，但不能证明平台由库仑项单独产生，因为 0.06 项被明确放进模型。

令 $\bar\theta=(\theta_p+\theta_n)/2$，定义角不对称相对于强制对称角的张量变化

$$\Delta T_{22}^{\rm asym}=T_{22}(\theta_p,\theta_n)-T_{22}(\bar\theta,\bar\theta),$$

$$\Delta B(E2)^{\rm asym}=|T_{22}(\theta_p,\theta_n)|^2-|T_{22}(\bar\theta,\bar\theta)|^2.$$

在 $\omega=0.80$ MeV，$\Delta\theta=\theta_p-\theta_n=11.0^\circ$，模型给出 $\Delta B(E2)^{\rm asym}=+0.00711\ e^2\mathrm b^2$；在端点 $\omega=1.0$ MeV，$\Delta\theta=11.75^\circ$，该量为 $+0.00581\ e^2\mathrm b^2$。这表明非对称闭合可对带端强度产生约 $10^{-2}\ e^2\mathrm b^2$ 的修正，但修正大小依赖 $q_p,q_n$、核芯项和轨道密度。

### 4. 量子费米子截断：为什么四叶片价核子上限是 $18\hbar$

经典矢量图把两个 $g_{9/2}$ 质子空穴和两个 $h_{11/2}$ 中子粒子完全同向排列时写成 $2j_p+2j_n=20\hbar$。这个数不是同一单-$j$ 壳层中四个同种费米子的允许上限。对两个相同 $j$ 粒子，交换算符作用在耦合态上为

$$P_{12}|(jj)JM\rangle=(-1)^{2j-J}|(jj)JM\rangle.$$

反对称化要求 $(-1)^{2j-J}=-1$。因此半整数 $j$ 时只保留偶数 $J$：

$$g_{9/2}^2:\quad J_p=0,2,4,6,8,\qquad J_{p,\max}=2j_p-1=8,$$

$$h_{11/2}^2:\quad J_n=0,2,4,6,8,10,\qquad J_{n,\max}=2j_n-1=10.$$

四叶片单-$j$ 截断的价核子角动量于是满足

$$J_{\rm val,max}=J_{p,\max}+J_{n,\max}=8+10=18\hbar.$$

这解释了 $18\hbar$ 的量子自旋饱和截断：$J_p=9$ 和 $J_n=11$ 的完全同向耦合分别是交换对称的禁态。它不是说实验能带必然在 $18\hbar$ 终止，因为核芯转动、跨壳层组态、配对破缺和有效多-$j$ 混合可以继续提供角动量；它说明了“仅由 $\pi g_{9/2}^{-2}\otimes\nu h_{11/2}^{2}$ 四个显式价核子承载全部自旋”的模型边界。相应的角动量加法中，$J_p=8$ 与 $J_n=10$ 可耦合出 $J_{\rm val}=18$，而其它允许的偶数对给出 $|J_p-J_n|\le J_{\rm val}\le J_p+J_n$。

### 5. 极端闭合处的库仑—短程竞争

有限密度直接库仑项在 $\theta_p\to0$ 时趋于有限的正值，而短程核力的等效局域项可写成

$$V_N(d)\simeq -V_0\exp[-d^2/(2s_N^2)],\qquad d=2r_p\sin\theta_p.$$

因此极端闭合不是“库仑无限大而其它项消失”：库仑、短程核力、交换和单-$j$ 反对称化共同重整化有效 $V_J$。在同一轨道中，严格的两体通道应由

$$V_J=\langle (jj)J|V_C+V_N| (jj)J\rangle_{\rm antisym}$$

定义；$J$ 为奇数的通道根本没有对应的反对称同种费米子态，不能以“强短程吸引”恢复。局域短程项可降低允许偶数 $J$ 通道的能量，但也会通过有限径向波函数、张量分量和配对重整化改变通道间相对排序。这里工件中的距离势仅是可追溯的数量级诊断，不是 $V_J$ 的第一性原理计算。

工件 `amr_fermion_pair_limits.py` 逐项输出允许的 $J_p,J_n$、$18\hbar$ 上限及 $\theta_p=0$ 到 $90^\circ$ 的有限库仑/短程示意势。其输出明确把经典 $20\hbar$ 与量子 $18\hbar$ 分开，并记录了 $a\to0$ 点极限的奇异性和有限宽度正则化。

## Assumptions

1. 两个质子空穴和两个中子粒子可由两个镜像角自由度描述；没有显式求解配对、阻塞、三轴形变和角动量投影。
2. 质子—质子项采用有限宽度正则化的直接项；交换、有限范围核力、电子屏蔽和自洽核芯极化未显式计算。
3. $\Im_c=19.5\ \mathrm{MeV}^{-1}$ 借用 Roy 对 $^{110}$Cd 的有效粒子加转子设置；不把它迁移为 $^{104}$Pd 参数。
4. $T_{22}^{\rm core}$ 是残余 $B(E2)$ 的代理参数，用来隔离角度效应；它不是从库仑相互作用推导的核芯响应。
5. 网格最小化使用 0.25° 步长；数值误差小于该网格分辨率，但模型误差远大于此数值误差。
6. $J_p=8$、$J_n=10$ 的选择规则只适用于各自单一半整数 $j$ 壳层的两个同种费米子；不能直接迁移到多-$j$、质子—中子等粒子或含显式核芯角动量的空间。

## Competing Explanations

- **核芯四极极化与集体转动**：Roy 已明确用 AMR 与核芯转动耦合解释 $^{110}$Cd 的平缓 $B(E2)$；它是当前来源支持最直接的解释。
- **有效质子—质子残余相互作用**：Rather 的半经典模型包含 $V_{\pi\pi}=0.2$ MeV，但没有把该参数分解成库仑与核力，也没有独立的质子角测量。
- **配对破缺、组态混合和 PNC 波函数**：高自旋端的占据重排可改变闭合轨迹，可能模拟本模型的残余角；有效两空穴模型不能代替显式四空穴计算。
- **feeding、stopping power 与分支选择**：Roy 的寿命和 $B(E2)$ 含实验系统边界，22+ 附近还存在评价分支与实验门控差异；强度平台不应直接反演为角度平台。

## Transfer Conditions

该诊断可以迁移到弱形变、偶偶、近似镜像四叶片候选，但必须重新确定 $j_p,j_n$、核芯惯量、径向密度和有效电荷。$^{104}$Pd 可作为几何比较对象；其完整来源给出不同的核芯惯量和更低端点 $B(E2)$，不能直接套用 $^{110}$Cd 参数。对于强形变转子、奇核单粒子阻塞、显著三轴手征构型或非共面剪刀，二维镜像模型失效。

## Failure Conditions

1. 以 $e^2/(2r\sin\theta_p)$ 的点粒子表达式直接声称真实核的能量发散。
2. 仅凭模型端点 10–15° 就宣称实验已经测得该角度，或把它写成所有 AMR 核的常数。
3. 把外加的 $B_{\rm core}=0.06\ e^2\mathrm b^2$ 当成库仑项的预测。
4. 把 Rather 的有效两空穴构型与 PNC 四空穴波函数混为同一微观状态。
5. 忽略交换、配对、组态混合和 DSAM 系统误差后，声称完成“第一性原理”反演。
6. 把 $J_{\rm val,max}=18\hbar$ 写成完整原子核的绝对自旋终止；该值只属于四价核子单-$j$ 截断，核芯和跨壳层自由度可延长能带。

## Falsification or Reverse Tests

- 用带阻塞的 PNC-CSM、TAC-RMF 或 GCM 直接计算 $\langle\alpha\beta|e^2/r_{12}|\alpha\beta\rangle$ 及交换项；若其角依赖远小于本诊断，库仑残余角机制被削弱。
- 对 $a$、$r_p$、$\kappa$ 做敏感性扫描。若只有不合理的宽度或增强因子才能得到 10–15°，则该数值窗口应被判定为参数调谐而非预测。
- 同时拟合多个 $B(E2)$、$J^{(2)}$、寿命和分支，并允许 $T_{22}^{\rm core}$ 自由变化；若不含库仑项的模型同样拟合，则 $B(E2)$ 平台不能辨识库仑机制。
- 搜索能带终止附近的四极矩、核共振荧光或电子散射约束；若能独立重建质子密度且显示闭合无残余角，模型假设被反驳。
- 比较 $^{106,108,110}$Cd 和 $^{104}$Pd。若残余角不随质子数、轨道半径和核芯极化按模型趋势变化，单一质子库仑解释不足。

## Open Questions

1. 在真实 $g_{9/2}$ 空穴波函数上，直接与交换库仑矩阵元的数量级、符号和 $K$ 分量是什么？
2. 质子—中子残余四极作用与库仑项是否会共同产生非轴向、非等角的自洽极小？
3. $^{110}$Cd 带端 $B(E2)=0.06(2)\ e^2\mathrm b^2$ 的核芯贡献能否由独立四极矩或 PNC 电四极算符算出，而不是作为拟合平台？
4. $\theta_p$ 与 $\theta_n$ 能否通过多极混合比、静态四极矩或偏振观测分别约束？目前来源只给总带内强度。
5. $^{104}$Pd 更小的核芯惯量与更低的 $B(E2)$ 是否会放大或抑制库仑导致的闭合非对称？
6. 在同一 Woods–Saxon 或 Nilsson 径向波函数上计算 $V_J$，能否确认高允许 $J$ 通道的短程重整化足以产生可观测的闭合延迟？
7. $18\hbar$ 量子价核子上限与 $^{110}$Cd 实验带端的核芯角动量增量如何在 PNC-CSM 或粒子—转子投影中连续匹配？

## Human Review

本页为 `status: ai-draft`、`review_status: unreviewed`、`reasoning_status: provisional`。Roy、Rather 和 Frauendorf 来源页已有各自的 review 边界；本页的正则化库仑模型、10–15°窗口和 $T_{22}$ 分解均需要核结构专家逐项审核，尚未升级为 `human-reviewed` 或论文级结论。

## Promotion or Rejection History

- 2026-10-29：创建研究笔记和可复现两角 Routhian 工件。保留“点极限发散、有限密度矩阵元有限”的边界；将“10–15°”降级为参数化模型输出。
- 2026-10-29：未将库仑项写成已证实的 $^{110}$Cd $B(E2)$ 平台根源；等待有限波函数直接矩阵元、参数敏感性和独立角度观测。
- 2026-10-29：新增费米交换选择规则推导；确认 $g_{9/2}^2$ 与 $h_{11/2}^2$ 的允许最大配对角动量分别为 8 与 10，单-$j$ 四价核子截断为 $18\hbar$，并将其与经典 $20\hbar$ 矢量上限区分。
