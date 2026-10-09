---
type: learning-daily
graph-excluded: true
created: 2026-10-08
updated: 2026-10-09
---

# 2026-10-08 DAY9 — B(E2)、B(M1)、约化矩阵元与强度比

## Run state

- run_id: `2026-10-08-day-09-01`; run_date: `2026-10-08`; day_index: `9`; timezone: `Asia/Shanghai`
- schedule_id: `wiki-daily-learning`; session mode: `new-session-per-run`
- session_id: `01a11a87-45cf-7781-a014-f992aafb49e2`
- resume_command: `codex resume 01a11a87-45cf-7781-a014-f992aafb49e2 -C /workspace/wiki -s danger-full-access -a never`
- status at this continuation: **Day9 card complete; normal runner receipt remains `failed-verification` after same-session writer-lock conflicts. The interactive session remains active; the run-local clock had stopped for Farmer manual attention and has since been resumed against this same receipt/thread.**
- hard research deadline: `2026-10-09T15:00:00+08:00`; closeout window: 15:00–16:00.
- latest Runtime snapshot: `2026-10-09T15:12:00+08:00`; research cutoff reached at `2026-10-09T15:00:00+08:00`; closeout only; Day9 credit awaits normal runner gates; Day10 remains partial and Day11 unopened.
- course state before run: `next_day_index=9`, `completed_day_count=8`. State is not advanced in this report; only the normal runner may update it after final closeout checks.
- completed_day_indices: [9]
- partial_day_indices: [10]
- Day 9 card audit: complete

### Day 9 card completion audit

| Day-matrix deliverable | Evidence locator / artifact | Status |
|---|---|---|
| 来源前回忆并标明 priming，之后与定义核对 | [recall-record.md](20261008-DAY9-be2-bm1-reduced-matrix-elements-strengths-run-01/recall-record.md)；LKH82 printed p.121 / PDF p.3, Eqs.2.1–2.3a | complete |
| 读取 lifetime synthesis、MU08，并回到原表和率/算符归一 | [MU08 source](../../knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md) MU08-4/5/9/10；printed 034311-3/Table I、034311-4/Table II；LKH82 printed p.121, Eqs.2.2–2.3a | complete |
| 独立核验 I=18、Ex=6711.4 的三支及 τ，并重算一条条件 B(E2) 输入链 | [day9-input-chain.json](20261008-DAY9-be2-bm1-reduced-matrix-elements-strengths-run-01/day9-input-chain.json)；本报告输入—公式—输出—误差表 | complete |
| 检查 branching basis、辐射分数、IC/E0、feeding、stopping、误差协方差与派生量依赖 | 本报告 “Counter-evidence and missing companion observables”；MU08 printed 034311-3 / PDF p.3 and 034311-5 / PDF p.5 | complete |
| 将可复用的引用身份/方法边界写入 canonical knowledge，保留 review 状态 | [MU08 source](../../knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md) MU08-10；唯一 `knowledge-writeback` block | complete |

本卡交付已完成；此前已完成 Day10 限定预习的现有证据核算。当前不足 90 分钟，只结束现有分析与准备收束；Day9 卡完成本身不构成当日 schedule closeout。

## Candidate pool and selection

| Candidate | Information value | Decision |
|---|---|---|
| MU08 Band 1 I18: lifetime → three branches → B/RME | 可直接核验一条完整数值链，并辨别 printed branching ratio 是否等于每次母态衰变的 photon probability | 已完成有条件 L2 重构；原文没有给出 branch denominator 或完整 IC ledger，保留多个 forward case |
| LKH82 p.121 rate/operator normalization | 可排除 mean/half-life、`2Ji+1` 与单位换算混淆 | 已回原图核验 Eqs.2.2–2.3a，并由物理常数重新算单位系数 |
| MU08 Ref.[16] branching extraction procedure | 可能限制 branch/IC basis 解释 | 已从 APS 官方 endpoint 获取并定向阅读 Chiara 全文；其 partial τ 使用 fitted level τ、observed branch ratios 与 IC，但未给 MU08 的绝对 photon-per-parent ledger；纯 M1 与未观测 E2 crossover 处理仍是 Chiara 文章自己的假设 |
| Day10: 电磁比值与集体模式判别 | 选定预习时距截止超过 120 分钟；MU07 有可量化 interband 点，Suzuki 提供寿命分解 comparison，LV19 可区分候选 E2 line class | 已核对 MU07 五个同自旋 quotient、四个图估点；以 `105Ag` configuration mixing 和 `103,104Rh` 的 E2-driven ratio staggering补充竞争解释；发现并撤回 E2-rate 单能量换算，改列两条 conditional forward paths。Qt 仍无 source-supported 唯一数值；Day10 仍 partial、不计学分、不打开 Day11 |

没有检索无关核素或扩大文献批次。Day9 branch/radiative fraction 的来源定义已到 L2 source boundary；当前 Day10 只记在 `partial_day_indices`，课程 state 不越过 Day10。

### Day10 uncredited preview (partial)

- **状态：** 仅预习一张下一日卡；`day_index` 仍为 9，Day10 不计分，也没有打开 Day11。
- `135Nd` MU07 原文 PDF 的 SHA-256 `9eccc9c2ad02cc10735d1aad0d76eb2fd8af0a4acc814bcaab8099f50e748425` 与 source page 匹配；直接重读/渲染了 printed 172501-2 / PDF p.2 Table I。该页明确说 B(M1)/B(E2) 由寿命推得，并报告 Band A/B 共同自旋 31/2−–39/2− 的 B 中心值。预览只重算这五个匹配点，没有重建整条实验线形或作者的拟合。

| Spin | Band A B(M1) / B(E2) | Band A derived quotient | Band B B(M1) / B(E2) | Band B derived quotient |
|---|---|---|---|---|
| 31/2− | `2.5(3) μN² / 0.32(3) e²b²` | `7.8125 μN²/(e²b²)` | `2.7(3) μN² / 0.28(3) e²b²` | `9.6429 μN²/(e²b²)` |
| 33/2− | `2.2(2) / 0.32(3)` | `6.8750 μN²/(e²b²)` | `2.1(2) / 0.28(3)` | `7.5000 μN²/(e²b²)` |
| 35/2− | `2.4(3) / 0.32(3)` | `7.5000 μN²/(e²b²)` | `2.2(2) / 0.28(4)` | `7.8571 μN²/(e²b²)` |
| 37/2− | `1.7(3) / 0.32(4)` | `5.3125 μN²/(e²b²)` | `1.7(2) / 0.29(4)` | `5.8621 μN²/(e²b²)` |
| 39/2− | `2.1(3) / 0.13(3)` | `16.1538 μN²/(e²b²)` | `1.9(3) / 0.11(3)` | `17.2727 μN²/(e²b²)` |

这些是 Table I 中已由寿命/branch 推得的两个不同 in-band B 值之商，不是单一跃迁的 mixing ratio `δ²`。共同母态寿命可作为共享输入，但 branch、能量与模式分解不随取比自动消失；未给 joint covariance，故不传播 quotient error。39/2 的 B(E2) 分母误差较大，中心值跳升不能单独作模式转换证据。完整的 derived ratio 表和来源回链写在 [MU07 source](../../knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md) MU07-5 与 [preview artifact](20261008-DAY9-be2-bm1-reduced-matrix-elements-strengths-run-01/day10-strength-ratio-preview.json)。

| Spin | `B(M1)_B/B(M1)_A` | `B(E2)_B/B(E2)_A` | `[B(M1)/B(E2)]_B/[B(M1)/B(E2)]_A` |
|---|---:|---:|---:|
| 31/2− | 1.0800 | 0.8750 | 1.2343 |
| 33/2− | 0.9545 | 0.8750 | 1.0909 |
| 35/2− | 0.9167 | 0.8750 | 1.0476 |
| 37/2− | 1.0000 | 0.9062 | 1.1035 |
| 39/2− | 0.9048 | 0.8462 | 1.0693 |

这是同五行 Table I 中心值的跨带商，没有 joint errors/covariance；它把相近 B 强度与 quotient 的自旋变化区分开，但不形成额外独立观测。

#### Table-I `B(M1)/B(E2)` 与同一跃迁 `δ²` 的区分

Table-I 同自旋中心商 `B(M1)/B(E2)` 的单位是 `μN²/(e²b²)`，不是无量纲 mixing ratio。LKH82 将同一已识别跃迁定义为 `δ²=Tγ(E2)/Tγ(M1)`；Krane–Steffen common-unit 式给 `δ²=[0.835 Eγ(MeV)]² × B(E2)[e²b²]/B(M1)[μN²]`。因此还需要同一初末态的跃迁能量和 M1/E2 分解，且 B 值本身不能给 signed `δ`。MU07 Table I 只按初始自旋列出 lifetime、`B(M1)`、`B(E2)`，没有逐行给出 `Eγ`、末态自旋或分支；它支持同表强度商，却不提供 transition-specific `δ²` 映射。来源定位：[MU07-11](../../knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md)；率比定义：[LKH82-1](../../knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md)。

#### 39/2− matched-spin quotient: denominator sensitivity

At 39/2− the Table-I central quotients are `2.1/0.13=16.15` for Band A and `1.9/0.11=17.27 μN²/(e²b²)`. Pairing each printed numerator endpoint (`B(M1)=2.1±0.3` or `1.9±0.3`) with denominator endpoints (`B(E2)=0.13±0.03` or `0.11±0.03`) gives rectangular sensitivity ranges of `11.25–24.0` and `11.43–27.5`. They overlap broadly, showing that the apparently high 39/2 quotients are sensitive to weak E2 denominators. This is not a confidence interval: no joint covariance or quoted-error coverage is given, and the quotients reuse Table-I inputs. Locator: [MU07-14](../../knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md).

#### 同一自旋标记的带间/带内强度比（图上估读）

分子来自 MU07 Figs.2–3 的 Band B→Band A 空心圆，分母为 Table I 同一 I 的 Band B 带内中心值。Fig.2/3 的四个 interband 点只覆盖 31/2−–37/2−；没有 39/2− 点。方括号是图中误差线端点的纵轴换算，原文未说明其统计覆盖。

| I | B(M1)_out 图估值 (μN²) | B(M1)_in Table I (μN²) | B(M1)_out/B(M1)_in | B(E2)_out 图估值 (e²b²) | B(E2)_in Table I (e²b²) | B(E2)_out/B(E2)_in |
|---|---:|---:|---:|---:|---:|---:|
| 31/2− | 0.084 [0.075–0.093] | 2.7(3) | ≈0.031 | 0.039 [0.035–0.043] | 0.28(3) | ≈0.14 |
| 33/2− | 0.119 [0.110–0.127] | 2.1(2) | ≈0.057 | 0.068 [0.063–0.073] | 0.28(3) | ≈0.24 |
| 35/2− | 0.080 [0.074–0.087] | 2.2(2) | ≈0.036 | 0.133 [0.122–0.144] | 0.28(4) | ≈0.48 |
| 37/2− | 0.189 [0.178–0.200] | 1.7(2) | ≈0.11 | 0.144 [0.136–0.153] | 0.29(4) | ≈0.50 |

#### Graph/table endpoint sensitivity (not a confidence interval)

