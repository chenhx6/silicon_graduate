#!/usr/bin/env python3
"""Conditional Pb207 13/2->5/2->1/2 Stokes; no experimental response fit."""
from __future__ import annotations
import argparse
from functools import lru_cache
import hashlib,json,math
from pathlib import Path
import numpy as np
from day16_co60_conditional_stokes import operators,stokes


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def amplitude(delta,theta,basis='native',dual=False):
    first=(('E' if dual else 'M',4,1.),('M' if dual else 'E',5,float(delta)))
    last=(('M' if dual else 'E',2,1.),)
    h1=operators(13,5,first,0.,0.,basis)
    h2=operators(5,1,last,float(theta),0.,basis)
    return np.einsum('bfj,aji->abfi',h2,h1)


def reduce(a,role):
    if role=='first':return np.einsum('abfi,cbfi->ac',a,a.conj())/14
    return np.einsum('abfi,acfi->bc',a,a.conj())/14


def calculate(delta,theta,basis='native',dual=False):
    a=amplitude(delta,theta,basis,dual)
    mat=a.reshape(4,-1)@a.reshape(4,-1).conj().T/14
    vals=np.linalg.eigvalsh(mat);tr=np.trace(mat).real
    assert vals.min()>-1e-12*tr
    r={role:stokes(reduce(a,role),(4*math.pi)**2) for role in ['first','last']}
    assert abs(r['first']['IQUV'][0]-r['last']['IQUV'][0])<1e-12
    return r


