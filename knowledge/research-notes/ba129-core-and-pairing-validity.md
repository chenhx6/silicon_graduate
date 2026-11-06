---
type: research-note
title: "129Ba：核芯约束与配对近似的有效性反检验"
aliases: [Ba129 core and pairing validity, Ba129 controlled pairing]
created: 2026-11-05
updated: 2026-11-06
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [nndc-ba128-ba130-core-ba131-transfer, konigshofen-2001-mixing-ratios-130ba, book-greiner-nuclear-models, meyer-ter-vehn-1975-triaxial-rotor-particle-model, nomura-2017-odd-mass-gamma-soft-shape-transitions, klein-2000-v1-number-conserving-foundations, protopapas-klein-1997-core-particle-approximation]
created_from: "A130 goal: controls following the published Ba129 observable checkpoint"
promotion_target: "Physically controlled same-wavefunction test; no novelty admission yet"
nuclei: [128ba, 129ba, 130ba, 131ba]
tags: [a130, model-validity, pairing, core-constraint, rigid-rotor, em-operator]
---

# 能谱最优点还需要通过什么检查

## Research Trigger

[[ba129-model-input-and-holdout-contract]]的能量定标给出明显不同的分支预测，
而最佳自由惯量点的舍弃耦合尚不够小。本轮分别核查完整矩阵的态选择、
邻偶核输入和低自旋E2算符，先判断哪些比较有物理含义。

## Grounded Evidence

[[nndc-ba128-ba130-core-ba131-transfer]]保存实际版本、字段和locator。
Greiner–Maruhn原书本轮只核printed pp.145–150（物理PDF164–169）的选段，
不是重新声称完成全书阅读；§6.4.3 Eqs.6.169–6.174给对称化基和三态关系。
Königshofen2001 TableI前两行重新视觉核对。

| 核素/输入 | 实际数据 | 本轮用途 |
| --- | --- | --- |
| 128Ba | E(2_1)=284.00，E(2_2)=884.50，E(3_1)=1324.37 keV | 检查恒定惯量核芯 |
| 130Ba | E(2_1)=357.38，E(2_2)=908.02，E(3候选)=1361.06 keV | 同上，保留3(+)指定 |
| 130Ba光子分支 | 907.7/550.5光子比0.74(2)，后者δ=−75(20)；表中B比0.061(2) | E2算符比较；三者有派生依赖 |
| 130Ba静态量 | B(E2)↑=1.163(11)e²b²，g=0.35(3)，Q两支−1.02(16)/−0.09(16)eb | 可约束尺度，不能隐去Q分支 |
| 130Ba(d,p)131Ba | 当前2006评价对象无明确l=5强度 | 暂无可直接用于同j加/移除联合拟合的输入 |

## Provisional Reasoning

### 恒定惯量的反检验不需要先选γ

定义\(A_k=\hbar^2/(2\mathcal J_k)>0\)。在归一化D₂的I=2基
\(\{|K=0\rangle,(|2\rangle+|-2\rangle)/\sqrt2\}\)中，
\[
H_2=\begin{pmatrix}
3(A_1+A_2)&\sqrt3(A_1-A_2)\\
\sqrt3(A_1-A_2)&A_1+A_2+4A_3
\end{pmatrix}.
\]
I=3只剩K=2反对称组合，故
\[
E(3)=4\sum_k A_k=\operatorname{Tr}H_2=E(2_1)+E(2_2).
\]
这在任意三个固定正惯量下成立，不依赖irrotational处方。
实际\(E(3)-E(2_1)-E(2_2)\)为128Ba的155.87 keV、130Ba的95.66 keV。
即便三个能量等权自由调整，任何满足该平面的模型对三点的RMS也至少为
51.96、31.89 keV。这是几何距离下界，不是实验χ²或显著性。

固定惯量和这组态对应不能精确描述这些中心值；这不唯一证明γ软度，
也不排除自旋依赖惯量、振转耦合、形状极化或其它有效模型。

### E2分支相近不关闭能谱反例

进一步限定\(\mathcal J_k\propto\sin^2(\gamma-2\pi k/3)\)，
以及同一形状的集体E2张量。设
\(s=\sin^2(3\gamma),\ d=9-8s,\ a=(3-2s)/\sqrt d\)，
标准D₂基和CG张量积分给
\[
\frac{B(E2;2_2\to0)}{B(E2;2_2\to2_1)}
=\frac7{20}\frac{d-(3-2s)\sqrt d}{s},
\]
\[
\frac{B(E2;2_2\to0)}{B(E2;2_1\to0)}
=\frac{1-a}{1+a},\qquad
\frac{B(E2;2_2\to2_1)}{B(E2;2_1\to0)}
=\frac{20s}{7[d+(3-2s)\sqrt d]}.
\]
这些E2式是本任务的矩阵推导/复算，不声称Greiner §6.4.3印有它们。
第一比值在\(\gamma\to0\)的极限为7/10，在30°为0；
30°时第二比值也为0，第三比值为10/7。不能用旧的
\((20/7)s/(9-8s)\)、其另加根号分母的版本或30°时7/40的说法。
它们不满足这组明确算符的极限检查。