Pairing each graph-read numerator endpoint with the quoted same-spin Band B Table-I `B±σ` denominator gives a rectangular input-sensitivity envelope. For E2 `out/in` at 31/2−–37/2− the ranges are `[0.113,0.172]`, `[0.203,0.292]`, `[0.381,0.600]`, `[0.412,0.612]`; the first two increases are separated, but the last two overlap. M1 ranges are `[0.025,0.039]`, `[0.048,0.067]`, `[0.031,0.0435]`, `[0.094,0.133]`, retaining a nonmonotonic pattern. The graph-bar coverage, numerator/denominator covariance and common DSAM systematics are unknown, so these are sensitivity envelopes, not statistical confidence intervals or independent evidence. MU07 attributes lifetime errors to χ²-fit behavior near minimum and does not provide a separate stopping/feeding systematic budget for the B-ratio plot; the endpoint ranges therefore do not bound those unreported systematics (MU07-15). Source locators: [MU07-13](../../knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md) and [MU07-15](../../knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md).

#### Zhu 2003 Ref.[8] line-identity crosswalk

Zhu et al. 2003, DOI 10.1103/PhysRevLett.91.132501, supplies the earlier Band A/B partial level scheme cited by MU07. Fig.2 maps the same initial-spin labels to candidate links:

| I | Band B→Band A link (Zhu 2003 Fig.2) | Band B in-band link (same figure) | Evidence boundary |
|---|---|---|---|
| 31/2− | 31/2−→29/2−, 648 keV in Fig.2 | 31/2−→29/2−, 226 keV | Fig.2 says 648; later p.4 DCO text says 649 |
| 33/2− | 33/2−→31/2−, 639 keV | 33/2−→31/2−, 282 keV | Scheme crosswalk |
| 35/2− | 35/2−→33/2−, 591 keV | 35/2−→33/2−, 309 keV | Scheme crosswalk |
| 37/2− | 37/2−→35/2−, (556) keV | 37/2−→35/2−, 372 keV | 556 is parenthesized/tentative in Fig.2 |

The 2007 source explicitly points to the 2003 partial scheme, but its strength plots do not print these energies. The 2003 and 2007 papers use different reactions and acquisition campaigns. This table links transition identities; the 2003 Fig.2 arrow thickness is relative intensity and contributes no extra B-strength measurement. See [ZH03-3](../../knowledge/sources/zhu-2003-135nd-composite-chiral-pair.md) and [MU07-9](../../knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md).

**Later line-class cross-check:** the 2019 Table I lists at the same initial spins separate D6→D5 candidates: 31/2− has a 648.9-keV ΔI=1 M1/E2-mixed link and an 896.8-keV ΔI=2 E2 crossover; 33/2− has 640.2-keV mixed and 931.3-keV E2 lines; 35/2− has 591.4-keV mixed and 949.6-keV E2 lines. At 37/2− it lists a 963.0-keV ΔI=2 E2 line, but no matching ΔI=1 link corresponding to historical `(556)`. This is a later-campaign transition table, not MU07 strength data; it shows why the E2 graph numerator cannot be assigned by spin alone. Locator: [LV19-9](../../knowledge/sources/lv-2019-chirality-135nd-reexamined.md).

### Conditional M1 partial photon-rate out/in (Day10 partial)

For the `B(M1)` graph points, use the candidate same-parent `ΔI=1` link energies and the same-spin Band B `ΔI=1` in-band lines. If each open-circle numerator is the M1 component, then the LKH82 rate relation gives `Γγ,out/Γγ,in=(Eout/Ein)^3 × B(M1)_out/B(M1)_in`. The 2019 table independently lists corresponding later-campaign D6→D5 ΔI=1 links at 648.9, 640.2, and 591.4 keV and D6 in-band lines at 225.8, 282.4, and 309.4 keV for 31/2−, 33/2−, and 35/2− (LV19-9); these are identity cross-checks, while the strengths below remain MU07 data.

| I | candidate ΔI=1 Eout / Ein (keV) | MU07 graph `B(M1)` out/in | conditional M1 partial photon-rate out/in |
|---|---:|---:|---:|
| 31/2− | 648 / 226 | ≈0.0311 | ≈0.73 |
| 33/2− | 639 / 282 | ≈0.0567 | ≈0.66 |
| 35/2− | 591 / 309 | ≈0.0364 | ≈0.25 |
| 37/2− | (556) / 372 | ≈0.1112 | **not evaluated** |

For 37/2− the 2003 scheme parenthesizes 556 keV. The later Table I includes a 681.0-keV 37/2−→33/2− entry, but this check has not established that it is the numerator transition behind the MU07 open-circle `B(M1)` point, so neither energy is used to calculate a rate ratio. The 648/649 label choice changes the first ratio by less than 1%. These are conditional transforms of graph-read B values, not measured branch ratios/counts; they omit IC, E2 admixture, gate/feeding and shared covariance.

Transforming the MU07-13 rectangular B out/in endpoint envelopes by the fixed candidate ΔI=1 energy factors gives M1 partial-rate endpoint envelopes `[0.59,0.91]`, `[0.56,0.78]`, `[0.22,0.30]` at 31/2−, 33/2−, 35/2−; 37/2− remains unassigned. The first two overlap and the third is lower, but the input graph bars have no stated statistical coverage and covariance/systematic errors are missing, so these are not confidence intervals or evidence for a spin-transition mechanism.

### E2 photon-rate ratio: transition identity unresolved

An E2 rate requires the E2-specific `Eγ^5` pair, but the MU07 E2 graph points are not linked to individual lines. Two explicit forward readings remain:

| I | `B(E2)` out/in | If marker is E2 component of ΔI=1 mixed link | If marker is ΔI=2 E2 crossover |
|---|---:|---:|---:|
| 31/2− | ≈0.1393 | ≈27.3 | ≈137.7 |
| 33/2− | ≈0.2429 | ≈14.5 | ≈94.7 |
| 35/2− | ≈0.4750 | ≈12.1 | ≈129.4 |
| 37/2− | ≈0.4966 | not evaluated; `(556)` is tentative | ≈58.0 |

These alternatives apply different candidate energies to the same graph B(E2) quotients and add no independent data. LV19 is a later campaign and does not identify which transition contributes to a MU07 open-circle marker. The previous single E2 column using only ΔI=1 energies is withdrawn as under-identified. Locators: LKH82-1; ZH03-3; LV19-9; MU07-8/11.

**Additional denominator premise:** all E2 numbers in this subsection also assume that the Table-I Band B `B(E2)` denominator is the E2 component of the selected adjacent-spin in-band line. MU07 does not establish this identity. Central values use `Ein=225.8,282.4,309.4,371.6 keV`; endpoint sensitivities use the historical rounded `226,282,309,372 keV`. If the denominator belongs to a different line, a displayed transform is rescaled by `(Ein,assumed/Ein,true)^5`. The two outgoing-line cases are not an exhaustive line-pair inventory or source-supported physical rate series. Locator: [MU07-10](../../knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md), using the row-identity limit [MU07-11](../../knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md).

Applying the same candidate energy factors to the rectangular endpoint envelopes in MU07-13 gives, for the mixed-link reading, `[22.1,33.7]`, `[12.2,17.5]`, `[9.7,15.3]` at 31/2−–35/2−; for the crossover reading it gives `[111.6,170.0]`, `[79.3,113.9]`, `[103.8,163.4]`, `[48.2,71.5]` at 31/2−–37/2−. The graph-bar/quoted-error coverage and joint covariance are unknown, so these are only transformed input envelopes, not confidence intervals. They show that the line-class choice materially changes the E2 photon-rate scale while leaving the source-supported graph B(E2) out/in ratios unchanged.



两个 out/in 比值分别无量纲；B(M1) 和 B(E2) 分开，不组合成一个有量纲混合指标。四个中心值显示 B(E2)_out/B(E2)_in 在该区间从约 0.14 上升到约 0.50，B(M1)_out/B(M1)_in 约为 0.03–0.11 且不单调。这是同一 DSAM 分析链中已派生强度的再派生比较，不是新增独立测量。若把图上误差线与 Table I 括号误差暂视为独立边际标准差，一阶传播的比例误差约为 B(M1)：0.005、0.007、0.004、0.015；B(E2)：0.02、0.03、0.08、0.07。这个传播仅用于量级感知：图误差线覆盖定义、分子/分母协方差和共享 lifetime/branch covariance 均未报告，不能当作论文给出的比例置信区间。 若图示 I 对应同一 Band B 初态且两项强度都使用该母态的同一 fitted lifetime τ(I)，则同一多极下该公共 τ 因子在 out/in 比值中代数消去（LKH82-1 率式）。此条件不会消掉逐支 branch/radiative fractions、不同转移能、line-specific gate/feeding 或协方差；也不表示跨自旋或跨带的停止功系统误差共模。
- MU07 printed 172501-3 / PDF p.3 Figs.2–3 的 legend 将 Band B→Band A 空心圆数据点与 TAC/RPA model curve 分开；相邻正文称 RPA wave functions 给出 interband rates，TAC 保留 intraband baseline。本 continuation 对四个空心圆数据点作矢量图纵轴估读，并用同一 I 的 Band B Table-I 带内值作分母；结果只作低精度图上估读，不把 RPA 曲线当数据。
- `128Cs` GR18 source page 给 `Iπ=9+` isomer 的 TDPAD measured `g=+0.59(1)`，Orsay 与 SUNY 两次测量一致；PRM+constrained-CDFT 将 bandhead 描述为近 planar，而不是理想 static chirality（GR18-1/3；PDF pp.1–5, Table I, Eqs.2–3, Fig.4）。这是独立的 magnetic-moment geometry observable；不能与 `B(M1)/B(E2)` 混成同一观测量。
- 已有 MU08 `136Nd` 反例显示近简并两带仍可因不同组态及 band mixing 出现相差约 2–3 倍的 `B(E2)`，所以强度相似/强度比趋势是 partner-band evidence，不是结构模式充分条件（MU08-1/2/4；PDF pp.3–6, Tables I–II, Figs.3–5）。
- MU07 与 GR18 两个现有 source 页均为 `ai-draft / review_status: unreviewed`；本次重算 GR18 五页 raw PDF SHA-256，与 source page 相同，并直接复核 PDF p.1 abstract、p.3 Table II/Fig.3、p.4–5 Fig.4 与结论；亦直接复核 MU07 raw PDF p.2 Table I 与 p.3 Figs.2–3。GR18 Fig.3 的 g=0.4/0.6 planar 端点属于 j_p=j_n=11/2、j_R=2 的简化向量构型，aplanar 值居中，不是跨核素普适判据。source page 保持 unreviewed，未改变 review status。
- Qt 是由带内 E2 强度/寿命推得、表征转动带电四极集体性的 transition quadrupole moment；它不同于 spectroscopic moment 和模型内禀矩。Singh 2016 的 source-specific rotor Eq.(1) 写作 `T(E2; I→I−2)=1.224×10^12 Eγ(MeV)^5 CG(I,K)^2 Qt(eb)^2 s−1`，Eq.(2) 对非轴/混合 K 按 K 振幅替换 CG 因子（SI16-17）。这说明换算还依赖明确跃迁、Eγ 和 K/转子矩阵元。Zhu 2003 Fig.2 maps the 43/2−→41/2− Band A 494-keV candidate line, which MU07 Fig.1 also uses as a representative line-shape fit; but MU07 Table I does not explicitly bind its 43/2 B(E2) row to that line (MU07-11), nor supply K/rotor conversion. The crosswalk narrows candidate identity but does not yield a unique source-supported numeric Qt. MU08 Table II reports B(E2) and Qt on one DSAM-derived chain and cannot supply the missing MU07 convention.

