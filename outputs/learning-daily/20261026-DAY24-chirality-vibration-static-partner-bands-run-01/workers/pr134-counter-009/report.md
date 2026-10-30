# 134Pr lifetime counterexample — primary-source access boundary and dependency audit

**The intended original experiment is identified, but its body was not obtained.** D. Tonev et al., **“Transition Probabilities in134Pr: A Test for Chirality in Nuclear Systems,” PRL96,052501(2006)**, DOI **10.1103/PhysRevLett.96.052501**, is the direct partner-transition-probability source cited by Petrache2006 Ref9. Fresh Crossref metadata verifies its title/author/year/DOI and publication date2006-02-09. The main scientific request cannot be completed without that body: **0 Tonev pages,0 figures,0 tables read; no actual B(E2)/B(M1) values, measured-state list or branch choices extracted.** No synopsis or metadata is substituted for its experiment.

## Existing knowledge and original-file checks

The scoped source search found **no dedicated Tonev2006 source page**. The directly pertinent existing page is `knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md`, especially PE06-D18-1 and PE06-D21-R45-1–4 at lines97–159. It already correctly separates the2.0(4) transition-moment inference, branching-data source and lifetime qualitative comparison. This unit does not claim a new science delta merely by repeating those entries.

Scoped filename search of raw/papers found Petrache1996 and Petrache2006 originals but no Tonev-named original. Existing `tmp/day18-20261020/tonev134pr/` contains failed-access records: APS/Padova verification HTML, HAL API metadata and a HAL landing response saying the requested page does not exist; no target PDF was found there. These old failed web routes were read as failure evidence and not blindly repeated. A broad recursive tmp filename search returned these files but encountered some unrelated permission-denied package directories; this is not an exhaustive all-files guarantee.

An active-recall note was frozen in `active-recall.md` before any target-body reading. It is explicitly **Wiki-primed**, not a blind/scored test, and distinguishes expected lifetime+branch inference from the unknown actual technique, measured levels and B values.

## New access attempts and validation

| Route | Observed result |
|---|---|
| Crossref exact DOI | HTTP200 JSON,7655bytes, SHA256 `67c203b7a65c6113ded2aac05b120c832d7c5db5cf062717084305ff151e8233`; target identity verified, no body |
| Official arXiv `au:Tonev AND all:chirality` | HTTP200 Atom,0 entries; this limited query does not establish absence of any possible preprint |
| OpenAlex exact DOI | HTTP200; publisher/HAL/Padova locations surfaced. Its OA labels do not establish that the current requests can obtain full text |
| Fresh APS harvest fulltext endpoint from Crossref | HTTP401 JSON,69bytes, SHA256 `ab55ce9d2b53c63a4d0ff077f1577ed8c998c7893b42333c085a7a3f020bbb0d`; no PDF signature |
| HAL exact DOI structured record, asking specifically for fileMain/files/external links | HTTP200 JSON,445bytes, SHA256 `9bdd493c6dcf24c9fbda10c7ac53d0df53462a4696b6f6b8f14d4eeb90c03c77`; record in2p3-00025844v1 has only APS external PDF link, **no fileMain_s/files_s** returned |
| Padova public OAI GetRecord for the discovered handle, then one bounded identifier-host repair | HTTP200 XML both times, but XML error **idDoesNotExist**;589/593bytes, no full-text URL/body. The repaired response SHA256 is `98ae7e100962596fdf2c9d83e81e47511397309bd9f2109f82dc0648d67bc3c4` |

No response starts with `%PDF`. Network and format outcomes are in per-route JSON and `receipt.json`; raw responses are under the exclusive temporary prefix. APS401 and the metadata-only repository routes were not retried in a loop. The final OAI attempt ended this body-recovery route.

## Existing primary: what Petrache2006 itself contributes

Per leader steering, a limited **source-dependency check** used the actual existing four-page Petrache PDF:

`raw/papers/gpt/high-spin-20260920/三轴/手征/2006_Petrache et al_Risk of Misinterpretation of Nearly Degenerate Pair Bands as Chiral Partners in.pdf`

