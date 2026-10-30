"""Small direct response/Jacobian audit; no CLI producer or nuclear fit."""
import json, sys
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'raw/writing/pado/Upload'))
from p_ado.physics.pado import build_pado_points
from p_ado.compute.jacobian import transform_pdf_with_central_difference

def main():
    delta=np.array([-2.,-1.,-.5,0.,.5,1.,2.])
    theta=np.array([-63.,-45.,-26.565,0.,26.565,45.,63.])
    sigma_i=np.array([.10,.20,.30,.40,.50])
    rows=[]
    for ji,jf,label in [(5.5,4.5,'11/2->9/2'),(9.5,8.5,'19/2->17/2')]:
        points=build_pado_points(ji,jf,delta,theta,ji*sigma_i,sigma_i)
        # Constant PDFs isolate the response Jacobian from input-likelihood shape.
        out,report,export=transform_pdf_with_central_difference(
            points,lambda x: np.ones_like(x),lambda x: np.ones_like(x),
            return_report=True,return_array=True,return_export_data=True,
            high_density_rel_thresholds=(1e-3,))
        rr=report['delta_sigma']; rt=report['theta_sigma']
        rows.append({'transition':label,'grid_shape':list(points.shape),
          'delta_report':{k:rr[k] for k in ['status','zero_count','near_zero_count','abs_min','signed_min','signed_max','positive_count','negative_count','sign_change','high_density']},
          'theta_report':{k:rt[k] for k in ['status','zero_count','near_zero_count','abs_min','signed_min','signed_max','positive_count','negative_count','sign_change','high_density']},
          'array_shape':list(out.shape),'export_keys':sorted(export),
          'point_shape':list(points.shape)})
    checks={'two_transitions':len(rows)==2,
      'all_finite_regular_grid':all(r['delta_report']['status']=='accepted' and r['theta_report']['status']=='accepted' for r in rows),
      'small_grid_not_full_production':True,
      'no_claim_of_global_invertibility':True}
    result={'scope':'small synthetic-PDF direct response/Jacobian audit; not manuscript benchmark or experiment','delta_grid':delta.tolist(),'theta_grid_deg':theta.tolist(),'sigma_i':sigma_i.tolist(),'rows':rows,'checks':checks,'passed':all(checks.values())}
    assert result['passed']; print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