Day10 preview 的证据分层为：source-reported experimental-analysis outputs 包括 MU07 的 DSAM-fitted lifetimes 与图示带内/带间 strength points，以及 GR18 从 TDPAD precession analysis 得到的 g=+0.59(1)；MU07 Table-I B values 是作者由寿命等输入派生，五个 matched-spin quotient 和四组 digitized out/in quotient 是本次再派生；MU07 TAC in-band/RPA interband curves 与 GR18 PRM+CDFT geometry 属模型结果。GR18 raw 已直接核验，但 source 页仍为 unreviewed。MU08 的 136Nd configuration crossing/band mixing 是严肃非目标解释，但现有来源没有证明它能定量复现 MU07 的全部比值轨迹。

#### 有界模式判别卡（Day10 partial）

| 证据 / 模式层 | 直接支持什么 | 竞争解释与边界 | 来源 locator |
|---|---|---|---|
| 135Nd partner-resolved strengths | Table I 的两带带内强度相近；本次图估的 B(E2)_out/B(E2)_in 约由 0.14 升至 0.50。endpoint sensitivity 区间显示 31/2→33/2 与 33/2→35/2 分离，但 35/2 与 37/2 重叠；Zhu 2003 Fig.2 映射四个 plotted-spin link，仍仅为候选身份。| 趋势与同作者 chiral-vibration→static 解释相容，但不定位临界自旋；图误差覆盖/协方差未知，无 39/2− 带间点；556 仍为括号线，648/649 差异保留。| MU07-1; MU07-8; MU07-13; ZH03-3 |
| 135Nd 动力学解释 | MU07 用 PQTAC+RPA 描述低自旋 chiral vibration、RPA mode softening 与临界点附近的 static onset；Zhu 2003 的 3D-TAC 同样给 planar→aplanar onset near I≈19, calls it transient, and predicts a high-spin return toward planarity. These are qualitatively compatible model descriptions of the same 135Nd band pair around the onset, not independent experiment evidence.| 2003 的高自旋 return-to-planarity prediction should be retained. MU07 的局部 onset result does not prove an indefinitely persistent static regime; both results remain model-dependent and are kept separate from the two distinct experimental campaigns.| MU07-2; MU07-3; ZH03-8 |
| 非目标机制：crossing / configuration mixing | `134Pr` near-degenerate region `13<I<19` contains a Band1/Band2 crossing at `I=15–16`; the two bands also differ by about `2ħ` alignment at `I=14–18`, and a branching-based two-band mixing analysis gives `Q0,1/Q0,2=2.0(4)`. `136Nd` provides a second case where near-degenerate bands have markedly different B(E2)/Qt and are attributed to distinct configurations/band mixing. | PE06 authors use a simplified mixing analysis to infer shape difference; it is not a universal crossing signature or a direct fit to `135Nd`. MU08/PE06 are different nuclei and experiments, not a common 135Nd measurement. | PE06-1; PE06-2; MU08-2; MU08-4 |
| 非目标机制：105Ag configuration mixing | `105Ag` D/G 的能差约 70 keV、ratio-staggering 相似并满足部分手征候选指纹；原文同时指出自然宇称下无手征耦合的激发也可能造成相似性，并明确 `πg9/2⊗νh11/2(g7/2,d5/2)` 简单组态混合仍无法排除。 | 这是相似指纹非唯一性的直接反例，不证明该机制定量复现 `135Nd` 的曲线；`105Ag` 与 `135Nd` 不合并为同一实验比较。D/G 无专门 TAC 计算、寿命或绝对强度。 | TI07-11; TI07-13; TI07-14; TI07-15 |
| 候选 wobbling / signature 竞争 | wobbling 的相邻 phonon bands 预期有 collective interband E2 enhancement；实验常以 ΔI=1 connecting links predominantly E2 来区别 M1-dominated signature partner。 | MU07 E2 open-circle trend不能单独判为wobbling信号：它没有逐线身份、mixing ratio/δ，且LV19后续表显示同初始spin同时有ΔI=1 mixed与ΔI=2 E2 links；本计算的两种rate forward亦不唯一。`135Nd` 的MU07模型比较主张chiral vibration→static，不等于已与wobbling同数据比较。 | F24-3; LV21-11; MU07-8/11; LV19-9 |
| 实验控制：131Xe low-|δ| signature partner | `131Xe` selected yrast ΔI=1 links 的 small `|δ|` 和 M1-dominated character 被作者用于排除该序列的 wobbling 解释，转而支持 unfavoured signature-partner reading。 | 这是不同核素的测量/作者解释，不能裁决 `135Nd`；它显示 transition-resolved mixing ratio / E2 fraction 是判别必要量，而 MU07 graph markers 缺少逐线 δ。 | C23-2; C23-3; C23-7 |
| 同核 different-band control：135Nd D1/TiP1/TiP2 | 后续 JUROGAM II 实验给 TiP1→D1 的 `δ=-0.32(5), -0.48(14)`、E2 fractions `9.3%,18.7%`，TiP2→TiP1 `δ=-0.26(8)`、E2 `6.3%`；作者认为这些连接以 M1 为主，不满足其 wobbling predominant-E2 criterion，并采用 tilted-precession reading。 | 这是同核但不同能带、不同实验 campaign 的测量；它不能给 MU07 D5/D6 赋模式，也不能填补 MU07 图 marker 的线身份。 | LV21-9; LV21-10; LV21-11; LV21-17 |
| 分子/分母分解：103,104Rh lifetime comparison | Suzuki 的绝对强度结果显示 measured `B(M1)` 随自旋下降，而 weak odd-even staggering 在 `B(E2)`；作者据此将早先 `B(M1)/B(E2)` staggering 归于 E2 denominator。 | 仅测每对候选中的一个成员；`B(M1)` 假定 pure M1 且能量/分支从先前实验导入。`B(E2)` staggering 起因未解，且该 A≈100 结果不等于 135Nd 的独立 partner test。 | SU08-6; SU08-7; SU08-8; SU08-13 |
| 几何伴随量：128Cs g factor | TDPAD 给出 g=+0.59(1)；GR18 Fig.3 的简化 j_p=j_n=11/2, j_R=2 向量模型中，planar limits 为 g=0.4 与 0.6，aplanar 几何在两者之间；PRM+CDFT 对该 bandhead 给近 planar 解。| 测得的是 g，几何来自模型；0.4/0.6 是指定简化构型的端点，不是普适分类器。该例来自不同核素和自旋点，不是 135Nd 的几何结果。| GR18-1; GR18-3; GR18-5 |

最低伴随观测与修订触发：要提高具体带对的模式判别力，须固定逐线带身份与匹配自旋，联合看 partner-resolved absolute lifetimes、B(M1)/B(E2)、out/in multipole-separated strengths、Qt 的同一几何约定、alignment/crossing 与模型角动量几何，并取得共享分支/寿命误差协方差。若能差只在 crossing 附近缩小、同时 alignment 与 partner B(E2)/Qt 显著分离，应把解释转向 crossing/mixing；若声称静态手征却只有近平面模型解，或模型不能同时解释 splitting、interband strengths 与几何随自旋演化，应降低 static-regime 结论。Qt 转换需要逐线 B(E2) 映射与 K/rotor matrix-element 假设；MU07 Table I 没有列逐行末态、ΔI 或 K，Fig.1 的 494-keV 43/2−→41/2− 代表性 line-shape fit 未被原文明示为该行 B(E2) 跃迁，故本次不报 MU07 source-supported numeric Qt。一般几何边界见 [transition-quadrupole-moment](../../knowledge/observables/transition-quadrupole-moment.md)。

#### Conditional parent photon-budget check

The candidate line bindings must also fit a total mean-lifetime budget. With all added same-parent/normalization premises stated, any subset of distinct photon components obeys `S=τΣΓγ≤1`. Existing Table-I Band-B lifetimes are `1.46(2),0.87(6),0.64(5),0.48(3) ps` at31/2−–37/2−.

| Spin | τ (ps) | Nominal M1 in+out budget | Nominal M1 in+candidate E2-crossover budget |
|---|---:|---:|---:|
| 31/2- | 1.46 | 1.3872 | 1.2027 |
| 33/2- | 0.87 | 1.2012 | 1.2313 |
| 35/2- | 0.64 | 0.9195 | 1.5385 |
| 37/2- | 0.48 | unassigned | 1.4376 |

The first two M1 pairs and every candidate E2-crossover pair overfill this nominal budget. The interpretation jointly assumes that the plot spin labels the Table-I parent, that τ is its total mean lifetime, and that each B component belongs to the selected line with the common radiative normalization. This excludes that added joint interpretation at these inputs; it does not identify which premise fails or prove author error. Nonnegative IC/omitted channels cannot repair an already overfilled photon budget. Fixed-energy rectangular endpoint sensitivities are in the JSON audit; they have no statistical coverage or unreported-systematic guarantee. Preserve the graph estimates/table entries, but use the earlier rate transforms only as arithmetic hypotheses, not a validated physical rate series. This is a same-input consistency check and adds no independent evidence. Atomic locator: [MU07-16](../../knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md); rate definition [LKH82-1](../../knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md).

## Sources and evidence

### Direct source evidence

