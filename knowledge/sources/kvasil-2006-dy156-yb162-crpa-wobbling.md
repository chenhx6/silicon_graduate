---
type: source
title: "Kvasil–Nazmitdinov：156Dy、162Yb 的推转 RPA 与摆动"
aliases: [Kvasil 2006 Dy Yb wobbling]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
source_type: preprint-theory
reading_depth: deep-read
title_original: "Wobbling excitations in 156Dy and 162Yb"
authors: [J. Kvasil, R. G. Nazmitdinov]
year: 2006
arxiv: "nucl-th/0611059v1"
doi:
citation_key:
canonical_source: "arxiv:nucl-th/0611059v1"
raw_file: "raw/papers/gpt/query/20261108-r3-g45-quantum-labels/kvasil-nazmitdinov-2006-wobbling-dy156-yb162.pdf"
raw_sha256: "dee4d852c401c5d522b10655d26a477925f9e8da7b06c09190e66243f3fa2405"
archive_required: true
nuclei: [156dy, 162yb]
tags: [doctoral-foundations, crpa, wobbling, gamma-vibration, pairing]
---

# 推转 RPA 中的模式连续变化与实现条件

## Bibliographic Record

实际底本为17物理页预印本。首页边注和官方arXiv API均给v1、2006-11-16；
页面另印“Dated: August 14, 2018”，不据此改发表年。
API实际记录留在`raw/papers/gpt/query/20261108-r3-bibliography-audit/manifest.json`。
本轮未核定匹配的最终发表DOI，不从相似题名填入。

## Scope and Reading Depth

已核定 arXiv v1 的 17 个物理页。G45 先读 PDF 1–4、16，本轮补读 PDF 5–15、17，覆盖恢复对称性的 RPA 条件、摆动模的识别、实验能级的转动系比较、电磁衰变、附录和参考文献。视觉核对 PDF 9–10、12–13 的公式与图表。原 CRPA 程序及历史 NuDat 能级输入尚未复现。

## Summary

作者在指定推转Nilsson+RPA框架讨论γ分支与摆动型激发的演化，联合比较惯量和电磁跃迁，并明示配对处理近似。

## Key Results

| claim | claim_kind | evidence_level | locator | boundary |
|---|---|---|---|---|
| 在所研究模型中，156Dy奇自旋γ分支随推转频率改变可发展为摆动型激发 | author-model-interpretation | located-original | PDF1–2 | 不是任何γ带的普遍命运 |
| 同文对Dy与Yb带弯曲提出不同驱动：γ软模与中子对顺排 | model-calculation | located-original | PDF3–4, Eq.(6), Figs.2–3 | 使用特定平均场、残余作用与配对方案 |
| Eq.(6)在带交叉附近采用唯象配对隙处方避免数值奇异 | explicit-model-input | located-original | PDF3 | “自洽”不等于所有输入从一个无近似泛函导出 |
| 动力学惯量与TV惯量的比较用作实现一致性检查 | author-method | located-original | PDF4, Fig.3 | 图上吻合不是所有响应和实验解释的充分检验 |
| 带间E2与M1含不同惯量组合和内禀算符 | analytical-approximation | located-original | PDF16, Eqs.(A.13)–(A.18) | 明示高自旋、忽略相应1/I项 |
| \(c_\nu\) 从四极振幅的乘积构造，并满足包含冗余模的总和关系。作者在所选计算中将 \(c_\Omega=-1\) 的转动冗余模与 \(c_w\simeq+1\) 的摆动态区分，后者的识别使用其余物理解的乘积贡献近似相消。 | model-mode-diagnostic | located-original | PDF 6 Eqs. (20), (27)；PDF 9 Eqs. (49)–(54)；PDF 10 Figs. 8–9 | \(c_\nu\) 是带符号的模型诊断量。对称性守恒与冗余模分离的数值质量影响该判据。 |
| \(^{162}\mathrm{Yb}\) 的最低负签名解在约 \(\hbar\Omega=0.32\) MeV 由作者按 Eq. (54) 归为摆动态。其 E2 分支偏向低自旋末态约在 \(0.28\) MeV 起出现。\(^{156}\mathrm{Dy}\) 的相应分支变化正文给约 \(0.32\) MeV，Fig. 12 图注给较粗的 \(\hbar\Omega\geq0.3\) MeV。 | model-result | located-original | PDF 10 右栏，PDF 12 Eq. (65)，PDF 13 Figs. 11–12 和右栏 | Figs. 11–12 为计算强度，曲线由两种模型表达取出。Fig. 10 的带内 E2 数据与这里的带间计算区分记录。 |
| 采用文中 PA 轴序及 \(W_2,W_3>0\)，Eq. (65) 用两条 E2 分支的强弱关系区分 \(\gamma\) 符号。Eq. (74) 的 M1 优势分支在该近似下对 \(\gamma\) 符号无要求。 | model-selection-rule | located-original | PDF 9 Eq. (44)；PDF 12 Eqs. (63)–(65)；PDF 14 Eqs. (73)–(74)；PDF 15 附录 A | 回到同一带身份、内禀轴序与高自旋近似后才可应用。 |

## Competing Interpretations and Limitations

原文对旧模型的批评属于其理论比较；不能倒写成已由独立实验排除旧模型。
附录的主轴排序及稳定条件属于指定展开点，不能代替所有粒子转子分支。
由电磁跃迁推断γ符号须保留轴序、算符、组态与模型条件。

## Extracted Pages

- [[doctoral-r3-quantum-labels-and-model-boundaries-20261108]]
- [[doctoral-foundations-research-question-register-20261108]]
