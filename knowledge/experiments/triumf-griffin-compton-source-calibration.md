---
type: experiment
title: "GRIFFIN源符合Compton偏振标定：P/A/Q与输入账本"
aliases: [GRIFFIN Compton source calibration, GRIFFIN source Q calibration]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
experiment_id: triumf-griffin-compton-source-calibration
facility: TRIUMF-ISAC
beam: radioactive-source-calibration
target: source-at-array-centre
beam_energy: not-applicable
reaction: radioactive-source-decay-calibration-no-incident-beam
evaporation_channel: not-applicable
residual_nuclei: [60Ni, 207Pb, 56Fe]
detector_array: GRIFFIN-HPGe-clover
data_status: published-summary-verified-events-response-covariance-not-acquired
sources: [garnsworthy-2019-griffin-facility, grsisort-2026-compton-polarimetry-code]
tags: [polarimetry, calibration, GRIFFIN, response-readiness]
---

# GRIFFIN源偏振标定的可复用输入账本

## Identity

本页按[[garnsworthy-2019-griffin-facility]] GF19-6–12组织论文原件实际source-calibration，不是新数据集或当前程序运行的alias。母核source标签60Co/207Bi与γ发射核60Ni/207Pb分开。创建理由是保存一套未来能检查matching reference/target的实验输入合同，避免只按仪器名称搬Q。

## Beam, Target and Reaction

放射源位于array中心的beam-implantation位置，非fusion-evaporation beam experiment。这里的coincidence plane由两γ方向定义，不等于in-beam的束轴–γ反应面。source的其它RIB示例和future polarized beam不属于这组calibration。

## Detector Configuration

主锚点为16clover的1332-keV calibration；cloverpair约90°，论文相应crystal coincidence Θ为68–113°。Θ、Compton极角ϑ、方位平面角ξ三者不可混用（GF19-6/7）。实际distance、threshold、逐台weights/完整selection与calibrationCov需原ledger，不以当前helper默认145mm或其它efficiency图配置补写。

## Trigger and Coincidence Conditions

同clover两晶体记录Compton scatter，加另一clover的coincident γ；unpolarized reference由event mixing构造。A_CE=1−Wpol/Wunpol，实用fit为A(ξ)=.5 Q Pγ(Θ)cos2ξ。Fig18a/b同data，b选择8角组并排稀疏组合；它不是原source多一次独立采集（GF19-8）。

## Data Products

| Eγ / keV | 发射核/source | reported Q(σ) | 角色与source locator |
| --- | --- | --- | --- |
| 1332 | 60Ni/60Co | .240(.012) | 锚点；nominal P90=1/6；GF19-8 |
| 1173 | 60Ni/60Co | .258(.012) | 另一能量检查，共source family；GF19-9 |
| 570 | 207Pb/207Bi | .390(.024) | known-P检查；与Fig20 E2角色复用cascade；GF19-9/10 |
| 1771 | 56Fe | .201(.045) | known-P检查，本文正文未给完整逐门ledger；GF19-9 |

GF19-10的Fig20a为1064 M4(+E5)散射/570门，b为570 E2散射/1064门；不得互换target/gate。不同发射核检查提供覆盖，但不能假定每个derived Q、图点与标定参考都统计独立。

源Figure19曲线从1332按方法模型缩放，绿色带不是每能量独立calibration。任务按当前固定generic ScaleQ的条件值.378202/.259795/.198649与源570/1173/1771作比较，仅保存source/code合同与共同anchor rank1敏感性（GF19-13），不重拟实验Q。

## Nuclei and Bands Studied

60Ni与207Pb已知cascade用作reference/仪器演示；56Fe为另能量检查。本页不提供A≈130 mode、未知Jπ或δ的新赋值。实际其它核谱学需自己的relativeplane、P来源和matching response。

## Known Limitations

- 原events/ROOTmatrix、background/逐峰/逐台gate/response与完整Σ未取得；reported known-P calibration不是独立P测量。
- [[grsisort-2026-compton-polarimetry-code]] GRS26-5/6/13显示当前newAnalyzer/默认Lean与schema差别；不是原2018producer认证或论文错误证明。
- 源作者关于减少clover不改变Q的报告只在其校准条件使用（GF19-11）；其它targetweights需核，[[polarimetry-shared-calibration-count-design]]保存条件推导与反例。
- 15clover/PACES效率与16clover偏振calibration分开，不能把photopeak效率直接当selected Compton ε或source-supported F（GF19-1/4）。
- GF19-15–17的Table2方向与当前带45mm代表深度的native点相合，但Table8三角类复现partial；同clover-axis90°在110/145mm给不同crystalΘ域。只保存条件/identity，不从pointgeometry转为原calibration实际event权重或Q。

## Sources

- [[garnsworthy-2019-griffin-facility]] GF19-6/7/8/9/10/11/12/13。
- [[grsisort-2026-compton-polarimetry-code]] GRS26-6/10/13；仅软件路径/版本证据。
- 使用门：[[compton-polarimetry]]、[[linear-polarization-asymmetry]]。

## Evolution Log

- 2026-10-19：本session完整原件读取后建立source标定账本；Codex self-audit、unreviewed，无新experiment/CI或human-review。
