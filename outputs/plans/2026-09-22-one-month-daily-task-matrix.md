# 一个月核结构训练：逐日任务矩阵

本文件是
[`2026-09-22-one-month-codex-cli-apprenticeship.md`](2026-09-22-one-month-codex-cli-apprenticeship.md)
的逐日展开。它补充每日学习动作和验收物，不替代 `system/workflows/continuous-learning.md`
中的证据、写回、L0–L4 和 Git 约束。

博士论文轨道的总设计见
[`2026-09-22-a130-triaxial-thesis-pipeline.md`](2026-09-22-a130-triaxial-thesis-pipeline.md)。从本轮起，每个 Day 卡片同时服务课程能力和论文证据积累。

## 使用规则

- 2026-09-22 的 Day 1/Day 2 回执是 Docker/runner 实例验收，标记为 `acceptance-only`，不计入实质测试；正式 30 天从新的 `day_index: 1` 开始。正式运行失败或中断时重复当天，不跳日。
- 每天完成一个连续性槽位和一个可选的新颖性槽位即可。候选来源以信息增益、独立性和证据可得性排序，不按固定篇数达标。
- 每天的核心交付由五部分组成：不看资料的主动回忆、一个理论或量纲练习、一条主来源证据链、一项反证/缺失伴随观测检查、当日记录。
- 每天还必须产生一项 `durable knowledge delta`：更新 source/project/evidence matrix、保存可复核练习产物、修订开放问题，或留下带证据的 verified no-op；只有日报文字而没有增量时不能把本日称为论文轨道完成。
- 下面的 Wiki 页面是入口候选。实际运行时必须回到原文、图表、公式、能级位置和不确定度；页面摘要不能替代来源证据。
- 每天记录都要写清：实验直接报告、作者解释、模型结果、Codex 推断，以及本日支持、限制、修正、冲突或无实质变化的决定。

## 第 1 周：从研究契约到集体运动

### Day 1 — 基线考试与研究契约

- **回忆：** 不看资料解释 `J^\pi`、激发能、γ 跃迁、能级纲图、claim、locator、evidence level 和 source independence。
- **主线：** 阅读 [`system/vocabulary.md`](../../system/vocabulary.md)、[`spin-parity-assignment`](../../knowledge/methods/spin-parity-assignment.md) 和最近一份 daily record，建立“事实—作者解释—模型—推断”四列表。
- **练习：** 从一个已有能级页画出最小 level scheme，给每条箭头标记证据来源和不确定性；把 12 条陈述分类并说明理由。
- **反证：** 找一条仅由能量简并或模型计算支持的陈述，写出它缺少的必要观测量。
- **交付：** `baseline-error-log`、六个口试问题的初答、当天 continuation prompt，以及 `knowledge/projects/a130-thesis-evidence-matrix.md` 的第一版论文证据矩阵；不创建无证据的知识页。

### Day 2 — 壳层、magic gap 与单粒子轨道

- **回忆：** 说明球形壳层、形变壳隙和单粒子组态的区别。
- **主线：** 以 [`haxel-jensen-suess-1949-magic-numbers`](../../knowledge/sources/haxel-jensen-suess-1949-magic-numbers.md) 和 [`ragnarsson-nilsson-sheline-1978-shell-structure`](../../knowledge/sources/ragnarsson-nilsson-sheline-1978-shell-structure.md) 为入口，追踪一个质量区的轨道演化。
- **练习：** 对比一个近闭壳层核和一个高自旋形变核，写出“壳隙变大/变小”各自需要的实验或计算证据。
- **反证：** 检查 magicity 是否被单一高激发能或单一模型图直接证明，列出至少两个替代 observable。
- **交付：** 一张轨道—壳隙—可观测量映射表，标注模型结果和实验事实。

### Day 3 — 平均场、Nilsson/CSM、HFB 与投影模型

