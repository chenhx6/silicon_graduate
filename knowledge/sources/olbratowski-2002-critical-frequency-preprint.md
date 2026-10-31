---
type: source
title: "Olbratowski2002早期稿：核手征均匀转动的临界频率"
aliases: [Olbratowski critical frequency early manuscript, nucl-th/0211075v1]
created: 2026-10-26
updated: 2026-10-26
status: ai-draft
review_status: unreviewed
source_type: theoretical-preprint
reading_depth: deep-read
title_original: "Critical frequency in nuclear chiral rotation"
authors: [P. Olbratowski, J. Dobaczewski, J. Dudek]
year: 2002
arxiv: nucl-th/0211075v1
doi:
related_published_doi: 10.1103/PhysRevLett.93.052501
canonical_source: https://arxiv.org/abs/nucl-th/0211075v1
citation_key: ""
raw_file: raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/olbratowski-2002-critical-frequency-arxiv-v1.pdf
raw_sha256: 3cc0000405bb8360d0b7112fbd6d6a3811546091dee182da2b44be071c8bbffb
raw_storage_status: archived-2026-10-28
actual_body_file: tmp/day24-critical-tac-007/arxiv-0211075v1.response
nuclei: [132la]
models: [tilted-axis-cranking, skyrme-hartree-fock, frozen-gyroscope-model]
observables: [rotational-frequency, energy-splitting]
methods: [cranking, constrained-variation]
tags: [chirality, critical-frequency, planar-aplanar, model-validity]
---

# 临界频率：给定gyro与惯量的均匀转动分岔

## Bibliographic Record

实际读本为2002-11-25的三作者arXiv:nucl-th/0211075v1，4页。官方PDF URL `https://arxiv.org/pdf/nucl-th/0211075v1` 本轮HTTP200、application/pdf、252547bytes、有效PDF签名；2026-10-28 已将同一字节流归档到 `raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/olbratowski-2002-critical-frequency-arxiv-v1.pdf`，SHA见frontmatter。

Crossref及作者机构网页把这一早期稿关联到*Phys. Rev. Lett.* **93**, 052501 (2004)，DOI10.1103/PhysRevLett.93.052501；2004元数据还列W. Płóciennik为第四作者。实际作者HTML仍是三作者稿，APS正式body未取得。另查官方arXiv历史仅有v1；本轮无版本号current PDF与已读v1逐字节相同，仍为三作者稿，没有因此取得2004正文。不能将早期稿的公式/数值/字面问题无条件归给未读2004 VoR；本source的科学locator一律属于2002 v1。

## Scope and Reading Depth

独立worker读4页全文文本/视觉、全部Figs1–6/Eqs1–7；leader另读四页主线文本并fresh视觉全部四页，抽核Eq1/4–7、参数、Fig6和方法脚注。没有重跑HFODD、原HF continuation或particle-core量子谱；条件代数检查不是实验认证。原PDF/HTML/metadata回执留本run workers/critical-tac-007；归档副本与实际读本逐字节一致。

## Summary

稿件在132La固定粒子/空穴组态的Skyrme-HF上找到planar与aplanar自洽旋转解，再用固定短/长轴gyro加常惯量的经典模型解释临界频率。该临界是body-frame角速度恒定的均匀转动解起始；它不量子化左右隧穿、不给有限核实验双带的普适临界自旋。原稿保留HF起始高于实验候选频率的张力和planar/axial-l替代。

## Experimental or Theoretical Setup

目标组态为132La的πh11/2粒子与νh11/2空穴，约β=.25、γ45°。先做非自洽s/l方向single-particle response探针，再由自洽轴向推转提取s_s=5.43ℏ、s_l=5.00ℏ和𝒥_s/𝒥_m/𝒥_l=8.5/31/20ℏ²MeV⁻¹。小的odd-nucleon横向响应δ𝒥已包含在提取惯量中，不能再次叠加。

