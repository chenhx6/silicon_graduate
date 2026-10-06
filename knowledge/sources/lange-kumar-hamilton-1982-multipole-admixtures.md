---
type: source
title: "Lange, Kumar & Hamilton 1982 - E0-E2-M1 multipole admixtures in even-even nuclei"
aliases: [Lange Kumar Hamilton 1982 mixing-ratio review]
created: 2026-09-21
updated: 2026-10-07
status: ai-draft
review_status: unreviewed
source_type: review-and-data-compilation
reading_depth: deep-read
title_original: "E0-E2-M1 multipole admixtures of transitions in even-even nuclei"
authors: [J. Lange, Krishna Kumar, J. H. Hamilton]
journal: "Reviews of Modern Physics"
year: 1982
citation_key: lange_1982_E0E2M1
volume: 54
pages: "119-194"
doi: "10.1103/RevModPhys.54.119"
canonical_source: "https://doi.org/10.1103/RevModPhys.54.119"
library_file: "raw/papers/gpt/high-spin-20260920/review/1982_Lange et al_E0-E2-M1 multipole admixtures of transitions in even-even nuclei.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/review/1982_Lange et al_E0-E2-M1 multipole admixtures of transitions in even-even nuclei.pdf"
raw_sha256: "ed925a0577a9257903806acd209c1db707529e86a5bfd9a301a83d597bf78ffb"
nuclei: [even-even-nuclei]
reactions: [decay-spectroscopy, angular-correlation, conversion-electron]
experiments: [historical-mixing-ratio-database]
models: [single-particle, rotational, rotation-vibration, pairing-plus-quadrupole, interacting-boson]
observables: [E2-M1-mixing-ratio, E0-E2-mixing-ratio, internal-conversion, B(E2), B(M1), monopole-matrix-element]
methods: [angular-correlation, angular-distribution, linear-polarization, internal-conversion]
tags: [mixing-ratio, E0, E2, M1, review, even-even]
---

# E0–E2–M1 multipole admixtures in even-even nuclei

## Bibliographic Record

- J. Lange, K. Kumar & J. H. Hamilton, *Rev. Mod. Phys.* **54**, 119–194 (1982), DOI `10.1103/RevModPhys.54.119`。原 PDF 共 76 页，首/末页页眉为 119/194；旧页范围 119–185 已据原件纠正。

## Scope and Reading Depth

- The 76-page RMP was read section-by-section and table-by-table: Introduction; definitions and sign conventions; collective, rotational, rotation–vibration, microscopic PPQ and IBM models; the adopted E2/M1 and E0/E2 compilation (Tables I–IX); data-quality notes; and the comparison/conclusions through the final references. Dense table pages were visually checked where OCR was unreliable.

- 2026-10-07 定向复核：摘要、目录和引言主线；printed pp.121–123 / PDF pp.3–5 的定义与约定；printed p.169 / PDF p.51 的 Eq.4.1；首末页与 raw 哈希。本次没有重读全部数据表，不把历史摄入的全文覆盖声明当成本次新完成的阅读。本文 PDF 页号 = printed page − 118；下文旧的 `PDF pp.121…` 写法所指实际为印刷页码。

## Definitions and Convention Rules

初态 `J1,π1`，末态 `J2,π2`。Sec.II.A 限定 E2/M1 同时允许：`J1+J2≥2`、`|J1−J2|≤1`、`π1π2=+1`。Eq.2.1 定义 `δ²=Tγ(E2)/Tγ(M1)`；这里 `Tγ` 是 γ 发射率，不是含内转换的总跃迁率。

Eq.2.5 的完整 Krane–Steffen 定义是：

`δKS = (√3/10) qγ ⟨J2||M(E2)||J1⟩ / ⟨J2||M(M1)||J1⟩`，`qγ=Eγ/(ℏc)`。

