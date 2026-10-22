---
type: source
title: "Simultaneous deorientation and lifetime measurement in 98Ru using RDDS in inverse Coulomb excitation"
aliases: [Radeck 2012 98Ru deorientation lifetime, Radeck 2012 RDDS deorientation, simultaneous deorientation lifetime 98Ru]
created: 2026-07-09
updated: 2026-07-09
status: ai-draft
review_status: human-reviewed
source_type: experiment-method-article
reading_depth: deep-read
title_original: "Simultaneous Deorientation and Lifetime Measurement in 98Ru Using the Recoil Distance Doppler Shift Method in Inverse Coulomb Excitation"
authors: [D. Radeck, V. Werner, G. Ilie, N. Cooper, V. Anagnostatou, T. Ahn, L. Bettermann, R. J. Casperson, R. Chevrier, A. Heinz, J. Jolie, D. McCarthy, M. K. Smith, E. Williams]
journal: Physical Review C
year: 2012
volume: 85
pages: 014301
doi: 10.1103/PhysRevC.85.014301
language: en
canonical_source: doi:10.1103/PhysRevC.85.014301
citation_key: radeck_2012_Simultaneousdeorientation
raw_file: "raw/papers/2012_Radeck et al_Simultaneous deorientation and lifetime measurement in 98 Ru using the recoil distance Doppler shift.pdf"
raw_sha256: 21ED965EB3FD0F57059D2BFE3367ECC39FA6CC2761B1F23EC95875D1A6FE3642
nuclei: [98ru]
observables: [attenuation-coefficient, transition-quadrupole-moment]
methods: [angular-correlation, recoil-distance-doppler-shift, coulomb-excitation]
tags: [deorientation, angular-correlation, attenuation-factor, lifetime, rdds, pado-support]
---

# Radeck et al. (2012): Deorientation and Lifetime Measurement in `98Ru`

## Bibliographic Record

D. Radeck et al., *Physical Review C* **85**, 014301 (2012), DOI `10.1103/PhysRevC.85.014301`. The title, author list, journal, volume, article number, year and DOI match citation key `radeck_2012_Simultaneousdeorientation`.

## Scope and Reading Depth

Full PDF text layer was read for article pages 014301-1--014301-10. Key checks include Secs. II--V, Eqs.1--9, Figs.3--12, Tables I--II, and the Summary. The focus for this Wiki ingest is the deorientation correction and time-dependent attenuation formalism; the `98Ru` structure discussion and IBM comparison were read but only minimally extracted because they are not central to the sigma-over-I project.

This is a `method-ingest + experiment-ingest + project-ingest` source. It is relevant as deorientation and angular-correlation correction background. It must not be overgeneralized into direct fusion-evaporation `σ/I` evidence because the experiment uses inverse Coulomb excitation and RDDS.

## Summary

Radeck et al. measure lifetimes in `98Ru` using inverse Coulomb excitation plus recoil distance Doppler shift (RDDS). In this geometry, the first `2+` state shows a visible deorientation effect caused by hyperfine interactions during recoil. The authors develop a correction based on measured perturbations of distance-dependent particle-γ angular correlations and fit time-dependent attenuation factors `Gk(d)` for shifted and unshifted components.

For the current project, the central methodological lesson is that alignment/deorientation can be a time-dependent experimental response that must be measured or modeled separately from the transition mixing ratio. The paper also clearly separates nuclear alignment terms from detector solid-angle factors.

## Experimental or Method Setup

