"""Refine conditional detJ sign brackets; no CLI producer or raw edits."""
from __future__ import annotations
import importlib.util, json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
src=ROOT/'outputs/learning-daily/20261027-DAY25-chirality-counterevidence-shape-coexistence-run-01/pado-jacobian-sign-audit-011.py'
spec=importlib.util.spec_from_file_location('audit011',src)
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

def root_for(xi,left,right,h_delta=1e-5,h_sigma=1e-5):
    delta=math.tan(math.radians(xi)); fl=mod.finite_det(9.5,8.5,delta,left,h_delta,h_sigma); fr=mod.finite_det(9.5,8.5,delta,right,h_delta,h_sigma)
    assert fl*fr<0
    a,b=left,right
    for _ in range(70):
        m=(a+b)/2; fm=mod.finite_det(9.5,8.5,delta,m,h_delta,h_sigma)
        if fl*fm<=0: b,fr=m,fm
        else: a,fl=m,fm
    x=(a+b)/2
    return {'xi_deg':xi,'bracket':[left,right],'root_sigma_over_i':x,'det_at_root':mod.finite_det(9.5,8.5,delta,x,h_delta,h_sigma),'det_left':fl,'det_right':fr,'h_delta':h_delta,'h_sigma_over_i':h_sigma}

def main():
    roots=[]
    for xi,a,b in [(-85,.50,.60),(80,.40,.50)]:
        base=root_for(xi,a,b)
        base['step_sensitivity']=[root_for(xi,a,b,hd,hs) for hd,hs in [(1e-4,1e-4),(1e-5,1e-5),(1e-6,1e-6)]]
        roots.append(base)
    result={'schema':'pado-jacobian-root-refinement-012','scope':'conditional bisection of finite-mesh detJ sign brackets for Ji=19/2->17/2; not a global-fold or mode proof','source':'pado-jacobian-sign-audit-011','roots':roots,'checks':{'two_roots_refined':len(roots)==2,'residuals_small':all(abs(r['det_at_root'])<1e-8 for r in roots),'steps_recorded':all(len(r['step_sensitivity'])==3 for r in roots)}}
    result['passed']=all(result['checks'].values()); assert result['passed']; print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
