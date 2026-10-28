---
type: research-note
title: "Ba–Ra八极驱动轨道、E1相消与奇中子阻塞：算符及解耦拟合边界"
aliases: [ba-ra-blocking-cancellation-operator-boundary]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [bucher-2017-146ba-direct-octupole, bernard-2016-144ba-sccm-octupole, nomura-2018-odd-mass-ba-octupole, engel-2003-ra225-selfconsistent-schiff, dobaczewski-2005-ra225-schiff, nndc-2009-ra225-adopted-parity-doublet]
created_from: Day26 delegated doctoral mechanism investigation
promotion_target: octupole-correlation
tags: [octupole, E1, SCCM, blocking, parity-doublet, Ba, Ra, operator-boundary]
---

# Ba–Ra八极驱动轨道、E1相消与奇中子阻塞

## Research Trigger

追问144,146Ba的中子占据如何改变质心修正E1，以及这套解释能否定量外推至145Ba与225Ra。关键是分清八极驱动轨道对、真正的rank-1电偶极核、奇核自洽极化、宇称双重态运动学拟合这四层。以下推导不提供不存在的生产SCCM算符核，也不把谱拟合截距认作实测隧穿能。

## Grounded Evidence

| 来源与原件定位 | 本次确认的证据 | 分层与限制 |
| --- | --- | --- |
| [[bucher-2017-146ba-direct-octupole]] PDF3 Table I、PDF4 Fig5/末段、PDF5首段 | 146Ba的三条变形中子轨道具有h9/2、f7/2、i13/2球形parentage，对应3/2−、5/2−、1/2+标签，v²=0.40、0.27、0.20；作者将其占据与近抵消质子偶极贡献关联 | 模型解释；不是完整j壳占据，未给出本任务所需的逐项有符号Dz矩阵元 |
| 同上PDF3 Table I | 实验E1幅度0.000223^(+0.000010)_(-0.000008) e b^(1/2)，SCCM为0.00474；前者主要由既有寿命/分支约束 | 中心幅度比21.2556，平方比451.8008；定性趋势不能冒充绝对幅度已重现 |
| [[bernard-2016-144ba-sccm-octupole]] PDF2 Eqs3–5 | F=N^(1/2)f；可观测跃迁需要双坐标投影算符核 | F图与v²不能替代相干核求和 |
| [[nomura-2018-odd-mass-ba-octupole]] PDF8、Tables VI–VII | 145Ba最低负宇称带在该sdf-IBFM中主要含h9/2⊗sd；较高八极带有明显f玻色子成分并预报强E3 | 属DD-PC1映射的粒子–芯模型；没有等于D1S自洽阻塞计算，不能推出阻塞率 |
| [[engel-2003-ra225-selfconsistent-schiff]] PDF4–6、Fig3 | Ra计算的D0在N=134–138之间换号，N=136的近零实验提取值与此相容；作者强调转动态提取D0与基态内禀D0可能不同，奇核末粒子还会极化芯 | Skyrme模型与实验提取比较；不提供224Ra相消的质子/中子数值分项 |
| [[dobaczewski-2005-ra225-schiff]] PDF2 Eqs1–4、PDF3–4 | 225Ra的55-keV同自旋伙伴进入PT奇Schiff响应分母；算符具有额外r²权重，计算允许Kramers简并破缺与自旋极化 | 这是PT奇响应问题，不等于普通E1强度或直接测得的Schiff矩 |
| [[nndc-2009-ra225-adopted-parity-doublet]] 原始225088001的A/B带L行 | 同自旋E−−E+依次55.16、−11.21、94.95、−42.24 keV；1/2−及7/2−指认带括号 | 评价数据；带标签及指认边界保留，不是独立原实验重分析 |

## Provisional Reasoning

### 1. 质心修正给出严格相消条件，而非八极振幅相消

忽略质子、中子质量差，令R=(Σp r+Σn r)/A。笛卡尔内禀电偶极算符为

$$\hat D_z=e\sum_p(z_p-R_z)=e\frac NA\sum_pz_p-e\frac ZA\sum_nz_n.$$