- **回忆：** 区分 mean field、cranked mean field、HFB 和 angular-momentum projection 的输入与输出。
- **主线：** 阅读 [`aberg-flocard-nazarewicz-1990-mean-field-shapes`](../../knowledge/sources/aberg-flocard-nazarewicz-1990-mean-field-shapes.md) 与 [`hara-sun-1995-projected-shell-model-high-spin`](../../knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md) 的模型适用条件。
- **练习：** 给一个 A≈130 高自旋谱学问题选择最小模型路线，写出模型能回答和不能回答的两列。
- **反证：** 对模型计算出的形状或组态，寻找至少一个可能的实验反例或竞争解释。
- **交付：** `model-choice-card`，不得把计算能级写成测量结果。

### Day 4 — 配对、准粒子与组态变化

- **回忆：** 说明 pairing gap、准粒子激发、两准粒子/三准粒子组态与 odd-even effect 的关系。
- **主线：** 结合 [`nomura-2021-pairing-triaxial-vibrations-gamma-soft`](../../knowledge/sources/nomura-2021-pairing-triaxial-vibrations-gamma-soft.md) 和一个已有奇核能带页，追踪配对对能级和集体性的影响。
- **练习：** 把一条 band crossing 或 alignment 特征拆成“直接测量—派生量—解释”三层。
- **反证：** 检查同一 crossing 是否也能由形变改变、带混合或 feeding 解释。
- **交付：** 一张组态变化证据链和一个未解决问题。

### Day 5 — β、γ、八极自由度与 shape coexistence

- **回忆：** 解释 `β_2`、`β_3`、`γ` 的几何含义，以及 γ-soft 与 γ-rigid 的区别。
- **主线：** 阅读 [`davidson-1965-rotations-vibrations-deformed-nuclei`](../../knowledge/sources/davidson-1965-rotations-vibrations-deformed-nuclei.md)、[`heyde-wood-2011-shape-coexistence-review`](../../knowledge/sources/heyde-wood-2011-shape-coexistence-review.md) 和 [`gamma-soft-vs-gamma-rigid-diagnostics`](../../knowledge/synthesis/gamma-soft-vs-gamma-rigid-diagnostics.md)。
- **练习：** 为能级 staggering、B(E2)、静态矩和跃迁连接各指定一个可支持的形状命题，并标出不能单独支持的命题。
- **反证：** 找一个“γ-soft/γ-rigid”竞争解释，写出最小区分观测组合。
- **交付：** `shape-observable-matrix`，保留适用条件和 evidence boundary。

### Day 6 — 转动、振动、alignment 与 signature

- **回忆：** 说明 rotational band、vibrational band、alignment、signature splitting/inversion 的定义。
- **主线：** 以 [`afanasjev-1999-termination-rotational-bands`](../../knowledge/sources/afanasjev-1999-termination-rotational-bands.md)、[`stephens-1975-coriolis-rotation-alignment`](../../knowledge/sources/stephens-1975-coriolis-rotation-alignment.md) 和 [`liu-1996-signature-inversion-a130`](../../knowledge/sources/liu-1996-signature-inversion-a130.md) 为入口。
- **练习：** 从一个能级序列或已有 alignment 描述重建自旋随频率的变化，并写出 band termination 的判据。
- **反证：** 检查 signature inversion 是否可由组态、粒子—转子耦合或参考带选择造成。
- **交付：** 一张 alignment/signature 判读卡和一个带结构草图。

### Day 7 — 第一次周考：集体运动口试

- **回忆：** 随机回答前六天各一个定义题，不看 Wiki。
- **主线：** 选择一个已读案例，完整复述从壳结构/形变到能带解释的证据链。
- **练习：** 对一个未知能带描述完成 20 分钟结构判读：组态候选、必要观测、替代解释和停止条件。
- **反证：** 明确指出哪一条证据最可能改变当前判断，以及为什么。
- **交付：** 周考评分表（理论、判图、误差、证据分层、反证、可证伪问题各 0–4 分）和 `weekly REFLECT`。

