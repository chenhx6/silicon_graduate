"""Verify the bounded archive and write source/locator metadata, not source text."""
import sys
sys.dont_write_bytecode = True
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path

ROOT = Path("/workspace/wiki")
OUT = Path(__file__).resolve().parent
RAW = ROOT / "raw/papers/gpt/query/20261106-spin-invariant-precedents"
LOCAL = "raw/papers/gpt/learning-daily/20261022-DAY20-be2-qt-deformation-systematics/"
NOM = "raw/papers/gpt/query/20261105-nomura2017-input-audit/"

# Locator scopes describe actual reading, not certification of authors' code.
SOURCES = [
    ("N17", "Nomura et al. 2017, PRC96,014304",
     "raw/papers/2017_Nomura et al_Shape-phase transitions in odd-mass γ -soft nuclei with mass A ≈ 130.pdf",
     "PDF p.11 Eqs.(12)-(15), Figs.14-15; p.13 Refs.42-43; associated TeX lines 1258-1311",
     "PDF/TeX exact-formula comparison; PDF p.11 visually checked",
     "J+2 only, n=5, magnitude cubic expression and bandhead CG conversion",
     "Printed definitions verified; actual implementation and numerical figures not reproduced"),
    ("W00", "Werner et al. 2000, PRC61,021301(R)",
     str((RAW/"werner2000-nucl-th-0005013.pdf").relative_to(ROOT)),
     "arXiv PDF pp.2-4, Eqs.(3)-(4),(8)-(11),(15)-(21)",
     "Ground-state definitions, closure, geometrical interpretation and approximations",
     "The cited simple two/three-link expressions are for 0_1+, not arbitrary J",
     "Author preprint; no independent final-publisher text comparison"),
    ("C86", "Cline 1986, Annual Review 36,683",
     LOCAL+"cline-1986-nuclear-shapes-coulomb-excitation.pdf",
     "printed pp.697-700; p.698 general-state 6j expansion; pp.705-708 Figs.8,10",
     "Definitions and applicability read; p.698 visually checked",
     "General-spin scalar method predates Nomura; nonzero-spin experimental examples and operator/truncation limits",
     "Review examples are not newly read independent experimental papers"),
    ("W05", "Werner, Scholl and von Brentano 2005, PRC71,054314",
     str((RAW/"werner2005-five-observables.pdf").relative_to(ROOT)),
     "arXiv PDF pp.2-5 Eqs.(1)-(15); Secs.III-IV",
     "Definition and first/second-order approximation discussion",
     "Explicit prior comparison of restricted-observable estimates with rotor and IBM invariants",
     "Ground-state approximation study; not the odd-A Ba/Xe J+2 prescription"),
    ("W06", "Werner et al. 2006, Rev. Mex. Fis. S52(4),103",
     str((RAW/"werner2006-structural-evolution.pdf").relative_to(ROOT)),
     "printed pp.103-104 Eqs.(1)-(13); p.106 Sec.5 Fig.3",
     "General-J definitions, ground-state specialization, spin-dependent IBM transitions",
     "Finite-spin q2 evolution and movement of the apparent critical point studied up to J=10",
     "Even-even IBM example, not the claimed odd-A diagnostic correction"),
    ("N16", "Nomura et al. 2016, PRC94,064310",
     str((RAW/"nomura2016-arxiv1610-00469.pdf").relative_to(ROOT)),
     "arXiv PDF p.9 Eq.(8); pp.10-11 Fig.10 and adjacent discussion",
     "Definition of restricted average B(E2) and DeltaJ=1 versus 2 behavior",
     "Explicit analogy/proxy and different branch-selection trends already demonstrated in odd Eu/Sm",
     "Different nuclei and quadratic proxy; no cubic Ba/Xe correction"),
    ("N18", "Nomura et al. 2018, PRC97,064314",
     str((RAW/"nomura2018-prolate-oblate-odd-mass.pdf").relative_to(ROOT)),
     "arXiv1803.07802v2 PDF pp.8-10, Eqs.(5)-(9); p.12 Ref.17",
     "All relevant formula text read; p.9 visually checked",
     "All allowed J-prime/J-double-prime channels and signed cubic expression replace the earlier restriction",
     "Printed expression still lacks explicit general-J 6j weights; not identified as an erratum or verified correction; publisher PDF returned 401"),
    ("H20", "Henderson 2020, PRC102,054306",
     LOCAL+"henderson-2020-quadrupole-invariant-convergence.pdf",
     "arXiv PDF pp.2-3 Eqs.(7)-(13); pp.5-7 Tables I-II; p.9 Sec.III",
     "General closure formula and finite-state/model-space convergence scope",
     "Published truncation-convergence benchmark; five states is not a universal closure guarantee",
     "Quantitative sample is lighter even-even nuclei, not odd Ba/Xe"),
    ("RZ21", "Rocchini and Zielinska 2021, Physics3,1237",
     str((RAW/"rocchini-zielinska2021-coulex-shell-model.pdf").relative_to(ROOT)),
     "printed p.1241, Eqs.(3)-(7), Sec.2.3",
     "Explicit arbitrary-spin two/three-link formulas and experimental signs",
     "General-spin 6j and normalization are an established method",
     "Method review; no independent Ba/Xe reanalysis"),
    ("B22", "Bally et al. 2022, EPJA58,187",
     str((RAW/"bally2022-xe128-129-130.pdf").relative_to(ROOT)),
     "arXiv PDF pp.7-9 Eqs.(12)-(20), Table2; p.16; p.18 Table5; p.21 App.A Eqs.(30)-(34)",
     "Shape-definition comparison, 129Xe exclusion and general-spin closure",
     "Direct A130 precedent: different shape estimators disagree in 128Xe; 129Xe Kumar evaluation withheld",
     "No calculation of the Nomura2017 J+2 bias; 129Xe full-invariant result absent by authors' stated choice"),
    ("R25", "Rouoof et al. 2025, PRC111,054309",
     str((RAW/"rouoof2025-e2-matrix-elements.pdf").relative_to(ROOT)),
     "arXiv PDF pp.12-17, Sec.IV C, Figs.11-14, conclusions",
     "Spin-dependent invariants, limited-versus-full available networks, configuration-mixing discussion",
     "Published microscopic finite-spin and truncation comparison",
     "Even-even TPSM; full means the stated four-band network, not the entire physical Hilbert space"),
    ("Q26", "Qureshie et al. 2026, arXiv2604.10972",
     str((RAW/"qureshie2026-e2-matrix-elements-II.pdf").relative_to(ROOT)),
     "PDF pp.9-11 Sec.III C and conclusions; Figs.12-18",
     "Discussion of energy-staggering versus invariant-based diagnoses",
     "Additional direct theoretical counterexample to treating shape proxies as interchangeable",
     "Preprint status; different proxy and even-even systems"),
    ("E21", "Boyukata et al. 2021, EPJA57,292, Erratum",
     str((RAW/"boyukata2021-erratum.pdf").relative_to(ROOT)),
     "entire one-page publisher erratum",
     "Entire correction read",
     "Search false positive: corrects funding project number only",
     "Does not correct Nomura or a quadrupole-invariant formula"),
    ("N17G", "Nomura et al. 2017, PRC96,064316",
     str((RAW/"nomura2017-gogny-gamma-soft.pdf").relative_to(ROOT)),
     "PDF abstract; E2-operator/model section; full-text keyword screen",
     "Targeted follow-up screening, not full technical replication",
     "Same-region alternative Gogny-IBFM calculation is a relevant model-dependence comparator",
     "No matching invariant-correction discussion identified by this targeted text screen"),
]


