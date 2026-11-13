---
type: research-note
title: "A130壳演化研学：谱重心、单极添粒定义、冻结参考与非正交重叠"
aliases: [A130 ESPE centroids freezing and overlaps]
created: 2026-11-08
updated: 2026-11-13
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "冻结G70-v1、Terra T11原件/代数核查与总控数值重放"
promotion_target: ""
evidence_sources: [doctoral-r1-g28-otsuka-2023-type-ii-shell-evolution, doctoral-r1-g28-togashi-2016-zr-mcsm-qpt, duguet-2015-non-observable-nuclear-shell-structure]
tags: [A130, shell-evolution, ESPE, monopole, spectral-centroid, nonorthogonal-basis]
---

# 同一个“单粒子能量”，需要先问它是哪一种定义

## Research Trigger

2.2初稿把有限观测窗内单路碎片平均称为完整谱重心，
并混用了反对称两体平均、添粒有限差和冻结参考态的算符结构。
本页保存可复核的定义与模型边界；T11审计不是发表文献，冻结稿不是核物理事实源。

## Grounded Evidence

| 原件/实际版次 | T11本轮读取 | 支持内容 |
|---|---|---|
| [[doctoral-r1-g28-otsuka-2023-type-ii-shell-evolution]]，2022独立28页文章 | PDF5–8、13、15–19、25；Eqs.(5)–(8),(12)–(16)，Figs.12–15，Appendix A | 单极/ESPE定义、pn权重、参考态冻结、T-plot和谱重心关系 |
| [[doctoral-r1-g28-togashi-2016-zr-mcsm-qpt]]，arXiv1606.09056v2，5物理页 | PDF1–4；Fig.3在PDF3，说明在PDF4 | 相互作用输入、占据/ESPE模型输出、MCSM及T-plot |

Otsuka文章印刷258–285，2023只是重印；两种版式不计为两份独立理论证据。
本单元未读Baranger1970原文、实际转移反应数据或MCSM实现；
以下完整谱表达和简化数算符模型的推论明确标为任务定义/推导。
后续定向原文获取不以题录或摘要替代实读。

## Provisional Reasoning

### 1. 单路观测重心与完整加/去谱矩不同

对某反应通道、轨道和观测窗W，可以定义

$$
\bar E_{j,W}^{\mathrm{obs},+}
=\frac{\sum_{\mu\in W}C^2S_{\mu j}^{+}E_\mu^{+}}
{\sum_{\mu\in W}C^2S_{\mu j}^{+}}.
$$

这可用于描述实际观测的碎片，但不能仅因其加权就称完整Baranger重心。
若E只是残核激发能，它也不是带共同分离能零点的添粒能。
谱因子还依反应分析、角动量和简并度约定。

为作条件化对照，取同一归一化A核参考态、规范单体产生/湮灭算符，
定义 \(E_\mu^+=E_\mu^{A+1}-E^A\)、
\(E_\nu^-=E^A-E_\nu^{A-1}\)，以及
\(S_{\mu jm}^+=|\langle\Psi_\mu^{A+1}|a^\dagger_{jm}|\Psi^A\rangle|^2\)、
\(S_{\nu jm}^-=|\langle\Psi_\nu^{A-1}|a_{jm}|\Psi^A\rangle|^2\)。
本任务的完整谱重心表达为

$$
e_j^{\rm cent}=
\frac{\sum_m\left(\sum_\mu S_{\mu jm}^{+}E_\mu^+
 +\sum_\nu S_{\nu jm}^{-}E_\nu^-\right)}
{\sum_m\left(\sum_\mu S_{\mu jm}^{+}+\sum_\nu S_{\nu jm}^{-}\right)}.
$$

完整终态及相同规范空间下，反对易关系使分母为gⱼ=2j+1。
添粒/去粒强度分别对应空位和占据；需要的连续谱也在完备和内。
去粒残核的激发能在E⁻中带负号，加粒支则带正号，不能直接拼两核的激发能表。
若改用约化谱因子、有效转移算符或截断空间，应重新核权重和闭合。
此公式不宣称已核Baranger原文的逐字记号，也不把所得辅助量说成模型无关的绝对能级。

