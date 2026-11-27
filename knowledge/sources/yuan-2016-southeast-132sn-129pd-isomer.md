---
type: source
title: "Isomerism in the “south-east” of 132Sn and a predicted neutron-decaying isomer in 129Pd"
aliases: [Yuan 2016 129Pd neutron-decaying isomer, Yuan 2016 PLB]
created: 2026-11-07
updated: 2026-11-27
status: active
review_status: unreviewed
source_type: journal-article-theory
reading_depth: deep-read
title_original: "Isomerism in the “south-east” of 132Sn and a predicted neutron-decaying isomer in 129Pd"
authors: [Cenxi Yuan, Zhong Liu, Furong Xu, P. M. Walker, Zs. Podolyák, C. Xu, Z. Z. Ren, B. Ding, M. L. Liu, X. Y. Liu, H. S. Xu, Y. H. Zhang, X. H. Zhou, W. Zuo]
journal: Physics Letters B
year: 2016
volume: 762
pages: 237–242
doi: 10.1016/j.physletb.2016.09.030
language: en
canonical_source: doi:10.1016/j.physletb.2016.09.030
citation_key:
raw_file: "raw/papers/isomer/isomer_application/nuclear_astrophysics/2016_Yuan et al_Isomerism in the “south-east” of 132Sn and a predicted neutron-decaying isomer in 129Pd 1.pdf"
raw_sha256: cf9c983dc4f88bffc8e2d5041948b0c1e0aabf396a696edd710be3f8c8e1ade1
archive_required: true
nuclei: [129pd, 128pd, 131cd, 130cd, 132in, 134in, 135sn, 136sn, 138sn]
reactions: []
experiments: []
models: [shell-model, oxbash, jj46-hamiltonian, monopole-based-universal-interaction, m3y-spin-orbit, two-potential-approach]
observables: [level-energy, one-neutron-separation-energy, b-e2, partial-half-life, neutron-decay-width]
methods: [large-scale-shell-model, bohr-sommerfeld-quantization, barrier-penetration]
tags: [shell-model, 129pd, neutron-radioactivity, isomer, southeast-132sn, jj46, theoretical-prediction]
---

# Yuan 等（2016）：`132Sn`“东南区”同核异能性与 `129Pd` 中预测的中子放射性同核异能态

## Bibliographic Record

The article was published in *Physics Letters B* 762, 237–242 (2016), received 2 July 2016, accepted 9 September 2016, available online 21 September 2016 (DOI: 10.1016/j.physletb.2016.09.030). The 6-page PDF is preserved at `raw/papers/isomer/isomer_application/nuclear_astrophysics/2016_Yuan et al_Isomerism in the “south-east” of 132Sn and a predicted neutron-decaying isomer in 129Pd 1.pdf` with SHA-256 `cf9c983dc4f88bffc8e2d5041948b0c1e0aabf396a696edd710be3f8c8e1ade1` (517,797 bytes). `archive_required: true` is preserved.

## Scope and Reading Depth

The 6-page paper was read in full, covering theoretical model construction, effective single-particle energy evolutions, calculated level schemes, Table 1 (neutron separation energies), Table 2 (isomer properties and transition rates), and equations (1)–(3) for the two-potential neutron barrier penetration.

## Summary

Yuan et al. developed a new shell-model Hamiltonian, designated `jj46`, tailored for the "south-east" quadrant of $^{132}_{50}\text{Sn}_{82}$ ($Z \le 50, N \ge 82$). The valence space comprises 4 proton hole/particle orbits ($\pi 0f_{5/2}, 1p_{3/2}, 1p_{1/2}, 0g_{9/2}$) and 6 neutron orbits ($\nu 1f_{7/2}, 2p_{3/2}, 2p_{1/2}, 0h_{9/2}, 1f_{5/2}, 0i_{13/2}$). The proton-proton and neutron-neutron matrix elements are derived from CD-Bonn $G$-matrix interactions, while the cross-shell proton-neutron interaction is constructed from the monopole-based universal interaction ($V_{MU}$) augmented by M3Y spin-orbit force ($V_{MU} + LS$).

