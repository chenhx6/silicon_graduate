---
type: source
title: "Larsson–Leander–Ragnarsson1978：芯—准粒子耦合的历史接口与EM核"
aliases: [Larsson1978 core quasiparticle coupling, LLR78]
created: 2026-10-27
updated: 2026-10-27
status: ai-draft
review_status: unreviewed
source_type: theory-method-and-applications
reading_depth: deep-read
title_original: Nuclear core-quasiparticle coupling
authors: [S. E. Larsson, G. Leander, I. Ragnarsson]
year: 1978
journal: Nuclear Physics A
volume: 307
pages: 189–223
doi: 10.1016/0375-9474(78)90613-9
canonical_source: https://doi.org/10.1016/0375-9474(78)90613-9
citation_key: ""
raw_file: raw/papers/1-s2.0-0375947478906139-main.pdf
raw_sha256: 108c29bed9de467d99f330c0b8cef47be82a290263a85e398ba3b4f2e97d77eb
nuclei: [185re, 75se, 77se]
models: [core-quasiparticle-coupling, rigid-triaxial-rotor, modified-oscillator, BCS]
methods: [strong-coupling-basis, coherent-electromagnetic-matrix-elements]
tags: [133Ce-method-blueprint, model-contract, stretched-coordinates, gamma-softness]
---

# 历史方法矩阵元已可原读，2022实际job仍须另核

## Bibliographic Record

S. E. Larsson、G. Leander和I. Ragnarsson，*Nuclear Physics A* **307**, 189–223 (1978)，DOI `10.1016/0375-9474(78)90613-9`。本地用户补充的出版商扫描PDF为35页、1772577bytes、SHA见frontmatter；首页received1978-05-03/revised1978-06-21。fresh Crossref HTTP200核题名、作者、卷/页及1978-09出版月。physicalPDF页+188=印刷页。

该原件在另项已发布的2026-10-26获取登记后才进入本日可解析输入。此前Larsson访问body0/原读0页是历史真实结果，不回填成当时已读；[[ragnarsson-semmes-1988-particle-rotor-moments]]的转引也不冒作本篇原读。

## Scope and Reading Depth

分工后已覆盖全部科学主线：032实际读PDF1–11、31–34的Introduction/§2/Conclusion/Appendix，036读PDF11–31全部§3应用及Conclusion，并视觉核全部Figs3–10、Tables2–5、Eqs18–22；连同032的Figs1/2、Table1、Eqs1–17/A1–16，非只依自动提取充阅读。root独立读PDF1–11/31–35方法/附录/参考及应用关键PDF15/20–22/29–30，视觉核PDF6/Table1、PDF32–33/Appendix及PDF13/18/19/28/30的定标、EM表与Figs9/10。引用实验原件并未逐篇新读；这不是全文数值复现或恢复作者producer。WK22 PDF47–48/Eqs3.17–3.24定向回核，程序分工段复用既有原读。未执行作者程序、未知附件或旧114。

## Summary

原文显式给单粒子能/六类j矩阵、D2 good-I基、Coriolis/recoil、两种BCS处方及相干signed M1/E2核，关闭了[[133ce-thesis-analysis-blueprint]]的一项历史方法原件缺口。它没有交付2022 GAMPN/ASYMO/PROBMO的版本、input/header、完整本征系数或数值EM输出，不能替作者选λ零点、blocking或修ε4。

## Experimental or Theoretical Setup

§2从Bohr Hamiltonian在变形静态场附近展开，冻结内禀形状、保转动坐标；R=I−j给Σ(Ik²−2Ikjk+jk²)/(2𝒥k)。strong-coupling基是技术上的表示选择，增加deformed orbitals可移除单轨道adiabatic限制，不代表所有态都处物理强耦合极限。应用所选hydrodynamic 𝒥k=(4/3)𝒥0 sin²(γ+2πk/3)有自身轴/γ及𝒥0归一，不和其它文的无4/3形式或WK22的Harris合同混数值。

## Key Results

