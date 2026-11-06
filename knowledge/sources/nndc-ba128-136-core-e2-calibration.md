---
type: source
title: "NNDC 128–136Ba 偶偶核心 E2 标定：评价强度、寿命方向与数据依赖"
aliases: [Five-Ba core E2 calibration, 128–136Ba first-2+ ENSDF calibration]
created: 2026-11-06
updated: 2026-11-06
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data-tables
reading_depth: read
authors: [Zoltan Elekes, Janos Timar, Balraj Singh, Yu. Khazov, A. A. Rodionov, S. Sakharov, A. A. Sonzogni, E. A. McCutchan]
title_original: "128,130,132,134,136BA ADOPTED LEVELS, GAMMAS / COULOMB EXCITATION"
journal: Nuclear Data Sheets
year: 2026
year_basis: snapshot-acquisition-year
publication_years: [2001, 2004, 2005, 2015, 2018]
doi:
citation_key: NNDC_Ba128_136_core_E2_snapshots
citation_key_origin: agent-local-dataset-collection-label
canonical_source: "NNDC ENSDF: adopted 128056001,130056001,132056001,134056001,136056001; Coulomb 130056007,132056010,134056008,136056012"
data_version: "128:201510; 130:200107; 132:200504; 134:200410; 136:201810; actual archived retrieval UTC 2026-11-05"
raw_file: "raw/papers/gpt/query/20261106-ba-core-E2-calibration/manifest.json"
raw_sha256: "ee30e3a0c13f8f5187f871b794269e085810b8f81e68c56c4e08c0363e6e192b"
reused_archive_file: "raw/papers/gpt/query/20261105-ba129-core-constraints/manifest.json"
reused_archive_sha256: "4aa6e4e1e746fea3a1444d5399d5343254fedce09b53e82f98bb23a1b6a330c0"
raw_storage_status: archived-local-public-evaluated-data
archive_required: true
nuclei: [128ba, 130ba, 132ba, 134ba, 136ba]
reactions: [Coulomb-excitation, heavy-ion-fusion-evaporation]
observables: [B-E2, half-life, gamma-energy, internal-conversion-coefficient]
methods: [evaluated-data-audit, detailed-balance, lifetime-to-transition-strength, calibration-dependency-audit]
tags: [ensdf, nndc, a130, even-core, e2-calibration, covariance, source-dependence]
---

# NNDC 128–136Ba 偶偶核心 E2 标定

## Summary

本页固定 \(^{128,130,132,134,136}\mathrm{Ba}\) 第一 \(2^+\) 态至 \(0^+\) 基态的五个 E2 标定输入。选定的向下强度依次为 **0.2765251611、0.2326、0.1720、0.1358、0.0814 \(e^2b^2\)**。前者按已声明的寿命换算约定计算；后四者来自评价所列绝对向上强度，再除以 5。它们是已有核数据评价及其条件换算，不是五次新测量，也不是本页执行的模型拟合。

## Bibliographic Record

Frontmatter 的 `year: 2026` 仅指本集合的 **NNDC 快照获取年份**，不表示所有评价或原实验发表于 2026 年；各评价出版年份及文献截止日以下表为准。

| 核素 | Adopted 数据集／记录戳 | 文献截止日 | 评价书目信息 |
|---|---|---|---|
| \(^{128}\)Ba | 128056001／201510 | 2015-02-28 | Z. Elekes、J. Timar，NDS **129**, 191 (2015) |
| \(^{130}\)Ba | 130056001／200107 | 2001-05-11 | B. Singh，NDS **93**, 33 (2001) |
| \(^{132}\)Ba | 132056001／200504 | 2005-02-10 | Yu. Khazov、A. A. Rodionov、S. Sakharov、B. Singh，NDS **104**, 497 (2005) |
| \(^{134}\)Ba | 134056001／200410 | 2004-07-31 | A. A. Sonzogni，NDS **103**, 1 (2004) |
| \(^{136}\)Ba | 136056001／201810 | 2018-04-01 | E. A. McCutchan，NDS **152**, 331 (2018) |

身份定位均在对应 ENSDF 文本第 2–4 行。2026 年是归档时间，不是这些评价或原实验的年份；部分 Q 记录有更晚的质量表引文，也不能据此更新谱学文献截止日。目录名 `20261106` 与实际保存的 2026-11-05 UTC 获取时间分别保留。

## Scope and Reading Depth

