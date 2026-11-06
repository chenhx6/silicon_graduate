---
type: source
title: "E2 Weisskopf 单位、方向与寿命比：NNDC 帮助页的局部记号核查"
aliases: [ordinary downward E2 Weisskopf unit, NNDC E2 direction and lifetime ratio audit]
created: 2026-11-06
updated: 2026-11-06
status: ai-draft
review_status: unreviewed
source_type: online-help-documentation
reading_depth: read
title_original: "B(E2) Values - Help; Gamma Emission and Internal Conversion"
authors: [National Nuclear Data Center]
year: 2026
year_basis: "Archive/audit year; the help pages do not supply a publication date."
canonical_source: "NNDC-help:be2/help.html+nudat3/help/gammaemission.jsp@20261106:WU-direction-lifetime-audit"
citation_key: NNDC2026E2WeisskopfDirectionLifetimeHelp
citation_key_origin: "Unique local identifier for the exact two-page help snapshot."
raw_file: "raw/papers/gpt/query/20261106-ba137-isomer-validation/manifest.json"
raw_sha256: "43c4d2616a7d90dd7b380fecb24ff793c718b59ca33237dca9d9eb451fe595ca"
raw_storage_status: archived-local
archive_required: true
nuclei: [137ba]
observables: [reduced-E2-transition-probability, half-life, mean-lifetime, internal-conversion-coefficient]
methods: [unit-conversion, dimensional-analysis, source-lineage-audit]
tags: [a130, weisskopf-units, E2, transition-direction, lifetime-ratio, documentation-ambiguity]
---

# E2 单位必须同时注明参考定义和跃迁方向

## Bibliographic Record

本页审计父任务于 **2026-11-06** 归档的两个 NNDC 帮助页。`year: 2026` 是快照/核查年度，不是未注明的页面发表年。唯一集合标识由两个具体端点及快照日期构成，不使用泛化 NNDC 首页作为 canonical source。

| 标识 | 原始页面与本地原件 | SHA-256 |
|---|---|---|
| H-BE2 | `https://www.nndc.bnl.gov/be2/help.html`；`raw/papers/gpt/query/20261106-ba137-isomer-validation/nndc-be2-help.html` | `df0058d7fffef7cd92c25aafabb1b3591666129ff0febf7c11b3190d9cd2323c` |
| H-GAMMA | `https://www.nndc.bnl.gov/nudat3/help/gammaemission.jsp`；`raw/papers/gpt/query/20261106-ba137-isomer-validation/nndc-gamma-help.html` | `e2b863a873aa062c1c06966a20ed4fa33833ee2703e4f4e1e8a3ee13d78316cb` |

集合 [manifest](/workspace/wiki/raw/papers/gpt/query/20261106-ba137-isomer-validation/manifest.json) 的 SHA-256 为 `43c4d2616a7d90dd7b380fecb24ff793c718b59ca33237dca9d9eb451fe595ca`；`retrieved_at=2026-11-06T08:32:37.918371+00:00`，各页面的实际 HTTP 时间另列在条目中。下面的 HTML 行号从原始文件第 1 行计，不是网页抓取工具重新排版后的行号。

独立理论依据为 A. Bohr、B. R. Mottelson，*Nuclear Structure*, Vol. I，初版 1969；本地为 World Scientific 1998 版。原件 `raw/books/nuclear structure Ⅰ_Bohr, Mottelson.pdf`，SHA-256 `a31a158e0aff2ec6734d46f5aea5eb42dbebb82280835774f49350dd6f8c79df`。本次相关位置：印刷 p.381 / PDF p.400 的半径约定，以及印刷 **p.382 / PDF p.401，Eqs. (3C-16)–(3C-18)** 的辐射率和约化跃迁概率定义。

137Ba 实验锚点回链 [[vogt-2017-135xe-137ba-isomers-high-spin]]：Vogt et al., *Phys. Rev. C* **95**, 024316 (2017)，DOI `10.1103/PhysRevC.95.024316`。使用已归档 Birmingham accepted manuscript，PDF p.14 / 稿件 p.13 的 Table III，以及 PDF p.9 的 Fig.7/Section III B。

## Scope and Reading Depth

**Covered scope:** 两个短帮助页的物理说明、B(E2) 方向与 W.u. 定义、寿命符号；Bohr–Mottelson 的指定辐射率段落；Vogt2017 的目标核素、能级、自旋方向和已校正强度。实际视觉重核已有的 Vogt Table III 页图；教材只读取指定 PDF 文本，没有生成新的教材页图。

