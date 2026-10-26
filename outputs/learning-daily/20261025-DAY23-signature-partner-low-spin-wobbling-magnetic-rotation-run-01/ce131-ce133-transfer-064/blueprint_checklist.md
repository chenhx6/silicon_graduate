# 用户后续分析可执行蓝本：从真实观测到模型检验

这是方法合同，不是声称用户已经完成这些步骤。每项都需要实际run/response/谱线输入，不能搬用另一核的δ、g、τ、Q、Harris参数、阵列比值或band编号。

## A. 固定来源、带身份与计数单位

- [ ] 为每个核/采集建立manifest：run、反应、beam/target、active detector mask、角度、触发/fold、死时间、Doppler及gain处理、sorting版本。
- [ ] 单独注册AW13-Gammasphere131Ce、WK22-AFRODITE133Ce、Ding-GALILEO131Ba；AFRODITE13/8的跨文差异以actual mask核，不任择文献。
- [ ] 逐level登记Ex、Jπ及tentative括号；逐transition登记Ei/Ef、初末band、Eγ、Iγ定义、峰/门/污染、multipolarity、δ、Cov/limits。
- [ ] band对应表按head/configuration/link核；“两核都叫Band4”“同spin”不作为合并条件。131Ce Band3=61.8keV低激发，不误作133Ce的1/2+ground。
- [ ] 多次论文/学位论文或转载值写source lineage；不因多篇引用把同event算成独立实验。

## B. 608/609keV的2D/3D分解练习

直接原件：WK22 PDF62–63/Table5.2 PDF67/Fig5.2 PDF68。608.3是Band4 19/2−→15/2−带内E2；608.7是Band4 15/2−→Band1 13/2−mixed。399.3与209.0是绕过608.3直跃迁的两步支路，仍可与608.7连接。

1. [ ] 保存608区原通道、binning、gain drift、分辨率、非Gaussian尾、最近contaminants及其时间/角度响应。不要先用round608/609标签把两线分成“纯门”。
2. [ ] 原文607–609和608–610门均含重叠贡献；为每个门建立包括两个line response及背景的forward mixture。峰间.4keV是否能可靠分解取决于actual resolution/counts，不能承诺两Gaussian拟合就唯一。
3. [ ] 在2D matrix用独立clean已知线分别选择母/末路径；同时看608区、209、399及下游Band1线。记录门宽/左右sidebands/背景归一和每个角组efficiency，不用两幅raw峰高直接相减。
4. [ ] 在3D cube使用两条独立clean gates检验拓扑。例如209+399路径应走两步支路；608.3直支路不能与这两条同时属于同一单次cascade，仍可能与608.7相接。需要比较条件谱，不能因doublet门谱里两者都出现就连成608.3→209→399的假串联。
5. [ ] 比较871与936门：490/380在936门出现、871门缺失支持平行支路，但缺峰先检查预期检出率、背景和上限。以response折叠后检验候选纲图，不把“未见”编码成概率严格0。
6. [ ] 输出各gate对各candidate line的response/acceptance矩阵、联合Poisson/合适计数likelihood及条件可识别性。若多种peak decomposition/level graph同样可行，保留多个解与所需additional gate，不强选一个。
7. [ ] 反证练习：故意把608.7污染归给608.3，检查哪些互符合/能量闭合破坏；故意把anti-coincidence当零，检查低counts下的假排除。
8. [ ] 验证产物应含原/模型gated spectra、残差、profile或bootstrap边界（如actualdata允许）、line identities和contamination ledger。没有真实counts时只做条件设计，不填新CI。

## C. AD / RAD / DCO / Rac的实际口径

|来源/方法|角组与门定义|源报参考量级|不可搬用的前提|
|---|---|---|---|
|AW13 Gammasphere angular-intensity R，PDF54 Eq3.7|near35°/145° target intensity比near90°，按实际门列表|pure stretched dipole约.5，stretched quadrupole约1|与该角组、gain/效率、取向、门平均及已知参考线相配；不是DCO一律.5/1|
|WK22 AFRODITE RAD，PDF59 Eq4.6|target135°/90°，两边gateγ2均来自all detectors|stretched quadrupole约1.3、dipole约.8|all-angle门简化在其实际acceptance/feeding/取向近似下成立，非任意有限阵列的精确门独立定理|
|WK22一般DCO，PDF59 Eq4.5|I135(target,g90)/I90(target,g135)，交换门角|gateE2：quadrupole约1、dipole约.5；gatedipole：dipole约1、quadrupole约2|门multipolarity、δ、spin sequence、alignment、有限几何及能量依赖均保留|
|Ding2021 GALILEO131Ba Rac，原PDF2|90°/152°两点相关，具体geometry25HPGe=10/5/5/5在90/119/129/152°|quad约1.54、dipole约.77|这些数属于131Ba的该次数据/标定，不是133Ce或用户阵列的新实测阈值|
|Ding2021 AFRODITE133Ce Rac，原PDF2|90°/135°，该文写8clovers=4+4|quad约1.27、dipole约.74|与WK22的13clover/1.3/.8分别登记，先核actual detector mask，不合并作“更精确统一阈值”|

