"""Pin primary passages and derive observable candidates from stored primary results.

No model imports, fits, diagonalizations, or coupling controls. All products
are new files in this sidecar; prior reports and parent results are preserved.
"""
import sys
sys.dont_write_bytecode=True
import csv
from datetime import datetime,timezone
import hashlib
import io
import json
import math
from pathlib import Path
import pymupdf

ROOT=Path("/workspace/wiki")
OUT=Path(__file__).resolve().parent
RAW=ROOT/"raw/papers/gpt/query/20261106-spin-invariant-precedents"
NEW=RAW/"focused-sidecar"
STUDY=ROOT/"outputs/l4/20261105-ba129-controlled-pairing/shape-closure-v1/study.json"


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def write_new(path,data):
    with path.open("x") as f:
        f.write(json.dumps(data,ensure_ascii=False,indent=2)+"\n")


def main():
    pins=[]
    specs=[
        (
            "N16",RAW/"nomura2016-arxiv1610-00469.pdf",9,
            "depends on whether a band exhibits a weak-coupling or strong-coupling systematics.",
            "PDF p.9 Eq.(8); p.10 paragraph below Fig.9; p.11 Fig.10(a-d), caption.",
            "Definition and discussion of five-state DeltaJ=1/2 indicators in odd Eu/Sm; Fig.10 visually checked.",
        ),
        (
            "R25",RAW/"rouoof2025-e2-matrix-elements.pdf",12,
            "only those TPSM matrix elements",
            "PDF pp.12-13 Sec.IV C; p.13 first paragraph below Fig.13; p.16 conclusion item 2.",
            "Larger four-band network versus experimentally covered subset; smaller dispersion with restricted network.",
        ),
        (
            "L25",NEW/"lawrie-orce2025-simple-ratios-publisher.pdf",2,
            "as an empirically established dependence.",
            "Publisher pp.2-3 Eqs.(5)-(13), Fig.1; pp.4-5 Eqs.(14)-(15), Fig.3; Table1 pp.7-9.",
            "Main text read; p.3 visually checked. No reanalysis of the tabulated experimental data.",
        ),
        (
            "F26",NEW/"frauendorf2026-systematic-tpsm-2609.10431v1.pdf",4,
            "The apparent contradiction reveals a limitation of the CM.",
            "PDF pp.4-5 Sec.4, Eqs.(10)-(14), Figs.7-10; p.6 Refs.8-10.",
            "Six-page preprint read; p.4 visually checked. References and figure provenance identify reuse of TPSM studies.",
        ),
    ]
    for sid,path,page,quote,locator,scope in specs:
        document=pymupdf.open(path)
        text=" ".join(document[page].get_text().split())
        assert quote in text,(sid,quote)
        assert len(quote.split())<=25
        pins.append({
            "id":sid,"path":str(path.relative_to(ROOT)),"sha256":sha(path),
            "size":path.stat().st_size,"pdf_pages":len(document),
            "literal_excerpt":quote,"excerpt_pdf_page_one_based":page+1,
            "locators":locator,"actual_read_scope":scope,
        })
    write_new(OUT/"source-pinpoints.json",{
        "recorded_at_actual_utc":datetime.now(timezone.utc).isoformat(),
        "sources":pins,
        "new_source_metadata":{
            "F26":"arXiv2609.10431v1, submitted 2026-09-09 16:43:36 UTC; journal publication not established here.",
            "L25":"Lawrie and Orce, ADND164 (June 2025) 101730; publisher PDF online 2025-04-25; CC BY-NC-ND4.0.",
        },
        "dependence":"F26 cites R25 as Ref.9, earlier 104Ru work as Ref.8 and the follow-up as Ref.10; do not count repeated figures as independent evidence.",
        "unreconciled_source_difference":"F26 p.5 calls the Os cases gamma rigid; R25 p.16 item3 describes moderate gamma softness. No reconciliation or validation of either classification was performed.",
    })
    study_hash=sha(STUDY)
    data=json.loads(STUDY.read_text())
    inputs=dict(data["input_sha256"])
    current={p:sha(ROOT/p) for p in inputs}
    assert current==inputs
    rows=[]
    for c in data["cases"]:
        p=c["primary"]
        full=p["full"]
        channels={x["two_J"]:x for x in p["quadratic_channels"]}
        splus=channels[15]["q2_e2b2"]
        ss=p["same_spin"]
        d=ss["static_q2_e2b2"]; same=ss["other_same_spin_q2_e2b2"]
        firstplus=next(x for x in p["selected_matrix_elements"]
                       if x["two_J_final"]==15 and x["ordinal_zero_based"]==0)
        selected_same=[x for x in p["selected_matrix_elements"]
                       if x["two_J_final"]==11 and not x["same_state"]]
        r5=next(x for x in p["restricted"] if x["max_states"]==5)
        rall=next(x for x in p["restricted"] if x["max_states"] is None)
        assert abs(d+same-channels[11]["q2_e2b2"])<1e-10
        # Standard spectroscopic quadrupole convention, J=11/2:
        # |<J J;2 0|J J>|^2 = J(2J-1)/[(J+1)(2J+3)] = 55/91.
        inferred_d=(5/(16*math.pi))*ss["spectroscopic_Qs_eb"]**2/(55/91)
        assert abs(d-inferred_d)<1e-10
        if r5["raw_proxy_ratio"]>1:
            assert r5["proxy_angle_deg"] is None
        cancellation=p["cubic_cancellation"]
        assert abs(cancellation["sum_positive_spin_pairs_e3b3"]
                   +cancellation["sum_negative_spin_pairs_e3b3"]-full["q3_e3b3"])<1e-10
        row={
            "odd_A":c["case"]["odd_A"],"eB_eb":c["calibration"]["eB"],
            "eF_eb":c["calibration"]["eF_eb"],"q2_primary_e2b2":full["q2_e2b2"],
            "signed_cubic_ratio":full["signed_ratio"],
            "folded_full_angle_deg":full["folded_rigid_equivalent_angle_deg"],
            "proxy_n5_ratio":r5["raw_proxy_ratio"],"proxy_n5_angle_deg":r5["proxy_angle_deg"],
            "proxy_all_Jplus2_ratio":rall["raw_proxy_ratio"],
            "proxy_all_Jplus2_angle_deg":rall["proxy_angle_deg"],
            "Qs_model_eb":ss["spectroscopic_Qs_eb"],
            "static_strength_e2b2":d,"inelastic_same_spin_strength_e2b2":same,
            "all_Jplus2_strength_e2b2":splus,
            "R_static_to_all_Jplus2":d/splus,
            "R_inelastic_same_to_all_Jplus2":same/splus,
            "R_all_same_to_all_Jplus2":(d+same)/splus,
            "R_static_to_first_Jplus2":d/firstplus["B_E2_e2b2"],
            "first_Jplus2_fraction_of_channel":firstplus["B_E2_e2b2"]/splus,
            "static_fraction_of_same_spin_channel":d/(d+same),
            "first_two_other_same_spin_fraction_of_inelastic_channel":
                sum(x["B_E2_e2b2"] for x in selected_same)/same,
            "spin_sector_positive_q3_e3b3":cancellation["sum_positive_spin_pairs_e3b3"],
            "spin_sector_negative_q3_e3b3":cancellation["sum_negative_spin_pairs_e3b3"],
            "spin_sector_cancellation_factor":
                cancellation["sum_abs_spin_pairs_e3b3"]/abs(full["q3_e3b3"]),
            "primary_q2_reduced_minus_direct":p["closure"]["reduced_minus_direct_q2"],
            "primary_q3_reduced_minus_direct":p["closure"]["reduced_minus_direct_q3"],
            "observable_status":"conditional model prediction; physical moment benchmark pending",
        }
        rows.append(row)
    checks={
        "checked_at_actual_utc":datetime.now(timezone.utc).isoformat(),
        "parent_result":str(STUDY.relative_to(ROOT)),"parent_result_sha256":study_hash,
        "input_sha256":inputs,"all_recorded_input_hashes_match":True,
        "evidence_scope":"Read and arithmetic-checked parent calibrated calculation; no independent model rerun.",
        "max_primary_q2_closure_abs":max(abs(x["primary_q2_reduced_minus_direct"]) for x in rows),
        "max_primary_q3_closure_abs":max(abs(x["primary_q3_reduced_minus_direct"]) for x in rows),
        "A135_proxy_domain_failure_preserved":next(x for x in rows if x["odd_A"]==135)["proxy_n5_angle_deg"] is None,
        "physical_validation_pending":"Parent reports Galileo benchmarking static moments, including model Qs(137Ba)=0.772963 eb. No experimental agreement is claimed.",
        "causal_controls":"Assigned to Huygens; not inspected or rerun in this sidecar.",
        "rows":rows,
    }
    assert sha(STUDY)==study_hash
    write_new(OUT/"calibrated-observable-checks.json",checks)
    buffer=io.StringIO(newline="")
    writer=csv.DictWriter(buffer,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    with (OUT/"calibrated-observable-candidates.csv").open("x") as f:f.write(buffer.getvalue())
    print("Pinned four primary sources and derived five calibrated observable rows.")
    print("Maximum stored direct/6j errors:",checks["max_primary_q2_closure_abs"],checks["max_primary_q3_closure_abs"])
    for r in rows:
        print(r["odd_A"],"Qs",r["Qs_model_eb"],"Rstat",r["R_static_to_all_Jplus2"],
              "Rinel",r["R_inelastic_same_to_all_Jplus2"],"Rstat1",r["R_static_to_first_Jplus2"])


if __name__=="__main__":
    main()
