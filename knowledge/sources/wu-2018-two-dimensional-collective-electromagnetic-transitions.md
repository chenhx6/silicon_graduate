---
type: source
title: "Wu2018：手征集体模型的带内EM是局部率平均"
aliases: [2DCH PartII electromagnetic transitions, Wu2018 collective EM]
created: 2026-10-26
updated: 2026-10-26
status: ai-draft
review_status: unreviewed
source_type: theoretical-paper
reading_depth: deep-read
title_original: "Two-dimensional collective Hamiltonian for chiral and wobbling modes. II. Electromagnetic transitions"
authors: [X. H. Wu, Q. B. Chen, P. W. Zhao, S. Q. Zhang, J. Meng]
year: 2018
doi: 10.1103/PhysRevC.98.064302
arxiv: 1809.04418v2
canonical_source: https://arxiv.org/abs/1809.04418
citation_key: ""
raw_file: raw/papers/2018_Wu_TwoDimensionalCollectiveEM_arxiv180904418v2.pdf
raw_sha256: 7d7c12ebc754f23721bd5367acc050c54dd3cf0f03f2f7480de407c1f3493dcb
raw_storage_status: public-staging-not-archived
actual_body_file: tmp/day24-chiral-em-014/wu2018.response
nuclei: []
models: [two-dimensional-collective-hamiltonian, tilted-axis-cranking, particle-rotor-model]
observables: [intraband-bm1, intraband-be2, effective-orientation-angles]
methods: [probability-averaged-local-transition-rates]
tags: [chirality, wobbling, electromagnetic-transitions, model-validity]
---

# 集体取向涨落修正带内率，未给完整相干跨带振幅

## Bibliographic Record

X. H. Wu等，*Physical Review C* **98**, 064302 (2018)，DOI `10.1103/PhysRevC.98.064302`，Crossref核作者/题名/出版2018-12-03。实际读本为官方`https://arxiv.org/pdf/1809.04418v2`，HTTP200/application/pdf、276035bytes、17页、SHA见frontmatter。边栏v2为2018-09-13，PDF1排印日期为September14,2018；先于12月期刊出版，VoR未另读，locator只归此17页读本。原件仍public staging，raw归档未做。

## Scope and Reading Depth

worker与root各读17页全文主线；全部4图（PDF9–12）及关键Eqs1–21由worker视觉核，root另视觉PDF4–7/9–12，核率定义、输入、四图和字面遗漏。没有运行作者producer、恢复V/B数表、拟合实验或报告新CI。本文是[[chen-2016-two-dimensional-collective-chiral-wobbling]]的直接EM后续，Ref1为该文；不是独立实验。

## Summary

本文计算带内M1、ΔI2 E2及ΔI1 E2，方法是用单个集体态的概率分布平均已经平方的局部TAC B值。这给出取向涨落对平滑带内强度的修正，并与同参数PRM比较。它没有构造不同集体态/sector或精确Ii/If之间的相干跃迁核，作者也明确承认PRM的奇偶交错未复现。

## Experimental or Theoretical Setup

单h11/2粒子⊗空穴、γ=−30°、Cπ/ν=±.25MeV、J0=40ℏ²/MeV；gp−gR=1、gn−gR=−1、Q0=1eb，1DCH/2DCH/TAC/PRM共同采用（PDF7 §III）。这些是示意共同输入，不是135Nd/133Ce实测g或Q。

