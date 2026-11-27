---
type: source
title: "A nuclear clock synchronized to 229Th"
aliases: ["huang-2026-nuclear-clock-synchronized-229th", "Beichen Huang 2026"]
created: 2026-11-07
updated: 2026-11-27
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

## 2026-11-27 — 馆藏原件与覆盖核对

- {"from": 1, "to": 5, "sections": "题名页、引言、VUV 光源、晶体制备、荧光与吸收光谱、锁定与稳定度、跨晶体频率比较和结论，含 Fig. 1–3 图注"}
- {"from": 6, "to": 6, "sections": "正文文献 [1]–[48]、出版声明和许可"}
- {"from": 7, "to": 9, "sections": "Methods，含式(2)–(30)、文献 [49]–[51] 及数据、代码和补充材料声明"}
- {"from": 10, "to": 11, "sections": "Extended Data Fig. 1 图注及 Extended Data Table 1 表题和参数释义"}
- 本次获取的具体覆盖：逐页审读 PDF1–11 的供文，覆盖正文、方法、文献 [1]–[51]、图注和文末声明。PDF11 供文仅含表题及符号说明，缺表格数据行。本次仅核文字，图像和表格版面均待检查。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A21-1 | 连续波 148.4 nm 探针锁至 TS1 晶体的 b 线。优化光电管配置的环内频率记录给出重叠 Allan 偏差，测量区间内的拟合为 5 × 10⁻¹³ / √(τ/s)。 | 实验数据拟合 | source-reported | PDF3/905 Fig. 1c,e；PDF5/907 Fig. 3、式(1)。图注明确给出 τ⁻¹ᐟ²，式(1)的根号及图中拟合待查 PDF5。 | true |
| A21-2 | 在 301.4(1) K，两块独立制备晶体 S1 与 TS1 的 b 线中心相差 5.6(13) × 10² Hz，相对差为 2.8(6) × 10⁻¹³。差值的不确定度计入线中心统计误差和残余相对温度不确定度。 | 实验派生量 | source-reported | PDF5/907 跨晶体比较正文；PDF9 Absolute-frequency determination，式(28)列出两条线中心。 | true |
| A21-3 | TS1 的 b 线单洛伦兹拟合 FWHM 为 27(1) kHz。QU 共振激发后的荧光衰减经单指数拟合得到激发态平均寿命 631(2) s。 | 实验数据拟合 | source-reported | PDF2/904 荧光光谱正文；PDF4/906 Fig. 2b,f；PDF7 式(2)、(6)及拟合说明。PDF10 Extended Data Fig. 1 图注另列全谱双洛伦兹拟合。 | true |
| A21-4 | 作者用实测鉴频参数、探测功率和反馈占空比估算优化配置的光子散粒噪声极限，得到 2.9 × 10⁻¹³ / √(τ/s)。 | 噪声模型估算 | source-reported | PDF8 式(20)、(24)及 PDF9 式(25)–(27)。式(27)的根号待查 PDF9，时间标度可由式(26)辨认。 | true |

绝对线中心经频率梳、氢钟及国际原子时校正重建。JILA 比较取文献 [43] 的 C10、C13 数据，按文献 [17] 的二次温度模型在 301.4(1) K 求值，见 PDF9 式(29)–(30)。PDF9 所列 Figshare 数据和绘图脚本 DOI 为 10.6084/m9.figshare.33386191，属于独立归档对象。

- 保留现有条目的图号修订。主图为 PDF3/905 Fig. 1、PDF4/906 Fig. 2、PDF5/907 Fig. 3，旧稿 Fig. 4 定位应删除。
- 保留 12 kHz 为频率调制幅度 δ_b，依据 PDF3 Fig. 1e 图注及 PDF8 Methods。T_m = 10 s 和 T_c = 11.8 s 另有 PDF9 正文支持。f_m = 0.888 kHz 目前沿用旧注的表格读取记录，待查 PDF11 Extended Data Table 1 的优化行。
- 温度记录应写为 301.4(1) K，其中 0.1 K 是传感器校准主导的系统标准不确定度，3 mK 是该次运行的温度时间涨落 RMS，见 PDF5/907。
- Wiki 的 903–913 保留为待核著录。供文可直接确认 PDF1–6 的印刷页码 903–908，PDF7–11 采用物理页定位。检查 PDF11 版面时核对有无印刷末页页码。
- 逐字转录前核对 PDF3 Fig. 1b 的能级字符、PDF5 式(1)和 PDF9 式(27)的根号，以及 PDF7 式(8)、(12)与 PDF8 式(21)–(23)中抽取时易丢失的根号和系数。
