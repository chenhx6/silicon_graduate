---
type: source
title: "Nolan & Sharpey-Schafer 1979 - The measurement of the lifetimes of excited nuclear states"
aliases: [Nolan Sharpey-Schafer 1979 lifetime review]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: review-method
reading_depth: deep-read
title_original: "The measurement of the lifetimes of excited nuclear states"
authors: [P. J. Nolan, J. F. Sharpey-Schafer]
journal: "Reports on Progress in Physics"
year: 1979
volume: 42
pages: "1-87"
canonical_source: "Nolan & Sharpey-Schafer, Rep. Prog. Phys. 42, 1 (1979)"
library_file: "raw/papers/gpt/high-spin-20260920/review/1979_Nolan_Sharpey-Schafer_The measurement of the lifetimes of excited nuclear states.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/review/1979_Nolan_Sharpey-Schafer_The measurement of the lifetimes of excited nuclear states.pdf"
raw_sha256: "5e20f735e995021f4a0eb8c1a937acedeee53509caed3ffa2cd8ddaa794bbc4f"
nuclei: [lifetime-methods]
reactions: []
experiments: []
models: [DSAM-stopping, recoil-distance, electronic-timing]
observables: [nuclear-lifetime, gamma-energy-shift, attenuation-factor, transition-strength]
methods: [doppler-shift-attenuation-method, recoil-distance-method, electronic-timing, Coulomb-excitation]
tags: [lifetime, DSAM, RDM, Doppler-shift, review, nuclear-structure-method]
---

# The measurement of the lifetimes of excited nuclear states

## Bibliographic Record

- P. J. Nolan and J. F. Sharpey-Schafer, *Reports on Progress in Physics* **42**, 1–87 (1979).
- 规范文件：`raw/papers/gpt/high-spin-20260920/review/1979_Nolan_Sharpey-Schafer_The measurement of the lifetimes of excited nuclear states.pdf`。
- 88-page review PDF (printed pp.1–87); full chapter map and method comparisons read.

## Scope and Reading Depth

- Fully read: Doppler-shift techniques (DSAM, stopping theories, RDM), electronic timing, blocking, fission isomers, indirect Coulomb/electron/resonance/capture methods, exotic techniques and accuracy/reliability comparison.
- Not covered: reanalysis of every historical lifetime experiment, modern stopping codes and post-1979 detector developments.

## Key Evidence and Method Logic

- Lifetime `τ=ℏ/Γ` links measured widths/decay probabilities to electromagnetic matrix elements; complementary spins, parities, branching, multipole mixing and conversion data are required for model comparison.
- DSAM compares Doppler shift/attenuation with recoil slowing time (~`3×10⁻13 s`), requiring electronic/nuclear stopping models, recoil velocity, feeding and side-feeding treatment.
- RDM compares decay time with recoil flight between foils (`~5 μm–2 cm`), while electronic timing and blocking cover other lifetime ranges.
- Indirect methods infer widths from Coulomb excitation, electron scattering, resonance fluorescence or capture; products of matrix elements and ground-state access impose boundaries.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| NS79-1 | DSAM and RDM dominate direct lifetime measurements in the `10⁻18–10⁻6 s` range but rely on stopping/flight-time models. | method-framework | direct | PDF Ch.II, Fig.2 | true |
| NS79-2 | Lifetime interpretation requires complementary spin/parity, branching, mixing and conversion information. | method-boundary | direct | PDF pp.3–6 | false |
| NS79-3 | Coulomb excitation and other indirect methods measure matrix-element products/widths rather than direct decay time. | method-boundary | direct | PDF pp.4–6, Ch.VI | false |

## Summary

Nolan & Sharpey-Schafer is a foundational lifetime-method review that calibrates DSAM/RDM, stopping, feeding, timing and indirect-width assumptions. It is the method lineage for later `61Ni`, `165Tm`, `131Ce` and high-spin lifetime sources.

