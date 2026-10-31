---
type: research-note
title: "`135Nd/134Pr` 伙伴带逐线身份与绝对电磁量 ledger"
aliases: [135Nd 134Pr transition identity ledger, partner-resolved EM identity ledger]
created: 2026-10-31
updated: 2026-10-31
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [mukhopadhyay-2007-135nd-chiral-vibration-static, zhu-2003-135nd-composite-chiral-pair, lv-2019-chirality-135nd-reexamined, tonev-2007-134pr-dynamic-chirality, petrache-1996-rotational-bands-134pr]
created_from: "2026-10-31 P3 transition-identity audit"
promotion_target: "post-30-day-nuclear-structure-paper-prospectus"
scope: 135nd/134pr/transition-identity/absolute-electromagnetic-strength
nuclei: [135nd, 134pr]
observables: [transition-energy, spin-parity, multipolarity, lifetime, b-e2, b-m1, branching]
tags: [135nd, 134pr, transition-identity, partner-bands, covariance, l3-readiness]
---

# `135Nd/134Pr` 伙伴带逐线身份与绝对电磁量 ledger

## Research Trigger

`135Nd` 的 MU07 数值主要按初始自旋列出，而 ZH03/LV19 提供不同层级的逐线身份；
`134Pr` Tonev07 提供更完整的逐线表。若不分层，伙伴带比较会误绑 `Eγ`、终态和
绝对强度。

## Grounded Evidence

本页使用 MU07、ZH03、LV19、Petrache96 和 Tonev07 的具体表格与图谱系。

## Purpose

本页冻结 `135Nd` 与 `134Pr` 伙伴带比较时的字段语义和来源谱系。它的首要作用是
防止把“按初始自旋列出的状态级 `τ/B`”误写成逐线 `Eγ–J_i→J_f` 记录，也防止把
同一实验的详细报告当成独立复测。它是 L3 identity ledger，不是新的拟合或手征
模式裁决。

## Field Semantics

- `τ_i` 是初态平均寿命，除非原表明确说明，否则不是某一条 γ 线的独立寿命；
- `B(M1)`、`B(E2)` 只有在原表明确绑定到同一 transition row 时才可逐线使用；
- `M1+E2` 只表示混合多极性类别，没有 `δ` 或成分分解时不能拆成两个独立 `B`；
- 空白、括号、上限和 `Seen` 必须保留原语义，不能补成零或确定值；
- 近似能量不能自动绑定终态、母态或多极性。

## Provisional Reasoning

将 `135Nd` 保持为 state-level 与 line-level 两层、将 `134Pr` Tonev07 行作为
身份控制，可以减少重复算术，但不能自动提供共同 covariance 或机制裁决。

## `135Nd`: State-Level Rows from MU07

MU07 Table I gives band, initial spin, lifetime and derived `B(M1)`/`B(E2)` rows.
It does not provide a complete `Eγ`, final-spin and component ledger. Therefore the
following values are state-level strength rows:

| Initial spin | Band | `τ_i` (ps) | `B(M1)` (`μN²`) | `B(E2)` (`e²b²`) | line identity |
|---|---|---:|---:|---:|---|
| `31/2−` | A | `0.75(8)` | `2.5(3)` | `0.32(3)` | not bound |
| `33/2−` | A | `0.44(2)` | `2.2(2)` | `0.32(3)` | not bound |
| `35/2−` | A | `0.28(2)` | `2.4(3)` | `0.32(3)` | not bound |
| `37/2−` | A | `0.23(2)` | `1.7(3)` | `0.32(4)` | not bound |
| `39/2−` | A | `0.22(2)` | `2.1(3)` | `0.13(3)` | not bound |
| `31/2−` | B | `1.46(2)` | `2.7(3)` | `0.28(3)` | not bound |
| `33/2−` | B | `0.87(6)` | `2.1(2)` | `0.28(3)` | not bound |
| `35/2−` | B | `0.64(5)` | `2.2(2)` | `0.28(4)` | not bound |
| `37/2−` | B | `0.48(3)` | `1.7(2)` | `0.29(4)` | not bound |
| `39/2−` | B | `0.24(4)` | `1.9(3)` | `0.11(3)` | not bound |

MU07 Fig. 1 supplies two line-shape examples, `494 keV` for Band A
`43/2−→41/2−` and `440 keV` for Band B `39/2−→37/2−`. These two examples do not
bind every Table I strength row to those specific transitions. The source boundary is
[[mukhopadhyay-2007-135nd-chiral-vibration-static]] `MU07-1`–`MU07-3`,
`MU07-8`–`MU07-11`.

