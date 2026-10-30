# 032：新取得Larsson1978原件恢复历史矩阵元合同，未恢复2022 actual job

本单元承接133Ce蓝本候选池，选择新已得输入的**历史RME/坐标/BCS接口原读**。它有真实科学delta：不再只有RS88指回Ref1的一句转引，现已读1978自己的§2.3与Appendix。但没有因此得到2022 GAMPN/ASYMO/PROBMO代码、输入卡或实际矩阵值。

本worker只写指定worker/tmp；canonical/raw/PLAN/Bib/Git、课程/session均未改。旧Larsson006的body0页是当时访问结果，保持历史；本次新scope单独记录，不能回填旧轮阅读。新claims均`needs_review:true`，未运行任何代码producer/114。

## 候选池重建与本次选择

先读当前133Ce blueprint及WK22/RS88有关输入边界，并核本轮既有worker：ce133-node005九条observed边、highspin006映射、本人Li/Singh与AW13/1978-access报告及当前canonical的对应写回。

| 候选 | 当前已有内容/缺口 | 032处理 |
|---|---|---|
|624.6/582.7/464.4母态branches|九条observed边/末态已逐表核；582 out/out仍无observed reference；817.7仅energy差|不再重复summary，也不补造818的强度或upperlimit |
|131Ce↔133Ce带/零点/τ|source-scoped桥与AW13 Band2/3身份已写入；A13高spin映射有独立版本/零点边界|不按同band号/同spin继续强拼 |
|实际角响应、ε/λ零点与模型输出|active mask、header/input、完整波函数/EM输出缺；已停endpoint无新信息|不重复失败访问或调用旧producer |
|Larsson1978历史方法|旧006只获metadata；**用户新补充35页body现已真实登记**|选作本次新输入，核explicit RME与coupling字段 |

这不是以source摄入/译完结项。已有branch问题没有因新方法文自动关闭；本次只把一个实际可读的方法缺口向前推进。

## 原件、身份和实际读区

S.E.Larsson, G.Leander, I.Ragnarsson, **Nuclear core-quasiparticle coupling**, NPA307(1978)189–223，DOI10.1016/0375-9474(78)90613-9。首页三作者、题名、期刊/页码及received1978-05-03/revised1978-06-21已fresh核。实际文件为用户补充的publisher/scanned article：

`raw/papers/1-s2.0-0375947478906139-main.pdf`

35页，1772577bytes，SHA256 **108c29bed9de467d99f330c0b8cef47be82a290263a85e398ba3b4f2e97d77eb**，匹配新获取回执。本文PDF页+188=印刷页。

**实际scope：**PDF1–11/printed189–199的Introduction、§2.1–2.3、185Re应用开头；PDF31的§4 Conclusion及前接段；PDF32–34/printed220–222 AppendixA1–A16/引用入口。共15页范围的主线文本，非35页全文精读；PDF12–13只曾提取为定位，不据它们新认证应用表。视觉核PDF1、3–11、31–34，含Figs1/2、Table1、Eq6/7/8–17、AppendixA1–16。旧扫描/OCR的符号以原页视觉为准。

另fresh读/视觉WK22 PDF47–48/printed36–37（Eqs3.17–3.24）；PDF49–50 §3.4程序分工只作已有原读复用。未下载新body、未查新endpoint。

## 一、哪些历史字段现在确实可闭合

### 1. 单粒子→耦合层不仅需要energies

L78 **PDF8/printed196 §2.3 Eq8–9**先定义单粒子εν和带符号的c_(NljΩ)^ν展开，3轴可选任一principal axis；barred态有明确time-reversal相位。**PDF9/197 Eqs11–16**列六类generalized decoupling/operator矩阵元：

| 历史字段 | 原件对象 |
|---|---|
|(a+b)μν|⟨χμ\|j+\|χbarν⟩ |
|cμν|⟨χμ\|j−\|χbarν⟩ |
|dμν|⟨χμ\|j²−j3²\|χν⟩ |
|eμν|⟨χμ\|j+²+j−²\|χν⟩ |
|Ωμν|⟨χμ\|j3\|χν⟩ |
|(Ω²)μν|⟨χμ\|j3²\|χν⟩ |

原文明确单粒子势对这个coupling calculation的影响经由这些矩阵和εν传递。这给GAMPN类输出一个**可审查的历史字段清单**，不只要求单粒子能表或三个最大振幅。Eq15与16也提示j3²矩阵须独立保留；在截断空间中不能默认它等于已截断j3矩阵的平方。

**PDF9–10/197–198 Eq17**构造D2-symmetrized good-total-I强耦合基，K−Ω为偶整数；I±为body-fixed，I+在K指标上降、I−升，并有小K额外贡献。`strong-coupling basis`在此是实现/收敛选择，并不把每个本征态都限制成物理强耦合极限：PDF2/190 Introduction说增加deformed orbitals移除adiabatic限制。这与只保一条轨道的FA不是自动同一近似。

### 2. Core-H含Coriolis与recoil，不能暗删后者