末态在左、初态在右，算符和约化矩阵元采用 Bohr–Mottelson 约定，E2 算符没有加入 Coulomb-excitation 分析中常见的 `i^λ` 因子。Eq.2.6 写成常用单位为 `δKS=0.835 Eγ(MeV) × RME(E2)[eb]/RME(M1)[μN]`。原文 “positive root” 表示 Eq.2.5 的比例系数取正，矩阵元之比仍有正负；它不要求所有 δ 非负，也不等于裸矩阵元或裸 B 值之比。定位：printed p.121 / PDF p.3, Eqs.2.1–2.6。

发射级联 `J1→J2→J3` 的第一、第二 γ 在 Eq.2.8a/b 分别有 `−2δF`、`+2δF` 干涉项。printed p.122 / PDF p.4 末给出 `δKS(γ1)=−δBR(γ1)=−δRB(γ1)`，`δKS(γ2)=+δBR(γ2)=−δRB(γ2)`。这是该发射级联与其几何系数的约定映射，不能直接照搬到吸收或其它 multipole pairs。Eq.2.10b 的 RB 电算符有发射 `+` / 吸收 `−`，磁算符 Eq.2.10c 没有此正负项；Eq.2.9a/b 的交叉项分别取 `±2δR` / `∓2δR`（上号发射）。Eq.2.10a 还给出 `RΛ,RB=(−1)^(λ−λ′+Λ)FΛ,FS`，Eq.2.11 给出 RB/BM 约化矩阵元的 `(2J2+1)^−1/2` 归一化映射。

作者在固定 BM 算符定义下说明：同时交换初末态使 E2、M1 获得相同 `(−1)^(J1−J2)` 因子，因此比值不变。这不表示任意算符/发射吸收约定均可交换。Sec.II.A/B 没有显式推导时间反演与实数 δ；实数性条件回到 [[rose-brink-1967-phase-defined-angular-distributions]] 的 Eq.3.32 note(v) 和 Eq.3.39 footnote17。

E0/E2 的 `qK²=T_K(E0)/[αK(E2)Tγ(E2)]`（Eq.2.12, printed p.123 / PDF p.5）是 K 壳电子混合比，和光子波数 `qγ` 不同。Eq.4.1（printed p.169 / PDF p.51）在 M1/E2 两个 γ 成分的截断下给出：

`αK,obs=[αK(M1,λpen)+δ²(1+qK²)αK(E2)]/(1+δ²)`。

分子包含 E0_K、E2_K、M1_K 电子，分母只含 E2、M1 γ；`λpen` 是 M1 penetration 参数，不是 multipole rank。只有忽略 E0 与 penetration 才退化为普通两成分 ICC 式；它只约束 δ²。`2+→2+` 可以有非 γ 的 E0 通道，不能用单 γ 的 rank 列表把它排除。Pair 通道的能量条件未由这些段落给出，不归入该式的直接证据。

The review's first-order rotation–vibration treatment gives selection-rule and angular-momentum dependence for β/γ-to-ground-band transitions. It shows why E2-dominated collective transitions can nevertheless acquire sensitive M1 admixtures through band mixing, and why signs can vary with nucleus and transition even when the macroscopic deformation looks similar (pp.124–133, Eqs.3.14–3.47).

## Model Comparison and Data Audit

The model survey compares the single-particle/Weisskopf limit, rigid-rotor and rotation–vibration estimates, PPQ/quasiboson and self-consistent time-dependent Hartree–Bogolyubov methods, dynamic deformation, and IBM (pp.123–132). PPQ generally captures the signs and a broad set of magnitudes better than IBM, while IBM can fit selected magnitudes; neither removes the nucleus- and transition-specific sensitivity of the M1 matrix element (pp.178–180, Tables V–VI). E0 data show large β→ground-band values and very small γ→ground-band values, but E0 strength is not a unique β-band signature because two-quasiparticle states can also produce large values (pp.180–183, Tables VII–IX).

