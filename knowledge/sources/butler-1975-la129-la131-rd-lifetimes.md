---
type: source
title: "Butler1975：129/131La recoil-distance寿命与三轴模型检验"
aliases: [Butler1975 triaxial light La, La129 La131 RD lifetimes]
created: 2026-10-27
updated: 2026-10-27
status: ai-draft
review_status: unreviewed
source_type: experimental-paper-with-model-comparison
reading_depth: deep-read
title_original: Triaxial shapes in light La nuclei
authors: [P. A. Butler, J. Meyer-ter-Vehn, D. Ward, H. Bertschat, P. Colombani, R. M. Diamond, F. S. Stephens]
year: 1975
journal: Physics Letters B
volume: 56
issue: 5
pages: 453–456
doi: 10.1016/0370-2693(75)90410-4
canonical_source: https://doi.org/10.1016/0370-2693(75)90410-4
citation_key: ""
raw_file: raw/papers/1975_Butler_TriaxialShapes_LightLa.pdf
raw_sha256: 231b6f427ac9bdd15688bf373959d2dff63dd7e694ee2dbb9b12cc0186ba8e0a
raw_storage_status: public-staging-not-archived
actual_body_file: tmp/day24-butler1975-la129-la131-lifetimes-071/attachment-object-response.pdf
nuclei: [129La, 131La, 130Ce, 128Ba, 130Ba, 132Ce, 107Cd]
methods: [recoil-distance, joint-feeding-lifetime-fit, electromagnetic-transition-probabilities]
models: [triaxial-rotor-plus-quasiparticle, rotation-aligned-coupling, strong-coupling, weak-coupling]
observables: [lifetime, B(E2), level-energy]
tags: [source-lineage, core-normalizer, feeding-response, triaxiality]
---

# 原寿命支持条件三轴比较，邻偶核仍是定标输入

## Bibliographic Record

P.A.Butler等，PLB56(5)(1975)453–456，DOI10.1016/0370-2693(75)90410-4；received11-April-1975、刊头26-May-1975。本篇是[[meyer-ter-vehn-1975-odd-a-unique-parity-comparison]] Ref29及其Table5 La强度的primary，后者转引不加另一份独立实验。

071 Crossref exact及首页/末页核身份，FULL XML实际MAIN attachment经Object API取得真4页、268368bytes与上述SHA。默认检查SI；小si1.gif为ALTIMG/符号，不冒补充数据，检索范围内未识别科学SI。原件暂tmp，raw未改；完整PDF/XML/OCR/页图不入公开manifest。

## Scope and Reading Depth

071读全部4页/Figs1–2/Table1/公式/脚注/参考，先PartII-primed recall非盲测；root074另读全部原文及四页fresh视觉，核两横轴、完整表和参数排印。未原读Refs3–7全部正文、未得原counts/逐distance峰面积、actual转换/拟合producer或fullCov，未重拟作者曲线。

## Summary

本文直接测129/131La最低15/2−、19/2−寿命，并另测130Ce参考态；通过邻偶核定标的B(E2)与single-j三轴芯模型比较，提供能谱以外的有用EM检验。sidefeeding和共同origin进入联合拟合，B转换缺逐支BR/ICC合同；模型γ和绝对尺度又取偶核数据，不能把所有图点当独立预测或将这些La寿命迁到133Ce。

## Experimental Setup and Response

LBL88inch cyclotron，129La用119Sn(14N,4n)67MeV、130Ce用118Sn(16O,4n)82MeV、131La用116Cd(19F,4n)72MeV。Sn自支撑.75mg/cm²，Cd富集.6mg/cm²蒸于.2mg/cm²Ni；Ni为靶backing，原文未因此给stopper材质。planar Ge在0°，由stopped/moving峰积分画Is/(Is+Im)对plunger setting。

Fig1的131La15/2→11/2用上方0–400μm尺度，其余曲线用下方0–100μm，不混横轴。最大flight400/1600ps仍有14% stopped，作者主要归直接sidefeeding到15/2，图已修该分量；不能把图作未校正纯指数或14%普适量。平均v由centroid shift并校Ge有限立体角，129La/130Ce/131La为.0087/.0103/.0105c；作者显式纳入velocity spread后无显著结果差，限其数据范围。

