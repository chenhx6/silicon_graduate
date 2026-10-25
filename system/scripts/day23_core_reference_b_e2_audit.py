#!/usr/bin/env python3
"""Conditional printed-centre E2 arithmetic; no historical-source or fit certification."""
import argparse
import hashlib
import json
import math
from pathlib import Path

from day23_au187_api_identity import read_csv


def select(gamma_path, level_path, z, n, start, end):
    _, _, gs = read_csv(gamma_path)
    _, _, ls = read_csv(level_path)
    hits = [r for r in gs if (r["z"], r["n"], r["start_level_idx"], r["end_level_idx"])
            == (z, n, start, end)]
    parents = [r for r in ls if (r["z"], r["n"], r["idx"]) == (z, n, start)]
    if len(hits) != 1 or len(parents) != 1:
        raise ValueError("Target identity is missing or nonunique")
    g, level = hits[0], parents[0]
    outgoing = [r for r in gs if (r["z"], r["n"], r["start_level_idx"]) == (z, n, start)]
    guards = {"one_listed_E2_outgoing": len(outgoing) == 1 and g["multipolarity"] == "E2",
              "level_energy_join": g["start_level_energy"] == level["energy"],
              "half_life_unit_ps": level["unit_hl"] == "ps",
              "half_life_seconds_matches_ps": math.isclose(
                  float(level["half_life"])*1e-12, float(level["half_life_sec"]), rel_tol=1e-12)}
    if not all(guards.values()):
        raise ValueError(f"Unmet input guards: {guards}")
    energy = float(g["energy"])/1000
    thalf = float(level["half_life"])
    alpha = float(g["tot_conv_coeff"])
    mass = int(z)+int(n)
    # Declared radius r0=1.2 fm and the conventional Weisskopf E2 definition.
    bw = (1/(4*math.pi))*(3/5)**2*(1.2*mass**(1/3))**4/10000
    tau = thalf/math.log(2)
    tau_gamma = tau*(1+alpha)
    calculated = .0816/(energy**5*tau_gamma)
    table_wu = float(g["b_e2"])
    return {"gamma_tokens": g, "parent_tokens": level, "input_guards": guards,
            "listed_outgoing_count": len(outgoing), "BW_E2_eb2": bw,
            "mean_lifetime_ps": tau, "conditional_partial_photon_lifetime_ps": tau_gamma,
            "conditional_B_down_eb2": calculated,
            "conditional_B_down_Wu": calculated/bw,
            "table_B_down_Wu": table_wu, "table_B_down_eb2": table_wu*bw,
            "relative_centre_difference_to_table": calculated/(table_wu*bw)-1,
            "assumption": "The one listed E2/CE decay exhausts the level decay; no unlisted branch or additional multipole contributes. This is assumed, not proved by relative_intensity=100.",
            "source_cutoff": g["ensdf_publication_cut-off"]}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ["pt-gammas", "pt-levels", "au-gammas", "au-levels", "output"]:
        p.add_argument("--"+name, type=Path, required=True)
    a = p.parse_args()
    pt = select(a.pt_gammas, a.pt_levels, "78", "108", "1", "0")
    au = select(a.au_gammas, a.au_levels, "79", "108", "10", "2")
    x = {"calculation_status": "computed-conditional",
         "scope": "Modern API export and declared formulas only; not Baglin2003 full text, original experiment, historical source validation, independent evidence or original producer replay.",
         "inputs_sha256": {str(f): hashlib.sha256(f.read_bytes()).hexdigest()
                           for f in [a.pt_gammas, a.pt_levels, a.au_gammas, a.au_levels]},
         "pt186": pt, "au187": au,
         "formula": "B(E2)[e2b2]=0.0816*ln(2)/(E[MeV]^5*T_half[ps]*(1+alpha_total)), conditional on one exhaustive E2 channel",
         "quoted_reference_values": {"S20_core_eb2": .84, "SE21_core_eb2": 1.44,
                                     "both_quote_Au_reference_eb2": 1.49,
                                     "core_quote_ratio_only": 1.44/.84},
         "limitations": ["b_e2 and lifetime/conversion entries belong to the same evaluation chain, not independent measurements.",
                         "No complete covariance, alpha uncertainty or original reference notes restored; no new CI/total error interval computed.",
                         "Pt cutoff2022 and Au cutoff2008 cannot prove the original Baglin2003 values or every number behind Guo2022's broad bracket.",
                         "The two author publications retain beta=.23; a 1.714 ratio between quoted reference numbers is not a measured change in beta or actual model input.",
                         "Raw export archival remains deferred; these are temporary public snapshots."]}
    a.output.write_text(json.dumps(x, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"calculation_status": x["calculation_status"],
                      "Pt_B_conditional_eb2": pt["conditional_B_down_eb2"],
                      "Au_B_conditional_eb2": au["conditional_B_down_eb2"],
                      "independent_validation": False}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
