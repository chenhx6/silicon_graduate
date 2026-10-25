---
type: observable
title: 带间集体 E2 强度
aliases: [interband E2 strength, B(E2)out, B(E2)out/B(E2)in]
created: 2026-07-01
updated: 2026-07-04
status: active
review_status: unreviewed
observable_kind: reduced-electric-quadrupole-strength
symbol: B(E2)out/B(E2)in
units: dimensionless-or-source-dependent
tags: [wobbling, electric-quadrupole]
---

# 带间集体 E2 强度（Interband E2 Strength）

## Definition

候选伙伴带之间的 E2 跃迁强度，常与基带内 E2 归一化为 `B(E2)_out/B(E2)_in`。

## Formula and Conventions

必须记录所比较的具体跃迁、自旋和多极混合处理。

## How It Is Obtained

由 mixing ratio、分支比、能量和寿命信息推导；弱跃迁时系统误差关键。

## Diagnostic Use

相邻 wobbling quanta 带之间 collectively enhanced E2 是 [[frauendorf-2024-wobbling-review]] 强调的核心实验判据。

## Model Dependence

QTR/PTR 与 TPSM 对其绝对大小可能有系统差异。

## Failure Modes and Ambiguities

只有 δ 而缺寿命时，通常得到相对 E2 成分，不一定得到绝对集体强度。

## Examples

`131Xe` 新序列的连接跃迁 E2 成分很小，因此不支持 wobbling。

[[matta-2015-transverse-wobbling-135pr]] 的 Table I 给出 `135Pr` side-to-yrast transitions 的 E2 fractions 与相对 `B(E2_out)/B(E2_in)`；作者将其作为 wobbling 支持证据。没有独立寿命时，这些是 mixed-transition 分解后的相对量，不等同于绝对 `B(E2)`。

[[sensharma-2019-two-phonon-wobbling-135pr]] 的 Fig.3 比较 TW2→TW1、TW1→yrast、TW2→yrast 与 signature-partner→yrast 的相对 `B(E2)_out/B(E2)_in`。论文明确说明未测得绝对跃迁概率；这些比值由强度和 angular-distribution mixing ratios 提取。

[[lv-2022-evidence-against-wobbling-135pr]] 报告 `B(E2;747)/B(E2;526)=0.7(+0.7/-0.5)`；作者认为两条强度相近，不符合 wobbling-to-yrast 应显著强于到 signature-partner 的预期。

[[sensharma-2020-longitudinal-wobbling-187au]] 的 LW→yrast `B(E2)_out/B(E2)_in` 最大约 0.7，并显著高于 SP→yrast；PRM 较好再现 E2 ratios，但 M1 ratios 存在系统偏差。

[[guo-2022-low-spin-wobbling-187au]] 由其小 mixing ratios 与外部文献的 `B(E2)_in=100-200 W.u.` 估计 `B(E2)_out` 仅数 W.u.，作者据此反对 Band 2 的 collective excitation。该量是派生估计，不是本文 lifetime/absolute-`B(E2)` measurement。

[[lv-2021-tilted-precession-135nd]] 对 TiP1→D1 报告 `B(E2)out/B(E2)in` ratios，并与 QTR 比较；618.3/566.0 keV links 的实验值为 0.11(4)/0.12(7)。注意 566.0 keV ratio row 与 Table II 中另一个 566.8 keV、`δ=-0.48(14)` 的 connecting transition 不是同一行。这些值由 branching/mixing-ratio information 得到，不等于完整 independent lifetime/absolute-`B(E2)` measurement。

[[nomura-2022-questioning-wobbling-ibfm]] 计算四个 γ-soft odd-mass cases 的 `B(E2)out/B(E2)in`。对若干 reported wobbling bands，IBFM 值低于早期实验派生值；这属于模型-实验比较，并受 band matching、transition operators 和争议中的 mixing ratios 限制，不是新的 lifetime/absolute-`B(E2)` measurement。

## Sources

- [[chakraborty-2023-131xe-wobbling-origin]]
- [[frauendorf-2024-wobbling-review]]
- [[matta-2015-transverse-wobbling-135pr]]
- [[sensharma-2019-two-phonon-wobbling-135pr]]
- [[lv-2022-evidence-against-wobbling-135pr]]
- [[sensharma-2020-longitudinal-wobbling-187au]]
- [[guo-2022-low-spin-wobbling-187au]]
- [[lv-2021-tilted-precession-135nd]]
- [[nomura-2022-questioning-wobbling-ibfm]]

## Evolution Log

