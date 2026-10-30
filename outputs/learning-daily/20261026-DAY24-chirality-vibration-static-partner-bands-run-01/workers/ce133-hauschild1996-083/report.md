# Day24 / 083 — Hauschild et al. 1996 PRC 54, 613–619 (1996Ha20)

## Decision

**The paper is a high-value same-data follow-up to Hauschild 1995, not an
independent event sample.** It searches the 133Ce Gammasphere matrix used for
the three 1995 superdeformed (SD) bands and reports six additional
`Delta E_gamma ~ 100 keV` rotational sequences (bands 2–7 in this paper, with
band 1 already known from Ref. [7]). It adds alignment/backbend systematics,
conditional crossing assignments and a normal/deformed shape-coexistence
discussion. It does not add a lifetime, a new absolute quadrupole measurement,
or a completed normal-to-new-band linking network.

The 1996 article and 1995Ha34 have the same reaction, target, detector and
event totals, and 1996 explicitly says the six sequences are extracted “in
addition to the three superdeformed bands reported in [11]”, where [11] is
Hauschild 1995. Treating their numbers as independent experimental evidence
would double-count the same high-fold data. Joss 1998 is experimentally
independent (100Mo(36S,xn), DSAM/DBLS), although author and model lineage
overlap and Joss cites this paper.

## Source identity, acquisition and reading scope

- K. Hauschild, R. Wadsworth, R. M. Clark, I. M. Hibbert, P. Fallon,
  A. O. Macchiavelli, D. B. Fossan, H. Schnare, I. Thorslund, P. J. Nolan,
  A. T. Semple and L. Walker, “Triaxial bands in 133Ce”, *Physical Review C*
  **54**, 613–619 (1996), DOI `10.1103/PhysRevC.54.613`.
- The official APS PDF was already present in the authorized staging area:
  `tmp/day24-ce133-independent-primary-079/1996Ha20-aps.pdf` (7 pages,
  229,413 bytes, SHA-256
  `560215bbff5898a3e304f4219f35f628b3a4bd03c87ed1745dc25ae147162872`).
  OCR is `1996Ha20.txt` (SHA-256
  `c4698adcee37a7911cff58624558b09a1a7044278bef17d4ff7a68b39992e5a2`).
- I read all printed pages 613–619 and visually inspected Figs. 1–9
  (`Ha20-page01.png`–`Ha20-page07.png`). No Supporting Information or author
  producer/model code was identified. The conclusions below are restricted to
  the article and its figures; no reconstruction of the cranked Woods–Saxon
  calculation was run.

## Atomic evidence ledger

All entries remain `needs_review: true` for the knowledge layer; they are
source-grounded worker findings, not user-reviewed claims.

