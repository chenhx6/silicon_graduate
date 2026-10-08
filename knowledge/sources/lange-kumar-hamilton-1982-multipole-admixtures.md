---
type: source
title: "Lange, Kumar & Hamilton 1982 - E0-E2-M1 multipole admixtures in even-even nuclei"
aliases: [Lange Kumar Hamilton 1982 mixing-ratio review]
created: 2026-09-21
updated: 2026-10-08
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

- 2026-10-07 模型续读：Sec.III printed pp.123–133 / PDF pp.5–15 的模型主线；Sec.V pp.174–184 / PDF pp.56–66 的比较、讨论和结尾叙述；Sec.IV.A.2 pp.167–169 / PDF pp.49–51 的数据质量方法。原图重点核对 pp.125–129、131–133、178–179、183 与 p.121。实际目录没有独立 Summary 节；p.183 的结论段延续到 p.184，随后为 Acknowledgments/References。历史表格仅核相关 caption、角色和讨论，没有逐行重新认证全部数值或被引原始实验。

## Definitions and Convention Rules

初态 `J1,π1`，末态 `J2,π2`。Sec.II.A 限定 E2/M1 同时允许：`J1+J2≥2`、`|J1−J2|≤1`、`π1π2=+1`。Eq.2.1 定义 `δ²=Tγ(E2)/Tγ(M1)`；这里 `Tγ` 是 γ 发射率，不是含内转换的总跃迁率。

Eq.2.5 的完整 Krane–Steffen 定义是：

`δKS = (√3/10) qγ ⟨J2||M(E2)||J1⟩ / ⟨J2||M(M1)||J1⟩`，`qγ=Eγ/(ℏc)`。

末态在左、初态在右，算符和约化矩阵元采用 Bohr–Mottelson 约定，E2 算符没有加入 Coulomb-excitation 分析中常见的 `i^λ` 因子。Eq.2.6 写成常用单位为 `δKS=0.835 Eγ(MeV) × RME(E2)[eb]/RME(M1)[μN]`。原文 “positive root” 表示 Eq.2.5 的比例系数取正，矩阵元之比仍有正负；它不要求所有 δ 非负，也不等于裸矩阵元或裸 B 值之比。定位：printed p.121 / PDF p.3, Eqs.2.1–2.6。

同页 Eq.2.2 给出 `Tγ(XL)=8π(L+1)/{L[(2L+1)!!]²ℏ} qγ^(2L+1)B(XL)`，Eq.2.3a 给出 `B=|⟨J2||M(XL)||J1⟩|²/(2J1+1)`。该电磁约定与 Eq.2.3c 中 `eℏ/(2Mc)` 的磁算符一致；不能直接混入 SI charge/moment。[[high-spin-lifetime-strength-deformation]] 保存从这些定义到现代 E2/M1 单位系数、mean/partial lifetime、total/photon branching、IC 和误差的重构。现代绝对寿命系数不是本页直接印出的数值，须与作者 quoted B 分开。

发射级联 `J1→J2→J3` 的第一、第二 γ 在 Eq.2.8a/b 分别有 `−2δF`、`+2δF` 干涉项。printed p.122 / PDF p.4 末给出 `δKS(γ1)=−δBR(γ1)=−δRB(γ1)`，`δKS(γ2)=+δBR(γ2)=−δRB(γ2)`。这是该发射级联与其几何系数的约定映射，不能直接照搬到吸收或其它 multipole pairs。Eq.2.10b 的 RB 电算符有发射 `+` / 吸收 `−`，磁算符 Eq.2.10c 没有此正负项；Eq.2.9a/b 的交叉项分别取 `±2δR` / `∓2δR`（上号发射）。Eq.2.10a 还给出 `RΛ,RB=(−1)^(λ−λ′+Λ)FΛ,FS`，Eq.2.11 给出 RB/BM 约化矩阵元的 `(2J2+1)^−1/2` 归一化映射。

作者在固定 BM 算符定义下说明：同时交换初末态使 E2、M1 获得相同 `(−1)^(J1−J2)` 因子，因此比值不变。这不表示任意算符/发射吸收约定均可交换。Sec.II.A/B 没有显式推导时间反演与实数 δ；实数性条件回到 [[rose-brink-1967-phase-defined-angular-distributions]] 的 Eq.3.32 note(v) 和 Eq.3.39 footnote17。

E0/E2 的 `qK²=T_K(E0)/[αK(E2)Tγ(E2)]`（Eq.2.12, printed p.123 / PDF p.5）是 K 壳电子混合比，和光子波数 `qγ` 不同。Eq.4.1（printed p.169 / PDF p.51）在 M1/E2 两个 γ 成分的截断下给出：

`αK,obs=[αK(M1,λpen)+δ²(1+qK²)αK(E2)]/(1+δ²)`。

分子包含 E0_K、E2_K、M1_K 电子，分母只含 E2、M1 γ；`λpen` 是 M1 penetration 参数，不是 multipole rank。只有忽略 E0 与 penetration 才退化为普通两成分 ICC 式；它只约束 δ²。`2+→2+` 可以有非 γ 的 E0 通道，不能用单 γ 的 rank 列表把它排除。Pair 通道的能量条件未由这些段落给出，不归入该式的直接证据。

The review's first-order rotation–vibration treatment gives selection-rule and angular-momentum dependence for β/γ-to-ground-band transitions. It shows why E2-dominated collective transitions can nevertheless acquire sensitive M1 admixtures through band mixing, and why signs can vary with nucleus and transition even when the macroscopic deformation looks similar (pp.124–133, Eqs.3.14–3.47).

## Model Comparison and Data Audit

