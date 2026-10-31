---
type: source
title: "Chen et al. 2017 - Chiral geometry in symmetry-restored states: 128Cs"
aliases: [Chen 2017 128Cs angular-momentum projection]
created: 2026-10-10
updated: 2026-10-26
status: ai-draft
review_status: unreviewed
source_type: theory
reading_depth: deep-read
title_original: "Chiral geometry in symmetry restored states: Chiral doublet bands in 128Cs"
authors: [F. Q. Chen, Q. B. Chen, Y. A. Luo, J. Meng, S. Q. Zhang]
journal: "Physical Review C"
year: 2017
volume: 96
article_number: "051303"
doi: "10.1103/PhysRevC.96.051303"
arxiv: "1708.07282v1"
canonical_source: "https://doi.org/10.1103/PhysRevC.96.051303"
full_text_url: "https://arxiv.org/pdf/1708.07282v1"
downloaded_pdf_sha256: "d176aed6be49e350c18d130ec388383b680da9844173f4e0b386cb34f0c676c6"
nuclei: [128Cs]
models: [angular-momentum-projection, particle-number-projection, pairing-plus-quadrupole]
observables: [energy-spectrum, B(E2), B(M1), K-distribution, angular-momentum-orientation]
methods: [symmetry-restoration, Hill-Wheeler-equation]
tags: [128Cs, chirality, angular-momentum-projection, transition-strengths, spin-dependent-geometry]
citation_key: "Chen_2017"
raw_file: "raw/papers/gpt/learning-daily/20261009-DAY10-electromagnetic-ratios-collective-modes/chen-2017-128cs.pdf"
raw_sha256: "d176aed6be49e350c18d130ec388383b680da9844173f4e0b386cb34f0c676c6"
---

# Chiral geometry in symmetry-restored states: chiral doublet bands in 128Cs

## Bibliographic Record