- Mukhopadhyay *et al.* 2008 的本地原文 PDF SHA-256 为 `ea77d7d033051369d19aad2f82a542e91e262eb490d518b246f7f04c2d0dcd2c`，与 source page 一致。直接查看了 PDF p.3、p.4 原图：printed 034311-3/Table I 给 `Ex=6711.4 keV, 18−` 三支 `401.2 keV, 18−→17−, 0.57(6)`；`757.4 keV, 18−→16−, 0.24(2)`；`389.6 keV, 18−→17−, 0.19(2)`。三个中心值之和为 1.00。
- Table I caption 仅称这是从“同一能级退激的跃迁”的 branching ratios；紧邻正文说该分支数据在本工作中按 Chiara *et al.* [16] 的过程提取，并明确说先前 Refs.[17,18] 没有这些分支信息。原文因此未显示一个更早的分支表可补足其定义。caption/正文仍没有写明本表归一化分母，也没有说明数值是 relative photon intensity、absolute per-parent photon fraction，还是含 IC 的 total branch。三支中心值归一到 1 不能独立证明无漏枝、无 IC 或无非 γ 通道。两个 `18−→17−` 表项能量不同，不能把同一 `J_f` 标签当作同一条跃迁。
- 同一 PDF p.4 / printed 034311-4 Table II 给 Band 1 `I=18−` 的 lifetime `0.56(8) ps`、作者报告 `B(M1)=0.9(2) μ_N²`、`B(E2)=0.14(2) e²b²`、`Qt=1.26(9) eb`。这些属于同一 DSAM 实验及派生链；author B、Qt 不作为独立输入或本次倒推隐藏输入的依据。
- MU08 printed 034311-3 / PDF p.3 说明 lifetime uncertainties 由拟合最小值附近 `χ²` 行为导出；stopping-power modeling systematic 不含在 quoted errors 内，且可达 15%；absolute `B(M1)` 对 `ΔI=1` 跃迁采用 pure-M1 假设。printed 034311-5 / PDF p.5 Fig.4 caption 再说明图中 error bars 仅为 statistical，并排除约 15% stopping-power error。
- MU08 PDF p.2 记录：LINES​​HAPE DSAM 使用 5000 个 recoil-velocity Monte Carlo histories；stopping 取自 SRIM；feeding 用五跃迁 cascade 表示并改变 quadrupole moments；fit 纳入 shifted 与 stopped peak tails，并逐层构成 global fit。该流程支持作者的 lifetime 提取，但 feeding 与 stopping 仍是模型输入；本轮无 raw event、response、stopping/feeding code 或 covariance 可重复拟合。
- MU08 DOI `10.1103/PhysRevC.78.034311` 的 APS landing page / SI resolver / 标准 supplement PDF endpoint 于 2026-10-09 复查：无附件链接、resolver 回到文章 `#supplemental`、标准 SI URL 为 HTTP 404；未找到 MU08 SI。见 [MU08-SI-1](../../knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md)。
- MU08 更正核查：Crossref API 返回空 `relation` 且 `update-to=null`；APS article page HTTP 200，未发现 correction/erratum link。仅能说这些正式端点未发现更正，不能排除另处独立编目的公告。回执：[mu08-correction-check.json](20261008-DAY9-be2-bm1-reduced-matrix-elements-strengths-run-01/mu08-correction-check.json)；source locator [MU08-CORR-1](../../knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md)。
- Lange, Kumar & Hamilton 1982 raw PDF SHA-256 为 `ed925a0577a9257903806acd209c1db707529e86a5bfd9a301a83d597bf78ffb`，与 source page 一致。原图 printed p.121 / PDF p.3 Eq.2.2 给 γ rate 与 `B_G(XL)` 的关系，Eq.2.3a 明确 `B(XL;Ji→Jf)=|⟨Jf||M(XL)||Ji⟩|²/(2Ji+1)`；初态角动量在分母，不能二次除以 `2Ji+1`。LKH82 的算符/率采用 Gaussian 约定，下面的 modern SI rate constants 是本次单位重构，不是 LKH82 印出的绝对 ps 系数。
- MU07 raw PDF SHA-256 为 9eccc9c2ad02cc10735d1aad0d76eb2fd8af0a4acc814bcaab8099f50e748425，与 source page 一致；直接查看 printed 172501-2 / PDF p.2 Table I 和 printed 172501-3 / PDF p.3 Figs.2–3。原文明确 B(M1) 与 B(E2) 从 lifetime 推得；图例区分 Band B→Band A 数据点与 RPA 曲线。本 continuation 从 PDF 矢量图按纵轴刻度估读四个点，并通过 Zhu 2003 Ref.[8] Fig.2 将其 crosswalk 到 648/639/591/(556)-keV links；556 括号和 648/649 差异保留。2007 Figs.2–3 本身不标线能量，crosswalk 只作 identity，不改变 figure-digitized ratio 的证据等级。
- `135Nd` 后续 Lv 2019 arXiv PDF SHA-256 `97182e90125ce57ac2faa0feeef42b6bc12952b3287f82f277a04f8d32cf0303` matches its source page. Direct reading of PDF pp.9–10 Table I distinguishes, at matched initial spins, ΔI=1 D6→D5 mixed links from ΔI=2 E2 crossovers: 31/2− 648.9/896.8 keV, 33/2− 640.2/931.3 keV, 35/2− 591.4/949.6 keV; at 37/2− it lists a 963.0-keV E2 line but no matching ΔI=1 link for the parenthesized 556-keV crosswalk. This later-campaign table corroborates line classes but does not identify which line produced a MU07 B(E2) open-circle point. Locator: [LV19-9](../../knowledge/sources/lv-2019-chirality-135nd-reexamined.md).
- `131Xe` Chakraborty 2023 PDF SHA-256 `730db39eb9a5aecd3bbce1dce3cb9c32829eb2f4a2062ee31c59ddc4d52bd9ff` matches the source record. Directly rechecked PDF pp.4–5: the yrast 1055-keV `17/2−→15/2−` link has `δ≈0`; 671/882-keV links have low `|δ|` (about 0.03/0.09) and roughly 1% E2 admixture. The authors exclude wobbling for that studied yrast sequence and favor an unfavoured signature-partner interpretation; this is an experiment-specific control, not evidence assigning the `135Nd` pair. Atomic locators: [C23-2](../../knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md), [C23-3](../../knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md), [C23-7](../../knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md).
- Lv 2021 `135Nd` TiP source SHA-256 `e28bc232617af4d6ee83d95d267b2e7acd24eddb0d03cc1592124d31e9871150` matches its source page. Direct PDF pp.6–8, Table II gives TiP1→D1 `δ=-0.32(5), -0.48(14)` with E2 fractions `9.3±2.6%`, `18.7±8.9%`, and TiP2→TiP1 `δ=-0.26(8)` with `6.3±3.6%`; the authors treat these separate-band links as M1-dominated and reject a wobbling reading for them. Same nucleus, but different D1/TiP bands and 152-MeV JUROGAM II campaign; these data do not classify MU07 D5/D6. Locators: [LV21-9](../../knowledge/sources/lv-2021-tilted-precession-135nd.md), [LV21-10](../../knowledge/sources/lv-2021-tilted-precession-135nd.md), [LV21-11](../../knowledge/sources/lv-2021-tilted-precession-135nd.md), [LV21-17](../../knowledge/sources/lv-2021-tilted-precession-135nd.md).
- Petrache 2006 raw PDF SHA-256 `ec32a76efbeebf1a924a1c95eb9d404a99158fc9226605414b324e982cfe1d4f` matches its source page. Direct PDF pp.1–3 reports `134Pr` near-degeneracy over `13<I<19`, a Band 1/Band 2 crossing between I=15 and 16, about `2ħ` alignment difference at `14<I<18`, and branching/two-band-mixing-derived `Q0,1/Q0,2=2.0(4)`. The source authors treat these as inconsistent with an ideal chiral pair, while the Q0 ratio remains model-analysis dependent. Atomic locators: [PE06-1](../../knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md), [PE06-2](../../knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md).
- Singh *et al.* 2016 原文 SHA-256 `95e0831b9864a58fd1a896a1b20e227d88d9b7aa5de56c738c3792441caa1a30` matches its source page. Direct PDF p.5 review of Eqs.(1)–(2) confirms the source-specific E2 rotor rate conversion, units, and mixed-`K` CG-amplitude replacement recorded as [SI16-17](../../knowledge/sources/singh-2016-lifetime-131ce-133pr.md). This method example is used to explain the `Q_t` input requirements, not to transfer any `131Ce` measured value to `135Nd`.

### Chiara 2001 Ref.[16] method source

The 30-page APS original was downloaded through the official HTTPS publisher PDF endpoint and hash-verified; Unpaywall classifies it as closed/no OA repository, and the article page has no SI link. Direct reading of printed 054314-18–19 / PDF pp.18–19 shows that `τ(Mλ)` partial lifetimes are derived from fitted level lifetimes and observed branch ratios, with IC included. The same method description treats ΔI=1 dipoles as predominantly pure M1 and assumes zero E2 crossover intensity when none is seen within sensitivity. PDF p.7 Table III normalizes line intensities to the 213-keV reference transition, while the Table V caption says the B strengths use branch/IC-adjusted lifetimes. This does not document an absolute photon-per-parent ledger or every unobserved channel for MU08. Exact method locators: [CHI01-2](../../knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md), [CHI01-3](../../knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md), [CHI01-4](../../knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md).

### MU07 Supporting Information check

The official APS 2007 article page had no supplement/attachment link; its SI resolver redirected to the same article at `#supplemental`, and the standard APS supplemental-PDF endpoint returned HTTP 404. No SI file was found on these official endpoints; the source page records locator `MU07-SI-1`. This check does not rule out separately hosted author material.

### Zhu 2003 Ref.[8] transition identity source

CrossRef metadata and the local PDF identify S. Zhu et al., “A Composite Chiral Pair of Rotational Bands in the Odd-A Nucleus 135Nd,” Phys. Rev. Lett. 91, 132501 (2003), DOI 10.1103/PhysRevLett.91.132501, arXiv:nucl-ex/0302029v2. The main text was obtained through the Unpaywall OA route from arXiv and copied read-only to raw/papers/gpt/high-spin-20261009; SHA-256 8dd7aaa0a2e369532dd673384bcc18c60abc330408f20243939b31df15d98542.

PDF p.4 Fig.2 maps the four Band B→Band A links to the corresponding lower-spin Band A states: 31/2−→29/2− at 648 keV in the figure, 33/2−→31/2− at 639 keV, 35/2−→33/2− at 591 keV, and 37/2−→35/2− at (556) keV. The same figure labels Band B in-band links at 226, 282, 309 and 372 keV. Zhu's text has a 648/649-keV difference across DCO discussions; 556 is parenthesized. MU07 printed p.1 says its partial scheme is taken from Ref.[8], while the DSAM strengths come from a separate 100Mo(40Ar,5n) campaign. The 2003 arrow widths indicate relative intensity only, not B values. Atomic locator: [ZH03-3](../../knowledge/sources/zhu-2003-135nd-composite-chiral-pair.md).

### Zhu 2003 Supporting Information check

The user authorized obtaining any needed supplementary material. The APS article page returned HTTP 200 with no supplement/attachment link; the APS supplemental resolver returned to the article record at `#supplemental`; the standard APS SI PDF endpoint returned HTTP 404; and the official arXiv record listed the article PDF and TeX source without an SI/ancillary entry. No SI file was found at these official endpoints. This does not rule out separately hosted author material. Exact route locators are recorded in [Zhu source](../../knowledge/sources/zhu-2003-135nd-composite-chiral-pair.md): `ZH03-SI-1` through `ZH03-SI-4`; retrieval receipt: [zhu-2003-si-check.json](20261008-DAY9-be2-bm1-reduced-matrix-elements-strengths-run-01/zhu-2003-si-check.json).

### Grodner 2018 direct-source check

The 5-page original PDF SHA-256 `c71ec59160c444c34ab7f340db5f045c1f26456bc1741197ec62caea7f4efbf2` matches the source record. PDF p.1 reports the measured `g=+0.59(1)` for the 56-ns isomer; p.3 Table II shows the `j_R=0` two-component estimates `g≈0.50–0.519`, and Fig.3 gives a simplified vector-geometry illustration in which planar endpoints are `g=0.4` and `0.6` for `j_p=j_n=11/2, j_R=2`, with the aplanar case between them. PDF pp.4–5 then give the PRM+CDFT model result `g≈0.58` with orientation parameter `⟨ô⟩≈0.15`, interpreted as nearly planar. The measurement and model interpretation are separate; the endpoints belong only to this simplified configuration. Source locators: [GR18-1](../../knowledge/sources/grodner-2018-128cs-chiral-g-factor.md), [GR18-3](../../knowledge/sources/grodner-2018-128cs-chiral-g-factor.md), and [GR18-5](../../knowledge/sources/grodner-2018-128cs-chiral-g-factor.md).

### Timár 2007 `105Ag` configuration-mixing counterexample

The local original PDF hash `730be91dc2ffbbc785ebe36f5ecc50aeefd8ef74d577c8a2e314204cb4f58442` matches its source record. Direct reading of PDF p.9 / Fig.6 confirms that Bands D/G have an approximately 70-keV separation and similar branching-derived `B(M1)/B(E2)` fingerprints with pronounced staggering. The same page says natural-parity similarities may come from excitations without chiral angular-momentum coupling and that the reported comparison cannot distinguish chiral geometry from simple mixing of the `g7/2` and `d5/2` neutron configurations. No dedicated D/G TAC calculation is reported. This establishes a live competing explanation for a similar fingerprint, not a quantitative alternative fit to `135Nd`. Atomic locators: [TI07-11](../../knowledge/sources/timar-2007-high-spin-105ag-chiral-search.md), [TI07-13](../../knowledge/sources/timar-2007-high-spin-105ag-chiral-search.md), [TI07-14](../../knowledge/sources/timar-2007-high-spin-105ag-chiral-search.md), [TI07-15](../../knowledge/sources/timar-2007-high-spin-105ag-chiral-search.md).