The `jj46` Hamiltonian successfully reproduces experimental $S_n$ values, level energies, and isomeric $B(E2)$ values in $^{134,136,138}\text{Sn}$, $^{130}\text{Cd}$, and $^{128}\text{Pd}$. The authors systematically predict several unobserved isomers across the region:
1. In $^{135}\text{Sn}$, a $21/2^-$ isomer at $2.288\text{ MeV}$ with $\tau_{E2} \approx 100\text{ ns}$ ($\nu(1f_{7/2})^2(0h_{9/2})$).
2. In odd-odd $^{132,134}\text{In}$ and $^{130}\text{Ag}$, low-lying $5^-$ isomers located $\sim 70\text{ keV}$ above the $7^-$ ground states with extended lifetimes due to $\pi-\nu$ transition cancellation.
3. In $^{129}_{46}\text{Pd}_{83}$, a $19/2^-$ isomer is predicted at $E_x = 1.903\text{ MeV}$, which lies above the calculated one-neutron separation energy ($S_n = 1.524\text{ MeV}$ in `jj46`, giving $Q_n = 0.379\text{ MeV}$; $S_n = 1.461\text{ MeV}$ in FRDM, giving $Q_n = 0.442\text{ MeV}$). Decay to the $2^+$ first excited state of $^{128}\text{Pd}$ ($1.311\text{ MeV}$) is energetically closed, so neutron emission can proceed only to the $0^+$ ground state with orbital angular momentum $\ell = 9$. The calculated partial neutron half-life $T_{1/2}(n) \approx 0.3–10\ \mu\text{s}$ competes directly with the calculated $E2$ $\gamma$ decay ($\tau_{E2} = 0.955\ \mu\text{s}$).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| YUA16-1 | A shell-model Hamiltonian `jj46` is constructed for $Z \le 50, N \ge 82$ using CD-Bonn $G$-matrix for $\pi\pi/\nu\nu$ and $V_{MU} + LS$ for $\pi\nu$, reproducing experimental $S_n$, levels, and seniority $B(E2)$ in $^{134,136,138}\text{Sn}$, $^{130}\text{Cd}$, and $^{128}\text{Pd}$. | model-calculation | direct | PDF p. 1–2, Table 1, Fig. 1 | false |
| YUA16-2 | In $^{129}\text{Pd}$, the ground state is predicted to be $7/2^-$ ($\pi(0g_{9/2})^{-4} \nu(1f_{7/2})$) and a $19/2^-$ seniority-core isomer is predicted at $E_x = 1.903\text{ MeV}$ ($\pi(0g_{9/2})^{-4}_{8^+} \otimes \nu(1f_{7/2})$). | model-calculation | direct | PDF p. 4, Table 2, Fig. 3 | false |
| YUA16-3 | The calculated one-neutron separation energy $S_n$ for $^{129}\text{Pd}$ is $1.524\text{ MeV}$ in `jj46` ($1.461\text{ MeV}$ in FRDM; $1.780\text{ MeV}$ in AME2012 extrapolation), placing the $19/2^-$ isomer at $Q_n = 0.379\text{ MeV}$ ($0.442\text{ MeV}$ in FRDM; $0.123\text{ MeV}$ in AME2012) above the $^{128}\text{Pd}(0^+) + n$ threshold, while decay to $^{128}\text{Pd}(2^+, 1.311\text{ MeV})$ is energetically closed. | model-calculation | direct | PDF p. 2, 4, Table 1, text col. 1 | false |
| YUA16-4 | Using the two-potential approach with Bohr-Sommerfeld quantization (Eqs. 2–3), the partial half-life for $\ell=9\hbar$ centrifugal-barrier neutron emission to $^{128}\text{Pd}(0^+)$ is predicted to be $T_{1/2}(n) \approx 0.3–10\ \mu\text{s}$, which is directly competitive with the calculated $E2$ $\gamma$-decay mean life ($\tau_{E2} = 0.955\ \mu\text{s}$, $B(E2) = 12.88\ e^2\text{fm}^4$). | model-calculation | direct | PDF p. 4–5, Table 2, text col. 2 | false |
## Competing Interpretations and Limitations

