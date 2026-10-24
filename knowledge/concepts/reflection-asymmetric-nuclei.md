---
type: concept
title: "Reflection-Asymmetric Nuclei"
aliases: [reflection-asymmetric nuclei, reflection asymmetry]
created: 2026-07-13
updated: 2026-07-13
status: ai-draft
review_status: unreviewed
concept_type: nuclear-shape-symmetry
confidence: low
tags: [reflection-asymmetry, octupole, parity]
---

# Reflection-Asymmetric Nuclei

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Definition

A reflection-asymmetric mean field has nonzero odd-multipole moments, especially an electric octupole moment. In a rotating system, the orientation of the angular-momentum vector relative to the asymmetric density determines additional discrete-symmetry classes and parity patterns.

## Experimental Connections

Fast E3 or E1 transitions and parity-doublet structures are discussed as possible consequences. They are evidence for a reflection-asymmetric interpretation only when combined with configuration, energy and transition-systematics checks.

## Boundary

Octupole correlations or softness do not automatically establish a stable reflection-asymmetric minimum. Mean-field order parameters and cited examples from reviews must be kept separate from directly measured transition strengths.

## Necessary Assumptions

- Odd-multipole moments, parity structure and angular-momentum orientation are specified in a model or measured through suitable transition data.
- Reflection-asymmetric correlations are distinguished from a static octupole minimum.

## Discriminating Observables

E1/E3 strengths, parity-doublet spacing, spin dependence and configuration systematics can constrain the interpretation.

## Supporting Evidence

- [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]
- [[reflection-symmetry-breaking]]

## Counter-evidence and Competing Interpretations

Octupole softness, vibrational correlations and configuration mixing can produce parity-related patterns without stable reflection asymmetry.

## Our Current Position

Use reflection-asymmetric language only at the strength supported by direct transition and model evidence.

## Sources

- [[gaffney-2013-pear-shaped-rn-ra]]
- [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]
- [[reflection-symmetry-breaking]]

## Review Status

New concept page; review pending.

## Day 21 Checkpoint 022 证据门量化审计：反射不对称核与静态梨形判定准则

依据推断阶梯方法论（[[experimental-claim-boundaries]]）及独立量化程序 day21_checkpoint022_rn220_ra224_octupole_audit.py（产物 outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/rn220-ra224-octupole-audit-022.json），对反射不对称核的实验判定确立核心证据门规则：

1. **增强 B(E3) 的非排他性：**
   单一基态 B(E3) ~ 30–50 W.u. 的集体增强无法区分静态梨形极小与动态八极软振动（Gaffney 2013 GA13-6 原文明确界定）。
2. **正负宇称带交错能级位移 delta E(I) 趋零准则：**
   确证静态反射不对称形变必须满足交错宇称带能量位移随自旋快速向零收敛（delta E(I) -> 0，如 224Ra 降至 <20 keV）；若能级位移长期维持在数百 keV（如 220Rn 维持在 >140 keV），排他性归属于动态八极振动。
3. **内禀电八极矩 Q3 随自旋平坦守恒：**
   静态梨形转子要求内禀 Q3(I) 在全带保持恒定，离心衰减指示八极振动的非绝热猝灭。
