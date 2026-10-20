---
type: research-note
title: "侧喂养时间与取向：相同边际量不保证相同联合响应"
aliases: [feeding time alignment joint response, DSAM time alignment dependence]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: Day17-uncredited-Day18-DR70-joint-design
evidence_sources: [draper-1970-gaussian-substate-side-feeding]
promotion_target: ""
tags: [DSAM, side-feeding, angular-distribution, polarization, response, identifiability]
---

# 侧喂养时间与取向的联合输入

## Research Trigger

DR70积分混合与DSAM时间feeding是否能分别约束后直接相乘，是本次新问题。若time与取向相关，需要明确何种companion能识别该耦合；本页只证明边际输入的非充分性。

## Grounded Evidence

[[draper-1970-gaussian-substate-side-feeding]] DR70-D17-1/2/10固定purestretchedE2完整求迹、归一population积分混合及原文无DSAMtimekernel的边界；DR70-D17-3/4说明实际表中smoothedfeeding不等独立实验yield/时间分布。以下是Codex条件推导，不是Draper1970的实验结果或当前核的修正。

## Assumptions

孤立、宇称守恒的pureE2级联；两incoherent路径，parentM分布为声明输入，不含precession/退取向。未观测parentγ完整求迹，pointresponse无有限角接受/真实背景；只在所声明模型内讨论识别性。

## Provisional Reasoning

### 相同时间与取向边际不能确定联合响应

设两个路径以各1/2进入同一targetJ=2，随后pureE2到0。目标population `q_A`不是任意捏造的极限：由parentJ=4、M=0经未观测pureE2完整求迹得到，按m=−2…2为(1,16,36,16,1)/70；`q_B`由相同parentJ4的isotropic population同样求迹，为每m的1/5。两者均正且归一，parent的取向可分别赋给两条物理允许的注入路径；没有宣称具体反应能制备这些分布。

目标自身平均寿命τ。prompt注入的光子发射时间密度`g_d=e^(−t/τ)/τ`；另一路先等待平均τ_f再进入target，其密度为两指数卷积。τ_f=τ时`g_f=t e^(−t/τ)/τ²`。两个联合模型为

\[
R_1(t)=\tfrac12[g_d(t)\rho_A+g_f(t)\rho_B],\qquad
R_2(t)=\tfrac12[g_d(t)\rho_B+g_f(t)\rho_A].
\]

它们有完全相同的`Tr R(t)=(g_d+g_f)/2`和`∫R(t)dt=(ρ_A+ρ_B)/2`，所以总时间密度和时间积分的全部光子角度/偏振线性观测都相同。逐时间的取向一般不同；这不等同不同目标τ或不同积分alignment。

对包含能窗、角接受、Doppler及必要Compton选择的线性response operator K(t)，

\[
N_1-N_2=\frac12\int_0^\infty(g_d-g_f)\,
\operatorname{Tr}[(\rho_A-\rho_B)K(t)]\,dt.
\]

若K与t无关，差精确为零。若两kernel相同、两ρ相同，或该响应对两ρ无法区分，差也为零。实际谱响应随slowing/反应点/门变化时，单独测得两个边际并不足以判定联合谱；不能把“可能不同”当已测bias。

## 解析设计与数值核验

仅为无量纲设计，设straightrecoil、nonrelativistic pointcentroid、β(t)=β0exp(−t/t_s)，τ=τ_f=t_s=1。没有使用任何真实核的stopping材料、fs/ps值、detectorgeometry或resolution。

\[
L_d=\frac1{1+\tau/t_s},\qquad
L_f=\frac1{(1+\tau/t_s)(1+\tau_f/t_s)}.
\]

实际CG给`W_A=1+(25/49)P2−(18/49)P4`，`W_B=1`。在同一个pointθ处，归一速度矩为

\[
F_1(\theta)=\frac{W_A L_d+W_B L_f}{W_A+W_B},\qquad
F_2(\theta)=\frac{W_B L_d+W_A L_f}{W_A+W_B}.
\]

