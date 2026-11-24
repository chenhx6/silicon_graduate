"""Small response-level study of weighted detector groups; not a GUI release."""
from dataclasses import replace
from pathlib import Path
import argparse
import hashlib
import json
import sys
import numpy as np
from multipolepdm.contracts import Geometry
from multipolepdm.io.input import example_data, job_from_dict
from multipolepdm.models.registry import evaluate_response
from multipolepdm.physics.joint import single_channels, joint_channels, azimuth_mean_channels
from multipolepdm.physics.populations import initial_population, orientation_tensor


def group_single(job, angle, rho, entries):
    return sum(float(g['weight']) * single_channels(
        job, angle, rho, (np.deg2rad(g['theta_deg']), np.deg2rad(g.get('phi_deg', 0))))
        for g in entries)


def group_joint(job, angle, rho, target_entries, gate_entries, select_phi=False):
    channels = np.zeros(2)
    for t in target_entries:
        for g in gate_entries:
            direction = (np.deg2rad(t['theta_deg']), np.deg2rad(t.get('phi_deg', 0)))
            values = (joint_channels(job, angle, rho, direction,
                      (np.deg2rad(g['theta_deg']), np.deg2rad(g.get('phi_deg', 0))))
                      if select_phi else azimuth_mean_channels(
                          job, angle, rho, (direction[0], 0), np.deg2rad(g['theta_deg'])))
            channels += float(t['weight']) * float(g['weight']) * values
    return channels


