#!/usr/bin/env python3
"""Published Tm165 band-mixing algebra and reference dependency; no original fit."""
from pathlib import Path
import hashlib,json,math
from datetime import datetime,timezone
import numpy as np
import sympy as s
from sympy.physics.wigner import clebsch_gordan
ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    path=RUN/'jensen-bandmixing-contract.json';c=json.loads(path.read_text());assert c['identity']=='J01-BANDMIXING-REFERENCE-CHAIN-01'
    for p,h in c['source_hashes'].items():assert sha(ROOT/p)==h,p
    n=c['negative_pair'];ratio=n['I_1639']/n['I_1775'];energy3=(n['E_1639_keV']/n['E_1775_keV'])**3;bb_over_aa=ratio/energy3;aa=1/(1+bb_over_aa);bb=1-aa;alpha,beta=math.sqrt(aa),math.sqrt(bb);sine=2*alpha*beta;theta=2*math.atan2(beta,alpha);principal=math.asin(sine);V=n['observed_gap_keV']*alpha*beta
    J=s.Rational(13,2);Ks=[s.Rational(7,2),s.Rational(1,2)];g=[]
    for K in Ks:
        cg2=clebsch_gordan(J,2,J-2,K,0,K)**2
        closed=3*(J+K-1)*(J+K)*(J-K-1)*(J-K)/(2*J*(J-1)*(2*J-1)*(2*J+1))
        assert s.simplify(cg2-closed)==0;g.append(cg2)
    G=s.factor(g[0]/g[1]);assert G==s.Rational(3,7)
    kinematic=(n['E_2587_keV']/n['E_2040_keV'])**5*(n['E_1284_keV']/n['E_1422_keV'])**3
    lambda1=n['I_2587']/n['I_1422'];lambda2=n['I_2040']/n['I_1284'];lambda_ratio=lambda1/lambda2
    R_Q=math.sqrt(kinematic*(aa/bb)*float(G)/lambda_ratio)
    assert abs(energy3*(beta/alpha)**2-ratio)<1e-12
    wrong_ratio=energy3*math.tan(principal/2)**2
    # Positive-parity two-band table's eigenvalues/eigenvectors are model
    # outputs. Check printed normalization and interaction, not data GOF.
    positive=[]
    for row in c['positive_pair_table5']:
        a,b=row['a'],row['b'];gap=row['Ecalc404']-row['Ecalc411'];v=abs(a*b*gap);eps=.00005;bound=2*eps*(abs(a)+abs(b))+2*eps*eps
        positive.append({**row,'norm_squared_minus1':a*a+b*b-1,'normalization_outer_rounding_bound':bound,'norm_necessary_rounding_check':abs(a*a+b*b-1)<=bound,'abs_interaction_from_printed_model_values_keV':v,'fits_printed5point0_rounding_box':4.95<=v<=5.05})
    # A separate explicitly conditional SD design, not recovered original fit.
    q541,q411,rplus,rminus=[c['reference_primitives'][k] for k in ['Q541','Q411','r404_over411','r541_over523']]
    Q=np.array([q541,q411,rplus*q411,q541/rminus]);Jac=np.array([[1,0,0,0],[0,1,0,0],[0,rplus,q411,0],[1/rminus,0,0,-q541/rminus**2]],float);sd=np.array(c['conditional_primitive_SD_design']);Sigma=Jac@np.diag(sd*sd)@Jac.T
    R=Q/Q[0];L=np.eye(4)/Q[0];L[:,0]-=Q/Q[0]**2;SigmaR=L@Sigma@L.T
    direct_sd=sd[3]/rminus**2;assert abs(math.sqrt(SigmaR[3,3])-direct_sd)<1e-14
    assert np.linalg.eigvalsh(Sigma).min()>0 and np.linalg.eigvalsh(SigmaR).min()>-1e-14
    crossings=c['matched_N96_crossing_rows'];first=crossings[0];double=[]
    for row in crossings[1:]:
        obs=first['measured_keV']-row['measured_keV'];theory=first['calculated_keV']-row['calculated_keV']
        double.append({'reference':row['nucleus'],'same_N':row['N'],'observed_Tm_minus_reference_keV':obs,'model_Tm_minus_reference_keV':theory,'double_difference_keV':obs-theory,'not_new_proton_neutron_interaction_measurement':True})
    result={'identity':c['identity'],'script_sha256':sha(__file__),'contract_sha256':sha(path),'negative_pair_from_actual_printed_inputs':{'M1_photon_ratio':ratio,'beta_squared_over_alpha_squared':bb_over_aa,'alpha_squared':aa,'beta_squared':bb,'theta_selected_deg':math.degrees(theta),'principal_asin_deg':math.degrees(principal),'M1_ratio_from_wrong_principal_branch':wrong_ratio,'abs_V_keV':V,'author_V_keV':n['author_abs_V_keV'],'CG_squared_exact':[str(x) for x in g],'CG_ratio_squared_exact':str(G),'lambda523':lambda1,'lambda541':lambda2,'Q541_over_Q523_from_Eq5':R_Q,'author_Q541_over_Q523':n['author_Qratio'],'not_new_signed_V_or_multipole_delta':True},'positive_pair_table5_model_closure':positive,'reference_dependency':{'order_Q':['Q541','Q411','Q404','Q523'],'order_primitives':['Q541','Q411','r404_over411','r541_over523'],'Q_from_author_printed_primitives':Q.tolist(),'Jacobian':Jac.tolist(),'conditional_independent_SD_design':sd.tolist(),'conditional_Sigma_Q':Sigma.tolist(),'conditional_ratio_Q_over_Q541':R.tolist(),'conditional_Sigma_ratios':SigmaR.tolist(),'conditional_sigma_Q523_over_Q541':direct_sd,'source_Table6_R523_printed':[.87,.10],'do_not_infer_actual_Cov_from_matching_summary_errors':True,'no_extra_5percent_added':True},'matched_N96_crossing_rows':crossings,'crossing_central_double_differences':double,'assumptions':c['assumptions'],'original_VMI_DCO_or_Dsam_fit_reproduced':False,'new_experimental_CI':False,'ok':all(x['norm_necessary_rounding_check'] and x['fits_printed5point0_rounding_box'] for x in positive),'generated_at':datetime.now(timezone.utc).isoformat()};(RUN/'jensen-bandmixing-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['negative_pair_from_actual_printed_inputs','positive_pair_table5_model_closure','reference_dependency','ok']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
