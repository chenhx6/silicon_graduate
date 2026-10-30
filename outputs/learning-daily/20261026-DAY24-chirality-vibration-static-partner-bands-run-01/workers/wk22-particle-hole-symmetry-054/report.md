# 054：WK22粒子—空穴等谱声称的真实Ref51与严格模型边界

**Ref51原文给的是有明确single-j、能量零点、配对与core合同的精确模型对称；不能仅凭轴置换将它迁给WK22实际多orbital Nilsson job。** WK22 PDF48的简述省略了这些关键条件。这个判断来自新取得的真原件及连续方法原读，不是只凭“single-j常识”反驳，也不是认证任何实际Ce组态等能或程序有错。

## 身份、取得与阅读范围

WK22 physicalPDF126/printed115的**Ref51**是J. Meyer-Ter-Vehn, *Collective model description of transitional odd-A nuclei (I). The triaxial-rotor-plus-particle model*, NPA **249** (1975)111–140，DOI `10.1016/0375-9474(75)90095-0`、PII0375947475900950。Ref52才是PartII，不混用。出版商FULL XML的题名/DOI/卷页与真PDF首页一致，cover date1975-09-08。

取得使用已授权配置的publisher API，按既有daily `--si`授权：

- 常规skill batch PDF HTTP200给**1页60529bytes**，SHA `b99a46ae900de79788a340305b22c55b6dbff6ce7054d6433584c06d27081b13`，仅preview；不把工具downloaded标签当完整body。SI探测报告CDP不可达，本轮未启动浏览器/宿主。
- 复用已验证的FULL XML→**该XML实际返回的MAIN attachment EID**→标准Object Retrieval API，两请求均HTTP200，无transport retry、无猜main端点。真body `tmp/day24-wk22-particle-hole-symmetry-054/attachment-object-response.pdf`，**30页1365168bytes**，SHA `10cb7aca223dcbccb17ee7aa224a7a1c13fb9f1e6e58a04fcdd8ab1e4b888da9`。
- FULL XML的si1.gif/si2.gif对象实际标`category="thumbnail" type="ALTIMG"`，不是仅凭文件名si就当科学补充材料；本轮未识别可下载scientific SI，不断言所有SI不存在。完整XML与API manifest留本tmp，不含凭据输出。

实际scope：WK22连续PDF44–49/printed33–38文字核上下文，重点视觉PDF46/48，另PDF125–127 references定位；Ref51**连续PDF4–12/printed114–122，Chapter2 §2.1–2.6全部文字与整页视觉**。PDF12最末§3标题/开头一段是阅读边界；PDF1摘要/题名只核metadata，PDF2–3及§3/结论尚未由本单元深读。055独立负责其余科学主线；不以本scope冒称30页全文阅读。

重叠检查：既有WK22-29/30/39、LLR78/RS88方法与041/042字典，以及ZH07特殊p/n交换控制。它们未固化WK22此项Ref51严格scope。ZH07的γ30/等j/相反C的p/n交换是不同模型操作，不拿来代替本粒子—空穴共轭。

## 原文先把问题限定清楚

**Ref51 PDF4/printed114 §2.1**明确：“Its configuration space will be restricted to a **single j-shell**”，奇核子以BCS quasiparticle表示，采用2×2 particle/hole空间。只考虑one-quasiparticle states；该模型不是完整multi-qp配置库。

PDF5/printed115 Eq2.6为（τ为particle/hole Pauli矩阵）

\[
\mathcal H_p=(\varepsilon_j-\lambda_F)\tau_z+V_p\tau_z+\Delta\tau_x.
\]

紧接原文：“Restricting to a unique j-shell, one can set **εj=0** in the following。”球形壳能量是同壳常数，可共同吸收入λ零点；没有把所有多轨道spherical spacings抹去的权利。Eq2.7只取该壳内quadrupole deformation field；共用径向因子k(r)与球谐组合，未含后来实际多轨道spin-orbit/l²/ε4的全部矩阵。

原文Eq2.11–13另假定

\[
\mathcal H_R=h_R\,1_{ph},\qquad
h_R=\sum_k{(I_k-j_k)^2\over2\mathcal J_k},
\]

