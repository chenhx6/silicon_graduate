---
type: method
title: "组态列示的占据数与完整性审计"
aliases: [configuration occupation audit, 组态占据数审计]
created: 2026-10-15
updated: 2026-10-15
status: ai-draft
review_status: unreviewed
method_type: theoretical-model-input-audit
tags: [configuration, particle-number, number-parity, pairing, input-contract]
---

# 组态列示的占据数与完整性审计

## Purpose

把论文的valence、unpaired、active configuration标签与可重放的完整occupied/blocked输入分开。先检查必要的粒子数/奇偶条件，再讨论模型能否解释谱；不从一个标签的缺项断言实际代码错误。

## Inputs and Assumptions

实际示例来自[[lv-2025-136pr-tac-covariant-density-functional]] LV25-32，acceptedPDF15 TableII十行，以及PDF11 Figs9/10captions。原始列和Ω近似标签均保留，不将未列轨道写成测得零。为valence记账选Zcore50、Ncore82，目标Z59、N77；这验证该常见reference下的净9protons/−5neutrons，不认证作者实际HFBreference/blockedlist。

更强的检查只在**unpaired列代表偶pairedreference上全部pair-reduced inventory**时适用。若列仅列activealigning部分，或reference/旁观者另有奇核子，此假设不成立，需补定义而不是补写轨道。

## What It Can Establish

- 对列示signedpowers求和，检查给定reference下的Z/N记账；hole负号必须保留。
- 检查把列当完整输入时的必要number-parity条件；fail可限制这种解释，pass不是wavefunction有效证明。
- 分开spatialparity标签乘积、speciesnumberparity、total-I整数/半整数sector和未投影的meanI。

## What It Cannot Establish Alone

不能恢复实际blocking、spectator、mixing coefficients、pairing或code行为；不能据TableII判断TAC程序错，不能把β/γ/tilt升级为测量，也不决定Q1实际π。没有原occupied/blocked数据，不进行实际模型复跑或新实验L4。

## 完整pair-reduced解释的必要条件

令v_s和u_s分别为species s的valence列与unpaired列的**列示signedpower sum**。若两者只差额外**like-particle** pairedparticles/holes，则每species必有

`v_s−u_s=2 k_s`，`k_s∈Z`。

这是like-particle配对下的必要条件，不需要知道pair数；同species pair改变该species粒子数偶数。允许proton-neutron pairing时，单独species差可为奇数，普适必要条件改为`(vp−up)+(vn−un)`为偶数；任何two-fermion pair都保留总fermionnumberparity。不能将逐species规则无条件用于pn配对。负holepower与对应绝对holecount在mod2上相同。满足此式仍不认证orbitalcapacity、antisymmetry、blocking或实际wavefunction。

对标准good-parity orbital标签，另可算label spatialparity：g/d/s取+，h/f取−，oddpower才影响乘积。这与numberparity是不同检查。若完整unpaired列表含奇数个半整数fermions、reference为偶pairedbackground，其projected物理sector是半整数I；这**不**要求未投影TAC的meanI必须是整数，也不说明作者实际reference符合此前提。

## 136Pr TableII的条件审计

所有十行valence都给(vp,vn)=(9,−5)，基本Z/N记账通过；包括Q1*、Q2*的备选和Q3/Q4共同配置，不是十条独立新band。unpaired列的列示和如下：

| TableII row | listed(up,un) | listed绝对particle/hole项数 | v−u | 完整列+仅paired补全的必要条件 |
| --- | --- | ---: | --- | --- |
| D1 | (1,−1) | 2 | (8,−4) | pass，非充分证明 |
| D2 | (3,−1) | 4 | (6,−4) | pass，非充分证明 |
| D3 | (5,−1) | 6 | (4,−4) | pass，非充分证明 |
| D4 | (3,−5) | 8 | (6,0) | pass，非充分证明 |
| D6 | (3,−5) | 8 | (6,0) | pass，非充分证明 |
| Q1 | (3,0) | 5 | (6,−5) | fail此完整解释 |
| Q1* | (3,0) | 5 | (6,−5) | fail此完整解释 |
| Q2 | (3,−1) | 6 | (6,−4) | pass，非充分证明 |
| Q2* | (3,−1) | 6 | (6,−4) | pass，非充分证明 |
| Q3Q4 | (3,−3) | 6 | (6,−2) | pass，非充分证明 |

本例Q1/Q1* residual=(6,−5)，**总差1也为奇数**，所以即便允许pn pairs，也不能仅靠two-fermion pairs补齐这一完整列读法；不依赖更强的like-particle限制。

Q1/Q1*的valence neutron列含sd^-3、h11/2^-3与一个h9/2或f7/2 particle；unpaired列只印h11/2^-1与intruder^1，sd在该列**未列**。两项的列示net为0，不代表测得sd占据零。只有假定该列完整时，−5 residual才排除“其余全是pairs”的解释。一个未列奇number-parity贡献或不同reference可以改变必要条件；当前不把它指定为某个νsd hole，更不替作者修表/改模型。

列中各组态的spatialparity标签乘积都为+，仍不能消除上述Q1 number-ledger缺口，也不是Q1实验π的独立确认。valence列本身始终满足Z/N，所以这里**没有识别到实际程序粒子数不守恒**；被限制的是仅凭unpaired标签重建完整输入的做法。

### Caption通过奇偶条件仍不认证同一blocking

Fig9 D4caption列示2个particle/hole项，而TableII unpaired列为8；Fig10 D6caption为6，TableII为8。它们各自均可通过speciesmod2必要条件，但列示的active/blocked信息不同，mod2不能判哪列是实际计算输入，也不能自动断言物理state不同或作者错。需要实际occupied/blocked轨道和reference/spectator定义。

