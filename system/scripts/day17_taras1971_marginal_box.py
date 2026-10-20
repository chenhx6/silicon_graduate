#!/usr/bin/env python3
"""Exact open-cell AD marginal-box/positive-population projection for T71."""
from datetime import datetime, timezone
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp
from sympy.physics.wigner import clebsch_gordan as cg
from day17_taras1971_table5_audit import zvalue

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'
U=sp.Symbol('u',real=True)
QA=[(7,-2,3),(14,-1,-9),(14,5,3)]


class RootField:
    """QQ[u]/f with the real embedding fixed by an isolating interval."""
    def __init__(self,modulus,lo,hi):
        self.modulus,self.lo,self.hi=modulus,lo,hi
        self.signs={}

    def element(self,value):
        if isinstance(value,Element):
            assert value.field is self
            return value
        return Element(self,sp.Poly(value,U,domain=sp.QQ).rem(self.modulus))

    def sign(self,poly):
        if poly.is_zero:
            return 0
        key=tuple(poly.all_coeffs())
        if key in self.signs:
            return self.signs[key]
        for _ in range(12):
            low=high=sp.S.Zero
            for coeff in poly.all_coeffs():
                values=[low*self.lo,low*self.hi,high*self.lo,high*self.hi]
                low,high=min(values)+coeff,max(values)+coeff
            if low>0 or high<0:
                result=1 if low>0 else -1;self.signs[key]=result
                return result
            assert self.lo!=self.hi
            self.lo,self.hi=self.modulus.refine_root(self.lo,self.hi,eps=(self.hi-self.lo)/1000)
        raise AssertionError('Could not certify a nonzero algebraic sign')


class Element:
    def __init__(self,field,poly):
        self.field,self.poly=field,poly

    def __add__(self,other):
        other=self.field.element(other)
        return Element(self.field,(self.poly+other.poly).rem(self.field.modulus))
    __radd__=__add__

    def __neg__(self):
        return Element(self.field,-self.poly)

    def __sub__(self,other):
        return self+-self.field.element(other)

    def __rsub__(self,other):
        return self.field.element(other)+-self

    def __mul__(self,other):
        other=self.field.element(other)
        return Element(self.field,(self.poly*other.poly).rem(self.field.modulus))
    __rmul__=__mul__

    def __truediv__(self,other):
        other=self.field.element(other)
        assert not other.poly.is_zero
        inv=sp.invert(other.poly,self.field.modulus)
        return Element(self.field,(self.poly*inv).rem(self.field.modulus))

    def __rtruediv__(self,other):
        return self.field.element(other)/self

    def __bool__(self):
        return not self.poly.is_zero

    def __eq__(self,other):
        return (self-self.field.element(other)).poly.is_zero

    def __hash__(self):
        return hash((id(self.field),tuple(self.poly.all_coeffs())))

    def __ge__(self,other):
        return self.field.sign((self-other).poly)>=0

    def __gt__(self,other):
        return self.field.sign((self-other).poly)>0

    def __le__(self,other):
        return self.field.sign((self-other).poly)<=0

    def __lt__(self,other):
        return self.field.sign((self-other).poly)<0

    def __str__(self):
        return str(self.poly.as_expr())


def evaluate_field(expr,field):
    num,den=sp.fraction(sp.cancel(expr))
    root=field.element(U)
    def horner(poly):
        out=field.element(0)
        for coeff in sp.Poly(poly,U,domain=sp.QQ).all_coeffs():
            out=out*root+field.element(coeff)
        return out
    return horner(num)/horner(den)


def clip(poly,rule):
    const,ca,cb=rule
    value=lambda p:const+ca*p[0]+cb*p[1]
    result=[]
    if not poly:
        return result
    for start,end in zip(poly,poly[1:]+poly[:1]):
        vs,ve=value(start),value(end)
        if vs>=0:
            result.append(start)
        if (vs<0 and ve>=0) or (vs>=0 and ve<0):
            t=vs/(vs-ve)
            result.append(tuple(s+t*(e-s) for s,e in zip(start,end)))
    return list(dict.fromkeys(result))


