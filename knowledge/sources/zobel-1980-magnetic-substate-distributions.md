---
type: source
title: "The shape of magnetic substate distributions in fusion-evaporation reactions"
aliases: [Zobel 1980 magnetic substate distributions, Zobel 1980 attenuation coefficients, alignment-yrast curve]
created: 2026-07-08
updated: 2026-10-15
status: ai-draft
review_status: human-reviewed
source_type: experiment-method-article
reading_depth: deep-read
title_original: "The Shape of Magnetic Substate Distributions in Fusion-Evaporation Reactions"
authors: [V. Zobel, L. Cleemann, J. Eberth, H. P. Hellmeister, W. Neumann, N. Wiehl]
journal: Nuclear Instruments and Methods
year: 1980
volume: 171
pages: 223--231
doi: 10.1016/0029-554X(80)90494-2
language: en
canonical_source: doi:10.1016/0029-554X(80)90494-2
citation_key: zobel_1980_shapemagnetic
raw_file: "raw/papers/1980_Zobel et al_The shape of magnetic substate distributions in fusion-evaporation reactions.pdf"
raw_sha256: EAAACC6154936D8E1725A9A98B198FCFCF90D4CC3B70B31E51323A31CD1CFFCC
nuclei: [63zn, 65ga, 66ge, 67ga, 69as, 72se, 97tc]
reactions: ["57Fe(12C,xnyp) A≈70", "54Fe(14N,xnyp) A≈70", "58Ni(16O,xnyp) A≈70", "94Zr(6Li,xnyp)97Tc"]
observables: [attenuation-coefficient, angular-distribution-coefficient]
methods: [angular-distribution]
tags: [magnetic-substate-population, attenuation-coefficients, fusion-evaporation, gaussian-hypothesis, pado-support]
---

# Zobel et al. (1980): Magnetic Substate Distributions in Fusion-Evaporation Reactions

## Bibliographic Record

V. Zobel, L. Cleemann, J. Eberth, H. P. Hellmeister, W. Neumann and N. Wiehl, *Nuclear Instruments and Methods* **171**, 223--231 (1980), DOI `10.1016/0029-554X(80)90494-2`. The title, authors, year, DOI and file name uniquely match citation key `zobel_1980_shapemagnetic`.

## Scope and Reading Depth

Full text was read from the PDF text layer for pp.223--231. Key checks include Eq.1 for the angular-distribution/attenuation-coefficient relation, Eqs.3--6 for alignment change in cascades and superposed feeding components, Tables 1--2 and Fig.3 for measured attenuation-factor systematics, Figs.4--5 for Doppler-broadening effects, and the Appendix for uncertainty/covariance treatment. Some table rows in the text layer are OCR-noisy; source claims below avoid relying on unverified row-level transcription except where values are central to the authors' stated examples.

This is an `experiment-ingest + method-ingest + project-ingest` source. It supports the P-ADO project by showing how attenuation coefficients and magnetic-substate distributions enter angular-distribution analysis, and by listing conditions under which Gaussian-shaped substate assumptions are acceptable or unreliable.

## Summary

Zobel et al. compile and measure spin-alignment attenuation factors `αK` for high-spin states in nuclei around `A≈70` populated by heavy-ion-induced fusion-evaporation reactions. They argue that the measured `α2,α4` pairs show a correlation and are generally near a theoretical alignment-yrast (ALY) curve derived from stretched γ cascades under the assumption of highly aligned entry states.

