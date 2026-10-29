#!/usr/bin/env python3
"""Audit published 144,146Ba E3 intervals and the SCCM orbital-occupancy claim.
No HFB/SCCM calculation is performed; unpublished orbital-resolved kernels remain null.
"""
from pathlib import Path
import datetime as dt, hashlib, json, math, subprocess

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).with_suffix('.json')


def interval(center, low, high):
    return [center-low, center+high]


def overlap(a,b):
    lo, hi = max(a[0],b[0]), min(a[1],b[1])
    return {'interval': [lo,hi] if hi >= lo else None,
            'length': max(0.0,hi-lo),
            'union_length': max(a[1],b[1])-min(a[0],b[0]),
            'jaccard': max(0.0,hi-lo)/(max(a[1],b[1])-min(a[0],b[0]))}


def pdf_info(rel, pages_read):
    p=ROOT/rel; b=p.read_bytes()
    text=subprocess.run(['pdftotext','-layout',str(p),'-'],capture_output=True,text=True,check=True).stdout
    info=subprocess.run(['pdfinfo',str(p)],capture_output=True,text=True,check=True).stdout
    pages=int(next(x.split(':',1)[1] for x in info.splitlines() if x.startswith('Pages:')))
    return {'raw_file':rel,'raw_sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),
            'pdf_signature':b[:5].decode('ascii','replace'),'pages':pages,
            'pages_read':pages_read,'text_has_key_terms':all(x in text for x in ['E3'])}


def main():
    # These are reported asymmetric error intervals; papers do not establish a common
    # formal confidence level in the text used here, so do not label them as 95% CIs.
    m144=interval(.65,.23,.17)
    m146=interval(.65,.20,.14)
    b144=[14.,73.]
    b146=[19.,69.]
    orbital=[
      {'orbital_parent':'nu h9/2','K_pi':'3/2-','v2_144Ba':0.0,'v2_146Ba':0.40,'paper_statement':'significant occupancy; contribution collectively participates in near cancellation','per_orbital_dipole_kernel_published':None},
      {'orbital_parent':'nu f7/2','K_pi':'5/2-','v2_144Ba':0.0,'v2_146Ba':0.27,'paper_statement':'significant occupancy; contribution collectively participates in near cancellation','per_orbital_dipole_kernel_published':None},
      {'orbital_parent':'nu i13/2','K_pi':'1/2+','v2_144Ba':0.0,'v2_146Ba':0.20,'paper_statement':'significant occupancy; contribution collectively participates in near cancellation','per_orbital_dipole_kernel_published':None},
    ]
    amp_ratio=.00474/.000223
    result={
      'status':'source-grounded bounded audit; no new HFB/SCCM run',
      'generated_at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
      'question':'How far do published SCCM results identify nu h9/2, f7/2, i13/2 occupancy as the microscopic origin of E1 cancellation, and what does E3 interval overlap imply for static pear shape?',
      'experimental_E3':{
        '144Ba':{'M_0_to_3_eb3_2':.65,'reported_error_interval_eb3_2':m144,'B_down_Wu':[14.,73.],'Q3_efm3':[1.11,2.18],'beta3_fixed_beta2_018':[.11,.21]},
        '146Ba':{'M_0_to_3_eb3_2':.65,'reported_error_interval_eb3_2':m146,'B_down_Wu':b146,'Q3_efm3':None,'beta3':None},
        'matrix_element_overlap':overlap(m144,m146),
        'B_E3_reported_interval_overlap':overlap(b144,b146),
        'interpretation':'overlapping reported asymmetric error intervals show no resolved isotope difference in this observable; they are not a formal common-confidence test',
        'B_relation':'B(E3;3- -> 0+) = |M(0+ -> 3-)|^2 / 7; intervals above are the published rounded W.u. intervals',
        'relative_E1_E3_sign_sensitivity_144Ba':'opposite sign changes fitted E3 magnitude by about 10%, within quoted errors',
      },
      'SCCM_146Ba':{
        'force':'Gogny D1S',
        'collective_coordinates':['Q20','Q30'],
        'symmetries_restored':['angular momentum','parity','neutron number','proton number'],
        'PES_minimum_beta2':.21,'PES_minimum_abs_beta3':.10,
        'collective_amplitude_observation':'0+ and 1- amplitudes have very large overlap in 144,146,148Ba, interpreted as strong octupole correlations',
        'E1_experimental_matrix_eb1_2':.000223,
        'E1_SCCM_matrix_eb1_2':.00474,'E1_SCCM_to_exp_amplitude_ratio':amp_ratio,
        'orbital_occupancies':orbital,
        'published_mechanism':'The paper attributes the sudden E1 drop to projected intrinsic-state dipole overlap and states that these three neutron orbital parentages, empty in 144Ba and occupied in 146Ba, collectively nearly cancel the proton contribution.',
        'unpublished_or_unresolved':['individual signed h9/2/f7/2/i13/2 dipole contributions','Q-dependent v2 and transition kernels','full covariance of SCCM E1 output and experiment','a unique phase-independent orbital decomposition of the projected matrix element']
      },
      'static_shape_boundary':{
        'directly_supported':'strong E3 transition collectivity in both isotopes',
        'model_supported':'reflection-asymmetric D1S minima and SCCM collective amplitudes consistent with octupole correlations',
        'not_proven':'a rigid static pear shape from E3 interval overlap alone',
        'reason':'E3 is a transition matrix element; converting it to intrinsic Q3 or beta3 invokes axial/rotor and shape-truncation assumptions. Soft collective amplitudes and PES fluctuations remain compatible with the same E3 strength.',
        'additional_required_evidence':['state-resolved E3 systematics beyond 0+↔3-','opposite-parity energy displacement and E1/E3 branching','converged multi-coordinate projected kernels and inertia','explicit Q-dependent density/orbital-resolved dipole kernels']
      },
      'sources':[
       pdf_info('raw/papers/gpt/high-spin-20260920/形变/2016_Bucher et al_Direct Evidence of Octupole Deformation in Neutron-Rich Ba 144.pdf',[1,2,3,4,5]),
       pdf_info('raw/papers/gpt/high-spin-20260920/external-146ba/PDFs/Direct_Evidence_for_Octupole_Deformation_in_146Ba_and_the_Origin_of_Large_E1_Moment_Variations_in_Reflection-Asymmetric_Nuclei.pdf',[1,2,3,4,5,6]),
       pdf_info('raw/papers/gpt/day26-20261028/bernard-2016-144ba-sccm-arxiv1604.06706v1.pdf',[1,2,3,4,5,6])
      ],
      'evidence_level':'direct experiment plus author-interpreted SCCM mechanism; orbital-level quantitative decomposition unavailable in cited pages',
    }
    # Correctly encode 146 E1 error notation separately; avoid fake numeric CI.
    result['SCCM_146Ba']['E1_experimental_reported_notation']='0.000223(+10/-8) eb^(1/2)'
    result['SCCM_146Ba']['E1_experimental_error_interval_if_literal']=[.000215,.000233]
    result['SCCM_146Ba']['E1_experimental_error_interval_status']='literal asymmetric reported error range; confidence level not specified here'
    OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'output':str(OUT.relative_to(ROOT)), 'M_overlap':result['experimental_E3']['matrix_element_overlap'], 'B_overlap':result['experimental_E3']['B_E3_reported_interval_overlap'], 'E1_ratio':amp_ratio},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
