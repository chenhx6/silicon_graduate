---
type: research-note
title: "轻锕系八极形变与高自旋 backbending 阻尼的微观机制"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [actinide-octupole-backbending-damping, 锕系八极回弯阻尼机制]
tags: [actinides, octupole, backbending, cranking, pairing, high-spin]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: Day26 directed study of octupole induced damping of high-spin crossings
evidence_sources: [odd-a-actinide-parity-doublet-direct-e3-transitions-angular-coupling, cns-high-spin-octupole-phase-transitions-in-neutron-rich-ba, butler-nazarewicz-1996-intrinsic-reflection-asymmetry]
---

# 轻锕系八极形变与高自旋 backbending 阻尼的微观机制

## Research Trigger

本页检验一个可证伪的机制假设：在 `220–228Th`、`222–228Ra` 一带，有限的反射不对称坐标 `β3` 使 `Δl=Δj=3` 的粒子—空穴轨道发生八极混合，并将原本集中在窄频率区的 aligned two-quasiparticle crossing 展宽为平滑 upbending。

## Grounded Evidence

本页检验一个可证伪的机制假设：在 `220–228Th`、`222–228Ra` 一带，有限的反射不对称坐标 `β3` 使 `Δl=Δj=3` 的粒子—空穴轨道发生八极混合，并将原本集中在窄频率区的 aligned two-quasiparticle crossing 展宽为平滑 upbending。相关轨道对写作 `π(1f7/2,1i13/2)` 与 `ν(1g9/2,1j15/2)`。奇 A 直接 E3 笔记提供 `Q30`、CG 几何和 Coriolis 边界；Ba 的 CNS 笔记则提醒离心八极稳定化与高自旋 alignment 淬灭是竞争机制。

现有本地证据支持“八极耦合可以打开避免交叉并改变高自旋响应”的理论路线，但没有为上述完整 Th/Ra 同位素链提供逐线 `J^(2)` 与 blocked-HFB 参数。因此本页的扫描是可复现的机制示意，不是实验拟合或自洽 Cranked-HFB/CRMF 预测。`β3`、配对参数和 `V3` 都保留为显式控制量。

## Provisional Reasoning

### 1. 极小推转哈密顿量

以配对参考构型 `A` 和已对齐两准粒子构型 `B` 为基底，在推转频率 `ω` 下取

```text
H'(ω,β3) = [ E_A(ω)          V_pair(β3)+V3 β3 ]
            [ V_pair(β3)+V3 β3       E_B(ω)   ]

E_k(ω) = e_k - 1/2 J_k ω² - i_k ω,
Δ_eff(β3) = Δ0/(1 + 6 β3²).
```

这里 `iA=8`, `iB=14`, `JA=22`, `JB=30`（单位分别为 `ħ` 和 `ħ²/MeV`），`eB-eA=1.20 MeV`。微小的 `V_pair=0.030(Δ_eff/Δ0)^2 MeV` 代表残余配对混合；`V3β3` 代表八极场在两组 `Δl=Δj=3` 轨道间的矩阵元。选择 `Δ_eff` 随 `β3` 下降，是题设“八极混合削弱单极配对”的显式参数化；阻尼峰的主要来源仍是 `V3β3` 增大的 avoided-crossing gap，二者没有被混成同一个效应。

从最低 Routhian 得到

```text
I(ω) = -dE'_yrast/d(ħω),     J^(2)(ω) = dI/d(ħω).
```

导数在 `0≤ħω≤0.8 MeV`、801 点均匀网格上用二阶中心差分。代码、扫描表和图位于：

`outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/actinide-backbending-damping/`

运行：

```bash
python3 solve_backbending_damping.py
```

### 2. 数值扫描结果

| `β3` | crossing gap (MeV) | peak `J^(2)` (`ħ²/MeV`) | peak width proxy (MeV) |
|---:|---:|---:|---:|
| 0.00 | 0.060 | 530.2 | 0.008 |
| 0.03 | 0.287 | 133.5 | 0.038 |
| 0.06 | 0.513 | 86.3 | 0.077 |
| 0.10 | 0.813 | 64.1 | 0.139 |
| 0.15 | 1.187 | 52.3 | 0.238 |

`β3=0` 的小残余耦合保留了清晰的 backbending 峰；`β3=0.15` 时八极矩阵元把交叉间隙增大约 20 倍，alignment weight 在更宽的频率窗内转移，`J^(2)` 峰高下降约 90%，而宽度约扩大 30 倍。这就是本模型定义的 backbending damping。配对间隙从 `0.820` 降至 `0.722 MeV`（约 12%），所以模型同时显示配对削弱与八极展宽，但不能由该玩具模型单独判定真实核中哪一项占主导。

