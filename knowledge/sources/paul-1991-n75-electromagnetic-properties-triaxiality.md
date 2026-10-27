---
type: source
title: "Paul et al. 1991 - Electromagnetic properties of N=75 isotones: evidence for triaxiality at low spin"
aliases: [Paul 1991 N=75 isotones, Paul 1991 133Ce triaxiality, 1991Pa04]
created: 2026-10-27
updated: 2026-10-27
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Electromagnetic properties of N = 75 isotones: evidence for triaxiality at low spin"
authors: [E. S. Paul, R. Ma, C. W. Beausang, S. A. Forbes, D. B. Fossan, J. Gizon, J. R. Hughes, Y. Liang, S. M. Mullins, P. J. Nolan, W. F. Piel Jr, R. J. Poynter, P. H. Regan, R. Wadsworth]
journal: "Journal of Physics G: Nuclear and Particle Physics"
year: 1991
volume: 17
issue: 5
pages: "605–617"
doi: "10.1088/0954-3899/17/5/009"
citation_key: Paul_1991
canonical_source: "https://doi.org/10.1088/0954-3899/17/5/009"
raw_file: "raw/papers/1991_Electromagnetic properties of N=75 isotones_evidence for triaxiality at low spin.pdf"
raw_sha256: "1c3859a03a76e200048b8e087e91131d7dc5f21fb8a683cd39155ab00e0818c9"
nuclei: [133Ce, 131Ba, 135Nd, 137Sm, 139Gd]
reactions: [120Sn-16O-3n-133Ce, 122Sn-13C-4n-131Ba, 114Cd-27Al-p3n-135Nd, 107Pd-37Cl-p3n-137Sm, 92Mo-52Cr-2pn-139Gd]
experiments: [stony-brook-tandem-angular-distribution]
models: [Donau-Frauendorf-semiclassical, cranked-shell-model, total-routhian-surface]
observables: [multipole-mixing-ratio, BM1-BE2-ratio, BE2-BE2-ratio, signature-splitting]
methods: [in-beam-gamma-spectroscopy, angular-distribution, directional-correlation]
tags: [133Ce, N=75, triaxiality, mixing-ratio, Donau-Frauendorf, BM1-BE2, A130]
---

# Electromagnetic properties of N=75 isotones: evidence for triaxiality at low spin

## Bibliographic Record

