---
type: concept
title: "重离子熔合蒸发与反应道规划：势垒、质量约束、竞争退激及探测响应"
aliases: [heavy-ion-fusion-evaporation-and-reaction-channel-design, 熔合蒸发反应道设计]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [fusion-evaporation, reaction-planning, evidence-boundary, doppler-response]
needs_review: true
sources: [book-lin-heavy-ion-reactions, book-bertulani-nuclear-reactions]
---

# 重离子熔合蒸发与反应道规划

## Definition

熔合蒸发（fusion-evaporation）先涉及入射体系的俘获与复合核形成，再涉及复合核在粒子、光子与裂变等通道间的竞争退激。规划在束高自旋谱学实验，需要将**目标余核的产生、目标能带的布居、可记录的符合事例**分别建模。一个势垒穿透面积不能独自给出这三个量。林书印刷 pp.134–138、177–179 分别讨论一维俘获近似及复合核形成/裂变途径；Bertulani 印刷 p.179 式 (5.88) 将穿透与进一步熔合概率分开，pp.150–151 式 (4.180)–(4.189) 给出固定自旋宇称的统计衰变框架。精确原件位置见 Sources。

本页区分四层：教材直接支持的理论框架；给定输入后的运动学推导；需要数据约束的现象学模型；未实现的实验响应与规划输入。本页未提供新的实验截面、最佳束能、靶厚或机时建议，教材也不构成某个具体反应计算结果的实验验证。

对弹靶体系，完全熔合时

$$A_{\rm CN}=A_p+A_t,\qquad Z_{\rm CN}=Z_p+Z_t.$$

若只发射 $x$ 个中子，则 $A_r=A_{\rm CN}-x$、$Z_r=Z_{\rm CN}$。更一般地，发射 $n,p,\alpha$ 的数目分别为 $x,y,z$ 时，$A_r=A_{\rm CN}-x-y-4z$、$Z_r=Z_{\rm CN}-y-2z$。这些是守恒关系，不能建立核素存在性、通道开放性或布居强度。比如 $^{36}$S+$^{100}$Mo 对应 $Z_{\rm CN}=58,A_{\rm CN}=136$；5n/6n 的质量电荷账分别对应 $^{131}$Ce/$^{130}$Ce，不表示这里已知其产生截面。

## Necessary Assumptions

### 质量、反应能与分离能须使用一致的输入

静止靶、非相对论两体入射的运动学给出

$$E_{\rm cm}=E_{\rm lab}\frac{m_t}{m_p+m_t},\qquad
\mu=\frac{m_pm_t}{m_p+m_t},\qquad
E^*=E_{\rm cm}+Q_{\rm fus},$$

$$Q_{\rm fus}=(m_p+m_t-m_{\rm CN})c^2.$$

此处小写 $m$ 是质量。脚本使用 $m_i\simeq A_i m_u$ 计算质心能量、约化质量与初始反冲，使用半经验质量公式（semi-empirical mass formula, SEMF）的核静能差估计 Q。这两种近似必须明确，不能将其输出称为评价质量或精确激发能。SEMF 的一般结构可回链 Bertulani pp.164–166 式 (5.10)–(5.12)，但脚本保留的系数并非该书式 (5.12) 的系数集；本轮没有为它建立拟合来源或误差。

真正的阈值计算需给出质量表版本、评价/外推身份、质量单位与协方差；缺测质量使用哪一套模型也必须记录。核质量与原子质量不可混用。总电荷守恒时，采用一致原子质量定义可消去电子静质量项；需要的电子束缚能修正仍应与精度要求一致。逐级中子分离能为

$$S_n(Z,A)=[m(Z,A-1)+m_n-m(Z,A)]c^2.$$

每一步会换核素，不能把固定的 8 MeV 当作整条链的已知 $S_n$。Bertulani p.168、图 5.9 显示液滴估计与分离能的壳效应偏离，支持此处保留质量模型边界。评价质量表、目标核及各蒸发子核的逐项质量 locator **本轮缺失**，故不提供物理阈值表。

