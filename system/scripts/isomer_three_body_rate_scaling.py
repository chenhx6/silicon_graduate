#!/usr/bin/env python3
"""Matrix-element and E2 phase-space scaling in the same finite toy model.

Compare a degenerate pure-pairing baseline with a particle-hole-conserving
J=2 two-body baseline that already splits J=10 and J=8. R=(Delta E)^5 B is
a dimensionless proxy, not a decay rate in s^-1 or a lifetime prediction.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import isomer_three_body_ph_breaking as three
import isomer_seniority_transfer_validation as old


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def baseline(jval, eta):
    block = three.block(jval)
    block["h"] = old.ham(6, jval, eta)
    v, energy, *_ = three.solve(block, 0.0, block["ref"])
    block["ref"] = v
    return block, energy


def first_derivative(block, energy):
    z = block["z"]
    en, u = np.linalg.eigh(z.T @ block["h"] @ z)
    states = z @ u
    derivative = np.zeros_like(block["ref"])
    for e, vec in zip(en, states.T):
        if abs(e - energy) > 1e-9:
            derivative += vec * (vec @ block["v"] @ block["ref"]) / (energy - e)
    return derivative


def analyze(eta):
    initial, ei0 = baseline(10, eta)
    final, ef0 = baseline(8, eta)
    vi0, vf0 = initial["ref"], final["ref"]
    a0 = three.components(vi0, vf0)[0]
    assert a0["strength"] < 1e-25
    for b in (initial, final):
        c = old.conjugation(6, 2*b["J"])
        assert np.linalg.norm(b["h"]@c-c@b["h"]) < 1e-10
    di, df = first_derivative(initial, ei0), first_derivative(final, ef0)
    slope = (three.components(di, vf0)[0]["amplitude"]
             + three.components(vi0, df)[0]["amplitude"])
    w = old.w3j(16, 4, 20, -16, 0, 16)
    bcoef = slope*slope/(21*w*w)
    de0 = ei0-ef0
    deslope = float(vi0@initial["v"]@vi0-vf0@final["v"]@vf0)
    if abs(de0) < 1e-12:
        exponent = 7
        rcoef = deslope**5*bcoef
    else:
        assert de0 > 0
        exponent = 2
        rcoef = de0**5*bcoef
    rows = []
    refi, reff = vi0, vf0
    for lam in (1e-6, 2e-6, 5e-6, 1e-5, 2e-5, 5e-5, 1e-4):
        vi, ei, ri, hi, *_ = three.solve(initial, lam, refi)
        vf, ef, rf, hf, *_ = three.solve(final, lam, reff)
        refi, reff = vi, vf
        strength = three.components(vi, vf)[0]["strength"]
        gap = ei-ef
        assert gap > 0 and max(ri, rf, hi, hf) < 1e-10
        rows.append({
            "lambda":lam, "E10_minus_E8":gap, "B":strength,
            "dimensionless_E5_B_proxy":gap**5*strength,
            "B_over_lambda2":strength/lam**2,
            "proxy_over_expected_lambda_power":gap**5*strength/lam**exponent,
        })
    powers = [
        math.log(b["dimensionless_E5_B_proxy"]/a["dimensionless_E5_B_proxy"])
        / math.log(b["lambda"]/a["lambda"])
        for a, b in zip(rows, rows[1:])
    ]
    assert abs(powers[0]-exponent) < 0.01
    assert abs(rows[0]["B_over_lambda2"]/bcoef-1) < 1e-3
    assert abs(rows[0]["proxy_over_expected_lambda_power"]/rcoef-1) < 1e-3
    return {
        "eta_J2_baseline":eta, "baseline_energy_gap":de0,
        "baseline_B_roundoff":a0["strength"],
        "first_order_gap_slope":deslope, "first_order_B_coefficient":bcoef,
        "leading_proxy_exponent":exponent, "leading_proxy_coefficient":rcoef,
        "rows":rows, "neighboring_log_slopes":powers,
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output",type=Path,required=True)
    a = p.parse_args()
    results = [analyze(eta) for eta in (0., 0.05)]
    result = {
        "model":"j=11/2,n=6,H=-P0+eta*P2+lambda*V3(J=27/2)",
        "units":"dimensionless; single-particle reduced E2 element 1",
        "proxy":"positive (E10-E8)^5 * B(10->8), omits physical radiation constant",
        "cases":results,
        "interpretation":"B starts as lambda^2 in both tested cases. The rate proxy starts as lambda^7 only when the same perturbation also opens a zero baseline gap; a finite symmetry-preserving baseline gap instead gives lambda^2.",
        "limitations":"Illustrative eta is not fitted to a nucleus; no total competing widths, internal conversion or physical lifetime.",
        "scripts":[{"path":str(path),"sha256":sha(path)} for path in (
            Path(__file__), Path(three.__file__), Path(old.__file__))],
    }
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,indent=2,allow_nan=False)+"\n")
    print(json.dumps([{
        "eta":r["eta_J2_baseline"],"baseline_gap":r["baseline_energy_gap"],
        "leading_B_coefficient":r["first_order_B_coefficient"],
        "proxy_exponent":r["leading_proxy_exponent"],
        "first_measured_log_slope":r["neighboring_log_slopes"][0],
    } for r in results],indent=2))


if __name__ == "__main__":
    main()