新claims全部`needs_review:true`。历史定义、任务线性代数解释与actual2022缺口分别列出。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LLR78-D24-001 | 新35页原件身份/hash及本次实际方法阅读已核，旧body0访问记录保历史；本篇不是2022代码/输入发布证明。 | artifact-and-reading-scope | actual-original | PDF1 printed189; §2.3; Appendix | true |
| LLR78-D24-002 | Eq8/9给带符号单粒子c展开及conjugate相位，Eqs11–16列energies以外六类j/j² coupling矩阵。只给能表或若干最大权重不能重建coupling-H；截断j3²不能默认是截断j3的平方。 | direct-interface-plus-projection-boundary | direct-original-and-labelled-linear-algebra | PDF8–9 printed196–197 Eqs8–16 | true |
| LLR78-D24-003 | Eq17为D2 good-I基、K−Ω偶整数；body-fixed I+在K上降、I−升，有小K额外项。strong-coupling basis的技术选择不等单轨道FA或物理强耦合极限。 | basis-and-approximation-distinction | direct-original | PDF2 printed190; PDF9–10 Eqs17及其后段 | true |
| LLR78-D24-004 | recoil只在particle-H已显式含相应项时才可删；本文constant-core 𝒥k的4/3归一/轴γ号须保，不能直接替WK22 spin-dependent coreR/Harris。 | Hamiltonian-and-input-convention | direct-original | PDF3–4 printed191–192 Eqs6–7 | true |
| LLR78-D24-005 | 方法段standard BCS与Ref20/§3.3的Δ=12/√A、λ放odd orbital是两处方；明确忽略blocking和recoil特殊性，ξ另乘pairing factors。coupling-H段的uu′+vv′不能自动扩为整个core+particle E2乘同因子，也不选出2022实际方案。 | approximation-and-transfer-boundary | direct-original | PDF10 printed198 pairingparagraphs | true |
| LLR78-D24-006 | A1–A4给final/initial real signed a相干求和的M1/E2，再按A1平方；M1含gR I/自旋/轨道项，E2为coreQ与particleq的振幅和。原A3/A4没有共轭星号，通用a_f* a_i为任务推广，非literal转录。 | explicit-EM-kernel-and-real-convention | direct-original-plus-labelled-extension | PDF32 printed220 A1–A4 | true |
| LLR78-D24-007 | A2字面RME顺序为⟨I∥M∥I−1⟩，sqrt(.7)不单独恢复2022的WE/单位/emission/sign字典。favoured/unfavoured态之间的负δ规则限其decoupled-band语境。 | direction-units-and-sign-scope | direct-original | PDF32 printed220 A2及其后句 | true |
| LLR78-D24-008 | A5–16显式把physical j写成stretched l及校正，ωx=ωy时A11/12的A=1、B=0；一般不能用j=l_stretched+s替换。single-particle q2μ的stretched公式仍指Ref23，032时未读该1975原件；后续043/044原读另见本页Ref23续接。 | coordinate-operator-and-residual-gap | direct-original-plus-labelled-limit | PDF32–34 printed220–222 A5–A16; Ref23 | true |
| LLR78-D24-009 | Fig1的软/动态/刚性芯共享E2+与B20等定标，换QME对所选odd-A谱移相对小，core stiffness与particle截断影响仍明显；Table1 γ→ground的odd/even EM区别保留。不是实测133Ce或普适shape不可辨定理。 | actual-cross-model-control | direct-model-output | PDF3–8 printed191–196 Fig1/Table1/Fig2 | true |
| LLR78-D24-010 | WK22的generic basis/EM与本历史方法可逐字段比较，但本篇已读方法/Appendix不提供三程序实际版本/input/output；全文native名称检索无命中也不等全史无此程序。 | method-lineage-versus-producer | source-grounded-bounded-audit | §2.3/Appendix; WK22 PDF47–50 | true |
| LLR78-D24-011 | 作者不把rigid shape当严格守恒量；高j core alignment/3qp扩展作为未包含路线。近yrast谱吻合不能自动证明shape刚性或已在原1qp空间处理backbend。 | validity-and-space-boundary | direct-original | PDF3 printed191 §2.2; PDF8 printed196; PDF31 printed219 Conclusion | true |
| LLR78-D24-012 | Table1共享⟨0∥Q∥2⟩=−100标尺：γ4→ground4的软/动态/刚芯RME为127/102/70，ground4→2为−165/−164/−158。按相同Ii的A1，软/刚B比前者3.29163、后者1.09057；是原模型表的任务算术，不是实核差异、photon-rate比或精度/功效认证。 | direct-model-table-exercise | original-values-plus-explicit-rate-definition | PDF6 printed194 Table1; PDF32 A1 | true |

