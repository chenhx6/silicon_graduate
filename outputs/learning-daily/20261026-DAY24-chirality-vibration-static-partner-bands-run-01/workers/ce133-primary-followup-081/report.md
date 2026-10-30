# Ce-133 primary follow-up 081 — Hauschild 1995 (1995Ha34)

## Decision

**new independent primary (high-spin superdeformed spectroscopy; no lifetime).**
This is not a no-op against Joss 1998 or Gizon 1974. It is a distinct
`116Cd(22Ne,5n)` Gammasphere campaign and supplies three Ce-133
superdeformed cascades, dynamic-moment-of-inertia/alignment information and
configuration/shape calculations. It does not supply a Ce-133 lifetime, Qt or
absolute transition strength. Joss 1998 uses `100Mo(36S,3n)` and DSAM
lifetime/Qt of a normal triaxial band; Gizon 1974 uses `120Sn(16O,3n)` and
low-spin in-beam spectroscopy. The author overlap and citation of the 1995
work in later papers are lineage dependencies, not duplicate event data.

## Source identity and acquisition

- Key: **1995Ha34** (NNDC adopted-reference key).
- K. Hauschild et al., *Physics Letters B* **353** (1995) 438–443,
  “Neutron orbitals above the N = 74 shell gap at large deformation:
  spectroscopy in the superdeformed minimum of 133Ce”.
- DOI: `10.1016/0370-2693(95)00601-G`.
- NNDC adopted-reference locator: `tmp/day24-ce133-evaluated-zero-entry-069/adopted-refs-text.txt`, lines 108–122 (title, reaction, observables, DOI).
- Publisher API route: Elsevier article PII `037026939500601G`,
  `httpAccept=application/pdf`; object endpoint returned the six-page main PDF.
- Full PDF: `tmp/day24-ce133-primary-followup-081/1995Ha34-full.pdf`;
  SHA-256 `ce219bb983b42a15cb634f95e9ad99bcfbc8442bc179a5e5f0e613b9ac9958fb`;
  690,165 bytes; 6 pages (printed pp. 438–443).
- Text extraction: `tmp/day24-ce133-primary-followup-081/1995Ha34-full.txt`.
  The first downloader artifact was only a one-page PDF (`fc4c11e2…db9744`,
  86,755 bytes); it is retained as an acquisition failure boundary. The
  six-page object endpoint is the evidence-bearing file.
- No Supporting Information was requested or downloaded (`--no-si`); the
  article is complete as the six-page main text with Figures 1–3 and Table 1.

## Atomic evidence ledger

