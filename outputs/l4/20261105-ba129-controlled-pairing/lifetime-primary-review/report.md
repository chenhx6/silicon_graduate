# 129Ba lifetime primary-source audit

**Disposition: original lifetime table not recovered; evaluated half-lives retained.**

This audit did not obtain Stuch et al., *Physical Review C* **61**, 044325 (2000),
DOI `10.1103/PhysRevC.61.044325`, or a direct author-equivalent table containing the
two requested lifetimes. It found a well-identified author thesis and its actual
three-page table of contents, and resolved an earlier conference contribution.
Neither acquired artifact contains the requested numerical lifetime rows.
**No evidence was found that the ENSDF evaluation is wrong.**

The numerical input remains the 2014 ENSDF half-life field. Converting that input
to a mean lifetime is a derived change of quantity, not a reconstruction of the
original Stuch table and not a new measurement. Model agreement played no role
in the source search, field interpretation, or conversion.

The user-requested directory label is `20261106`. Retrieval timestamps in the
manifest use the actual runtime UTC clock, which fell on November 5, 2026 during
this audit; they were not changed to match the directory label.

## 1. Verified lifetime input

Canonical existing input:

[NNDC 129056013, 201408 ENSDF](/workspace/wiki/raw/papers/gpt/learning-daily/20261016-DAY15-ado-angular-distribution-geometry/nndc-129ba-129056013-201408-09194d4feed3.ens).

| Level | Direct evaluated locator | Evaluated quantity | Derived mean lifetime |
|---|---|---|---|
| 797.4 keV, \(15/2^-\) | L143 | \(T_{1/2}=6.5\pm0.2\) ps | \(\tau=9.377517766\pm0.288539008\) ps; suitably rounded \(9.38\pm0.29\) ps |
| 1475.4 keV, \(19/2^-\) | L206 | \(T_{1/2}=1.0\pm0.4\) ps | \(\tau=1.442695041\pm0.577078016\) ps; suitably rounded \(1.44\pm0.58\) ps |

The source-level provenance is explicit:

- L10–11: `2000St07`, \(^{116}\mathrm{Cd}(^{18}\mathrm O,5n\gamma)\),
  \(E=76\) MeV, recoil-distance technique, differential decay curve method,
  `T{-1/2}`.
- L38–39: the level `T` field comes from RDDS, `2000St07`, unless otherwise stated.
- L143 and L206 contain the literal fields `6.5 PS    2` and `1.0 PS    4`.
  Their uncertainty digits correspond to 0.2 and 0.4 ps, respectively.

The transformation used is

\[
\tau=\frac{T_{1/2}}{\ln 2},\qquad
\Delta\tau=\frac{\Delta T_{1/2}}{\ln 2}.
\]

The same linear transformation is applied to each quoted error. This does not
assign a new confidence level, recover systematic errors, or establish
cross-level independence. The original paper's table heading, its own numerical
rows, and its error-budget definition remain unverified.

The new direct
[NSR keynumber response](/workspace/wiki/raw/papers/gpt/query/20261106-ba129-lifetime-primary-check/nndc-stuch-keynumber-records.json),
`data[0]`, binds `2000ST07` to the exact DOI, authors, journal and reaction.
NSR also indexes `T1/2`, but this is an indexing convention, not a substitute for
reading the original article's lifetime column.

## 2. Branches: an original table was available

The previously archived
[Byrne et al. 1992 original PDF](/workspace/wiki/raw/papers/gpt/query/20261105-ba129-model-readiness/byrne1992-main.pdf)
was used for a limited visual cross-check of Table 1, printed pp.135–137 /
PDF pp.5–7. Its caption specifies relative gamma intensities for
\(^{116}\mathrm{Cd}(^{18}\mathrm O,5n)\) at **86 MeV**, with angular-correlation
corrections when intensities were extracted from coincidence spectra.
The corresponding ENSDF header, L22, attributes `E,RI` to `1992By03`.

| Initial level | Gamma and destination | Byrne Table 1 intensity | ENSDF RI | Original / evaluated locator |
|---|---|---:|---:|---|
| 797.4, \(15/2^-\) | 153.8(1) keV → 643.6, \(13/2^-\) | 74(4) | 7.4(4) | p.135/PDF5; ENSDF L144 |
| 797.4, \(15/2^-\) | 518.6(1) keV → 278.81, \(11/2^-\) | 1000(20) | 100.0(20) | p.136/PDF6; ENSDF L149 |
| 1475.4, \(19/2^-\) | 157.0(1) keV → 1318.4, \(17/2^-\) | 53(14) | 5.3(14) | p.135/PDF5; ENSDF L207 |
| 1475.4, \(19/2^-\) | 678.0(1) keV → 797.4, \(15/2^-\) | 796(16) | 79.6(16) | p.137/PDF7; ENSDF L211 |