The model survey compares single-particle/Weisskopf, rigid-rotor/rotation–vibration, PPQ/quasiboson, self-consistent time-dependent Hartree–Bogolyubov, dynamic deformation and IBM approaches (Sec.III, printed pp.123–133 / PDF pp.5–15). 对Table V的共同样本，作者明确说IBM更符合δ的magnitudes、PPQ更符合signs；可共同比较的8例中，IBM错号3例、PPQ1例。PPQ可比较的更大46例中有8例sign disagreement，并明确指出W isotopes的disagreement。不能将8例与46例当同一统计基线，也不把这一historical comparison升为模型普遍优劣。M1 transition matrix element在这些案例典型约±0.01 nm，而diagonal magnetic-moment matrix element典型约1 nm，解释δ对wavefunction/operator细节敏感。旧知识页将PPQ同时概括为幅度/符号更优，已据原图纠正（printed p.179 / PDF p.61，Table V后左栏前三段；Table VI为另一collective model比较）。 E0 data show large β→ground-band values and very small γ→ground-band values, but E0 strength is not a unique β-band signature because two-quasiparticle states can also produce large values (pp.180–183, Tables VII–IX).

The adopted data table is a critical survey through January 1980, not a homogeneous new experiment. It excludes or downgrades cases with unresolved close-lying transitions, inconsistent `A2/A4`, NaI summing, unknown gating multipolarity, hyperfine attenuation or incompatible results; numerous nucleus-specific footnotes document these decisions (pp.133–167). In heavy even-even systems, the table shows very large E2/M1 ratios compared with the single-particle limit, but the spread and sign changes remain real structure information rather than a universal deformation meter.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LKH82-1 | δKS includes the positive kinematic factor `(√3/10)qγ` multiplying the signed BM E2/M1 reduced-matrix-element ratio; `δ²=Tγ(E2)/Tγ(M1)`. “Positive root” does not remove a negative matrix-element ratio. | convention-boundary | direct | Sec.II.A, printed p.121 / PDF p.3, Eqs.2.1–2.6 | true |
| LKH82-2 | 作者对Table V共同样本报告IBM更合δ magnitudes、PPQ更合signs；8共同例错号IBM3/PPQ1，PPQ更大46例错号8且W isotopes有明显disagreement。样本/比较量不同，不能概括成PPQ在幅度与符号都胜IBM或普遍model ranking。 | author-interpretation | direct | printed p.179 / PDF p.61，Table V后左栏comparison三段；model scope Sec.III printed pp.123–133 / PDF pp.5–15 | true |
| LKH82-3 | The historical E0/E2/M1 compilation is heterogeneous and preserves detector/feeding/branch-quality exclusions in footnotes. | data-compilation | direct | PDF pp.133–167, Tables I–IX | true |
| LKH82-4 | The fixed KS convention and the RB/BR emission-cascade conventions differ in the signs shown separately for the first and second gamma; absorption requires the operator/geometry mapping in Eqs.2.9–2.11. | convention-boundary | direct | Sec.II.A, printed p.122 / PDF p.4, Eqs.2.7–2.11 and final sign relations | true |
| LKH82-5 | Same-spin, same-parity transitions may contain E0 conversion in addition to gamma multipoles; K-shell ICC can then depend on E0/E2 admixture and M1 penetration as well as δ². | formula-and-limitation | direct | Sec.II.B, printed p.123 / PDF p.5, Eq.2.12; Sec.IV.B, printed p.169 / PDF p.51, Eq.4.1 | true |
| LKH82-6 | Under the explicit M1/E2 gamma truncation and no-penetration assumption, a single K-shell ICC generally leaves a continuum of δ²/E0-rate solutions. Zero reference-gamma rates require a different rate normalization; δ=0 does not itself exclude E0 conversion. The inequalities and endpoints are our reconstruction, not the author's directly tabulated result. | our-inference | indirect | Premises: printed p.123 / PDF p.5, Eq.2.12; printed p.169 / PDF p.51, Eq.4.1 and the requirement that E2/M1 admixture be known before E0/E2 extraction | true |
| LKH82-7 | 合成same-spin/parity四γ U pair在one total electron ICC与τ下，可于αobs≥maxκ、λγ和Ω_e,total正的条件下由不同非负E0 rates完成；额外shell能否辨别由明确contrast及covariance决定。这是47-check条件性补全，不证明任意data可fit或微观实现。 | our-inference | indirect | premises printed123/PDF5 Eq2.12; printed169/PDF51 Eq4.1; KB08 printed204/PDF3 Eqs6–7/11; gamma pair RB67-14 | true |
| LKH82-8 | Eq.3.9 的形变无关零阶项是常数乘总 J，不能连接不同能量态；完整一阶算符另含 αJ 修正。通用 rank-1 张量不必等于 J；零值限于该模型项。交换子及 internal-multiplet 证明是本任务推导。 | model-boundary-and-our-inference | indirect | printed pp.124–125 / PDF pp.6–7 Eqs.3.5/3.9; p.127 / PDF p.9 Sec.III.C.3; p.128 / PDF p.10 末段; generic M1 Eq.2.3c p.121 | true |
| LKH82-9 | n=1→0 的直接算符修正与波函数混合必须按同一小振幅阶次保留；首阶 derivative 为零不保证所有阶次为零。ΔK 的使用还需此算符、K purity 和近轴对称条件。 | source-model-result | direct | printed pp.126–127 / PDF pp.8–9 Eqs.3.21–3.24; pp.128–129 / PDF pp.10–11 Eqs.3.31–3.40、152Sm 例及 footnote 3 | true |
| LKH82-10 | PPQ 在投影五维集体空间内处理 rot-vib/K mixing，不消除 adiabatic、interaction、basis、pairing 和直接 quasiparticle coupling 的限制；Table V theory δ 使用实测 Eγ，是条件性模型比较。 | model-and-input-boundary | direct | printed p.131 / PDF p.13 Sec.III.D.2–3; p.133 / PDF p.15 spin/Pauli 限制; p.178 / PDF p.60 Table V caption | true |
| LKH82-11 | 大 δ 仅固定 E2/M1 部分光子率比，不能给绝对 E2 增强；允许 M3/E4 时还不固定全部辐射的 E2 份额。DF shape-factor 消去式只在共同率非零时定义比值，零率点是极限。 | our-inference-with-model-premise | indirect | printed p.121 / PDF p.3 Eqs.2.1–2.6; p.125 / PDF p.7 Eqs.3.10–3.13; low-order scope p.119 / PDF p.1 | true |
| LKH82-12 | p.169 明给 M1 penetration 的线性/二次修正式，原叙述为增强 IC；没有本题系数或允许参数域。未知修正下 E0 的非负率排除需指定 reference model/允许域；固定独立 t 与未修正 E2、非负 M1 时仍有 E2 floor。δ sign 与 penetration 参数的符号信息不同。 | source-formula-and-our-inference | indirect | printed p.169 / PDF p.51 Eq.4.1 下方修正式与叙述；p.123 / PDF p.5 Eq.2.12；KB08 printed pp.207–208 / PDF pp.6–7 Eq.24、NP/SC 比较 | true |
| LKH82-13 | 同一物理Hermitian核多极、标准BM归一时，反向RME须复共轭且B反向带初态自旋简并比。该方向变换是推导，不增加独立测量；RB同算符归一须换bra-spin因子，不能代替photon-T的adjoint/发射吸收映射。 | our-inference-with-definition-premise | indirect | printed121/PDF3 Eq2.3a–c；printed122/PDF4 Eqs2.10–2.11与state-reversal段；RB67 printed316/PDF11 Eq3.22的不同adjoint | true |
| LKH82-14 | 同electric type/energy/transition，在所用长波核电算符率公式内，E4/E2率比=(5/23814)(qR)^4|χ|²，χ=M4/(R²M2)需M2非零。小qR必须结合独立矩阵元界才支持此率截断；不单独控制干涉角分布误差或证明真实核素高阶不存在。 | our-inference-with-formula-premise | indirect | printed121/PDF3 Eqs2.2/2.3a–b；RB67 printed313–314/PDF8–9 Eq3.12与footnote9、p318/PDF13 Eqs3.29–3.30与footnote12；46-check hierarchy | true |
| LKH82-15 | Eq2.3c的orbital l是作用于态的导数；hard radius/归一和small totalJ不能直接继承electric multiplication范数界。固定2→1的two-orbital形式反例可有增长RME，物理域需另控orbital/kinetic moments与nonrel/current有效性，不预测真实低能强度无界。 | our-inference-with-operator-premise | indirect | printed121/PDF3 Eqs2.3a/c；p125/PDF7 Eq3.9、p127/PDF9 generator-only scope；54-check magnetic domain/CG/6j/Racah重构 | true |
| LKH82-16 | 对同一 2+→2+ 的 M1/E2 截断，独立 hard-support、磁 moment/domain 与正 E2 floor 可条件性界定完整 M3+E4 被省 photon-rate 份额及绝对测量误差；未给实际先验，不认定真实截断已有效。 | our-inference-with-operator-premise | indirect | printed p.121/PDF3 Eqs.2.2–2.3c；72-check conjugated M3 gradient Gram、B/units/rate budget；RB67-21/22 的条件误差界 | true |

