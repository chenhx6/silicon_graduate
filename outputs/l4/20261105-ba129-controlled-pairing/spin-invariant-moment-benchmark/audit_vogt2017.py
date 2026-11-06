#!/usr/bin/env python3
"""Read the two archived Vogt2017 manuscripts; create new sidecar files only.

No downloads, model solves, fitting, or copying source-page reproductions into
outputs. Numerical entries below were checked visually against Figs. 6/7 and
Tables II/III. Existing static and pre-primary-readiness artifacts are preserved.
"""

from datetime import datetime, timezone
import csv
import hashlib
import json
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
RAW = ROOT / "raw/papers/gpt/query/20261106-vogt2017-ba137-rstat"
KEY = "Vogt2017PRC95_024316"
DOI = "10.1103/PhysRevC.95.024316"
TITLE = "Isomers and high-spin structures in the N=81 isotones 135Xe and 137Ba"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_ii_row(words, energy):
    match = next(w for w in words if w[4] == energy)
    center = (match[1]+match[3])/2
    return [w for w in words if abs((w[1]+w[3])/2-center) < 4 and w[0] > 310]


def main():
    names = ["vogt2017-metadata.json", "vogt2017-citation.bib",
             "vogt2017-readiness.json", "vogt2017-constraints.csv"]
    if any((OUT/name).exists() for name in names):
        raise FileExistsError("Refusing to overwrite Vogt2017 sidecar outputs")
    old = {p.name: sha(p) for p in OUT.iterdir() if p.is_file()
           and not p.name.startswith("vogt2017") and p.name != Path(__file__).name}
    manifest = json.loads((RAW/"manifest.json").read_text())
    for item in manifest["files"]:
        path = ROOT/item["path"]
        assert path.stat().st_size == item["size"] and sha(path) == item["sha256"]
    metadata = json.loads((RAW/"crossref-vogt2017.json").read_text())["message"]
    assert metadata["DOI"].lower() == DOI.lower()
    assert metadata["published-online"]["date-parts"] == [[2017, 2, 15]]
    assert metadata["volume"] == "95" and metadata["issue"] == "2"
    assert metadata["article-number"] == "024316"
    authors = [dict(given=a.get("given", ""), family=a["family"]) for a in metadata["author"]]
    assert len(authors) == 89

    pdf_checks = {}
    for filename in ("vogt2017-osti.pdf", "vogt2017-accepted.pdf"):
        with pymupdf.open(RAW/filename) as doc:
            assert len(doc) == 18
            for pageno, values in [
                (8, ["2229.8", "2349.9", "120.1", "1568.1", "589(20)"]),
                (9, ["1568.2", "2229.8", "661.7", "589(20)"]),
                (14, ["589(20)", "0.46(3)", "2.58(29)", "0.52(6)"]),
            ]:
                text = doc[pageno-1].get_text()
                assert all(v in text for v in values), (filename, pageno)
            pdf_checks[filename] = {"pages": len(doc), "sha256": sha(RAW/filename),
                                   "audited_entries_present": True}
    with pymupdf.open(RAW/"vogt2017-accepted.pdf") as doc:
        words = doc[8].get_text("words")
        for energy in ("120.1", "1568.2"):
            row = table_ii_row(words, energy)
            assert not any(w[0] > 530 for w in row), (energy, "expected blank I_gamma cell")
        assert any("100" in w[4] and w[0] > 530 for w in table_ii_row(words, "274.5"))

    bibauthors = " and ".join(f"{a['family']}, {a['given']}" for a in authors)
    bib = (
        f"@article{{{KEY},\n"
        f"  author = {{{bibauthors}}},\n"
        "  title = {Isomers and high-spin structures in the {$N=81$} isotones {$^{135}$Xe} and {$^{137}$Ba}},\n"
        "  journal = {Physical Review C},\n"
        "  volume = {95},\n  number = {2},\n  pages = {024316},\n"
        "  year = {2017},\n  month = feb,\n  date = {2017-02-15},\n"
        f"  doi = {{{DOI}}},\n"
        "  note = {Article number 024316; published 15 February 2017}\n}\n"
    )
    bibliography = {
        "citation_key": KEY, "title": TITLE, "authors": authors, "author_count": len(authors),
        "journal": "Physical Review C", "volume": "95", "issue": "2",
        "article_number": "024316", "publication_date": "2017-02-15", "year": 2017,
        "doi": DOI, "canonical_source": f"doi:{DOI}",
        "date_evidence": [
            "Archived Crossref DOI record: published-online.date-parts and published.date-parts",
            "OSTI/CHORUS cover: Phys. Rev. C 95, 024316; Published 15 February 2017",
        ],
        "version_boundary": {
            "osti": "Accepted manuscript with CHORUS bibliographic cover; body dated January 17, 2017",
            "birmingham": "Peer-reviewed accepted manuscript; body dated January 25, 2017 despite January 21 in URL",
            "preferred_reading_copy": "vogt2017-accepted.pdf",
            "pagination": "One cover plus 17 manuscript pages; PDF page = printed manuscript page + 1",
            "published_typeset_VoR_verified": False,
            "repository_download_dates_are_not_publication_dates": True,
        },
        "raw_manifest": str((RAW/"manifest.json").relative_to(ROOT)),
        "raw_manifest_sha256": sha(RAW/"manifest.json"), "pdf_checks": pdf_checks,
    }
    # Every row names the element: 135Xe must never be joined to the 135Ba target.
    constraints = [
        {"nucleus": "137Ba", "A": 137, "Z": 56, "transition": "(15/2-)_1 -> 11/2-_1",
         "parent_keV": 2229.8, "daughter_keV": 661.7,
         "Egamma_tableII_keV": 1568.2, "Egamma_quoted_margin_keV": .5,
         "Egamma_figure6_keV": 1568.1, "relative_Igamma": None,
         "T_half_parent_ns": None, "T_half_margin_ns": None, "Bdown_E2_Wu": None,
         "Bdown_margin_Wu": None, "ICC_numeric": None,
         "role": "R_stat^(1) denominator candidate; absolute strength still unavailable",
         "locator": "Fig.6 PDF p.8/printed p.7; Table II and Sec.III B PDF p.9/printed p.8"},
        {"nucleus": "137Ba", "A": 137, "Z": 56, "transition": "(19/2-)_1 -> (15/2-)_1",
         "parent_keV": 2349.9, "daughter_keV": 2229.8,
         "Egamma_tableII_keV": 120.1, "Egamma_quoted_margin_keV": .5,
         "Egamma_figure6_keV": 120.1, "relative_Igamma": None,
         "T_half_parent_ns": 589., "T_half_margin_ns": 20.,
         "Bdown_E2_Wu": .46, "Bdown_margin_Wu": .03, "ICC_numeric": None,
         "role": "Separate additional EM benchmark, under the author's tentative assignments/E2 interpretation; not the R_stat^(1) denominator",
         "locator": "Fig.7/Sec.III B PDF p.9; Sec.IV PDF p.13; Table III PDF p.14/printed p.13"},
        {"nucleus": "135Xe", "A": 135, "Z": 54, "transition": "(19/2-)_1 -> (15/2-)_1",
         "parent_keV": 2058., "daughter_keV": 1749.,
         "Egamma_tableII_keV": None, "Egamma_quoted_margin_keV": None,
         "Egamma_figure6_keV": None, "relative_Igamma": None,
         "T_half_parent_ns": 9., "T_half_margin_ns": .9,
         "Bdown_E2_Wu": .52, "Bdown_margin_Wu": .06, "ICC_numeric": None,
         "role": "Other-isotope context from the same paper; not a 135Ba datum",
         "locator": "Fig.5 PDF p.8; Table III PDF p.14/printed p.13"},
        {"nucleus": "133Te", "A": 133, "Z": 52, "transition": "19/2-_1 -> 15/2-_1",
         "parent_keV": 1610.4, "daughter_keV": None,
         "Egamma_tableII_keV": None, "Egamma_quoted_margin_keV": None,
         "Egamma_figure6_keV": None, "relative_Igamma": None,
         "T_half_parent_ns": 100., "T_half_margin_ns": 5.,
         "Bdown_E2_Wu": 2.58, "Bdown_margin_Wu": .29, "ICC_numeric": None,
         "role": "Previous-work context; used to adjust SN100PN proton charge in this paper, not its independent validation",
         "locator": "Sec.IV PDF p.13; Table III PDF p.14/printed p.13"},
    ]
    allowed = list(range(11-4, 11+5, 2))
    assert allowed == [7, 9, 11, 13, 15]
    assert 19 not in allowed and abs(19-11) > 4
    result = {
        "schema": "Vogt2017-primary-Rstat-first-readiness-v1",
        "actual_checked_at": datetime.now(timezone.utc).isoformat(),
        "bibliography": bibliography,
        "137Ba_current_status": {
            "candidate_assignment_available": True,
            "assignment": "(15/2-) at 2229.8 keV",
            "assignment_basis": "Isotonic systematics; parentheses retained in Fig.6 and Table II, with shell-model discussion in Sec.IV.",
            "globally_complete_lowest_state_identification_established": None,
            "absolute_E2_denominator_available_in_this_paper": False,
            "experimental_Rstat_first": None,
            "missing": ["Independent lifetime of the 2229.8-keV state or another absolute E2 measurement",
                        "Numerical branch/ICC data needed for a fresh lifetime-to-strength extraction"],
            "old_ENSDF_absence": "Retained only as a historical result for the checked 2007 dataset, not current research status.",
        },
        "constraints": constraints,
        "lifetime_attribution": {
            "gate_energy_keV_approx": 1568,
            "fitted_parent_keV": 2349.9,
            "fitted_parent_Jpi": "(19/2-)",
            "T_half_ns": 589., "quoted_margin_ns": 20.,
            "method": "GAMMASPHERE gamma-time matrix; six fit windows between 100 and 700 ns; weighted arithmetic mean",
            "not_the_half_life_of": "2229.8-keV (15/2-) state",
            "locator": "Sec.III B and Fig.7, accepted PDF p.9, printed p.8",
            "no_further_few_ns_lifetime_statement_scope": "The paper explicitly says above the 2349.9-keV state; it is not a quantified lifetime bound for the lower 2229.8-keV state.",
        },
        "ICC": {
            "published_B_values_already_corrected": True,
            "source": "Table III caption, reference [69]: Kibedi et al., NIM A 589, 202-229 (2008), BrIcc",
            "numeric_alpha_values_reported_for_target_or_120keV": None,
            "policy": "Do not set missing ICC to zero or apply a second correction to the published B(E2).",
        },
        "separate_benchmark_scope": {
            "observed": "137Ba B(E2;(19/2-)->(15/2-))=0.46(3) W.u.",
            "direct_Rstat_first_input": False,
            "direct_initial_11over2_cubic_moment_input": False,
            "allowed_intermediate_two_J_from_11over2_rank2": allowed,
            "reason": "Both intermediate spins in R[i,a] R[a,b] R[b,i] must couple directly to J=11/2 by rank 2; J=19/2 cannot.",
            "future_model_comparison": "Separate EM test with an explicitly fixed state mapping and operator; no model comparison or retuning performed here.",
            "author_state_ordering_caveat": "Sec.IV discusses interchanging the first two calculated 19/2 states in PQM130; this is not permission to choose a model ordinal after seeing B(E2).",
        },
        "author_theory_137Ba_tableIII": [
            {"model": "PQM130", "two_J_initial": 19, "initial_ordinal": 1, "Einitial_keV": 2595, "B_E2_Wu": .31},
            {"model": "PQM130", "two_J_initial": 19, "initial_ordinal": 2, "Einitial_keV": 2688, "B_E2_Wu": .41},
            {"model": "SN100PN", "two_J_initial": 19, "initial_ordinal": 1, "Einitial_keV": 2105, "B_E2_Wu": .01},
            {"model": "SN100PN", "two_J_initial": 19, "initial_ordinal": 2, "Einitial_keV": 2452, "B_E2_Wu": 1.19},
        ],
        "theory_values_are_not_experimental_data": True,
        "cross_version_audited_entries_agree": True,
        "TableII_target_and_120keV_intensity_cells_visually_and_spatially_blank": True,
        "scope": "Only this primary paper and its two supplied manuscript copies; no wider literature search, model fitting, or invented uncertainties.",
        "old_outputs_sha256": old,
        "old_outputs_unchanged": all(sha(OUT/name) == digest for name, digest in old.items()),
        "source_page_reproductions_location": str(RAW.relative_to(ROOT))+"/inspection/",
        "article_package_may_include_full_PDF_or_page_reproductions": False,
    }
    assert result["old_outputs_unchanged"]
    for filename, data in [("vogt2017-metadata.json", bibliography),
                           ("vogt2017-readiness.json", result)]:
        with (OUT/filename).open("x") as stream:
            json.dump(data, stream, indent=2, ensure_ascii=False, allow_nan=False)
            stream.write("\n")
    with (OUT/"vogt2017-citation.bib").open("x") as stream:
        stream.write(bib)
    with (OUT/"vogt2017-constraints.csv").open("x", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(constraints[0]))
        writer.writeheader()
        writer.writerows(constraints)
    print(json.dumps({
        "citation_key": KEY, "publication_date": bibliography["publication_date"],
        "manifest": bibliography["raw_manifest"], "manifest_sha256": bibliography["raw_manifest_sha256"],
        "candidate_assignment_available": True, "Rstat_first_denominator_available": False,
        "separate_19to15_B_E2_Wu": .46,
        "old_outputs_unchanged": result["old_outputs_unchanged"],
    }, indent=2))


if __name__ == "__main__":
    main()