### Distinction Between Theoretical Prediction and Physical Observation
The neutron-decaying $19/2^-$ isomer in $^{129}\text{Pd}$ is strictly a **THEORETICAL MODEL PREDICTION** within the Yuan et al. (2016) paper, not an experimental observation reported by the authors.
- In Yuan et al. (2016), the authors explicitly state: "The predicted $19/2^-$ isomer in $^{129}\text{Pd}$ could decay by both electromagnetic transitions and neutron emission with comparable partial life-times, making it a good candidate for neutron radioactivity, a decay mode which is yet to be discovered."
- Kinematics and Threshold Sensitivity: Because $E_x(19/2^-) = 1.903\text{ MeV}$, the decay energy $Q_n = E_x - S_n$ is finite and positive for $S_n < 1.903\text{ MeV}$ (e.g. $Q_n = 0.379\text{ MeV}$ in `jj46`; $0.442\text{ MeV}$ in FRDM; $0.123\text{ MeV}$ using AME2012 mass extrapolation). Closing the neutron decay channel requires $S_n \ge 1.903\text{ MeV}$ (an increase of $\Delta S_n \ge 379\text{ keV}$ over `jj46`), or a lower isomeric level energy. A $+200\text{ keV}$ shift in $S_n$ reduces $Q_n$ to $\sim 0.18\text{ MeV}$, which substantially suppresses the $\ell = 9$ penetration rate due to the centrifugal barrier, but does not strictly close the channel unless $Q_n \le 0$.
- The claim must be cited as a model prediction and candidate for experimental verification, never as an observed physical decay.

## Source Self-Audit

- Audit date: 2026-11-07 by Codex research agent (self-audit, not human-reviewed).
- Consistency check: confirmed that $E_x(19/2^-) = 1.903\text{ MeV}$, $S_n(jj46) = 1.524\text{ MeV}$, $B(E2) = 12.88\ e^2\text{fm}^4$, $\tau_{E2} = 0.955\ \mu\text{s}$, and $T_{1/2}(n) = 0.3–10\ \mu\text{s}$ match Table 1, Table 2, and text on PDF p. 4–5.
- Status classification: purely theoretical paper (`source_type: journal-article-theory`).

## Extracted Pages

- PDF p. 1 (237): Abstract; introduction to $N=82$ shell gap and isomer stepping stones; motivation for neutron radioactivity.
- PDF p. 2 (238): Construction of `jj46` Hamiltonian; model space; Table 1 one-neutron separation energies $S_n$ across Sn, In, Cd, Ag, Pd.
- PDF p. 3 (239): Fig. 1 levels of $^{134,136,138}\text{Sn}$; Fig. 2 neutron effective single-particle energies (ESPE); configuration mixing discussion.
- PDF p. 4 (240): Fig. 3 levels of In, Cd, Pd; Fig. 4 $\pi^{-1}\nu$ multiplets in $^{132}\text{In}$; Fig. 5 proton-hole and neutron-particle ESPEs; Table 2 predicted isomer properties.
- PDF p. 5 (241): Table 2 continuation; Eqs. (2)–(3) two-potential model for neutron emission barrier penetration; predicted $\ell=9\hbar$ neutron decay lifetime in $^{129}\text{Pd}$.
- PDF p. 6 (242): Summary, acknowledgments, and references (1–37).

## 2026-11-27 — 馆藏原件与覆盖核对

