---
type: synthesis
title: "γ-soft deformation: diagnostics, coupling, and deformation evolution"
aliases: [γ-soft 与 γ-rigid 的低能谱判别, gamma-soft deformation synthesis]
created: 2026-07-01
updated: 2026-10-25
status: ai-draft
review_status: human-reviewed
scope: gamma-soft-deformation-a130-and-nearby-evidence
confidence: medium
high_confirmed_by:
high_confirmed_date:
sources: [zamfir-casten-1991-gamma-softness-triaxiality, nomura-2017-odd-mass-gamma-soft-shape-transitions, nomura-2021-pairing-triaxial-vibrations-gamma-soft, babra-2019-deformation-change-136sm, frauendorf-2024-wobbling-review, singh-2016-lifetime-131ce-133pr]
tags: [gamma-softness, gamma-rigidity, shape-phase-transition, pairing-vibration, deformation-evolution, evidence-matrix]
---

# γ-soft Deformation：判据、耦合与形变演化的阶段性综合

## Agent active summary — Day22

当前Day22增量保留“邻芯softness不是奇A高spin模式普适禁戒”和模型PES/磁性算符的不同约束。[[frauendorf-2024-wobbling-review]] F24-D22-R108-1属于作者模型比较；[[nomura-2022-questioning-wobbling-ibfm]] NOM22-D22-R108-2说明受限PES不独立确定所有影响M1的参数，不能由此认证任一模式。 本段是Codex self-audit导航，新增内容needs_review: true，不扩张原有human-reviewed范围，也不替代source locator。

## Question and Scope

基于四篇已审核核心 source，阶段性综合 γ-soft deformation 的定义、与 γ-rigid triaxiality 的区别、A≈130 形状相变、配对-三轴振动耦合和 `136Sm` 随自旋形变变化。[[frauendorf-2024-wobbling-review]] 只用于 low-spin collective-band relation；未审核的 [[singh-2016-lifetime-131ce-133pr]] 仅作为 `131Ce` targeted update，并保留独立 P1。本文不是 paper conclusion；每项主张仍须回到 source、raw 与 locator。

## Evidence Matrix

| 主张 | 支持证据 | 反证/限制 | 替代解释 | 来源独立性 | 置信度 |
|---|---|---|---|---|---|
| γ-soft 是 γ 方向势能较平坦和波函数涨落，不是固定 γ 值 | ZC91-1 至 ZC91-4；PDF pp.1-4；NOM21-1/NOM21-7；PDF pp.1-4 | W-J/O(6) 是理想 γ-independent 极限；真实核常处于两极限之间 | 固定三轴极小、组态混合、shape coexistence | Zamfir 与 Nomura 方法链独立；Nomura 2017/2021 相互依赖 | medium |
| γ-band staggering 可区分 W-J 与 D-F 理想极限 | ZC91-1 至 ZC91-3；PDF pp.1-4, Figs.1-2 | 只限低自旋偶偶 γ 带；弱 γ 依赖即可改变相位/幅度 | 带混合、能级误指认、微观模型中的分布效应 | 单一奠基来源 | medium |
| A≈130 偶偶芯与奇 A 低能态呈现相关但态依赖的 shape-phase-transition signals | NOM17-1 至 NOM17-9；PDF pp.5-12, Figs.1-15 | `γ_eff` 是模型 E2 不变量；Fig.13 `0+_1` 峰值不普遍复制到奇 A 态 | 奇粒子极化、逐核拟合、有限核平滑 | 单一理论实现 | low |
| pairing softness 与 γ softness 可共同影响低能谱 | NOM21-1 至 NOM21-9；PDF pp.1-5, Figs.1-4 | 只计算 `128,130Xe`；无质子/中子 pairing 分离，缺多准粒子空间 | shape coexistence、准粒子激发 | 与 Nomura 2017 共享作者/映射方法 | low |
| `136Sm` 带交叉后 E2 集体性下降 | B19-1 至 B19-5、B19-8；PDF pp.1-3, Table I; p.6, Fig.8 | `Q_t` 系统误差与 feeding；只到 20+ | 带混合、多个竞争形变极小 | 独立实验来源 | medium |
| `136Sm` 从 γ-soft 到稳定三轴的演化是模型支持的作者解释 | B19-6 至 B19-12；PDF pp.4-9, Figs.6-10 | TRS/TPSM 参数化；第二交叉以上寿命不足 | oblate / highly deformed prolate / triaxial coexistence | 同一实验内的两模型比较，不是独立实验复现 | low |
| γ-softness 只能作为 low-spin band interpretation 的形变背景 | F24-3/F24-7；PDF pp.22-26；[[low-spin-wobbling-controversies]] LSW-SYN-1 | review 不是原始实验；wobbling 仍需 band identity 与电磁判据 | signature partner、TiP、β/γ vibration、其他 qp excitation | review + 已审 project navigation | low |
| `131Ce` Band-1-like 寿命补上目标核 E2 集体性约束，但不独立建立 γ-softness | SI16-1 至 SI16-7；PDF pp.5-10, Table 1, Figs.5,9-12 | 四个有限 `Q_t` 点的下降仅 `0.64σ`；γ-soft/具体 γ 来自 TRS 与作者解释 | 组态/带交叉响应、其他非轴芯响应、分析系统学 | Singh 与 Li 当前测量是独立实验；Singh 转载 Li 行不重复计权 | low / needs review |