| ID | Direct report | Locator | Evidence boundary |
|---|---|---|---|
| HA95-081-01 | `116Cd(22Ne,5n)` at 120 MeV populated high-spin 133Ce; Gammasphere early implementation used 31 large-volume Compton-suppressed HPGe detectors; about `1.5×10^9` suppressed-fold events and `~3.5×10^9` unpacked triples. | PDF p. 1 (printed 438), p. 2 (439), Experimental paragraph; text lines 100–120 | direct apparatus/event report; no raw cube or efficiency covariance |
| HA95-081-02 | Three new weakly populated superdeformed bands were identified by variable-spaced-lattice search and triple-coincidence spectra. Relative populations were about 3%, 1.5% and 0.6% of the 133Ce population for Bands 1–3. | PDF p. 2–3 (439–440), Fig. 1 and text; lines 119–137 | direct band observation; relative population only |
| HA95-081-03 | Linking transitions to normal-deformed states were not observed; therefore excitation energies, spins and parities of the SD states were unknown. Assuming ~4ℏ unseen links gave estimated ranges 43/2–105/2, 37/2–99/2 and 45/2–101/2 for Bands 1–3. | PDF p. 3 (440), text; lines 148–163 | spin ranges are conditional estimates, not measured assignments |
| HA95-081-04 | In-band spacings were roughly 70 keV and were treated as likely E2 cascades; insufficient 90° statistics prevented a directional-correlation analysis. | PDF p. 3 (440), text; lines 165–170 | E2 character is an assumption; no DCO/absolute multipole proof |
| HA95-081-05 | Bands 1 and 2 had dynamic moments of inertia close to the 132Ce yrast SD band and fed out near `ℏω≈0.4 MeV`; Band 3 showed a pronounced `J^(2)` hump near `ℏω≈0.70 MeV`. | PDF pp. 3–4 (440–441), Fig. 2 and text; lines 158–175 | `J^(2)` is derived from transition spacings; no lifetime |
| HA95-081-06 | Extended pairing/deformation self-consistent calculations predicted an SD minimum near `β2≈0.40`, `β4≈0.01`, `γ≈0°`, with a coexisting lower-deformation minimum near `β2≈0.30` for one signature configuration. | PDF p. 4 (441), Fig. 3 caption/text; lines 188–222 | model PES result, not a static shape measurement |
| HA95-081-07 | Band 1 transitions were identical to 132Ce yrast from 1132–1570 keV with `ΔEγ(rms)=1.0 keV`; the favored `[530]1/2−` alignment was calculated as `1.6(1)ℏ` over the identicality interval. | PDF p. 4 (441), Fig. 3(c) discussion; lines 228–236 | identical-band comparison and calculated alignment |
| HA95-081-08 | Assuming signature-partner assignments, the authors tentatively associated Bands 1/2 with the `[530]1/2−` neutron orbital coupled to a `π(h11/2)^4ν(i13/2)^2` core; Band 3 was tentatively associated with a `π(h11/2)^4ν(i13/2)^3` configuration and a `[530]` neutron-pair alignment. | PDF pp. 4–6 (441–443), Fig. 3 and conclusion; lines 228–236, 266–299, 329–351 | author/model interpretation; not direct configuration proof |
| HA95-081-09 | Table 1 reports the Band-2/136Nd yrast comparison (720.3(2)–1822(1) keV versus 716.5(2)–1815(1) keV; differences −3.9 to +9.5 keV, with most differences near 0–2 keV). | PDF p. 5 (442), Table 1; lines 240–267 | literal transition-energy comparison; no absolute level placement |
| HA95-081-10 | Band-3 alignment gain was estimated as `Δix≈3.9ℏ` experimentally versus `≈3.5ℏ` from the single-particle diagram; a low-frequency `J^(2)` rise was tentatively attributed to mixing of `νi13/2` configurations. | PDF p. 5–6 (442–443), Fig. 2(b), discussion/conclusion; lines 283–299, 329–351 | derived/model comparison and explicitly tentative mixing |

## Independence and overlap audit

- **Against Joss 1998 (`1998Jo16`):** independent reaction and campaign:
  Hauschild uses `116Cd(22Ne,5n)` at 120 MeV and SD-band spectroscopy;
  Joss uses `100Mo(36S,3n)` and DSAM/DBLS lifetimes of a normal triaxial
  band. Joss cites the 1995 work, and several authors overlap, so the
  *bibliographic/model lineage* is dependent. The event sample and principal
  observables are different; this is not duplicate lifetime data.
- **Against Gizon 1974:** independent experiment, detector generation,
  reaction and spin domain. Gizon’s `120Sn(16O,3n)` data are low-spin/normal
  deformation with historical level-zero ambiguity; Hauschild’s data are
  high-spin SD cascades. No shared event set or copied numerical ledger was
  found.
- **Against Emediato 1997:** different `120Sn(16O,3n)` RDDS lifetime
  campaign; Hauschild has no τ. It should not be used to fill the RDDS clock
  cells.

## Stop boundary

This follow-up establishes a genuinely new high-spin/shape evidence node but
does **not** close the Ce-133 SD lifetime/Qt gap. No τ, Qt, absolute B(E2),
linking transition or directional-correlation result is reported for the new
bands. The spin ranges, E2 assumption, configurations, β/γ values and
signature-partner language must remain conditional/model-labelled. A future
1995Ha28 read would be the relevant lifetime/Qt companion from the same
reaction family; 1996Ha20 is a later shape/crossing companion, not needed to
establish this primary’s independence.
