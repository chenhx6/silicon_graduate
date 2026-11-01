---
type: concept
title: "摆动候选的混合比、相位约定与双根证据边界"
aliases: [摆动多极混合比, delta(E2/M1), DCO双根区分]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [wobbling, mixing-ratio, evidence-boundary, triaxiality]
---

# 摆动候选的混合比、相位约定与双根证据边界

## Definition

本页修正此前以“相位符号法则”和最近理论根匹配自动确认摆动的规则。**理论偏好不是独立实验信息**；没有核验过的通用 TW 混合比公式，也不能由 `g_j-g_R` 的符号直接裁决实验 δ 的正负。

## 从矩阵元到真正可比较的量

[[book-petrache-chirality-and-wobbling]] Ch. 11，Eq. (11.10)，印刷 p. 225 / PDF 244 给出

\[
\delta=0.835 E_\gamma[\mathrm{MeV}]
 \frac{\langle I_f\Vert T(E2)\Vert I_i\rangle[e\,b]}
      {\langle I_f\Vert T(M1)\Vert I_i\rangle[\mu_N]}.
\]

计算需使用同一波函数和相位约定下的**跃迁约化矩阵元**。内禀四极矩 Q0 不是这一个矩阵元；spin、γ、g 因子和 TW/LW 标签也不够确定它。Eq. (11.11)–(11.12) 展示了核芯与单粒子贡献，因此无依据把 LW 的 E2 振幅固定乘 0.25。

由辐射振幅定义可得光子跃迁几率的 E2 份额

\[
f_{E2}=\frac{\delta^2}{1+\delta^2}.
\]

这是代数关系，不是绝对集体性测量。两个不同的矩阵元都乘同一常数，δ 不变而跃迁率改变；M1 相消也能使 δ 变大。原书 Ch. 11，PDF 246 / p. 227 的 127Xe 计算正提供了小 M1 分母的例子。

已知效率修正分支 bγ、平均寿命 τ、总内转换系数 α（单分支或分支归一须定义一致），才可把光子部分率与混合份额连接到 B(E2)/B(M1)；不同能量的分支强度比还须除以对应的 Eγ^(2L+1) 因子。不能把 fE2 直接记作 B(E2)out/B(E2)in。

## 双根如何保留与检验

对给定初末自旋、定向与有限立体角，一个角分布系数可写为

\[
a_k=\alpha_k\frac{F_k(LL)+2\delta F_k(LL')+\delta^2F_k(L'L')}{1+\delta^2}.
\]

因此由单个系数反演时**可能**有两个实根，也可能重根、无实根或退化为线性问题；DCO 的条件符合几何不能一律简化为这个单系数方程。此处是代数重构，实际拟合应参照 [[experimental-uncertainty-propagation-and-double-root-triage]] 和对应 source 的几何/约定。

- 保留全部可容许 δ 分支和共同 nuisance 参数，例如取向宽度、有限立体角与校准。
- 用实际测得的偏振、独立角关联、内转换或其它足够敏感观测构造共同似然。偏振符号本身不保证唯一 δ 解。
- 没有观测误差及模型/校准协方差，就不能把“离理论值差 1.5”解释成置信区间。
- 理论模型可以作为明示的先验或竞争假设，但不能同时选根又被称为该根的独立验证。

原书 Ch. 2 PDF 56–57 与 Ch. 5 PDF 120–121 对 135Pr 的测量与解释仍持不同立场；本页保留争议，未复核原始计数数据，不将任何一方写成终局事实。

## 从混合比到模式指认

原书 Ch. 5 PDF 123 / p. 104 明确讨论：130Ba/136Nd 两准粒子案例中 M1 分量可以超过 E2，但 E2 仍相对旋称伙伴增强。故固定 `|δ|≥2`、`fE2>80%` 或 `B(E2)out/B(E2)in∈[0.2,0.5]` 不应作为所有核、所有摆动模式的统一关口。

综合判断需要能量/自旋宇称、带间连接、强度、寿命、组态、角动量几何，以及 γ 软核耦合、旋称伙伴、构型混合、倾斜进动等替代解释。几何上的 TW/LW 与一个 δ 数值之间没有一对一映射。

## 可运行的有限用途

`system/scripts/analysis/wobbling_branching_ratio_phase_calculator.py` 和统一 CLI `wobphase` 现在：

1. 只有 spin、Q0、g 因子等输入时返回 `insufficient-model-input`，不虚构 δ；
2. 明示输入有符号 E2/M1 约化矩阵元时执行 Eq. (11.10) 的换算；
3. 输入两个候选根时保留两者，`selected_matching_root=null`、`is_wobbling_confirmed=false`；没有输入时不伪造某核的实验根。

```bash
# 以下 -0.15 与 3.10 仅为代数演示，不是 135Pr 的已核验实验数据

## Definition
python3 system/scripts/analysis/nuclear_analyzer.py wobphase --root1 -0.15 --root2 3.10 --json
# 人工矩阵元演示，非 TW/LW 物理指认

## Definition
python3 system/scripts/analysis/nuclear_analyzer.py wobphase --eg 1000 --e2-me -2 --m1-me 0.835 --json
```

## 修订与自审

2026-11-02：撤回旧版所谓 Frauendorf–Dönau 通用闭合 δ 式、质子 δ 必正、LW 固定衰减 0.25，以及“正大根确认 TW”。来源核查：[[book-petrache-chirality-and-wobbling]] 的 CW-3–CW-7；基础近似：[[book-bohr-mottelson-nuclear-structure-vol2]]；独立理论路线：[[frauendorf-2014-transverse-wobbling]]。P0 已隔离自动裁决；P1 是后续对实验原数据、相位与响应的逐案核查。未作 human-reviewed 或整书 deep-read 声明。


## Necessary Assumptions

详见正文模型条件及推导假设。


## Discriminating Observables

详见正文特征观测量及区分判据。


## Supporting Evidence

详见正文模型公式推导及支持证据。


## Counter-evidence and Competing Interpretations

详见正文反例与竞争解释讨论。


## Our Current Position

明确标记为本 Wiki 当前阶段性认知与工作边界，不作为无条件定论。


## Sources

- [[book-petrache-chirality-and-wobbling]]
- [[book-bohr-mottelson-nuclear-structure-vol2]]


## Evolution Log

- 2026-11-02: 建立与修订本页概念规范。
