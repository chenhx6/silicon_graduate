---
type: source
title: "Chen2013：一维手征集体Hamiltonian的量子化与边界"
aliases: [Chen2013 collective chiral modes, Collective Hamiltonian for chiral modes]
created: 2026-10-26
updated: 2026-10-26
status: ai-draft
review_status: unreviewed
source_type: theoretical-paper
reading_depth: deep-read
title_original: "Collective Hamiltonian for chiral modes"
authors: [Q. B. Chen, S. Q. Zhang, P. W. Zhao, R. V. Jolos, J. Meng]
year: 2013
doi: 10.1103/PhysRevC.87.024314
arxiv: 1212.2313v2
canonical_source: https://arxiv.org/abs/1212.2313
citation_key: ""
raw_file: raw/papers/2013_Chen_CollectiveHamiltonianChiralModes_arxiv12122313v2.pdf
raw_sha256: bef6182263a6282ea6c4fc3e2fbae481bbf629e484dbf9668e3ea9e622342a2c
raw_storage_status: public-staging-not-archived
actual_body_file: tmp/day24-collective-chiral-008/chen2013-collective-chiral-arxiv.pdf
nuclei: []
models: [one-dimensional-chiral-collective-hamiltonian, tilted-axis-cranking, particle-rotor-model]
observables: [energy-splitting, orientation-wavefunction]
methods: [collective-quantization, cranking-mass]
tags: [chirality, finite-tunnelling, model-validity, collective-measure]
---

# 一维集体量子化补上有限隧穿，也保留其冻结自由度

## Bibliographic Record

Q. B. Chen等，*Physical Review C* **87**, 024314 (2013)，DOI `10.1103/PhysRevC.87.024314`。Crossref和INSPIRE核到题名/作者/期刊；实际科学正文为官方arXiv:1212.2313v2，16页，固定URL `https://arxiv.org/pdf/1212.2313v2`。下载HTTP200、987932bytes、有效PDF，SHA见frontmatter；raw归档槽未写入，原文仍在tmp public staging。

官方history为2012-12-11 v1、2013-02-23 v2；PDF1边栏同v2日期，typeset date另字面写July24,2018。两日期字段分别保留，不据此创造新科学版本或改出版年。PRC VoR未取得，locator全部属于这个16页arXiv读本。

## Scope and Reading Depth

worker读16页全文主线、全部8图及关键公式；root另读16页文本，视觉核PDF4–7/9–14，覆盖Figs1–8、Eqs4–14/16–28。阅读链为TAC构造→质量近似→Pauli量子化/基与壁→势和质量→能级/波函数→PRM反例与比较坐标。没有运行作者producer、重建其B/V数表或拟合真实核实验。

## Summary

本文在固定形变的单j粒子-空穴示意体系中，以TAC给出的势和质量构建一个φ自由度的集体Hamiltonian；有限区间量子化能产生偶/奇φ态和有限能隙，恢复平均场破缺的左右反射对称。它超出单个均场极小和局部谐振图像，但仍忽略θ量子涨落；作者自己的PRM比较显示高频第二次手征振动未被一维方案描述。

## Experimental or Theoretical Setup

只有示意πh11/2粒子⊗νh11/2空穴+刚性三轴rotor；γ=−30°，Cπ=.25MeV、Cν=−.25MeV，J0=40ℏ²/MeV（PDF8 §III）。Eq6为Jk=J0 sin²(γ−2πk/3)，直接代得[10,40,10]ℏ²/MeV，没有额外4/3因子。Eq4的粒子/空穴符号与正文Cν符号在恢复producer前须核约定，不能未经说明重复施负号。

