---
type: research-note
title: "R3 基础解释：量子标签、坐标冗余、投影与集体模式边界"
aliases: [R3 quantum labels and model boundaries, 集体模式基础解释检查]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [bohr-1952-surface-particle-coupling, bohr-mottelson-1953-collective-individual-original, matsuzaki-2004-nuclear-inertia-and-wobbling, kvasil-2006-dy156-yb162-crpa-wobbling, book-bohr-mottelson-nuclear-structure-vol2]
created_from: "博士前置原作学习、解释能力检查及独立理论审计"
promotion_target: ""
tags: [doctoral-foundations, symmetry, chirality, signature, projection, octupole]
---

# 从“这个态叫什么”走到“这个名称允许预言什么”

## Research Trigger

准备博士论文前，需要把实验标签、参考态对称性、坐标重标记和近似声子标签分开。
本页以早期原作与旋转RPA为入口，逐项解释并纠正本轮工作稿中过强的结论。
推导和数学反例不是新的实核拟合，不作为发现新运动模式的证据。

## Grounded Evidence

| evidence | source / locator | provenance | limitation |
|---|---|---|---|
| 五个四极坐标可写成形状及取向，主轴命名不唯一 | [[bohr-1952-surface-particle-coupling]], pp.9–13,19–21 | 原作者模型 | 纯表面标量空间有特定限制 |
| 粒子/集体分离需要能标条件 | [[bohr-mottelson-1953-collective-individual-original]], pp.10–21, Eq.(II.3) | 原始理论综合 | 不是所有核、所有自旋的严格分解 |
| 奇自旋γ带成员与小幅摆动在所述模型有相同π、signature | [[matsuzaki-2004-nuclear-inertia-and-wobbling]], PDF2，及pp.3–8 | 作者理论陈述 | 共同标签不决定耦合强度 |
| RPA色散式、旋转伪模与带符号求和规则 | 同来源 Eqs.(11)–(12),(21)–(25) | 指定模型 | 不作为所有QRPA实现的充分必要定理 |

## Provisional Reasoning

### 1. 换轴名字不改变核，却改变波函数的写法

取一个一般三轴四极形状，三条主轴的名字和正向有多种选法。
这些选法对应同一个实验室四极张量；一个单值波函数需要在重标记下保持一致。
Bohr1952 pp.19–21处理24种右手轴标记，其中还包含γ坐标与角度的联合变化。
因此，把局部 \(q_\gamma\to-q_\gamma\) 的反射单独称为原子核空间宇称或旋称，
需要另给出它在完整坐标和波函数上的作用。

在固定形状扇区，先只取右 \(D_2=\{e,R_x(\pi),R_y(\pi),R_z(\pi)\}\)。
对纯四极单值**标量**函数和整数 I，固定实验室 M 后，容许的K通道数为

\[
P_{D_2}=\tfrac14\sum_{g\in D_2}D^I(g),\qquad
m_I=\operatorname{tr}P_{D_2}
=\frac{2I+1+3(-1)^I}{4}.
\]

这是任务的特征标推导；π转动的特征标为 \((-1)^I\)。
\(m_{0,1,2,3,4}=1,0,2,1,3\)，故该空间没有 I=1，
却有 I=3；m也不是所有振动径向本征态的总个数。
它与原文的K偶及 \(g_K=(-1)^Ig_{-K}\) 相容。
24种完整轴置换还给γ边界条件，不能把它们全部替换为四个D₂元素。

加入奇粒子后，粒子内禀波函数也随轴变换，总态应联合满足一致性。
质子/中子相对取向等额外自由度也改变模型空间。
所以纯单四极模型的I=1缺失不是所有核态的Pauli禁戒，
不能用它排除磁剪刀等含相对自由度的1⁺激发。
对半整数I直接使用同一四元素平凡平均也不是上述整数投影；
自旋/内禀表示及双群条件必须保留。

### 2. 实验室自旋、K和signature有不同的使用条件

在通常忽略弱相互作用宇称破缺、无外场的旋转不变强/电磁Hamiltonian中，
可用实验室 \(I^\pi\) 标记能态。
K是相对指定体轴的投影标签；轴对称、Coriolis/组态混合可忽略等条件下
它可成为有用的好或近似量子数。三轴项允许K混合，但混合程度须由具体作用及能隙确定。