PDF7–8称follow PartI的periodic计算；并非原CH13 box。质量指回CH13/CH16，没有明确选择PartI的Ω0 baseline或后加1.10MeV的版本、actualmassgrid或截断；不能推定本文已经修复低spin能谱失败。本文没有真实多轨道/3qp/BCS或目标核response。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WU18-D24-001 | 带内EM按单态ρ平均局部TAC B值；Eqs11–13/15–17没有Ψf或不同态间的相干transitionkernel，不等完整跨I/sector RME计算。 | direct-method-and-scope | direct-version-specific-original | PDF3 endintro; PDF6 Eqs11–13; PDF7 Eqs15–17 | true |
| WU18-D24-002 | 局部率用θJ/φJ，即总角动量方向；它一般不同于cranking θ/φ，stationary TAC才相同。集体平均采样离极小取向，不能全域置两组角相等。 | direct-coordinate-contract | direct-original | PDF5 Eqs6–8; PDF6 Eqs9–10/discussion | true |
| WU18-D24-003 | 单ρ局部率函数仍依赖density/nodes，但不能从中恢复不同态相对phase、跨取向干涉或intersector selection-rule矩阵；分开平均M1/E2也不给signed δ。 | labelled-method-inference | direct-formula-plus-output-boundary | PDF5–7 Eqs6–17; PDF11 Fig3 | true |
| WU18-D24-004 | 四种benchmark共享单j/固定γ/惯量及gp−gR=1、gn−gR=−1、Q0=1eb；非真实核测量/独立定标。 | direct-model-input | direct-original | PDF7 §III | true |
| WU18-D24-005 | 继承periodic与CH16谱系明确，但全文未明确mass Ω版本/新grid/截断，不能据本文强度趋势宣布PartI低spin能谱已无条件修复。 | inherited-input-readiness-boundary | direct-reference-and-body-scope | PDF4 modelrefs; PDF7–8 §IVopening; PDF1–17 scope | true |
| WU18-D24-006 | Figs1/3的平滑带内尺度/趋势有PRM支持，但M1与ΔI1 E2的odd-even staggering未恢复；作者解释I不是good quantum number。高spin CH M1非零与stationary TAC零值之差为模型涨落修正，非新实验认证。 | model-benchmark-and-adverse-result | direct-original | PDF9–10 Fig1discussion; PDF11 Fig3; PDF13–14 Summary | true |
| WU18-D24-007 | φeff为E abs(φ)，θeff为E[π/2−abs(π/2−θ)]，是折叠cranking坐标矩，不是signed均值/RMS/θJ有效角。约I15相近均值“might be”static signal保为作者暂定模型解释。 | direct-definition-and-inference-boundary | direct-original | PDF8 Eq19; PDF11 Eqs20–21; PDF13 firstparagraph | true |
| WU18-D24-008 | Jcoll为measure-averaged JTAC并作Icoll=Jcoll−1/2，不是严格I投影；它不提供精确Ii/If态对，作者以非good-I解释交错缺失。 | comparison-map-and-quantum-number-boundary | direct-original | PDF6 Eq14; PDF7 Eq18; PDF10/13 staggeringparagraphs | true |
| WU18-D24-009 | 原引言列interband E2诊断后，本文新输出明确仅intraband，未检验那些跨带规则，也未生成τ/BR/ICC/δ/P/g/Cov实验网络。 | source-output-and-transfer-boundary | direct-original-scope | PDF3 intro; PDF5–7 method; PDF13–14 Summary | true |
| WU18-D24-010 | 此v2 PDF4 Eq2字面缺1/√B后的末个∂φ，视觉确认不是提取丢字。CH13完整Pauli式和本篇2D Eq4另保，未据此定义新的一阶H或判实际producer错误，VoR是否改正未知。 | literal-author-version-boundary | direct-original-visual | PDF4 Eqs2/4; CH13 PDF5 Eqs12–13 | true |
| WU18-D24-011 | 完整官方v2 source archive仅EM.tex和fig1–4.eps五个regular文件，提供文章/图而非已核数值solver/inputgrid。此包没有code/data/supp文件，不等全网不存在producer，无法据图逆造实际mass/端点/job。 | bounded-author-archive-readiness | actual-official-complete-inventory | arXiv1809.04418v2 src complete tar member inventory | true |

## Analytical Reconstruction

以X表示所选M1/ΔI1 E2/ΔI2 E2通道，源Eqs15–17给

$$\overline B_i[X]=\int_0^\pi d\theta\int_{-\pi/2}^{\pi/2}d\varphi\,
\sqrt w\,|\Psi_i(\theta,\varphi)|^2 B_\mathrm{TAC}[X](\theta,\varphi).$$

1D式把测度换为√B dφ并沿θ最小化路径取局部率。这里是正局部率的期望，不是先对orientation振幅相干求和再平方，也不是用均值角代入非线性B公式。不能从已平均B倒推出一个唯一signed RME或δ。