- Beam and target: `98Ru` beam at `300 MeV` on `24Mg`; inverse Coulomb excitation below the Coulomb barrier.
- Device: New Yale plunger device, target-to-stopper distances `3--450 μm`.
- Detectors: SPEEDY/YRAST Ball HPGe clover setup with six effective angular rings.
- Method: RDDS using shifted and unshifted γ components; particle-γ angular correlations used to determine deorientation correction.
- Context boundary: Coulomb excitation was chosen partly because unobserved side feeding as in fusion-evaporation reactions does not appear in the same way.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| R12-1 | 本文用 inverse Coulomb excitation + RDDS 测量 `98Ru` 的 `2+_1`、`2+_2`、`4+_1` 寿命，并报告 `B4/2=1.86(16)`，倾向低能激发的 vibrational character。 | observed-fact | direct | Abstract; pp.014301-7--014301-9, Table II, Summary | false |
| R12-2 | 作者说明该 RDDS/inverse-Coulomb-excitation 技术需要 relativistic、efficiency 和 deorientation corrections；本文提出用 experimental angular-correlation perturbation 修正 deorientation。 | method-formalism | direct | Abstract; p.014301-2, Introduction; p.014301-3, Sec.III | false |
| R12-3 | 在 lifetime analysis 语境中，作者指出 Coulomb excitation 通常直接强布居低能态、来自高能级 feeding 常可忽略，因此不同于 fusion-evaporation 中的 unobserved side feeding 问题。 | method-boundary | direct | p.014301-3, Sec.III | false |
| R12-4 | 高 recoil velocity 使 shifted/unshifted γ components 分离，但也要求 Lorentz boost、shifted/unshifted efficiency 和 time/distance-dependent alignment correction；Lorentz solid-angle correction 写在 Eq.1。 | method-formalism | direct | p.014301-3, Sec.III, Eq.1 and Fig.3 | false |
| R12-5 | 作者把 deorientation 描述为 Coulomb excitation 后 nuclear spin 与 electron spin 的 hyperfine interaction 导致 alignment 随时间减弱，从而产生 time-dependent angular distribution。 | method-formalism | direct | pp.014301-3--014301-4, Sec.IV, Fig.4 | false |
| R12-6 | 若没有 deorientation，efficiency 和 solid-angle 修正后的 shifted+unshifted 总强度应与距离无关；Fig.5 对 `2+_1→0+_1` 显示总强度随距离下降，Fig.6 显示 `2+_1` 的角强比有明显距离依赖，而 `4+_1`/`2+_2` 在误差内不明显。 | experimental-criterion | direct | p.014301-4, Figs.5--6 | false |
| R12-7 | 作者使用 `W(θ)=Σ Rk Bk Qk Pk(cosθ)=Σ AkPk(cosθ)`；其中 `Rk` 考虑跃迁的 spin 和 multipolarity，`Bk` 对应 reaction 后 alignment，`Qk` 是 Ge detector finite-solid-angle effect。 | method-formalism | direct | pp.014301-4--014301-5, Sec.IV | false |
| R12-8 | 引入 time-dependent attenuation factor `Gk(t/d)` 后，实验角关联参数相对初始 Coulomb-excitation correlation 的变化给出 `Gk(d)=Ak^exp(d)/Ak^coul(d=0,dΩp)`；unshifted component 用 Eq.5，shifted component 用 decay function average 的 Eq.7。 | method-formalism | direct | pp.014301-5--014301-6, Eqs.2--7, Fig.8 | false |
| R12-9 | simultaneous fits 给出 `Gk(d)` 参数：`α2=0.18(11)`, `Γ2=0.142(31) 1/ps`, `C2=3.3(8) ps`; `α4=0.24(13)`, `Γ4=0.314(110) 1/ps`, `C4=1.5(5) ps`；作者警告 hard-core values 因长距离数据缺失和误差大而不可靠。 | observed-fact | direct | p.014301-7, Table I and text below Fig.8 | false |
| R12-10 | deorientation correction factor 定义为 `α_deor(d,θ)=W^US(d,θ)/W^SH(d,θ)`；校正后 shifted+unshifted 总强度在误差内恢复为常数。 | method-formalism | direct | p.014301-7, Eq.8 and Fig.9 | false |
| R12-11 | 寿命结果为 `τ(2+_1)=8.36(29) ps`、`τ(4+_1)=2.31(16) ps`、`τ(2+_2)=1.7(2) ps`；`2+_2` 和 `4+_1` 的 deorientation correction 在误差内不必要。 | observed-fact | direct | pp.014301-7--014301-8, Figs.10--12, Table II | false |
| R12-12 | 作者总结：当寿命位于 RDDS sensitive region 且与 deorientation time 同量级时，inverse-kinematics 中 simultaneous deorientation and lifetime measurement 有优势，并可用于 radioactive beams 和 relative g-factor studies，但需要合适 calibration / velocity conditions。 | author-interpretation | direct | p.014301-9, Summary | false |