### Wong 面积是有条件的单势垒结果

有效径向势写为

$$V_\ell(r)=V_N(r)+V_C(r)+\frac{\hbar^2\ell(\ell+1)}{2\mu r^2}.$$

在单个倒抛物线势垒、适当的强吸收边界和分波积分近似下，

$$\sigma_W(E)=\frac{\hbar\omega R_B^2}{2E}
\ln\!\left[1+\exp\!\left(\frac{2\pi(E-V_B)}{\hbar\omega}\right)\right].$$

$E,V_B,\hbar\omega$ 使用 MeV，$R_B$ 使用 fm，结果为 fm$^2$；$1$ fm$^2=10$ mb。形式与适用条件由林 p.137 式 (6.9)–(6.15)、p.138 的抛物线近似限制及 Bertulani p.179 式 (5.86) 支持。高于势垒的数学渐近式是 $\pi R_B^2(1-V_B/E)$；真实截面是否仍服从它，要另查复合核形成竞争与能量范围。

脚本保留的半径/势垒高度经验配方只是**未经约束的旧示例参数**。本轮未核实它们可归属于 Bass 或 Christensen–Winther，故撤销该归属；默认 $\hbar\omega=4$ MeV 也不是所有体系共有的已知量。接口允许显式输入 $R_B,V_B,\hbar\omega$，但输入参数本身不能将示例升级为实验预测。形变、转移与非弹耦合可改变近垒结果与自旋分布：林 pp.138–143、Bertulani pp.181–182 给出框架依据。

由离心势得到的经典尺度满足

$$\ell_c(\ell_c+1)=\frac{2\mu R_B^2\max(0,E-V_B)}{\hbar^2}.$$

脚本求解这一二次关系；它不是总自旋 $J$ 的分布，更不是裂变截断。在垒下返回经典尺度零时，Wong 穿透面积仍可非零。若入射核有自旋，需耦合通道自旋与轨道角动量；若要规划高自旋能带，还需复合核至余核的角动量输运，不能直接令 $J_{\rm entry}=\ell_c$。

### 余核产生需要自旋宇称及竞争宽度

对零自旋入射核，一种用于组织物理输入的分解是

$$\sigma_r(E)=\frac{\pi}{k^2}\sum_\ell(2\ell+1)
T_\ell(E)P_{\rm CN}(E,\ell)W_r(E^*,J=\ell).$$

$T_\ell$、$P_{\rm CN}$ 与 $W_r$ 分别描述入射穿透、复合核形成，以及最终进入指定余核的概率。非零入射自旋须使用适当的自旋耦合权重。此式是本页将入射与衰变框架连接的组织方式，不是脚本已实现的计算。固定 $J^\pi$ 时通道宽度归一化的依据见 Bertulani p.150 式 (4.181)、(4.188)–(4.189)，该书 p.151 明确其为能量平均的角积分统计截面，不能误称为一般微分截面。

$W_r$ 应对不同蒸发历史求和，并对每步发射粒子能量、角动量及余核状态积分。它至少依赖各步质量与分离能、光学模型透射系数、能级密度及其自旋宇称分布、离散能级、光子强度，以及裂变通道。归一化分母须含所有纳入的开放退激通道；$xn$、$pxn$、$\alpha xn$、光子竞争及必要时的非平衡过程不可被四个 $xn$ 权重代替。中子没有库仑势垒也不足以推出任意体系都由中子道主导。

裂变势垒、热能、自旋、形变及耗散可共同影响竞争。即使在固定基态/鞍点转动惯量的简单模型中，旋转修正也为

$$B_f(J)\simeq B_f(0)+\frac{\hbar^2J(J+1)}{2}
\left(\frac{1}{\mathcal I_{\rm saddle}}-\frac{1}{\mathcal I_{\rm ground}}\right),$$

