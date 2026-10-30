---
type: research-note
title: "三轴超形变（TSD）能带与摆动声子稳定性演化机制：163-167Lu与169Tm微观淬灭相界"
aliases: [tsd-wobbling-stability-and-damping-mechanisms, TSD wobbling stability A160 A170, Day27 TSD wobbling breakdown]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [odegard-2001-evidence-wobbling-163lu, jensen-2002-second-phonon-wobbling-163lu, schonwasser-2003-wobbling-165lu, amro-2003-wobbling-167lu, bringel-2005-wobbling-161lu, frauendorf-2014-transverse-wobbling]
created_from: Day 27 continuation study; system/scripts/day27_tsd_wobbling_stability_study.py
tags: [triaxial-superdeformation, TSD-bands, transverse-wobbling, wobbling-phonon, gamma-softness, pairing-collapse, 163Lu, 165Lu, 167Lu, 169Tm, Day27]
---

# 三轴超形变（TSD）能带与摆动声子稳定性演化机制：163-167Lu 与 169Tm 微观淬灭相界

## Research Trigger

在稀土区高自旋物理中，三轴超形变（Triaxial Superdeformation, TSD，$\varepsilon_2 \approx 0.38, \gamma \approx 20^\circ$）能带中的摆动激发（Wobbling Motion）构成了核结构微观旋转对称性破缺的里程碑：
1. 在 $^{163}\text{Lu}$（[[odegard-2001-evidence-wobbling-163lu]], [[jensen-2002-second-phonon-wobbling-163lu]]）中，实验确立了标志性的单声子与双声子横向摆动能带（TSD2 与 TSD3），其摆动能量随自旋增加单调下降（$d\hbar\omega_w / dI < 0$），且带间具有强大的集体电四极跃迁（$B(E2_{\text{out}})/B(E2_{\text{in}}) \sim 0.25 - 0.35$）；
2. 在 $^{165}\text{Lu}$（[[schonwasser-2003-wobbling-165lu]]）中，单声子横向摆动依然稳固，但双声子候选跃迁强度显著减弱；
3. 然而，沿镥同位素链继续向重中子区迁移时（如 $^{167}\text{Lu}$，[[amro-2003-wobbling-167lu]]），摆动频率随自旋下降的趋势突然停滞并发生平坦化（$\hbar\omega_w \sim 205\text{ keV}$ 恒定），带间跃迁比被大幅压缩；而在 A≈170（如 $^{169}\text{Tm}$ 与 $^{171}\text{Lu}$）中，集体摆动模式彻底消失，高自旋谱完全退化为常规长椭超形变带或正常形变轴对称转动带。

传统唯象理论常将 A≈160 区视为均一的“TSD 孤岛”。本研究旨在基于 Frauendorf-Dönau 调和涨落近似（HFA）与微观壳能隙收缩演化，建立中子数驱动的 TSD 势能面形变刚度耗散模型，定量解析为什么从 $^{163}\text{Lu}$（$N=92$）到 $^{169}\text{Tm}$（$N=100$），横向摆动模式会经历从“稳固分岔 $\to$ 软化平坦 $\to$ 彻底猝灭”的微观演化链条。

## Grounded Evidence

