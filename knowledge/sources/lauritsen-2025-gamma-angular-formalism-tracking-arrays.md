---
type: source
title: "Gamma-ray angular correlations, distributions and linear polarization in tracking arrays"
aliases: [Lauritsen 2025 tracking-array angular formalism, Lauritsen 2025 gamma-ray tracking angular distributions, gamma-ray angular correlations distributions linear polarization tracking arrays]
created: 2026-07-09
updated: 2026-10-16
status: ai-draft
review_status: human-reviewed
source_type: method-review-article
reading_depth: deep-read
title_original: "gamma-ray angular correlations, distributions and linear polarization in tracking arrays"
authors: [T. Lauritsen, A. Korichi, C. M. Campbell, M. P. Carpenter, P. A. Copp, J. P. Greene, R. V. F. Janssens, T. L. Khoo, F. G. Kondev, C. Mueller-Gatermann, S. Nandi, W. Reviol, G. Savard, M. Siciliano, D. Seweryniak, S. Zhu]
journal: European Physical Journal A
year: 2025
volume: 61
pages: 76
doi: 10.1140/epja/s10050-025-01533-5
language: en
canonical_source: doi:10.1140/epja/s10050-025-01533-5
citation_key: "lauritsen_2025_$$gamma$$ray"
raw_file: "raw/papers/2025_Lauritsen et al_$$gamma $$-ray angular correlations, distributions and linear polarization in tracking arrays.pdf"
raw_sha256: 5EE6A654905BE64113229D6F10567308E3995580906527AF896EB9B92E478AE0
nuclei: [152dy]
reactions: ["108Pd(48Ca,4n)152Dy"]
observables: [angular-distribution-coefficient, attenuation-coefficient, multipole-mixing-ratio, linear-polarization-asymmetry]
methods: [angular-correlation, angular-distribution, dco-ratio, linear-polarization-asymmetry, tracking-array]
tags: [tracking-array, angular-correlation, angular-distribution, linear-polarization, sigma-over-i, pado-support]
---

# Lauritsen et al. (2025): Gamma Angular Formalism in Tracking Arrays

## Bibliographic Record

T. Lauritsen et al., *European Physical Journal A* **61**, 76 (2025), DOI `10.1140/epja/s10050-025-01533-5`. The title, author list, journal, year and DOI match citation key `lauritsen_2025_$$gamma$$ray`.

## Scope and Reading Depth

Full PDF text layer was read for article pages 1--25. Key checks include the Abstract, Introduction, Secs.2--6, Eqs.1--21, Eqs.28--41, Figs.6--10, Figs.21--22, and Appendix B. The focus for this Wiki ingest is the formula chain connecting angular distributions, attenuation/alignment coefficients, Gaussian `Pm(J)` and `sigma/J`, plus the tracking-array response-function and linear-polarization boundary.

This is a `method-review-ingest + project-ingest` source. It is not an experiment-specific validation of the user's P-ADO code, but it provides the modern notation and tracking-array caveats needed for the sigma-over-I project.

## Summary

Lauritsen et al. review and adapt classical gamma-ray angular-correlation, angular-distribution and linear-polarization methods for gamma-ray tracking arrays such as GRETINA and AGATA. Tracking arrays provide continuous-angle information and high position resolution, so detector solid-angle attenuation can often be close to unity, but angular-distribution extraction becomes non-trivial because tracked data have complex energy- and angle-dependent response.

For the current project, the most important section is Sec.3.1: the angular-distribution formula explicitly separates transition-dependent `Ak`, nuclear alignment/deorientation attenuation `alpha_k`, Gaussian magnetic-substate population `Pm(J)`, and the normalized width `sigma/J`. Sec.5 adds that linear-polarization and DCO information can resolve ambiguities left by angular distributions alone.

## Experimental or Method Setup

