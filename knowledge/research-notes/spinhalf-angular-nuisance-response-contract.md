---
type: research-note
title: "spin1/2的角关联nuisance：核静止系、末态门与实验室响应"
aliases: [spin-half angular nuisance contract, 31S A2 physical domain]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: Day17-uncredited-Day18-SunSI-object-audit
evidence_sources: [sun-2023-bayesian-dsam-31s, yamazaki-1967-aligned-angular-coefficients]
promotion_target: ""
tags: [angular-distribution, polarization, spin-half, DSAM, nuisance, reference-frame]
---

# spin1/2的A2首先要定观测对象

## Research Trigger

[[sun-2023-bayesian-dsam-31s]] SUN23-20的官方SI Fig9/12把3076/5156-keV态标为1/2+，同时展示名为A2的α–γ angular-correlation nuisance后验。作者本来就称其为nuisance，并未把它报告为核alignment。当前未取得其actualemission/boost/response模块或A2角的参考系。

新问题是：若A2表示核静止系的发射强度，spin允许域是什么；若它表示实验室/响应的现象参数，能否直接用相同限制？本页给必要条件与反例，不做原寿命重拟合或作者错误判断。

## Grounded Evidence

- [[yamazaki-1967-aligned-angular-coefficients]] YA67-13：原PDF1 Eq1用两个同J的CG定义statisticaltensor；k≤2J来自triangle。本文的alignedpopulation公式不单独证明任意非对角ρ的全部Stokes，本页另作photontrace推导。
- Sun SUN23-6/20：主文A2 uniform[-1,1]、A4=0，SI两1/2+态也显示A2。原文没有在所取对象中给private模块/完整参数config。
- Sun SUN23-2/3/18/19：αtag/transferkinematics、0°cloveraddback与γ谱响应/门能窗是实际选择，不能按名称自动视为裸restframe angular distribution。
- 本session定向复核YA67原PDF1/printed1 Eq1/2并视觉核，原hash不变；没有重读其全部23页/表或换新实验信用。

## Assumptions

所证明对象是：isolated、宇称守恒的核EM发射；初态Ji=1/2、任意正的2×2条件密度ρ且Trρ=1；只选定一个核transition，**末态核磁子态不再作后选择**。未测光子偏振的强度和linearStokes都在核静止系、响应折叠之前定义。

αtag在此模型中只制备条件ρ，不扩展核spin空间。实multipole混合与native算符在合同中声明；不是Sun actualamplitudes/ρ/速度。旧CG/Jones已有priming，新的source-specific问题/合同不是独立盲测，也不把旧check数换成formal18信用。

## Provisional Reasoning

### 核静止系的必要rank限制

任意ρ的不可约分量来自Ji⊗Ji，因而k≤2Ji=1。未测偏振、宇称守恒的单光子强度只取evenrank，故仅k=0：归一角强度I_rest(n)=1，裸核A2=A4=…=0。

另从沿光子方向量子化的helicity幅度看，光子off-diagonal密度需要初态m−m′=±2；spin1/2的差最大1，所以该coherence为0。于是Q_J=U=0，linearP=0；vectororientation仍可使两helicity强度不同，故V未必0。不能把“强度各向同性/无linearP”改写成光子完全无偏振。

新程序的exactCG矩阵给

\[
4\pi\sum_hT_h^\dagger T_h=\mathbf1_2,
\qquad4\pi T_-^\dagger T_+=\mathbf0_2.
\]

四个声明的pure/mixed通道(Jf=1/2、3/2、5/2)均作符号δ恒等式，旋转协变使任意方向/任意正ρ成立；旋转Jones数值迹给I/矩阵残差约8.9×10⁻16、Q/U约4.4×10⁻16，声明pureorientation可达|V|=1。这是模型控制，不是实测31S圆偏振或新polarimeterQ。

### 不能省略末态求迹条件

若测后续γ，原末态的接受算符E_G通常不再是identity。声明未取向1/2→3/2→1/2、pureM1/M1级联，选择第二γ方向，直接jointtrace得到

\[
W_{\gamma\gamma}(\Theta)=1+\frac14P_2(\cos\Theta).
\]

初态spin1/2并没有禁止这个**双光子条件观测**的rank2；它不再是上式末态全求迹的singles。另一个Ji=3/2、pureM1、低|m|布居控制给I=1−½P2，排除了程序把所有A2都机械清零的可能。

Sun所述α初始tag与此后续γ门不是同一操作。必须先核真实eventselection，不能把条件初态、末态接受与γγ关联的rank混为一个上限；这个边界也连接Day17的referencegate/P/A/Q问题。