## Synthesis

## What Gamma-soft Deformation Means in This Wiki

γ-soft 描述 γ 方向的势能曲率和集体波函数分布：势面较平、波函数可在较宽 γ 区间涨落。它允许非零平均 γ，也不要求完全 Wilets-Jean γ independence。最稳妥的语言是“该模型/观测组合支持较软的 γ 动力学”，而不是把一个拟合 γ 写成直接形状测量（ZC91-4；PDF p.4；NOM21-1/NOM21-2；PDF p.2, Fig.1）。

## Difference from Gamma-rigid Triaxiality

γ-rigid 要求低能波函数在某个非零 γ 附近局域，比“存在三轴性”更强。Zamfir–Casten 的 γ-band staggering 和 Nomura 2021 的 `E2γ/R3γ` 只把数据或计算放到 W-J/D-F 理想参考之间；二者都不允许由单个指标反演唯一刚度（ZC91-1 至 ZC91-4；PDF pp.1-4；NOM21-7；PDF p.4, Fig.3）。

手征双重带和 wobbling bands 是稳定三轴形变研究中的重要候选集体指纹：前者依赖三轴体系中的 aplanar angular-momentum geometry，后者依赖三轴转动惯量和集体进动。然而，候选模式的能带标签不等同于对势能面局域性的直接测量；手征性和 wobbling 身份还分别需要伙伴带、电磁跃迁、角动量几何和竞争解释检验（FM97-1 至 FM97-6；PDF pp.5-16；F24-1 至 F24-7；PDF pp.1-26）。

## Why A≈130 and Nearby Nuclei Matter

Ba/Xe 在 N≈76-78 附近提供近球形到 γ-soft 的形状相变模型案例；奇 A Ba/Xe/La/Cs 又展示奇粒子耦合后信号会随宇称和自旋态错开（NOM17-1 至 NOM17-9；PDF pp.5-12）。`136Sm` 位于邻近质量区，提供形变背景可随转动频率和带交叉改变的实验参照，但不能替代 Ce 的 nucleus-specific evidence（B19-1 至 B19-12；PDF pp.1-9）。

## Shape-phase Transition Perspective

Nomura 2017 的 RHB→IBM/IBFM 计算把 `134Ba/132Xe` 放在 E(5)-like 过渡区，并用能级演化、基态自旋变化与 E2 形状不变量讨论 N≈76-78 的转变。该结果是一个统一模型内的相关证据链，不是多个独立实验的共同裁决；IBFM 粒子-芯耦合还需逐核拟合（NOM17-1 至 NOM17-10；PDF pp.5-12）。