只用130Ba两2+能量，irrotational模型坐标为24.247°或35.753°。
由其预测第一B比0.06483，而Königshofen表中为0.061(2)；
用同一表的光子比及δ重算为0.06073。后一数与表中B比有共同输入，
不是独立测量。这一局部分支接近并未消除上面的95.66-keV三态失配。
因此24.247°不是已测得的静态γ，亦非完整核芯模型认证。
相同条件还预测130Ba的R4/2=2.88024，而评价值为2.52350；
128Ba对应3.02333对2.68775。该额外能量控制同样不支持由局部分支接近
宣布整个刚性模型成立。

能量使用2001 ENSDF版本，分支使用2001原实验印刷值；两者的能量末位不同，
按态标签及衰变拓扑对应并分别保存，没有混成统一协方差或新评价。

### BCS标签、物理空穴和能量正负不能混用

指定矩阵中
\[
H(t)=\begin{pmatrix}A+E&tK\\tK^\dagger&A-E\end{pmatrix},
\quad K=-UH_RV+VH_RU,\quad E>0.
\]
“+/-”是BCS坐标扇区。A≥0并不保证A−E<0，不能筛选所有总能量为正的
本征值作为物理态。冻结最佳参数的I=11/2块维数为72，其中正本征值数
从t=0的42变为t=1的41，而原H+只有36态；能量零点平移也会改变该计数。

原文Meyer-ter-Vehn1975 p.118的Eq.2.31写\(h\xi\pm e_\nu\)，把minus集合称
rotor-plus-hole，Eq.2.32又写particle/reflected-hole等谱。
直接把这些字面标签当作本A±E是不相容的：
对本规范的反射有A′∼A、E′∼E，所以
\(\operatorname{Tr}H_+-\operatorname{Tr}H_-^\prime=2\operatorname{Tr}E>0\)。
减去标量参考能一般也不能使两组完整相对谱相同。
这是原式标签/约定的待解问题，可能涉及排印或术语；没有原程序或可靠勘误，
不替作者指定修正。正能准粒子通过v占据变得hole-like，不等于进入负BCS扇区。

完整矩阵重建恢复一个已显示的耦合项，尚未加入blocking、多j、三准粒子或
形状涨落。沿t从H+态追踪可定义数学参考，但仍需谱隙、网格与逆向检验；
原文未给出将此路径认证为物理一准粒子空间的规则。

本轮已在三组冻结能量参数下完成30个指定态的K(t)路径。
自适应细化后，前向/网格/谱隙/逆向检查均通过；28态通过全部数值控制。
最佳C≤120点的19/2态对仍按共同规则保留标记：局部约0.8-eV避免交叉处，
加100-MeV公共参考后的扇区权重差\(5.74\times10^{-8}\)超过预定\(10^{-8}\)阈值。
未放宽阈值。C60解端点BCS+权重均≥0.99078，而部分C120延拓态变为
BCS−主导。它们仍是数学参考，不是物理“空穴态”判定或修正后实验能谱。

[[protopapas-klein-1997-core-particle-approximation]]的既有处方开启的是
共轭对称/芯激发部分，起点与本固定转子K(t)不同。
[[klein-2000-v1-number-conserving-foundations]]还要求CFP、两邻偶核、
轨道归一与数目约束；不能用一组归一化Nambu向量自动替代。
其v1附录的若干迭代式有字面矩阵反例，未据此编写新的物理解筛选器。

### 单j IBFM：可以重建的部分与实际失败

[[nomura-2017-odd-mass-gamma-soft-shape-transitions]] TablesI/III/V及
p.8明确135Ba→134Ba芯的例子，共同支持129Ba→128Ba的A−1重建。
常规计数给NB=3个质子粒子对+5个中子空穴对=8；这是有来源支持的推定，
不是已恢复的作者输入卡。130Ba/NB7是另一参考，不能只换数字而沿用粒子解释。

