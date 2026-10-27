"""Synthetic Pauli metric audit. No CH13 actual inputs, nuclear data, or author code."""
from pathlib import Path
import json
import math
import platform
import numpy as np
import scipy
from scipy.linalg import eigh_tridiagonal

HERE = Path(__file__).resolve().parent
A = math.pi / 2
HBAR = 1.0
B0 = 1.0
ALPHA = 0.7
KAPPA = 18.0
WELL = 0.85
GRIDS = [127, 255, 511, 1023, 2047, 4095]
REFERENCE_N = 16383


def mass(phi, kind):
    if kind == 'constant':
        return np.ones_like(phi)
    if kind == 'even_variable':
        return 1.0 + ALPHA * phi**2
    if kind == 'asymmetric':
        return 1.0 + 0.3 * phi
    raise ValueError(kind)


def potential(phi, kind):
    if kind == 'zero':
        return np.zeros_like(phi)
    if kind == 'double_well':
        return KAPPA * (phi**2 - WELL**2)**2
    raise ValueError(kind)


def solve_tridiagonal(diag, off, levels=4):
    return eigh_tridiagonal(diag, off, select='i', select_range=(0, levels - 1),
                            lapack_driver='stebz', tol=1e-12)


def fv_generalized(n, mass_kind, potential_kind, levels=4):
    """Integrated FV: S psi = E M psi; M_i=h sqrt(B_i) positive."""
    h = 2 * A / (n + 1)
    phi = np.linspace(-A, A, n + 2)[1:-1]
    faces = np.linspace(-A + h / 2, A - h / 2, n + 1)
    b = mass(phi, mass_kind)
    w = np.sqrt(b)
    p_faces = 1.0 / np.sqrt(mass(faces, mass_kind))
    m = h * w
    diag_s = HBAR**2 / (2*h) * (p_faces[:-1] + p_faces[1:]) + m * potential(phi, potential_kind)
    off_s = -HBAR**2 / (2*h) * p_faces[1:-1]
    diag = diag_s / m
    off = off_s / np.sqrt(m[:-1] * m[1:])
    energies, vec = solve_tridiagonal(diag, off, levels)
    psi = vec / np.sqrt(m[:, None])
    return energies, psi, phi, m, diag, off


def x_of_phi(phi, mass_kind):
    if mass_kind == 'constant':
        return phi.copy() if isinstance(phi, np.ndarray) else phi
    if mass_kind == 'even_variable':
        return 0.5 * (phi * np.sqrt(1 + ALPHA * phi**2) + np.arcsinh(np.sqrt(ALPHA)*phi)/np.sqrt(ALPHA))
    raise ValueError(mass_kind)


def phi_of_x(x, mass_kind):
    if mass_kind == 'constant':
        return x.copy()
    # Newton inversion of analytic x(phi); no FV grid, interpolation or eigenvectors reused.
    phi = x * A / x_of_phi(A, mass_kind)
    for _ in range(12):
        phi -= (x_of_phi(phi, mass_kind) - x) / np.sqrt(mass(phi, mass_kind) / B0)
    return phi


def x_grid(n, mass_kind, potential_kind):
    left = float(x_of_phi(-A, mass_kind))
    right = float(x_of_phi(A, mass_kind))
    h = (right - left) / (n + 1)
    x = np.linspace(left, right, n + 2)[1:-1]
    phi = phi_of_x(x, mass_kind)
    diag = np.full(n, HBAR**2 / (B0 * h*h)) + potential(phi, potential_kind)
    off = np.full(n-1, -HBAR**2 / (2*B0*h*h))
    energies, vec = solve_tridiagonal(diag, off)
    inverse_error = float(np.max(np.abs(x_of_phi(phi, mass_kind) - x)))
    return energies, inverse_error


def flat_phi(n, potential_kind):
    """u=B^(1/4)psi: -hbar²/2 D(B^-1 D) + V + Q_B in flat dphi."""
    h = 2*A/(n+1)
    phi = np.linspace(-A, A, n+2)[1:-1]
    faces = np.linspace(-A+h/2, A-h/2, n+1)
    b = mass(phi, 'even_variable')
    bp = 2*ALPHA*phi
    bpp = 2*ALPHA
    p_faces = 1/mass(faces, 'even_variable')
    q = HBAR**2/2 * (bpp/(4*b*b) - 7*bp*bp/(16*b**3))
    diag = HBAR**2/(2*h*h)*(p_faces[:-1]+p_faces[1:]) + potential(phi, potential_kind) + q
    off = -HBAR**2/(2*h*h)*p_faces[1:-1]
    energies, _ = solve_tridiagonal(diag, off)
    return energies


def row(n, mass_kind, potential_kind):
    ef, *_ = fv_generalized(n, mass_kind, potential_kind)
    ex, inv_err = x_grid(n, mass_kind, potential_kind)
    result = {'n_interior':n, 'fv_generalized':ef.tolist(), 'x_grid':ex.tolist(),
              'max_fv_x_difference':float(np.max(np.abs(ef-ex))), 'x_inverse_residual':inv_err}
    if mass_kind == 'even_variable':
        eu = flat_phi(n, potential_kind)
        result['flat_phi_u'] = eu.tolist()
        result['max_flat_phi_x_difference'] = float(np.max(np.abs(eu-ex)))
    return result


