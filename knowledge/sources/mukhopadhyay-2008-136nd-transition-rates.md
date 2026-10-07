---
type: source
title: "Mukhopadhyay et al. 2008 - Electromagnetic transition rates in high-spin bands in 136Nd"
aliases: [Mukhopadhyay 2008 136Nd transition rates]
created: 2026-09-21
updated: 2026-10-07
status: ai-draft
review_status: unreviewed
source_type: experiment-and-model
reading_depth: deep-read
title_original: "Electromagnetic transition rates in high-spin bands in 136Nd"
authors: [S. Mukhopadhyay, D. Almehed, U. Garg, S. Frauendorf, T. Li, P. V. Madhusudhana Rao, X. Wang, S. S. Ghugre, M. P. Carpenter, S. Gros, A. Hecht, R. V. F. Janssens, F. G. Kondev, T. Lauritsen, D. Seweryniak, S. Zhu]
journal: "Physical Review C"
year: 2008
volume: 78
pages: "034311"
doi: "10.1103/PhysRevC.78.034311"
citation_key: Mukhopadhyay_2008
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "https://doi.org/10.1103/PhysRevC.78.034311"
library_file: "raw/papers/gpt/high-spin-20260920/三轴/手征/2008_Mukhopadhyay et al_Electromagnetic transition rates in high-spin bands in Nd 136.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/三轴/手征/2008_Mukhopadhyay et al_Electromagnetic transition rates in high-spin bands in Nd 136.pdf"
raw_sha256: "ea77d7d033051369d19aad2f82a542e91e262eb490d518b246f7f04c2d0dcd2c"
nuclei: [136Nd]
reactions: [100Mo-40Ar-4n]
experiments: [Gammasphere, BLUE, LINESHAPE, DSAM]
models: [tilted-axis-cranking, random-phase-approximation, quadrupole-quadrupole]
observables: [lifetime, B(M1), B(E2), Qt, chiral-vibration, band-mixing]
methods: [doppler-shift-attenuation, gamma-gamma-coincidence, high-fold-spectroscopy]
tags: [136Nd, chirality, band-mixing, DSAM, transition-rates]
---

# Electromagnetic transition rates in high-spin bands in `136Nd`

## Bibliographic Record

- S. Mukhopadhyay *et al.*, *Phys. Rev. C* **78**, 034311 (2008), DOI `10.1103/PhysRevC.78.034311`.

## Scope and Reading Depth

- The six-page PRC article was read end-to-end: introduction, Gammasphere/BLUE and DSAM gates, Fig.1 level scheme, Fig.2 line-shape fits, Table I branching data, Table II lifetimes/strengths, TAC+RPA Hamiltonian and Figs.3–5.

- 2026-10-07 以寿命—分支—强度输入链定向复读全文主线，主代理图核 PDF pp.3–5 的 Tables I–II、误差段落与 Fig.4；本次保留原 raw 哈希、作者报告与 review 状态。此处纠正的是既有知识页的表格转录，不是修订作者的实验结果。

## Experiment and Evidence

`100Mo(40Ar,4n)` at 175 MeV populated `136Nd`; about `2.5×10^9` fivefold-and-higher Gammasphere events were sorted angle-by-angle. BLUE matrices, careful double gates, ring-dependent background subtraction and 5000 Monte Carlo recoil histories were used in LINESHAPE DSAM fits (PDF pp.1–3, Fig.1). Stopping powers came from SRIM; side-feeding was represented by a five-transition cascade whose quadrupole moments were varied.

The two negative-parity bands cross near `I≈17ℏ` and have strong linking transitions. Table II shows markedly different strengths: Band 1 `B(E2)=0.26(3),0.08(1),0.14(2),0.11(2) e²b²` for `I=16–19ℏ`; Band 2 `0.54(8),0.51(7),0.44(6),0.04(1),0.05(1) e²b²` correspond to **`I=15–19ℏ`**, respectively. The old knowledge-page summary shifted the first four Band 2 values by one spin and omitted the fifth. `Qt` similarly differs (`~0.95–1.73 eb` versus `~0.67–2.50 eb`). The quoted errors exclude stopping-power systematics that may reach 15% (034311-3 / PDF p.3, uncertainty paragraph; 034311-4 / PDF p.4, Table II; 034311-5 / PDF p.5, Fig.4 caption).

## Lifetime and Branching Input Audit

下表是作者 Table II 的报告值，不是本轮拟合。`τ` 为文中 DSAM level lifetime，B 值和 `Qt` 是从同一寿命、分支和指定多极性推得的输出，不能计作三份独立观测。Table II / printed 034311-4 / PDF p.4：