本次固定输入为
\[
(\epsilon_d,\kappa,\chi_H)=(0.03,-0.102,-0.18),\quad
v_h^2=0.453,\quad(\Gamma_0,\Lambda_0,A_0)=(0.6,2.1,-0.15).
\]
能量参数单位MeV。模型与正规排序见[[single-j-interacting-boson-fermion-model]]。
E2采用原文\(\chi'=+0.35,\ e_F=0.125\,eb\)，eB由128Ba首2+的
T1/2=105(9)ps、Eγ=284.10keV和α=0.0539定标：本任务转换
B(E2;2→0)=0.276525 e²b²，eB=0.132680 eb。此转换不是新测量。
未知gB由原有一组光子比约束共同磁尺度，未擅自取Z/A。

独立矢量图核查显示，计算的五个128Ba核芯理论能级与Fig.3(a)图点差≤0.365keV，
六个129Ba最低负宇称理论点与Fig.5(c)差≤0.721keV。原图点近似整数keV；
15/2点超出假定的±0.5-keV最近舍入区间。因此称“约1keV内的已展示谱子集重建”，
不称精确PBOS复现，也不把绘图精度当理论或实验误差。

未重新拟合的十态合同（九个相对残差）给RMS=482.605keV。
主要偏差在未展示于该原图的第二组13/2、15/2、17/2、19/2态：
分别高468.684、709.036、550.942、1006.768keV。
五个未用于尺度定标的光子比也没有同时再现：

| γ对/keV | 本任务强度检验值 | 1992/2014中心比 |
| --- | ---: | ---: |
| 364.7/461.6 | 0.457595 | 3.936364 |
| 604.7/701.3 | 2.774548 | 0.608333 |
| 521.0/674.8 | 0.099940 | 1.060976 |
| 157.0/678.0 | 0.027343 | 0.066583 |
| 526.6/634.9 | 2.393510 | 0.928571 |

604.7/701.3的E2项本身为1.632997，非负M1不能降到观测中心比。
157-keV对在模型中甚至反序，模型母末态差为−121.330keV；
153.8-keV标定对的模型间隔仅19.013keV。
因此上述表严格是**使用实验相空间的波函数强度检验**，不是自洽预测的放光谱。
失败不能自动排除整个IBFM族；它表明该冻结重建不足以承担本例模式裁决。

原文的eB、gB逐核值和完整EM输出未公开，能谱重建也不自动认证这些量。
初步按字面E2算符复算的形状诊断与原文部分图仍未对上，
后续应分开处理算符字典和非零自旋求和问题，不凭谱图相近宣布全部复现。

## Assumptions

核芯态标签按来源保留；上述能量关系假定对应同一个常惯量D₂转子。
E2公式额外假定irrotational惯量与集体电荷形状共用γ。
静态Q的两个重取向分支均保留，Coulomb由B(E2)导出的寿命不重复计数。
完整配对矩阵的后续计算只命名为“H+连接的数学参考”，直到物理态合同闭合。

## Competing Explanations

γ软核、振转耦合、核芯极化、有效算符和多轨道成分都可能改变联合预测。
[[nomura-2017-odd-mass-gamma-soft-shape-transitions]]已经提供微观输入的IBFM先例；
其具体核芯/玻色子数及标定谱系须核清后再作数值比较。

## Transfer Conditions

P131未给l=5不代表h11/2加中子强度为零。更不能把129Ba移除与131Ba加粒子
当作同一末核的两次测量，或把全数学空间的U/V求和强加给不完整实验窗口。

## Failure Conditions

若路径选择依赖能量零点、任意tie-break或未收敛步长，不报告唯一的延拓态。
若用保留EM重新调整尺度/对应/耦合，必须登记为重新标定。
常惯量核芯失败或原文标签歧义均不自动成为文章创新。

## Falsification or Reverse Tests

`system/scripts/ba129_core_constraints.py`从有哈希的ENSDF字段重建以上数值；
64组正惯量验证迹关系与I=2解析谱，CG矩阵E2比对解析式、0→2闭合与两个极限。
`paired_single_j_nambu.py`另外验证完整变换、t端点、C=0及对偶协变。
延拓、IBFM输入/图点审查和结果回执在`outputs/l4/20261105-ba129-controlled-pairing/`。
IBFM核通过25项解析/合成检查，Nambu核通过19项检查；
仍未据此进行新的Hamiltonian参数拟合或论文模式裁决。

## Open Questions

原文plus/minus标签能否由作者后续文献或程序消歧？完整矩阵的有效物理空间
如何与固定粒子数/偶芯对应？采用受来源约束的软核芯后，129Ba未标定分支的
预测是否稳定？这些问题尚未由本轮两个局部控制解决。

## Human Review

Codex来源与公式self-audit；未作human-reviewed标记。

## Promotion or Rejection History

- 2026-11-05：将核芯谱关系、E2极限修正、加中子资料缺口及Nambu态选择边界写回；
  坚持单点论文目标，暂不提升任何一个局部控制为新物理主张。
- 2026-11-06：补入完整有界延拓、数守恒来源边界和实际IBFM重建；公开能谱子集
  相符与未标定观测量失败分别保存。新增形状不变量线索先做定义/先例审核，
  没有改写为已成立的新颖性结论。