### Timár 2007 Supporting Information check

The user authorized retrieval of needed SI. The official APS article page for DOI `10.1103/PhysRevC.76.024307` returned HTTP 200 with no SI/attachment links; the APS supplemental resolver returned to the article record at `#supplemental`; the standard SI PDF URL returned HTTP 404. No SI file was found on these publisher routes; separately hosted author material is not ruled out. The local main PDF is already hash-verified, so no duplicate was downloaded. See [timar-2007-si-check.json](20261008-DAY9-be2-bm1-reduced-matrix-elements-strengths-run-01/timar-2007-si-check.json) and durable source locator [TI07-SI-1](../../knowledge/sources/timar-2007-high-spin-105ag-chiral-search.md).

### Lv 2019 Supporting Information check

The official APS article page for DOI `10.1103/PhysRevC.100.024314` returned HTTP 200 with no attachment candidate; its standard SI PDF endpoint returned HTTP 404. The APS supplemental resolver timed out on the first request, then one bounded retry returned HTTP 200 to the article record at `#supplemental`, still with no attachment. The official arXiv record for `1907.12809` lists the article PDF without an ancillary entry. No SI file was found on the successfully checked records; this is not a global absence claim. No duplicate article PDF was downloaded. Receipt: [lv19-2019-si-check.json](20261008-DAY9-be2-bm1-reduced-matrix-elements-strengths-run-01/lv19-2019-si-check.json); source locator [LV19-SI-1](../../knowledge/sources/lv-2019-chirality-135nd-reexamined.md).

### Suzuki 2008 `103,104Rh` denominator-driver comparison

The five-page original PDF SHA-256 `f9c421090b33da94206f9d1d4ebd36ad0f5be79ee1dcd6a19fe38b32a7ec5927` matches the source record. Direct reading of PDF p.3 Table III and p.4 Fig.3/Tables IV–V confirms the authors' decomposition: measured `B(M1)` falls with spin, while weak odd-even structure appears in `B(E2)` and accounts for the reported ratio staggering. The paper contrasts this with A≈130 examples where the ratio staggering was attributed to `B(M1)`. Its `103Rh/104Rh` lifetimes cover only one member of each proposed pair; pure-M1 extraction and earlier energy/branch inputs remain. This shows that ratio staggering need not be a magnetic-numerator signal, but does not test partner equality or transfer directly to `135Nd`. Atomic locators: [SU08-6](../../knowledge/sources/suzuki-2008-lifetimes-103rh-104rh.md), [SU08-7](../../knowledge/sources/suzuki-2008-lifetimes-103rh-104rh.md), [SU08-8](../../knowledge/sources/suzuki-2008-lifetimes-103rh-104rh.md), [SU08-13](../../knowledge/sources/suzuki-2008-lifetimes-103rh-104rh.md).

### Grodner 2018 Supporting Information check

After the user authorized fetching needed SI, the official APS article page was checked for DOI `10.1103/PhysRevLett.120.022502`: the initial request returned HTTP 200 with no supplement/attachment links; a later metadata-only recheck timed out, so Crossref was used to verify DOI/title identity. The APS supplemental resolver returned to the article record at `#supplemental`; the standard supplemental-PDF URL returned HTTP 404. No SI file was found on these publisher routes; separately hosted author material is not ruled out. No file was downloaded. The route receipt is [grodner-2018-si-check.json](20261008-DAY9-be2-bm1-reduced-matrix-elements-strengths-run-01/grodner-2018-si-check.json), and the durable source locator is [GR18-SI-1](../../knowledge/sources/grodner-2018-128cs-chiral-g-factor.md).


**Relative-intensity illustration only:** Chiara Table V's `108In` Band 2 `15−` row lists `Iγ=31.6` for the 527.8-keV M1 line and `Iγ=2.0` for the 864.2-keV E2 crossover. Normalizing just those two entries to their sum gives `31.6/33.6=0.9405` and `2.0/33.6=0.0595`; this demonstrates a relative share of the two listed observed photon intensities, not an absolute probability per parent decay or a complete IC-corrected channel ledger (CHI01-6).

### `135Nd` model-evolution comparison

Direct reading of Zhu 2003's model discussion gives planar orientation below the critical frequency, an aplanar/static interval near `I≈19`, and a near-planar return at higher frequency; the authors call the static interval transient. MU07's later TAC+RPA result associates low-spin chiral vibration with a softening RPA mode and places static onset around the critical frequency, about one spin unit above the closest approach in the experimental partner bands. These two theories are qualitatively compatible near onset, but their model results do not become another measurement and should not be averaged as independent evidence. Keep Zhu's high-spin return-to-planarity prediction distinct because the MU07 onset statement alone neither confirms nor rejects the same full-spin trajectory. Source locators: [ZH03-8](../../knowledge/sources/zhu-2003-135nd-composite-chiral-pair.md), [MU07-2](../../knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md), [MU07-3](../../knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md).

### Candidate reference [16]

Crossref DOI metadata identifies C. J. Chiara *et al.*, “Spectroscopy in the Z=49 108,110In isotopes: Lifetime measurements in shears bands,” *Phys. Rev. C* 64, 054314 (2001), DOI `10.1103/PhysRevC.64.054314`. This closes the prior identity-only status. The official APS article page returned HTTP 200 and exposed the standard `citation_pdf_url`; its HTTPS PDF endpoint returned HTTP 200, `application/pdf`, 440,801 bytes. The downloaded file has SHA-256 `5672ffce1e4049245b3107e6132af0ff7501d14182a03d803cd66828e6660a4e`. Unpaywall still reports `is_oa=false`, no repository copy or OA locations; exact DOI arXiv query returned zero and exact-title OpenAlex/Semantic Scholar searches returned zero. The file is recorded as an official publisher endpoint retrieval, not an OA-licensed copy. The APS article page contained no supplement link, so no SI file was available there. Route/status receipt: [chiara-acquisition-check.json](20261008-DAY9-be2-bm1-reduced-matrix-elements-strengths-run-01/chiara-acquisition-check.json).

Targeted direct read covered PDF p.1 abstract, p.7 Table III caption, pp.18–19 Sec. IV.C/Eqs.(2)–(3)/Table V, and p.29 conclusions; see [Chiara source](../../knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md). The authors derive partial lifetimes from fitted level lifetimes plus observed branching ratios, include IC in `B(M1)/B(E2)`, assume `δ≈0` for the dipole transitions, and set unobserved E2 crossover intensity to zero when below the sensitivity of the experiment (CHI01-2/3). Table III efficiencies/intensities use a stopped reference transition; this is not an absolute per-parent photon ledger. The cited procedure narrows the method class but does not establish MU08's exact denominator, unseen-channel completeness or branch/τ covariance (MU08-11/12).
## Theory/analysis exercise

### Primed recall 与来源后校准

来源前记录在 [recall-record.md](20261008-DAY9-be2-bm1-reduced-matrix-elements-strengths-run-01/recall-record.md)。它明确是 **primed recall**：先读了 Day8 日报、Day9 plan 与 active handoff；不是 blind recall。初答已区分 `τ` 与 `T1/2`、absolute `pγ` 与 relative γ intensity、`B∝Eγ^(2L+1)` 的逆关系，以及 `δ²` 是分量 γ-rate ratio 而非 branch。对照 MU08 原表后补充了本数据集特有缺口：printed branch denominator、IC basis、branch/tau covariance 均未报告；因此绝对 B 只能以明确条件计算。没有把 Day8 预习算作本次独立交付。

### 输入—公式—输出—误差表

| 输入/步骤 | 数值与单位 | 公式 / 输出 | 误差与条件 | 原文定位 |
|---|---|---|---|---|
| 母态 `τ` | `0.56(8) ps`，作为 mean lifetime 使用 | `λ_total=1/τ`; `T1/2=ln(2)τ=0.3882(555) ps` | `T1/2` 为本次换算值；MU08 表头写 lifetime，不写 half-life | MU08 Table II, printed 034311-4 / PDF p.4 |
| target line | `757.4 keV = 0.7574 MeV`; `18−→16−`; `ΔI=2` | 目标多极按 pure E2 条件提取 | 自旋差支持低阶 E2 选项，但不单独证明 `f_E2=1`；M3/E4 等高阶成分未由该表排除。E0(`L=0`) 不允许在此 `ΔI=2` 支路混合 | MU08 Table I, printed 034311-3 / PDF p.3 |
| 同母态所有印出 branch | `401.2: 0.57(6)`；`757.4: 0.24(2)`；`389.6: 0.19(2)`；无量纲 | centers sum to `1.00` | 分母/IC correction 未定义；printed uncertainty 的联合协方差和 coverage 未给 | MU08 Table I, Ex=6711.4 group |
| rate / partial γ lifetime | 条件 `pγ=0.24`; `τγ=2.3333 ps`; `λγ=4.2857×10¹¹ s⁻¹` | `λγ=pγ/τ`; `τγ=τ/pγ` | 仅当 `pγ` 是每次母态总衰变发出该 photon 的绝对概率时成立 | LKH82 Eq.2.2 + rate definition; MU08 Table I/II |
| E2 rate coefficient and strength | `K_E2=1.225186722×10¹³ s⁻¹ MeV⁻⁵ (e²b²)⁻¹`; `C_E2=0.0816202120 e²b²·ps·MeV⁵` | `Tγ(E2)=K_E2 Eγ⁵ B(E2)`；`B(E2)=C_E2 pγ f_E2/[τ(ps)Eγ(MeV)⁵]`；在 `pγ=.24, f_E2=1` 条件下 `B=0.140344 e²b²` | `K_E2/C_E2` 从 LKH82 Gaussian 公式按现代物理常数和 `1 b²=10⁴ fm⁴` 重构；不把 author `0.14(2)` 当输入 | LKH82 printed p.121 / PDF p.3, Eqs.2.2–2.3a |
| reduced matrix element | `Ji=18`; conditional `B=0.140344 e²b²` | `|⟨16||M(E2)||18⟩|=√[(2Ji+1)B]=√[37B]=2.27876 eb` | 只给 magnitude；没有 RME sign/phase。由同一 B 派生的 reverse `B(16→18)=(37/33)B=0.15736 e²b²` 不是新测量 | LKH82 Eq.2.3a; same MU08 branch/lifetime inputs |
| statistical propagation | `στ=.08 ps`; `σb=.02`; Table I 未给 `σE` | 若暂作独立 τ 与 branch 输入且忽略能量误差：`σB/B=√[(.08/.56)²+(.02/.24)²]`；`σB=0.02321 e²b²`；`σRME=0.18844 eb` | branch/tau correlation `ρ` 未给；在固定边际误差、`ρ∈[-1,1]` 的一阶代数范围为 `σB=0.00835–0.03174 e²b²`，不是实际置信区间。未加 15% stopping 标签 | MU08 Table I/II; stopping/systematic text p.3; Fig.4 caption p.5 |

### Branch 与 radiative-fraction forward cases

目标支路可用 `B(E2)=C_E2 pγ f_E2/(τEγ⁵)`。原文没有确定 `pγ` 的定义，因此不把中心值结果宣称为无条件 absolute B：