这是对两种形状转动能差的条件推导，不是已拟合的 RLDM 势垒或动态裂变率。书中对自旋依赖及不同裂变途径的讨论不支持脚本旧版通用的 $52\hbar$ 截断、5% 存活下限或由 $\ell_c$ 单独确定的存活函数；这些数值处方已撤销。没有输入竞争宽度时存活率是未知，不能默认为 0、1 或某个保底概率。

## Discriminating Observables

反应规划应在下列数据与模型层间建立可检验联系，而非只比较一个总面积。

| 需要判断的问题 | 有区分力的测量/输入 | 仍需控制的混淆因素 |
| --- | --- | --- |
| 穿透与复合核形成是否相同 | 跨能量的俘获、裂变及蒸发余核激发函数；合适时的碎片质量与角关联 | 不同实验的接受度、截面定义，准裂变与熔合裂变分离 |
| 目标余核与邻核如何竞争 | 逐核素残核标记、粒子标记、校准过的特征 gamma 产额 | 未见分支、同量异位素污染、衰变馈入和探测效率 |
| 产生余核是否布居目标带 | 指定带的相对/绝对强度、符合级联、spin/parity 证据 | feeding、同核异能态及选择门造成的偏置 |
| 束能/靶厚是否合适 | 束能标定、靶成分与面密度分布、透射/能损或相应 stopping 数据 | 靶退化、束斑、同位素丰度、靶倾角与衬底 |
| Doppler 校正后的线宽来自何处 | 分角度/分位置的峰位与线形、反冲速度约束、效率/位置响应标定 | 寿命、feeding、阻止本领、粒子反冲、散射和本征响应 |

本表为任务提出的验证设计，不代表这些数据已获取。没有物理截面、目标带布居与真实响应时，计算器不能决定哪组束能、靶厚或机时更优。

### 靶内输运与可记录计数的闭环

以沿束路的面密度 $\eta$（g/cm$^2$）为坐标，束能应由

$$\frac{dE}{d\eta}=-S(E;\text{beam, material}),\qquad E(0)=E_{\rm in}$$

求得，并与能量歧离（straggling）、束能分布、反应深度和靶材非均匀性联合传播。阻止本领表必须对应实际离子、材料、能区、单位和版本，电子/核阻止成分也要明确；本轮未核验相应表，脚本没有实现这一步。增加输入面密度而不改变结果，是明确的未建模状态，不是厚度没有物理影响。

若 $\Phi_p(t)$ 是每秒入射离子数，$f$ 是目标同位素的原子数丰度，$M$ 是相应均匀元素靶的摩尔质量，薄于强束流衰减尺度时可用如下计数组织式：

$$\lambda_s=\int dt\,\Phi_p(t)\int_0^{\eta_{\rm max}}
\frac{fN_A}{M}\,d\eta\;
\sigma_r[E(\eta,t)]\,P_{\rm band}[E(\eta,t)]\,
B_{\rm cascade}\,\epsilon_{\rm gate}(\eta,t)\,L(t).$$

这里 $P_{\rm band}$ 为条件布居概率，$B_{\rm cascade}$ 为指定衰变路径分支，$\epsilon_{\rm gate}$ 含真实符合/位置/几何效率，$L$ 为记录接受比例。复合靶应换为正确的目标核数密度，不能把化合物面密度全部当作目标同位素。束流若以电流提供，应按离子电荷态转换为离子数率。此式是本页的维度明确的规划框架，不是源书给出的特定实验处方，也不是模块预测。

### 角响应与 Doppler 线形

完全动量转移、反应前静止靶、非相对论质量数近似下，初始复合核反冲满足

$$\beta_{\rm CN}\simeq\sqrt{\frac{2E_{\rm lab}}{A_pm_uc^2}}\frac{A_p}{A_p+A_t}.$$

这是初始复合核速度，不是蒸发余核整个寿命期间的速度分布。给定发射时速度 $\beta$ 与光子在实验室相对该速度方向的夹角 $\theta$，洛伦兹变换给出

