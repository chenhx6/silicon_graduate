---
type: research-note
title: "高K进动、TiP与有限自旋取向分布的约定"
aliases: [A130 angular convention and precession reference]
created: 2026-11-13
updated: 2026-11-13
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "Gemini正文返修后由父按原件与接受范围重建"
promotion_target: ""
evidence_sources: [shimizu-2005-high-k-precession, lawrie-2020-tilted-precession-wobbling, frauendorf-2014-transverse-wobbling, nomura-2022-questioning-wobbling-ibfm, lv-2022-evidence-against-wobbling-135pr, book-suhonen-from-nucleons-to-nucleus]
tags: [doctoral-thesis, high-K, precession, TiP, wobbling, convention]
---

# 取向模式的坐标、能量比较和波函数条件

## Research Trigger

3.4返修需要区分固定I的局域模式、固定K的跨自旋能级差、经典轨迹和量子分布。
本页记录可复用条件，不以声子标签或一条下降曲线代替共同的谱学预言。

## Grounded Evidence

[[shimizu-2005-high-k-precession]]实际v2原PDF2–3的Eqs.(1)、(5–11)，
以及PDF5–6的Eqs.(29–40)，用于高K强耦合谱和指定轴对称RPA参考系关系。
[[lawrie-2020-tilted-precession-wobbling]]原PDF2–3的Eqs.(1–4)、Figs.2–3
用于所选转子/粒子转子取向图景；不据此声称所有PRM轨迹均为闭合椭球交线。
[[frauendorf-2014-transverse-wobbling]]PDF6的Eqs.(11–24)与PDF10讨论，
分别限定冻结顺排展开及M1等模型局限。[[nomura-2022-questioning-wobbling-ibfm]]
与[[lv-2022-evidence-against-wobbling-135pr]]的软核IBFM和固定形变QTR是不同实现。
原件路径/实际SHA回相应source；没有全本通读或复现实核程序的声明。

## Provisional Reasoning

理想轴对称形状转子的轴角冗余由R3=0表示，不能推广成所有轴对称微观体系
的轴向推转响应都为0。物理核芯角动量R带作用量单位，mathcalI和j已除以hbar，
则Hcoll=Rperp²/(2Jperp)=hbar²(mathcalIperp−jperp)²/(2Jperp)，不能再多乘hbar²。
固定内禀K、常惯量、忽略跨组态科里奥利混合的强耦合谱为

$$E_K(I)-E_{\rm intr}=\frac{\hbar^2}{2\mathcal{J}_\perp}[I(I+1)-K^2],\quad I\ge K.$$

相邻允许能级差为hbar²I/Jperp，首差为hbar²(K+1)/Jperp。
能差的存在与是否实际出现相应光子是两个问题，后者另受算符和选择定则约束。
大K领先项hbar²K/Jperp不能抹去有限K修正。

在Shimizu所述轴对称小振幅RPA、物理DeltaK=+1分支中，
omega_wob=omega_prec−omega_rot，且omega_prec=hbar K/Jperp_eff(omega_prec)。
K=<Jx>/hbar无量纲；这是一条自洽的频率关系。进一步的适用绝热极限才允许
将频率相关惯量近似为静态响应。x轴与前段数字3轴是明确的坐标重标，不能无声混用。

纯转子或冻结内禀向量的简化经典模型可画角动量球与二次能量曲面的交线；
动态内禀自由度的一般PRM不能缩成同一幅图。分离轨道不必周期闭合。
取向概率图是量子表象，实验通过能谱、矩阵元及相应响应约束模型。

对标准一维问题，若动能、势与边界均在x->−x下不变，反射奇态有psi(0)=0。
对称非简谐项不消除这一节点；有限I的投影/边缘概率另按其定义计算。
角反射、三维空间宇称与signature不是一个操作。
局域大I、低阶激发、远离软模时可有角宽约1/sqrt(I)标度，不是普适FWHM。

声子近似要求局域展开受控，而非所有EM强度严格线性或所有惯量必须互异。
冻结j是一个模型假定，频率相关响应或耦合正规模并不自动排除谐振描述。
1/I和M1抑制须保留各自算符、惯量、g因子与自旋窗口，不能当跨核区的认证门。
SI磁矩型M_mu和电荷量纲型M_S=M_mu/c的配对、命名单位数值与实用率常数，
沿用[[a130-rewrite-magnetic-unit-and-numerical-normalization-20261113]]；
有名的相位标签与完整几何系数的统一由全书约定核查完成，不能只翻delta符号。

## Assumptions

各谱式属于明确的轴对称强耦合或局域模型；原件RPA的频率关系不推广成所有
三轴运动的恒等式。节点论证限于对应反射和适当函数定义域。

## Competing Explanations

signature伴带、准粒子重取向、组态交叉、软核耦合均可改变伴带能差和EM特征。
固定形变QTR的重取向不等于显式gamma振动；模型输出也不等于实测转轴轨迹。

## Transfer Conditions

迁移的是定义和检验方法；目标核的轴序、占据、内禀态、响应及可测自旋窗须重建。
高K进动与三轴小振幅模可在指定模型极限联系，但不能凭名称认定全动力学同构。

## Failure Conditions

混用物理R与无量纲j、漏频率中的hbar、把有限K首差当大K精确式、将所有轨迹
画成闭合交线、由非简谐或Coriolis存在就断节点消失，以及把单曲线命名成模式。

## Falsification or Reverse Tests

T17的有理数控制核固定K能差与SI两种振幅形式，不验证实核拟合。
比较未参与调参的绝对EM、相位敏感观测和能谱，并保留共享输入的协方差。

## Open Questions

具体核的完整响应和观测是否支持局域展开，须用各模型与实际测量检验；
不要求先解决全部模式争议才能写出条件完整的综述。

## Human Review

本轮为智能体原件与代数自审，没有新增真实用户审核事件，不写作human-reviewed。

## Promotion or Rejection History

2026-11-13：父重建以撤回旧稿全闭合轨迹、严格线性要求和未核数值阈值；
3.4科学内容与最终TeX/ledger实际指纹以G88父验收回执为准，组稿与全书约定另核。