## 第 2 周：电磁跃迁与 γ 谱学实验链

### Day 8 — 角动量耦合、选择定则与多极性

- **回忆：** 写出 E1/M1/E2 的宇称变化和角动量选择定则，说明禁止与受抑的区别。
- **主线：** 阅读 [`lange-kumar-hamilton-1982-multipole-admixtures`](../../knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md) 和 [`rose-brink-1967-phase-defined-angular-distributions`](../../knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md)。
- **练习：** 给三条跃迁列出可能的多极组合，写出需要哪种角分布、偏振或寿命信息来排除解。
- **反证：** 检查 parity、spin、multipolarity 是否被同一观测独立支持。
- **交付：** 选择定则和多解表；所有符号约定写明来源。

### Day 9 — B(E2)、B(M1)、约化矩阵元与强度比

- **回忆：** 说明 partial lifetime、branching ratio、mixing ratio 与 B(Eλ)/B(Mλ) 的关系。
- **主线：** 以 [`high-spin-lifetime-strength-deformation`](../../knowledge/synthesis/high-spin-lifetime-strength-deformation.md) 和 [`mukhopadhyay-2008-136nd-transition-rates`](../../knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md) 为主线。
- **练习：** 从给定的寿命、能量和分支强度重算一条 B(E2) 或 B(M1) 的输入链，列出单位和分支归一化。
- **反证：** 检查未观测分支、feeding、内转换或 branching uncertainty 对结果的影响。
- **交付：** 一页“输入—公式—输出—误差”表，不能把视觉强度当作 B 值。

### Day 10 — 电磁比值与集体模式判别

- **回忆：** 解释 B(M1)/B(E2)、in-band/out-of-band 强度比和 transition quadrupole moment 的物理含义。
- **主线：** 结合 [`mukhopadhyay-2007-135nd-chiral-vibration-static`](../../knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md)、[`grodner-2018-128cs-chiral-g-factor`](../../knowledge/sources/grodner-2018-128cs-chiral-g-factor.md) 和相关 project 页。
- **练习：** 对两条候选带制作比值随自旋的表格，区分直接测量、派生强度和模式解释。
- **反证：** 写出至少一个能产生相似比值趋势的非目标机制。
- **交付：** `mode-discrimination-card`，注明哪些趋势只构成必要条件而非充分条件。

### Day 11 — 反应布居、蒸发道与高自旋入口

- **回忆：** 解释 fusion-evaporation、compound nucleus、evaporation residue、γ cascade 和 side feeding。
- **主线：** 阅读 [`in-beam-gamma-spectroscopy`](../../knowledge/methods/in-beam-gamma-spectroscopy.md)、[`compound-nucleus-reaction-model`](../../knowledge/models/compound-nucleus-reaction-model.md) 和一个实验页（如 `Ding 127,128I` 或 `193Bi`）。
- **练习：** 从束流/靶/反应道重建“布居—探测—门控—能级”的流程图。
- **反证：** 标出产额、选择偏差、side feeding 和未观测通道可能改变哪一项结论。
- **交付：** 反应到 level scheme 的证据流程图。

### Day 12 — γγ 符合、门条件、背景与能级纲图

- **回忆：** 解释 prompt/delayed gate、coincidence、random、Compton background 和 gate bias。
- **主线：** 以 [`gamma-gamma-coincidence`](../../knowledge/methods/gamma-gamma-coincidence.md)、[`walz-2015-competitive-double-gamma-137ba`](../../knowledge/sources/walz-2015-competitive-double-gamma-137ba.md) 和 [`soderstrom-2020-137ba-competitive-gamma`](../../knowledge/sources/soderstrom-2020-137ba-competitive-gamma.md) 为入口。
- **练习：** 为一张假想 coincidence matrix 设计 gate 顺序，并写出每一步如何排除随机或级联背景。
- **反证：** 检查一条弱线是否可能是 escape、sum peak、随机符合或错误级联。
- **交付：** `gate-and-background-audit`，含至少一个不能由当前数据解决的歧义。

