---
type: source
title: "Morse 2015 - 70As and 74Rb lifetimes"
title_original: "Nuclear Structure of Proton-Rich Intermediate Mass Nuclei Studied with Advanced Lifetime Measurement Techniques"
aliases: []
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: doctoral-thesis
reading_depth: read
authors: ["Christopher Scott Morse"]
year: 2015
institution: "Michigan State University"
doi: "10.25335/m54t6f946"
canonical_source: "Michigan State University doctoral thesis, 2015"
raw_file: raw/theses/gpt/query/20261119-international-nuclear-structure/etd_2784_Original_file.pdf
raw_sha256: e64081484913043c80204f529776b96e8af44721928a41df18894bfbcd1a81c5
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/theses/gpt/query/20261119-international-nuclear-structure/manifest-user-recheck.json
comparison_manifest_file: raw/papers/gpt/query/20261120-morse-70as-74rb-crosswalk/manifest.json
comparison_manifest_sha256: 71443d87f66615f90be9a830cb4b1be9943c6a6474f461251591cf600af2e6be
nuclei: ["70As", "74Rb", "74Kr"]
tags: ["SeGA", "GRETINA", "TRIPLEX", "lineshape", "lifetime", "thesis"]
---

# Morse 2015：⁷⁰As 符合谱形和 ⁷⁴Rb 三箔寿命

## Bibliographic Record

Christopher Scott Morse，Michigan State University 博士论文，2015，181 页。⁷⁰As 结果见 Phys. Rev. C **90**, 034310（2014），`10.1103/PhysRevC.90.034310`，对照层为书目及索引保存的摘要。⁷⁴Rb 见 Phys. Lett. B **787**, 198–203（2018），`10.1016/j.physletb.2018.10.064`，已留存 INSPIRE 提供的 Elsevier 出版版。同一核素的论文和相应学位章节共享采集。

## Scope and Reading Depth

覆盖原件 177/181 页科研与书证范围。PDF 3–6 为版权、献辞和致谢，不计正文。正文印刷页 = PDF 页减 22。关键图及 ⁷⁴Rb 的原刊寿命读数已目视或按对应原表核实。

## Summary

两个 NSCL 实验采用不同方法。⁷⁰As 用 SeGA 与 S800 的粒子鉴别、γ 符合和 Geant4 谱形，区分串联的两个寿命。⁷⁴Rb 用 GRETINA、S800 和 TRIPLEX，在同一距离设置利用两段速度分量并模拟多种馈入与产生位置。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| MOR-AS | ⁹Be(⁷⁸Rb,⁷⁰As) 入口能量 101.6 MeV/u。⁷⁰As 的 788.3 keV \(8^+\to7^-\) 谱形在 \(10^+\to8^+\) 馈入门下约束 \(8^+\) 寿命。76.1 keV 线受阈值和辐射电子俘获背景限制，用级联门与后继 788.3 keV 谱形约束 \(9^+\) 寿命，并传播 \(8^+\) 的误差。 | measurement-and-feeding | direct-original-pages | 学位 PDF 109–121、126–132，图 4.2–4.7、4.11–4.12 |
| MOR-DEGEN | 学位采用 \(\tau(8^+)=80(29)\) ps、\(\tau(9^+)=85(43)\) ps。单谱双参数拟合在 \((0,160)\) 和 \((100,80)\) ps 附近有两处极小值，符合门排除近零 \(8^+\) 解，采用值来自具有明确馈入的符合谱。未测 \(10^+\) 馈入寿命取邻核推值并以五倍变化估系统误差。 | competing-likelihood-minima | direct-original-pages | 学位 PDF 112、129–134，图 4.11–4.14 |
| MOR-B | ⁷⁰As 采用外来混合比 \(\delta=0.017(13)\)（E1/M2 支路）和 \(0.01(3)\)（M1/E2 支路），给 \(B(E1;8^+\to7^-)=1.2(4)\times10^{-5}\) W.u. 与 \(B(M1;9^+\to8^+)=0.85(42)\) W.u.。阻碍 E1 和相对强 M1 支持 \(\pi g_{9/2}\nu g_{9/2}\) 组态解释。 | derived-strength-and-configuration | direct-original-pages | 学位 PDF 134–138，图 4.15–4.16；PRC 2014 摘要 |
| MOR-DR | ⁷⁴Rb 实验用 ⁹Be(⁷⁴Kr,⁷⁴Rb) 电荷交换，将目标、两减速箔对应为快、中、慢峰。在可忽略慢馈入且箔间飞行时间短于寿命时，\(\tau\simeq(\Delta x/v)I_s/I_r\)。此处 \(\Delta x\sim1\) mm、\(v\sim0.1\) mm/ps、比值约 3，给约 30 ps 的估算。正式分析用 Geant4 纳入效率、箔内发射、减速箔反应和 S800 接受度。 | method-and-approximation | direct-original-pages | 学位 PDF 61–64、146–163，式 2.27–2.30、5.3，图 5.13；PLB PDF 2–4，式 2–4 |
| MOR-RB | 学位给 ⁷⁴Rb \(2_1^+\) 的 26.7(60) ps、\(B(E2;2_1^+\to0_1^+)=1227(276)\ e^2\mathrm{fm}^4\)。2018 终稿给 27(6) ps、\(1.2(3)\times10^3\ e^2\mathrm{fm}^4\)。同轮 ⁷⁴Kr 对照给 31(3) ps（有馈入）及 33(3) ps（忽略馈入），后者对快峰再现较差。 | versioned-lifetime-and-feeding-control | direct-original-pages | 学位 PDF 160–164，图 5.10–5.13；PLB PDF 4–5，图 3，§§4–5 |

## Competing Interpretations and Limitations

- ⁷⁰As 的 76.1 keV 门有颗粒筛选、低能阈值和近邻本底限制。旁门只作真符合控制，原分析没有把它直接扣为等效本底。报告的 \(9^+\) 寿命继承 \(8^+\) 与馈入寿命的不确定度。主要组态仍是基于强度比较的解释。
- 三箔公式用有限差分近似。若只为比较，在相同参考系、定速、无馈入及分量相同接受度下，纯指数给 \(\tau=t_f/\ln(1+I_r/I_s)\)，所以 \(I_s/I_r=3\) 时一阶式相当于 \(3t_f\)，指数式约 \(3.48t_f\)。实测强度还需箔与谱形响应，不能将这一条件差直接加到作者模拟寿命上。
- ⁷⁴Rb 与 ⁷⁴Kr 相近的同位旋类似态 \(B(E2)\) 支持同标量成分主导，并可间接约束形状混合。⁷⁴Rb 的对应激发 \(0_2^+\) 在作者分析中尚未被直接观察，寿命测量只给 \(2_1^+\to0_1^+\) 强度。见学位 PDF 164–173、PLB PDF 5–6。

## Extracted Pages

- 学位 PDF 1–2、7–64：身份、目录、问题动机、电磁几率、谱形与三箔推导。
- 学位 PDF 65–138：S800、SeGA/GRETINA、TRIPLEX，⁷⁰As 的束流标定、拟合与物理解读。图 4.14 目视 PDF 133。
- 学位 PDF 139–181：⁷⁴Rb 和 Kr 对照、模型讨论、结论与书目。目视 PDF 155、163。PLB PDF 1–6 用于版本核对。