| ID | Direct report or author interpretation | Locator | Boundary |
|---|---|---|---|
| HA96-083-01 | High-spin 133Ce was populated with `116Cd(22Ne,5n)` at 120 MeV on two 500 μg cm−2 self-supporting targets; early Gammasphere had 31 large-volume (75–80% efficient) Compton-suppressed HPGe detectors. | PDF p.1 (printed 613)–p.2 (614); OCR lines 55–67, 84–93 | Direct apparatus/reaction report; no raw cube or efficiency covariance supplied. |
| HA96-083-02 | The event stream is ~`1.5×10^9` suppressed Ge-fold >3 events and ~`3.5×10^9` unpacked triples, sorted into Eγ1–Eγ2 matrices and a RADWARE cube. | PDF p.2/614; OCR 84–94 | Same numerical stream as 1995Ha34; establishes data dependence, not a new sample. |
| HA96-083-03 | Six weak rotational sequences with `ΔEγ≈100 keV` were extracted in addition to the three SD bands reported in 1995Ha34 [11]; the new sequences are assigned to 133Ce by coincidences with known low-lying transitions. | PDF pp.2–3/614–615, Figs.1–3; OCR 98–110 | New lattice-search result in the same matrix; relative populations only. |
| HA96-083-04 | Relative populations are ~10% (band 1), ~2% (band 2), ~1.5% (band 4), and ~0.5% each for bands 3, 5, 6 and 7. | PDF p.2/614; OCR 92–98 | Single-gate estimates relative to total 133Ce population, not absolute cross sections. |
| HA96-083-05 | Some sequences backbend near `ħω≈0.6 MeV` and are observed to `ħω≈0.85 MeV`; this contrasts with the SD bands and motivates a triaxial interpretation. | Abstract/PDF p.1 and p.2; OCR 17–23, 39–50, 84–86 | Frequency and structural contrast are derived from transition spacings; no independent static-shape observable. |
| HA96-083-06 | Band 1 links are unresolved: the previously suggested paths cannot be confirmed, and no definite path from band 1 to low-lying states was found. 832, 847, 934 and 1177 keV lines are coincident with band 1 and the low-lying yrast νh11/2 band B1 and might later complete a link. Other ΔEγ≈100 keV bands have no observed links to normal-deformed states. | PDF pp.2–3/614–615, Fig.3; OCR 102–110, 123–132 | Coincidence candidates and Fig.3 predominant paths are not completed level-scheme links; excitation energies, spins and parities remain unknown. |
| HA96-083-07 | DCO could not be performed because of insufficient 90° statistics. Band 1 intensity ratios support ΔI=2; all other bands are **assumed** to be stretched E2. Conditional spin examples are bands 3 and 6 to about 99/2 and 93/2, respectively, using assumed unseen links, bandhead and E2 character. | PDF p.3/615; OCR 132–149 | No independent multipolarity or spin-parity closure. |
| HA96-083-08 | For band 1, TRS gives γ-soft oblate/triaxial minima `β2≈0.19`, `γ≈−70° to −90°` over `0.23≤ħω≤0.45 MeV`; comparison with a γ≈−30° reference gives observed alignment gain ≈11ħ. Cranked Woods–Saxon predicts ν(h11/2)2 crossing gain ≈4.5ħ at γ=−30° or ≈8ħ at γ=−80°, with shape-change contribution giving ≈7.5–11ħ. | PDF pp.4–6/616–617, Figs.4–6; OCR 168–207 | Model/derived alignment comparison; bandhead I=27/2 and Harris parameters are assumptions. |
| HA96-083-09 | Band 1 is tentatively assigned ν(h11/2)3; gradual νs1/2 and νd3/2 pair alignment is suggested to account for its smooth alignment rise. The prior νi13/2⊗π(h11/2)2 assignment is argued difficult to reconcile with neighboring Ce i13/2 bands. | PDF pp.4–5/616–617; OCR 169–180, 210–213 | Author/model interpretation; no direct configuration tag. |
| HA96-083-10 | Bands 2 and 4 primarily depopulate into band 1. A proton π(h11/2)2 crossing near `ħω≈0.45 MeV` is inferred from alignment gains ≈4.0ħ and ≈3.2ħ; with a γ change −80°→−30° the effective gain is ≈1.0–3.8ħ. Bands 2 and 4 are tentatively ν(h11/2)3⊗π(h11/2)2 five-quasiparticle structures and possible signature partners. | PDF pp.5–6/617; OCR 242–281 | 882/892.4 ordering and unseen links are assumed; the signature-partner statement is explicitly speculative. |
| HA96-083-11 | Bands 3 and 5 show the shared backbend at `ħω≈0.6 MeV`; it is attributed to π(g7/2)2 alignment (calculated gain ≈5ħ, observed ≈4.3ħ). They are tentatively ν(h11/2)3⊗π(h11/2)2⊗π(g7/2)2 seven-quasiparticle structures. | PDF pp.5–6/617–618, Figs.7–8; OCR 262–278 | Crossing/configuration are model interpretation; no direct g7/2 occupancy measurement. |
| HA96-083-12 | Band 6 feeds the νh11/2⊗π(h11/2)2 side band, has near-prolate γ≈0° from absent signature splitting, and is proposed as ν(h11/2)2⊗νs1/2⊗π(h11/2)2 before and ⊗π(g7/2)2 after the ~0.6 MeV backbend. Band 7 feeds the positive-parity νh11/2⊗πh11/2⊗πg7/2 side band and is tentatively ν(h11/2)2⊗νs1/2⊗πh11/2⊗πg7/2; exact identities remain open. | PDF pp.6/618; OCR 289–332, 307–316 | Shape and configurations are conditional Woods–Saxon interpretations. |
| HA96-083-13 | At high frequency, TRS predicts weak noncollective oblate minima near γ≈+60° for all (π,α) combinations; authors speculate complete particle alignment and possible “soft-band” termination, but no termination is observed here. | PDF p.6/618, Fig.9; OCR 317–332 | Prediction/speculation only, not an experimental crossing or terminating state. |
| HA96-083-14 | No new lifetime or absolute transition-strength measurement is reported. The paper cites a prior mean `Qt>2.3 eb` for band 1 and compares it with SD `Qt=7.5±0.8 eb` (`β2=0.41±0.04`), then extracts `β2≈0.18` from the prior Qt under γ=−80° and rotor relations. | PDF pp.1, 5/613, 617; OCR 44–50, 214–239 | Qt is imported from Ref. [12] (unpublished report), not measured in this article; β2 is model conversion, not static deformation measurement. No τ, absolute B(E2), Q uncertainty or full EM network. |

