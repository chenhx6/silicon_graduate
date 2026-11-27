---
type: source
title: "Åberg, Flocard and Nazarewicz 1990 - Nuclear shapes in mean field theory"
aliases: [Aberg Flocard Nazarewicz 1990 mean-field shapes]
created: 2026-09-21
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: review
reading_depth: deep-read
title_original: "Nuclear Shapes in Mean Field Theory"
authors: [S. Åberg, H. Flocard, W. Nazarewicz]
journal: "Annual Review of Nuclear and Particle Science"
year: 1990
citation_key: "aberg_1990_generic-shapes-mean"
volume: 40
pages: "439-528"
canonical_source: "Åberg, Flocard & Nazarewicz, Annu. Rev. Nucl. Part. Sci. 40, 439-528 (1990)"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/形变/1990_Aberg et al_Nuclear Shapes in Mean Field Theory.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/形变/1990_Aberg et al_Nuclear Shapes in Mean Field Theory.pdf"
raw_sha256: "90e3d1324dbf591cc042a3ad3b777a75e00af1463869d9ad557af433469562e6"
nuclei: [generic, 152Dy, 192Hg, 147Gd, 212Rn, 186Pb]
reactions: [generic-high-spin-mean-field]
experiments: [high-spin-spectroscopy, electromagnetic-moments]
models: [Hartree-Fock, Hartree-Fock-Bogoliubov, Nilsson-Strutinsky, cranked-mean-field, relativistic-mean-field]
observables: [shape, beta2, gamma, beta3, quadrupole-moment, band-termination, superdeformation, shape-coexistence]
methods: [mean-field, constrained-HF, HFB, Strutinsky, rotating-frame]
tags: [mean-field, nuclear-shapes, triaxiality, high-spin, octupole, shape-coexistence, superdeformation]
---

# Nuclear shapes in mean-field theory

## Bibliographic Record

