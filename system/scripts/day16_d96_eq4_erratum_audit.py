#!/usr/bin/env python3
"""Compare corrected D96 Eq.1/4 with photon amplitudes on fixed new paths.

Shared CG/Wigner primitives are reused. The tensor contraction and explicit
photon-channel traces are different algebraic routes, not independent data.
Only real amplitudes, integer spins, L<=2 and at most one polarimeter are used.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day16_pdco_ambiguity_preview import cg, nine_j, orientation, pure_operator, small_d


def d_element(rank: int, mp: int, m: int, theta: float) -> float:
    # Eq.1 also contains rank-zero terms; d^0_(mu,±2) is exactly zero.
    if abs(mp) > rank or abs(m) > rank:
        return 0.
    return small_d(rank,mp,m,theta)


@lru_cache(None)
def coefficient(ji: int, jf: int, parts: tuple, outgoing: int, incoming: int,
                rank: int, polarized: bool, corrected: bool = True) -> float:
    norm = sum(a*a for _, _, a in parts)
    total = 0.
    for kind, ell, a in parts:
        for kindp, ellp, ap in parts:
            # Eq.8's denominator cancels Eq.7's photon CG; do not divide 0/0.
            photon_cg = cg(ell, -1, ellp, -1 if polarized else 1,
                           rank, -2 if polarized else 0)
            if photon_cg == 0:
                continue
            pref = ((-1)**(ell-1) * math.sqrt(
                (2*ji+1)*(2*jf+1)*(2*ell+1)*(2*ellp+1)
                *(2*outgoing+1)*(2*incoming+1)))
            f = pref * photon_cg * nine_j(
                ji, ji, incoming, ell, ellp, rank, jf, jf, outgoing)
            magnetic = kindp == "M" if corrected else kind == "M"
            total += a*ap*f*(-1 if polarized and magnetic else 1)
    return total/norm


def tensor_terms(spins: tuple, first: tuple, second: tuple,
                 pop: np.ndarray, corrected: bool = True) -> list[tuple]:
    ji, jmid, jf = spins
    rho = np.diag(pop)
    result = []
    for incoming in range(0, 2*ji+1, 2):
        b = orientation(ji, rho, incoming)
        if abs(b) < 1e-14:
            continue
        for outgoing in range(0, 2*jmid+1, 2):
            g0 = coefficient(jmid, jf, second, 0, outgoing, outgoing, False)
            g2 = coefficient(jmid, jf, second, 0, outgoing, outgoing, True, corrected)
            for rank in range(abs(incoming-outgoing), min(incoming+outgoing, 4)+1):
                f0 = coefficient(ji, jmid, first, outgoing, incoming, rank, False)
                f2 = coefficient(ji, jmid, first, outgoing, incoming, rank, True, corrected)
                for mu in range(min(rank,outgoing)+1):
                    factor = b*cg(incoming,0,outgoing,mu,rank,mu)/(1+(mu==0))
                    if max(abs(factor*f0*g0), abs(factor*f2*g0), abs(factor*f0*g2)) > 1e-15:
                        result.append((rank,outgoing,mu,factor*f0*g0,
                                       factor*f2*g0,factor*f0*g2))
    return result


def source_density(terms: list[tuple], angles: list, mode: dict) -> float:
    t1,t2,phi = np.deg2rad(angles)
    psi1,psi2 = np.deg2rad([mode["psi1_deg"],mode["psi2_deg"]])
    q1,q2 = mode["q1"],mode["q2"]
    assert not (q1 and q2), "PPCO intentionally excluded"
    total = 0.
    for k,k1,mu,c0,c1,c2 in terms:
        d10,d20 = d_element(k,mu,0,t1),d_element(k1,mu,0,t2)
        v = c0*d10*d20*math.cos(mu*phi)
        if q1:
            v -= .5*c1*d20*(
                d_element(k,mu,2,t1)*math.cos(mu*phi+2*psi1)
                +(-1)**k*d_element(k,mu,-2,t1)*math.cos(mu*phi-2*psi1))
        if q2:
            v -= .5*c2*d10*(
                d_element(k1,mu,2,t2)*math.cos(mu*phi-2*psi2)
                +d_element(k1,mu,-2,t2)*math.cos(mu*phi+2*psi2))
        total += v
    return total*(2-q1)*(2-q2)/(32*math.pi**2)


def direct_operators(ji: int, jf: int, native: tuple, theta: float,
                     phi: float, psi: float | None) -> list[np.ndarray]:
    norm = math.sqrt(sum(a*a for _,_,a in native))
    helicities = {}
    for h in (-1,1):
        # Same operator mapping derived before this frozen benchmark, not fitted.
        helicities[h] = sum((-1)**ell*a/norm * pure_operator(
            ji,jf,ell,kind,theta,phi,h) for kind,ell,a in native)
    if psi is None:
        return list(helicities.values())
    return [(-np.exp(1j*psi)*helicities[1]
             +np.exp(-1j*psi)*helicities[-1])/math.sqrt(2)]


def direct_density(spins: tuple, first: tuple, second: tuple,
                   pop: np.ndarray, angles: list, mode: dict) -> float:
    ji,jmid,jf = spins
    t1,t2,phi = np.deg2rad(angles)
    # Eq.1's directed analyzer coordinate is opposite this fixed Jones probe's
    # exponent coordinate. In/perpendicular planes alone cannot reveal it.
    ps1 = -math.radians(mode["psi1_deg"]) if mode["q1"] else None
    ps2 = -math.radians(mode["psi2_deg"]) if mode["q2"] else None
    value = 0j
    for op1 in direct_operators(ji,jmid,first,t1,0.,ps1):
        for op2 in direct_operators(jmid,jf,second,t2,phi,ps2):
            amplitude = op2@op1
            value += np.sum(np.sum(abs(amplitude)**2,axis=0)*pop)
    assert abs(value.imag) < 1e-14 and value.real >= -1e-14
    return float(value.real)


def integrate_tensor(terms: list[tuple], nt: int, nphi: int) -> float:
    nodes,weights = np.polynomial.legendre.leggauss(nt)
    mode = {"q1":0,"q2":0,"psi1_deg":0,"psi2_deg":0}
    total = 0.
    for x,w in zip(nodes,weights):
        for y,v in zip(nodes,weights):
            for phi in np.arange(nphi)*360/nphi:
                total += w*v*source_density(terms,[np.rad2deg(np.arccos(x)),
                                                 np.rad2deg(np.arccos(y)),phi],mode)
    return total*2*math.pi*2*math.pi/nphi


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    args = p.parse_args()
    cfg = json.loads(args.input.read_text())
    cases = []
    normalization = []
    complement_errors = []
    symmetry_errors = []
    for model in cfg["models"]:
        spins = tuple(model["spins"])
        assert len(spins) == 3 and all(isinstance(j,int) and j>=0 for j in spins)
        pop = np.array(model["population_weights"],dtype=float)
        assert len(pop) == 2*spins[0]+1 and np.all(pop>=0)
        pop /= pop.sum()
        second = ((model["gate_kind"],model["gate_L"],1.),)
        for case in cfg["first_transition_cases"]:
            first = tuple(tuple(x) for x in case["components"])
            for native,ji,jf in [(first,spins[0],spins[1]),(second,spins[1],spins[2])]:
                assert sum(a*a for _,_,a in native)>0
                assert all(kind in ("E","M") and ell in (1,2)
                           and abs(ji-jf)<=ell<=ji+jf for kind,ell,a in native)
                assert len({(-1)**(ell+(kind=="M")) for kind,ell,a in native}) == 1
            correct = tensor_terms(spins,first,second,pop,True)
            original = tensor_terms(spins,first,second,pop,False)
            rows = []
            for angles in cfg["geometries"]:
                unpolarized = {"q1":0,"q2":0,"psi1_deg":0,"psi2_deg":0}
                w00 = source_density(correct,angles,unpolarized)
                for which in (1,2):
                    a = {**unpolarized,"q"+str(which):1}
                    b = {**a,"psi"+str(which)+"_deg":90}
                    complement_errors.append(abs(source_density(correct,angles,a)
                                                 +source_density(correct,angles,b)-w00))
                for mode in cfg["modes"]:
                    source = source_density(correct,angles,mode)
                    printed = source_density(original,angles,mode)
                    direct = direct_density(spins,first,second,pop,angles,mode)
                    reflected = [180-angles[0],angles[1],angles[2]+180]
                    reflected_mode = {**mode,"psi1_deg":-mode["psi1_deg"]}
                    symmetry_errors.append(abs(source-source_density(
                        correct,reflected,reflected_mode)))
                    rows.append({"angles_deg":angles,"mode":mode,
                                 "corrected_Eq1_Eq4":source,"original_T_phase":printed,
                                 "direct_photon_trace":direct,
                                 "corrected_absolute_error":abs(source-direct),
                                 "original_absolute_error":abs(printed-direct)})
            cases.append({"spins":spins,"gate":second,"first_case":case["label"],
                          "chosen_population":pop.tolist(),"rows":rows})
            if case["label"] == "mixed_d+.3":
                normalization.append({"spins":spins,"nt6_phi10":integrate_tensor(correct,6,10),
                                      "nt8_phi14":integrate_tensor(correct,8,14)})
    max_error = max(row["corrected_absolute_error"] for case in cases for row in case["rows"])
    original_mixed = max(row["original_absolute_error"] for case in cases
                         if case["first_case"].startswith("mixed") for row in case["rows"])
    original_pure = max(row["original_absolute_error"] for case in cases
                        if not case["first_case"].startswith("mixed") for row in case["rows"])
    out = {"identity":cfg["identity"],"input_sha256":hashlib.sha256(args.input.read_bytes()).hexdigest(),
           "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "cases":cases,"normalization":normalization,
           "max_corrected_absolute_error":max_error,
           "max_original_phase_error_mixed":original_mixed,"max_original_phase_error_pure":original_pure,
           "max_complement_sum_error":max(complement_errors),
           "max_reflection_symmetry_error":max(symmetry_errors),
           "coordinate_map":"Native amplitudes -> probe: (-1)^L. Directed analyzer psi_probe=-psi_Eq1; source input angles are unchanged. This implementation map does not certify actual detector axes or global experimental handedness.",
           "first_numeric_failure_preserved":"day16-d96-eq4-audit-first.json with first-code snapshot; all grids source-informed, not blind or an independent holdout.",
           "scope":"Point-response benchmark; no actual source code or array/event covariance. Fixed real/integer/L<=2 inputs, DCO or one polarimeter only."}
    args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k not in ["cases"]},ensure_ascii=False,indent=2))
    assert max_error < 2e-12
    assert original_pure < 2e-12 and original_mixed > 1e-6
    assert max(complement_errors) < 2e-12 and max(symmetry_errors) < 2e-12
    assert all(abs(x[k]-1)<2e-12 for x in normalization for k in ["nt6_phi10","nt8_phi14"])


if __name__ == "__main__":
    main()
