---
type: research-note
title: "Doppler 前向与反演约定混用的谱峰偏差检验"
aliases: [Doppler convention roundtrip audit]
created: 2026-10-13
updated: 2026-10-14
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [aladili-2009-agata-doppler-simulation, mavela-2019-32s-quadrupole-moment-doppler-correction-thesis, ciemala-2021-deep-inelastic-lifetime-method]
created_from: Day13 autonomous-method-study
promotion_target: doppler-correction
tags: [doppler-correction, convention, roundtrip, provisional]
---

# 前向与反演约定的可证伪诊断

## Research Trigger

同一条模拟line的generated E0与corrected centroid若存在keV尺度差异，可能影响后续门选择和resolution验证；这是一项可追踪的方法问题，值得保存有界counterfactual及推翻条件。

## Grounded Evidence

[[aladili-2009-agata-doppler-simulation]] AA09-8：exact式(3.7)与linear式(3.8)、人为γ生成和figurecenter≈1436，与标称1434keV存在约2keV差。[[mavela-2019-32s-quadrupole-moment-doppler-correction-thesis]] DD-20261013-32S-27给exact forward/inverse，但不证明Al-Adili实际pipeline的反演是哪种。问题是：前向生成的近似约定和校正器是否一致？

## Provisional Reasoning

新的文档case：[[ciemala-2021-deep-inelastic-lifetime-method]] CM21-4，p.7印Eq.(1) `Eγ=Eγ0/[γ(1−βcosθ)]`，紧邻文字定义Eγ0为measuredlabenergy。图页视觉核验一致；若按该标签将lab还原rest，应乘`γ(1−βcosθ)`。本任务仅定位印刷公式/label冲突，不知productioncode实际使用哪式，也未证明它造成任何source寿命偏差。此case和AA09的linear/exact混用候选分开，不把两个不同source问题合成一个已证实pipelineerror。

2026-10-14正式version核验修订：CM21-14/15，publisherp.6明确`Eγ0=Eγ×D`、measuredEγ/correctedEγ0，且明示aftertargetreference；v1的文字标签冲突在正式版消除。当前arXiv无版本URL仍为v1相同hash，引用版本必须明示。CM21“正式文档也错误”的候选已被直接反证；关于v1label的记录保留，但它不支持执行错误或150fs偏差归因。AA09的不同混用候选仍未裁决。

令q=βcosθ，exactforward为`E_lab=E0 sqrt(1−β²)/(1−q)`，linearforward为`E_lab=E0(1+q)`。若linearforward后接exactinverse，

$$\frac{E_{corr}}{E_0}=\frac{1-q^2}{\sqrt{1-\beta^2}},\qquad
\Delta E\simeq E_0\beta^2(\tfrac12-\cos^2\theta).$$

对E0=1434keV、β=.0548、θ90°，exactmixed bias为+2.158041keV，得到1436.158041keV；与sourcefigure≈1436只量级相容。这里没有拟合原line、没有exec-code证明，不能写成已定位源错误。

## Competing Explanations

- 若原sortpax/MGT分别都使用同一linear式及其一致inverse，则该混用机制被排除；E0标签、precision、data重bin、平均velocity方向、generated energies及calibration仍可解释shift。
- 同样可检验exactforward+linearinverse，在90°偏差为−2.154799keV，符号不同；只看宽度不区分共同centroid convention。
- [[tunl-2017-12c-level-widths]]提供不同gap/width的评价语境；photonrecoil是另一个frame候选，但A52/gap1.434MeV的free-mass-numbertoy给gap→photon差约.0212keV、parent→daughterframe差约.0424keV，均远小于本case约2keV。因此在这些明确输入下，它不能独自解释该shift；实际generatedenergy/particleidentity仍需code确认。复算见[day13_photon_recoil_width.py](../../system/scripts/day13_photon_recoil_width.py)，不是原MGT执行证据。
- code replay应先用stationary/monoenergetic/knownvector零nuisance事件，做linear-linear、exact-exact、mixed两方向roundtrip；再加入reaction/position spread。检查实际formula、units/frame、E0输入与每步centroid，不靠最后一张峰图猜原因。

## Assumptions

单line、known constantβ和lab θ为自设，不含sourceactualevaporation/covariance。 [day13_doppler_conventions_decay.py](../../system/scripts/day13_doppler_conventions_decay.py)的exact-exact和linear-linear roundtrip分别max0和1.14×10⁻13keV；mixedbias表为解析/数值一致推导。source标称β/γ能量输入只用于illustrativecounterfactual，未成为MGT执行证据。

## Knowledge Impact and Lifecycle

此前的判断是“β<0.1可使用一阶式，但须声明精度”；修订为“对keV分辨率，还要核对forward/inverse是否同约定，β²E0可与intrinsicwidth同量级”。 reusable原则已写 [[doppler-correction]]，sourcecase因缺执行版仍`provisional`，本note不作为source事实或论文错误指控。

## Transfer Conditions

一般roundtrip检查可迁移到其它simulation/reconstruction，前提是E0、lab angle和velocity输入已定义；不能把该source的β或2.158keV数值迁移为其它实验的offset。

## Failure Conditions

若executed code采用相同forward/inverse，本case的混用解释即失败；如果角度/生成能量不是所设值，counterfactual不再预测原plotcentroid。无源码时保留provisional，不晋升source错误结论。

## Falsification or Reverse Tests

查sortpax/MGT实式、精确generated E0、β/角度及code版本；用monoenergetic/knownvector零nuisance事件逐步记录centroid，比较两种consistent和两种mixedroundtrip，再恢复spread。仅有图上的width不能完成这项判别。

## Open Questions

执行版inverse和generated-energy convention是否可取得？是否有无需估计reactionspread的零nuisance测试记录？source既有图像不足以选因。

## Human Review

尚无Human review；目前是Codex source/formula self-audit后的provisional推理。具体claim未来用于论文措辞时按证据门定向核验。

## Promotion or Rejection History

2026-10-13：创建有界candidate，Codex self-audit检查sourceformula/figure与counterfactual；没有Human review。若code证明约定相同则reject该case假设并保留此记录；若定位为其它原因则supersedecase，但保留一般roundtrip验证原则。