### Day 13 — Doppler correction、recoil 与速度信息

- **回忆：** 说明 Doppler shift、recoil velocity、detector angle、stopping history 和 event-by-event correction。
- **主线：** 阅读 [`doppler-correction`](../../knowledge/methods/doppler-correction.md)、[`mavela-2019-32s-quadrupole-moment-doppler-correction-thesis`](../../knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md) 和一个 in-beam 实验 source。
- **练习：** 用给定能量、速度和角度重算 Doppler-shifted energy，并说明速度不确定度如何传递。
- **反证：** 区分真实宽线、未完全校正、反冲停止和多条近邻跃迁。
- **交付：** 一页 Doppler correction 诊断表，保留原文 locator。

### Day 14 — 第二次周考：从谱到能级纲图

- **回忆：** 盲画一条三层级联并标注门条件、DCO/偏振/寿命可能放在哪一步。
- **主线：** 选择 [`herzan-2015-193bi-spectroscopy`](../../knowledge/sources/herzan-2015-193bi-spectroscopy.md) 或 [`ding-2012-phd-thesis-127-128i-high-spin`](../../knowledge/sources/ding-2012-phd-thesis-127-128i-high-spin.md)，沿全文主线核对一张图和一张表。
- **练习：** 重建一段 level scheme，并给每条新线标记能量、符合、multipolarity、spin/parity 证据等级。
- **反证：** 写出至少一个会让该纲图重排的观测结果。
- **交付：** 实验判据矩阵、周考评分表和 weekly REFLECT。

## 第 3 周：角分布、偏振、寿命与形变

### Day 15 — ADO、角分布系数与几何修正

- **回忆：** 解释 angular distribution、`A_2/A_4`、ADO 和效率修正。
- **主线：** 阅读 [`angular-distribution`](../../knowledge/methods/angular-distribution.md)、[`angular-distribution-coefficient`](../../knowledge/observables/angular-distribution-coefficient.md) 和 [`zheng-2002-ado-coincidence-angular-anisotropy`](../../knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md)。
- **练习：** 用两角度计数和效率比计算一个 `f_ADO`，并画出输入误差如何影响比值。
- **反证：** 检查 alignment、feeding、有限立体角和门条件是否改变 multipolarity 判读。
- **交付：** 一个可复核的 ADO 计算单和 convention 注记。

### Day 16 — DCO/RDCO、混合比与符号约定

- **回忆：** 说明 DCO gate、reference transition、`δ`、E2/M1 混合和 sign convention。
- **主线：** 以 [`angular-correlation`](../../knowledge/methods/angular-correlation.md)、[`droste-1996-pdco-formalism`](../../knowledge/sources/droste-1996-pdco-formalism.md) 和 [`krane-steffen-1970-cd110-mixing-ratios`](../../knowledge/sources/krane-steffen-1970-cd110-mixing-ratios.md) 为入口。
- **练习：** 对一个 RDCO/`δ` 数据点列出两个可能解，写出需要补充的 reference 或偏振信息。
- **反证：** 对照两个 phase/convention 来源，找出相同符号下公式不能直接互换的原因。
- **交付：** `delta-double-solution-sheet`，明确保留多解。

### Day 17 — 线偏振、P/A/Q 与 Compton 响应

