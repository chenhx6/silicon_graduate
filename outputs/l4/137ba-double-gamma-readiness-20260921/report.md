---
type: l4-readiness-audit
unit_id: 137ba-double-gamma-readiness-20260921
created: 2026-09-21
updated: 2026-09-21
status: not-ready
review_status: unreviewed
---

# L4 readiness audit: `137Ba` competitive double-γ path re-fit

## Question

Can the Walz 2015 and Söderström 2020 `137Ba` measurements be re-fitted jointly to test whether the E3M1/M2E2 ranking survives a common response and covariance treatment?

## Public-input check

- Söderström 2020 is openly readable and points to Mendeley Data DOI `10.17632/skhmjshxdj` for final points.
- On 2026-09-21 the DOI endpoint returned HTTP 404. The Mendeley landing endpoint returned HTML whose embedded dataset state says that no snapshot exists for `skhmjshxdj` at any version.
- The same article states that raw data and sorting codes are available from the authors on reasonable request; no public response matrix or covariance package was found in the checked route.
- Walz 2015 provides published spectra/plots and supplementary equations, but not a complete event-level response package.

## Readiness matrix

| Requirement | State | Consequence |
|---|---|---|
| Data identity and article provenance | available | Can define the literature question and preserve experiment independence. |
| Final plotted/summary points | partial | Supports qualitative comparison only. |
| Complete event or tabulated energy-sharing/angular observations | missing | No common likelihood can be reconstructed. |
| Detector response, efficiency and background templates | missing | Cannot propagate acceptance/systematic effects. |
| Joint covariance and fit code | missing | Cannot reproduce the reported χ² contours or test branch correlations. |
| Negative/random-window controls | partial in article, not machine-readable | Cannot rerun the failure checks. |

## Decision and stop reason

`not-ready` / `safe-suspended-input-limited`. No L4 analysis, digitization-as-data, or pseudo-result is created. Figure digitization could make a descriptive plot, but it would not meet the Wiki L4 contract because response and covariance are absent and would create false precision.

## Re-entry condition

Reopen only after a valid public snapshot or author-supplied package contains the observations, units, uncertainties/covariance, response/background treatment and executable analysis path. Until then the L3 conclusion remains: energy sharing is the decisive published discriminator, but a common response-aware re-fit is unverified.

## Provenance

- [[soderstrom-2020-137ba-competitive-gamma]]; PDF p.7, Data/Code availability.
- [[walz-2015-competitive-double-gamma-137ba]]; Supplement HS-116, pp.1–14.
- `outputs/high-spin-reconciliation-20260921/external-research/EXT-20260921-002.json`.
