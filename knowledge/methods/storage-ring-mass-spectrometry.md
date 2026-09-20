---
type: method
title: 存储环质量与等时飞行谱学
aliases: [storage-ring mass spectrometry, isochronous mass spectrometry, Schottky mass spectrometry, S+IMS]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
method_type: storage-ring-spectroscopy
tags: [storage-ring, isomer, lifetime, Schottky, IMS]
---

# 存储环质量与等时飞行谱学（Storage-Ring Mass Spectrometry）

## Purpose

利用离子在存储环中的回旋频率与非破坏性 Schottky 信号，测量高电荷态核素的质量、低能异构态激发能和毫秒至秒级寿命。

## Inputs and Assumptions

Known ring transition energy `γt`, controlled velocity/momentum spread, charge state, frequency calibration, ion-loss stability and a resolved isomer/ground-state frequency doublet.

## Procedure

Inject fully stripped fragments, tune the ring to isochronous mode, record Schottky spectra continuously, align frequency traces, fit peak areas versus time, and convert laboratory decay constants to rest-frame half-lives with the Lorentz factor.

## What It Can Establish

Nondestructive isomer populations, excitation energies and partial decay half-lives without foil-detector losses or γ-ray background.

## What It Cannot Establish Alone

It measures total population decay and mass/frequency observables; it does not by itself identify multipole composition, angular correlations or separate E1/M1/E2 polarizabilities.

## Supporting Evidence

[[freirefernandez-2024-isolated-two-photon-72ge]] demonstrates S+IMS for the isolated 2γ decay of bare `72Ge32+`.

## Counter-evidence and Competing Interpretations

Ion losses, unresolved contaminants, frequency drift and incomplete decay branches can mimic population changes; multipole decomposition requires independent γ/angular or model constraints.

## Sources

- [[freirefernandez-2024-isolated-two-photon-72ge]]