| LLR78-D24-013 | 185Re以六positive-hole轨道/A187 MO参数，在186Os先验外按奇核Q、groundband惯量和[4111/2]bandhead调ε/ε4/γ/coreE2；总体谱/EM支持保留，定标量不再算完全独立预测。未见理论K7/2带的sidefeeding解释是可能性，非有效上限。 | calibration-and-conditional-support | direct-model-and-reused-experiment | PDF11/13–14 printed199/201–202 Fig4/Table2 | true |
| LLR78-D24-014 | Se应用ε.29/ε4=0、五正四负轨道和BCS处方；惯量按odd-A spacing、γ35/30按负低态次序选，75Se正宇称ξ.85为恢复groundstate。模型内γ选值不是独立γ分布/刚性测量。 | actual-calibration-contract | direct-original | PDF15 printed203; Figs5–6 | true |
| LLR78-D24-015 | Tables3/4 half-life/branch计算用实验Eγ且略ICC及非M1/E2模式；部分谱/EM支持伴75Se E2的125对6、34对37W.u.等不同质量比较，不能称完整衰变链独立预测。 | decay-contract-and-adverse-result | directly-reported-model-versus-cited-data | PDF18–19 printed206–207 Tables3–4及脚注 | true |
| LLR78-D24-016 | 作者保rigidcore缺额外low0+family、两parity惯量/邻核coreE2不一和同gap导致负谱低485/413keV等弱点；blocking/高阶pairing/particle-hole/manyqp是建议改善，未在此解决。 | author-adverse-results-and-unexecuted-extensions | direct-original | PDF20–21 printed208–209 weaknesses(i)–(vi) | true |
| LLR78-D24-017 | fully-decoupled示例的unfavoured states可由较远多轨道组成且仍almost aligned，不等简单antialigned；Fig8/Table5组分随spin/γ变化，权重不提供全phase。 | direct-model-mechanism-and-output-boundary | direct-original | PDF22 printed210 Eqs20–21及后段; PDF24–26 Fig8/Table5 | true |
| LLR78-D24-018 | Fig9中ε4与引入γ可经不同机制使某些unfavoured谱向同方向移动，幅度还依λ/Δ；Fig10 jmixing也可改变谱。是特定模型例，不证明所有能量普适不可辨或恢复133Ce ε4/λ。 | conditional-parameter-discrimination | direct-original-plus-labelled-inference | PDF27–31 printed215–219 Figs9–10 | true |
| LLR78-D24-019 | γunstable芯加f7/2改变模型⟨cos3γ⟩及谱，rigid芯不能被极化却也可有类似谱移；不能混同两种原因。单加邻壳未达数值收敛，作者明言。 | dynamic-core-versus-space-effect-and-convergence | direct-original | PDF29–31 printed217–219 Fig10/Eq22及结论前段 | true |
| LLR78-D24-020 | 标准3j WE及两算符同Hermitian spherical-tensor convention下，Rfi=(−1)^(If−Ii)Rif*，M1/E2反向RME比仅复共轭，real convention下A2的同正Eγ系数δ不另加相对负号。此方向代数可闭合，但不认证2022单位/算符/radiation字典；个别B仍有不同初态统计权重。 | conditional-task-direction-derivation | direct-A1/A2-premise-plus-independent-algebra-review | PDF32 printed220 A1–A2; task direction-review037 | true |
| LLR78-D24-021 | 在明确bare磁矩μ与标准T(M1)=√(3/4π)μ、同RME/单位前提下，B(M1)=3/(4π)Bμ；若E2已标准，人工bare-μ比得到的δ再乘√(4π/3)才与此标准定义一致。它是条件算符字典，不是WK22实际rate/δ的修正率或代码漏因子证据。 | task-conditional-M1-normalization-dictionary | direct-prefactor-plus-declared-convention | PDF32 A1–A3; WK22 physicalPDF48 Eqs3.21–3.24 | true |
| LLR78-D24-022 | 定义完整Q-like张量O2μ=√(16π/5)T2μ才可对各分量统一换算B(E2)=5/(16π)BO；WK22球谐积分已含Y2归一，不能再盲乘。若同时从O2和bareμ转标准，两算符比例使δ因子为√(5/12)，actual Q2/q22/tesseral定义仍需核。 | task-component-resolved-E2-normalization | direct-operators-plus-declared-spherical-harmonic-dictionary | PDF32 A3–A4; WK22 physicalPDF48 Eq3.23 | true |
| LLR78-D24-023 | 任务明确选择X_i=√(ω_i/ω0)x_i后，由physical r²Y2μ可推五分量pointwise表达与dimensionless ξ的length²桥；给定该约定的几何转换可闭合，不需要伪称已读Ref23。仍不给历史库/实际频率/径向basis矩阵或Ce预测。 | explicitly-task-derived-stretch-identity | source-coordinate-premise-plus-continuous-derivation | PDF33 A11–A13 coordinate premise; WK22 physicalPDF48 Eq3.23; task042 | true |
| LLR78-D24-024 | 指定伸缩后physical L为加权微分生成元，完整q仍是其rank2；普通stretched球谐展开中的r_t²项一般不与physical L对易，不代表物理E0。Hermitian/轴对称/球形极限与全五分量张量关系已作有界符号核验，非actualproducer测试。 | task-tensor-covariance-and-multipole-boundary | continuous-identity-plus-symbolic-component-check | PDF33 A11–A13; task042 coordinate identity | true |