def main(root, output):
    root = root.resolve(); output.mkdir(parents=True, exist_ok=True)
    sys.path.insert(0, str(root / 'raw/writing/pado/Upload'))
    from p_ado_135Pr.physics.pado import prepare_transition, fast_pr
    inputs = json.loads((root / 'raw/code/PDM/analysis/cases/point_angle_ado_jobs.json').read_text())['jobs']
    a = [dict(theta_deg=157.6, weight=2), dict(theta_deg=133.6, weight=1)]
    b = [dict(theta_deg=75.5, weight=3)]
    b_pair = [dict(theta_deg=75.5, weight=1.5), dict(theta_deg=104.5, weight=1.5)]
    records = []
    for doc in inputs:
        if not doc['label'].startswith('135Pr'): continue
        job = job_from_dict(doc)
        for width in [.15, .3, .6]:
            pop = initial_population(job.reference_spin, width * job.reference_spin)
            rho = np.diag(pop)
            tensors = [orientation_tensor(job.reference_spin, pop, k) for k in [2,4]]
            constants = prepare_transition(job.target.spin_initial, job.target.spin_final)
            for delta in [-10,-1,-.1,.1,1,10]:
                angle = np.arctan(delta)
                numerator = group_single(job, angle, rho, a).sum()
                denominator = group_single(job, angle, rho, b).sum()
                ratio = float(numerator/denominator)
                mean_a = [dict(g, weight=g['weight']/3) for g in a]
                mean_b = [dict(theta_deg=75.5, weight=1)]
                mean_ratio_equivalent = float(group_single(job,angle,rho,mean_a).sum()
                                              /group_single(job,angle,rho,mean_b).sum())
                np.testing.assert_allclose(mean_ratio_equivalent, ratio, rtol=1e-13)
                paired_ratio = float(numerator/group_single(job, angle, rho, b_pair).sum())
                channels = group_single(job, angle, rho, [dict(theta_deg=75.5,weight=1)])
                p = float((channels[0]-channels[1])/channels.sum())
                legacy_p, legacy_r = fast_pr(delta, *tensors, constants)
                mean_ratio = float(group_single(job, angle, rho, [dict(theta_deg=145.6,weight=1)]).sum()
                                   /group_single(job, angle, rho, [dict(theta_deg=90,weight=1)]).sum())
                records.append(dict(label=job.label,delta=delta,sigma_over_i=width,
                    weighted_P=p,weighted_R_ADO=ratio,legacy_P=legacy_p,legacy_R_ADO=legacy_r,
                    denominator_two_ring_R_ADO=paired_ratio,representative_angle_R_ADO=mean_ratio,
                    approximate_ratio_relative_difference=(mean_ratio-ratio)/ratio))
    assert max(abs(r['weighted_R_ADO']-r['legacy_R_ADO']) for r in records)<1e-10
    assert max(abs(r['weighted_P']-r['legacy_P']) for r in records)<1e-10
    assert max(abs(r['weighted_R_ADO']-r['denominator_two_ring_R_ADO']) for r in records)<1e-10
    job = replace(job_from_dict(example_data('PDCO')), geometry=Geometry(
        theta_a_deg=125,theta_b_deg=90,theta_p_deg=90,theta_gate_p_deg=125,
        ratio_azimuth_average=True,polarization_gate_azimuth_average=True))
    angle=np.arctan(.5); sigma=.3*job.reference_spin;rho=np.diag(initial_population(job.reference_spin,sigma))
    A=[dict(theta_deg=125,weight=1)];B=[dict(theta_deg=90,weight=1)]
    ab=group_joint(job,angle,rho,A,B);ba=group_joint(job,angle,rho,B,A)
    polar=group_joint(job,angle,rho,B,A)
    production=evaluate_response(job,np.array([angle]),np.array([sigma]))
    expected=[float((polar[0]-polar[1])/sum(polar)),float(sum(ab)/sum(ba))]
    np.testing.assert_allclose(expected,[production.polarization[0,0],production.angular_ratio[0,0]],rtol=1e-12)
    point=group_joint(job,angle,rho,B,A,select_phi=True)
    phi_control={'P_ring_averaged':expected[0], 'P_phi_zero':float((point[0]-point[1])/sum(point)),
                 'R_DCO_ring_averaged':expected[1], 'single_group_matches_production':True}
    sources=['raw/writing/pado/Upload/p_ado_135Pr/physics/pado.py','raw/writing/pado/Upload/p_ado_135Pr/config.py']
    result={'formula':'(2 W(157.6) + W(133.6)) / (3 W(75.5))',
            'legacy_P_theta_deg':75.5,'new_synthetic_P_theta_deg':90,
            'weights_are_effective_response_weights':'No raw-count reprocessing. Literal sums [2,1]/[3] equal explicit within-group means [2/3,1/3]/[1]; GUI normalization choice must be visible.',
            'group_A':a,'group_B':b,'equivalent_group_B':b_pair,'records':records,
            'max_abs_ratio_legacy_difference':max(abs(r['weighted_R_ADO']-r['legacy_R_ADO']) for r in records),
            'max_abs_P_legacy_difference':max(abs(r['weighted_P']-r['legacy_P']) for r in records),
            'max_abs_representative_ratio_relative_difference':max(abs(r['approximate_ratio_relative_difference']) for r in records),
            'phi_control':phi_control,'sources':[{'path':s,'sha256':hashlib.sha256((root/s).read_bytes()).hexdigest()} for s in sources]}
    pr = job_from_dict(next(d for d in inputs if d['label'] == '135Pr 747.3 keV'))
    angle_grid = np.linspace(-1.56, 1.56, 401)
    sigma_grid = np.array([.3 * pr.reference_spin])
    first = evaluate_response(replace(pr, geometry=Geometry(theta_a_deg=157.6,
        theta_b_deg=75.5, theta_p_deg=75.5)), angle_grid, sigma_grid)
    second = evaluate_response(replace(pr, geometry=Geometry(theta_a_deg=133.6,
        theta_b_deg=75.5, theta_p_deg=75.5)), angle_grid, sigma_grid)
    approximate = evaluate_response(pr, angle_grid, sigma_grid)
    np.savetxt(output/'dense_curves.csv', np.column_stack((angle_grid,
        (2*first.angular_ratio[0]+second.angular_ratio[0])/3,
        approximate.angular_ratio[0], first.polarization[0], approximate.polarization[0])),
        delimiter=',', header='angle_rad,weighted_ratio,representative_ratio,P_75p5,P_90', comments='')
    (output/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['max_abs_ratio_legacy_difference','max_abs_P_legacy_difference',
          'max_abs_representative_ratio_relative_difference','phi_control']},indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--wiki-root',type=Path,required=True);ap.add_argument('--output',type=Path,default=Path(__file__).resolve().parent);args=ap.parse_args();main(args.wiki_root,args.output)
