"""Arithmetic audit for the effective-g boundary.

The Pb ratio is a scale comparison (0.92/1.17), not a pure spin quenching
measurement. Pr has no absolute B(M1); Ag values are listed but no unique
geometry is assumed.
"""
from pathlib import Path
import json,math
out=Path(__file__).resolve().parent
pb={'g_eff_fit':0.92,'g_eff_schmidt':1.17}
pb['scale_ratio']=pb['g_eff_fit']/pb['g_eff_schmidt']
def conditional_delta_g(B,I,jp,jn,theta_deg):
 return math.sqrt(8*math.pi*B/3)*I/(jp*jn*math.sin(math.radians(theta_deg)))
# Illustrative only: not assigned to an isotope, and intentionally not used as an empirical result.
illustrative={'B_M1_muN2':2.0,'I':15.0,'jp':5.5,'jn':10.0,'theta_deg':90.0,'delta_g_conditional':conditional_delta_g(2,15,5.5,10,90)}
data={'status':'boundary-audit','Pb':pb,'Pr':{'135Pr':'no absolute lifetime; no empirical delta-g inversion','137Pr':'relative B(M1)/B(E2) only; no empirical delta-g inversion'},'106Ag':{'absolute_BM1_available':True,'unique_shears_geometry_available':False,'empirical_delta_g':'not identifiable from Table I alone'},'illustrative_formula_check':illustrative,'warnings':['Pb ratio is not q_s','GT and M1 giant-resonance quenching are not the same observable','illustrative value is not an isotope fit'],'review_status':'unreviewed'}
(out/'mr-effective-g-audit.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