### 3. 微观物理机制解析

1. `β3=0` 时，正负宇称轨道对不混合；两准粒子组态的角动量在接近交叉频率时集中转移，形成窄的 `J^(2)` 增强。
2. `β3>0` 时，`Q30` 场连接 `Δl=Δj=3` 的轨道。质子和中子单粒子波函数同时含有低、高 `j` 成分，因而 aligned angular momentum 不再是单一组态的突变，交叉变成 avoided crossing。
3. 八极场也改变配对基底中的准粒子能量；本模型用 `Δ_eff` 的下降表示配对削弱，用独立的 `V3β3` 表示相干混合，避免把“配对减弱”直接等同于“阻尼增强”。
4. 与 Ba 笔记的竞争解释一致，高自旋的平滑化也可能由普通 configuration crossing、带标记变化、`γ`/`β4` 响应或配对塌缩造成；观测到平滑 `J^(2)` 不能排他证明静态梨形。

## Assumptions

- 这是二构型 cranking surrogate，不含完整 proton/neutron Woods–Saxon 或 Nilsson spectrum、粒子数投影、宇称投影、blocking、time-odd 场和自洽形变极小化。
- `V3`、`Δ0`、惯量和构型能差是示意输入；不得当作 `220–228Th` 或 `222–228Ra` 的测量值。

## Competing Explanations

与 Ba 笔记的竞争解释一致，高自旋的平滑化也可能由普通 configuration crossing、带标记变化、`γ`/`β4` 响应或配对塌缩造成；观测到平滑 `J^(2)` 不能排他证明静态梨形。

## Transfer Conditions

适用于费米面处于满足 `Δl=Δj=3` 轨道对的轻锕系与重钡核区；不得直接迁移至强刚性四极变形转子区。

## Failure Conditions

- 真实体系若 `β3` 是大振幅软振动而非静态内禀形变，需在 GCM/QRPA 中对 `β3` 量子涨落平均，单一 `β3=0.15` 曲线不适用。
- 若完整 blocked-HFB 计算显示八极混合增强而 `J^(2)` 峰反而变尖，说明本页的参数化耦合或构型顺序不适用。

- 这是二构型 cranking surrogate，不含完整 proton/neutron Woods–Saxon 或 Nilsson spectrum、粒子数投影、宇称投影、blocking、time-odd 场和自洽形变极小化。
- `V3`、`Δ0`、惯量和构型能差是示意输入；不得当作 `220–228Th` 或 `222–228Ra` 的测量值。
- 真实体系若 `β3` 是大振幅软振动而非静态内禀形变，需在 GCM/QRPA 中对 `β3` 量子涨落平均，单一 `β3=0.15` 曲线不适用。
- 若完整 blocked-HFB 计算显示八极混合增强而 `J^(2)` 峰反而变尖，说明本页的参数化耦合或构型顺序不适用。

## Falsification or Reverse Tests

应在统一的 blocked-cranked-HFB 或 particle–rotor 模型中逐频率跟踪上述四条轨道的 Routhian、占据、pairing tensor、`J^(1)`, `J^(2)` 和 E3 矩阵元；分别运行 `β3=0`、固定 `β3`、动态 `β3` 和 `V3=0` 对照。实验上需要同一带系的高自旋能级、寿命、`B(E2)`/`B(E3)` 和 alignment，同时检查交错宇称位移是否与 `J^(2)` 展宽在同一频率区出现。只有这些联合检验成立，才能把本页的机制从 provisional 提升为核素特定结论。

## Open Questions

- 在更高角动量下，Coriolis 力能否克服八极刚度恢复回弯？
- 质子与中子八极驱动轨道对的干涉相位如何微观定域？

## Human Review

本页为自主研学计算，保持 unreviewed。

## Promotion or Rejection History

- 2026-10-29: 完成轻锕系八极回弯阻尼微观两构型推转模型与全网格求解。

## Reproducibility

- `solve_backbending_damping.py`: Hamiltonian、差分、CSV/JSON 和 SVG/PNG 输出。
- `scan.csv`: 五个 `β3` 值的逐频率结果。
- `scan.json`: 参数、轨道对、摘要和证据边界。
- `backbending_damping.svg`, `backbending_damping.png`: `J^(2)` 与 `I(ω)` 扫描图。

`review_status: unreviewed`；本页保留直接来源、模型解释和本任务推断的证据分层。