原稿PDF4 Ref6说明HFODD v2.00k、14个spherical oscillator shells、SKM*、无pairing、time-odd fields关闭、仅保parity。这里的自洽是该选定近似内的自洽，不表示全部相关项都计算。原稿Ref10还提醒这些惯量不必等于同形状massive rigid body的惯量。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| OL02-D24-001 | 固定s/l gyro与常对角惯量下，I=𝒥ω+s；只寻找body-frame ω恒定的均匀转动，要求ω×I=0。受限Routhian极值给ω_m(μ−𝒥_m)=0；μ=𝒥_m的aplanar分支固定ω_s/ω_l并需ω≥ωcrit。等号时m分量0，与planar分支相接；两非零handed signs要求严格大于。 | direct-model-derivation | direct-version-specific-original | PDF2 uniformrotationparagraph/Eqs2–4; PDF3 Eqs6–7 | true |
| OL02-D24-002 | 原参数代Eq7得ℏωcrit≈.514639MeV；Eq5另给新planar分支阈值≈1.282267MeV，两者不同。原稿HF自洽搜索称从ℏω=.6MeV出现chiral解，非实验测得阈值或量子双带劈裂；经典Icrit≈15.9538ℏ是连续矢量长度，非实验量子spin。 | source-parameter-conditional-arithmetic | direct-input-plus-task-calculation | PDF2 preFig2parameterparagraph; PDF3 Eqs5/7/HFparagraph | true |
| OL02-D24-003 | 132La粒子/空穴、约β.25/γ45°、SKM*、无pairing、14shells、time-odd关闭及已含δ𝒥限定结果；非自洽单粒子探针与自洽轴向/倾斜分支是不同计算步骤。 | model-input-and-numerical-scope | direct-original | PDF1 configuration/Fig1; PDF2 Eq1/axialparagraph; PDF4 Ref6 | true |
| OL02-D24-004 | 稿件明确HF .6MeV起始高于实验候选带出现频率；Fig6讨论下带planar、上带axial-l的暂定替代，也可再现约350keV能量分离。因此一个aplanar均场分岔或相近能谱不排他认证实验partner身份，不能数值迁移到128Cs/135Nd。 | author-counterinterpretation-and-boundary | direct-original-and-bounded-inference | PDF3 lastparagraph; PDF4 Fig6/discussion/conclusion | true |
| OL02-D24-005 | 已读2002v1三作者与2004四作者记录分开。v1 Eq1后long/short prose顺序与明确公式/后文gyro定义相反；PDF4称decrease惯量差又使ωcrit降低，与Eq7在固定非零s下的推论不同。保字面与条件，未判未读VoR错误，也不以这段文字建立γ→ωcrit普适单调关系。 | version-and-literal-ambiguity | direct-original-and-task-algebra-boundary | PDF1 authorblock; PDF2 postEq1prose; PDF3 last/PDF4 firstparagraphs | true |

| OL02-D24-006 | Eq3/4的stationarity给I=μω，μ有惯量单位且μ=𝒥m仅属aplanar分支。Fig6纵轴为E−I²/(2𝒥m)，不是Routhian；源经典chiral分支该量恒为−½[ss²/(𝒥m−𝒥s)+sl²/(𝒥m−𝒥l)]≈−1.791584MeV。局部约束曲率核验不等完整RPA动力学谱或量子隧穿。 | source-quantity-identity-and-bounded-algebra | direct-original-plus-conditional-reconstruction | PDF2 Eqs2–4; PDF4 Fig6axis/caption | true |
| OL02-D24-007 | 同源固定模型的两种约束需分开：给定ω最小化R，给定I最小化H。后者低I的yrast先走D再A再aplanar，与Fig4正文相符；负μ允许ω/I反向。两种同球面能差有精确二次式全局证书，阈值零切向曲率仍有正quartic代价；这些为本任务代数，不是作者HF/实际RPA/量子谱复现。 | source-grounded-conditional-global-variation | direct-input-plus-task-derivation | PDF2 Eqs2–4; PDF3 Fig4/yrastparagraph; task gyro-stability-010 | true |

## Analytical Reconstruction

对给定源模型，约束Routhian导数为

$$\omega_s={s_s\over\mu-\mathcal J_s},\qquad
\omega_l={s_l\over\mu-\mathcal J_l},\qquad
\omega_m(\mu-\mathcal J_m)=0.$$

这里I=μω，μ的单位是ℏ²/MeV；stationarity先保证共线，不能把所有planar根也强定μ=𝒥_m或正平行。于是aplanar分支取μ=𝒥_m，

$$\omega_c=\sqrt{\left({s_s\over\mathcal J_m-\mathcal J_s}\right)^2+
\left({s_l\over\mathcal J_m-\mathcal J_l}\right)^2},\qquad
\omega_m=\pm\sqrt{\omega^2-\omega_c^2}.$$