## Nuclear Structure Information

The nuclear-structure result is a refined `98Ru` lifetime and `B4/2` determination. This Wiki currently uses the paper mainly for deorientation and angular-correlation methodology, not for building a `98Ru` structure page.

## Authors' Interpretation

- The deorientation effect must be corrected for the `2+_1` lifetime in this inverse-Coulomb-excitation RDDS experiment.
- Simultaneous deorientation and lifetime measurement is useful when the nuclear lifetime is comparable to the deorientation time scale.
- The method is promising for radioactive beams and relative g-factor measurements, provided calibration and comparable charge-state/velocity conditions are available.

## Competing Interpretations and Limitations

- The source is not a fusion-evaporation side-feeding paper and does not prescribe `σ/I`.
- It uses particle-γ angular correlations and hyperfine-induced time-dependent attenuation, not the same formal object as Draper/Cejnar Gaussian side-feeding width.
- Hard-core attenuation parameters `αk` are stated by the authors to be unreliable in this dataset because long-distance information and precision are limited.

## Project Relation

For [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]], this source adds a modern method example showing that alignment/deorientation corrections can be measured through angular correlations and encoded in `Gk(t/d)`. It also provides a useful symbol boundary: `Qk` is a detector finite-solid-angle factor, `Bk` is alignment, and `Gk` is time-dependent deorientation attenuation. It should be cited as related methodology, not as primary evidence for a universal fusion-evaporation `σ/I` value.

## Extracted Pages

- Concepts: [[deorientation]], [[spin-alignment]]
- Methods: [[angular-correlation]], [[angular-distribution]]
- Observables: [[attenuation-coefficient]], [[angular-distribution-coefficient]]
- Projects: [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]

## Personal Notes

Review note: R12-3/R12-7/R12-8/R12-10 were user-reviewed on 2026-07-09. Keep R12-3 as the boundary preventing overgeneralization from RDDS/Coulomb excitation to fusion-evaporation P-ADO.


## Day18内无学分Day19预习：新的完整原读与分量响应合同

