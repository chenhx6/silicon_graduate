#!/usr/bin/env python3
"""Reconstruct 192Os branch ratios from a frozen, source-verified Table 1.

Photon and conversion-inclusive rates differ. Absolute branch rates below
assume closure on the listed transitions; same-parent ratios do not need that
assumption. No guessed Weisskopf constants or microscopic shape inversion.
"""
import argparse
import csv
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def propagate_ratio(i1, s1, i2, s2, rho):
    return math.sqrt((s1/i1)**2 + (s2/i2)**2 - 2*rho*s1*s2/(i1*i2))

def run(input_path, output_dir):
    data = json.loads(input_path.read_text())
    source = ROOT / data['source_pdf']
    assert source.exists() and sha(source) == data['source_sha256'], 'Original missing or hash mismatch'
    isomers, flat = [], []
    for iso in data['isomers']:
        parent = {k:v for k,v in iso.items() if k != 'branches'}
        tau = iso['parent_tau_s']
        assert tau > 0
        total = sum(b['I_gamma']*(1+b['alpha_tot']) for b in iso['branches'])
        branches = []
        for b in iso['branches']:
            assert b['I_gamma'] > 0 and b['alpha_tot'] >= 0
            ig, it = b['I_gamma'], b['I_gamma']*(1+b['alpha_tot'])
            row = {**b, 'I_including_conversion':it,
                   'listed_closure_branch_fraction':it/total,
                   'conditional_lambda_gamma_s_inv':ig/(total*tau),
                   'conditional_lambda_total_s_inv':it/(total*tau),
                   'conditional_partial_gamma_half_life_s':math.log(2)*total*tau/ig}
            branches.append(row)
            flat.append({**parent, 'parent_T12_s':tau*math.log(2),
                         'parent_dT12_s':iso['parent_dtau_s']*math.log(2), **row})
        assert math.isclose(sum(b['listed_closure_branch_fraction'] for b in branches),1.,rel_tol=1e-14)
        isomers.append({**parent,'listed_total_intensity':total,'branches':branches})
    iso = next(d for d in isomers if d['parent_nucleus']=='192Os' and d['parent_JiPi']=='12+')
    a = next(b for b in iso['branches'] if b['E_gamma_keV']==111.5)
    b = next(b for b in iso['branches'] if b['E_gamma_keV']==445.7)
    assert a['multipolarity'] == b['multipolarity'] == 'E2'
    photon_ratio = a['I_gamma']/b['I_gamma']
    phase = (b['E_gamma_keV']/a['E_gamma_keV'])**5
    intensity_strength_ratio = photon_ratio*phase
    printed_strength_ratio = a['reported_B_Wu']/b['reported_B_Wu']
    printed_B_photon_ratio = printed_strength_ratio/phase
    total_ratio = photon_ratio*(1+a['alpha_tot'])/(1+b['alpha_tot'])
    assert math.isclose(a['conditional_lambda_gamma_s_inv']/b['conditional_lambda_gamma_s_inv'],photon_ratio,rel_tol=1e-14)
    assert math.isclose(a['conditional_lambda_total_s_inv']/b['conditional_lambda_total_s_inv'],total_ratio,rel_tol=1e-14)
    assert math.isclose(phase*((a['E_gamma_keV']/b['E_gamma_keV'])**5),1.,rel_tol=1e-14)
    assert math.isclose(intensity_strength_ratio*((b['I_gamma']/a['I_gamma'])/phase),1.,rel_tol=1e-14)
    for energy_scale in (1e-3,1e3):
        assert math.isclose(((energy_scale*b['E_gamma_keV'])/(energy_scale*a['E_gamma_keV']))**5,phase,rel_tol=1e-14)
    for tau_scale, norm_scale in ((2.5,7.),(.2,.1)):
        x=a['I_gamma']/(iso['listed_total_intensity']*norm_scale*iso['parent_tau_s']*tau_scale)
        y=b['I_gamma']/(iso['listed_total_intensity']*norm_scale*iso['parent_tau_s']*tau_scale)
        assert math.isclose(x/y,photon_ratio,rel_tol=1e-14)
    # Printed last-digit rounding consistency is separate from measurement errors.
    rounding_bounds = [(9.7-.05)/(.044+.0005),(9.7+.05)/(.044-.0005)]
    assert rounding_bounds[0] <= intensity_strength_ratio <= rounding_bounds[1]
    scenarios=[]
    for rho in (-1.,-.5,0.,.5,1.):
        rel=propagate_ratio(a['I_gamma'],a['dI_gamma'],b['I_gamma'],b['dI_gamma'],rho)
        scenarios.append({'rho':rho,'first_order_relative_error':rel,
                          'linear_error_on_strength_ratio':intensity_strength_ratio*rel})
    naive=math.hypot(a['reported_dB_Wu']/a['reported_B_Wu'],b['reported_dB_Wu']/b['reported_B_Wu'])
    result={'source_pdf':data['source_pdf'],'source_sha256':data['source_sha256'],
            'input_sha256':sha(input_path),'script_sha256':sha(Path(__file__)),
            'source_locator':data['source_locator'],'isomers':isomers,
            'two_branch_e2_audit':{
                'parent':'192Os 2865-keV 12+; mean lifetime 2.0(4) ns',
                'low_energy_branch_final':'10+_2, author aligned/oblate assignment',
                'high_energy_branch_final':'10+_1, ground-state band',
                'E5_high_over_low':phase,'photon_rate_ratio_from_intensities':photon_ratio,
                'conversion_inclusive_rate_ratio':total_ratio,
                'strength_ratio_from_intensities':intensity_strength_ratio,
                'strength_ratio_from_printed_B_values':printed_strength_ratio,
                'photon_ratio_from_printed_B_values':printed_B_photon_ratio,
                'relative_difference_intensity_vs_printed_strength_ratio':intensity_strength_ratio/printed_strength_ratio-1,
                'printed_B_rounding_ratio_bounds':rounding_bounds,
                'rounding_consistency':True,
                'conditional_intensity_covariance_scenarios':scenarios,
                'independent_printed_B_relative_error_for_comparison_only':naive,
                'uncertainty_boundary':'First-order scenarios using reported intensity marginal errors; energy, multipolarity and ICC systematics not quantified. No calibrated confidence interval or true covariance inferred.',
                'tau_cancellation':'Common parent lifetime and listed-branch normalization cancel in this same-parent E2 ratio.'},
            'absolute_rate_scope':'Conditional on closure over listed transitions and adopted ICC/multipolarity; missing branches alter absolute rates but cancel in same-parent ratios.',
            'microscopic_boundary':'Branch strengths constrain matrix-element magnitudes, not unique gamma, K distribution, configuration overlap or a shape-tunneling barrier.',
            'checks':['source hash fail-closed','listed probability closure','photon/total intensity-rate identities',
                      'branch-swap reciprocal','keV/MeV scaling','shared tau/normalization cancellation',
                      'printed precision consistent with intensity-derived ratio']}
    output_dir.mkdir(parents=True,exist_ok=True)
    jp=output_dir/'os192_branch_rates.json';cp=output_dir/'os192_transitions.csv'
    jp.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    keys=sorted(set(k for row in flat for k in row))
    with cp.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=keys,lineterminator="\n");writer.writeheader();writer.writerows(flat)
    provenance={'artifact_type':'conditional-branch-rate-reduction','created_at':datetime.now(timezone.utc).isoformat(),
                'command':'python3 system/scripts/os192_branch_rate_audit.py --input '+str(input_path)+' --output-dir '+str(output_dir),
                'source_pdf':data['source_pdf'],'source_sha256':data['source_sha256'],
                'artifacts':[{'path':str(p),'sha256':sha(p),'size_bytes':p.stat().st_size} for p in [Path(__file__),input_path,jp,cp]],
                'parent_corrections':['Printed B rounding distinguished from intensity ratio','No unsourced Weisskopf rate constants','No microscopic exclusivity or fixed gamma barrier','Hash mismatch aborts','Unknown covariance/energy errors do not become confidence intervals']}
    (output_dir/'run-provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result['two_branch_e2_audit'],ensure_ascii=False,indent=2))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,default=ROOT/'outputs/l4/20261107-isomer-cross-region-round2/os192/table1-transcription.json')
    p.add_argument('--output-dir',type=Path,default=ROOT/'outputs/l4/20261107-isomer-cross-region-round2/os192')
    a=p.parse_args();run(a.input,a.output_dir)

if __name__=='__main__':main()
