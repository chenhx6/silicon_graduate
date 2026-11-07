---
type: source
title: "Hinohara 2015：NG 惯量、零频响应及出版版本核查"
aliases: [Hinohara 2015 Nambu Goldstone inertia, pairing rotational FAM]
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article-theory
reading_depth: skimmed
title_original: "Collective inertia of the Nambu-Goldstone mode from linear response theory"
authors: [Nobuo Hinohara]
journal: Physical Review C
year: 2015
volume: "92"
pages: "034321"
doi: 10.1103/PhysRevC.92.034321
arxiv: 1507.00045v1
language: en
canonical_source: https://doi.org/10.1103/PhysRevC.92.034321
citation_key: ""
raw_file: raw/papers/gpt/query/20261108-r2-t05-response-definitions/aps-publication.pdf
raw_sha256: 764d644a2349235027e15c320d78f15fcd7d8fd264ebe6412fd2b80e1a625f86
preprint_file: raw/papers/gpt/query/20261108-r2-g39-fam-ng/hinohara-2015-collective-inertia-ng-fam.pdf
preprint_sha256: fedcecbf8bdc7981ee4c3073ed2cc6aba384f34bc414edba4185053e0eb3c0bf
raw_storage_status: archived-local
archive_required: true
nuclei: [26mg, 116sn, 142nd, 130xe]
reactions: []
experiments: []
models: [hfb, fam-qrpa, sly4, pairing-rotation]
observables: [static-response, pairing-rotational-inertia, binding-energy-curvature]
methods: [finite-amplitude-method, nambu-goldstone-mode]
tags: [doctoral-foundations, linear-response, pairing, source-version-audit]
---

# 同样叫“转动”的配对规范响应与空间取向响应

## Bibliographic Record

主底本为 APS 发表版，**13 个物理页**；arXiv v1 为 14 页。
官方 arXiv 页面及 API 核查仍只有 v1，最新 PDF 与原 v1 字节相同。
两个版本均保留；以下公式默认指 APS 页/式，不能将预印本的编号直接代入。
APS 发表记录为 2015-09-21。网页/题录和本次版本获取在 T05 collection manifest。

## Scope and Reading Depth

- Completed reading_depth: skimmed，有界公式、版本与数值核查。
- Covered scope: APS pp. 3,5–10 的实/虚 QRPA 分块、NG 零频响应、
  共轭坐标、IB、平移和配对应用；与 arXiv v1 的相应公式对读。
  总控直接核出版 pp. 3,5–6,8–10，Terra 独立推导定义与因子。
- Not covered: 全文全部 PQ 展开重推、作者生产代码、全部基底收敛、
  130Xe 参考态和约束族的独立再计算、所有历史引用与完整勘误库穷尽搜索。

## Paper Question and Scientific Motivation

利用 NG 生成元的零频线性响应计算 Thouless–Valatin 惯量，并构造共轭坐标。
数值应用以平移和粒子数规范旋转为主；
空间三维转动在结论中作为后续实现方向，而非本文已逐轴算出的实核张量。

## Method and Design Logic

对精确守恒的 NG 生成元，非零频通常的激发强度与严格零频静态解需要分别处理。
作者给 \(S(P,0)=-M_{\rm NG}\)，共轭坐标的响应则有 \(1/\omega^2\) 极点。
外场取 P 是便捷路线，不能说只有 P 才能给惯量。
在可选实 A、B 的约定中，实与纯虚准粒子对矩阵元分别涉及 A+B 和 A−B。
基底、相位、外场符号和可逆子空间不可省略。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| H15-1 | 一般 NG 惯量同时有实/虚分量，不能把所有“动量生成元”统一套入 A+B。 | model-result | direct | APS p. 3, Eqs. (18)–(23); p. 5, Eqs. (49)–(51) | false |
| H15-2 | \(S(P,0)=-M_{\rm NG}\) 是严格零频解；近似对称性时有限伪模能量的处理为近似，不是任意小基底都自动精确。 | model-result | direct | APS pp. 5–7, Eqs. (49)–(60) | false |
| H15-3 | 116Sn 的中子配对转动模型值 TV=5.95、Belyaev=4.71 MeV⁻¹；属于指定 EDF/配对及参考态。 | model-result | direct | APS p. 8, Sec. VII A, Fig. 4 | false |
| H15-4 | 142Nd 的质子配对转动模型值 TV=2.35、Belyaev=6.13 MeV⁻¹；作者将其差异解释为残余库仑作用的重要贡献。 | model-result | direct | APS p. 9, Sec. VII A, Fig. 5 | false |
| H15-5 | 上述相反方向的变化反对“全部集体惯量都按同一固定因子增大”，但该质子配对例子不是空间转动 TV 张量的直接反例计算。 | our-inference | contextual | H15-3/4 与其配对通道定义 | false |
| H15-6 | 130Xe 的 \(J_{np}=-4.236\) MeV⁻¹ 按作者定义是交叉曲率元素的倒数，不是惯量矩阵或响应矩阵的 np 元。 | model-result | direct | APS p. 10, Eqs. (76)–(80) 及 Sec. VII C | false |

