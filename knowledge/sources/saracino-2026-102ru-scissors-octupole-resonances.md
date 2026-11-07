---
type: source
title: "Saracino等2026：102Ru低能偶极强度分布与剪刀模及八极共振共存（PRL全文7页）"
aliases: [Saracino 2026 102Ru dipole response, PRL136252501, 10.1103/rcb1-gntj]
created: 2026-11-07
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Low-Energy Dipole Strength Distribution in 102Ru: Coexistence of Scissors and Octupole Resonances"
authors: [A. Saracino, A. D. Ayangeakaa, Q. B. Chen, S. Frauendorf, S. R. Johnson, R. V. F. Janssens, E. Churchman, S. W. Finch, D. Gribble, F. E. Idoko, X. K.-H. James, T. M. Kowalewski, M. Lee, A. Psaltis, K. Song]
journal: Physical Review Letters
year: 2026
volume: 136
pages: 252501
doi: 10.1103/rcb1-gntj
canonical_source: "doi:10.1103/rcb1-gntj"
citation_key:
raw_file: raw/papers/Low-Energy Dipole Strength Distribution in ¹⁰²Ru Coexistence of Scissors and Octupole Resonances.pdf
raw_sha256: 4bc6bb6c613b121bae9def9d9bedf37e9c02db89eca265c4c16d5dd9ecf43a89
highlight_file: raw/papers/gpt/query/20261107-round2-ru102-dipole/verified-official/author-highlight.html
highlight_sha256: 04b651d22a6e74c4b3e0d5abb798b2f1913c1e2d8ef73fc23943ac27c8b5692d
supplemental_file: raw/papers/gpt/query/20261107-continuation-G14/102Ru-PRL-136-252501-Supplemental-Material.pdf
supplemental_sha256: 8b9fba94fd43ea2af1860029889c0cb3e30ebb3c2cc29a5e0d749649c93a2df0
archive_required: true
nuclei: [102ru]
experiments: [TUNL-HIGS-clover-array]
models: [TAC-QRPA]
observables: [B(M1), B(E1), polarization-asymmetry, spectral-density, cumulative-strength]
tags: [nrf, scissors-mode, octupole-resonance, pdr, two-phonon, a100, fulltext-read, higs, tunl]
---

# 102Ru：NRF偶极响应、八极解释与共同拟合边界

## Bibliographic Record

A. Saracino et al., PRL136,252501(2026)，DOI10.1103/rcb1-gntj。
出版PDF为7物理页，在线日2026-06-23；正文首页、原件路径和SHA见元数据。

## Scope and Reading Depth

### Covered scope

完整7页主线、Figs1–4、Eqs1–2及参考列表。总控回查PDF2–6实验段、图注、
模型输入与结论；参考列表存在不等于已读53篇被引原文。
正文给出的是低自旋偶极响应与模型比较，没有直接E3矩阵元的本次测量。

### Not covered

此前附件入口失败的历史记录保留；本轮续接已取得5页Supplemental Material[33]，
读取pp1–3 TableI、p3 Eqs1–4及pp3–5模型/吸收截面比较。
尚无原事件、逐态完整Cov、效率/feeding响应或作者生产代码。PDF6 Data availability明确称
支持数据不公开，作者可接受合理请求；本轮未向他人发送请求。

## Acquisition History

早先实际只归档PubMed摘要XML、Crossref响应和作者网页；它们保持原字节，
当前以用户提供的610850字节出版PDF为底本。全文的获取关闭了原正文缺口，
当时未关闭SI、分支修正及可重放生产输入缺口；本轮续接SI已取得，后两项仍不完备。

## Experimental Setup

PDF2报告2 g、99.25(5)%富集粉末，HIγS线偏振束扫描2.30–8.70 MeV，
步长约3%且接近束宽FWHM，每点约3h。阵列含8 HPGe Clover与12 CeBr3；
四个HPGe在θ90°，方位平行和垂直偏振面各两个，另有后向探测器。
PDF3给塑闪监测、NaI(Tl)标定、0°HPGe束形与HORST响应处理。
这些是本文报告的装置条件，不是其它高自旋实验可直接照搬的灵敏度。

## Key Results