$$E_\gamma(\theta)=\frac{E_{\gamma0}\sqrt{1-\beta^2}}{1-\beta\cos\theta}.$$

这里的运动学关系和下述传播是本页条件推导；本轮没有为实际阵列、寿命或 stopping 取得专门原文 locator。使用精确光子变换并不消除输入反冲速度的近似。$90^\circ$ 中心角处一阶频移为零，但二阶横向项不为零。

接口将 $\Delta\theta$ 定义为**完整极角区间宽度**，以中心角为中心并裁至 $[0,180^\circ]$。给定恒定 $\beta$ 时，两个端点的能量差定义的是角覆盖的 full span。小 $\beta$、小开口时它近似为 $E_{\gamma0}\beta|\sin\theta|\Delta\theta$，不是 FWHM；它在前/后向零导数附近也不能代替端点计算。

如果角误差本身是小的高斯分布且标准差已知，才可线性传播 $\sigma_E\simeq|\partial E/\partial\theta|\sigma_\theta$，并在该高斯近似成立时用 $\mathrm{FWHM}=2\sqrt{2\ln2}\,\sigma_E$。实际线形要将反应深度、粒子反冲、衰变时间、减速轨迹与方向分布同探测器位置/能量响应卷积。事件级 Doppler 校正的残余不确定度还受速度、方向与重建误差限制；没有“薄靶即可完全恢复某个固定分辨率”的保证。

## Supporting Evidence

下表只列本轮回读原件后支持的框架，不把来源页旧有概述当成已核验事实。两书是理论教材背景，不能作为同一示例反应的两份独立实验数据。

| 来源与精确 locator | 可支持的内容 | 不能据此声称的内容 |
| --- | --- | --- |
| [[book-lin-heavy-ion-reactions]]，印刷 pp.134–136 / PDF pp.144–146，式 (6.1)–(6.8) | 分波、经典锐截止及其近垒限制 | 任意能量下的物理熔合/余核截面 |
| 同书印刷 p.137 / PDF p.147，式 (6.9)–(6.15)；p.138 / PDF p.148 | 有效势、Hill–Wheeler/Wong 与抛物线近似限制 | 某个默认半径配方的已验证 Bass/CW 身份 |
| 同书印刷 pp.138–143 / PDF pp.148–153，图 6.7–6.13、式 (6.17)–(6.20) | 近垒增强、自旋分布与形变耦合 | 四个高斯即为 Hauser–Feshbach 或 PACE |
| 同书印刷 pp.177–179 / PDF pp.187–189，图 7.1–7.2 | 复合核形成、快裂变、准裂变及条件依赖 | 所有 $A\sim130$ 核共享一个裂变截止自旋 |
| [[book-bertulani-nuclear-reactions]]，2021 第二版，印刷 pp.150–151 / PDF pp.161–162，式 (4.180)–(4.189) | 自旋宇称分辨的平均统计反应与通道竞争 | 未输入宽度也能给出绝对产额 |
| 同书印刷 pp.164–166 / PDF pp.175–177，式 (5.10)–(5.12)；p.168 / PDF p.179，图 5.9 | SEMF 的平均性质、参数与壳效应缺失 | 液滴质量就是评价质量，或本脚本系数已被书中验证 |
| 同书印刷 p.179 / PDF p.190，式 (5.86)–(5.88)；pp.181–182 / PDF pp.192–193，式 (5.96)–(5.103) | Wong、额外熔合概率及耦合道/势垒分布框架 | 单势垒曲线已包含光学势拟合与实验势垒分布 |

林书扫描页使用 PyMuPDF 渲染后以 Tesseract `chi_sim+eng` OCR，式 (6.15) 所在 PDF p.147 另做图像核对；OCR 的核素上标与公式字符不能直接作为精确数值录入。Bertulani 为文本提取。临时文件位于 `tmp/reaction-design-audit/`，长期回链依靠原始 PDF 与以上页码，不能依靠临时 OCR 文件。

