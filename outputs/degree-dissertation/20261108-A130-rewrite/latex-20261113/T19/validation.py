#!/usr/bin/env python3
"""Independent exact-rational controls of orientation and the frozen toy model."""
import ast, hashlib, json, math
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent
src=P/'a130_angular_branch_figure.frozen.py'
variables={}
for node in ast.walk(ast.parse(src.read_text())):
 if isinstance(node,ast.Assign) and len(node.targets)==1:
  target=node.targets[0]
  if isinstance(target,ast.Tuple) and all(isinstance(x,ast.Name) for x in target.elts):
   try: values=ast.literal_eval(node.value)
   except (ValueError,TypeError): continue
   for name,value in zip(target.elts,values):
    if name.id in ('n0','n1','n2','d0','d1','d2','w0','w1','w2','p0','p1','p2','exp_val','exp_err'): variables[name.id]=F(str(value))
  if isinstance(target,ast.Name) and target.id in ('exp_val','exp_err'):
   variables[target.id]=F(str(ast.literal_eval(node.value)))
assert len(variables)==14
def coeff(prefix): return tuple(variables[f'{prefix}{i}'] for i in range(3))
def add(p,q,sgn=1): return tuple(a+sgn*b for a,b in zip(p,q))
def ev(p,x): return float(p[0])+float(p[1])*x+float(p[2])*x*x
def describe(p):
 c,b,a=p; disc=b*b-4*a*c
 return {'coefficients_constant_first':list(map(str,p)), 'discriminant':str(disc), 'minimum':str(c-b*b/(4*a)), 'strictly_positive':a>0 and disc<0}
N,D,W,H=map(coeff,('n','d','w','p'))
r=variables['exp_val']; c,b,a=tuple(n-r*d for n,d in zip(N,D)); discr=b*b-4*a*c
roots=[(-float(b)-math.sqrt(float(discr)))/(2*float(a)),(-float(b)+math.sqrt(float(discr)))/(2*float(a))]
# B0 and B1 for I=1/2, P(+1/2)=1: CG(1/2,1/2;1/2,-1/2|0,0)
# and CG(...|1,0) are both 1/sqrt(2), giving B0=B1=1.
helicity={str(k):sum(h**k for h in (-1,1)) for k in range(5)}
result={'figure':{'extracted_coefficients':{k:str(v) for k,v in variables.items()},'R_numerator':describe(N),'R_denominator':describe(D),'polarization_W':describe(W),'linear_analyser_plus':describe(add(W,H)),'linear_analyser_minus':describe(add(W,H,-1)),'delta_roots':roots,'polarizations':[ev(H,x)/ev(W,x) for x in roots],'clip_required_on_real_delta':not all(describe(q)['strictly_positive'] for q in (add(W,H),add(W,H,-1))),'boundary':'Positivity checks of freely chosen algebraic functions, not a nuclear-transition or detector calculation.'},'orientation':{'I':'1/2','P_plus':'1','P_minus':'0','CG_k0':'1/sqrt(2)','CG_k1':'1/sqrt(2)','B0':'1','B1':'1','helicity_sums_k0_to_k4':helicity,'boundary':'Helicity cancellation requires electromagnetic good-parity assumptions in Hamilton Eqs. 12.180–12.189; B1 remains nonzero.'},'inversion':{'cleared_equation_example':'(delta-1) - (1/2)*(delta^2-1) = -(delta-1)^2/2','crossed_root':'1','original_denominator_at_root':'0','conclusion':'delta=1 is excluded even though it is a double root after cross multiplication','projective_equation':'(n2-R*d2)u^2+(n1-R*d1)u*v+(n0-R*d0)v^2=0, delta=u/v','endpoint_condition':'v=0 is admissible if n2-R*d2=0 and d2 != 0; +infinity and -infinity are the same pure high-multipole direction','degenerate_examples':{'all_zero':'N=2D, R=2: all delta with D!=0 are solutions','constant_nonzero':'N=D+1, R=1: no finite solutions','linear':'coefficient of delta^2 vanishes but coefficient of delta does not: solve the linear equation and separately test the pure endpoint'}},'provenance':{'producer_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'calculation':'Python fractions.Fraction and math; no imported producer execution'}}
(P/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