| 设计pointθ | F1 | F2 | Δcentroid/(E0β0)=cosθ(F1−F2) |
|---|---:|---:|---:|
| 30° | .39178744 | .35821256 | .02907670 |
| 60° | .37759563 | .37240437 | .00259563 |
| 90° | .34444444 | .40555556 | 0 |
| 120° | .37759563 | .37240437 | −.00259563 |
| 150° | .39178744 | .35821256 | −.02907670 |

90°的F只是条件速度矩，cosθ=0时不能从point质心估F。全角平均速度矩两者同为.375；它不是全角Doppler质心（对称角积分的一阶shift为0），也不是实验F(τ)数据。

新script `system/scripts/day17_time_alignment_joint.py`：CG正性/归一、isotropicparent→isotropicdaughter、独立时间quad对解析Laplace、16/32角投影、equalρ/equaltime/τ_f=0、t_s→0/∞、逐时Tr相同和全角速度矩相同均核。[冻结合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/time-alignment-joint-contract.json)与[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/time-alignment-joint-result.json)保存dependency/script/inputhash。完整sourceCG组件来自本session已核DR70 exercise，不认证原实验producer。

## Necessary Companion and Readiness

需要同transition、同parent/gate的路径强度及对应timekernel/条件取向，或能区分该耦合的多角line-shape/已知feeding标记；再加actualstopping、角能响应、背景和共享Σ。时间积分AD/P不能自动给每个Doppler能窗的P，也不能用当前模型F差替真实实验重标Q或推δ。

对Compton选择，必须传递I/Q/U到同一response和共同分母后再构A；当前设计只实际计算I和理想速度矩，未算阵列Q或实验Comptoncounts。两个积分ρ相同意味着任何固定的线性Stokes算符边际相同，不证明任意能窗/事件排序后仍相同。

## Knowledge Impact and Learning Decision

`limits`把积分feeding/固定alignment分别拟合便视作jointinput已闭合的做法；`supports`记录samegate时间—取向合同的必要性。没有新的τ、δ、P/Q、实验CI或模式判定。对当前165Tm/136Nd/110In及公开23Mg，actualjointinputs未取得，不能推其实际偏差或声称作者原fit错误。


## Competing Explanations

该存在反例不表明所有角间差都来自time-alignment耦合；真实几何、能标、背景、feedingbranch及stopping可产生或掩盖类似差。若各路径ρ或timekernel实际相同，本文差为零，fixedalignment可以适用。

## Transfer Conditions

迁移需相同transition/门、路径身份及制备密度、时间与逐角/逐能response合同；强度与Stokes共享分母。当前无量纲数不转给任何核素、阈值或polarimeterQ。

## Failure Conditions

末态门非identity、相干路径、随时间deorientation、relativisticrecoil或有限接受需替换相应operator/kernel。若实验response对两ρ投影相同，模型差不可观测；当前point例不提供实际探测灵敏度。

## Falsification or Reverse Tests

equalρ/equaltime/零feeding及时间常量K应消差；fullangle一阶centroid为0；90°point无法由质心反推F。新数值quad与解析Laplace及CG正性控制已经执行，真实samegate多角谱若能支持共同kernel，应相应收缩该耦合nuisance。

## Open Questions

当前165Tm/136Nd/110In或公开23Mg是否具备逐路径取向/时间输入；实际门/能窗对该耦合有多大灵敏度；该参数与stopping/feeding/背景的jointΣ是否可识别？当前未获输入，保readiness，不提出实验偏差数值。

## Human Review

本页为Codex自审的provisionaldesign，未human-reviewed；不清除任何source needs_review。论文用途需定向回源与actualresponse核验。

## Promotion or Rejection History

2026-10-20首次以条件研究笔记保留。尚未晋升实验finding/模式判据或给正式Day18学分；若actualinputs满足零差条件，保留证明并缩小对该实验的相关性。


### 实际取向汇编的输入边界

[[ekstrom-1979-spin-alignment-attenuation-a61-a67]] EK79-D17-1–11提供实际39行/32rank4的反例/来源核：同lab、共parent与private/unpublished源不独立；模型alpha2误差处方用同data挑选，不是experimentα4/σprior。原Fig5的20%feed是design，仍无真实time-alignmentkernel；因此本页存在反例获得输入相关性的实验背景，未获得任何当前核jointinput或bias验证。