局部式用Jk=⟨jk⟩+𝒥kωk确定θJ/φJ，原文以tan写方向；actualproducer的quadrant/atan2选择未给。远离stationary极小J不必平行ω，两个角组需各自计算。折叠角均值即使相近，也不决定完整分布、signed handedness或隧穿相位；φeff>0本身不是实核静态手征判据。

源参数下，局部θJ=φJ=π/2的Eq7给B(E2,ΔI2)=5/(32π)≈.04973592e²b²、Eq8为0，吻合图的约.05平台尺度。这只是局部公式检查，不复现集体平均曲线。M1为0还需要相应横向intrinsic μ为0，不能只凭这两个角对任意磁矩向量作零率判决。原示意stationary i轴对齐与实际实验态分开。

本征态的overallphase本来任意，并不是待测的band绝对phase。这里缺的是完整内部相干幅、不同初末态核及E/M算符的一致约定；good-I投影的具体对照见[[chen-2017-128cs-angular-momentum-projection-chirality]] CH17-D24-001–004，不能据其框架直接补本文未算的量。

## Source Independence

Ref1为[[chen-2016-two-dimensional-collective-chiral-wobbling]]、Ref70为[[chen-2013-collective-hamiltonian-chiral-modes]]，共同参数还沿[[frauendorf-meng-1997-tilted-rotation-chirality]]。PRM交错参考Koike2004谱系，不增加[[mukhopadhyay-2007-135nd-chiral-vibration-static]]实验证据票。这里新增的是某种EM输出方法及其局限，不是实际核的B/τ重测。

## Competing Interpretations and Limitations

对chirality与wobbling的跨带E2规则，本文只在背景列举，没有用新计算验证。概率平均的带内相似性不能替代完整跨带EM网络，也不能由四sector标签直接证明跨sector振幅消失。各模型使用同输入而趋势相近是有界benchmark；明显PRM交错差异必须保留，不能统称“完整定量符合”。

低spin质量版本、基/端点处理和EM的full coherent kernel仍缺。本文并未企图完成所有此类计算；其明确的取向涨落修正不因scope有限而全部失效。实际135Nd/133Ce迁移还需核素特定空间、算符、相干波函数、normalizer与response，不能拿本局部率平均填GAMPN→PROBMO实际EM合同。

## Knowledge Impact and Learning Decision

`supports`带内平滑强度的取向涨落修正，`limits`有集体wavefunction就已恢复全部EM相位/选择规则的推断。进入[[135nd-chiral-partner-resolved-evidence-map]]，并为[[133ce-thesis-analysis-blueprint]]保输出类型边界。新claims全部needs_review:true，不修改既有人审或撤回。

## Extracted Pages

PDF1身份；PDF2–3范围/背景；PDF4集体H及literal缺项；PDF5局部率/角；PDF6–7积分与共同输入；PDF8–13全部4图、折叠角与失败；PDF13–17总结/引用。worker/root读取范围见Reading Depth。原PDF、全文和页图只供暂存复核，不进最终publication manifest；raw归档未做。

本run015另取`https://arxiv.org/src/1809.04418v2`，HTTP200/gzip、curl0、121695bytes，完整archive SHA `b2ed43e6b61dfc867ac8159059a9683e656a6feac06d17db45944d6fcf3d1275`。安全逐regular member读字节/文本，不按归档内路径任意解出、不执行TeX/PS：EM.tex79259bytes（SHA `ce27435b6d600ae8172c0428ac83b020fc4a213d798c6f704879f86c11d87ee7`）及四EPS。EM.tex只include这四图，line89字面`\date{\today}`；该制作源不等数值模型源。完整清单/各member哈希在workers/chiral-producer-readiness-015，机构/出版商其它入口未查的范围明确保留。

## Agent self-audit triage

P0：本来源单元身份/权限未发现阻断项。P1：局部率/相干振幅、cranking/J角、折叠矩/有符号量、good-I边界与mass版本分开。Eq2只留字面版本问题，不改原producer。P2：citation key空/raw归档deferred，不动Bib/raw消项。
