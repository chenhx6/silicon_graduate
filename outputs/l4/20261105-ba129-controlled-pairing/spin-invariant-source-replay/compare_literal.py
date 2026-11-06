"""Compare frozen source geometry with the declared case's literal Eqs12-15.

No Hamiltonian/charge/chi fit, no operator replacement, no finite-J closure
derivation. The complete-scalar numbers are retained as parent diagnostics.
Only the literal J'=J+2 calculation is independently replayed here.
"""

from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import sys
import time

import numpy as np

ROOT = Path("/workspace/wiki")
OUT = ROOT/"outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-source-replay"
SOURCE = OUT/"source-invariants-frozen.json"
PROBE = ROOT/"outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-probe/probe-v1.json"
CASE = ROOT/"outputs/l4/20261105-ba129-controlled-pairing/ibfm-case-v1/prediction.json"

sys.path.insert(0,str(ROOT/"system/scripts/analysis"))
from single_j_ibfm import IBFMParameters, CoreParameters, IBFMKernel, BosonCore
from paired_single_j_em import clebsch_gordan as cg


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def restricted_vector(solution, operator, index, n):
    """RME vector only; component tensors need not define a real cubic angle."""
    tj = int(solution.two_J[index])
    tm = int(solution.basis.two_M)
    tjp = tj+4
    intermediate = solution.indices_for_J(tjp)[:n]
    factor = cg(tj,tm,4,0,tjp,tm)/math.sqrt(tjp+1)
    assert factor != 0
    return (
        solution.vectors[:,intermediate].conj().T
        @ (operator.block(solution.basis) @ solution.vectors[:,index])
    )/factor


def literal(solution, operator, index, n):
    """Direct q=0 RMEs and the coherent restricted chain in printed Eq.13."""
    tj = int(solution.two_J[index])
    tm = int(solution.basis.two_M)
    tjp = tj+4
    intermediate = solution.indices_for_J(tjp)
    if n is not None:
        intermediate = intermediate[:n]
    block = operator.block(solution.basis)
    vi = solution.vectors[:,index]
    vp = solution.vectors[:,intermediate]
    up_factor = cg(tj,tm,4,0,tjp,tm)/math.sqrt(tjp+1)
    middle_factor = cg(tjp,tm,4,0,tjp,tm)/math.sqrt(tjp+1)
    assert up_factor != 0 and middle_factor != 0
    u = (vp.conj().T @ (block @ vi))/up_factor
    middle = (vp.conj().T @ (block @ vp))/middle_factor
    q2 = float(np.vdot(u,u).real)
    chain = complex(np.vdot(u,middle @ u))
    assert abs(chain.imag)<1e-10
    q3 = math.sqrt(7/10)*abs(chain)
    argument = q3/q2**1.5
    assert 0 <= argument <= 1
    band_cg = cg(tjp,tj,4,0,tj,tj)
    G = 1/((tjp+1)*band_cg**2)
    beta_no_radius = math.sqrt(G*q2)
    return dict(two_J=tj,two_Jprime=tjp,states_used=len(intermediate),
                q2=q2,q3_abs=q3,coherent_chain_real=chain.real,
                gamma_argument=argument,gamma_deg=math.degrees(math.acos(argument))/3,
                G_J=G,beta_without_radius_prefactor_eb=beta_no_radius),u


def beta_from_eb_scale(value,A,Z=56):
    # Strip the elementary charge unit; 1 b = 100 fm^2. Eq.14 has R0 in fm.
    return 4*math.pi/(3*Z*(1.2*A**(1/3))**2)*100*value


