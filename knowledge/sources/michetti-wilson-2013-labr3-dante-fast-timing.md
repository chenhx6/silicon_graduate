---
type: source
title: "Michetti-Wilson 2013 - LaBr3(Ce) and DANTE fast timing"
title_original: "Characterization of LaBr3(Ce) Detectors for Picosecond Lifetime Measurements"
aliases: []
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: masters-thesis
reading_depth: read
authors: ["Julian Michetti-Wilson"]
year: 2013
institution: "University of Guelph"
url: "https://hdl.handle.net/10214/6671"
canonical_source: "University of Guelph MSc thesis; title page dated May 2013"
raw_file: raw/theses/gpt/query/20261119-international-nuclear-structure/Michetti-Wilson_Julian_201310_Msc.pdf
raw_sha256: 2f2366ed9b2779211b1e105f3d607987336d72df3d3adadb2723758dd17a5b34
raw_storage_status: archived-local
archive_required: true
nuclei: ["60Co", "60Ni", "152Eu", "152Sm"]
tags: [fast-timing, LaBr3, DANTE, Compton-suppression, thesis]
---

# Michetti-Wilson 2013：LaBr₃ 快定时与 DANTE 响应

## Bibliographic Record

Julian Michetti-Wilson，University of Guelph 物理硕士论文。107 页本地原件的题页标为 2013 年 5 月。馆藏标识 `10214/6671`；正文印刷页为 PDF 页减 16。

## Scope and Reading Depth

Codex 已核对 105/107 页科研、书证与索引。PDF 3–4 为致谢，留原件。文献介绍中的材料属性按引用处理，图表数据和作者诊断按本实验记录。

## Summary

这项 8π/DANTE 研究用标准源检验 LaBr₃(Ce) 的能量与定时响应。它同时提供了优化后的 prompt 峰宽和一例未通过验证的半衰期拟合。二者分别说明仪器分辨和跨能量/通道准确度。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| MW-TAC | 100 ns/8192 只给名义 12.207 ps/channel。4 个已标定模块为 12.5963、12.4876、12.4238、12.5968 ps/channel，作者对其它模块采用 12.526(100) ps/channel。 | calibration-and-adopted-input | direct-original-pages | PDF 73，§3.5 |
| MW-PROMPT | 1332 keV 的 LaBr₃–快塑闪符合，表 4.1 的五只 1500 V 探测器平均 248.48 ps FWHM，与文末 248.5 ps 相符。Q-092 在 2000 V，报 316.6(4.5) ps，六只等权平均 259.83 ps。 | measurement-and-arithmetic-check | direct-original-pages-and-arithmetic-check | PDF 75–78、94、97，表 4.1，附录 A 图 1 |
| MW-VETO | BGO veto 在该 ⁶⁰Co 谱的光峰下侧去除约 61% 的 Compton 事例；光峰能门下，prompt 时间谱的变化小。被动屏蔽 S5 的四个配门对照均变宽，相差 21.3–31.5 ps，均值 26.6 ps。 | configuration-specific-comparison | direct-original-pages-and-arithmetic-check | PDF 78–84，表 4.2–4.3、图 4.3–4.8 |
| MW-FAILED-TAU | ¹⁵²Eu 源的 ¹⁵²Sm 244.7 keV 馈入、约 121 keV 出射级联中，较接近模型的一组时间谱拟合给 \(T_{1/2}=1582(18)\) ps；论文对照的是当时采用的 1430(15) ps。峰形失配和通道非对称使作者判定这次寿命测量失败。 | failed-fit-and-reference | direct-original-pages | PDF 87–90、98–100，§4.3、附录 A 图 2、附录 B 图 3–4 |
| MW-CONTROLS | 自触发约 23 ps，同长度分路约 30 ps，不同长度分路最宽约 100 ps。三组对照均未重现 0.8 ns 左右的双成分或约 4 ns 的异常峰。故障在该实验中尚无独立定位。 | diagnostic-control | direct-original-pages | PDF 83–90、101–102，图 4.8–4.10、附录 B 图 5–7 |
| MW-CONV | 单边指数与高斯响应的卷积直接积分支持式 2.15；式 2.11 的 \(\sigma^2\lambda\) 符号应随式 2.9 取正。 | derivation-and-numerical-check | direct-original-pages-and-arithmetic-check | PDF 48–55，式 2.4、2.9、2.11、2.15 |

