#!/usr/bin/env python3
"""Bounded replay of JO95 Table2, pure-E2 point P and calibration budgets."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day16_pdco_ambiguity_preview import cg, small_d
from day16_st99_table_replay import quoted


def polarization(a2: float, a4: float) -> float:
    return (1.5*a2+.625*a4)/(1-.5*a2+.375*a4)


def jacobian(a2: float, a4: float) -> np.ndarray:
    denominator = 1-.5*a2+.375*a4
    return np.array([1.5+.875*a4,.625-.875*a2])/denominator**2


def q_point(energy_keV: float) -> float:
    x = energy_keV/511.
    # Klein-Nishina at scatter angle90°, then an independently simplified form.
    value = 1/(1+x+1/(1+x)-1)
    assert abs(value-(1+x)/(1+x+x*x))<3e-16
    return value


def sigma_enclosure(gradient: np.ndarray, sigmas: np.ndarray) -> tuple[float,float]:
    contributions = abs(gradient*sigmas)
    assert len(contributions)==2
    return abs(contributions[0]-contributions[1]),float(contributions.sum())


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    cfg=json.loads(args.input.read_text())
    root=Path(__file__).resolve().parents[2]
    assert hashlib.sha256((root/cfg["raw_file"]).read_bytes()).hexdigest()==cfg["raw_sha256"]
    h_coeff={rank:cg(2,-1,2,-1,rank,-2)/cg(2,-1,2,1,rank,0) for rank in (2,4)}
    numerator_coeff={rank:-h_coeff[rank]*small_d(rank,0,2,math.pi/2) for rank in (2,4)}
    assert abs(numerator_coeff[2]-1.5)<1e-14
    assert abs(numerator_coeff[4]-.625)<1e-14
    rows=[]
    max_derivative_error=0.
    for nucleus,energy,ji,jf,aa2,aa4,pp,aa,qq in cfg["rows"]:
        a2,s2=quoted(aa2);a4,s4=quoted(aa4)
        pol,sp=quoted(pp);asym,sa=quoted(aa);q,sq=quoted(qq)
        point=polarization(a2,a4)
        grad=jacobian(a2,a4)
        step=1e-6
        numeric=np.array([(polarization(a2+step,a4)-polarization(a2-step,a4))/(2*step),
                          (polarization(a2,a4+step)-polarization(a2,a4-step))/(2*step)])
        max_derivative_error=max(max_derivative_error,float(max(abs(grad-numeric))))
        independent=float(np.linalg.norm(grad*np.array([s2,s4])))
        low,high=sigma_enclosure(grad,np.array([s2,s4]))
        qgrad=np.array([1/pol,-asym/pol**2])
        qlow,qhigh=sigma_enclosure(qgrad,np.array([sa,sp]))
        rows.append({"nucleus":nucleus,"E_keV":float(energy),"Ji":ji,"Jf":jf,
                     "source_a2":a2,"source_a4":a4,"source_P":pol,"source_sigma_P":sp,
                     "pureE2_point_P":point,"dP_da2_da4":grad.tolist(),
                     "sigmaP_independent_coefficient_model":independent,
                     "nominal_sigmaP_any_pair_covariance_interval":[low,high],
                     "source_sigmaP_within_nominal_pair_interval":bool(low<=sp<=high),
                     "A_over_source_P":asym/pol,"source_Q":q,"source_sigma_Q":sq,
                     "sigmaQ_independent_A_P_model":float(np.linalg.norm(qgrad*np.array([sa,sp]))),
                     "nominal_sigmaQ_any_A_P_covariance_interval":[qlow,qhigh]})
    curves=[]
    for energy in cfg["cross_source_comparison"]["energies_keV"]:
        ideal=q_point(energy)
        jo95=ideal*.29
        st99=ideal*(.31+7e-5*energy)
        curves.append({"E_keV":energy,"Q_ideal":ideal,"JO95_central_if_Qprime_equals_KN90":jo95,
                       "ST99_printed_central_Q":st99,"ST99_over_JO95":st99/jo95,
                       "legacy_JO95_C_as_mean_control":ideal*(.29+.003*energy/1000)})
    assert max_derivative_error<1e-8
    out={"identity":cfg["identity"],"input_sha256":hashlib.sha256(args.input.read_bytes()).hexdigest(),
         "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         "raw_sha256_verified":cfg["raw_sha256"],"pureE2_D96_H_coefficients":h_coeff,
         "P90_numerator_coefficients":numerator_coeff,"max_analytic_vs_numeric_Jacobian_error":max_derivative_error,
         "rows":rows,"central_curves":curves,
         "C_mean_per_MeV":0.,"C_sigma_per_MeV":.003,"C_sigma_per_keV":.000003,
         "Qprime_identification_boundary":"JO95 describes KN pointscatterer/analyzers90deg but does not print an explicit Qprime algebraic formula. Equating it to ST99Eq6 KN90 form is the declared analytical identification in this comparison. With that identification, B=.29,C=0 gives .098337 at1368, unlike printedTable2Q=.121; no normalization/producer/fit-recipe closure is claimed.",
         "boundary":"Nominal local-Jacobian covariance enclosures are not confidence regions or actual uncertainty budgets. Source STAG/acceptance and nonlinear treatment not replayed. Central curves differ across calibration identities; no p-value or causal attribution."}
    args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(out,ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
