---
type: source
title: "On the Graphical Extraction of Multipole Mixing Ratios of Nuclear Transitions"
aliases: [Rezynkina 2017 graphical extraction, Rezynkina 2017 mixing-ratio extraction, graphical ICC mixing-ratio extraction]
created: 2026-07-12
updated: 2026-07-12
status: ai-draft
review_status: human-reviewed
source_type: method-article
reading_depth: read
title_original: "On the Graphical Extraction of Multipole Mixing Ratios of Nuclear Transitions"
authors: [K. Rezynkina, A. Lopez-Martens, K. Hauschild]
journal: Nuclear Instruments and Methods in Physics Research Section A
year: 2017
volume: 844
pages: 96--98
doi: 10.1016/j.nima.2016.11.029
language: en
canonical_source: doi:10.1016/j.nima.2016.11.029
citation_key: rezynkina_2017_graphicalextraction
raw_file: "raw/papers/2017_Rezynkina et al_On the graphical extraction of multipole mixing ratios of nuclear transitions.pdf"
raw_sha256: AF87B4E5CE2FFCCEE5484902B252E8FCD4FD0940EE996B204BF7983FD2A41E72
nuclei: []
reactions: []
observables: [multipole-mixing-ratio, internal-conversion-coefficient]
methods: [internal-conversion-analysis]
tags: [mixing-ratio, internal-conversion, graphical-method, uncertainty-propagation, gamma-spectroscopy]
---

# Rezynkina et al. (2017): Graphical Extraction of Multipole Mixing Ratios

## Bibliographic Record

K. Rezynkina, A. Lopez-Martens and K. Hauschild, *Nuclear Instruments and Methods in Physics Research Section A* **844**, 96--98 (2017), DOI `10.1016/j.nima.2016.11.029`, citation key `rezynkina_2017_graphicalextraction`.

The BibTeX key matches uniquely by title, year and DOI. Local file size is `394118` bytes; local timestamp `2026-03-31 11:06:11`; SHA-256 is recorded above.

## Scope and Reading Depth

The full three-page article was read from the PDF text layer. Key checks covered the introduction on ICC-based `delta` extraction, the probability-density derivation in Sec.2, the graphical construction in Sec.3, and the applicability/limitation discussion in Secs.4--5.

This is a `method-ingest` source. It does not provide a new experimental nuclear-structure result; its value is methodological: how to propagate measured and theoretical internal-conversion-coefficient uncertainties into asymmetric `delta` intervals.

## Summary

The paper proposes a graphical method for extracting multipole mixing ratios from internal-conversion coefficients. Instead of treating the theoretical ICC values as exact and the mixed-transition formula as a simple inversion, the authors propagate the uncertainties of the measured conversion coefficient and of the pure-multipole theoretical coefficients. They derive the full probability density function `P(delta)` and compare it with a simpler graphical construction based on intersections of the measured and theoretical ICC bands.

For the current Wiki, the main lesson is not a new number for one nucleus, but a method boundary: ICC-based `delta` extraction can require asymmetric confidence intervals, and naive inversion of the mixed-transition ICC formula can bias the central value when the experimental ICC uncertainty is large.

## Experimental or Theoretical Setup

- Method input: experimental internal-conversion coefficient `alpha_exp`, plus pure-multipole theoretical coefficients `alpha(sigma L)` and `alpha(sigma' L')`.
- ICCs may be determined either from electron-to-gamma intensity ratios or, when electron measurements are incomplete, from X-ray-to-gamma intensity ratios with fluorescence yields.
- The worked example is a `200 keV` mixed `M2/E3` transition in `251Fm`, using `K`-shell conversion coefficients and BrIcc values as the theoretical input.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| RZ17-1 | 文章把 mixed-transition `delta` extraction 建立在 internal-conversion coefficients 上，并回顾了 `alpha_tot = I_ICE / I_gamma` 以及 `X-ray / gamma` 替代测量路线。 | method-formalism | direct | p.96, Introduction and Eqs.(1)--(2) | false |
| RZ17-2 | 作者指出 pure-multipole theoretical ICC values 也带有约 `1--2%` 的不确定度，来源于理论计算本身和非 tabulated 数值的插值；这些不确定度应进入 `delta` 误差传播。 | method-formalism | direct | p.97, Sec.2 first paragraph | false |
| RZ17-3 | 对 mixed transitions，`delta` 的概率密度 `P(delta)` 被写成 measured `alpha_exp` 与两条 pure-multipole theoretical ICC PDFs 的卷积，因此一般不是 Gaussian。 | method-formalism | direct | p.97, Sec.2, Eqs.(7)--(15) | false |
| RZ17-4 | 图解法通过 `alpha(delta)` 理论曲线及其上下不确定度带，与 `alpha_exp` 及其置信区间的交点来给出 `delta` 的中心值和非对称误差条。 | method-formalism | direct | p.98, Sec.3, Eq.(17), Fig.2 | false |
| RZ17-5 | 对 `251Fm` 的 `200 keV` `M2/E3` 示例，全文给出 analytical PDF mean `delta_a = 0.92^{+0.42}_{-0.37}`，而 graphical method 得 `delta_g = 0.81^{+0.47}_{-0.36}`。 | observed-fact | direct | p.97, Table 1; p.98, Sec.3 | false |
| RZ17-6 | 作者指出仅用混合 ICC 公式直接反演得到的解，在该 `251Fm` 示例中低估了 `P(delta)` 的均值；当实验 `alpha` 的相对误差超过约 `25%` 时，这种偏差开始明显，`60%` 时可达 `36%`。 | method-boundary | direct | p.98, Sec.4, Fig.3 | false |
| RZ17-7 | 结论段说明：图解法通常给出不小于真实 `68%` 置信区间的区间估计，但在实验 ICC 不确定度很大时，中心值仍可能被低估；若图解法不适用，应回到完整卷积。 | method-boundary | direct | p.98, Secs.4--5 | false |