即**core旋转能不依奇核子被写成particle还是hole**。Eq2.14采用同一overall J0的irrotational形状依赖`Jk=(4/3)J0 sin²(γ−2πk/3)`。精确对称不仅是Vp的一个负号，还包括该rotor、配对、空间与能量基准。

## 原文的完整对称操作

PDF6–7/printed116–117 §2.3先区分同形状的六个axis-label扇区，再用Eq2.18给

\[
V_p(\beta,\gamma,\theta_3,\phi_3)
=-V_p(\beta,60^\circ-\gamma,\theta_2,\phi_2).
\]

这里是quadrupole potential在**不同轴标与γ反射**下的负关系，并非单纯“任意Hamiltonian换轴就反号”。Eq2.19实际操作Γ为

\[
(\beta,\gamma,\lambda_F,\Delta)
\mapsto(\beta,60^\circ-\gamma,-\lambda_F,-\Delta),
\quad(\hat1,\hat2,\hat3)\mapsto(\hat3,\hat1,\hat2).
\]

按它的角与轴定义，Γ†HpΓ=−Hp而Γ†HRΓ=HR。单独particle/hole的σy又使Hp反号、HR不变；合成才得到Eq2.22

\[
(\sigma_y\Gamma)^\dagger\mathcal H(\sigma_y\Gamma)=\mathcal H.
\]

这是**不同参数表示间的unitary equivalence/模型等谱映射**，不是同一实际核中两条不同configuration必然degenerate。原文同页说Δ符号变化不影响谱；那是此BCS配对势的gauge自由度，不能丢掉配对幅度/相位合同再宣称任意配对方案等价。β/轴/γ convention与WK22 ε2也须对应，不能只抄参数名字。

## BCS与实际计算近似分别保留

PDF8 Eq2.25–26给eν=√[(εν−λF)²+Δ²]与usual occupation。若配对的逐线对应满足

\[
\varepsilon'_\nu=-\varepsilon_\nu,\quad
\lambda'_F=-\lambda_F,\quad |\Delta'|=|\Delta|,
\]

则e′ν=eν且u′²ν=v²ν、v′²ν=u²ν。这是明确零点下的代数，不是只改λ符号而保持原多轨道εν不动。ξμν=uμuν+vμvν在共同实gauge和成对映射下不变，而ημν=uμvν−vμuν按同gauge变号；精确doubled合同中的这些项须整体变换。

原文**实际数值方案**还有独立近似：Eq2.28的rotor在qp/qh之间含hη交叉块，Eq2.30将其丢弃，只留两个hξ块；Eq2.31/32在这套对称一致的处理下给particle/hole等谱关系。PDF9/printed119明确讨论该近似：λ远高/低于壳时η=0；穿壳时以小level差/弱耦合理由估计hη小，讨论对象为约.1<β<.2的弱形变核。**对称定理是该模型内精确，不等原文每项近似已被实验或本任务证明精确。** 阻塞、selfconsistent λ/Δ、active space或近似若只改一边，等谱也不能自动沿用。

## λ反号必须围绕共同能量零点

原文εj=0后，λF实际表示相对所选球形j壳中心的λ。若某程序使用绝对或另有offset的E，壳中心为E0，则真正应反射的是

\[
e_\nu=E_\nu-E_0,\qquad\ell=\Lambda_F-E_0,
\]
\[
e'=-e,\quad\ell'=-\ell
\quad\Longrightarrow\quad
E'_\nu=2E_0-E_\nu,\quad\Lambda'_F=2E_0-\Lambda_F.
\]

只有E0=0的**同一数值约定**才写Λ′F=−ΛF。共同平移E→E+c、Λ→Λ+c保持E−Λ，但不能让两列本来未核的零点自动变共同。

WK22正宇称Ce的λF=50.6MeV与打印ε约5–6MeV仍未获共同offset/header。故不能拿这条对称把50.6任意变−50.6，更不能把“−λ”解释成**负宇称λ输入**。空间宇称是所选轨道的性质，particle/hole反射不把positive parity轨道变negative parity轨道。此前WK22-30的actual零点/负πλ缺口保持。