## Method and Observable Chain

单粒子接口需保存εν、完整带符号c_(NljΩ)^ν、barred态相位，以及以下六类矩阵：⟨χμ|j+|barχν⟩、⟨χμ|j−|barχν⟩、⟨χμ|j²−j3²|χν⟩、⟨χμ|j+²+j−²|χν⟩、⟨χμ|j3|χν⟩、⟨χμ|j3²|χν⟩。它们对应(a+b)、c、d、e、Ω及Ω²；完整算符的压缩与先压缩再平方不是同一操作。

A3的M1核包括gRδII′δKK′δνν′√I(I+1)，以及CG乘(gs−gl)s与(gl−gR)j相关矩阵；总I生成元的项跨I为零，不意味着剩余M1为零。A4 E2核为(Q0δνν′+q20)乘ΔK0的CG，加(Q2δνν′+q22)乘ΔK±2的CG组合。二者都先对K/ν与初末态signed系数求和，再平方，不能在B层把core/particle或不同组分独立相加。完整原式仍以printed220 A3/A4的相位/基约定为准。

历史应用gs=.6free、Q0/Q2由protonFermi面填充或odd-neutron的macroscopic替代，是要说明选择来源的输入；它与RS88的.7或WK22的.6不因数值一致而成为同一个job。WK22单竖线记号/散文算符定义还需actualoutput来核reduced/full、μN/eb及全相位。

Appendix的jz=sz+A lz^t+B fz^t，A/B=1/2(√(ωy/ωx)±√(ωx/ωy))，展示physical/stretched字典；A9/A10的commutator归约和A14–16产品亦影响recoil矩阵。原文把single-particle q2μ表达指向G. Leander与S. E. Larsson，*NPA*239(1975)93（Ref23），故本原件并非完整数值operator library。

### A2方向的条件代数可以闭合