## Competing Interpretations and Limitations

Historical stopping powers, feeding models, detector resolution and side-feeding assumptions can dominate lifetime uncertainty. Direct and indirect methods are not interchangeable; each has a range, observable and input-data boundary.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| NS79-AR-1 | Method chain | Reaction/recoil → Doppler/timing/flight observable → stopping/response model → τ → transition strength. | PDF Chs.II–VIII | self-checking |
| NS79-AR-2 | Transfer condition | Reuse only with matching recoil velocity/material/feeding/detector and uncertainty model. | PDF Ch.II, Sec.VIII | active-L3 |
| NS79-AR-3 | Independence | Review; historical examples are not new experiments. | Scope/References | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` and strengthens [[doppler-shift-attenuation-method]] and lifetime evidence boundaries.
- Persistence: link to Jensen 2001, Wadsworth 1977 and the `131Ce` lifetime project.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `NS79-P0-1`: lifetime-derived strengths cannot be reused without stopping/feeding and method-specific uncertainty mapping.

## Extracted Pages

- Methods: [[doppler-shift-attenuation-method]]。


## Day18内无学分Day19预习：时间窗与交叉方法边界

本段为同一Day18 session在Radeck之后的下一卡无学分preview。原页面旧字节、旧NS79-1–3、`unreviewed`状态和既有flags均保留；以下新claims是本session targeted page verification、`needs_review: true`，不把旧完整阅读记录当本次盲读。核对PDF3 contents、PDF6–7 DSAM/RDM框架、PDF10–12 attenuation与side-feeding、PDF19–23 Coulomb/feeding、PDF78–81 accuracy comparison；没有重建历史实验或现代fast-timing source。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| NS79-P19-1 | review把直接方法范围置于约10^-18–10^-6 s；DSAM把寿命和固体/气体减速时间比较，RDM把寿命和5 µm–2 cm两箔间飞行时间比较。此为方法框架，不是任意核素的硬可用区间。 | method-window-framework | direct-review | PDF3 contents；PDF6 | true |
| NS79-P19-2 | DSAM centroid/attenuation的F=〈v〉/v0需Stopping theory；作者区分electronic与nuclear stopping的速度域，并强调F(T)曲线依该理论。 | dsam-stopping-dependence | direct-review | PDF6；PDF10–11 Eqs2.4–2.5/Fig6 | true |
| NS79-P19-3 | 重离子fusion-evaporation中side feeding可在slowing time内发生；上级gate可削弱部分feed，但初始速度/feeding component仍须响应模型。Coulomb excitation可减少side-feeding time，因为目标态由散射过程直接布居，但只适用于可达低能态/稳定体系等条件。 | feeding-method-boundary | direct-review | PDF19–21/Figs11–12 | true |
| NS79-P19-4 | RDM在原理上不需stopping theory且可高精度，但短寿命端受靶—stopper separation标定困难；DSAM/RDM约1–20 ps有重叠，交叉核验本身很难。 | cross-method-overlap-boundary | direct-review | PDF78–81/Table7 | true |
| NS79-P19-5 | review明确警告：DSAM与Coulomb-excitation yield若相合，可能因两者共享相同（甚至错误）stopping powers；不同方法相合不自动等独立确认。 | shared-systematic-counterexample | direct-review | PDF80–81/Table7/Fig56 discussion | true |
| NS79-P19-6 | 对同一候选寿命，方法选择应先看响应主导项：DSAM需stopping/feeding/velocity；RDDS需distance/shifted-US/finite-stopper/deorientation；fast timing需prompt response/time-walk/background。Nolan只直接支持前两者，第三项仍是本preview设计边界，不能冒原文现代结论。 | decision-tree-boundary | synthesis-and-boundary | NS79-P19-1–5；R12-P19-1–10 | true |
| NS79-P19-7 | 由寿命到strength还需spin/parity、branching、mixing、conversion和efficiency；Coulomb-excitation yield本身还受feeding、absolute efficiency、dead time、angular distribution、stopping/target absorption等输入影响。 | strength-input-contract | direct-review | PDF4–5/Eq1.2；PDF65–67 | true |
| NS79-P19-8 | 本session仅完成Nolan targeted pages和方法决策树边界；不把Radeck/Nolan旧文献变成正式Day19 credit，不打开Day20；原Nolan旧full-read status不被改成新盲测。 | actual-scope-and-credit-boundary | task-reading-receipt | nolan-protected-prefix-008；day19-preview-state-007 | true |

本段[访问/身份回执](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/nolan-protected-prefix-008.json)冻结原页/raw hash；没有取得历史DSAM/RDM原计数、现代fast-timing producer或jointCov。与[[radeck-2012-deorientation-lifetime-98ru-rdds]]的R12-P19段合用时，仍须区分综述方法框架、Radeck实测response和本任务条件推断。

正式Day19仍需新session逐卡验收；本preview只补方法边界和决策树，不授课程学分。


## Day18内无学分Day19预习补充：电子计时响应

继续核对本次方法预习的PDF48–52（electronic timing）并保留旧页prefix/status。新claims仍`needs_review: true`，不是新实验或正式Day19学分。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| NS79-P19-9 | 电子计时review给出约10^-11–10^-6 s的有效范围；production time由脉冲束、粒子或形成γ定义，decay time由退激γ定义，时间谱是指数衰变与PRF卷积。 | timing-window-and-zero-time | direct-review | PDF48–49 Sec3.1–3.2/Eq3.1/Fig34–35 | true |
| NS79-P19-10 | PRF由prompt decay测得，受探测器距离/固体角、charge-carrier统计、rise time和电子学影响；slope方法适合τ长于PRF尾，centroid方法比较prompt/delayed first moments，可测远小于FWHM的差，但要求系统误差控制。 | prompt-response-contract | direct-review | PDF49–50 Sec3.2；PDF52 centroid examples | true |
| NS79-P19-11 | 电子计时选择应同时记录prompt calibration与delayed spectrum；对小于PRF FWHM约0.5–1%的差异，PRF随γ能量/门条件变化必须核验，不能把统计样本大直接换成窄响应。 | timing-calibration-boundary | direct-review-and-synthesis | PDF50/52；NS79-P19-10 | true |
| NS79-P19-12 | 由DSAM/RDM/electronic timing组成的选择树仍是响应主导的条件设计：DSAM看stopping/feeding，RDM看distance/finite-stop，timing看PRF/zero-time/walk/background。三者结果相合才有交叉价值，若共享reaction/branch/model仍不自动独立。 | complete-preview-decision-boundary | synthesis-and-boundary | NS79-P19-1–11；R12-P19-1–10 | true |


### 2026-10-20 preview scope复核

NS79-1旧行/flag原样保留，但其10^-18–10^-6s不能读成DSAM/RDM各自全域：PDF5/printed4 Fig2画的是全套direct/indirect方法的范围，DSAM与RDM只是其中分段；PDF4限定的是review总scope。NS79-P19-1/4及方法选择页按这一范围使用。

本次Nolan读取是定向段落/选表，并非全88页。早先工具对部分页只返回开头1800字，属于页面内选段而非完整页认证；2026-10-20晚再次完整核PDF4–7及78–81并视觉核PDF5 Fig2、PDF79 Tables5–6与PDF81 Table7/Fig56。PDF48–52电子计时正文已另完整核。Table7/Refs只是review转引；Hermans1977、Schwalm1977原body未得前不当primary已读或新独立测量。


## Day 19正式课程：全景时间测量方法选择与物理时钟决策树

checkpoint008更正前轮范围与来源归因。本次实际读取PDF80–81可靠性比较；现代MSCD与DDCM不得倒灌为1979原文直接结论。旧NS79-1–3/preview与flags保持，尚不认证本次88页完整主线。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| NS79-D19-1 | PDF80印刷78说DSAM/RDM重叠约1–20ps且短τRDM受系统误差；PDF81印刷79的“相同（也许错误）stopping相合”直接对象是DSAM line shape与Coulomb-excitation yield的same-data分析，不是RDM。 | cross-method-attribution | direct-review | printed78 overlap paragraph；printed79 Fig56 discussion | true |
| NS79-D19-2 | superseded：PRF卷积/zero-time可由本综述电子计时段核；“必须MSCD”和任意相同E自动消所有walk不是此1979来源结论。现代方法需另核Régis原件和detector-pair PRD。 | attribution-correction | source-boundary | NS79-P19-9；NS79-P19-10 | true |
| NS79-D19-3 | superseded：直接feeder gate/DDCM仅在所选级联、正确分量/归一/污染及finite-response处理下消去相关feeding，不得归为此处1979的“全部已知未知feeding严格消失”定理。 | method-transfer-boundary | synthesis-and-boundary | NS79-P19-3 | true |
| NS79-D19-4 | 标称方法窗口随反应、速度、几何、PRF、门和材料改变；TDPAD主要测超精细频率/矩，寿命须人口衰减或匹配计时。不能将本表窗口当通用硬阈值。 | window-boundary | synthesis-and-boundary | NS79-P19-1 | true |
| NS79-D19-5 | 寿命到B需匹配state/branch、photon概率、ICC/mixing；Qt到形状另需几何和模型。输出多个派生量不增加独立证据。 | strength-input-contract | synthesis-and-boundary | NS79-2 | true |


## Day19本session主线补读：介质、距离响应与校准反例

checkpoint009实际完成88-page PDF的全文文本读取（cover、contents、printed1–86正文/References及一页图版）；不是每个历史引用的primary重读，亦未认证全部56图/所有公式的独立重构。关键视觉范围单记scope，OCR不清公式不用猜补。metadata1–87保原记录；本PDF末印页86并有单独图版与cover，不据此擅改书目。

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | needs_review |
| --- | --- | --- | --- | --- | --- | --- |
| NS79-D19-6 | 用气体减速可将DSAM扩至约10–1000ps；气压/局部气体密度与束流加热使同τ的F(P)受影响。该历史设计不支持“DSAM固定只到2ps”的硬窗口，也不保证气体DSAM精度胜过RDM。 | method-window-and-medium | direct-review | review-not-new-primary | PDF22 printed20 gas targets；PDF24 printed22 Fig16 | true |
| NS79-D19-7 | 高β有利峰分离却可增stopper慢化时长；综述Yb例约5ps，短τ端需DSAM式stopped-peak响应修正。无feeding时该效应可表现为R(d)乘常数/距离原点平移，宜用zero-distance line shape检验；不能从大β直接推出无材料依赖。 | finite-stopping-and-distance-alias | direct-review | review-quoted-example | PDF38 printed36 Sec2.4.3；PDF39 Fig28 | true |
| NS79-D19-8 | 综述建议约55°使P2近0以减弱退取向，但同时讨论a2/a4不同时标；不等价于P4或有限角接受/boost也自动消。Radeck实际高β仍逐分量/逐角修正，二者适用条件须对齐。 | angular-design-boundary | direct-review-and-synthesis | same-method-framework | PDF43 printed41 Sec2.4.6(d) | true |
| NS79-D19-9 | 电子计时slope看PRF tail与寿命相对尺度，centroid需对应prompt和delayed同条件。原例强调PRF随能量同时测；综述转引219Rn 269keV的microwave39(5)ps与electron recoil-distance6.0(1.4)ps不合，并提出低频prompt替高频测量可能有系统误差；不是本session已独立核两primary。 | prompt-calibration-counterexample | direct-review | review-dependent-originals | PDF50/52 electronic timing；PDF76 printed74 final paragraph | true |
| NS79-D19-10 | Table6的21Ne历史RDM从早期约20ps到后期约10ps，综述列distance scale、feeding和stopper靶材沉积等系统风险；一个小quoted statistical error不认证方法无偏。仅作review evidence，不重算或平均这些历史实验。 | precision-versus-reliability | direct-review | review-compilation | PDF79 printed77 Table6 and preceding discussion | true |


### Day19条件桥：常数finite-stop因子与距离原点

NS79-D19-7的“无feeding时常数因子等于origin shift”不能认证所有峰定义。本任务在[[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-D19-8/9给完整count partition：全尾归US、部分尾分配、丢尾后再归一是三个不同observable。只有特定的全count/常数q合同下才出现常数因子，机械零点/foil慢化/peak acceptance须分开核验，不反认原作者的实际job。


### Day19同一寿命的条件方法设计

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| NS79-D19-11 | Eq2.9/2.10在非常粗略的1D指数减速v(t)=v0 exp(−t/s)下给F=s/(s+τ)，不是通用stopper transport。新τ20ps控制取s=.3/20ps得到F=.014778/.5；假设σF=.005时，F项的局部τ相对误差约34.34%/2%。若s未知，F只识别τ/s，共同比例缩放不变。气体DSAM不能因F≈.5就免去密度/stopping/feeding校准。 | simple-response-and-readiness | direct-review-and-task-derived | PDF25 printed23 Eqs2.7–2.10；NS79-D19-6；same-lifetime-readiness-result-012.json | true |


## Day19新原读：55°魔角对P4与有限孔径的局限

本session新读PDF36–38（Alexander/Bell装置、电容测距、机械零点与已知寿命标尺）及PDF43（退取向与55°角）。raw hash保持5e20f735e995021f4a0eb8c1a937acedeee53509caed3ffa2cd8ddaa794bbc4f。旧flags保留。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| NS79-D19-12 | PDF43明确退取向由真空高离化原子产生，A≈150区a2/a4衰减常数约40/15ps。综述建议用55°(cosθ≈.57)使P2≈0最小化效应；但P4在54.74°为−7/18(≈−.389)，在55°为−.385，魔角完全不消除P4。若a4显著，55°仍有退取向偏差。 | deorientation-and-magic-angle-boundary | direct-original-and-derived | PDF43 printed41 Sec2.4.6(d) | true |
| NS79-D19-13 | 有限探测器半开角或不同孔径形状对角响应有卷积；自设10°圆形立体角保持P2魔角零点，但全方位极角带会在同一中心角重新引入P2项；在β=.045下实验室54.74°在静止系变为56.869°、P2=−.0519。高速RDDS不可直接套实验室魔角。 | finite-aperture-and-aberration | direct-and-task-derived | PDF43 Sec2.4.6(d)；angular-acceptance-contract-result-015.json | true |

Knowledge Impact and Learning Decision：limits将55°当成消除全部角分布/退取向效应的通用方案；supports在RDDS/DSAM设计中将P2、P4、有限孔径和光行差作为最小角响应清单。保持未取得Guidry/Ward历史原件的边界。

## Day19重叠窗口与共享阻停系统误差审计

依据独立审计程序 day19_nolan_dsam_rdm_overlap_audit.py 的 14 项检验与基准输出 nolan-dsam-rdm-overlap-result-029.json，系统核准了 Nolan 1979 综述第 8 章中关于 DSAM 与 RDM 在 $1\text{--}20\text{ ps}$ 重叠区对比及共享阻停反例的事实：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| NS79-D19-14 | checkpoint088纠正：原Table7最后列为tau_RDM/tau_DSA，数值1.02/1.28/1.06/1.45/1.16/1.13，后两行为36Cl不同态、没有30P。此前反向比值及8%或9%stopping低估归因撤回；不将综述转引当新primary或合并出新绝对校准。条件DDCM门依赖纯度/分量/归一与finite stopping，不保证所有feeding免疫；四方法物理响应不同不等共享输入Cov为零。准确表见NS79-D19-18。 | overlap-and-shared-stopping-contract | direct-review-and-derived | PDF80–81 printed78–79 Table7/Fig56；nolan-dsam-rdm-overlap-result-029.json | true |

## Day19量化审计：全景时间方法决策树、时钟正交性与最小校准八项清单

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_nolan79_method_selection_tree_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/nolan79-method-selection-tree-result-073.json`，核准了针对 Nolan 1979 综述重叠窗口、全景方法选择决策树与最小校准规范的系统学审计：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| NS79-D19-15 | checkpoint088纠正：原Table7最后列为tau_RDM/tau_DSA，数值1.02/1.28/1.06/1.45/1.16/1.13，后两行为36Cl不同态、没有30P。此前反向比值及8%或9%stopping低估归因撤回；不将综述转引当新primary或合并出新绝对校准。条件DDCM门依赖纯度/分量/归一与finite stopping，不保证所有feeding免疫；四方法物理响应不同不等共享输入Cov为零。准确表见NS79-D19-18。 | task-nolan-method-selection-tree-audit | derived-and-boundary | PDF78-81 Table7, Fig56; nolan79-method-selection-tree-result-073.json | true |

