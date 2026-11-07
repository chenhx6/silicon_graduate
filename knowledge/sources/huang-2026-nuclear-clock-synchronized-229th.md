---
type: source
title: "A nuclear clock synchronized to 229Th"
aliases: ["huang-2026-nuclear-clock-synchronized-229th", "Beichen Huang 2026"]
created: 2026-11-07
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: experiment-article
reading_depth: deep-read
title_original: "A nuclear clock synchronized to 229Th"
authors: ["Beichen Huang", "Gaowei Yan", "Qi Xiao", "Wenhao Bu", "Chengchun Zhao", "Zhen Zhang", "Chao Yan", "Zhi-Ang Chen", "Peixiong Zhang", "Gleb Penyazkov", "Zhenhai Zhan", "Lingfeng Yan", "Yuefei Wang", "Lin Li", "Shanming Li", "Dapeng Jiang", "Xiaobo Qian", "Xuegang Liu", "Qiange He", "Taoxiang Sun", "Haochen Tian", "Bingkun Lu", "Ningyuan Ma", "Juxian Li", "Yanzhang Wu", "Qiaorui Gong", "Yuxiang Li", "Haoyu Shi", "Xiangliang Li", "Longsheng Ma", "Shining Zhu", "Yuxiang Mo", "Jun Lin", "Li You", "Yige Lin", "Xibo Zhang", "Yin Hang", "Liangbi Su", "Shiqian Ding"]
journal: "Nature"
year: 2026
volume: "658"
pages: "903--913"
doi: "10.1038/s41586-026-11122-1"
canonical_source: "doi:10.1038/s41586-026-11122-1"
raw_file: "raw/papers/isomer/isomer_application/nuclear_clock/2026_Huang et al_A nuclear clock synchronized to 229Th.pdf"
raw_sha256: "9fc65f07dd7dadf3aedcff90612d6af299ab327ee0a60d767f88cca78a4f0788"
archive_required: true
nuclei: ["229th"]
observables: []
methods: []
tags: ["229th", "isomer", "nuclear-clock", "vuv-spectroscopy"]
---

# A nuclear clock synchronized to 229Th

## Bibliographic Record

- **Citation**: Beichen Huang, Gaowei Yan, Qi Xiao, Wenhao Bu, Chengchun Zhao et al., *Nature* **658**, 903--913 (2026). DOI: `10.1038/s41586-026-11122-1`.
- **Local Raw File**: `raw/papers/isomer/isomer_application/nuclear_clock/2026_Huang et al_A nuclear clock synchronized to 229Th.pdf`
- **File SHA-256**: `9fc65f07dd7dadf3aedcff90612d6af299ab327ee0a60d767f88cca78a4f0788`
- **Physical Page Count**: 11 pages.

## Scope and Reading Depth

本次对象为frontmatter指定的本地PDF，页数及实际读取范围见本轮clock逐文件台账。关键主张依下表原页定位；未在该PDF中实际检查的独立SI、原始计数和装置文件不自动包含在核验范围。

2026-11-08 R3总控回读PDF1–5、8–9、11，并视觉核Extended Data Table 1。
原印刷页与图位置重新对应：Fig.1在PDF3/905，Fig.2在PDF4/906，
Fig.3在PDF5/907；本文主图止于Fig.3，不沿旧稿“Fig.4”。
12kHz是优化配置的频率调制**幅度**δb，调制频率fm=0.888kHz，
不是12kHz调制频率或反馈带宽。PDF11表1给Tm=10s、Tc=11.8s。

## Summary

Huang et al. (online 7 October 2026; Nature Vol.658, pp.903–913, 22 October 2026)
report feedback locking of a continuous-wave 148.4nm probe to line b in 229Th:CaF2.
The optimized configuration uses a phototube for transmission readout,
fm=0.888kHz and frequency-modulation amplitude δb=12kHz.
The in-loop frequency record gives fitted instability
5×10⁻¹³/√(τ/s); independent-crystal comparison gives 5.6(13)×10²Hz difference.
Neither quantity alone is a complete accuracy budget or a direct measurement of nuclear T2.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| H26-1 | In-loop overlapping Allan deviation fitted by 5×10⁻¹³/√(τ/s) over measured interval. | derived-measurement | direct | PDF5/907, Eq.(1), Fig.3 | false |
| H26-2 | Independent-crystal line-b difference 5.6(13)×10²Hz. | derived-measurement | direct | PDF5/907 text; PDF9 Eqs.(28)–(30) | false |
| H26-3 | Optimized phototube readout uses fm=0.888kHz, δb=12kHz, Tm=10s, Tc=11.8s. | apparatus-input | direct-visual | PDF11, Extended Data Table 1 | false |
| H26-4 | Single-exponential fluorescence mean decay time τe=631(2)s, following QU excitation. | fitted-measurement | direct | PDF2/904 text; PDF4/906 Fig.2f | false |

## Competing Interpretations and Limitations

局域环境、谱展宽与温度进入结果。PDF5报告301.4(1)K，
3mK为该次运行的RMS时间涨落，0.1K为传感器校准主导的系统标准不确定度；
不是所有核钟的mK必要条件。27(1)kHz是TS1 b线FWHM（PDF2/904），
不能直接反推均匀T2。本文未提供独立于环内记录的完整钟稳定性测量或10⁻¹⁹精度证明。

## Extracted Pages

- [[huang-2026-nuclear-clock-synchronized-229th]]
- [[nuclear-clock-isomer-learning-and-transfer-20261107]]