**Not covered:** 未审查整个 NNDC 网站、全部 ENSDF 数据或帮助页每个独立公式的适用条件；未通读教材；未重分析 Vogt 时间谱或重算 ICC；未执行任何 IBFM/转子模型计算、态选择或重拟合。对其它强度/部分半衰期约定不作越界推广。

## Summary

对向下衰变采用普通 E2 Weisskopf 参考值
\[
W_d(E2)=\frac{1}{4\pi}\left(\frac35\right)^2
[1.2A^{1/3}]^4\,e^2\mathrm{fm}^4.
\]
137Ba 的 \(0.46(3)\) W.u. 对应
\[
B_\downarrow=(1.930\pm0.126)\times10^{-3}\ e^2\mathrm b^2,
\]
其中只转换原文 quoted margin，不增加模型误差或新的置信解释。这里是 \(19/2^-\to15/2^-\)，不是 \(15/2^-\to11/2^-\)。

归档帮助页存在两处局部表达不一致：H-BE2 的特殊 \(0^+\to2^+\) 参考值写成下箭头；H-GAMMA 将时间比按 \(T_\gamma/T_W\) 印为 W.u. 强度。后者在匹配的辐射部分半衰期定义下是强度的倒数/阻碍比。此结论不表示 NNDC 整体或 ENSDF 实验数据无效。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | source_independence | confidence | locator | needs_review |
|---|---|---|---|---|---|---|---|
| WU-1 | H-BE2 的一般式及其向下跃迁说明给出普通 E2 参考系数 \(0.0594042641992\,A^{4/3}\ e^2\mathrm{fm}^4\)。 | our-inference | direct | single | high | H-BE2 原始 HTML 60–66，代入 \(\lambda=2\) | false |
| WU-2 | H-BE2 接着说明 \(0^+\to2^+\)，使用约 0.297 的五倍系数，却印下箭头；系数与 upward 上下文一致，箭头不一致。 | our-inference | direct | single | high | H-BE2 44–46、68–70 | false |
| WU-3 | 固定 \(E_\gamma\) 和多极性时，辐射率与 \(B\) 成正比；匹配的部分光子半衰期满足 \(B/B_W=T_{\gamma,W}/T_\gamma\)，不是反比。 | our-inference | direct | multiple-dependent | high | Bohr–Mottelson I p.382 Eqs.(3C-16)–(3C-18)；H-GAMMA 178–192；下述推导 | false |
| WU-4 | 在 H-GAMMA 将 \(T_\gamma,T_W\) 都定义为时间的上下文下，190 行的 \(T_\gamma/T_W\) 对应阻碍比；取单支路、\(\alpha=0\) 已可确认反向问题。 | our-inference | direct | single | high | H-GAMMA 180–191；check_units.py 的四个纯代数控制 | false |
| WU-5 | Vogt 的 137Ba \(T_{1/2}=589(20)\) ns 和 \(B(E2)=0.46(3)\) W.u. 属于 2349.9→2229.8 keV 的 \((19/2^-)\to(15/2^-)\)；强度已校正内转换。 | experimental-fact | direct | multiple-dependent | high | Vogt2017 Table III，PDF p.14；Fig.7/Section III B，PDF p.9 | false |
| WU-6 | 该态对的反向物理强度因子为 \(20/16\)，不是 5；普通单位、特殊向上参考单位和物理详细平衡因子应分别记录。 | our-inference | direct | multiple-dependent | high | H-BE2 44–46；Bohr–Mottelson Eq.(3C-17)；下述归一化 | false |
| WU-7 | 以 \(A=137\) 和普通参考值，仅从已发表 0.46(3) W.u. 得到 \((0.00192990623330\pm0.00012586345000)\ e^2\mathrm b^2\)。寿命不参与这次换算。 | our-inference | direct | multiple-dependent | high | check_units.py；unit-audit.json；原始 B 值见 WU-5 | false |

**单位与方向。** 因 \(1\,\mathrm b=100\,\mathrm{fm}^2\)，故 \(1\,\mathrm b^2=10^4\,\mathrm{fm}^4\)。普通定义在 \(A=137\) 给出：

| 量 | 数值 |
|---|---:|
| \(1\,\mathrm{W.u.}_{d}(E2)\) | \(41.9544833325\ e^2\mathrm{fm}^4\) |
| 同一参考值 | \(0.00419544833325\ e^2\mathrm b^2\) |
| \(0.46\,\mathrm{W.u.}_{d}\) | \(0.00192990623330\ e^2\mathrm b^2\) |
| 原文 0.03-W.u. margin 的换算 | \(0.00012586345000\ e^2\mathrm b^2\) |