For P-ADO/mixing-ratio work, the key methodological boundary is explicit: angular distributions can determine multipolarities and mixing ratios if the alignments of the particular states are known, but using angular distributions alone leaves three unknowns (`α2`, `α4`, and `δ`) constrained by only two coefficients. Zobel et al. list three ways out of that ambiguity: estimate attenuation coefficients, add linear-polarization or conversion-coefficient measurements, or assume a one-parameter magnetic-substate distribution such as a Gaussian. The Gaussian magnetic-substate assumption is therefore a practical reduction of unknowns, not a universal fact.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| Z80-1 | 对 prompt dipole/quadrupole γ rays，作者写出 `W(θ)=1+α2(I)A2maxP2(cosθ)+α4(I)A4maxP4(cosθ)`，其中 `αK=PK/BK` 表示 actual partial alignment 相对 complete alignment 的衰减系数。 | method-formalism | direct | p.223, Eq.1 and preceding paragraph | false |
| Z80-2 | 作者指出若 particular states 的 alignments 已知，fusion-evaporation 后的大各向异性角分布可用于确定 γ-ray multipolarities and mixing ratios；在 Gaussian 参数化中，这类 alignment 信息可与 `σ/I` 或 Gaussian variance 相联系，但本文直接使用的是 `αK`。 | method-formalism | direct | p.223, Introduction first paragraph | false |
| Z80-3 | 仅从角分布实验得到两个 coefficients 时，要同时确定 `α2`、`α4` 和 mixing ratio `δ` 三个参数会有歧义。作者给出的三类出路是：(a) 用 statistical-model 估计 attenuation coefficients，(b) 增加 linear polarization / conversion-coefficient measurements，或 (c) 假设单参数 magnetic-substate distribution。 | method-formalism | direct | pp.223--224, Introduction | false |
| Z80-4 | 作者列出三类处理途径：statistical-model estimate of attenuation coefficients、linear polarization / conversion coefficients additional measurements、或用单参数 distribution function 表示 magnetic-substate populations。 | method-formalism | direct | pp.223--224 | false |
| Z80-5 | Gaussian 是最简单的单参数分布选择，可把未知数降为 `δ` 与 Gaussian variance；但作者同时引用 A≈40 compilation 指出并非所有数据都支持固定 `αK` relation。 | author-interpretation | direct | p.224, Introduction | false |
| Z80-6 | 在 heavy-ion compound reactions 中，evaporated nucleons 通常只带走较小 angular momentum，残余核 entry states 仍高度 aligned；direct feeding primarily populates high-spin states。 | review/background | direct | p.224, Sec.2.1 | false |
| Z80-7 | 作者定义 ALY curve 为 completely stretched cascade 可给出的 highest possible alignments；non-stretched transitions cause larger alignment loss and shift final `α2,α4` pairs down along or below the stretched-cascade curve。 | method-formalism | direct | pp.225--226, Fig.2 | false |
| Z80-8 | 对多个 feeding components，final magnetic-substate distributions must be superimposed；若两个 components contribute，resulting `α2,α4` lies on the connecting line between component pairs according to relative intensities。 | method-formalism | direct | p.227, Sec.2.3 | false |
| Z80-9 | 作者的 A≈70 / `97Tc` data compilation 中 `α2,α4` pairs are concentrated around the ALY curve and generally consistent with expected behavior once confidence ellipses are considered。 | observed-fact | direct | pp.227--228, Tables 1--2, Fig.3 | false |
| Z80-10 | Gaussian/ALY use is conditional and is central for P-ADO caution: authors state Gaussian-shape analysis should be acceptable in many cases only if there is no β feeding, no preceding isomeric state, and the level lifetime is long enough that Doppler broadening can be neglected。 | author-interpretation | direct | p.230, Summary | false |
| Z80-11 | Short lifetimes and Doppler broadening can remove angle-dependent peak intensity from Gaussian peak fits; for their example, even lifetimes above 2 ps can cause more than 10% loss at `θγ=0°`, shifting apparent attenuation coefficients。 | model-calculation | direct | pp.228--230, Figs.4--5, Table 3 | false |
| Z80-12 | The Appendix states that covariance between fitted Legendre coefficients must be included; confidence regions for `α2,α4` are ellipses rather than simple rectangles from independent error bars。 | method-formalism | direct | pp.230--231, Appendix Eqs.A1--A6 | false |
| Z80-13 | Fig.5 explicitly links initial-level lifetime to apparent attenuation coefficients: its upper panel shows Doppler-broadened line shapes for different lifetimes, middle panel shows lifetime- and angle-dependent intensity loss outside the Gaussian central peak, and lower panel shows the resulting shifts of `αK` pairs for a pure quadrupole transition. | model-calculation | direct | pp.229--230, Fig.5 caption and text | false |
| Z80-14 | p231的A2扫描字面在两个relative-variance项后仅减2rho；rho按下一行定义为标准correlation。按ratio Jacobian，相关项还需乘sigma_b0 sigma_bK/(b0 bK)，否则chosen positive-Cov控制可给负variance。后半为Codex公式自审，不是officialerratum。 | primary-transcription-and-task-algebra | mixed | printed p.231 / PDFp.9，Eq.A2与紧随rho定义 | true |
| Z80-15 | A4密度指数为−h/2且h的cross term为−2rho；A6扫描的polynomial为+a cross-square+b cross+c cross-square，却印b=+D cov。以A4作逆Cov核，所需b=−D cov。A5的ln[1/(1−x)]与Q/2半径可相容，不将其单独判为少2因子。 | primary-transcription-and-task-algebra | mixed | printed p.231 / PDFp.9，Eq.A4–A6 | true |
| Z80-16 | A3扫描写sigma_alpha=sigma_a/Amax，未见absolute-value；Table1的a4max转换为负而两组quotederrors均正，执行stderror转换需abs(Amax)或直接variance传播。公式/表的符号边界保留，未改raw。 | primary-transcription-and-convention | mixed | printed p.231 Eq.A3；printed p.226 Table1 958.0-keV行 | true |
| Z80-17 | Table1的67Ga 958.0keV、13/2+→9/2+行给a2=.349±.007、a4=−.093±.007与alpha2=.794±.016、alpha4=.431±.032；Table2 reactionA为57Fe+12C、40.0MeV。当前只转录同parent这一行作变量约定cross-check，不作全部17行Gaussian检验。 | published-fit-result-and-scope | direct | printed p.226 / PDFp.4，Table1 958.0-keV行；printed p.228 Table2 A | true |
| Z80-18 | 1980 Table1的67Ga输入指向Ref9=Zobel等NPA316,165(1979)，与1983 Ref4相同；配套方法文及后续beam scan不能仅凭两篇出版物认证independent raw events。 | source-lineage-and-boundary | mixed | printed p.226 Table1 ref栏；printed p.231 References9 | true |
| Z80-19 | p229引用Table3，但当前sha-verified223–231九页scan仅见Table1/2；GNOMON在p231 Ref14列为unpublished。当前不填缺失数值loss表或补造可重放code，Fig4/5属于source model control。 | input-readiness-boundary | mixed | printed p.229 Sec.4.2；printed p.231 References14 | true |