同时least-squares拟两低态decay curves，上馈近似两个或更多free寿命level，受23/2→19/2曲线形状及共同origin部分约束，另按强度降幅加其它feeding。τ、sidefeeding、zero可能相关，单误差不恢复jointCov；Fig1有23/2曲线用于feeding不等本篇已报其独立B。

## Key Results

新claims全needs_review:true；reported τ/B、model与本轮条件算术分别标。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BU75-D24-001 | 三反应/束靶、0°Ge和recoil-distance Is/(Is+Im)有明确实际输入；不是DSAM或无feeding DDCM。 | experimental-method-and-channel | direct-original | PDF1 setup/Fig1 | true |
| BU75-D24-002 | 131La大flight仍14% stopped，作者归sidefeeding且Fig1已校正；速度及有限Ge角校正、velocity-spread检验均具体实验范围内。 | actual-response-and-correction | direct-original | PDF1–2 Fig1 and velocity paragraphs | true |
| BU75-D24-003 | 两低态曲线jointfit，上馈≥2freeτlevel与commonorigin/23→19curve约束，未知Cov不能把各τ当独立指数。 | actual-fit-contract | direct-original | PDF2–3 fitting paragraphs | true |
| BU75-D24-004 | 新La四τ/B为129La130(6)/8.7(1.3)ps与.42(2)/.38(6)e²b²；131La55(2)/5.8(.6)ps与.34(2)/.33(3)，分别15/2→11/2和19/2→15/2。表头τ保原记号，不称数据库T列。 | measured-derived-lifetime-and-B | direct-original | PDF2 Table1 | true |
| BU75-D24-005 | 本文130Ce新τ211(9)ps与Ref4旧225(19)比较，且core B进入模型定标；它是有用新实验，不因同装置/作者就抹去，也不是全无共同systematics的独立校准票。 | actual-core-measurement-and-dependence | direct-original | PDF2 Table1; PDF3 comparison paragraph | true |
| BU75-D24-006 | La B缺逐branch BR/ICC表和actual转换程序，不能凭τ/Eγ默认qγ=1后称精确重现，更不反造ICC或实验错误。 | B-conversion-readiness-boundary | direct-original-scope | PDF1–3 method/Table1 | true |
| BU75-D24-007 | 邻core中央B的无权平均.33/.28可复PartII normalizer；未知共享误差不naive传播成其.05/.07，primary weak131行实际.30不改。 | normalizer-source-arithmetic | direct-original-plus-arithmetic | PDF2 Table1 | true |
| BU75-D24-008 | 尺度取core B、λ由Nilsson、Δ由mass、γ22/23由even能谱/systematics；模型不是全部observable independent prediction。 | explicit-model-calibration | direct-original | PDF2 Table1 footnotes; PDF3 final paragraphs | true |
| BU75-D24-009 | Table1脚注实印β/A^(2/3)=6.8/6.4，与Fig2/正文乘积βA^(2/3)不一致；保排印边界、不照除法造β，也不据此判全部计算错。 | literal-parameter-dictionary-conflict | direct-original | PDF2 footnotes; PDF3 Fig2caption; PDF4 text | true |
| BU75-D24-010 | Fig2归一B/[(5/16π)Q0²]的约5%稳定限b4–7和e1≤λ≤e2，是模型参数敏感性，不是实验CI/full理论误差；primary理论数没有±.02errorbars。 | normalization-and-error-scope | direct-original | PDF2 Table1; PDF3 Fig2caption | true |
| BU75-D24-011 | γ扫描35°附近15/2 states crossing解释B振荡，不是实测随spin crossing；高23/2/27/2 B曲线仍prediction，feeding曲线不当其reported B。 | model-coordinate-and-prediction-boundary | direct-original | PDF3 Fig2 and model discussion | true |
| BU75-D24-012 | weak higher/first约1.4/2须另假rotational/vibrational core，原文说core4→2精确数据欠缺；不排所有weak/soft模型。 | competing-model-domain | direct-original | PDF3 final paragraph | true |
| BU75-D24-013 | 同Table5/同作者模型的数据谱系连PartII，不重复计实验或理论票；La/Cd支持不直接测γrigid/chirality或给Ce τ。 | cross-source-lineage-and-transfer | direct-original-plus-PartII-comparison | PDF2 Table1; PDF4 References; PartII Table5 | true |
| BU75-D24-014 | 以通用E2率式、mean-life convention反算qγ中央约.942/.980/.981/1.009，只是印数条件诊断，不是原actual BR/ICC、误差或重现。 | task-conditional-rate-consistency | source-values-plus-standard-radiation-formula | PDF2 Table1 | true |