def closed_forms():
    # Independent exact Condon-Shortley CG and factorial d sum, no float helper.
    import sympy as s
    from sympy.physics.wigner import clebsch_gordan as cg
    d=s.symbols('d',real=True);x=s.symbols('x',real=True)
    @lru_cache(None)
    def exactd(j,mp,m,angle):
        c,t=s.cos(angle/2),s.sin(angle/2);f=s.factorial
        pref=s.sqrt(f(j+m)*f(j-m)*f(j+mp)*f(j-mp));out=0
        for k in range(2*j+1):
            z=(j+m-k,k,mp-m+k,j-mp-k)
            if min(z)>=0:out+=(-1)**(mp-m+k)*pref*c**(2*j+m-mp-2*k)*t**(mp-m+2*k)/math.prod(f(v) for v in z)
        return s.simplify(out)
    @lru_cache(None)
    def C(jf,mf,L,mu,ji,mi):return cg(s.Rational(jf,2),L,s.Rational(ji,2),s.Rational(mf,2),mu,s.Rational(mi,2))
    pts=[]
    for angle,cost in [(s.pi/2,0),(s.pi/3,s.Rational(1,2)),(0,1),(s.pi/6,s.sqrt(3)/2)]:
        # Scaled amplitudes (4pi)*T1*T2; normalization only (1+d²) afterwards.
        amps={}
        for a,h in enumerate([-1,1]):
            for b,k in enumerate([-1,1]):
                for mf in [-1,1]:
                    for mi in range(-13,14,2):
                        mj=mi-2*h
                        if abs(mj)>5:continue
                        mu=(mj-mf)//2
                        if abs(mu)>2:continue
                        t1=3*h*C(5,mj,4,h,13,mi)-d*s.sqrt(11)*C(5,mj,5,h,13,mi)
                        t2=s.sqrt(5)*C(1,mf,2,mu,5,mj)*exactd(2,mu,k,angle)
                        amps[a,b,mf,mi]=s.expand(t1*t2/2)
        def reduced(role):
            z=s.zeros(2)
            for h in range(2):
                for k in range(2):
                    for other in range(2):
                        for mf in [-1,1]:
                            for mi in range(-13,14,2):
                                i1=(h,other,mf,mi) if role=='first' else (other,h,mf,mi)
                                i2=(k,other,mf,mi) if role=='first' else (other,k,mf,mi)
                                z[h,k]+=amps.get(i1,0)*amps.get(i2,0)/14
            return s.factor(s.trace(z)/(1+d*d)),s.factor(-2*z[0,1]/(1+d*d))
        pts.append((cost,{role:reduced(role) for role in ['first','last']}))
    forms={}
    for role in ['first','last']:
        forms[role]={}
        for k,key in enumerate(['I','Q_plane']):
            poly=s.factor(s.interpolate([(t*t,v[role][k]) for t,v in pts[:3]],x*x))
            assert s.simplify(poly.subs(x,pts[3][0])-pts[3][1][role][k])==0
            forms[role][key]=poly
        forms[role]['P_plane']=s.factor(forms[role]['Q_plane']/forms[role]['I'])
    return d,x,forms


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--contract',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();c=json.loads(a.contract.read_text());assert c['identity']=='PB207-CONDITIONAL-STOKES-01'
    for path,h in c['dependencies_sha256'].items():assert sha(path)==h,path
    for path,h in c['source_hashes'].items():assert sha(path)==h,path
    rows=[];errors=[];controls=[]
    for delta in c['delta_native_design_values']:
        for angle in c['theta_deg']:
            theta=math.radians(angle);r=calculate(delta,theta);rb=calculate(-delta,theta,'RB');dual=calculate(delta,theta,dual=True)
            for role in ['first','last']:
                v=np.array(r[role]['IQUV']);errors.append(float(max(abs(v-np.array(rb[role]['IQUV'])))));w=np.array(dual[role]['IQUV']);errors.append(float(max(abs(w-v*np.array([1,-1,-1,1])))))
                assert abs(v[2])+abs(v[3])<1e-12
                rows.append({'delta_native':delta,'theta_deg':angle,'role':role,**r[role]})
    assert max(errors)<1e-11
    d,x,forms=closed_forms();lambdas={role:{k:__import__('sympy').lambdify((x,d),v,'numpy') for k,v in fs.items()} for role,fs in forms.items()};exact_err=[]
    for row in rows:
        xx=math.cos(math.radians(row['theta_deg']));role=row['role'];delta=row['delta_native']
        exact_err += [abs(float(lambdas[role]['I'](xx,delta))-row['IQUV'][0]),abs(float(lambdas[role]['Q_plane'](xx,delta))-row['IQUV'][1])]
    assert max(exact_err)<1e-11
    import sympy as s
    rankforms={}
    for role,fs in forms.items():
        assert s.simplify(s.integrate(fs['I'],(x,-1,1))/2-1)==0
        rankforms[role]={str(k):str(s.factor((2*k+1)*s.integrate(fs['I']*s.legendre(k,x),(x,-1,1))/2)) for k in [0,2,4]}
    # Finite relative-angle interval is a stated design acceptance only.
    finite=[]
    lo,hi=sorted(math.cos(math.radians(z)) for z in c['uniform_cos_design_interval_deg'])
    for delta in c['delta_native_design_values']:
        for role in ['first','last']:
            ff=lambdas[role];n,w=np.polynomial.legendre.leggauss(24);xx=lo+(n+1)*(hi-lo)/2
            intensity=ff['I'](xx,delta);numerator=ff['Q_plane'](xx,delta);mean=float(np.sum(w*numerator)/np.sum(w*intensity));grid=np.linspace(lo,hi,5001);pv=ff['P_plane'](grid,delta)
            roots=s.solve(s.together(s.diff(forms[role]['P_plane'],x)).as_numer_denom()[0].subs(d,s.Rational(str(delta))),x)
            critical=[lo,hi]+[float(s.re(z)) for z in roots if abs(float(s.im(z)))<1e-10 and lo<float(s.re(z))<hi]
            vals=[float(ff['P_plane'](z,delta)) for z in critical]
            finite.append({'delta_native':delta,'role':role,'uniform_cos_design_P':mean,'angle_interval_extrema_P':[min(vals),max(vals)],'stationary_and_endpoint_cosines':critical,'grid_vs_analytic_extrema_error':max(abs(min(vals)-min(pv)),abs(max(vals)-max(pv)))})
    # Common-axis gate integral: rotate event-plane Q by azimuth; not scalar mean.
    full=[]
    for role in ['first','last']:
        I=s.integrate(forms[role]['I'],(x,-1,1))/2
        qlocal=s.factor(s.integrate(forms[role]['Q_plane'],(x,-1,1))/2)
        full.append({'role':role,'fullgate_I':str(I),'local_event_plane_Q_integral':str(qlocal),'common_axes_Q_U_integral':[0.,0.],'reason':'uniform azimuth integral of cos2phi/sin2phi vanishes; local eventplane scalar is a distinct observable'})
    result={'identity':c['identity'],'script_sha256':sha(__file__),'contract_sha256':sha(a.contract),'exact_formulas':{role:{k:str(v) for k,v in fs.items()} for role,fs in forms.items()},'W_Legendre_coefficients':rankforms,'rows':rows,'native_RB_and_EMduality_max_error':max(errors),'exact_vs_numeric_max_error':max(exact_err),'finite_angle_design':finite,'ungated_common_axes_control':full,'scope':c['assumptions'],'experimental_Q_P_or_CI':False,'ok':True}
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['rows','scope']},ensure_ascii=False,indent=2))
    return 0
if __name__=='__main__':raise SystemExit(main())