- **回忆：** 解释 `P`、`A`、`Q`、polarization sensitivity、FOM 和 Compton analyzer geometry。
- **主线：** 阅读 [`gamma-ray-linear-polarization`](../../knowledge/methods/linear-polarization-asymmetry.md)、[`starosta-1999-pdco-experimental-test`](../../knowledge/sources/starosta-1999-pdco-experimental-test.md) 和 [`schmid-1998-gammasphere-polarization`](../../knowledge/sources/schmid-1998-gammasphere-polarization.md)。
- **练习：** 从平行/垂直计数和 `Q(E)` 计算偏振不对称，并写出统计误差。
- **反证：** 检查几何、阈值、背景和 calibration transition 对 parity/multipolarity 的影响。
- **交付：** 一张 P/A/Q 分层表和一项需要独立校准的输入。

### Day 18 — DSAM：寿命到跃迁强度

- **回忆：** 说明 line-shape、stopping power、feeding、side feeding、`τ` 和 `Q_t` 的关系。
- **主线：** 阅读 [`doppler-shift-attenuation-method`](../../knowledge/methods/doppler-shift-attenuation-method.md)、[`jensen-2001-165tm-h9-2-configuration`](../../knowledge/sources/jensen-2001-165tm-h9-2-configuration.md) 和 [`mukhopadhyay-2008-136nd-transition-rates`](../../knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md)。
- **练习：** 写出 `τ → B(Eλ) → Q_t` 的假设链，给每一项加入一个系统误差来源。
- **反证：** 检查不同 stopping model、feeding 假设或 band mixing 是否能改变形变结论。
- **交付：** `lifetime-strength-audit`，区分测量、拟合、换算和解释。

### Day 19 — RDDS、fast timing 与时间响应

- **回忆：** 区分 DSAM、RDDS、fast timing、TDPAD 的时间窗口和主要响应。
- **主线：** 阅读 [`recoil-distance-doppler`](../../knowledge/methods/recoil-distance-doppler-shift.md)、[`radeck-2012-deorientation-lifetime-98ru-rdds`](../../knowledge/sources/radeck-2012-deorientation-lifetime-98ru-rdds.md) 和 [`nolan-sharpey-schafer-1979-lifetime-measurements`](../../knowledge/sources/nolan-sharpey-schafer-1979-lifetime-measurements.md)。
- **练习：** 为同一寿命范围选择 DSAM、RDDS 或 fast timing，并说明分辨率、feeding 和停止材料约束。
- **反证：** 写出一个看似精确但被时间响应或校准系统误差主导的情形。
- **交付：** 方法选择决策树和最小校准清单。

### Day 20 — B(E2)、Q_t 与形变系统学

- **回忆：** 解释 `B(E2)`、`Q_t`、静态四极矩和 β₂ 之间的模型依赖。
- **主线：** 以 [`transition-quadrupole-moment`](../../knowledge/observables/transition-quadrupole-moment.md)、[`petrache-1998-highly-deformed-lifetimes-131ce-nd`](../../knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md) 和 [`singh-2016-lifetime-131ce-133pr`](../../knowledge/sources/singh-2016-lifetime-131ce-133pr.md) 为案例。
- **练习：** 从一组相邻自旋的 B(E2) 或 Q_t 数值计算加权趋势，写出不能跨组态直接比较的条件。
- **反证：** 检查 γ-soft、带混合、feeding 或不同 lifetime 技术是否足以产生相似趋势。
- **交付：** 一张 lifetime/strength/deformation 证据图。

### Day 21 — 第三次周考：实验结论边界

- **回忆：** 不看资料说明从 γ 能量到形变/集体模式结论至少经过哪些转换。
- **主线：** 选一个 `131Ce`、`135Nd` 或 `100Sn` 案例，逐条回到原文 locator，检查一条主张的直接证据和竞争解释。
- **练习：** 给定未知实验摘要，写一段“可以说什么、不能说什么、下一步测什么”的证据门文本。
- **反证：** 明确一个会推翻当前解释的结果，并说明它是否在现有装置上可测。
- **交付：** 综合口试评分表、一个 claim-level audit 和 weekly REFLECT；不清除任何 `needs_review`。

## 第 4 周：争议模式、跨质量区与独立研究

