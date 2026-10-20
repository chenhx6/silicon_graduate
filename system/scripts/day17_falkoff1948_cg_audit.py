#!/usr/bin/env python3
"""Independent sparse CG cascade audit of FA48, no historical producer import."""
from datetime import datetime, timezone
from functools import lru_cache
import hashlib
import json
from pathlib import Path

import sympy as sp
from sympy.physics.wigner import clebsch_gordan

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


@lru_cache(None)
def axes(ji, jf, ell, back=False, magnetic=False):
    helicities={}
    for h in [-1,1]:
        mu=-h if back else h
        values={}
        for mf in range(-jf,jf+1):
            mi=mf+mu
            if abs(mi)<=ji:
                value=clebsch_gordan(jf,ell,ji,mf,mu,mi)
                if back:
                    value*=(-1)**(ell+h)
                if magnetic:
                    value*=h
                if value:
                    values[(mf+jf,mi+ji)]=value
        helicities[h]=sp.SparseMatrix(2*jf+1,2*ji+1,values)
    x=(-helicities[1]+helicities[-1])/sp.sqrt(2)
    y=-sp.I*(helicities[1]+helicities[-1])/sp.sqrt(2)
    # Local e_theta at theta=pi is -global x; e_phi stays global y.
    return (-x if back else x), y


def rate(op, ji):
    return sp.simplify(sum(sp.expand_complex(z*sp.conjugate(z)) for z in op.values())/(2*ji+1))


def cascade(ji, j, jf, l1, l2, magnetic_second=False):
    x1,y1=axes(ji,j,l1)
    x2,y2=axes(j,jf,l2,True,magnetic_second)
    four=[rate(b*a,ji) for a in [x1,y1] for b in [x2,y2]]
    assert four[0]==four[3] and four[1]==four[2]
    assert sum(four)>0
    corr=sp.simplify((four[0]-four[1])/(four[0]+four[1]))
    scale=sp.simplify((four[0]+four[1])/2)
    for phi in [sp.pi/6,sp.pi/4,sp.pi/3]:
        actual=rate((sp.cos(phi)*x2+sp.sin(phi)*y2)*x1,ji)
        assert sp.simplify(actual-scale*(1+corr*sp.cos(2*phi)))==0
    return corr, four


def main():
    path=RUN/'falkoff1948-CG-contract.json'
    contract=json.loads(path.read_text())
    jvar=sp.Symbol('J'); rows=[]
    for j in contract['dipole_J_test']:
        for ri,dj in enumerate([-1,0,1]):
            for ci,dJ in enumerate([-1,0,1]):
                ji,jf=j-dj,j+dJ
                corr,four=cascade(ji,j,jf,1,1)
                expected=sp.sympify(contract['A_abs_formulas'][ri][ci],locals={'J':jvar}).subs(jvar,j)
                assert abs(corr)==expected,(j,dj,dJ,corr,expected)
                sign=(-1)**(1+1+ji-jf+1+1)
                assert sp.sign(corr)==sign
                mixed,_=cascade(ji,j,jf,1,1,True)
                assert mixed==-corr
                rows.append({'J':j,'delta_j':dj,'Delta_J':dJ,'Ji':ji,'Jf':jf,
                             'A':str(corr),'Table_abs':str(expected),'four':list(map(str,four))})
    quad=[]
    for j in contract['quadrupole_stretched_J_test']:
        corr,four=cascade(j+2,j,j-2,2,2)
        mixed,_=cascade(j+2,j,j-2,2,2,True)
        assert corr==sp.Rational(2,7) and mixed==-corr
        quad.append({'Ji':j+2,'J':j,'Jf':j-2,'sameEM_A':str(corr),
                     'oppositeEM_A':str(mixed),'four':list(map(str,four))})
    a=sp.Rational(2,7); b=sp.simplify(2*a/(1-a)); phi=sp.Symbol('phi',real=True)
    assert sp.trigsimp(1+a*sp.cos(2*phi)-(1-a)*(1+b*sp.cos(phi)**2))==0
    result={
        'at':datetime.now(timezone.utc).isoformat(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'dipole_Table1_checks':rows,'quadrupole_stretched_checks':quad,
        'harmonic_ratio':str((1+a)/(1-a)),
        'wrong_same_A_cos_squared_ratio':str(1+a),
        'equivalent_cos_squared_b':str(b),
        'CG_and_source_Table1_Eq3_and_harmonic_controls':True,
        'common_axis_unoriented_P1_P2_zero_PP1_equals_A':True,
        'source_Wiki_transcription_revision_not_official_erratum':True,
        'no_modern_Co60_M3_or_array_Q_or_experimental_data_reestimated':True,
        'ok':True,
    }
    (RUN/'falkoff1948-CG-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print('exact dipole rows',len(rows),'quad rows',len(quad),'ratio',result['harmonic_ratio'],'OK')


if __name__=='__main__':
    main()