本段为2026-10-20同一正式Day18 session在新primed回忆冻结后追加；**原2026-07-09整段字节、human-reviewed历史和R12-1–12全部false flags原样保留**。新段和下列新claims仅Codex self-audit、needs_review，不继承human review。本次完整原读十页/十三图/三表/九个编号公式及参考，PDF2–9图表视觉核；先前“Figs3–12/TablesI–II”的scope是旧摄入焦点，不代表本段漏读Fig13/TableIII。没有取得Winther–deBoer job、逐ring/distance计数/fitbins、实际距离坐标producer或jointΣ。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| R12-P19-1 | 300MeV98Ru+24Mg(0.7mg/cm²)，15.7mg/cm²natCu stopper，v/c=.0450(.0006)、六ring；Mg particleγtag约束靶激发而非stopper激发。减速尾明确并入US，不把所有US当严格零速原始光子。 | original-acquisition-and-component-contract | direct-original | PDF2–3SecII/III/Figs2–3 | true |
| R12-P19-2 | 总SH+US需particle singles归一、eff/粒子solidangle等修正，Fig5下降用于deorientation诊断；P=SH/(SH+US)的同一归一/粒子solidangle则在分子分母消。SH/US效率、boost与deorientation并不随之取消。 | observable-and-normalization | direct-original | PDF4Fig5、PDF7Eq9后段/Fig9 | true |
| R12-P19-3 | 90°clover效率标定意外缺失，作者用最短d3µm处理论初始角关联补ring3/4相对eff，假定短时alignment变化小并加systematic；d3不进attenuation参数fit。该环节不是独立实测efficiency或无模型初alignment。 | calibration-substitution-and-boundary | direct-original | PDF6左栏首两段 | true |
| R12-P19-4 | US衰变的取向被假定在stopper中冻结，故GUS对应到达时间；SH则用decay function在飞行域平均G，Eq7显式含τ。作者以旧τ起步、回填新deorientation-correctedτ，两步迭代称足够；未给收敛criterion/完整jointΣ，不当本任务重放或独立两次measurement。 | component-conditional-kernel-and-iteration | direct-original-and-boundary | PDF5stopper假设、PDF6Eqs4–7/Fig8 | true |
| R12-P19-5 | Γk=|g|/Ck；C跨同元素迁移仍要求相同v/c和相近charge-state分布、靶足以达charge equilibrium。由g=.47得到C2≈3.31/C4≈1.497ps；换成文中另g=.41时为2.887/1.306只条件算术，不测新g、符号或核τ。αhardcore作者明确不可靠，不能把central作已知精确校准。 | calibration-transfer-and-sign-boundary | direct-original-and-derived | PDF6Eq6、PDF7TableI/邻文 | true |
| R12-P19-6 | 在额外明确physicalt≥0、G=α+(1−α)e^(−Γt)、stopperalignment冻结的chart下，GSH=α+(1−α)(1−e^−(Γ+1/τ)t)/[(1+Γτ)(1−e^−t/τ)]；α≤GUS≤GSH≤1。源τ8.36/Γ/α中心给SH长时极限.554922(k2)/.449653(k4)，US极限.18/.24。非actualangularresponse/τfit/CI。 | task-analytic-component-average | derived-and-boundary | PDF6Eqs4/7、PDF7TableI；新radeck-kernel-result-007 | true |
| R12-P19-7 | PDF5Eq2后字面写normalization A0(d)=0，而Fig7a有正的非零角强度；PDF7Eq9印d−d0且邻文d0≈8(1)µm，d3若直接代正8、a1会给P≈−.045333。保存文字/坐标边界，不擅改符号或给erratum；缺actualproducer不能从literalcontrol推原τbias。 | literal-normalization-and-coordinate-boundary | direct-original-and-derived | PDF5Eq2后/Fig7a；PDF7Eq9后/Fig10；新result | true |
| R12-P19-8 | PDF8prose印BE2(2→0)=31.0(17)W.u.，TablesII/III印31(1)，R12-11的τ8.36(.29)ps保持。另I85/I41.5与前Fig6的36.5、重复6b标签也保位置；不据此修原数据/猜版本更正。 | literal-printing-boundary | direct-original | PDF8prose/TableII；PDF9TableIII；PDF5Fig6caption | true |
| R12-P19-9 | TableII的2+2支路和mixing从Ref46评价取，TableIII6+/8+实验强度来自旧Ref8，IBM bosoncharge调到本次2+1强度。新τ/派生BE2/模型匹配不能按列重复计独立证据；作者也强调只看B4/2可能误导absolutecollectivity。 | source-lineage-and-model-dependency | direct-original | PDF8TableIIcaption/讨论；PDF9TableIII/讨论 | true |
| R12-P19-10 | 本次只完成下一卡的一项原件/核响应exercise；Nolan1979本preview尚未重新原读，方法选择完整决策树/最小校准清单待后续。R12主文对其它Refs/未发表工作不作本session已读；无新session/正式19学分。 | actual-scope-and-credit-boundary | task-reading-receipt | day19-preview-recall-freeze-007；radeck-preview-reading-scope-007 | true |

本次[冻结合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/radeck-kernel-input-contract-007.json)、[程序](../../system/scripts/day19_radeck_component_kernel.py)/[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/radeck-kernel-result-007.json)只给条件平均/原打印检查。physicaltime与原相对距离offset必须有执行桥，不能悄悄把Eq7积分域或Eq9符号修成想要的fit。未取得实验计数/理论初始角关联系数/效率Cov，不能重报τ/g/coverage。

