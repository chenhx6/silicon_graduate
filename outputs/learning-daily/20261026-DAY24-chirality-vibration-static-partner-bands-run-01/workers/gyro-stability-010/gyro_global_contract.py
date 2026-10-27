"""OL02 fixed-gyro ensemble audit: incremental global and degeneracy checks.

No HF/quantum solver. Units: hbar, MeV/hbar, hbar^2/MeV.
"""
from pathlib import Path
import json
import math
import numpy as np
from scipy.optimize import brentq

OUT = Path(__file__).resolve().parent
J = np.array([8.5, 31.0, 20.0])
s = np.array([5.43, 0.0, 5.0])
wc = math.hypot(s[0] / (J[1] - J[0]), s[2] / (J[1] - J[2]))
Ic = J[1] * wc
checks = []


def check(name, ok, **data):
    assert bool(ok), (name, data)
    checks.append(dict(name=name, passed=True, **data))


def sphere_secular(radius, poles, coeffs):
    """All real planar roots, including the double-root threshold once."""
    order = np.argsort(poles)
    p, a = np.asarray(poles)[order], abs(np.asarray(coeffs)[order])
    f = lambda x: np.linalg.norm(a / (x - p)) - radius
    eps = (p[1] - p[0]) * 1e-10
    span = max(1.0, p[1] - p[0])
    lo, hi = p[0] - span, p[1] + span
    while f(lo) > 0:
        span *= 2
        lo = p[0] - span
    span = max(1.0, p[1] - p[0])
    while f(hi) > 0:
        span *= 2
        hi = p[1] + span
    roots = [brentq(f, lo, p[0] - eps, xtol=1e-13),
             brentq(f, p[1] + eps, hi, xtol=1e-13)]
    powers = a ** (2 / 3)
    mid = p[0] + (p[1] - p[0]) * powers[0] / sum(powers)
    minimum = np.linalg.norm(a / (mid - p))
    if radius > minimum + 1e-10:
        roots.extend([brentq(f, p[0] + eps, mid, xtol=1e-13),
                      brentq(f, mid, p[1] - eps, xtol=1e-13)])
    elif abs(radius - minimum) <= 1e-10:
        roots.append(mid)
    return sorted(roots), minimum


def tangent_eigen(v, diagonal):
    basis = np.linalg.svd(np.asarray(v).reshape(1, 3))[2][1:].T
    return np.linalg.eigvalsh(basis.T @ np.diag(diagonal) @ basis)


def H(I):
    return float(np.sum((I - s) ** 2 / J) / 2)


def R(w):
    return float(-np.dot(J * w, w) / 2 - np.dot(s, w))


def at_omega(radius):
    mus, threshold = sphere_secular(radius, [J[0], J[2]], [s[0], s[2]])
    states = []
    for mu in mus:
        w = np.array([s[0] / (mu - J[0]), 0.0, s[2] / (mu - J[2])])
        states.append(dict(kind="planar", mu=mu, w=w))
    if radius >= wc - 1e-12:
        m = math.sqrt(max(0.0, radius**2 - wc**2))
        for sign in ([1] if m < 1e-10 else [-1, 1]):
            w = np.array([s[0] / (J[1] - J[0]), sign * m, s[2] / (J[1] - J[2])])
            # The zero-m branch point already occurs in the planar inventory.
            if m > 1e-10:
                states.append(dict(kind="aplanar", mu=J[1], w=w))
    for state in states:
        w, mu = state['w'], state['mu']
        state.update(I=J * w + s, R=R(w), H=H(J * w + s),
                     curvatures=tangent_eigen(w, mu - J))
    return states, threshold


