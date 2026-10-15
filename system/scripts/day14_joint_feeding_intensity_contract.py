#!/usr/bin/env python3
"""Two observed feeders, transition/node intensity identity and conditional weights.

Contract A and pure-E1 B transfer are explicitly assumed controls. Contract B
remains symbolic because ICC/normalization inputs were not established.
"""
from __future__ import annotations

import argparse
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path

from day14_unobserved_feeding_transfer import tensor, transfer
from day14_feeding_fraction_moment_bound import geometry, normalized_point, slack, positive_certificate, dec

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02"
TOL = D("1e-50")


def u_value(ti, tf, multipole, rank):
    result = transfer(ti, tf, multipole, rank)
    ci, cf = tensor(ti, rank)[1], tensor(tf, rank)[1]
    return dec(F(result["rational_eigenvalue"]))*(dec(cf)/dec(ci)).sqrt()


def solve(precision):
    with localcontext() as ctx:
        ctx.prec = precision
        data = json.loads((RUN / "tm167-intensity-joint-input.json").read_text())
        checks = {}
        def check(name, value):
            checks[name] = bool(value)
            if not value:
                raise AssertionError(name)
        rows = {r["gamma_kev"]: r for r in data["rows"]}
        check("nine_literal_graph_bound_rows", len(rows) == 9)
        for name, a, b in [("parent993", "371.52", "304.41"), ("parent1086", "397.38", "345.20")]:
            check("same_parent_"+name, rows[a]["parent_id"] == rows[b]["parent_id"])
            check("different_reported_values_"+name, D(rows[a]["I_table"]) != D(rows[b]["I_table"]))
        target = data["target_id"]
        check("known_incoming_bind_to_target", all(rows[e]["target_id"] == target for e in ["271.12","218.90"]))
        check("known_outgoing_bind_from_target", all(rows[e]["parent_id"] == target for e in ["184.33","99.21"]))
        check("B_parent_probe_binds_to_B_feeder", rows["318.135"]["parent_id"] == rows["218.90"]["parent_id"])
        residuals = {e: D(r["parent_energy"])-D(r["target_energy"])-D(e) for e,r in rows.items()}
        check("nonzero_printed_energy_residuals_retained", any(v != 0 for v in residuals.values()))
        tf = data["target_experimental"]["spin_twice"]
        geo = geometry(tf)
        parent = {tag:[D(data["parent"+tag]["rho2"]),D(data["parent"+tag]["rho4"])] for tag in ["A","B"]}
        for tag in ["A","B"]:
            positive_certificate(normalized_point(parent[tag], geometry(data["parent"+tag]["spin_twice"])), geometry(data["parent"+tag]["spin_twice"]))
        ua = [u_value(17,tf,2,k) for k in [2,4]]
        ub = {l:[u_value(15,tf,l,k) for k in [2,4]] for l in [1,2]}
        check("B_U_rows_match_printed_precision", all(abs(float(ub[l][i])-data["YA_U_B_table"][f"L{l}"][f"U{k}"]) <= .00000501 for l in [1,2] for i,k in enumerate([2,4])))
        f = {"A":[ua[i]*parent["A"][i] for i in range(2)], "B":[ub[1][i]*parent["B"][i] for i in range(2)]}
        nf = {tag:normalized_point(v,geo) for tag,v in f.items()}
        check("both_known_reference_components_positive", all(slack(face,v) >= -TOL for face in geo["faces"] for v in nf.values()))
        exp = [D(data["target_experimental"]["rho2"]),D(data["target_experimental"]["rho4"])]
        ne = normalized_point(exp,geo)
        ratio = D(rows["218.90"]["I_table"])/D(rows["271.12"]["I_table"])
        bounds = []
        for face in geo["faces"]:
            n = slack(face,ne)
            den = slack(face,nf["A"])+ratio*slack(face,nf["B"])
            if den > TOL:
                bounds.append((n/den,face))
        bound, active = min(bounds,key=lambda x:x[0])
        bound = min(bound,1/(1+ratio))
        single = D(json.loads((RUN/"tm167-feeding-fraction-audit.json").read_text())["center_bound"])
        check("adding_knownB_tightens_A_center_bound", 0 < bound < single)
        rest_fraction = 1-(1+ratio)*bound
        rest = [(ne[i]-bound*nf["A"][i]-ratio*bound*nf["B"][i])/rest_fraction for i in range(2)]
        check("joint_bound_remainder_positive", all(slack(face,rest) >= -TOL for face in geo["faces"]))
        positive_certificate(rest,geo)
        den_closed = sum(D(rows[e]["I_table"]) for e in ["184.33","99.21"])
        wa, wb = D(rows["271.12"]["I_table"])/den_closed, D(rows["218.90"]["I_table"])/den_closed
        check("reference_scalar_weights_positive_normalized", 0 < wa and 0 < wb and wa+wb < 1)
        check("reference_closed_centers_not_all_exact_feasible", wa > bound)
        # This point is an author calculation, not another experimental vector.
        calc = [D(data["target_calculated_source_point"]["rho2"]),D(data["target_calculated_source_point"]["rho4"])]
        nc = normalized_point(calc,geo)
        rc = [(nc[i]-wa*nf["A"][i]-wb*nf["B"][i])/(1-wa-wb) for i in range(2)]
        witness = positive_certificate(rc,geo)
        check("author_calculated_target_inside_quoted_marginal_widths", all(abs(calc[i]-exp[i]) <= D(data["target_experimental"][f"quoted_error_rho{k}"]) for i,k in enumerate([2,4])))
        check("author_calculated_point_positive_reference_remainder", all(slack(face,rc) >= -TOL for face in geo["faces"]))
        mixes=[]
        angle = data["B_radiative_mixing"]["arctan_delta_deg"]
        half = data["B_radiative_mixing"]["angle_halfwidth"]
        lo_angle, hi_angle = angle-half, angle+half
        for theta in [lo_angle,0.,angle,hi_angle]:
            delta2=D(str(math.tan(math.radians(theta))**2))
            u=[(ub[1][i]+delta2*ub[2][i])/(1+delta2) for i in range(2)]
            mixes.append(dict(theta_deg=theta, delta_M2_over_E1_squared=delta2,U2=u[0],U4=u[1],scope="radiative unobserved kernel only; no mixed total-conversion transfer asserted"))
        check("pureE1_reference_declared_zero", data["B_radiative_mixing"]["reference_delta"] == 0)
        check("pureE1_reference_within_source_angle_interval", lo_angle <= 0 <= hi_angle)
        check("radiative_mixing_sensitivity_small_in_this_interval", max(abs(x["U2"]-ub[1][0]) for x in mixes)<D(".0002") and max(abs(x["U4"]-ub[1][1]) for x in mixes)<D(".0006"))
        check("field_and_covariance_boundaries_preserved", data["field_semantics_verified"] is False and data["actual_weights"] is None and data["actualCov"] is None and data["intensity_contract_B"]["alpha_response_values"] is None)
        check("doublet_quadruplet_warnings_kept", rows["184.33"]["peak_flag"]==rows["99.21"]["peak_flag"]=="D" and rows["371.52"]["peak_flag"]=="Q")
        return dict(precision=precision,checks=checks,check_count=len(checks),passed=all(checks.values()),
                    rows=data["rows"],printed_energy_residuals=residuals,
                    contract_A_unverified_reference=dict(B_over_A=ratio, target_known_out_sum=den_closed,
                        A_center_geometric_bound=bound, B_weight_at_bound=ratio*bound,
                        active_remainder_m_twice=active["m_twice"], fixed_other_fraction_at_bound=rest_fraction,
                        no_other_outgoing_reference_weights=dict(A=wa,B=wb,other=1-wa-wb),
                        author_calculated_target_witness=dict(target_rho=calc,remainder_moment_normalized=rc,
                            remainder_positive_example=witness,not_new_measurement_or_field_validation=True)),
                    U_A=ua,U_B_pure_L1=ub[1],U_B_pure_L2=ub[2],component_A=f["A"],component_B_reference=f["B"],
                    radiative_mixing_sensitivity=mixes,contract_B_symbolic=data["intensity_contract_B"],
                    measured_weights=None,actual_covariance=None,
                    interpretation="source-field conditional controls; not originalmodelreplay, missingbranch discovery or experimental confidence limit")


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=RUN/"tm167-intensity-joint-audit.json")
    args=parser.parse_args()
    low,high=solve(80),solve(110)
    key="A_center_geometric_bound"
    assert abs(low["contract_A_unverified_reference"][key]-high["contract_A_unverified_reference"][key]) < D("1e-60")
    high["precision80_110_same60digits_reference_bound"]=True
    high["dependency_sha256"]={p:hashlib.sha256((ROOT/"system/scripts"/p).read_bytes()).hexdigest() for p in ["day14_unobserved_feeding_transfer.py","day14_feeding_fraction_moment_bound.py"]}
    high["source_input_sha256"]=hashlib.sha256((RUN/"tm167-intensity-joint-input.json").read_bytes()).hexdigest()
    args.output.write_text(json.dumps(high,ensure_ascii=False,indent=2,default=str)+"\n")
    print(json.dumps(dict(passed=high["passed"],checks=high["check_count"],conditional_A=high["contract_A_unverified_reference"],no_actual_weights=True),default=str))


if __name__=="__main__":
    main()