## Day19量化审计：21Ne历史寿命双倍发散、早期RDM四大失效模式与高速DSAM对账定理

**checkpoint088：撤回旧科学认证；原标题保留为历史anchor。**

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| NS79-D19-16 | checkpoint083修订：PDF79/印77 Table6中Beck1977为RDM(18O,n)，Grawe1977为DSAM(20Ne,p)，Grawe打印10(+10/−5)ps而不是10.1±.6。Rowe为RDM(20Ne,p)。不对这些历史、异方法、不对称误差且独立性未核的数据作新加权真值或12.48sigma认证。综述列feeding、distance scale、靶材沉积等可能系统风险，未逐实验给35um、40%或35ps的原因参数；这些和“DDCM根除全部风险”均撤回。 | source-and-analysis-correction | direct-where-reread-otherwise-withdrawn | checkpoint088 source scope and rejection registry | true |

## Day19量化审计：26Mg多方法寿命对账、共享阻停假相合与无阻停基准定理

**checkpoint088：撤回旧科学认证；原标题保留为历史anchor。**

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| NS79-D19-17 | checkpoint084撤回错行对账：PDF79/印77 Table5的480(50)fs为Endt/van der Leun1973采纳值，脚注明确含前八项测量，不是RDM测量；710(70)fs为Lees1973(e,e′)。McDonald1971是700(300)fs RDM；Durrell1972是610(180)fs DSAM。此前498(108)fs“无阻停均值”误用行身份，所有相对伪基准的sigma和2um接触死线归因撤回。Schwalm两输出共享同次数据、stopping作用不同；正文只说相合可能共享错误stopping，不证明15%真实偏差。 | source-and-analysis-correction | direct-where-reread-otherwise-withdrawn | checkpoint088 source scope and rejection registry | true |