## Collective M1 Zero, Perturbation Order and Transfer Conditions

### 总角动量算符的零值与普遍选律

Eq.3.9 保留至表面形变 α 的一阶。其第一项是

\[
\mathcal M_0(M1,q)=\sqrt{3/(4\pi)}\,\mu_N g_R\bar J_q,
\qquad \bar J_q=J_q/\hbar.
\]

g_R=Z/A 是均匀电荷/磁矩密度模型的假设；μ_N 是核磁子。Eq.3.9 的第二项另含 αJ，不属于常数乘 J 的零值证明。p.127 明确限定 “zeroth-order (deformation-independent) part”，p.128 再指出该项是 a constant times J。不能把作者保留一阶算符的整个 M1 预测都称为零。

下面是从 rotationally invariant H、good J 和正交态推出的本任务证明，原文没有逐式给出：

\[
[H,J_q]=0\quad\Rightarrow\quad
(E_f-E_i)\langle f|J_q|i\rangle=0.
\]

表示空间可写成各 J 的 internal multiplicity space 与 spin-J representation 的直和；J 对 internal space 是恒等算符。因此

\[
\langle\nu_fJ_f\|\bar J\|\nu_iJ_i\rangle
=\delta_{J_fJ_i}\delta_{\nu_f\nu_i}
\sqrt{J_i(J_i+1)(2J_i+1)}.
\]

这里的 RME 采用末态在左的标准 Wigner–3j 归一化；不把它与 RB Eq.3.39 的初态 bra 及其辐射振幅归一化直接等同。ν 标记正交内部 multiplets。J± 在同一简并 multiplet 的不同 M 子态间可非零；这些矩阵元不构成孤立核的有限能量结构 γ 跃迁。外场破坏交换关系、非正交近似态或非恒定 gyromagnetic operator 都需要另行处理。

通用 M1 算符 Eq.2.3c 分别含核子的 orbital/spin 权重，通常不是共同常数乘 total J。合成两个正宇称 J=2 multiplets 的合法 rank-1 张量 `σx_internal⊗Jq` 可连接不同能量态；它和 generator-only 零值共同经过 SU(2) 交换关系核验。此反例仅区分 triangle/parity 允许与模型项为零，没有给真实核素指定该 toy current，也没有测得 hindrance。判断受抑仍需绝对强度及明确参考。