### 2. 两体平均必须和反对称基、对计数相容

下式用j简称完整单粒子轨道；只有角动量数相同而径向/轨道不同，不是同一个轨道。
对正交单粒子态α≠β，取
\(|\alpha\beta\rangle_A=a^\dagger_\alpha a^\dagger_\beta|0\rangle\)。
同种核子的单极平均应对规范反对称态求值，交换项不能因省略下标而丢掉。
不同轨道的对数为gⱼgⱼ′；同轨有序m≠m′求和有gⱼ(gⱼ−1)项，
改用无序m<m′则分子分母同时减半。

实际数算符表达为
\(V_{jj}n_j(n_j-1)/2\)及不同轨道的\(V_{jj'}n_jn_{j'}\)。
旋转不变时，可等价用Pauli允许的JT矩阵元按2J+1平均；
同轨同类半整数核子只允许偶J。具体相位/归一须对应所选相互作用文件。

Otsuka Eqs.(7)–(8)直接给出其同位旋平均约定：

$$
\widetilde V_{pn}(j,j')=\frac{V_0(j,j')+V_1(j,j')}2\quad(j\ne j'),
$$
$$
\widetilde V_{pn}(j,j)=\frac12
\left[\frac{2j+2}{2j+1}V_0(j,j)+\frac{2j}{2j+1}V_1(j,j)\right].
$$

同轨T=0的奇J通道维数为g(g+1)/2，T=1的偶J为g(g−1)/2，
除以总数g²即得以上权重；这是任务计数解释。
它不是任意电荷依赖、多体或不同JT规范下pn作用的无条件通式。

### 3. 添粒、移粒和连续导数的自项不同

固定其它占据，取简化单轨单极能量
\(\mathcal E(n)=e_0n+Vn(n-1)/2+nB\)，B表示其它轨道的给定贡献。
允许添/去粒的范围内，

$$
e^+(n)=\mathcal E(n+1)-\mathcal E(n)=e_0+Vn+B,
$$
$$
e^-(n)=\mathcal E(n)-\mathcal E(n-1)=e_0+V(n-1)+B,\qquad
\partial_n\mathcal E=e_0+V(n-\tfrac12)+B.
$$

Otsuka明确采用添粒变化的ESPE约定，因此其+Vn不和n(n−1)/2矛盾。
在同一固定H和同一约定下作两态差，添粒/移粒/导数之间态无关常数可消去。
但完整谱重心在本纯单极、球平均模型中是

$$
e^{\rm cent}(n)=\frac{(g-n)e^+(n)+ne^-(n)}g
=e_0+Vn(1-\tfrac1g)+B.
$$

它与添粒式相差−Vn/g，变化差为−VΔn/g，并不普遍取消。
这个模型例子对应Otsuka Appendix A所提示的同轨修正，
不证明任意关联态、三体作用和有效转移算符均满足同一关系。
在半填充n=g/2，谱重心恰与连续导数相等，不能只用这个特例“验证二者始终一样”。

### 4. 冻结参考态不是把两体算符换成一个常数

Otsuka PDF17/Fig.13的操作，是取指定参考态的每轨ESPE作为新SPE，
同时移除活动两体单极项，保留多极项。按此可示意写

$$
H_{\rm frozen}[\Phi_{\rm ref}]
=\sum_{\tau j}\langle\Phi_{\rm ref}|\hat e_j^\tau|\Phi_{\rm ref}\rangle n_j^\tau
 +V^{\rm multi}+C.
$$

C可选作态无关能量零点；原程序的对齐细节未核。
参考态的信息仍编码在一体谱内，切断活动反馈不等于撤掉所有单极影响。
154Sm的基态参考与球形HF参考产生不同结果且仍能形变，
是该H下的干预，不是所有核中形变必要/充分机制的证明。
PDF19/Fig.15是166Er，不能误作同一154Sm干预。