新分析写回[[lifetime-method-selection-response-contract]]、[[recoil-distance-doppler-shift]]；原人审项目结论和字节不动。正式Day19应新session承认本priming并逐卡新交付；本段不给学分。


## Day 19正式课程：RDDS时间响应、退取向分量条件与实验边界核验

checkpoint008更正前轮未实际raw读却称十页/全部图表新核的声明。本次已实际读取十页全文文本；图表/公式视觉范围单独记入source-reading-scope-008.json。旧R12-1–12人审prefix字节恢复并保留，新段仍needs_review。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| R12-D19-1 | v/c=.0450(6)给13.4907μm/ps，τ8.36ps的条件vτ=112.782μm；这不消除距离offset、foil不平整、速度分布或效率误差。Radeck是Cu stopper，不是Suzuki薄degrader。 | kinematics-and-boundary | direct-original-and-derived | PDF2 SecII；PDF7 Eq9 | true |
| R12-D19-2 | US在stopper冻结是作者假设；SH须按飞行域衰变密度平均。α2=.18、Γ2=.142及τ8.36中心给条件SH渐近.554922；不是新独立实测角响应或已知无误的硬核参数。 | component-kernel | direct-original-and-derived | PDF5–7 Eqs4–7/TableI | true |
| R12-D19-3 | superseded：−4.6%不是Radeck实测bias或普遍上限。旧自设A2=.35、k4=0、θ0°的简化才给该量级；新同τ/Γ控制在A2=−.35/0/+.35给+8.07%/0/−4.92%，说明符号与大小依角响应。 | synthetic-counterinput | derived-and-boundary | PDF5 Eq2；evidence-repair-result-008.json | true |
| R12-D19-4 | 90°效率意外缺失，作者用最短d=3μm理论初始角关联补rings3/4相对效率、加系统误差并排除该点的attenuation fit。这是显式模型辅助校准，不可称独立实测，也不能凭缺失直接断言严重偏差。 | calibration-substitution | direct-original | PDF6 first two paragraphs | true |
| R12-D19-5 | 此实验低能inverseCoulEx可减小unobserved sidefeeding；两步激发feeding被认为可忽略并纳入系统误差。不能外推任意fusion或复杂级联。 | feeding-domain | direct-original | PDF3 SecIII；PDF7 SecV | true |
| R12-D19-6 | 寿命比值中公共particle归一和particle solid angle消；SH/US能量eff、Lorentzboost、deorientation仍须校正。并非每个RDDS都必须恰有90°detector，任一校准缺项也不必然主导总误差。 | normalization-contract | direct-original | PDF7 Eq9 following paragraphs | true |
| R12-D19-7 | Eq2后A0(d)=0与Fig7正角强度、Eq9的d−d0且d0约8μm/最短相对3μm仍保字面坐标边界。未取得实际producer，不猜erratum或把负physicaltime套成真实fit。 | literal-coordinate-boundary | direct-original | PDF5 Eq2 following text；PDF7 Eq9 | true |


## Day19分量库存设计：US是否包括全部慢化尾

本项从PDF3“slowing tail加入US”出发，联合Nolan Sec2.4.3的有限stopper响应做本任务条件推导。自设τ=2ps、stopper区间ts=1ps；不是本文或Klemme实测stop time，没有用相对d−d0填真实physical time。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| R12-D19-8 | 完整库存S=1−exp(−tf/τ)、T=exp(−tf/τ)[1−exp(−ts/τ)]、U=exp[−(tf+ts)/τ]之和1。尾全归US时T+U恢复真空存活；丢T后U/(S+U)不是同一指数。自设tf=τ=2ps、ts1ps时完整US=.367879，丢尾比=.260894，naive点τ1.48849ps。此为定义/归一反例，不是本文τbias。 | component-inventory-design | task-derived-and-boundary | PDF3 SecIII tail paragraph；rdds-component-inventory-result-011.json | true |
| R12-D19-9 | 保全count而把qT归US、(1−q)T归SH时R=C exp(−tf/τ)，C=q+(1−q)exp(−ts/τ)，可等价为额外tf偏移−τlnC。不同q/τ可有不同effective offset，不能一概当共同mechanical zero。若丢尾导致分母也变，则有曲率，即使R(0)=1/R∞=0也不认证正确响应。 | origin-alias-and-selection-design | task-derived-and-boundary | PDF3 SecIII；Nolan1979 printed36 Sec2.4.3；rdds-component-inventory-result-011.json | true |


