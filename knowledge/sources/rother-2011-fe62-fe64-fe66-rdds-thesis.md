---
type: source
title: "Rother 2011 - 62,64,66Fe fast-beam RDDS lifetimes"
title_original: "Lifetime Measurements in 62,64,66Fe"
aliases: []
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: doctoral-thesis
reading_depth: read
authors: ["Wolfram Rother"]
year: 2011
institution: "Universität zu Köln"
canonical_source: "University of Cologne dissertation, 2011, Verlag Dr. Hut; examination 2011-04-08"
raw_file: raw/theses/gpt/query/20261119-international-nuclear-structure/Arbeit.final.pdf
raw_sha256: 1e711e219ee9eed9b4a78159af756910747d27e86e1ca266fdc53a9f0fa855e9
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/theses/gpt/query/20261119-international-nuclear-structure/manifest-user-recheck.json
nuclei: ["62Fe", "64Fe", "66Fe"]
tags: [RDDS, fast-beam, shell-evolution, thesis]
---

# Rother 2011：⁶²,⁶⁴,⁶⁶Fe 的快束 RDDS 寿命

## Bibliographic Record

Wolfram Rother，科隆大学博士论文，2011 年出版，原件 107 页。PDF 2 载 2011 年 4 月 8 日口试。正文印刷页比 PDF 小 2。相关 Phys. Rev. Lett. **106**, 022502（2011）APS CHORUS 录用稿载同一实验，DOI `10.1103/PhysRevLett.106.022502`。

## Scope and Reading Depth

已核 98/107 页科学正文、身份、附录和书目。分隔、致谢、声明与履历页留原件。另核验 5 页 APS CHORUS 录用稿，其中含出版社封面。

## Summary

论文用 NSCL 的快碎片束、S800 粒子鉴别、SeGA 前后两环和 Köln/NSCL plunger，以快慢 Doppler 谱线的相对面积随距离演化估计 \(2_1^+\) 的平均寿命。减速片再次激发贡献与靶后的飞行衰变都可进入慢分量，需分别建模。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| ROT-TAU | 期刊表 I 对 ⁶²,⁶⁴,⁶⁶Fe 报 \(\tau=8.0(10),10.3(10),39.4(40)\) ps。学位表 4.7 的 ⁶²Fe 行给 7.8(10) ps，学位表 5.2 与期刊一样给 8.0(10) ps。 | measurement-and-version-audit | direct-original-pages | 学位 PDF 59、74；期刊录用稿 PDF 4，表 I |
| ROT-E2 | 期刊表 I 报 \(B(E2;2_1^+\to0_1^+)=198(25),344(33),332(34)\,e^2\mathrm{fm}^4\)。用表列 \(E_\gamma\)、寿命和学位 §5.1 的系数复算中心值为 197.5、344.4、331.0，舍入和能量精度内一致。 | measured-quantity-and-arithmetic-check | direct-original-pages-and-arithmetic-check | 学位 PDF 65、74；期刊录用稿 PDF 4 |
| ROT-PID | ⁷⁶Ge 碎裂束经 A1900 选择。入射时间门和 S800 的出射飞行时间–能损门分别应用，出射时间还经过轨迹相关订正。⁶⁶Fe 示例显示 ⁶⁷Co 污染在入射门后受压制。 | experimental-selection | direct-original-pages | 学位 PDF 14–15、35–41，图 3.3–3.7 |
| ROT-VELOCITY | 对 ⁶⁴,⁶⁶Fe，靶前、靶后和减速片后的速度锚定 LISE++ 插值。⁶²Fe 靶后 \(v/c=0.368(4)\) 来自快峰拟合。谱形按靶内、间隙、减速片内与片后离散，各段的存活与衰变权重进入能量响应。 | experimental-input-and-response | direct-original-pages | 学位 PDF 49–52，表 4.1–4.2；PDF 79–90，式 A.1–A.24 |
| ROT-DEG | 学位附录把靶和减速片激发的谱形相加。\(D\) 表示减速片对靶的激发比。式 A.23 另乘 \(\Delta_T/\Delta_D\)，A.1 将 \(\Delta_*\) 定义为各区间分段的长度。表 4.7 对 ⁶²,⁶⁴,⁶⁶Fe 分别给 \(D=0.49,\ 0.77(5),\ 0.40(5)\)。期刊的约 30%–40% 对应长距离谱约束的产额比例。 | conditional-response-and-nuisance | direct-original-pages | 学位 PDF 53–59、79、90，式 A.22–A.24；期刊录用稿 PDF 3 |

## Competing Interpretations and Limitations

- ⁶⁶Fe 两环、多距离一起拟合。⁶⁴Fe 的同时拟合未收敛，先拟 30°，再在固定 \(\tau,D\) 时定 140° 对应参数，之后扫描寿命。⁶²Fe 的 140° 有未识别污染，仅作对照。表 4.7 的括号误差来自固定其它量目视检查的寿命范围，花括号另给数值最小化误差。保留两种误差的原定义。学位 PDF 57–63。
- 期刊与学位论文的 RDDS 为同一 NSCL 数据。[[ljungvall-2020-shapes-collectivity-spectroscopy-hdr]] 收录较早的 GANIL 独立采集，⁶²,⁶⁴Fe 的下行 \(B(E2)\) 分别为 \(214(26)\) 和 \(470^{+210}_{-110}\ e^2\mathrm{fm}^4\)。NSCL 三点支持集体性由 ⁶²Fe 到 ⁶⁴Fe 增强且延续到 \(N=40\) 的 ⁶⁶Fe。由速率换算的形变参数与壳模型的组态比例属于解释。学位 PDF 19–20、65–72，图 5.1–5.6；期刊录用稿 PDF 4–5，表 I、图 2；HDR PDF 127–131。
- LNPS 对三个核素的下行 \(B(E2)\) 分别给 270、344、421 \(e^2\mathrm{fm}^4\)。⁶⁴Fe 的中心值相合，⁶²、⁶⁶Fe 的计算中心值偏高。比较采用 ⁴⁸Ca 核芯，质子为全 \(pf\) 壳，中子空间含 \(g_{9/2},d_{5/2}\)。表 I 的实验能量来自既有谱学结果。学位 PDF 73–77；期刊录用稿 PDF 4–5。
- 图 4.1 的 ⁶⁶Fe 长距离分解显示，靶激发对慢峰的贡献随距离减小。表 4.3 的最短采集距离是 1.49 mm，图 4.1 所画最短距离为 3.50 mm。式 A.23 下方将 \(\Delta_T/\Delta_D\) 简称为厚度比，具体复现应按 A.1 的分段定义和表 4.1 的步长核算，并保留原文用词差异。学位 PDF 49–50、54–56、79、90。

## Extracted Pages

- PDF 1–45：书证、物理背景、装置、探测器校准及入射/出射粒子鉴别。
- PDF 47–63、65–77：速度、谱形、归一、激发项、寿命与集体性和壳模型比较。
- PDF 79–101：附录 A 的衰变权重、几何、Doppler 能量、效率与谱形叠加，以及参考文献。
- PRL 录用稿 PDF 1–5：版本、采集关系、表 I 及讨论。原件见 `raw/papers/gpt/query/20261120-rother-fe-rdds-crosswalk/manifest.json`。