## Competing Interpretations and Limitations

- S5 四行共用一组晶体对，改变的是 DANTE stream 或配能门。平均 FWHM 只是该组合的描述量。同一对探测器在互换起停时出现不同形状或偏移，会破坏镜像差分依赖的响应等效性。即便部分配门下总面积接近，也可能有不同的时间分布。
- 附录 C 的十 TAC/六 FIFO 接线为作者拟议电路，尚需核实反射和跨通道定时。它与已实测 DANTE 的异常时间谱分别登记。对同位素寿命或其它阵列采用值时，需各自验证能量、几何、prompt reference、读出方向和门选择。
- §5.1.3 将 3.03% 引作效率，表 4.4 明确是 1332 keV 光峰的能量分辨 \( \mathrm{FWHM}/E \)。原表字段可支持分辨率比较，此数无法用于光峰效率。PDF 91、95。
- §3.6 称 2060(25) ps 为半衰期。若作平均寿命 \(\tau\)，乘 \(\ln 2\) 得 1428(17) ps，与 §4.3 给的参考半衰期 1430(15) ps 相容。前者仍保留原引用标记，数值转换由本次核验给出。PDF 74、88–89、107，[18]。
- 该工作早于 S1790，设备为 8π/DANTE；与 [[kalaydjieva-2023-cd106-zr100-shape-coexistence-thesis]] 的 GRIFFIN 测量及 [[smith-2017-109ru-109tc-fast-timing-thesis]] 只作方法对照。

## Fit and response checks

- 以高斯 prompt \(G(u;\mu,\sigma)\) 与单边 \(e^{-\lambda t}\mathbf 1_{t\ge0}\) 卷积，在时间轴沿延迟方向增长的约定下，得 \(A/2\cdot e^{-\lambda(u-\mu)+\sigma^2\lambda^2/2}\operatorname{erfc}[(\mu+\sigma^2\lambda-u)/(\sqrt2\sigma)]\)。指数核如需面积归一，再乘 \(\lambda\)。用原文测试参数 \(\mu=20,\sigma=11,\lambda=0.03\) 在 \(u=0,20,40,100\) 直接积分，与式 2.15 一致。将式 2.11 的负号代入会改变前沿。在 \(u=20\)、单位 \(A\) 时，数值由 0.39144 变成 0.66452。这个检查验证数学形式，原 `jfit` 程序与原事例另需取得。
- PDF 54 的收敛例使用加高斯噪声的模拟输入，考查初值与回收，未检验 DANTE 的通道响应误差。独立高斯响应相加时 \(\sigma_{ij}^2=\sigma_i^2+\sigma_j^2\)，因此 PDF 76 提到可用三种配对估计单只探测器的方差。表 4.1 的 LaBr₃–快塑闪宽度仍包含塑闪及其读出。峰宽、能量相关的时间位置、适用的寿命拟合下限须分别测定。
- ORTEC 935 的外部延迟和过零电压共同影响形状。作者在 M 输出的叠加波形上先缩小过零散布，再用有能门的 TAC 谱调 FWHM。各探测器优化延迟约 2.6–3.0 ns，后续统一 2.8 ns 再比较互换起停，仍见时移与非对称。DANTE 的定时起停与用于能门的 dynode 能量链分开处理。PDF 42–43、58–62、69–74、77。
- 8π 的 HPGe/BGO 用于 γ 能谱及反符合，SCEPTAR 用于 β 标记，PACES 用于转换电子，ZDS 快塑闪可提供时间参考，DANTE 支持多个快闪烁体的起停配对。第一章引材料文献中的掺杂与光产额作为条件说明。晶体尺寸与光收集条件会改变本实验 FWHM。论文给出的本底源包括 La-138 与 Ac-227 系列。PDF 29–47，图 1.7–1.15、1.21。

## Extracted Pages

- PDF 1–2、5–16：学位题页、摘要、目录、图表索引。
- PDF 17–47：γ 相互作用、LaBr₃(Ce) 闪烁、PMT、内部本底、CFD 和 8π 仪器。
- PDF 48–96：拟合、探测器实验配置及读出、TAC 标定、实验结果、诊断及结论。
- PDF 97–104：能门、异常时间峰、分路对照与拟议 FIFO 布置。
- PDF 105–107：材料、仪器、拟合和参考寿命的书证定位。
