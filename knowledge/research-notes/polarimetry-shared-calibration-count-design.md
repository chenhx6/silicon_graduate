---
type: research-note
title: "偏振计数的共同几何校准与参考线比值设计"
aliases: [shared geometry calibration in polarimetry, P A Q count design]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: daily-learning-Day17-L3-design
evidence_sources: [starosta-1999-pdco-experimental-test, schmid-1998-gammasphere-polarization, garnsworthy-2019-griffin-facility]
promotion_target: ""
tags: [polarimetry, calibration, covariance, experimental-design]
---

# 偏振计数的共同几何校准与参考线比值设计

## Research Trigger

[[starosta-1999-pdco-experimental-test]] 原 printed18 Eq3/4（ST99-14）定义 clover 的散射计数不对称度和无偏振几何校准；[[schmid-1998-gammasphere-polarization]] printed100 Eq13、printed101 Eq15/16（SG98-4/13）给双分段的另一种估计量。两文均由已知偏振参考的 A/P 标定 Q，均未提供可恢复全部共同校准依赖的原始计数与 Σ。这里保存可复用的联合计数设计和一个改分母反例；这是本任务推导，不是两篇论文直接报告的新实验结果。

关键问题是：同一个无偏振样本校准 a 或 η 后，同时用于参考 A_r 与目标 A_t，怎样计算 P_t 的误差？只分别列 σ_A 与 σ_Q 不足以回答。该问题直接影响 matching-reference 的 δ/EM 判据，值得持久化，但尚未验证任一实际实验的完整统计模型。

## Grounded Evidence

### P/A/Q分层与原件输入

| 层 | Clover：ST99实际定义 | Gammasphere双分段：SG98实际定义 | 需要另行测量或核验的输入 |
| --- | --- | --- | --- |
| physical P | 电场在反应面内减面外的强度差/和，printed17 Eq1 | J0−J90 的差/和，printed99 Eq5 | 指定自旋、布居、方向、gate、纯度与相位；不是 Compton 散射计数本身 |
| measured A | (aN⊥−N∥)/(aN⊥+N∥)，printed18 Eq3 | (ηC−S)/(√η(C+S))，printed101 Eq15 | 原始/拟峰计数、背景与事件复用；C须含两侧confined及side-ADC-zero |
| null response | a=U∥/U⊥，printed18 Eq4 | η=Su/Cu，printed101 Eq15后定义 | 同能量、阈值、门和arrayweights的无偏振样本；null不能单独确定Q |
| polarimeter Q | Q=A_r/P_r；原NORDBALL单clover向EUROGAM移用有边界 | Q=A_r/P_r；三pureE2参考的P来自AD/Eq6 | 已知P_r及其误差/响应；几何、阈值与参考选择必须匹配 |
| angular Q_k | 与上述标量Q不等同 | 与上述标量Q不等同 | 角关联有限立体角的逐rank response，不由polarimeterQ补齐 |
| F与ε | 单次接受计数或绝对效率的分母需声明 | Eq18用photopeak ε，传统Eq11用coincidence ε | 曝光/入射或发射光子、deadtime和背景；裸F不提供beamtime排名 |

ST99 Table1 的 Ba参考P由上游AD而来，Cd/Sn CE参考P由GOSIA而来；这些不是本篇独立直接测到的P。SG98同一calibration的A/P/Q三列不是三个独立实验。ST99的10⁻5指数/脚注勘误和SG98的294-keV印刷closure边界仍按原source保留，本设计没有修复它们。

## Provisional Reasoning

### 两个估计量的Jacobian

令 clover 的 x=N⊥、y=N∥、D=ax+y：

\[
\partial_x A=\frac{2ay}{D^2},\qquad
\partial_y A=-\frac{2ax}{D^2},\qquad
\partial_a A=\frac{2xy}{D^2}.
\]

SG98令 n=C+S：

\[
\partial_C A=\frac{(1+\eta)S}{\sqrt\eta n^2},\quad
\partial_S A=-\frac{(1+\eta)C}{\sqrt\eta n^2},\quad
\partial_\eta A=\frac{\eta C+S}{2\eta^{3/2}n}.
\]

