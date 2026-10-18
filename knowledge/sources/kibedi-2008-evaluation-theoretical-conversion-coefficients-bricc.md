---
type: source
title: "Evaluation of Theoretical Conversion Coefficients Using BrIcc"
aliases: [Kibedi 2008 BrIcc, BrIcc theoretical conversion coefficients, Kibedi 2008 ICC uncertainties]
created: 2026-07-12
updated: 2026-10-15
status: ai-draft
review_status: human-reviewed
source_type: method-review-article
reading_depth: read
title_original: "Evaluation of Theoretical Conversion Coefficients Using BrIcc"
authors: [T. Kibedi, T. W. Burrows, M. B. Trzhaskovskaya, P. M. Davidson, C. W. Nestor]
journal: Nuclear Instruments and Methods in Physics Research Section A
year: 2008
volume: 589
number: 2
pages: 202--229
doi: 10.1016/j.nima.2008.02.051
language: en
canonical_source: doi:10.1016/j.nima.2008.02.051
citation_key: kibedi_2008_Evaluationtheoretical
raw_file: "raw/papers/2008_Kibédi et al_Evaluation of theoretical conversion coefficients using BrIcc.pdf"
raw_sha256: 5A7B25491864ACD4D2FEA7A599136657DA336A03F902009B423C6C450926CC34
nuclei: []
reactions: []
models: []
observables: [internal-conversion-coefficient, multipole-mixing-ratio]
methods: [internal-conversion-analysis]
tags: [internal-conversion, bricc, uncertainty-propagation, mixing-ratio, ensdf]
---

# Kibedi et al. (2008): BrIcc Theoretical Conversion Coefficients

## Bibliographic Record

T. Kibedi et al., *Nuclear Instruments and Methods in Physics Research Section A* **589**(2), 202--229 (2008), DOI `10.1016/j.nima.2008.02.051`, citation key `kibedi_2008_Evaluationtheoretical`.

The BibTeX key matches uniquely by title, year and DOI. Local file size is `1111858` bytes; local timestamp `2025-03-05 09:51:26`; SHA-256 is recorded above.

## Scope and Reading Depth

The full 28-page article was read with targeted focus on the introduction, the ENSDF/ICC formalism in Secs.2--3, the mixing-ratio uncertainty treatment in Sec.3.4, the BrIccFO/BrIccNH discussion in Sec.4.1, and the interpolation/summary sections in Sec.5--6. Appendix tables were skimmed only as reference data tables rather than page-by-page evidence content.

This is a `review-ingest + theory-ingest` source. It should be used as a method/theory/database anchor for internal-conversion coefficients and their uncertainty handling, not as a primary experimental source for any single nucleus.

## Paper Question and Scientific Motivation

**Author-explicit.** The paper asks how accurate theoretical internal-conversion coefficients can be made accessible in an ENSDF-compatible evaluation tool while retaining the uncertainty and atomic-vacancy treatments needed for multipolarity and mixing-ratio work. The motivation is that experimental ICCs are compared with theory to determine transition multipolarities and mixing ratios, while modern calculations had reached percent-level accuracy that experiments could test (p.202, Abstract and Sec.1).

## Method and Design Logic

**Author-explicit.** The design follows the data-evaluation chain rather than a single-nucleus analysis: define the ENSDF transition inputs; give formulae for pure and mixed transitions; propagate theoretical-table, transition-energy and mixing-ratio uncertainties; compare vacancy treatments against compiled experimental ICCs; then package the adopted tables and interpolation rules in BrIcc (pp.202--207, Secs.1--4.1; pp.211--214, Secs.4.3--6).

## Key Evidence and Reasoning Chain

1. Experimental ICC use requires a theoretical coefficient for a specified `Z`, energy, shell and multipolarity (pp.202--203, Secs.1--3).
2. Mixed-transition ICCs depend on pure components and `delta^2`, so the coefficient cannot determine the sign of `delta` (p.203, Eqs.(1)--(5)).
3. The final uncertainty depends separately on the theoretical table, transition energy and mixing-ratio distribution; zero-crossing or limited `delta` cases are not captured by a single symmetric Gaussian error (pp.203--205, Secs.3.2--3.4, Fig.1).
4. Comparison with compiled experimental coefficients supports the Frozen-Orbitals vacancy treatment as the adopted default, while interpolation and nonunique multipolarity labels impose additional operational boundaries (pp.206--213, Secs.4.1--5.1).
5. Therefore BrIcc is useful as a controlled theory/database input to an ICC analysis, not as independent experimental evidence for a particular nuclear assignment (p.214, Summary; source boundary above).

## Analytical Reconstruction

The table separates source-grounded locators from Agent reconstruction. User review on 2026-07-15 accepted all rows without changing the existing source claims.

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-KB08-1 | Core reconstruction | Treat ICC inference as a forward-model problem: declare candidate multipolarities and the adopted atomic calculation, propagate all input uncertainties through `alpha(delta)`, and only then invert or compare with experiment. This is an Agent reconstruction, not a sentence quoted from the authors. | Eqs.(1)--(5), Secs.3.2--3.4; vacancy and interpolation tests in Secs.4.1 and 5.1 | human-reviewed |
| AR-KB08-2 | Transfer conditions | Transfer is justified only when transition energy, `Z`, shell/total coefficient convention, candidate multipolarities, `delta` convention and uncertainty model are explicit and the selected BrIcc table covers the case. | pp.203--205, Secs.3--3.4; pp.206--213, Secs.4.1 and 5.1 | human-reviewed |
| AR-KB08-3 | Failure conditions | Do not transfer silently for nonunique multipolarity input, an unmodelled third component/E0 admixture, direct interpolation of nonmonotonic total ICC, or a `delta` distribution crossing zero without adequate likelihood treatment. | p.203, Sec.2; pp.204--205, Sec.3.4 and Fig.1; p.211, Sec.4.3 | human-reviewed |
| AR-KB08-4 | Reverse/falsification test | Compare an inferred `delta` against independent angular-distribution/polarization constraints or repeat the forward calculation with the relevant vacancy/table choice; disagreement can localize whether the conflict is experimental, atomic-model or multipolarity-input dependent. | Forward relations in p.203, Eqs.(1)--(5); vacancy comparison in pp.206--207, Sec.4.1.1 | human-reviewed |
| AR-KB08-5 | Research-question decision | Not created: the reviewed reconstruction did not produce an independent research question beyond the stated ICC inference and reverse-test boundaries; no question is added merely to fill the framework. | Assessment of the complete reconstruction above; no additional source claim | human-reviewed |
| AR-KB08-6 | Persistence/shared-page decision | No research note or project/synthesis update. The transferable content is source-grounded and already owned by [[internal-conversion-analysis]]; no new cross-source hypothesis or evidence-state change would be lost. | Existing source claims KB08-1--8 and linked method ownership | human-reviewed |

## Summary

Kibedi et al. present BrIcc, a database and software layer for theoretical internal-conversion coefficients (ICC), electron-positron pair conversion coefficients, and `E0` electronic factors. The paper formalizes how mixed-multipolarity ICCs are calculated from pure components, how ENSDF-style uncertainties in transition energy and mixing ratio propagate into the quoted ICC uncertainty, and why the treatment of atomic vacancies matters for theoretical accuracy.

For the current Wiki, its two most reusable contributions are: the mixed-transition relation `alpha = (alpha_1 + delta^2 alpha_2)/(1+delta^2)` with explicit uncertainty propagation rules, and the database-level boundary that interpolation, vacancy treatment, and nonunique multipolarity labels can affect whether an ICC-based `delta` extraction is trustworthy.

## Experimental or Theoretical Setup

