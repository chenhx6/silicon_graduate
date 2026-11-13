#!/usr/bin/env python3
"""Independent analytic cascade and quadrature checks of the frozen didactic producer."""
import ast
import hashlib
import json
import math
from pathlib import Path
import numpy as np
from scipy.integrate import quad_vec

HERE = Path(__file__).resolve().parent
producer = HERE / 'a130_lifetime_response_figure.frozen.py'
# Extract and execute only the nested shape function; never call main() or write Img/.
tree = ast.parse(producer.read_text())
node = next(n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == 'dsam_shape')
module = ast.fix_missing_locations(ast.Module(body=[node], type_ignores=[]))
namespace = {'np': np, 'E0': 1000.0, 'dE_max': 20.0, 'sig_det': 1.2}
exec(compile(module, str(producer), 'exec'), namespace)
shape = namespace['dsam_shape']

# B -> i -> ground, unit initial B population. a=1/tau_B; b=1/tau_i.
a,b,t,v = 0.5,0.2,3.0,6.0
ub = math.exp(-a*t)
ui = (a*math.exp(-b*t)-b*math.exp(-a*t))/(a-b)
su = a*(math.exp(-b*t)-math.exp(-a*t))/(a-b)
ss = 1-ub-su
gate = 1-ub
ss_dot = b*su
gate_dot = a*ub
su_dot = gate_dot-ss_dot
fraction = ss/gate
fraction_dot = (ss_dot*gate-ss*gate_dot)/(gate*gate)
res = {
 'model': {'description':'One initially populated B feeds i with probability 1; constant speed; ideal full-acceptance detection.', 'tau_B_ps':1/a,'tau_i_ps':1/b,'time_ps':t,'v_um_per_ps':v,'x_um':v*t},
 'singles': {'U_i':ui,'U_B':ub,'dS_i_dt':b*(ui-ub),'corrected_tau_ps':(ui-ub)/(b*(ui-ub)),'omitting_feeding_tau_ps':ui/(b*(ui-ub)),'dS_dt_plus_dU_dt':0.0},
 'direct_gate': {'I_su':su,'I_ss':ss,'gate_total':gate,'gate_total_derivative_per_ps':gate_dot,'dI_ss_dt':ss_dot,'minus_dI_su_dt':-su_dot,'correct_tau_ps':su/ss_dot,'wrong_tau_from_negative_dI_su_ps':su/(-su_dot),'per_distance_normalized_naive_tau_ps':(su/gate)/fraction_dot,'normalized_fraction_derivative_per_ps':fraction_dot},
}
E=np.linspace(990,1030,800); sig=1.2; E0=1000.; de=20.; ts=0.8
checks=[]
for tau in (0.1,0.8,5.0):
    observed=shape(E,tau)
    # Independent continuous-time quadrature: emission before stopping plus stopped Gaussian.
    gaussian=lambda y: np.exp(-0.5*(y/sig)**2)/(sig*np.sqrt(2*np.pi))
    exact=np.exp(-ts/tau)*gaussian(E-E0)+quad_vec(lambda q: np.exp(-q/tau)/tau*gaussian(E-(E0+de*(1-q/ts))), 0, ts, epsabs=1e-10, epsrel=1e-10)[0]
    checks.append({'tau_ps':tau,'frozen_area_990_1030':float(np.trapezoid(observed,E)), 'correct_area_990_1030':float(np.trapezoid(exact,E)), 'frozen_area_outside_flight_energy_interval':float(np.trapezoid(np.where((E<1000)|(E>1020),observed,0.),E)), 'correct_area_outside_flight_energy_interval':float(np.trapezoid(np.where((E<1000)|(E>1020),exact,0.),E)), 'max_absolute_difference_per_keV':float(np.max(np.abs(observed-exact)))})
res['dsam']={'description':'Gaussian resolution sigma=1.2 keV; linear velocity-to-energy over 0.8 ps, then stopped; unit total probability. Finite 990–1030 keV energy window.', 'grid_spacing_keV':float(E[1]-E[0]), 'producer_kernel_spacing_keV':3.0/20., 'results':checks}
res['provenance']={'producer_sha256':hashlib.sha256(producer.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'numpy_version':np.__version__}
(HERE/'results.json').write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(res,indent=2,ensure_ascii=False))
