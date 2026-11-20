---
type: source
title: "Davies and Hamilton 1968 - Gamma-gamma polarimeter calibration"
title_original: "Gamma-Gamma Linear Polarization Measurements"
aliases: []
created: 2026-11-21
updated: 2026-11-21
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: read
authors: ["K. E. Davies", "W. D. Hamilton"]
year: 1968
doi: "10.1016/0029-554X(68)90338-8"
canonical_source: "Nuclear Instruments and Methods 59 (1968), 1-21, published edition"
raw_file: raw/papers/gpt/query/20261119-polarization-delta-collection/10.1016_0029-554x_68_90338-8.pdf
raw_sha256: c617d1c1bfad294c926a47d634f727e826ca51a4cbdd06afa219aa25e187df04
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/papers/gpt/query/20261119-polarization-delta-collection/manifest.json
nuclei: ["46Ti", "60Ni", "134Ba", "192Pt"]
tags: ["gamma-gamma-correlation", "linear-polarization", "finite-solid-angle", "calibration"]
---

# Davies 与 Hamilton 1968：γ–γ 线偏振的有限接受度和标定

## Bibliographic Record

K. E. Davies、W. D. Hamilton，*Nuclear Instruments and Methods* **59**, 1–21（1968）。同 DOI 另存的一页 PDF 为相同出版版的首面摘录。1967 年 *Nucl. Phys. A* **96**, 65 的 ¹⁸¹Ta 混合比是本文引用的应用，实验关系须按该文核对。

## Scope and Reading Depth

覆盖印刷页及 PDF 1–21，包括理论、装置、计数校正、标定、系统偏差和书目。目视核对式 14–22、图 8、§4.4 及表 1–6。

## Summary

作者使用两晶体 NaI 求和康普顿极化仪测量方向–极化关联，并用已知纯 E2 级联标定灵敏度。有限角度衰减、门内其他真级联和多次散射分别影响预测或标定，文中用 316 keV 数据展示级联串扰的处理。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| DH-ANGLE | γ–γ 极化关联的级联夹角为 \(\theta\)，极化仪相对级联平面的方位为 \(\gamma\)。分析第一或第二条线一般得到不同的 \(\delta\) 函数。固定一个 \(\theta\) 扫方位只能约束结合后的调制，无法从该扫描分离各阶系数。各阶有限接受度衰减进入前向计算，有独立方向关联时可另用它约束各阶。 | theory-and-experimental-analysis | direct-original-pages | PDF 1–7、11–14，式 8–13、23–25，§§4.1、4.4.2 |
| DH-COUNT | 两个 NaI(Tl) 晶体做能量求和。固定散射晶体，分析晶体绕轴转动。设计采用 \(\Delta\theta_c=\Delta\phi_c=60^\circ\)，反向串散射通过屏蔽与对应 \(55^\circ\)–\(105^\circ\) 的分析晶体能窗减弱。五个方位记录校正后真三重符合，拟合 \(1+C\cos 2\gamma\)。监测真/随机极化仪符合、真三重符合及方向计数单计数，随机项的简化用到两线效率接近等条件。 | measured-apparatus-and-reduction | direct-original-pages | PDF 7–13，图 8–9、§§3.4、4.1–4.3 |
| DH-CAL | \(k=N_0/N_{90}\) 是校正后的实验计数比。\(p'=W'(90^\circ,0)/W'(90^\circ,90^\circ)\) 是折入有限接受度的理想极化比。纯 \(4(E2)2(E2)0\) 级联给点探测器 \(p'=1.40\)，表 3 的有限接受度参考值约为 1.316–1.334。测量范围 316–1173 keV，采用 ¹⁹²Ir、¹³⁴Cs、⁴⁶Sc、⁶⁰Co 衰变级联。按 PDF 17 的公式，取 \(Q=[(p'+1)/(p'-1)][(k-1)/(k+1)]\)，该处理想响应约定 \(Q=-1\)，表 4 列正的幅值。 | calibration-and-instrument-response | direct-original-pages | PDF 14–17，表 1–4 |
| DH-IR | ¹⁹²Ir 的 468 keV 门纳入 600 keV 复合峰的康普顿本底，给 316 keV 观测带来真实级联串扰。用独立 ¹³⁷Cs 谱剥离估计该成分占 11.6%，表 5 合成串扰 \(p'=0.567\)。作者对 316 keV 采用修正后的 \(p'\simeq1.20\)，表 4 报告 \(\lvert Q\rvert=0.440(76)\)。 | measured-contamination-and-correction | direct-original-pages-and-arithmetic | PDF 17–18，表 3–5、图 17 |
| DH-MULTI | 计算单次散射的有效几何曲线与实测标定比较，原文 \(\chi^2\) 尾概率为 0.01%。把二次散射按各向同性近似加入，以 \(\Delta\) 表示相对单散射的附加计数，则 \(Q'=Q/(1+\Delta)\)。表 6 的估计 \(\Delta\) 从 316 keV 的 0.263 降到 1173 keV 的 0.128。拟合 \(Q'=(A+BE)/(1+\Delta)\)，\(E\) 用 MeV，\(A=0.604(98)\)、\(B=-0.104(131)\)、\(\operatorname{Cov}(A,B)=-0.012\)。低能残差可受二次散射角分布和有效散射角影响。 | model-dependent-calibration | direct-original-pages | PDF 18–20，表 6、图 18–20 |