## `135Nd`: Identity Crosswalk from ZH03 and LV19

ZH03 Fig. 2 provides a historical Band A/B topology. Its arrow thickness is relative
intensity, not an absolute `B` value:

| Historical link | `Eγ` | `J_i→J_f` | safe multipolarity statement | status |
|---|---:|---|---|---|
| B→A | `648` (text also `649`) | `31/2−→29/2−` | `ΔI=1`; mixed class may be retained, `δ` absent | identity bound, energy version retained |
| B→A | `639` | `33/2−→31/2−` | `ΔI=1`; no independent closure | topology bound |
| B→A | `591` | `35/2−→33/2−` | `ΔI=1`; no independent closure | topology bound |
| B→A | `(556)` | `37/2−→35/2−` | `ΔI=1`; tentative | candidate only |
| B→A | `896` | `31/2−→27/2−` | `E2`; forward/90° ratio reported | identity and E2 bound |
| B→A | `930` | `33/2−→29/2−` | no independent closure | topology candidate |
| B→A | `949` | `35/2−→31/2−` | no independent closure | topology candidate |
| B→A | `(963)` | `37/2−→33/2−` | tentative/weak | candidate only |

LV19 Table I provides a later D5/D6 line ledger:

| `Eγ` | `J_i→J_f` | multipolarity field | safe use |
|---:|---|---|---|
| `648.9` | `31/2−→29/2−` | `M1/E2` | line identity and class |
| `640.2` | `33/2−→31/2−` | `M1/E2` | line identity and class |
| `591.4` | `35/2−→33/2−` | blank | endpoint only |
| `896.8` | `31/2−→27/2−` | `E2` | identity and E2 |
| `931.3` | `33/2−→29/2−` | `E2` | identity and E2 |
| `949.6` | `35/2−→31/2−` | `E2` | identity and E2 |
| `963.0` | `37/2−→33/2−` | `E2` | identity and E2 |
| `591.8` | `35/2−→31/2−` | blank | separate line; no inferred E2 |
| `681.0` | `37/2−→33/2−` | blank | no inferred E2 |
| `812.0` | `39/2−→35/2−` | blank | no inferred E2 |

The `591.4` and `591.8 keV` lines have different final states and must remain separate.
LV19's absolute strengths refer back to the MU07 campaign; they are not a new absolute
`B(M1)/B(E2)` measurement. See [[zhu-2003-135nd-composite-chiral-pair]]
`ZH03-1`–`ZH03-8` and [[lv-2019-chirality-135nd-reexamined]] `LV19-*`.

## `134Pr`: Rows That Can Be Used Line by Line

Tonev07 Table I/II gives an unusually complete line-level ledger. The following
same-band E2 rows can safely enter a partner-band comparison:

| `J_i→J_f` | `Eγ` | `τ_i` (ps) | `B(E2)` (`e²b²`) |
|---|---:|---:|---:|
| `14_1^+→12_1^+` | `811.5` | `0.882(147)` | `0.153(21)` |
| `15_1^+→13_1^+` | `890.3` | `0.608(68)` | `0.148(21)` |
| `16_1^+→14_1^+` | `975.6` | `0.562(47)` | `0.115(19)` |
| `17_1^+→15_1^+` | `1026.8` | `0.422(30)` | `0.108(22)` |
| `14_2^+→12_2^+` | `661.0` | `1.280(50)` | `0.039(19)` |
| `15_2^+→13_2^+` | `705.8` | `0.887(47)` | `0.089(20)` |
| `16_2^+→14_2^+` | `768.4` | `0.824(52)` | `0.050(18)` |
| `17_2^+→15_2^+` | `872.0` | `0.353(49)` | `0.047(17)` |

The mixed `ΔI=1` rows can bind `B(M1)` to the source transition row without splitting
the E2 component:

| `J_i→J_f` | `Eγ` | `τ_i` (ps) | `B(M1)` (`μN²`) | E2 component |
|---|---:|---:|---:|---|
| `14_1^+→13_1^+` | `395.3` | `0.882(147)` | `0.419(85)` | unresolved |
| `15_1^+→14_1^+` | `495.3` | `0.608(68)` | `0.290(80)` | unresolved |
| `16_1^+→15_1^+` | `480.6` | `0.562(47)` | `0.146(70)` | unresolved |
| `17_1^+→16_1^+` | `546.1` | `0.422(30)` | `0.194(70)` | unresolved |
| `14_2^+→13_2^+` | `337.0` | `1.280(50)` | `0.678(100)` | unresolved |
| `15_2^+→14_2^+` | `368.8` | `0.887(47)` | `0.472(90)` | unresolved |
| `16_2^+→15_2^+` | `399.6` | `0.824(52)` | `0.333(75)` | unresolved |
| `17_2^+→16_2^+` | `472.0` | `0.353(49)` | `0.545(67)` | unresolved |