采用标准3j约定，⟨IfMf|Tλq|IiMi⟩=(−1)^(If−Mf)(If λ Ii;−Mf q Mi)Rfi，且Tλq†=(−1)^qTλ,−q。Hermiticity和3j对称给Rfi=(−1)^(If−Ii)Rif*；相同spin端点的M1/E2有同一反向因子，rank没有额外相对号；比值要求M1分母非零，纯E2极限另表。故A2的upward-order RME比是downward-order比的复共轭，在real convention和同一正Eγ系数下δ不变。M1的time-odd不表示anti-Hermitian，不能据此再添一个负号。

这关闭声明前提下的方向数学疑点，不把可解析项永远留unknown。与此同时，(2Ii+1)B(Ii→If)=(2If+1)B(If→Ii)，个别B不因RME模相同就反向相等；逆跃迁若无正放光Eγ也不因此成为已观测γ。2022的full/reduced、M1 moment/transition归一、μN/eb/Eγ单位及radiation/emissionδ定义仍需actualproducer证据，不能由这条代数一并认证。

## EM归一条件字典

### moment、transition tensor与E2分量的条件字典

041把可解析归一与actual字段身份分开。明确μq=μN[gR Rq/ℏ+Σ(gl lq+gs sq)/ℏ]，则标准M1张量为√(3/4π)μq；若角动量矩阵已以ℏ为单位，不再重复除ℏ。在同态/同RME convention下，B(M1)=3/(4π)Bμ。若E2已为标准球谐张量，人工δbare=√.7 Eγ R_E2/R_μ转为δstd需乘√(4π/3)。这不是对WK22现有δ实际施加的校正，其actual输出是否为bareμ并未得到证明。

采用标准Condon–Shortley球谐，T20=√(5/16π)∫ρ(2z²−x²−y²)，T2,±1=∓√(15/8π)∫ρ z(x±iy)，T2,±2=√(15/32π)∫ρ(x±iy)²，积分均含d³r。若定义O2μ=√(16π/5)T2μ，O20为Cartesian Q型，O2,±1系数为∓√6，O2,±2为√(3/2)，必须逐分量保留这套字典。只有在A4的Q0/q20、Q2/q22分别消费这些量且轴/实分量一致时，可与其前因子作充分条件识别；不由相同Q名字自动识别actual库。A4内禀0/±2核也不意味着任意lab或off-diagonal single-particle的±1分量为零。

WK22 Eq3.23若本来就是标准∫ρr²Y2，再乘√(5/16π)会重复归一。在完整O2定义下才有B(E2)=5/(16π)BO；若E2从O2、M1从bareμ一起转换，δ因子为√(5/12)，不能只补M1。通式T_E=a_E O_E、T_M=a_M O_M给B乘各自abs(a)²、δ乘a_E/a_M（同单位/辐射约定、M1非零）。正实归一不改变sign，但相位/辐射约定不由此认证。

普通ME/RME的3j字典已在[[ragnarsson-semmes-1988-particle-rotor-moments]] RS88-18建立，本轮是对WK22字段的应用no-op：须知Mi/Mf/q及非零3j，静态moment也不靠单一辐射常数就变跃迁RME。单位恒等式1eb=100e fm²、1e²b²=10⁴e²fm⁴不依producer；把√.7与Eγ[MeV]/R_E2[eb]/R_M1[μN]配套使用仍须确认actual字段，不能由排版系数反推其单位。

## 指定stretch下的physical E2：任务推导

042不依赖新下载，亦不冒1975 Ref23原读。取右手轴、标准复球谐，单粒子几何q2μ=r²Y2μ不含有效电荷，量纲length²；定义dimensionful X_i=√(ω_i/ω0)x_i、a_i=ω0/ω_i>0、d_i=√a_i。未取任何实际核频率，未假定volume conservation或double stretch。记A=√(5/16π)、B=√(15/8π)、C=√(15/32π)，有

$$q_{20}=A(2a_zZ^2-a_xX^2-a_yY^2),$$
$$q_{2,\pm1}=\mp B d_z Z(d_xX\pm i d_yY),\qquad
q_{2,\pm2}=C(d_xX\pm i d_yY)^2.$$

