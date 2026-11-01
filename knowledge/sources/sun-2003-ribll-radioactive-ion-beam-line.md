---
type: source
title: "Sun et al. 2003: RIBLL radioactive ion beam line"
aliases: [RIBLL, radioactive ion beam line in Lanzhou, RIBLL1]
created: 2026-11-01
archive_required: true
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
source_type: accelerator-detector-method-paper
reading_depth: read
title_original: "RIBLL, the radioactive ion beam line in Lanzhou"
authors: [Z. Sun, W. L. Zhan, Z. Y. Guo]
journal: "Nuclear Instruments and Methods in Physics Research A"
year: 2003
volume: 503
pages: "496–503"
doi: 10.1016/S0168-9002(03)01005-2
arxiv:
language: en
canonical_source: "https://www.sciencedirect.com/science/article/pii/S0168900203010052"
citation_key: sun_2003_ribll
raw_file: "raw/papers/RIBLL, the radioactive ion beam line in Lanzhou.pdf"
raw_sha256: "3d5e793dfa6c02b59365f0596ca45ed23ea8080d58347752653ec477ec2536d8"
nuclei: []
reactions: [projectile-fragmentation]
experiments: [RIBLL]
models: [gios, mocadi, lise]
observables: [beam-purity, time-of-flight, delta-e-e, mass-resolution, beam-profile, polarization]
methods: [radioactive-ion-beam, fragment-separator, br-de-br-separation, tof, silicon, csi, ppac]
tags: [accelerator-method, ribll, radioactive-beam, fragment-separator, tof, beam-identification]
---

# Sun et al. 2003：RIBLL 放射性束流线

## Bibliographic Record

Z. Sun et al., *RIBLL, the radioactive ion beam line in Lanzhou*, *Nuclear Instruments
and Methods in Physics Research A* **503** (2003) 496–503, DOI
`10.1016/S0168-9002(03)01005-2`。本地 PDF 为 8 页，SHA-256 为
`3d5e793dfa6c02b59365f0596ca45ed23ea808d58347752653ec477ec2536d8`。

## Scope and Reading Depth

本轮读取 PDF 全部正文、Table 1–3、图注和结论，覆盖 magnetic optics、Br–ΔE–Br
分离、F2/F4 operation modes、TOF/ΔE–E identification、beam profile 和调束结果。
论文描述的是早期 RIBLL1，不把所有性能数字直接迁移到后续 RIBLL-II 或 HIAF。

## Key Results

| ID | Narrow statement | claim_kind | evidence_level | locator | Boundary |
|---|---|---|---|---|
| RBL03-1 | RIBLL 采用四个大偶极磁铁、四个 focal points（F0/F2/F4 等）和反对称双消色差布局；主分离可用 Br–ΔE–Br，F1 设 wedge degrader。 | accelerator-design | PDF pp.1–3, Fig.1, Table 1 | 这是 RIBLL1 layout，后续线的磁光学和 detector inventory 需独立确认 |
| RBL03-2 | Table 1 给出水平/垂直角接受各 50 mrad、动量接受 `Δp/p=10%`、最大 rigidity 4.2 Tm、rigidity resolution `≤6×10^-4`、`A/ΔA>300` 目标和最小可测寿命小于 1 ms。 | accelerator-performance | PDF pp.2–3, Table 1 | 表列值是设计/测试条件下参数，不是所有束种和能量的保证 |
| RBL03-3 | F2 可插入薄 Si 与 RF 做 TOF–ΔE identification；第二段可作高级纯化、TOF spectrometer 或 zero-degree spectrometer，并在 F2 放二级反应靶。 | operation-mode | PDF pp.4–5, Sec.2.2 | 二级靶模式的传输、束斑、靶厚和 reaction rate 必须按目标实验重算 |
| RBL03-4 | RIBLL 设计考虑通过 fragment momentum/deformation selection 获得部分偏振 RIB，并设置 beam swinger，入射束角可偏转到 5°。 | accelerator-capability | PDF p.5, Sec.2.1 | 偏振程度不是装置常数，需对具体碎片、磁场和 acceptance 做测量 |
| RBL03-5 | 低束流时用 PPAC 测 beam position，高束流时用 scintillator-fiber beam scanner；F4 使用 300-mm Si ΔE 与 position-sensitive CsI(Tl) E detector。 | beam-diagnostic | PDF pp.2, 5–6, Fig.4 | detector response、threshold 和 rate limit 要按实验配置重新标定 |
| RBL03-6 | 80 A MeV `20Ne+9Be` tuning 中，TOF/ΔE 图清晰分离多种同位素，`A/ΔA>300`；加入 1-mm Al degrader 选择 `17F` 时，目标束约占总束 47%。 | commissioning-result | PDF pp.6–7, Figs.4–5 | 这是 tuning case，不是目标核素的可得束流率或纯度承诺 |
| RBL03-7 | F4 beam profile 的示例 FWHM 约 12.4 mm horizontal、17.0 mm vertical；论文结论称实测参数与设计目标相符。 | commissioning-result | PDF pp.7–8, Fig.6 and conclusion | beam spot 与能量、fragment species、slits、degrader 和 target geometry 有关 |