### 同阶项与模型范围

- p.126 Eqs.3.21–3.24 对 equilibrium shape 展开算符与态；n=1→0 的 direct operator term 与 band-mixing term 都是一阶小振幅，作者明确批评旧的 zeroth/first 标签。n=0→0 的一阶 fluctuation correction 消失是另一条件性结果。
- pp.128–129 Eqs.3.31–3.40 用 shape-dependent g 的导数产生 β/γ→g 的 M1。用 `Gν=μ_N gν` 保留 dimensionful slope，β 无量纲、γ 用 rad；source 以 n.m. 报告的导数不可再次乘 μ_N。152Sm 例的首阶导数为零，作者仍报告来自更高阶的小非零 M1，且没有将该性质推广所有核。
- p.129 footnote 3 指出所用算符的 body-J 和 D-function 各可改 K 一单位，因而可连接 ΔK=2。不能脱离该算符与波函数近似只用 L=1 宣布这一模型跃迁必为零。
- p.131 的 PPQ 方法在 adiabatic time-derivative expansion 至二阶后，将 3A 维问题投到五维 quadrupole collective space。空间内 K/rot-vib mixing 的处理保留 PPQ interaction、HO radial basis、忽略 Coriolis antipairing/随自旋 pairing 减弱、直接 two-or-more-quasiparticle coupling 的限制。p.133 的约 ±15% spin contribution 是该模型讨论：对 static moment 可小，对已很小的 transition M1 却重要；不是统一修正系数。同页提醒 naive collective/few-nucleon combination 的非正交与 Pauli 问题。

### 比值、绝对率和高阶截断

同一 Eγ、同一任意 √rate 单位下，`(aM1,aE2)=(1/100,1)` 与 `(1/10000,1/100)` 都给 δ=100，但 E2 部分率相差 10⁴。δ 本身丢失绝对尺度；M1=0 时该比值没有普通有限值或相对符号，两者皆零是 0/0。允许其它 γ 成分时 `δ²/(1+δ²)` 只是在 M1/E2 子集中的 E2 份额。

DF rotor 的 Eqs.3.10–3.12 有共同 shape factor。非零时消去得到

\[
\delta_{DF}^{2}=\frac{3q_\gamma^2}{100}\frac7{80}
\left(\frac{ZeR_0^2}{g_R\mu_N}\right)^2.
\]

source 采用 `R0=1.2 A^(1/3) fm`、`gR=Z/A`，Eq.3.13 给 `|δDF|=3.56×10⁻³ Eγ(MeV) A^(5/3)`。β=0 或 sin(3γ)=0 使所保留两率都为零时，消去后的表达式只作为模型极限，不能赋予无辐射点一个实测 mixing ratio。Eq.3.46 的 sign/shape-derivative 关系也有模型条件，不是通用 prolate/oblate 标志。

把 [[rose-brink-1967-phase-defined-angular-distributions]] 的自由多极反例用于真实核时，需核共同 many-body states/current、long wavelength 和 matrix-element 尺度、高阶率上限、绝对率与非 γ inventory，以及 population/gate/response/covariance。p.119 的低阶观察近似和 p.121 Eq.2.2 的 `qγ^(2L+1)` 因子不单独证明 M3/E4 为零；低阶项已受抑时尤其不能只凭小 qR 删除高阶。模型可限制自由振幅的物理实现范围，必须把这一先验与测量约束分开。

本节 27 项精确代数检查及 raw/原图哈希由主代理复现；是 L2 source-bound reconstruction，不是核素计算、实验拟合或 L4。Table V 的 magnitudes/signs 历史比较保留 LKH82-2，caption 所用实测 Eγ 是共享输入，既有 review compilation 不增加独立实验。

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

- 2026-10-07 `revises` 旧PPQ/IBM比较概括：原图p179区分magnitudes与signs及8/46样本，原needs_review保持true；该review比较不增加独立实验。
- 2026-10-07 `limits` generator-only M1 零值的外推、大 δ 的绝对强度解读与高阶删除；`supports` 同阶 operator/wave-function 展开和模型输入审计，见 LKH82-8–11。本轮 Sec.III/V 主线覆盖与历史全文摄入分开，不重认证全部历史表格。

- Effect: `supports` [[multipole-mixing-ratio]], [[angular-distribution]], [[angular-correlation]], [[linear-polarization-asymmetry]] and the batch-wide evidence/convention checklist; it supplies the historical bridge for HS-076, HS-081, HS-088 and HS-112.
- Reusable rule: retain sign convention, state order, alignment attenuation, gate complexity and table footnotes alongside every adopted δ; never treat a review compilation as independent experimental evidence.
- Review state: Codex self-audited; not `human-reviewed`.

## ICC/E0 Identifiability and Reference-Rate Boundaries

本轮由 Eqs.2.12/4.1 重构合成 `2+→2+` 的逆问题。全部 gamma 候选仍为 M1/E2/M3/E4；以下额外截断为M1/E2、忽略penetration，并只讨论K壳。须 `αK(E2)>0`；a/r的归一化不适用于闭合/空K壳或其它使该参考系数为零的情形。本节 `a=αK(M1)/αK(E2)>0` 是纯ICC比，与前文辐射振幅 a_Lπ 分开。

定义 `t=δ²=Tγ(E2)/Tγ(M1)>0`、`z=qK²=T_K(E0)/[αK(E2)Tγ(E2)]≥0`、`r=αK,obs/αK(E2)>0`。率定义给出：

`r=[a+t(1+z)]/(1+t)`，`z=(r−a)/t+r−1`。