这些是乘法算符的精确坐标重写，不等选定basis的积分矩阵。若tμ为直接以(X,Y,Z)组成的普通r_t²Y2μ，令α=(4az+ax+ay)/6、ct=(2az−ax−ay)/3、u=(ax+ay+2dxdy)/4、v=(ax+ay−2dxdy)/4，则

$$q_{20}=\alpha t_0+\frac{a_y-a_x}{2\sqrt6}(t_{+2}+t_{-2})+A c_t r_t^2,$$
$$q_{2,\pm1}=\frac{d_z}{2}[(d_x+d_y)t_{\pm1}-(d_x-d_y)t_{\mp1}],$$
$$q_{2,\pm2}=u t_{\pm2}+v t_{\mp2}-\frac{a_x-a_y}{2\sqrt6}t_0+\frac{C(a_x-a_y)}3r_t^2.$$

共同的是同一个r_t²函数，各分量系数不同，±1没有此项。物理转动在X上为S R S^−1而非普通R，故循环(i,j,k)的physical生成元为

$$L_i=-i\hbar[(d_j/d_k)X_j\partial_{X_k}-(d_k/d_j)X_k\partial_{X_j}].$$

它连完整q满足[Lz,q2μ]=ℏμq2μ与标准L± ladder关系；用L^t直接替换一般会破坏这些关系。特别[L_i,r_t²]=−2iℏ(dj/dk−dk/dj)XjXk一般非零；r_t²在stretched展开中的trace不等物理E0，不改变q的E2选择规则。物理scalar r²=ΣaiXi²反而与全部physical L对易，物理harmonic条件为Σai^−1∂Xi²q=0，不能换成普通stretched Laplacian。正实尺度下q2μ†=(−1)^μq2,−μ；常Jacobian权重/正规化坐标变换需一致保留。

若actual采用dimensionless ξ_i=√(mω_i/ℏ)x_i，需先声明ℓ_i=√(ℏ/(mω_i))、ℓ0=√(ℏ/(mω0))：x_i=ℓ_iξ_i、X_i=ℓ0ξ_i、ℓ_i²=ℓ0²ai。把上式X_i换ℓ0ξ_i后整体带length²；不能将无量纲二次式直接标fm²/b。电荷、basis径向积分与actual归一仍另需输入。

轴对称ax=ay=a⊥时q±2=a⊥t±2、q±1=√(az a⊥)t±1、q20=(2az+a⊥)t0/3+2A(az−a⊥)r_t²/3，Lz=Lz^t但全部L未必相同；球形尺度ai=a时qμ=a tμ、全部physical L=L^t、trace消失。root读连续推导/有限符号脚本并重跑exit0，核全部分量/ladder与字典，不使用实核参数，不认证截断basis或作者producer。042时Ref23实际历史定义未读；后续043/044已补读，见下节。GAMPN实际采用哪种stretch、径向矩阵/有效电荷和signed态仍缺。

## 应用里的定标、成功和失败

185Re的“A187”是MO参数组标签，不是185Au/187Au的实验。186Os core先验ε.20/ε4.06/γ16/E2=137keV经奇核Q、惯量和[4111/2]头调整为ε.25/ε4.08/γ15/E2=115keV，ξ1。Fig4/Table2显示实际支持，但用来选参的Q/间隔不又变独立holdout；未见理论带的强M1 feeding只为作者可能解释。

75/77Se的γ35/30及不同parity惯量由具体低态选取，75Se positive ξ=.85为ad hoc。部分谱/branch/EM有非平凡支持，另有显式失败：75Se的7/2+→5/2+ E2 quotedexp125、calc6W.u.，9/2+→5/2+为34/37；负谱相对实验低485/413keV，negative惯量对应coreE2=360keV与邻偶芯633/560/614不同，positive约600keV。作者未把差别唯一归为shape，且提醒某Q实验不够可靠。Tables3/4理论half-lives/branches用实验Eγ，忽略ICC和非M1/E2，不能直接当完整totalwidth预测；实验列仍是本文引用资料而非本次新实验核验。

