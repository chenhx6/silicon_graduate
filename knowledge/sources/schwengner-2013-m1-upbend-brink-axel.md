---
type: source
title: "Schwengner et al. 2013 - Low-Energy Enhancement of Magnetic Dipole Radiation"
aliases: [Schwengner 2013 M1 upbend, Brink-Axel breakdown M1 upbend, SCH13]
created: 2026-10-30
updated: 2026-11-22
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Low-Energy Enhancement of Magnetic Dipole Radiation"
authors: [R. Schwengner, S. Frauendorf, A. C. Larsen]
journal: Physical Review Letters
year: 2013
volume: 111
issue: 23
pages: "232504"
doi: "10.1103/PhysRevLett.111.232504"
canonical_source: "https://doi.org/10.1103/PhysRevLett.111.232504"
citation_key: schwengner2013m1upbend
raw_file: "raw/papers/gpt/learning-daily/20261031-OPEN-RESEARCH-source-recovery/PhysRevLett.111.232504.pdf"
raw_sha256: d7a70974055150e736e3c07a5ba444e32e33bf41a44ada6ae8afff847520ce39
nuclei: [90zr, 94mo, 95mo, 96mo]
reactions: []
experiments: []
models: [spherical-shell-model, generalized-Lorentzian-E1]
observables: [gamma-ray-strength-function, B-M1-transition-rate, level-density, low-energy-upbend]
methods: [shell-model-transition-strength, gamma-strength-model-comparison]
tags: [gamma-ray-strength-function, brink-axel-breakdown, M1-upbend, TAC, shears-recoupling, Day27]
---

# Low-Energy Enhancement of Magnetic Dipole Radiation

## Bibliographic Record

PRL 111, 232504 (2013), DOI `10.1103/PhysRevLett.111.232504`.

## Scope and Reading Depth

刊版 PDF1–5 对应 232504-1 至 232504-5。核定壳模型空间、M1 跃迁样本、Figs. 1–6、经验 E1 项和引用实验比较。图中数值未数字化，计算未复现。

## Summary

计算对象为 90Zr 与 94,95,96Mo。作者从激发态间的壳模型 M1 跃迁得到低能增强，并以高 \(j\) 轨道重耦合解释较强分量。含 E1 的强度函数比较采用另行选取的经验 E1 项。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SCH13-1 | 计算对每种宇称考虑超过 14,000 条 M1 跃迁，按 \(E_\gamma=E_i-E_f\) 分箱计算平均强度。所算样本低于 2 MeV 的平均强度可用指数函数近似。 | model-result | direct-to-model | PDF2 methods and PDF3 Figs. 4–5 | false |
| SCH13-2 | 作者把大 M1 矩阵元归于两个态共享的高 \(j\) 破对组态及磁矩相干相加。文中用磁转动与混合对称态作机制类比，模型本身为壳模型。 | author-interpretation | direct-to-model | PDF3–5 wave-function and comparison discussion | false |
| SCH13-3 | 壳模型 \(\overline{B(M1)}\) 结合所算初态能级密度得到 \(f_{M1}\)。与 Mo 既有实验比较时再加广义洛伦兹 E1 项，该项依据引用的光中子数据和较高能区谱拟定。 | model-to-data-comparison | conditional | PDF4 formula and Figs. 1–3 | false |
| SCH13-4 | 90Zr 的低能增强在本篇属于计算结果。作者建议用实验检验。所引其它核素的现象用于讨论可能的核区依赖。 | prediction-and-boundary | direct-to-source | PDF4–5 discussion | false |

## Competing Interpretations and Limitations

原文的核区、激发态与可达组态限定了上述结果。实验总强度的比较依赖所加 E1 项。旧条目的独立 TAC 计算、160Dy/208Pb 定量结论及普适失效阈值均撤出本文归属。

## Extracted Pages

- [[brink-axel-breakdown-and-low-energy-m1-upbend]] 保存迁移比较的证据边界。
