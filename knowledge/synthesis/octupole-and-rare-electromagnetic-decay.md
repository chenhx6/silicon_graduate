---
type: synthesis
title: "Octupole evidence and rare electromagnetic decay"
aliases: [八极与稀有电磁衰变证据综合]
created: 2026-09-21
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
scope: octupole-and-rare-electromagnetic-decay
confidence: low
sources: [bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, gaffney-2013-pear-shaped-rn-ra, walz-2015-competitive-double-gamma-137ba, soderstrom-2020-137ba-competitive-gamma, dey-2026-116cs-multifaceted-decay]
tags: [octupole, two-photon-decay, drip-line, rare-decay, evidence-map]
---

# Octupole evidence and rare electromagnetic decay

## Question and Scope

This synthesis asks how direct E3, E1 correlations, mean-field order parameters, competitive double-γ decay and exotic particle decay should be ranked without merging observables or model claims.

## Evidence Matrix

| Layer | Example | What it supports | Boundary |
|---|---|---|---|
| Direct E3 matrix element | `144Ba` Bucher 2016; `220Rn/224Ra` Gaffney 2013 | strong octupole collectivity | static `β3` conversion uses model assumptions |
| E1 links and parity systematics | `78Br`, `74As`, `131Ba` | octupole correlations or reflection-asymmetric coupling | does not alone establish stable octupole deformation |
| Mean-field/PES order parameter | Li 2024 `144Ba` | model deformation tendency | no parity projection or direct laboratory splitting |
| Double-γ total branch | Walz, Söderström, Schirmer, Kramp | second-order electromagnetic decay | virtual-path decomposition can be underdetermined |
| Drip-line particle correlations | Dey 2026 `116Cs` | continuum, pairing and exotic-decay hypotheses | low statistics and unavailable raw data limit L4 |

## Synthesis

Walz 2015 and its audited supplement establish a competitive `137Ba` branch with timing, energy and angle controls. Söderström 2020 independently confirms the total branch and adds energy sharing, which favors E3M1 over the original Aqq-dominant reading. The two results agree on the existence and approximate total strength while differing in the virtual multipole decomposition. The difference is a research question, not a reason to erase either source.

### 2026-10-12 gate, branch and source-independence audit

Walz's five-LaBr₃ acquisition and Söderström's eleven-CeBr₃ acquisition are distinct experiments. The quoted integrated branches, `2.05(37)×10⁻6` and `2.62(30)×10⁻6`, differ by `0.57×10⁻6`; treating the quoted uncertainties as independent gives `σΔ≈0.48×10⁻6` or about `1.2σ`. This arithmetic checks compatibility of the total branch only, not the virtual-path coefficients. Walz's gate controls include a prompt time peak, off-time random sidebands, lead shielding, individual-photon spectra and 72°/144° angular checks (W15-1/W15-2). Söderström uses a separate CeBr₃ response and timing calibration and reports the independent branch at `8.7σ` (SO20-1/SO20-AR-1).

The source-dependence boundary is claim-specific: Söderström's 2020 branch count is a separate acquisition, while its Fig.5 joint energy-sharing fit also plots and fits Walz points. Therefore the 2020 measurement independently confirms that the branch exists; the combined fit is not a wholly independent refit of Walz's multipole-path result (SO20-AR-3). The energy-sharing distribution shifts the author interpretation toward a larger E3M1 and smaller M2E2 component, while model and sign/ordering alternatives remain. A 2026-10-30 access audit refined the data boundary: the Mendeley landing shell returned HTTP 200 but reported no v1 snapshot, the public API returned `dataset not found`, and no event-level spectra, response, efficiency, background, cuts or covariance files were recovered (SO20-D28-1). No reproducible L4 refit is claimed.

## Octupole cross-source result

Bucher 2016 and the external Bucher 2017 source supply direct E3 matrix elements in `144Ba` and `146Ba`, both around `48 W.u.`. The neighboring-isotope comparison shows that a strongly varying E1 dipole moment does not track E3 strength one-to-one. Relative E1 links in lighter or different mass regions are useful correlation evidence, but they must remain below the direct E3 layer. Li 2024 supplies a mean-field prediction, not a measurement. Dey 2026's low-energy octupole assignment is supported by decay and RHB/QRPA comparison, but its particle and cluster branches remain statistics and data limited.