这些长小数仅供复算，不代表实验精度提升。采用精确表达式中的 \(\pi\) 和约定 \(r_0=1.2\) fm；0.0594、0.297 是相应舍入系数，不是需要重新拟合的物理输入。

对 \(0^+\leftrightarrow2^+\)，详细平衡给出 \(B_\uparrow=5B_\downarrow\)。H-BE2 的特殊向上参考也相应取
\[
W_{0\to2}^{\rm special}=5W_d\simeq0.297A^{4/3}e^2\mathrm{fm}^4 .
\]
如果物理强度和参考单位同时乘五，无量纲比值不变；若两个方向都使用同一个普通 \(W_d\)，则它们的 W.u. 数值相差物理自旋因子。不能把该特定 \(0\to2\) 参考中的五倍系数移给任意核态之间的向下衰变。

对当前 137Ba：
\[
B_\downarrow(19/2\to15/2)=\frac{|R_{15/2,19/2}|^2}{20},
\qquad
B_\uparrow(15/2\to19/2)=\frac{20}{16}B_\downarrow .
\]
已按 \(2J_i+1=20\) 归一的模型 \(B_\downarrow\) 直接与换算后的实验值比较，不再除一次 20。这里也不能误用另一态对 \(11/2\leftrightarrow15/2\) 的 \(16/12\) 因子。

**寿命比的限定推导。** 教材的 \(T(E2)\) 符号表示每秒的跃迁率，并非半衰期。本页统一写成 \(\lambda_\gamma\)，在相同能量和多极性下：
\[
\lambda_\gamma=C_\lambda E_\gamma^{2\lambda+1}B,\quad
T_\gamma=\frac{\ln2}{\lambda_\gamma},
\quad
\frac{B}{B_W}=\frac{\lambda_\gamma}{\lambda_{\gamma,W}}
=\frac{T_{\gamma,W}}{T_\gamma}.
\]
例如一个纯代数控制取 \(B=10B_W\)，应有 \(T_\gamma=T_{\gamma,W}/10\)；帮助页所印 \(T_\gamma/T_W\) 则得到 0.1，恰为倒数。这个控制取 \(\alpha=0\)、单支路，没有使用实际 137Ba 寿命。

上述时间必须是相同定义的**辐射部分时间**。存在内转换/分支时，不能直接将总能级半衰期代入；半衰期与均寿命也须一致，\(\tau=T_{1/2}/\ln2\)。H-BE2 的 \(\tau\) 行（74–77）明确是均寿命。本次没有采用帮助页的部分寿命公式重算任何实验强度。

## Competing Interpretations and Limitations

- 两处问题限定于归档帮助页的箭头/比值表达。一般 Weisskopf 公式、详细平衡和网站数据不能因此被一并否定；本文不对未审计的其它公式作结论。
- Vogt 的 \(B(E2)\) 已作 ICC 校正，文中没有列出本次可用的数值 \(\alpha\)。本次直接换算作者给出的 0.46(3) W.u.，不从 \(0.589\,\mu\mathrm s\) 重建强度、不假设 \(\alpha=0\)、不重复加转换因子。
- 寿命及由其导出的强度属于同一衰变证据组，不能作为独立实验数据重复加权；原文 quoted margin 不自动变成给定置信度的区间。
- 图中 tentative 自旋标注保留。父任务的模型 primary ordinal 0/0 和预先确定的 energy-only alternative 不由本侧车选择或重排。模型数值、态对应优劣和拟合结果均不在本次工作内。
- 0.46(3) W.u. 是 \(19/2^-\to15/2^-\) 的另列 EM 约束，不是 \(R_{\rm stat}^{(1)}\) 所需的 \(15/2^-\to11/2^-\) 分母，也不直接验证初态 11/2 的三阶电荷矩或内禀形状。

## Extracted Pages

- 本次仅新建本 source 页，不更新 index、handoff 或任何既有 source。
- 相关实验 source：[[vogt-2017-135xe-137ba-isomers-high-spin]]；相关既有集合：[[nndc-ba135-ba137-static-e2-constraints]]。
- [有界报告](/workspace/wiki/outputs/l4/20261106-a130-next-evidence/isomer-source-review/report.md)、[unit-audit.json](/workspace/wiki/outputs/l4/20261106-a130-next-evidence/isomer-source-review/unit-audit.json)、[单条观测 CSV](/workspace/wiki/outputs/l4/20261106-a130-next-evidence/isomer-source-review/observed-strength.csv)、[复核脚本](/workspace/wiki/outputs/l4/20261106-a130-next-evidence/isomer-source-review/check_units.py)。转换函数只接受 A、已发表 W.u. 强度及其 margin，不接受寿命或 ICC 参数。
