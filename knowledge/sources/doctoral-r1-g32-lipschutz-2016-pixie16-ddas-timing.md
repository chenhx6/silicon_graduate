---
type: source
title: 'Lipschutz等 2016: 基于Pixie-16的数字获取系统（DDAS）定时与时间游走修正（NIM A）'
aliases: [Lipschutz 2016 DDAS timing, 'arXiv:1601.04579', NIM A 815 1]
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: read
title_original: Digital Data Acquisition For the Low Energy Neutron Detector Array (LENDA)
authors: [S. Lipschutz, R. G. T. Zegers, J. Hill, S. N. Liddick, S. Noji, C. J. Prokop, M. Scott, M. Solt, C. Sullivan, J. Tompkins]
journal: Nuclear Instruments and Methods in Physics Research Section A
year: 2016
volume: 815
pages: 1-6
doi: 10.1016/j.nima.2016.01.050
arxiv: 1601.04579v2
canonical_source: https://doi.org/10.1016/j.nima.2016.01.050
citation_key: ''
raw_file: raw/papers/gpt/query/20261108-foundations-G32/lipschutz-2016-lenda-ddas-timing.pdf
raw_sha256: 466c421c59f5c964b14de545f315c74c1d614a60b78192eb72efe427f75740cc
raw_storage_status: fully-archived-local
archive_required: true
nuclei: []
reactions: []
experiments: [nscl-lenda-ddas, pixie-16-250mhz]
models: []
observables: [time-resolution, time-walk, energy-resolution]
methods: [digital-cfd, fast-trapezoidal-filter, time-walk-correction, linear-vs-cubic-interpolation]
tags: [digital-daq, pixie-16, digital-cfd, time-walk, time-resolution, scintillator]
---

# Lipschutz2016：LENDA的定时算法与探测器限制

## Bibliographic Record

*Digital data acquisition for the Low Energy Neutron Detector Array (LENDA)*，NIMA815,1–6(2016)，正确DOI `10.1016/j.nima.2016.01.050`。
旧`.01.037`指EXIN激光毛细管论文，已撤回；作者列表按本地首页与Crossref校准。
实际六物理页arXiv底本；总控从PDF首页水印核为1601.04579v2，SHA固定实际内容。

## Scope and Reading Depth

G32研学；总控独立读PDF1–4，尤其Eq2–6、Fig1–4及分路/两条探测棒测试区别。
没有波形原始数据、全参数扫描结果或硬件重放。

## Summary

数字CFD的插值与参数优化会影响电子学定时；LENDA棒在高信号幅度时约400ps的限制来自探测器。
分路同信号固定延迟测试不能直接当不同探测器随机到达事件的时间响应。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LI16-1 | LENDA为24条BC408塑闪；此实现用250MSPS、14bit Pixie16 | apparatus | direct-original | PDF1摘要、PDF2 §2 | false |
| LI16-2 | 快滤波后CFD[i+D]=FF[i+D]−wFF[i]；参数单位clock ticks，w无量纲 | algorithm-convention | direct-original | PDF2 Eqs2–3 | false |
| LI16-3 | 单PMT分路加2ns延迟测试对比优化线性与四点三次多项式插值；先作幅度相关walk修正 | reported-test | direct-original | PDF2–3 §4、Figs2–3、Eq4 | false |
| LI16-4 | 两棒22Na测试用四PMT平均时间差，按相等独立响应的约定除√2取单棒分辨；最高能区约400ps，作者认为探测器限制 | reported-test-and-interpretation | direct-original | PDF3–4 §5 Eq5 Fig4 | false |

## Competing Interpretations and Limitations

原文三次法为四点多项式，不直接等同三次样条。
FWHM随脉冲幅度和算法参数变化；不保留未核的“500道即50ps”阈值。
400ps与keVee光输出有关，不能不经响应映射套成HPGe或任意中子能量的性能。
本任务toy采用另一明确CFD延迟/分数约定，不冒充逐行重现本文设置。

## Extracted Pages

[[doctoral-r1-g32-digital-daq-observable-chain-20261108]]用本例说明应分开电子学、探测器及采样相位。

## Agent Self-audit Triage

P0：DOI/作者匹配已改正；PDF1–4方法与测试已核。
P1：完整数据和联合误差未取得；与吴论文是方法比较，不是同一实验的独立重复。