- E. S. Paul *et al.*, *J. Phys. G: Nucl. Part. Phys.* **17**, 605–617 (1991), DOI: `10.1088/0954-3899/17/5/009`.
- 本地原件：`raw/papers/1991_Electromagnetic properties of N=75 isotones_evidence for triaxiality at low spin.pdf`，SHA-256 为 `1c3859a03a76e200048b8e087e91131d7dc5f21fb8a683cd39155ab00e0818c9`。
- 本文献由用户提供，补齐此前 Day 24 遗留的 1991Pa04 原件缺口，为 [[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] (WK22) 第 6 章带内混合比与三轴粒子-转子模型提供直接历史溯源。

## Scope and Reading Depth

- 全文 14 页（含封面）、图 1–6、表 1 与公式 (1)–(8) 完整通读；
- 重点核对 133Ce 在 Stony Brook 串列加速器上的角分布实验条件、多极混合比 delta(E2/M1) 符号约定、电磁跃迁几率比值定义，以及基于 Donau-Frauendorf 半经典模型对 133Ce 三轴形变（beta2=0.17, gamma=-20 deg）与有效 K 投影的理论计算。

## Summary

本文系统测量并汇总了 N=75 奇中子同中子素（131Ba, 133Ce, 135Nd, 137Sm, 139Gd）基于独特性宇称 nu h11/2 轨道的负宇称能带的电磁性质：
1. **实验测量**：在 Stony Brook 利用 120Sn(16O, 3n gamma)133Ce（69 MeV，厚铅衬靶）开展 5 角区（90, 115, 125, 135, 145 deg）角分布测量，利用 chi2 极小化拟合提取带内 Delta I=1 跃迁的多极混合比 delta(E2/M1)；
2. **符号与单位约定**：采用 Yamazaki 1967 符号约定（与 Krane-Steffen 一致，delta < 0），跃迁比率公式含因子 0.697 MeV^2；
3. **三轴性证据**：
   - 提取的带内 B(M1; I -> I-1)/B(E2; I -> I-2) 比值在低自旋区平均约为 1 (muN/eb)^2；跨越回弯后，随着一对 h11/2 质子对齐，比值增加约 5 倍；
   - 竞争的非拉伸与拉伸电四极跃迁比值 B(E2; I -> I-1)/B(E2; I -> I-2) 围绕平均值 ~ 2 起伏，大于 1 的事实反映了波函数中低 Omega 组分的掺杂，是核具有非轴对称（三轴）形状的明确信号；
   - 采用 Donau-Frauendorf 半经典模型计算 133Ce：TRS 计算给出低自旋 (beta2=0.17, gamma=-20 deg)，高自旋三准粒子态 (beta2=0.17, gamma=0 deg)。在三轴形变下 K 不再是好量子数，有效 K=7/2 能更好地再现实验比值；
   - 依据 Hagemann-Hamamoto 三轴性检验（Delta B(M1)/<B(M1)> 与能谱旋称劈裂 Delta e_prime/hbar omega 的对比），确立轻同中子素（131Ba, 133Ce）比重同中子素具有更显著的三轴形变。

## Experimental and Method Contract

- **反应与靶**：120Sn(16O, 3n)133Ce，束能 69 MeV，靶厚 9.7 mg/cm2 120Sn，背衬 100 mg/cm2 Pb（完全阻止反冲核与束流）；
- **探测布局**：1 台反康普顿 HPGe 探测器（距离靶点 22 cm）在 5 个角度旋转测量，另 1 台固定在 -90 deg 作为束流强度与产额监测；利用 133Ba 与 152Eu 点源进行精确几何与探测效率刻度；
- **跃迁几率比值提取公式**（PDF p. 6）：
  delta(E2/M1) = 0.835 E_gamma <I_f || E2 || I_i> / <I_f || M1 || I_i>  (E_gamma in MeV)
  B(M1; I -> I-1) / B(E2; I -> I-2) = 0.697 [E_gamma(E2; I -> I-2) / E_gamma(M1; I -> I-1)]^5 / [lambda * (1 + delta^2)]  [(muN/eb)^2]
  式中 lambda = I_gamma(E2; I -> I-2) / I_gamma(M1; I -> I-1) 为分支比；
  B(E2; I -> I-1) / B(E2; I -> I-2) = delta^2 [E_gamma(E2; I -> I-2) / E_gamma(M1; I -> I-1)]^5 / lambda

## Key Results and Claims

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PA91-01 | 120Sn(16O, 3n)133Ce 在 69 MeV 下测定负宇称带内 Delta I=1 跃迁的角分布，确立混合比 delta(E2/M1) < 0（采用 Yamazaki 1967 约定）。 | experiment-result | direct | PDF pp. 2–5, Fig. 1 | true |
| PA91-02 | 133Ce 低自旋 nu h11/2 带内 B(M1)/B(E2) 比值约为 1 (muN/eb)^2；在 h11/2 质子对齐后，比值跃升约 5 倍。 | observable-systematics | direct | PDF pp. 6–9, Fig. 3 | true |
| PA91-03 | 非拉伸与拉伸四极比 B(E2; I -> I-1)/B(E2; I -> I-2) 约 2 > 1，反映三轴形变波函数中低 Omega 组分的非对角混合。 | triaxiality-indicator | mixed | PDF pp. 6–9, Fig. 4 | true |
| PA91-04 | Donau-Frauendorf 半经典模型以 TRS 参数 (beta2=0.17, gamma=-20 deg)、有效 K=7/2 与实测能谱旋称劈裂 Delta e_prime/hbar omega = 0.39(3) 较好地再现了 133Ce 的跃迁比率。 | model-interpretation | mixed | PDF pp. 9–11, Fig. 5 | true |
| PA91-05 | Hagemann-Hamamoto 检验（跃迁率不对称度与能谱旋称劈裂的比例关系）确立轻同中子素（131Ba, 133Ce）具有比重同中子素更显著的三轴性。 | cross-isotone-comparison | mixed | PDF pp. 11–12, Fig. 6 | true |
| PA91-06 | 确认 WK22 Figure 6.15(a) 采用的 133Ce Band 1 带内 delta 数据直接源自本篇，两文献形成确凿的谱系继承与互补关系。 | cross-source-lineage | direct | PDF p. 5, Fig. 1; WK22 PDF p. 113 Fig. 6.15(a) | true |

## Boundaries and Limitations

1. **谱线与带身份范围**：本篇仅研究负宇称 yrast 带（Band 1）及其高自旋 3-qp 延伸，未报告亦未涉及高激发 Band 4 及其跨带连接跃迁；
2. **寿命与绝对标度缺口**：本篇实验为厚衬靶角分布，未测定态寿命 tau，所有电磁量均为相对比值（B(M1)/B(E2) 或 B(E2)/B(E2)），无法单独给出绝对 B(E2) 或内禀电四极矩 Q0；
3. **有效 K 的唯象性**：在三轴形变下将 K 从 9/2 唯象调至 7/2 属于准粒子转子模型的参数化补偿，不能替代完全非谐微观波函数的严格对角化。