## Counter-evidence and Competing Interpretations

旧版页面将示例公式输出称作“实测输出”，把任意的存活下限与高斯归一化转换为 mb，再据此建议具体靶厚。这一整条推理撤回：数值来自代码，并无对应实验原件、评价质量或校准过的统计反应模型。旧版引用的 Bertulani “第 11 章”不适用于本地第二版；本轮核实相关内容在第 4、5 章。林书熔合章实际从印刷 p.134（PDF p.144）开始。共享来源页旧概述仍可能含错章、错页或未核验结论，本轮没有修改共享来源，使用时应以本页列出的实际 locator 为限。

竞争解释应按观测层次保留：余核产额下降可能来自不同入射竞争、裂变、带电粒子通道或实验接受度；目标带变弱还可能来自布居、feeding、寿命或门选择。谱线展宽可能由角响应、反冲分散、靶内减速、本征能量响应与峰混叠共同贡献。单独增大 $E^*$ 或减小厚度不能排除这些机制。

### 统计与系统不确定度

- **计数统计**：在独立计数模型适用时，信号区和控制背景区建立泊松似然；低计数/零计数应保留上限与非对称区间。零计数不等于物理截面为零，背景扣除后的数也不能自动作为泊松观测。
- **相关标度**：束流积分、靶核数、效率及分支可跨束能点共用。对 $Q=c^2\boldsymbol v^T\boldsymbol m$，质量协方差给出 $\mathrm{Var}(Q)=c^4\boldsymbol v^T C_m\boldsymbol v$；把质量差的各项一律视为独立可能错误地放大或压低不确定度。
- **响应传播**：让质量/束能、靶厚/阻止本领、反冲与角响应通过同一前向模型联合传播；共享 nuisance 参数保留相关性。对非线性阈值、单侧限制或多峰结果，报告分布/区间与条件，不只报一个均值加误差。
- **模型差异**：光学势、耦合通道、能级密度、裂变势垒、离散能级及未纳入通道产生的变化属于模型不确定度。参数扫描本身不是有覆盖率保证的置信区间；须说明先验/校准数据、验证范围和外推失败条件。

这是本页提出的统计分析设计，尚未对实际反应数据执行。必须分开 Monte Carlo 有限抽样误差、实验统计/系统误差与模型误差，不能用输出的小数位数代替任何一项。

## Our Current Position

本模块目前是**带明确边界的运动学与单势垒示例**。其 Q 是 SEMF 估计，Wong 数值是给定参数后的条件面积，角能量区间是恒速条件下的几何 span；这些量均不建立实际产额、存活率或可记录计数。

| API 字段/行为 | 本轮契约 |
| --- | --- |
| 原九个位置参数、四个主要结果分组 | 保留；新增 `scientific_boundary` |
| `Q_fusion_MeV`、`E_excitation_MeV` | 保留数值，邻接状态字段标明 SEMF/条件性；另给 `Q_fusion_SEMF_MeV` |
| `R_barrier_fm`、`V_barrier_MeV`、`hbar_omega_MeV` | 记录实际使用值与来源状态，可用 keyword 参数覆盖 |
| `schematic_wong_cross_section_mb` | 唯一数值 Wong 面积字段；不作为物理融合/余核截面 |
| `sigma_fusion_mb`、`sigma_evaporation_total_mb`、`L_fission_limit_hbar`、`fission_survival_fraction` | `None`（JSON `null`），不再虚构物理输出 |
| 各通道 `cross_section_mb`、`branching_ratio_pct`、`E_opt_MeV`、`relative_weight` | `None`；默认仅列 A/Z 守恒允许的 3n–6n 候选账目 |
| `illustrative_xn=True` | 仅新增各通道的 `illustrative` 子对象；归一化权重只对显示子集定义，不检查真实阈值、不给 mb、不命名为物理分支 |
| `L_max_hbar` | 求解 $\ell(\ell+1)$ 的经典尺度，语义比旧 $\sqrt{\ell(\ell+1)}$ 近似更明确；不是自旋布居 |
| `doppler_shift_keV` | 用同一近似初始 $\beta$ 的完整光子变换；旧一阶值另放 `doppler_shift_first_order_keV` |
| `doppler_broadening_fwhm_keV` | `None`；新增端点能量区间、full span 与小开口近似字段 |
| 靶厚度参数 | 只记录元数据，`target_transport_modeled=False`、能损未知；零厚度允许作为无输运对照 |

