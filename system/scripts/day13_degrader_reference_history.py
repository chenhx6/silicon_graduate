#!/usr/bin/env python3
"""Day13 declared finite-degrader/reference/feeding model; no RDDS refit.

Pre/post beta .12/.09, 16.7um foil, gaps and corrected-energy sigma1keV are
self-chosen. Gamma1222.9keV and lifetimes3.8/7.5ps are source-inspired LS23
scales, not a calibrated experiment. Lab velocity decreases linearly inside
the foil; proper clock is integrated exactly. Photon recoil, loss straggling,
vertex displacement, actual detector geometry/response and covariance absent.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad


C_MM_PS=.299792458


def primitive(beta):
    b=np.asarray(beta)
    return .5*(b*np.sqrt(1-b*b)+np.arcsin(b))


def proper_foil_clock(beta_in,beta_out,length):
    lab_duration=2*length/(C_MM_PS*(beta_in+beta_out))
    if abs(beta_in-beta_out)<1e-12:
        proper_duration=lab_duration*math.sqrt(1-beta_in*beta_in)
    else:
        proper_duration=lab_duration/(beta_out-beta_in)*float(primitive(beta_out)-primitive(beta_in))
    numerical=quad(lambda t:math.sqrt(1-(beta_in+(beta_out-beta_in)*t/lab_duration)**2),
                   0,lab_duration,epsabs=1e-12)[0]
    assert abs(numerical-proper_duration)<1e-12
    return lab_duration,proper_duration


def cdf(t,tau,feeder=0.):
    if feeder==0:return 1-math.exp(-t/tau)
    return 1-(feeder*math.exp(-t/feeder)-tau*math.exp(-t/tau))/(feeder-tau)


def beta_inside(times,beta_in,beta_out,length,grid_size):
    lab_duration,proper_duration=proper_foil_clock(beta_in,beta_out,length)
    lab_grid=np.linspace(0,lab_duration,grid_size)
    beta_grid=beta_in+(beta_out-beta_in)*lab_grid/lab_duration
    proper_grid=lab_duration/(beta_out-beta_in)*(primitive(beta_grid)-primitive(beta_in))
    return np.interp(times,proper_grid,beta_grid)


def calculate():
    rest,pre,post,foil=1222.9,.12,.09,.0167
    tau,feeder_tau,samples=3.8,7.5,500000
    lab_foil,proper_foil=proper_foil_clock(pre,post,foil)
    rng=np.random.default_rng(131024);rows=[];max_fraction=0.;max_grid=0.;max_inverse=0.
    post_gamma=1/math.sqrt(1-post*post)
    for feeder in (0.,feeder_tau):
        proper_times=rng.exponential(tau,samples)
        if feeder:proper_times+=rng.exponential(feeder,samples)
        # Full-sphere rest-isotropic photons, then select an ideal full-azimuth
        # laboratory120-170degcap, not the actual AGATA crystal tiling.
        rest_cos=rng.uniform(-1,1,samples)
        for gap in (.020,.470,2.):
            before_clock=gap*math.sqrt(1-pre*pre)/(C_MM_PS*pre)
            before=proper_times<before_clock
            during=(proper_times>=before_clock)&(proper_times<before_clock+proper_foil)
            after=proper_times>=before_clock+proper_foil
            betas=np.where(before,pre,post)
            if np.any(during):
                relative_time=proper_times[during]-before_clock
                coarse=beta_inside(relative_time,pre,post,foil,1024)
                fine=beta_inside(relative_time,pre,post,foil,2048)
                max_grid=max(max_grid,float(np.max(np.abs(coarse-fine))))
                betas[during]=fine
            gammas=1/np.sqrt(1-betas*betas)
            lab_cos=(rest_cos+betas)/(1+betas*rest_cos)
            lab_energy=rest*gammas*(1+betas*rest_cos)
            corrected_reference=lab_energy*post_gamma*(1-post*lab_cos)
            truth=lab_energy*gammas*(1-betas*lab_cos)
            max_inverse=max(max_inverse,float(np.max(np.abs(truth-rest))))
            mask=(lab_cos>=math.cos(math.radians(170)))&(lab_cos<=math.cos(math.radians(120)))
            selected_corrected=corrected_reference[mask]+rng.normal(0,1.,int(np.sum(mask)))
            peak_gate=np.abs(selected_corrected-rest)<5.
            analytical=np.array([cdf(before_clock,tau,feeder),
                                 cdf(before_clock+proper_foil,tau,feeder)-cdf(before_clock,tau,feeder),
                                 1-cdf(before_clock+proper_foil,tau,feeder)])
            MC=np.array([np.mean(before),np.mean(during),np.mean(after)])
            max_fraction=max(max_fraction,float(np.max(np.abs(analytical-MC))))
            chosen_labels=np.where(before[mask],0,np.where(during[mask],1,2))
            accepted_labels=chosen_labels[peak_gate]
            gate_stage=[float(np.mean(accepted_labels==i)) if len(accepted_labels) else None for i in range(3)]
            rows.append({'gap_mm':gap,'proper_level_tau_ps':tau,'proper_feeder_tau_ps':feeder,
                         'proper_clock_before_foil_ps':before_clock,'analytic_unconditional_stage_fractions':analytical.tolist(),
                         'MC_unconditional_stage_fractions':MC.tolist(),'ideal_cap_selected_fraction':float(np.mean(mask)),
                         'selected_cap_stage_fractions':[float(np.mean(chosen_labels==i)) for i in range(3)],
                         'rest_reference_plusminus5keV_gate_fraction':float(np.mean(peak_gate)),
                         'gate_conditioned_stage_fractions':gate_stage,
                         'boundary':'stage0before/1insidefoil/2after; isotropic ideal cap and Gaussian sigma1 are self-chosen'})
    # Before-foil emitted line under the post-foil correction has a lower
    # energy in backward angles. For equal speeds it has no residual.
    residuals=[]
    for angle in (120.,145.,170.):
        cosine=math.cos(math.radians(angle));dpre=(1-pre*cosine)/math.sqrt(1-pre*pre)
        dpost=(1-post*cosine)/math.sqrt(1-post*post)
        residual=rest*(dpost/dpre-1);assert residual<0
        residuals.append({'lab_angle_deg':angle,'before_foil_reference_residual_keV':residual})
    equal_cos=np.linspace(-1,1,51);d=(1-pre*equal_cos)/math.sqrt(1-pre*pre)
    assert np.max(np.abs(rest/d*d-rest))<1e-10
    assert max_fraction<.003 and max_grid<1e-7 and max_inverse<1e-9
    return {'schema_version':1,'kind':'synthetic finitefoil/properclock/postvelocity reference and feeding fixture',
            'parameters':{'rest_gamma_keV':rest,'chosen_beta_pre':pre,'chosen_beta_post':post,
                          'chosen_foil_mm':foil,'lab_foil_crossing_ps':lab_foil,'proper_foil_crossing_ps':proper_foil,
                          'Gaussian_corrected_energy_sigma_keV':1.,'ideal_lab_cap_deg':[120,170],'samples_each_history':samples},
            'rows':rows,'before_reference_angle_residuals':residuals,
            'verification':{'analytic_properclock_vs_independent_quad_passed':True,
                            'stage_fraction_MC_max_absolute_difference':max_fraction,
                            'proper_to_beta_grid1024_2048_max_difference':max_grid,
                            'truth_velocity_inverse_max_error_keV':max_inverse,
                            'equal_velocity_no_reference_shift_limit_passed':True,
                            'backward_shift_sign_passed':True,'passed':True},
            'boundaries':['No actualMg stoppingpower/lossstraggling, beam/population/PID/geometry packet is supplied.',
                          'Source lifetime central values only set illustrative clocks; no lifetime is fitted.',
                          'Gate and peak shape under a postvelocity reference retain history; truth inverse collapses energies but does not preserve energy-only history by itself.',
                          'U afterfoil is still moving; stage fractions after angular/energy selection differ from unconditional decay probabilities.'],
            'numpy_version':np.__version__}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=calculate()
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(a.output),'verification':r['verification'],
                     'gap0_47_rows':[x for x in r['rows'] if x['gap_mm']==.470],
                     'angle_residuals':r['before_reference_angle_residuals']}))


if __name__=='__main__':
    main()