- BrIcc is designed as an ENSDF-compatible evaluation tool, not as one nucleus one experiment paper.
- Inputs include atomic number `Z`, transition energy, multipolarity field, mixing ratio `delta` and their uncertainties/limits.
- Data sources include BrIccFO/BrIccNH ICC tables, pair-conversion tables, and `E0` electronic-factor tables.
- The paper compares alternative vacancy treatments using a large compiled experimental ICC set.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KB08-1 | BrIcc 被设计为 internal-conversion / pair-conversion / `E0` electronic-factor database 与软件工具，其 mixed-transition、mixing-ratio 与 uncertainty 处理遵循 ENSDF 规则。 | method-formalism | direct | p.202, Abstract; pp.202--203, Secs.1--2 | false |
| KB08-2 | 对 mixed `(pi L + pi' L')` transitions，ICC 使用 `alpha = [alpha(pi L) + delta^2 alpha(pi' L')] / (1 + delta^2)`；conversion coefficient 对 `delta` 的符号不敏感，只依赖 `delta^2`。 | method-formalism | direct | p.203, Sec.3, Eqs.(1)--(5) | false |
| KB08-3 | BrIcc 把 ICC 不确定度拆成理论表本身、跃迁能量和 mixing ratio 三部分；Sec.3.4 还给出了 symmetric/asymmetric `delta`、上下限 `delta` 以及特殊 multipolarity 情况的传播规则。 | method-formalism | direct | pp.204--205, Secs.3.4--3.5, Eqs.(17)--(22) | false |
| KB08-4 | 当 `delta` 及其不确定度跨过零时，由 ICC 反映出的有效 `P(delta)` 不再能简单表述为带非对称误差的 normal distribution；作者明确说一般化统一处理仍需后续工作。 | method-boundary | direct | p.205, Sec.3.4.3, Fig.1 | false |
| KB08-5 | 重新分析实验 ICC 数据后，作者认为考虑 atomic vacancy 的模型更受支持；NSDD 在 2005 年采用了 `Frozen Orbitals` 近似作为默认 BrIcc 表，而不是继续使用 `No Hole` 近似。 | author-interpretation | direct | pp.206--207, Sec.4.1.1 | false |
| KB08-6 | BrIccFO/BrIccNH 的默认理论表覆盖 `Z=5--110`、`1--6000 keV`、所有壳层，并采用 `1.4%` 的理论表精度；作者还给出 BrIccFO/BrIccNH 插值精度约 `0.3%` 的上限。 | observed-fact | direct | p.206, Table 2; pp.212--213, Sec.5.1; p.214, Summary | false |
| KB08-7 | 文章明确提醒 total ICC `alpha_T` 不是 transition energy 的单调函数，因此一般不推荐对已 tabulated 的 `alpha_T` 直接做插值。 | method-boundary | direct | p.211, Sec.4.3 opening paragraph | false |
| KB08-8 | 若 multipolarity 只给出非唯一标签如 `D/Q/O` 等，BrIcc 不计算 conversion coefficient；若没有给出 `delta` 而 multipolarity 仍有效但不唯一，则会按特定规则给出平均化处理。 | method-boundary | direct | p.203, Sec.2; p.205, Sec.3.4.3 | false |

## Nuclear Structure Information

This source is not a nucleus-specific structure paper. The many listed nuclei or transitions are database, interpolation, or validation examples only.

## Authors' Interpretation

- BrIcc is presented as a practical evaluation tool for nuclear-structure work and data sheets.
- The authors argue that uncertainty propagation in `delta` and transition energy should be part of routine ICC evaluation rather than ignored.
- Their preferred default is BrIccFO, not because BrIccNH is unusable, but because FO gave the more consistent agreement pattern in the reevaluated experimental set.

## Model Results

- The paper compares vacancy treatments (`No Hole`, `Self-Consistent`, `Frozen Orbitals`) against an experimental ICC database.
- It quantifies adopted average experiment-theory differences and reduced chi-squared values for those approximations.
- It characterizes interpolation accuracy and the table coverage needed for a database implementation.

## Competing Interpretations and Limitations

- This paper is a theory/database review; it does not by itself validate ICC extraction in every modern experiment.
- The source explicitly leaves some special uncertainty cases and three-component multipolarities for future work.
- BrIcc values still depend on the adopted atomic-vacancy treatment and on the integrity of the multipolarity/mixing-ratio inputs.
- It should not be used to rewrite model-calculated ICCs as experimental observables.

## Extracted Pages

- Nuclei:
- Bands:
- Concepts:
- Methods: [[internal-conversion-analysis]]
- Observables: [[internal-conversion-coefficient]], [[multipole-mixing-ratio]]
- Projects: [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]

## Personal Notes

Navigation only: use this source with [[rezynkina-2017-graphical-extraction-multipole-mixing-ratios]] and [[internal-conversion-analysis]] for future ICC/mixing-ratio work. Scientific reconstruction is owned by the table above; no additional provisional reasoning is stored here.

## 2026-10-07 Supplement — Codex self-audit, needs_review

本附录为2026-10-07的新学习/查询，**未经人工审核**。原page `review_status`、KB08-1–8的false标记和AR-KB08-1–6的human-reviewed记录原样保留；它们对应2026-07-15历史审核，不能延伸覆盖本附录。以下新claim均needs_review=true。

### 新阅读覆盖与直接来源定位

本次读Sections1–6的问题、ENSDF/ICC、误差、FO/NH、数值/物理边界、插值、实现和Summary；读Appendix A接口、按用途浏览Appendix B，定向核Z60 row（printed221 / PDF20）。原图核p203/PDF2 Eqs.(1)–(5)、p206/PDF5 Table2/脚注、p207/PDF6 FO/NH和Eq.(24)、p213/PDF12 interpolation。未宣称逐行重读全Appendix；raw SHA与原记录一致。

- p206/PDF5 Table2脚注的1.4% **已包括插值贡献**；p213/PDF12的约0.3%是插值精度界，不能再独立quadrature加入。原KB08-6的总体覆盖摘要须连同各subshell边界使用。
- p208/PDF7 Sec.4.1.4：Z59–75的N6在约400keV有数值截断；作者说被省的高能外壳贡献typically less than10⁻⁹，这不是对某一具体缺项点的严格upper bound。
- p221/PDF20 TableB.1列60-Nd-144默认mass/radius与K binding43.5689keV；用于Mu08的136Nd时，Z相同不等于已对A136作新的finite-size计算。当前web未暴露逐点radius/datafile hash，不按A幂改α。
- p208/PDF7的surface-current/penetration、neutral free atom与chemical/ionization条件保留。BrIcc理论不增加独立核谱实验，也不给δ sign。

### 五个独立理论查询点

官方入口 https://bricc.anu.edu.au/ ，检索日期2026-10-07，实际返回 **BrIccS v2.3 (9-Dec-2011) / BrIccFO**。输入Z60、给定E和pure M1/E2；未向server提交寿命、branch或B。标记沿Mu08提取假设：ΔI1 pure M1是作者假设，ΔI2沿其E2赋值；没有新measured δ。五个点共6次POST（初始All空响应、授权FO-only同点control、其余4点）。NH数值没有查得。

| Eγ (keV), pure hypothesis | Program-reported Tot α | αK | Returned coverage |
|---|---|---|---|
| 401.2 M1 | 0.0320(5) | 0.0274(4) | N6 missing; warning retained |
| 389.6 M1 | 0.0345(5) | 0.0295(5) | no returned-table warning |
| 757.4 E2 | 0.00416(6) | 0.00351(5) | N6 missing; warning retained |
| 199.6 M1 | 0.204(3) | 0.1739(25) | no returned-table warning |
| 382.0 E2 | 0.0251(4) | 0.0204(3) | no returned-table warning |