SHA256 **ec32a76efbeebf1a924a1c95eb9d404a99158fc9226605414b324e982cfe1d4f**. This unit read the relevant scope/dependency passages on PDF1–4 as text; **it did not newly certify a full-paper or visual read**. The complete earlier reads and corrections in PE06 remain their own provenance. Local text extracts are stored under tmp with the `petrache2006-pageN-targeted-text.txt` names for verification.

- **112502-1, abstract and final scope paragraph:** “experimental information … is critically analyzed”; its own work is explicitly critical analysis, not a reported new beam-time/lifetime acquisition. It is an ordinary four-page PRL article titled *Risk of Misinterpretation…*, **not a title-labeled Comment**. Classifying it as analysis does not change its original scientific contribution: it extracts model-dependent transition-moment/coupling constraints from existing data.
- **112502-2, paragraph beginning “Some branching ratios and lifetimes…”:** cites **[9,11]**, states measured in-band B(E2) for both bands is available only around the crossing, and motivates accounting for band mixing to infer unperturbed strengths. The actual experimental uncertainty/branch tables of Tonev remain unverified here.
- **112502-3, paragraph after allowed Q ratio1.6–2.4:** says the pronounced difference in measured B(E2)_in **[9]** is in **qualitative agreement** with its own result. This is the explicit dependence of Petrache's argument on Tonev; it is not a new independent lifetime experiment or the direct origin of the2.0(4) ratio.
- **112502-4, Ref9:** D. Tonev et al., AIP Conf.Proc.764(2005),p93; **PRL96,052501(2006)**.
- **112502-3 TableI caption / 112502-4 Ref11:** branching data are attributed to **K. Starosta, D.B.Fossan, T.Koike, C.J.Chiara, A.J.Boston, H.C.Chandler, E.S.Paul, R.Wadsworth and A.A.Hecht, “to be published.”** This source is distinct from Tonev's Ref9. Its publication identity remains an actual bibliography node to recover, not something to silently fill with the lifetime DOI.
- **112502-4 conclusion:** criticizes the analyzed ideal-pair interpretation while asking whether/how much a reminiscence of chiral geometry is present. The existing PE06 page already preserves this qualification. A2.0(4) inferred transition-moment ratio is not an independent direct beta/shape measurement or a universal exclusion of all chiral dynamics.

## FM97 and MU07 boundary

This unit has **no new Tonev-body evidence** with which to quantify a challenge to FM97 or MU07. Existing directly sourced chain remains: FM97's early134Pr partner discussion precedes the later absolute-strength test; MU07's135Nd comparison explicitly allows orientation/shape coupling and anharmonic differences in134Pr (existing source MU07-D24-002), rather than requiring each finite-nucleus partner strength to be exactly equal in all regimes. Petrache's already-read analysis can constrain ideal-pair claims, but **its branch data, inferred Q range or lifetime summary cannot be imported as135Nd observations or used to reconstruct Tonev's missing B table**.

## Atomic provenance candidates and next useful nodes

These are access/provenance candidates, **not new experimental science claims**; leader may record them only where needed rather than duplicating existing PE06 claims.

| Candidate | Exact support and boundary |
|---|---|
| Tonev2006 exact experiment identity is resolved, body still missing | Fresh Crossref DOI record; target body0pages/0figures/0tables. Technique, matched partner spins, actual B values, branch choices and covariance stay unknown |
| Petrache2006 is a critical analysis/model extraction using prior measurements, not an independent new lifetime campaign | Primary112502-1 abstract/scope and112502-2 mixing paragraph; ordinary PRL article, no title-labeled Comment |
| Tonev Ref9 and Starosta Ref11 are different input nodes | Primary112502-3 qualitative-agreement sentence/TableI caption and112502-4 bibliography; do not merge lifetime and branch provenance |

Highest-information future routes: (1) exact Tonev original via a **new** repository/entitled-access/local-PDF source, then matched-spin lifetime/branch audit; (2) structured bibliographic recovery of the specifically named Starosta Ref11 to close the already-known branch-source identity. Neither a generic chirality review nor another nucleus' lifetime table closes these nodes. No new fetch was opened for those future routes in this bounded unit.

Only the assigned worker prefix and `tmp/day24-pr134-counter-009/` were written. Shared canonical/raw/PLAN/Bib/Git and session/credits were untouched. No scientific claim is ready for writer promotion from a missing original body.