**PDF3/191 Eq6**从R=I−j得到Σ(Ik²−2Ikjk+jk²)/(2Jk)；作者明确仅当single-particle shell model中已显式包含相应项时，才可将recoil从此处删除。**PDF9/197 Eq10**给ladder展开，Eqs11–16供其实际矩阵。

**PDF4/192 Eq7**本文应用的hydrodynamical处方为Jk=(4/3)J0sin²(γ+2πk/3)，且本模型此处Jk为constant。这个4/3前因子与轴/γ号数必须连同原式；不能把别文无4/3的J0或WK22的Harris spin-dependent值直接搬入。本文并未恢复WK22 actual coreR/惯量消费方式。

### 3. BCS方案和忽略项有直接原句

**PDF10/198 §2.3**：standard BCS作用在adiabatic single-particle levels，给λF、uν/vν并将εν换为Eν；core-coupling段给uu′+vv′ pairing factor。作者明确**忽略recoil term的特殊性质和blocking effects**，另引ξ乘在pairing factors上。

同页又列另一处方用于Ref20/§3.3：只以Δ=12/√A MeV、λF放在odd orbital来替换quasiparticle energies。因此即便此文有λ/u/v的定义，**也不能据它选择WK22实际用了哪一方案**。该段在coupling-H方法语境中，不能把文字“each single-particle matrix element”未经核验扩为整个core+particle E2统一乘plus因子。

原文称此BCS计算“without additional adjustable parameters”是其已选模型内的说法，不等于不需要pairing强度、粒子数/空间等输入，更不恢复2022 λ50.6与ε5–6MeV的单位/零点。

### 4. Appendix终于给相干many-body RME，而不只有抽象B定义

**PDF32/printed220 A1**：

\[
B(O\lambda;I_i\to I_f)=\frac{1}{2I_i+1}
|\langle I_f\Vert\mathcal M(O\lambda)\Vert I_i\rangle|^2.
\]

**A3/M1与A4/E2**明确把final和initial的带符号a_(Kν)^I系数相乘后对K,K′,ν,ν′相干求和，最后才按A1取模平方。其核包括CG、spin/generalized-decoupling因子以及：

- M1的gR·I diagonal项、(gs−gl)s项和(gl−gR)j相关项；首项显式含δ_(II′)，故跨I不由总I生成元提供振幅。
- E2的**Q0δνν′+q20**与**Q2δνν′+q22**，连ΔK=0及±2的CG相干组合；core与odd-particle贡献不是在B层简单相加。

**原字面边界：**A3/A4印的是real/sign convention下的`a_final a_initial`，**没有印共轭星号**。若写通用复幅形式a_f* a_i，那是本任务的线性代数推广，不冒作原页literal式。相干signed sums的结构本身已直接可读。

**A2的direction/单位边界：**原式是

\[
\delta=\sqrt{0.7}\,E_\gamma\,
\frac{\langle I\Vert\mathcal M(E2)\Vert I-1\rangle}
{\langle I\Vert\mathcal M(M1)\Vert I-1\rangle}.
\]

它字面使用⟨I\|…\|I−1⟩，不能未经Hermitian/WE convention核对就改成downward ⟨I−1\|…\|I⟩；也不能仅凭√.7推定WK22实际绝对单位或signedδ convention完全一致。本页的favoured/unfavoured负δ sign rule只在作者所说decoupled-band条件下，不用于给所有跨带线定标签。

同页gs=.6free为历史应用选择；RS88的.7及WK22的.6不能仅凭数字相同就认actual版本。E2 coreQ0/Q2可由填充到protonFermi面求和；odd-neutron应用可用macroscopic值替代。其source选择必须进实际input合同。

### 5. stretched/physical算符差别现在有explicit形式

**PDF33–34/221–222 A5–A16**把physical orbital/j算符写成stretched l^t加f^t、g^t校正，由ωx/y/z系数变换，包含j²/recoil所需产品。例：A11–12给

\[
j_z=s_z+A l_z^t+B f_z^t,
\quad A,B=\tfrac12(\sqrt{\omega_y/\omega_x}\pm\sqrt{\omega_x/\omega_y}).
\]

所以ωx=ωy的轴对称极限有A=1、B=0；一般不能用j=l^t+s假装已完成physical operator。A9/A10给oscillator-shell selection rules和commutator归约，后续产品也不能只从单一截断j矩阵天真平方。

**仍有外部formalism字段：**PDF32末明确single-particle q2μ在stretched basis的表达转**Ref23=Leander–Larsson,NPA239(1975)93**（PDF34）。这篇1978body不是整个single-particle E2 library/actual数值矩阵的自包含发布；本轮未读Ref23 body。

## 二、与WK22原字面对接到哪一步

WK22 **PDF47/printed36 Eqs3.17–3.20**给D2/K−Ω、BCS和coherent basis展开；**PDF48/37 Eqs3.21–3.24**给B、core+particle M1/E2定义及同样方向的δ式。L78提供了此前缺少的explicit historical A3/A4核，二者在方法层可逐字段比较。