def main():
    path=RUN/'taras1971-box-contract.json';c=json.loads(path.read_text())
    a=sp.Rational(c['a2_central']);sa=sp.Rational(c['a2_sigma'])
    b=sp.Rational(c['a4_central']);sb=sp.Rational(c['a4_sigma'])
    abox=[a-sa,a+sa];bbox=[b-sb,b+sb]
    c2=sp.sympify(c['c2'],locals={'u':U});c4=sp.sympify(c['c4'],locals={'u':U})
    norm=1+U**2/35;ji=sp.Rational(5,2)
    delta=U/sp.sqrt(35)
    f2=zvalue(5,3,1,1,2)-2*delta*zvalue(5,3,1,2,2)+delta**2*zvalue(5,3,2,2,2)
    for m,va,vb in zip([sp.Rational(1,2),sp.Rational(3,2),sp.Rational(5,2)],c['population_A_weights'],c['population_B_weights']):
        p2=(-1)**(ji-m)*cg(ji,ji,2,m,-m,0)
        p4=(-1)**(ji-m)*cg(ji,ji,4,m,-m,0)
        assert sp.simplify(p2*f2/norm-va*c2)==0
        assert sp.simplify(-p4*delta**2*zvalue(5,3,2,2,4)/norm-vb*c4)==0
    expressions=[c2,c4]
    for av,bv in itertools.product(abox,bbox):
        aa,bb=av/c2,bv/c4
        expressions.extend(const+ca*aa+cb*bb for const,ca,cb in QA)
    for va,vb in zip(c['population_A_weights'],c['population_B_weights']):
        expressions.extend(va*c2-x for x in abox)
        expressions.extend(vb*c4-x for x in bbox)
    factors={}
    for expr in expressions:
        numerator=sp.fraction(sp.cancel(expr))[0]
        if not numerator.has(U):
            continue
        poly=sp.Poly(numerator,U,domain=sp.QQ)
        for fac,_ in sp.factor_list(poly)[1]:
            fac=fac.monic();factors[tuple(fac.all_coeffs())]=fac
    eps=sp.Rational(c['isolation_eps'])
    for attempt in range(4):
        roots=[]
        for fac in factors.values():
            for interval,multiplicity in fac.intervals(eps=eps):
                lo,hi=interval
                roots.append({'lo':lo,'hi':hi,'poly':str(fac.as_expr()),'multiplicity':multiplicity})
        roots.sort(key=lambda x:(x['lo']+x['hi'])/2)
        if all(x['hi']<y['lo'] for x,y in zip(roots,roots[1:])):
            break
        eps/=1000
    else:
        raise AssertionError('Distinct irreducible root isolations still overlap')
    def feasible(u):
        s2,s4=c2.subs(U,u),c4.subs(U,u)
        if not s2 or not s4:
            return []
        al,ah=sorted(x/s2 for x in abox);bl,bh=sorted(x/s4 for x in bbox)
        polygon=[(al,bl),(ah,bl),(ah,bh),(al,bh)]
        for rule in QA:
            polygon=clip(polygon,rule)
        return polygon
    cells=[]
    for index in range(len(roots)+1):
        left=roots[index-1] if index else None
        right=roots[index] if index<len(roots) else None
        u=(min(right['lo']-1,2*right['lo']) if left is None else
           max(left['hi']+1,2*left['hi']) if right is None else
           (left['hi']+right['lo'])/2)
        polygon=feasible(u);entry={'cell':index,'feasible':bool(polygon)}
        if polygon:
            aa=sum(p[0] for p in polygon)/len(polygon)
            bb=sum(p[1] for p in polygon)/len(polygon)
            q=[(7+3*bb-2*aa)/21,(14-9*bb-aa)/42,(14+3*bb+5*aa)/42]
            a2,a4=sp.cancel(c2.subs(U,u)*aa),sp.cancel(c4.subs(U,u)*bb)
            assert min(q)>=0 and sum(q)==1
            assert abox[0]<=a2<=abox[1] and bbox[0]<=a4<=bbox[1]
            entry['exact_witness']={'u':str(u),'folded_q':list(map(str,q)),'a2':str(a2),'a4':str(a4)}
        cells.append(entry)
    bands=[];index=0
    while index<len(cells):
        if not cells[index]['feasible']:
            index+=1;continue
        first=index
        while index+1<len(cells) and cells[index+1]['feasible']:
            index+=1
        last=index
        def boundary(k):
            return float((roots[k]['lo']+roots[k]['hi'])/(2*sp.sqrt(35)))
        bands.append({'first_open_cell':first,'last_open_cell':last,
                      'delta_bounds_approx':[None if first==0 else boundary(first-1),None if last==len(roots) else boundary(last)],
                      'finite_endpoints_feasible_by_compactness':True})
        index+=1
    unresolved=[i for i in range(len(roots)) if not cells[i]['feasible'] and not cells[i+1]['feasible']]
    boundary_checks=[]
    lookup={str(fac.as_expr()):fac for fac in factors.values()}
    for i in unresolved:
        root=roots[i];field=RootField(lookup[root['poly']],root['lo'],root['hi'])
        s2,s4=evaluate_field(c2,field),evaluate_field(c4,field)
        polygon=[]
        if s2 and s4:
            al,ah=sorted(field.element(x)/s2 for x in abox)
            bl,bh=sorted(field.element(x)/s4 for x in bbox)
            polygon=[(al,bl),(ah,bl),(ah,bh),(al,bh)]
            for rule in QA:
                polygon=clip(polygon,rule)
        entry={'critical_root':i,'feasible':bool(polygon),'exact_algebraic_field_signs':True}
        if polygon:
            aa=sum(p[0] for p in polygon)/len(polygon);bb=sum(p[1] for p in polygon)/len(polygon)
            q=[(7+3*bb-2*aa)/21,(14-9*bb-aa)/42,(14+3*bb+5*aa)/42]
            assert min(q)>=0 and sum(q)==1
            entry['isolated_point_folded_q_in_root_field']=list(map(str,q))
        boundary_checks.append(entry)
    al,ah=sorted(x/sp.Rational(-5,98) for x in abox)
    bl,bh=sorted(x/sp.Rational(16,49) for x in bbox)
    infinity_polygon=[(al,bl),(ah,bl),(ah,bh),(al,bh)]
    for rule in QA:
        infinity_polygon=clip(infinity_polygon,rule)
    m2_values=[(1-2*aa-bb/4)/(1+aa+bb) for aa,bb in itertools.product(abox,bbox)]
    pbox=[sp.Rational(c['p_central'])-sp.Rational(c['p_sigma']),sp.Rational(c['p_central'])+sp.Rational(c['p_sigma'])]
    assert max(m2_values)<pbox[0]
    result={'at':datetime.now(timezone.utc).isoformat(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'shared_Z_helper_sha256':hashlib.sha256((ROOT/'system/scripts/day17_taras1971_table5_audit.py').read_bytes()).hexdigest(),
        'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'critical_irreducible_factors':len(factors),'isolation_epsilon':str(eps),
        'critical_root_isolations':[{'lo':str(x['lo']),'hi':str(x['hi']),'poly':x['poly']} for x in roots],
        'open_cells':cells,'closures_of_feasible_open_bands':bands,
        'other_critical_points_exact_field_classification':boundary_checks,
        'projective_infinity_feasible_exact':bool(infinity_polygon),
        'literal_pure_M2_p_range_over_AD_marginal_box':list(map(str,[min(m2_values),max(m2_values)])),
        'printed_p_marginal_box':list(map(str,pbox)),
        'exact_source_response_and_open_cell_witnesses':True,
        'literal_pure_M2_outside_declared_p_box':True,
        'no_jointCI_or_original_recipe_attribution':True,
        'all_closed_projection_points_classified':True,'ok':True}
    (RUN/'taras1971-box-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'critical_factors':len(factors),'roots':len(roots),'bands':bands,
                     'other_boundary_points_exactly_checked':len(boundary_checks),
                     'isolated_boundary_points_found':sum(x['feasible'] for x in boundary_checks),
                     'projective_infinity_feasible':bool(infinity_polygon),
                     'pure_M2_p_range':list(map(float,[min(m2_values),max(m2_values)])),
                     'p_box':list(map(float,pbox))},indent=2))


if __name__=='__main__':
    main()