- Main method scope: source angular correlations, in-beam angular distributions, DCO from oriented nuclei, and linear polarization in tracking arrays.
- Tracking-array boundary: high position resolution makes conventional detector solid-angle attenuation coefficients often close to unity, but incomplete tracking can create energy-dependent halos.
- In-beam example: `108Pd(48Ca[191 MeV],4n)152Dy` with GRETINA, 47 crystals, `v/c=0.027`; used to demonstrate angular-distribution, DCO and linear-polarization extraction.
- Source response data: `152Eu`, `207Bi`, `60Co`, `137Cs`, `88Y`, `243Am`, `226Ra` and `57Co` are used to construct angular-distribution response matrices or test methods.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| L25-1 | 本文目标是把经典 gamma angular correlations、angular distributions 和 linear polarization 技术统一命名、适配到 tracking arrays，并引入 tracking-array response-function 生成方法。 | author-interpretation | direct | Abstract; p.2, Introduction; p.19, Summary | false |
| L25-2 | tracking arrays 可由 first interaction points 给出高精度 gamma 方向，因此通常的 detector solid-angle attenuation coefficients 可一般设为 unity；但 incomplete decomposition/tracking 可产生轻微 energy-dependent halo。 | method-boundary | direct | p.2, Introduction | false |
| L25-3 | in-beam fusion-evaporation 产生的核通常相对 beam axis aligned；若 `m` 与 `-m` population 相等则是 aligned，若该对称性破缺则为 polarized，若所有 `m` substates 等占据则 unoriented。 | method-formalism | direct | p.2, Introduction | false |
| L25-4 | source angular correlation 公式 `omega(theta)=a0+alpha2 a2 P2(cos theta)+alpha4 a4 P4(cos theta)+...` 适用于 initial state random `m` distribution；`alpha_k` 在这里是 detector solid-angle attenuation，tracking arrays 中接近 unity。 | method-formalism | direct | pp.3--4, Sec.2.1, Eqs.1--5 | false |
| L25-5 | in-beam angular distribution 写为 `omega(theta)=A0+alpha2 A2 P2(cos theta)+alpha4 A4 P4(cos theta)+...`；这里的 `alpha_k` 描述 emitting state 的 actual alignment/deorientation，必须与 detector solid-angle attenuation 区分。 | method-formalism | direct | p.6, Sec.3.1, Eq.6 and following text | false |
| L25-6 | `Ak=alpha_k Amax_k`，而 `Amax_k` 由 spin sequence、multipolarities 和 mixing ratio `delta` 决定；若 `delta` 非零，通常改写为 `A0(1+alpha2 A2 P2+alpha4 A4 P4+...)` 并报告 `A2/A0`、`A4/A0`。 | method-formalism | direct | pp.6--7, Sec.3.1, Eqs.7--17 | false |
| L25-7 | attenuation coefficient `alpha_k(J)` 由 magnetic-substate distribution `Pm(J)` 加权求和；`Pm(J)` 通常取 Gaussian 形式，并以相对 beam axis 的 `sigma/J` 表征，`sigma/J=0` 对应 full alignment。 | method-formalism | direct | p.6, Sec.3.1, Eqs.12--14 | false |
| L25-8 | 作者说明 Gaussian `Pm(J)`/`sigma/J` 对 fusion-evaporation 反应通常适用，但 fragmentation 等反应可能需要显式给出 `Pm(J)`；实际 fusion-evaporation 中粒子蒸发导致 `sigma/J` 非零。 | method-boundary | direct | p.6, Sec.3.1, text around Eqs.13--15 | false |
| L25-9 | 对 rotational band，若假定 transitions 为 stretched E2，可通过寻找能再现实验 `A2` 和 `A4` 的值来确定 `sigma/J`；fast-moving nuclei 还需 Lorentz transformation。 | method-formalism | direct | p.7, Sec.3.1, Eqs.18--19 | false |
| L25-10 | tracking-array in-beam angular distributions 需要构建 absence-of-angular-distribution-effects 的 response function；作者提出用多个 radioactive-source polar-angle spectra 建 response matrix，再与同能量 in-beam spectrum 相除。 | method-formalism | direct | pp.7--8, Sec.3.2, Figs.6--7 | false |
| L25-11 | `152Dy` examples show that response-function extraction still has systematic fluctuations: 991-keV line fit gives `A2=+0.251(2)`, `A4=-0.046(3)`; 781-keV line gives `A2=-0.210(3)`; 432-keV line with `sigma/J=0.3` and `delta=0.7` illustrates mixed character. | observed-fact | direct | pp.8--9, Figs.8--10 | false |
| L25-12 | angular distribution alone cannot decide whether the `152Dy` 432-keV line is mixed `M1/E2`, `E1/M2`, or possibly `E2`; the authors use DCO and linear-polarization measurements to clarify the nature. | experimental-criterion | direct | p.9, Sec.3.2; pp.12 and 18, Figs.14 and 22 | false |
| L25-13 | DCO from oriented nuclei uses a more general formula with an orientation parameter connected to the angular-distribution formalism; for tracking arrays, continuous-angle DCO response cubes and event mixing are used to preserve phase space. | method-formalism | direct | pp.9--12, Sec.4.1, Eqs.20--21, Fig.12 | false |
| L25-14 | 对 fusion-evaporation 的 linear polarization，本文把角分布项扩展为 `Pk(cos theta) -> Pk(cos theta) + (±)_{L'} Kk(LL') cos(2psi) Pk^(2)(cos theta)`；`Kk(LL')` 由 Eq.33 定义，`(±)_{L'}` 类似 `P_+` 的电/磁符号约定，`E(L')` 取正而 `M(L')` 取负。 | method-formalism | direct | pp.13--16, Secs.5.1--5.3, Eqs.31--41 | false |
| L25-15 | In the `152Dy` in-beam example, linear polarization resolves the 432-keV ambiguity: calculations with `sigma/J=0.3` and `delta=0.7` leave only the `E1/M2` mixed solution consistent with the data. | observed-fact | direct | p.18, Sec.5.5, Fig.22 | false |
| L25-16 | Appendix B.1 reports the `152Dy` in-beam dataset: `108Pd(48Ca[191 MeV],4n)152Dy` at ATLAS (experiment 1909), GRETINA with 47 crystals, a `108Pd` target of `0.789 mg/cm2`, a `24 mg/cm2` Pb catcher about 35 cm downstream, recoil `v/c=0.027`, and `1.55e9` good gamma rays with `FOM<0.8`. | observed-fact | direct | Appendix B.1, p.20 | false |
| L25-17 | 出版商正文/HTML与Crossref均为EPJ A61,article76(2025)，protected Bib亦为76；本页旧81为metadata错误已修。本地raw为25页带EPJ manuscript/日期占位符的稿件版，另核publisher24页版本；两者不是独立采集。 | source-identity-and-version-audit | direct | publisher PDF1 title/header; publisher HTML citation_firstpage76; Crossref DOI record | true |
| L25-18 | few-mm first-interaction定位使usual finite-solid-angle attenuation可近似unity，但原文仍保留energy-dependent halo及PSA/tracking/tiling响应。近unity不等于角能量效率平坦，source角谱相除也不自动反卷积angular migration。 | response-object-and-applicability-boundary | direct-and-derived | publisher PDF2 Introduction; publisher PDF7 Sec3.2 | true |
| L25-19 | Fig6以每条源线的renormalized polar-angle counts放入一个energybin；Fig7在能量间插值、端外线性外推。作者还构造/调整variance matrix，明确误差不只是缩放后的sqrt(counts)；不据图补出实际算法/完整Cov或全部migration kernel。 | source-response-construction-and-replay-boundary | direct-and-derived | publisher PDF7 Figs6–7/Sec3.2; publisher PDF8 opening paragraph | true |
| L25-20 | Fig8的991线fit A2=.251(2)/A4=−.046(3)，Fig9的781线A2=−.210(3)，Fig10的432线A2=.363(2)/A4=.123(3)；caption χ²分别35/21/142。正文明确fit errors未完全包含systematic fluctuations，故不把括号误差单独当totalerror或jointCI，不凭caption补ndf/reducedχ²。 | fitted-observables-and-author-error-boundary | direct-and-derived | publisher PDF8 Figs8–9 and text; publisher PDF9 Fig10 | true |
| L25-21 | 本例角覆盖约70–175°、3°bin；432上方stoppedline使其只用接近/高于90°数据。Sec3.1明确额外符合选择在非4π阵列可改m-population，Eqs6–19可能需修改；source-response除法不认证相同selection/alignment。 | selection-support-and-population-boundary | direct-and-derived | publisher PDF7 paragraph before Sec3.2; publisher PDF8 Sec3.2; publisher PDF9 Fig10 | true |
| L25-22 | Eq18将theta定义为CM、theta_lab为lab，而紧接Eq19分母仍字面cos(theta)，HTML/两版PDF一致。本任务从Eq18独立推得光子数Jacobian应为(1−beta²)/(1−beta*x)²、x=cos(theta_lab)；若Eq19字面用CM变量会有条件差异。未取得作者code，保留原标记，不称官方erratum或已知实际fit错误。 | printed-frame-marker-and-independent-derivation | direct-and-derived | publisher PDF6 Eqs18–19; publisher HTML Equ18/Equ19; manuscript PDF7 Eqs18–19 | true |
| L25-23 | AppB1是2022 exp1909、47crystal的152Dy数据，含17+60ns isomer下方gamma trigger；B2说部分源数据阵列配置不同。publisher Data/Code Availability仅给reasonable request，没有本任务可下载的events/response/Cov/code；稿件/期刊与其图表不重复计实验。 | acquisition-lineage-and-data-readiness | direct-and-derived | publisher PDF20 Appendix B1–B2; publisher PDF19 Data/Code Availability | true |
| L25-24 | publisherPDF/HTML Eq13字面为exp[−m²/(2σ)]，Eq14字面为1−3m²/S及1−10m²/S+35m4/(3S²)，S=J(J+1)。Ref39是Morinaga/Yamazaki1976专著，非1967表；未取该书原近似上下文/作者code，保留字面与两种参数合同。 | literal-formula-and-cited-source-scope | direct | publisher PDF6 Eqs13–14; publisher HTML Equ13/Equ14; References39 | true |
| L25-25 | 以Eq10/12和YA67归一张量作exact finite-J解释时，uniform population的true k>0 tensor为0，而Eq14字面第四阶平均为−7/(9S)。J23为−7/4968，J13/2为−28/1755；半整数complete-alignment参考也不为字面两权重同时1。本任务独立CG/多项式核验，不指认作者实际程序。 | our-finite-J-limit-audit | derived | publisher PDF6 Eqs10/12/14; YA67 PDF1 Eq1 and PDF2 Eqs6/10 | true |
| L25-26 | 字面第四阶可写A*a4+B*a2−7/(9S)，a是相同mref归一的exact权重。它在finiteJ含低rank分量，未换基不能直接照pure-U4传播；自选2→2未观测E2的uniform例给原/child均−7/54，而pureU4乘法给−1/27。 | our-basis-and-feeding-consistency-control | derived | publisher PDF6 Eqs14–16; YA67 PDF3 Eqs12–15 | true |
| L25-27 | 对整数J，本任务证明字面与exact第四阶逐m差为35m²(2m²−S)/[3S²(S−2)]，绝对值≤35/[3(S−2)]，故可视为large-J主项而非exact finite-J恒等式。该数学极限不证明实际σ/δ偏差可忽略或作者明确作此近似。 | our-large-J-scope-boundary | derived | publisher PDF6 Eq14; YA67 PDF1 Eq1 | true |
| L25-28 | Gaussian width合同W用exp[−m²/(2s²)]，literal variance合同V用exp[−m²/(2v)]，仅v=s²时同布居。两者同标sigma/J=.3的示例会不同；J23时literal v/J=.3等效width/J≈.114208，不是.3。未重拟Fig8/恢复actualσ；旧flags/humanreview不扩展。 | our-parameter-contract-not-fit | derived | publisher PDF6 Eq13 and text sigma/J; YA67 PDF2 Eq11 | true |
| L25-29 | AppendixA1 Eq42给出P2/P4；本任务令z=m/sqrt(S)后，Eq14的q2/q4恰等于P2(z)/P2(0)、P4(z)/P4(0)。这支持一种经典投影的独立解释；有限量子迹与连续各向同性投影的矩不同，不能据形式匹配归给未读Ref39或作者actualcode。 | our-analytical-reconstruction-with-direct-polynomial-input | direct-and-derived | publisher PDF19 AppendixA1 Eq42; publisher PDF6 Eq14 | true |