The decimal uncertainty tokens above use the last printed digit convention.
Byrne's level-energy columns are rounded to integer keV; the more precise
destination labels in this table come from ENSDF, including 278.81 keV at L97.
The direct table and ENSDF RI agree after a scale factor of 0.1. They are the
same intensity lineage, not independent measurements.

ENSDF assigns M1+E2 to 153.8 keV, (M1+E2) to 157.0 keV, and E2 to 518.6 and
678.0 keV. Those multipolarity labels are retained as evaluated assignments;
the primary visual check here establishes the Table 1 energies, level
placements, spins, and relative intensities.

The listed RI values are neither total electromagnetic branching fractions nor
RDDS feeding fractions. L32–33 says \(\delta(E2/M1)=0.5\) was assumed for
unreported mixed-transition ratios when computing conversion coefficients.
Thus the tabulated mixed-line CC values are conditional on a default mixing
ratio. No missing mixing ratio, conversion uncertainty or joint intensity
covariance was supplied by this audit, and no absolute \(B(E2)\) was calculated.

## 3. Feeding: connectivity is available, original RDDS selection is not

The evaluated scheme contains the following incoming candidates. They were
located by their parent-level records and gamma-energy closure within 0.15 keV.
The literal records and closure residuals are in `audit.json`; this selection
does not identify the actual Stuch gates.

| Target | Incoming gamma / parent level | ENSDF gamma lines |
|---|---|---|
| 797.4 keV | 412.6 / 1210.0; 521.0 / 1318.4; 678.0 / 1475.4; 747.8 / 1545.3 | L181, L196, L211, L222 |
| 1475.4 keV | 670.8 / 2146.3; 805.8 / 2281.2; 861.3 / 2336.7; 1124.3 / 2599.6 | L256, L263, L270, L310 |

The main 678.0-keV cascade edge links the two audited levels directly. The
Byrne Table 1 columns explicitly corroborate several of these placements,
including 521.0 and 678.0 into 797, and 670.8 and 805.8 into 1475
(printed pp.136–137 / PDF pp.6–7).

Still missing from the Stuch primary source:

- exact coincidence-gate energies and whether shifted or stopped components
  were selected;
- distance-dependent shifted/stopped yields and fitting intervals;
- the actual feeding correction or cancellation demonstrated for each row;
- recoil velocity, target/stopper specifications, distance calibration and their
  contributions to the reported uncertainty;
- treatment of weak/unobserved feeding, contaminants and unresolved components;
- lifetime covariance, uncertainty decomposition and any source-specific
  systematic allowance.

The evaluated note establishes RDDS/DDCM as the method. It does not demonstrate
that each requested row is free of feeding systematics. Byrne's 86-MeV intensity
balance cannot be substituted for Stuch's 76-MeV population and gate conditions.
Intrinsic de-excitation branches, experimental population intensities and
coincidence-selection weights are different inputs.

## 4. Original and author-equivalent source identity

| Source | Strongest acquired evidence | What remains unavailable |
|---|---|---|
| Stuch et al., PRC61,044325(2000) | Existing Crossref exact-DOI record; new NNDC/NSR `2000ST07`; INSPIRE525065; OSTI20215890. OSTI reports an 11-page article; the APS-derived abstract describes six 129Ba and twelve 130Ba lifetimes. | Original PDF/body, exact table number, individual lifetime values and author quantity/error labels. |
| Oliver Stuch thesis | DNB955612446, exact title **Koinzidenzmessung von Lebensdauern in 130Ba und Nachbarkernen mit EUROBALL-Clusterdetektoren**; MARC502: Cologne dissertation, **1997**; catalog publication year **1998**; extent **IV,126 pages**. Actual three-page contents scan acquired and visually checked. | Thesis body and numerical tables. |
| Stuch et al. conference contribution | Exact NSR `1998STZX`: **Coincidence RDDS Lifetime Measurement in 130Ba with an EUROBALL Cluster Detector Array**, Contrib. Nuclear Structure '98, Gatlinburg, **p.128 (1998)**. | Conference page itself. The indexed title and reaction cover **130Ba only**; no verified 129Ba table. |
| Möller2005 thesis | University-hosted original thesis; only title page and bibliography entry `[STU98]`, PDF88 / printed p.78, were used. It cites the Stuch thesis as 1998. | This is not the Stuch thesis and supplies no direct values for the audited levels. |

The actual Stuch
[contents PDF](/workspace/wiki/raw/papers/gpt/query/20261106-ba129-lifetime-primary-check/stuch1997-thesis-toc.pdf)
gives precise next-read locations:

- PDF2 / printed iii, §4.3: lifetime overview at **p.57**;
- PDF2 / printed iii, §6.2: 129Ba and125Xe at **p.82**, with negative-parity
  bands in §6.2.2 at **p.83**;
- PDF3 / printed iv, AppendixE: intensity tables starting at **p.109**.

These are chapter locators read from the contents; they do not establish that a
particular requested row appears on those pages. The DNB catalog links the
contents and physical holdings, without a full-body download. The Cologne
repository's S-author index contains Stephan Stuch, not a matching Oliver Stuch
thesis entry. This does not prove that no digital copy exists elsewhere.