### 5. 非正交重叠不能当互斥组分概率

Togashi将基矢内禀Q₀、Q₂坐标画在PES上，
圈面积与相应投影基矢和模型本征态的重叠量相关。
不同基矢非正交，其投影不是互斥完备分解：
重叠平方不自动加和为1，也不等于展开系数模平方。
取归一向量u₁=(1,0)、u₂=(0.6,0.8)及
\(\Psi=(u_1+u_2)/\sqrt{3.2}\)，两个重叠平方各0.8、和1.6，
而展开系数平方和0.625。它仅是任务代数控制，非实际MCSM数据。

MCSM是投影选基/变分方法，并不预知每个基矢与全空间真态的最大重叠。
固定H也不等于无经验输入：Togashi区分JUN45/SNBG3原有经验构造、
VMU中心T=1缩放和本计算进一步的局部T=1微调。
作者另报告未微调时仍有快速转变，不能仅以存在拟合就否定其机制。

## Assumptions

有限差与谱重心代数限上述纯单极模型及统一能量/算符规范。
原件转引的研究不计为本任务新读原作或独立实验。

## Competing Explanations

张量吸排是指定相互作用分量、径向与同位旋下的轨道趋势，非跃迁几何选择定则。
中心项和张量项在Zr所用轨道可相干或相消；总漂移不能一律归张量。
偶宇称E2单体不能直接连接异宇称轨道，四极关联、占据重排和对激发需分别说明。

## Transfer Conditions

跨区比较须对齐轨道空间、相互作用、SPE/ESPE定义、有效算符与实际观测通道。
相同轨道名或同一质量区不保证相同核芯/耦合，也不能由有限数据等同整个壳结构。

## Failure Conditions

把有限窗反应重心当完整谱矩、用未反对称态平均、
把参考SPE当二体常数、把T-plot当实测概率，
或宣称有限体系不能发生任何精确交叉，均会误导后续解释。

## Falsification or Reverse Tests

[`a130_rewrite_monopole_centroid_audit.py`](../../system/scripts/a130_rewrite_monopole_centroid_audit.py)
实际重放T11核心数值一致，另用n=1、3核非半填充的导数/谱重心差异。
producer/input/输出哈希见`outputs/l4/20261108-A130-monopole-centroid-controls/run-provenance.json`。
这些只检验指定代数，不是完整壳模型、反应分析或MCSM复算。

## Open Questions

原始谱重心文献、分辨尺度/有效算符的可比性以及实际反应强度完整性，
需要定向原件和共同计算输入；缺口不由综述题名或代数控制自动填补。

## Human Review

T11独立原件/代数核查与总控重放，没有用户人工审核事件。

## Promotion or Rejection History

- 2026-11-08：固定ESPE定义和计数，撤回有限窗/非正交概率的过强解释。

## 2026-11-13补充：T12独立审查后的谱矩阵与可观测性边界

本节追加后续核查，不撤换上述T11的指定单轨模型推论、参考冻结和T-plot结论。
直接理论来源是
[[duguet-2015-non-observable-nuclear-shell-structure]]，
其本地16页原件为arXiv:1411.1237v3（2015-09-11），对应2015年PRC92,034313；
PDF第1页2018年Dated是本载体再编译日期。
T12/report.json与correction.tex只记录独立审查及记号校正，不计作原始文献。
G82定向复核了原件身份页及第4–8页的定义/变换段，没有重跑toy。

### 复非对角谱矩阵不能由对角强度替代核对

沿Duguet PDF4 Eqs.(4a,b),(5a,b)，把原文 \(a\) 单纯改名为 \(c\)：

\[
U_\mu^p=\langle\Psi_0^A|c_p|\Psi_\mu^{A+1}\rangle,\qquad
V_\nu^p=\langle\Psi_0^A|c_p^\dagger|\Psi_\nu^{A-1}\rangle,
\]
\[
S_\mu^{+pq}=U_\mu^p(U_\mu^q)^*,\qquad
S_\nu^{-pq}=(V_\nu^p)^*V_\nu^q.
\]