括号是NDSh尾位误差，α无量纲；Tot与K不同。401.2与757.4两点的warning均为 `ICC could not be calculated for EG above 398.000 keV`，N6为空，未补零或外推。其它三点只表示返回表无coverage warning；不能据此保证实际原子/实验decay inventory完全闭合。主要壳层之和在打印Tot误差内；保留原Tot，避免重舍入或对Total作手工插值。

下面保存本次实际返回的所有subshell与major sums，shell行M1/M2/M3表示电子壳层，表头M1/E2表示核γ的假设多极性，二者分开。所有数据都是该FO模型lookup，不是Mu08测得的conversion coefficients。

| Subshell / major sum | 401.2 M1 | 389.6 M1 | 757.4 E2 | 199.6 M1 | 382.0 E2 |
|---|---|---|---|---|---|
| Tot | 0.0320(5) | 0.0345(5) | 0.00416(6) | 0.204(3) | 0.0251(4) |
| K | 0.0274(4) | 0.0295(5) | 0.00351(5) | 0.1739(25) | 0.0204(3) |
| L1 | 0.00344(5) | 0.00371(6) | 0.000419(6) | 0.0221(3) | 0.00232(4) |
| L2 | 0.000203(3) | 0.000221(3) | 5.76E-5(8) | 0.001554(22) | 0.000831(12) |
| L3 | 4.02E-5(6) | 4.36E-5(7) | 3.26E-5(5) | 0.000301(5) | 0.000570(8) |
| L-tot | 0.00368(6) | 0.00398(6) | 0.000509(8) | 0.0239(4) | 0.00372(6) |
| M1 | 0.000723(11) | 0.000780(11) | 8.75E-5(13) | 0.00464(7) | 0.000482(7) |
| M2 | 4.68E-5(7) | 5.09E-5(8) | 1.331E-5(19) | 0.000357(5) | 0.000191(3) |
| M3 | 9.37E-6(14) | 1.018E-5(15) | 7.66E-6(11) | 6.97E-5(10) | 0.0001339(19) |
| M4 | 7.61E-8(11) | 8.51E-8(12) | 3.01E-8(5) | 1.100E-6(16) | 6.97E-7(10) |
| M5 | 7.75E-8(11) | 8.56E-8(12) | 2.99E-8(5) | 9.13E-7(13) | 6.16E-7(9) |
| M-tot | 0.000779(11) | 0.000841(12) | 0.0001085(16) | 0.00507(7) | 0.000809(12) |
| N1 | 0.0001624(23) | 0.0001752(25) | 1.96E-5(3) | 0.001043(15) | 0.0001080(16) |
| N2 | 1.010E-5(15) | 1.099E-5(16) | 2.87E-6(4) | 7.70E-5(11) | 4.13E-5(6) |
| N3 | 2.02E-6(3) | 2.19E-6(3) | 1.655E-6(24) | 1.501E-5(21) | 2.89E-5(4) |
| N4 | 1.610E-8(23) | 1.80E-8(3) | 6.38E-9(9) | 2.32E-7(4) | 1.473E-7(21) |
| N5 | 1.620E-8(23) | 1.79E-8(3) | 6.26E-9(9) | 1.90E-7(3) | 1.286E-7(18) |
| N6 | 未返回（coverage warning） | 5.46E-12(8) | 未返回（coverage warning） | 1.278E-10(18) | 4.14E-11(6) |
| N-tot | 0.0001745(25) | 0.000188(3) | 2.42E-5(4) | 0.001135(16) | 0.0001785(25) |
| O1 | 2.50E-5(4) | 2.70E-5(4) | 3.02E-6(5) | 0.0001607(23) | 1.663E-5(24) |
| O2 | 1.323E-6(19) | 1.440E-6(21) | 3.77E-7(6) | 1.009E-5(15) | 5.41E-6(8) |
| O3 | 2.47E-7(4) | 2.68E-7(4) | 2.02E-7(3) | 1.83E-6(3) | 3.53E-6(5) |
| O-tot | 2.66E-5(4) | 2.87E-5(4) | 3.60E-6(5) | 0.0001726(25) | 2.56E-5(4) |
| P1 | 1.748E-6(25) | 1.89E-6(3) | 2.11E-7(3) | 1.122E-5(16) | 1.161E-6(17) |
| P-tot | 1.748E-6(25) | 1.89E-6(3) | 2.11E-7(3) | 1.122E-5(16) | 1.161E-6(17) |

各响应的URL、physics参数、返回版本、原始HTML SHA与warning记录在对应查询回执；在此按能量定位原始响应：

- 401.2 M1：response SHA256 `2a4ef98e8af1d30d54a0a3662d8857ba04d41a5b6d64f5a8aa5bf2a66abf4b4f`。
- 389.6 M1：response SHA256 `341496d6b99cb792d653ab9ee028b4b5fbeee5723c75ce319d40e54fb5b1ff50`。
- 757.4 E2：response SHA256 `d39a0ef24a2865ade42d17a79bd3f73cb191a0b166481c92b09f6485d3f9a7cf`。
- 199.6 M1：response SHA256 `1930f8c41229d9f26b695a2e71659d3a5935eb549ddd23733d08cceef5046659`。
- 382.0 E2：response SHA256 `fa6dc37e4fd21a935a7beb5d1aeaebfe2285460958bc4592a63f634f220284ae`。

官方Linux binary只作help/provenance probe，实报v2.3d(13-Sep-2022)，未作本地ICC计算；本地BrIccFOV22/NHV22 .idx/.icc缺失，与实际web2011 backend分开。NNDC旧入口404、IAEA分发403、All空响应均为保存的失败。HTTP200/参数echo本身不是numerical lookup成功。没有修改global环境、raw或凭据。

### Branch-definition 的条件forward检验

从p203/PDF2 Eq.(3) `α=Tic/Tγ`和rate inventory推出：若g_i是完整相对photon fraction，`Dg=Σ g_j(1+α_j)`、`τTγ,i=g_i/Dg`；若β_i是total-decay fraction，`τTγ,i=β_i/(1+α_i)`。这些简式额外假定所列branches齐全、无未计extra decays。以相同Mu08印出数字分别作为g或β、使用上述FO报告Tot，得到：

| Parent / branch | Dg | Photon-formula / total-formula − 1 |
|---|---|---|
| B1-I18 / 401p2 | 1.0257934 | +0.605% |
| B1-I18 / 757p4 | 1.0257934 | -2.109% |
| B1-I18 / 389p6 | 1.0257934 | +0.849% |
| B2-I15 / 199p6 | 1.191477 | +1.051% |
| B2-I15 / 382p0 | 1.191477 | -13.964% |