## Pairing and Triaxial Shape Vibration Perspective

Nomura 2021 表明，若模型空间允许玻色子数变化，pairing vibration 会显著降低激发 `0+` 态，而三轴自由度主要控制 γ 带结构；配对耦合还可能因子空间混合提高 γ 带能量（NOM21-3 至 NOM21-6；PDF pp.2-4, Eqs.(1)-(5), Figs.2-3）。因此，把低能结构只归因于 γ softness 可能遗漏 pairing softness；但当前证据只来自 `128,130Xe` 的同一模型实现。

## Experimental Deformation-change Perspective from 136Sm

Babra 2019 的实验层建立了寿命、`Q_t`、alignment 与带交叉。12+ 以上 `Q_t` 总体下降支持集体性减弱（B19-2 至 B19-5、B19-8；PDF pp.2-3, Table I; p.6, Fig.8）。TRS/TPSM 再把这一变化解释为由低频 γ-soft 极小转向较稳定三轴极小；形状标签和具体 `β2/γ` 仍属模型结果/作者解释（B19-6 至 B19-12；PDF pp.4-9）。

### γ-soft→rigid/stable-triaxial Transition as a Research Topic

这条 transition 是当前 A≈130 及邻近核结构研究的重要问题，因为它把形变动力学、带交叉、准粒子对齐和高自旋集体模式放入同一条可检验链。Babra 2019 当前提供的链条为：

1. **实验层**：DSAM 给出 8+ 至 20+ 的寿命/上限及 `Q_t`；`Q_t` 在 12+ 以上总体降低，经验 alignment/`J^(2)` 在约 `ħω=0.30, 0.38, 0.50 MeV` 显示交叉（B19-1 至 B19-5；PDF pp.1-3, Table I, Fig.5）。
2. **TRS 模型层**：低频 `ħω=0.10-0.30 MeV` 存在 `β2≈0.30, γ≈0°` 附近的 γ-soft 极小；其后 `β2≈0.22, γ≈-25°` 的较稳定三轴极小出现。第二交叉以上还有 oblate 与 highly deformed prolate 竞争极小（B19-7/B19-9；PDF pp.5-6, Figs.7-8）。
3. **TPSM 模型层**：`β=0.30, γ=26°` 较好描述低自旋及 γ 带头，`β=0.22, γ=-25°` 较好描述交叉以上 yrast 能量和 `Q_t`；第一次、第二次交叉分别联系到 2qp proton 与 4qp proton-neutron structures（B19-10/B19-11；PDF pp.7-8, Figs.9-10）。
4. **作者解释层**：作者综合实验和两类模型，将其表述为第一次带交叉附近由 γ-soft 形状向 rigid/stable-triaxial shape 演化（B19-12；PDF pp.8-9, Conclusions）。

这条链的科学价值在于提出了“随自旋发生 soft-to-rigid localization”的可检验问题；它尚未构成模型无关证明。后续需要在目标 A≈130 核中联合寿命/绝对 B(E2)、E2 matrix elements 或 shape invariants、带交叉组态和允许 γ 涨落的动态计算，并与固定三轴模型在 common input/convention 下比较。对于 `131Ce/133Ce`，还必须显式处理奇粒子-芯耦合，不能把 `136Sm` 的转变直接迁移过去。

## How Gamma Softness May Affect Low-spin Collective-band Interpretation

γ-softness 会改变芯的形状涨落、能级和 E2 背景，并可能影响奇粒子-芯耦合模型的适用性；它应在 wobbling、chirality 或 signature-partner 判断之前检查。但 γ-soft 与 wobbling 不自动绑定：wobbling 仍需 band identity、连接跃迁性质、能量行为、角动量几何和近似条件等独立证据（F24-3/F24-7；PDF pp.22-26；[[low-spin-wobbling-controversies]] LSW-SYN-1/LSW-SYN-5）。

## What Gamma-soft Evidence Can and Cannot Establish

可以建立：