## Reported Lifetime and B Ledger

|nucleus/transition|Eγ keV|τ ps|B(E2) e²b²|triaxial model|axial model|
|---|---:|---|---|---:|---:|
|129La15/2−→11/2−|269|130±6|.42±.02|.37|.50|
|129La19/2−→15/2−|475|8.7±1.3|.38±.06|.42|.52|
|131La15/2−→11/2−|336|55±2|.34±.02|.32|.45|
|131La19/2−→15/2−|533|5.8±.6|.33±.03|.37|.47|

表头τ原样保；条件辐射率练习明确取通常mean-life convention，不将后来的数据库half-life混入。与PartII同一reported B不是新增一组点。strong K1/2/11/2四组为.53/.07、.55/.22、.49/.06、.50/.20；weak first两核.33/.30，higher blank不补。La higher/first实测中央.90476/.97059，印model1.13514/1.15625，保差异，不缺Cov给排除σ。

|core/comparison|原reported τ ps|B(E2) e²b²|来源/角色|
|---|---|---|---|
|128Ba2→0，279keV|140±30|.33±.07|Ref6，129La coreinput|
|130Ce2→0，254keV|旧225±19；新211±9|.33±.02|Ref4/本文；不凭同row造两个独立B|
|130Ba2→0，357keV|未列|.24±.08|Ref7，131La coreinput|
|132Ce2→0，325keV|68±10|.32±.05|Ref4，131La coreinput|
|106/108Cd group，633keV|未列|.082±.006|Ref5 group，不给两核各造一个γ|
|107Cd15/2→11/2，515keV|23.5±1.5|.095±.006|Ref5转引，本篇未新测Cd|

(.33+.33)/2=.33，(.24+.32)/2=.28，是PartII core平均中央来源；原误差不能只按独立quadrature推。107Cd .095/.082=1.15854，模型.096/.082=1.17073、轴向.12/.082=1.46341，能复正文量级，quoted误差仍属原来源。

## Conditional Rate Exercise

采用选定pure E2、mean τ的一般近似单位式B[e²b²]=.0816 qγ/(E[MeV]^5 τ[ps])，qγ=b_total/(1+αIC)。人为qγ=1得到四个中央.44564/.38788/.34644/.32706；对原B反算qγ=.94246/.97967/.98140/1.00899。它们只检印数尺度和缺转换输入，不能认实际qγ/α，末数略>1也不以rounded数/近似常数/未知Cov宣判违例。原reported B支持保留，不用此练习替原分析。

## Competing Interpretations and Limitations

能谱unfavored态、B与邻核系统学联合支持指定模型的triaxial interpretation；实际shape distribution、γrigidity、chirality或模式唯一性不是直接测量。Fig2中不同I偏好不同轴、随γ扫描crossing是模型输出，轴字典不可跨源搬。

原来缺primary的Table5现在有实际RD/feeding/normalizer链，信息增益是把测量、取参、派生和prediction分开，而非增paper count。缺原counts/零点/stopper/峰面积共同误差、branch/ICC与actualproducer仍不足精确重放。La的实测τ不迁Ce，原core参考论文尚未本轮独立全文核验。

## Extracted Pages

- [[meyer-ter-vehn-1975-odd-a-unique-parity-comparison]]：Table5 primary和core定标来源。
- [[133ce-thesis-analysis-blueprint]]：寿命—B—形状模型的分层和迁移合同。
- [[135nd-chiral-partner-resolved-evidence-map]]：必要EM检验保输入依赖，原实验价值不被重复票或硬判门替代。


Day24 source link: [[butler-1975-la129-la131-rd-lifetimes]]