球张量采用M(E1,0)=√(3/4π)Dz。令质子和中子中心为Rp=Σp z/Z、Rn=Σn z/N，则

$$D_z=e\frac{NZ}{A}(R_p-R_n).$$

因此D=0只约束质子与中子的一阶中心相同。它不要求各自三阶奇矩为零，也不要求β3=0。COM选择Σp z+Σn z=0只是固定平动原点；若同时D=0，两类中心均在原点，而两类密度仍可以具有非零r³Y30。对good-parity本征态，对角E1和E3奇算符期望本就为零；实验信息是异宇称跃迁及相关性，内禀D只能连同破缺对称性和投影约定讨论。

在过渡密度语言，相消是

$$\frac NA\mathrm{Tr}(z\rho^{fi}_p)=\frac ZA\mathrm{Tr}(z\rho^{fi}_n).$$

对SCCM，两个迹还必须包进同一套f_f*、投影、非对角q,q′核和f_i的相干求和。单点平均场Dz=0，并不证明整个跃迁核或GCM的E1矩阵元为零。质子/中子振幅的分拆须先统一坐标、相位及归一化，才能讨论“相消百分比”。

### 2. 八极驱动对不能直接等同于E1矩阵元

球形单粒子电多极矩的必要条件是宇称改变因子(−1)^λ、|j−j′|≤λ≤j+j′，轨道角部分还要求|l−l′|≤λ≤l+l′且l+l′+λ为偶数。由此：

| 轨道对 | Δl、Δj | 直接球形E1 | E3必要条件 |
| --- | --- | --- | --- |
| πd5/2↔h11/2 | 3、3 | 禁止 | 允许 |
| νf7/2↔i13/2 | 3、3 | 禁止 | 允许 |
| νh9/2↔i13/2 | 1、2 | rank-1角动量三角条件不满足 | 允许 |
| νh9/2↔f7/2 | 2、1，同宇称 | 宇称条件不满足 | 宇称条件不满足 |

所以不能写“πd5/2–h11/2的直接E1矩阵元与νf7/2–i13/2的直接E1矩阵元相消”。这些轨道影响八极形变、单粒子混合和完整密度；反射不对称的变形轨道包含多种l,j、宇称成分，E1来自其中允许的rank-1通道及自洽极化。BU17 Fig5的parentage标签不是完整波函数，v²也不提供这些允许分量的幅度和相位。νh9/2、f7/2、i13/2全部变化与D0近零关联，仍不足以唯一反演其各自Dz贡献。

### 3. 奇中子阻塞的方向取决于波函数与自洽反馈

采用ρ=V*Vᵀ约定，从偶真空阻塞准粒子μ、尚未重迭代时：

$$\delta\rho^{(\mu)}=U_\mu U_\mu^\dagger-V_\mu^*V_\mu^T.$$

故固定N,Z的一次密度变化贡献为δD=Tr(Dδρ)，完整奇核解还含重新调整的配对张量、粒子数、平均场形状与质子芯极化。跨核素比较时D算符中的N/A、Z/A本身也变，必须逐核重算。等填充近似对Kramers伙伴取平均，不能恢复完整时间反演破缺的自旋极化。

如果某阻塞态的中子Dz贡献原本与质子项近抵消，减弱该贡献可能增大|D|；若它原本偏离相消，则阻塞也可能减小|D|。八极响应同样可能减弱、重排或增强；不存在“奇粒子必然把八极相消点破坏到某一侧”的普遍定理。实际预测需同EDF的偶偶与逐组态奇核解，以及投影后的E1/E3核。Nomura的145Ba波函数成分可帮助选组态，却不能给出D1S阻塞修正数值。225Ra的Skyrme研究明确强调奇粒子–芯反馈，而该2003实现的时间反演破缺奇核计算不含配对，不能充当完整blocked-HFB/SCCM基准。

### 4. K=1/2双重带的解耦拟合可描述交错，不能唯一抽出隧穿

轴向强耦合截断下分别写

$$E_\pi(I)=c_\pi+A_\pi[I(I+1)-K^2]+(A_\pi a_\pi)(-1)^{I+1/2}(I+1/2),\quad K=1/2.$$

