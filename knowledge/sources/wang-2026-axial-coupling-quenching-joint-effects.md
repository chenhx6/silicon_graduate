---
type: source
title: "Wang 等 2026：手征两体流与粒子-振动耦合对 β 衰变 gA 淬灭的联合效应"
aliases: [Wang 2026 arXiv:2605.21218, wang-2026-axial-quenching]
created: 2026-11-13
updated: 2026-11-13
status: active
review_status: unreviewed
source_type: preprint
reading_depth: skimmed
title_original: "The quenching of the axial-vector coupling constant gA in beta-decay: joint effects from chiral two-body currents and many-body correlations"
authors: [Bin-Lei Wang, Wan-Li Lv, Li-Gang Cao, Yi-Fei Niu, Gianluca Colò, Hiroyuki Sagawa, Feng-Shou Zhang]
year: 2026
arxiv: 2605.21218v1
language: en
canonical_source: "arXiv:2605.21218v1 (Dated 20 May 2026); journal publication not verified"
citation_key: wang-2026-axial-coupling-quenching-joint-effects
raw_file: raw/papers/gpt/query/20261113-A130-axial-currents/wang-2026-arxiv2605.21218v1.pdf
raw_sha256: 64b8098517bdf4754ff71d80ab4256aab77102aaa9257390f99db1b3788c0c8d
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/papers/gpt/query/20261113-A130-axial-currents/manifest.json
actual_read_pages: [1, 2, 4, 5]
actual_read_scope: "第1页摘要与作者机构；第2页RPA+PVC与手征两体流微观算符定义；第4页Fig.3对SGII/SIII/SkM*/SLy5在100Sn中与实验条的比较；第5页Table II与结语。仅核实2026年5月20日arXiv预印本，未核实期刊正式发表状态。"
nuclei: [56ni, 100sn, 132sn]
reactions: []
experiments: []
models: [skyrme-energy-density-functional, rpa-plus-pvc, chiral-two-body-currents]
observables: [gamow-teller-strength, b-gt]
methods: [particle-vibration-coupling, chiral-effective-field-theory]
tags: [A130, beta-decay, gamow-teller, quenching, two-body-currents, pvc, 100sn, 132sn]
---

# Wang 等 2026：手征两体流与粒子-振动耦合

## Bibliographic Record

Bin-Lei Wang 等于 2026 年 5 月 20 日提交至 arXiv（arXiv:2605.21218v1），题为 *The quenching of the axial-vector coupling constant gA in beta-decay: joint effects from chiral two-body currents and many-body correlations*。本地持有原始预印本 PDF（11 页）与 arXiv 页面记录。本记录明确其为预印本，未核实期刊正式审稿与发表状态；不复述任何撤回的历史日期。

## Scope and Reading Depth

本记录基于预印本 PDF 第 1、2、4、5 页定向选读：
- 第 1 页：摘要与问题陈述（探讨 RPA+PVC 多体关联与手征两体流 TBC 的共同作用）。
- 第 2 页：手征弱两体流算符分解，区分接触项（含 $\bar{c}_D$）与有限介子交换动量依赖项。
- 第 4 页：Fig. 3 在 $^{100}\mathrm{Sn}$ 中比较不同 Skyrme 泛函（SGII, SIII, SkM*, SLy5）并展示 $\bar{c}_D=0$ 时与两组实验条的对比；Table I 与式 (5) 明确所列 $q$ 的分子、分母及不同近似。
- 第 5 页：Table II 动量依赖项对 $B(GT)$ 的微小影响与结论总结（提取有效淬灭比 $q \approx 0.73\text{--}0.80$）。

未核实附录后半部分单粒子波函数展开与所有参数组细节。

## Summary

Wang 等（2026，arXiv 预印本）在双闭壳核 $^{56}\mathrm{Ni}$、$^{100}\mathrm{Sn}$ 与 $^{132}\mathrm{Sn}$ 中，基于 Skyrme 能量密度泛函采用 RPA+PVC，并引入手征弱两体电流（TBC）。须区分关联打开低能通道与TBC相对单体流的修正：Table I 的纯RPA对 $^{56}\mathrm{Ni}$、$^{132}\mathrm{Sn}$ 在所用 $Q_\beta$ 窗口内没有GT强度，加入PVC后出现强度；同表所列 $q$ 则按式 (5) 的指定分子、分母计算，不能当作对这一零RPA基线乘上的普适因子。作者在所选模型中得到约0.73–0.80的比值。对其考察的TBC项，文中报告介子交换部分贡献较大、动量依赖项很小，短程项的影响小于主要TBC贡献；结论依赖所取泛函、LEC和近似。

## Key Results

| ID | 声明与物理内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WANG-1 | 作者按式 (5) 定义 $q=\sqrt{\sum B_{\rm GT}^{1,3,4}/\sum B_{\rm GT}^{1}}$，上标对应原式 (3) 所保留的项。同表PVC行的中心数分别给出约0.80、0.77、0.73；不能不说明分母就等同于总Ikeda差和或任意模型的淬灭常数。 | model-result-and-definition | direct-original-parent-check | PDF p.4 Table I、式 (3)、(5)及表下解释；本轮未重算全部矩阵元 | false |
| WANG-2 | 对文中所考察设置，动量依赖项贡献很小，介子交换项贡献较大，短程项影响小于主要TBC贡献；具体结论与LEC、泛函选择绑定。 | model-result | direct-original-parent-check | PDF p.5 Table II、Fig.4及结论段 | false |
| WANG-3 | arXiv记录的v1提交日期为2026-05-20；所存PDF首页内部日期为2026-05-21。当前未核实期刊发表，二者均不应改写成已核的2026年11月出版日期。 | version-and-access-boundary | direct-metadata-and-original | 归档arXiv记录citation_date；PDF p.1日期 | false |
| WANG-4 | Table I 的纯RPA在 $^{56}\mathrm{Ni}$、$^{132}\mathrm{Sn}$ 的所用 $Q_\beta$ 窗口内给零GT强度，PVC设置给非零值；本文案例不能被概括为“增加关联只会压低低能强度”。 | model-comparison | direct-original-parent-check | PDF p.4 Table I及式 (5) 后段 | false |

## Competing Interpretations and Limitations

该文展示了在能量密度泛函框架下 PVC 多体涨落与 TBC 协同工作的图像，与 Gysbers 等从头算耦合簇方法在多体基矢与核力来源上存在具体实现差异。二者不可作为两个完全相互独立的实验证据，也不可简单相加其具体百分比。

## Extracted Pages

选读范围覆盖预印本 PDF 第 1、2、4、5 页。关键核验图表为 Fig.3、Table I/式 (5) 与 Table II；总控增量回读第4–5页并核对比值与“先打开通道、再比较算符”的区别。相关边界提取至 [[a130-rewrite-axial-operator-scope-20261113]]。这些是指定理论输入的核查，不是对全部附录或实验输入的重新评价。
