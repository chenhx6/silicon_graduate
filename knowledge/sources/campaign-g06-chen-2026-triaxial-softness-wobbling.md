---
type: source
title: "Effects of triaxial softness on wobbling motion"
aliases: [Chen 2026 triaxial softness wobbling, Chen 2026 gamma softness wobbling]
created: 2026-11-07
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: read
title_original: "Effects of triaxial softness on wobbling motion"
authors: [Yeruoxi Chen, Q. B. Chen, S. Frauendorf, R. V. Jolos]
journal: Physical Review C
year: 2026
volume: 114
pages: 014324
doi: 10.1103/f2zp-rb6f
arxiv:
language: en
canonical_source: https://doi.org/10.1103/f2zp-rb6f
citation_key:
zotero_item_key:
zotero_uri:
library_file:
raw_file: raw/papers/gpt/query/20261107-continuation-G16/chen-2026-triaxial-softness-wobbling-prc.pdf
raw_sha256: f0b2f1ae994d79817c41a01fa5f69e8d07a11338e6c2c6a061eaa45aa9e44274
archive_required: true
nuclei: []
reactions: []
experiments: []
models: [core-quasiparticle-coupling-model, triaxial-rotor-model]
observables: [wobbling-energy, interband-e2-strengths, wobbling-frequency]
methods: [core-quasiparticle-coupling]
tags: [theoretical-model, wobbling, triaxial-softness, gamma-softness, longitudinal-wobbling, transverse-wobbling, prc-2026]
---

# Chen2026：三轴软度与摆动的四情景模型比较（出版全文）

## Bibliographic Record

Yeruoxi Chen、Q.B.Chen、S.Frauendorf、R.V.Jolos，PRC114,014324(2026)，
DOI10.1103/f2zp-rb6f。实际出版PDF21页、7498113字节，路径/hash见元数据。
旧官方摘要HTML保持原字节，旧“只有摘要”的获取状态已由本轮正文更新。

## Scope and Reading Depth

### Covered scope

G16提取全文模型/比较段；总控重点回读PDF1、3、7、9、15、17–18，
核对单j/配对/费米面、E2/M1算符、两方向跃迁与结论。
[[continuation-g16-soft-core-wobbling-20261107]]保存共同输入合同及被收窄的worker断言。

### Not covered

未恢复作者生产代码/波函数及完整数值图点，附录尚未逐式重算。
作者PDF18声明数据不公开但可合理请求；本任务没有联系作者。
被引TPSM等作品的参数/运行不因本篇转引而视为已独立核验。

## Key Results

| ID | 实际内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CH26-F1 | 比较γ30°TR与γ无关WJ核芯，各耦合low-shell或midshell h11/2准粒子 | model-result | direct | PDF9 SecIV、PDF17 Summary | false |
| CH26-F2 | 核芯TR J0=30ℏ²/MeV、WJ C=.06MeV令基带谱接近；不是严格同谱 | model-assumption | direct | PDF7 SecIIID/Fig3 | false |
| CH26-F3 | 单j输入χ2=12.5MeV/b²、Δ1MeV、λF−2.5或0MeV | model-assumption | direct | PDF9 SecIV | false |
| CH26-F4 | E2只取核芯，M1先给完整gR/gl/gs形式，再以所用单j约化 | model-assumption | direct | PDF3 Eqs14–21 | false |
| CH26-F5 | 所研究low-shell+TR有TW到LW变化，low-shell+WJ没有TW；midshell的LW与前者高自旋LW跃迁模式不同 | model-result | direct | PDF15、17 | false |
| CH26-F6 | 两组不同初末态的ΔI1带间E2/M1对软度有比较价值；TR下E2变接近而非普适严格相等 | model-result | direct | PDF15、17及Fig15 | false |
| CH26-F7 | 作者认为未受扰动的偶邻核芯近似过简，奇粒子可改核芯；当前CQPC如何扩展仍待研究 | author-interpretation | direct | PDF17末–18开头 | false |

## Competing Interpretations and Limitations

1. 两个核芯极限和两个费米面代表值不构成所有真实核/所有软度的禁戒定理。
2. 能量增减须与波函数几何/跃迁网络共同判断；大E2混合比也不唯一摆动。
3. w(I)→y(I−1)与y(I)→w(I−1)连接不同态对，不能用详细平衡直接代换。
4. PDF17明确含M1排序的7.5→6.5例外，不写全自旋无例外结论。
5. A100/130的偶邻核软性不自动排除奇A核TW；反过来，本文也未认证任何具体实验候选。

## Knowledge Impact and Decision

旧摘要层边界已关闭，新增可复用的占据—核芯—算符共同输入合同。
下一步可比较真实核的两方向支路与奇粒子极化，不能先以偶邻核柔软度替代奇核波函数。

## Agent Self-audit Triage

Codex自审，不是human-reviewed。已移除worker的严格合并/永不合并/普适识别指纹、
完全匹配及未验证的机构授权归属。原始PDF字节不变；原获取时间元数据另由本轮核验回执限定。

## Extracted Pages

实际出版PDF1–21已可用；总控本轮重点页与未重算部分见Scope。


## Summary

本页记录该原件实际提供的实验/模型信息与读取边界；核心数据/公式沿用上文原表locator，不作为新实验或作者代码复现。