## 期望粒子数、数目投影与奇偶性

以单species、like-particle pairedvacuum为例，本任务的示意态`(|N=76>+|N=78>)/sqrt2`有meanN=77，但只含evenN、对N77的投影为0。对该单species参考叠加同类pair项，其numberparity不变；给定blockedfermion数的奇偶决定该sector。允许pn配对时不能把这个单species结论不加条件套用，普适不变量是总fermionnumberparity。未实施particle-numberprojection不自动取消这个性质，投影也不能从错误奇偶sector创造目标分量。

这是条件的数学反例，不是作者态。论文未给完整reference/blockedlist，不能据此判其程序用了错误sector；可提出的输入缺口是源标签是否省略了spectator及实际投影/配对约定。参考[[a130-model-choice-card]]的模型路线边界，不能把本审计计为新PSM/TPSM投影覆盖。

## 配对方法companion不能补全实际阻塞输入

[[wang-2017-109ag-tac-separable-pairing]] W17-1、W17-3、W17-5提供直接方法校准：TAC-RHB以U/V构造密度和配对张量；不同λ/ω迭代时须追踪、阻塞准粒子轨道，且Bogoliubov态的粒子数未恢复。其109Ag的1qp/3qp简称是组态标签，完整轨道追踪仍回指上游方法。它不能给136Pr Q1/Q1*填入未列的spectator或reference，也不能据此认证TableII/实际代码。

### Spin-singlet投影不指定配对species

该文Eq.(11)的`(1−Pσ)/2`作用于两个自旋，是Hermitian、idempotent、rank1的S=0 projector。它本身不指定proton/neutron或isospin通道。按只有同类pair的构造，各species number parity固定；允许pn pair时，普适保留的是总fermion parity。不能从“S=0”直接宣称源程序包含或排除了pn pairing。

本任务用声明的四Fock modes `p↑,p↓,n↑,n↓`作控制：每species未阻塞双态为`u|0>+v|↑↓>`，阻塞态为`|↑>`。四种blocking组合逐一给出固定species parity；另构造`S†=(p↑†n↓†−p↓†n↑†)/sqrt2`和`ψ=sqrt(.6)|0>+sqrt(.4)S†|0>`，它的总parity为+1，但各species的parity期望均为.2，而非固定好量子数。`(|0>+|n↑n↓>)/sqrt2`仍有meanNn=1、Nn=1投影权重0。所有系数与状态均为本任务声明控制，不是作者波函数、实际Z/N占据或Pr136输入。

### Form factor、算符与可重放边界

W17-2的源参数`G=−738 MeV fm³, a=.636 fm`配合Eq.(12)：

`P(r)=(4πa²)^(-3/2) exp[−r²/(4a²)]`。

数值积分给`∫P d³r=1`、以P作归一权重的`∫r²P d³r=6a²=2.426976 fm²`。这是form factor形式矩，不是核内pair密度半径或实测长度。P维度fm^-3，非局域两体kernel为MeV fm^-6；配合四个归一单粒子波函数和四位置积分，矩阵元为MeV。只核这些条件不等于复现自洽RHB。

W17-9的Eq.(24)/(28)、Fig.8还要求把算符变化和态的配对变化分开。若横向磁矩由Dirac项D与anomalous项A组成，只缩放前者时强度正比`|cD+A|²`，一般不等于`c²|D+A|²`。声明控制`D=3,A=−1,c=.58`分别给.5476与1.3456；分量不是109Ag/Pr136实际值。配对改变波函数，Dirac项缩放改变算符，两者都能改变B(M1)，不能仅从曲线降低唯一识别机制。

### 公式字面异常与程序错误分开

W17-10的v2 Eq.(25)中段有μ⊥²，末项却无平方；声明分量`μx=3,μz=4,θJ=0`给中段1.909859、末项−.477465，且磁矩整体×2时分别×4/×2。这检验的是所读版本表达式不自洽，不能替作者认证或修复代码。W17-11的A18/A19在`nγ=nδ=1,N=0`时分别要求n=−2/2；需回到同一定义/正式版本，不能直接按字面生成实际矩阵元。W17-12的.87/1.26直接降幅约30.95%，保留其与“20% smaller”的差异，不改原结果。

上述练习见[day14_tac_pairing_contract.py](../../system/scripts/day14_tac_pairing_contract.py)及[50-check回执](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/tac-pairing-contract.json)。真实blocking、reference、轨道overlap追踪、pn通道和输入/输出文件仍是独立必要材料；科学未决不能由toy或源码缺项补造。

## Verification and Learning Decision

[day14_pr136_configuration_ledger.py](../../system/scripts/day14_pr136_configuration_ledger.py)完成62checks：actualPDF SHA、TableII block与Fig16legend分离、十row双列解析、Z/N/mod2/spatialparity、Q1未列sd保留None、oddabstractspectator/pairs不能修复oddresidual、captionsliteral及必要条件非充分性、toymeanN/number-sector检查。原raw、source列与review状态不改；[62-check回执](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/pr136-configuration-ledger.json)保存完整literal和未知字段。

Decision: supports基本valence记账；revises把标签当完整模型输入或把π一致当全部一致的捷径；limits完整unpaired解释。没有源程序错误判决、新实验或形状/模式结论。

## Sources

- [[lv-2025-136pr-tac-covariant-density-functional]] LV25-32：acceptedPDF15 TableII、PDF11 Figs9/10captions，数据与条件输入缺口。
- [[wang-2017-109ag-tac-separable-pairing]] W17-1–W17-13：TAC-RHB配对/阻塞方法、未恢复数目、局部失效、算符和预印本公式边界；不提供Pr136实际输入。
- [[a130-model-choice-card]]：理论路线与reproducibility边界，不增加投影论文或实验数。
