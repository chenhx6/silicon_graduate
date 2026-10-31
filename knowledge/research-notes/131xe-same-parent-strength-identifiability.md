---
type: research-note
title: "131Xe同母态M1/E2强度分解与模型能量约定"
aliases: [131Xe same-parent strength identifiability]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [chakraborty-2023-131xe-wobbling-origin, rose-brink-1967-phase-defined-angular-distributions]
created_from: "Day28 independent-L3 strength worker and parent source audit"
promotion_target: "131xe-low-spin-partner-crosswalk"
tags: [131xe, mixing-ratio, branching-ratio, covariance, model-convention]
---

# 131Xe同母态M1/E2强度分解与模型能量约定

## Research Trigger

[[131xe-low-spin-partner-crosswalk]]已由1055.1/815.6-keV光子强度重算作者的B(M1)/B(E2)。本页补齐E2商与识别性：两个由同一强度比和δ算出的商不是新增的两项独立观测；模型δ还需要能量、算符和相位合同。

## Grounded Evidence

| Evidence | source / locator | provenance | limitation |
|---|---|---|---|
| 1861.9-keV同母态的1055.1与815.6-keV线，强度6.0(2)/1.0(1)；Fig.4标δ1055=0.1(2) | [[chakraborty-2023-131xe-wobbling-origin]] C23-D28-6 | Table I、Fig.4的出版数据 | 未提供本次所需的共同响应、联合Σ或全局δ似然 |
| 模型商1.27与δTPRM=−0.69；最右TPRM列出带 `17/2−→15/2−` 为902 keV、带内 `17/2−→13/2−` 为799 keV | 同source C23-D28-4、C23-D28-7 | Fig.11、printed064318-6/7 | δ计算所用Eγ未在该段明示 |
| 全角积分光子率、多极能量幂与相位定义的混合比 | [[rose-brink-1967-phase-defined-angular-distributions]] RB67-D28-001 | printed318 Eqs.3.29–3.30、printed319 Eq.3.39 | 本页常用B归一、同母态代数和单位换算是任务推导 |

## Provisional Reasoning

### 同母态两商的条件推导

设d为M1/E2混合出带线，c为纯E2参照线，r=Id/Ic，u=|δ|²。Id、Ic须是匹配布居与门选样、经效率和角响应校正的积分光子强度。采用常用B归一，写

\[
\lambda_{\gamma,E2}=k_E E_\gamma^5B(E2),\qquad
\lambda_{\gamma,M1}=k_M E_\gamma^3B(M1).
\]

δ²在实振幅约定内等于该线E2/M1积分光子率比。共同母态寿命消去后，

\[
R_E=\frac{B(E2;d)}{B(E2;c)}
=C r\frac{u}{1+u},\quad
R_M=\frac{B(M1;d)}{B(E2;c)}
=A r\frac1{1+u},
\]
\[
C=(E_c/E_d)^5,\qquad A=\kappa E_c^5/E_d^3 .
\]

能量用MeV、B(E2)用e²b²、B(M1)用μN²时κ≈0.697；RE无量纲，RM单位为μN²/(e²b²)。worker从率公式与SI单位换算得到κ≈0.696776；本次对账沿用舍入0.697，不把额外小数当实验精度。光子强度已经是辐射分支，不能再任意乘内转换系数。

代入印刷中心值得RE≈0.0163964、RM≈1.2722366。RE是选定小δ分支与输入合同下的出版表推导，不能另称独立实验测量。仅将δ的印刷数值区间[−0.1,0.3]映射到RE也不是新的置信区间。

### 识别性与共享信息

在固定能量下，两商满足

\[
\frac{R_E}{C}+\frac{R_M}{A}=r,\qquad
u=\kappa E_d^2\frac{R_E}{R_M}\quad(R_M>0).
\]

只有光子强度比时，分解落在一条直线上；加入独立获得的|δ|才选定条件分量。两商不恢复δ符号，也不恢复绝对B。由同一r、δ构造RE/RM，再把二者与r、δ一起当四项独立模型得分，会重复计权。

(r,u)到(RE,RM)的Jacobian行列式为−ACr/(1+u)²，r>0时非零；改用δ坐标多一个2δ，故δ=0处一阶敏感性消失。其物理含义是小δ附近二次敏感，绝不表示E2误差为零。

### 协方差合同

令x=(Id,Ic,Ed,Ec,δ)，y=(RE,RM)，局部传播必须用Σy=JΣxJᵀ。对δ≠0：

\[
d\ln R_E=d\ln I_d-d\ln I_c+5d\ln E_c-5d\ln E_d+
\frac{2d\delta}{\delta(1+\delta^2)},
\]
\[
d\ln R_M=d\ln I_d-d\ln I_c+5d\ln E_c-3d\ln E_d-
\frac{2\delta\,d\delta}{1+\delta^2}.
\]

共同强度归一化消去；效率、背景、门、alignment与δ拟合仍可能产生交叉协方差。固定r只变δ时两商反相关；固定δ只变r时正相关。不能预设两商独立。

仅为局部示范，假定印刷σId=0.2、σIc=0.1、σδ=0.2互相独立并固定能量，得到σM≈0.14326、ρ(RE,RM)≈−0.32668。固定δ=0、只传播独立强度又得σM≈0.13545，两者都舍入成0.14。因此复现“1.27(14)”不认证原作者使用了哪种误差算法。局部σE≈0.06496大于RE中心值，不能把它发布为新的对称实验误差或任意截断成置信区间。