源单位为s用ℏ、𝒥用ℏ²/MeV，ω用MeV/ℏ。代入s_s=5.43、s_l=5.00、三𝒥=8.5/31/20得到ℏω_s=.241333、ℏω_l=.454545、ℏω_c=.514639MeV。atℏω=.50此模型无real m分量；at.60模型有ℏω_m≈.308459MeV、|I|=18.6ℏ。它不是实际HF解/误差或实验spin映射。

当𝒥_m最大时，源图的yrast极值在临界后沿chiral分支；其受限Routhian在非退化aplanar点的局部曲率可检查。这个局部模型判断不等完整动力学稳定性、RPA谱或量子拓扑。惯量差退化、gyro变小/改变或形状变化时需重新推导，不能拿公式奇点或zero numerator给实核硬门。

Fig6绘制的是扣除刚体参考后的E−I²/(2𝒥_m)，不是Routhian E−ω·I。把上述aplanar分支代入E=½Σ𝒥_kω_k²及I=𝒥_mω，得到

$$E-{I^2\over2\mathcal J_m}=-{1\over2}\left[{s_s^2\over\mathcal J_m-\mathcal J_s}+{s_l^2\over\mathcal J_m-\mathcal J_l}\right]\simeq-1.791584\;\mathrm{MeV}.$$

这解释源图经典水平线的量身份；在不同核或量子谱中不能直接沿用该常数。独立review以给定ω的Routhian和给定I的Hamiltonian两条约束变分路线核局部曲率，25项有界控制通过；这是本源声明模型的代数/局部检验，不认证实际HF收敛、RPA零模或实验spin。

## Competing Interpretations and Limitations

实验能谱对应可能包含平面/轴向分支、configuration及形状响应；该稿自己的planar/axial-l替代已保留。与[[frauendorf-meng-1997-tilted-rotation-chirality]]、[[almehed-2011-chiral-vibrations-a135]]和[[qi-2009-135nd-particle-rotor-chirality]]比较时，应分开经典/均场分岔、谐振soft模、有限核隧穿和实际实验partner。本文没有量子化±ω_m的耦合，不能由其degenerate均场直接导出实验精确简并。

原Fig4正文低I先D再A再chiral，不是所有I都选fixedω最低R。条件全局证明、负μ/λ0的chart边界及退化极限保存在[[135nd-chiral-partner-resolved-evidence-map]]的“固定ω和固定I的全局分支”；脚本和72项有界数值控制为本run gyro-stability-010。该固定参数问题已局部饱和，增加小数位不能补实际HF continuation/质量或RPA动力学。

## Knowledge Impact and Learning Decision

`supports` [[tilted-axis-cranking]]及[[nuclear-chirality]]的有条件均匀转动onset；`limits`最低自旋/频率的跨核普适化及只用能量识别。用于[[135nd-chiral-partner-resolved-evidence-map]]的理论域对照；这是新直接方法原稿，不是135Nd新实验，不能填其g/branch/normalizer。

## Agent self-audit triage

P0: none identified（版本/字面歧义已隔离）。P1：Eq7/参数/替代解释与方法输入已双读原件；v1/VoR及局部curvature/实际HF/量子谱保持分层，全部新增needs_review:true。已完成 raw 归档；按原 URL/version/hash 可恢复，仍不能将 v1 当作未读的 2004 VoR。P2：书目关联已核、citation key仍空，不改Bib。

## Extracted Pages

归档原件位于 frontmatter 的 `raw_file`；本轮4页全文与 Figs.1–6/Eqs.1–7 已读。PDF2 参数/Eqs.2–4、PDF3 Eqs.5–7 和 PDF4 Fig.6/Ref.6 是本页原子主张的定位入口，页码属于2002 v1，不能作2004 VoR页码。

## Archive Recovery History

2026-10-28：从 `tmp/day24-critical-tac-007/arxiv-0211075v1.response` 恢复同一 PDF 字节流至 `raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/olbratowski-2002-critical-frequency-arxiv-v1.pdf`。复制前目标路径不存在；归档副本 `%PDF-1.4`、4 页、252547 bytes，SHA-256 `3cc0000405bb8360d0b7112fbd6d6a3811546091dee182da2b44be071c8bbffb`，与实际读本逐字节一致。此恢复只改变存储身份，不改变 source 的版本、locator、review flags 或 2004 VoR 未读边界。