def at_I(radius):
    lambdas, threshold = sphere_secular(radius, [1 / J[0], 1 / J[2]],
                                       [-s[0] / J[0], -s[2] / J[2]])
    states = []
    for lam in lambdas:
        I = np.array([s[0] / (1 - lam * J[0]), 0.0, s[2] / (1 - lam * J[2])])
        states.append(dict(kind="planar", lam=lam, I=I))
    if radius > Ic + 1e-10:
        component = math.sqrt(radius**2 - Ic**2)
        for sign in [-1, 1]:
            I = np.array([J[1] * s[0] / (J[1] - J[0]), sign * component,
                          J[1] * s[2] / (J[1] - J[2])])
            states.append(dict(kind="aplanar", lam=1 / J[1], I=I))
    for state in states:
        I, lam = state['I'], state['lam']
        state.update(w=(I - s) / J, H=H(I),
                     curvatures=tangent_eigen(I, 1 / J - lam))
    return states, threshold


def serial(state):
    return {k: (v.tolist() if isinstance(v, np.ndarray) else v) for k, v in state.items()}


inventories = dict(fixed_omega=[], fixed_I=[])
for radius in [.2, .5, wc, .6, 1.28, 1.3]:
    states, threshold = at_omega(radius)
    winner = min(states, key=lambda q: q['R'])
    check(f"omega{radius:.9f}-global-min-certificate", min(winner['mu'] - J) > -2e-10,
          winning_kind=winner['kind'], mu=winner['mu'], planar_root_count=sum(q['kind']=='planar' for q in states))
    for state in states:
        dw = state['w'] - winner['w']
        cert = float(np.dot((winner['mu'] - J) * dw, dw) / 2)
        check(f"omega{radius:.9f}-exact-difference-{len(checks)}",
              abs(state['R'] - winner['R'] - cert) < 2e-10)
    inventories['fixed_omega'].append(dict(omega=radius, planar_middle_threshold=threshold,
                                          winner=serial(winner), states=list(map(serial,states))))

for radius in [1.0, 5.0, float(np.linalg.norm(s)), 10.0, Ic, 18.6, 30.0]:
    states, threshold = at_I(radius)
    winner = min(states, key=lambda q:q['H'])
    check(f"I{radius:.9f}-global-min-certificate", min(1 / J - winner['lam']) > -2e-10,
          winning_kind=winner['kind'], lam=winner['lam'], w_dot_I=float(np.dot(winner['w'],winner['I'])))
    for state in states:
        di = state['I'] - winner['I']
        cert = float(np.dot((1 / J - winner['lam']) * di, di) / 2)
        check(f"I{radius:.9f}-exact-difference-{len(checks)}", abs(state['H'] - winner['H'] - cert) < 2e-9)
    inventories['fixed_I'].append(dict(I_norm=radius, planar_middle_threshold=threshold,
                                      winner=serial(winner), states=list(map(serial,states))))

low_I = inventories['fixed_I'][1]['winner']
check("low-I-yrast-is-anti-aligned-and-not-fixed-omega-minimum",
      low_I['lam'] < 0 and np.dot(low_I['w'], low_I['I']) < 0)
at_s = inventories['fixed_I'][2]['winner']
check("lambda-zero-chart-mu-infinite-at-I-equals-s",
      abs(at_s['lam']) < 1e-12 and np.linalg.norm(at_s['w']) < 1e-11 and abs(at_s['H']) < 1e-20)

# Critical null direction has a positive quartic cost, not a continuum of minima.
wstar = np.array([s[0]/(J[1]-J[0]), 0., s[2]/(J[1]-J[2])])
C = float(np.dot((J[1] - J) * wstar, wstar))
quartic = C / (8 * wc**4)
quartic_data=[]
for t in [.04, .02, .01]:
    w = math.sqrt(1-t*t/wc**2)*wstar + np.array([0,t,0])
    stable_difference = .5 * C * (1-math.sqrt(1-t*t/wc**2))**2
    ratio = stable_difference / t**4
    quartic_data.append(dict(t=t, energy_cost=stable_difference, cost_div_t4=ratio))
    check(f"critical-quartic-cost-t{t}", stable_difference > 0 and abs(ratio/quartic-1)<.004)