**来源身份与阅读边界。** 实际证据是两个既存 manifest 绑定的官方 NNDC ENSDF 对象、完整 HTTP 响应和已归档 PDF。读核了第一 \(2^+\) 能级、所属 γ 记录、评价说明及 Coulomb-excitation 方法分支；没有以评价摘要代替原始实验论文的全文审查。评价转述的 RDDS、DSAM 和 Coulomb-excitation 实验结论保留其原始文献键，但本页的直接证据层是**评价记录**。

**Covered scope：** 五核素第一 \(2^+\) 标定记录、原文定位、方向换算、评价依赖和所列替代分支。

**Not covered：** 全部能级／反应数据集的逐条审查、原实验论文全文和未提供的联合协方差；不将局部核查标为全文 `deep-read`。

## Key Results

下表汇总既有正文。实验量的 `indirect` 指经评价转述原实验；`direct` 指直接核到评价处理说明或完成本页所列的条件计算，不表示重新测量。`confidence` 仅针对各行限定的记录／计算结论。

| ID | 陈述 | claim_kind | evidence_level | source_independence | confidence | locator | needs_review |
|---|---|---|---|---|---|---|---|
| BAE2-1 | 五个 adopted 第一 \(2^+\) 态均列一条至 \(0^+\) 的纯 E2 γ；能级能量、实际 γ 能量、半衰期和 ICC 分别保留。 | experimental-fact | indirect | multiple-dependent | high | Adopted 128056001 L48–53；130056001 L43–60；132056001 L75–84；134056001 L25–32；136056001 L51–64；下方原件链接 | false |
| BAE2-2 | \(^{128}\)Ba 由 \(105(9)\) ps、284.10(8) keV 和 \(\alpha=0.0539\)，在 parent/task-declared \(C_{E2}\) 下换算出 \(B_\downarrow=0.2765251611\ e^2b^2\)；系数不归属于用户或 ENSDF 原记录。 | our-inference | direct | single | high | 128056001 L48、L51；本页“半衰期、平均寿命和方向因子”中的声明与公式 | false |
| BAE2-3 | \(^{130,132,134,136}\)Ba 所选向上强度按 \(B_\uparrow=5B_\downarrow\) 换向；不把反向量另计为数据。 | our-inference | direct | multiple-dependent | high | Coulomb 130056007 L18；132056010 L13；134056008 L15／PDF p.1；136056012 L47；其余向上箭头见 adopted PDF p.1 | false |
| BAE2-4 | \(^{132,134,136}\)Ba 的第一态寿命由 B(E2) 导出；\(^{130}\)Ba adopted 寿命含由 B 导出的分量。 | author-interpretation | direct | multiple-dependent | high | Adopted 132056001 L81；134056001 L29；136056001 L55；130056001 L55–56 | false |
| BAE2-5 | 保留的干涉分支、评价组成和方法替代值不增加独立标定点；共同来源键不足以确定跨核素数值协方差。 | our-inference | direct | multiple-dependent | high | Coulomb 130056007 L20–22；132056010 L15–17；134056008 L17–19；136056012 L48–54；下方替代表和依赖说明 | false |
| BAE2-6 | \(^{128}\)Ba 所列寿命／能量一阶误差贡献不是完整误差预算；未给出的总 ICC 误差和协方差不补零。 | our-inference | direct | single | high | 128056001 L48、L51；本页“误差与协方差边界”的传播公式 | false |

**能级、γ 能量及所选强度。** 括号沿用来源的末位误差记法；没有重新赋予置信水平或误差分布。\(B_\uparrow\) 指 \(0_1^+\to2_1^+\)，\(B_\downarrow\) 指 \(2_1^+\to0_1^+\)。

| 核素 | \(E_x(2_1^+)\), keV | 实际 \(E_\gamma\), keV | 所列 \(T_{1/2}\), ps | \(\alpha_{\rm tot}\) | 所选 \(B_\uparrow\), \(e^2b^2\) | \(B_\downarrow\), \(e^2b^2\) |
|---|---:|---:|---:|---:|---:|---:|
| \(^{128}\)Ba | 284.00(8) | **284.10(8)** | 105(9) | 0.0539 | 1.3826258057，换算值 | 0.2765251611，换算值 |
| \(^{130}\)Ba | 357.38(8) | 357.4(1) | 41.8(12) | 0.0262 | 1.163(11) | 0.2326，原报误差幅换算为 0.0022 |
| \(^{132}\)Ba | 464.508(12) | 464.52(3) | 15.1(11) | 0.0121 | 0.86(6) | 0.1720，原报误差幅换算为 0.0120 |
| \(^{134}\)Ba | 604.7223(19) | 604.721(2) | 5.12(9) | 0.00599 | 0.679(11) | 0.1358，原报误差幅换算为 0.0022 |
| \(^{136}\)Ba | 818.522(10) | 818.514(12) | 1.89(3) | 0.00283 | 0.407(7) | 0.0814，原报误差幅换算为 0.0014 |