约−13.964%的B2 382-keV分支差异是nominal forward sensitivity，没有选择Mu08实际branch convention或用哪个结果接近quoted B来倒解α/δ/ρ。B1含两条N6警告input，是带覆盖边界的比较。各α共用理论/表来源；无energy uncertainty、NH spread、atomic/radius correction、shared covariance或完整feeding/stopping预算，不能生成完整B confidence interval。Raw实验inputs与单位链分别见[[mukhopadhyay-2008-136nd-transition-rates]]和[[high-spin-lifetime-strength-deformation]]；未进行L4或mode ranking。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KB08-D8-1 | 1.4%已包括interpolation contribution；约0.3% interpolation accuracy不能再次独立叠加。默认table全局覆盖须保留N6等subshell例外及atomic/radius条件。 | our-inference | indirect | printed206 / PDF5 Table2 footnote; printed208 / PDF7 Sec.4.1.4; printed213 / PDF12 Sec.5.1; printed221 / PDF20 TableB.1 | true |
| KB08-D8-2 | 2026-10-07官方FO查询的五个program Tot/K记录及两点N6缺项是独立理论输入；保留实际web v2.3(2011)、未用local v2.3d(2022)、data hash与质量边界，不作为实验ICC或Mu08所用处理的证据。 | model-result | direct | official https://bricc.anu.edu.au/ five Z60/E/pure-multipole response hashes in Supplement table; theory context printed206–208 / PDF5–7 | true |
| KB08-D8-3 | 相同branch numbers作为photon或total fractions时，五条pure-mode forward γ-rate可不同；B2 382-keV差约−13.964%只度量条件敏感性，不识别作者实际定义或机制。 | our-inference | indirect | premises printed203 / PDF2 Eq.(3); Mu08 printed034311-3/PDF3 TableI B1I18/B2I15; Supplement forward table | true |
| KB08-D8-4 | HsIcc/RpIcc 的 NP 与新的 DF/SC 已近似含 penetration 是不同 reference models；FO/NH vacancy 与 NP/SC 核流选择分别记录。将现代 DF/FO 自动作 NP 基线再乘 Hager 修正可能重复计入；没有改变本附录五个 FO inputs 或旧人审行。 | reference-model-boundary | direct | printed pp.207–208 / PDF pp.6–7 Sec.4.1.1–4.1.2、Eq.24 及 p.208 左栏开头 | true |
| KB08-D8-5 | 原五能量各一次官方NH查询认证了actual BrIccNH/v2.3(2011)输入；打印Tot下FO/NH的nominal强度敏感性很小但有舍入/coverage界。共5POST/0重试/0新FO查询，spread不是独立1σ或实验，未识别MU08实际处理。 | model-result-and-our-inference | indirect | official https://bricc.anu.edu.au/五NH response hashes及本附录表；p207/PDF6 Sec4.1.1、p206/PDF5 Table2 footnote、p208/PDF7 N6条件；MU08 TableI/II | true |

### FO/NH vacancy 的有界敏感性（2026-10-07 self-audit）

本轮唯一 Day9 无学分预习对相同五个 Z60 energy/mode 各作一次 official ANU NH 查询：程序实际返回 `Data Sets: BrIccNH`、`BrIccS v2.3 (9-Dec-2011)` 与所选 Z/E/mode 列，非仅参数 echo。5 次 POST、0 retry、0新FO请求。已存精确response压缩档/hash并由主代理离线 replay，0新增网络请求。原 FO 五点及其receipt保持不变。

| Eγ/题设mode | FO Tot α | NH Tot α | FO K α | NH K α | NH response SHA256 |
|---|---|---|---|---|---|
| 401.2 keV M1 | .0320(5) | .0320(5) | .0274(4) | .0274(4) | `1f5a09ae24c4661b0208a63e9054e9fcb0d767a1ad490e39a38725665ea07121` |
| 389.6 keV M1 | .0345(5) | .0345(5) | .0295(5) | .0295(5) | `435980f6c2ab13dea11c0994695d28df88c1c6cf20b8c906f40cfd10f0c97c04` |
| 757.4 keV E2 | .00416(6) | .00416(6) | .00351(5) | .00351(5) | `d4697b0465608cc9d659ec7e6f179acc49adb9fc58c03b04e9596802072c9503` |
| 199.6 keV M1 | .204(3) | .204(3) | .1739(25) | .1736(25) | `4b12470e0c293118d3de71e416a5bb89fc51024c23a588996bacaf2cc4be083f` |
| 382.0 keV E2 | .0251(4) | .0250(4) | .0204(3) | .0203(3) | `6b3da9d0e7006465278e9a3b639f3a6224895e5e50c398793a5f873983da11a9` |

401.2与757.4的NH仍有N6 blank/above398-keV警告，未补零；报出的Tot与rounded-shell sums分开，不能冒称严格all-shell闭合。B1三个分支的Dg两model均1.0257934；B2 Dg,FO=1.191477、Dg,NH=1.191470。分别以原数字作photon g或total β，固定E/mode/τ时的rate/B敏感性为：B1均0（打印精度）；B2 photon两支共同 NH/FO−1≈+0.000588%；total β时199.6支0、382.0支≈+0.009756%。K系数199.6、382.0的中心差约−0.173%、−0.490%，不把K差直接作total-rate差。

计算多位小数只表示rounded input的算术精度，0不证明未舍入理论值相等。FO/NH共享atomic方法，spread是确定性模型敏感性，不能作为独立1σ或与已含interp的1.4%随意叠加。未取得逐点data-file/radius hash或136Nd专属finite-size重算，未从作者quoted B识别vacancy、branch convention或penetration。Source p207的vacancy说明与本附录NP/SC区别共同使用；没有实验/机制排序或Day9学分改变。

### Penetration reference 与 vacancy 的区分（2026-10-07 self-audit）

p.207 Eq.24 分开电子系数与核 penetration 参数，p.208 左栏明确 HsIcc/RpIcc 使用 Rose 的 no-penetration（NP），新的 DF 则使用近似纳入 penetration 的 Sliv surface-current（SC）。核结构修正必须针对相容的 reference model；不能将本附录的 modern DF/FO 数值未经映射直接再乘 NP 修正式。FO/NH 描述电子空穴处理，不是 NP/SC 的同义词；No Hole 不表示零 penetration。Source 的100-keV M1、Z50–120量级例不迁移成本次 Z60/五能量的逐点界。

