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

本段为2026-10-21正式Day 19独立课程session原读与定量核查产物；**原2026-07-09整段字节、human-reviewed历史、R12-1–12以及历史R12-P19-1–10条目与flags原样保留**。新段和下列新claims仅经Codex self-audit、保持needs_review: true，不设human-reviewed。本session针对全文十页、十三图、三表与九个编号公式进行严格物理核验，重点对账反冲运动学放大、真空超精细退取向的分量条件平均、90°探测器效率缺失的代数影响，以及 Yale plunger 的机械零点边界。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| R12-D19-1 | 300 MeV 98Ru + 24Mg 逆运动学提供 v/c = 0.0450(6)（13.491 um/ps）反冲速度，较常规运动学（4.797 um/ps）实现 2.81 倍空间放大，使 tau(2+_1)=8.36 ps 态飞行距离达 112.8 um，完全摆脱接触零点（d0约8 um）与箔片粗糙度约束。 | experimental-kinematics-scaling | direct-original | PDF2–3 Sec.II/III, Fig.2–3 | true |
| R12-D19-2 | 真空中超精细场引起退取向衰减 G_k(t)；阻停分量在到达 stopper 时冻结（G_US(t) = G(t)），飞行衰变分量沿衰变时间密度加权平均（G_SH(t)）；渐近极限下 G_SH(inf) 为 0.554922(k=2) 与 0.449653(k=4)，远高于 G_US(inf) 的 0.18 与 0.24。 | deorientation-component-asymmetry | direct-original-and-derived | PDF5–6 Eqs.4–7, Fig.8, Table I | true |
| R12-D19-3 | 在前向探测器（theta=0 deg）若忽略退取向 G_k 修正，测得比值 P(d) 发生系统性偏离，在敏感飞行时程（5–15 ps）导致表观提取寿命发生最大 -4.6% 的系统性负偏差，证实退取向不是全局常数缩放，而是距离相关的线形畸变。 | systematic-deorientation-bias | derived-and-verified | PDF7 Eq.8, Fig.9; day19_rdds_timing_response_analysis.py | true |
| R12-D19-4 | 90° clover 探测器效率标定实验中缺失，作者在最短距离 d=3 um 处借用理论初始角关联代替相对效率，假定短时 alignment 变化微弱；该代数替代引入了对理论角分布模型的依赖，并非无偏实测效率。 | calibration-deficiency-boundary | direct-original | PDF6 左栏首两段 | true |
| R12-D19-5 | 逆库仑激发通过粒子-γ符合直接强布居低自旋集体态（2+_1, 4+_1, 2+_2），上能级侧馈极其微弱，在方法学上避开了熔合蒸发反应中未知慢侧馈（slow side feeding）对寿命拟合的主导模型依赖。 | feeding-topology-advantage | direct-original | PDF3 Sec.III | true |
| R12-D19-6 | RDDS 寿命提取的最小校准闭环严格依赖：机械绝对零点 d0 标定、全角度阵列相对效率矩阵（尤其 90° 环）、反冲初速矢量及真空中退取向衰减参数 G_k(t) 的独立约束，任何单项缺失均构成主导系统误差。 | minimal-calibration-contract | synthesis-and-boundary | PDF6–7 Sec.IV/V, Table I | true |

本段定量结果见 [rdds-timing-response-result.json](../../outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/rdds-timing-response-result.json) 与 [day19_rdds_timing_response_analysis.py](../../system/scripts/day19_rdds_timing_response_analysis.py)。
