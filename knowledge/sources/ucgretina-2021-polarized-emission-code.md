---
type: source
title: "UCGretina公开发射内核：统计张量、Stokes与禁戒系数边界"
aliases: [UCGretina polarized emission core, UCGretina zero CG Stokes audit]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: software-code
reading_depth: read
title_original: "UCGretina"
authors: [L. A. Riley, UCGretina contributors]
year: 2021
data_version: "historical1cd773473028ee4d2a30b848187471a06089fc99; head1271388e03ec9b3f8e055a988aeb4c2e4d2efedf; Geant4v10.7.4 functions/installed11.4.2 SDK"
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "rileyle/UCGretina selected pinned files and officialGeant4 selected v10.7.4 sources"
source_url: "https://github.com/rileyle/UCGretina"
raw_file: "raw/data/gpt/day16-20261018/ucgretina-ITDecay-6f89e531060c.cc"
raw_sha256: "6f89e531060cdcf1420f160f2ff4626afa4c21112426db29d0e83fdebf3218c9"
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [24Mg, 25Na]
reactions: []
experiments: []
models: [Geant4, statistical-tensor, photon-Stokes]
methods: [fixed-code-execution, phase-convention, photon-density-matrix]
observables: [angular-distribution-coefficient, gamma-ray-linear-polarization]
tags: [software-validation, pure-limit, polarization, response-readiness]
---

# UCGretina：发射代数、软件实现与阵列响应分开

## Bibliographic Record