## Nuclear Structure Information

The nucleus-specific content is only a worked `251Fm` example for method illustration. This source should be cited as an ICC-based mixing-ratio extraction method note, not as primary structure evidence for `251Fm`.

## Authors' Interpretation

- The graphical construction is intended as a simple and illustrative alternative to a heavier analytical/PDF treatment.
- The method is most useful when one wants an asymmetric uncertainty estimate without assuming the final `P(delta)` is Gaussian.
- The authors explicitly treat the graphical interval as conservative rather than exact.

## Model Results

- The paper is methodological and does not contain a separate nuclear-structure model comparison.
- The only computational layer is the PDF construction and the use of theoretical ICC inputs for pure multipoles.

## Competing Interpretations and Limitations

- The method still depends on the quality of the theoretical ICC inputs; it is not a model-free extraction.
- The graphical interval is not the exact PDF interval; it is a practical approximation.
- When the experimental ICC uncertainty is large, the graphical method itself can bias the central `delta` value low.
- This paper should be paired with an ICC theory/database source such as [[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] rather than used alone.

## Extracted Pages

- Nuclei:
- Bands:
- Concepts:
- Methods: [[internal-conversion-analysis]]
- Observables: [[internal-conversion-coefficient]], [[multipole-mixing-ratio]]
- Projects: [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]

## Personal Notes

This paper is small but high-yield. Its real value is the warning that even after choosing an ICC calculation, `delta` extraction can remain asymmetric and non-Gaussian. That makes it a good complement to BrIcc and to the general "one observable, one answer" simplifications often used in practice.

## 2026-10-18原式复核：P(delta)的测度与卷积配方边界

本节是新Codex self-audit，**全部旧字节prefix、page human-reviewed和RZ17-1–7/needs_review:false保留**，不把新检查冒充人审。新使用时先看本节的复现边界：旧摘要对“convolution/true68%”的记录是作者方法声明，尚不是本Wiki对其RooFit配方/覆盖性的独立证明。

本session先冻结primed预期，再核source-declared原SHA-256 `af87b4e5ce2ffccee5484902b252e8fcd4fd0940ee996b204bf7983fd2a41e72`、重读完整三页并放大Eqs7–17/Table1/Figs1–3。首hardcodedhash手抄多一个c导致guard失败，改为从source读hash核actual后确认原raw未变，不当来源身份异常。Crossref重新核三作者/NIMA844/96–98/2017，原PDFonline2016与volume2017分开。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| RZ17-8 | Eq3–5仅得到abs(delta)，作者示例为251Fm/200keV/M2-E3/5/2+→9/2−、K-shell，Table1输入alphaexp8.8(3.1)、alphaM214.49(.21)、alphaE3.227(.004)。它不是新采集或本任务重测；不要换作E2/M1数据。 | published-example-and-coordinate | direct | printed96 Eq3–5；printed97 Table1 | true |
| RZ17-9 | Eq7/8以变量变换写partialPi，Eq11–13各Pi将另两alpha固定在中央值，Eq14写P=P1⊗P2⊗Pexp且说RooFit。三页未给可复跑的centering/FFT范围/support/归一recipe；若将其读成三个正deltaPDF的普通未平移sum convolution，会多加两个centraldelta，不能直接重建所报mean。 | literal-formula-and-producer-boundary | direct-and-task-invariant | printed97 Eqs7–15/Fig1/Table1 | true |
| RZ17-10 | 作者Eq15均值与“34%各在mean两边”区间为.92^(+.42/−.37)，Fig1上error却标+.43；graphical.81^(+.47/−.36)由Eq17 band交点定义。“conservative/true”是该文方法解释，本文未给频率学coverage保证或实际RooFitcode。 | reported-interval-definition-and-printing | direct | printed97 Eq15正文/Table1/Fig1annotation；printed98 Eq17/Conclusions | true |
| RZ17-11 | 显式选independentGaussian三alpha并condition alpha1>alphaexp>alpha2>0的joint pushforward，本任务均值.924386996与原.92打印相容，equaltailed16/84为[.5093701,1.2714561]，按本分布mean左右各.34则[.6156646,1.6700673]；均不以此更改发表δ或认作新实验CI。 | declared-probability-measure-audit | task-calculation | printed97 Table1/Eqs7–15；DAY16-RZ17-PDF-MEASURE-01 | true |
| RZ17-12 | 同一声明measure的PDF尾为C/delta³、C=.08320715>0，mean有限但secondmoment对数发散；flat-delta Gaussian likelihood则趋正常数，0到∞不proper。故68%概率区间与sqrtVar(delta)、“flatprior无选择”不能混同。此结论限该Gaussian/物理域模型，不是原作者code已被证明使用无限域。 | derived-tail-and-parameterization-boundary | task-derivation-and-numeric-check | printed96 Eq4/5；printed97 Eq13/15；本任务tail/coordinate audit | true |

### 实际复算与尚未闭合的内容

冻结identity `DAY16-RZ17-PDF-MEASURE-01`、Table1参数在数值前固化。令A1/A2/E为三个独立Gaussian random inputs，对物理域H={A1>E>A2>0}显式条件化；从E=a(d)=(A1+d²A2)/(1+d²)变换到d>0的密度含绝对Jacobian `2d(A1−A2)/(1+d²)²`，并除Z=P(H)。这是**本任务声明的概率传播选择**，不是未注明prior/采样模型的普适“truePDF”。Z=.9636291873，其余约3.637%物理域外概率未静默夹到pure端点。

GaussHermite12/20与theta=atan(d)的Legendre80/160/320/640均值稳定约5e−14；独立bivariate ratio路线以X=A1−E、Y=E−A2给Cov(X,Y)=−Var(E)=−9.61、correlation≈−.99771255，八点PDF差≤2.62e−13；independentGaussian原inputs不使这两个差或最后ratio独立。独立800000抽样/seed2026101804在物理域保留770970，分位数与积分相符。MC sampleSE不被用来证明无限域variance有限。

| 统计/算法对象 | 本任务数值与意义 |
| --- | --- |
| Eq5 direct inverse | .8146850022；不是P的mean或mode证明 |
| declared joint pushforward mean | .9243869963；与作者.92在打印精度内相符 |
| sourceEq17实际band交点 | [.4515408969,1.2823631086]，准确回到source图解约.81^(+.47/−.36) |
| 上述graphical区间在本joint分布的概率 | .7280638427；不是频率覆盖率/普适保守性证明 |
| sourceanalytical打印界[.55,1.34]在本joint的概率 | .6710446540；在sourcecentral.92两边分别.40043746/.27060720，不能称本measure中各.34 |
| Pi三个positive均值 | .81454611/.81468507/.92426038；普通sumconvolution mean2.55349156 |
| theoryerror→0控制 | 普通positive convolution会把Pexp平移2δ0；必须另给error-kernel居中或实际producerrecipe，不能仅抄Eq14便称精确复现 |

新harness没有为了配source区间改Gaussian尺度/截断/δ号，也未把literal卷积failure归给实际RooFit代码。作者的mean可相容而interval/普通卷积口径尚未复现是当前结论；原文的所有数值仍按原样保留。

### 尾部与有界parameter的使用门

在E接近A2的物理端点时，a(d)=A2+(A1−A2)/(1+d²)，于是非零Gaussian密度乘Jacobian给p(d)∼C/d³。数值dmax2/10/100/1000的未重归一secondmoment分别约.839912/1.120635/1.316718/1.508353，随logcutoff增长；不能通过一次finitegrid MonteCarlo的有限samplevariance宣称真实Var有限。均值partial在dmax2仅.8299368，至1000才.9243038，故隐含plot/FFT边界也需保存。

若改为f=d²/(1+d²)∈[0,1]，其moment有界；但flatf与flatdelta是不同概率/先验选择。固定purealphas时a(f)=A1(1−f)+A2f的Jacobian是常数，本任务的E-transform可对应flatf的条件posterior；有theory nuisance时仍须完整写明joint模型。有限ICC数据本身在pureE3极限饱和，不能无声明地把flatdelta likelihood归一到∞。ICC仍不给sign。

原创[程序](../../system/scripts/day16_rz17_probability_measure_audit.py)、[输入](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/rz17-pdf-measure-input.json)、[结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/rz17-pdf-measure-audit.json)含全部模型、归一、变换、MC与failurecontrols；本节只新增selfaudit。决定`supports`非Gaussian/理论误差和图解交点方法，`limits`Eq14/“68%”转录为完整可运行算法或任何输入下的exactcoverage。新canonicalowner为[[icc-mixing-probability-domain]]，不覆盖旧人审事件。
