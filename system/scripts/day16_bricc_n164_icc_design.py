#!/usr/bin/env python3
"""Fixed-point ICC references and a chosen conditional-count design, not data."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

from scipy.stats import binom


def probability(alpha: float, kappa: float) -> float:
    return kappa*alpha/(1+kappa*alpha)


def divergence(p: float, q: float) -> float:
    return p*math.log(p/q)+(1-p)*math.log((1-p)/(1-q))


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args();cfg=json.loads(args.input.read_text())
    snap=Path(cfg["coefficient_snapshot"])
    assert hashlib.sha256(snap.read_bytes()).hexdigest()==cfg["coefficient_sha256"]
    models={x["multipolarity"]:x for x in json.loads(snap.read_text())["model_inputs"]}
    delta=math.tan(math.radians(cfg["source_hypothesis"]["arctan_delta_degrees"]))
    t=delta*delta;wM=1/(1+t);wE=t/(1+t)
    refs={}
    for shell in ["K","L-tot","Tot"]:
        m=models["M1"]["coefficients"][shell];e=models["E2"]["coefficients"][shell]
        base=wM*m["value"]+wE*e["value"]
        sigma=[]
        for rho in cfg["illustrative_theory_covariance_sensitivity"]["rho_between_M1_E2_chosen"]:
            variance=(wM*m["quoted_sigma"])**2+(wE*e["quoted_sigma"])**2+2*rho*wM*wE*m["quoted_sigma"]*e["quoted_sigma"]
            sigma.append({"chosen_rho":rho,"local_sigma_if_quoted_errors_are_covariance_scales":math.sqrt(max(variance,0))})
        assert min(m["value"],e["value"])<=base<=max(m["value"],e["value"])
        refs[shell]={"pureE2":e["value"],"pureM1":m["value"],"fixed_mixed_point":base,
                     "mixed_over_E2":base/e["value"],"illustrative_sigma_mixed":sigma,
                     "coverage":"N6/N7 missing in programTot/N; exactK output retained"}
    design=cfg["conditional_count_design"];kappa=design["electron_over_gamma_efficiency_ratio_chosen"]
    a0=refs["K"]["pureE2"];a1=refs["K"]["fixed_mixed_point"]
    p0,p1=probability(a0,kappa),probability(a1,kappa)
    expected=[]
    for label,truth,other in [("pureE2",p0,p1),("fixed_M1_E2",p1,p0)]:
        kl=divergence(truth,other);n=math.ceil(design["expected_twice_log_likelihood_gap_target_chosen"]/(2*kl))
        # Conditional likelihood uses no unknown common photon-yield parameter.
        slope=math.log(truth/other)-math.log((1-truth)/(1-other))
        intercept=n*math.log((1-truth)/(1-other))
        boundary=-intercept/slope
        power=(binom.sf(math.floor(boundary),n,truth) if slope>0
               else binom.cdf(math.ceil(boundary)-1,n,truth))
        expected.append({"truth_point":label,"per_detected_event_KL":kl,
                         "chosen_total_detected_n":n,"expected_electron_count":n*truth,
                         "expected_gamma_count":n*(1-truth),"expected_twice_logLR":2*n*kl,
                         "probability_LR_prefers_true_fixed_point_known_model":float(power),
                         "probability_description":"Simple LR>1 at two fixed exact points only, not power at a specified type-I error or a sigma level"})
    calibration_alias=kappa*a0/a1
    assert abs(probability(a0,kappa)-probability(a1,calibration_alias))<1e-16
    equal_frac=(a1-a0)/(a1+a0)
    assert 0<equal_frac<1
    # The two symmetric fractional efficiency-nuisance intervals first touch here.
    assert abs((1+equal_frac)*a0-(1-equal_frac)*a1)<1e-16
    out={"identity":cfg["identity"],"input_sha256":hashlib.sha256(args.input.read_bytes()).hexdigest(),
         "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         "coefficient_snapshot_sha256":cfg["coefficient_sha256"],
         "delta_source":delta,"radiative_weights":{"M1":wM,"E2":wE},"references":refs,
         "source_K_electron_kinetic_reference_keV":cfg["energy_keV"]-cfg["K_binding_reference_keV"],
         "count_model":{"chosen_kappa":kappa,"pureE2_p_electron":p0,"fixed_mixed_p_electron":p1,
                        "directed_expected_designs":expected,
                        "free_kappa_alias":{"pureE2_kappa":kappa,"mixed_kappa_with_identical_conditional_distribution":calibration_alias},
                        "symmetric_fractional_kappa_interval_touching_value":equal_frac},
         "E0_lower_bound_fixed_delta":a1,
         "boundary":"Known-response/zero-background fixed-point design only. No new actual event counts, significance, confidence region, mass correction, completeTotal, fixed E0 value or author fit. Unmodelled response/efficiency can absorb the ratio; E0/radiative families require additional matched observables."}
    args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(out,ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
