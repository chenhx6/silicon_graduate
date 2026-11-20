---
type: source
title: "DeGraaf 1997 - Lifetimes in 114Xe and 116Xe"
title_original: "Nuclear Structure Studies in Highly Neutron-Deficient 114,116Xe"
aliases: []
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: doctoral-thesis
reading_depth: read
authors: ["James H. DeGraaf"]
year: 1997
institution: "University of Toronto"
canonical_source: "University of Toronto doctoral thesis, 1997"
raw_file: raw/theses/gpt/query/20261119-international-nuclear-structure/W1615955459.pdf
raw_sha256: f109994a494383a4a8f153e8e259d6f0dd9dd2ed3557a3671e8427e353314dc3
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/theses/gpt/query/20261119-international-nuclear-structure/manifest-acquisition-batch1.json
comparison_manifest_file: raw/papers/gpt/query/20261120-degraaf-xe-rdds-crosswalk/manifest.json
comparison_manifest_sha256: 608a05345759c3405acca6d636b7ba5f0153a74566c0e3567e75defbea687715
evaluations_manifest_file: raw/papers/gpt/query/20261120-degraaf-xe-rdds-crosswalk/manifest-ensdf.json
evaluations_manifest_sha256: 14ac55dc7e2080a2069731af0db09b868124bc77699a2daa17a162c7adfd4e0d
nuclei: ["114Xe", "116Xe", "112Te", "114Te"]
tags: ["RDDS", "lifetime", "feeding", "quadrupole-collectivity", "octupole", "thesis"]
---

# DeGraaf 1997：¹¹⁴,¹¹⁶Xe 的反冲距离寿命

## Bibliographic Record

James H. DeGraaf，University of Toronto 博士论文，1997 年，143 页。对应 Phys. Rev. C **58**, 164（1998），`10.1103/PhysRevC.58.164`，另有 Phys. Rev. C **59**, 1818（1999）勘误，`10.1103/PhysRevC.59.1818`。两条目前核至正式书目，勘误的具体订正未取得。对照 Lakenbrink 等 Eur. Phys. J. A **59**, 290（2023）独立实验，`10.1140/epja/s10050-023-01204-3`，及早期 ENSDF 评价。原件见两份对照清单。

## Scope and Reading Depth

覆盖 140/143 页科研与书证范围。PDF 2 的版权复印声明、PDF 4 的致谢和 PDF 143 的扫描靶页不计。正文印刷页 = PDF 页减 7。旧扫描中常把 Xe 识别成 Se，寿命、强度和核素回到图表核对。

## Summary

