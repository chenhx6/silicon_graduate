---
type: concept
title: 潮汐波转动
aliases: [tidal wave, tidal-wave rotation]
created: 2026-09-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
concept_type: collective-rotation
confidence: low
tags: [high-spin, collective-motion, vibration, rotating-mean-field]
---

# 潮汐波转动（Tidal Wave）

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Definition

Tidal-wave rotation is a rotating-frame description of weakly deformed yrast vibrational states in which angular momentum grows mainly through increasing collective deformation amplitude while rotational frequency remains near a vibrational frequency.

For a quadrupole pattern, the pattern/cranking angular speed is half the
time-oscillation frequency of the shape at a fixed direction, not half another
independently defined rotation speed. Gu2007's harmonic yrast example gives
E(I)-E(0)=hbar*Omega_vib*I/2 and omega_crank=Omega_vib/2
([[gu-2007-tsd-tidal-waves-thesis]], PDF69,71-74). Constant frequency and
near-linear B(E2) growth describe a limit, not a universal sufficient criterion.

## Necessary Assumptions

The yrast sequence remains coherent and sufficiently weakly damped; deformation coordinates can be represented by a slowly varying rotating-frame mean field or collective Hamiltonian.

## Discriminating Observables

Moment of inertia versus spin, near-constant rotational frequency, `B(E2)` growth and the ratio `B(E2)/J` relative to harmonic/free-boson and interacting-boson limits.

## Supporting Evidence

[[frauendorf-2018-beyond-unified-model]] discusses Eqs.155–156 and `102Pd/110Cd` examples; the figures are review-level routes to the cited original calculations and data.

## Counter-evidence and Competing Interpretations

Band crossings, aligned quasiparticles, anharmonic vibrations and ordinary collective rotation can produce similar moment-of-inertia trends. A tidal-wave label is not a direct deformation measurement.

## Our Current Position

Use tidal-wave language as a rotating-frame collective interpretation, with `B(E2)`, frequency and configuration evidence kept separate.

## Sources

- [[frauendorf-2015-low-energy-quadrupole-mode]]
- [[frauendorf-2018-beyond-unified-model]]
- [[gu-2007-tsd-tidal-waves-thesis]]


## 102Pd寿命原件的增量约束（2026-11-20）

[[ayangeakaa-2013-tidal-waves-chirality-thesis]] PDF113-130提供寿命实验、
误差和模型比较，而不是仅凭等间距能谱给模式命名：

- Table3.2（PDF121）的带内向下B(E2)从6+的0.174(48)增至14+的
  0.272(+0.015/-0.022) e^2 b^2。16+列0.277(+0.033/-0.042)，
  但该态寿命不能与侧馈分离，原文仅作寿命下限，不能当作同等确定的普通数据点。
- 原文把可靠的七d玻色子解释放在I=14（n=I/2=7）；16+是可能的八玻色子
  延伸而非“七声子16+”。这是作者对实测趋势的解释，不是直接数出微观声子。
- PDF120所述MINOS区间与停止本领系统误差分开；后者可达约20%，未包含于
  所给统计误差。没有逐态敏感性结果时，不能保证该系统效应只是共同尺度、完全不改趋势。
- 此处惯量采用原文Eq3.17的J_tw=2I/E_gamma（hbar=1），不是自动等同
  Chapter1中(2I-1)/E_gamma的量子运动学惯量。近恒定B(E2)/J_tw支持潮汐波图像，
  仍须保留非简谐性、组态混合及高自旋顺排等竞争因素。
- WS-SCTAC采用通用势参数而未对本组实验调整参数；名称含TAC，但该例自洽解沿
  中间主轴转动（PDF126）。几何集体模型GCM的低能谱参数拟合及B(E2)尺度调整，
  与此前生成坐标法同缩写不同方法，不能按名字混合或据一个算例给模型永久排名。
- PDF121 Eq3.16与表中Qt有sqrt(2)不一致：按原式逐项算得约1.67-1.99 eb，
  表列2.36-2.81 eb。表值与标准K=0 Clebsch-Gordan系数反解相容；
  PDF46 Eq1.46/1.47也有同类因子差异。保留原式、表和适用条件，不能静默纠正或推断作者代码错误。
- PDF123 Eq3.19按印刷式在I=2给B_2/B_2=2；从该文恒定B/J_tw假设实际推出
  B_I/B_2=I*E_gamma(2)/(2*E_gamma(I))。Eq3.20的Grodzins关系为向上0+到2+，
  转成向下2+到0+还需除以5。该代数检查不等于新寿命测量或官方勘误。

这补充了[[gu-2007-tsd-tidal-waves-thesis]]中早期有限B(E2)证据的范围；
论文/学位论文/综述若复用同一实验，不重复计为独立支持。旧历史段中的排他性措辞仍不恢复。

## Day 21 Checkpoint 014 证据门量化审计

2026-11-20边界订正：以下历史102Pd数值未在本轮重新核对，不作新的数据认证；
“排除了”“完全符合”“确证”的排他性措辞不能由几个比值自动推出。
Gu2007 PDF92–94明确区分能谱趋势、有限的B(E2)实验及准粒子顺排贡献。
当前使用以本页定义和竞争解释段、以及直接来源为准，历史段保留为审计记录。

依据独立审计程序 `system/scripts/day21_checkpoint014_tidal_wave_audit.py` 与审计产物 `outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/tidal-wave-audit-014.json`（对标 [[frauendorf-2015-low-energy-quadrupole-mode]] 之 `FR15-D21-1`），确立四极潮汐波在推断阶梯上的实证判据：
1. **转动频率迟滞与非刚性转动本质：**
   在弱形变 $\gamma$-软核（如 $^{102}	ext{Pd}$）中，转动频率 $\hbar\omega = \Delta E / 2$ 随自旋增长极其迟缓（在 $^{102}	ext{Pd}$ 中自旋由 $2^+$ 升至 $10^+$，频率仅由 $278.2	ext{ keV}$ 升至 $490.0	ext{ keV}$，比值为 $1.76$，远低于刚性转子的 $5.0$），排除了常规刚性集体转动；
2. **$B(E2)$ 离心拉伸与声子退相干：**
   实测带内 $B(E2)$ 随自旋发生大幅激增（由 $32	ext{ W.u.}$ 扩张至 $105	ext{ W.u.}$，增长 $3.28$ 倍），显著打破了刚性转子 Clebsch-Gordan 几何因子的饱和极限（预测饱和上限仅 $1.69$ 倍），同时低于简谐 5 声子自由玻色子预测（$5.0$ 倍），与四极振幅随自旋拉伸的潮汐波物理图像（$B(E2) \propto \beta_2^2(I) \propto I$）完全符合；
3. **证据门准则：**
   严禁仅凭表观等间距能级或 $R_{4/2} \approx 2.0 - 2.4$ 直接断言原子核处于简谐多声子振动态或刚性形变转动；确证四极潮汐波集体机制必须依赖绝对能级寿命测量提取 $B(E2) \propto I$ 随自旋线性或超线性增长轨迹，并联合转动频率迟滞排除回弯与静态转子假象。