1. 若 `0.24` 已是每次母态衰变产生目标 γ 的绝对 probability，则 `pγ=0.24`；本表数值再要求 `f_E2=1`。三条 `pγ` 中心值之和为 1 会隐含这个 observed gamma ledger 已闭合，但 Table I 未证明这种完整性。
2. 若 `0.24` 是在 observed γ lines 间归一的 relative photon fraction，则 `pγ=0.24 Fγ`，其中全部母态衰变中进入 photon ledger 的 `Fγ` 未知，故 `B=0.140344 Fγ f_E2 e²b²`。
3. 若 `0.24` 是包含内部转换的 true total-transition branch，且普通全壳层 conversion 账本完整，则 `pγ=0.24/(1+α_eff)`，`B=0.140344 f_E2/(1+α_eff) e²b²`。MU08 未给此处 `α_eff`，本次没有从 quoted B 反算它。

目标 18−→16− 的 `E0` mixing 禁止于 `ΔI=2`，且 `757.4 keV` 低于 pair-creation threshold；这不排除表格未列出的其它母态衰变通道。MU08 Table I 没有给 `α_tot` 或 shell-resolved conversion。现代 BrIcc FO/NH 数值若引用，只是给定理论输入下的 forward scenario，不能识别作者实际采用的 IC/branch 处理。

### Mixing、RME 与共享强度比

LKH82 printed p.121 Eq.2.1 定义 `δ²(E2/M1)=Tγ(E2)/Tγ(M1)`，而 Eq.2.5 给 signed convention；平方率和 `B`/RME magnitude 不给 relative amplitude sign。401.2-keV `ΔI=1` 分支在 MU08 的绝对 `B(M1)` 提取中假定 pure M1，这是 extraction assumption，不是实测 `δ=0`。对该条件 M1 与 757.4-keV 条件 E2 的同母态强度比，重构值为 `B(M1;401.2)/B(E2;757.4)=6.387 μN²/(e²b²)`；共同 `τ` 抵消，但它仍共享同一组 branch、能量、level assignment 和多极性假设，故不构成独立确认。branch-specific IC、feeding 或门条件 bias 不会仅因取比自动抵消。

`B↓`、`B↑`、RME magnitude、`Qt` 和上述 ratio 是同一寿命/分支链的确定性派生或模型化输出；不得重复计作独立实验支持。`RME` 的绝对值不等于 `Qt`，且不保存相位。

## Counter-evidence and missing companion observables

- **漏枝与归一化：** Table I 三个中心值和为 1，但未列分支、未观测 γ、门效率/feeding 偏差或非 γ 通道可以改变绝对 `pγ`。`0.57(6),0.24(2),0.19(2)` 的括号数不能自动当成独立误差，也没有联合协方差。
- **归一化—quoted-error 相容性：** 对十个 MU08 Table-I 母态组逐行作 conditional covariance test：若同一 branch-vector 每次样本精确归一且把打印括号误差当作精确边际 SD，则两支组必须有相等 SD，三支组须逐项满足 `σ_i≤Σ_(j≠i)σ_j`（L2 三角不等式）。按打印值作为精确 SD，该必要条件在 8/10 组不成立；例如 I=18− 为 `0.06>0.02+0.02`，I=16− 为 `0.04>0.01+0.01`，而 I=19− 两支为 `0.08≠0.02`。另加 nearest-0.01 SD rounding 的假设（保守闭区间 ±0.005）后，7 组仍违反；B2-I17 对末位舍入敏感，例如 `0.036≤0.024+0.014` 可满足必要条件。此舍入模型及其通过项均不证明实际误差定义或 covariance。详细输入/代码化结果见 [day9-branch-normalization-sigma-audit.json](20261008-DAY9-be2-bm1-reduced-matrix-elements-strengths-run-01/day9-branch-normalization-sigma-audit.json)。原文未说括号误差属于该 joint SD 模型、每次母态衰变严格落在表列分支集合且无额外通道；此 reductio 只排除这些额外假设的联合解释，不判作者错误、漏枝或实际 covariance 符号。
- 本次逐组审计只用 MU08 printed 034311-3 / PDF p.3 Table I 的全部 10 组数字；对应耐久 claim 为 [MU08-14](../../knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md)。
- **IC/E0 与 branch basis：** target E0 不允许，但全母态非 γ inventory 仍未知。Chiara Ref.[16] 现在已直接读到 partial-τ/observed-branch/IC procedure；它未报告 MU08 136Nd 的逐线绝对 photon ledger、弱/漏枝处理或 covariance。若 MU08 branch 是 photon-relative、true total branch 或 absolute `pγ`，B 的 forward formula 不同；未选任何一种为 MU08 事实。
- **feeding/stopping：** 五跃迁 side-feeding cascade、可变 quadrupole moments、SRIM stopping 以及 line-shape/global fit 都进入寿命推断。作者明说 stopping systematic 可达 15% 且不含在 quoted errors 内；没有分布/covariance，不能自动把 15% 当独立 1σ，也不能宣称跨带共模而抵消。
- **遗漏误差项：** Table I 没列能量误差；本次公式按 printed central Eγ 计算。branch/tau covariance、branch-branch covariance、能量协方差、IC/E0 response 和 feeding/stopping 的联合系统均未提供。`σB=0.02321` 是明确独立输入假设下的条件性统计传播，不是完整误差预算。
- **输出依赖：** Table II 的 B、作者 Qt、本次 RME/reverse-B 与 same-parent ratio 使用同一实验的 level lifetime / branch / energy information。中心值接近 author `B(E2)=0.14(2)` 仅说明此 gamma-only 算术复现一致；不能由此验证 branching denominator、ICC、feeding 或 covariance。

## Knowledge Impact and Learning Decision

- `supports`: 现有 lifetime synthesis 对平均寿命、绝对 photon fraction、`B` 与 RME 归一的区分；MU08 原表的三个 branch/lifetime 输入与 LKH82 rate definitions 经本次原图复核。
- `limits`: 把 Table I printed branching ratio 直接当作 absolute radiative probability、把 `0.14(2)` 与 `Qt` 当独立测量、或从 quoted B 反求未报告 `α/δ/covariance` 的用法。
- `revises`: MU08 source now records the verified identity and directly read procedure for Ref.[16]: partial lifetimes from fitted level τ plus observed branch ratios, IC included, with pure-M1 and unseen-crossover assumptions stated. This narrows the method boundary but leaves MU08 Table-I normalization and completeness unresolved. The MU07, Zhu, GR18, Timár, Chakraborty, Petrache, Chiara, Singh, lifetime/Qt and synthesis changes remain source-linked; all measurements and model results stay separated.
- Day10 rate-crosswalk audit revised the conditional transforms: retain candidate M1 rates for the first three ΔI=1 links, keep two E2 line-class forward alternatives without selecting one, and withdraw the earlier single E2-rate column because the MU07 graph does not identify its line. LV19 cross-checks later line classes but cannot bind a MU07 marker to one line.
- Day10 partial adds a bounded **Codex algebraic counterexample** to [B(M1)/B(E2) ratio knowledge](../../knowledge/observables/bm1-be2-ratio.md): if a shared dimensionless amplitude factor multiplies both selected transition matrix elements, the common factor cancels in the B ratio. This establishes a ratio-identifiability limitation, not a source claim or a fitted mechanism for MU07; distinguish it using absolute/partner-resolved strengths and independent observables.
- Day10 partial also adds a source-grounded denominator-driver example: in `103,104Rh`, Suzuki's lifetimes show `B(M1)` declining while weak odd-even structure in `B(E2)` accounts for the published ratio staggering. It is one-member-per-pair evidence with a pure-M1 and imported-branch dependency, not a partner-equality test for `135Nd`.
- The date-scoped MU08 correction check found no correction relation in Crossref and no correction link on the APS article page (`MU08-CORR-1`); this confirms only the checked endpoints and does not resolve the original branching denominator.
- MU08 Table I–II、Fig.4 是同一 DSAM 实验；LKH82 是 rate/operator 方法来源，不增加实验独立性。Codex self-audit only；未设置 `human-reviewed` 或清除任何 `needs_review`。

## Durable knowledge delta