The adopted data table is a critical survey through January 1980, not a homogeneous new experiment. It excludes or downgrades cases with unresolved close-lying transitions, inconsistent `A2/A4`, NaI summing, unknown gating multipolarity, hyperfine attenuation or incompatible results; numerous nucleus-specific footnotes document these decisions (pp.133–167). In heavy even-even systems, the table shows very large E2/M1 ratios compared with the single-particle limit, but the spread and sign changes remain real structure information rather than a universal deformation meter.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LKH82-1 | δKS includes the positive kinematic factor `(√3/10)qγ` multiplying the signed BM E2/M1 reduced-matrix-element ratio; `δ²=Tγ(E2)/Tγ(M1)`. “Positive root” does not remove a negative matrix-element ratio. | convention-boundary | direct | Sec.II.A, printed p.121 / PDF p.3, Eqs.2.1–2.6 | true |
| LKH82-2 | PPQ generally captures signs and broad magnitudes better than IBM in the reviewed comparisons, but neither is universal. | model-comparison | mixed | PDF pp.123–132, 178–180, Tables V–VI | true |
| LKH82-3 | The historical E0/E2/M1 compilation is heterogeneous and preserves detector/feeding/branch-quality exclusions in footnotes. | data-compilation | direct | PDF pp.133–167, Tables I–IX | true |
| LKH82-4 | The fixed KS convention and the RB/BR emission-cascade conventions differ in the signs shown separately for the first and second gamma; absorption requires the operator/geometry mapping in Eqs.2.9–2.11. | convention-boundary | direct | Sec.II.A, printed p.122 / PDF p.4, Eqs.2.7–2.11 and final sign relations | true |
| LKH82-5 | Same-spin, same-parity transitions may contain E0 conversion in addition to gamma multipoles; K-shell ICC can then depend on E0/E2 admixture and M1 penetration as well as δ². | formula-and-limitation | direct | Sec.II.B, printed p.123 / PDF p.5, Eq.2.12; Sec.IV.B, printed p.169 / PDF p.51, Eq.4.1 | true |

## Summary

This RMP is a convention- and provenance-aware bridge from historical mixing-ratio measurements to collective and microscopic model tests.

## Competing Interpretations and Limitations

- Review tables are not independent experiments and must be traced to the cited primary source for numerical use.
- E0 strength and E2/M1 magnitude are sensitive to configuration mixing, band assignment and model assumptions; neither is a stand-alone deformation observable.

## Analytical Reconstruction and Self-Audit

| ID | Audit item | Agent judgment | Locator | Status |
|---|---|---|---|---|
| LKH82-AR-1 | Definition chain | `δ` includes photon-energy normalization and the signed E2/M1 matrix-element ratio; `δ²` alone loses interference information. | printed pp.121–123 / PDF pp.3–5, Eqs.2.1–2.15 | self-checking |
| LKH82-AR-2 | Model hierarchy | Collective limits organize trends, but microscopic configuration mixing is needed for sign/magnitude variations; PPQ and IBM are not interchangeable evidence. | PDF pp.123–132, Tables V–VI | self-checking |
| LKH82-AR-3 | Compilation reliability | Table values are curated from heterogeneous angular-correlation, angular-distribution, polarization and conversion data; footnotes preserve unresolved branches and detector-era failures. | PDF pp.133–167, Table I notes | self-checking |
| LKH82-AR-4 | E0 interpretation | Large E0/E2 is compatible with β collectivity but can also arise from quasiparticle/shape-coexistence configurations. | PDF pp.169–183, Tables VII–IX | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[multipole-mixing-ratio]], [[angular-distribution]], [[angular-correlation]], [[linear-polarization-asymmetry]] and the batch-wide evidence/convention checklist; it supplies the historical bridge for HS-076, HS-081, HS-088 and HS-112.
- Reusable rule: retain sign convention, state order, alignment attenuation, gate complexity and table footnotes alongside every adopted δ; never treat a review compilation as independent experimental evidence.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `LKH82-P0-1`: Before paper-level numerical reuse, return to the cited primary angular-correlation/polarization paper and the exact table footnote; the review's adopted value is a traceable index, not a replacement source.

## Extracted Pages

- Methods/observables: [[multipole-mixing-ratio]], [[angular-distribution]], [[angular-correlation]], [[linear-polarization-asymmetry]]。

- Day8 方法依赖回链：[[spin-parity-assignment]] 保存 spin/parity/multipolarity 的观测与共享输入审计；[[multipole-mixing-ratio]] 保存三例全候选及 convention 边界。
