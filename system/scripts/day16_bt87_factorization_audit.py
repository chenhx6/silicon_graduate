#!/usr/bin/env python3
"""Compare BT87 factorized correlations with the declared exact point model.

Ordinary F and initial B may be finite-spin exact while the joint factorization
remains approximate. No fit of the KF89 values or reconstruction of DCOMAP is
performed. The primitives are shared with the documented Day16 quantum audit.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day16_kf89_w178_gate_audit import density, population
from day16_pdco_ambiguity_preview import cg, orientation, small_d, source_f


def pk(k: int, x: np.ndarray | float) -> np.ndarray:
    return np.polynomial.legendre.legval(x, [0.0] * k + [1.0])


def infinite_f(delta_j: int, ell: int, k: int) -> float:
    """BT87 printed515 Eq7 for one pure multipole; 3j expressed via CG."""
    if k > 2 * ell:
        return 0.0
    return ((-1.0)**(delta_j - 1 - k - 2 * ell)
            * (2 * ell + 1) / math.sqrt(2 * k + 1)
            * cg(ell, 1, ell, -1, k, 0)
            * cg(ell, delta_j, ell, -delta_j, k, 0))


def ordinary(ji: int, jf: int, ell: int, finite: bool) -> dict:
    return {k: source_f(k, 0, k, ell, ell, ji, jf) if finite
            else infinite_f(ji - jf, ell, k) for k in (0, 2, 4)}


def moments(ji: int, pop: np.ndarray, finite: bool, width: float | None) -> dict:
    if finite:
        rho = np.diag(pop)
        return {k: orientation(ji, rho, k) for k in range(0, 9, 2)}
    if width is None:
        # BT87 Eq16, complete perpendicular alignment in the infinite-spin limit.
        return {k: float(math.sqrt(2*k+1) * pk(k, 0.0)) for k in range(0, 9, 2)}
    # Limit of the frozen discrete Gaussian when sigma/J stays fixed.
    # x=M/J=cos(theta_spin); integral is independently converged below.
    x, w = np.polynomial.legendre.leggauss(80)
    weight = w * np.exp(-x*x/(2*width*width)); weight /= weight.sum()
    return {k: float(math.sqrt(2*k+1) * (weight @ pk(k, x))) for k in range(0, 9, 2)}


@lru_cache(None)
def geometry(angles: tuple, nt: int, nphi: int) -> tuple:
    x, w = np.polynomial.legendre.leggauss(nt)
    phi = np.arange(nphi) * (2*math.pi/nphi)
    t1, t2, rel = np.deg2rad(angles)
    nspin = np.stack([np.sqrt(1-x*x)[:,None]*np.cos(phi)[None,:],
                      np.sqrt(1-x*x)[:,None]*np.sin(phi)[None,:],
                      np.broadcast_to(x[:,None], (nt,nphi))], axis=-1)
    n1=np.array([math.sin(t1),0.,math.cos(t1)])
    n2=np.array([math.sin(t2)*math.cos(rel),math.sin(t2)*math.sin(rel),math.cos(t2)])
    return x,w,nspin@n1,nspin@n2


def factorized(spins: tuple, ranks: tuple, pop: np.ndarray, angles: tuple,
               finite: bool, width: float | None, nt: int, nphi: int) -> float:
    a1=ordinary(spins[0],spins[1],ranks[0],finite)
    a2=ordinary(spins[1],spins[2],ranks[1],finite)
    bs=moments(spins[0],pop,finite,width)
    x,w,c1,c2=geometry(angles,nt,nphi)
    initial=sum(math.sqrt(2*k+1)*b*pk(k,x) for k,b in bs.items())
    first=sum(math.sqrt(2*k+1)*a*pk(k,c1) for k,a in a1.items())
    second=sum(math.sqrt(2*k+1)*a*pk(k,c2) for k,a in a2.items())
    # This finite moment polynomial is not asserted to be a positive classical
    # spin-axis probability density. Eq10's finite-spin substitution is formal.
    return float(np.sum(w[:,None]*initial[:,None]*first*second)/(2*nphi))


def exact(spins: tuple, ranks: tuple, pop: np.ndarray, angles: tuple) -> float:
    return 16*math.pi**2*density(spins,pop,(("E",ranks[0],1.),),
                                 (("E",ranks[1],1.),),list(angles))


def algebraic_factorization(spins: tuple, ranks: tuple, pop: np.ndarray,
                            angles: tuple, finite: bool,
                            width: float | None) -> float:
    """Independent BT87 Eq10 spherical-harmonic contraction, axial initial rho."""
    a1=ordinary(spins[0],spins[1],ranks[0],finite)
    a2=ordinary(spins[1],spins[2],ranks[1],finite)
    bs=moments(spins[0],pop,finite,width)
    t1,t2,phi=np.deg2rad(angles); total=0j
    def y(k,q,t,p):
        return math.sqrt((2*k+1)/(4*math.pi))*np.exp(1j*q*p)*small_d(k,q,0,t)
    for k1,f1 in a1.items():
        for k2,f2 in a2.items():
            for k,b in bs.items():
                c0=cg(k1,0,k2,0,k,0)
                if abs(c0)<1e-15: continue
                for q in range(-min(k1,k2),min(k1,k2)+1):
                    total += b*f1*f2*4*math.pi/math.sqrt(2*k+1)*c0*cg(k1,q,k2,-q,k,0)*y(k1,q,t1,0.)*y(k2,-q,t2,phi)
    assert abs(total.imag)<1e-12
    return float(total.real)


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args(); cfg=json.loads(args.input.read_text())
    assert cfg["identity"]=="DAY16-BT87-KF89-FACTORISATION-01"
    nt,nphi=cfg["spin_axis_quadrature"]; nt2,nphi2=cfg["quadrature_repeat"]
    tab=[(0,1,-.447,0.),(1,1,.224,0.),(0,2,.319,-.571),
         (1,2,.160,.381),(2,2,-.319,-.095)]
    table_control=[]
    for dj,ell,a2,a4 in tab:
        values=[infinite_f(dj,ell,k) for k in (0,2,4)]
        assert abs(values[0]-1)<1e-12
        assert abs(values[1]-a2)<=.0005 and abs(values[2]-a4)<=.0005
        table_control.append({"delta_J":dj,"L":ell,"A0_A2_A4":values,"printed_A2_A4":[a2,a4]})
    table=[([10,8,6],2,2,1.),([10,8,7],2,1,.56),([10,8,7],2,2,.66),
           ([10,8,8],2,1,1.07),([10,8,8],2,2,.57),([9,8,6],1,2,1.81),
           ([9,8,7],1,2,.92),([9,8,7],1,1,1.),([9,8,8],1,1,1.79),([9,8,8],1,2,1.12)]
    ab=tuple(cfg["KF89_geometry"]); ba=(ab[1],ab[0],ab[2]); results=[]; convergence=[]
    width=cfg["KF89_std_width_over_initial_J"]; algebraic_errors=[]
    for spins,l1,l2,printed in table:
        spins=tuple(spins); ranks=(l1,l2); pop=population(spins[0],width*spins[0])
        row={"spins":spins,"ranks":ranks,"printed":printed}
        row["exact"]=exact(spins,ranks,pop,ab)/exact(spins,ranks,pop,ba)
        for finite,label in [(False,"infinite"),(True,"finite_improvement")]:
            vals=[factorized(spins,ranks,pop,ang,finite,width,nt,nphi) for ang in (ab,ba)]
            vals2=[factorized(spins,ranks,pop,ang,finite,width,nt2,nphi2) for ang in (ab,ba)]
            algebraic=[algebraic_factorization(spins,ranks,pop,ang,finite,width) for ang in (ab,ba)]
            convergence.extend(abs(np.array(vals)-vals2).tolist())
            algebraic_errors.extend(abs(np.array(vals)-algebraic).tolist())
            assert min(vals)>0
            row[label]=vals[0]/vals[1]
        row["within_printed_half_unit"]={label:abs(row[label]-printed)<=.005+1e-12
                                          for label in ("exact","infinite","finite_improvement")}
        results.append(row)
    fig2=[]
    control=cfg["source_Fig2_control"]
    for ji in control["initial_spin_choices"]:
        pop=np.zeros(2*ji+1);pop[ji]=1.
        for dj,ell in control["first_pure_transition_choices"]:
            spins=(ji,ji-dj,ji-dj-2);ranks=(ell,2);points=[]
            for angle in control["theta1_degrees"]:
                ang=(float(angle),float(control["theta2_degrees"]),float(control["relative_phi_degrees"]))
                e=exact(spins,ranks,pop,ang)
                f=factorized(spins,ranks,pop,ang,True,None,nt,nphi)
                inf=factorized(spins,ranks,pop,ang,False,None,nt,nphi)
                assert e>0
                points.append({"theta1_deg":angle,"exact_W":e,"finite_W":f,"infinite_W":inf,
                               "finite_absolute_error":f-e,"infinite_absolute_error":inf-e,
                               "finite_fractional_error":(f-e)/e,"infinite_fractional_error":(inf-e)/e})
            fig2.append({"initial_J":ji,"first_delta_J":dj,"first_L":ell,"points":points,
                         "max_abs_error_finite":max(abs(x['finite_absolute_error']) for x in points),
                         "max_abs_error_infinite":max(abs(x['infinite_absolute_error']) for x in points),
                         "max_abs_fractional_error_finite":max(abs(x['finite_fractional_error']) for x in points),
                         "max_abs_fractional_error_infinite":max(abs(x['infinite_fractional_error']) for x in points)})
    assert max(convergence)<1e-11
    assert max(algebraic_errors)<1e-11
    j=20; m0=np.zeros(2*j+1);m0[j]=1.
    b2=orientation(j,np.diag(m0),2)
    pseudo_moment=b2/math.sqrt(5)
    analytic=-math.sqrt(j*(j+1)/((2*j-1)*(2*j+3)))
    assert abs(pseudo_moment-analytic)<1e-13 and pseudo_moment<-.5
    result={"identity":cfg["identity"],"input_sha256":hashlib.sha256(args.input.read_bytes()).hexdigest(),
            "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "source_Table1_limit_control":table_control,"KF89_pure_table_comparison":results,
            "BT87_Fig2_conditions_point_control":fig2,"quadrature_max_difference":max(convergence),
            "Eq10_algebra_vs_Eq12_axis_integral_max_difference":max(algebraic_errors),
            "finite_B_classical_axis_boundary":{"J":j,"M":0,"B2":b2,
                 "formal_P2_moment_B2_over_sqrt5":pseudo_moment,
                 "independent_quadrupole_formula":analytic,
                 "positive_classical_axis_P2_lower_bound":-.5,
                 "interpretation":"Exact finite-spin tensor cannot simply be read as the moments of a positive classical unit-axis probability; the finite-spin Eq10 substitution remains formal."},
            "rounding_matches":{label:sum(r['within_printed_half_unit'][label] for r in results)
                                for label in ('exact','infinite','finite_improvement')},
            "scientific_boundary":"All results use stated point/Gaussian or complete-alignment inputs; neither printed values nor producer provenance are refitted.",
            "all_internal_checks_passed":True}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    print(json.dumps({"output":str(args.output),"rounding_matches":result['rounding_matches'],
                      "quadrature_max_difference":max(convergence),"pure_table":results,
                      "Fig2_max_errors":[{k:v for k,v in r.items() if k!='points'} for r in fig2]},ensure_ascii=False))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
