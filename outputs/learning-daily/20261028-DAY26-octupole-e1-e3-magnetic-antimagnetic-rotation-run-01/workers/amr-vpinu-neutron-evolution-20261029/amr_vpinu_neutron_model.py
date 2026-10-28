#!/usr/bin/env python3
"""Transparent proxy calculations for AMR V_pinu/core and neutron-evolution sensitivity.

This is a schematic particle-plus-rotor calculation. It is not a fit to 104Pd/106Cd.
"""
import csv, json, math
from pathlib import Path

OUT=Path(__file__).parent
jh=4.5
Vpip=0.15
n=4

def p2(c): return (3*c*c-1)/2

def omega(c,V,n_pairs=n):
    return (1.5*V/jh)*c - (6*Vpip/(n_pairs*jh))*(2*c*c-1)*c

def domega_dc(c,V):
    return 1.5*V/jh - (6*Vpip/(n*jh))*(6*c*c-1)

def torque(c,V):
    # magnitude of -d[V P2(cos theta)]/dtheta
    return 3*V*c*math.sqrt(max(0.0,1-c*c))

def bnorm(c): return (1-c*c)**2

def D(c,V,Jc): return 2*jh + Jc*domega_dc(c,V)

def solve_c(I,jn,V,Jc,n_pairs=n):
    # Monotone branch in the parameter ranges used here.
    lo,hi=0.0,1.0
    def f(c): return jn+2*jh*c+Jc*omega(c,V,n_pairs)-I
    flo,fhi=f(lo),f(hi)
    if abs(flo)<1e-12: return lo
    if abs(fhi)<1e-12: return hi
    if flo*fhi>0: return None
    for _ in range(100):
        mid=(lo+hi)/2; fm=f(mid)
        if abs(fm)<1e-13: return mid
        if flo*fm<=0: hi=mid; fhi=fm
        else: lo=mid; flo=fm
    return (lo+hi)/2

# V_pinu torque and angular response
rows=[]
for V in (0.6,1.2,2.4):
    for theta in range(15,91,5):
        c=math.cos(math.radians(theta))
        rows.append({'V_pinu_MeV':V,'theta_deg':theta,'cos_theta':c,'torque_MeV':torque(c,V),'omega_sh_MeV':omega(c,V),'B_E2_norm':bnorm(c)})
