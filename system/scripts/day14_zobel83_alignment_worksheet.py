#!/usr/bin/env python3
"""Published 958-keV coefficient rows and a conditional population exercise.

The table means/errors are published fit outputs. s is a task-defined Gaussian
standard deviation, not a measured source sigma/I. No actual covariance or
experimental significance is reconstructed. The figure is a Wiki method aid.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import brentq

from day14_cascade_order_identifiability import coupling


def tensor_polynomials(j):
    m=np.arange(j,-j-1,-1);s=j*(j+1)
    p=np.array([3*m*m-s,
                35*m**4-(30*s-25)*m*m+3*s*s-6*s])
    return m,p/p[:,np.argmin(abs(m))][:,None]


def population(j,r):
    m=np.arange(j,-j-1,-1)
    w=np.exp(-(m*m-min(m*m))/(2*(j*r)**2));return w/w.sum()


def alpha(j,r):
    _,t=tensor_polynomials(j);return t@population(j,r)


def inverse_alpha2(j,a2):
    if not 0<a2<1:raise ValueError('mean is outside this Gaussian branch')
    return brentq(lambda r:alpha(j,r)[0]-a2,1e-5,100)


def curve_derivative(j,r):
    m,t=tensor_polynomials(j);w=population(j,r);x=m*m
    da=(t@(w*x)-(t@w)*np.dot(w,x))/(j*j*r**3)
    return da[1]/da[0]


def audit(fixture):
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    rows=fixture['rows'];check('ten_same_parent_published_rows',len(rows)==10 and fixture['transition']['Ji']==6.5)
    check('missing_covariances_kept_null',all(x['covariance_alpha2_alpha4'] is None for x in rows))
    check('unique_beam_energy_rows',len({(x['beam'],x['beam_energy_lab_MeV']) for x in rows})==len(rows))
    check('positive_printed_stat_errors',all(x['sigma_alpha2_stat_fit']>0 and x['sigma_alpha4_stat_fit']>0 for x in rows))
    for j in [3.5,4.5,6.5,8.5]:
        m,t=tensor_polynomials(j)
        for k,index in [(2,0),(4,1)]:
            # J x J -> k is a statistical-tensor coupling, not photon rank J.
            cg=coupling(j,j,k)[k,np.arange(len(m)),np.arange(len(m)-1,-1,-1)]
            cg*=(-1.0)**np.rint(j-m);cg/=cg[np.argmin(abs(m))]
            check(f'J{j}_k{k}_CG_and_Stevens_independent_agreement',np.allclose(cg,t[index],atol=2e-12))
        check(f'J{j}_isotropic_tensors_zero',np.allclose(t@np.ones(len(m))/len(m),0,atol=1e-14))
        check(f'J{j}_complete_alignment_limit',np.allclose(alpha(j,1e-3),1))
        values=np.array([alpha(j,r)[0] for r in np.geomspace(.01,20,61)])
        check(f'J{j}_Gaussian_alpha2_monotone',np.all(np.diff(values)<=1e-13))
    diagnostics=[];j=fixture['transition']['Ji']
    for row in rows:
        a2,a4=row['alpha2'],row['alpha4'];s2,s4=row['sigma_alpha2_stat_fit'],row['sigma_alpha4_stat_fit']
        r=inverse_alpha2(j,a2);pred=alpha(j,r)[1];slope=curve_derivative(j,r)
        h=1e-5;fd=(alpha(j,inverse_alpha2(j,a2+h))[1]-alpha(j,inverse_alpha2(j,a2-h))[1])/(2*h)
        label=row['beam']+'_'+str(row['beam_energy_lab_MeV'])
        check(label+'_inverse_and_gradient',abs(alpha(j,r)[0]-a2)<1e-11 and np.isclose(slope,fd,rtol=1e-7))
        sensitivity=[]
        for rho in [-.8,0,.8]:
            cov=np.array([[s2*s2,rho*s2*s4],[rho*s2*s4,s4*s4]])
            g=np.array([-slope,1]);var=float(g@cov@g)
            if np.linalg.eigvalsh(cov).min()<=0:raise AssertionError('chosen covariance not PSD')
            sensitivity.append({'chosen_rho':rho,'delta_method_residual_sigma':float(np.sqrt(var))})
        diagnostics.append({'beam':row['beam'],'beam_energy_lab_MeV':row['beam_energy_lab_MeV'],
                            'conditional_s_over_J_from_alpha2_only':float(r),'Gaussian_alpha4_at_that_width':float(pred),
                            'alpha4_minus_conditional_Gaussian':float(a4-pred),'d_model_alpha4_d_alpha2':float(slope),
                            'unknown_covariance_sensitivity':sensitivity,'one_stat_error_alpha2_upper_exceeds_model_endpoint':a2+s2>1})
    deltas=[]
    for beam in ['alpha','12C']:
        selected=sorted((x for x in rows if x['beam']==beam),key=lambda x:x['beam_energy_lab_MeV']);lo,hi=selected[0],selected[-1]
        deltas.append({'beam':beam,'high_minus_low_energy_MeV':[hi['beam_energy_lab_MeV'],lo['beam_energy_lab_MeV']],
                       'delta_alpha2':hi['alpha2']-lo['alpha2'],'sigma_delta_alpha2_independent_stat_only':float(np.hypot(hi['sigma_alpha2_stat_fit'],lo['sigma_alpha2_stat_fit'])),
                       'delta_alpha4':hi['alpha4']-lo['alpha4'],'sigma_delta_alpha4_independent_stat_only':float(np.hypot(hi['sigma_alpha4_stat_fit'],lo['sigma_alpha4_stat_fit']))})
    # This mixture is explicitly chosen, not a fit of Fig3 feeding fractions.
    w0,w1=population(j,.12),population(j,.38);lam=.45;mix=lam*w0+(1-lam)*w1;m,t=tensor_polynomials(j)
    mixed_alpha=t@mix;r_eff=inverse_alpha2(j,mixed_alpha[0]);curve_gap=mixed_alpha[1]-alpha(j,r_eff)[1]
    check('chosen_mixture_tensor_linearity',np.allclose(mixed_alpha,lam*alpha(j,.12)+(1-lam)*alpha(j,.38)))
    check('chosen_mixture_not_Gaussian_in_coefficient_plane',abs(curve_gap)>.01)
    positive=m>0;x=m[positive]**2;logw=np.log(mix[positive]);order=np.argsort(x);slopes=np.diff(logw[order])/np.diff(x[order])
    check('chosen_mixture_log_population_not_affine',np.ptp(slopes)>.01)
    ticks=fixture['figure3_ticks'];lab=np.array(ticks['beam_lab_MeV']);printed=np.array(ticks['printed_above_threshold_MeV'])
    reconstructed=lab*ticks['mass_number_CM_ratio_task_inference']-ticks['caption_Q_MeV']-ticks['initial_excitation_MeV']
    check('Fig3_ticks_mass_number_CM_crosscheck',np.max(abs(reconstructed-printed))<.005)
    return {'kind':'published fit means plus conditional task-defined Gaussian diagnostics; no experimental refit',
            'diagnostics':diagnostics,'same_parent_endpoint_differences':deltas,
            'chosen_population_mixture':{'s_over_J_components':[.12,.38],'first_weight':lam,'alpha2_alpha4':mixed_alpha.tolist(),'same_alpha2_Gaussian_s_over_J':r_eff,'alpha4_gap':float(curve_gap),'not_Fig3_fit':True},
            'Fig3_above_threshold_crosscheck':{'reconstructed_MeV':reconstructed.tolist(),'printed_MeV':printed.tolist(),'max_abs_difference_MeV':float(np.max(abs(reconstructed-printed))),'recipe_is_task_inference':True,'Q4_is_subtracted_threshold_magnitude':True},
            'checks':checks,'checks_passed':sum(checks.values()),
            'boundaries':['The10rows are published attenuation-fit estimates with statistical marginal errors, not raw spectra.','Delta0 and pureE2 assumptions are adopted by the original source; s is task-defined standard deviation.','The alpha2-only inverse is not a joint alpha2/alpha4 fit or a source-measured s/I.','Unknown covariance and full response forbid experimental significance and L4 replay.','Endpoint difference uncertainties assume independent statistical errors only; calibration/shared systematics are absent.','The chosen covariance range and population mixture are sensitivity controls, not measured inputs.','OriginalJuly humanreview scope is preserved; new analysis has no new humanreview event.','Day14 continues andDay15 remains an uncredited preview.']}


def plot(fixture,prefix):
    root=Path(__file__).resolve().parents[2];prefix.resolve().relative_to(root)
    os.environ['MPLCONFIGDIR']=str(root/'tmp/day14-20261014/mplconfig')
    import matplotlib as mpl
    mpl.use('Agg')
    import matplotlib.pyplot as plt
    mpl.rcParams.update({'font.family':'sans-serif','font.sans-serif':['Arial','Liberation Sans','DejaVu Sans'],
                         'svg.fonttype':'none','pdf.fonttype':42,'svg.hashsalt':'day14-zobel83-data-model',
                         'font.size':9,'axes.spines.top':False,'axes.spines.right':False,'axes.linewidth':.8,'legend.frameon':False})
    fig,ax=plt.subplots(figsize=(5.511811023622047,4.330708661417323));j=fixture['transition']['Ji']
    curve=np.array([alpha(j,r) for r in np.geomspace(.01,20,501)])
    ax.plot(curve[:,0],curve[:,1],color='.35',lw=1.2,label='Conditional Gaussian, J = 13/2')
    for beam,marker,color,label in [('alpha','o','#cc6677','Alpha beam: published estimates'),('12C','s','#4477aa','12C beam: published estimates')]:
        rows=[x for x in fixture['rows'] if x['beam']==beam]
        ax.errorbar([x['alpha2'] for x in rows],[x['alpha4'] for x in rows],xerr=[x['sigma_alpha2_stat_fit'] for x in rows],
                    yerr=[x['sigma_alpha4_stat_fit'] for x in rows],fmt=marker,color=color,markersize=4,capsize=2,lw=.8,label=label)
    ax.set(xlabel='Alignment attenuation α₂',ylabel='Alignment attenuation α₄',xlim=(0,1.08),ylim=(0,1.08),
           title='67Ga: same 958.0 keV transition across beam settings')
    ax.legend(loc='upper left',fontsize=8);fig.subplots_adjust(left=.15,right=.98,top=.90,bottom=.22)
    fig.text(.15,.065,'Zobel et al. (1983), Table 1: fit estimates ± stat. errors.\nCovariance not supplied; curve is a conditional model.',fontsize=8,color='.35')
    # Installed skill is an audit library; all output/cache paths remain in Wiki.
    sys.dont_write_bytecode=True
    sys.path.insert(0,'/root/.codex/skills/nature-figure/scripts')
    from audit_panel_alignment import require_matplotlib_panel_alignment
    require_matplotlib_panel_alignment(fig,json_out=str(prefix)+'.alignment.json',overlay_svg=str(prefix)+'.alignment.svg',strict=True)
    svg=Path(str(prefix)+'.svg');fig.savefig(svg,metadata={'Date':None});svg.write_text('\n'.join(x.rstrip() for x in svg.read_text().splitlines())+'\n')
    fig.savefig(str(prefix)+'.pdf',metadata={'CreationDate':None,'ModDate':None});fig.savefig(str(prefix)+'.png',dpi=400);plt.close(fig)
    with Path(str(prefix)+'.source-data.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(fixture['rows'][0]),lineterminator='\n');writer.writeheader();writer.writerows(fixture['rows'])


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--fixture',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--plot-prefix',type=Path)
    args=p.parse_args();root=Path(__file__).resolve().parents[2]
    for path in [args.fixture,args.output]:path.resolve().relative_to(root)
    fixture=json.loads(args.fixture.read_text());result=audit(fixture);args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    if args.plot_prefix:plot(fixture,args.plot_prefix)
    print(json.dumps({k:result[k] for k in ['checks_passed','same_parent_endpoint_differences','chosen_population_mixture','Fig3_above_threshold_crosscheck']},ensure_ascii=False))


if __name__=='__main__':main()