## 5. Distinct access routes and stopping reasons

All new response bodies, including failures, are registered in the root-relative
[manifest](/workspace/wiki/raw/papers/gpt/query/20261106-ba129-lifetime-primary-check/manifest.json).
Exact request URLs, timestamps and outcomes are retained in
[routes.json](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/lifetime-primary-review/routes.json).

| Route | Outcome | Boundary / disposition |
|---|---|---|
| Existing APS Harvest fulltext request | Prior401 receipt read; **not retried** | Same authorization failure retained. |
| Existing HAL exact DOI search | Prior200/zero-results receipt read; **not retried** | Identical empty query avoided. |
| Existing Crossref exact DOI lookup | Existing JSON reused | Metadata only. |
| Normal APS abstract and PDF paths | Both403 | HTML access-failure bodies saved; no PDF. |
| OpenAlex DOI record | 200; closed; no OA or repository PDF URL | Discovery only, not proof of worldwide unavailability. |
| Semantic Scholar DOI record | 200; `openAccessPdf.url=""`, `CLOSED` | No manuscript URL. |
| INSPIRE exact DOI and author bibliography | 200; exact article and five author records | No matching `documents` or manuscript URLs. |
| TUM institutional publication-path candidate | 404 | Candidate failed; no inference that the institution holds no copy. |
| Cologne repository / cited thesis | 200: S-author index and Möller2005 thesis PDF | Bibliographic lead established; no Oliver Stuch body recovered. |
| DNB SRU, catalog and linked contents | 200; exact catalog plus actual3-page contents | Strongest author-equivalent identity evidence; numerical table unavailable. |
| OSTI exact article | 200, record20215890 | Citation link only; no fulltext link. |
| CORE using existing authorized key | 500 | Error response retained; key absent from records. No repeated identical request. |
| Conference discovery via Crossref / OSTI | Crossref returned other works; broad OSTI results irrelevant; focused title/date query500 | No conference page recovered. |
| Legacy NNDC NSR links | 200 but generic modern homepage | Explicitly not accepted as a keynumber result. |
| Current official NSR keynumber API | 200; exactly `2000ST07` and `1998STZX` | Both report `pdfAvailable=false`, `xundlAvailable=false`; exact identities resolved. Conference indexes130Ba only. |

Public web discovery also used exact DOI/title, author+dissertation, the German
thesis title and the conference key. Search snippets were candidate locators,
not lifetime evidence. The paper was not obtained from unauthorized mirrors;
no author or institution was messaged, and no account or access request was made.

The exact NSR record contains an empty errata list. That field does not prove
the absence of all corrections; it provides no evidence for changing the
evaluated quantity. The search stops here because further use of the available
metadata/contents would not verify the requested numerical rows.

## 6. Contract for the active A130 work

Use:

```text
source_layer = ENSDF2014 evaluation, attributed to 2000St07
quantity = T1/2
797.4 keV, 15/2-: T1/2 = 6.5 +/- 0.2 ps
1475.4 keV, 19/2-: T1/2 = 1.0 +/- 0.4 ps
tau = T1/2 / ln(2)
original_table_verified = false
original_author_quantity_label = null
original_author_error_definition = null
source_covariance = null
source_RDDS_gates = null
evaluation_error_evidence_found = false
```

The means \(9.38(29)\) ps and \(1.44(58)\) ps can be used as **derived from the
evaluated half-lives**, carrying that provenance and the quoted-error boundary.
Do not relabel 6.5 and1.0 ps as original-author mean lifetimes to improve a model
comparison. Do not borrow a neighboring level's lifetime or an86-MeV feeding
balance to complete the76-MeV RDDS inputs.

A later source can change this disposition only after direct inspection of
the original table/header, level identity, units, uncertainty definition,
and gate/feeding discussion. The best concrete pending source is the Stuch
thesis body at the contents locators above. Merely finding another citation,
catalog record, abstract, or model using these numbers is insufficient.

## 7. Deliverables and scope

- `audit.json`: typed evaluated lifetimes, exact conversions, branch provenance,
  evaluated incoming candidates, original-source null fields and identity audit.
- `routes.json`: all new retrieval attempts and actual UTC timestamps.
- `checks.json`: archive-gate and local hash/field checks.
- Raw collection manifest: 26 downloaded response bodies; **zero target original
  articles or author-equivalent numerical lifetime tables**. The two acquired
  PDFs are the3-page Stuch contents and the different-author Möller thesis.
- Text and image inspection artifacts remain under
  `tmp/ba129-lifetime-primary-check/`.

Only the three user-authorized directories were written. Existing raw inputs,
PLAN, knowledge pages, other session outputs, credentials/configuration and Git
index/history were not modified. The get-paper skill was not inspected or run.
No commit was made. This is a completed access-and-evidence audit with an
explicitly unresolved original-lifetime-table check, not completion of the
parent A130 research goal.