明确令 \(\mathbf j=\mathbf J/\hbar\)，主轴推转
\(H'=H-\hbar\omega_{\rm rot}j_x\) 若保有 \(R_x(\pi)\)，
则可用其本征相位 \(r=e^{-i\pi\alpha}\) 分类相应参考态或局域模式。
这不是在任意TAC态中都存在的额外实验室标量。
角动量投影是恢复/构造好I态的一种方法；旋转不变空间中的直接对角化也可以做到，
不能称三维投影为唯一途径。

Matsuzaki2004 PDF2明确比较奇自旋γ带分支和小幅摆动的
\(\pi=+,\alpha=1\)。
横向 \(j_y,j_z\) 在绕x轴π转动下均反号，可给小幅声子的相应旋称变化。
共同标签只意味着该对称性不禁止耦合：
两态模型中 \(\tan2\theta=2|V|/(E_1-E_2)\)，
V仍可为零，非零时也可因能差大而弱混合。
不能从“γ模式”或“取向模式”的名字给所有状态指定同一个局部坐标反射性。

### 3. 参考系中的伪模不等于另一条核带

若完整H旋转不变，则

\[
[H-\omega_{\rm rot}J_x,\ J_z+iJ_y]
=\hbar\omega_{\rm rot}(J_z+iJ_y).
\]

因此在相应自洽线性响应中，转动系参考取向的模式可出现在
\(\omega_{\rm rot}\)；“零频”需要注明实验室/静态参考的含义。
这段为任务的角动量对易推导，不把伪模命名为新的实验激发。

Matsuzaki的Eq.(11)在所述模型和γ≠0的推导中分离出该因子，
不是说γ≠0对所有实现都是NG分离的充分必要条件。
轴对称自洽QRPA也可处理适用的被破缺转动；
某套三轴消元式在轴对称极限奇异，不能推出物理分离必然失败。
式中不显含κ，也不表示任意改变残余作用后全部响应和预测不变。

其 \(\sum_{n\ne NG}\sigma_n c_n^2=1\) 是带符号规则。
\(|c_n|\)不是一般的概率或纠缠熵。
要讨论形状—取向纠缠，须先定义物理子系统分解、归一化态及约化密度矩阵；
两个由约束/坐标变换关联的描述不自动构成独立子系统。

### 4. 手征反幺正操作为何不能照抄宇称

采用 \(T\mathbf jT^{-1}=-\mathbf j,\ TiT^{-1}=-i\) 及
\(T^2=(-1)^{2I}\)，令 \(C=T R_y(\pi)\)。
反幺正性使

\[
TR_y(\theta)T^{-1}=R_y(\theta),\qquad
C^2=T^2R_y(2\pi)=+1
\]

对整数/半整数I都成立。
Kramers保护针对 \(T^2=-1\) 的条件，不强制两条不同同Iπ带简并；
无外场旋转不变时，半整数体系的M与−M通常已经属于同一I多重态。

若 \(C|\psi\rangle=\lambda|\psi\rangle\)，重定相
\(|\psi'\rangle=e^{i\phi}|\psi\rangle\) 后
\(\lambda'=e^{-2i\phi}\lambda\)。这样的±相位不能像普通宇称那样作为独立可观测标签。
特定集体模型可另有线性的左右交换/坐标反射算符并定义±，
但必须给出该算符和空间，不能把它等同于C。
左右正交、等对角元的二维近似可给劈裂 \(2|t|\)；
非正交或高维耦合需另解，不是任何近简并双带都满足的普适隧穿公式。

### 5. 非正交宇称恢复还需要重叠

取线性幺正宇称P，\([H,P]=0\)，归一化 \(|\Phi\rangle\)，定义
\(S=\langle\Phi|P|\Phi\rangle\)、
\(h=\langle\Phi|H|\Phi\rangle\)、
\(k=\langle\Phi|HP|\Phi\rangle\)。
S无量纲，h/k有能量单位；\(|S|<1\) 时，

\[
|\Psi_\pm\rangle=\frac{(1\pm P)|\Phi\rangle}{\sqrt{2(1\pm S)}},
\quad E_\pm=\frac{h\pm k}{1\pm S},
\quad E_--E_+=\frac{2(hS-k)}{1-S^2}.
\]

这是任务的二态广义本征推导。
共同能量零点平移使h和k分别改变，但hS−k不变；
单独k并不具有这种不变性。H=h·1时，k=hS可以非零而劈裂为零。
\(|S|=1\) 时一个投影态零范数，不能继续套两态式。
反幺正C的 \((1\pm C)/2\) 对复数标量不线性，不是此处的线性量子投影。

### 6. 八极“有利”与E1/E3幂次

\(\Delta l=\Delta j=3\) 常见于有利轨道组合，却不保证所有角因子或径向积分最大。
任务的单个零磁3j反例为
\(|(1\,3\,2;0\,0\,0)|^2=3/35>4/63=|(1\,3\,4;0\,0\,0)|^2\)；
只比较这两个因子，不替完整约化矩阵元或实核集体性排序。

平移不变偶极可写
\(\mathbf D=e\int\mathbf r[\rho_p-(Z/A)\rho]d^3r\)。
质中密度处处同比例时D为零；仅有β₂=0并不等价于这个条件。
最低二阶协变项 \([Q_2\otimes O_3]_1\) 在轴向常写为β₂β₃；
更高阶对称性允许性不能因此删除。
任务的精确角向控制给

\[
P_3(x)^3=\frac{36}{385}P_1(x)+\cdots,\qquad
\int Y_{10}Y_{30}^3d\Omega=\frac{3\sqrt{21}}{55\pi}\ne0.
\]

所以八极立方可以含L=1。这只证明允许，不保证特定密度模型/质心修正后的
物理系数非零；不把它命名为已发现的八极核特征。
对所选小形变几何模型，E3振幅最低阶可随β₃，
\(B(E3)=|\langle f\|\mathcal M(E3)\|i\rangle|^2/(2I_i+1)\)
才随其平方；RME和B的单位分别为e·fm³和e²·fm⁶。
强E3仍需结合波函数/模型区分动态关联与稳定形状。

### 7. 多根与非谐性：保留判别条件

某观测的二次有理式 \(F(\delta)=(a+b\delta+c\delta^2)/(d+e\delta+f\delta^2)\)
对应给定中心y的二次方程。其判别式可正、零、负，分母零点需排除；
第二独立观测可能消歧，也可能因误差或共同参数而仍保留多个分支。
不存在“角分布加偏振联立必有两个实根”的代数定理。

固定I=4、固定惯量的
\(H/\epsilon=j_x^2+2j_y^2+4j_z^2\) 在D₂标量空间有不等的相邻间隔，
控制值约为16.5582ε与27.0814ε。
这证明固定惯量不等于完整谱精确谐振；
没有仅凭该矩阵把三态认作真实零/一/二声子。
谐振子 \(B(n\to n-1)\propto n\) 要求共同线性算符和适当的自旋/几何比较，
不能把不呈2倍增强作为所有摆动解释的一票否决。

### 8. 历史理论怎样用两种观测暴露自己的不足

Bohr–Mottelson1953 pp.90–95用 \(E_I=\hbar^2I(I+1)/(2\mathcal J)\)
与 \(\mathcal J=3B\beta^2\)连接能谱与形变，另用E2率映射Q和β。
Table XXIII的160Dy列E2=85keV、F=140、βE=.65、βQ=.28，
表内没有误差；它们是当时采用的测量和条件映射，不是现代评价量。
作者看到两种β趋势相近、大小有差别，同时考虑几何Q映射不足和B低估。
因此，历史模型的力量既在可比的关系，也在能暴露不一致；
不能将该偏差唯一归因某个后来才明确的惯量机制。
Table XXII保留暂定自旋；旧表的208Pb标签不拿来作现代2⁺能量。
不虚构“科学家当时必然怎样想”或“某段直接催生后来的模型”的因果。

[[kvasil-2006-dy156-yb162-crpa-wobbling]]的CRPA原件（PDF1–4,16）提供现代对照：
同一模型可随频率改变模性质，并联合比较E2、M1与惯量；
同时其Eq.(6)明确在交叉附近用唯象配对处方。
这种比较不要求将所有模先贴互斥标签，也不把“自洽”当无近似保证。
现代结果相对早期增加了可计算的组态/配对/响应，
其新增价值仍须由未拟合电磁和一致性检查衡量。

## Assumptions

每个推导明确固定空间、参考系、相位和算符。
静态对称的精确量子态、破缺参考态与半经典近似不是同一个对象。
标准5DCH的形状—转动耦合仍通常处在绝热集体框架内；
“大振幅”或加入更多坐标不自动证明超越绝热。

## Competing Explanations

相同Iπ、近简并、增强E2或相似形状矩可来自不同组态与耦合。
转子有限自旋非谐、带交叉、有效算符和响应选择都可能改变声子指纹。
不能用一个归一化的模型诊断量代替完整波函数或实验区分。

## Transfer Conditions

数学一致性可跨区复用，实际模式需逐核说明占据、配对、能隙、形状分布、
惯量、取向和可观测量。单一质量数或固定γ不决定上述近似有效。

## Failure Conditions

若把K/旋称/局部反射/空间宇称互相替代、把允许写成必强混合、
把模型空间限制写成全核禁戒、或忽略非正交度量，则推理失败。

## Falsification or Reverse Tests

[symmetry控制脚本](../../system/scripts/doctoral_r3_symmetry_projection_controls.py)
实际通过22项代数/矩阵控制；结果和环境在
[controls.json](../../outputs/l4/20261108-symmetry-projection-controls/controls.json)
及其run-provenance。它们不是真实核实验、原RPA程序或新模式验证。
对实核仍须共同模型与未拟合EM、上限、探测灵敏度比较。

## Open Questions

怎样在实际可得的共同Hamiltonian/算符下定量连接γ分支和取向模？
如何让形状—取向联合描述增加可测预言，而不只是重画同一边缘分布？
这些为D11的研究问题，不把未解决问题当作永远不能讲清基础的理由。

## Human Review

- Review scope: 原件学习和总控/Terra定向审计；无用户逐项科学审核事件。
- Decision: 解释与可重放控制持久化，实核归因保持provisional。
- Complete unresolved P0/P1 inventory: 全部原RPA/波形/绝对EM数据未重放；
  对数学恒等式的控制不扩大到原作者全部近似或实际核的唯一机制。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-11-08 | 原作/量子标签/投影基础核查 | 分域草稿 | provisional | 移除若干必然混合、双根、刚性必谐及普适禁戒断言 | doctoral-nuclear-structure-foundations |