- {"from": 1, "to": 2, "sections": "出版信息、摘要、§1 引言、§2 有效哈密顿量、§3 开头及表1"}
- {"from": 3, "to": 4, "sections": "§3 能级和组态讨论；第3页图1–2及 ESPE 式(1)，第4页图3–5及表2引介"}
- {"from": 5, "to": 6, "sections": "第5页完整表2、跃迁及中子发射讨论、式(2)–(3)、§4 总结与致谢；第6页文献[1]–[37]"}
- 本次获取的具体覆盖：通读 PDF 物理第1–6页的逐页文本，含表1、表2、图1–5图注、公式上下文和文献表。核对了可辨的表行和正文数值。图内能级标号及抽取受损的公式符号留待原页视觉核查。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A19-1 | 作者为 ¹³²Sn 东南区构造 jj46 有效哈密顿量，采用四个质子价轨道和六个中子价轨道。同类核子相互作用来自 CD-Bonn G 矩阵，跨壳质子–中子相互作用采用 V_MU 加 M3Y 自旋–轨道项。作者用已有分离能、能级与 E2 数据检验计算。 | model-construction | source-reported | PDF 第2页 §2 和表1、第3页图1、第4页图3、第5页表2；能级图待核第3–4页。 | true |
| A19-2 | jj46 预测 ¹²⁹Pd 的 19/2⁻ 态位于 1.903 MeV，主组态为 π(0g₉/₂)⁻⁴ν(1f₇/₂)，权重 74.2%。对 15/2⁻ 态的计算跃迁能为 0.146 MeV，B(E2) 为 12.88 e²fm⁴，E2 平均寿命为 0.955 μs。 | model-calculation | source-reported | PDF 第5页表2的 ¹²⁹Pd 行；图示能级顺序待核第4页图3。 | true |
| A19-3 | ¹²⁹Pd 的 Sₙ 在 jj46 和 FRDM 中分别为 1.524 和 1.461 MeV，对预测异能态分别给出 Qₙ = 0.379 和 0.442 MeV。按这两套阈值，通往 ¹²⁸Pd 的 0⁺ 基态的发射通道开放，轨道量子数 ℓ = 9；该论文列出的 1.311 MeV 的 2⁺ 态在能量上不可达。 | model-calculation | source-reported | PDF 第2页表1的 ¹²⁹Pd 行、第5页中子发射正文与表2；第2页列对齐待核。 | true |
| A19-4 | 两势方法与 Bohr–Sommerfeld 条件给出的中子发射时间尺度为 0.3–10 μs，适用计算区间为 Qₙ = 0.35–0.50 MeV，取 G = 9。作者据此提出中子发射可能与 E2 电磁衰变竞争。 | model-calculation | source-reported | PDF 第5页表2、式(2)–(3)及其后正文；势和积分式的完整符号待核第5页。 | true |

jj46 用 OXBASH 计算，单粒子能依据 ¹³¹In 和 ¹³³Sn 的已知态设定，质子–质子相互作用乘 0.74，V_MU 中心项乘 1.07。表1区分实验、jj46、AME2012 和 FRDM，表2区分理论和实验 B(E2)，计算采用 eₚ = 1.7e、eₙ = 0.7e。两势法、势参数与量子化条件依赖文献[35]–[37]。

- 删除 ¹²⁹Pd 的 AME2012 1.780 MeV 及其导出的 Qₙ = 0.123 MeV。PDF 第2页表1的抽取将 1.780 MeV 列在 ¹³⁰Ag 的 AME2012 栏，¹²⁹Pd 该栏为空，须核原表列线。旧条目基于 ±质量变化推演的内容如保留，应另标为条目推演。
- 表2完整位于 PDF 第5页，第4页是正文引介。式(1)在第3页，定义 ESPE；第5页式(2)给出核势与自旋–轨道项，式(3)给出 Bohr–Sommerfeld 条件。总结和致谢在第5页，文献表在第6页。补录首页修回日期。
- PDF 第4页图3的抽取仅保留图注，旧条目所列的 ¹²⁹Pd 7/2⁻ 基态和 19/2⁻ 态中质子空穴子组的 8⁺ 标记缺少可读原图支撑。该细化暂标待核第4页，组态主项及权重引用第5页表2。
- 将三个奇奇核的共同结论限定为低激发 5⁻ 候选态。PDF 第5页正文专门把 ¹³²In 的小 B(E2) 和较长平均寿命归于质子、中子贡献的抵消，表2分别给出三核的跃迁值。
- PDF 第3页式(1)的求和、轨道撇号和占据数矩阵元抽取受损，同页 Sn 组态的 1h₉/₂ 与模型空间的 0h₉/₂ 也需核原页。第5页另有 1p₃/₂ 与价空间 2p₃/₂ 的下标歧读，以及式(2)–(3)的矢量、指数、根号和转折点条件抽取问题。公式逐字转录须以对应原页为准。
