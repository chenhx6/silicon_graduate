"""Conditional AMR vector/tensor identities and literal Roy (2011) Eqs. 1,3-5.

No EDF, projected many-body calculation, fit, or experimental geometry inversion.
Only standard-library Python is required. Run this file to regenerate JSON and CSV.
"""
from pathlib import Path
import cmath
import csv
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent

def c2(n):
    x, y, z = n
    return {
        'C20': (3*z*z-1)/2,
        'C21': -math.sqrt(1.5)*z*complex(x,y),
        'C22': math.sqrt(3/8)*complex(x,y)**2,
    }

def blades(theta, phi=0):
    s,c = math.sin(theta),math.cos(theta)
    x,y=s*math.cos(phi),s*math.sin(phi)
    return (x,y,c),(-x,-y,c)

def tensor_pair(theta, phi=0, q1=1, q2=1):
    n1,n2=blades(theta,phi)
    a,b=c2(n1),c2(n2)
    return {k:q1*a[k]+q2*b[k] for k in a}

def mu_pair(theta,phi=0,gh1=1,gh2=1,jh1=4.5,jh2=4.5,gn=0.1,jn=10):
    a,b=blades(theta,phi)
    return tuple(gh1*jh1*a[i]+gh2*jh2*b[i]+(gn*jn if i==2 else 0) for i in range(3))

max_c21=0.0
max_t22_residual=0.0
max_mu_perp=0.0
max_tensor_rotation_residual=0.0
for it in range(181):
    t=math.pi*it/360
    for ip in range(31):
        p=2*math.pi*ip/31
        pair=tensor_pair(t,p)
        max_c21=max(max_c21,abs(pair['C21']))
        normalized_t22=pair['C22']/math.sqrt(3/8)
        analytic=2*math.sin(t)**2*cmath.exp(2j*p)
        max_t22_residual=max(max_t22_residual,abs(normalized_t22-analytic))
        mu=mu_pair(t,p)
        max_mu_perp=max(max_mu_perp,math.hypot(mu[0],mu[1]))
        rotated=tensor_pair(t,p+math.pi)
        for k in pair:
            max_tensor_rotation_residual=max(max_tensor_rotation_residual,abs(pair[k]-rotated[k]))
assert max_c21 < 1e-12
assert max_t22_residual < 1e-12
assert max_mu_perp < 1e-12
assert max_tensor_rotation_residual < 1e-12

angle_table=[]
for deg in (90,75,70,60,50,45,30,15,5,0):
    t=math.radians(deg)
    rel=math.sin(t)**4
    v=mu_pair(t)
    angle_table.append({'theta_deg':deg,'T21_abs':abs(tensor_pair(t)['C21']),
                        'normalized_T22':2*math.sin(t)**2,
                        'BE2_over_B90':rel,
                        'drop_factor_from_90':1/rel if rel>0 else None,
                        'illustrative_mu_perp':math.hypot(*v[:2]),
                        'illustrative_mu_z':v[2]})

asymmetry=[]
t=math.pi/4
for eps in (0,.001,.01,.05,.1):
    # Magnetic and electric weights are deliberately changed separately.
    mu=mu_pair(t,gh1=1+eps,gh2=1-eps)
    e=tensor_pair(t,q1=1+eps,q2=1-eps)
    asymmetry.append({'epsilon':eps,'magnetic_weight_mismatch_mu_x':mu[0],
                      'mu_x_analytic':9*eps*math.sin(t),
                      'BE2_weight_mismatch_abs_C21':abs(e['C21']),
                      'illustrative_semiclassical_BM1':3/(8*math.pi)*mu[0]**2})

# Source: Roy 2011 p.324 Eqs.3-5; p.325 parameter discussion.
jh,jn,J,Vpn,Vhh,n,Q=4.5,10,19.5,1.2,.15,4,1.1

def omega_sh(c):
    return (1.5*Vpn/jh)*c-(6*Vhh/(n*jh))*(2*c*c-1)*c

def spin(c, inertia):
    return jn+2*jh*c+inertia*omega_sh(c)

def solve_cos(I,inertia):
    if not spin(0,inertia)<=I<=spin(1,inertia):
        return None
    lo,hi=0.,1.
    for _ in range(90):
        c=(lo+hi)/2
        if spin(c,inertia)>I:
            hi=c
        else:
            lo=c
    return (lo+hi)/2

def be2(c):
    return 15/(32*math.pi)*Q**2*(1-c*c)**2

expt=[(16,1075,.36,.03,.14,.01), (18,1224,.23,.03,.12,.02),
      (20,1323,.17,.03,.11,.02),(22,1314,.21,.07,.09,.03),
      (24,1358,.27,.07,.06,.02)]
rows=[]
for I,eg,tau,etau,B,eB in expt:
    c=solve_cos(I,J)
    assert abs(spin(c,J)-I)<1e-12
    purec=solve_cos(I,0)
    R=J*omega_sh(c)
    dw_dc=1.5*Vpn/jh+6*Vhh/(n*jh)-36*Vhh/(n*jh)*c*c
    incremental=(J*dw_dc)/(2*jh+J*dw_dc)
    rows.append({'I':I,'Egamma_keV_reported':eg,'tau_ps_reported':tau,
                 'tau_error_ps_reported':etau,'BE2_reported_e2b2':B,
                 'BE2_error_reported_e2b2':eB,
                 'theta_deg_literal_Eq3':math.degrees(math.acos(c)),
                 'I_shears_hbar':jn+2*jh*c,'R_core_hbar':R,
                 'R_over_I':R/I,'dR_over_dI':incremental,
                 'BE2_literal_Eqs1and3_e2b2':be2(c),
                 'BE2_model_minus_reported':be2(c)-B,
                 'pure_shears_BE2_same_I':None if purec is None else be2(purec)})