## Crossing and shape ledger

| Observed feature | Paper's assignment | Status |
|---|---|---|
| Band 1 smooth alignment rise, reference-relative gain ≈11ħ over 0.23–0.45 MeV | ν(h11/2)2 alignment plus γ change −30°→−80°; ν(h11/2)3 band | Derived/model, conditional on bandhead and Harris reference. |
| Bands 2/4 alignment near 0.45 MeV | π(h11/2)2 crossing; γ change back toward −30° | Model inference; gain depends on unseen links and γ. |
| Bands 3/5 backbend ≈0.6 MeV | π(g7/2)2 alignment | Model inference; observed backbend is direct, particle identity is not. |
| Band 6 backbend ≈0.6 MeV | Same π(g7/2)2 alignment after a near-prolate side band | Model inference; exact band configuration open. |
| High-frequency weak minimum γ≈+60° | Possible complete alignment/soft termination | TRS prediction/speculation only. |

The 1996 paper therefore supplies a richer *crossing/configuration hypothesis
map* than 1995Ha34, but it does not turn any crossing into a direct
configuration measurement. Its “triaxial” label is based on alignment, dynamic
moment and model-PES consistency; there is no partner-band electromagnetic
network, signed phase, static γ measurement or tunneling observable that would
establish chirality.

## Independence and evidence-lineage audit

### Hauschild 1995 (1995Ha34)

This is a **same-data dependent follow-up**, despite being a separate article.
The two papers share the reaction (`116Cd(22Ne,5n)` at 120 MeV), two 500 μg
cm−2 targets, early 31-detector Gammasphere and the exact event totals
(`~1.5×10^9` fold>3; `~3.5×10^9` triples). The 1996 text names 1995 as Ref.
[11] and says the six new sequences were extracted “in addition to the three
superdeformed bands reported” there. Count 1995 and 1996 as different
analyses/structure nodes but not independent event-level evidence. The new
1996 bands are not the 1995 SD bands; they are a reanalysis/extension of the
same high-fold data stream.

### Joss 1998 (1998Jo16)

This is an **independent experimental campaign**: Joss uses
`100Mo(36S,xn)` and DSAM/DBLS line shapes, whereas Hauschild 1996 uses
`116Cd(22Ne,5n)` and coincidence/alignment spectroscopy. Joss reports four
parent-specific lifetimes and Qt values; Hauschild 1996 reports none. Author
overlap (including Hauschild, Clark, Fallon, Macchiavelli, Nolan, Semple and
Wadsworth) and citation/model continuity create bibliographic dependence, but
not shared event data. Joss's τ/Qt therefore supplies a distinct clock and
collectivity node, subject to its own stopping/side-feeding systematics.

## Self-audit and stop boundary

1. **Established from the original:** seven ≈100-keV structures, backbends,
   alignment plots, intensity estimates, candidate coincidence paths, and the
   article's explicit tentative configuration/model statements.
2. **Not established:** independent event sample relative to 1995; exact spins,
   parities, multipolarities for most bands; direct normal–new-band linking;
   τ, absolute Q/B(E2); static γ; partner-band phase or chirality.
3. **Most important correction for the canonical map:** replace any wording
   that calls 1996 an “independent Gammasphere reaction/campaign” from 1995;
   retain “new analysis/new structures from the same 116Cd(22Ne,5n) data”.
4. **No further acquisition loop:** official APS PDF, full text and all visuals
   were available and read. SI/producer was not identified. This worker writes
   only this report/receipt; no canonical, raw or Git file was modified.
