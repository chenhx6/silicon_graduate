---
type: observable
title: Nuclear excited-state lifetime
aliases: [lifetime, nuclear level lifetime, 激发态寿命]
created: 2026-09-05
updated: 2026-09-05
status: ai-draft
review_status: unreviewed
tags: [lifetime, gamma-spectroscopy, fast-timing, dsam, rdds]
observable_kind: temporal-decay-scale
symbol: tau / T1/2
units: ps, ns, ms, s
---

# Nuclear excited-state lifetime

## Definition

激发态寿命 `τ` 或半衰期 `T1/2` 描述核态衰变时间尺度。由寿命进一步得到 `B(Eλ)`、`B(Mλ)` 或 `Q_t` 时，必须同时记录 feeding、branching、conversion、stopping-power、prompt-response 和模型假设。

## Measurement Routes in This Batch

- LaBr₃(Ce) fast timing / MSCD：[[regis-2011-fast-timing-labr3]]。
- β-γ delayed coincidence / MLH：[[hinke-2010-100sn-decay-spectroscopy]]、[[lubos-2016-100sn-neighboring-nuclei-decay-spectroscopy]]。
- `87Zr` β-γ lifetime：[[qiang-2019-high-spin-130-131ba-87zr]]。
- `237Pu` fission-isomer timing：[[morgan-2008-237pu-nilsson-orbitals]]。

## Evidence Boundary

寿命是电磁强度和集体性的重要约束，但单个寿命值不能独立决定组态、γ 形变、wobbling 或 chirality。不同方法的系统误差和 source independence 必须分开记录。

## How It Is Obtained

可由 fast timing/centroid shift/MSCD、β-γ delayed coincidence、MLH decay-chain fit、RDDS/DDCM、DSAM 或 fission-isomer timing 获得；具体方法和 response/feeding model 必须随数值记录。

## Diagnostic Use

寿命结合 branching、multipolarity 和 transition energy 可约束 `B(Eλ)`、`B(Mλ)`、`Q_t`、集体性和组态变化。

## Model Dependence

由寿命派生的 `B(E2)/B(M1)/Q_t` 依赖 multipolarity、mixing ratio、conversion、feeding、stopping power、prompt response、efficiency 和几何校准。

## Failure Modes and Ambiguities

长 feeding、daughter/background contamination、time walk、deorientation、stopping-power uncertainty、未解析分支和 upper-limit semantics 都可能改变结果；不同实验的寿命不能无条件合并。

## Human Review Triage

### P0

- 使用具体寿命或由其派生的 `B(E2)/Q_t` 前，回到原始 source 核对 locator、feeding 和误差。

### P1

- 区分 fast timing、MLH、RDDS/DSAM 和 fission-isomer timing 的适用条件。

## Sources

- [[regis-2011-fast-timing-labr3]]
- [[hinke-2010-100sn-decay-spectroscopy]]
- [[lubos-2016-100sn-neighboring-nuclei-decay-spectroscopy]]
- [[qiang-2019-high-spin-130-131ba-87zr]]
- [[morgan-2008-237pu-nilsson-orbitals]]