[Riley公开仓库](https://github.com/rileyle/UCGretina)的README把主体程序关联Riley等*NIM A*1003,165305(2021)，DOI10.1016/j.nima.2021.165305，把POL实现明确关联[[morse-2022-gretina-polarization-sensitivity]]的DOI10.1016/j.nima.2021.166155。本页证据对象是固定代码，并未把Riley2021论文当全文已读。

默认`geant4.10`分支本次固定到[1271388e03ec9b3f8e055a988aeb4c2e4d2efedf](https://github.com/rileyle/UCGretina/tree/1271388e03ec9b3f8e055a988aeb4c2e4d2efedf)，commit date2026-08-04；按2021-12-02 author-preprint日期查得较早固定[1cd773473028ee4d2a30b848187471a06089fc99](https://github.com/rileyle/UCGretina/tree/1cd773473028ee4d2a30b848187471a06089fc99)，date2021-05-19。两者`src/ITDecay.cc`逐字节相同，SHA256如frontmatter；相关文件历史有2019新增、2020transition lookup修订、2021POL编译门。历史接近及README关联仍不足以认证作者实际binary、数据包、macro、geometry和后处理版本。

## Scope and Reading Depth

完整读所选`ITDecay.cc`436行、当前`Reaction.cc`285行及2021 tensor主线、GNUmakefile、alignment例子的README/macro/plot脚本；定向读README的build/EM/angle/alignment/source、PhysicsList过程与开关。官方Geant4 v10.7.4固定commit`098f6c74e60fbe2dbde3c347fdf5e0e321e311a2`的CG/W3j/W6j/LittleD/F coefficient、gamma multipolarity编码、nuclear tensor储存、Stokes轴旋转和Compton harmonic也已定向读。未声称通读788个仓库对象或整个Geant4。

17份UCGretina文件及Geant4选择文件放repo tmp，下载SHA256与Git blob均对照官方tree；raw归档槽未填。具体重放为原Stokes body135–272，body SHA256=`cc15968679ec3960a5151cc19a1ef9bacad07fabef52a823b672d7289a9711b5`；复制表达式不改，另用薄wrapper提供其既有输入。固定10.7.4的CG等函数只改class名，链接现有11.4.2 SDK的G4Pow/Exp/Log服务；另一组直接调用现有11.4.2 helpers。**这是两种已声明helper环境中的内核抽取执行，不是完整10.7.4 runtime或原阵列producer重放。**

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| UC21-1 | README/GNUmakefile要求POL=1启用Reaction张量与自定义ITDecay；AngularCorrelations和SetGammaPolarization另有runtime开关。PhysicsList默认usePolar=false，true时换入polarized photon processes。仅给初态alignment不自动启用所有偏振响应。 | code-configuration-contract | direct-code | README NuclearAlignment；GNUmakefile POL；PhysicsList ConstructProcess；2021PhysicsList_Messenger | true |
| UC21-2 | Reaction构建全部k=0…2J、κ=0…k，Pk0按CG之比与1/sqrt(2k+1)从P(m)计算；G4NuclearPolarization SetPolarization复制而不trim该输入。ITDecay在EmittedFragment更新前复制parentPol，因此不能以daughter事后trim来消除本次初始高rank问题。 | tensor-object-and-time-order | direct-code | Reaction.cc polV/Pk0_z；ITDecay.cc95–100；G4NuclearPolarization.hh69–74 | true |
| UC21-3 | ITDecay的P1/P2含C(L,1;L′,1→k,2)/C(L,1;L′,−1→k,0)乘F，未先消去共同CG。实际旧/新helper下mixed k0 L1/L′2及pureM1 k4的分子、分母、F均恰为0；浮点0/0×0不等于物理零项。 | source-expression-failure-condition | direct-code-and-execution | ITDecay.cc135–272；G4PolarizationTransition FCoefficient；G4Clebsch ClebschGordanCoeff | true |
| UC21-4 | 冻结的168次调用中，Morse spin2→0 pureE2与spin1→0 pureM1共48次有限，spin2→1 pureM1、spin1→1 M1/E2、同mixedlabel δ0及Na1041条件路径共120次P1/P2非有限；所有归一norm仍有限且正。两个helper环境现象相同，未把共有代码处理计独立实验。 | conditional-software-execution | actual-extracted-core | pinnedITDecay body135–272；本页控制表；ucgretina-core-audit-v2 | true |
| UC21-5 | 独立photon-helicity trace在相同spin/实振幅/PSD布居下均给有限且模长≤1的Stokes；finite purecontrols最大差1.11×10^-15，全部强度归一最大差7.78×10^-16。故这些NaN不是actual zero-intensity的undefined P边界；没有用clip或改输入消去失败。 | mathematical-companion-and-physicality | independent-algebraic-route | G4 F/CG definitions；本页photontrace控制表；ucgretina-core-validation-v2 | true |
| UC21-6 | 同一1→1、p−1/p0/p+1=.1/.8/.1、θ90°，MP3 pureM1给P1=.636364，MP304 mixedM1/E2且δ0却给NaN，两者norm≈1.65相同。代码标签改变破坏purelimit，不是新增物理解。 | same-path-limit-failure | actual-code-and-photon-trace | G4GammaTransition MP编码；ITDecay MP<99/else；本页purelimit行 | true |
| UC21-7 | 所选same-emitter路径/rank有F_G4(k,L,L′)=(−1)^(L′−L)R_RB，最大残差1.56×10^-15，故相邻M1/E2需δnative=−δRB。L26两支0/−.85在此映为0/+.85；同Gaussianσ/J=.56下θ90°的photontrace P1≈.340288/.017054，均是条件forward量，不是本run实测偏振或A0重拟合。 | convention-crosswalk-and-conditional-model | direct-coefficient-execution | G4 FCoefficient；L26 Eqs3–4；ucgretina-g4-rb-phase-crosscheck | true |
| UC21-8 | Morse给的p0=.52、p±1=.24、p±2=0之2→0 pureE2控制在θ90°给P1≈1，原代码finite并与photontrace相符。它是本页必要反证：不能从mixed/highrank失败宣判Morse pureE2标定或L26实验错误；exactproducer仍未认证。 | counter-evidence-and-scope | source-input-and-code-control | M22 Sec4.2 population；ITDecay pureMP4；本页控制表 | true |
| UC21-9 | Geant4 photon frame X=eθ/Y=eφ，Stokes轴旋转用2φ；对unpolarized electrons，Compton采样含−sin²ψ(P1cos2χ+P2sin2χ)。这一步的physical analyzing harmonic无额外1/2；若后续经验定义A0=Q Pbar/2，须由匹配jointkernel得到Q=2〈ΣP〉/Pbar，不能固定Q删半因子或称Q恒等于裸Σ。 | frame-and-response-normalization | direct-code-and-conditional-algebra | G4PolarizationHelper GetParticleFrameX/Y；G4StokesVector RotateAz；G4PolarizedComptonModel gdist | true |
| UC21-10 | 先用原F中的3j–CG关系约去公共CG，得到有限H系数；在所选全部原分母非零处与Cplus/Cminus×F最大差2.00×10^-15。该恒等式提供禁戒项的解析处理，未将NaN强置0或修改原publicsource。 | finite-expression-design | derivation-and-conditional-computation | G4PolarizationTransition FCoefficient；本页有限H公式；ucgretina-finite-product-first-result | true |
| UC21-11 | 实际10.7.4 Legendre函数含CS相位，sqrt((k−κ)!/(k+κ)!)P_k^κ=d_{κ0}=(−1)^κd_{0κ}；原角度sampler用前者，ITDecay Stokes归一用d_{0κ}。对相同声明PSD tensor，sampler I与独立trace差≤1.34×10^-15，IT归一核可差.48–.74；κ0轴对称控制不受此区别影响。 | source-internal-kernel-contract | direct-code-and-same-input-comparison | G4LegendrePolynomial EvalAssocLegendrePoly；G4PolarizationTransition GenerateGammaPhi；ITDecay preNorm | true |
| UC21-12 | 仅偶κ的pure1→0 M1、态v=[i,0,1]/sqrt2使原CG比值全有限、κ转置phase恒为+。16次literal调用的I/Q/V与固定eθ/eφ Jones trace相符，但U反号，最大(I,Q,Uopposite,V)残差6.67×10^-16；θ45°/φ0给原U=−.942809、JonesU=+.942809。该控制独立于mixed NaN及κodd问题。 | isolated-linear-Stokes-sign-control | actual-original-core-and-independent-trace | ITDecay pre2/P2；G4PolarizationHelper axes；本页evenκ控制；ucgretina-even-kappa-U-audit | true |
| UC21-13 | 在无偏振电子、511keV入射/90°Compton、相同G4正Φ轴的声明点模型中，核B=1.5，K45/K135=(B−U)/(B+U)；上述θ45°行分别给4.38415与.228094。此为消费端符号影响的条件计算，不是实际计数比或Q。另真实I=0控制保留Stokes undefined；预想d_k00(−1)NaN未观察，实际旧/新helpers均为1。 | consumer-and-failure-boundaries | source-code-and-conditional-calculation | G4PolarizedComptonModel gdist/dirx-diry；G4Clebsch WignerLittleD；本页零强度/极限控制 | true |

## Summary

这份公开代码补上了Morse文中“tensor→Stokes另文解释”的一个可定位实现入口，并暴露了混合/高rank条件下的字面浮点边界。它没有恢复原实验事件、阵列响应或作者exact producer；literal代码、独立物理振幅和经验Q三个对象仍须分层。

## 实际控制与相位自审

以下数值取声明的θ90°/meridian轴、正布居、无detector response；norm是源码两helicity及未归一振幅合并的量，photontrace `W=norm/[2(1+δ²)]`（pure为norm/2）。

| 声明输入 | 原P1/P2 | 独立trace P1 | 原norm | 解释 |
| --- | --- | --- | --- | --- |
| Morse2→0 E2，p0=.52/p±1=.24 | finite，P1≈1 | 1 | 1.2 | 与实际标定所选pure路径相容 |
| 1→0 M1，p0=.8/p±1=.1 | finite | −.777778 | 2.7 | 简单M1正控制 |
| 2→1 M1，p=[.05,.2,.5,.2,.05] | NaN | −.391304 | 2.3 | k4禁戒比值失败，强度非零 |
| 1→1 M1/E2，δnative=.2 | NaN | .518519 | 1.296 | k0 cross项0/0 |
| 同1→1 pureMP3 / mixedMP304 δ0 | finite / NaN | .636364 | 1.65 /1.65 | 同物理pure端点、不同代码分支 |
| 9/2→9/2，σ/J=.56，δRB0/−.85 | NaN /NaN | .340288/.017054 | 另见实际JSON | 正确native0/+.85；无新fit |

本run首轮Na测试曾直接把−.85送入native，并以两branch命名；这只验证那个native输入，不是L26的正确branch身份。原input/result保留，`ucgretina-core-identity-correction.json`记录纠正；数值重放前再冻结v2、核F/R相位桥，canonical只采用v2。ctypes首次加载也因static TLS失败（编译0、physics尚未执行），命令级LD_PRELOAD后执行0，未改系统配置或原科学输入。

复跑入口：[core脚本](../../system/scripts/day16_ucgretina_stokes_audit.py)、[oracle脚本](../../system/scripts/day16_ucgretina_stokes_oracle.py)；输入与实际编译/错误/结果保存在Day16原run的`ucgretina-core-audit-input-v2.json`、`ucgretina-core-audit-v2.json`和`ucgretina-core-validation-v2.json`。原第三方源码、生成C++与binary只在repo tmp，不stage。

## Competing Interpretations and Limitations

- `0/0×F`是所选固定源代码和helper下的可重复失败，不推断原作者用了相同commit、是否有未公开修改或是否曾请求这些路径。Morse的pure2→0通过控制，是必须同记的反证。
- 公开ITDecay按gamma处理Stokes，代码明确暂不处理conversion-electron polarization。这里没有扩展ICC或寿命课程，也不把非γ路线假为同一polarimeter observable。
- 本次trace是声明PSD对角布居/实振幅/单emitter；轴旋转、一般κ/coherence、无强度点、真实Compton事件与background仍有额外检查。没有对整个simulation作correct/incorrect二值认证。
- Geant4两helper共享公式/数学服务，不是独立实验；Morse calibration、tuning与同代码simulation也共享输入。若以后做修复设计，应保留literal失败，另算先消去公共CG的有限表达式，不能用“遇NaN置0”代替物理检验。
- Q的jointkernel等式只在明确的azimuth/reference/acceptance假设下成立；缺matching selection时，不能由本页局部KN核直接重算原Q或选择1041的δ支。

## 有限系数与非轴对称tensor续核

设`Cminus=C(L1,L′−1→k0)`、`Cplus=C(L1,L′1→k2)`。由原FCoefficient及3j–CG关系，在本页state ordering下：

`H_k(L,L′)=(-1)^(L−L′+Ji+Jf−1) Cplus {L L′ k; Ji Ji Jf} sqrt[(2Ji+1)(2L+1)(2L′+1)]`。

它等于原式的`(Cplus/Cminus)F`，但求值时从未除以Cminus。k<2时Cplus直接禁戒；不是先浮点0/0再截断。独立设计脚本[finite product](../../system/scripts/day16_ucgretina_finite_product.py)保存原finite处的残差和未闭合的general测试，不覆盖原literal失败。输入/冻回执在本run `ucgretina-finite-product-input-v2.json`及其freeze。

初始一般密度矩阵CG桥采用升序m、rho_mm′，`rho_kκ=sqrt[(2J+1)/(2k+1)]Σ(-1)^(J−m′) C(Jm,J−m′→kκ)rho_mm′`。六个事前固定PSD案例包括旋转后的Morse密度、oriented M1、整数/半整数coherent M1/E2与E1/M2。first-result对nonaxial量不闭合被完整保留，未从数据拟合选择新phase。

随后按原代码的关联Legendre/小d恒等式比较**同一tensor**：原角度sampler核与Stokes归一核不是相同指标顺序。实际抽取旧Legendre函数执行后，Pnorm/dκ0恒等式最大差5.45×10^-15，小d转置恒等式差4.27×10^-15。相同tensor下角度sampler与photontrace的I全闭合，而ITDecay用于归一Stokes的核未闭合；这里未声称实际gamma角采样本身错误。

把IT收缩按解析恒等式写成dκ0仅是诊断等价表达式：六案例的I/Q/V差≤1.56×10^-15，U仍严格反号（U_variant+U_trace≤5.07×10^-16）。因此没有把“消去0/0”称为一般tensor完整修复。

为隔离U，另冻结v=[i,0,1]/sqrt2、pureM1 1→0的literal控制。它无奇κ也无禁戒CG比，原核直接运行；eθ/eφ Jones定义固定为Q=Jθθ−Jφφ、U=2ReJθφ、V=2ImJθφ。前向解析态给U=+1，选定非pole角的原U却为相反号，I/Q/V匹配。G4消费端的`dirx=sinψ cosΦ,diry=sinψ sinΦ`及`−P2 sin2Φ`把该区别传给Compton方位分布。这里的原发射实现、消费端轴、photontrace定义与条件预测同时保存；没有调整轴/sign使结果通过，也未上报或改写外部仓库。

pole和零强度分别处理：actual old/SDK `d_k00(cosθ=−1)`在k0/2/4均给1，原先预想NaN不成立；pureE2 2→0、|m0>在θ0的IQUV恰为0，normalized Stokes为undefined。两个控制都保留，不能用一个“除0”标签混同。

复跑还包括[angle-kernel比较](../../system/scripts/day16_ucgretina_angle_kernel_audit.py)与[evenκ U控制](../../system/scripts/day16_ucgretina_even_kappa_u.py)，均在同一命令级preload/PYTHONPATH下执行exit0。真实event/geometry/response/Cov、一般量子相位和后处理重建仍有范围边界，未发布通用patch或新实验结论。

## Knowledge Impact and Learning Decision

`supports`统计张量/P-A-Q分层和完整phase合同；`revises`“public producer入口尚未找到”的缺口，新增可复核literal-core边界；`limits`将pureE2 benchmark推广到任意mixed/highrank路径。保留所有needs_review，不新增独立实验或正式Day17信用；Day16同session继续到原deadline。

## Extracted Pages

- [[compton-polarimetry]]：开关/统计张量/Stokes/阵列响应的独立合同。
- [[gretina-25na1041-polarization-response-contract]]：正确native branch与public-code readiness，未重测δ。
- [[multipole-mixing-ratio]]：符号桥不等于第二物理解，purelimit还须检查代码分支。