对任意真实Σ，先用gᵀΣg传播。以下数字只用事先声明的独立Poisson原始类别计数和独立P_r局部误差；不把源Table3的拟峰误差改成√面积。ST99与SG98的两个分母不同，不能共用一套导数。

## 共同校准如何进入参考比值

只有在同一可适用的Q及匹配物理P下，才能写

\[
Q=\frac{A_r(h)}{P_r},\qquad
P_t=P_r\frac{A_t(h)}{A_r(h)},\quad h=a\ \text{或}\ \eta.
\]

对SG98，参考/目标使用同一η时，√η相消：

\[
P_t=P_r\frac{(\eta C_t-S_t)(C_r+S_r)}
{(\eta C_r-S_r)(C_t+S_t)}.
\]

在A_t/A_r非零的局部区域，

\[
\partial_\eta\log(P_t/P_r)=
\frac{C_t}{\eta C_t-S_t}-\frac{C_r}{\eta C_r-S_r}.
\]

因此共同η误差既不是自动完全抵消，也不是两个独立标定误差；只有额外的相同计数比条件才局部抵消。目标A_t=0时用未除A_t的Jacobian，不套对数式。

等价的A_t/Q传播是

\[
\operatorname{Var}(P_t)=\frac{\operatorname{Var}(A_t)}{Q^2}
+\frac{A_t^2\operatorname{Var}(Q)}{Q^4}
-\frac{2A_t\operatorname{Cov}(A_t,Q)}{Q^3}.
\]

这里Cov(A_t,Q)即使target与reference采集独立也可能因共享U校准而非零。其符号和影响依实际设计；以下正Cov例不证明省略它总会保守，也不补出真实实验Σ。A_r除以它自己回代P_r是恒等式，不能当独立验证。

## 声明设计的计数与定量结果

表中为本session新声明的Poisson均值，非源实验counts；每行内先后类别按表头，P_r也为设计值，不假称一条实际reference。

| 设计 | 无偏振U两类别 | 参考r两类别/P_r | 目标t两类别 | h；A_r；A_t；Q |
| --- | --- | --- | --- | --- |
| clover：⊥、∥ | 500000、500000 | 55000、45000；.5±.01 | 53000、47000 | 1；.10；.06；.20 |
| SG98：C、S | 1000000、160000 | 101600、14400；.8±.012 | 100600、15400 | .16；.04；.015；.05 |

原始六counts/P_r的联合Jacobian给出：

| 设计 | P_t及联合local σ | 错把A_t、Q独立的σ | 新120000次Poisson设计MC的σ |
| --- | --- | --- | --- |
| clover | .300000±.0194486 | .0201951 | .0195646 |
| SG98 | .300000±.0627474 | .0646613 | .0634302 |

clover的variance分量依target/reference/U/P_r为.00024910/.00008910/.00000404814/.000036；SG98依次为.00333887931/.00044340517/.00013469828/.00002025。数字是chosen设计的一阶传播，不是实验confidence interval或detector排名；两个设计的counts/参考P并不等价。

独立推导的条件binomial likelihood使用

\[
p_\perp(A,a)=\frac{1+A}{a(1-A)+1+A},\qquad
p_C(A,\eta)=\frac{1+\sqrt\eta A}{1+\eta},
\]

对参数(log h,log Q,P_t,P_r)构造Fisher矩阵，外加独立P_r约束。其逆矩阵P_t分量与原始计数delta variance一致；它是同一设计的另一数学核验，不是新独立实验。MC有限样本平均轻微比值bias分别为.01483σ/.01248σ，未证明有限样本比值无偏。零/近零A_r、负净峰和有背景问题需要真实likelihood，不能靠本地Gaussian式裁剪。

## 改分母后重标一条线仍会失败

若把SG98改成

\[
B=\frac{\eta C-S}{\eta C+S},
\]

根据原式与C+S守恒，有