### Day 22 — wobbling：几何、声子与观测量

- **回忆：** 区分 transverse/longitudinal wobbling、wobbling phonon、out-of-band E2 和 M1/E2 比值。
- **主线：** 阅读 [`wobbling-motion`](../../knowledge/concepts/wobbling-motion.md)、[`frauendorf-2014-transverse-wobbling`](../../knowledge/sources/frauendorf-2014-transverse-wobbling.md)、[`hamamoto-2003-quantized-wobbling-excitations-alignments`](../../knowledge/sources/hamamoto-2003-quantized-wobbling-excitations-alignments.md)。
- **练习：** 对一个候选 wobbling 带列出 band energy、in/out-of-band strengths、alignment 和 polarization 四列证据。
- **反证：** 以 `135Pr` 或 `135Nd` 的反例检验“近简并 + 强 E2”是否足够。
- **交付：** wobbling 判据卡，注明必要条件、支持条件和反证。

### Day 23 — signature partner、低自旋 wobbling 与磁转动

- **回忆：** 区分 signature partner、wobbling、tilted precession、magnetic rotation 和 antimagnetic rotation。
- **主线：** 阅读 [`signature-partner-bands`](../../knowledge/concepts/signature-partner-bands.md)、[`guo-2022-low-spin-wobbling-187au`](../../knowledge/sources/guo-2022-low-spin-wobbling-187au.md)、[`lv-2022-evidence-against-wobbling-135pr`](../../knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md)。
- **练习：** 对 `187Au/135Pr` 建立支持—反证—依赖关系矩阵，显式标出 shared dataset。
- **反证：** 写出一个只改变 configuration assignment 而不改变实验计数的替代解释。
- **交付：** 一份争议谱系图和一个可证伪问题。

### Day 24 — chirality：手征振动、静态手征与 partner bands

- **回忆：** 解释三根角动量、左右手构型、chiral vibration 与 static chirality 的区别。
- **主线：** 阅读 [`nuclear-chirality`](../../knowledge/concepts/nuclear-chirality.md)、[`frauendorf-meng-1997-tilted-rotation-chirality`](../../knowledge/sources/frauendorf-meng-1997-tilted-rotation-chirality.md) 和 [`mukhopadhyay-2007-135nd-chiral-vibration-static`](../../knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md)。
- **练习：** 为一个双带候选逐项填写能量、B(M1)/B(E2)、角动量几何和 g 因子证据。
- **反证：** 检查 crossing、configuration change、γ-softness 和 band mixing 是否能重现部分特征。
- **交付：** partner-resolved evidence map，分开实验、TAC/RPA 和推断。

### Day 25 — chirality 反例与 shape coexistence

- **回忆：** 说明“近简并”为什么不是手征充分条件，并区分 shape coexistence 与 chiral doublet。
- **主线：** 阅读 [`petrache-2006-near-degenerate-chiral-misinterpretation`](../../knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md)、[`lv-2019-chirality-135nd-reexamined`](../../knowledge/sources/lv-2019-chirality-135nd-reexamined.md) 和 [`triaxial-shape-coexistence`](../../knowledge/concepts/triaxial-shape-coexistence.md)。
- **练习：** 对 `134Pr/135Nd/136Nd` 做三行比较：直接观测、作者解释、替代解释。
- **反证：** 写出最小 companion observables 组合，说明缺一项时结论如何降级。
- **交付：** chirality/shape-coexistence 竞争解释矩阵。

### Day 26 — 八极关联、E1/E3 与磁/反磁转动

