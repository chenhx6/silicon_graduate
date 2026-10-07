---
type: source
title: "Evaluation of Theoretical Conversion Coefficients Using BrIcc"
aliases: [Kibedi 2008 BrIcc, BrIcc theoretical conversion coefficients, Kibedi 2008 ICC uncertainties]
created: 2026-07-12
updated: 2026-10-08
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