可选高斯仅为演示归一化的任意函数：$T_{\rm demo}=\sqrt{E^*/(A_{\rm CN}/8.5)}$、$C_x=x(8+2T_{\rm demo})+5$ MeV、$w_x\propto\exp[-(E^*-C_x)^2/(2s^2)]$，默认 $s=6$ MeV。所有常数都没有本轮核验的来源或参数拟合；$C_x$ 不是最优束能或阈值。非正 SEMF 激发能或无守恒允许的候选道时不产生权重。脚本从不把权重乘以 Wong 面积。

独立演示入口（不是实验方案）：

```bash
python3 system/scripts/analysis/heavy_ion_fusion_evaporation_channel_calculator.py --json
python3 system/scripts/analysis/heavy_ion_fusion_evaporation_channel_calculator.py --barrier-radius 11 --barrier-height 82 --barrier-curvature 4 --illustrative-xn
python3 -m unittest discover -s system/tests -p test_fusion_design_boundary.py -v
```

输入检查包括整数核素与 $0<Z\leq A$ 的带电入射核、有限正束能/光子能/势垒参数、非负厚度与角宽及 $[0,180^\circ]$ 角域。零束能不通过人为分母下限计算截面。非相对论入射速度达到光速的输入被拒绝；动能/静能比超过 0.01 时附带近似复核提示，这个提示阈值是软件诊断选择，不是普适物理分界。

后续要形成可评估的实验设计，依次补齐：评价质量及逐子核阈值；有实验约束的入射与自旋宇称分布；包含竞争通道的版本固定统计模型及邻近激发函数验证；实际材料阻止/歧离与靶剖面；符合计数及角/速度响应；联合统计与系统误差。应逐项核验这些输入后才讨论可行性，不能将本页示例直接写入束流申请的产额或机时预算。

## Sources

- [[book-lin-heavy-ion-reactions]]：原件 `raw/books/重离子核反应 (林承键) (Z-Library).pdf`；SHA-256 `792bfe7f7807623b7e1439b32eddb7320ab3ec6bf6be7e3894b436c1c9f65b2e`。本轮选择性回读 PDF pp.144–153（印刷 pp.134–143）、pp.187–189（印刷 pp.177–179），另查 PDF pp.3、9–10 的书名/目录。核心公式 PDF p.147 已视觉核对。不是全书精读认证。
- [[book-bertulani-nuclear-reactions]]：原件 `raw/books/Introduction to Nuclear Reactions (C.A. Bertulani P. Danielewicz) (Z-Library).pdf`；SHA-256 `ad1391abd781e2277433283b6635679cfc45efc9d9d5472d4aabcd172509cb71`。PDF p.5 核对版权为 2021 第二版；本轮相关文本回读 PDF pp.159、161–162、173–179、190、192–193（对应印刷 pp.148、150–151、162–168、179、181–182）。只对 Supporting Evidence 表中命题提供上述 locator。

两份原件沿用已有 `raw_file`/哈希登记并只读核验，本轮不新增或修改共享 source。具体反应的评价质量、截面、实际统计程序输入/版本、停止本领与阵列响应 locator 尚缺，保持 `needs_review: true`。本页的守恒、误差传播和前向计数组织式属于标明假设的任务推导，未冒称为教材原文或实验结论。