- **回忆：** 区分直接 E3、E1 enhancement、octupole correlation、magnetic rotation 和 antimagnetic rotation。
- **主线：** 阅读 [`bucher-2016-144ba-direct-octupole`](../../knowledge/sources/bucher-2016-144ba-direct-octupole.md)、[`bucher-2017-146ba-direct-octupole`](../../knowledge/sources/bucher-2017-146ba-direct-octupole.md)、[`garg-2015-135pr-magnetic-rotation`](../../knowledge/sources/garg-2015-135pr-magnetic-rotation.md)。
- **练习：** 做“直接测量—派生强度—模型解释”三级证据梯度，核对单位和不确定度。
- **反证：** 检查 E1 强度变化是否可以脱离 octupole strength 单独解释。
- **交付：** octupole/MR 证据梯度图，保留质量区适用边界。

### Day 27 — 跨质量区迁移与不适用性

- **回忆：** 说出至少三个不能把同一判据直接跨核素迁移的原因。
- **主线：** 选择 A≈80/100/130/160/190 中四个已有 Wiki 案例，例如 `78Br`、`100Sn`、`131Ce/135Pr`、`165Tm` 或 `188Pt`。
- **练习：** 建立“机制—observable—装置—证据等级—竞争解释”横向表，至少包含一个方法相同但物理解释不同的案例。
- **反证：** 找一个跨质量区类比会失败的实例，记录停止理由。
- **交付：** cross-mass transfer matrix；不新增无来源的普适结论。

### Day 28 — 独立 L3 研究日与第四次周考

- **回忆：** 用五分钟口述 L3 的问题、证据、反证、停止条件和下一步。
- **主线：** 从 `knowledge/questions.md`、active WIP queue 和近期 source fingerprints 选一个未解决问题；最多一个 continuity 槽位和一个 novelty 槽位。
- **练习：** 完成 source-to-claim-to-locator evidence map，做一次定量/设计检查，并写出 falsifier。
- **反证：** 若原始数据、response、covariance 或 code 缺失，写 readiness boundary，禁止生成代理 L4 结果。
- **交付：** L3 milestone、周考评分表、weekly REFLECT 和明确的停止/续跑理由。

### Day 29 — 研究设计答辩

- **回忆：** 解释一个研究问题所需的最小 observable、校准、响应、背景和协方差。
- **主线：** 为 Day 28 的问题设计可执行的实验或分析方案：样品/反应、探测器、门控、校准、效率、systematics、negative control。
- **练习：** 写出三种结果情形及其 belief revision：支持、削弱、改变竞争解释排序。
- **反证：** 列出最可能的失败模式和在正式结论中应如何降级措辞。
- **交付：** 一页 research-defense，明确哪些内容仍需用户数据或人工审核。

### Day 30 — 综合口试与月度 prospectus

- **回忆：** 从四个模块各抽一道题：理论、谱学、争议证据、研究设计。
- **主线：** 回读本月四份 weekly REFLECT、错题表和 Day 28 L3 milestone，检查是否有重复引用、未闭合 locator 或被误升格的模型解释。
- **练习：** 完成最终 prospectus：问题、已有证据、竞争假设、最小 observable 组合、数据需求、响应/协方差、失败检查、预期 belief revision、下一阶段阅读路线。
- **反证：** 写出“什么结果会让我改变主结论”，并区分可在当前资源下检验与暂不可检验的部分。
- **交付：** 月度口试评分、prospectus、30 天状态回执；只有 30 次成功 receipt 齐全时才标记课程完成。

## 每日记录的最小验收

当天报告必须能回答以下问题：

1. 今天选择的问题相对候选池为什么有更高信息增益？
2. 哪一条 claim 有原文 locator，属于哪种 evidence level 和 source independence？
3. 今天找到的反证、替代解释或缺失伴随 observable 是什么？
4. 理论/计算练习的输入、单位、不确定度和结果是什么？
5. Knowledge Impact and Learning Decision 是 supports、limits、revises、conflicts 还是 no material change？
6. 当前 L0–L4 状态、停止原因和下一次 continuation prompt 是什么？

没有实质新知时，写 `verified no-op` 并说明检查过的候选和停止依据，不制造空页面或空提交。