[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-12 保存其 p.169 明示修正式、作者增强叙述与未知允许域的条件性 E0 下界。固定 photon mixing 下的标量 α 对 δ sign 不敏感，不等于 penetration 参数没有线性符号敏感性。此新增解释没有核素修正 fit 或新 coefficients，旧 review_status、KB08-1–8 与原 AR 人审记录保留；KB08-D8-4 属本次自审，needs_review=true。

### 新附录E0 electronic-factor locator（self-audit, needs_review）

printed204 / PDF3 Sec3.1 Eqs6–7/11给ρ无量纲、Ω单位s⁻¹及T_s(E0)=ρ²Ω_s，并允许将K-shell式按Ω推广到其它shell。E0与singleγ不同，same-spin/parity方可使用；electron ΣΩ与pair Ω分别盘点。本日合成四γ+E0补全在[[lange-kumar-hamilton-1982-multipole-admixtures]]的LKH82-7，不把本页Mu08/FO lookup数字转给synthetic，也不改原人审状态。

### NH subshell记录（同次查询，不补缺项）

以下是provider原打印α/uncertainty，与Tot分开，不由rounded sums覆盖Tot。N6空白保留为缺项；每点均为BrIccNH/v2.3(2011)、Z60，source定位p207 vacancy与上述exactresponsehash。

| Shell | 401.2 M1 | 389.6 M1 | 757.4 E2 | 199.6 M1 | 382.0 E2 |
|---|---|---|---|---|---|
| Tot | 0.0320 (5) | 0.0345 (5) | 0.00416 (6) | 0.204 (3) | 0.0250 (4) |
| K | 0.0274 (4) | 0.0295 (5) | 0.00351 (5) | 0.1736 (25) | 0.0203 (3) |
| L1 | 0.00344 (5) | 0.00371 (6) | 0.000419 (6) | 0.0220 (3) | 0.00232 (4) |
| L2 | 0.000203 (3) | 0.000221 (3) | 5.76E-5 (8) | 0.001554 (22) | 0.000831 (12) |
| L3 | 4.03E-5 (6) | 4.37E-5 (7) | 3.26E-5 (5) | 0.000302 (5) | 0.000570 (8) |
| L-tot | 0.00368 (6) | 0.00398 (6) | 0.000509 (8) | 0.0239 (4) | 0.00372 (6) |
| M1 | 0.000723 (11) | 0.000780 (11) | 8.75E-5 (13) | 0.00464 (7) | 0.000482 (7) |
| M2 | 4.68E-5 (7) | 5.09E-5 (8) | 1.331E-5 (19) | 0.000357 (5) | 0.000191 (3) |
| M3 | 9.38E-6 (14) | 1.018E-5 (15) | 7.67E-6 (11) | 6.98E-5 (10) | 0.0001339 (19) |
| M4 | 7.62E-8 (11) | 8.52E-8 (12) | 3.01E-8 (5) | 1.101E-6 (16) | 6.97E-7 (10) |
| M5 | 7.76E-8 (11) | 8.58E-8 (12) | 3.00E-8 (5) | 9.15E-7 (13) | 6.17E-7 (9) |
| M-tot | 0.000779 (11) | 0.000841 (12) | 0.0001085 (16) | 0.00507 (7) | 0.000808 (12) |
| N1 | 0.0001624 (23) | 0.0001752 (25) | 1.96E-5 (3) | 0.001043 (15) | 0.0001080 (16) |
| N2 | 1.010E-5 (15) | 1.100E-5 (16) | 2.87E-6 (4) | 7.70E-5 (11) | 4.13E-5 (6) |
| N3 | 2.02E-6 (3) | 2.19E-6 (3) | 1.656E-6 (24) | 1.502E-5 (21) | 2.89E-5 (4) |
| N4 | 1.611E-8 (23) | 1.80E-8 (3) | 6.38E-9 (9) | 2.32E-7 (4) | 1.473E-7 (21) |
| N5 | 1.621E-8 (23) | 1.79E-8 (3) | 6.27E-9 (9) | 1.90E-7 (3) | 1.286E-7 (18) |
| N6 | missing / warning | 5.46E-12 (8) | missing / warning | 1.278E-10 (18) | 4.14E-11 (6) |
| N-tot | 0.0001745 (25) | 0.000188 (3) | 2.42E-5 (4) | 0.001135 (16) | 0.0001785 (25) |
| O1 | 2.50E-5 (4) | 2.70E-5 (4) | 3.02E-6 (5) | 0.0001607 (23) | 1.663E-5 (24) |
| O2 | 1.323E-6 (19) | 1.440E-6 (21) | 3.77E-7 (6) | 1.009E-5 (15) | 5.41E-6 (8) |
| O3 | 2.47E-7 (4) | 2.68E-7 (4) | 2.02E-7 (3) | 1.83E-6 (3) | 3.53E-6 (5) |
| O-tot | 2.66E-5 (4) | 2.87E-5 (4) | 3.60E-6 (5) | 0.0001726 (25) | 2.56E-5 (4) |
| P1 | 1.748E-6 (25) | 1.89E-6 (3) | 2.11E-7 (3) | 1.122E-5 (16) | 1.161E-6 (17) |
| P-tot | 1.748E-6 (25) | 1.89E-6 (3) | 2.11E-7 (3) | 1.122E-5 (16) | 1.161E-6 (17) |


## 2026-10-15 Supplement — Z31实际理论输入与67Ga ledger

本项是Day14的同一source-field/strength问题的必要companion，Day15仅无学分预习。使用既有已读KB08方法与official[ANU BrIcc](https://bricc.anu.edu.au/)，先冻结primed回忆。未提交τ、RI或B以倒推ICC；只提交Z31、E/DE、puremode、BrIccFO和subshells。原paper人审metadata及所有旧claim flags保持，新D14-1–6全needs_review:true，没有新人审。

### 查询输入、版本与失败控制

初4POST将能量error当绝对小数.4/.05，收到HTTP200校验页“Energy uncertainty invalid”，没有数字。校对ENSDF格式后将DE分别置4/5；168.8(4)对应.4keV，958.01(5)对应.05keV。手册II.A的E12.4/DE+1-2→+.1−.2keV例保留，网站literal(+4−4)/(+5−5)输出不改写。4个failed+4个corrected请求完整留存，未无界重试或将empty data填0。

实际服务实报BrIccS v2.3(9-Dec-2011)、DataSets BrIccFO、Z31/Ga，区别本地2022help probe；页面Updated2026是网页日期，不升级physics backend。所有quoted errors是provider打印uncertainty，不制造jointCov或其频率含义。

| Eγ(keV) / 核假设mode | program Tot α | K α | response SHA256 |
| --- | --- | --- | --- |
| 168.8 / M1 | 0.0175(3) | 0.01559(24) | c959b9e7b345b2eb7369d5494fa92a574e0b366e0665c7eaf40172fd9d28e2ad |
| 168.8 / E2 | 0.0976(17) | 0.0864(15) | 596bd2cfff3787d46d566a58233afb28ce116082a398402995a5b212413f2e2e |
| 958.01 / E2 | 0.000358(5) | 0.000320(5) | e757679416fd9a55db9bf884abcb7ac974ef2006819fc952deef29c34d028004 |
| 958.01 / M3 | 0.001513(22) | 0.001350(19) | 5cebaacd93d0c94868a69a22876f079074679d79eec097c8e5e977e8eb600f2d |

每点全部subshells、major sums与打印精度在本run bricc67-parsed-forward/offline-replay.json保存。Tot从program取，不用rounded-shells sums覆盖；electron-shell M1/M2/M3与核M1/E2/M3分开，K不作all-shell。168.8E2的energyunc贡献>1%警告保留；既有KB08-D8-1的1.4%含interp原则继续用，不另加一次.3%。Energy与derivedα误差共用输入，后续B误差须保留chain/cov，不能假装全独立重复energyerror。

未取得逐点datafile/radius hash，未验证A67专属finite-size或实际离子态；Z相同不证明此是67Ga重新计算。FO/NH与NP/SC不同，未额外乘penetration修正或声称覆盖所有weakline允许higher ranks。

### 32-check条件forward与未闭合边界

[[nndc-2005-67ga-selected-level-gamma-records]] N67-2/4/5/6提供parentT1/2、E/RI、finiteMR及评价B。Source原空白CC保持；四个lookup另列theoryinputs。以KB08-2公式alpha_eff,strong=(alpha_E2+δ²alpha_M3)/(1+δ²)连接电磁rateledger。假设只有958与168两γ、无extra、weak仅M1/E2、δs0：两端给B_E2 9.614759/9.613223WU，较zeroIC9.618530分别−.039206%/−.055179%。若weak在M1/E2间混合，同一FO模型的αw是两endpoint凸组合，条件中心值在这一区间；不是未知全部multipolarity或真实decay的全局界。

另选δs=.01/.02仅作sensitivitypoints（不是quotederror的hardCI）；6个modelcases保存了totalbranch/photonprobability/rate闭合。变化小于parentquotedlifetime约9%不认证NDS2005算法，亦不修复raw RI gate/eff/angle、未观测branches/高阶/penetration或actualCov。没有把theory lookup计独立实验或清除N67 missingICC。

即使只见weakphoton RI.2对100，也不能称weakreducedstrength：若**额外假设两条均pureE2**且photon intensities恰当，same-parent Bweak/Bstrong=r(Estrong/Eweak)^5=11.776548；τ/共同ledger可消掉，但weakM未测，该数不是实测Bweak或E2赋值。

复算[day14_bricc67_forward.py](../../system/scripts/day14_bricc67_forward.py)，offline32checks与capturedresponse32checks数值一致。Canonical rate/库存/量义在[[level-scheme-reconstruction]]“67Ga：FO理论输入补全的条件强度范围”。本run未做真实谱/event fit，L4 not-ready。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| KB08-D14-1 | official ANU BrIccFO/v2.3(2011)、Z31、E168.8、M1、DE4 query给Tot=.0175(3)、K=.01559(24)。是默认table/theory，不是67Ga measuredICC。 | model-result | direct | 2026-10-15 ANU response c959b9e7b345b2eb7369d5494fa92a574e0b366e0665c7eaf40172fd9d28e2ad / Tot,K | true |
| KB08-D14-2 | 同Z/E的pureE2、DE4给Tot=.0976(17)、K=.0864(15)，并明确energyuncertainty对ICC误差贡献>1%。 | model-result | direct | 2026-10-15 ANU response 596bd2cfff3787d46d566a58233afb28ce116082a398402995a5b212413f2e2e / Tot,K,warning | true |
| KB08-D14-3 | Z31、E958.01、E2、DE5给Tot=.000358(5)、K=.000320(5)。Quotederrors/actualversion保留，不指认2005evaluator所用程序。 | model-result | direct | 2026-10-15 ANU response e757679416fd9a55db9bf884abcb7ac974ef2006819fc952deef29c34d028004 / Tot,K | true |
| KB08-D14-4 | Z31、E958.01、M3、DE5给Tot=.001513(22)、K=.001350(19)，用于声明E2/M3 truncation下的forward input。 | model-result | direct | 2026-10-15 ANU response 5cebaacd93d0c94868a69a22876f079074679d79eec097c8e5e977e8eb600f2d / Tot,K | true |
| KB08-D14-5 | 初4请求DE=.4/.05小数遭Energy uncertainty invalid，HTTP200无numeric；改ENSDF末位4/5后4点成功，原失败响应保留。源手册12.4、DE+1-2例解为+.1−.2keV；web(+4−4)/(+5−5)回显不改写。 | interface-validation-and-boundary | direct | Day14 invalid/corrected request receipts；manualII.A E/DE example | true |
| KB08-D14-6 | actualFO4inputs用于67Ga complete2γ/weakM1-orE2/δ0控制，给B_E2=9.614759/9.613223WU，比zeroIC下降.0392%/.0552%。这是32-check任务forward，不是新strength测量/完整物理ceiling；highermultipoles、extra/cov仍缺。 | our-inference | indirect | Day14 four-input table / conditional forward ledger；paperp203 Eq.3与N67-4/5 | true |


## 2026-10-17 Supplement — 明确壳层的164Yb参考与E0使用门

本节为Day15正式完成后的**Day16无学分预习**，新增内容仅Codex self-audit，未经人工审核。原page review、KB08-1–8、AR-KB08及之前D8/其它增补逐字与flags保留，不扩展历史human review。先冻结已见旧Wiki的primed回忆，再核原PDF SHA-256 `5a7b25491864acd4d2fea7a599136657da336a03f902009b423c6c450926cc34`；完整读主线printed202–214/Secs1–6，AppendixA接口printed215，并定向核AppendixB Z70行printed222及末页228脚注，不声称逐行复审其余Appendix数据。视觉核Fig1–7、Table1–3、Eq3/5/7/11、Table2注、Z70行。旧理论说明只作为校准入口，不重复算旧Z60 query或旧check数。

### 原件适用条件与新的两次官方查询

原Sec3.1/printed204允许同Jπ E0，无single-gamma E0，pair emission须超过1022keV；489.8keV此线不能产生E0 pair。Eq7的Omega为s^-1而rho²无量纲；Eq11把E0 electron rate加到M1/E2 K电子/γ比。Sec4.4/printed212–213明确E0电子因子数据不完整且不采用统一Datheor；不能照搬ICC表的1.4%。Table2的1.4%已含interpolation贡献，原有D8边界不变。

TableB.1 printed222的Z70为`70-Yb-173`、K binding61.3323keV；superscript b仅指closed atomic shells（printed228脚注），不是为A164重算的标记。当前web只接受Z、不显示底层mass/datafile hash；本次没有改A/radius或作按A幂修正。默认A173与目标A164的有限尺寸差异保留，而非给一个记忆中的修正百分比。

2026-10-17在官方[ANU BrIcc](https://bricc.anu.edu.au/)只执行**2次POST、0retry**，pureM1与pureE2，Z70/E489.8、FO-only，实际返回BrIccS v2.3 (9-Dec-2011)/BrIccFO及对应列。输入v2仅nominal energy，未发送实验.1keV误差；v1在任何POST前supersede，保留版本和原因。Table2/AppendixA核NDS规则，但不事后把未送字段写成已传播。HTTP200/echo以外，所有数值行、shell/uncertainty与warnings均已离线验证。

| hypothesis | 程序报告Tot alpha | K alpha | L-tot alpha | 原HTTP HTML SHA-256 |
| --- | --- | --- | --- | --- |
| pureM1 | .0432(6) | .0363(5) | .00536(8) | `0f74bd9078a77504e3c65e12eff2084533c18db876d2000a03ec6e8d05c7e26d` |
| pureE2 | .0188(3) | .01475(21) | .00314(5) | `bde3a2eefe5d1f813df58cbbc0273ad0458fce09e462eef0a23e8c682221450d` |

两表N6/N7均空白，各有两条`ICC could not be calculated for EG above 398.000 keV`。缺项未补0；程序仍返回的Tot按“program-reported with coverage warning”保存，**不认证完整total**。K壳条目有值、electron kinetic energy428.47keV，与2008K binding的名义差428.4677相符。主要shell sum在打印Tot误差内只核转录，不恢复missing shells或给严格缺项upper bound；source说典型<1e−9不是每点保证。

响应原件新建为`raw/papers/gpt/day15-20261016/bricc-z70-489p8-fo-m1-0f74bd9078a7.html`和`raw/papers/gpt/day15-20261016/bricc-z70-489p8-fo-e2-bde3a2eefe5d.html`，从不stage raw。全部printed rows及定向设计保存在[[internal-conversion-analysis]]与[[st99-pdco-calibration-table-replay]]，不仅在outputs。查询/离线capture/计算脚本分别为`day16_bricc_reference_query.py`、`day16_bricc_reference_capture.py`、`day16_bricc_n164_icc_design.py`；精确冻结与hash见其artifact链接。

### 固定ST99候选的理论reference

采用[[starosta-1999-pdco-experimental-test]]的单个mixed点atanδ=−21°，radiative weights M1=.871572/E2=.128428，Eq5给alphaK=.0335323855、L=.0050748908、programTot=.0400663669。与同表pureE2的K比为2.273382。它们是新匹配壳层的**模型参考**，不是重现原文未明确定义的alpha_κ，也不是实验测得δ或一整族候选的区间。

M1/E2 ICC的quoted误差共享table/energy来源，Cov未给；只把两quoted marginal scales用于rho=−1/0/+1的敏感性，mixedK local sigma约.0004088/.0004366/.0004628。该范围不是实际Sigma或置信区间，未加入delta误差、energy.1keV、A/radius、penetration、ionization、E0、geometry等预算，不再独立叠加.3%插值。

同Jπ的14+→14+候选允许非负E0 electron rate，故在固定reference/delta截断下只能使alphaK≥.0335324，不能把这个点降到pureE2 .01475；这是条件lower-bound设计，不是任意delta/核结构/penetration的普适排除。未知rho²/Omega、electron接受与branch缺口仍保留。标量ICC只含δ²，不判断phase sign。两壳联合识别需要明确Omega/reference与response的rank，详见owner方法页。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| KB08-D15-1 | 同Jπ E0无single-gamma，489.8keV低于pair阈值；Omega为s^-1，E0表不采用统一Datheor，不能用ICC1.4%作E0误差。 | direct-method-and-case-boundary | direct-and-task-application | printed204 Sec3.1 Eq7/11；printed212–213 Sec4.4 | true |
| KB08-D15-2 | TableB.1的Z70参考为A173、Kbinding61.3323keV，b仅closed shells；本次Z70 web lookup不等于A164 finite-size重算，currentbackend mass/datafilehash未公开核定。 | reference-identity-boundary | direct-and-web-scope | printed222 TableB.1 Z70；printed228 footnote b | true |
| KB08-D15-3 | 官方Z70/E489.8 FO-only新两POST返回M1/E2 K .0363(5)/.01475(21)、programTot .0432(6)/.0188(3)，v2.3(2011)；N6/N7空、>398keV警告各两条，未补0/认证完整total，dataenergy误差未发送。 | theory-lookup-with-coverage-boundary | direct-program-output | officialANU Z70 E489.8 M1 response0f74bd9078a7；E2 responsebde3a2eefe5d | true |
| KB08-D15-4 | 固定ST99 atanδ−21°及新FO参考给mixedK .0335323855；非负E0在相同reference截断下只升高此比。未知实际response/δ族/penetration等使其仍是reference设计，非489观测或唯一Jpi。 | conditional-reference-and-design | task-calculation | printed203 Eq5；printed204 Eq11；本节fixedpointtable | true |


### Z70/489.8实际返回的全部shell与ratio行

表头M1/E2为核辐射多极性，行M1/M2等为电子subshell，二者不可混淆。E(ce)对major sum是程序打印的代表值，shell-ratio行没有E(ce)。N6/N7保持未返回；比例行不参与shell之和。均为上述同两次FO理论lookup。

| shell / ratio | E(ce) M1/E2 (keV) | nuclear M1列 | nuclear E2列 |
| --- | --- | --- | --- |
| Tot | — / — | 0.0432(6) | 0.0188(3) |
| K | 428.47 / 428.47 | 0.0363(5) | 0.01475(21) |
| L1 | 479.31 / 479.31 | 0.00495(7) | 0.00186(3) |
| L2 | 479.82 / 479.82 | 0.000362(5) | 0.000848(12) |
| L3 | 480.86 / 480.86 | 4.75E-5(7) | 0.000430(6) |
| L-tot | 479.36 / 479.66 | 0.00536(8) | 0.00314(5) |
| K/L | — / — | 6.77(14) | 4.70(10) |
| M1 | 487.40 / 487.40 | 0.001095(16) | 0.000408(6) |
| M2 | 487.63 / 487.63 | 8.90E-5(13) | 0.000208(3) |
| M3 | 487.85 / 487.85 | 1.189E-5(17) | 0.0001088(16) |
| M4 | 488.22 / 488.22 | 1.204E-7(17) | 7.73E-7(11) |
| M5 | 488.27 / 488.27 | 1.195E-7(17) | 5.97E-7(9) |
| M-tot | 487.42 / 487.54 | 0.001196(17) | 0.000726(11) |
| L/M | — / — | 4.48(9) | 4.32(9) |
| N1 | 489.31 / 489.31 | 0.000258(4) | 9.58E-5(14) |
| N2 | 489.40 / 489.40 | 2.04E-5(3) | 4.77E-5(7) |
| N3 | 489.46 / 489.46 | 2.70E-6(4) | 2.48E-5(4) |
| N4 | 489.60 / 489.60 | 2.81E-8(4) | 1.80E-7(3) |
| N5 | 489.62 / 489.62 | 2.75E-8(4) | 1.373E-7(20) |
| N6 | 489.79 / 489.79 | 未返回 | 未返回 |
| N7 | 489.79 / 489.79 | 未返回 | 未返回 |
| N-tot | 489.32 / 489.36 | 0.000281(4) | 0.0001686(24) |
| L/N | — / — | 19.1(4) | 18.6(4) |
| O1 | 489.75 / 489.75 | 3.76E-5(6) | 1.395E-5(20) |
| O2 | 489.77 / 489.77 | 2.41E-6(4) | 5.65E-6(8) |
| O3 | 489.78 / 489.78 | 2.97E-7(5) | 2.73E-6(4) |
| O-tot | 489.75 / 489.76 | 4.03E-5(6) | 2.23E-5(4) |
| L/O | — / — | 133(3) | 141(3) |
| P1 | 489.79 / 489.79 | 2.17E-6(3) | 8.07E-7(12) |
| P-tot | 489.79 / 489.79 | 2.17E-6(3) | 8.07E-7(12) |
| L/P | — / — | 2.47E3(5) | 3.89E3(8) |

### 同能量E0 electronic factor与两壳rank的有界续查

上面的pureM1/E2两POST预算完成后，因owner的K/L1 full-rank条件仍缺匹配Omega，另冻结一个明确新问题/预算：**仅1POST、0retry**，Z70/E489.8/E0、名义能量。输入`dataset=BrIccFO`，实际response必须按返回的**BeOmg**识别，不能误记为FO E0表或M1/E2的1.4%误差。actualversion仍BrIccS v2.3(9-Dec-2011)，无coverage warning，但只返回K/L1/L2及programTot；不据此认证其它shell已完整覆盖。

| returned row | E(ce) (keV) | value | 单位 |
| --- | ---: | ---: | --- |
| K | 428.47 | 5.595E10 | s^-1 |
| L1 | 479.31 | 8.284E9 | s^-1 |
| L2 | 479.82 | 1.616E8 | s^-1 |
| programTot | — | 6.440E10 | s^-1，非认证complete total |
| K/Tot | — | .8688 | 无量纲 |

原HTTP SHA-256 `f6bf17c5f15368b2e3143175415a959b9745b87446d134c2434a8abf315aa1dc`；新raw为`raw/papers/gpt/day15-20261016/bricc-z70-489p8-e0-beomg-f6bf17c5f153.html`，未覆盖已有raw且不stage。列出K+L1+L2为6.43956E10，与programTot打印精度相容只检转录；没有填缺壳层或理论误差。这个量是电子因子Omega，pureE0没有single-gamma，不能给它定义普通ICC。

用上述两壳M1/E2与Omega，定义w为M1辐射分数、z=OmegaK rho²/Tgamma，无量纲，则K/L1 ratios减pureE2 vector后，矩阵为`A=((.02155,1),(.00309,.1480607685))`。列分别归一后夹角.262192°、2norm条件数437.0513。打印中心满秩不代表stable inversion；source-inspired的名义1% L1 ratio变化、K不变可使w移动−.452108（不是测得误差或blind实验）。另一个postlookup独立scope控制在两K quoted margins内可取M1_K=.0358209924/E2_K=.0149511832，使两列严格共线；不声称实际shared atomicCov允许该同时偏移，也不把marginal误差当joint置信域。

因此补两个electron shell只有在reference/响应/误差和条件数都受控时才可能有效。本任务没有E0观测或拟合rho²，未将actual164Yb ΔJ0候选解出。input/hash/矩阵/derivative与rank-loss控制均在[[internal-conversion-analysis]]和本run artifact保存，非原作者结果。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| KB08-D15-5 | 官方E0新一次POST实际返回BeOmg/v2.3(2011)，K/L1/L2 Omega为5.595E10/8.284E9/1.616E8s^-1，programTot6.440E10/Kratio.8688；只有列明shell，无reportedtheoryerror，不将其当ICC或完整total。 | theory-electronic-factor-lookup | direct-program-output | officialANU Z70 E489.8 E0 responsef6bf17c5f153 | true |
| KB08-D15-6 | 以新printedK/L1 pureICC和Omega作条件M1fraction/E0rate线性模型，中心column-normalizedcondition437、夹角.2622°；printedmarginalbox存在ranklosswitness，只证明边际摘要不足以认证stableactualinversion，不给真实Cov/δ/E0。 | conditional-identifiability-and-scope-test | task-calculation | printed204 Eq7/11；本节K/L1matrix与rankcontrol | true |


## 2026-10-18 W178 K-shell理论输入与使用边界：新增Codex self-audit

**原页面全部字节前缀与既有人审范围保持不变。本节及KB08-D16-1–4是新Codex self-audit，needs_review:true，不扩张为human-reviewed。** 本session在来源前冻结primed回忆后，重核原PDF SHA-256，重读printed202–214完整主线及AppendixA printed215，定向原图核Eq1/5、Eq20、Table2、Sec4.1.2/Eq24和printed223/TableB1的74-W-184行；未逐行重读整个AppendixB。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| KB08-D16-1 | 原Eq20对有效mixed多极且MR缺失的情形可用delta=1作默认平均alpha，误差取pure差的一半；这不是实测delta=1。Table2的1.4%含interpolation。Sec4.1.2区分NP correction与DF的surface-current近似，动态penetration需核参数，本run没有拟合lambda/eta/chi或认定W178存在异常转换。 | original-rule-and-model-boundary-recheck | direct-and-self-audit | printed205 Eq20；printed206 Table2脚注；printed207 Eq24与208 Sec4.1.2 | true |
| KB08-D16-2 | 两次官方nominal lookup只取Z74/E920.8/BrIccFO、pureM1/E2，actual程序echo BrIccS v2.3(9-Dec-2011)。K为.00995(.00014)/.00435(.00006)，programTot为.01188(.00017)/.00533(.00008)。是理论reference，不是测量或A178专门波函数重算。 | versioned-official-theory-query | direct-online-theory-object | https://bricc.anu.edu.au/；DAY16-BRICC-W178-K-REFERENCE-01的M1/E2响应K与Tot行 | true |
| KB08-D16-3 | 两响应N6/N7均空并警告EG>398.000keV，未补0/认证completeTotal；K行有效且Ece851.27keV。published TableB1给74-W-184、Kbinding69.5250keV，当前Z-only接口未暴露实际mass或datafile hash；物理Egamma误差.1keV未传入nominal查询，实际Cov也缺。 | shell-coverage-and-reference-boundary | direct-and-self-audit | 两web响应N6/N7/K行和warnings；printed208 Sec4.1.4/4.1.6；printed223 TableB1 | true |
| KB08-D16-4 | 将新K理论与N178-12 reported Kexp=.0067(.0011)作明确条件比较，本任务R=.66两个固定point根预测K=.00990314/.00435261，均不与所列一倍quoted marginal boxes相交；这不是实验排除或整族delta分支检验。名义Eq5中央映射给abs(delta)=1.176001，正负仍双解，不是新测delta或联合fit。 | bounded-companion-forward-check | task-calculation | 本篇printed203 Eq5；N178-12；day16_bricc_w178_reference.py analyze及冻结input | true |

### 实际查询对象与可复现性

输入identity `DAY16-BRICC-W178-K-REFERENCE-01`，输入SHA-256 `e2d0cd1737398b4b2698cb5c2fbf4f49399e126300dad228a1e205cbcaeba934`。先保存query input，再pure M1/E2各一POST，零automatic retry；没有NH/All/其它能量或E0新查询。实际HTTP raw hashes：

| mode | raw HTTP SHA-256 | 临时快照 |
| --- | --- | --- |
| M1 | `293b1fe91a101ce879518952c49614f24fc0232d529dfd32e76c0bd07d8507cd` | `tmp/day16-bricc-w178/responses/bricc-Z74-E920p8-FO-M1.html` |
| E2 | `c585c7e826cdc09e1d614cb6224e0d8447217ad81bc55af8e88cd42d1d157256` | `tmp/day16-bricc-w178/responses/bricc-Z74-E920p8-FO-E2.html` |

HTTP200与offline数值校验分开：核Z/element/energy/multipole/dataset/version echo，逐行保存所有coef/error/Ece、unknown cells与warnings；没有将404/HTML说明或参数回显当数据。原网页仅在repo tmp，本次保持raw归档不变；关键K/程序Tot数值、覆盖与hash已在本source保存。旧Z70/E489.8的程序/结果没有被本次W query替换。

程序[day16_bricc_w178_reference.py](../../system/scripts/day16_bricc_w178_reference.py)提供query/capture/analyze三个独立阶段。query/capture时的准确旧code hash及snapshot在本日run-dir的code-snapshot-002；后续增加analyze未重复网络查询。query receipt/capture/conditional comparison保存输入输出hash及真实状态。

### 从theory input到真实companion的门

[[nndc-2009-178w-dco-reference-records]] N178-12是13C1998Pu01层的reported K-shell experiment；不以CC total或adopted多极标签增加独立似然。当前只能做普通FO/M1-E2、已报告alpha定义正确的条件检验。原electron/photon efficiency、角接受、门/峰分解、normalization/Σ及可能共享reference仍未取得。

在Eq5名义pure系数下，reported central alphaK映射到radiative E2份额.580357与abs(delta)1.176001；把alphaK的quoted范围[.0056,.0078]反映到名义theory得abs(delta)[.789423,1.865476]，正负两支，**没有置信水平**，未传播物理E误差、theory共同Cov或原DCO的branch family。若观测central在pure envelope之外，程序保留no-physical-central-root而不夹到端点。

这项结果限制的是所声明fixed point model和“额外observable必然挑中其中一根”的预期，不裁决原实验或结构模式。转换delta符号不会改变ICC；不能用phase换号掩盖magnitude/response条件的问题。未自由调sigma、K-efficiency或penetration参数强配数据。当前batch stop contract完成；下一高信息输入为primary calibration/response及同对象联合误差，而非更多任意能量query。

## 2026-10-18未观测168.71-keV参考：新的nominal总转换输入

本节与KB08-D16-5为新增Codex self-audit；本节前全部旧字节/人审prefix保持，未扩人审。因[[martin-1987-ensdf-mixing-ratio-phase-conventions]] MA87-3的Eq9需要totalICC，独立冻结新168.71-keV/W74/FO纯M1/E2请求，各一POST/零retry；不是重复920.8-Kshell查询。实际BrIccS v2.3(9-Dec-2011)，本能量所列N6/N7均有数值且无missingwarnings。

| multipole | programTot | K | Ltot/Mtot/Ntot/Otot/Ptot |
| --- | --- | --- | --- |
| M1 | 1.073(.015) | .891(.013) | .1409/.0321/.00772/.001260/.0000897 |
| E2 | .553(.008) | .265(.004) | .218/.0546/.01289/.00180/.0000204 |

所列shelltotal之和M1=1.0730697、E2=.5523104，差异处于各列打印精度口径，不擅以sum重写programTot或称allphysicalcorrections已认证。输入nominalE168.71，其.05keV误差未传入；Zonly/defaultW184/reference及backend原子数据hash仍不暴露，不声称A178核尺寸重算。total与K不可互代；theoryerror/Cov、能区与noE0等适用条件保持。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| KB08-D16-5 | 新Z74/E168.71/BrIccFO pureM1/E2实际返回Tot1.073(.015)/.553(.008)、K.891(.013)/.265(.004)，v2.3(2011)；所列shell数值齐全/无warning，与920.8能区N6/N7缺值边界分开。是nominaltheoryinput，不是独立measuredICC或A178专用重算。 | versioned-official-total-conversion-input | direct-online-theory-object | https://bricc.anu.edu.au/；DAY16-W178-168P71-UNOBSERVED-IC-01的M1/E2响应Tot/K行 | true |

HTTP SHA256 M1=`04e1dcc22d60fa663faadfca5f575a60d2f78fa0f246c0b84c6323df6a137494`、E2=`d6a3a1a7c9712a7a4429751ee640bd0dea05c27a13f4f366e2d3e49d3594298d`；raw只在repo tmp，不改旧query或rawarchive。[[internal-conversion-analysis]]保存完全未观测/光子选择两样本的权重和W178有界设计；没有新测delta或加一项samegate实验。
