"""Read-only corpus/receipt reconciliation; writes only this sidecar directory.

Reported intervals are evidence about prior records, never automatic reading
credit. No skills, generated modules or test results can complete a packet.
"""
from datetime import datetime, timezone
import csv
import hashlib
import json
from pathlib import Path
import re

import pymupdf

ROOT = Path("/workspace/wiki")
OUT = Path(__file__).resolve().parent
MILE = ROOT/"outputs/learning-milestones"
LEDGER = ROOT/"knowledge/synthesis/book-corpus-coverage-ledger.md"
BOOKS = {
    "BM-II": ("B25", "raw/books/nuclear structure Ⅱ_Bohr, Mottelson.pdf",
              "46015a1401bcbdd40d4fd7267a1b066b4aef662050dcf35693e4e3a10a6d417a", 772,
              "book-bohr-mottelson-nuclear-structure-vol2"),
    "Greiner": ("B10", "raw/books/Nuclear Models (Walter Greiner, Joachim A. Maruhn) (Z-Library).pdf",
                "db5e43efaa80877822540bf0caae9be93d54d5499c5df89faae69769e6f77091", 399,
                "book-greiner-nuclear-models"),
    "Petrache": ("B02", "raw/books/Chirality and Wobbling in Atomic Nuclei.pdf",
                 "787c7ae68836d95f4a9022f2c1e07177fefcebc11d752a62919b4b547e3fe7d2", 339,
                 "book-petrache-chirality-and-wobbling"),
    "Casten-1990": ("B34-added-casten", "raw/books/Nuclear Structure From A Simple Perspective Casten.pdf",
                    "9028649fb9fad55d6d624b88ef8bf8487e8462c07596d9a42bd6117552fa3ea9", 391,
                    "book-casten-nuclear-structure-simple-perspective"),
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expand(ranges):
    return {p for lo, hi in ranges for p in range(lo, hi+1)}


def intervals(pages):
    answer = []
    for p in sorted(pages):
        if answer and p == answer[-1][1]+1:
            answer[-1][1] = p
        else:
            answer.append([p, p])
    return answer


def compact(ranges):
    return ",".join(str(a) if a == b else f"{a}-{b}" for a,b in ranges)


def dump(name, value):
    with (OUT/name).open("x", encoding="utf-8") as f:
        json.dump(value, f, ensure_ascii=False, indent=2)
        f.write("\n")


def main():
    baseline_path = MILE/"20261102-book-corpus-inventory.json"
    add_path = MILE/"20261102-casten-book-corpus-addendum.json"
    baseline = json.loads(baseline_path.read_text())
    add = json.loads(add_path.read_text())
    assert sha(baseline_path) == add["baseline_sha256"]
    locked = {str(p.relative_to(ROOT)): sha(p) for p in (LEDGER, baseline_path, add_path)}
    identities = {}
    for book,(bid,raw,expected,count,card) in BOOKS.items():
        p=ROOT/raw
        assert sha(p)==expected
        with pymupdf.open(p) as doc:
            assert len(doc)==count
        source=ROOT/"knowledge/sources"/f"{card}.md"
        text=source.read_text()
        assert expected in text and raw in text
        identities[book] = dict(baseline_id=bid, raw_file=raw, sha256=expected,
                                physical_pages=count, size=p.stat().st_size,
                                source_page=str(source.relative_to(ROOT)),
                                source_page_snapshot_sha256=sha(source),
                                source_page_updated=re.search(r"(?m)^updated: (.+)$",text).group(1))
        locked[raw]=expected
    known={b["raw_file"] for b in baseline["books"]}
    current={p.as_posix() for p in (ROOT/"raw/books").rglob("*.pdf")}
    current={str(Path(p).relative_to(ROOT)) for p in current}
    additions=[]
    for rel in sorted(current-known):
        p=ROOT/rel
        with pymupdf.open(p) as doc:
            additions.append(dict(path=rel, sha256=sha(p), size=p.stat().st_size,
                                  physical_pages=len(doc),
                                  credit="none from file metadata; editions/translations kept distinct"))
    records=[]
    def receipt(book, suffix, ranges, kind, note=""):
        p=MILE/suffix
        data=json.loads(p.read_text())
        text=p.read_text()
        expected=BOOKS[book][2]
        assert expected in text
        locators=data.get("source_locators",data.get("rendered_pages",data.get("key_locators",[])))
        src=data.get("source",{})
        if not locators and isinstance(src,dict):
            locators=src.get("rendered_pages",[])
        outputs=[]
        for w in data.get("knowledge_writeback",[]):
            name=w.get("path","")
            if name.startswith(("knowledge/methods/","knowledge/concepts/","knowledge/synthesis/")):
                q=ROOT/name
                outputs.append(dict(path=name,exists=q.is_file(),
                                    snapshot_sha256=sha(q) if q.is_file() else None))
        records.append(dict(
            book=book,record=str(p.relative_to(ROOT)),sha256=sha(p),
            date=data.get("run_date",data.get("date","2026-11-02")),
            declared_pdf_intervals=ranges,coverage_kind=kind,
            record_status="record-verified: identity and locators audited; not automatic completion",
            reported_source_scope=src.get("scope") if isinstance(src,dict) else data.get("scope"),
            reported_object_locators=locators,
            source_hash_matches=True,durable_writeback_records=outputs,
            limitation=note,
        ))
        locked[str(p.relative_to(ROOT))]=sha(p)
    def card_record(book, ranges, date, locator, kind="selected-pages-source-record"):
        p=ROOT/identities[book]["source_page"]
        records.append(dict(book=book,record=str(p.relative_to(ROOT)),sha256=sha(p),
                            date=date,declared_pdf_intervals=ranges,coverage_kind=kind,
                            record_status="record-verified; current source card is a scoped declaration",
                            locator=locator,source_hash_matches=True,
                            limitation="Broad claim-table citations and reading_depth labels are not added as read intervals."))

    card_record("BM-II",[[212,214]],"2026-11-02","Scope, PDF212–214 / printed190–192")
    bm=[
        ("high-spin-asymmetric-rotor",[[197,197],[199,199],[201,201],[205,205],[207,207],[209,209],[211,218]],"selected-pages"),
        ("finite-spin-harmonic-benchmark",[[212,218]],"selected-section"),
        ("particle-rotor-appendix",[[219,230]],"selected-pages-in-appendix"),
        ("deformed-band-m1-e2-contract",[[76,80]],"bounded-section-text-reported"),
        ("rotational-intrinsic-coupling-mikhailov",[[167,196]],"bounded-section-text-reported"),
        ("nilsson-deformed-shell-model-coriolis",[[233,260],[265,277]],"bounded-section-text-reported"),
        ("particle-vibration-coupling-rpa",[[438,457]],"bounded-section-text-reported-with-locator-conflict"),
        ("collective-vibrations-and-sum-rules",[[64,66],[383,437],[620,656]],"bounded-sections-reported"),
    ]
    for suffix,ranges,kind in bm:
        note=""
        if suffix=="particle-vibration-coupling-rpa":
            note="PDF450 has Eq6-223c/d, not the claimed Eq6-258–261; PDF456 has Eq6-230, not Eq6-276. Do not promote the entire receipt as formula-verified."
        if suffix=="collective-vibrations-and-sum-rules":
            note="Rendered-page claim PDF483–485 lies outside all declared scope intervals; retain separately as an object-check assertion."
        receipt("BM-II",f"20261103-bm2-{suffix}.json",ranges,kind,note)
    card_record("Greiner",[[164,169]],"2026-11-05","Current source lines72–76; printed145–150")
    receipt("Greiner","20261104-greiner-nuclear-models-book-to-skill-closure.json",[],
            "generated-skill-only","Status complete means skill delivery, not reading completion. Zero page credit from this receipt.")
    card_record("Casten-1990",[[32,42],[201,245],[262,285],[290,335]],"2026-11-02",
                "Current source Scope and Reading Depth, numbered selected spans")
    receipt("Casten-1990","20261102-casten-ch02-ch05-reading.json",
            [[43,59],[62,153]],"bounded-review-reported",
            "Same-day addendum, not evidence that the original ledger already included Casten. End pages59/153 are blank; printed-range endpoints need correction.")
    receipt("Casten-1990","20261102-casten-ch07-ch09-reading.json",
            [[262,285],[328,347]],"bounded-review-reported",
            "PDF347 is blank. Ch7 overlaps the source card; Ch9 overlaps the tail of its Ch8 selected span.")
    receipt("Casten-1990","20261103-casten-ch10-experimental-design.json",
            [[350,385]],"chapter-scope-reported-with-pagination-correction",
            "Chapter body is PDF350–378 / printed335–363; 379/385 blank, 380–384 references. No whole-chapter credit from nominal interval alone.")
    receipt("Casten-1990","20261102-casten-book-to-skill-extraction.json",[],
            "extraction-and-generated-skill-only","Whole-file text extraction and ten skill cards give no reading credit.")
    card_record("Petrache",[[43,47],[56,57],[118,123],[244,246],[258,259]],"2026-11-02",
                "Current source explicit actual scope; chapter12 selected pages")
    chapters=[
        ("ch1-ch8-closure",[[20,42],[167,203]],"full-chapter-text-and-figures-reported"),
        ("ch2-frauendorf-topological-wobbling",[[43,80]],"chapter-text-reported-selected-objects"),
        ("ch3-chiral-geometry-and-selection-boundary",[[81,91]],"chapter-body-reported-references-excluded"),
        ("ch4-tanabe-top-on-top",[[94,109]],"full-chapter-text-and-figures-reported"),
        ("ch5-experimental-wobbling-evidence",[[110,126]],"chapter-scope-selected-objects"),
        ("ch6-lawrie-model-boundary",[[127,155]],"page-by-page-chapter-read-reported"),
        ("ch7-grodner-cs-chiral-transition",[[156,166]],"full-chapter-text-and-figures-reported"),
        ("ch9-zhao-tdcdft-chiral-precession",[[204,221]],"full-chapter-text-and-figures-reported"),
        ("ch10-chen-cdft-prm-wobbling",[[222,238]],"full-chapter-text-and-figures-reported"),
        ("ch11-ibfm-mixing-ratio",[[239,255]],"selected-formula-and-result-pages"),
        ("ch12-sheikh-tpsm-wobbling",[[256,274]],"full-chapter-text-and-figures-reported"),
        ("ch13-budaca-spin-dynamics",[[275,291]],"full-chapter-reported-object-page-conflict"),
        ("ch14-wang-tpsm-even-even",[[292,301]],"full-chapter-text-and-figures-reported"),
        ("ch15-qi-a80-chirality",[[302,310]],"full-chapter-text-and-figures-reported"),
        ("ch16-li-chen-cs-chiral-mchid",[[311,322]],"full-chapter-text-and-figures-reported"),
        ("ch17-zhang-gamma-vibrational-model",[[323,337]],"full-chapter-text-and-figures-reported"),
    ]
    for suffix,ranges,kind in chapters:
        note="Chapter-level reading declaration retained; this audit does not newly certify every object, exercise or recall requirement."
        if suffix.startswith("ch13"):
            note+=" Figure13.1–13.6 locators259/260/261/264/266/268 are PRINTED folios; physical pages278/279/280/283/285/287. PDF259 is chapter12."
        if suffix.startswith("ch3-"):
            note+=" PDF92–93 are explicitly classified as references, not covered as chapter-body text."
        receipt("Petrache",f"20261103-petrache-{suffix}.json",ranges,kind,note)
    summaries={}
    packet_rows=[]
    for book,(bid,raw,expected,n,card) in BOOKS.items():
        rr=[r for r in records if r["book"]==book]
        union=set().union(*(expand(r["declared_pdf_intervals"]) for r in rr))
        memberships={p:sum(p in expand(r["declared_pdf_intervals"]) for r in rr) for p in union}
        repeated={p for p,c in memberships.items() if c>1}
        summaries[book]=dict(
            reported_scope_union=intervals(union),
            reported_scope_unique_page_count=len(union),
            reported_scope_overlap_ranges=intervals(repeated),
            reported_scope_overlap_unique_pages=len(repeated),
            no_explicit_interval_record_ranges=intervals(set(range(1,n+1))-union),
            meaning="Record-range accounting only. Selected scopes may include unread pages, references or blanks. Counts are not completed-reading percentages.",
            fully_certified_chapters_awarded_by_this_audit=0,
        )
        prefix="Q-B34" if book=="Casten-1990" else "Q-"+bid
        for ix,lo in enumerate(range(1,n+1,40),1):
            hi=min(lo+39,n);ps=set(range(lo,hi+1))
            packet_rows.append(dict(
                book=book,packet=f"{prefix}-{ix:03}",pdf_start=lo,pdf_end=hi,
                origin="Nov2 Casten addendum" if book=="Casten-1990" else "original 318-packet queue",
                recorded_scope_overlap=compact(intervals(ps&union)),
                new_completed_unit_overlap=compact(intervals(ps&set(range(66,72)))) if book=="BM-II" else "",
                status="not completed as a 40-page packet; original ledger unchanged",
            ))
    next_units=[
        dict(book="BM-II",pdf=[72,75],printed=[50,53],packet="Q-B25-002",
             topic="Continuation of 4-3b: generalized E2 intensity relations and corrections",
             status="No bounded continuous reading receipt located; newly completed unit stops at71"),
        dict(book="Greiner",pdf=[170,175],printed=[151,156],packet="Q-B10-005",
             topic="6.5.2 quantal Hamiltonian after rotation-vibration classical energy",
             status="PDF170 heading source-checked only; 170–175 not a completed unit"),
        dict(book="Casten-1990",pdf=[156,163],printed=[141,148],packet="Q-B34-004/Q-B34-005",
             topic="Beginning of Chapter6 collective excitations",
             status="Concept/skill citations exist; no corresponding bounded full-interval reading receipt located"),
        dict(book="Petrache",pdf=[247,251],printed=[228,232],packet="Q-B02-007",
             topic="Chapter11 IBFFM-2 continuation, particle-core and residual interaction dictionary",
             status="Inside a selected-formula receipt, so needs continuous-unit completion; not asserted never previously inspected"),
    ]
    record=dict(
        schema="book-coverage-reconciliation-v1",
        review_date="2026-11-06",observed_utc=datetime.now(timezone.utc).isoformat(),
        original_ledger=str(LEDGER.relative_to(ROOT)),original_ledger_sha256=sha(LEDGER),
        original_packet_count=sum((b["page_count"]+39)//40 for b in baseline["books"]),
        original_pdf_count=len(baseline["books"]),
        original_page_count=sum(b["page_count"] for b in baseline["books"]),
        casten_addendum_packet_count=add["current_packet_count"],
        target_identities=identities,
        current_pdf_path_count=len(current),missing_baseline_paths=sorted(known-current),
        additions_since_original_inventory=additions,
        inventory_boundary="Only target raw hashes and added-file metadata/hashes inspected; no full original-corpus hash refresh or automatic edition/translation curriculum merge.",
        records=records,summaries=summaries,
        chapter_completion_boundary="Full-chapter reading receipts are retained as record-verified declarations, distinct from selected checks and generated modules. No new chapter or original packet completion is awarded solely from these records.",
        new_completed_unit=dict(id="U-B25-002-E2-20261106",pdf=[66,71],printed=[44,49],
                                original_packet="Q-B25-002",whole_assigned_interval_read=True,
                                figures_checked=["Fig4-5 graph on PDF70 and caption PDF71"],
                                equations_checked="4-66 through4-73; includes4-68a/b",
                                full_section_or_chapter_complete=False,
                                overlap_with_existing_declared_ranges=[66],
                                new_pages_outside_existing_declared_ranges=[67,68,69,70,71],
                                methods="All six native-text pages read, then all six page renders visually checked; exact algebra and counter-limit check retained separately."),
        next_uncredited_units=next_units,input_snapshot_hashes=locked,
    )
    assert record["original_packet_count"]==318
    dump("coverage-reconciliation.json",record)
    with (OUT/"packet-crosswalk.csv").open("x",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(packet_rows[0]));w.writeheader();w.writerows(packet_rows)
    flat=[dict(book=r["book"],date=r["date"],record=r["record"],sha256=r["sha256"],
               physical_pdf_intervals=compact(r["declared_pdf_intervals"]),
               coverage_kind=r["coverage_kind"],status=r["record_status"],limitation=r.get("limitation",""))
          for r in records]
    with (OUT/"interval-evidence.csv").open("x",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(flat[0]));w.writeheader();w.writerows(flat)
    for rel,h in locked.items():
        assert sha(ROOT/rel)==h,rel
    print(json.dumps({"records":len(records),"packets":len(packet_rows),
                      "original_packets":318,"current_pdf_paths":len(current),
                      "summaries":summaries},ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