- [ ] 对每条target保存角分组计数、gating role、sideband、效率、归一和Cov；角组相除前先核实际被条件化的cascade/选门。
- [ ] 用同run已知E2/dipole/reference fit alignment/attenuation及finite geometry，reference本身的mixing/feeding不确定度进入响应。
- [ ] mixed M1+E2不能靠“介于两个参考值之间”线性插值得δ。拟合角分布或ratio response，保留相位与全部允许roots。
- [ ] E1/M1都可属dipole；仅角比不充分区分electric/magnetic。若用偏振，需actual plane convention、a/Q(E)标定及其Cov、共同gate/污染模型。
- [ ] 同一δ²的rate不含符号，AD/P干涉项可含符号；不把“P正号”单独当唯一大δ解。
- [ ] 不把源论文没给P/δ likelihood解释为用户数据必然没有这些信息；本轮输入不足是本轮边界。

## D. 同母态branch与out/in、out/out

- [ ] reference b必须与混合线a同一个实际母态，且其E2成分/纯度、末band、branch identity明确。先查是否重叠峰、同能异transition或不同mother同spin。
- [ ] out/in：a连到partner/其它band，b在母band内；out/out：a与b均连到其它band，但multipole/spin差不同。两类分母不是同一个observable。
- [ ] WK22 624.6/794.8可按同母态out/out建立；464.4/608.3为out/in，464.4/982.0为out/out候选；582.7/577.8为out/in。582的out/out仍需actual reference line，不能造817.7keV线与强度。
- [ ] AW13 Band4内243.7与连接611.1具有相同17/2−→15/2−spin差但不同终band，不能互换。504.9、871.2是Band1→4，538.3、611.1、994.3、1108是Band4→1/yrast，须按arrow/table/prose逐线核。
- [ ] 由共同母态上方clean gate取得branch yields，减少feeding差异但仍核gate acceptances、summing、conversion、efficiency及相对归一Cov。不能假定共享母态就消除一切系统误差。
- [ ] 光子yield口径下，令u=Ya/Yb、Ea/Eb均MeV：
  rE2=u·δ²/(1+δ²)·(Eb/Ea)^5；
  rM1≈.7u/(1+δ²)·Eb^5/Ea^3（μN²/(e²b²)）。
  若yield已总转换校正，先恢复或显式重写相应α口径。
- [ ] AW13 Eq5.6系数.697、δ=0是其原假设；不能把“ratio已测”变成δ已测。δ不为零时固定branch ratio的rM1相对δ=0结果除以1+δ²。
- [ ] δ/rE2/rM1有共同输入约束；连同E拟合后的S，不能作独立数据多次计权。
- [ ] different mother不能代数消去τ；相同spin但不同level也不能。缺reference写missing，不补0、不以能差臆造线。

## E. 从τ到absolute B：补什么、如何选方法

现有AW13网络只有相对比值，不意味着131Ce所有态都缺τ。优先把Li2004、Singh2016的具体Ei/Jπ/Eγ/branch、mean-vs-half-life及实验谱系与当前网络核对；static Qs/g(TDPAD)另列，不把它当transition τ或Qt。

- [ ] 将所有partial photons与conversion/其它退激通道放在完整branch账本，建立每次母态衰变的实际光子概率；meanτ与T1/2用τ=T1/2/ln2转换。
- [ ] 有τ和完整BR/ICC后，先求各γ分量partial rate，mixed线按δ拆E2/M1，再用相应Eγ幂和单位求absolute B。缺测branch/limit进入误差或boundary，不能把相对Iγ直接除τ。
- [ ] DSAM可行性由recoil velocity history、target/backing stopping、τ相对slowdown、角度/能量分辨和line purity决定。需coupled side-feeding、stopping-systematic、各角lineshape/gate response；不是从谱上“峰窄”就报唯一寿命。
- [ ] RDDS可行性由recoil flight/target-degrader geometry、距离校准、velocity distribution、shifted/unshifted分量分离、feeding/门条件决定。DDCM或Bateman/完整feeding处理必须与实际观测定义相配。
- [ ] 先用目标line的τ范围与模拟response选择DSAM/RDDS/其它timing，而不是给一个跨实验普适ps分界。低counts下允许限值，不把τupper/lower或effective lifetime与finite fit同权合并。
- [ ] partner-resolved τ和同motherbranches能提供独立absolute-strength检验；仍需完整Jπ/δ、组态/模型预测与竞争解释。DSAM/RDDS不是wobbling、chirality、TiP、MR/AMR的普适必要充分认证。
- [ ] 多方法/多篇论文可能共享feeding参数或转载同τ；核实际dependency后再称独立。

## F. 模型训练、holdout与迁移失败

- [ ] separate131Ce CSM/TRS与133Ce正/负parity QTR；Harris参考、ε/β、γ轴、Coriolis χ、gs/gl/gR、Q、λ/Δ及空间均显式冻结。
- [ ] 先闭合GAMPN→ASYMO→PROBMO actual版本/header/input/output；ε列约5–6而λ正文50.6/51.0的单位/零点未恢复，不以ħω≈8换算猜实际输入。
- [ ] 训练量选定后，拿未定标的δ、branch、absolute strengths、static moments或links作holdout；能量和由其派生的S不算两份独立证据。
- [ ] Table6.3归一、Table6.9/10与图尺度、Fig6.16 caption分母冲突分别保留；不得任选图值“优化”到理论优胜。
- [ ] 高spin3qp crossing只在sameconfiguration/spin/branch ledger下比较；不以不同核同Band5/6/7编号相互替代。
- [ ] 输出observable-by-observable成功/失败，不以一项能谱符合认证全部collective labels；也不以一个toy数学控制宣布作者模式解释全错。

验收产物：原始manifest、level/transition edge table、gate response、全部δ根与Cov/limits、branch reference ledger、absolute-strength需求、模型输入及holdout表。缺actual data时，可以完成合同与source arithmetic；不能伪造真实拟合完成状态。
