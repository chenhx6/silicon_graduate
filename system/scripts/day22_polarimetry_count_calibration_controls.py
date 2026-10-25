#!/usr/bin/env python3
"""Miller convention/count algebra and chosen calibration degeneracy; no beam-time prediction."""
import argparse,hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
RAW=ROOT/'raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/2007_Miller et al_Linear polarization sensitivity of SeGA detectors.pdf'
SHA='a334ee35a84ded50f6a7937c037ee13d2d06b2f8406b0c68fac1a4245999acf3'
def pol(x,y,a,q):return (x-a*y)/(x+a*y)/q

def calculate():
 if hashlib.sha256(RAW.read_bytes()).hexdigest()!=SHA:raise ValueError('raw identity mismatch')
 x,y,a,q=180.,1250.,.12,.14;den=x+a*y;A=(x-a*y)/den
 jac=[2*a*y/(q*den**2),-2*a*x/(q*den**2),-2*x*y/(q*den**2),-A/q**2]
 args=[x,y,a,q];fd=[]
 for i,value in enumerate(args):
  step=max(abs(value),1)*1e-6;up=args.copy();down=args.copy();up[i]+=step;down[i]-=step
  fd.append((pol(*up)-pol(*down))/(2*step))
 varA=4*a*a*x*y*(x+y)/den**4
 N=x+y;D=(a+1)+(a-1)*A
 fisher_varA=D*D*(1-A*A)/(4*a*N)
 # Reconstruct source'srounded5000photopeakexample withknowna andindependentprimitivecounts.
 Npeak=5000;nx=.03*Npeak;ny=.25*Npeak;anull=nx/ny;Q=.14
 null_varP=4*anull**2*nx*ny*(nx+ny)/(nx+anull*ny)**4/Q**2
 # Chosen means(954,940), oppositeP values compensated byunknowna andyieldc.
 Qtest=.2;P0=.3;a0=.9;c0=1000.;mu0=[a0*c0*(1+Qtest*P0),c0*(1-Qtest*P0)]
 P1=-P0;a1=(mu0[0]/mu0[1])*(1-Qtest*P1)/(1+Qtest*P1);c1=mu0[1]/(1-Qtest*P1)
 mu1=[a1*c1*(1+Qtest*P1),c1*(1-Qtest*P1)]
 controls={
  'reciprocal_a_conventions_agree_for_nonzero_A':abs(A-((x/a-y)/(x/a+y)))<1e-14,
  'analytic_jacobian_matches_finite_difference':max(abs(u-v) for u,v in zip(jac,fd))<1e-7,
  'Poisson_variance_matches_conditional_binomial_Fisher':abs(varA-fisher_varA)<1e-14,
  'source_rounded_photopeak_example_has_sigmaP_near_point31':.30<math.sqrt(null_varP)<.32,
  'opposite_physical_P_same_positive_target_means_without_a_calibration':max(abs(u-v) for u,v in zip(mu0,mu1))<1e-10 and min(mu0+mu1+[a0,a1,c0,c1])>0,
 }
 return {'raw_sha256':SHA,'source':'printed714Eqs5/6,716selectionfractions,718Outlook','convention':'A=(Nperp-a*Nparallel)/(Nperp+a*Nparallel),a=Uperp/Uparallel;otherCloverconventionusesreciprocala','Jacobian_P_wrt_x_y_a_Q':jac,'finite_difference_Jacobian':fd,'chosen_nonzero_A_case':{'x':x,'y':y,'a':a,'Q':q,'A':A,'Poisson_varA':varA,'conditional_Fisher_varA':fisher_varA},'photopeak_example':{'Npeak':Npeak,'rounded_perp_fraction':.03,'rounded_parallel_fraction':.25,'selected_counts':[nx,ny],'selected_sum':nx+ny,'chosen_known_a_from_rounded_fractions':anull,'Q_chosen_from_source_table':Q,'conditional_sigmaP':math.sqrt(null_varP),'naive_using_photopeak_as_balancedselected_sigmaP':1/(Q*math.sqrt(Npeak))},'calibration_degeneracy_witness':{'mean_counts':mu0,'case0':{'Q':Qtest,'P':P0,'a':a0,'c':c0},'case1':{'Q':Qtest,'P':P1,'a':a1,'c':c1},'model':'mu_perp=a*c*(1+Q*P),mu_parallel=c*(1-Q*P)'},'controls':controls,'boundaries':['AllstatisticsconditionalonindependentPoisson,exclusivebins,knownbackground-freepositivecounts;realnetpeakfitsneedtheiractualCov/likelihood.','Rounded3%/25%andQ.14exampleisnotnewSeGAcalibrationoritsactualconfidenceinterval.','UnknownaunconstrainedwitnessdoesnotshowambiguitywithinactualmeasuredCloverauncertainties.','FullVarP=g^T Sigma g;ifcalibrationisuncertaincorrelationsmustbekept;nosourceunitspreadtreatedastargetsigma.','NoQ,selectedefficiency,rate,CLorpowerisassignedto225.8keV/JYFL/AGATA.']}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True);a=p.parse_args();out=(ROOT/a.output).resolve()
 if not out.is_relative_to(ROOT/'outputs'):p.error('outputmustbeinsideoutputs/')
 d=calculate();out.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'controls':d['controls'],'conditional_sigmaP_5000photopeak':d['photopeak_example']['conditional_sigmaP'],'unknown_a_witness':d['calibration_degeneracy_witness']}));return 0 if all(d['controls'].values()) else 1
if __name__=='__main__':raise SystemExit(main())