五个第一 \(2^+\) 能级块均只列一条至 \(0^+\) 基态的纯 E2 γ，所列相对光子强度为 100。它是强度归一化，不是 100 次计数，也不是包含转换电子后的光子分支概率。下述单支换算以该评价的衰变分支完整为条件；没有从“仅列一条”推断额外的分支完整性误差。

能级拟合能量与实际 γ 能量分开保留。特别是 \(^{128}\)Ba 的换算使用 **284.10 keV**，不能替换为 284.00 keV。所有 \(\alpha_{\rm tot}\) 字段均未给出总系数的误差；空误差保留为未知，不能当成测得的零误差，也不把带误差的分壳层系数直接相加成总误差。上述记录定位如下：

| 核素 | Adopted 文本定位 | Coulomb 文本定位／向上方向核验 |
|---|---|---|
| \(^{128}\)Ba | [L48 第一 \(2^+\)](/workspace/wiki/raw/papers/gpt/query/20261105-ba129-core-constraints/nndc128-adopted-text.ens:48)；L51 γ／ICC；L52 `BE2W=72 7`；L17–18 寿命一般来源 | 所选换算不使用另一个绝对 Coulomb 强度；adopted PDF p.1 能级、p.5 γ |
| \(^{130}\)Ba | [L43 能级](/workspace/wiki/raw/papers/gpt/query/20261105-ba129-core-constraints/nndc130-adopted-text.ens:43)；L46 B；L55–56 寿命依赖；L58 γ | [130056007，L18 所选 B](/workspace/wiki/raw/papers/gpt/query/20261105-ba129-core-constraints/nndc130-coulomb-text.ens:18)；L20–22 分支；adopted PDF p.1 明示 \(B(E2)\uparrow\)，p.3 γ |
| \(^{132}\)Ba | [L75 能级](/workspace/wiki/raw/papers/gpt/query/20261106-ba-core-E2-calibration/nndc132-adopted-text.ens:75)；L77 B；L81 寿命由 B 导出；L82 γ | [132056010，L13 所选 B](/workspace/wiki/raw/papers/gpt/query/20261106-ba-core-E2-calibration/nndc132-coulomb-text.ens:13)；L15–17 符号分支；adopted PDF p.1 向上箭头、p.6 γ |
| \(^{134}\)Ba | [L25 能级](/workspace/wiki/raw/papers/gpt/query/20261106-ba-core-E2-calibration/nndc134-adopted-text.ens:25)；L29 B／寿命依赖；L31 γ | [134056008，L15 所选 B](/workspace/wiki/raw/papers/gpt/query/20261106-ba-core-E2-calibration/nndc134-coulomb-text.ens:15)；L17–19 组成；L24 寿命由 B 导出；[Coulomb PDF](/workspace/wiki/raw/papers/gpt/query/20261106-ba-core-E2-calibration/nndc134-coulomb.pdf) p.1 明示向上箭头，adopted PDF p.5 γ |
| \(^{136}\)Ba | [L51 能级](/workspace/wiki/raw/papers/gpt/query/20261106-ba-core-E2-calibration/nndc136-adopted-text.ens:51)；L53 B；L55 寿命由 B 导出；L62 γ | [136056012，L47 所选 B](/workspace/wiki/raw/papers/gpt/query/20261106-ba-core-E2-calibration/nndc136-coulomb-text.ens:47)；L48–54 依赖／分支；adopted PDF p.1 向上箭头、p.7 γ |

上述行号绑定归档的 `*-text.ens`：它们是 HTTP HTML 中唯一 `pre` 元素的原样 UTF-8 文本，未重排固定列宽；响应、提取文本和 PDF 的 SHA-256 由 manifest 分别记录。后续重取 NNDC 对象时应作为另一版本处理。

**半衰期、平均寿命和方向因子。** ENSDF 本页引用的 \(T\) 是半衰期 \(T_{1/2}\)。平均寿命是 \(\tau=T_{1/2}/\ln2\)，故总衰变率既可写为 \(\ln2/T_{1/2}\)，也可写为 \(1/\tau\)；不能将同一个数值同时当作两种时间。

本轮采用的数值约定为

\[
\lambda_\gamma(E2)
=C_{E2}E_\gamma^5B_\downarrow,\qquad
C_{E2}=1.2239\times10^{13},
\]

