---
type: output
title: "高自旋 127 篇候选 PDF 身份与污染审计"
created: 2026-09-20
updated: 2026-09-20
status: user-confirmed-input-audit
review_status: unreviewed
tags: [high-spin, identity-audit, contamination, 2026-09-20]
---

# 高自旋 127 篇候选 PDF 身份与污染审计

## 审计边界

本报告记录 `raw/high-spin-reading-record.md` 中 127 个未匹配条目及其外部目录 `/workspace/zotero-reference/高自旋/` 的身份审计。用户随后已核实并删除下列 9 个污染 PDF；本报告保留历史审计结果，当前执行基线以最终计划和输入快照为准。本轮没有建立 `knowledge/sources/` 来源页。

台账原始统计为：244 个候选 PDF，117 个 SHA-256 已在 `raw/papers/` 匹配，127 个尚未匹配。127 条台账路径本次均能在外部目录定位，未发现缺失路径。

## 初步计数

| 类别 | 数量 | 处理含义 |
|---|---:|---|
| 台账条目 | 127 | 每条均保留原相对路径 |
| 唯一 SHA-256 | 119 | 127 条中有 8 条是重复副本 |
| 精确重复组 | 5 组 | 只保留一个 canonical candidate |
| 重复副本条目 | 8 | 不作为独立文献重复摄入 |
| 用户确认污染并删除 | 9 | 排除，不下载恢复，不计入未读欠账 |
| 其余唯一候选 | 110 | 暂保留为核结构/方法/理论候选，不代表已完成科学核验 |

“身份污染”是文件身份判断；9 项现已由用户确认并删除。其余候选仍需在正式摄入前完成题名、作者、版本和正文身份核验。

## 疑似身份污染（9 条）

以下条目的文件名直接指向非低能核结构主题，且 PDF 元数据或页数与该主题一致：

1. `三轴/进动/理论/1977_Cohen et al_Tachycardia and bradycardia-dependent bundle branch block alternans.pdf`
2. `三轴/进动/理论/1975_Sandhu et al_Potable water quality in rural Georgetown County.pdf`
3. `1975_Radiochemical assay of glutathione S-epoxide transferase and its enhancement by phenobarbital in rat.pdf`
4. `1975_Atomic models for the polypeptide backbones of myohemerythrin and hemerythrin.pdf`
5. `1975_Effect of chloroquine on cultured fibroblasts release of lysosomal hydrolases and inhibition of the.pdf`
6. `1975_Formate assay in body fluids application in methanol poisoning.pdf`
7. `形变/1975_Cannon et al_N-Isopropyl derivatives of dopamine and 5,6-dihydroxy-2-aminotetralin.pdf`
8. `1975_Metal substitutions incarbonic anhydrase a halide ion probe study.pdf`
9. `1975_Maturation of the adrenal medulla--IV. Effects of morphine.pdf`

用户已完成裁决：9 项均排除并删除源文件。

## 精确重复组（8 个副本条目）

这些不是身份污染，但应避免重复摄入：

- `NPA695-Jensen-2001-3.pdf` 与 `纲图/2001_Jensen et al_General properties of the πh92[541]12− configuration and level scheme of 165Tm.pdf`：2 份相同 PDF。
- `multipolarity/angular distribution/polarizaiton/1970_Twin et al_Polarization and angular correlation measurements following the 40Ar(p, nγ)40K reaction.pdf`、`...following the 40Ar(p, nγ)40K.pdf` 与 `multipolarity/mixing ratio/1970_Twin et al_Polarization and angular correlation measurements following the 40Ar(p, nγ)40K reaction.pdf`：3 份相同 PDF。
- `形变/2021_Nomura et al_Coupling of pairing and triaxial shape vibrations in collective states of γ.pdf` 与 `振动/2021_Nomura et al_Coupling of pairing and triaxial shape vibrations in collective states of γ -soft nuclei.pdf`：2 份相同 PDF。
- `振动/2018_Eldridge et al_E2M1 mixing ratios in transitions from the gamma vibrational bands to the ground state rotational b 1.pdf` 与 `振动/2018_Eldridge et al_E2M1 mixing ratios in transitions from the gamma vibrational bands to the ground state rotational b.pdf`：2 份相同 PDF。
- `review/1965_Davidson_Rotations and Vibrations in Deformed Nuclei 1.pdf`、`review/1965_Davidson_Rotations and Vibrations in Deformed Nuclei.pdf`、`形变/1965_Davidson_Rotations and Vibrations in Deformed Nuclei.pdf` 与 `振动/1965_Davidson_Rotations and Vibrations in Deformed Nuclei.pdf`：4 份相同 PDF。

## 暂不判为污染的项目

其余 110 个唯一候选暂保留。某些文件可能是预印本、勘误、补充材料、版本副本或目录分类不准确，但仅凭文件名和基础 PDF 元数据不能安全排除；后续需在用户裁决后做题名/作者/DOI 和正文首页核验。

## 下一步状态

污染裁决已完成。9 个污染路径当前不存在；原 127 条清单保留历史 ID。剩余 118 个文件、110 个唯一哈希和 8 个精确重复副本进入最终计划的全文学习与摄入后自我审核路线。重复 PDF 不重新摄入，但不得跳过逐条 source 映射和自我审核。全文摄入、raw 复制、知识库写回和 L3/L4 仍等待用户审阅最终计划并明确启动。