def limit_case(mass_kind):
    length = float(x_of_phi(A, mass_kind)-x_of_phi(-A, mass_kind))
    exact = np.array([HBAR**2 * math.pi**2*k*k/(2*B0*length*length) for k in range(1,5)])
    rows = []
    for n in [127,255,511,1023]:
        r = row(n,mass_kind,'zero')
        r['max_fv_exact_error'] = float(np.max(np.abs(np.array(r['fv_generalized'])-exact)))
        r['max_x_exact_error'] = float(np.max(np.abs(np.array(r['x_grid'])-exact)))
        rows.append(r)
    return {'mass_kind':mass_kind,'x_box_length':length,'exact_E':exact.tolist(),'grids':rows}


def packet_diagnostics(n):
    e, psi, phi, m, diag, off = fv_generalized(n,'even_variable','double_well')
    # Fix relative sign so (psi0+psi1)/sqrt2 is predominantly at phi<0.
    sign = np.sign(phi)
    m01 = float(np.sum(m*psi[:,0]*psi[:,1]*sign))
    if m01 > 0:
        psi[:,1] *= -1
        m01 = -m01
    gap = float(e[1]-e[0])
    gram = psi.T @ (m[:,None]*psi)
    parity_error = [float(np.max(np.abs(psi[:,j]-((-1)**j)*psi[::-1,j]))) for j in range(4)]
    odd_expect = [float(np.sum(m*psi[:,j]**2*sign)) for j in range(4)]
    time_rows=[]
    for phase in [0,math.pi/2,math.pi,3*math.pi/2,2*math.pi]:
        time = phase/gap
        packet = (np.exp(-1j*e[0]*time)*psi[:,0]+np.exp(-1j*e[1]*time)*psi[:,1])/np.sqrt(2)
        norm = float(np.sum(m*np.abs(packet)**2))
        signed = float(np.sum(m*np.abs(packet)**2*sign))
        time_rows.append({'phase_gap_t':phase,'t_dimensionless':time,'norm':norm,
                         'sign_expectation':signed,'analytic_m01_cos':m01*math.cos(phase),
                         'P_left_half_at_zero':(1-signed)/2,'P_right_half_at_zero':(1+signed)/2})
    weighted_phi2 = float(np.sum(m*psi[:,0]**2*phi**2))
    naive_phi2 = float(np.sum(psi[:,0]**2*phi**2)/np.sum(psi[:,0]**2))
    # Algebraic unitary measure conversion on the same quadrature, not an independent spectrum check.
    b = mass(phi,'even_variable')
    h = 2*A/(n+1)
    u = b[:,None]**.25*psi
    unitary_gram = h * u.T @ u
    return {'n':n,'energies':e.tolist(),'gap':gap,'max_weighted_orthonormality_error':float(np.max(np.abs(gram-np.eye(4)))),
            'max_flat_u_gram_difference':float(np.max(np.abs(unitary_gram-gram))),
            'parity_max_amplitude_errors':parity_error,'eigenstate_odd_sign_expectations':odd_expect,
            'm01':m01,'half_transfer_t':math.pi/gap,'full_return_t':2*math.pi/gap,
            'time_rows':time_rows,'ground_phi2_correct_measure':weighted_phi2,'ground_phi2_wrong_flat_psi':naive_phi2,
            'warning':'Dimensionless synthetic unitary two-level packet, not nuclear lifetime or decoherence prediction.'}


def main():
    results={'scope':'Synthetic smooth positive mass / even V on a Dirichlet interval. Not CH13 actual producer or 133Ce/135Nd prediction.',
             'parameters':{'phi_interval':[-A,A],'hbar':HBAR,'B0':B0,'B_even':'1+0.7 phi²','V':'18(phi²−0.85²)²','barrier_V0':KAPPA*WELL**4},
             'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
             'constant_mass_zero_potential':limit_case('constant'),
             'variable_mass_zero_potential':limit_case('even_variable')}
    rows=[row(n,'even_variable','double_well') for n in GRIDS]
    ref, inv = x_grid(REFERENCE_N,'even_variable','double_well')
    prev, _ = x_grid(8191,'even_variable','double_well')
    extrap=ref+(ref-prev)/3
    for r in rows:
        r['max_fv_ref_error']=float(np.max(np.abs(np.array(r['fv_generalized'])-ref)))
        r['max_x_ref_error']=float(np.max(np.abs(np.array(r['x_grid'])-ref)))
    results['double_well_convergence']={'grids':rows,'x_reference_n':REFERENCE_N,'x_reference_E':ref.tolist(),
        'x_reference_inverse_residual':inv,'x_8191_to_16383_E_change':(ref-prev).tolist(),
        'second_order_Richardson_E':extrap.tolist(),'Richardson_is_conditional':'Assumes leading h² error; no experimental uncertainty.'}
    results['packet']=packet_diagnostics(4095)
    ea, pa, phi, m, *_=fv_generalized(4095,'asymmetric','double_well')
    results['V_even_B_not_even_counterexample']={'B':'1+0.3phi >0 on box','V_even':True,
        'B_even':False,'energies':ea.tolist(),'ground_sign_expectation':float(np.sum(m*pa[:,0]**2*np.sign(phi))),
        'interpretation':'V even alone does not make H reflection symmetric.'}
    (HERE/'results.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps({'reference_E':ref.tolist(),'reference_gap':float(ref[1]-ref[0]),
        'reference_grid_change_max':float(np.max(np.abs(ref-prev))),
        'finest_three_route_differences':{k:v for k,v in rows[-1].items() if k.startswith('max_')},
        'packet':results['packet'],'asymmetric_counterexample':results['V_even_B_not_even_counterexample']},indent=2))

if __name__=='__main__':
    main()