## checkpoint088：原表行身份、比值方向与共享输入

本轮定向读PDF79–81（印77–79），视觉核PDF79 Tables5/6和PDF81 Table7/Fig56；不是重新核验各历史primary。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| NS79-D19-18 | Table5采纳480(50)fs依赖前八行，Lees710(70)fs是(e,e′)，McDonald700(300)fs才是RDM，Durrell610(180)fs为DSAM。Table6中Beck为RDM、Grawe为DSAM且10(+10/−5)ps；不能以旧错配表生成加权真值和12sigma认证。Table7打印比值RDM/DSAM而非倒数，36Cl含两态。Fig56下正文指出相合可能源自相同错误stopping，但beam/recoil slowing的依赖不同，不证明所有时钟完全独立或实际有15%误差。 | literal-table-identity-and-attribution-repair | direct-original-review | PDF79 printed77 Tables5–6; PDF81 printed79 Table7 and Fig56 paragraph | true |

## checkpoint090：总轨迹重标与分量停止修正

本轮定向读PDF25/29/31/32（印23/27/29/30）的相关正文；视觉核PDF25 Eqs2.7–2.13、PDF29 Eq2.16及PDF32 Eqs2.19–2.21。不是新读其全部历史primary。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| NS79-D19-19 | Eq2.7是速度历史的指数寿命加权；Eq2.9的指数减速被作者称first very rough approximation，Eq2.16分别引入fe电子和fn核停止修正，Eq2.19另计投影速度/散射。整体u_k(t)=u_0(kt)且其余合同固定时可导F_k(tau)=F_0(k tau)，但fe单独改变不保证这种轨迹同形。新声明双分量law中仅ke变动令各tau的dln tau_fit/dln ke约−.589至−.517，反例限制旧066的普适反比/双比值免疫；不估任何核素真实停止修正或CI。 | original-nuisance-roles-and-conditional-scaling | direct-review-and-task-derived | PDF25 Eqs2.7–2.13; PDF29 Eq2.16; PDF32 Eq2.19 | true |


