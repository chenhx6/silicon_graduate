---
type: source
title: "Attosecond coherent control of free-electron wave functions using semi-infinite light fields"
aliases: [Vanacore 2018 attosecond electron control, Vanacore 2018 coherent electron wavefunctions]
created: 2026-11-07
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: method-article
reading_depth: deep-read
title_original: "Attosecond coherent control of free-electron wave functions using semi-infinite light fields"
authors: [G. M. Vanacore, I. Madan, G. Berruto, K. Wang, E. Pomarico, R. J. Lamb, D. McGrouther, I. Kaminer, B. Barwick, F. J. García de Abajo, F. Carbone]
journal: Nature Communications
year: 2018
volume: 9
pages: 2694
doi: 10.1038/s41467-018-05021-x
language: en
canonical_source: doi:10.1038/s41467-018-05021-x
raw_file: "raw/papers/isomer/isomer_application/nuclear battery/2018_Vanacore et al_Attosecond coherent control of free-electron wave functions using semi-infinite light fields.pdf"
raw_sha256: f0cfef202d345d6d8cf9dcb15a91e0d6f0de18fe42de145bd60450a03a78dcfe
archive_required: true
nuclei: []
reactions: []
observables: [electron-energy-gain-spectra, attosecond-pulse-train, quantum-coherent-modulation]
methods: [ultrafast-transmission-electron-microscopy, ponderomotive-phase-modulation, semi-infinite-light-fields]
tags: [electron-wavefunction-engineering, attosecond-physics, electron-optics, external-control-methods, nuclear-excitation-gedankenexperiment]
---

# Vanacore et al. (2018): Attosecond coherent control of free-electron wave functions using semi-infinite light fields

## Bibliographic Record

G. M. Vanacore, I. Madan, G. Berruto, K. Wang, E. Pomarico, R. J. Lamb, D. McGrouther, I. Kaminer, B. Barwick, F. J. García de Abajo, and F. Carbone, "Attosecond coherent control of free-electron wave functions using semi-infinite light fields," *Nature Communications* **9**, 2694 (2018), DOI: `10.1038/s41467-018-05021-x`. Primary PDF is 11 pages, SHA-256: `f0cfef202d345d6d8cf9dcb15a91e0d6f0de18fe42de145bd60450a03a78dcfe`.

## Scope and Reading Depth

The 11-page article was read completely. Reading scope covers ultrafast electron microscopy, ponderomotive phase modulation of 200-keV electrons, synthesis of attosecond electron pulse trains (PDF p. 1--6 / printed p. 1--6, Figs. 1--5), and the discussion subsection "External control of nuclear excitations" (PDF p. 7--8 / printed p. 7--8, Fig. 7e).
**Explicit Boundary**: Contains **no nuclear experimental data or measurements of nuclear isomers**. Documented strictly as electron-optics methodology context.

## Summary

The paper demonstrates longitudinal coherent phase modulation of relativistic free-electron beams (200 keV) interacting with semi-infinite optical fields at a mirror surface. The interaction synthesizes attosecond and zeptosecond electron pulse trains. In the discussion, the authors propose a conceptual gedanken-experiment (Fig. 7e): synchronizing attosecond electron pulse trains with X-ray pulses could dynamically control out-of-equilibrium atomic charge states to manipulate NEEC.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| VA18-1 | Demonstrates coherent longitudinal phase modulation of 200-keV electron beams generating discrete energy sidebands spaced by 1.55 eV. | method-report | direct experimental report | printed p.1--4, Figs. 1--3 | true |
| VA18-2 | Generates periodic trains of attosecond electron pulses via optical near-field phase modulation at a reflective surface. | method-report | direct experimental report | printed p.4--6, Figs. 4--5 | true |
| VA18-3 | Proposes a conceptual gedanken-experiment where attosecond electron pulse trains synchronized with X-rays coherently drive NEEC. | speculative-proposal | theoretical concept | printed p.7--8, Fig. 7e | true |
| VA18-4 | Provides electron-wavefunction engineering foundation for subsequent NEEC-EXI (Gargiulo 2022) and electron vortex (Wu 2022) proposals. | methodology-context | conceptual lineage | printed p.7--8 | true |