- S. Åberg, H. Flocard & W. Nazarewicz, *Annu. Rev. Nucl. Part. Sci.* **40**, 439–528 (1990).
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/形变/1990_Aberg et al_Nuclear Shapes in Mean Field Theory.pdf`。

## Scope and Reading Depth

- Local PDF 1–89 (printed pp. 439–527) read by section: effective interactions and constrained HF/HFB, symmetries and Nilsson–Strutinsky, shape parametrization/consistency, axial/triaxial quadrupole shapes, high-spin stretching/polarization/intruder bands/termination/noncollective rotation/superdeformation, reflection-asymmetric/octupole shapes, shape coexistence, neutron–proton and higher-deformation interactions, relativistic/configuration developments and beyond-mean-field limits.
- Not covered: cited primary data and post-1990 computational developments.

## Key Results

- HF/HFB and Nilsson–Strutinsky are complementary mean-field routes: self-consistent effective interactions treat the full density, whereas the shell-correction approach separates liquid-drop and shell energies and uses a variational potential deformation. Shape inconsistency in the latter is usually a few percent but can matter when converting mass to charge moments (PDF pp.442–454, Eqs.8–14).
- The quadrupole surface uses `β2,γ`; prolate and oblate limits are `γ=0°` and `60°`, with triaxial sectors and rotation-axis conventions explicitly defined. Higher multipoles are required for realistic large-deformation surfaces (PDF pp.452–456).
- Rotation changes shape through centrifugal stretching, decoupled-particle polarization, intruder configurations, band termination, noncollective rotation and superdeformation. Alignment and shape evolution must be solved self-consistently in the rotating frame (PDF pp.457–488, Sec.5).
- Reflection-asymmetric shapes are treated with octupole degrees of freedom. Octupole correlations, parity doublets, E1/E3 moments and exotic higher-order shapes are related, but a static octupole minimum is not implied by a single parity splitting or relative transition strength (PDF pp.488–502, Sec.6).
- Shape coexistence is reviewed for prolate/oblate competition, spherical–deformed isomers and pairing isomers; mean-field minima require beyond-mean-field mixing/projection to connect intrinsic configurations to laboratory spectra (PDF pp.502–511, Sec.7).
- Neutron–proton interactions, higher multipole deformations, approximate configuration labels and early relativistic mean-field work are identified as important extensions, while the final section lists symmetry restoration, collective fluctuations and configuration mixing as missing beyond-mean-field ingredients (PDF pp.511–527, Secs.8–10).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AFN90-1 | Mean-field potential minima are intrinsic model outputs; laboratory shape claims require consistency, observables and (when needed) symmetry restoration/mixing. | model-boundary | review | PDF pp.442–454, 518–527 | true |
| AFN90-2 | Rotation can drive stretching, triaxiality, noncollective alignment, band termination and superdeformation. | review-synthesis | review | PDF pp.457–488 | true |
| AFN90-3 | Octupole and shape-coexistence minima have distinct companion observables and competing dynamic interpretations. | interpretation-boundary | review | PDF pp.488–511 | true |
| AFN90-4 | `β2/γ` parametrization and rotation-axis sector are convention-dependent; higher multipoles and self-consistency matter for large deformations. | formalism-boundary | direct | PDF pp.452–456 | false |

## Summary

Åberg, Flocard and Nazarewicz provide a foundational map from effective interactions to rotating nuclear shapes. The durable Wiki lesson is to keep intrinsic mean-field minima, laboratory spectra, symmetry restoration and collective fluctuations as separate evidence layers; high-spin alignment, octupole, superdeformation and coexistence labels cannot be read directly from a single calculated `β,γ` point.

## Competing Interpretations and Limitations

- Nilsson–Strutinsky, HF/HFB and early relativistic mean-field results can agree qualitatively while differing in parameterization, pairing, self-consistency and zero-point corrections.
- High-spin shape changes may arise from centrifugal stretching, quasiparticle polarization, band crossing, termination or shape coexistence; alignment alone does not uniquely identify a triaxial or superdeformed minimum.
- Octupole observables can reflect static deformation, soft vibrations or reflection-asymmetric correlations. E1/E3 and parity-doublet information must be combined with lifetimes and model sensitivity.
- Mean-field minima break rotational/parity symmetries; projection and configuration mixing are required before assigning a unique laboratory band identity.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AFN90-AR-1 | Shape chain | Effective interaction → constrained HF/HFB or shell-correction energy surface → intrinsic `β,γ,β3` minimum → rotating-frame observables. | PDF Secs.2–5 | self-checking |
| AFN90-AR-2 | High-spin chain | Cranking/rotation → quasiparticle alignment and shape polarization → band crossing/termination/superdeformation; configuration and pairing are explicit inputs. | PDF Sec.5 | self-checking |
| AFN90-AR-3 | Laboratory transfer | Intrinsic octupole/coexistence minimum → projected/mixed states and transition moments; without restoration, retain model-only status. | PDF Secs.6–10 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[rotating-mean-field]], [[triaxial-deformation]], [[octupole-deformation]], [[octupole-softness]], [[triaxial-shape-coexistence]], [[band-termination]] and [[superdeformation]].
- New reusable rule: annotate every shape claim as intrinsic/model, direct observable, or projected/laboratory inference; preserve rotation-axis and parametrization conventions.
- This source is a review and adds no independent experiment; it is a theory backbone for cross-source self-audit and L3 shape questions.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `AFN90-P0-1`: Do not promote mean-field minima or early model examples into direct triaxial/octupole/shape-coexistence evidence without observable and beyond-mean-field boundaries.

## Extracted Pages

- Concepts/models: [[rotating-mean-field]], [[triaxial-deformation]], [[octupole-deformation]], [[octupole-softness]], [[triaxial-shape-coexistence]], [[band-termination]], [[superdeformation]]。

## 2026-11-27 — 馆藏原件与覆盖核对

刊版馆藏共 89 个 PDF 页，对应印 439–527。PDF 16（印 454）进入四极形状一节，PDF 64（印 502）讨论低激发能的形状共存及竞争组态。正文分页与下载水印中 439–528 的条目范围存在一页差异，本地末页明确印为 527，未将潜在末页计为已读。

## 2026-11-27 — 馆藏原件与覆盖核对

- 物理第 1–4 页（印 439–442）题名、目录、§1 引言。
- 物理第 4–16 页（印 442–454）§2 有效相互作用、约束 HF/HFB、对称性及 Nilsson–Strutinsky 方法，§3 形状参数化与一致性。
- 物理第 16–19 页（印 454–457）§4 轴对称与三轴四极形状。
- 物理第 19–49 页（印 457–487）§5 高自旋形状、离心拉伸、粒子极化、闯入带、带终止、非集体转动和超形变。
- 物理第 50–63 页（印 488–501）§6 反射不对称形状、八极谱学、电偶极矩与非轴向八极形状。
- 物理第 64–73 页（印 502–511）§7 低激发能形状共存、球形—形变异构与配对异构。
- 物理第 73–81 页（印 511–519）§8 中子–质子相互作用与高阶形变，§9 组态与相对论平均场，§10 对称性恢复及超越平均场方法。
- 物理第 81–89 页（印 519–527）致谢及所见书目，末条编号 501。
- 本次获取的具体覆盖：逐读物理第 1–89 页的提取文本，覆盖题名页、目录、正文 §§1–10、致谢及馆藏所见参考文献。对读了正文、图 1–42 的图注及表 1 的表题和可辨文字。未目检图像，公式及图内标注仅按可辨文本核对。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A21-1 | Strutinsky 展开把平滑能量与一阶壳修正分开。形状一致性分析区分作为变分量的势形变与计算所得的密度形变。综述报告所讨论模型中的差异通常在实际形变值的 5% 以内，仍可能影响电荷矩与质量矩之间的换算。 | model | source-reported | 物理第 12–13 页，§2.5、式（5）–（7）、图 3。物理第 15–16 页，§3.2、式（13）–（14）。此处据正文概述，公式字符待核。 | true |
| A21-2 | 综述转述了 ¹⁵²Dy 中观测到的一串规则、间隔接近的 γ 跃迁及后续寿命测量。图注所述的实验能级还包括同核另外两组共存序列。 | reported-observation | source-reported | 物理第 38 页，§5.6、引文 253–254。物理第 39 页正文及第 41 页图 18 上部，图中各序列的标签待核。 | true |
| A21-3 | 推转 Nilsson–Strutinsky 计算将 ¹⁵²Dy 的三组结构分别关联到扁形非集体、小形变集体和超形变的内禀势能面极小。图 18 下部比较仅约束宇称与签名的势能面和进一步约束占据组态的势能面。 | model | source-reported | 物理第 39 页，§5.6.1。物理第 41 页，图 18 下部及图注，左右面板与对应极小待核。 | true |
| A21-4 | 综述用 ²²²Th 的自旋—转频数据检验八极形变解释。作者报告，含八极形变的推转计算再现了已测区间的渐进顺排。随后向近反射对称形状的转变是模型预测，正文将其置于最后一个实验点以上。 | interpretation | source-reported | 物理第 57–58 页，§6.2、图 31、计算引文 355 和实验引文 357。第 57 页正文与第 58 页图注的自旋表述分别约为 26 和 24，需核对第 58 页曲线、实验点和图注后再引用阈值。 | true |

本文为综述。¹⁵²Dy 的级联和寿命分别取自引文 253、254，图 18 的计算比较取自 262。²²²Th 的计算与实验点分别取自 355、357。上述依赖按正文和图注追踪，未独立查阅被引论文、原始谱图或实验数据。

- 将 Wiki 中误标为 PDF 页码的 442–454、457–488、488–502、502–511、511–527 改按物理页著录。§§2–3 为第 4–16 页，§5 为第 19–49 页，§6 为第 50–63 页，§7 为第 64–73 页，§§8–10 为第 73–81 页。第 81–89 页另标致谢与书目。将馆藏实读印页 439–527 与水印引文 439–528 分列。
- 将 AFN90-1 的方法定位改为第 12–16 页图 3、式（5）–（7）及（13）–（14），将超越平均场的定位收至第 80–81 页 §10。将 AFN90-4 定位到第 14–15 页 §3.1，写明通常四极形状扇区为 0° 至 60°，两端分别为长形与扁形，Lund 一维推转的轴选择使用 −120° 至 60°。
- 将高自旋段的普遍自洽要求改为核对各例的模型、组态约束和配对处理。第 32 页图 13 的 ¹⁵⁸Er 计算明确忽略配对。保留 ¹⁹²Hg 为 §5.6.2 的区域标题实例，具体图证据按第 45 页图 22 著录为 ¹⁹⁴Hg 和 ¹⁹¹Hg。将 generic-high-spin-mean-field 移至方法或主题字段。
- 第 1 页作者栏提取误作 Flacard，按第 2 页页眉及现有条目规范为 Flocard。Witald 的全名拼写待核，引文暂用 W. Nazarewicz，Åberg 的重音按现有条目著录。
- 逐式引用前须核对下列物理页。第 5 页式（1）、第 6 页式（2）、第 9 页式（4）、第 12 页式（5）、第 16 页式（13）–（14）、第 22 页式（15）和（17）、第 39 页式（20）、第 74 页式（22）–（23）的主体缺失或近乎缺失。第 7 页式（3）、第 12 页式（6）–（7）、第 14–15 页式（8）–（12）、第 22 页式（16）、第 33 页式（18）、第 39 页式（19）、第 60 页式（21）有矩阵、上下标、运算符或希腊字母残缺。暂保留式号和正文能支持的语义。
- 图 1–42 均有可辨图注，表 1 有表题。第 30 页图 12 图注提取为 100 MeV 的等高线间隔待核，暂缓引用该数值及单位。第 48 页图 24 图注提取为 ⁸⁰Si，同页图内两处标记和第 66 页正文均支持暂录为 ⁸⁰Sr。