| ID | 实际内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SR26-F1 | 在所给几何，E1峰主要垂直偏振面，M1峰主要平行；图注给不对称度电−1、磁+1理想极限 | experimental-criterion | direct | PDF3 Fig1–2与邻段 | false |
| SR26-F2 | 约2–4MeV内ΣB(M1)↑≈1 μN²；后文报告总观测1.7 μN²，不能将两者默认为同一积分区间 | experimental-fact | direct | PDF3及PDF5 | false |
| SR26-F3 | 2.95MeV强E1的B(E1)↑=.016 e²fm²；4.5–5.5MeV、约4.9MeV中心有E1聚集，所述和约.1 e²fm² | experimental-fact | direct | PDF3 Fig2及正文；图注另列2953.2(19)、5080.9(31)keV | false |
| SR26-F4 | 平均场采用ε=.183、γ=0°，配对Δp=1.04、Δn=.97MeV；相互作用含可调IS/IV多极项 | model-result | direct | PDF4模型段 | false |
| SR26-F5 | E1算符Eq2含偶极项与八极极化项；b=.009 fm^-2与κIVOO=4κ3sc共同拟合累计E1，κIVDD=−1.5κ1sc采用100Mo的GDR约束 | model-result | direct | PDF5 Eq2至PDF6开头 | false |
| SR26-F6 | 当前仅IVDD模型的累计E1低于.01 e²fm²；加入上述八极项后再现累计强度和约5MeV聚集的大体特征 | model-result | direct | PDF4–6 Figs3–4 | false |
| SR26-F7 | 2.95MeV态可能为四极—八极两声子型，声子和2518keV；当前TAC-QRPA不描述这一孤立态 | author-interpretation | direct | PDF6 | false |
| SR26-F8 | 作者将约5MeV结构解释为形变诱导偶极—八极混合的低能八极共振 | author-interpretation | direct | PDF6结论 | false |

## Model Operators and Reading Boundary

本文Eq2为内禀表示
\[
 O(E1;\nu)=e_{\rm eff}rY_{1\nu}+e_{\rm eff}b_\nu r^3Y_{3\nu}.
\]
作者以八极声子在四极电荷分布上诱导的偶极极化解释第二项，并采用共同b。
这不是未经旋转恢复即可在实验室把秩1、秩3算符相加的普适张量定义。
SI3 Eqs1–4现已读到Hamiltonian的六项相互作用形式；这仍不等于独立恢复作者数值实现。
M1用0.7倍自由自旋g因子和IS/IV项分解（PDF4 Eq1、PDF5）。

## Competing Interpretations and Limitations

1. 作者把约5MeV峰与稳定核通常更高能的PDR区比较，认为八极解释有利；
   当前纯IVDD比较失败只限制该具体计算，不排除所有PDR、组态混合或扩展模型。
2. 作者对2.95MeV用“may”提出两声子解释；不能升级为已确定组态。
   一个孤立态解释失败也不把整个E1聚集指定为同一模式。
3. PDF4提D0约.3 e fm是文献物理量级的比较，并非本研究独立测得的102Ru静态D0。
   NRF E1强度不等于直接E3、非零β3或高自旋手征证据。
4. SI已给逐态BR，但没有完整响应及联合误差，不能声称全部分支/feeding已校正、窄束完全消除了feeding，
   或每个报告强度都是严格下界。主文没有公开这些问题的完整可重放输入。
5. 极化符号须带本实验几何/归一；不能无条件搬到Compton偏振不对称。
   A=(N∥−N⊥)/(N∥+N⊥)可作为与图注极限一致的重建，正文未单列这个公式。

## Summary

主文直接支持宇称分辨的M1/E1响应与约5MeV的E1增强；八极共振是结合
指定QRPA和扩充算符的作者解释。参数与算符从摘要未知变成可以具体核查，
对拟合可辨识性和跨自旋迁移的限制也随之更明确。

## Knowledge Impact and Learning Decision

`revises + provisional research-note`：参见[[campaign-g02-ru102-fulltext-20261107]]。
与[[karmakar-2024-100ru-enhanced-e1-lifetimes]]比较时保留核素、N、自旋、算符与采集谱系。
不以一个低自旋NRF响应替代100Ru高自旋交替宇称网络。

## Agent Self-audit Triage

P0: none identified in source identity/hash。P1：联合Cov、分支/feeding、拟合参数可识别性、
D0估计的身份及PDR/两声子排他性均按上述范围校准。
总控撤回worker草案的“全部争论闭合”、纯IVDD普适禁戒、固定形变必要值与
将拟合分解当独立实测贡献的说法。

## Extracted Pages

本地出版PDF1–7及本轮续接SI1–5；作者原始事件、完整联合Cov与代码未取得。


## 2026-11-07 Continuation: Supplemental Material

新附件5页、322835字节，路径及SHA见frontmatter。
[[continuation-g14-ru102-si-thesis-20261107]]记录106行转录、上下跃迁方向、模型形式与读取边界。
SI1–3 TableI有34个M1标签、72个E1标签（分别含1和6个括号标签）；
总控表列求和含括号为1.660 μN²与.15408 e²fm²，属于本任务算术而非新实验。
SI2的5081.22-keV母态/5080.93(31)-keV线有BR=.12(11)、B(E1)↑=.05(4)e²fm²，
其误差与其它行的完整Cov未公开；不可把所有表行或累计点当独立。
SI3 Eqs1–4提供六项IS/IV可分相互作用形式；SI3–4 SecIV/Fig2说明
κIVDD标定依赖100Mo的IVGDR，附图QRPA洛伦兹宽度Δ=3.5MeV，
SLO比较参数Eres15.5MeV、Γ7.0MeV、σres172mb。
这些补充不等于作者数值实现、原始事件及模型识别问题全部恢复。
