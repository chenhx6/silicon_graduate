---
type: research-note
title: "超重核八极不稳定性、第二裂变势垒与自发裂变半衰期调控"
aliases: [superheavy octupole fission barrier lowering, beta3 WKB superheavy, 254No 256Rf octupole]
created: 2026-10-29
updated: 2026-10-29
created_from: Day 26 delegated superheavy-octupole-fission-barrier study
category: research-notes
promotion_target: ""
evidence_sources: [butler-nazarewicz-1996-intrinsic-reflection-asymmetry, robledo-2010-bcp-d1s-octupole-ra-ba, warda-2011-actinide-cluster-radioactivity-gogny]
tags: [superheavy, 254No, 256Rf, octupole, beta3, fission-barrier, spontaneous-fission, WKB, toy-model, evidence-boundary]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
---

# 超重核八极不稳定性、第二裂变势垒与自发裂变半衰期调控

## Research Trigger

本轮问题是检验在 Z=100-108, N=152-162 的超重核候选区，第二裂变鞍点附近的反射不对称自由度 beta3 是否能开辟低于反射对称鞍点的路径，并把势垒变化传递到自发裂变半衰期。具体测试核素为 254No (Z=102,N=152) 和 256Rf (Z=104,N=152)。

## Grounded Evidence

- `claim_kind: contextual`, `evidence_level: direct`, `confidence: medium`, `locator: Butler-Nazarewicz RMP 68 (1996), Secs. II-VII`, `needs_review: false`: 反射变换使奇多极形变变号；费米面附近相反宇称、Delta-l=Delta-j=3 的轨道耦合可驱动八极响应。该综述讨论裂变形变与微观轨道机制，但不提供本次两枚核的数值势垒。
- `claim_kind: model-result`, `evidence_level: indirect`, `confidence: low`, `locator: Robledo 2010 and Warda-Robledo 2011 source pages`: Gogny/宏观-微观计算在锕系和邻近区域显示八极坐标可与裂变通道、颈约束和集体惯量耦合；这些来源不是 254No 或 256Rf 的直接计算，只能作为机制背景。
- `claim_kind: model-result`, `evidence_level: none`, `confidence: low`, `locator: worker CSV/JSON`: toy PES 给出 254No 的 BfII 从 6.200 降至 5.066 MeV（降低 1.134 MeV），S/hbar 从 8.199 降至 5.372，Delta-log10(Tsf)=-2.456。256Rf 从 6.550 降至 5.105 MeV（降低 1.445 MeV），S/hbar 从 8.432 降至 4.103，Delta-log10(Tsf)=-3.760。这是参数化计算结果，不是实验事实。

求解器使用偶函数 Landau 形式 V(q,beta3)=Vsym(q)+a3(q)beta3^2+c3 beta3^4，并在 a3<0 时取 beta3*=sqrt[-a3/(2c3)]。沿路径计算 S/hbar=integral sqrt[2M(s)(V(s)-E0)] ds，其中 M 以 hbar^2/MeV 给出、E0=0.80 MeV。半衰期代理为 Tsf=(ln2/nu)exp(2S/hbar)，nu=10^20 s^-1。

## Provisional Reasoning

当外鞍点附近的 a3(q) 变负时，beta3=0 的径迹在局部失稳并分岔为 +/-beta3 两个等价谷。路径降低来自壳修正代理项，而不是由反射对称性本身保证。由于 WKB 指数依赖作用量，约 1-1.5 MeV 的势垒降低可以对应 2.5-3.8 个十进数量级的 toy 半衰期缩短；实际数值会同时受惯量、配对和零点能影响。

## Assumptions

1. q 是单一无量纲伸长代理；真实 PES 还应包括 beta2、beta4、gamma、颈变量和可能的非轴八极分量。
2. Mqq 与 M33 是平滑的现象学惯量，未由 ATDHFB 或 GCM 计算。
3. 反射不对称路径在每个 q 上绝热地取 Landau 极小；未求解动力学路径或有限温度耗散。
4. E0=0.80 MeV 和 assault frequency 仅用于相对比较。

## Competing Explanations

- 三轴形变可能主导第一鞍点软化，而非 beta3 主导外鞍点；本模型没有 gamma 自由度，不能区分两者。
- 壳修正、配对塌缩或惯量增大可能抵消势能降低；仅观察到寿命变化不能反推出静态梨形。
- 对称裂变与非对称质量分裂也可能由颈形成、beta4 或组态依赖的壳效应控制；beta3 只是其中一个通道。

## Transfer Conditions

该 toy 结果只可迁移为参数敏感性尺度：当自洽计算在外鞍点找到负的八极曲率、连续的 beta3>0 谷，并给出相应惯量张量时，WKB 指数放大效应仍应存在。不能把本次 1.134/1.445 MeV 直接外推到其它核素或当作实验系统学。

## Failure Conditions

若真实二维或多维 PES 中 a3(q) 始终为正、beta3 谷只在基态而不在外鞍点出现，或惯量沿不对称路径显著增大，则本模型的寿命缩短结论失效。若存在低于第二鞍点的第三势阱，单一穿透段也不足以描述总半衰期。

## Falsification or Reverse Tests

1. 用同一 EDF 对 254No、256Rf 做约束 HFB/ATDHFB 二维 (beta2,beta3) 扫描；若外鞍点 beta3=0 曲率为正且最低路径仍反射对称，则否定本机制在这两核中的主导地位。
2. 用自洽惯量替换 toy 惯量并重算作用量；若 Delta-S 反号，说明势能降低被动力学质量抵消。
3. 比较裂变碎片质量不对称性、同位素链寿命和鞍点附近宇称相关观测；没有与 beta3 谷一致的独立迹象时，不应把寿命凹陷归因于八极形变。

## Open Questions

- N=152 区域真实第二鞍点的八极曲率、beta4 耦合和非轴自由度是否足以产生 1-2.5 MeV 的降低？
- 配对、准粒子阻塞和自发裂变的耗散动力学如何改变 S？
- 254No 与 256Rf 是否存在可区分的第二势垒/第三势阱实验指纹？

## Human Review

页面为 review_status=unreviewed、reasoning_status=provisional。直接来源没有被本轮重新深读到能支持两枚目标核的定量势垒；数值结果已完成代码自审、量纲说明和对称极限检查，但仍需人工核对来源 locator 与真实 EDF 文献。

## Promotion or Rejection History

2026-10-29：由 Day 26 任务建立。toy 计算保留为可复现敏感性工件；在获得 254No/256Rf 的直接多维自洽计算前，不晋升为定量模型结论。

## Reproducible Outputs

- [worker README](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/superheavy-octupole-fission-barrier/README.md)
- [Python solver](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/superheavy-octupole-fission-barrier/superheavy_octupole_wkb.py)
- [scan summary](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/superheavy-octupole-fission-barrier/scan_summary.json)
- [vector figure](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/superheavy-octupole-fission-barrier/barrier_and_beta3.svg)