## checkpoint092：Nolan主线全文与关键视觉范围

本轮实际读PDF1–88文字，并视觉核27页，含DSAM/RDM主要式/模型比较、level/feeding/circuit图、电子计时Tables2–3、间接方法输入及Tables5–7/Fig56；source-reading-scope-092.json保存逐页角色。PDF12为无编号图版，PDF13印11至末PDF88印86；保留书目1–87，不擅改元数据。不认证全部56图/所有式的独立重构或历史primary已读；旧review/needs_review保持。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| NS79-D19-20 | Fig11人口计算中12+/10+因sidefeeding快于yrast级联，峰值可早于14+；Fig12的上游gamma门定义下游初始平均速度。任意coincidence不等于消除全部feeding，必须声明门/级联和速度选择。 | level-population-and-gate | direct-review | PDF19 printed17 Figs11–12 | true |
| NS79-D19-21 | Eq2.19用平均投影速度；Eq2.20把速度与散射角平均相乘是近似。Table1的MonteCarlo/Blaugrund是同stopping框架的模型输出，非独立实验。Blaugrund平均不提供全部分布；Winterbon的exact受其stopping理论/无限介质前提限制。 | transport-model-boundary | direct-review | PDF32–35 printed30–33 Eqs2.19–2.21 Table1 Fig25 | true |
| NS79-D19-22 | RDM Eq2.22–24的flight/stopped指数有指定分量和初始布居前提，Eq2.27–28另写feeding，Eq2.29加distance-independent背景。电容监控也不能代替distance gain/zero的检验，作者仍建议可行时用已知寿命reference检查。 | rdm-calibration-and-feeding | direct-review | PDF35–40 printed33–38 Eqs2.22–2.29 Figs26–28 | true |
| NS79-D19-23 | Table2分开PRF的FWHM和tau_half（尾部半衰尺度）；slope要求待测寿命相对PRF尾部足够长，centroid依赖同能量prompt/zero-time，统计改善不能替代matched PRF。原文亦转引Ge计时16(9)ps，不给“1979统一50ps下限”。 | electronic-response-boundary | direct-review | PDF48–53 printed46–51 Sec3 Tables2–3 | true |
| NS79-D19-24 | CoulEx yield积入射beam stopping和多步矩阵元，DSAM积recoil slowing；electron scattering依赖form-factor/低q外推与模型/Coulomb修正；NRF scattering测Gamma0²/Gamma，selfabsorption测Gamma0，须branch/spin/flux等才能转换总tau。“无recoil stopping”不等于无条件绝对时钟。 | indirect-input-and-observable | direct-review | PDF65–71 printed63–69 Eqs6.1–6.15 | true |
| NS79-D19-25 | PDF65放大视觉确认Eq6.5字面为(2Ji+1)B(E2,Jf→Ji)=(2Jf+1)B(E2,Ji→Jf)，与通常initial-spin加权关系似反向；保留literal及needs_review，后续独立推导，不当OCR自动纠正或已核erratum。Eq6.2积分方向与dE/dx符号也须先声明。 | literal-equation-boundary | direct-visual-with-open-consistency | PDF65 printed63 Eq6.2 Eq6.5 | true |
| NS79-D19-26 | Blocking依赖晶格/prompt dip/校准且可涉及compound lifetime；fission shadow短时输出可混合第二势阱ground/excited态衰变，不能直接等同一个gamma-level tau。219Rn微波39(5)ps与electron-recoil6.0(1.4)ps差异，综述提示低频prompt替代的可能系统误差，不构成本轮两primary独立裁决。 | observable-and-counterexample | direct-review | PDF55–61 blocking/fission; PDF76 printed74 Sec7.2.2 | true |
| NS79-D19-27 | Tables5–7和Fig56关键视觉重核保持088修表；PDF82正文明确adopted480(50)fs与Lees710(70)fs比较。Fig55多方法和Table1多模型均非自动独立；全部参考表只算综述已读，不代表取得Schwalm/Hermans等body。 | source-dependence-and-scope | direct-review | PDF79–82 printed77–80 Tables5–7 Figs55–56 | true |