# Differentiation of E_sh=Vpn P2(c)-Vhh/n*(P2(2c^2-1)-1).
# dE_sh/dc / dI_sh/dc must agree with Eq.4. This checks the potential factors.
max_energy_derivative_residual=0.
for it in range(101):
    c=it/100
    dE_dc=3*Vpn*c-12*Vhh/n*(2*c*c-1)*c
    max_energy_derivative_residual=max(max_energy_derivative_residual,abs(dE_dc/(2*jh)-omega_sh(c)))
assert max_energy_derivative_residual<1e-12

sources=[]
for rel,coverage in [
 ('raw/papers/gpt/day26-20261028/roy-2011-cd110-systematics-plb.pdf','5/5 pages read; Eqs.1-6, Table1, Figs3-4; pp323/325 visually inspected'),
 ('raw/papers/gpt/day26-20261028/rather-2014-104pd-antimagnetic-prc.pdf','only first journal page 061303-1 obtained, of 5 journal pages'),
 ('raw/papers/gpt/day26-20261028/zhang-2019-104pd-pnc-amr-arxiv1912.11990v1.pdf','8/8 PDF pages read; method p2, Fig3 p4, occupation/alignment pp4-7')]:
    p=ROOT/rel
    blob=p.read_bytes()
    sources.append({'path':rel,'pdf_signature_ok':blob.startswith(b'%PDF-'),
                    'bytes':len(blob),'sha256':hashlib.sha256(blob).hexdigest(),
                    'reading_coverage':coverage})

result={'status':'conditional-algebra-and-literal-source-recalculation',
 'claim_scope':'Not a microscopic nuclear wavefunction calculation or an experimental fit.',
 'tensor_convention':{
  'C2m':'sqrt(4*pi/5)*Y2m of unit direction; equal real quadrupole weights q1=q2=1',
  'normalized_T2m':'(C2m(n_plus)+C2m(n_minus))/sqrt(3/8)',
  'T21':'0','T22':'2*sin(theta)^2*exp(2i*phi); real 2*sin(theta)^2 only for phi=0',
  'physical_strength':'Roy Eq1 supplies its own Qeff normalization; the normalized angular tensor alone does not fix absolute B(E2)'},
 'grid':{'theta_count':181,'phi_count':31,'max_C21':max_c21,
          'max_T22_identity_residual':max_t22_residual,
          'max_mu_perp':max_mu_perp,
          'max_Rz_pi_tensor_invariance_residual':max_tensor_rotation_residual,
          'max_energy_potential_derivative_residual':max_energy_derivative_residual},
 'angle_table':angle_table,'symmetry_breaking_sensitivity':asymmetry,
 'symmetry_boundaries':['Rz(pi) exchanges equal blades and cancels odd tensor q expectations.',
  'T alone reverses nonzero total spin; AMR is not time reversal invariant at finite spin.',
  'TRy(pi) preserves an xz-plane vector geometry; this planar antiunitary symmetry is also possible for MR.',
  'mu_perp=0 is an intrinsic semiclassical expectation property, not a universal zero operator or arbitrary interband matrix element.',
  'Signature and parity are different; Rz(pi) does not establish good parity.'],
 'roy_parameters':{'jh':jh,'jn':jn,'J_hbar2_per_MeV':J,'Vpn_MeV':Vpn,'Vhh_MeV':Vhh,'n':n,'Qeff_eb':Q},
 'roy_spin_convention':'Literal printed Eq3, jn=10; no unreported I-offset fitted. Paper discusses a 12-hbar bandhead separately; these tabulations do not certify Fig4 reproduction.',
 'roy_comparison':rows,
 'spin_capacity':{'classical_frozen_jn_pure_max':spin(1,0),
                  'classical_literal_coupled_max':spin(1,J),
                  'finite_shell_two_identical_g9over2_holes_max_J':8,
                  'frozen_four_qp_finite_shell_max':18,
                  'source_rejects_highest_observed_28plus_as_AMR':True},
 'core_gain_16_to_24':{'delta_R_hbar':rows[-1]['R_core_hbar']-rows[0]['R_core_hbar'],
                       'delta_R_over_delta_I':(rows[-1]['R_core_hbar']-rows[0]['R_core_hbar'])/8,
                       'not_equal_to_total_spin_fraction_range':'R/I is 18.27%-26.21%; incremental gain fraction here is 42.10%'},
 'pd_boundary':'Zhang 2019 arXiv1912.11990v1 pp4-7: increased normal-rotation alignment does not ensure B(E2) flattening; fitting deformation epsilon2 decrease is needed for rapid high-frequency B(E2) fall; the shape fit is not an independent measurement.',
 'acquisition_failures':[{'url':'https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevC.89.061303/fulltext','status':401,'effect':'Rather2014 coverage remains first page only'}],
 'raw_fingerprints':sources}
(OUT/'amr_tensor_core_audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
with (OUT/'roy_literal_core_comparison.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
with (OUT/'angular_tensor_table.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=angle_table[0].keys());w.writeheader();w.writerows(angle_table)
print(json.dumps({'grid':result['grid'],'roy_rows':rows,'gain':result['core_gain_16_to_24']},indent=2))