\[
B=\frac{(1+\eta)A}{2\sqrt\eta+(\eta-1)A}
=\frac{(1+\eta)QP}{2\sqrt\eta+(\eta-1)QP}.
\]

除η=1或只取局部小A极限，这不是一个与P无关的常数乘P。所以上面的SG98设计用旧Q会得到P_t=.441961；即使用B_r/P_r重新标一条reference，仍得到.291999而非设计真值.300000。这是响应合同被改变的明确反例，不是SG98实验结果失效或新Q校准。

在承认这个非线性forward model后可以用B反演P；问题在于沿用线性A=QP。未来若以新的估计量分析实验，必须同时更新完整forward response和误差模型，不能仅更换分母/参考一点。

## 效率分母、必要companion和失败条件

SG98-14的原文字典需带到任何F比较：printed100 Eq13将N写成source总发射光子，而printed101 Eq18邻文将N_i称incident photons，ε写成photopeak efficiency。必须显式提供N_emitted→N_incident的几何接受/照射定义，或声明incident指整个装置的归一；本文未给可替用户恢复该字典的独立N ledger。不能混用每次入射晶体的本征效率、每发射光子的绝对效率、相对NaI效率和选中photopeak条件概率。纯粹把分母改名不改变观测counts，但改变了F比较的意义。

最小独立校准输入是一条**没有参与Q拟合的、已知P的检查支路**，其方向、布居/门、能量/阈值、background与arrayselection均有可追溯匹配；如P不是直接测量而来自AD/GOSIA，须另带相应误差和模型边界。增加一条同Q拟合内参考的回代点不足以填此缺口。

另需原始U、r、t峰/背景和event-overlap ledger：共享拟合、插值η(E)、多个参考能量的共同参数、P_r的AD校准依赖、gate/finiteacceptance变化均可破坏当前独立Poisson假设。原SG98 Fig9为130keV threshold而Fig10/Pb为60keV；ST99单clover79°校准不是任意EUROGAM/gate的完整响应。这些都必须回原数据，而不是从设计MC估计实际systematics。

反证一是ST99-2的490-keV E2/M1-E2仍多解，说明P/DCO并不保证唯一Jπ；反证二是SG98-9/12的高背景P散布和ADcompanion，说明更多acceptedcounts不自动提高真实结论可信度。P/A号不能独断δ、宇称或shears/wobbling解释。

## Assumptions

定量练习限定单一能量、匹配的阈值/geometry/gates/arrayselection和可共用的线性Q。六primitive类别计数独立Poisson、无背景和事件复用；P_ref具有独立的局部Gaussian误差。这些是设计假设，不是原两篇实验已经满足的已知事实。

## Competing Explanations

真实P变化、未分峰/背景拟合、逐探测器权重变化、阈值/geometry变化和共同校准可造成不同A。当前设计仅隔离最后一项和估计量归一；未用它排除其它解释，也未解释实际294-keV或490-keV未决项。

## Transfer Conditions

迁移前提供明确物理P坐标/自旋与参考身份，及同对象energy/threshold/gate/geometry/arrayweights。若能量不同，Q(E)、a(E)/η(E)插值的共同参数/Σ必须显式提供；不能仅同仪器名称便采用本设计一个Q。

## Failure Conditions

近零参考A、负净峰、未给background/event-overlap Σ、偏振相关总接受度或不同参考/target选择，都会使当前比值与误差近似失去保证。√η取消不认证剩余η取消；不对物理区间外估计作clip或擅加伪计数。

## Falsification or Reverse Tests

完整primitive Jacobian与条件binomial Fisher给同一local variance，MC核有限样本sigma/bias；改分母的非线性公式给明确反例。真正实验验证必须另留未参与Q拟合的known-P支路；与同reference恒等回代不同。

## Open Questions

当前缺真实逐detector/gate的U、reference、target净峰/背景ledger与Σ，以及Q/P_ref/AD的共同依赖。合并detector的a/η/Q迁移条件已在下方新段以原合同和Rational设计明确；实际逐台/gate ledger仍缺，下一核公开producer输入，不用更多同模型MC代替它。