因此双重带差只给Δc、ΔA、Δ(Aa)。不能将最后一项自动写成共同A乘Δa，除非另加A+=A−。对上述四个评价中心值作非加权三参数拟合，得到Δc=31.313172 keV、ΔA=0.438000 keV、Δ(Aa)=−20.428345 keV；预测差为51.9605、−8.0105、96.3212、−43.6112 keV。残差为3.1995、−3.1995、−1.3712、1.3712 keV，RMS=2.4614 keV，仅剩1个自由度。

这些keV级残差明显大于已列能级的0.02–0.06-keV不确定度，因此不能以“拟合得不错”声称按实验误差精确解释。未提供能级协方差，也未拟合组态混合。把转动自变量从I(I+1)−1/4改成I(I+1)，同一预测的截距就变成31.203672 keV；这一约定依赖说明截距本身不是唯一的物理隧穿能。既有064工件所谓“true mean octupole tunneling splitting=31.31 keV”与排除振动/共存的措辞超出拟合信息，不能沿用。K≠1/2时缺少上述一阶特有项，也不代表所有高阶Coriolis效应为零。

### 5. 224Ra的普通E1相消不能等同于225Ra的Schiff响应相消

2003原文Fig3并列D0和Schiff内禀矩：D0对密度一阶中心差敏感，Schiff算符有r²附加权重。两个核或两个算符不共享一个必须同时为零的相消点。2005 Eq1的实验室Schiff矩还包含PT奇相互作用矩阵元与能量分母；强E3、小E1、低同自旋异宇称间隔分别约束不同因子。由224Ra强八极证据直接给225Ra一个已测Schiff矩，或从小D0推出Schiff增强消失，都不成立。此处仅研学该结构边界，不进行超出Day26的完整EDM课程计卡。

## Assumptions

COM推导忽略核子质量差；球形选择规则用于纯lj分量；阻塞公式须遵循给出的Bogoliubov矩阵约定；解耦式限轴向K=1/2强耦合、忽略显式带混合。新取得的两个Ra预印本仅存tmp，未伪称已永久raw归档；正文日期栏的2018重排日期不改变arXiv版本与论文年份。

## Competing Explanations

小E1既可源于密度/算符核相消，也可受组态、投影、转动频率和波函数混合影响；大E3可对应较稳定反射不对称或软八极关联。奇核低能谱的交错可受解耦与带混合共同影响。当前信息不能唯一筛除这些解释。

## Transfer Conditions

可以跨Ba与Ra迁移COM恒等式、张量选择规则、投影核形式和拟合可辨识性检查；不能迁移具体EDF轨道、v²、Dz贡献、相消百分比或阻塞率。

## Failure Conditions

无生产非对角核、完整波函数分量和一致相位时不能计算真实质子/中子相消份额；未重算奇核自洽极化时不能定量宣称相消点移动；没有独立转子参数/组态身份时不能把Δc识别成八极隧穿。

## Falsification or Reverse Tests

用同一EDF依次生成144–148Ba及各低能blocked145Ba组态，输出原始密度、配对、E1/E3投影核及相位；比较E1符号/幅度、E3多跃迁、能量与寿命，检验是否能同时符合。对225Ra，先增加自旋范围和带连接再评估强耦合解耦式的失配，不用四点三参数曲线排除所有竞争解释。

## Open Questions

Egido–Robledo1990完整分项、现代D1S生产核、blocked145Ba的投影E1及225Ra同EDF的配对敏感性仍缺。145Ba与225Ra的阻塞是否移动各自相消点、移动多少，当前无数值答案。

## Human Review

Codex source self-audit与条件推导；未经过用户科学审核，保持unreviewed。

## Promotion or Rejection History

2026-10-29：新增算符选择规则与阻塞边界；对064工件的“真实隧穿”和竞争解释排除不予采纳。保留原工件历史，未改写共享来源页或既有学分。

## Next Actions

生产核和逐组态阻塞计算取得后再做有符号分项。两个新PDF的原件指纹与定向阅读覆盖记录在同名output JSON；由主代理决定按raw治理规则归档与source ingest。不要用自选占据/常数构造百分比，冒充微观复现。