with (OUT/'vpinu_torque_grid.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

# Core sensitivity at fixed geometry. Positive D means closure c increases with spin.
rows=[]
for V in (1.2,2.4):
    for Jc in (0.0,5.0,10.0,19.5):
        for c in (0.2,0.5,0.8):
            d=D(c,V,Jc)
            rows.append({'V_pinu_MeV':V,'J_core_hbar2_per_MeV':Jc,'cos_theta':c,'domega_dc_MeV':domega_dc(c,V),'D_dI_dc':d,'dc_dI':1/d,'dBnorm_dI':-4*c*(1-c*c)/d,'dtheta_dI_rad_per_hbar':-1/(math.sqrt(1-c*c)*d),'omega_sh_MeV':omega(c,V)})
with (OUT/'core_closure_sensitivity.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

# Roy-style proxy values for Cd chain; parameters are literature/model descriptors, not fitted isotope results.
chain=[
 {'nucleus':'106Cd','N':58,'jnu_eff':18.0,'n_pairs':8,'Jcore':0.0,'V_pinu':1.2,'spin_range':'18-24','basis':'Roy comparison / effective jnu; V is phenomenological reference'},
 {'nucleus':'108Cd','N':60,'jnu_eff':16.0,'n_pairs':8,'Jcore':0.0,'V_pinu':1.2,'spin_range':'16-22','basis':'Roy comparison / effective jnu; V is phenomenological reference'},
 {'nucleus':'110Cd','N':62,'jnu_eff':10.0,'n_pairs':4,'Jcore':19.5,'V_pinu':1.2,'spin_range':'16-24','basis':'Roy particle-plus-rotor interpretation; Jcore is model input'},
]
rows=[]
for p in chain:
    lo,hi=map(int,p['spin_range'].split('-'))
    for I in range(lo,hi+1,2):
        c=solve_c(I,p['jnu_eff'],p['V_pinu'],p['Jcore'],p['n_pairs'])
        rows.append({**p,'I_hbar':I,'cos_theta':None if c is None else c,'theta_deg':None if c is None else math.degrees(math.acos(c)),'B_E2_norm':None if c is None else bnorm(c),'omega_sh_MeV':None if c is None else omega(c,p['V_pinu'],p['n_pairs']),'R_core_hbar':None if c is None else p['Jcore']*omega(c,p['V_pinu'],p['n_pairs'])})
with (OUT/'cd_neutron_evolution_proxy.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

# Same-N 106Cd/104Pd V scaling thought experiment, fixed jnu=18 and selected Jcore.
rows=[]
for nucleus,np_holes,V in [('same_N_control_2holes',2,1.2),('counterfactual_4holes_doubled_V',4,2.4)]:
    for Jc in (0.0,5.0,19.5):
        for I in (18,20,22,24):
            c=solve_c(I,18.0,V,Jc)
            rows.append({'nucleus':nucleus,'proton_g9_2_holes':np_holes,'V_pinu_MeV':V,'Jcore_hbar2_per_MeV':Jc,'I_hbar':I,'cos_theta':None if c is None else c,'theta_deg':None if c is None else math.degrees(math.acos(c)),'B_E2_norm':None if c is None else bnorm(c),'omega_sh_MeV':None if c is None else omega(c,V),'R_core_hbar':None if c is None else Jc*omega(c,V)})
with (OUT/'same_N_106Cd_104Pd_scaling.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

summary={
 'model':'Roy-style particle-plus-rotor proxy',
 'equations':{
  'I_of_c':'I = j_nu + 2*j_h*c + J_core*omega_sh(c)',
  'omega_sh':'omega_sh = (1.5*V_pinu/j_h)*c - (6*V_pipi/(n*j_h))*(2*c^2-1)*c',
  'B_E2_normalized':'B/B_bandhead = (1-c^2)^2',
  'torque_magnitude':'|tau_pinu| = 3*V_pinu*c*sqrt(1-c^2)',
  'closure_denominator':'D = dI/dc = 2*j_h + J_core*domega_sh/dc'
 },
 'fixed_inputs':{'j_h':jh,'V_pipi_MeV':Vpip,'n':n},
 'interpretation':[
  'For J_core=0, c(I)=(I-j_nu)/(2*j_h), so changing V_pinu changes omega and torque but not B(E2) versus I in this fixed-length proxy.',
  'For J_core>0, larger positive V_pinu increases D and reduces dc/dI, delaying shear closure at fixed spin; core rotation makes B(E2) decline more slowly in this convention.',
  'A four-hole/four-blade 104Pd system cannot be assigned V_pinu=2*1.2 MeV from data. The factor-two case is a counterfactual sensitivity scenario, not a physical upper bound; pairing and configuration mixing renormalize it.',
  'Cd chain parameters are literature/model descriptors from existing local audits, not isotope-by-isotope fitted values.'
 ]
}
(OUT/'model_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')

# Single-j angular quadrupole proxy for all h11/2 substates.
# The sign is angular only; radial and effective-charge factors are unspecified.
qrows=[]
j=5.5
for two_m in range(-11,12,2):
    m=two_m/2
    qrows.append({'j':j,'m':m,'q20_angular_3m2_minus_jj1':3*m*m-j*(j+1)})
with (OUT/'h11_2_quadrupole_substates.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(qrows[0]));w.writeheader();w.writerows(qrows)
qtrace=sum(r['q20_angular_3m2_minus_jj1'] for r in qrows)
summary['single_j_quadrupole_trace']=qtrace
summary['toy_shell_warning']='m denotes projection about the chosen quantization axis, not an experimentally assigned Nilsson orbital or an actual neutron number.'
(OUT/'model_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')

# Antisymmetric axial Slater determinants of holes in a complete g9/2 shell.
# Select removed time-reversed pairs. These are T-even quadrupole controls,
# not cranked AMR wavefunctions; radial/reduced angular factor is omitted.
from itertools import combinations
paired_rows=[]
jp=4.5
positive_m=[0.5,1.5,2.5,3.5,4.5]
for pair_count in (1,2):
    for ms in combinations(positive_m,pair_count):
        removed_q=sum(2*(3*m*m-jp*(jp+1)) for m in ms)
        paired_rows.append({'hole_count':2*pair_count,'removed_abs_m_pairs':';'.join(map(str,ms)),
            'q20_missing_particle_angular':removed_q,'q20_hole_relative_closed_shell':-removed_q,
            'ratio_to_two_hole_abs_m_4p5':removed_q/72.0})
with (OUT/'g9_2_hole_quadrupole_controls.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(paired_rows[0]));w.writeheader();w.writerows(paired_rows)
summary['g9_2_hole_quadrupole_controls']={
    'count':len(paired_rows),'two_hole_abs_m_4p5_Qh':-72.0,
    'four_hole_abs_m_4p5_3p5_Qh':-96.0,
    'four_hole_abs_m_4p5_0p5_Qh':-24.0,
    'warning':'Axial T-even Slater quadrupole controls; not fitted/cranked AMR states. Common radial/angular factor omitted.'}
(OUT/'model_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
