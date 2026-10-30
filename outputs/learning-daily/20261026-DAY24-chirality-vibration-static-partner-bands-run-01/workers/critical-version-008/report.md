# Official-current arXiv version check

**Verified no new body on the official-current arXiv route.** The unversioned current PDF for `nucl-th/0211075` is byte-for-byte identical to the previously acquired explicit v1. The official abstract page lists only **[v1] Mon, 25 Nov 2002 11:38:58 UTC** in submission history and names only **P. Olbratowski, J. Dobaczewski, J. Dudek**. No v2 or four-author replacement appears in that official history at the time checked.

The actual-body versus publication-metadata distinction therefore remains: the current arXiv body is the three-author2002 manuscript; the verified2004 PRL93,052501 metadata includes W. Płóciennik. No final published body or independently identified four-author final author manuscript was obtained by this check.

## Direct checks

| Item | Result |
|---|---|
| Abstract/history URL | `https://arxiv.org/abs/nucl-th/0211075` |
| HTTP/content | 200, `text/html; charset=utf-8`, 39274 bytes |
| Abstract-page SHA256 | `43d8061c907a6b2a9153da495ba1e6e24dc219dee044c4915273b982bfaf7cc0` |
| History locator | Saved `tmp/day24-critical-version-008/arxiv-abs.response`, HTML183–185: Submission history, single v1 date/time |
| Author/DOI locator | Same saved HTML39 has all three citation_author entries and the PRL DOI; HTML157/163 gives the journal reference/related DOI |
| Current PDF URL | `https://arxiv.org/pdf/nucl-th/0211075` (no explicit v suffix) |
| HTTP/content | 200, `application/pdf`, valid `%PDF`, 252547 bytes, four pages |
| Current PDF SHA256 | `3cc0000405bb8360d0b7112fbd6d6a3811546091dee182da2b44be071c8bbffb` |
| Comparison with `tmp/day24-critical-tac-007/arxiv-0211075v1.pdf` | **Exact byte equality**; every page's extracted text also identical |
| New body reading | **0 new pages, 0 new figures, 0 new equations**; prior four-page/Figs1–6/Eqs1–7 reading remains applicable to this identical artifact |

This was one motivated body route (official current arXiv) plus its official history page. No previous APS401 or author HTML request was repeated. The history and byte equality directly settle whether the prior explicit-v1 download missed a newer version on this arXiv item, so no second speculative body route was added.

## Interpretation boundary

The present check supplies **version evidence**, not a new physical result. There is no new-body revision to compare for s_s/s_l, inertias, .51/.6MeV critical values, axis-prose reversal, inertia-gap wording, pairing or time-odd terms. Prior worker `critical-tac-007/report.md` locators and explicit-v1 ambiguities remain unchanged. The check cannot establish whether the2004 VoR corrected those statements, nor prove that no four-author manuscript is hosted elsewhere. It cannot establish equivalence of the2002 body with the published2004 paper solely from their title/DOI association.

Reusable writeback wording: **“The official arXiv abstract/history and unversioned current PDF were checked; history lists only2002 v1, and current PDF SHA2563cc000...8bbffb is byte-identical to the explicit v1. All numerical/formula claims remain attributed to that three-author early manuscript; the four-author2004 published body is still unverified.”** This is source/version provenance, with `needs_review:true` retained for final-version differences; it is not a new critical-frequency claim.

`receipt.json`, `arxiv-abs.json` and `arxiv-current-pdf.json` contain the checks and request metadata. Only the assigned worker output prefix and `tmp/day24-critical-version-008/` were written. Shared canonical/raw/PLAN/Bib/Git, session and credits were untouched.