### boost与响应会改变实验室角谱

即便restI=1，单一速度β沿z的理想Lorentz变换也给

\[
I_{\rm lab}(x)=\frac{1-\beta^2}{(1-\beta x)^2},\quad
x=\cos\theta_{\rm lab},\quad\frac12\int_{-1}^1I_{\rm lab}dx=1.
\]

小β展开为1+2βP1+2β²P2+O(β³)。声明β=.1控制的Legendrea2≈.0200862；它不是Sun的actualβ或A2。真实slowing/角接受、γ能窗、反应点和仪器响应还会进一步改变lab分布。

因此“核restA2=0”不能直接要求一个lab/response现象参数也为0；若actualcode确在发射前把它当核P2，则该spin允许域应进入物理prior。当前缺的正是这一module/frame映射，不能从SI图的非零后验直接推寿命偏差。

## Competing Explanations

| A2实际对象 | 可以说什么 | 尚不能说什么 |
| --- | --- | --- |
| 核restframe、末态全求迹的P2发射项 | 给定Ji1/2及本页EM条件，必须0 | 未确认module语义前不归因原paper |
| 末态γgate后的jointcorrelation | 可以出现rank2；需联合测量算符 | 不能套singles上限 |
| labframe/响应现象项 | 可以吸收kinematics/接受形状 | 不称独立测得核alignment/δ |

另有显式宇称违背E1+M1形式控制：允许vectorrank1强度，但仍不能造出Ji1/2的核rank2。本控制只测试定理假设，不赋予真实31S这种发射机制。

## Transfer Conditions

迁用前写明Ji、γ分支与finalselection、强度/linear/circular对象、rest/labframe、boost和响应顺序。αtag、下游γgate与只按源/阵列名称不是可互换的条件；同名A2未必同一层。

## Failure Conditions

末态后选择、外部相互作用改变isolated核EM对象、未识别的混合母态/feeding、在lab参数上误套rest定理，都使机械置零失效。拟合nuisance可能只是现象自由度，不能仅凭与微观rank不同就称原数据错。

## Falsification or Reverse Tests

最高信息输入是Sun actualA2生成/boost/acceptance代码及其参数config。确认A2为rest发射项后，才比较physicalmodel与额外现象模型的同数据拟合、posteriorpredictive与prior敏感性。没有actuallikelihood/训练/事件，不能从cornerplot直接算条件τCI；硬设A2=0也不是过滤有限MCMC样本中恰好等0的点。

## Evidence Gaps

2023VoRmainbody、actualprivateproducer/训练/完整支持与posterior draws仍未取得；source已取得的是2022v2和publisherSI。当前无法定量判断A2角色对τ的影响，更未输出原实验新CI、δ或spin赋值。

## Open Questions

原A2究竟乘在哪个frame/阶段？1/2+态是否只是与其它state共用一个phenomenological模板自由度？若它代表残余response，是否有独立source/geometry约束？这些不能靠更多相同数学测试解决。

## Reproducibility

[问题/priming冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/sun2023-spinhalf-freeze.json)、[新合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/spinhalf-angular-contract.json)、[新程序](../../system/scripts/day17_sun2023_spinhalf_angular_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/spinhalf-angular-result.json)核SI/YA67原hash与所复用helpers。最初未加末态γgate控制的script/contract/result另存，后补控制不覆盖初版本。

运行`PYTHONPATH=/workspace/wiki/tmp/day16-jt74/python-deps python3 system/scripts/day17_sun2023_spinhalf_angular_contract.py`。输出精确矩阵/新native迹/反控制，点数只是声明模型覆盖，不是独立数据、实验样本量或课程分数。

## Human Review

本推导和source前提为Codex自审/needs_review；不设human-reviewed、不以程序输出清除原sourceclaimreview，不把现有缺口自动变为用户待办。

## Knowledge Impact and Learning Decision

`supports`对核发射prior施加明确物理域；`limits`把任何拟合A2都叫核alignment，及由spin1/2机械否定所有条件/实验室角关联的推断。条件定理与其必要反例都持久化，不宣称作者实际模型错。

## Promotion or Rejection History

2026-10-19 Day17内恰好无学分Day18方法preview。L2 theorem/native/反控制闭合，L3 module/frame输入问题已收窄；L4原DSAM重拟仍未ready。不授18、不重授17、不打开19。

符号z矩阵和旋转光子迹采用不同收缩，但共享SymPyCG后端和既有d/helper；它们是互补代数/数值控制，不是完全独立软件验证或独立实验。
