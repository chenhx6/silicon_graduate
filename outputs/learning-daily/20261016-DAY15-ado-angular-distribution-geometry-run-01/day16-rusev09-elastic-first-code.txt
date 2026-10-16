#!/usr/bin/env python3
"""Point-amplitude NRF branch audit with frozen RU09 summary inputs."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day16_se21_m3_reference import photon
from day16_st99_table_replay import quoted


def emit(ti: int, tf: int, kind: str, ell: int, theta: float,
         phi: float, helicity: int) -> np.ndarray:
    matrix=photon(ti,tf,kind,ell,theta,helicity).astype(complex)
    mf=np.arange(-tf,tf+1,2)/2
    mi=np.arange(-ti,ti+1,2)/2
    return matrix*np.exp(1j*(mi[None,:]-mf[:,None])*phi)


def components(ground: int, excited: int, theta: float, phi: float,
               helicity: int) -> tuple:
    # Source KS/native coefficient -> fixed RB photon basis; no fit to RU09.
    return tuple((-1)**ell*emit(excited,ground,kind,ell,theta,phi,helicity)
                 for kind,ell in [("M",1),("E",2)])


def amplitude_terms(ground: int, excited: int, theta: float,
                    phi: float, helicity: int) -> list[np.ndarray]:
    inp={h:components(ground,excited,0.,0.,h) for h in (-1,1)}
    incoming=tuple((-inp[1][k]+inp[-1][k])/math.sqrt(2) for k in (0,1))
    outgoing=components(ground,excited,theta,phi,helicity)
    return [outgoing[0]@incoming[0].conj().T,
            outgoing[1]@incoming[0].conj().T+outgoing[0]@incoming[1].conj().T,
            outgoing[1]@incoming[1].conj().T]


def coefficients(ground: int, excited: int, theta: float, phi: float) -> np.ndarray:
    values=np.zeros(5)
    for h in (-1,1):
        terms=amplitude_terms(ground,excited,theta,phi,h)
        for i,a in enumerate(terms):
            for j,b in enumerate(terms):
                values[i+j]+=float(np.trace(a@b.conj().T).real)/(ground+1)
    return values


def direct(ground: int, excited: int, theta: float, phi: float, delta: float) -> float:
    result=0.
    for h in (-1,1):
        a=amplitude_terms(ground,excited,theta,phi,h)
        matrix=(a[0]+delta*a[1]+delta**2*a[2])/(1+delta*delta)
        result+=float(np.trace(matrix@matrix.conj().T).real)/(ground+1)
    return result


def asymmetry(h: np.ndarray, v: np.ndarray, delta: float, c: float) -> float:
    a=np.polynomial.polynomial.polyval(delta,h)
    b=np.polynomial.polynomial.polyval(delta,v)
    assert a+b>0
    return c*(a-b)/(a+b)


def roots(h: np.ndarray, v: np.ndarray, c: float, observed: float) -> dict:
    polynomial=c*(h-v)-observed*(h+v)
    polynomial/=max(abs(polynomial))
    result=[];complex_roots=[]
    for value in np.polynomial.polynomial.polyroots(polynomial):
        if abs(value.imag)<1e-8:
            d=float(value.real)
            assert abs(asymmetry(h,v,d,c)-observed)<5e-11
            result.append({"delta":d,"arctan_delta_deg":math.degrees(math.atan(d)),
                           "E2_radiative_fraction":d*d/(1+d*d)})
        else:complex_roots.append([float(value.real),float(value.imag)])
    return {"observed_asymmetry":observed,"all_real_roots":result,
            "other_complex_roots":complex_roots,"polynomial_coefficients":polynomial.tolist()}


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args();cfg=json.loads(args.input.read_text())
    root=Path(__file__).resolve().parents[2]
    assert hashlib.sha256((root/cfg["raw_file"]).read_bytes()).hexdigest()==cfg["raw_sha256"]
    g=cfg["source_inputs"]["ground_twice_spin"];rows=[];errors=[]
    for row in cfg["elastic_rows"]:
        j=row["excited_twice_spin"]
        h=coefficients(g,j,math.pi/2,0.);v=coefficients(g,j,math.pi/2,math.pi/2)
        a,sa=quoted(row["asymmetry"])
        for delta in (-1.3,-.158,0.,.158,1.3):
            for phi,pol in [(0.,h),(math.pi/2,v)]:
                direct_value=direct(g,j,math.pi/2,phi,delta)
                poly_value=np.polynomial.polynomial.polyval(delta,pol)/(1+delta*delta)**2
                errors.append(abs(direct_value-poly_value));assert direct_value>=0
        inversion=[roots(h,v,row["C"],value) for value in [a-sa,a,a+sa]]
        predicted=asymmetry(h,v,float(row["reported_delta"]),row["C"])
        rows.append({"E_keV":row["E_keV"],"excited_twice_spin":j,
                     "H_coefficients":h.tolist(),"V_coefficients":v.tolist(),
                     "source_C":row["C"],"inversions":inversion,
                     "reported_delta":float(row["reported_delta"]),
                     "predicted_at_reported_delta":predicted,
                     "observed_central":a,"central_residual":predicted-a})
    h=coefficients(g,1,math.pi/2,0.);v=coefficients(g,1,math.pi/2,math.pi/2)
    iso=max(abs(asymmetry(h,v,d,1.)) for d in (-2.,-.1,0.,.1,2.))
    out={"identity":cfg["identity"],"input_sha256":hashlib.sha256(args.input.read_bytes()).hexdigest(),
         "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         "rows":rows,"max_polynomial_direct_error":max(errors),"isotropic_excited_halfspin_max_asymmetry":iso,
         "scope":"Conditional source-informed real-amplitude/integer-rank/halfspin NRF model. No original event/GEANT code, exact beamP/theoryCov or new spin assignment. All real roots retained, larger roots not discarded by a plausibility prior."}
    args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"rows":[{"E":x["E_keV"],"central":x["inversions"][1],
                              "predicted_at_reported_delta":x["predicted_at_reported_delta"],
                              "central_residual":x["central_residual"]} for x in rows],
                      "polynomial_direct_error":max(errors),"isotropic_control":iso},ensure_ascii=False,indent=2))
    assert max(errors)<2e-14 and iso<2e-13


if __name__=="__main__":
    main()