用 `y=tz=T_K(E0)/[αK(E2)Tγ(M1)]` 可写 `r=(a+t+y)/(1+t)`、`y=(r−a)+(r−1)t`。在有限t>0下，非负E0条件等价于 `(r−1)t≥a−r`。这些量全为dimensionless；Tγ/T_K是s⁻¹率，Γγ=ℏTγ有能量单位。

| Exact r/a 条件 | 可行有限 t>0 |
|---|---|
| r>1，a≤r | 任意t>0 |
| r>1，a>r | `t≥(a−r)/(r−1)` |
| r=1，a≤1 | 任意t>0，`z=(1−a)/t` |
| r=1，a>1 | 无有限解；pure E2是独立端点 |
| 0<r<1，a<r | `0<t≤(r−a)/(1−r)` |
| 0<r<1，a≥r | 无有限解 |

有限界点等号给z=0。a=1时 `r=1+tz/(1+t)≥1`；r=1令z=0但不定t。t=0时不能把有限z的代数延拓当成无E0：E2-rate分母为零，z未定义；改用y得到 `r=a+y`，y≥0仍允许pure M1 gamma+E0 electrons。固定有限z的t→0给r→a，固定y的路径可有z=y/t发散而r→a+y。pure E2时M1-rate为零，t/y坐标不适用；以E2为参照得 `r=1+z`。两种保留gamma rates皆零时electron/gamma比未定义，不能据此默许M3/E4也不存在。

z=0的普通两gamma式是纯系数的convex combination：`αobs=αM1/(1+t)+t αE2/(1+t)`，故 `min(a,1)≤r≤max(a,1)`。有限t>0、a≠1时严格位于内部；E0增加分子，只能使r相对同t普通混合值上升。高侧越界可与E0相容，低于min(a,1)则连非负E0也不能解释。这种越界只否定该假设包；M1 penetration、允许的M3/E4改变的系数集合、response/background或assignment问题仍须核查，不独证E0。

纯代数例 a=4,r=2 同时容许(t,z)=(2,0)与(4,1/2)，没有任何Z/E或原子ICC赋值。一个r通常不能拆出t/z；p.169直接说明E2/M1未知时不能唯一提取E0/E2。公式只含δ²，不给δ sign。上述不等式与奇异参考端点由我们从率定义推出；原指定段落没有直接讨论这些2+→2+端点。K壳结果也不能替代总转换系数或其它分支的total-lifetime归一化。

## Gamma, Total ICC and Lifetime with an Allowed E0 Component

本节用合成2+→2+的RB67-14 U pair作companion-completeness反证。四γ自由实振幅、相同aligned布居与λγ>0保持；额外E0只作electron conversion，忽略penetration、pair与其它branches。没有指定Z/E或使用Mu08/FO数字。直接前提：LKH82 p123/PDF5 Eq2.12、p169/PDF51 Eq4.1；KB08 p204/PDF3 Sec3.1 Eqs6–7/11的 `T_s(E0)=ρ²Ω_s`，ρ无量纲、Ω单位s⁻¹。E0同spin/parity允许、single γ禁止。

定义 `κ_j=Σ_L f_L,j α_e,total,L` 为普通四γ的electron ICC baseline，Ω_e,total=ΣsΩ_s>0；αobs是包含E0的total electron/γ率比。若 `αobs≥max(κ_a,κ_b)`，可取

`T_j(E0)=λγ(αobs−κ_j)≥0`，`ρ_j²=λγ(αobs−κ_j)/Ω_e,total`。

于是两模型均有 `αtotal=αobs`、`τtotal^−1=λγ(1+αobs)`；光子W/Δ、共同gamma scale和γfraction总概率也保持。κ不同则需要不同E0 rate。此构造说明单个total ICC与总寿命可以在E0自由度下仍不排除该不同multipole pair；并非任意data都能补全。αobs若低于较大κ，该model须negative E0而被排除；高κ端点E0=0，严格高于两κ时两E0均正。独立已知λγ与实测τ不满足上述一致式时两模型都失败，不能同时保持total ICC又另调E0修τ。

λγ=0时electron/γ比和photonic normalization失效，不等于没有E0；Ω_e,total=0时不能按ρ²分解非零T0；closed shell Ω_s=0不收到E0电子。原E2-reference qK²在E2 gamma为零也失效，total-gamma归一化没有继承这一分母。本节符号/端点47项经主代理复现（约8.41s），是L2 rate algebra与source-bound reconstruction，不是新的核素/实验或microscopic realizability证明。

### Shell 信息何时能破除该对

令 `η_s=Ω_s/Ω_e,total`、`κ_s,j=Σ f_L,j α_s,L`，Ση_s=1、Σκ_s,j=κ_j。total完成后

`α_s,j=κ_s,j+η_s(αobs−κ_j)`，

`d_s=α_s,a−α_s,b=η_s(κ_b−κ_a)−(κ_s,b−κ_s,a)`，`Σs d_s=0`。

一个额外shell/total分布 `h_s=α_s/αobs` 仅当d_s≠0且uncertainty/response能分辨时可排除该对；两个shell/total观测测试两个contrasts，但纯two-shell分布仅一个独立shape degree。shell/shell比需正分母，并在 `d_s α_t,b−d_t α_s,b≠0` 时有判别力；同比例变化可能使比值盲。若全部 `κ_s,b−κ_s,a=η_s(κ_b−κ_a)`，整个shell向量仍退化，增加重复统计量不能补出信息。

统计独立与functionally independent约束分别核验。以primitive counts传播joint Jacobian，`α_s=αtotal·h_s` 是派生关系；不能将total、shell fractions和derived partial ICCs当三套独立输入。在理想independent-Poisson计数的一阶控制中，shell fractions之间负cov、shared gamma denominator使partial ICCs正cov，而totalα与shell fraction可零cross-cov；共同数据不意味着每一对cov都非零。真实background/efficiency/gates会改变该特例，需要actual covariance。