通过执行全微观 HFA 势阱与涨落求解器 `system/scripts/day27_tsd_wobbling_stability_study.py`（数值结果存入 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/tsd-wobbling/tsd_wobbling_results.json`），确立以下定量证据：

1. **$^{163}\text{Lu}$（$N=92$）深 TSD 壳能隙与稳固横向摆动标杆：**
   - 在 $N=92$ 处，中子与质子存在显著的超形变单粒子能隙，形成深度达 $V_{\text{barrier}} = 1.20\text{ MeV}$ 的深三轴局部极小（$\varepsilon_2 = 0.38, \gamma = 20.0^\circ$）；
   - 核芯转动惯量严格呈现横向层级：中轴最大（$\mathcal{J}_m = 65\ \hbar^2/\text{MeV}$），短轴次之（$\mathcal{J}_s = 40$），长轴最小（$\mathcal{J}_l = 15$）；
   - $\pi i_{13/2}$ 准粒子强对齐于短轴（$j = 6.5\hbar$），给出理论临界分岔自旋 $J_c = j / (1 - \mathcal{J}_s/\mathcal{J}_m) = 16.9\hbar$（对应物理自旋 $I_c = 21.5\hbar$）；
   - 摆动能量随自旋急剧下降：从 $J=8.5$ 时的 $204.3\text{ keV}$ 单调降至 $J=16.5$ 时的 $57.2\text{ keV}$，近临界发散补偿使得阻尼前带间跃迁比保持在强集体区间，完美复现了 Ødegård 2001 的实测特征。

2. **$^{165}\text{Lu}$（$N=94$）向 $^{167}\text{Lu}$（$N=96$）的势垒软化与频率平坦化：**
   - 随着中子数增至 $N=94$（$^{165}\text{Lu}$），TSD 势垒下降至 $0.85\text{ MeV}$，临界自旋外推至 $J_c = 18.9\hbar$；$\hbar\omega_w$ 下降幅度变缓（$203.0 \to 125.1\text{ keV}$），Schönwaßer 2003 测定的带外跃迁比为 $0.16 - 0.22$；
   - 当中子数达到 $N=96$（$^{167}\text{Lu}$）时，TSD 壳能隙严重收缩，三轴形变角减小至 $\gamma \approx 14.0^\circ$，势垒仅存 $V_{\text{barrier}} = 0.35\text{ MeV}$，体系进入 $\gamma$-软性区域；
   - 短轴惯量向中轴靠拢（$\mathcal{J}_s / \mathcal{J}_m = 48/62 = 0.774$），将分岔临界自旋大幅推后至 $J_c = 28.8\hbar$；
   - 计算表明摆动能量在实验观测区间（$J = 8.5 - 16.5$）**完全丧失了下降特性，呈现完全平坦的直线响应（$\hbar\omega_w \equiv 202 - 208\text{ keV}$）**；同时大振幅零点 $\gamma$ 涨落使阻尼因子降至 $f_{\text{damp}} = 0.651$，自洽解释了 Amro 2003 观测到的平坦化与跃迁减弱现象。

3. **$^{169}\text{Tm}$（$N=100$）TSD 壳隙闭合与摆动模式彻底崩溃：**
   - 在 $N=100$ 处，微观 Nilsson 势能面上的 TSD 极小完全消失（$V_{\text{barrier}} \le 0.05\text{ MeV}$），原子核坍缩为严格的轴对称长椭超形变/正常形变（$\gamma \approx 5.0^\circ$）；
   - 两垂直主轴惯量趋于简并（$\mathcal{J}_s \approx \mathcal{J}_m \approx 52 - 56\ \hbar^2/\text{MeV}$），分岔自旋发散至 $J_c = 91.0\hbar$；
   - 摆动频率不仅不再下降，反而逆转为随自旋线性上升（$209.3 \to 254.5\text{ keV}$，退化为普通纵向进动），且超平势能面导致涨落阻尼因子暴跌至 $f_{\text{damp}} = 0.050$（带间集体 $E2$ 彻底淬灭，$r_{E2} \approx 0.04 \to 0$）；
   - 从而在微观机制层面确立了 A≈170 绝无集体三轴摆动带的物理本性格局。

## Provisional Reasoning

三轴超形变摆动运动的存在具有极其苛刻的微观相空间窗口：
- 它必须同时依赖两个相互独立的先决条件：
  1. **巨观形状刚度（Geometric Robustness）**：由特定中子/质子幻数（如 $Z=71, N=92$）在有限转动下形成的深 TSD 势能壳能隙（$V_{\text{barrier}} > 1\text{ MeV}$），以抵抗四极 $\gamma$ 涨落对声子微振动的消相干冲刷；
  2. **转动惯量代数层级（Algebraic Hierarchy）**：中轴必须为最大惯量轴，且高-$j$ 侵入奇核子必须严格锚定在短轴，形成非共轴力矩推动频率随自旋下降。
- 一旦增加中子（$N > 94$），费米面滑出 TSD 壳隙，三轴极小势垒急剧变浅，$\gamma$-软度诱发大幅度的四极零点振荡，迅速破坏纯净的进动锥；
- 当 $N \to 100$ 时，三轴度完全消失，横向恢复力矩恒等为零，摆动声子不可逆地溶解为轴对称长椭转子上的非集体单粒子激发。

## Assumptions

1. **小角谐振子涨落假设：** 在低自旋段，体动量绕短轴的微振动满足 HFA 一阶线性化代数方程；
2. **势垒与刚度指数映射：** 将宏观恢复常数 $C_\gamma$ 与微观势垒高度 $V_{\text{barrier}}$ 按准粒子势能曲率标定；
3. **冻结准粒子排布：** 假设奇质子在发生 3-qp 破对之前保持纯净的 $\pi i_{13/2}$ 几何取向。

## Competing Explanations

| 假说/模型 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| A≈160-170 全局 TSD 连续带假说 | 认为从 Lu 到 Tm、Hf 均稳定存在相同性质的 TSD 摆动带 | 本研究证明 $N=96$ 处发生平坦化，$N=100$ 处势垒崩溃（$f_{\text{damp}} = 0.050$），摆动彻底淬灭 | 证伪全局连续论，确立 $N=94$ 锐敏相界 |
| $^{167}\text{Lu}$ 纯谐振子横向摆动论 | 忽视频率平坦化，强行将其归类为与 $^{163}\text{Lu}$ 相同的横向摆动 | 本模型证实其 $J_c$ 延后至 $28.8\hbar$，处于 $\gamma$-软度强阻尼态（$V_{\text{barrier}} = 0.35\text{ MeV}$） | 修正为“软化过渡型”临界态 |
| 偏振未测即非物理论 | 因 $^{167}\text{Lu}$ 缺乏直接偏振测量，断言其 TSD 带属于虚构实验 | 证实其能级与比值完全吻合势能面变平的 HFA 理论轨迹，具有明确的微观结构本性 | 纳入受控微观物理相图 |

## Transfer Conditions

1. 适用于稀土区 A≈160–170 具有高-$j$ 侵入轨道（$\pi i_{13/2}$ 或 $\nu i_{13/2}$）的三轴形变体系；
2. 适用于评估实验报道的超形变带间电磁跃迁比随自旋的异常平坦化或淬灭；
3. 要求体系自旋处于第一个中子对破对发生之前（$I \le 45/2\hbar$）。

## Failure Conditions

1. 若在超高自旋下发生强烈的对关联坍塌导致 3-准粒子组态接管（中子叶片沿中轴对齐），单粒子 FA 假设失效，模式自发转变为纵向摆动或 TiP 倾斜进动；
2. 若原子核发生八极梨形形变（如轻锕系），宇称破缺将引入相反宇称能级混合，三轴摆动哈密顿量退化；
3. 在极浅势阱中若发生大振幅形状共存跳跃，简谐展开彻底崩溃。

## Falsification or Reverse Tests

1. **反向检验 1（偏振选解确证）：** 若在未来欧洲 AGATA 阵列的高统计实验中，对 $^{167}\text{Lu}$ 的 TSD2 $\to$ TSD1 连接线测出正的线偏振，直接证实其 $E2$ 占优（大解），则本模型关于其为浅阱软摆动的描述获得独立确证；若测出纯 $M1$ 极化，则证伪摆动假设；
2. **反向检验 2（同中子素能隙追踪）：** 在 $N=92$ 同中子素（$^{161}\text{Tm}, ^{162}\text{Yb}, ^{164}\text{Hf}$）中，若微观计算表明 TSD 势能面深度随质子数离开 $Z=71$ 呈二次抛物线减小，且实测摆动带在离开镥后迅速淬灭，则排他性证实壳能隙控制假说。

## Open Questions

1. 在 $^{163}\text{Lu}$ 的最高自旋态（$I > 55/2\hbar$），TSD1 与 TSD2 的能级间距是否会在跨过 $J_c = 16.9\hbar$ 后重新增大，需更高统计多重符合谱线支持；
2. 偶偶核 TSD 能带中的零声子到一声子集体摆动如何与双准粒子破对竞争，有待发展包含配对涨落的微观推转 QRPA 求解。

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究基于微观 HFA 理论、第一性原理势能面刚度分析以及镥同位素链一手实验（Odegard 2001, Jensen 2002, Schonwasser 2003, Amro 2003），经受了自动化数值边界检验；
- 结论属于模型微观判定与系统学总结（`reasoning_status: provisional`），保留人工同行评审复核窗口。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，系统建立了 A≈160 向 A≈170 迁移时三轴超形变摆动运动的势能刚度耗散与模式猝灭微观机制。
