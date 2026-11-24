---
type: source
title: "Pandit et al. 2012 - Critical behavior in the variation of GDR width at low temperature"
aliases: [Pandit 2012 GDR thermal width, GDR width critical behavior TSFM, PAN12]
created: 2026-10-30
updated: 2026-11-22
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Critical behavior in the variation of GDR width at low temperature"
authors: [D. Pandit, S. Mukhopadhyay, S. Pal, A. De, S. R. Banerjee]
journal: Physics Letters B
year: 2012
volume: 713
issue: "4-5"
pages: "434-438"
doi: "10.1016/j.physletb.2012.06.033"
canonical_source: "https://doi.org/10.1016/j.physletb.2012.06.033"
citation_key: pandit2012gdr
raw_file: "raw/papers/gpt/learning-daily/20261031-OPEN-RESEARCH-source-recovery/1-s2.0-S0370269312006594-main.pdf"
raw_sha256: e05ec85afd0ea75ae49a678a11ba86f02f5599bfdee98c1000b79c4df6df5aac
nuclei: [201tl, 63cu, 119sb, 120sn, 208pb]
reactions: ["alpha + 197Au @ 35/42/50 MeV", "alpha + 59Co @ 35 MeV"]
experiments: [VECC-Kolkata-LAMBDA-BaF2]
models: [thermal-shape-fluctuation-model, critical-temperature-included-fluctuation-model, phonon-damping-model]
observables: [GDR-width, gamma-cross-section, nuclear-temperature, angular-momentum]
methods: [high-energy-gamma-spectroscopy, statistical-model-CASCADE, TSFM-Monte-Carlo]
tags: [giant-dipole-resonance, thermal-width, shape-fluctuations, TSFM, 201Tl, 63Cu, Day27]
---

# Critical behavior in the variation of GDR width at low temperature

## Bibliographic Record

PLB 713, 434-438 (2012), DOI `10.1016/j.physletb.2012.06.033`.

## Scope and Reading Depth

核对刊版物理 PDF1–5，对应印刷 pp.434–438。包括新实验、CASCADE 线宽提取、既有数据比较、Figs. 1–4、Eqs. (1)–(2) 与结论。已引用的旧数据和响应标定各自保留独立来源范围。

## Summary

本篇新实验为 \(^{201}\mathrm{Tl}\) 和 \(^{63}\mathrm{Cu}\)，用高能 γ 谱拟合提取 GDR 宽度。\(^{119}\mathrm{Sb}\)、\(^{120}\mathrm{Sn}\) 与 \(^{208}\mathrm{Pb}\) 来自引用文献。作者提出巨偶极振动诱发的四极形变与热形变涨落竞争，并据此修订热宽现象学参数化。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PAN12-1 | VECC 用 α 束轰击197Au及59Co，LAMBDA与多重性选择记录201Tl及63Cu的高能γ谱。Fig. 2把本篇测量和既有119Sb、120Sn、208Pb数据分别标出。 | experimental-result | source-reported | PDF1 abstract, PDF2 methods, PDF3 Fig. 2 | false |
| PAN12-2 | 201Tl 的五个拟合宽度为3.4、3.7、3.8、4.6、4.5 MeV，对应估计平均温度0.82、0.94、0.97、1.09、1.12 MeV。宽度误差估计为 ±0.45 MeV。宽度源于对折叠响应的谱拟合，温度源于统计模型。 | derived-observable | source-reported | PDF2–3 Fig. 1 and analysis paragraphs | false |
| PAN12-3 | CTFM 规定零自旋宽度在 \(T\leq T_c\) 时为 \(\Gamma_0\)，在高温端为 \(\Gamma_0+c(A)\ln(T/T_c)\)，并采用 \(T_c=0.7+37.5/A\)、\(c(A)=8.45-A/50\)。式 (2) 给出另外的自旋缩放。 | empirical-model | direct-to-model | PDF4 Eq. (1), PDF5 Eq. (2) | false |
| PAN12-4 | 作者用 GDR 诱发形变与热形变涨落竞争解释低温宽度，并提出用 GDR 到 \(2^+\) 态的衰变分支检验耦合。原文把这一联系作为待进一步检验的解释。 | author-interpretation | direct-to-source | PDF4 Fig. 3 and discussion; PDF5 summary | false |

## Competing Interpretations and Limitations

低温端比较涉及带壳效应的 TSFM 与含热配对的声子阻尼模型，两者在本文的208Pb比较中不能复现所有低温宽度趋势。参数化阈值由该数据和模型定义。早期 Wiki 的「本文新测119Sb」「普适配对塌缩温度」和「208Pb 双体碰撞占主导」均已撤回原文归属。

## Extracted Pages

- [[gdr-thermal-width-expansion-and-tsfm-inapplicability]] 保存历史模型练习的证据边界。