其中能量以 MeV、强度以 \(e^2b^2\)、速率以 \({\rm s}^{-1}\) 计。**这个 \(C_{E2}\) 是 parent/task-declared 的固定换算约定，不是用户指定的常数，也不是从本页 ENSDF 原记录提取的数值。** 本次只纠正归属，保持该系数及所有标定值不变；其来源层级与评价数据分开记录。

对本页采用的一条纯 E2 总跃迁支路，

\[
\lambda_{\rm tot}=(1+\alpha_{\rm tot})\lambda_\gamma,\qquad
B_\downarrow=
\frac{\ln2}{T_{1/2}\,C_{E2}E_\gamma^5(1+\alpha_{\rm tot})}
=\frac{1}{\tau\,C_{E2}E_\gamma^5(1+\alpha_{\rm tot})}.
\]

转换电子因子只计一次。若改为多支情形，光子分支应为
\(b_{\gamma,j}=I_{\gamma,j}/\sum_k I_{\gamma,k}(1+\alpha_k)\)；
对纯 E2 的第 \(j\) 支再用
\(B_{\downarrow,j}=\ln2\,b_{\gamma,j}/(T_{1/2}C_{E2}E_{\gamma,j}^5)\)。
缺少所需 ICC 时不能自动补零。

标准约化跃迁几率满足

\[
(2J_i+1)B(i\to f)=(2J_f+1)B(f\to i),\qquad
B_\uparrow(0\to2)=5B_\downarrow(2\to0).
\]

因子 5 来自初态磁子态平均，和半衰期的 \(\ln2\)、内转换修正属于不同环节。若模型给出的是单位算符的 \(B_{\rm unit}(0\to2)\)，相应电荷应按
\(e_B^2=5B_{\downarrow,\rm adopted}/B_{\rm unit}(0\to2)\)
确定；若模型直接给出 \(B_{\rm unit}(2\to0)\)，则没有额外的 5。本页不计算任何特定模型的 \(e_B\)。

\(^{128}\)Ba 的 `BE2W=72 7` 是同一衰变汇总中的向下 W.u. 值，具有舍入与单位约定依赖。本页保留该记录，但不把它另计为一条独立绝对 B 数据，也不另引入半径约定替换已声明的 \(T/E_\gamma/\alpha\) 换算。

## Competing Interpretations and Limitations

**误差与协方差边界。** \(^{128}\)Ba 从 \(105(9)\) ps 得到的仅寿命一阶误差贡献为
\[
\Delta_T B_\downarrow
=B_\downarrow\,\frac{9}{105}
=0.023702156669\ e^2b^2.
\]
单独的 γ 能量一阶贡献为
\[
\Delta_E B_\downarrow
=5B_\downarrow\,\frac{0.08}{284.10}
=0.000389334968\ e^2b^2.
\]
这两个量没有被解释为完整置信区间，亦未在缺少协方差的情况下自动合成。总 ICC 的误差、系数的误差及它们和其它输入的相关性均未提供。

在有合适误差模型时，单支换算的一阶梯度为
\[
\nabla_{(T,E,\alpha,C)}B
=\left(-\frac BT,-\frac{5B}{E},
        -\frac B{1+\alpha},-\frac BC\right).
\]
只有给定相应输入协方差 \(\Sigma\)，才可用
\(\mathrm{Var}(B)\simeq\nabla B\,\Sigma\,(\nabla B)^T\)；
这里写出传播关系不等于已指定 \(\Sigma\)。上、下两个方向又满足精确比例，不能按独立数据处理；同一来源的寿命、B 值和 W.u. 汇总也必须保留依赖。

| 核素 | 重复计数风险及证据 |
|---|---|
| \(^{128}\)Ba | Adopted L17–18 的一般说明是 RDDS 2000Pe20／2000Pe19 或 DSA 1998Pe17；第一 \(2^+\) 块未印出逐实验权重。选定 \(105(9)\) ps 及其换算 B、W.u. 只占一个数据块，不虚构该行背后的独立测量数。 |
| \(^{130}\)Ba | Adopted L55–56 写明 \(41.8(12)\) ps 为 \(43.2(5)\) ps RDDS 与由所选 Coulomb B 导出的 \(40.7(4)\) ps 的评价加权结果。不能再把 adopted T 与所选 B 当作完全独立约束。 |
| \(^{132}\)Ba | Adopted L81、Coulomb L9 明说 T 来自 B(E2)，不是新增寿命观测。 |
| \(^{134}\)Ba | 第一态 Adopted L29／Coulomb L24 明说 T 来自 B(E2)，优先于文件层面的一般寿命来源说明。 |
| \(^{136}\)Ba | Adopted L55／Coulomb L48 明说评价者由 B 与 adopted γ 性质导出 T；不能与 B 重复计数。 |