## checkpoint093：独立详细平衡推导与间接观测的可识别性

先从定义而非Eq6.5抄写：对Hermitian电张量，正逆reduced matrix element模相同；\(B(i\to f)=|\langle f||T||i\rangle|^2/(2J_i+1)\)，故\((2J_i+1)B(i\to f)=(2J_f+1)B(f\to i)\)。这与NS79-D19-25记录的源字面在不等spin时不相容。保持原件、字面和needs_review，不宣称已核publisher erratum或实际作者producer。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| NS79-D19-28 | 独立integer-spin Racah磁量子数求和对0↔2、2↔4、1↔3及2↔2给B=R²/(2J_initial+1)；0→2的B为2→0的5倍。若将源Eq6.5字面用于此控制，其LHS/RHS为25而非1。此为标准定义下的一致性反证，不是新实验或已验证勘误。 | independent-definition-control | task-derived-from-definition | PDF65 printed63 B definition and Eq6.5; indirect-observable-result-093.json | true |
| NS79-D19-29 | 用signed dE/dx<0时yield从E0积分到Emin；用S=−dE/dx>0时反向积分，两者均正。自设sigma=.002E² barn、E0/Emin=10/5MeV、S=2MeV/(mg/cm²)给scaled积分.2916667 barn·mg/cm²；混用正S与下降积分限会误出负yield。未含N/rho、branch、角与eff，非原实验yield。 | signed-stopping-convention | task-derived | PDF65 Eq6.2–6.3; indirect-observable-result-093.json | true |
| NS79-D19-30 | 在已除spin/flux/geometry/source-line等响应的理想NRF合同下，scattering q=Gamma0²/Gamma=b0²Gamma；仅q不能定总tau。自设q1meV、b0=.2/.5/1给tau26.3285/164.5530/658.2120fs而q相同。若另有selfabsorption r=Gamma0=4meV，则Gamma=r²/q=16meV、b0=q/r=.25、tau41.13825fs。数字均合成，不是某核测量。 | width-identifiability-and-companion | direct-review-and-task-derived | PDF70–71 Eqs6.14–6.15; indirect-observable-result-093.json | true |
| NS79-D19-31 | 上述组合ln tau=ln hbar+ln q−2ln r，一阶variance包含−4Cov(lnq,lnr)。自设10%/5%边际误差且rho=−1/0/+1给相对sigma20%/14.142%/0；零是同源误差精确抵消的极端控制，不是实际precision。缺fullCov不能把两个observable自动当独立。 | companion-covariance-boundary | task-derived | NS79-D19-30; indirect-observable-result-093.json | true |