ω=(ωsinθcosφ,ωsinθsinφ,ωcosθ)，0≤θ≤π/2、−π/2≤φ≤π/2；V(φ)=minθ E′(θ,φ)。θ可沿最小化路径改变，但没有θ的量子动能，也没有γ/β的动力学、多轨道/3qp组态重排或目标核BCS输入。不是135Nd/133Ce/134Pr的新数据计算。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CH13-D24-001 | 一维φ连接左右取向，V=minθE′；固定γ的单j对称粒子-空穴示意体系，θ量子涨落未纳入。134Pr旧势面只是选择φ软方向的动机，不是本篇真实核拟合。 | direct-model-construction-and-scope | direct-version-specific-original | PDF4 Eqs5/7/8; PDF5 opening; PDF8 §III; PDF15 discussion | true |
| CH13-D24-002 | Pauli量子化给−ℏ²/(2√B)∂φ[(1/√B)∂φ]+V，Hermitian测度√B dφ。B依赖φ，不能静默改常质量或flat测度而保留同一算符。 | direct-quantization-contract | direct-original | PDF5 Eqs10–14 | true |
| CH13-D24-003 | 质量推导假设从最低cranking态出发、激发幅小及φ̈=−Ω²φ，并略去所列φ²项；rotation域的Ω≈0只用于质量处方，最终量子gap仍有限。 | approximation-and-result-boundary | direct-original-with-explicit-inference | PDF6 Eqs16–22; PDF7 Eq23; PDF9 Eq28; PDF11 energyparagraph | true |
| CH13-D24-004 | 偶/奇φ基为B^−1/4乘cos[(2n−1)φ]/sin(2nφ)，与√B测度配套；±π/2取Dirichlet壁，作者以边界大B为动机明确称wall approximation。φ反射的偶/奇不是核空间宇称。 | basis-boundary-and-symmetry-identity | direct-original-plus-identity-boundary | PDF7 Eqs24–27; PDF10–11 wallparagraph | true |
| CH13-D24-005 | 示意TAC势在ℏω≥.20MeV双阱，.20/.25/.50对应势垒.001/.07/1.93MeV；.25/.30低态仍宽广，作者解释振动重要。双极小不自动认证量子局域单手性。 | direct-model-result-and-hierarchy | direct-original | PDF8 §IV.A; PDF10 Fig2; PDF12–13 Figs6/7 | true |
| CH13-D24-006 | 最低gap从1.19MeV@.25降至.01MeV@.50；本征ψ1偶、ψ2奇，左右对称恢复。非简并定态奇量期望为零；局域左右组合在有限gap下一般不是定态，是本任务基于该对称性的推断。 | model-result-and-labelled-inference | direct-original-plus-quantum-synthesis | PDF11 Fig4/energyparagraph; PDF12–13 Figs6/7 | true |
| CH13-D24-007 | Fig7字面画abs(ψ)²，Eq14的积分测度却为√B dφ；每单位φ的概率密度需含√B。不说明测度就把图当flat角度频数是不成立的，不由此判原图错误。 | observable-measure-boundary | direct-original-plus-measure-inference | PDF5 Eq14; PDF13 Fig7caption | true |
| CH13-D24-008 | PRM在ℏω约.35后gap重新增大，本一维集体gap仍减小；作者明确second chiral vibration未包括。高spin/高频无条件更静态的单调推断不受支持。 | direct-model-failure-boundary | direct-original | PDF14 Fig8; PDF15 firstparagraph | true |
| CH13-D24-009 | 比较固定ω而非同good-I；PRM两带同I时ω可不同。作者laboratory-frame措辞不等严格I投影；本文未给新的实验τ/δ/g或本集体模型完整EM率表。 | comparison-coordinate-and-output-scope | direct-original-and-labelled-boundary | PDF13 labframeparagraph; PDF14 comparison; PDF15 fixedfrequencyparagraph | true |
| CH13-D24-010 | 在闭盒上B光滑正且有限、Dirichlet域的额外regular合同下，x=∫√(B/B0)dφ使该Pauli算符变常质量；同φ下flat幅u=B^1/4ψ另有Q_B势项。V偶须连B偶和反射不变的域才推出奇量期望零；large或singular B本身不推出硬墙。这是本任务方法推导，synthetic三路谱不复现作者producer。 | conditional-task-metric-and-domain-derivation | source-premise-plus-independent-math | PDF5 Eqs12–14; PDF7 Eqs24–27; task chiral-metric-011 | true |

## Analytical Reconstruction