## Human Review

本页为Codex self-audit，未发生用户科学审核；`review_status: unreviewed`。本session的继续/自动执行授权不等于逐claim确认。

## Promotion or Rejection History

- 2026-10-19：从Day17原件阅读与新联合计数设计创建；保持provisional。未晋升为任一实际实验结论，未改原source review flags。

## 可复算与self-audit

输入[paq-design-input.json](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/paq-design-input.json)、[脚本](../../system/scripts/day17_paq_shared_calibration.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/paq-shared-calibration-result.json)保存设计参数、原件hash、全Jacobian/Σ、Fisher和MC。命令：

```bash
PYTHONPATH=/workspace/wiki/tmp/day16-jt74/python-deps python3 system/scripts/day17_paq_shared_calibration.py
```

依赖NumPy/SymPy；该路径是现有repo内依赖缓存，未修改系统配置。首次两个interpreter均缺SymPy的实际失败见同run的`first-execution-failure.json`；不能称首次执行即成功。缓存可重建，核心公式/输入/代码已在持久层；脚本不重放Day16的旧检查。

P1 self-audit：`supports`直接从primitive counts保留共同校准；`revises`只要重标一点就可随便更换A归一的直觉；`limits`F或√count对高背景实际P精度的保证。新分析均为`our-inference`/声明模型、`source_independence: multiple-dependent`、`needs_review: true`；没有新增实验δ/Jπ/P/Q或human-review。晋升待实际matching-response/Σ输入。

## 探测器合并：匹配零点仍不保证一个线性Q

ST99-7/15原printed21/Fig2给所选18台单台a∈[.95,1.05]、合并a∈[.99,1.01]且取a=1；SG98-4/15原Eq13和printed106给12台C/S合并。下面是分析前另冻问题后完成的**声明response模型**，没有原逐台illumination、Q或Σ，不能当原阵列发生偏差的证据。共同物理P（同一偏振坐标、兼容方向和gate）是额外假设；一般array的P_j不同须逐台forward model，不适用以下单P缩写。

### Clover：原始垂直效率权重下的精确合并

取X_j=ℓ_j e⊥,j(1+Q_jP)、Y_j=ℓ_j e∥,j(1−Q_jP)，a_j=e∥,j/e⊥,j。定义w_j∝ℓ_j e⊥,j，归一Σw_j=1；它是**无偏振perpendicular基线权重**，不是总accepted counts或γ强度Iγ。令ā=〈a〉、q̄=〈Q〉、c=Cov_w(a,Q)。若U、reference和target均匹配这个w，合并U给a_U=ā，直接合并原始计数再校正得到

\[
A_{\rm pool}(P)=\frac{kP}{1+\lambda P},\qquad
k=\bar Q+\frac{c}{2\bar a},\qquad
\lambda=-\frac{c}{2\bar a}.
\]

即使A_pool(0)=0，也不保证A_pool/P为常数。若各a相同、各Q相同，或恰好c=0，则恢复线性；这是可检验的充分条件，不是原论文已测c=0。用单一P_r标Q_r=A_pool(P_r)/P_r后，

\[
\widehat P_t=P_t\frac{1+\lambda P_r}{1+\lambda P_t}.
\]

在共同w、a与Q的范围及单P假设成立时，Cauchy–Schwarz与有界变量方差给出Grüss界：c的绝对值不超过(a_max−a_min)(Q_max−Q_min)/4。**额外取0≤Q_j≤1、ā≥.99**，源a范围条件下λ绝对值≤5/396≈.0126263；对P_t、P_r∈[−1,1]且参考非零/response非零，单参考非线性引起的P绝对偏差≤10/391≈.0255754。这是保守数学界，不是实验systematic σ、置信区间或完整calibration预算；若权重不匹配，该界不约束总偏差。

若target为P=0但w_t与U不同，其a_eff仍只是a_j的凸平均，原a_U∈[.99,1.01]和a_eff∈[.95,1.05]给