| Band | Initial spin | τ (ps) | B(M1) (μN²) | B(E2) (e²b²) | Qt (eb) |
|---|---|---|---|---|---|
| 1 | 15− | 0.93(9) | 2.7(3) | — | — |
| 1 | 16− | 0.88(10) | 1.7(2) | 0.26(3) | 1.73(10) |
| 1 | 17− | 0.71(6) | 1.1(1) | 0.08(1) | 0.95(6) |
| 1 | 18− | 0.56(8) | 0.9(2) | 0.14(2) | 1.26(9) |
| 1 | 19− | 0.32(5) | 1.7(3) | 0.11(2) | 1.11(10) |
| 2 | 15− | 1.27(6) | 4.4(3) | 0.54(8) | 2.50(19) |
| 2 | 16− | 0.87(8) | 3.5(3) | 0.51(7) | 2.42(17) |
| 2 | 17− | 0.61(7) | 1.4(2) | 0.44(6) | 2.24(15) |
| 2 | 18− | 0.51(7) | 1.0(2) | 0.04(1) | 0.67(8) |
| 2 | 19− | 0.31(5) | 1.6(3) | 0.05(1) | 0.75(8) |

选择 Band 1 的 `Ex=6711.4 keV, 18−` 能级作为输入链核验。Table I / printed 034311-3 / PDF p.3 给出该母态的三条分支。为保持其余输入可追溯，下表保存全部10个母态、26条印出分支；Band 编号沿2008本文，不自动映射后续命名：

| Band | Parent Ex (keV) | Jiπ → Jfπ | Eγ (keV) | Printed branching ratio |
|---|---|---|---|---|
| 1 | 5645.3 | 15− → 14− | 229.3 | 0.60(3) |
| 1 | 5645.3 | 15− → 14− | 274.0 | 0.14(2) |
| 1 | 5645.3 | 15− → 14− | 338.0 | 0.26(3) |
| 1 | 5954.0 | 16− → 15− | 308.7 | 0.82(4) |
| 1 | 5954.0 | 16− → 14− | 538.0 | 0.13(1) |
| 1 | 5954.0 | 16− → 15− | 224.7 | 0.05(1) |
| 1 | 6310.2 | 17− → 16− | 356.2 | 0.62(3) |
| 1 | 6310.2 | 17− → 15− | 664.9 | 0.09(1) |
| 1 | 6310.2 | 17− → 16− | 332.8 | 0.29(3) |
| 1 | 6711.4 | 18− → 17− | 401.2 | 0.57(6) |
| 1 | 6711.4 | 18− → 16− | 757.4 | 0.24(2) |
| 1 | 6711.4 | 18− → 17− | 389.6 | 0.19(2) |
| 1 | 7147.2 | 19− → 18− | 435.8 | 0.83(8) |
| 1 | 7147.2 | 19− → 17− | 837.0 | 0.17(2) |
| 2 | 5729.3 | 15− → 14− | 199.6 | 0.93(5) |
| 2 | 5729.3 | 15− → 13− | 382.0 | 0.07(1) |
| 2 | 5977.4 | 16− → 15− | 248.1 | 0.90(3) |
| 2 | 5977.4 | 16− → 14− | 447.7 | 0.10(1) |
| 2 | 6321.8 | 17− → 16− | 344.4 | 0.66(4) |
| 2 | 6321.8 | 17− → 15− | 592.5 | 0.24(2) |
| 2 | 6321.8 | 17− → 16− | 367.8 | 0.10(1) |
| 2 | 6756.0 | 18− → 17− | 434.2 | 0.73(7) |
| 2 | 6756.0 | 18− → 16− | 778.6 | 0.08(1) |
| 2 | 6756.0 | 18− → 17− | 445.8 | 0.19(2) |
| 2 | 7221.5 | 19− → 18− | 465.5 | 0.88(9) |
| 2 | 7221.5 | 19− → 17− | 899.7 | 0.12(2) |

每个母态印出分支的中心值之和均为1，只证明表中归一化，不证明没有漏枝或非γ通道。Table I 没有印出各能量的不确定度，也没有明确写出 branching ratio 是仅对 photon intensities 归一化、对全部 level decays 归一化，还是已含哪种 IC 修正；正文只说明采用 Chiara et al. [16] 的提取过程。本次没有将该引用的未知细节补成独立输入。其解释须保持条件，不能从 quoted B 值反解 ICC 再作为验证证据。

以 `757.4 keV` 分支作纯 E2 的寿命—强度重算，是沿作者 B(E2) 输出所用多极赋值的有条件检查；Table I 的 spin change 本身不等于独立测得所有高阶振幅为零。在 gamma-only、branching ratio 可作每次 level decay 的 photon fraction、忽略能量误差且 τ/b 的 quoted errors 独立这组条件下，现代常数重构给 `B(E2)=0.14034 ± 0.02321 e²b²`，与作者 `0.14(2)` 的中心值一致。完整单位、总分支与 photon 分支的区别和协方差式见 [[high-spin-lifetime-strength-deformation]]；这个重算没有重新测量 τ 或验证 IC/feeding 模型。

