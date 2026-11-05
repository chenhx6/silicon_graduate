---
type: plan
title: "131Xe 794-keV 宇称与 882-keV 双根响应闭合束流申请初稿"
created: 2026-11-01
updated: 2026-11-01
status: draft
---

# `131Xe` 794-keV 宇称与 882-keV 双根响应闭合束流申请初稿

## Physics case

`130Te(α,3n)131Xe` 已有 38-MeV INGA 数据，但同一 acquisition 的后续重分析仍留下
794-keV 宇称版本和 880/882-keV mixing-ratio 双根。申请的核心假设是：把
角分布/偏振、K 壳电子/γ 比和 partner-resolved lifetime 放进同一 response contract，
可以把“核结构分支”与“alignment/feeding/response 差异”分开。

The explicit alternative is that the current ambiguity survives even after the response
and companion observables are measured; that outcome is a useful identifiability result.

## Reaction and target

- Candidate reaction: `130Te(α,3n)131Xe`, using the established enriched-`130Te` target
  and 38-MeV beam family from the primary experiment.
- Beam-energy scan: reproduce the known channel first, then scan around the channel
  maximum after an evaporation-code calculation; do not assume the old optimum is the
  new optimum for electron/polarization hardware.
- Target audit: thickness, backing, stopping, heat load, target contamination and beam
  energy loss must enter the response manifest.

## Required observables

1. `794.8-keV` target line and the `795-keV` E1 control with K-shell electron/γ response.
2. `880.1/881.8-keV` branches with gate-resolved peak shape, sideband and random windows.
3. `642-keV` known E2 control for angular acceptance and polarization sign.
4. `704.6-keV` same-parent/feeding control, used only under a declared gate contract.
5. `813/450` companion lines as predeclared cross-checks after transition identity is frozen.
6. One partner-resolved lifetime or absolute branch normalization tied to the 1046-keV
   parent, with feeding and side-feeding recorded.

## Detector configuration

- Compact IMP-DRAGON HPGe+BGO core for weak cascade efficiency and Compton suppression.
- Four or more clover HPGe units at calibrated angular rings for linear polarization and
  selected angular distributions.
- LaBr3(Ce) fast timing units for lifetime/feeding timing where the line intensity permits.
- Silicon/recoil or evaporation-particle tag if γ gates alone do not close channel identity.
- Calibrated K-electron module with transport map, threshold scan and random-electron
  control; this subsystem is essential to the parity branch test.
- Unified list-mode timing: HPGe, BGO, clover scatter, LaBr3, electron and particle
  channels must retain run ID, timestamp, deadtime/livetime and calibration version.

## Analysis contract

- Primary fit: count-level Poisson likelihood for peak/sideband/random windows, with
  detector response, efficiency, feeding, alignment, deadtime and shared calibration
  covariance profiled.
- Secondary fit: summary-level Gaussian contract only if raw counts are unavailable;
  every compressed observable must carry its joint covariance and source lineage.
- Branch parameter: signed `δ` or bounded `ξ=arctan(δ)`; do not replace it with `δ²`
  before the polarization/angle likelihood has used the interference sign.
- Holdout: predeclare `813` as the main holdout and `450` as sensitivity line; they cannot
  be used to tune the primary 747/882 branch model.
- Negative controls: empty/random gates, no-electron gates, known E2 polarization, BGO
  veto-on/off, and an energy-sideband response check.

## Belief revision

| Result | Revision |
|---|---|
| 794 response separates the parity hypotheses and 882 branches remain separated after nuisance profiling; lifetime/absolute EM holdout agrees | Raise the corresponding branch/identity hypothesis; retain a conditional mode interpretation |
| 794 ICC convex hull overlaps or 882 branches overlap after full response | Keep parity and δ unresolved; the experiment demonstrates a readiness boundary |
| Gate, deadtime, feeding or electron response changes the branch ranking | Revise the response/lineage model before making a nuclear-structure claim |
| Absolute EM contradicts the selected branch | Lower the branch and test signature-partner/configuration-mixing alternatives |

## Beam-time and calibration request

The request should include dedicated calibration and control runs for:

- energy/efficiency and BGO veto;
- clover polarization analyzing power and axis sign;
- electron transport and K-shell efficiency;
- LaBr3 timing response and walk correction;
- particle/recoil identity and target energy loss;
- empty/random/sideband backgrounds.

The number of physics shifts must come from the rate/response pilot. This draft deliberately
does not invent a cross section, peak count, statistical significance or guaranteed beam
time.

## Go/no-go gates

- **Go:** transition identity, known-channel production, detector response, electron
  efficiency, polarization calibration and a usable lifetime/absolute-EM companion are
  all demonstrable in pilot data.
- **Pause:** any missing raw response, joint covariance, or partner-lifetime input leaves
  the result at L3/readiness.
- **Reject the mode claim:** if all observables are measured but competing response-folded
  predictions remain overlapping, report non-identifiability rather than force a label.

## Current status

This is a provisional beam-application draft derived from the existing `131Xe` source
lineage and Day29 design contract. It is ready for a rate model, detector geometry model
and collaboration-specific resource estimates; it is not a submitted proposal or an
experimental result.
