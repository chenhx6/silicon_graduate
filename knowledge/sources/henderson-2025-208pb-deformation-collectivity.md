---
type: source
title: "Henderson et al. 2025 - Deformation and collectivity in doubly magic 208Pb"
aliases: [Henderson 2025 208Pb quadrupole moment, 208Pb two-phonon octupole splitting]
created: 2026-11-01
archive_required: true
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Deformation and Collectivity in Doubly Magic 208Pb"
authors: [J. Henderson, J. Heery, M. Rocchini, M. Siciliano, N. Sensharma, et al.]
journal: Physical Review Letters
year: 2025
volume: 134
article_number: 062502
doi: 10.1103/PhysRevLett.134.062502
language: en
canonical_source: https://doi.org/10.1103/PhysRevLett.134.062502
direct_pdf_url: https://eprintspublications.npl.co.uk/10188/1/eid10188.pdf
raw_file: "raw/papers/gpt/learning-daily/20261101-day29-208pb-audit/2025-208pb.pdf"
raw_sha256: 59cfb36a34024aeeda65f725829ec666b758047be1fe2e335b1e95670f106d5e
raw_link_status: linked-and-hash-match
source_raw_audit: linked-and-hash-match
hash_verified_at: 2026-11-01
nuclei: [208pb]
reactions: [70ge-208pb-coulex, 130te-208pb-coulex, 150nd-208pb-coulex, 166er-208pb-coulex]
experiments: [atlas-208pb-gretina-chico2-coulex]
models: [shell-model, sccm, hf-rpa, tdhf, relativistic-gcm]
observables: [spectroscopic-quadrupole-moment, b-e2, b-e3, two-phonon-octupole-splitting]
methods: [safe-coulomb-excitation, gamma-ray-spectroscopy, particle-gamma-coincidence, gosia]
tags: [208pb, doubly-magic, octupole, quadrupole-coupling, two-phonon, cross-mass]
---

# Henderson 等（2025）：`208Pb` 形变、集体性与两声子八极分裂边界

## Bibliographic Record

J. Henderson et al., *Physical Review Letters* **134**, 062502 (2025),
DOI `10.1103/PhysRevLett.134.062502`。本文 PDF 由公开机构镜像取得，并在本轮
逐文件核验后归档到受保护 raw 路径。PDF SHA-256 为
`59cfb36a34024aeeda65f725829ec666b758047be1fe2e335b1e95670f106d5e`。

## Scope and Reading Depth

通读 8 页正文，核对摘要、引言中两声子 quartet 的证据状态、Table I 的矩阵元、
四种库仑激发束流/探测器链和结论段的两声子分裂推断。补充材料未摄入，因此本页
不扩展其产额或逐门响应。

## Summary

四种重离子库仑激发测量给出 `208Pb` 的 `3−_1` 与 `2+_1` 大负谱学四极矩；
作者同时明确指出 `3−⊗3−` 两声子 quartet 尚未获得 conclusive identification。
`0+` candidate 与 `800–1500 keV` coupling-induced splitting estimate 构成一个
新的、可证伪的 quadrupole–octupole coupling 边界，而不是完整 quartet 的确认。

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HE25-1 | 四种重离子库仑激发测量给出 `208Pb` 的 `3−_1` 与 `2+_1` 大负谱学四极矩；作者将其解释为这些激发态具有时间平均的偏长轴成分。 | experimental-result / author-interpretation | direct | PDF p.1 abstract; pp.5–6 conclusion | true |
| HE25-2 | 正文明确写出 `3−⊗3−` 两声子 `0+,2+,4+,6+` quartet 尚未获得 conclusive identification，现有最好证据集中在 `0+` candidate。 | evidence-boundary | direct | PDF p.2, paragraph beginning “Arguably the most famous…” | true |
| HE25-3 | 联合 GOSIA 分析给出 `Qs(3−_1)=-0.63(11) eb`（含文献 `B(E2)` 约束时）和 `Qs(2+_1)=-0.42(7) eb`；不含该约束的对应行也在 Table I。 | experimental-result | direct | PDF p.4, Table I | true |
| HE25-4 | 作者依据 `Qs(3−_1)` 与 quadrupole–octupole coupling 关系估计两声子 quartet 的可能分裂尺度约为 `800–1500 keV`；这是模型关联的设计推断，不是四个已测能级的分裂。 | author-interpretation / experiment-design-inference | direct | PDF p.6, paragraph beginning “Importantly…” | true |
| HE25-5 | 已知 `0+` candidate 位于 `5241 keV`；作者指出该点与上述分裂估计存在张力，因而 `208Pb` 仍是未解决的核结构问题。 | experimental-result / synthesis | direct | PDF p.6, final paragraph before references | true |
| HE25-6 | 文章实验只直接观察到 `3−→0+` 与 `2+→0+` 退激线；两声子 quartet 的完整 γ closure 不由本次数据建立。 | source-completeness-boundary | direct | PDF p.4, GOSIA-analysis paragraph | true |

## Scientific Correction

这篇 primary 结果纠正了本库旧笔记把 `208Pb` 写成“完整、近简谐 quartet 已被无可辩驳坐实”的说法。更安全的基线是：`208Pb` 有强 `3−` E3 集体性和一个有力的 `0+` candidate，但 quartet 的完整身份、非简谐分裂和二声子 E3 网络仍未闭合；新的 `Qs` 测量反而给出了一个可检验的强 quadrupole–octupole coupling 假设。

## Competing Interpretations and Limitations

- `0+` candidate 可以是两声子 doorway 的成员，也可以与其它正宇称组态混合；当前论文没有凭自身数据完成四成员 closure。
- `800–1500 keV` 是由 `Qs` 和模型关系得到的分裂尺度估计，不是四个候选态的直接能级测量。
- `Qs`、`B(E2)` 和 `B(E3)` 约束了集体响应，却不能单独提供完整的两声子 E3/feeding 矩阵。
- 本页没有把旧文献候选表、外部模型输出或缺失的 event-level response 当作 `208Pb` 的独立实验事实。

## Extracted Pages

- PDF p.1: abstract and publication metadata.
- PDF p.2: `3−⊗3−` quartet motivation and statement that conclusive identification remains open.
- PDF p.4: Table I and GOSIA analysis description.
- PDF pp.5–6: theory comparison, `Qs` interpretation and `800–1500 keV` splitting estimate.

## Experimental Chain

四种束流为 `70Ge`、`130Te`、`150Nd` 和 `166Er`，靶为富集 `208Pb`；γ 射线由
GRETINA 探测，束流/靶散射粒子由 CHICO2 提供位置、时间和散射角。GOSIA 对多种
束流和角度区间做联合分析。本文给出了装置和分析链，但没有提供本轮所需的
事件级响应矩阵或完整两声子候选 closure。

## Transfer and Limitations

- `208Pb` 可作为 `132Sn` 两声子实验的“强单声子、但 quartet 尚未闭合”控制，而不是
  已完成 quartet 的阳性金标准。
- `Qs` 是对 quadrupole–octupole coupling 敏感的补充 observable；它不能替代
  `0+,2+,4+,6+` 候选的逐态能级、feeding、寿命和 E3 分支。
- `800–1500 keV` 只属于本文在 `208Pb` 的 coupling-based estimate，不能迁移为
  `132Sn` 的预测区间。
- staging PDF 已核验身份与哈希，raw 归档和人工审核仍未完成。

## Human Review

本页是 Codex self-audit，保持 `unreviewed`；`HE25-*` 不设置为
`human-reviewed`。
