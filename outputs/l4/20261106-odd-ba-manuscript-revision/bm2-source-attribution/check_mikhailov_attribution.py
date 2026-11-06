"""Exact algebra check of the attribution correction, not a nuclear model run."""
from fractions import Fraction as F
import json
import math
from pathlib import Path
import time

OUT = Path(__file__).resolve().parent


def cg_squared(j1, m1, j2, m2, J, M):
    assert m1+m2 == M
    tri = (J+j1-j2, J-j1+j2, j1+j2-J)
    assert all(v >= 0 for v in tri)
    f = math.factorial
    pref = F((2*J+1)*math.prod(f(v) for v in tri), f(j1+j2+J+1))
    pref *= math.prod(f(v) for v in (J+M,J-M,j1-m1,j1+m1,j2-m2,j2+m2))
    series = F(0)
    for k in range(j1+j2+J+1):
        args=(k,j1+j2-J-k,j1-m1-k,j2+m2-k,J-j2+m1+k,J-j1-m2+k)
        if min(args) >= 0:
            series += F((-1)**k, math.prod(f(v) for v in args))
    return pref*series**2


def main():
    start=time.perf_counter()
    c0=cg_squared(2,2,2,-2,0,0)
    c2=cg_squared(2,2,2,-2,2,0)
    assert c0==F(1,5) and c2==F(2,7)
    ratio0=c0/c2
    assert ratio0==F(7,10)
    cases=[]
    for a in [F(0),F(1,1000),F(-1,1000),F(1,100),F(-1,100),F(1,20)]:
        z=2*a/(1-4*a)
        direct=c0*(1+a*(0-6))**2/(c2*(1+a*(6-6))**2)
        in_a=F(7,10)*(1-6*a)**2
        in_z=F(7,10)*((1-z)/(1+2*z))**2
        assert direct==in_a==in_z
        cases.append(dict(a2=str(a),z2=str(z),ratio=str(direct)))
    a=F(1,100);z=2*a/(1-4*a)
    original_expression_with_book_z=F(7,10)*((1-2*z)/(1+z))**2
    correct=F(7,10)*(1-6*a)**2
    assert original_expression_with_book_z!=correct
    result={
        "scope":"Book Eq4-230 and4-231 parameter dictionary, exact CG algebra only; no isotope or fit.",
        "source_locators":"Physical PDF181 / printed159, Eqs4-230–4-231; epsilon2/h2 dictionary separately checked on PDF183.",
        "CG_squared_2K2_to_0K0":str(c0),
        "CG_squared_2K2_to_2K0":str(c2),
        "zero_correction_ratio":str(ratio0),
        "identity":"R=(7/10)*(1-6*a2)^2=(7/10)*((1-z2)/(1+2*z2))^2; z2=2*a2/(1-4*a2)",
        "exact_cases":cases,
        "old_expression_comparison":{
            "condition":"Identify old z symbol with the book's z2; other parameterizations require an explicit separately verified dictionary.",
            "a2":str(a),"z2":str(z),
            "correct":str(correct),
            "old_expression":str(original_expression_with_book_z),
            "equal":False,
        },
        "boundary":"The ratio is an audit derivation from the book's effective-strength relation, not a newly located printed equation or experimental universal reduction.",
        "runtime_seconds":time.perf_counter()-start,
        "passed":True,
    }
    with (OUT/"mikhailov-algebra-check.json").open("x",encoding="utf-8") as f:
        json.dump(result,f,ensure_ascii=False,indent=2);f.write("\n")
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
