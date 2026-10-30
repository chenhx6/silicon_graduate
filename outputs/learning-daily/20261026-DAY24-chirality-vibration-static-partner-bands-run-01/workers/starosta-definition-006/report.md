# GR18 Ref.14 original-definition recovery — bounded negative result

Target: K. Starosta, T. Koike, C. J. Chiara, D. B. Fossan and D. R. LaFosse, **“Chirality in odd–odd triaxial nuclei”**, Nuclear Physics A **682**, 375–386 (2001), DOI **10.1016/S0375-9474(00)00663-1**, PII **S0375947400006631**.

**Result: target body not obtained.** No target PDF, readable full-text HTML, author manuscript or full-body XML was recovered through the routes below. No conclusion is drawn about whether another accessible copy exists. The original orientation definition, its normalization and coupling convention remain **unknown from this target body**. The PRL 86, 971 paper is a different article and was not substituted.

## Scientific boundary preserved

The starting scientific question is recorded at `knowledge/sources/grodner-2018-128cs-chiral-g-factor.md:150–177`, especially GR18-D22-R114-1/2 and R119-1. Under usual independent laboratory spin operators, signed triple-product, RMS and Gram-of-mean proxies can differ; the existing conditional calculations are not a reproduction of Starosta's producer. This recovery attempt supplies no new body evidence to decide whether the NPA article uses signed expectation, absolute value, RMS, a semiclassical proxy or another convention. It neither changes the GR18 measured g value nor establishes an error in either paper.

| Required body-level item | Result |
|---|---|
| Signed / absolute / RMS / semiclassical orientation | Unknown from target body |
| Normalization, dimensional factors and operator ordering | Unknown from target body |
| Definition of coupled angular momenta and basis/conventions | Unknown from target body |
| Exact target-body page/equation/figure locator | Unavailable |
| Target-body pages / figures / equations read | **0 / 0 / 0** |
| Full-text version identity | Unverified; metadata identifies the intended published article only |

## Existing failures read before retrieval

- `tmp/day22-evidence-correction/gr18-ref14-acquisition/manifest.json`: explicit OA route returned `oa_not_found`, no OA attempts or successful download; Unpaywall had `is_oa:false` and no PMC ID. Its separate `oaAssessment:confirmed_oa` field must not be treated as proof of access: it coexists with `is_oa:false` and an Elsevier TDM user-license link.
- `tmp/day23-originals/starosta2001-npa-openalex023.json`: target metadata, `oa_status:closed`, one DOI/publisher location, no PDF URL or repository full-text location.
- Source-page lines 159 and 167 explicitly preserve the missing Ref.14 body and distinguish the existing PRL article.

Old failed ScienceDirect/paywall/empty PDF paths were not repeatedly requested. The new publisher request was the actual Article API link supplied by fresh Crossref metadata, and was content-checked rather than accepted because of HTTP 200.

## New route results

| Route and rationale | Observed result |
|---|---|
| Fresh Crossref DOI metadata; exact target identity and registered text-mining URL | HTTP 200 JSON, 2660 bytes; correct DOI/title/author list and `api.elsevier.com/content/article/PII:S0375947400006631` XML/plain links. Metadata only. |
| Registered Elsevier Article API XML link | **HTTP 200 `text/xml;charset=UTF-8`, 1789 bytes**, SHA256 `3ea0dc691a86e37b9bf2ff46dff3bdca4e59e96175524c2ca7ef61782c6659fb`. XML contains `coredata` only; no `originalText`, `body` or `rawtext`. Correct target DOI/title, but not full text. |
| One explicit PDF representation request to that same API, to distinguish metadata response from body availability | HTTP **406**, 162-byte XML, `INVALID_INPUT`: PDF Accept value is restricted. No PDF signature. This is a format/access response, not proof that no entitled institutional access exists. No credentials were requested or configured. |
| Fresh OpenAlex DOI lookup and search | Correct NPA target; `oa_url:null`, `is_oa:false`, a single publisher DOI location and no PDF. This is a discovery result, not evidence of global unavailability. |
| Tohoku institutional repository; coauthor Koike and an independently surfaced related author publication make this a motivated repository route | Public WEKO3 root and REST search readable. Broad “Chirality” search returned 31 items, all 31 inspected across two pages. Related nuclear records 5324 / 5352 / 5318 are other PRC articles. No target-title record in those returned items. Quoted full DOI search returned **0** items; quoted “Chirality in odd” phrase search returned 4 other records. The broad DOI-suffix query is tokenized and not an exact-match absence check. |
| Starosta's SFU author/department route | Faculty and retired-faculty pages readable; guessed current author/group URLs 404. The old public `https://www.sfu.ca/~starosta/` directory returned HTTP 200, **672 bytes, empty directory listing**. No manuscript link. |
| Koike's Tohoku department/group route | Nuclear group root readable; two candidate personal-profile paths 404 and one old host did not resolve. No target publication link recovered. |
| arXiv title+author query `ti:Chirality AND au:Starosta` | HTTP 200 Atom; five entries returned, none the 2001 NPA target. No unrelated arXiv paper was downloaded or used as a replacement definition. |
| Scholar / Semantic Scholar / general web fallback | Scholar tool failed/timed out; Semantic Scholar HTTP 429; Google, CiNii, OSTI and DuckDuckGo routes hit connection failures/timeouts. Bing returned HTTP 200 pages with irrelevant generic results even for the exact PII, so those pages were rejected as unusable discovery evidence. |

The Tohoku related record 5324 links `https://tohoku.repo.nii.ac.jp/record/5324/files/PhysRevC.65.044328.pdf`. It may be a future *separate* definition-lineage investigation, but it is the 2002 PRC article and was not downloaded or presented as the NPA original. Direct recovery would need a newly surfaced author/repository copy or an already authorized institutional copy of the exact NPA DOI; rerunning the same failed routes has little expected gain.

## Reproducibility and stopping reason

Detailed URL, redirect URL, HTTP/content type, byte count, SHA256 and PDF-signature outcomes are consolidated in `receipt.json` and per-route JSON files here. Raw network responses are retained only in `tmp/day24-starosta-definition-006/`, with neutral `.bin` names; none of the **25 retained response files** starts with `%PDF`. The receipt records **32 direct request records** plus three MCP discovery queries. Headers retained for the Article API/author-route batch have sensitive header values redacted without printing them.

This bounded route stops because the motivated author/repository paths yielded no target body, the registered publisher endpoint supplied only metadata, the explicit PDF request was restricted, and remaining web searches were unavailable/unusable. Metadata and snippets cannot answer the operator-definition question. There is no recovered original equation to quote or classify.

Only the exclusive temporary directory and this exclusive worker output prefix were written. Shared canonical knowledge, raw, PLAN, BibTeX, configuration and Git remained read-only; no session, run or credit was created. Source writeback belongs to the leader.