## Summary

NG 语言描述关于破缺平均场的局域响应，不是说精确有限核态失去粒子数。
空间取向、配对规范角及配对幅度振动对应不同的生成元、坐标和单位。
质量差分只有在光滑局部态族与结构变化受控时才近似配对能面曲率。

## 版本差异与原件内部边界

1. arXiv v1 p. 6 Eq. (54) 的 \(-M/2\)，在 APS p. 6 Eq. (56) 为
   \(+M/2\)；后者与其 \(H+\lambda P\) 符号相容。
2. 常 \(T_z\) 路径在 APS p. 10 Eq. (82) 为同一曲率组合乘
   \((\Delta A)^2/4\)，v1 p. 11 Eq. (80) 未带这个 1/4。
3. APS p. 6 Eq. (61) 仍印有外侧因子 2：
   对不重复准粒子对求和，其分子已经是
   \(F_i^{20*}F_j^{20}+F_i^{20}F_j^{20*}\)。
   按同页 Eqs. (62)–(64) 直接代入冻结场振幅，得到的同一分子没有这个外侧 2。
   总控/独立理论审计记录为**公式之间的二因子内部差异**，
   不据此认定作者实际数值程序用了哪个式或所有结果错误。
4. APS p. 10 报 130Xe 的三个正号响应值 12.704、8.725、3.083 MeV⁻¹，
   以及 \(J_{nn}=11.986,J_{np}=-4.236,J_{pp}=2.909\) MeV⁻¹。
   按其定义构造曲率矩阵
   \(C_{ab}=1/J_{ab}\)，任务算术给
   \(\det C\simeq-0.02705\ \mathrm{MeV}^2\)；
   它不是正定响应 Schur 补证明的例子。
   固定 N、Z 的参考态稳定与释放粒子数方向后的能面凸性是不同条件，
   **不能仅凭这个行列式宣称原子核的形状 HFB 解不稳定或论文计算错误**。
   其数值/符号/约束路径须在具体应用中另核，不能静默换号或改为正定。

第 3、4 项是任务自审，尚不是出版商承认的勘误。
APS 作品页和本次 Crossref 记录未见更正关联，不代表穷尽所有更正渠道。
矩阵算术及推导持久化于
[[doctoral-r2-collective-inertia-response-crosswalk-20261108]]；
运行回执不作为论文事实源。

## Competing Interpretations and Limitations

正的谱函数强度、可能为负的实静态响应 S、正定 Hessian 中的正磁化率，
是不同对象；必须连同外场符号与约束写出。
局部 QRPA 共轭规范角的态平均对易归一化不等于完整有限 Hilbert 空间存在
全局自伴的角算符严格满足 \([\Theta,N]=i\)。
关于粒子数 NG 的结论不能直接证明配对消失后的空间流必为刚体。

## Knowledge Impact and Learning Decision

supports：响应定义、实/虚分块和配对/空间转动的区分；
limits：固定 TV/IB 因子、将 \(J_{np}\) 当响应矩阵元、仅用 v1 公式而忽略出版修改。
与 [[petrik-kortelainen-2018-rotational-tv-inertia]] 是方法发展依赖，
不是两个独立实验。

## Agent Self-audit Triage

P0：APS/预印本身份、关键方程、两个配对数值和矩阵定义已经双版本对读；
公式内部差异隔离，不拿来校准模型或证明稳定性。
P1：混合配对曲率的约束条件、全/半空间因子和作者程序仍需具体任务核查。
P2/P3：没有用户逐项审核事件；citation key 不猜测；原件不进入公开 Git。

## Extracted Pages

- 可复用方法与比较合同：[[doctoral-r2-collective-inertia-response-crosswalk-20261108]]。
- 具体案例、真实表与边界：[[doctoral-r2-inertia-evidence-and-band-reconstruction-20261108]]。
- 当前不另建能带或实验页；本来源中的实核数值与模型条件按上文保留，
  不将理论参数登记成新的测量。