## Penetration, Reference Models and Conditional ICC Exclusions

printed p.169 / PDF p.51 的 Eq.4.1 下方明确写出

\[
\alpha_K(M1,\lambda_{pen})=\alpha_K^{ref}(M1)
\bigl[1+B_1(M1)\lambda_{pen}+B_2(M1)\lambda_{pen}^{2}\bigr].
\]

λ_pen 与 penetration/gamma 矩阵元之比相关；不是 photon rank 或 λ_γ 发射率。本文段落称 B1/B2 为 small expansion terms，却没有本题的数值、符号、完整参数归一化或允许 λ 域。作者描述额外 IC 而非 γ 发射、因此增大转换系数，尤其在 γ 高度受抑时；该来源叙述保留，不能把任意有符号多项式都当成作者认证的真实修正。小 B 也不单独约束未知的 B1λ/B2λ²。作者在此没有观察到 E2 penetration 的历史陈述，不是排除一切 E2 核结构修正的定理。

限定 M1/E2 γ、λ_γ=Tγ(M1)+Tγ(E2)>0，并令独立固定的 t=δ²。给定同一 reference model 下的修正后 M1 系数和未修正 E2 系数：

\[
\kappa_K(\lambda_{pen})=
\frac{\alpha_K^{ref}(M1)P(\lambda_{pen})+t\alpha_K(E2)}{1+t},
\quad
T_K(E0)=\lambda_\gamma[\alpha_{K,obs}-\kappa_K(\lambda_{pen})].
\]

这里 P 是上式括号，T_K(E0)≥0 当且仅当指定参数的 α_K,obs≥κ_K。未知 penetration 时，在物理允许域 Λ 内存在 κ_K≤α_K,obs 才可完成；只有所有允许参数都使 κ_K>α_K,obs 才能排除。若采用并独立验证“同一基线上的修正仅增强”，κ_K≥κ_K,ref，则原 fixed-baseline 低侧排除仍成立。更弱率模型中降低正 κ 的 toy 不是实证，也不证明实际 penetration 能降低系数。若使用 inf κ，下侧可排除；恰等于 inf 的端点还需最小值确实能取到。

一个不需要 M1 修正数值的条件性下界是

\[
\kappa_K(\lambda_{pen})\ge
\frac{t}{1+t}\alpha_K(E2).
\]

这只用修正后 M1 系数非负，还要求 t 独立固定、E2 系数不修正、M1/E2 截断。低于该 E2 floor 的数据排除此条件包；未知 t 可含 t=0，或 E2 也修正时，不能沿用正下界。固定 t 本身也未解决未知 penetration 与 E0 的分配。

[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] printed pp.207–208 / PDF pp.6–7, Eq.24 与 Sec.4.1.2 区分 NP 和 SC：HsIcc/RpIcc 使用 no-penetration，新的 DF 使用已近似纳入 penetration 的 surface-current 模型。现代 DF/FO 不能自动作 NP 的 λ=0 基线后再乘 Hager 修正；先核 reference mapping，避免重复计入。FO/NH 描述 atomic vacancy，独立于 NP/SC 的核流近似，No Hole 不等于 no penetration。本页固定 ordinary ICC 的构造是条件性输入，不许可任意调 κ；没有改变 MU08 的五个 FO 数值。

固定 penetration 参数时 Eq.4.1 对 δ→−δ、qK→−qK 不变，不能给 E2/M1 或 E0/E2 的相对符号。B1λ 是线性项，在已知系数/其它率/允许域下可对 penetration 参数符号敏感；不要将“不给 δ sign”扩大为“不含任何核矩阵元相位信息”。K-shell α 也不能代替所有壳层和分支的 total-lifetime inventory。M1 γ reference 为零时有限 α(M1,λ) 坐标失效，可能的 electron rate 要直接处理，不能默认 `0×∞=0`；E2 或 total γ reference 为零的端点同理。

本节35项符号检查经主代理复现，是既有来源定义与本任务率推导的 L2 边界；没有原子/核素数值拟合、物理 λ 域认证或新实验。

## Reverse Strength and Physical Operator Normalization

对同一对核态与物理核多极 `M_Lμ†=(−1)^μ M_L,−μ`，采用末态bra的标准BM/Wigner–3j归一，令 `Rfi=⟨Jf||M_L||Ji⟩`。由 spherical adjoint 与3j对称性得到本任务重构：

\[
R_{if}=(-1)^{J_i-J_f}R_{fi}^{*},\qquad
B_{f\to i}=\frac{2J_i+1}{2J_f+1}B_{i\to f}.
\]

E2的B单位保持e²b²，M1保持μ_N²；此式不要求RME是实数，B不确定其sign/phase。核强度的upward转换不是反向自发γ寿命，激发过程另需其运动学/反应响应。Already rate-derived B已包含Eq2.3a的初态spin除数，不能再除一次。

Eq2.11对**同一物理算符**的normalization-only映射为 `Rfi,RB=Rfi,BM/√(2Jf+1)`，因此 `B_i→f=(2Jf+1)/(2Ji+1)|Rfi,RB|²`；反向bra改为Ji，`Rif,RB=(−1)^(Ji−Jf)√[(2Jf+1)/(2Ji+1)]Rfi,RB*`。RB photon interaction T另有 Eq3.22 `T_Lμ†=(−1)^(L−μ+1)T_L,−μ` 与本页Eqs2.10的operator/发射吸收因子，不能用physical-M adjoint替它。