## Day19新原读：六环对称性、P4与有限角孔径

本session新读PDF2–7关于SPEEDY六个ring（36.5°、46.5°、85°、95°、133.5°、143.5°）、Lorentz boost式1及SecIV退取向。raw hash仍21ed965eb3fd0f57059d2bfe3367ecc39fa6cc2761b1f23ec95875d1a6fe3642。旧review/needs_review flags不变。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| R12-D19-10 | 六个ring在US偶阶Legendre为3对互补角(36.5/143.5、46.5/133.5、85/95)，对静态A0+A2P2+A4P4只有3个独立行；四个外环(1,2,5,6)仅2个独立行。若A0未知且无先验约束，外环无法唯一确定A0/A2/A4，中心环效率可吸收不同形状。 | geometry-rank-and-identifiability | direct-and-task-derived | PDF2 SecII；PDF6–7 SecIV；angular-acceptance-contract-result-015.json | true |
| R12-D19-11 | 在β=.045下，SH分量经历雅可比(1−β²)/(1−βcosθ)²与光行差，破坏互补角对称性；六环及四外环SH基底在已知β的此点环模型中均rank3。真实寿命提取依赖SH/US每环效率、雅可比与退取向G_k(t)核，不等于6个完全独立的四极矩角度采样。 | relativistic-boost-and-response | direct-original-and-derived | PDF3 Eq1；PDF6–7 Eqs4–9 | true |

Knowledge Impact and Learning Decision：limits把6个ring当成6个任意独立角分布采样点；supports建立外环对称性、中央环理论效率代换与Lorentz boost的分层。[[recoil-distance-doppler-shift]]与[[lifetime-method-selection-response-contract]]保存34项几何控制；原Winther job和联合Cov缺口保留。

## Day19坐标桥与运动学误差压缩分析

依据独立审计程序 day19_radeck_coordinate_bridge_audit.py 的 11 项检验与基准输出 radeck-coordinate-bridge-result-025.json，系统解析了 Radeck 2012 式 (5) 与式 (9) 的距离坐标约定与接触零点不确定度传播：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| R12-D19-14 | checkpoint088视觉纠正：PDF7 Eq9实际印a[1−exp(−(d−d0)/(v tau))]，不是此前抄录的−(d+d0)。PDF6 Eq5同用d−d0。正文给relative distance、d0约8(1)um、v13.49(18)um/ps，但没有本任务actualproducer坐标桥；不能由最短3和d0中心猜真实11um、猜符号erratum或宣称Fig3定量验证。保持字面/校准语义边界，撤回checkpoint025的物理距离认证。 | coordinate-bridge-contract | direct-original-and-derived | PDF7 Eq9；PDF6 Eq5；PDF3 Fig3 | true |
| R12-D19-15 | checkpoint088纠正：beta更大能在同tau下放大飞行长度是中心运动学算术；Delta tau=Delta d0/v只在额外指定t约tau等特殊单点合同下成立，不能作为任意RDDS拟合的机械误差传播公式。固定a、v与单点P时tau=(d−d0)/[v*(−ln(1−P/a))]；d0/scale/velocity/eff/fit参数须联合传播。原实际distance producer与Cov未得，不报真实0.074ps系统误差或2.81倍精度提升。 | kinematic-compression-contract | task-derived-and-boundary | PDF7 SecV；PDF2 SecII；radeck-coordinate-bridge-result-025.json | true |