Tonev07 also gives explicit interband E2 rows:
`13_2^+→11_1^+` at `944.0 keV`, `14_2^+→12_1^+` at `975.1 keV`,
`15_2^+→13_1^+` at `927.2 keV`, `16_2^+→14_1^+` at `931.0 keV`, and
`17_2^+→15_1^+` at `907.8 keV`, with source Table I/II values. They must remain
separate from same-band E2 rows. See [[tonev-2007-134pr-dynamic-chirality]]
`TO07-D24-002`–`TO07-D24-007`.

## Identity Hazards and Lineage

1. MU07 graph points are not line-level `B` values; do not bind them to `648`, `896` or
   any other `Eγ` without an explicit producer table.
2. Preserve `648/649`, `591.4/591.8` and the tentative `(556)/(963)` versions.
3. `135Nd` uses ZH03 Band A/B and later LV19 D5/D6; do not rewrite the historical labels.
4. Tonev06 and Tonev07 are one `134Pr` experimental lineage; Tonev07 is the detailed
   report, not a second independent lifetime/B measurement.
5. `134Pr` mixed `ΔI=1` rows have a source multipolarity class but no safe δ decomposition.
6. Tonev07's `τ(15_2)=0.887(47) ps` table value and its `0.897(47) ps` prose value are
   an unresolved internal version conflict; preserve the table value with a note.
7. Shared DSAM/RDDS stopping, feeding, branch and normalization nuisance are not
   supplied as a joint covariance. Ratios are conditional and cannot be treated as
   independent Gaussian votes.

## Next Evidence

- `135Nd`: recover the MU07 producer-level mapping from plotted points to parent,
  final state, component, branch and covariance; LV19 is an identity control, not an
  absolute-strength replacement.
- `134Pr`: archive the Tonev07 primary PDF and obtain branch/feeding nuisance and mixed
  `M1/E2` covariance.
- Before any partner fit, freeze version conflicts and source lineage; do not increase
  precision by reading more pixels from unresolved plots.

## Knowledge Impact and Learning Decision

`supports`: P3 remains a viable partner-resolved EM benchmark only if `135Nd` is kept
state-level until the producer mapping is recovered; `134Pr` supplies the stronger
line-level control ledger.

`limits`: this page does not create missing `135Nd` transition identities, convert
relative intensities into absolute strengths, or claim a static-chirality verdict.

`revises`: future P3 analysis must use line identity as a hard gate before comparing
`B(E2)`, `B(M1)`, `δ` or partner ratios.

## Assumptions

表格中的 `B`、`τ`、相对强度和多极性按各 source 原始语义保留；没有 producer、
branch 或 covariance 时不进行逐线反演。

## Competing Explanations

近简并和相似 `B(E2)/B(M1)` 可由动态手征、crossing、configuration mixing、形状
涨落或实验归一化差异产生。ledger 只解决身份，不解决机制。

## Transfer Conditions

本 ledger 可迁移到其它伙伴带，前提是保留 source lineage、版本差异、状态级/逐线
区分和共同 feeding/covariance 边界；本页数值不能跨核素复制。

## Failure Conditions

若多条近能量线、图点缺 branch 或 source 版本冲突未闭合，停止逐线绑定；若绝对
`B` 的生产者和共享 nuisance 不明，停止 partner ratio。

## Falsification or Reverse Tests

若取得 producer-level mapping 后，MU07 图点能在共同 response/Cov 合同下唯一绑定
到某一条 transition，才可升级相应行；若多个 mapping 都能解释图点，保留 identity
non-identifiability。

## Open Questions

- 能否恢复 MU07 的完整 line/branch producer mapping？
- LV19 的 selected-event response 能否约束 MU07 图点而不重复计作绝对强度？
- Tonev07 的 branch/feeding covariance 和 mixed `M1/E2` 成分是否可取得？
- 如何在保留 `648/649`、`591.4/591.8` 和 `τ(15_2)` 版本冲突下进行 partner fit？

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-10-31 | P3 transition-identity audit | none | provisional L3 ledger | MU07 is state-level while Tonev07 supplies stronger line-level rows; covariance remains missing | [[post-30-day-nuclear-structure-paper-prospectus]] |

## Human Review

Codex self-audit; `review_status: unreviewed`, `reasoning_status: provisional`.