若保留旧G74报告采用的共轭振幅
\(U_G^p=(U^p)^*,V_G^p=(V^p)^*\)，乘积相应变为
\(S^{+pq}=(U_G^p)^*U_G^q\)、
\(S^{-pq}=V_G^p(V_G^q)^*\)。
这是换记号的代数核对，不是新实验事实；
在对角项上共轭差别消失，不能用只核对角的结果保证复非对角元正确。

PDF5 Eqs.(9)–(11)、PDF6 Eq.(13)定义的 \(h^{\mathrm{cent}}\) 是Hermitian矩阵，
其本征值才是ESPE。在球形 \(0^+\) 参考及所声明粒子种类守恒下，
旋转与宇称限制 \(j,m,\pi,\tau\) 块，但同一块内不同径向轨道仍可混合；
必须另行对角化，不能宣称球形 \(0^+\) 使任意轨道基底的重心矩阵必对角。
选择条件回PDF4脚注5；径向块解释是本稿按该对称结构作的条件化说明。

### 同轨扣除项的适用条件

Duguet PDF4 Eq.(3b)、PDF6 Eqs.(14)–(15)的直接结果包含反对称两体矩阵元
与密度，另有三体及更高体贡献。本稿的单轨化简另取以下条件：
同一固定两体Hamiltonian与正交基底，同种粒子的 \(j\) 壳，
球平均密度 \(\rho_{jm,jm}=n_j/g_j\)，以及
\(V_{jj}\) 为 \(g_j(g_j-1)\) 个Pauli允许反对称有序磁子态对的平均，\(g_j>1\)。
在这些条件下同轨项为

\[
V_{jj}n_j(1-1/g_j),
\]

相对添粒单极约定 \(V_{jj}n_j\) 的差为 \(-V_{jj}n_j/g_j\)。
两态在相同基底、相互作用及上述密度条件下比较，差的变化是
\(-V_{jj}\Delta n_j/g_j\)。
从此矩阵元化简推广到ESPE本征值，尚要求所选轨道基底使相关矩阵对角，
或实际处理剩余非对角耦合；不能把三体/任意关联Hamiltonian都纳入同一公式。
这是本稿在直接来源表达之上的代数推论，不说成Duguet给出的普适修正公式。
高 \(j\) 只在固定 \(V_{jj},\Delta n_j\) 时显式带来 \(1/g_j\) 因子；
占据差可随简并度增加，没有据此得到的普适绝对误差阈值。

### 裸场固定与一致演化场是两种合同

Duguet PDF7–8 Eqs.(23)–(29)及邻文讨论：
固定裸单体场形式而演化Hamiltonian和态，谱强度与ESPE一般具有分辨率/方案依赖；
态与场算符精确一致变换则保留原振幅及相应谱矩阵，但场算符通常产生高体项。
不把非可观测性说成每个导数必须非零，更不说成所有实验量均不可测。
能谱、分离能与截面仍是可观测量；有限窗统计重心、反应模型谱因子重心
与完整谱矩阵本征值须分开记录其权重、能窗、算符及误差。

T12不支持也不采用旧G74的SRG \(\lambda=1.8\)–\(2.2\,\mathrm{fm}^{-1}\)、
NO2B和动态自能平缓的普适必要充分门槛。
比较应声明Hamiltonian、分辨率/方案、场算符、基底/径向映射、
相互作用与多体截断、强度覆盖及误差，再按具体问题判断。

### 原始载体和权限的剩余边界

Baranger1970本地PDF实测1页、79996字节，另有有损OCR XML而无可靠公式结构；
本次没有取得可全文逐式校对的影印本，不将T12现代文献核对冒充Baranger原作核验。
2026-11-08一次entitlement响应不能推出2026-11-13权限或整个过刊库状态。
本轮没有重新联网或调用API测试权限，当前权限未知。
新manifest只记录本轮实际查验及原文件哈希，不覆盖历史manifest、PDF或XML。
