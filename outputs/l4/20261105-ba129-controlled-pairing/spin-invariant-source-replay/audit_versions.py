"""Compare archived Nomura arXiv versions without reading any model results.

Originals remain in their authorized raw directories. This script writes only
hashes, locators and comparison results to this audit's output directory.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import tarfile
import time

import pymupdf

ROOT = Path("/workspace/wiki")
OUT = ROOT / "outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-source-replay"
RAW1 = ROOT / "raw/papers/gpt/query/20261106-nomura-invariant-version-audit"
RAW2 = ROOT / "raw/papers/gpt/query/20261105-nomura2017-input-audit"
V2PDF = ROOT / "raw/papers/2017_Nomura et al_Shape-phase transitions in odd-mass γ -soft nuclei with mass A ≈ 130.pdf"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load_archive(path, expected):
    assert sha(path.read_bytes()) == expected
    with tarfile.open(path) as archive:
        return {
            m.name: archive.extractfile(m).read()
            for m in archive.getmembers() if m.isfile()
        }


def block(text, start, end):
    begin = text.index(start)
    finish = text.index(end, begin) + len(end)
    value = text[begin:finish]
    uncommented = re.sub(r"(?m)%.*$", "", value)
    return {
        "line_start": text[:begin].count("\n") + 1,
        "line_end": text[:finish].count("\n") + 1,
        "exact_sha256": sha(value.encode()),
        "whitespace_and_comment_normalized_sha256":
            sha(re.sub(r"\s+", "", uncommented).encode()),
    }


def geometry_digest(drawings):
    # Equality is also tested directly. Hash uses PyMuPDF's deterministic
    # repr in this recorded runtime, not a claim of a version-neutral format.
    return sha(repr(drawings).encode())


def main():
    start = time.perf_counter()
    archive1 = RAW1 / "nomura2017-v1-source.tar.gz"
    archive2 = RAW2 / "nomura2017-v2-source.tar.gz"
    v1 = load_archive(archive1, "4c018fac3e73402df11a3b57430d5f9f4407d37f06f8fd83f8095748cb864a59")
    v2 = load_archive(archive2, "f7ed6dc746f50f16169d8796e4d12becd8827eaf4ac2ee4d5f1ff9cd04690faf")
    tex1, tex2 = v1["v2.tex"].decode(), v2["v4.tex"].decode()
    # Verify the inspected, line-located derivatives are exact members.
    tmp = ROOT / "tmp/ba129-spin-invariant-source-replay"
    assert (tmp / "v1-v2.tex").read_bytes() == v1["v2.tex"]
    assert (tmp / "nomura2017-v2-v4.tex").read_bytes() == v2["v4.tex"]
    specs = [
        ("total_E2_decomposition", "The E2 operator contains", "The expression for the IBM boson E2 operator:"),
        ("Eq7_boson_E2", r"\hat T^{(E2)}_B =", r"\end{eqnarray}"),
        ("Eq8_fermion_E2", "The fermion E2 operator used", r"\end{eqnarray}"),
        ("charges_and_chi_prime", "the effective charge $e_B$ is determined", "standard IBFM calculations performed in this and other mass regions"),
        ("Eq12_q2", "q_2=", r"\end{eqnarray}"),
        ("Eq13_q3", "q_3=", r"\end{eqnarray}"),
        ("Jprime_restriction", r"where $J^{\prime}=J+2$", "energies of the levels"),
        ("n5", "present study, the sum runs", "$n=5$."),
        ("Eq14_Eq15_beta_gamma", r"\label{eq:eff_beta}", r"\end{eqnarray}"),
    ]
    blocks = []
    for name, begin, end in specs:
        a, b = block(tex1, begin, end), block(tex2, begin, end)
        exact = a["exact_sha256"] == b["exact_sha256"]
        normalized = (a["whitespace_and_comment_normalized_sha256"]
                      == b["whitespace_and_comment_normalized_sha256"])
        assert normalized, name
        blocks.append(dict(name=name, v1=a, v2=b,
                           exact_equal=exact, normalized_equal=normalized))
    figures = []
    for member in ["even.qinvar.pdf", "oddn.qinvar.pdf", "even.level.pdf", "ba.level.pdf"]:
        with pymupdf.open(stream=v1[member], filetype="pdf") as a, \
                pymupdf.open(stream=v2[member], filetype="pdf") as b:
            da, db = a[0].get_drawings(), b[0].get_drawings()
            ta, tb = a[0].get_text(), b[0].get_text()
            assert da == db, member
            label_only = ta.replace("(deg.)", "(deg)") == tb
            assert label_only, member
            figures.append({
                "member": member,
                "v1_sha256": sha(v1[member]), "v2_sha256": sha(v2[member]),
                "byte_identical": v1[member] == v2[member],
                "page_rect_equal": a[0].rect == b[0].rect,
                "drawing_geometry_equal": da == db,
                "drawing_count_v1": len(da), "drawing_count_v2": len(db),
                "drawing_repr_sha256_v1": geometry_digest(da),
                "drawing_repr_sha256_v2": geometry_digest(db),
                "extracted_text_equal": ta == tb,
                "text_equal_after_deg_period_removal": label_only,
                "text_difference_description":
                    "gamma axis unit label loses its period: (deg.) -> (deg)"
                    if ta != tb else "none",
                "v1_pdf_metadata": a.metadata, "v2_pdf_metadata": b.metadata,
            })
    record = (RAW1 / "arxiv-v1-record.html").read_text()
    assert "24 Apr 2017 09:13:22 UTC" in record
    assert "8 Jul 2017 04:43:46 UTC" in record
    crossref = json.loads((RAW1 / "crossref-article.json").read_text())["message"]
    assert crossref["published"]["date-parts"] == [[2017, 7, 7]]
    pdfs = []
    for version, path, digest in [
        ("v1", RAW1 / "nomura2017-v1.pdf", "b7662bdd1d24c66ae9d0b81e95746c150dae1d51ec5c22cb9f5b8e9505062d2d"),
        ("v2", V2PDF, "481e6a9e0f6b01e9c5db5e2b06d9b350dba0638393c7da7f532c3040e9efaea9"),
    ]:
        assert sha(path.read_bytes()) == digest
        with pymupdf.open(path) as doc:
            first = re.sub(r"\s+", " ", doc[0].get_text())
            pdfs.append({
                "arxiv_version": version, "path": str(path.relative_to(ROOT)),
                "sha256": digest, "pages": len(doc),
                "dated_string": re.search(r"\(Dated: (.*?)\)", first).group(1),
                "metadata": doc.metadata,
            })
    assert r"\date{\today}" in tex1 and r"\date{\today}" in tex2
    manifest = json.loads((RAW1 / "manifest.json").read_text())
    aps = next(f for f in manifest["files"] if f["source_role"] == "access-failure")
    assert aps["http_status"] == 403
    result = {
        "review_date_declared": "2026-11-06",
        "container_observed_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Source-only arXiv v1/v2 comparison; no kernel/case/probe read.",
        "pymupdf_version": pymupdf.VersionBind,
        "arxiv_submitted_utc": {"v1": "2017-04-24T09:13:22+00:00", "v2": "2017-07-08T04:43:46+00:00"},
        "journal_identity": {
            "doi": "10.1103/PhysRevC.96.014304", "year": 2017,
            "volume": "96", "article": "014304",
            "publisher_deposited_publication_date": "2017-07-07",
            "date_source": "archived Crossref metadata",
        },
        "archives": [
            {"version": "v1", "path": str(archive1.relative_to(ROOT)), "sha256": sha(archive1.read_bytes()),
             "manuscript_member": "v2.tex", "manuscript_sha256": sha(v1["v2.tex"])},
            {"version": "v2", "path": str(archive2.relative_to(ROOT)), "sha256": sha(archive2.read_bytes()),
             "manuscript_member": "v4.tex", "manuscript_sha256": sha(v2["v4.tex"])},
        ],
        "pdfs": pdfs, "both_tex_date_commands": r"\date{\today}",
        "date_interpretation": "2022 and 2021 Dated strings match PDF regeneration metadata; arXiv version submission and journal publication remain 2017.",
        "equation_and_parameter_blocks": blocks, "figures": figures,
        "Q_dictionary": {
            "positive_textual_evidence": "Invariants are described as calculated using E2 matrix elements; this supports the E2 reading.",
            "explicit_Q_equals_TE2_or_QB_found": False,
            "distinct_defined_tensors": "HB uses QB(chi); E2 uses TB(eB,chi-prime)+TF(eF).",
            "remaining_boundary": "No producer-level Q/RME/units dictionary, invariant evaluation code, transition-matrix dump or numerical eB table in either source package.",
            "Eq8_notation": "Both versions label the fermion expression T(E2) without a subscript F; surrounding prose explicitly identifies the fermion term.",
            "commented_expression": "The commented generic Q RME in Eq8 is not an executable or printed definition of Q in Eqs12-15.",
        },
        "other_diffs_inspected": [
            "Exchange beta index jj-prime -> jj-double-prime; identical consequence in the all-indices-equal single-j restriction.",
            "An extra g_F multiplying the fermion M1 expression is removed in v2.",
            "Table V negative-parity monopole header becomes A-prime_(11/2); the selected numerical row is unchanged.",
            "Invariant captions/prose are edited but no relevant E2/invariant expression or plotted geometry changes.",
        ],
        "version_of_record_boundary": {
            "publisher_fulltext_compared": False,
            "aps_http_status": 403, "aps_archived_response": aps["path"],
            "claim": "The exact checks concern arXiv v1/v2 and the held regenerated v2 PDF. Journal DOI/date metadata do not establish VOR text or figure identity.",
        },
        "manifest_path": str((RAW1 / "manifest.json").relative_to(ROOT)),
        "manifest_sha256": sha((RAW1 / "manifest.json").read_bytes()),
        "runtime_seconds": time.perf_counter()-start,
    }
    payload = json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False)+"\n"
    with (OUT / "version-comparison.json").open("x", encoding="utf-8") as f:
        f.write(payload)
    print(json.dumps({
        "equation_blocks_compared": len(blocks),
        "all_exact_equal": all(x["exact_equal"] for x in blocks),
        "figure_geometry_equal": {x["member"]:x["drawing_geometry_equal"] for x in figures},
        "figure_bytes_equal": {x["member"]:x["byte_identical"] for x in figures},
        "runtime_seconds": result["runtime_seconds"],
    }, indent=2))


if __name__ == "__main__":
    main()