本 run 当前同步十五页：MU08 source 与 Chiara source 固化 Ref.[16] 方法、publisher/Crossref correction-route 结果、8/10 parent quoted-SD conditional normalization reductio 及未闭合的 136Nd branch ledger；更新 knowledge index 和 questions；high-spin-lifetime synthesis 加入 observed-branch partial-lifetime precedent；MU07 source 保存 ratio、line-class alternatives 与模型边界；Zhu source 记录线身份及 SI；LV19 source 添加 D6→D5 ΔI=1/ΔI=2 Table-I transition-class crosswalk；GR18 加入 g-factor 几何与 SI route 结果；TI07 加入 `105Ag` configuration-mixing fingerprint counterexample 与 SI route 结果；`131Xe` signature control、LV21 同核 TiP δ-control 与 PE06 `134Pr` crossing/Q0 counterexample 进入 chirality-wobbling synthesis；Singh source 补充 source-specific Qt formula；135Nd nucleus 与两个 ratio/Qt observable 同步。Review flags unchanged。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
      "anchor": "MU08-10",
      "summary": "Ref.[16] identity, APS publisher-PDF access and method text are verified. MU08 Table I labels same-level branching ratios but never states a photon-vs-total denominator or full-channel ledger; Chiara supplies only a related procedure using observed branches and IC, plus its own pure-M1/unseen-crossover assumptions. This narrows the method boundary but does not determine MU08 absolute pγ, branch completeness or covariance.",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-10"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-11"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-12"
        },
        {
          "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
          "locator": "CHI01-2"
        },
        {
          "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
          "locator": "CHI01-3"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-13"
        },
        {
          "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
          "locator": "CHI01-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
      "anchor": "MU08-14",
      "summary": "Record the ten-parent conditional covariance reductio: eight quoted-error groups violate a necessary marginal-SD constraint if their printed branch fractions are assumed to form one exactly normalized random vector. The count eight treats printed errors as exact SDs; seven violations remain under a hypothetical ±0.005 last-digit rounding model, while B2-I17 is sensitive. This excludes only the added joint interpretation; the source does not define the required covariance/normalization/rounding model.",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
      "anchor": "MU07-8",
      "summary": "Day10 partial保留MU07四个Band B→Band A空心圆out/in图估读及同母态寿命因子条件性消去；另以Zhu 2003 Ref.[8] Fig.2映射候选线能量/末态。556 parenthesized、648/649行文差异、图误差覆盖及covariance边界保留。2003/2007不同反应实验，2003 relative arrow intensities不作MU07 B。",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-6"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-2"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-1"
        },
        {
          "path": "knowledge/sources/zhu-2003-135nd-composite-chiral-pair.md",
          "locator": "ZH03-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/bm1-be2-ratio.md",
      "anchor": "### Shared-amplitude identifiability example",
      "summary": "Day10 无学分 partial 增加一个本任务构造的代数反例：若共同无量纲振幅因子同时乘到所选 M1/E2 matrix elements，其模平方会从B(M1)/B(E2)约分掉，故比例趋势不能排除共同绝对强度变化。明确标注该模型构造非 MU07 直接结论，并以 MU07-7 说明由同表B值再派生的quotients不新增独立证据。",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
      "anchor": "MU07-9",
      "summary": "Map MU07 same-spin Band B→Band A plot points through Zhu Fig.2 to 648/649, 639, 591 and (556)-keV links and the corresponding 226/282/309/372-keV in-band lines. Preserve the 556 parentheses and 648/649 text difference; this identity map adds no B evidence.",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-6"
        },
        {
          "path": "knowledge/sources/zhu-2003-135nd-composite-chiral-pair.md",
          "locator": "ZH03-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/zhu-2003-135nd-composite-chiral-pair.md",
      "anchor": "ZH03-3",
      "summary": "Persist the original Fig.2 spin/line-energy crosswalk and Band B in-band transition energies; preserve the parenthesized 556-keV line and the 648/649-keV text discrepancy.",
      "sources": [
        {
          "path": "knowledge/sources/zhu-2003-135nd-composite-chiral-pair.md",
          "locator": "ZH03-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/nuclei/135nd.md",
      "anchor": "[[zhu-2003-135nd-composite-chiral-pair]]",
      "summary": "Connect the 2003 Band A/B original level scheme to the distinct MU07 2007 strength campaign and later D5/D6 nomenclature without pooling measurements or backdating band labels.",
      "sources": [
        {
          "path": "knowledge/sources/zhu-2003-135nd-composite-chiral-pair.md",
          "locator": "ZH03-1"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "[[zhu-2003-135nd-composite-chiral-pair]]",
      "summary": "Add the canonical source-index entry for the 135Nd Band A/B original experiment and its line-identity/evidence boundary.",
      "sources": [
        {
          "path": "knowledge/sources/zhu-2003-135nd-composite-chiral-pair.md",
          "locator": "ZH03-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
      "anchor": "MU07-10",
      "summary": "Correction after crosswalk audit: retain conditional M1 partial-rate transforms and rectangular endpoint envelopes only for the first three candidate ΔI=1 links; the 37/2− link is tentative. For E2, record ΔI=1 mixed-link and ΔI=2 crossover forward transforms plus rectangular endpoint envelopes because the MU07 graph does not identify the plotted line; withdraw the previous single E2-rate series. LV19 is a later line-class cross-check, not MU07 strength data. Both E2 numerical alternatives also assume an unverified adjacent-spin in-band E2-component denominator; a different denominator energy rescales the transform by (Ein,assumed/Ein,true)^5. All results remain shared-input sensitivities, not measured branches/counts or confidence intervals.",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-8"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-9"
        },
        {
          "path": "knowledge/sources/zhu-2003-135nd-composite-chiral-pair.md",
          "locator": "ZH03-3"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-1"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
      "anchor": "LV19-9",
      "summary": "Persist the later Table-I distinction between same-spin ΔI=1 D6→D5 mixed links and ΔI=2 E2 crossovers, plus the absence of a listed ΔI=1 match for the tentative historical 556-keV link. This constrains energy-factor transforms but does not assign a MU07 plotted E2 marker.",
      "sources": [
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
      "anchor": "LV19-SI-1",
      "summary": "Record the date-scoped APS/arXiv SI check: no attachment on the APS page, standard endpoint 404, resolver timed out once then retried to the same article record without SI, and arXiv listed no ancillary entry; separately hosted material is not ruled out.",
      "sources": [
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-SI-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/zhu-2003-135nd-composite-chiral-pair.md",
      "anchor": "ZH03-SI-1",
      "summary": "Record the user-authorized 2026-10-09 official APS/arXiv SI availability check: no linked SI file was found on these endpoints; separately hosted author material remains outside the search boundary.",
      "sources": [
        {
          "path": "knowledge/sources/zhu-2003-135nd-composite-chiral-pair.md",
          "locator": "ZH03-SI-1"
        },
        {
          "path": "knowledge/sources/zhu-2003-135nd-composite-chiral-pair.md",
          "locator": "ZH03-SI-2"
        },
        {
          "path": "knowledge/sources/zhu-2003-135nd-composite-chiral-pair.md",
          "locator": "ZH03-SI-3"
        },
        {
          "path": "knowledge/sources/zhu-2003-135nd-composite-chiral-pair.md",
          "locator": "ZH03-SI-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
      "anchor": "GR18-5",
      "summary": "Record direct raw-PDF recheck of the Fig.3 simplified three-vector geometry: for jp=jn=11/2 and jR=2, planar limits have g=0.4 and 0.6, while the aplanar geometry is intermediate; these are configuration-specific model values, not a universal classifier.",
      "sources": [
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
      "anchor": "GR18-SI-1",
      "summary": "Record the authorized official APS supplement-route check: no link on the article page, resolver returns to the article record, and the standard SI PDF endpoint returns 404; separately hosted material is not ruled out.",
      "sources": [
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-SI-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/timar-2007-high-spin-105ag-chiral-search.md",
      "anchor": "TI07-SI-1",
      "summary": "Record the authorized official APS SI-route check: the article page had no attachment link, the resolver returned to the article record, and the standard SI PDF endpoint returned 404; separately hosted material is not ruled out.",
      "sources": [
        {
          "path": "knowledge/sources/timar-2007-high-spin-105ag-chiral-search.md",
          "locator": "TI07-SI-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/bm1-be2-ratio.md",
      "anchor": "### Difference from the multipole mixing ratio `δ`",
      "summary": "Distinguish the dimensionful reduced-probability quotient B(M1)/B(E2) from dimensionless same-transition rate ratio δ². In LKH82 common units, δ²=(0.835 Eγ[MeV])² B(E2)[e²b²]/B(M1)[μN²]; conversion needs a specified shared transition and B values do not give signed δ. MU07 Table I lacks row-specific Eγ/final-spin mapping.",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-11"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/bm1-be2-ratio.md",
      "anchor": "### Ratio staggering can be denominator-driven",
      "summary": "Add Suzuki 2008 as a lifetime-based example in which B(M1) decreases with spin while weak odd-even variation in B(E2) drives the reported B(M1)/B(E2) staggering. Preserve the one-member-per-pair and pure-M1/imported-branch boundaries.",
      "sources": [
        {
          "path": "knowledge/sources/suzuki-2008-lifetimes-103rh-104rh.md",
          "locator": "SU08-8"
        },
        {
          "path": "knowledge/sources/suzuki-2008-lifetimes-103rh-104rh.md",
          "locator": "SU08-7"
        },
        {
          "path": "knowledge/sources/suzuki-2008-lifetimes-103rh-104rh.md",
          "locator": "SU08-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/chirality-wobbling-competition-evidence.md",
      "anchor": "### `135Nd` model evolution: 3D-TAC and TAC+RPA",
      "summary": "Compare Zhu 2003 3D-TAC and MU07 TAC+RPA onset interpretations for the same 135Nd band pair. MU07 graph-estimated B(E2) out/in ratios rise with spin, but endpoint intervals overlap at 35/2–37/2 and there is no 39/2 interband point; this cannot locate the static onset. Zhu high-spin return-to-planarity remains distinct; model results are not independent measurements.",
      "sources": [
        {
          "path": "knowledge/sources/zhu-2003-135nd-composite-chiral-pair.md",
          "locator": "ZH03-8"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-2"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-3"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/chirality-wobbling-competition-evidence.md",
      "anchor": "| Low-`|δ|` M1-dominated `ΔI=1` links |",
      "summary": "Add the measured 131Xe low-|δ|, M1-dominated link case as an experiment-specific signature-partner control and preserve that it cannot classify 135Nd. This supplies a direct transition-resolved counterexample to wobbling readings from band similarity alone.",
      "sources": [
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-2"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-3"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/chirality-wobbling-competition-evidence.md",
      "anchor": "### `134Pr` crossing and shape-difference control",
      "summary": "Persist the quantified PE06 134Pr counterexample: the near-degenerate spin interval contains a band crossing/alignment difference and a branching-mixing-derived Q0 ratio; retain the model-dependent and cross-nucleus limits.",
      "sources": [
        {
          "path": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
          "locator": "PE06-1"
        },
        {
          "path": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
          "locator": "PE06-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/chirality-wobbling-competition-evidence.md",
      "anchor": "| `135Nd` D1/TiP1/TiP2 mixing-ratio control |",
      "summary": "Add the later 135Nd D1/TiP1/TiP2 measured mixing-ratio result as a same-isotope but different-band control. Selected M1-dominated links support the authors' tilted-precession interpretation over their wobbling criterion; do not transfer this label to the MU07 D5/D6 pair.",
      "sources": [
        {
          "path": "knowledge/sources/lv-2021-tilted-precession-135nd.md",
          "locator": "LV21-9"
        },
        {
          "path": "knowledge/sources/lv-2021-tilted-precession-135nd.md",
          "locator": "LV21-10"
        },
        {
          "path": "knowledge/sources/lv-2021-tilted-precession-135nd.md",
          "locator": "LV21-11"
        },
        {
          "path": "knowledge/sources/lv-2021-tilted-precession-135nd.md",
          "locator": "LV21-17"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/singh-2016-lifetime-131ce-133pr.md",
      "anchor": "SI16-17",
      "summary": "Persist the direct PDF recheck of Singh 2016 Eq.(1)–(2): its source-specific high-spin K-rotor rate conversion uses Eγ^5 and a CG/K factor multiplying Qt², while nonaxial or mixed-K states replace the single CG factor with a K-amplitude sum. This is an extraction convention, not a transferred 135Nd measurement.",
      "sources": [
        {
          "path": "knowledge/sources/singh-2016-lifetime-131ce-133pr.md",
          "locator": "SI16-17"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/transition-quadrupole-moment.md",
      "anchor": "### Source-specific `K`-rotor rate conversion",
      "summary": "Add a source-specific K-rotor E2-rate formula and its mixed-K replacement to explain why Qt requires a mapped transition, Eγ and applicable rotational matrix element; MU07 Table I and Zhu line crosswalk still do not identify a unique Qt conversion.",
      "sources": [
        {
          "path": "knowledge/sources/singh-2016-lifetime-131ce-133pr.md",
          "locator": "SI16-17"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-11"
        },
        {
          "path": "knowledge/sources/zhu-2003-135nd-composite-chiral-pair.md",
          "locator": "ZH03-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
      "anchor": "CHI01-2",
      "summary": "Record the targeted APS Ref.[16] direct read of level-lifetime-to-partial-lifetime formulas, branch/IC and M1/E2 assumptions, uncertainty boundaries, and one explicitly relative observed-intensity example; none establishes a MU08 absolute per-parent photon ledger.",
      "sources": [
        {
          "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
          "locator": "CHI01-2"
        },
        {
          "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
          "locator": "CHI01-3"
        },
        {
          "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
          "locator": "CHI01-4"
        },
        {
          "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
          "locator": "CHI01-5"
        },
        {
          "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
          "locator": "CHI01-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "[[chiara-2001-108-110in-shears-band-lifetimes]]",
      "summary": "Add the newly verified Chiara 2001 Ref.[16] source entry as a method precedent for lifetime/observed-branch/IC calculations; it does not resolve the 136Nd Table-I branch denominator.",
      "sources": [
        {
          "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
          "locator": "CHI01-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/high-spin-lifetime-strength-deformation.md",
      "anchor": "### Observed-branch method precedent",
      "summary": "Connect Chiara 2001 as a published observed-branch/partial-lifetime method precedent with IC and crossover assumptions, while retaining the boundary that these 108,110In choices do not prove MU08 136Nd absolute photon fractions or unseen-channel completeness.",
      "sources": [
        {
          "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
          "locator": "CHI01-2"
        },
        {
          "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
          "locator": "CHI01-3"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-10"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "anchor": "- [ ] `135Nd` 的 MU07 `B(M1)`、`B(E2)` 表列值与四个带间图点，能否映射为逐线 `(Eγ, Ji→Jf, ΔI, K)` 信息，从而区分同一跃迁的 `δ²`、同自旋强度商和 `Q_t`，且不预设固定 K？MU07 Table I 只按初始自旋列 lifetime/B，图点未逐线绑定；Zhu 2003 Fig.2 给候选连接，LV19 Table I 后续区分同一 initial spin 的 ΔI=1 mixed link 与 ΔI=2 E2 crossover，但仍未确定哪条产生 MU07 的 E2 图点或其 K；图估 B 与表列 B 共享 DSAM 链且无 joint covariance。（opened 2026-10-09；scope: high-spin/135nd/chirality/transition-identity; project: [[nuclear-chirality-and-multiple-chiral-doublet-bands]]; sources: [[mukhopadhyay-2007-135nd-chiral-vibration-static]], [[zhu-2003-135nd-composite-chiral-pair]], [[lv-2019-chirality-135nd-reexamined]], [[lange-kumar-hamilton-1982-multipole-admixtures]])",
      "summary": "Update the open question with the later LV19 same-spin line-class crosswalk: it separates candidate ΔI=1 mixed links from ΔI=2 E2 crossovers but still does not identify which MU07 plotted E2 marker maps to a specific transition or K.",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-11"
        },
        {
          "path": "knowledge/sources/zhu-2003-135nd-composite-chiral-pair.md",
          "locator": "ZH03-3"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-1"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
      "anchor": "MU07-SI-1",
      "summary": "Record the user-authorized official APS supplementary-material check for MU07: no linked SI file was found on the landing/resolver/standard PDF routes; separately hosted author material remains outside the checked endpoints.",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-SI-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
      "anchor": "MU07-13",
      "summary": "Add a rectangular endpoint sensitivity check to the four graph-estimated out/in ratios: the E2 rises are separated through 35/2 but the 35/2–37/2 envelopes overlap, while the M1 envelopes are nonmonotonic. The ranges are not confidence intervals because plot-bar coverage, covariance and systematics are unknown. Retain the 35/2 M1 upper endpoint as 0.0435 = 0.087/2.0 instead of truncating it to 0.043.",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-8"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
      "anchor": "MU07-14",
      "summary": "Add a 39/2− endpoint sensitivity envelope for the matched-spin Table-I B(M1)/B(E2) quotient. The ranges overlap broadly, showing denominator sensitivity only; they are not confidence intervals and add no independent evidence.",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-14"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
      "anchor": "MU08-SI-1",
      "summary": "Record the user-authorized 2026-10-09 official APS supplement-route check for MU08: no linked SI file was found at the article page, resolver, or standard SI endpoint; separately hosted material is not ruled out.",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-SI-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
      "anchor": "MU08-CORR-1",
      "summary": "Record the date-scoped Crossref and APS article-page check: no correction/update relation or correction/erratum link was found on those endpoints; separately indexed notices are not ruled out.",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-CORR-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
      "anchor": "MU07-16",
      "summary": "Add a conditional parent photon-budget consistency diagnostic using existing Table-I lifetimes, graph B components and candidate line energies. Nominal first-two M1 pairs and all candidate E2-crossover pairs exceed1; this rejects only added joint bindings, not author correctness, and neither infers ICC/delta/covariance nor adds independent evidence. Earlier rate transforms remain arithmetic hypotheses, not validated physical series.",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-16"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-11"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-9"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-1"
        }
      ]
    }
  ]
}
```

## Open questions and belief revision

1. **Branch denominator:** MU08 Table-I caption calls the entries branching ratios for transitions depopulating the same level and the following paragraph cites Chiara [16]; printed centers sum to 1. But the MU08 caption/text never states whether the denominator is photon intensities, total transitions including IC, or a complete all-channel inventory. Chiara Ref.[16] now supplies a direct method precedent (partial τ from fitted level τ and observed branches, with IC), but not MU08 line-by-line implementation or an absolute photon-per-parent ledger. Preserve the photon-relative, total-branch and absolute-pγ forward cases; do not reverse-engineer the denominator from quoted B.
2. **Conversion:** target 与其它支路各自的 all-shell `α_eff`、未观测 conversion/electron 通道及绝对 photon ledger 未报告；未来 BrIcc 输入仍须标成条件理论模型。
3. **Joint uncertainties:** τ/branch、branch-branch、energy、feeding 和 stopping covariance/coverage 未给；不得为吻合 author `0.14(2)` 而反解它们。
4. **L4 readiness:** 本地没有独立事件、原始 angle-gated spectra、detector response、stopping/feeding executable inputs 或 covariance，不能重跑 line-shape fit；当前为 L2 source-grounded calculation，不冒充 L4。
5. **Belief revision:** 相较初始 primed recall，主要修正不是公式，而是对 MU08 的应用边界：Table I 的归一化定义未被原文给出。即使 conditional B 重现作者中心值，也不提高绝对 B 的独立证据权重。
6. **Day10 partial:** MU07 Table I 的五个同自旋 B(M1)/B(E2) 中心商、跨带商、四个图估读 out/in ratios 与候选线 rate transforms 已记录。M1 photon-rate out/in 只给 31/2−–35/2− 条件值，37/2− 的 `(556)` 仍 tentative。E2 graph 点有 ΔI=1 mixed-link 与 ΔI=2 crossover 两种 line-class forward 值；MU07 未把点绑定到具体线，故不选唯一 E2 rate series。初版仅用 ΔI=1 能量的 E2 rate 数值已撤回。图误差线覆盖与 numerator/denominator covariance 未知，不能外推 39/2−。MU07 Table I 未逐行指定 B(E2) 最终态/ΔI/K，故不报 source-supported numeric Qt；共同输入派生量不重复计证，跨核素 comparison 也不并成独立测量。Conditional rate values are shared-input transforms, not independent evidence; MU07-16 rejects additional joint same-parent/line/normalization assignments for the nominal first-two M1 pairs and all candidate E2 crossovers, so no displayed series is treated as a verified physical rate series. `135Nd` transition-identity/δ²/Qt question remains tracked in [knowledge/questions.md](../../knowledge/questions.md); no course credit change.

## L0–L4 state

- `L0`: 已按 hash 核验 MU08/LKH82/MU07 原文身份，并直接检查关键表、公式原图。
- `L1`: source→lifetime synthesis link 与同实验依赖关系保持明确。
- `L2`: 完成一条 branch/lifetime/radiative-fraction→B(E2)/RME 条件重构、forward alternative 和不确定度边界。
- `L3`: 未启动；本任务是有界测量链核算，不构建新课题。
- `L4`: not-ready。所需事件/response/feeding/stopping输入和 covariance 不在仓库，未造模拟替代实验。
- Review: 保持 MU08 与 LKH82 页面原有 `unreviewed`/`needs_review`；Codex self-audit 不是人工审核。

## Verification and continuation

入口 boundary/preflight 均 exit 0，protected BibTeX SHA-256 与基线相同。MU07-10 经 line-class crosswalk audit 修订；原 562-page baseline 的 report/writeback/card validators 须在本轮全部修改后重跑。课程 coverage 为 completed [9]/partial [10]/computed next_day_index=10，实际 course state 仍 next_day_index=9/count=8，留待 finalizer。Day11 未开；rate alternatives、superseded calculation audit 与来源映射见 run-01/day10-strength-ratio-preview.json。

18:31 Asia/Shanghai scheduler receipt 记录 normal runner exit 2，错误为 `type object 'datetime.time' has no attribute 'sleep'`：模块 `time` 被 `datetime.time` 名称覆盖。此前首个 continuation returncode 0 已保存在 receipt，但 Python runner 在继续循环前崩溃，receipt remains `running`，课程 state 仍 `next=9/count=8`。已将 runner 的 sleep 调用改用 `time_module`，并加入受保护 `--resume-receipt` recovery mode，仅复用该 receipt 内已有 session ID、原 baseline 与正常 runner的 closeout/writeback/card/state/prompt gates，不创建新 Codex session。18:31 Asia/Shanghai scheduler receipt 记录 normal runner exit 2，错误为 `type object 'datetime.time' has no attribute 'sleep'`；已将 runner 的 sleep module 改为 `time_module`。随后两次 headless same-session resume 因 app-server thread-store active writer 冲突失败；停止 CLI process group后冲突仍由托管 app-server保持，故不再外部重试。课程 state 仍 `next=9/count=8`，receipt 是 `failed-verification` 且pre-closeout。当前继续由本 interactive session做研究；run-local clock PID 181367 真实运行、heartbeat有效，checkpoint-003 queue 于22:36接受，已于13:29在同一 session 处理并写入 observed_clock_executions。

Normal-runner `--finalize-receipt` gate 已增加：要求当前 `CODEX_SESSION_ID` 与receipt一致、时间在15:00–16:00、run-local clock ledger接受closeout event、同session attestation与日报hash一致，并且原baseline/报告/writeback/card/lint/diff全通过；之后仍由canonical updater与prompt preparer负责state和Day10 plan/prompt。当前same-baseline writeback/card/report验证通过，但未到closeout。Day9 credit、Git发布仍未完成。

12:35 Asia/Shanghai 将 same-isotope D1/TiP1/TiP2 的已测 mixing-ratio 模式对照写入现有 synthesis，和 MU07 D5/D6 明确分开；report writeback 增加 LV21-9/10/11/17 locators，review state 原样保留。Report/card/original-baseline validators will run after the current snapshot update; course state remains unchanged.

最新 Runtime snapshot `2026-10-09T13:43:17+08:00`，距硬截止 `76.7` 分钟；研究窗口未关闭，当前只结束已选分析，不开新来源或新卡。15:00 停止新研究并运行 boundary/lint/original-baseline/writeback/card/diff/Gitee H3；只有 normal runner 的 completed receipt 才推进课程 state 与 Day10 计划/prompt。

Precloseout checkpoint 2026-10-09T14:02:59+08:00：report/card/original-baseline writeback 均通过；15个changed knowledge paths全部映射，唯一writeback保留；lint 561 pages / 0 errors / 93 warnings / 1399 info，boundary及diff通过。checkpoint-003已确认，checkpoint-011在14:00 queue accepted，已于14:06左右在同一session收到并确认；时钟保持运行到15:00。当前交还执行权供同session排队提示续接，不等于schedule closeout；state仍next9/count8，不重启daemon。

Checkpoint-011 execution `2026-10-09T14:05:58+08:00`：receipt未完成，已按实际消息确认observed_clock_executions；候选池5项和15个existing atomic locator rows均已核对，未增加scientific claim或新来源/卡。当前只等待15:00同session收束，等待不计研究时长，课程state未推进。


## Closeout

closeout_event_id: `closeout`

The hard cutoff was `2026-10-09T15:00:00+08:00`. Research stopped at the cutoff; subsequent work is closeout only. The original session clock stopped at `14:49` after observing a fresh Farmer manual-attention marker. The same run-local clock was resumed against this receipt and existing session after Farmer reported `running`; it accepted closeout event `closeout` at `2026-10-09T15:07:24+08:00` for the same thread. This is inside the recorded `15:00–16:00` closeout window. Clock acceptance is recorded separately from observed message delivery.

This closeout is bound to session `01a11a87-45cf-7781-a014-f992aafb49e2` and `CODEX_SESSION_ID` matched the receipt. Day9 is the only completed card `[9]`; Day10 remains an uncredited partial `[10]`; Day11 was not studied. Normal-runner final validation, state update, Day10 plan/prompt preparation, explicit-manifest Gitee publication and post-commit reconciliation are recorded in the run receipt and closeout artifacts.