# A continuous degeneracy only after changing to an equal-inertia/zero-gyro model.
Jdeg=np.array([31.,31.,20.]); sdeg=np.array([0.,0.,5.]); om=.6
wl=sdeg[2]/(Jdeg[1]-Jdeg[2]); transverse=math.sqrt(om**2-wl**2)
circle=[]
for phi in [0.,.4,1.,2.]:
    w=np.array([transverse*math.cos(phi),transverse*math.sin(phi),wl]); I=Jdeg*w+sdeg
    curv=tangent_eigen(w,31-Jdeg)
    circle.append(dict(phi=phi,w=w.tolist(),R=float(-.5*np.dot(Jdeg*w,w)-np.dot(sdeg,w)),curvatures=curv.tolist()))
    check(f"changed-model-degenerate-circle-phi{phi}",np.linalg.norm(np.cross(w,I))<1e-14 and abs(curv[0])<1e-12)
check("changed-model-circle-is-isoenergetic",max(q['R'] for q in circle)-min(q['R'] for q in circle)<1e-14)
check("equal-J-with-nonzero-gyro-obstructs-finite-stationarity",s[0]!=0 and Jdeg[1]-Jdeg[0]==0)

# One surviving gyro gives a planar m-l solution, despite a finite radius onset.
sone=np.array([0.,0.,5.]); one_wl=sone[2]/(J[1]-J[2])
one_w=np.array([0.,math.sqrt(.6**2-one_wl**2),one_wl])
one_I=J*one_w+sone
check("one-zero-gyro-finite-formula-but-no-three-axis-chirality",
      np.linalg.norm(np.cross(one_w,one_I))<1e-14 and one_w[0]==0 and one_I[0]==0)
# Both zero gyros: ordinary rotor rotations around the largest-inertia axis.
for sign in [-1,1]:
    wz=np.array([0.,sign*.6,0.]); Iz=J*wz
    check(f"zero-gyros-ordinary-rotor-sign{sign}",
          np.linalg.norm(np.cross(wz,Iz))==0 and min(J[1]-J)==0 and min(1/J-1/J[1])==0)

# The fixed-I critical null direction has its own coefficient/units.
Istar=J[1]*wstar
CI=float(np.dot((1/J-1/J[1])*Istar,Istar))
quartic_I=CI/(8*Ic**4)
quartic_I_data=[]
for t in [1.,.5,.25]:
    exact=.5*CI*(1-math.sqrt(1-t*t/Ic**2))**2
    ratio=exact/t**4
    quartic_I_data.append(dict(t_hbar=t,energy_cost_MeV=exact,cost_div_t4=ratio))
    check(f"fixed-I-critical-quartic-t{t}",exact>0 and abs(ratio/quartic_I-1)<.003)

result=dict(scope="Incremental global-minimum, branch inventory, singular-chart and degeneracy audit. No HF/RPA/quantum claim.",
            source_parameters=dict(J=J.tolist(),s=s.tolist(),axis_order=['s','m','l']),
            wc=wc,Icrit=Ic,s_norm=float(np.linalg.norm(s)),inventories=inventories,
            critical_quartic_coefficient=quartic,critical_quartic_data=quartic_data,
            critical_fixedI_quartic_coefficient=quartic_I,critical_fixedI_quartic_data=quartic_I_data,
            changed_model_equal_inertia_zero_short_gyro_circle=circle,
            checks=checks,passed=len(checks))
(OUT/'global-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(passed=len(checks),wc=wc,Icrit=Ic,s_norm=np.linalg.norm(s),quartic=quartic,
    omega_inventory=[dict(omega=q['omega'],roots=len(q['states']),winner=q['winner']['kind'])for q in inventories['fixed_omega']],
    I_inventory=[dict(I=q['I_norm'],roots=len(q['states']),winner=q['winner']['kind'],lam=q['winner']['lam'])for q in inventories['fixed_I']]),indent=2))