## Counter-evidence

E1 links, parity systematics and PES minima can be compatible with octupole correlations without establishing a stable static shape. Angular-only double-γ fits can leave multiple virtual-path minima.

## Model Dependence

GOSIA, rotor conversions, EDF/QPM, QRPA and shell-model calculations constrain different layers; the inferred `β3`, polarizability decomposition and cluster parentage are model dependent.

## Limitations and Missing Evidence

Raw detector responses, full analysis code, partner E3 branches and public particle-event data remain incomplete for independent L4 re-analysis.

## Open L3 questions

- Can the Walz and Söderström event-level spectra, detector responses, sideband scaling and cut acceptances be refitted with common covariance to quantify the remaining E3M1/M2E2 path ambiguity, given that Söderström's joint Fig.5 fit includes Walz points?
- How consistently do direct E3 matrix elements, E1 links and PES `β3` values rank octupole collectivity across mass regions?
- Can a public data or code release make the `137Ba` or `116Cs` problems reproducible at L4?

## Sources

- [[bucher-2016-144ba-direct-octupole]], [[gaffney-2013-pear-shaped-rn-ra]], [[li-2024-144ba-octupole-cdf-3d-lattice]]
- [[bucher-2017-146ba-direct-octupole]]
- [[walz-2015-competitive-double-gamma-137ba]], [[soderstrom-2020-137ba-competitive-gamma]], [[schirmer-1984-double-gamma-40ca-90zr]], [[kramp-1987-160-two-photon-decay]]
- [[dey-2026-116cs-multifaceted-decay]], [[two-photon-nuclear-decay]], [[octupole-deformation]], [[octupole-correlation]], [[drip-line-radioactivity]]

## Self-audit

- Direct, indirect and model evidence are kept in separate rows.
- Total double-γ branch and virtual-path decomposition are treated as different claims.
- This synthesis is a Codex self-audit and remains unreviewed.

