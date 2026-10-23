#!/usr/bin/env python3
"""135Pr source-separated photon ratios and model limits; no datafit or confidence certification."""
import argparse,hashlib,json,math
from pathlib import Path
from day20_multipolarity_contract040 import fraction,envelope


def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run-dir',type=Path,required=True);args=p.parse_args();checks=[]
 def check(name,ok):
  if not ok:raise AssertionError(name)
  checks.append(name)
 rows=[{'Egamma_keV':747.3,'Ei_keV':1477.9,'initial_two_I':17,'final_two_I':15,'initial_band':3,'final_band':1,'delta':-.47,'delta_minus':.22,'delta_plus':.09,'P':.04,'P_minus':.13,'P_plus':.08,'Rac':.37,'Rac_error':.04,'SI_Ap':.006,'SI_Ap_minus':.019,'SI_Ap_plus':.012,'I_gamma':9.4,'I_gamma_error':.5,'polarization_gate_keV':450.},
 {'Egamma_keV':813.2,'Ei_keV':2203.9,'initial_two_I':21,'final_two_I':19,'initial_band':3,'final_band':1,'delta':-.37,'delta_minus':.14,'delta_plus':.10,'P':-.03,'P_minus':.12,'P_plus':.05,'Rac':.48,'Rac_error':.06,'SI_Ap':-.004,'SI_Ap_minus':.016,'SI_Ap_plus':.007,'I_gamma':6.4,'I_gamma_error':.3,'polarization_gate_keV':796.},
 {'Egamma_keV':450.2,'Ei_keV':1927.7,'initial_two_I':19,'final_two_I':17,'initial_band':4,'final_band':3,'delta':-.31,'delta_minus':.13,'delta_plus':.10,'P':-.07,'P_minus':.10,'P_plus':.09,'Rac':.49,'Rac_error':.04,'SI_Ap':-.017,'SI_Ap_minus':.023,'SI_Ap_plus':.022,'I_gamma':4.4,'I_gamma_error':.2,'polarization_gate_keV':747.}]
 for r in rows:
  r['photon_E2_fraction']=fraction(r['delta']);r['photon_M1_fraction']=1-r['photon_E2_fraction'];r['P_printed_endpoints']=[r['P']-r['P_minus'],r['P']+r['P_plus']];ds=[r['delta']-r['delta_minus'],r['delta']+r['delta_plus']];r['photon_E2_fraction_endpoint_transform']=[min(fraction(v) for v in ds),max(fraction(v) for v in ds)]
 check('all three printed P ranges include zero so sign alone is not branch selector',all(r['P_printed_endpoints'][0]<0<r['P_printed_endpoints'][1] for r in rows))
 check('all printed delta endpoints remain below unit modulus',all(max(abs(r['delta']-r['delta_minus']),abs(r['delta']+r['delta_plus']))<1 for r in rows))
 # Conditional same-parent E2ratio, SIphoton intensities and pure referenceE2 assumed.
 relatives=[]
 for row,eref,iref,quoted in [(rows[0],526.2,.4,.7),(rows[1],726.,3.7,.12)]:
  qratio=row['I_gamma']/iref*(eref/row['Egamma_keV'])**5*fraction(row['delta'])
  relatives.append({'same_parent_Ei_keV':row['Ei_keV'],'out_Egamma_keV':row['Egamma_keV'],'reference_Egamma_keV':eref,'I_out':row['I_gamma'],'I_reference':iref,'assumed_reference_pure_E2':True,'central_photon_reconstruction':qratio,'author_quoted_ratio':quoted,'scope':'Declared same-parent photon ratio and commonrate coefficient; parenttau cancels. No rawfit/branchCov, no uncertainty or experimentalCI reconstruction.'})
 check('two sameparent reconstructions at source printed central precision',round(relatives[0]['central_photon_reconstruction'],1)==.7 and round(relatives[1]['central_photon_reconstruction'],2)==.12)
 # Identical parent lifetime scales both extracted component strengths, cancelling ratio.
 base=relatives[1]['central_photon_reconstruction'];check('sameparent total lifetime cancellation is conditional on sharedparent inputs',all(math.isclose((base/t)/(1/t),base) for t in [.2,1.,5.]))
 older=[{'Egamma_keV':747.,'initial_two_I':17,'final_two_I':15,'delta':-1.24,'delta_error':.13,'A':.047,'A_error':.012,'quoted_E2_percent':60.6,'quoted_E2_error':5.1},
 {'Egamma_keV':812.8,'initial_two_I':21,'final_two_I':19,'delta':-1.54,'delta_error':.09,'A':.054,'A_error':.034,'quoted_E2_percent':70.3,'quoted_E2_error':2.4,'B_E2_out_in':.843,'B_E2_out_in_error':.032},
 {'Egamma_keV':754.6,'initial_two_I':25,'final_two_I':23,'delta':-2.38,'delta_error':.37,'A':None,'quoted_E2_percent':85.,'quoted_E2_error':4.,'B_E2_out_in':.500,'B_E2_out_in_error':.025}]
 out={'checkpoint':'041','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'experimental_fit_or_CI':False,
 'Lv2022_main_Table1_and_SI_Table1':rows,'Lv755_missing_measurement':{'Egamma_keV':755.1,'initial_two_I':25,'final_two_I':23,'Rac':.50,'Rac_error':.06,'P':None,'delta':None,'scope':'Author suggests similar solution to813, not direct new jointdelta measurement.'},
 'Matta2015_TableI':older,'sameparent_relative_E2_reconstruction':relatives,
 'observable_lineage':'MattaA is INGA countasymmetry, AD from separate Gammasphere acquisition. LvSI Ap and mainP are sameJUROGAM data withP=Ap/Q, not independentpolarization acquisitions; Rac shares data/gates and calibration, actualjointCov absent. Difference inpublishedP sign is not directly comparable toA.',
 'author_interpretations':{'Matta2015':'E2-dominated links plus decreasing E_wob support authorsTW interpretation; fittedQTR inertia and TAC discussed, not universally proven.', 'Lv2022':'NewP-Rac branch selection and .7(+.7/-.5) 747/526 relativeE2 test plus bandregrouping argue against proposedone/twophonon assignments; QTR withirrotationalMoI andfreeparticle yields authorTiP interpretation.'},
 'model_comparison_boundary':'MattaPDF4 fits Jm,Js,Jl=7.4,5.6,1.8 andc=.116. PDF5 explicitly Coriolis detaches j from shortaxis and aligns it withmediumaxis nearEwob upturn. LvPDF4–5/SI4–6 criticize earlierfrozen assumptions. Preserve both primary statements; do not infer actualMatta producer is frozen atallspins without originalcode/comparison.',
 'QTR_scope':'Lv epsilon2=.16 gamma26deg; SIJ0=12.5hbar2/MeV J1=12.5hbar4/MeV3,10negativeparityorbitals; modelunderliesorientation, not directtrajectory. Energiesbands2/5 overestimatedat highspin. No direct lifetime/absoluteB measurement generatedbythese ratios.',
 'withdrawn':['ratio<1.5 as universalphonon rejection threshold','M1fraction alone uniquely provesTiP or excludesallwobbling','A andP orSI Ap andmainP are independent identicalobservables','all earlierQTR spins provenfrozen fromlatercriticism','repeated oldAD fits are independentnewacquisition'],
 'controls':checks,'certification_scope':'Source ledger and declared photon-ratio algebra only; no newexperimentalCI/response replay or finalcontroversy verdict.'}
 path=args.run_dir/'pr135-source-contract-result-041.json';path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'artifact':str(path),'controls':len(checks),'reconstructed_ratios':relatives}))
if __name__=='__main__':main()