\[
-1/34\ \le A_{\rm false}(0)=\frac{a_U-a_{\rm eff}}{a_U+a_{\rm eff}}\le3/98.
\]

因此在这些**无背景/同a范围/同选择**前提下，单纯权重迁移不能从P=0生成ST99 printed21的A中央值+.120；它不排其它systematics，不计算实验概率，也不选490-keV的δ分支。

新两台design取a=(.95,1.05)、Q=(.10,.30)、w_U=w_r=(.5,.5)，有ā=1、c=.005、k=.2025、λ=−.0025。P_r=.8、P_t=.3时，matching-w的一点标定给P̂=.2996247；若仅target改w_t=(.9,.1)，P̂=.2792313；此选择的无偏振target也会给A=.0204082，沿Q_r得apparentP=.1005795。数字不是原18台的数据或实际偏差估计。

### SG98：photopeak权重下的线性与offset

每台依Eq13取总photopeak均值n_j对P不变，v_j=n_j/Σn_j；

\[
\frac{C_j}{n_j}=\frac{1+\sqrt{\eta_j}Q_jP}{1+\eta_j},\qquad
S_j=n_j-C_j.
\]

令c0(v)=Σv_j/(1+η_j)、d(v)=Σv_j√η_jQ_j/(1+η_j)。匹配U权重v_u时η_U=[1−c0(v_u)]/c0(v_u)，**不是**η_j的算术平均。用这个η_U处理target，

\[
A_t(P)=\frac{(1+\eta_U)c0(v_t)-1}{\sqrt{\eta_U}}
+\frac{(1+\eta_U)d(v_t)}{\sqrt{\eta_U}}P.
\]

若v_t=v_u，则offset为0且响应严格线性；若权重变，offset通常不为0，同时斜率也变。只校Q不能消除offset。不同物理P_j、偏振相关totalacceptance或不同threshold需要完整response，不能从该式自动认证。

新design取η=(.09,.25)、Q=(.04,.06)、v_u=v_r=(.5,.5)，有η_U=77/468≈.1645299而算术均值为.17，Q_eff≈.0502551。匹配v时reference P_r=.8与target P_t=.3准确回到.3；target改v_t=(.8,.2)则P̂≈2.24579，P=0也给apparentP≈2.01258。所有逐台类别均非负；这些越界估计揭示错误迁移的设计反例，不能clip成物理P=1或称源197Pb结果失效。

### 本问题的核验、复用与停止边界

[array-weight-input.json](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/array-weight-input.json)、[exact script](../../system/scripts/day17_paq_array_weight_contract.py)、[result](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/array-weight-result.json)保存Rational输入、直接逐台求和与闭式恒等式、P∈{−1,−.5,0,.3,.8,1}的正计数/逐台校正恢复控制。没有额外MC或实际事件；新分析与先前计数MC不计作独立实验。

此代数局部已解决“合并null接近1是否足够”的问题。真正提高原实验判断信息的下一输入是逐detector/gate的基线权重、参考/target共同坐标及Q_j/η_j、背景/Σ/producer。取得这些输入前，不继续扫同一toy或把条件上界当实测校正；可转向实际公开sorting/producer的readiness核验。

### 实际公开producer的后续输入门

[[grsisort-2026-compton-polarimetry-code]] GRS26-1–10已按固定commit/双hash核所选原件并执行原样组件。取得了Compton双hit/第三γ、ξ/θ、10-history mixed和归一consumer的实际路径，但没有真实ROOT/TTree、逐detector reference/targetledger与Σ。源newAnalyze/默认Lean并非同一path；已复现的index/secondF/normalizederror/bin边界需按该版本限定，不外推原ST99/SG98。

当前缺口已从“是否有公开producer”收窄为“能否取得matching actualdata/执行版本和统计结构”。下一个有信息增益的动作是检验对应构建路径、实际settings与输入basis或合法公开数据入口；不是再用合并权重toy取代真实证据。

### Q(E)角色与接受权重不能被一个同能量点认证