### 模型能量约定的撤回边界

C23公开材料给出`RM=B(M1;out)/B(E2;in)`，而报告的`δ`对应出带跃迁中的
`B(E2;out)/B(M1;out)`。两者之间还隔着未知的
`RE=B(E2;out)/B(E2;in)`：

\[
\delta^2=\kappa E_{\rm out}^2\,RE/RM.
\]

因此不能由`RM=1.27`和`δ=-0.69`反推出δ采用哪一个光子能量，也不能把
902/799-keV模型端点与1055.1/815.6-keV实验线静默绑定。**在明确声明
`E_ref`、同一out/in跃迁、单位和`κ`后，条件算术本身仍有效**：`E_ref=1.0551`
MeV给`RE=0.7792590923`、实验能量下条件光子比`8.7534953761`；`E_ref=0.902`
MeV给`RE=1.0662426471`、相应条件光子比`9.7932695843`。若同时采用Fig.11
902/799-keV端点，条件光子比为约`5.5351869375`或`6.0613929450`。
这些数值是本任务的条件敏感性算术，不能写成作者真实TPRM预测或统计裁决；
把模型δ混入实验强度得到`RM≈0.870509`也只是定义明确的hybrid sensitivity
calculation，不是模型输出。仍保留“模型电磁算符、有效电荷、g因子、淬灭和
δ能量约定未公开”的source boundary。完整单位审计见本轮
`tmp/day28-model-review/formula-and-unit-audit.md`。

## Assumptions

d截断为M1/E2、c在所用精度内可作纯E2；对象端点与同母态一致；强度是匹配选样的校正光子率；δ的相位、分子/分母与能量约定明确。ΔI=2本身不量化所有高阶多极的可忽略性。

## Competing Explanations

小RE可限制指定的强E2带间衰变解释，不能唯一确立signature partner。若Fig.5另一δ分支成立，分量商会改变；大RE也还需对具体wobbling、粒子—芯耦合或其它集体机制作显式比较。共享强度/δ的派生量不构成独立投票。

## Transfer Conditions

可迁移到其它同母态M1/E2—E2分支，前提是使用相同光子率、单位与选样合同。不得迁移到不同母态的原始峰面积比；绝对B另需寿命、分支和内转换信息。

## Failure Conditions

强度分母近似且无误差、门选择改变相对布居、未拆双峰、参照非纯E2、δ存在未跟踪的大解、模型能量约定不明，都会使本页条件计算不能承担实验裁决。零δ处只用一阶误差尤其会丢失E2的二阶不确定性。

## Falsification or Reverse Tests

代码以独立正向辐射率生成两条光子率再反求B商，检查单位、零/大δ极限、δ反号不变、共享率约束、Jacobian有限差分及共同归一化消去。当前11项控制通过只认证代数实现。实验若给出不满足共享率恒等式的“独立RE/RM/r”，应先核对象、校正与协方差，不能直接归为新物理。

## Open Questions

C23计算δTPRM时实际用哪组Eγ？与RM是否共用相同电磁矩阵元、相位和对象？真实联合Σ与全局δ分支如何恢复？这些是需继续取证的输入缺口，不由本页条件算术补齐。

## Public Convention Audit

arXiv源文件`131Xe.tex:265-275`和C23 Fig.11闭合了TPRM的公开方法骨架、参数`ε2=0.13`、`γ=33°`、`ξ=1`及端点映射：出带`902/1055.1 keV`、带内`799/815.6 keV`。来源没有公开E2/M1算符、有效电荷、轨道/自旋g因子、淬灭因子或`δTPRM=-0.69`的确切能量输入。

需要特别区分：

- `RM= B(M1;out)/B(E2;in)=1.27`；
- `δ²=κ E_out² [B(E2;out)/B(M1;out)]`。

因此`δ`与`RM`之间还隔着未知的`RE=B(E2;out)/B(E2;in)`，不能仅用公开的`δ=-0.69`和`RM=1.27`反推模型能量，也不能把这种反推写成“902-keV约定已由作者确认”。完整公开来源与阻断端点见[模型约定审计](../../outputs/learning-daily/20261030-DAY28-independent-l3-research-week-four-exam-run-01/workers/model-convention/findings.md)。

## Human Review

- Review scope: 本页为worker推导经父任务原图抽查后的Codex self-audit。
- Decision: provisional；未发生human review。
- Complete unresolved P0/P1 inventory: 科学P1为全局δ、真实Σ、光子校正和模型电磁约定；没有据此捏造L4数据或新实验误差。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-10-30 | Day28持久化条件推导 | worker output | provisional research-note | 真实表图输入与率公式闭合；误差及模型约定仍有边界 | [[131xe-low-spin-partner-crosswalk]] |

复现入口：[derive_strength.py](../../outputs/learning-daily/20261030-DAY28-independent-l3-research-week-four-exam-run-01/workers/strength/derive_strength.py)、[worker原推导](../../outputs/learning-daily/20261030-DAY28-independent-l3-research-week-four-exam-run-01/workers/strength/derivation.zh.md)。本页保存全部可复用公式、条件数值与限制，outputs只保存运行副本。