[[mukhopadhyay-2008-136nd-transition-rates]] 的18−→16−、quotedB(E2)=0.14(2)e²b²给派生reverse16−→18−值约0.157±0.022e²b²（statistical only），BM magnitude≈2.276eb。两方向确定性变换共享输入，不是新的excitation experiment；feeding/branch/ICC与未含stopping systematic原边界保留。190项实质代数/身份检查和247项phase-domain控制经主代理复现，归属唯一Day9无学分预习的L2。

## Electric Rank Hierarchy and Truncation Premises

从p.121 Eq.2.2 的 `C_L=8π(L+1)/{L[(2L+1)!!]²}` 得C2=4π/75、C4=2π/178605、C4/C2=5/23814。同一initial/final pair、Eγ和electric type下，物理BM核算符RME定义 `M4=R²χM2`，q=Eγ/(ℏc)为inverse length、R为指定physical length参照、χ无量纲，M2需非零：

\[
\frac{T_\gamma(E4)}{T_\gamma(E2)}
=\frac5{23814}(qR)^4|\chi|^2,
\qquad \frac{B(E4)}{B(E2)}=R^4|\chi|^2.
\]

同pair的spin因子抵消。R只是参照，不自动是wavefunction hard-support半径；R→sR会令χ→χ/s²，而rate expression不变。Source Gaussian约定 `[e²]=energy×length` 使两式率均为time⁻¹，不能裸混SI charge或RB Eq3.30的不同G_L normalization。

独立justify `|χ|≤X`、指定rate toleranceη>0时，`(5/23814)(qR)^4 X²≤η`才是这一个partial-rate截断的充分条件。χ=M4/(R²M2)没有选律给的普遍上界；M2很小时可大、M2=0时ratio chart失效。Fixed finiteχ的qR→0给率比趋零；χ随qR⁻²增长的代数控制可以阻止该极限，未构造真实核wavefunction。

RB67-19 原理想seed的E4/E2 photon比为1/4，需要 `|χ|=(63√30/10)/(qR)²≈34.5065/(qR)²`；第二认证分支比≈2.12584759，需要≈100.6230/(qR)²。只在合成qR=.01/.1及另加`|χ|≤1` prior时，这些formal分支不满足该prior。没有真实Eγ/R或独立χ界，不能据此称真实核不可能、确证低阶模型或比较两个分支的实际prior可信度。

RB pp.313–314 的Bessel长波近似与footnote9要求一致charge/current，p.318 footnote12另有残余electric energy dependence。以上系数/algebra限所采approximation，不保证finite-q/current余项的统一相对误差。小被省partial-rate也不单独给uniform angular/polarization-error bound：干涉按被省振幅的√rate尺度进入，还依赖population/response与归一分母。46项检查经parent复现；是L2模型迁移/量纲审计，不是新核素计算或L4。

### 额外hard-support假设下的条件范数界

下面是本任务推导，LKH82/RB没有直接报告该bound。对Eq2.3b的point-charge乘法算符，另要求normalized初末态、orthonormal final multiplet、固定charge sector `Qabs=Σk|ek|`、相关wavefunction配置严格满足每个rk≤R，以及standardY和无未控effective-charge/current/finite-q项。球谐addition identity与component-vector triangle给各配置的范数≤`Qabs R^L√[(2L+1)/(4π)]`；归一initialstate后投影到chosen final multiplet只会减小平方和。Eq2.3a的fixed-Mi和已含spin归一，故

`B(EL;i→f)≤Qabs²R^(2L)(2L+1)/(4π)`，不用再乘/除2Ji+1。

E4上界为`9Qabs²R^8/(4π)`；只有另有独立strict-positive `B(E2)≥B2min`，才得 `|χ|²≤9Qabs²R^4/(4πB2min)`。绝对E4上界本身不给普遍χ界；B2min→0会发散。TypicalR并不建立compact support，真实tails或projected-space moments需独立控制。独立source审计12项no-op、17项Fraction事实与10个fixed-Mi Racah求和确认系数/归一与复数χ模，未增加核素实现或experimental evidence。

## Magnetic Operator Domain and Radius-Only Bounds

p121 Eq2.3c采用非相对论one-body magnetic moment operator：µ(M)Σk[g_s s+2g_l l/(L+1)]·∇[r^L Y_Lµ]，µ(M)=eℏ/(2Mc)。括号gradient只微分solid harmonic，随后是vector乘法系数；dimensionless l=−i r×∇仍作用于wavefunction，s/g也无量纲。光滑共同domain上，Σa[l_a,∂a f]=−iεabc r_b∂c∂a f=0可移除contracted ordering差，不消除导数或证明boundedness。L=1给 √[3/(4π)]µ(M)Σ(g_l l_µ+g_s s_µ)，单位是moment；M=m_p时才采用µ_N，不能额外乘ℏ或混SI单位。

形式控制只取two distinguishable orbitaldegrees，不赋实际核素/Pauli sector：ℓ1=ℓ2=ℓ≥1，same normalized smooth radialfactor支持于a<r<R，couple到Ji=2、Jf=1。两state parity均+；weighted O=g1l1+g2l2=g2Jtot+(g1−g2)l1。Jtot不连接不同J，完整CG与独立6j/Racah给

|⟨(ℓℓ)1||l1||(ℓℓ)2⟩|²=[(2ℓ+1)²−4]/2=2ℓ(ℓ+1)−3/2。

ℓ=1,2,3,5分别为5/2、21/2、45/2、117/2；weighted RME乘g1−g2。物理M1 normalization下 B(M1;2→1)=(3/(20π))µ(M)²(g1−g2)²[2ℓ(ℓ+1)−3/2]，初态除数5已含。g1=g2回到generator-only zero；g不同是另一算符。这个共同R/fixedsmallJ的序列说明formal orbitaldomain没有radius-only uniformnorm，未给Hamiltonian、emissionenergy、低能谱或真实nuclear realization。