- 指定模型中 γ 势面较平或波函数具有较宽 γ 分布；
- 低能偶偶 γ 带相对 W-J/D-F 参考的谱学位置；
- 指定态的 E2 形状不变量、寿命/`Q_t` 和集体性随自旋变化；
- 形变背景是否需要考虑 pairing、带交叉或竞争极小。

不能单独建立：

- 唯一静态 γ、γ 符号或 γ-rigid 形状；
- 把偶偶低能判据无条件移植到奇 A 高自旋；
- 由 `Q_t` 下降唯一决定势能极小；
- wobbling、chirality、signature partner 或 TiP 的实验身份。

## Counter-evidence

- Nomura 2021 的两个诊断量指向不同参考极限，是“单一指标分类”的内部反向检验（NOM21-7；PDF p.4, Fig.3）。
- Nomura 2017 中偶偶 `0+_1` 与奇 A 各低能态的 `γ_eff` 变化不呈统一峰值，是“同一临界模板跨态迁移”的反向检验（NOM17-7/NOM17-8；PDF pp.11-12, Figs.13-15）。
- Babra 2019 在第二交叉以上给出 oblate、triaxial 与 highly deformed prolate 多个竞争极小，且寿命范围不足，是“`Q_t` 唯一选形状”的反向检验（B19-9；PDF p.6）。
- 当前库未找到现代 A≈130 Coulomb-excitation matrix-element 数据或 common-input soft-vs-rigid comparison；这表示当前覆盖缺口，不表示相关工作不存在。

## Model Dependence

- γ-unstable/W-J、D-F、IBM/IBFM、SCMF、TRS 与 TPSM 的 γ 参数、势能映射和自由度不同；
- Nomura 2017/2021 共享作者与 SCMF→IBM 方法链，不能机械计作两份完全独立理论证据；
- Babra 的 `Q_t` 是实验量，但从 `Q_t` 到 `β2/γ` 和稳定三轴的映射依赖 TRS/TPSM；
- 奇 A Ce 应显式包含奇粒子耦合、能带定义、pairing 和 band crossing，不能只套偶偶参考线。

## Synthesis Claims for Review

| ID | Synthesis statement | Source basis with locator | Reverse-test / boundary | needs_review |
|---|---|---|---|---|
| GSD-SYN-1 | γ-softness 应定义为势能面/波函数的 γ 动力学性质，而不是单一固定 γ | ZC91-1 至 ZC91-4, PDF pp.1-4；NOM21-1/NOM21-7, PDF pp.2,4 | 理想极限与真实核之间的映射依赖模型 | false |
| GSD-SYN-2 | 低能偶偶 γ-band staggering 适合排除简单极限，但不足以唯一反演 γ 刚度 | ZC91-1 至 ZC91-4, PDF pp.1-4 | 带混合、弱 γ 依赖和能级指认可改变指标 | false |
| GSD-SYN-3 | A≈130 shape-phase-transition signals 在偶偶芯和奇 A 各态之间相关但不普遍同形 | NOM17-1 至 NOM17-9, PDF pp.5-12 | 单一 IBFM/EDF 实现，奇 A 耦合逐核拟合 | false |
| GSD-SYN-4 | pairing softness 是 γ-soft 低能谱解释中不可忽略的候选自由度 | NOM21-1 至 NOM21-9, PDF pp.1-5 | 仅 `128,130Xe`；模型空间不含多准粒子高激发 | false |
| GSD-SYN-5 | `136Sm` 建立了一个可定位的 γ-soft→rigid/stable-triaxial transition 候选证据链：实验寿命/`Q_t` 和带交叉约束集体性变化，TRS/TPSM 给出交叉前后的不同形变极小/输入，作者据此提出 soft-to-rigid 演化；该 transition 是未来 A≈130 形变研究的重点，而不是已由单一实验量直接证明的普遍结论 | B19-1 至 B19-12；PDF pp.1-9, Table I, Figs.5-10, Conclusions | 模型参数与 γ 约定依赖；第二交叉以上多极小未闭合；`136Sm` 不能代替 `131Ce/133Ce` nucleus-specific evidence | false |
| GSD-SYN-6 | 形变背景可随自旋改变，因此固定形变输入的 collective-band interpretation 需跨带交叉复核 | B19-7 至 B19-12, PDF pp.5-9 | 邻近 Sm 案例不能代替 Ce 证据 | false |
| GSD-SYN-7 | γ-softness 是 wobbling/chirality/signature 分析的背景层，但不是任一模式的充分或必要身份标签 | F24-3/F24-7, PDF pp.22-26；low-spin umbrella LSW-SYN-1 | 仍需逐带电磁与几何判据 | false |
| GSD-SYN-8 | 截至 2026-07-05，四源足以建立 bounded evidence framework，但不足以裁决 `131Ce/133Ce` 的具体形变动力学 | 四个核心 source 全部已审 | 当时缺 nucleus-specific lifetime/E2；后续 Singh 2016 更新见 GSD-SYN-9，common-input calculations 仍缺 | false |
| GSD-SYN-9 | Singh 2016 补上 `131Ce` nucleus-specific 寿命/`Q_t`，直接约束 E2 集体性/core response；`3→2.5 eb` 是作者目视概括，有限点斜率仅 `0.64σ`，γ-softness 仍为 TRS/作者解释层 | SI16-1 至 SI16-7；PDF pp.5-10, Table 1, Figs.5,9-12；[[131ce-collective-mode-discrimination]] | 缺多带 absolute E2、shape invariants 和 common-input soft-vs-rigid calculation，不能由寿命单独裁决 γ 动力学 | false |