## Nuclear Structure Information

The paper includes real `152Dy` experimental information as well as method demonstrations. This ingest now records a `152Dy` nucleus page and the ATLAS/GRETINA experiment page, while keeping the current structural use limited to the transitions and observables explicitly discussed in this source.

## Authors' Interpretation

- Tracking arrays allow high-precision angular correlations and linear polarization, but angular distributions require careful response-function treatment.
- Modern tracking-array analyses benefit from continuous-angle methods and event-mixing/source-response normalization.
- Linear polarization, DCO and angular distribution should be used together when angular-distribution curvature alone leaves multipolarity or parity ambiguous.

## Competing Interpretations and Limitations

- The paper is a method review/formalism article with examples, not a validation of one universal `sigma/J` or `sigma/I` value.
- `alpha_k` is notation-dependent: in source angular correlations it denotes detector solid-angle attenuation; in in-beam angular distributions it denotes nuclear alignment/deorientation attenuation. This boundary is essential for project symbol mapping.
- Tracking arrays often simplify finite-solid-angle attenuation, but response halos, sparse detector population, clustering holes and source-response construction still create systematic effects.

## Project Relation

For [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]], this source supplies the requested modern formula chain: `delta` enters `Amax_k`; the in-beam angular distribution multiplies transition terms by alignment/deorientation attenuation `alpha_k`; `alpha_k(J)` can be calculated from `Pm(J)`; and `Pm(J)` is commonly parameterized by Gaussian `sigma/J`. It directly supports wording that `sigma/I` or `sigma/J` is a population/alignment assumption and should not be hidden as a universal constant in P-ADO mixing-ratio extraction.