- F. Q. Chen, Q. B. Chen, Y. A. Luo, J. Meng, and S. Q. Zhang, *Phys. Rev. C* **96**, 051303 (2017), DOI 10.1103/PhysRevC.96.051303.
- arXiv version 1: [1708.07282](https://arxiv.org/abs/1708.07282v1), posted 2017-08-24. DOI, title, author list, volume, and article number were checked against Crossref; the arXiv metadata identifies this version.
- The full text was read from the arXiv PDF. The temporary PDF copy had SHA-256 d176aed6be49e350c18d130ec388383b680da9844173f4e0b386cb34f0c676c6.

## Scope and Reading Depth

The main line was read from the model definition through the symmetry-restored basis, transition-strength comparison, K-distributions, angular-momentum orientation profiles, conclusions, and the references relevant to the experimental input. Figures 1–4 and Eqs. (1)–(11) were inspected. This is a theoretical calculation; its plotted experimental points are imported comparison data.

## Model and Observable Chain

The authors diagonalize a pairing-plus-quadrupole Hamiltonian in a basis with angular-momentum and particle-number projection. The orientation analysis uses distributions of angular-momentum components along the intrinsic short, intermediate, and long axes, plus the tilted-angle profile in the intrinsic frame. The calculation takes the Hamiltonian parameters from Ref. 40 and constrains the deformation to (β, γ) = (0.20, 30.0°); the blocked configuration is the lowest πh11/2 and fourth νh11/2 orbital. These are model inputs, not measurements made in this paper.

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CHEN17-1 | The starting Hamiltonian contains spherical single-particle, quadrupole-quadrupole, monopole-pairing, and quadrupole-pairing terms. | model-definition | model | PDF Eq. (1) | true |
| CHEN17-2 | The working basis restores angular momentum and neutron/proton number before Hill–Wheeler mixing of K and the specified four time-conjugate blocked κ states; this is not a demonstrated multishape or unrestricted quasiparticle-configuration mixing space. | model-definition | model | PDF Eq. (3) | true |
| CHEN17-3 | The 128Cs calculation fixes (β, γ)=(0.20,30.0°) and blocks a low πh11/2 orbital with the fourth νh11/2 orbital. | model-input | model | printed p. 5 | true |
| CHEN17-4 | Figure 2 compares calculated partner-band energies and intra/inter-band transition strengths with the data available from Ref. [14]. | model-comparison | mixed | Figure 2 | true |
| CHEN17-5 | The calculated B(E2) agrees near the bandhead but departs from the data at higher spin; the authors attribute the trend to the frozen nuclear shape. | model-limit | model | printed p. 5 | true |
| CHEN17-6 | The calculated K-distributions show chiral-vibration behavior near I=11ℏ, a static-chirality region around I=14ℏ, and a weakened pattern by I=18ℏ. | model-result | model | Figure 3 | true |
| CHEN17-7 | The calculated angular-momentum profiles place band A mainly in an s-l plane at I=11ℏ, in two handed orientations at I=14ℏ, and back toward a planar i-s orientation at I=18ℏ. | model-result | model | Figure 4 | true |
| CHEN17-8 | The transition-strength points in Figure 2 are comparison data cited to Grodner et al. 2006, rather than a new experiment in the AMP paper. | source-lineage | direct | Reference [14] | true |

## Figure-Level Reading

- Figure 2 places experimental points and AMP curves on the same energy and B-value panels. The authors report good energy reproduction and similar B(E2) in the two bands; the high-spin B(E2) trend does not follow the data because the shape is frozen. The M1 staggering appears in the calculation, but no geometry is directly measured by these strength curves.
- Figure 3 presents model K-distributions at I=11, 14, 18ℏ. The authors interpret the low-spin distributions as vibration about the s-l plane, the I=14ℏ distributions as two-handed orientations, and the less similar partner distributions at I=18ℏ as a weakening of static chirality.
- Figure 4 gives model angular-momentum orientation profiles. At I=11ℏ, band A is mainly planar while band B has two orientations; at I=14ℏ, both bands have paired orientations with finite tunneling probability; at I=18ℏ, the static-chirality pattern disappears in the model. This is a spin-dependent theoretical geometry, not a direct experimental assignment.

## Limitations and Evidence Boundary

The calculation imports the transition-strength and energy data cited as Ref. [14], fixes the deformation and blocked orbitals, and does not provide an experimental response/covariance reanalysis. The reported high-spin B(E2) mismatch is an explicit model limitation. A separately measured 128Cs g factor may be a complementary observable, but the present paper does not calculate that g factor; the different spin points and model frameworks prevent treating the two articles as a direct validation pair.

The detailed band-label crosswalk between Chen et al.'s A/B and the 2006 paper's yrast/side labels is not asserted here without a transition-by-transition verification.

## Summary

This is a symmetry-restored model study of the 128Cs partner bands. It calculates spin-dependent angular-momentum geometry and electromagnetic strengths, while reusing rather than independently remeasuring the Grodner 2006 data.

## Key Results

- CHEN17-1/2/3 describe the pairing-plus-quadrupole Hamiltonian, projection procedure, and fixed-shape inputs.
- CHEN17-4/5 compare calculated transition strengths with the 2006 data and show a high-spin B(E2) deviation.
- CHEN17-6/7 give spin-dependent K and angular-momentum geometry; CHEN17-8 identifies reuse of the Grodner 2006 experiment.

## Competing Interpretations and Limitations

The calculated geometry is model output, not a direct observation. The fixed-shape calculation departs from the high-spin B(E2) data, and the plotted experimental strengths are reused from Grodner 2006 rather than an independent dataset.

## Extracted Pages

- [[chirality-wobbling-competition-evidence]]
- [[grodner-2006-128cs-chiral-doublet-lifetimes]]

## Day24正文回读：投影态、相干核与几何分布

本轮复用原raw重新核SHA `d176aed6be49e350c18d130ec388383b680da9844173f4e0b386cb34f0c676c6`，279433bytes、12页；worker/root均读全文主线，worker全4图/Eqs1–11视觉，root视觉PDF3–7覆盖4图、基/metric/角字典/EM比较。fresh Crossref/officialabs核v1=2017-08-24，PDF1的August4,2021为另一个typeset字段，不建立新科学版本，VoR未核。WU18 PDF17 Ref55引用本篇；不是本篇自己的Ref55。

原CHEN17 flags保持；下列新增仅needs_review:true。直接正文、条件推导和未得producer分别记录。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CH17-D24-001 | 3D角动量与N/Z投影给good-I基；实际κ仅同一ν/π阻塞轨道及各自time-reversal组合四种，Hill–Wheeler混合K/κ。固定β=.20/γ30°，不等已混合多shape/多轨道对/其它qp数目的GCM空间。 | direct-state-space-and-frozen-input | direct-original | PDF3 Eqs2–5; PDF5 inputparagraph | true |
| CH17-D24-002 | 非正交基需norm kernel，g=N^1/2f；在保留支撑上g†g=f†Nf=1。raw abs(f)²不能直接当K概率，smallnorm截断/实际矩阵未给。 | direct-metric-and-probability-boundary | direct-original-plus-task-linear-algebra | PDF3 Eqs5–7 | true |
| CH17-D24-003 | Fig2实际给带内E2/M1及单向B→A跨带M1（W.u.），复用GR06 Ref14。没有跨带E2、signed RME/δ/g或实验全branch/Cov输出；不能当新增采集或双向全核已闭合。 | direct-output-and-data-lineage | direct-original | PDF5 comparisonparagraph; PDF6 Fig2; PDF10 Ref14 | true |
| CH17-D24-004 | 从Eq4投影态用于张量T可推Rfi=Σf_f* Tfi f_i、B=abs(Rfi)²/(2Ii+1)，在振幅层相干求和；用g需同步变换kernel。此双线性式是任务推导，正文未打印完整EM核、有效电荷/g/phase/实际producer，不能宣称逐数值复现。 | explicitly-derived-coherent-output-contract | direct-state-premise-plus-task-derivation | PDF3 Eq4; PDF5–6 Fig2scope | true |
| CH17-D24-005 | p(absK)用g的±K模方折叠并sumκ，成图后不能逆得各内部复幅phase。Eq7机械在K0加±0会双计；实际zero-bin convention未给，只留literal归一边界、不判图/程序错。 | distribution-and-literal-bin-boundary | direct-original-plus-conditional-inference | PDF3 Eqs6/7; PDF7 Fig3 | true |
| CH17-D24-006 | azimuthal图先对同κ的K振幅与WignerD相干求和，再取模方、sumκ/积分ψ′；保留K间干涉，不能叫完全无phase的abs(gK)²平均。发表的有限几何图仍不交付完整态/跨不同I的transitionkernel。 | direct-orientation-construction-and-boundary | direct-original-plus-output-scope | PDF4–5 Eqs8–11; PDF7 Fig4 | true |
| CH17-D24-007 | θ相对l轴、φ在i-s面从i轴起量，s-l平面是φ90°。标准Euler/Haar范数给P用sinθdθdφ的条件积分，非CH16 detB测度；Fig4只画θ0–90/φ0–180，完整域/折叠因子未另给，不按flat像素重归一。 | coordinate-measure-and-display-domain | direct-original-plus-labelled-Haar-derivation | PDF4 Eq8/Fig1; PDF5 Eqs9–11; PDF7 Fig4axes | true |
| CH17-D24-008 | 作者称without new/free parameter，仍有Ref40 H参数、固定shape/blocking及外部CDFT/PSM比较；未核Ref40原定标，不能断言严格out-of-sample。高spin E2因frozen shape偏离与I18 static特征减弱均须保留。 | parameter-and-adverse-result-boundary | direct-original | PDF1 Abstract; PDF5 input/E2paragraphs; PDF8 geometry/conclusion; PDF11 Ref40 | true |

### 与局部rate平均的差别

[[wu-2018-two-dimensional-collective-electromagnetic-transitions]] WU18-D24-001只按单ρ平均局部TAC带内率；本投影框架的态为|ΨIiσi⟩=Σb f_b P^Ii|Φb⟩。若指定张量算符，RME的线性性要求

$$\mathcal R_{fi}=\sum_{a,b}f^{I_f\sigma_f*}_a\,\mathcal T^{I_fI_i}_{ab}\,f^{I_i\sigma_i}_b,
\qquad B(T;i\to f)=\frac{|\mathcal R_{fi}|^2}{2I_i+1}.$$

这说明框架的相干输出合同；不能把本文未打印的actual核/EM参数补成已得。在g表示中还须将T核相应改为Nf^−1/2 T Ni^−1/2（保留支撑内），不能只换coeff。每个本征态overallphase本来任意，所缺是内部相干幅和EM算符一致的relativephase，不能发明可观测的band绝对phase。

### 两种取向图保留不同信息

K图p(absK)已折叠/求和；azimuthal图Gκ∝ΣK gKκ D*先有K/K′干涉，随后再取模方与求边缘，不能把两图都称为相位盲。有限发表图并不提供完整数字分布、κ内部态或跨Ii/If核；也不在这里作“所有完整取向密度都无tomography信息”的普适断言。

若ΣκK abs(g)²=1，使用标准全Euler域的dΩ=dψ′sinθ′dθ′dφ′，本任务推得∫₀^π sinθdθ∫_{−π}^π dφ P=1（或周期等价φ区间）。源Eq11本身未重写此归一，图只显示部分域，不擅补4倍或从图估左右概率/CI。φ从i轴起量，不能把与CH/WU不同原点的数字角直接拼合。

源I11振动/I14静态regime/I18减弱的几何解释，仍属于固定H/shape/空间的作者模型；有限平面概率不是独立测得的隧穿流或时钟。Projection不自动纳入未建的crossing/configuration/γ软度。新合同纳入[[135nd-chiral-partner-resolved-evidence-map]]，作为128Cs方法对照，不给135Nd/133Ce补EM数值。
