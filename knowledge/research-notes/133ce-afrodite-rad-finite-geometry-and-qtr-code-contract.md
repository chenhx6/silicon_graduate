---
type: research-note
title: "133Ce AFRODITE 阵列几何、全探测器门 RAD 算符偏差与 QTR 代码链输入合同"
aliases: [133Ce AFRODITE RAD and QTR contract, AFRODITE有限角门与GAMPN-ASYMO-PROBMO合同]
created: 2026-10-27
updated: 2026-10-27
status: active
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [wakudyanaye-2022-triaxiality-rotational-bands-133ce, ding-2021-131ba-133ce-signature-splitting, emediato-1997-133ce-rdds-lifetimes, ragnarsson-semmes-1988-particle-rotor-moments, larsson-1978-nuclear-core-quasiparticle-coupling]
created_from: Day25 checkpoint005 source audit
confidentiality: public
tags: [133ce, afrodite, rad, dco, qtr, gampn, asymo, probmo, analysis-blueprint]
---

# 133Ce：阵列接受度与QTR接口的可恢复边界

## Research Trigger

继续[[133ce-thesis-analysis-blueprint]]的实际分析蓝本。checkpoint005回读WK22 PDF49/50/54/59/61/77/78/98/99；父代理fresh视觉核Table6.2，独立代理核方法原件。新增判断均needs_review:true。

旧版“44.177+6.423精确恢复λ”“负宇称λ应为58.2”“相同事件数证明sorting差异”“门占比60–70%/实际残差数个百分点”认证撤回。Git与tmp/day25-audit005快照保留旧稿；结构lint不构成科学认证。

## Grounded Evidence

|来源|实际所述|边界|
|---|---|---|
|[[ding-2021-131ba-133ce-signature-splitting]]，PRC104,064304(2021)，§II.A|8 clovers：4@90°、4@135°|装置描述，不是actual mask|
|[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] WK22-01/31，PDF54/61|通用8 clovers+7 LEPS，具体段13 clovers：1@45°、8@90°、4@135°|冲突保留，不任选一组认证响应|
|两源报告事件数|2.8×10¹⁰双符合、5.4×10⁹高阶符合|强同源线索，不证明同event stream或差异成因|

run ID、active mask、45°events、sorting geometry和同门counts仍缺。45°被关闭仅是候选原因；去掉它也不会把8@90°变成4@90°。

## Provisional Reasoning

WK22-27/35（PDF59 Eq4.6）定义135°/90°目标线在all-detector门下的比值，报告约1.3/0.8的经验参考。响应需由有序级联核与逐pair接受度求和：

$$Y_a(g)=\sum_{i\in a,j}\int A_{ij}(\Omega_1,\Omega_2,E_1,E_2)
W_g(\Omega_1,\Omega_2)\,d\Omega_1d\Omega_2.$$

A包含效率、mask、固角、门宽、同detector排除及sorting，不能由clover数量恢复。门在线之后、方向/偏振完整无偏求和且无其它选择耦合时，可trace后续光子，恢复先前光子的边缘分布；门在线之前，上游辐射仍可通过布居转移影响后续取向。不能无序地把任意gate说成严格不依赖多极性。

仅在equal-weight point-ring及方位平均条件下：

$$q_k=\frac{\sum_j n_jP_k(\cos\theta_j)}{\sum_j n_j},\quad
(q_2,q_4)_8=(-1/8,-1/64),\quad(q_2,q_4)_{13}=(-11/52,31/416).$$

非零矩说明“all”不能保证4π消去；它不决定具体级联偏差的正负、大小甚至是否非零。8/13=61.54%仅等权数量比例，不是实测门份额。实际R_AD/δ需本run响应与校准，不跨阵列搬值。

## 4. 程序角色不等于actual输入

WK22-38/39（PDF49–50）说明GAMPN生成sp态/矩阵，ASYMO耦合转子，PROBMO计算EM；未交付2022版本、header、units、BCS/blocking、core-R惯量、完整signed wavefunctions与EM输出。