def main():
    start=time.perf_counter()
    locked={
        SOURCE:"4987fa80589b6a278edba95865665d4f7ec5bf742eb1feaeec46eb2f7d6aaf5b",
        PROBE:"9bc03128820d05f6f98f09fc170b077fa32ae3da777ad82760623891026fd0a3",
        CASE:"6dd5371fcaa7d2647e60490d15ca7e2816a1a517756af59515923167f6d1a2a4",
    }
    source=json.loads(SOURCE.read_text())
    probe=json.loads(PROBE.read_text())
    case=json.loads(CASE.read_text())
    locked.update({ROOT/k:v for k,v in probe["input_sha256"].items()})
    for path,h in locked.items():assert sha(path)==h,str(path)
    p=IBFMParameters(**case["parameters"])
    assert p.n_b==8 and p.chi==-.18 and p.v2==.453
    eB,eF,chiE=(case["core_calibration"][k] for k in ["eB","eF_eb","chi_E2"])
    assert eF==.125 and chiE==.35
    core=BosonCore(CoreParameters(p.n_b,p.eps_d,p.kappa,p.chi)); cs=core.solve()
    odd=IBFMKernel(p); os=odd.solve()
    ci=int(cs.indices_for_J(0)[0]);oi=int(os.indices_for_J(11)[0])
    cr,cu=literal(cs,core.e2(eB,chiE),ci,5)
    or_,ou=literal(os,odd.e2(eB,eF,chiE),oi,5)
    ca,_=literal(cs,core.e2(eB,chiE),ci,None)
    for new,old in [(cr,probe["core_128_J0"]["restricted_prescriptions"][1]),
                    (or_,probe["odd_129_J11half"]["restricted_prescriptions"][1])]:
        assert abs(new["q2"]-old["q2_raw_restricted"])<1e-10
        assert abs(new["q3_abs"]-old["q3_raw_restricted_abs"])<1e-10
        assert abs(new["gamma_deg"]-old["gamma_proxy_deg"])<1e-10
        assert abs(new["beta_without_radius_prefactor_eb"]-old["beta_proxy_without_radius_prefactor"])<1e-11
    core_beta=beta_from_eb_scale(cr["beta_without_radius_prefactor_eb"],128)
    odd_beta=beta_from_eb_scale(or_["beta_without_radius_prefactor_eb"],129)
    graphs={}
    for panel in source["panels"]:
        for point in panel["points"]:
            graphs[(point["isotope"],panel["quantity"])]=point["value"]
    comparison=[]
    for isotope,key,result,beta in [
        ("128Ba","core_128_J0",cr,core_beta),
        ("129Ba","odd_129_J11half",or_,odd_beta),
    ]:
        sg=graphs[(isotope,"gamma")];sb=graphs[(isotope,"beta")]
        comparison.append(dict(
            isotope=isotope,two_J=result["two_J"],
            source_beta=sb,source_gamma_deg=sg,
            literal_beta=beta,literal_gamma_deg=result["gamma_deg"],
            literal_beta_minus_source=beta-sb,literal_gamma_minus_source_deg=result["gamma_deg"]-sg,
            full_scalar_gamma_folded_parent_deg=probe[key]["full_moments"]["gamma_folded_deg"],
            literal_gamma_argument=result["gamma_argument"],
            source_gamma_argument_if_Eq15_applies=math.cos(3*math.radians(sg)),
        ))
    # Fixed-operator amplitude decomposition, not a variation or fitting of eB/eF.
    uB=restricted_vector(os,odd.core_quadrupole(chiE),oi,5)
    ut=restricted_vector(os,odd.fermion_unit_tensor(2),oi,5)
    uF=-(1-2*p.v2)*p.Q_jj/math.sqrt(5)*ut
    C_B=float(np.vdot(uB,uB).real)
    C_X=float(np.vdot(uB,uF).real)
    C_F=float(np.vdot(uF,uF).real)
    q2_b=eB**2*C_B;q2_cross=2*eB*eF*C_X;q2_f=eF**2*C_F
    assert abs(q2_b+q2_cross+q2_f-or_["q2"])<1e-10
    # Parent's already-computed alternatives are only reported diagnostics.
    candidates_path=PROBE.parent/"operator-candidates.json"
    phase_path=PROBE.parent/"phase-placement-probe.json"
    locked[candidates_path]=sha(candidates_path);locked[phase_path]=sha(phase_path)
    candidates=json.loads(candidates_path.read_text())
    phase=json.loads(phase_path.read_text())
    result={
        "review_date_declared":"2026-11-06",
        "container_observed_utc":datetime.now(timezone.utc).isoformat(),
        "source_freeze_sha256":sha(SOURCE),
        "scope":"Literal source-prescription replay only. Same fixed kernel/case; no finite-J closure derivation and no parameter/charge/chi changes.",
        "source_comparison":comparison,
        "literal_core_n5":cr,"literal_odd_n5":or_,"literal_core_all_J2_states":ca,
        "core_n5_to_all_gamma_change_deg":ca["gamma_deg"]-cr["gamma_deg"],
        "case_operator":{"eB_eb":eB,"eF_eb":eF,"eF_over_eB":eF/eB,"chi_E2":chiE,"chi_H":p.chi},
        "beta_units":"E2 RMEs in eb; divide out elementary charge and use 1 b=100 fm^2 with R0=1.2 A^(1/3) fm. This is the declared physical-E2 reading, not a certified author Q dictionary.",
        "beta_ratio":{
            "source_odd_over_core":graphs[("129Ba","beta")]/graphs[("128Ba","beta")],
            "declared_literal_odd_over_core":odd_beta/core_beta,
            "relative_difference":(odd_beta/core_beta)/(graphs[("129Ba","beta")]/graphs[("128Ba","beta")])-1,
            "boundary":"Not exactly charge-free for fixed nonzero eF: the ratio depends on eF/eB even when the two boson charges are assumed common.",
        },
        "odd_restricted_quadratic_charge_decomposition":{
            "C_B":C_B,"C_X":C_X,"C_F":C_F,
            "formula":"q2_odd=eB^2*C_B+2*eB*eF*C_X+eF^2*C_F",
            "boson_term":q2_b,"interference_term":q2_cross,"fermion_square_term":q2_f,
            "total":or_["q2"],"net_nonboson_fraction":(q2_cross+q2_f)/or_["q2"],
            "boundary":"At the frozen case only; no charge scan or charge adjustment.",
        },
        "parent_operator_candidates_attributed_only":candidates,
        "parent_phase_placement_scope":phase["scope"],
        "parent_chi_plus035_sum_abs_argument":next(x for x in phase["rows"] if x["chi"]==.35)["sum_abs_terms_argument"],
        "files_unchanged":{str(path.relative_to(ROOT)):h for path,h in locked.items()},
        "runtime_seconds":time.perf_counter()-start,
    }
    for path,h in locked.items():assert sha(path)==h,str(path)
    payload=json.dumps(result,indent=2,allow_nan=False)+"\n"
    with (OUT/"literal-comparison.json").open("x",encoding="utf-8") as f:f.write(payload)
    print(json.dumps(result["source_comparison"],indent=2))
    print("BETA RATIO",result["beta_ratio"])
    print("CHARGE DECOMPOSITION",result["odd_restricted_quadratic_charge_decomposition"])
    print("CORE n5 -> all",result["core_n5_to_all_gamma_change_deg"])
    print("RUNTIME",result["runtime_seconds"])


if __name__=="__main__":
    main()