## Confidence Notes

W-J/D-F 相位差和 `136Sm` 寿命/`Q_t` 数值为可定位证据；GSD-SYN-1 至 GSD-SYN-9 已完成相应人工审核，总体框架维持 medium。GSD-SYN-9 把“没有目标核寿命入口”修正为“已有 Band-1-like E2 约束，但 γ-soft 仍未被实验独立裁决”；Singh source 页面整体与其它 source claims 的 review 状态不随该 targeted synthesis review 改变。

## Limitations and Missing Evidence

- `131Ce` 已有 Band-1-like nucleus-specific 寿命/`Q_t`，但 `131Ce/133Ce` 仍缺多带 absolute B(E2)、E2 matrix elements 与 shape invariants；
- 缺现代偶偶 Xe/Ba/Ce/Nd Coulomb-excitation 不变量；
- 缺 common-input、common-γ-convention 的 soft collective model 与 rigid triaxial/odd-particle model 比较；
- 缺第二个独立理论链复核 Nomura 2017/2021；
- 缺 `136Sm` 第二交叉以上寿命与多极小判别；
- 缺针对 γ-softness 如何改变具体 low-spin wobbling/TiP 近似的 nucleus-specific calculation。

## Sources

- [[zamfir-casten-1991-gamma-softness-triaxiality]]
- [[nomura-2017-odd-mass-gamma-soft-shape-transitions]]
- [[nomura-2021-pairing-triaxial-vibrations-gamma-soft]]
- [[babra-2019-deformation-change-136sm]]
- [[frauendorf-2024-wobbling-review]]
- [[singh-2016-lifetime-131ce-133pr]]（GSD-SYN-9 targeted synthesis statement 已审；source 页面整体仍未审核）
- Project: [[gamma-soft-deformation-evidence-map]]

## Evolution Log

- 2026-07-01：首次建立低能判据与外推边界。
- 2026-07-05：基于三篇新审核 source 扩展为 shape-phase transition、pairing-triaxial coupling、`136Sm` deformation-change 与 low-spin relation 的阶段性综合；GSD-SYN-1 至 GSD-SYN-8 经用户审核，并按批注扩展 γ-soft→rigid/stable-triaxial transition 的分层证据链。
- 2026-08-04：每周自测保留 GSD-SYN-1 至 8 的审核历史；用户随后完成 GSD-SYN-9 targeted review，接受 `131Ce` 寿命约束 E2 集体性/core response、γ-softness 仍由 TRS/作者解释支持的分层。