## 为什么不能无条件迁到WK22 actual Nilsson空间

WK22 Eq3.14只给Hcoll，独自不含ε2、λF或完整single-particle field；因此48页声称不能仅由Eq3.14推出。相邻Eq3.16实际是多NljΩ Nilsson型势，含HO、quadrupole、spin-orbit与l²；§3.4 GAMPN还要求ε4与自选active orbitals，后续采用自己的core/Harris与BCS接口。

一个精确迁移的充分合同是：在同维度、变换封闭空间中存在U及已声明E0，使

\[
h'(\gamma')-E_0 1=-U[h(\gamma)-E_0 1]U^\dagger,
\quad\lambda'_F-E_0=-(\lambda_F-E_0),
\]

并同时使配对矩阵、particle/hole表示、core kinetic矩阵、每轴惯量/能量基准、阻塞/截断与实际近似协变。单j quadrupole模型提供该合同的一种实现，**single-j不是所有可能数学模型的必要条件**，也不是多轨道必然不可能等谱的断言；actual job却须逐项给证据。

最直观的失败条件：若h=h0+V2，h0为旋转scalar而在多轨道中有不同spherical energies，轴置换使h0不变，而所需particle-hole反射要求h0−E0反号。仅当在所选子空间h0=E0 1，或另有明确的成对谱映射时，才可吸成一个offset。spin-orbit/l²在单一固定nlj中是常数，但跨l/j的spacings一般不能如此处理；ε4及其轴/γ组合也必须另核，quadrupole的负关系不自动覆盖rank4。这里没有用“多轨道”标签当proof of failure，而是给出尚未满足的算符等式。

core若改为R-dependent惯量、Harris或good-core-R能量，可在**同一R、同一标量函数且轴变换协变**时保映射；但不同配置/core参数、粒子与空穴不同blocking/response或不同截断不会由一个R²名字自动相消。当前实际字段不足，结论是**不能认证WK22实际多轨道两配置严格同谱**，不是已算出它们不等谱。

## 等谱也不能推出δ不变

Ref51自己的EM定义已提供直接反例。PDF9–10 Eqs2.34–41给core+particle的Q、同ph号的M，并在原映射下

\[
S^\dagger Q_{2\mu}S=-Q_{2\mu},\qquad
S^\dagger M S=M,\quad S=\sigma_y\Gamma.
\]

原文明确：对应态的E2 reduced matrix elements改变符号，M1不变。PDF11 Eq2.49/50取平方给对应B不变；Eq2.51及其后正文进一步明确**Qsp与δ变号**、其余所列量不变。这不是从任意statephase变化制造的结论：共同重相位使同一transition的E2与M1振幅同时乘同一phase，比值不变；这里两算符在S下有**相对**odd/even行为。

因此只在**该原文算符定义、同一映射的初末态、共同相位/辐射与正Eγ约定，且M1非零**时，模型给δ′=−δ；|δ|与各B相同。本文没有把该符号关系迁成133Ce实测δ的反号预测，也没拿总体statephase当新物理。WK22 actual effective charges/g/operator/header和完整signed states未知，不能由能谱表单独认证其δ、q22或相位。

## 方法段剩余字段与停止边界

PDF11–12 §2.6也已连续读完：以β、γ、λ为free parameters，β/γ从邻偶芯低态估、λ从Nilsson图估，其余smooth mass处方；k=206/A^1/3 MeV、ℏ²/(2J0)=204/(β²A^7/3)MeV、Δ=135/A MeV与b=βA^2/3尺度。原文把轴向经验处方向三轴延伸并说明其不确定性；这些处方不填WK22实际参数，也不证明不同mass/j数值完全相同。新源方法阅读已经闭合，不需靠toy或拟合再演示一次。

可写回的窄增量：Ref51真实single-j/εj零点/Γ与ph操作合同；严格模型等谱与actual多orbital readiness分开；λ反射必须有E0，不能与宇称混同；源定义下E2 odd/M1 even及relative δ sign作为模型性质。canonical/raw/PLAN/Bib/Git、学分/session均未改；只写054/tmp，sameDay24＋恰好Day25未计分预习，无未知producer/114。