## Day19量化审计：真空超精细退取向动力学、双分量积分卷积与两步迭代自洽定理

**checkpoint088来源/代码纠正，原标题只保历史anchor。**

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| R12-D19-16 | 指数Gk及SH条件平均核在声明假设下可作数学推导；alpha=.18、Gamma=.142和tau8.36中心不是已知无误的普适参数。相近时间尺度不是已证明超精细“共振”。单点dGSH/dtau小不认证完整拟合迭代映射收敛或误差<.02ps；原文称两步在本数据下足够。Cu阻停取向冻结是采用假设，旧<.1ps屏蔽数值没有来源支持，撤回。旧−4.92/+8.07是早期自设角核控制、不是此脚本独立拟合，硬填检查不作科学证据。 | calibration-and-inference-boundary | direct-original-and-task-analysis | PDF5–7 Eqs4–7/TableI and two-step description | true |

## Day19量化审计：相对论光行差雅可比、光电峰效率梯度与逆运动学RDDS环间发散定理

**checkpoint088：撤回旧科学认证；原标题保留为历史anchor。**

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| R12-D19-17 | checkpoint081撤回：beta=.0754、32/58/72/90/108/145度不是此实验的实测输入；PDF2给mean v/c=4.50(6)%和36.5/46.5/85/95/133.5/143.5度。epsilon正比E^−1是额外设计假设，不是实测效率；原程序没有计算“六环残差<0.8%”，该认证无效。新的点环/各向同性响应控制见R12-D19-18，不能替代真实角分布、退取向、有限孔径或校准。 | source-and-analysis-correction | direct-where-reread-otherwise-withdrawn | checkpoint088 source scope and rejection registry | true |

## checkpoint088：实际六环与有边界的响应设计

本轮定向重读PDF2–3，视觉核PDF2实验/装置图；不是重新全篇阅读。checkpoint081的错误输入不再沿用。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| R12-D19-18 | PDF2实测mean beta=.0450(.0006)，六环36.5/46.5/85/95/133.5/143.5度。PDF3 Eq1以D²校正SH立体角，并强调SH/US效率、慢化尾和deorientation。本任务各向同性点环、合成epsilon(E)正比E^−a下C=D^(2−a)；a=1和P=.5给最前/最后环naive tau比.974585/1.026824。准确C代数反演回P仅为模型closure，不认证原实验残差；a=2只在这个各向同性幂律例中消boost。真实eff、角分布静止系光行差、Gk、有限接受和联合Cov仍需校准。 | original-input-and-declared-design | direct-and-task-derived | PDF2 SecII; PDF3 Eq1 and preceding paragraphs | true |

## checkpoint088：字面坐标与零点误差传播

本轮视觉核PDF6 Eqs4–7、PDF7 Eq9/TableI/Figs9–11，专门区分印刷式与实际producer。原relative坐标的物理桥仍未恢复，不擅改raw。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| R12-D19-19 | Eq5与Eq9字面均用d−d0；checkpoint025错抄Eq9为d+d0并推出11um，已撤回。Eq9同时拟合a与d0，单个误差换算Delta tau=Delta d0/v并非普适；固定a、v、P时导数为−1/[v*(−ln(1−P/a))]，多distance拟合另需完整Jacobian/Cov。TableI alpha2=.18(.11)且正文说hard-core values不可靠，不能仅用中心把G核或两步收敛当精确已知。 | literal-coordinate-and-parameter-contract | direct-visual-and-task-derived | PDF6 Eq5 and two-step paragraph; PDF7 Eq9/TableI | true |

## checkpoint091：完整主线、结果使用范围与来源依赖