## Day19量化审计：能谱交错与电磁分支双重分水岭定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_gamma_soft_rigid_watershed_audit.py` 的 16 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/gamma-soft-rigid-watershed-result-041.json`，核准了区分 $\gamma$-软核与刚性三轴核的双重分水岭判据：
1. **能级交错参数 $S(4,3,2)$ 的正负相变**：Zamfir-Casten 能量交错指标在 Wilets-Jean $\gamma$-软核极限下为 $-2.00$（形成 $(3^+, 4^+)$ 成对），在 Davydov-Filippov 刚性转子极限下为 $+1.67$（形成 $(2^+, 3^+)$ 成对）。对 A≈130 区域 7 个代表性 Xe 与 Ba 核的能级审计表明，实测值全部位于 $[-1.01, -0.42]$ 负值区间，无一落入刚性正值区，从能谱排布上确立了其普遍的 $\gamma$-软性本底；
2. **电磁跃迁比的 $\Delta\tau = 2$ 禁戒压制**：在 Wilets-Jean 极限下，由 $O(6)$ 动力学对称性导出 $B(E2; 2_2^+ \to 0_1^+) \equiv 0$；而在刚性转子 $\gamma = 30^\circ$ 下，该分支比预测为 $2/11 \approx 0.1818$。实测 $^{128}\text{Xe}$ 分支比仅为 $0.023(5)$，较刚性转子预测值受压制达 $7.9$ 倍，以电磁矩阵元独立证实了准 $O(6)$ 软性对称性；
3. **奇偶核集体激发的结构根源**：双重判据从根本上揭示了 A≈130 奇 $A$ 核中横向摇摆与静态手征难以稳定存在的核心机理：偶偶核芯缺少陡峭的刚性三轴势阱，当奇准粒子在旋转驱动下发生科里奥利单粒子对齐时，核芯极易发生软性形变调整，使弱进动模式被单粒子重排（如倾斜进动 TiP）所主导。


## checkpoint105：时间测量方法与gamma软性/刚性诊断边界整合

**checkpoint108撤回旧普适形状裁决。** [[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-D19-22/23保存作者weakvibrator解释和有限IBM charge/input谱系，B4/2=1.86(16)不等独立证明O6/gamma softness；vibrator2和finiteIBM U5 1.5属于不同参照。[[regis-2011-fast-timing-labr3]] RG11-D19-15/21的B4/2约1.335与X5比较是作者结合模型/多点解释，不由任意.20差阈值排他裁定shape。

旧Sm斜率−2.18/两分段均值及S432/2/11未在本checkpoint从原Hamiltonian或原表新核，不能被硬填常数通过认证；停止尺度不变要[[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-19所述条件，不普适电子-only。[[suzuki-2008-lifetimes-103rh-104rh]] SU08-D19-8只给实验门合同，不支持上述shape公式。原human-reviewed metadata/既有早期审核条目保持；本新增修订为Codex自审。

## Day22 checkpoint108：γ-soft不是模式禁止条件，PES不定标全部M1

[[frauendorf-2024-wobbling-review]] F24-D22-R108-1讨论同一TPSM输入同时出现core的softness交错特征与odd核的wobbling支持预测；这是作者模型解释，不能将fixedbasisγ独立当实验刚度，也不能从邻芯softness普适否定wobbling。其对IBFM能谱趋势的反驳与实际混合比冲突是不同层级，原privateenergy/producer未取得。

[[nomura-2022-questioning-wobbling-ibfm]] NOM22-D22-R108-1/2补充为什么整磁性向量重要：受限同质子/中子变形PES不能独立定Majorana强度，M1仍可受未确定项影响；该模型已有exchange term，不能称完全没有费米交换处理。127Xe的平均场v²=.4317使动力学/E2费米子prefactor较小、exchange权重接近最大，但这些不是实际B或普适M1零条件。额外磁性/混合对称响应能约束模型中静态PES不识别的方向；需实际数据/完整模型计算，不用固定γ宽度或M1百分比作跨核充要门。needs_review: true。
