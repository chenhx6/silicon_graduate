---
type: source
title: "吴治华 2005 - 原子核物理实验方法（第三版）"
aliases: [吴治华实验方法, Wu 2005 Experimental Methods, 原子核物理实验方法]
created: 2026-11-01
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: skimmed
title_original: "原子核物理实验方法（第三版）"
authors: [吴治华]
publisher: "原子能出版社"
year: 2005
pages: "483"
isbn: "9787502234058"
canonical_source: "吴治华, 《原子核物理实验方法（第三版）》, 原子能出版社 (2005)"
library_file: "raw/books/原子核物理实验方法--第三版 (吴治华) (Z-Library).pdf"
raw_file: "raw/books/原子核物理实验方法--第三版 (吴治华) (Z-Library).pdf"
raw_sha256: "e23f010ff8d3b4737405235c4aba920533f44e89409ebb7e2cb076b7ab4ee591"
archive_required: true
raw_storage_status: archived-local
nuclei: []
reactions: [in-beam-gamma, coulomb-excitation, rdm, dsam]
experiments: []
models: [detector-efficiency, doppler-broadening, coincidence-matrices]
topics: [hpge-detectors, gamma-spectroscopy, coincidence-measurements, lifetime-measurements, angular-distribution]
---

# 吴治华 2005 - 原子核物理实验方法（第三版）

> 阅读状态修订（2026-11-02）：撤回无逐页记录支持的整书 deep-read。下方旧概述不作为整章已读证据。本轮实际核查范围及需要修订的仪器表述见 [[reconciliation-of-detector-dead-time-and-pulse-pileup]]；仅对所列原件页取得局部阅读记录。


## 专著概况与定位

复旦大学吴治华教授编著的《原子核物理实验方法》是国内低能核物理在束谱学实验的权威经典。不同于通用高能粒子探测器书籍，本书高度针对低能核辐射、束内 $\gamma$ 谱仪阵列、高纯锗（HPGe）探测器性能、符合多道测量系统以及核激发态寿命测量（DSAM/RDM），是设计核物理实验方案与解析离线谱学数据的标准操作宝典。

## 核心章节精要与物理内容

### 第 3 章：半导体探测器与 HPGe 性能（pp. 67–112）
- **HPGe 探测器工作原理**：高纯锗中电离能 $\epsilon \approx 2.96\text{ eV}$（77 K 下），Fano 因子 $F \approx 0.1$，决定了其极致的能量分辨率（1.33 MeV 处 FWHM 可达 1.8–2.0 keV）。
- **死层（Dead layer）与不完全电荷收集**：反向偏压、耗尽区厚度、弹道亏损（Ballistic deficit）与捕获效应引起的低能峰拖尾。

### 第 10 章：$\gamma$ 射线能谱测量与阵列符合（pp. 257–295）
- **$\gamma$ 谱形全要素**：全能峰（Photopeak）、单逃逸峰（SEP: $E_\gamma - 511$ keV）、双逃逸峰（DEP: $E_\gamma - 1022$ keV）、康普顿边缘（Compton edge）与背散射峰（Backscatter peak）。
- **康普顿抑制屏蔽（BGO 抗符合套）**：通过环绕 HPGe 的 BGO 闪烁体探测逃逸光子实施反符合，使峰康比（Peak-to-Compton ratio, P/C）从常规的 40:1 提升至 80:1 以上。
- **绝对与相对全能峰效率校准**：采用标准放射源（如 $^{152}\text{Eu}, {}^{133}\text{Ba}, {}^{60}\text{Co}$），利用多项式对数函数拟合效率曲线：$\ln\epsilon = \sum_{k=0}^n a_k (\ln E_\gamma)^k$。
- **多探头符合阵列（$\gamma-\gamma$ 符合矩阵）**：偶然符合本底扣除、全对称矩阵折叠、选门（Gating）提取级联级联路径。

### 第 15 章：核态寿命的测量（pp. 421–452）
- **电子学延迟符合法**（测 $T_{1/2} > 1\text{ ns}$）：利用 BaF$_2$/LaBr$_3$ 或 HPGe 与时间数字转换器（TDC/TAC）测特征延迟曲线。
- **反冲距离多普勒法（RDM / Plunger 活塞法）**（测 $1\text{ ps} \sim 1\text{ ns}$）：利用高精度压电驱动器控制薄靶与停阻箔间微米级距离，测量非移位峰与移位峰强度比随距离的演化。
- **多普勒频移衰减法（DSAM）**（测 $10\text{ fs} \sim 1\text{ ps}$）：反冲核在厚衬底（如金/铅）中的连续慢化停阻过程，利用实验测量的连续多普勒展宽多峰谱形反演能级平均寿命 $\tau$。

## 对本 Wiki 研究的核心指导价值

1. **实验方案评估与硬件参数校核**：提供靶厚、束流发散角、立体角张角、吸收体厚度估算的规范流程。
2. **数据离线分析技术基准**：建立高效的背景扣除、符合矩阵投影分析与效率归一化链条。