Uniform磁bound还需moment/domain或validated finite-space限制。对normalizedψ、固定有限N和boundedg，一个充分保守界是 B(M1)≤(3/(4π))µ(M)²[Σ|g_l,k|√⟨l_k²⟩+Σ|g_s,k|√⟨s_k²⟩]²，由component-vector triangle和finalprojection得出。Spin1/2的s²=3/4固定，orbitalmoments需另外输入。共同smooth support/domain有 ⟨l²⟩≤R²⟨p²⟩/ℏ²；support单独不提供momentum上界。Hamiltonian/energy路线需独立potential/domain控制，不能只用总能量标签。

相同radialfactor的⟨p²⟩含ℏ²ℓ(ℓ+1)∫|u|²/r²dr≥ℏ²ℓ(ℓ+1)/R²，因此ℓ∞最终超出任一固定nonrelmomentum/velocity域。此operator-domain反例不宣称实际低能M1强度无穷；finite-q、relativistic/effective/exchangecurrent需另核。54项parent核验含180component、32norm、12orthogonalitycontrols，仍L2；未修改既有electric条件界或推全部magnetic hierarchy。

## Conditional Budget for the Complete M3 and E4 Omission

选择定则允许的 M1/E2/M3/E4 全部保留作 full model，retained 取其自身 M1/E2 projection。以下是本任务的条件推导，原文 p.121 提供 rate、B 与算符约定。要求同一 2+→2+ pair、同正 Eγ 和初态ρ；相关态在共同光滑算符域中，归一且每个粒子严格 rk≤R，charge sector 固定，g 为有界实常数。磁算符另需独立有限 moments Sk≥Trρ sk²、Lk≥Trρ lk²；典型/rms 半径单独不给这些条件。定义

\[
A_3=\sum_k|g_{s,k}|\sqrt{S_k}+\frac12\sum_k|g_{l,k}|\sqrt{L_k}.
\]

fμ=r³Y3μ 的 complex-conjugated gradient Gram 为 G_ab=Σμ(∂a fμ)*∂b fμ。七个 solid harmonics 的直接 Cartesian 求和给

\[
4\pi G=21r^2(2r^2 I+\mathbf r\mathbf r^{\mathsf T}),\qquad
\operatorname{spec}G=\frac{r^4}{4\pi}(42,42,63).
\]

PSD 差等于 21r²|r×v|²；63 是局部 gradient map 的最优系数，随后 many-body triangle/final projection 的界保守。Eq.2.3c 对 M3 的 orbital 系数为1/2；contracted ordering identity 可把 gradient 放左，但 l 仍微分态。用 component-vector triangle、mixedρ purification 和 Eq.2.3a 的 fixed-Mi 求和，得到

\[
B(M3)\le B_{M3}^{\max}=\frac{63}{4\pi}\mu(M)^2R^4 A_3^2,
\qquad B(E4)\le B_{E4}^{\max}=\frac9{4\pi}Q_{\rm abs}^2R^8.
\]

两式已含 B 的 spin normalization，不再除5。µ(M)=eℏ/(2Mc)，统一 Gaussian 单位下是 charge×length；因此 BM3/BE2 带 length²。不得把 µN²b²/e²b² 的裸数字直接当无量纲。需独立同一 pair 的 B(E2)≥B2min>0，并使先验共同可行；由 C3/C2=8/441、C4/C2=5/23814，q=Eγ/(ℏc)>0，定义

\[
u_3=\frac8{441}q^2\frac{B_{M3}^{\max}}{B_{2\min}},\qquad
u_4=\frac5{23814}q^4\frac{B_{E4}^{\max}}{B_{2\min}},\qquad
u=u_3+u_4,\qquad\varepsilon\le\frac{u}{1+u}.
\]

因为 Γret≥C2 q⁵B2min、Γom≤C3 q⁷BM3max+C4 q⁹BE4max，此 ε 是全部被省 photon-rate 份额。按 [[rose-brink-1967-phase-defined-angular-distributions]] RB67-21/22，同一 bounded probability effect 的绝对误差≤√[u/(1+u)]；同有限 emitted subspace 的 angular-average-one W 绝对误差≤5√[u/(1+u)]。它不保证 refitted δ/ρ 的参数误差、节点相对误差、条件偏振比、total lifetime 或 nonγ channel。

B2min 缺失/趋零、orbital moment/domain 未控或 support-tail/current 修正未界定时，这条证明不能认证截断。固定有效先验下 q→0+ 是代数极限；q=0 没有归一发射态。由目标截断拟合倒推自身 E2 floor 或布居，不能充当独立 prior。72 项 parent 复现已通过；原先验 receipts 保持 immutable，独立审计另留证。此处没有实际 E/R/current/strength 输入或真实核截断结论，仍为 L2。

## Human Review Triage

### P0

- `LKH82-P0-1`: Before paper-level numerical reuse, return to the cited primary angular-correlation/polarization paper and the exact table footnote; the review's adopted value is a traceable index, not a replacement source.

## Extracted Pages

- Methods/observables: [[multipole-mixing-ratio]], [[angular-distribution]], [[angular-correlation]], [[linear-polarization-asymmetry]]。

- Day8 方法依赖回链：[[spin-parity-assignment]] 保存 spin/parity/multipolarity 的观测与共享输入审计；[[multipole-mixing-ratio]] 保存三例全候选及 convention 边界。
- 寿命/强度回链：[[high-spin-lifetime-strength-deformation]] 和 [[mukhopadhyay-2008-136nd-transition-rates]] 保存 rate-to-B 约定、分支完整性与同一实验数据依赖；没有增加独立实验重复。
