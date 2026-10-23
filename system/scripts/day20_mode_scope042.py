#!/usr/bin/env python3
"""Source-specific La/Xe/Nd roots and declared geometry/relative-rate controls, no classifier."""
import argparse,hashlib,json,math
from pathlib import Path
import numpy as np
from day20_multipolarity_contract040 import fraction


def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run-dir',type=Path,required=True);a=p.parse_args();checks=[]
 def check(name,ok):
  if not ok:raise AssertionError(name)
  checks.append(name)
 la=[]
 for energy,ji,jf,d,dm,dp,be,small in [(758,17,15,-2.05,.30,.39,1.127,-.35),(874,21,19,-2.60,.47,.46,.716,-.40),(982,25,23,-3.07,.65,.47,.545,-.38)]:
  la.append({'Egamma_keV':energy,'initial_two_I':ji,'final_two_I':jf,'source_adopted_delta':d,'delta_minus':dm,'delta_plus':dp,'source_B_E2_out_in':be,'chosen_small_delta_not_tabulated_as_source_solution':small,'conditional_B_ratio_if_only_delta_changed':be*fraction(small)/fraction(d),'conditional_fraction_quotient':fraction(d)/fraction(small),'boundary':'Chosen root sensitivity, not original jointfit/candidate probability or noncollective proof.'})
 xe={'Egamma_keV':483,'initial_two_I':13,'final_two_I':11,'source_large_delta':-2.1,'large_delta_error':.2,'source_small_delta':-.29,'small_delta_minus':.04,'small_delta_plus':.03,'source_P':.23,'source_P_error':.13,'source_DCO':.303,'source_DCO_error':.021,'source_asymmetry':.058,'source_asymmetry_error':.032,'source_adoption':'Authors select large branch using polarization; small is an AD/DCOalternative, not adopted jointresult','B_E2_out_in':None}
 xe['central_fraction_ratio_large_to_small']=fraction(-2.1)/fraction(-.29)
 check('actual Xe source root differs from oldchosenminus.31',not math.isclose(xe['source_small_delta'],-.31))
 # Nd published file has repository cover: rawPDF5=journalpage4, rawPDF6=page5.
 nd={'printed_Egamma_keV':751,'initial_I':17,'final_I':16,'delta':-.48,'delta_minus':.14,'delta_plus':.13,'Rac':.55,'Rac_error':.05,'AP_literal':.03,'AP_minus':.07,'AP_plus':.06,'P_literal':.02,'P_minus':.05,'P_plus':.04,'B_M1_out_over_B_E2_in':.61,'B_M1_ratio_error':.29,'B_E2_out_over_B_E2_in':.36,'B_E2_ratio_error':.17}
 nd['photon_E2_fraction']=fraction(nd['delta']);nd['photon_M1_fraction']=1-nd['photon_E2_fraction']
 # Shared mixed outgoing line: B(M1)/B(E2)=(cE2/cM1)*E^2/delta^2.
 # Explicit conventional rounded coefficients in ps^-1 with B(E2)e2b2/B(M1)muN2.
 cE2,cM1=12.252,17.60;ratio=(cE2/cM1)*(.751**2)/(.48**2);bm1_derived=ratio*.36
 check('same mixedline already links the two relative strength ratios centrally',abs(bm1_derived-.61)<.01)
 # Retain AP/P literal conflict without importing another experiment'sQ.
 nd['central_Q_if_P_equals_AP_over_Q']=nd['AP_literal']/nd['P_literal']
 # Classical component counterexample and quantum highest-weight counterexample.
 jp=np.array([1.,1.,1.]);jn=np.array([2.,1.,1.]);R=jp+jn;J=jp+jn+R;volume=float(np.dot(np.cross(jp,jn),R))
 check('three nonzero totalJ components do not imply chiral vector tripleproduct',np.all(J!=0) and volume==0)
 j=5.5;m=np.arange(j,-j-1,-1);Jp=np.zeros((12,12),complex)
 for col in range(1,12):Jp[col-1,col]=math.sqrt((j-m[col])*(j+m[col]+1))
 Jx=(Jp+Jp.conj().T)/2;Jy=(Jp-Jp.conj().T)/(2j);Jz=np.diag(m);psi=np.eye(12,dtype=complex)[:,0]
 ex=lambda M:float(np.real(psi.conj()@M@psi));means=[ex(M) for M in [Jx,Jy,Jz]];variances=[ex(M@M)-ex(M)**2 for M in [Jx,Jy,Jz]]
 check('zero transverse means need not be zero quantumfluctuations',means[:2]==[0.,0.] and np.allclose(variances[:2],[j/2,j/2]))
 f1=1/(1+9);f2=100/(100+900)
 check('fixed multipole fraction does not set absolute componentstrength',math.isclose(f1,f2) and 100/1==100)
 out={'checkpoint':'042','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'experimental_fit_or_CI':False,
 'La_selected_Table1':la,'La_model_boundary':'AuthorsLW withj alignedshortaxis, earlypositiveparitypair alignment increaseseffectiveJs abovelargermediuminertia. Longitudinal relative tolargestMoIaxis, not universalj_m. Tablecontains618line and1031missingdelta row too; no source-smallrootprior inferred.',
 'Xe_483_source':xe,'Xe_topology_boundary':'Authors reportBand4 decaytoBand3 andBand1 withDeltaI0,1,2; DeltaI0moreintensethanDeltaI2 and resemblance to126Xequasigamma suggest possiblewobbling-gammacoupling, needtheory. TheyretainBand4n_w2interpretation, not exclusivepuregamma or disprovedwobbling. NoSIreadthischeckpoint.',
 'Nd_literal_selected':nd,'Nd_same_line_rate_identity':{'chosen_coeff_E2_ps_per_MeV5_e2b2':cE2,'chosen_coeff_M1_ps_per_MeV3_muN2':cM1,'B_M1_out_over_B_E2_out_from_delta':ratio,'B_M1_out_over_B_E2_in_if_B_E2_ratio0p36':bm1_derived,'boundary':'Shared derivedinputs mean agreement is not newindependentvalidation. Roundingconstantsnotactualproduceridentification; noCov/CI.'},
 'Nd_model_and_response_boundary':'Authorseveneven2qpcase explicitlyallowsM1-dominated links; energyparamsfitted, chi*beta2 fixedbyoneE2ratio, g_eff/Q fittedbysamedelta. Curvehighspinextrapolations conditional, not independentabsoluteB/tau. Literal AP=.03 andP=.02 retained; no actualresponseformula/calibrator here, no importedPrQ or silentcorrection. CentralQ1.5 only underaddedP=AP/Qcontract, not inferredrealQ or experimentalinconsistency significance.',
 'classical_counterexample':{'j_proton':jp.tolist(),'j_neutron':jn.tolist(),'R':R.tolist(),'total_J':J.tolist(),'triple_product':volume,'scope':'Chosen coplanarclassicalvectors, not nuclearfit.'},'quantum_component_counterexample':{'j':j,'mean_Jxyz':means,'variance_Jxyz':variances,'scope':'Highestweight spinstate only, not a solvedwobblingor chiralstate. Invalidatesmean0=>fluctuation0shortcut.'},
 'withdrawn':['fixedE2>80/M1>80 absolute mode rules','smallselected sensitivity root is actualexperimental branch','M1fraction orsmallrelativeE2 proves singleparticle/noncollectiveidentity','allLW means jmediumregardlessMoIordering','wobbling strictlyplanar withzeroallotherquantumcomponents','stringchecks validate completegeometric classifier','nearidenticalbands alone prove staticchirality'],
 'controls':checks,'certification_scope':'Source-specific literal data and chosen mathematicalcounterexamples only; no directshape/trajectory, finalmodeassignment or experimentalCI.'}
 path=a.run_dir/'mode-scope-result-042.json';path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'artifact':str(path),'controls':len(checks),'Xe_fraction_ratio_actualroot':xe['central_fraction_ratio_large_to_small'],'Nd_shared_rate_reconstruction':bm1_derived,'La_chosen_sensitivities':[r['conditional_B_ratio_if_only_delta_changed'] for r in la]}))
if __name__=='__main__':main()