但WK22 Eq3.21/3.24使用单竖线记号并配散文解释，M1段先定义moment operator，而L78 A3有显式√(3/4π)等归一。**不能凭形式类似就补写actual reduced/full-ME区分、绝对μN/eb单位、operator normalization或phase convention**；要用实际GAMPN/ASYMO/PROBMO输出header和transition output判断。

本轮35页native文本对GAMPN/ASYMO/PROBMO无命中，已读方法/appendix亦不提供这三个程序的具体名字/版本/输入文件；阴性文本检索不构成全史证明。历史论文+WK22引用关系仍不能当2022 actual execution manifest。

| 合同层 | 新关闭内容 | 仍未关闭 |
|---|---|---|
| 原件获取 | 35页身份/hash与15页实际方法读区 | 全文应用/所有fig/tab尚未精读 |
| GAMPN类结构 | εν、c展开、六类j/j² coupling矩阵、time-reversal/D2约定的历史定义 | 2022 actual νID/完整矩阵/header、κμ值/截断/频率/输出单位与零点 |
| ASYMO类结构 | goodI/D2 basis、full signed coefficient与BCS二种处方、显式recoil/Coriolis项 | 2022选哪种BCS/ξ规则、λ/Δ/blocking、Harris/coreR、实际eigencoefficients |
| PROBMO类结构 | A1–A4的coherent signed RME、core+particle与A2方向；stretch变换A5–16 | 2022operator版本/有效g/Q、完整相位/归一/单位/数值RME；q2μ历史Ref23本轮仍未读 |
| 目标133Ce实际输入 | **没有任何2022 actual numeric/card字段因本次而自动恢复** | ε约5–6MeV与λ50.6共同零点、负πλ、ε4.1/.01、582reference、τ/BR/ICC/Cov均保留 |

## 三、真实跨模型控制：同参考定标下软/动/刚芯不完全可分，也不全无信息

**已实际读的§2.2（PDF3–8/printed191–196）、Fig1/Table1/Fig2**提供一个可用于γ-softness竞争解释的历史模型控制：

- 取γ-unstable且β-deformed core、γ≈30°的dynamical rotor、γ=30°的rigid rotor；四种组合共享**E(2+)=.358MeV、B(E2;2+→0+)=.419e²b²、particle-core k=40MeV、A193/Z79**（PDF5/193 Fig1caption）。它们不是四次独立实验或四份独立定标。
- Fig1分别换core excitation energies与quadrupole RMEs。rigid-core rotational bands较stiff会明显反映到odd-A谱；在此截断/参数例中，换QME造成的odd-A level shifts相对小。作者说这给rigid effective core一项有限适用理由，**不是所有core shape信息都从谱中消失的定理**。
- **Table1（PDF6/194）与PDF7/195正文**保留EM可分信息：rigid rotor的γ→ground RMEs较大者偏odd-spin γ成员，γ-unstable例偏even-spin；各行仍有大小/符号差。Table1是按⟨0\|Q\|2⟩=−100缩放、phase consistent but not unique的模型矩阵元，不能把−100当实测eb。
- Fig2在同参考例中比较扩大core空间与扩大particle空间，后者对odd-A谱影响更大；本例将f7/2、f5/2加入h9/2。不能把该A≈190谱间距/结论数值当133Ce九轨道收敛证书。
- **PDF3/191 §2.2**一开始就说rigid core shape不能字面当严格守恒量；PDF8/196与ConclusionPDF31/219还把aligned3qp加入作为未来扩展。固定1qp刚芯空间不因能谱近似好就已经描述backbend/真实3qp配置。

可复用delta是**“同已用参考量定标后，看未用core EM/particle-space差异”**的竞争解释控制；不是声称本例已测133Ce的γ-soft/rigid，也不把单一个gamma值或一条band的拟合当刚性证明。

## 四、反证和下一可解析路线

本次是实际新原件支持的progress，未饱和为旧body0/no-op。反证/限制仍明确：历史作者在转动芯中冻结内禀形状，近yrast收敛经验不是本核证书；full/schematic pairing并列且ignoreblocking；q2μ细节仍外引；WK22 actual代码header/phase/card不在此body。

下一高信息路线可以是：按A3/A4构建**不带目标核拟合的有限component核检查**（如gR总I项跨I为零、core/particle E2振幅相干而非率相加、轴对称stretch极限），并要求未来actual transition export逐字段对上这份历史接口。若新的Ref23已实际取得，再查其q2μ库；没有body时不重撞失败端点。582/817.7与ε/λ实际缺口不因这条方法路线被假关闭，也不成为用户自动待办。

## 产物和检查

`source-reading.json`含新body身份/真实scope；`contract-fields.json`是历史定义/实际2022缺口的可消费清单；`claim-ledger.json`区分literal与复幅推广/方法推断；`artifact-manifest.json`存hash。tmp有35页自动text、实际读区图、WK22两页图；**自动35页text不算35页阅读**。

工具仅local PyMuPDF/hashlib、已有source/worker/directread、view_image、native名字检索和JSON检查。无联网/未知代码、无新run/credit、无canonical/raw/Git写入。