- 2026-07-01：建立 wobbling 的关键电磁判据。
- 2026-07-03：加入 Matta 2015 Table I 的相对 E2 支持链及绝对强度边界。
- 2026-07-03：加入 Sensharma 2019 的 TW2 相对 E2 ratios 及无绝对寿命的边界。
- 2026-07-03：加入 Lv 2022 的 747/526 E2-strength counter-test。
- 2026-07-03：加入 Sensharma 2020 的 `187Au` LW/SP relative-E2 对照。
- 2026-07-04：加入 Guo 2022 的数 W.u. `B(E2)_out` 估计及其外部输入边界。
- 2026-07-04：加入 Lv 2021 `135Nd` TiP1→D1 relative-E2 ratios 与非绝对寿命边界。
- 2026-07-05：加入 Nomura 2022 的 IBFM relative-E2 预测及其非实验测量边界。


## Day22相对比值、绝对强度与声子归一（checkpoint092）

同母态的M1+E2带外线与纯E2带内线，其相对四极强度为rE2=λ(Ein/Eout)^5 δ²/(1+δ²)，λ是两条光子支路之商。若强度是含转换电子的总支路，须先用各自α换为光子率；不能把校正对象混同。共同母态寿命在相对比中抵消，但缺寿命时不提供绝对B或W.u.。

在[[jensen-2002-second-phonon-wobbling-163lu]] JE02-D22-R092-3中，以476/627 keV、λ=.14、δ=−3.60/−.19的打印中心重建rE2≈.5154/.01934。与打印.51/.019的小差在输入末位舍入范围相容；这不是重放原实验误差。脚本另按混合比率关系得到rM1≈.00628/.08465 μN²/(e²b²)，与打印.006/.083相容。所有量仍相对同一个带内B，不能乘无出处的Q或寿命基准制造绝对强度。

### 两倍玻色子规则与双重归一

定义r21=B(E2;2→1)/B(E2;2→2)in，r10=B(E2;1→0)/B(E2;1→1)in，则

    r21/r10 = [B(E2;2→1)/B(E2;1→0)] × [B(E2;1→1)in/B(E2;2→2)in]。

因此r21/r10≈2不自动等于绝对矩阵元的理想两倍规则；需要指定带内分母尺度、spin匹配与非谐修正。JE02的.51/.21≈2.43是条件性支持，非独立寿命结果（JE02-D22-R092-4）。替代根之商.51/.019≈26.84是同一数据在两种解释下的中央值敏感性，不是随spin发生的实测物理暴跌。

旧本节全区寿命缺失、10–100 W.u.普适阈值及由小rE2唯一归属单粒子的认证撤回。相对强度本身仍可检验模型；其信息不会因缺寿命而消失。

## Day22 checkpoint099：163Lu的SD–ND E2对照

[[domscheit-1999-triaxial-superdeformation-163lu]] DO99-D22-R099-1/2给出两个同为21/2+、相隔111keV的ND/SD1态。作者以带外426/697keV E2退激的两态混合解释约40%光子脱带，并据假设的算符矩阵元提取p和Q比；不是将SD1/SD2识别为声子阶梯。任务打印中心重建p≈.0387、V≈21.4keV、QND/QSD≈.4868，五项指定代数控制通过，没有新Cov/CI或绝对B测量。

这说明同核的强光子脱带、近能量态和E2连接也可有SD–ND混合解释；强度份额还需Eγ^5修正，不能等同约化B。原Q_SD=10.7(.7)b为Schmitz1993旧寿命引用，只约束该带/模型，不能搬给新SD2/3的绝对强度或当三次独立测量。原Schmitz全文未得，F14 Ref25字面疑点仍开放。needs_review: true。

## Day22 checkpoint100：同母态out/out能消去什么

若两个out/in来自同一母态且用同一条纯E2带内分母，`r20/r21=B(E2,out20)/B(E2,out21)`，带内强度/τ消去。一般光子式为`(I20/I21)(E21/E20)^5 fE2,20/fE2,21`。它仍需逐线相位/多极性、效率、背景和共同Cov；两个derived ratios并非独立观测。

[[jensen-2002-second-phonon-wobbling-163lu]] JE02-D22-R100-1/2给具体45/2+控制：1119.2、476和627三线共母态。按打印rE2中央商，直接到TSD1的E2与到TSD2的E2相比，大根给约.0353，小根给约.947；重算打印光子输入给.03533/.94141。该重表达澄清分支机制，不新增寿命或选根证据。与比较不同母态/带内分母的.51/.21不同，不能把后者无条件称绝对两倍声子规律。needs_review: true。