§3.3进一步展示机制分歧：fully-decoupled band的unfavoured态不必反对齐；ε4、γ及jmixing能对局部谱作相似移动，而依赖不同空间/BCS/算符。Fig9的Fermi放最低orbital、Δ12/√A，略移Fermi会减弱ε4效应；Fig10的动态core polarization与rigidcore上改变s.p.空间必须分开。不能将原A≈130 proton示意参数移给133Ce，或由一个好谱冻结shape/occupation/跨parity零点。

## Competing Interpretations and Limitations

Table1给一个不需假造新模型的定量练习：γ4→ground4在软/动态/刚芯下RME为127/102/70，ground4→2为−165/−164/−158。在各自相同Ii=4的比较中，B的2Ii+1消去，所以前一支的软/刚B比=(127/70)²≈3.29163，动态/刚=(102/70)²≈2.12327；后一支软/刚仅约1.09057。这支持定标相同reference后选有分离预报的EM来补能谱；并非已选好实核测量方案。QME为原模型scaled值，符号依一致phase convention；没有Eγ响应/实验误差，不能将B比改名γ计数比、显著性或机时估计。

Fig1的四组组合共享E(2+)=.358MeV、B(E2;2+→0+)=.419e²b²、k=40MeV、A193/Z79，比较γ-unstable、γ30° dynamical与rigid core，并分别换core能量和QME。Table1按⟨0∥Q∥2⟩=−100缩放，phase consistent但不唯一；−100不是实测eb。谱移相近不等所有EM相同；Fig2扩大particle空间比本例扩大core空间影响更大，也不是133Ce九轨道收敛证明。真实可用教训是定标相同参考之后检验未用EM/空间，而非由能谱单独决定shape或宣布shape信息全消失。

还未恢复WK22正Ce λ50.6与ε约5–6MeV的共同零点、负πλ、ε4 .1/.01、blocking、coreR/Harris消费、完整signed波函数、g/Q/phase及逐线EM输出。582 out/out分母与817.7的observed状态也不因方法原件取得改变。`supports`历史方法可追溯性，`limits`以formalism文献代替actualproducer；不是133Ce研究结项。

## Extracted Pages

- [[133ce-thesis-analysis-blueprint]]：GAMPN类/ASYMO类/PROBMO类字段与实际未得输入分层。
- [[wakudyanaye-2022-triaxiality-rotational-bands-133ce]]：Ref40方法与2022实际代码身份分别核验。
- [[135nd-chiral-partner-resolved-evidence-map]]：γ-softness的跨模型例只支持适用域，不充当目标核替代fit。


## Ref23续接：完整原件已取得，A8范围比完整库窄

[[leander-larsson-1975-potential-energy-surfaces-n-equals-z]] LL75-D24-002–005/011现直接核到A1 dimensionless坐标、ω0与ω0°区别、A2/A3的CG-reduced角ME以及A8/A9。旧032/042“未读Ref23”的记录保留为当时状态，不再将它作为当前不可获取输入。

A8明确忽略γ、bra/ket为同一MO本征态ν，q2ν是Q-like对角期望；LL75-A2/A3同时确实有一般angular ME，不能因A8对角就说整篇无一般矩阵元。当前仍没取得的是完整三轴off-diagonal q2μ/radial数值库和2022actual输出，不能把历史对角式当该库已交付。其A8的ρ²项/length²与042轴向恒等式相符，041的0分量Q-like识别在此历史式中得到直接支持；实际q22等定义不由这一点全部闭合。

LL75 A2的double-bar角ME乘CG、无1/√(2j′+1)，按声明标准3j定义Rstd=√(2j′+1)rLL。此为实际归一差异例，不凭“双竖线”三个字识别actual程序。若同端点两个算符都采用同CG归一，spin因子在其比中可消；个别B仍须正确统计因子。本文没有因此修改任何既有rate/δ。
