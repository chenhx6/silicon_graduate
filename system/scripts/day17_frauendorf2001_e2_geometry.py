#!/usr/bin/env python3
"""Pinned source normalization and declared axial projection controls, not data."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
import numpy as np
import sympy as s
from sympy.physics.wigner import clebsch_gordan

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    cp=RUN/'frauendorf2001-e2-exercise-contract.json';c=json.loads(cp.read_text())
    assert sha(ROOT/c['pdf'])==c['pdf_sha256']
    prefix=json.loads((RUN/'frauendorf2001-human-prefix-snapshot.json').read_text())
    page=ROOT/prefix['path'];raw=page.read_bytes()
    assert hashlib.sha256(raw[:prefix['bytes']]).hexdigest()==prefix['sha256']
    rows=[]
    for deg in c['declared_theta_degrees']:
        theta=math.radians(deg);q=c['normalized_intrinsic_q']
        ry=np.array([[math.cos(theta),0,math.sin(theta)],[0,1,0],[-math.sin(theta),0,math.cos(theta)]])
        intrinsic=np.diag([-q/3,-q/3,2*q/3]);u=ry@intrinsic@ry.T
        q20=1.5*u[2,2]
        q22=math.sqrt(3/8)*(u[0,0]-u[1,1]+2j*u[0,1])
        q21=-math.sqrt(3/2)*(u[0,2]+1j*u[1,2])
        assert abs(q22-math.sqrt(3/8)*q*math.sin(theta)**2)<1e-14
        assert abs(q21+math.sqrt(3/2)*q*math.sin(theta)*math.cos(theta))<1e-14
        assert abs(q20-q*(3*math.cos(theta)**2-1)/2)<1e-14
        # Tensor norm includes both positive and negative m components.
        tensor_norm=q20*q20+2*abs(q21)**2+2*abs(q22)**2
        assert abs(tensor_norm-q*q)<1e-14
        b2=5/(4*math.pi)*abs(q22)**2
        q0=2*q
        assert abs(b2-15/(128*math.pi)*q0*q0*math.sin(theta)**4)<1e-14
        rows.append({'theta_degrees':deg,'normalized_intrinsic_q':q,'conventional_Q0':q0,
                     'Q20_lab':q20,'Q21_lab_in_declared_phase':q21.real,'Q22_lab_in_declared_phase':q22.real,
                     'tensor_norm':tensor_norm,'B_E2_DeltaI2_normalized':b2,
                     'B_E2_DeltaI1_normalized':5/(4*math.pi)*abs(q21)**2,
                     'boundary':'declared axial charge tensor, not measured nucleus, PAC/TAC solution or experimental shape'})
        if abs(math.sin(theta))>1e-12:
            measured_ratio=rows[-1]['B_E2_DeltaI1_normalized']/b2
            assert abs(measured_ratio-4*(math.cos(theta)/math.sin(theta))**2)<1e-12
    target=rows[-1]['Q22_lab_in_declared_phase']
    witnesses=[]
    for deg in c['declared_theta_degrees']:
        q=target/(math.sqrt(3/8)*math.sin(math.radians(deg))**2)
        witnesses.append({'theta_degrees':deg,'q_for_same_Q22':q,'Q22':target,
                          'B_E2_DeltaI2_normalized':5/(4*math.pi)*target*target})
    finite=[]
    for Istr,Kstr in c['finite_spin_cases']:
        I=s.Rational(Istr);K=s.Rational(Kstr)
        exact=s.simplify(clebsch_gordan(I,2,I-2,K,0,K)**2)
        J=I+s.Rational(1,2)
        high=s.Rational(3,8)*(1-(K/J)**2)**2
        gs=(2*I-3)/(2*I+1)
        finite.append({'I':str(I),'K':str(K),'J_bridge_declared':str(J),
                       'exact_strong_coupling_G':str(exact),'exact_G_float':float(exact),
                       'high_spin_G_with_declared_J':float(high),
                       'stretched_axis_candidate_G':float(gs),
                       'Qt_candidate_over_Q0_if_exact_axial_B_assumed':math.sqrt(float(exact/gs)),
                       'boundary':'exact rotor CG versus declared high-spin bridge and separate candidate scalar convention; no MU08 geometry identification'})
    out={'at':datetime.now(timezone.utc).isoformat(),'script_sha256':sha(Path(__file__)),
         'contract_sha256':sha(cp),'sympy_version':s.__version__,
         'operator_normalization':'Declared charge counterpart of the Eq10 spherical normalization, consistent with Eq34/35; q_ch=<Q20 prime>=Q0 conventional/2, not potential q_mu',
         'axial_forward_formula':'B(E2,I->I-2)=15/(128pi)*Q0^2*sin(theta)^4 within source semiclassical limit',
         'rotation_controls':rows,'same_B_different_intrinsic_moment_witnesses':witnesses,
         'axial_charge_E2_branch_ratio':'B(E2,DeltaI1)/B(E2,DeltaI2)=4*cot(theta)^2, denominator nonzero',
         'magnetic_transverse_normalization':'B(M1)=3/(8pi)*mu_perp^2 in the declared real-vector convention',
         'same_photon_delta_magnitude_relation':{'squared':'delta^2=(0.0569/0.0816)*Egamma_MeV^2*BE2_same_line/BM1_same_line',
              'B_ratio_coefficient':.0569/.0816,'delta_Q21_over_mu11_coefficient':math.sqrt((.0569/.0816)*(5/3)),
              'boundary':'same DeltaI1 photon and declared units; not interbranch strength ratio, signed delta, or IC/branch correction of an actual measurement'},
         'finite_spin_geometry_controls':finite,'original_human_review_prefix_bytes_preserved':True,
         'not_MU08_historical_producer_or_shape_measurement':True,
         'no_new_experimental_tau_B_Qt_or_CI':True,'ok':True}
    (RUN/'frauendorf2001-e2-exercise-result.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(out,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