误差与假设的直接来源：PDF p.3 左栏明确说 quoted errors 不含 stopping-power modeling systematic，后者可达15%；absolute B(M1) 将 `ΔI=1` 分支假定为 **pure M1**。PDF p.2 的 five-transition side-feeding cascade、下门含完整 shifted/stopped tails、自由 lifetime 的 global fit，以及 PDF p.5 Fig.4 的 statistical-only error bars，都是输入链的条件。没有 measured δ，不能把 pure-M1 假设写成测量结果，也不能默认 stopping/feeding 系统误差在两带间完全抵消。

本节来源独立性为 `single`：Table I、Table II、Fig.4 和本轮重算依赖同一实验；LKH82 只提供率/矩阵元 formalism，不增加寿命测量的独立性。

另有未消解的 transition-label 差异：PDF p.3 Fig.2 的 Band 2 右侧谱例标 `464.8 keV`，同页 Table I 的 `Ex=7221.5 keV, 19−→18−` 行标 `465.5 keV`，PDF p.2 Fig.1 仅标约 `465`。本次保留两处标签，不猜测哪一处是排版错误；选用的 Band 1 `18−` 输入组不受该行影响。复用这一 Band 2 谱例时仍须先确认 transition identity。

### Two-Parent Gamma-Only Chain Controls

以下四行只用印出的τ、Eγ、branch和现代单位系数作条件性重算；author B仅作输出对照。M1取作者ΔI1 pure-M1提取假设，E2沿其ΔI2赋值，不把这些假设当新measured δ。原始输入locators：printed034311-3 / PDF3 Table I；034311-4 / PDF4 Table II；pure-M1说明在PDF3左栏。率/单位定义回到LKH82 p121 Eqs.2.2–2.3a。

| Parent | Eγ (keV), pure extraction assumption | τ (ps), printed b | Gamma-only B | Author B | Descriptive center difference |
|---|---|---|---|---|---|
| Band 1, 18− | 401.2, M1 | 0.56(8), 0.57(6) | 0.89638532 μN² | 0.9(2) μN² | -0.402% |
| Band 1, 18− | 757.4, E2 | 0.56(8), 0.24(2) | 0.14034419 e²b² | 0.14(2) e²b² | +0.246% |
| Band 2, 15− | 199.6, M1 | 1.27(6), 0.93(5) | 5.237069 μN² | 4.4(3) μN² | +19.024% |
| Band 2, 15− | 382.0, E2 | 1.27(6), 0.07(1) | 0.55306379 e²b² | 0.54(8) e²b² | +2.419% |

Band1两个选中branch原b之和为0.81，保留其余389.6-keV branch的0.19，不把选中两条重新归一到1。Band2该母态两条印出b之和为1。Gamma-only低能M1的中心值偏差达到19.02%，而所选高能E2接近原表；这说明一条E2的算术吻合不足以验证全部input ledger。它没有证明作者错误或选定某种branch定义。

表中百分比只是与rounded作者中心值的描述性差值，没有用两份共享τ/branch的输出计算独立显著性。保留quoted误差、branch/τ covariance、未印能量误差、15% stopping systematic及单独feeding模型边界；不从残差反解α、ρ、δ、Qt或branch basis。独立atomic-theory ICC只能作为另一个明确假设下的forward输入，不能冒充MU08实际采用的处理。这是22-check L2算术，不是实验再测量或L4。

## Interpretation and Model Boundary

Self-consistent TAC with a QQ interaction reproduces the broad rotational energies using two distinct four-quasiparticle configurations, approximately `πh11/2²⊗νh11/2d3/2` and `πh11/2g7/2⊗νh11/2²`, with a configuration crossing near `I≈17ℏ` (pp.3–5, Fig.3). Pairing is neglected for these high-spin configurations. RPA around each TAC minimum gives collective phonons around `100–400 keV`; the authors interpret these as chiral-vibrational modes, while noting fragmentation/noncollective solutions in one configuration (p.5, Fig.5).