GRS26-11/12追加核原样完整ScalePlot程序：原函数calibration→target角色与plot循环传参反向；1332→1332的回代会掩盖反转，旧Lean正向调用是版本反证。源码均匀θ的单次Σ平均与KN×dΩ加权也不同；E→0分别√2−1和1/2、point90为1。该数学/程序结果说明Q必须连同role、平均kernel与经验半因子定义保存，不将一个理想平均或代码comment Q=.2509认成matching实验response。

### 原装置校准对当前推理的约束

[[garnsworthy-2019-griffin-facility]] GF19-6–14在完整原件后提供实际Q(.240±.012 at1332)、明确.5QPcos2ξ/90°cloverpair与68–113°crystal角组、三其它能量检查和同207Bi双角色。[[triumf-griffin-compton-source-calibration]]是测量/来源ledger；本note的sharedCov/array反例仍是声明模型，不能称paper实际失败。

源数据对当前generic正向ScaleQ作条件比较给570/1173/1771约.378202/.259795/.198649；源reported为.390/.258/.201，anchor共同误差的rank1项需保留，但actualcrossCov/fitΣ不足以报新置信度。Table7的ICC/summing真实摘要重算另显示photon/total分母的重要性；这些新summary-check不增加独立实验数或替代rawresponse。

### 官方207Pb参考的派生归一与概率门

[[nndc-2011-pb207-bi207-polarization-reference]] N207-1–11用真实selected官方对象核1064/570 roles：MR+.02(.01)/blank不同，EC photonRI/experimentalICC与Adopted theoreticalICC不同。RI570=(100−.131)/(1+α570)直接暴露RI–α依赖；在明确独立bypass/α的设计极限，totalσ的α项抵消而不是重复相加。条件pair emission≈.72918不等marginalRI乘积或detectorε，MR强度份额.0004也不等实际P误差界。这一来源相邻的真实输入审计收紧calibration readiness，原primaryphase/完整Σ仍缺，未造新实验P或CI。

### 另一种P不能混入本表

[[schuermann-2008-15o-6792-dsam]] SCH08-5的P=.987是有限Ge尺寸的Doppler修正，乘在β0Fcosθ前；它不是本表physicallinearP、a/η或ComptonQ。SCH08-11的actualcenter映射P×F=.97713只检验其F分母，不能当polarimetry校准或从DSAM曲线给γ的linearP。

## 真实工具合同补充：平滑与匹配不自动进入Cov

[[root-2008-v522-background-error-contract]] R522-2/3/5/10是本note计数设计的实际软件反证：ROOT5.22 Smooth只改content，Background未写估计误差，Add按固定系数diagonal合并。声明matching a=Dk/Bk给不同jointCov；原Compton/Si实验脚本未得时不把本design或工具名升级为实验置信区间。


## 三GeLi原计数式与独立校准层

[[butler-1973-three-geli-compton-polarimeter]] B73-D17-1/2/6/11/12把a相对absorbereff、A校正sumpeakarea、P核光子planeaxis、Q=A/P分层固定。旧Wiki额外1−alphaA分母是转录错已纠；source原Eq4只P=A/Q。新design6000/4000、a1.01的Jacobian/误差保自设Poisson及a独立条件；实际B73counts/背景fit与跨线Cov未取得，不能用印a1%或Qcurve方差当实验jointΣ。

Table1七个Q都是AD预测P和同测A派生；unpolarized56Co/66Ga的a才是另一相对effinput，且仍需samegeometry/selection。Ex2935/Eg967别与同母态groundγ2935混用；nominalpointP>1不clip，不以失配强改authorP/Q。


## 独立装置的null与分析能力分层

[[twin-1970-polarization-angular-correlation-40k]] TW70-D17-1–5的θ0null只relativeeff，R为另一有限geometry/knownAr1460检查；Comptonψ82不能当emissionθ。原R.21(.02)归2231γ，1.5MeV只有验证对象。与B73不同独立dataset仍共理论祖先；pointKN82/90结果不替actualresponse或跨装置factor，原counts/共同Cov未得。