## Competing Interpretations and Limitations

The paper is an experimental study of quantum electron optics. Its nuclear excitation discussion is strictly a speculative proposal and should not be cited as empirical evidence for nuclear isomer depletion.

## Extracted Pages

- electron-vortex-beams
- attosecond-physics
- neec

## 2026-11-27 — 馆藏原件与覆盖核对

- 物理第1–4页，书目、引言、200 keV 电子与半无限光场的能量和横向动量交换、图1–3及式(1)–(3)。
- 物理第5–7页，双光脉冲相干调制、傅里叶分析、等离激元近场实验与图4–6。
- 物理第8–9页，X射线模型与图7、External control of nuclear excitations、实验与理论 Methods 开头。
- 物理第10–11页，单双脉冲计算续、数据可用性、参考文献1–47及文末声明。
- 本次获取的具体覆盖：逐页读完物理第1–11页所供文本，含实验结果、计算、核激发讨论、Methods、图1–7图注与文献表。第6–7页部分图内文字存在去重占位符，图像均待核。建议接受同版书目。既有深读条目须修正实验与计算的归类、关键数值和页码，再经图核验收。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A20-1 | 200 keV 自由电子通过受光照射的 Ag/Si₃N₄ 双层镜时，EELS 显示相对零损失峰、以约1.57 eV光子能量为间隔的边带。能量–横向动量图显示同步交换。 | 实验观测 | source-reported | 物理第2页图1，物理第3页图2a–c，物理第4页图3e–g，物理第9页实验 Methods。图2和图3的实验与模拟面板待图核。 | true |
| A20-2 | 作者以500 as步进改变两束锁相光脉冲的相对延迟，测得第9和第14边带强度以约2.6 fs为周期振荡，两者相对相位约为 π。 | 实验观测 | source-reported | 物理第5页 Attosecond coherent control of an electron wave function，物理第6页图4a–c及对应模拟d–f。数据点和拟合待图核。 | true |
| A20-3 | 777 eV 双X射线脉冲模型预测首阶边带约5.3 as的振荡周期及约每511 zs变化1%的相对强度。511 zs 表示预测的强度变化尺度。 | 模型计算 | source-reported | 物理第8页图7a–d及 Zeptosecond coherent control of an electron wave function，物理第10页模拟 Methods。图7计算标签、边带和坐标待图核。 | true |
| A20-4 | 作者提出将经过时间调制的电子与X射线脉冲同步，以采样不同的非平衡电荷态，并以 γ 射线发射变化作为核激发思想实验的读出设想。 | 思想实验 | source-reported | 物理第8页图7e及图注，物理第9页 External control of nuclear excitations。图7e示意内容待图核。 | true |

边带模型以沿电子轨迹的电场积分定义耦合 β，并用贝塞尔函数及双脉冲相干叠加计算概率。按物理第10页式(7)–(10)及模拟说明，计算依赖窄能散、脉冲包络与材料介电参数，拟合采用的光场振幅为实验估计值的 1/1.7。

- 把 VA18-1 的1.55 eV改为约1.57 eV，并将镜面反射形成的半无限传播光场写为主实验的耦合机制。独立的等离激元近场实验见物理第7页图6。
- 把 VA18-2 和摘要的“产生阿秒和仄秒电子脉冲列”改为“实测阿秒延迟步进下的相干谱调制，仄秒调制由X射线模型预测”。将脉冲列从实测量字段移到思想实验说明。图4和图5分别在物理第6、7页。
- VA18-3 改定位为物理第8页图7e及第9页讨论，并把“相干驱动 NEEC”改为“提出通过同步电子和X射线采样非平衡电荷态的核激发思想实验”。本文无核同质异能态测量。
- 移除 VA18-4 的直接谱系归因。本文发表于2018年，所供正文和参考文献无法证明与条目列出的两项2022年工作的继承关系。
