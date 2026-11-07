---
type: source
title: "Decay spectroscopy of 129Cd"
aliases: [Saito2020, Saito 2020 PRC, 129Cd TRIUMF GRIFFIN decay]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Decay spectroscopy of 129Cd"
authors: [Y. Saito, I. Dillmann, R. Krücken, N. Bernier, G. C. Ball, M. Bowry, C. Andreoiu, H. Bidaman, V. Bildstein, P. Boubel, C. Burbadge, R. Caballero-Folch, M. R. Dunlop, R. Dunlop, L. J. Evitts, F. H. Garcia, A. B. Garnsworthy, P. E. Garrett, H. Grawe, G. Hackman, S. Hallam, J. Henderson, S. Ilyushkin, A. Jungclaus, D. Kisliuk, J. Lassen, R. Li, E. MacConnachie, A. D. MacLean, E. McGee, M. Moukaddam, B. Olaizola, E. Padilla-Rodal, J. Park, O. Paetkau, C. M. Petrache, J. L. Pore, A. J. Radich, P. Ruotsalainen, J. Smallcombe, J. K. Smith, C. E. Svensson, A. Teigelhöfer, J. Turko, T. Zidar]
journal: "Physical Review C"
year: 2020
volume: 102
pages: "024337"
doi: "10.1103/PhysRevC.102.024337"
language: en
canonical_source: "doi:10.1103/PhysRevC.102.024337"
citation_key:
raw_file: "raw/papers/gpt/query/20261107-continuation-G19/Saito_2020_PRC_102_024337_129Cd_decay.pdf"
raw_sha256: 817dd7ed60e57341c46697887a37481564c3887b104b7cc9cec9427e1e004399
archive_required: true
nuclei: [129cd, 129in, 132sn, 128cd, 130cd]
reactions: [480mev-proton-induced-fission-ucx]
experiments: [triumf-isac-griffin-sceptar-iglis]
models: [shell-model, oxbash, na-14, cd-bonn, v-low-k]
observables: [beta-decay-half-life, beta-feeding-intensity, log-ft, gamma-ray-energy, level-energy, gamow-teller-strength]
methods: [beta-gamma-gamma-coincidence, high-purity-germanium-clover, high-resolution-gamma-spectroscopy]
tags: [isomer-beta-decay, gamow-teller, first-forbidden, 129cd, 129in, griffin-spectrometer, beta-feeding-fragmentation, pandemonium-effect]
---

# Saito2020：TRIUMF-GRIFFIN高分辨129Cd同核异能态β衰变谱学

## Bibliographic Record

Y. Saito et al., Physical Review C 102, 024337 (2020)，DOI: 10.1103/PhysRevC.102.024337。
实际本地原件：arXiv:2008.02959v1，13物理页，SHA-256: `817dd7ed60e57341c46697887a37481564c3887b104b7cc9cec9427e1e004399`。

## Scope and Reading Depth

### Covered scope

通读13页全文：
1. 实验方法：TRIUMF-ISAC利用480 MeV质子轰击UCx靶，IG-LIS激光电离提取129Cd，由GRIFFIN阵列（16个HPGe clover）联合SCEPTAR闪烁探测器进行高精度β-γ-γ符合分析（第2页）。
2. 母态参数：基态 $J^\pi = 11/2^-$（$T_{1/2} = 147(3)\,\text{ms}$），同核异能态 $3/2^+$（$E_x = 343(8)\,\text{keV}$，由ISOLTRAP质谱测定，Manea 2020 PRL 124, 092502；$T_{1/2} = 157(8)\,\text{ms}$，直接采纳同批GRIFFIN数据的Dunlop 2016 PRC 93, 062801(R)结果）；基态 $Q_\beta = 9780(17)\,\text{keV}$（采纳自AME2016，与Manea 2020属于不同评估版本，不可在缺乏协方差下直接合成异能态 $Q$ 误差）。
3. 能级与衰变纲图扩展：识别出101条跃迁（含32条新跃迁）与38个激发态（含7个新能级）；建立 $17/2^-$ 异能态半衰期 $T_{1/2} = 10.8(1)\,\mu\text{s}$（第4页）。
4. Table II完整数据：给出40个激发能级逐态馈送强度 $I_\beta(11/2^-)$、$I_\beta(3/2^+)$ 及 $\log ft$，与Taprogge 2015全面对比；未观测到馈送的母态列在原表中均为空白，不可主观臆造上限。
5. GT分布与壳模型比较：对比OXBASH采用“NA-14”相互作用（CD-Bonn经 $V_{\text{low}-k}$ 重整化及经验多极修正）并取 $q=0.75$ 淬灭因子的两母态GT强度碎裂分布（FIG. 9）；该模型仅计算 $\nu 0g_{7/2} \to \pi 0g_{9/2}$ 允许GT跃迁，未微观计算一阶禁戒弱算符。
6. 模型局限与核结构机制：揭示模型空间截断（缺少质子完整 $N=4$ 主壳及 $\nu j \to \pi j$ 巨共振组态）导致绝对GT强度系统性高估；高能区Pandemonium效应对实测强度的潜在影响。