定义T=½B(φ)φ̇²，φ无量纲弧度，B单位ℏ²/MeV。源Pauli算符和内积为

$$H=-\frac{\hbar^2}{2\sqrt{B}}\partial_\varphi\frac{1}{\sqrt{B}}\partial_\varphi+V,
\qquad \langle f|g\rangle=\int_{-\pi/2}^{\pi/2}\sqrt{B}\,f^*g\,d\varphi.$$

Eq22质量为

$$B=2\hbar^2\sum_{l\ne0}\frac{(E_l-E_0)\left|\partial_\varphi\boldsymbol\omega\cdot\langle l|\hat{\boldsymbol j}|0\rangle\right|^2}{[(E_l-E_0)^2-\hbar^2\Omega^2]^2}.$$

Ω=0时约成能差三次方分母，不会删去Pauli动能；因此不等最低两个集体本征能量严格相同。质量推导的局部/小激发近似仍需与其用于大φ路径的有效域分别检验，不能称为完全无近似的量子惯量。

若B、V为偶函数且边界对称，最低非简并偶/奇态对任意φ奇乘法量f的期望均为零，来自偶测度下积分的奇性。取|L/R⟩=(|e⟩±|o⟩)/√2可构造偏向两井的相干组合；有限ΔE时相对相位以ΔE t/ℏ演化。此为本任务推断，不是原件给出的实验退相干/定态局域时间；不能把作者static regime改写成单个有限核能量本征态永久只占一手。

## Source Independence

新方法原稿没有新实验。参数声明沿用[[frauendorf-meng-1997-tilted-rotation-chirality]]；PRM/TAC比较与[[qi-2009-135nd-particle-rotor-chirality]]、[[almehed-2011-chiral-vibrations-a135]]是理论谱系，不是多次独立135Nd采集。与[[olbratowski-2002-critical-frequency-preprint]]比较需保留不同组态/轴/参数、经典均匀转动和量子集体空间的差别。

CH13-D24-010的连续推导及synthetic正质量/偶双阱三路谱保存在[[135nd-chiral-partner-resolved-evidence-map]]“一维测度的可复现练习”；没有使用原V/B曲线、核数据或作者代码。路间一致性小于共同截断误差，未按一致性宣称真实谱精度。

## Competing Interpretations and Limitations

本文的固定γ不能认证实核γ刚性或排除γ软度/混合；单配置不能排除crossing或3qp空间变化。PRM的高频再劈裂是作者原文内建反例，不由本任务另造。±π/2壁是近似域选择；真实B/V、边界/遗漏坐标敏感性和相应EM算符必须先得到，才能把方法用于目标核。不能迁移.20/.35MeV或1.19/.01MeV为135Nd/133Ce硬判据。

后续实际原读[[chen-2016-two-dimensional-collective-chiral-wobbling]] CH16-D24-004/007–011补θ动力学、再劈裂与PRM高spin支持，但连1D边界也改为periodic，低spin质量近似仍失败；不能称只加θ就排他修复本篇Fig8或将其晚期LW与本篇second vibration无条件同名。

## Knowledge Impact and Learning Decision

`supports`有限集体量子化可连接平均场势与隧穿谱；`limits`只凭双极小、波函数图像或高spin单调趋势判静态手征。进入[[135nd-chiral-partner-resolved-evidence-map]]和[[nuclear-chirality]]的模型层，不补其缺失g、branch、normalizer或实验Cov。新增claims全needs_review:true。

## Extracted Pages

实际16页v2全主线已读；PDF4坐标/势，PDF5算符/测度，PDF6质量，PDF7基/壁，PDF8参数，PDF9–14全部8图，PDF15失败/固定ω说明，PDF16references。tmp的全文与渲染页只供恢复与复核，不作为publication manifest内容；raw归档未完成。

## Agent self-audit triage

P0：未发现本有界来源单元的阻断问题。P1：原算符/测度/量子数/版本、推断与作者解释分开；没有实际producer与目标核输入，未声称复现其谱。P2：citation key空，raw归档deferred；这两项不通过改Bib/raw来消除。原作者2018typeset date、v2和2013出版年分别留痕。