### 表 4 的实验比与有效灵敏度

| \(E_\gamma\) (keV) | \(k\) | \(\lvert Q_{\rm eff}\rvert\) |
| --- | --- | --- |
| 316 | \(0.922\pm0.013\) | \(0.440\pm0.076\) |
| 468 | \(0.873\pm0.016\) | \(0.497\pm0.067\) |
| 605 | \(0.883\pm0.016\) | \(0.440\pm0.064\) |
| 797 | \(0.905\pm0.019\) | \(0.354\pm0.074\) |
| 887 | \(0.836\pm0.020\) | \(0.561\pm0.083\) |
| 1119 | \(0.873\pm0.025\) | \(0.480\pm0.101\) |
| 1173 | \(0.903\pm0.029\) | \(0.356\pm0.112\) |

## Competing Interpretations and Limitations

- 复算表 5 时，将比值转成 \(a_i=(p'_i-1)/(p'_i+1)\) 后按总计数权重相加，再还原 \(p'=(1+\sum_i w_i a_i)/(1-\sum_i w_i a_i)\)，得到 0.5674。将该串扰按 11.6% 混入 \(p'_{\rm main}=1.325\)，得约 1.2015。直接平均表中比值得约 0.649。以正文舍入后的 \(p'=1.20\) 有 \(\lvert Q\rvert\approx0.446\)，表 4 给 0.440。这里复核表格和正文的计数关系，未重做原始谱剥离。参见 [[taras-matas-1970-unresolved-gamma-polarimetry]] 的两线计数响应。
- PDF 4 目视可见式 20 的分子额外印有 4。按式 14、17–19，将调制矩阵元除以强度矩阵元，公共归一消去，分子为 \(\sin^2\theta_c\)。表 3 的 ⁶⁰Co 伴随线印作 1132 keV，表 1 是 1332 keV。§3 的极化晶体尺寸为 1.27 cm × 1.27 cm，§4.4.2 有限窗口计算处写 1.77 cm × 1.77 cm。复用几何时应核对各段输入，现有原刊未说明两尺寸的差别。
- 一阶把方向计数器与散射晶体的阶数衰减相乘。方向计数器的有限角度可用相同阶数的球谐衰减。对散射晶体还假定有效探测效率在体积内恒定，分析晶体有限角度的计算另外处理。出口二次散射若带偏振相关的方位分布，单一 \(Q'(E)\) 的标定可迁移性须另验。
- 标定的纯级联与串扰用的混合分量依据既有核数据。本文报告的是仪器标定，没有新拟合某条跃迁的数值 \(\delta\)，也没有关于在束分析 \(\sigma/I\) 采用频率的证据。

## Extracted Pages

- PDF 1–7：方向、方位、Stokes 与 Compton 响应，正反级联及接受度设计。
- PDF 8–13：布置、串散射、稳定性、符合电子学、随机与损失、拟合和几何近似。
- PDF 14–18：点与有限接受度标定、标准级联、¹⁹²Ir 门串扰和表 1–5。
- PDF 19–21：二次散射、简单与修正标定曲线、限制及引用。