## Authors' Interpretation

- The ALY curve can serve as a first-order estimate for magnetic-substate distribution shape after compound reactions under the stated assumptions.
- Gaussian-shaped magnetic-substate distributions are useful in many cases, but the paper explicitly preserves exceptions: β feeding, isomeric feeding, short lifetimes/Doppler broadening, and problematic data analysis.
- The paper's ambiguity argument is not merely algebraic; the listed options (model-estimated `αK`, additional polarization/conversion observables, or a one-parameter distribution) show exactly where a P-ADO/mixing-ratio analysis imports external alignment information.

## Competing Interpretations and Limitations

- The paper reports attenuation coefficients `αK`, not a universal normalized Gaussian width `σ/I`.
- If a later analysis silently fixes `σ/I`, it is effectively choosing a one-parameter population model for the alignment problem; that choice may be reasonable only under the paper's stated conditions and with reaction/level-specific checks.

## Project Relation

For [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]], this source supplies the direct warning that angular-distribution-only fitting has more unknowns than coefficients unless alignment information or a substate-population model is supplied. It supports P-ADO motivation by showing why a preset alignment relation is a model assumption, why linear polarization/conversion information can be needed to resolve ambiguities, and why ignoring the conditional nature of `σ/I`-like alignment assumptions can make extracted `δ` values less credible.

## Extracted Pages

- Concepts: [[magnetic-substate-population]], [[spin-alignment]], [[sigma-over-i]]
- Methods: [[angular-distribution]]
- Observables: [[attenuation-coefficient]], [[angular-distribution-coefficient]], [[multipole-mixing-ratio]]
- Projects: [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]

## Personal Notes

User review on 2026-07-08 resolved Z80-2/Z80-3/Z80-10 wording. Later paper use should emphasize the three ambiguity-removal routes and the Fig.5 lifetime-to-`αK` distortion mechanism.


## Day14 Ref5主线复核与公式自审

来源前primed回忆先冻结，再核raw SHA256、Crossref200的DOI/title/sixauthors/171(2)/223–231/1980-04。视觉读完整9页，覆盖Eq1–6、Fig1–5、Table1/2、discussion/summary和Appendix A1–A6；Table1旋转为upright，A2/A6以4倍局部图复核。只选择与此前Zobel1983相同parent的958行用于符号转换；其余16行已看但不作为本练习对应transition或完整模型检验。

实验/方法主线：作者在p227只编入pure quadrupole、舍弃误差过大的weaklines，外来数据要能追随error analysis；因此Fig3不是无条件总体sample。ALY从高度取向entry、stretched-cascade及feeding前提导出，p230仍保留beta/isomer/Doppler与不同reaction条件反例。Fig4明确是人工spectrum，Fig5来自chosen GNOMON/recoil/lifetime模型，不能升级为各核实测寿命或新实验intensity loss。

公式自审落点：[[angular-distribution]]“Zobel1980附录：字面公式与联合覆盖”保留原A2/A3/A4–A6转录、独立JCovJ与Gaussian密度核，23项计算控制通过。A2/A6按字面执行与其定义不一致；A3的不带abs标准差需按正variance约定处理；A5的半径必须与Q/2一起看。这里是Codex转录/代数自审，未取得officialerratum，未回改raw或重新拟合原数据。真实sourceCov仍未知。

review_status:human-reviewed及Z80-1–13的false是2026-07-08继承记录，未新增人审或扩大其范围；本run新14–19均needs_review:true。Z80-12“Cov须包含/联合区域为ellipse”的一般结论仍支持，精确式子需采用上面的可复核边界。此为Day14内Day15无学分预习，不变更正式21/24或课程信用。
