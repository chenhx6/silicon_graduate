---
type: source
title: "Possible overestimation of isomer depletion due to contamination"
aliases: [Guo 2021 Mo93m contamination, Guo 2021 Nature Matters Arising]
created: 2026-11-07
updated: 2026-11-07
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: comment-article
reading_depth: deep-read
title_original: "Possible overestimation of isomer depletion due to contamination"
authors: [Song Guo, Yongde Fang, Xiaohong Zhou, C. M. Petrache]
journal: Nature
year: 2021
volume: 594
pages: E1--E2 (Critique); E3--E4 (Chiara Reply)
doi: 10.1038/s41586-021-03333-5
language: en
canonical_source: doi:10.1038/s41586-021-03333-5
raw_file: "raw/papers/isomer/isomer_application/nuclear battery/2021_Guo et al_Possible overestimation of isomer depletion due to contamination.pdf"
raw_sha256: 5e98a2700de3c7892fac86abe69475194aa4a7d7b74a2e9608f710c0436a9236
archive_required: true
nuclei: [93mo, 95ru, 92mo]
reactions: ["90Zr(alpha,n)93Mo", "90Zr+12C", "7Li+90Zr"]
observables: [chance-coincidence-rate, background-k-ratio, contamination-peak-intensities]
methods: [pace4-fusion-cross-section-calculation, coincidence-background-reanalysis, spectral-overlay-audit]
tags: [mo93m, neec-critique, contamination, chance-coincidences, background-subtraction-flaw, matters-arising]
---

# Guo et al. (2021): Possible overestimation of isomer depletion due to contamination (plus Chiara et al. Reply)

## Bibliographic Record

The archived 4-page PDF contains two separate publications:
1. **Critique**: Song Guo, Yongde Fang, Xiaohong Zhou, and C. M. Petrache, "Possible overestimation of isomer depletion due to contamination," *Nature* **594**, E1--E2 (2021), DOI: `10.1038/s41586-021-03333-5`.
2. **Reply**: C. J. Chiara, J. J. Carroll, M. P. Carpenter, J. P. Greene, D. J. Hartley, R. V. F. Janssens, G. J. Lane, J. C. Marsh, D. A. Matters, M. Polasik, J. Rzadkiewicz, D. Seweryniak, S. Zhu, S. Bottoni, and A. B. Hayes, "Reply to: Possible overestimation of isomer depletion due to contamination," *Nature* **594**, E3--E4 (2021), DOI: `10.1038/s41586-021-03334-4`.

SHA-256 of combined PDF: `5e98a2700de3c7892fac86abe69475194aa4a7d7b74a2e9608f710c0436a9236`.

## Scope and Reading Depth

Deep reading of the critique (pp. E1--E2) and author reply (pp. E3--E4). Locators examined: Guo et al. Fig. 1 target cross sections (PDF p. 2 / printed p. E2), Guo et al. Fig. 2 background overlay scaled by 1.33 (PDF p. 2 / printed p. E2), and Chiara et al. Reply text and Figs. 1--2 (PDF p. 3--4 / printed p. E3--E4).

## Summary

Guo et al. present a Matters Arising critique of Chiara 2018, arguing that in-beam \(^{90}\text{Zr} + {}^{12}\text{C}\) fusion reactions inside the carbon catcher foils produced \(^{93}\)Mo directly at \(\sim 9.3\text{ kHz}\), and that the prominent 263-keV isomer decay line in prompt gates demonstrated unresolved chance/contamination background. In reply, Chiara et al. disputed that the 263-keV line was isomer decay (attributing it to an unpublished prompt 262-keV ANU transition) and defended chance coincidence estimates of \(0.03\%\) to \(0.08(8)\%\).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| G21-1 | PACE4 calculations indicate 90Zr + 12C reactions in carbon stopper produced 93Mo directly at ~9.3 kHz with ~2 kHz prompt 268-keV flux. | contamination-critique | theoretical calculation | printed p.E1--E2, Fig. 1 | true |
| G21-2 | The 263-keV isomer line appears in prompt coincidence with twice the intensity of the 268-keV peak, indicating random coincidence contamination. | spectral-evidence | re-analysis of published data | printed p.E1 | true |
| G21-3 | Re-scaling background spectra by 1.33 shows all prompt background lines share the same ratio as 268 keV, questioning evidence for 3-sigma NEEC excess. | data-analysis-audit | graphical spectral overlay | printed p.E2, Fig. 2 | true |
| G21-4 | Chiara et al. Reply disputes 263-keV attribution (proposing unpublished prompt 262-keV ANU line) and defends chance rates of 0.03% to 0.08%. | author-rebuttal | published author defense | printed p.E3--E4, Figs. 1--2 | true |

## Competing Interpretations and Limitations

The exchange established two competing interpretations: a contamination critique asserting that prompt reaction feeding accounted for the signal, versus the authors' defense asserting low chance rates and a prompt 262-keV contaminant. The dispute could not be settled from the 2018 data alone, leading directly to the 2022 RIBLL isomer-beam benchmark.

## Extracted Pages

- mo93m
- neec
- contamination-critique
