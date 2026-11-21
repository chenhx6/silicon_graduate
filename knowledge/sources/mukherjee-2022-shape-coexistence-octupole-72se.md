---
type: source
title: "Mukherjee et al. 2022 - Shape coexistence and octupole correlations in 72Se"
aliases: [Mukherjee 2022 72Se]
created: 2026-11-11
updated: 2026-11-11
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Shape coexistence and octupole correlations in 72Se"
year: 2022
journal: "Physical Review C"
volume: 105
pages: "014322"
doi: "10.1103/PhysRevC.105.014322"
canonical_source: "A. Mukherjee et al., Physical Review C 105, 014322 (2022)"
citation_key: mukherjee2022se72
raw_file: "raw/papers/gpt/query/20261111-delta-pilot-se72/Mukherjee2022_PhysRevC.105.014322.pdf"
raw_sha256: "b0712efd113f42aa65dfb3fe92783bf75428097c45b2803cfb69dcde4c22ec97"
archive_required: true
nuclei: [72Se]
tags: [72Se, mixing-ratio, angular-distribution, polarization, alignment]
---

# Shape coexistence and octupole correlations in 72Se

## Bibliographic Record

Published PRC PDF, DOI10.1103/PhysRevC.105.014322; local original and acquisition manifest under `raw/papers/gpt/query/20261111-delta-pilot-se72/`.

## Scope and Reading Depth

2026-11-21 已对账出版版 14 页，覆盖实验、能级纲图、角分布与极化方法、形状共存和八极关联讨论、TRS/CSM 计算及书目。早期 Gemini 回执仅覆盖下述定向数据提取，本轮的整源账本归 Codex。

Gemini extracted the experimental mixing-ratio passages; parent checked identity on p.1, angle/matrix definitions on p.3, TableI on p.5 and method/result passages on pp.7-9. This is targeted reading for E2/M1 extraction, not a full audit of the structure or theoretical calculations.

## Summary

The paper reports mixed transitions in72Se using DCO, ADO and clover asymmetry measurements. The454.5-keV2+2 to2+1 transition has delta=-5(3) from RDCO-polarization analysis. The magnetic-substate width sigma/j=0.3 is calculated from E1 reference transitions within the same experiment, then used as a fixed value.

## Experimental or Theoretical Setup

The50Cr(28Si,alpha2p)72Se experiment uses90MeV beam and INGA clovers. Detectors occur at32,57,90,123,148degrees. DCO matrix148by90 differs from ADO matrices148/all-other and90/all-other (p.3). BandB andC angular ratios use976.7 and862.0-keV quadrupole gates respectively (p.6). Polarimetry uses90degree clovers, P=Delta/Q; Q is calibrated from pure Kr transitions in the same reaction (TableII,pp.6-7).

## Key Results

| Claim | claim_kind | evidence_level | locator | Boundary |
|---|---|---|---|---|
|454.5-keV2+2 to2+1: RDCO=.82(.15), Rtheta=1.73(.22), asymmetry=.058(.039)|reported measurement| direct |TableI,p.5|Rtheta is an ADO ratio; Delta is not already P.|
|delta=-5(3) for454.5keV|experimental extraction| direct |p.7;Fig.7,p.8|Offsets3 give[-8,-2]; precise interval confidence not stated in inspected passage.|
|sigma/j=.3 calculated from879.0,1338.5,1536.0-keV E1 transitions|method condition| direct |p.7|Classify FIX_CALIBRATED, not an unsupported assumed0.3. No calibration uncertainty is supplied in that paragraph.|
|1136.1-keV2+3 to2+1: RDCO=1.12(.18),Rtheta=1.87(.22),asymmetry=.127(.089)|reported measurement| direct |TableI,p.5|Reported observables do not alone establish the exact delta extraction pipeline.|
|delta=-.10(.24) for1136.1keV|reported result, origin unresolved| direct |p.9,Sec.IV.B|The sentence calls it observed mixing ratio. It does not explicitly attribute this value to Ref42; absence of a separate chi2 curve is not proof it is adopted.|

## Authors' Interpretation

The large absolute delta of454.5keV is interpreted as predominantly E2. The paper compares its result with an earlier+11(+11,-4) value attributed to McCutchan et al. Ref42 (p.8). These are different reported results; this source page does not adjudicate the discrepancy or reinterpret all structure claims.

## Competing Interpretations and Limitations

Fixed alignment can be calibrated experimentally or assumed; these should remain separate in a methods survey. The observed1136.1-keV delta's origin and detailed fitting conditions remain unresolved in this targeted reading. Do not assign it the454.5-keV fitting contract merely because both lines occur in one experiment. The1571.3-keV parity-changing transition is excluded from the E2/M1 workbook.

## Related Knowledge

- [[delta-alignment-extraction-pilot-20261110]]: workbook revision and methods comparison.

## Extracted Pages

- E2/M1 result records and experimental conditions are retained in the four-nucleus workbook, with the canonical source-linked interpretation in [[delta-alignment-extraction-pilot-20261110]].
- No new nucleus or theory page is inferred from this targeted extraction.

## 2026-11-21 — 取向标定、极化输入和结果范围

- 014322-3 的 DCO 矩阵用 148° 和 90° 两臂，\(R_\theta\) 取自按 148° 或 90° 观察其余探测器符合的两套 ADO 矩阵。454.5 keV 的联合拟合明确使用 \(R_{\rm DCO}=0.82(15)\) 与线偏振，\(R_\theta=1.73(22)\) 是同表另列的角比。
- 014322-7 在联合拟合前由 879.0、1338.5、1536.0 keV 的 E1 参考线定出 \(\sigma/j=0.3\)，随后写明用 ANGCOR 在 \(-50\le\delta\le50\) 改变 \(\delta\) 并极小化 \(\chi^2\)。其取向是定标后固定宽度，文中未列宽度的不确定度。图 7（014322-8）得到 \(\delta=-5(3)\)。
- Table I 的 \(\Delta=0.058(39)\) 是 454.5 keV 的偏振不对称度。以式 (4)–(5) 的中心参数算得 \(Q=0.33238\)，故 \(\Delta/Q=0.17450\)，与图 7(a) 红点位置相符。这里的数值来自公式和原表联合换算，原文只在图 7(a) 直接展示该 \(P\) 及误差棒。不能从换算中心值补出原始极化误差与角比的协方差。
- 014322-8 的 \(B(E2;2_2^+\to2_1^+)=108(5)\) W.u. 使用本篇混合比、分支与既有寿命。014322-11 Table III 的八极讨论所用 \(B(E1)\) 也引用既有寿命。将它们保留为依赖不同输入的强度结果，1136.1 keV 的 \(\delta=-0.10(24)\) 仍按原文记录，具体拟合过程未给。