## Day19量化审计：137Ba竞争双光子总分支比与虚态八极—偶极路径反转裁决

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_ba137_double_gamma_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/ba137-double-gamma-result-045.json`，核准了对标 [[walz-2015-competitive-double-gamma-137ba]] 与 [[soderstrom-2020-137ba-competitive-gamma]] 的稀有双光子衰变综合裁决事实：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| OCT-D19-1 | 系统审计证实 $^{137}\text{Ba}$ 竞争双光子衰变在两次独立实验中的总分支比在 $1.20\sigma$ 内高度吻合（加权平均值 $2.39(23) \times 10^{-6}$），确立了竞争双光子衰变存在的坚实实验基础。两实验关于虚态多极路径的表观冲突（Walz $E2M2$ 主导 vs Söderström $E3M1$ 主导，极化率比反转达 $13.9$ 倍）由探测几何、对称能窗截断（Walz 滤除了 $>35\%$ 的非对称能量共享相空间）与核结构微观跃迁选择定则共同裁决：$M2$ 跃迁因 $\Delta l = 3$ 受单粒子禁戒削弱 1000 倍，而 $E3$ 跃迁耦合到核芯 $3^-$ 集体八极声子而获得大幅增强，最终确立了 $E3M1$ 路径的主导地位。这确立了解耦双光子虚态路径必须具备 $\ge 5$ 角度覆盖、全能量共享谱展开与微观核芯八极极化计算的三重伴随观测量规程。 | quantitative-synthesis-and-criterion | derived-and-source-boundary | Nature 526, 406; Nat. Commun. 11, 3242; ba137-double-gamma-result-045.json | true |

## Day19量化审计：144Ba与146Ba八极集体性一致性与四层八极证据阶梯

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_ba144_ba146_octupole_e1_audit.py` 的 9 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/ba144-ba146-octupole-e1-result-046.json`，核准了对标 [[bucher-2016-144ba-direct-octupole]] 与 [[bucher-2017-146ba-direct-octupole]] 的八极形变可迁移证据阶梯：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| OCT-D19-2 | $^{144}\text{Ba}$ 与 $^{146}\text{Ba}$ 的直接库仑激发测量确立了基态八极跃迁矩阵元（均为 $0.65\ e\text{b}^{3/2}$，对应 $B(E3) = 48\text{ W.u.}$）的严格一致性，同时揭示了其内禀电偶极矩 $D_0$ 发生 $>4.3$ 倍剧烈塌缩的量子相消机制（宏观液滴与中子侵入轨道壳修正抵消达 $93\%$）。这彻底解除了“小 $E1$ 意味着八极软化或对称”的认知束缚，确立了反射不对称核研究的四层可迁移证据阶梯：第一层为直接垒下库仑激发 $\langle 3^- \Vert \mathcal{M}(E3) \Vert 0^+ \rangle$（无歧义集体性金标准）；第二层为交替宇称能带与宇称劈裂 $\Delta E(K^\pi)$；第三层为带间 $E1$ 跃迁与 $D_0$ 测量（易受微观单粒子偶然相消破坏，如 $^{146}\text{Ba}$ 所示）；第四层为自洽平均场势能面（PES $\beta_3$ 极小，仅具理论导向价值）。 | quantitative-synthesis-and-criterion | derived-and-source-boundary | PRL 116, 112503; PRL 118, 152504; ba144-ba146-octupole-e1-result-046.json | true |

## Day19量化审计：220Rn与224Ra梨形八极形变、Alaga自洽性与EDM增强阶梯

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_gaffney13_rn220_ra224_octupole_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/gaffney13-rn220-ra224-octupole-result-059.json`，核准了对标 [[gaffney-2013-pear-shaped-rn-ra]] 的梨形八极形变微观证据阶梯：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| OCT-D19-3 | 综合 Gaffney 2013（Nature 497, 199）加速放射性束库仑激发实验数据，系统核准重核区反射不对称性与电偶极/八极跃迁性质：(1) 内禀四极与八极矩阶跃：从 $^{220}\text{Rn}$（$Q_2 = 434 \pm 14\text{ e}\text{fm}^2, Q_3 = 2180 \pm 130\text{ e}\text{fm}^3$）到 $^{224}\text{Ra}$（$Q_2 = 632 \pm 10\text{ e}\text{fm}^2, Q_3 = 2520 \pm 90\text{ e}\text{fm}^3$），$Q_2$ 跃升 $1.456$ 倍（$B(E2)$ 翻倍至 $98\text{ W.u.}$），$Q_3$ 跃升 $340\text{ e}\text{fm}^3$（显著性 $z = 2.15\sigma$），且带间八极跃迁 $\langle 2_1^+ \Vert E3 \Vert 1_1^- \rangle = 1370\text{ e}\text{fm}^3$（$210\text{ W.u.}$）在 $^{224}\text{Ra}$ 中坚实确立；(2) 刚性转子 Alaga 标度自洽性：$^{224}\text{Ra}$ 的四极矩阵元之比 $\langle 2_1^+ \Vert E2 \Vert 4_1^+ \rangle / \langle 0_1^+ \Vert E2 \Vert 2_1^+ \rangle = 315 / 199 = 1.583$ 在 $0.1\%$ 精度内精确吻合 $K=0$ 轴对称刚性转子 Alaga 清单预期，证实其基态能带具有稳定的非球体内禀形变；(3) 唯象模型甄别：实测 $Q_3$ 随质量数增加直接推翻了简单 $\alpha$-团簇模型的下降预言，决定性支持了具有非零静态八极形变 $\beta_3$ 的自洽平均场理论；(4) 原子 EDM 增强物理判据：内禀 Schiff 矩增强度度规（$Z Q_3 Q_2$）在 $^{224}\text{Ra}$ 达到 $^{220}\text{Rn}$ 的 $1.72$ 倍，结合奇质量同位素 $^{225}\text{Ra}$ 仅 $55\text{ keV}$ 的极小宇称双重态劈裂，物理确立了 Ra 同位素在探索时间反演破缺与原子电偶极矩极限中相对球形原子具备 $100\text{--}1000$ 倍巨大增强的排他性优势地位。 | quantitative-synthesis-and-criterion | derived-and-source-boundary | Nature 497, 199; gaffney13-rn220-ra224-octupole-result-059.json | true |

