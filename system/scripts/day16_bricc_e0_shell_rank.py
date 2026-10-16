#!/usr/bin/env python3
"""Audit the one captured E0 query and a conditional K/L1 inversion rank."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

from bs4 import BeautifulSoup
import numpy as np


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",type=Path,required=True)
    p.add_argument("--receipt",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args();cfg=json.loads(args.input.read_text());rec=json.loads(args.receipt.read_text())
    assert hashlib.sha256(args.input.read_bytes()).hexdigest()==rec["input_sha256"]
    assert rec["POST_count"]==1 and rec["automatic_retries"]==0 and rec["http_status"]==200
    path=Path(rec["response"]);data=path.read_bytes();assert hashlib.sha256(data).hexdigest()==rec["sha256"]
    soup=BeautifulSoup(data,"html.parser");table=soup.find("table")
    rows=[[td.get_text(" ",strip=True) for td in row.find_all(["td","th"],recursive=False)]
          for row in table.find_all("tr",recursive=False)]
    flat=" ".join(" ".join(x) for x in rows)
    assert all(x in flat for x in ["BrIccS v2.3 (9-Dec-2011)","Z=70","489.8","BeOmg","Ω(E0)"])
    assert "ICC could not be calculated" not in flat
    start=next(i for i,x in enumerate(rows) if x[:2]==["Shell","E(ce)"])
    omega={x[0]:{"printed":x[2],"value":float(x[2]),"Ece_printed_keV":x[1] or None,
                 "units":"s^-1" if "/" not in x[0] else "dimensionless"}
           for x in rows[start+1:] if len(x)>=3 and x[0] and x[2]}
    assert {"K","L1","L2","Tot","K/Tot"}==set(omega)
    subtotal=sum(omega[x]["value"] for x in ["K","L1","L2"])
    assert abs(subtotal-omega["Tot"]["value"])<5e6
    snapshot=Path(cfg["existing_M1_E2_snapshot"])
    assert hashlib.sha256(snapshot.read_bytes()).hexdigest()==cfg["existing_M1_E2_sha256"]
    modes={x["multipolarity"]:x["coefficients"] for x in json.loads(snapshot.read_text())["model_inputs"]}
    shells=cfg["analysis_if_success"]["shells"]
    e=np.array([modes["E2"][s]["value"] for s in shells])
    m=np.array([modes["M1"][s]["value"] for s in shells])
    om=np.array([omega[s]["value"] for s in shells])
    g=m-e
    # z=OmegaK*x removes units of x; column normalization separately checks geometry.
    A=np.column_stack((g,om/om[0]))
    normalized=A/np.linalg.norm(A,axis=0)
    sine=abs(np.linalg.det(normalized));condition=float(np.linalg.cond(normalized))
    inverse=np.linalg.inv(A)
    assert np.max(abs(inverse@A-np.eye(2)))<5e-13
    assert np.linalg.matrix_rank(normalized)==2 and sine>0
    theta=math.atan2(sine,float(normalized[:,0]@normalized[:,1]))
    w=1/(1+math.tan(math.radians(-21))**2)
    r=e+g*w
    recovered=inverse@(r-e)
    assert np.max(abs(recovered-np.array([w,0.])))<1e-12
    # A derivative scale, not a newly measured ratio or error budget.
    perturb=np.array([0.,.01*r[1]])
    shift=inverse@perturb
    perturbed=recovered+shift
    assert np.max(abs(e+A@perturbed-(r+perturb)))<1e-15
    # A post-lookup scope control: marginal printed errors do not certify rank.
    target_gK=g[1]/A[1,1]
    sM=modes["M1"]["K"]["quoted_sigma"]
    sE=modes["E2"]["K"]["quoted_sigma"]
    fraction=(g[0]-target_gK)/(sM+sE)
    assert 0<=fraction<=1
    mK_control=m[0]-fraction*sM
    eK_control=e[0]+fraction*sE
    singular_matrix=np.column_stack(([mK_control-eK_control,g[1]],om/om[0]))
    assert abs(np.linalg.det(singular_matrix))<2e-18
    out={"identity":cfg["identity"],"input_sha256":rec["input_sha256"],
         "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         "response_sha256":rec["sha256"],"actual_version":"BrIccS v2.3 (9-Dec-2011)",
         "actual_E0_dataset":"BeOmg","all_printed_rows":rows,"Omega":omega,
         "listed_partial_sum":subtotal,"program_reported_Tot_not_certified_all_shells":True,
         "atomic_reference_uncertainty_not_given":True,
         "shells":shells,"e_E2":e.tolist(),"m_M1":m.tolist(),"Omega_s_per_second":om.tolist(),
         "g_m_minus_e":g.tolist(),"model_matrix_for_parameters_w_z":A.tolist(),
         "inverse_model_matrix":inverse.tolist(),"normalized_column_sine":sine,
         "normalized_column_angle_degrees":math.degrees(theta),
         "normalized_column_2norm_condition_number":condition,
         "fixed_ST99_gamma_reference":{"wM":w,"ratios":r.tolist(),"recovered_w_z":recovered.tolist()},
         "post_lookup_illustrative_derivative_scale":{"chosen_relative_L1_change":.01,
              "K_change":0.,"ratio_change":perturb.tolist(),"w_z_shift":shift.tolist(),
              "result_w_z":perturbed.tolist(),"physical_nominal_domain":bool(0<=perturbed[0]<=1 and perturbed[1]>=0),
              "meaning":"Post-lookup1percentderivative scale, not frozen measurement, observed uncertainty, blind test oractualfit. Nominal linear model only."},
         "post_lookup_marginal_box_rank_loss_control":{
              "fraction_of_quoted_K_marginal_errors":fraction,
              "M1_K_control":mK_control,"E2_K_control":eK_control,
              "L1_and_Omega_centers_unchanged":True,
              "determinant":float(np.linalg.det(singular_matrix)),
              "meaning":"BothKcoefficients remain inside their quoted marginal intervals. This box witness does not assert the actual atomic covariance allows this simultaneous direction, or that the intervals are joint confidence/hard theory bounds."},
         "boundary":"Full rank at printed reference centers can still be poorly conditioned. Actual response, nuclear/atomic reference variation, coefficientCov, background and counts are missing. NoactualE0/delta extraction or completeOmegaTotal is certified."}
    args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k not in ["all_printed_rows"]},ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