[[ragnarsson-semmes-1988-particle-rotor-moments]] RS88-03/05和[[larsson-1978-nuclear-core-quasiparticle-coupling]]原formalism：

$$H=H_{\rm intr}+H_{\rm core}(R),\qquad
H_{\rm core}=\sum_k A_k(I_k-j_k)^2,\quad A_k=\hbar^2/(2\mathcal J_k).$$

I、j按ħ为单位。展开已含一次Coriolis交叉项，不能在含R的Hcore后再减同项。常惯量展开不能替代实际core-R依赖Harris的recoupling合同。

## 5. BCS共同零点不变性与反向构造的失败

WK22-30（PDF78 Table6.2）表头确写MeV；|18〉、|19〉、|20〉为5.8046、5.8239、5.8985，|23〉为6.4922且主要含N6分量。正Ce/Baλ=50.6/51.0MeV；负宇称实际λ未给。

经验41A^(-1/3)在A133约8.03218MeV，6.42302正是50.6−5.5ħω的倒算残差，不是原表数据。Fermi不必精确落在本征能；加法相等不证明表值的N4相对原点，也不能由N5推出λ≈58.2。表头误标振子单位、原点差或其它接口/排版问题都只是待核候选，不改表。

标准BCS中：

$$E_\nu=\sqrt{(\epsilon_\nu-\lambda)^2+\Delta^2},\qquad
v_\nu^2=\tfrac12[1-(\epsilon_\nu-\lambda)/E_\nu].$$

ε→ε+C、λ→λ+C共同移位不改变E与u/v；单位换算则ε、λ、Δ必须共同变换。不同宇称可在同mean field共用化学势，分别形变/阻塞job也可不同；必须由actual input判断。

直接反例：[[emediato-1997-133ce-rdds-lifetimes]] PDF2/2106的负宇称νh11/2 PTR计算明确用λ=50.6MeV、Δ=.92MeV、ħω0=8.41MeV及N4/5空间。这反驳“负宇称禁止50.6”的普适红线，但不恢复WK22实际参数。

## 6. ε4与下一必要输入

WK22 PDF77 Table6.1正宇称.1/正文.01同时保留，Ding正文.01只补谱系；负宇称.015另记。不由典型量级选择actual值或证明轨道交叉“虚假”。下一高信息输入为实际header/input/output；被阻时转可解析的同母态依赖/相干相位问题。

## Learning Decision

revises旧零点/实际响应认证；supports字段级程序合同、条件接受度和共同能量原点检查。actual作者job未复现。

## Assumptions

点环矩仅equal weight/point acceptance/方位平均控制。BCS共同移位保持同一Δ和配对处方；不同job不由此自动建立参数相同。Hcore展开仅常惯量说明。

## Competing Explanations

装置描述差异可能来自文字、升级或sorting子集，当前不能择一。ε表的单位/原点/接口问题是待核类别，不由数字近似选择实际转换。

## Transfer Conditions

实际角响应需本run逐pair校准；单位转换须共同处理ε、λ与Δ；历史PTR参数和代码角色不能直接迁为2022输入。

## Failure Conditions

仅用8/13推实际门份额、用壳数给λ强制差一个ħω、在Hcore(R)后再加Coriolis，均不满足当前合同。

## Falsification or Reverse Tests

共同平移ε与λ后BCS的E/u/v保持；将仅λ平移则不再是参考零点变换。负νh11/2原job的λ50.6反驳普适禁令，但不验证WK22 actual值。

## Open Questions

run/mask/45°events/sorting与actual header、ε4选择、配对/阻塞、完整signedEM仍缺。获取受阻时保留已查入口，转可解析问题。

## Human Review

本页未发生用户claim裁决，review_status保持unreviewed；不迁移其它source或Band5的人审到本推理。

## Promotion or Rejection History

2026-10-27 checkpoint005撤回旧强认证，以原件和声明条件的前向控制替代；reasoning_status为provisional。旧稿在Git和入口快照保留，未将self-audit写成human-reviewed。