## Day19量化审计：BN96微观八极配对条件、交替宇称位移塌缩与D0相消机制

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_bn96_octupole_microscopic_couplings_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/bn96-octupole-microscopic-result-060.json`，核准了对标 [[butler-nazarewicz-1996-intrinsic-reflection-asymmetry]] 的八极微观动力学契约：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| OCT-D19-4 | 严格核准了微观八极驱动机制：(1) $\Delta l = \Delta j = 3$ 轨道相干耦合在费米能级附近的聚集是诱发内禀反射不对称性的微观动力学根源；(2) $^{224}\text{Ra}$ 交替宇称位移 $\delta E(I)$ 随自旋上升由 $173.8\text{ keV}$（$1^-$）断崖式崩塌 $87.9\%$ 至 $21.0\text{ keV}$（$7^-$），实证了静态八极形变（单纯形量子数 $s=+1$ 单一转动带）的建立；(3) 偶极矩相消定理：$^{224}\text{Ra}$ 宏观液滴偶极矩（$0.202\text{ e}\text{fm}$）与微观壳修正偶极矩（$-0.172\text{ e}\text{fm}$）发生 $85.1\%$ 的反相干涉，确立了 $E1$ 跃迁不可作为八极形变充要判据的物理边界。 | quantitative-synthesis-and-criterion | derived-and-source-boundary | RMP 68, 349; bn96-octupole-microscopic-result-060.json | true |

## Day19量化审计：宏观微观电偶极矩D0相消、八极形变非可逆定理与单纯形带崩塌

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_octupole_e1_cancellation_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/octupole-e1-cancellation-result-079.json`，核准了对标 [[bucher-2017-146ba-direct-octupole]] 的八极综合裁决定理：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| OCT-D19-5 | 严格确立了宏观微观电偶极矩相消机制与八极形变非可逆定理：(1) 直接八极集体性一致：$^{144,146}	ext{Ba}$ 基态八极跃迁矩阵元严格等同（$0.65\ e	ext{b}^{3/2}$，对应 $B(E3) = 48	ext{ W.u.}$）；(2) 电偶极矩相消物理本质：$^{146}	ext{Ba}$ 宏观液滴偶极矩（$+0.180\ e\cdot	ext{fm}$）与增加 2 个中子占据 $
u i_{13/2}$ 侵入轨道诱导的微观壳修正偶极矩（$-0.146\ e\cdot	ext{fm}$）发生 $81.11\%$ 抵消，实测 $|D_0| = 0.034\ e\cdot	ext{fm}$ 暴跌 $73.85\%$；(3) 跨质量区普适性：$^{224}	ext{Ra}$ 宏观液滴项（$+0.202\ e\cdot	ext{fm}$）与壳修正项（$-0.172\ e\cdot	ext{fm}$）亦发生 $85.15\%$ 抵消；(4) 八极形变非可逆判据：小 $E1/D_0$ 不能作为否定八极形变的证据，直接垒下库仑激发与超快能级寿命测量是检验梨形形变的唯一排他性金标准；(5) 单纯形能带宇称劈裂塌缩：交替宇称位移 $\delta E(I)$ 随角动量升高收敛至零（$^{224}	ext{Ra}$ 塌缩 $87.92\%$），微积分确证了核梨形刚体转动动力学。 | quantitative-synthesis-and-criterion | derived-and-source-boundary | PRL 118, 152504; octupole-e1-cancellation-result-079.json | true |


## checkpoint107：稀有衰变与八极跃迁的时间滤波及物理时钟契约

**checkpoint108撤回来源不足的路径归因和精度认证。** 旧两总branch中心差在额外独立quotedσ假设下约1.20sigma只是兼容性算术，不重建原CI或使weightedmean成为新采纳值。对E1+E2=661.7keV若额外施加|E1−E2|<250keV，允许E1区间长度250keV，平坦一维区间fraction为.3778；它不等真实相空间/branch接受率，真实值需多极能量权重、角接受、阈值/eff/背景及原cut。不能据此断言已解释E3M1反转。

旧“千倍随机压制、93%相消、严格相同48W.u.、ZQ2Q3即Schiff矩或EDM排他优势”均无本轮matched原件/模型/响应支撑，撤回科学认证。[[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-24只支撑indirect输入边界，[[regis-2011-fast-timing-labr3]] RG11-D19-17和[[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-D19-20不是Ba/Rn/Ra实验的直接证据。原octupole页面早期direct/author/model层及独立性边界保持，不以107替代。