The different `B(E2)` patterns contradict treating the two near-degenerate bands as one ideal chiral pair. The authors instead attribute their closeness to band mixing between distinct configurations; this does not exclude future chiral vibration built on either configuration (pp.4–6).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU08-1 | DSAM strengths of the two `136Nd` bands differ markedly, especially in `B(E2)`. | experiment-result | direct | PDF pp.2–4, Table II, Fig.4 | true |
| MU08-2 | TAC with two configurations plus RPA phonons explains a band-crossing/mixing scenario. | model-interpretation | mixed | PDF pp.3–6, Figs.3–5 | true |
| MU08-3 | Near-degenerate energy and linking transitions do not establish an ideal chiral pair. | counter-evidence | mixed | PDF pp.4–6, Fig.4 | true |
| MU08-4 | Table II Band 2 E2 strengths are 0.54(8), 0.51(7), 0.44(6), 0.04(1), 0.05(1) e²b² at I=15–19, respectively. The 18− Band 1 lifetime is 0.56(8) ps, with a 757.4-keV 18−→16− branch of 0.24(2) in Table I. | experimental-fact | direct | printed 034311-3 / PDF p.3, Table I, Ex=6711.4-keV group; printed 034311-4 / PDF p.4, Table II, Band 1 I=18 and Band 2 I=15–19 rows | true |
| MU08-5 | Quoted errors omit stopping-power systematics up to 15%, and the absolute B(M1) extraction assumes pure M1 for ΔI=1 transitions. A branch-normalized, gamma-only B(E2) recalculation remains conditional on the branch/IC definition and covariance; it is not independent confirmation of the lifetime or mixing ratio. | our-inference | indirect | direct premises: printed 034311-3 / PDF p.3, paragraph above TAC formalism and Table I; printed 034311-5 / PDF p.5, Fig.4 caption; reconstruction: LKH82 printed p.121, Eqs.2.2–2.3a | true |
| MU08-6 | Gamma-only recalculations under the stated pure-M1/E2 extraction assumptions reproduce the selected Band1 high-energy E2 center closely but give 5.2371 μN² for Band2 I15 199.6-keV M1 versus the reported 4.4(3). This conditional arithmetic does not validate the full branch/IC ledger, establish an independent discrepancy, or identify hidden ICC/covariance inputs. | our-inference | indirect | inputs: printed034311-3 / PDF3 Table I Band1 I18 and Band2 I15 groups; printed034311-4 / PDF4 Table II matching rows; rates: LKH82 p121 Eqs.2.2–2.3a | true |

## Summary

The `136Nd` lifetime study is a direct electromagnetic-strength counterexample that forces partner-resolved transition probabilities into the chirality evidence gate.

## Competing Interpretations and Limitations

- DSAM stopping/feeding and 15% stopping-power systematics propagate into the strengths.
- Printed branching ratios and strength outputs do not provide a full photon/total-rate ledger or covariance. Pure M1 is an extraction assumption, and Qt/B values are derived from the same chain.
- TAC omits pairing for the selected configurations and RPA fragmentation complicates a universal chiral-vibration interpretation.

## Analytical Reconstruction and Self-Audit

| ID | Audit item | Agent judgment | Locator | Status |
|---|---|---|---|---|
| MU08-AR-1 | Lifetime-to-strength chain | DSAM line shapes → lifetimes → branching-normalized `B(M1)/B(E2)` and `Qt`; stopping/side-feeding choices are part of the inference. | PDF pp.2–4, Tables I–II | self-checking |
| MU08-AR-2 | Chiral-pair test | Near-degenerate energies and links are outweighed by large, spin-dependent E2-strength differences; electromagnetic rates are a direct counterexample to energy-only chirality. | PDF pp.4–6, Fig.4 | self-checking |
| MU08-AR-3 | Model scope | TAC configurations and RPA phonons explain a band-crossing/mixing scenario; pairing omission and fragmented RPA solutions limit universal transfer. | PDF pp.3–5, Fig.5 | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `limits` early `136Nd` chiral-band claims and `supports` [[nuclear-chirality]], [[tilted-axis-cranking]], [[random-phase-approximation]], [[doppler-shift-attenuation-method]] and the HS-012/HS-053 Petrache evidence map.
- 本次 `revises` Band 2 的 spin/value 转录；`limits` 把 branch、B(M1)、B(E2) 或 Qt 当作彼此独立数据的用法。[[high-spin-lifetime-strength-deformation]] 保存可复用的率、单位、分支归一化和误差链；不因条件性算术一致而升级实验结论。
- L3 unit: compare this lifetime-strength counterexample with the later D5-strengthened `136Nd` pair; retain chronological model revision rather than a single “136Nd chirality” label.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `MU08-P0-1`: Preserve the stopping-power systematic of up to 15% separately from unquantified feeding-model sensitivity, and preserve the distinction between distinct configurations, band mixing and any later chiral interpretation.

## Extracted Pages

- Nucleus/project: `136Nd`, [[nuclear-chirality-and-multiple-chiral-doublet-bands]]。
- Methods/models: [[doppler-shift-attenuation-method]], [[tilted-axis-cranking]], [[random-phase-approximation]]。
