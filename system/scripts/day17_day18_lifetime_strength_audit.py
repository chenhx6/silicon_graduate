#!/usr/bin/env python3
"""Day17 uncredited Day18: published table conversions, no DSAM refit."""
from __future__ import annotations
import argparse,hashlib,json,math
from pathlib import Path
import sympy as s
from sympy.physics.wigner import clebsch_gordan


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--contract',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();c=json.loads(a.contract.read_text());assert c['identity']=='DAY17-UNCREDITED18-LIFETIME-STRENGTH-AUDIT-01'
    for path,h in c['source_hashes'].items():assert sha(path)==h,path
    C=c['modern_E2_ps_MeV_e2b2_constant'];rows=[]
    for row in c['jensen_table2']:
        ji=s.Rational(row['Ji2'],2);jf=ji-2;k=s.Rational(1,2);cg2=clebsch_gordan(ji,2,jf,k,0,k)**2
        e=row['E_keV']/1000;t=row['tau_ps'];B=C/(t*e**5);qt=math.sqrt(16*math.pi*B/(5*float(cg2)))
        # Printed central decimal closure only, not quoted experimental intervals.
        E_lo,E_hi=(row['E_keV']-.05)/1000,(row['E_keV']+.05)/1000
        t_lo,t_hi=t-.005,t+.005
        q_lo=math.sqrt(16*math.pi*C/(5*float(cg2)*t_hi*E_hi**5))
        q_hi=math.sqrt(16*math.pi*C/(5*float(cg2)*t_lo*E_lo**5))
        overlap=max(q_lo,row['Qt_eb']-.05)<=min(q_hi,row['Qt_eb']+.05)
        rows.append({**row,'fixedK_half_CG_squared_exact':str(cg2),'conditional_partial_photon_rate_s-1':1e12/t,'conditional_B_E2_e2b2':B,'conditional_Qt_eb':qt,'Qt_vs_source_relative_difference':qt/row['Qt_eb']-1,'conditional_nearest_decimal_rounding_box_Qt':[q_lo,q_hi],'rounding_boxes_overlap':overlap})
    mu=[];boxes=[]
    for row in c['mu08_tableII']:
        ji=s.Integer(row['I']);b=row['BE2'];q=row['Qt'];gs=clebsch_gordan(ji,2,ji-2,ji,-2,ji-2)**2;g0=clebsch_gordan(ji,2,ji-2,0,0,0)**2
        assert s.simplify(gs-(2*ji-3)/(2*ji+1))==0
        make=lambda v,g:math.sqrt(16*math.pi*v/(5*float(g)))
        qs=make(b,gs);q0=make(b,g0);b_interval=[b-.005,b+.005];q_interval=[q-.005,q+.005];pred_interval=[make(z,gs) for z in b_interval];overlap=max(pred_interval[0],q_interval[0])<=min(pred_interval[1],q_interval[1])
        mu.append({**row,'candidate_stretched_axis_CG_squared_exact':str(gs),'fixedK_zero_CG_squared_exact':str(g0),'candidate_Qt_from_B_eb':qs,'fixedK_zero_Qt_from_B_eb':q0,'candidate_over_fixedKzero_Qt':qs/q0,'candidate_relative_to_printed_Qt':qs/q-1,'nearest_cent_rounding_boxes_overlap':overlap,'rounding_assumption':'hypothetical nearest0.01 for B and Qt; not source CI or recovered producer'})
        boxes.append(overlap)
    # Source independent statistical formulas; no actual covariance supplied.
    x=s.symbols('x',positive=True);i=s.symbols('I',positive=True);forms={'stretched_CG_squared':'(2I-3)/(2I+1)','Qt_constantK':'sqrt(16pi B/(5 G_K))','log_B':'log p_gamma-log tau-5log E+log C_E2','log_Qt':'(log B-log G_K+log(16pi/5))/2','mean_vs_half_life_factor_Qt':str(s.sqrt(s.log(2))),'unit_conversion_b2_to_fm4':10000}
    result={'identity':c['identity'],'formal_day_index':17,'preview_day_index':18,'formal_credit18':False,'script_sha256':sha(__file__),'contract_sha256':sha(a.contract),'source_hashes':c['source_hashes'],'jensen_conditional_rows':rows,'mu08_candidate_geometry_rows':mu,'jensen_max_conditional_Qt_relative_residual':max(abs(x['Qt_vs_source_relative_difference']) for x in rows),'mu08_all_candidate_roundingboxes_overlap':all(boxes),'formula_contract':forms,'assumptions':c['assumptions'],'experimental_lifetime_or_strength_refit':False,'ok':all(boxes) and all(row['rounding_boxes_overlap'] for row in rows)}
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['source_hashes','assumptions']},ensure_ascii=False,indent=2));return 0 if result['ok'] else 1
if __name__=='__main__':raise SystemExit(main())