### Not covered

不包含事件级列表模式原始数据；文中未报告也未测定 $^{129}\text{Cd}$ 的缓发中子发射几率 $P_n$（不可主观虚构 $P_n \approx 10-15\%$）；不包含一阶禁戒跃迁的微观形状因子与算符矩阵元计算（仅依据标准允许程序计算的 $\log ft$ 和选择定则定性推断）。

## Key Findings and Data

1. **两母态近等半衰期背后的非简并衰变机制**：
   - $11/2^-$ 母态（$147(3)\,\text{ms}$）：主要通过强允许GT跃迁 $\nu 0g_{7/2} \to \pi 0g_{9/2}$ 馈送到 $3150\,\text{keV}$ 的 $(13/2^-)$ 模型中以三孔成分为主的态（$\pi g_{9/2}^{-1} \nu(g_{7/2}^{-1} h_{11/2}^{-1})$ 组态占 92%，$I_\beta = 45(10)\%$（按11/2−母态归一；对全部母态混合衰变为24.1(9)%），$\log ft = 4.34(10)$），并有显著的一阶禁戒分支 $\nu 0h_{11/2} \to \pi 0g_{9/2}$ 馈送低激发态 $9/2^+$（基态）、$11/2^+$（$995\,\text{keV}$）、$13/2^+$（$1354\,\text{keV}$）。
   - $3/2^+$ 异能态（$157(8)\,\text{ms}$）：允许GT跃迁高度碎裂，分布于 $(5/2^+)$ $3184\,\text{keV}$（$I_\beta = 22(6)\%$（按3/2+母态归一；对全部衰变为10.4(5)%），$\log ft = 4.77(12)$）、$3347\,\text{keV}$（$I_\beta = 13(3)\%$（按3/2+母态归一；对全部衰变为6.1(4)%），$\log ft = 4.95(11)$）以及文中讨论的高激发候选态 $3701$、$3888$、$3971$、$4082$、$4118\,\text{keV}$；一阶禁戒分支 $\nu 1d_{3/2} \to \pi(1p, 0f_{5/2})$ 馈送 $1/2^-$（$451\,\text{keV}$）、$(3/2^-)$（$1082\,\text{keV}$）、$(5/2^-)$（$1220\,\text{keV}$）。
2. **两母态寿命相近与有效 $g_A$ 的关系**：
   - 两个母态半衰期均在 $\sim 150\,\text{ms}$，但初末态组态重叠、允许GT跃迁碎裂程度与一阶禁戒贡献完全不同。不能从相近总寿命反推存在唯一的介质有效弱相互作用算符或标称 $g_A$。



## Parent normalization audit

总控回读实际arXiv2008.02959v1的PDF8–10及TableII，核对总混合归一与母态归一、上限和空白。
正文中的GT/FF组态属于作者模型/候选解释，不能把低logft独自当唯一分类。
完整原始Cov与事件没有公开归档；原表转录不计作另一次实验。


## Summary

本页记录该原件实际提供的实验/模型信息与读取边界；核心数据/公式沿用上文原表locator，不作为新实验或作者代码复现。


## Competing Interpretations and Limitations

模型参数和解释不等于实验直接测量；原文未报告不等于严格为零或全球不存在。局部比较不能排除全部模型族，适用条件与缺失响应沿用本页记录。


## Extracted Pages

实际读取的PDF/出版页、XML原文段及表号见Scope和逐项locator；全文文件可用不代表全部图点/转引原件或生产实现已核。


## Key Results

| ID | 内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SA20-1 | 3150keV Iβ总混合归一24.1(9)%、11/2−母态归一45(10)% | experimental-derived-observable | direct | arXiv2008.02959v1 PDF10 TableII | false |
| SA20-2 | 147(3)、157(8)ms采纳同批GRIFFIN数据的Dunlop分析 | source-lineage | direct | 同版本PDF8 SecIVB | false |