## Extracted Pages

- Concepts: [[sigma-over-i]], [[magnetic-substate-population]], [[spin-alignment]], [[deorientation]]
- Methods: [[angular-distribution]], [[angular-correlation]], [[dco-ratio]], [[linear-polarization-asymmetry]], [[tracking-array]]
- Observables: [[attenuation-coefficient]], [[angular-distribution-coefficient]], [[multipole-mixing-ratio]]
- Nuclei / experiments: [[152dy]], [[atlas-gretina-152dy-ca48-191mev]]
- Projects: [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]

## Personal Notes

Review note: L25-5 to L25-9 and L25-14/L25-15 were user-reviewed on 2026-07-09. L25-2 and L25-4 remain important context because `alpha_k` changes meaning between detector solid-angle attenuation and nuclear alignment/deorientation attenuation in different sections.

## DAY14 tracking响应与版本核验

2026-10-16本次为Day15无学分预习。来源前priming另存run receipt；读取本地25页稿件的Intro/Sec3/Summary/AppB相关段，并取得[出版商24页PDF](https://link.springer.com/content/pdf/10.1140/epja/s10050-025-01533-5.pdf)，对照publisher PDF1–3、6–9、18–20的相关段、Figures6–10、Eqs18/19和HTML公式/availability；没有重新认证publisher所有24页公式、DCO/偏振代码或全表。原Scope的25页全文记录指既有raw作者稿，不能误读为publisher版页数。

DOI[10.1140/epja/s10050-025-01533-5](https://doi.org/10.1140/epja/s10050-025-01533-5)的正式article number为76，2025-04-10发表；publisher PDF首页、HTML citation_firstpage及[Crossref](https://api.crossref.org/works/10.1140/epja/s10050-025-01533-5)与只读Bib一致，故修正原81。旧raw的2372132bytes/SHA256`5ee6a654905be64113229d6f10567308e3995580906527af896eb9b92e478ae0`保持。新publisher PDF为2248094bytes/SHA256`0d89c27c0a354b1b215f8a9196142f76bd873fe9335d64ca6318f0f303422099`，仅下载到Wiki内tmp核验，不替换raw、不进Git；正式URL/页与图式为持久locator。

作者在publisher PDF7–8明确：Fig6/7是以源线能量索引的归一角谱与插值/外推图；它不是已公布的完整P(Ereco,thetareco|Etrue,thetatrue)迁移核。source response、variance图、角拟合Cov和核alignment各有对象。源码未得，原文有variance调整说明，不推定作者简单线性插variance或忽略归一相关。Fig8/9/10 quotedfit errors与systematic fluctuations也不能混作已完整误差预算。

本任务的[[angular-distribution]]“Tracking响应：源到在束的measure、能量与Cov合同”由Eq18独立推导dOmega_CM/dOmega_lab，再对source beta=.027、991-keV能量和声明collinear固定速度作条件表；另用明确自选计数/归一/插值验证一阶Cov合同。29checks只是本任务数学/输入检查，非原GRETINA response重放或新实测σ/δ。Eq19字面CM代入给出的归一/0.146%差别是条件反例，不能据此解释原systematics或指认作者程序错误。

Agent self-audit：metadata81→76已由直接publisher与Crossref/Bib处置；新L25-17–23 true，旧L25-1–16全部flag和页面既有人审事件保持，不扩展为新内容human-reviewed。实际responseaxis/单源归一常数/插值算法、原角fit Cov、trigger/selection与moving-source传递未恢复，scientific P1/readiness保留。没有向作者发送数据/code请求。Decision: **revises** article号和版本误读；**supports** 独立source response校准；**limits** near-unity几何、漂亮曲线或quotedfit误差代替完整响应/不确定度。

## DAY14 finite-J attenuation与Gaussian参数合同

本段核publisher PDF6 Eqs10、12–16及HTML同号公式，不改原件。Ref39实际为H.Morinaga/T.Yamazaki, *In-Beam Gamma-Ray Spectroscopy* (North-Holland,1976)，本轮raw文件名检索无match，未读该书对应段，不能把本任务的large-J解释写成该书原话。[[yamazaki-1967-aligned-angular-coefficients]] YA67-13另核Eq1/6/10的精确张量/参考与Eq11明确的2σ²；两来源提供定义对照，不形成新独立实验。

58-check独立CG finite-sum与多项式逐m比较：Eq14字面第四阶在uniform布居下不是0，并可精确分解为rank4/rank2/constant；半整数mref=.5的归一也需显式处理。证明整数J下与精确权重的差有O(1/S)一致界，所以“与large-J主项相容”和“finite-J exact tensor”须分开。不能未换基就把字面组合当pureU4作用的张量。

[[angular-distribution]]“Finite-J张量权重与Gaussian参数：先做极限再转移”保存公式、source/J23/13/2的条件数值、uniform与feeding反例。相同sigma/J数值在width/variance合同下不同，但没有原code/Ref39近似说明时，不倒推作者实际用了哪个合同、补σ/δ、解释原Fig8systematics或更改Zobel表列。L25-24–28 true，旧1–23原文/flags和legacyhumanreview保持；属于L2公式自审，非officialerratum或experimental refit。Decision: **limits** 直接抄式为精确finite-J定义；**supports** 定义/参考/参数重映射和极限检查。

## Ref39检索与经典权重的解释边界

2026-10-16本轮沿[本刊Ref39](https://link.springer.com/article/10.1140/epja/s10050-025-01533-5#ref-CR39)精确题名/作者检索：Crossref宽查询含无关报告/会议文及Gelletly1977同题期刊条目，均不能当作1976原书；book类型/作者过滤无结果，GoogleBooks/OpenLibrary连接失败，ScienceDirect题名检索HTTP403。原raw文件名/只读Bib亦未命中。只是这些选定路线未取得书中对应段，不证明原书全球不可得/无机构权限；未猜ISBN/书DOI、未绕过验证、未新建metadata-only booksource。

可执行路线转为明确的L2独立解释。视觉/文本同号的publisher PDF19 Eq42提供Legendre输入；用经典固定长度sqrt(S)投影z，字面q2/q4与P2/P4参考归一形式相同。另以量子m离散等占据的迹矩正交化四次式，得到精确T4的+25m²−6S修正。[[angular-distribution]]“经典方向权重与量子迹：四阶修正从何而来”保存推导及22项符号恒等核验；这不是声称Ref39/作者程序采用了本推导，也不恢复实验σ/δ或真实三维角动量分布。

新L25-29 true，旧1–28和legacy人审保持。Decision: **supports** 用连续/离散测度解释公式形状并从定义重建低rank正交；**limits** 同题metadata、搜索片段或公式相像充当原书/actualcode证据。原书对应近似声明仍待直接原文，网络边界没有结束整个DAY14窗口。


## DAY16必要companion：Q的观测与参考角色

本session仅定向重读本地manuscript Secs.5.1–5.5、Eqs.(27)–(38)和source-calibration Table2/相关图；不冒称重新全文读25页。上方所有旧文本/1–29 flags及既有人审prefix逐字节保留，新增自审不由旧review背书。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| L25-30 | 本文Q由实测ξ曲线/其calculated ideal曲线的amplitude ratio定义；60Co1333在1173 coincidence下measured+.016(.002)、calculated+.048得Q=.33(.04)，Table2另报1442 .31(.05)。这是条件γγ polarizing-reference，不等同Morse无γγ条件的source singles或L26 beam-defined reaction plane；同符号Q的迁移还需gates/response/归一合同。 | calibration-observable-and-reference-role | direct-and-boundary | manuscript printed13对Q的定义；printed16–18 Sec.5.4/Fig.17/Table2；Eq.(34) | true |

Secs.5.1/5.2的P±明取Electric +、Magnetic −，与混合跃迁还需higher-multipole/K系数相位一起用。此处Q是自己folded ideal calculation的经验缩放，不把它未经转换当另一篇的mean KN Sigma；.33与Morse .196不是自动可替换常数。新增与[[longfellow-2026-gretina-energy-ordering-polarization]] L26-22/24及[[morse-2022-gretina-polarization-sensitivity]] M22-5构成定义对照，不增加独立source event数量。