本轮先冻结承认强priming的回忆与dirty baseline，再实际读同一规范PDF十页全文（014301-1至10，包括全部正文、Summary与References），视觉核PDF2–9的全部13图/3表/9编号式。原件SHA256仍21ed965eb3fd0f57059d2bfe3367ecc39fa6cc2761b1f23ec95875d1a6fe3642；具体页/图/表/式角色见本run `source-reading-scope-091.json`。这是同一原件的本轮scope补证，不是独立实验、新盲测或新学分。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| R12-D19-20 | 本轮实际完整读10页文本、视觉核PDF2–9全部13图/3表/9式；主线从历史4+1寿命矛盾、inverseCoulEx/RDDS、角关联与退取向校准到结果/IBM解释。本文无单独level-scheme图，局部parent/daughter账本由TableII和caption建立；未取原counts、Wintherjob、fullCov或上游各primary。 | actual-reading-scope-and-data-lineage | direct-original-and-scope | PDF1–10; Figs1–13/TablesI–III/Eqs1–9 | true |
| R12-D19-21 | tau(2+1)=8.36(29)ps用rings1/2/5/6；tau(4+1)=2.31(16)ps和tau(2+2)=1.7(2)ps仅用1/6，因为745/761keV邻线在2/5中难分。2+2/4+1的deorientation在误差内不显著，不能泛称不存在。正文31.0(17)与TableII31(1) W.u.为首个B(E2)的两处literal值，保留不静默合误差；4+→2+ B57.6(40)、2+2→2+1 B47(5)、2+2→0+ B1.05(42)及B4/2=1.86(16)是同链派生，不增加beamrun。2+2支路/混合取Ref46。 | reported-results-and-analysis-scope | direct-original-and-boundary | PDF7 Figs10–11; PDF8 Fig12/TableII and discussion | true |
| R12-D19-22 | PDF6以理论初始角关联代缺失90deg效率并加sys，最短3um不参与attenuation fit；US200/300um无合理角关联而不入G fit，450um统计不足。TableI hard-core alpha作者明确说不可靠。两步迭代只报告本数据下足够；校正后sum近恒定为诊断，不替actualeff/距离/联合Cov验证。 | correction-selection-and-uncertainty-domain | direct-original-and-boundary | PDF6 calibration/fit paragraphs andFig8; PDF7 TableI/Fig9 | true |
| R12-D19-23 | IBM有效电荷调到B(2+1→0+)输入，因此TableIII首行31=31非独立检验；6+1→4+1与8+1→6+1的12.9(15)/2.5(4) W.u.沿用Ref8，不是本次新测高spin寿命。几何vibrator B4/2=2与finite-N IBM(U5,N4)1.5须分开，1.86(16)偏vibrational为作者低能解释，不能当整核全域唯一shape证明。Fig13系统学来自Refs47–49，不按每点重复计独立采集。 | model-normalization-and-companion-lineage | direct-original-and-author-interpretation | PDF1 introduction; PDF8 discussion; PDF9 Fig13/TableIII/Summary | true |
| R12-D19-24 | Gamma_k=abs(g)/Ck，Ck的推导采用外部g=.47(3)，并列另一值.41(3)。作者给相对g方法要求同元素及相当beta/电荷态分布、靶足够达charge equilibrium；这不提供g符号或对其他核无需校准的新绝对g测量，Refs44/45未在本轮重读。 | hyperfine-calibration-and-observable-scope | direct-original-and-boundary | PDF6 Eq6 and following paragraphs; PDF7 TableI; PDF9–10 Summary | true |

### 当前局部level/branch账本

| 源parent标签/能量(keV) | 源gamma标签(keV)与终态 | 本次tau(ps) | 分析/来源边界 |
| --- | --- | --- | --- |
| 2+1 /652 | 652→0+1 | 8.36(29) | deorientation correction；four outer rings |
| 4+1 /1397 | 745→2+1 | 2.31(16) | ring1/6；不是旧Ref8的11(2)ps |
| 2+2 /1414 | 761→2+1及1414→0+1 | 1.7(2) | sameparent tau；branches/mixing引Ref46 |

能量表是源整数标签；1414−652的整数差与761不强配，不补精确per-lineσ或误判新校准冲突。Fig7原A0(d)=0字面、Fig7正角强度和Eq9相对坐标producer缺口继续保留。没有基于原事件重建τ fit、B4/2 Cov或原误差coverage。
