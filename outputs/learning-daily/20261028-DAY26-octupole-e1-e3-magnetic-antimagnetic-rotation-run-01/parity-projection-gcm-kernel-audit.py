#!/usr/bin/env python3
"""Algebra/reproducibility audit. Illustrative states are not Gogny predictions."""
from pathlib import Path
import datetime
import hashlib
import json
import math
import subprocess

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).with_suffix('.json')


def energies(N, n, H, h):
    return (H+h)/(N+n), (H-h)/(N-n)


def quartic_old_inputs(q, barrier, mass):
    """Reproduce old heuristic, without endorsing parameters or approximation."""
    curvature = 8 * barrier / q**2
    omega = math.sqrt(curvature/mass)
    sigma2 = 1/(2*math.sqrt(mass*curvature))
    s = math.exp(-q*q/(2*sigma2))
    action_bottom = (4*q/3)*math.sqrt(2*mass*barrier)
    return dict(omega_MeV=omega, overlap=s, bottom_action_over_hbar=action_bottom,
                heuristic_projection_keV=1000*omega*s/(1-s*s),
                bottom_WKB_keV=1000*omega/math.pi*math.exp(-action_bottom),
                physical_status='unvalidated illustrative parameters; not microscopic kernels')


def main():
    states=[]
    max_sign_residual = 0.0
    max_shift_residual = 0.0
    for theta in [.03, .1, .4, math.pi/4, 1.0]:
        ce, co = math.cos(theta)**2, math.sin(theta)**2
        N, n, H, h = 1., ce-co, 1.2*co, -1.2*co
        ep, em = energies(N,n,H,h)
        delta = 2*(H*n-h*N)/(N*N-n*n)
        max_sign_residual=max(max_sign_residual,abs(em-ep-delta))
        shifted=energies(N,n,H+5.4*N,h+5.4*n)
        max_shift_residual=max(max_shift_residual,abs((shifted[1]-shifted[0])-delta))
        states.append(dict(theta_rad=theta,N=N,n=n,H_MeV=H,h_MeV=h,
                           Eplus_MeV=ep,Eminus_MeV=em,delta_formula_MeV=delta))
    coherent=[]
    for a in [1e-4, .001, .01, .1, .5, 1., 2.]:
        z=a*a
        # Stable analytic expression avoids cancellation in tiny odd norm.
        delta=2*z/math.sinh(2*z)
        coherent.append(dict(alpha=a,overlap=math.exp(-2*z),
                             odd_projection_norm=-math.expm1(-2*z)/2,
                             delta_over_hbar_omega=delta))
    bwu= (1/(4*math.pi))*(3/6)**2*(1.2*144**(1/3))**6 / 1e6
    e3=[]
    for scheme,m in [('1D-beta2',.450),('1D-beta3',.477),('2D',.460)]:
        e3.append(dict(scheme=scheme,M_eb_3_over_2=m,
                       Bdown_e2b3=m*m/7,Bup_e2b3=m*m,
                       Bdown_Wu=m*m/(7*bwu)))
    sources=[]
    for rel,pages,read in [
        ('raw/papers/gpt/day26-20261028/bernard-2016-144ba-sccm-arxiv1604.06706v1.pdf',6,[1,2,3,4]),
        ('raw/papers/day26-20261028/2010-robledo-octupole-ra-ba.pdf',14,[3,4,10,11,12])]:
        p=ROOT/rel
        data=p.read_bytes()
        info=subprocess.run(['pdfinfo',str(p)],capture_output=True,text=True,check=True).stdout
        actual_pages=int(next(x.split(':',1)[1] for x in info.splitlines() if x.startswith('Pages:')))
        sources.append(dict(path=rel,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),
                            signature=data[:5].decode(),expected_pages=pages,actual_pages=actual_pages,
                            targeted_pdf_pages_read=read))
    old={name:quartic_old_inputs(q,v,m) for name,q,v,m in [
        ('224Ra',2500.,1.45,1.8e-6),('144Ba',1500.,.42,2.5e-6),('146Ba',1300.,.28,2.7e-6)]}
    result=dict(
        status='bounded-self-audit; no new nuclear-structure simulation',
        generated_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        delta_definition='Eminus-Eplus',
        correct_formula='2*(H*n-h*N)/(N*N-n*n)',
        algebra_max_abs_residual_MeV=max_sign_residual,
        energy_shift_max_abs_residual_MeV=max_shift_residual,
        analytic_states=states,
        zero_overlap_counterexample={'N':1,'n':0,'H_MeV':.6,'h_MeV':-.6,'delta_MeV':1.2},
        zero_odd_norm_at_reflection_symmetric_point='Eminus undefined at exact q=0; finite tangent-state limit may exist',
        coherent_state_single_well_examples=coherent,
        E3={'Weisskopf_one_unit_e2b3':bwu,'table':e3,'source':'Bernard2016 PDF p.4 Table I'},
        GCM_ground_energy_gains_MeV={'2D_vs_1D_beta2':-1185.931-(-1187.547),'2D_vs_1D_beta3':-1186.709-(-1187.547)},
        old_076_input_recalculation=old,
        old_076_text_claims_keV={'224Ra':19.6,'144Ba':832.5,'146Ba':815.2},
        old_076_claims_reproduced=False,
        method_boundary={'Bernard2016':'explicit J,pi,N,Z projection plus 1D/2D HWG',
                         'Robledo2010':'1D GCM+GOA collective Schrodinger equation; ATDHF+ZPE mixture; rotational approximation for E3'},
        missing_for_nuclear_quantitative_projection=['HFB norm kernel','Hamiltonian kernel','consistent EDF kernel prescription','fixed-J comparison'],
        sources=sources)
    OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'output':str(OUT.relative_to(ROOT)),
                      'sign_max_residual':max_sign_residual,'shift_max_residual':max_shift_residual,
                      '2D_Bdown_Wu':e3[-1]['Bdown_Wu'],
                      'old_076_recalculation':old},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