所选来源中，1989Bu07 同时出现于 \(^{130,134}\)Ba，1972Ke16 同时出现于 \(^{134,136}\)Ba；这是共同来源依赖提示，不足以给出事件重叠或数值相关系数。跨同位素协方差保留为未知，不能把五行输入直接等同于五个统计独立观测。“独立偶偶核心标定”在本研究中只表示未用奇核观测量拟合该强度。

**保留的替代值和评价组成。** 下面的 B 均为 \(B_\uparrow\)，单位 \(e^2b^2\)。评价中心与误差原样保留，没有按组成重新加权，没有按拟合优劣选择干涉符号。它们共对应既存标定表的 23 条未选入基线的分支／组成／方法记录，不是额外 23 条独立标定数据。

| 核素 | 替代值／方法条件 | 原始键及归档定位 |
|---|---|---|
| \(^{130}\)Ba | 1.167(11)，相长；1.159(12)，相消；评价采用二者平均 1.163(11)。另列 1.21(38)、1.36(14)、0.75(18)。 | Coulomb L20–22：1989Bu07 两分支；1973ToXW（相消）、1967Si03、1958Fa01。 |
| \(^{130}\)Ba | 半衰期 43.2(5) ps（RDDS）及 40.7(4) ps（由 B 导出）保留作来源分量。 | Adopted L55–56；Coulomb L17、L27。此处不由摘要补写原实验的完整误差预算。 |
| \(^{132}\)Ba | 0.821(16) 与 0.897(16)，分别对应四个矩阵元乘积负／正；另有 0.73(18)。评价沿用 2001Ra27 推荐的 0.86(6)。 | Coulomb L15–17：1985Bu01 两符号分支；1958Fa01。两分支向下值为 0.1642、0.1794，误差幅各 0.0032。 |
| \(^{134}\)Ba | 组成 0.672(16)、0.700(15)、0.665(5)；所列评价 0.679(11) 原样采用。 | Coulomb L17–19：1972Ke16、1977Kl05、1989Bu07。 |
| \(^{136}\)Ba | 组成 0.399(3)、0.419(4)、0.418(11)；另有逆运动学方法值 0.46(4)。 | Coulomb L50–51：1984Be20、1986Ro15、1972Ke16、2002Ra21；逆运动学方法说明 L30–34。 |
| \(^{136}\)Ba | 相消分支 0.417(4)；取所列 \(Q=-0.19(17)\) 时为 0.388(10)／0.400(10)；1972 年分支为 0.418(11)／0.417(12)；另列 0.53(16)。 | Coulomb L52–54：1986BaZJ／1986Ro15、1985Bu01、1972Ke16、1963Al31。0.418(11) 同时列为评价组成和分支，保留一次。 |
| \(^{136}\)Ba | 另一个半衰期 \(2.2(3)\) ps，DSAM；与评价所列由 B 导出的 \(1.89(3)\) ps 分开。 | Coulomb L49，1973Fi15；方法见 L9–10。 |

**证据分层与可用范围。** 本页的能级、寿命、B(E2)、ICC 和方法分支首先是 **NNDC 评价报告**；评价作者的加权、推荐和“由 B 导出 T”是 **评价处理说明**；方向换算、\(^{128}\)Ba 的绝对 B 及一阶误差贡献是 **在 parent/task-declared 约定下的计算**；把重复量放入同一依赖块、保留未知协方差是 **本页的数据使用规则**。没有将评价复述升级为本页直接审核过的原始实验，也没有用这五个标定值证明 IBFM、形状不变量或某个 \(\gamma_{\rm eff}\) 结果。

## Extracted Pages

本页保存五核心标定记录、换算约定、误差依赖和替代分支的来源卡；原件入口如下。

原件入口为[五核心归档 manifest](/workspace/wiki/raw/papers/gpt/query/20261106-ba-core-E2-calibration/manifest.json)及[复用的 128／130Ba manifest](/workspace/wiki/raw/papers/gpt/query/20261105-ba129-core-constraints/manifest.json)。两者在本页 frontmatter 中各绑定 SHA-256；前者同时记录 8 个复用输入及其原获取时间。重新生成分析输出只应读取这些原件，不覆盖 raw。

**本页自审。** 2026-11-06 按上列原件定位核对来源、方向、归属和依赖；这是一项 Agent source audit，不是 human-reviewed 标注。尚缺原实验全文层的联合协方差、部分方法的系统误差拆分以及该五核素间的数值相关性。后续研究应明确所采用的误差／替代分支方案，不能从这些空缺自动构造完整实验似然。