Chalk River 的 8π 装置通过 BGO 总能和多重性增强 \(2p\) 产物通道。基于 γ 单谱的 RDM 分析在各距离拟合全移与减速分量，显式处理慢化、效率、取向衰减及侧馈。较新的科隆装置用符合门隔离馈入，并对与停止时间相近的短寿命改用谱形模拟。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| DEG-RUN | ¹¹⁴Xe、¹¹⁶Xe 分别用 215 MeV 的 ⁵⁸Ni(⁵⁸Ni,2p) 和 223 MeV 的 ⁵⁸Ni(⁶⁰Ni,2p)。RDM 取 13、18 个距离，分别约 10–6000、5.3–6000 μm。金箔减速后反冲仍在运动，晚分量依然有 Doppler 位移。 | reaction-and-response | direct-original-pages | 学位 PDF 53–55、79–82，图 3.11–3.12，§4.2 |
| DEG-FEED | RDM 的单谱拟合用已见级联和有效侧馈态。常见处理是高能段先拟合共同侧馈寿命，再向下固定，重要未知馈入另放自由参数。在 ¹¹⁴Xe，555 keV 的 \(3^-\) 出射线与 376 keV 馈入的曲线难以区分，主要靠下游 619/450 keV 线的拟合约束，直接 555 keV 曲线允许零寿命。 | correlated-feeding-and-resolution | direct-original-pages | 学位 PDF 61–69、75–78、89–91，图 4.8–4.9，表 4.1 |
| DEG-XE | 学位表 4.2 的 ¹¹⁴Xe \(2^+,4^+\) 平均寿命为 23.8(16)、4.9(3) ps，\(B(E2)\) 均约 \(0.184\ (eb)^2\)。表 4.4 的 ¹¹⁶Xe \(2^+,4^+,6^+,7^-\) 为 35.1(13)、4.8(2)、2.4(2)、3.0(12) ps，前两条 \(B(E2)\) 中心值之比约 1.78。 | measured-and-derived-values | direct-original-pages-and-arithmetic | 学位 PDF 91、95–96，表 4.1–4.4 |
| DEG-INDEP | Lakenbrink 的 ¹⁰²Pd(¹⁶O,2n)，62 MeV，是不同实验。取上方移峰门的符合 DDCM 给 ¹¹⁶Xe \(2^+,4^+\) 的 38.0(4)、5.4(2) ps，原学位中心值分别低约 2.1 个独立报告标准差。其 \(B_{4/2}=1.70(7)\) 与学位中心尺度相近。 | independent-lifetime-comparison | direct-original-pages-and-arithmetic | 学位 PDF 95–96；EPJ A PDF 2–6，式 1，表 1、3 |
| DEG-SHORT | 科隆的 \(6^+,7^-\) 寿命与停止时间可比。谱形模拟给 3.3(10)、2.3(10) ps，采用这两值而非 DDCM 的 1.4(9)、0.7(5) ps。911.6 keV \(7^-\to6^+\) 的 \(B(E1)=2.8^{+2.1}_{-0.9}\times10^{-4}\ e^2\mathrm{fm}^2\) 仍沿用 DeGraaf 的 0.78(8) 分支。 | independent-lifetime-shared-branching | direct-original-pages | EPJ A PDF 4–6，表 2–3、图 8 |
| DEG-K | 负宇称带的 \(Q_0(K)\) 以转子关系换算。¹¹⁴Xe \(5^-\) 的假定 \(K=3\) 给 606(34)，\(K=0\) 给 320(18)，与基带 304(11) 比较（\(e\,\mathrm{fm}^2\)）。作者在振动带与基带形变近似的前提下偏好低 \(K\)。不同 \(K\)、Coriolis 混合和八极振动与带间 \(E1\) 的关系须一起判断。 | conditional-model-comparison | direct-original-pages | 学位 PDF 105–114，表 4.5–4.6，图 4.16–4.17 |

## Competing Interpretations and Limitations

- ¹¹⁴Xe ENSDF 评价 PDF 1 对 1623.8 keV \(3^-\) 采用 \(T_{1/2}=8.3(21)\) ps，来源 2002De26，对应 \(\tau\approx12.0(3.0)\) ps。这个值与学位前后环拟合的 7.9(63)、5.3(32) ps 分开存。¹¹⁶Xe 已存 ENSDF 的截止日期为 2009-12-01，早于 2023 年科隆实验。
- ¹¹⁴Xe 的 619 keV 移峰受到邻道 ¹¹³I 的减速分量干扰。¹¹⁶Xe 的 394 keV 归一也与 ¹¹⁵I 的 411 keV 分量相干扰。不同环的同一寿命拟合共享馈入和部分校准，报告误差不能自动视为完全独立。
- ¹¹⁶Xe 的 2023 年 \(E1\) 可以约束八极关联。该文没有 ¹¹⁶Xe 的直接 \(E3\) 强度；引用的强 \(E3\) 来自 ¹¹⁴Xe。增强 \(E1\) 与静态八极形变之间仍需额外观测。学位 Appendix A 的 ¹¹²,¹¹⁴Te 则展示慢馈入会使低能级 singles 寿命难以辨识，高旋寿命另行报告。

## Extracted Pages

- 学位 PDF 1、3、5–35：原件身份、动机及电磁、单粒子与集体理论。
- 学位 PDF 36–114：8π、减速箔、RDMFIT、Xe 能级谱与前后环时间曲线、八极讨论。目视 PDF 91、95–96、111–113。
- 学位 PDF 115–142：Te 反例、全部衰变曲线附录与参考文献。
- 独立期刊 PDF 1–6 为定向比较，关键表 3 已目视。1998 期刊和 1999 勘误目前仅使用书目，ENSDF 作为版本有日期的评价层。
