---
type: source
title: "Lotina 2020 - Axial quadrupole-octupole collective Hamiltonian for Kr, Xe and Ba"
title_original: "Microscopic description of nuclear shapes and collective excitations"
aliases: ["Mikroskopski opis oblika i kolektivnih pobudenja atomske jezgre"]
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: masters-thesis
reading_depth: read
authors: ["Luka Lotina"]
year: 2020
institution: "University of Zagreb"
canonical_source: "University of Zagreb Faculty of Science, Master's thesis, Zagreb 2020"
raw_file: raw/theses/gpt/query/20261119-international-nuclear-structure/lotina_luka_2020.pdf
raw_sha256: b381accc0b9f011f34f18f56dbb2b00de79c01667b32bedd770b9b65a42fdd09
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/theses/gpt/query/20261119-international-nuclear-structure/manifest-user-recheck.json
nuclei: ["76Kr", "142Xe", "112Ba", "114Ba", "144Ba", "146Ba", "152Ba"]
tags: ["octupole", "RHB", "QOCH", "DD-PC1", "thesis"]
---

# Lotina 2020：Kr、Xe 与 Ba 的轴向四极–八极集体计算

## Bibliographic Record

Luka Lotina，萨格勒布大学理学院硕士论文，2020 年。76 页原件，正文印刷页为 PDF 页减 9。相关计算见 Nomura、Lotina、Nikšić 和 Vretenar，Phys. Rev. C **103**, 054301（2021），DOI `10.1103/PhysRevC.103.054301`。

## Scope and Reading Depth

已核 75/76 页科研、书证、附录与克罗地亚语扩展摘要。PDF 5 为致谢。另核对相关 PRC 出版版的模型式、核素范围、势能面与可观测量。

## Summary

受约束的相对论 Hartree–Bogoliubov 计算用 DD-PC1 产生轴向 \((\beta_2,\beta_3)\) 势能面，并为量子化四极–八极集体哈密顿量提供质量参数、转动惯量和集体势。作者将模型的低自旋能谱与从 \(1_1^-,2_1^+,3_1^-\) 到 \(0_1^+\) 的下行强度与实验比较。判断稳定性时分别记录 SCMF 极小、集体波函数分布和实验矩阵元。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| LOT-QOCH | RHB 势能面覆盖 \(-0.8\leq\beta_2,\beta_3\leq0.8\)，步长 0.05。轴向 QOCH 使用 \(B_{22},B_{23},B_{33}\)、转动惯量和 \(V_{\rm coll}\)。\(\mu=13\) 从 ⁷²Kr、⁷⁶Kr 能量平坦区选出。它检验该对核素的基展开尺度；单独改变 \(\mu\) 不检验变形网格或 \(\gamma\) 自由度。 | model-input-and-numerical-boundary | direct-original-pages | 学位 PDF 25–29、39–42，式 2.47–2.66、图 3.13–3.15 |
| LOT-PES | 表 3.1 的非零 \(\lvert\beta_3\rvert\) 网格极小包括 ⁷⁶Kr 和 ¹⁴²Xe 的 0.05、¹¹²,¹¹⁴Ba 的 0.15，以及 ¹⁴⁴–¹⁵²Ba 的五个偶偶同位素。⁷⁶Kr、¹⁴²Xe、¹⁵²Ba 的报告能量降低量约为 3.7、31.6、1.3 keV。PDF 39 将 \(E_{\rm oct}\) 定义为 \(E_{\min}-E_{\rm quad}\)，图和文字却给正值；按降低量绝对值引用。 | calculated-minima-and-sign-audit | direct-original-pages-and-inequality | 学位 PDF 30–35、39，表 3.1、图 3.4–3.12 |
| LOT-VERSION | 学位式 2.64 的振动零点修正写成 \(\frac14\mathrm{Tr}(M_{(3)}^{-1}M_{(2)})\)，式 2.66 还减转动零点修正。PRC 式 11 写 \(\frac14\mathrm{Tr}(M_{(2)}^{-1}M_{(1)})\)，集体势段落写减振动零点能。按版本引用公式，程序实现保留为待核。 | formula-and-version-audit | direct-original-pages | 学位 PDF 28，式 2.62–2.66；PRC PDF 3，式 9–11 |
| LOT-SPEC | 多个 Xe、Ba 的低位正宇称能量和 \(B(E2)\) 与实验接近。Kr 以及若干近壳闭合体系偏差更明显，负宇称能量常偏高。对 ¹⁴⁴,¹⁴⁶Ba 的 \(B(E3)\) 比较受实验误差制约；其输入来自 [[bucher-2016-144ba-direct-octupole]] 与 [[bucher-2017-146ba-direct-octupole]]，两个库仑激发实验分别保留。 | theory-data-comparison | direct-original-pages | 学位 PDF 43–55，图 3.16–3.22、引文 35–36；PRC PDF 6–10，图 5、7–11 |
| LOT-FLUCT | 相关 PRC 的轴向 QOCH 以 \(\sqrt{\langle\beta_\lambda^2\rangle}\) 和相对涨落描述 \(0_1^+\) 波函数，另展示 ¹⁴⁴Ba 两种宇称的概率分布。文中指出近 \(N=82\) 的部分相对涨落峰受很小的分母影响。 | calculated-collective-distribution | direct-original-pages | PRC PDF 6、9、11，图 6、13 |

## Competing Interpretations and Limitations

- \(|\beta_3|=0.05\) 仅比轴上点偏一个网格步长。浅极小的稳定性需要更细的二维势能面、集体惯量和波函数分布检验。比较用的反射对称点在相同 \(\beta_2\) 上，给出的八极能量降低量不是到最优对称形状的最低势垒。学位 PDF 29、34、39。
- [[doctoral-r1-g27-clement-2007-prc-krypton-coulex]] 的独立 E2 网络约束了 ⁷⁶Kr 的形状混合解释，尤其 \(2_1^+\) 的 \(Q_s=-0.7(2)\) eb。轴向势能面的单点不能直接给该激发态矩。比较必须经过可观测量和态匹配。CoulEx 原文 PDF 11，表 V–VI。
- 期刊把 Ce 和中子丰 Se/Kr/Sr 纳入专题，势能面近 \(N=56\) 的图保留 ¹¹²,¹¹⁴Ba，近 \(N=88\) 的图保留 ¹⁴⁴–¹⁵²Ba。它与学位论文共享作者和 RHB–QOCH 建模框架，比较中保留不同核素覆盖与公式。PRC PDF 3–5，图 1–4。
- 学位 PDF 10 的 \(E1\) 概述应分清普通异宇称 \(E1\) 跃迁与静态电偶极矩。单个 \(E1\) 跃迁强度无法建立 \(T\) 或 \(CP\) 破坏。Schiff 矩问题参见 [[dobaczewski-2005-ra225-schiff]]。

## Extracted Pages

- 学位 PDF 1–4、6–28：书证、背景、RHB 和 QOCH 的公式。
- 学位 PDF 29–55：势能面、结合能、网格、基参数、谱与电磁跃迁比较。
- 学位 PDF 56–76：轴谐振子基的 RHB 附录、克罗地亚语扩展摘要与书目。
- PRC 出版版 PDF 1–13。原件和哈希见 `raw/papers/gpt/query/20261120-lotina-qoch-crosswalk/manifest.json`。