def main():
    stamp = datetime.now(timezone.utc).isoformat()
    manifest_path = RAW / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    for item in manifest["files"]:
        data = (ROOT/item["path"]).read_bytes()
        assert len(data) == item["size"]
        assert hashlib.sha256(data).hexdigest() == item["sha256"]
        assert not Path(item["path"]).is_absolute()
        assert item.get("retrieved_at") and item.get("access_scope")
        if item.get("kind") == "pdf":
            assert data.startswith(b"%PDF")
        if item["path"].endswith("rocchini-zielinska2021-coulex-shell-model.pdf"):
            item["license_observed"] = "CC BY 4.0, stated on acquired article page 1"
    manifest["requested_collection_date"] = "2026-11-06"
    manifest["clock_note"] = (
        "Directory date follows the user's requested 20261106 collection. "
        "retrieved_at fields are actual host datetime.now(timezone.utc) readings, "
        "which fall on 2026-11-05; they were not replaced by the nominal directory date."
    )
    manifest["updated_at"] = stamp
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n")
    records = []
    for sid,title,path,locators,read_scope,established,boundary in SOURCES:
        data = (ROOT/path).read_bytes()
        records.append({
            "id":sid, "title":title, "path":path, "size":len(data),
            "sha256":hashlib.sha256(data).hexdigest(), "locators":locators,
            "actual_read_scope":read_scope, "established_precedent":established,
            "applicability_boundary":boundary,
        })
    associated = []
    for path in [NOM+"arxiv-v2-v4.tex", NOM+"arxiv-v2-v4.bbl",
                 NOM+"nomura2017-v2-source.tar.gz"]:
        data=(ROOT/path).read_bytes()
        associated.append({"path":path, "sha256":hashlib.sha256(data).hexdigest(),
                           "size":len(data)})
    inventory = {
        "generated_at":stamp, "nominal_task_date":"2026-11-06",
        "clock_note":manifest["clock_note"], "sources":records,
        "associated_existing_originals":associated,
        "new_archive_manifest":str(manifest_path.relative_to(ROOT)),
        "archive_manifest_sha256":hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
        "extracted_text_and_images":"tmp/ba129-spin-invariant-precedents/",
        "not_done":[
            "No author IBFM code or wavefunctions certified.",
            "No parent/Planck numerical counterexample or closure calculation repeated.",
            "No claim of novelty or exhaustive search.",
            "No knowledge/PLAN/core/script/other-session edit or commit.",
        ],
    }
    (OUT/"source-inventory.json").write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+"\n")
    fields=["id","title","path","locators","actual_read_scope",
            "established_precedent","applicability_boundary"]
    f=io.StringIO(newline=""); writer=csv.DictWriter(f,fieldnames=fields,extrasaction="ignore")
    writer.writeheader(); writer.writerows(records)
    (OUT/"evidence-matrix.csv").write_text(f.getvalue())
    checks = {
        "checked_at":stamp, "archive_files_verified":len(manifest["files"]),
        "new_PDF_count":sum(x.get("kind")=="pdf" for x in manifest["files"]),
        "recorded_failed_access_attempts":manifest["access_attempts"],
        "root_relative_paths_sha256_size_timestamp_access_scope_verified":True,
        "source_PDF_count_in_inventory":len(records),
        "nomura_exact_formula_locators":"TeX1267-1282,1306-1311; PDF p.11",
        "no_novelty_conclusion":True,
    }
    (OUT/"checks.json").write_text(json.dumps(checks,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:v for k,v in checks.items() if k!="recorded_failed_access_attempts"},indent=2))


if __name__ == "__main__":
    main()