## Detector-to-Experiment Mapping

RIBLL 的强项是把“束流身份”作为实验观测的一部分：F2/F4 position、TOF、ΔE、
残余能量、magnetic rigidity 和二级反应产物可以组成 event-by-event beam/fragment
ledger。对核结构实验，这允许把低产额 γ cascade 与明确的 incoming/outgoing
particle identity 绑定，降低 contaminant 和错误 level placement。

## Summary

RIBLL1 is a fragment-separator and beam-diagnostic architecture whose scientific value
comes from combining magnetic purification with event-by-event TOF/energy/position
identification and flexible F2/F4 operation. Its 2003 commissioning demonstrates the
design logic, while current beam yield, purity and detector response must be remeasured
for a new isotope and a later beam-line generation.

## Competing Interpretations and Limitations

- Table 1 parameters are conditional on rigidity, fragment species, slits, degrader and
  beam intensity; they are not universal RIBLL-II or HIAF specifications.
- A/ΔA and a clean TOF–ΔE plot do not determine production yield, secondary-target rate
  or γ-ray efficiency.
- Partial polarization is a possible operating mode, not a fixed property of every
  radioactive beam.

## Reusable Design Inference

若把 RIBLL 的 beam-identification chain 与 IMP-DRAGON 的 HPGe+BGO/clover/LaBr3
组合，可形成一个“束流身份—γ响应—寿命/偏振”的闭环实验：上游 TOF/ΔE 记录
incoming isotope，中间靶区放 reaction target，后方 Si/CsI 记录 charged ejectile，
周围 HPGe/clover 记录 γ，LaBr3 只承担快定时。这个组合是本任务的实验设计推断，
不是两篇论文已经运行过的统一装置。

## Extracted Pages

- PDF pp.1–3: layout, magnetic elements and Table 1 parameters.
- PDF pp.4–5: F2/F4 operation modes, degrader and beam diagnostics.
- PDF pp.6–8: TOF/ΔE commissioning, beam profile and conclusion.

## Related Knowledge

- [[cross-mass-phenomena-detector-beam-prospectus-20261101]]
- [[yue-ke-2010-hirfl-csr-gamma-ball-csi-thesis]]
- [[yan-duo-2015-csr-coulomb-excitation-detector-system-thesis]]
- [[sun-yazhou-2019-16c-single-proton-knockout-thesis]]

## Knowledge Impact and Learning Decision

- `extends`: the Wiki with a primary RIBLL1 accelerator/beam-diagnostic source.
- `supports`: using beam-line focal-plane diagnostics and event-by-event PID as a required
  companion observable for rare A≈130 or neutron-rich structure experiments.
- `limits`: RIBLL1 specifications cannot be silently presented as RIBLL-II/HIAF current
  performance or as a target-specific yield forecast.
- `design inference`: a future proposal must include a beam-rate/purity scan, F2/F4
  diagnostics, target reaction-rate estimate, γ efficiency/response simulation and a
  negative-control channel.

## Human Review

This page is a Codex self-audit of a detector/accelerator-method source. `review_status:
unreviewed`; all numerical parameters remain tied to the 2003 RIBLL1 paper and its stated
commissioning conditions.
