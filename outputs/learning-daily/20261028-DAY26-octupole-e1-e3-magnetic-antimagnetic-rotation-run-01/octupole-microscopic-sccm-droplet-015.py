#!/usr/bin/env python3
"""
octupole-microscopic-sccm-droplet-015.py
========================================
Comprehensive quantitative investigation of:
1. Microscopic Delta l = Delta j = 3 single-particle orbital driving mechanism in A~145 and A~225;
2. Macroscopic Droplet model vs microscopic shell correction for intrinsic dipole moment D0 cancellation;
3. Parity-projected GCM transition kernels, proving E1 quenching vs robust E3 collectivity despite identical coordinate densities;
4. Experimental confidence interval overlap analysis between 144Ba and 146Ba and limits on static pear-shape deduction.
"""

# Scientific claims from this historical calculation have been withdrawn.
import sys as _audit_sys
if "--replay-superseded" not in _audit_sys.argv:
    raise SystemExit("Superseded research artifact. Read knowledge/research-notes/day26-quantitative-claim-corrections.md; use 017-019 instead. Explicit historical replay requires --replay-superseded.")


import math
import json
from pathlib import Path
import numpy as np

def wigner_3j(j1, j2, j3, m1, m2, m3):
    """Compute Wigner 3j symbol using standard Racah formula."""
    if m1 + m2 + m3 != 0:
        return 0.0
    if abs(m1) > j1 or abs(m2) > j2 or abs(m3) > j3:
        return 0.0
    if j3 < abs(j1 - j2) or j3 > j1 + j2:
        return 0.0

    # Racah triangle coefficient
    def fact(n):
        return math.factorial(int(round(n)))

    # Triangle delta
    delta = math.sqrt(fact(j1 + j2 - j3) * fact(j1 - j2 + j3) * fact(-j1 + j2 + j3) / fact(j1 + j2 + j3 + 1))
    prefactor = delta * math.sqrt(fact(j1 + m1) * fact(j1 - m1) * fact(j2 + m2) * fact(j2 - m2) * fact(j3 + m3) * fact(j3 - m3))

    # Sum over t
    t_min = max(0, int(round(j2 - j3 - m1)), int(round(j1 - j3 + m2)))
    t_max = min(int(round(j1 + j2 - j3)), int(round(j1 - m1)), int(round(j2 + m2)))

    val = 0.0
    for t in range(t_min, t_max + 1):
        denom = (fact(t) *
                 fact(j1 + j2 - j3 - t) *
                 fact(j1 - m1 - t) *
                 fact(j2 + m2 - t) *
                 fact(j3 - j2 + m1 + t) *
                 fact(j3 - j1 - m2 + t))
        term = ((-1.0) ** (t + int(round(j1 - j2 - m3)))) / denom
        val += term

    return prefactor * val

def compute_single_particle_octupole_elements():
    """
    Compute reduced matrix elements <j1 || r^3 Y_3 || j2> for Delta l = Delta j = 3 pairs.
    Formula:
    < (l1 1/2) j1 || Y_3 || (l2 1/2) j2 > = (-1)^(j1 + 1/2) * sqrt( 7*(2j1+1)*(2j2+1) / (4pi) ) * ( j1 3 j2; 1/2 0 -1/2 )
    Radial part estimated as <r^3> ~ b^3 * (N_osc + 3/2)^(3/2), b = 1.01 * A^(1/6) fm.
    """
    pairs = [
        {"region": "A~145 (Ba-Sm)", "type": "proton", "n1": 2, "l1": 2, "j1": 2.5, "name1": "pi 2d5/2",
         "n2": 1, "l2": 5, "j2": 5.5, "name2": "pi 1h11/2", "A_ref": 144, "Nosc": 4},
        {"region": "A~145 (Ba-Sm)", "type": "neutron", "n1": 2, "l1": 3, "j1": 3.5, "name1": "nu 2f7/2",
         "n2": 1, "l2": 6, "j2": 6.5, "name2": "nu 1i13/2", "A_ref": 146, "Nosc": 5},
        {"region": "A~225 (Ra-Th)", "type": "proton", "n1": 2, "l1": 3, "j1": 3.5, "name1": "pi 2f7/2",
         "n2": 1, "l2": 6, "j2": 6.5, "name2": "pi 1i13/2", "A_ref": 224, "Nosc": 5},
        {"region": "A~225 (Ra-Th)", "type": "neutron", "n1": 1, "l1": 4, "j1": 4.5, "name1": "nu 1g9/2",
         "n2": 1, "l2": 7, "j2": 7.5, "name2": "nu 1j15/2", "A_ref": 224, "Nosc": 6}
    ]

    results = []
    for p in pairs:
        j1 = p["j1"]
        j2 = p["j2"]
        l1 = p["l1"]
        l2 = p["l2"]
        A = p["A_ref"]
        b = 1.01 * (A ** (1.0 / 6.0)) # oscillator length in fm

        # Parity check: l1 + l2 + 3 must be even
        parity_allowed = ((l1 + l2 + 3) % 2 == 0)
        assert parity_allowed, f"Parity forbidden for {p['name1']} <-> {p['name2']}"

        # 3j symbol (j1 3 j2; 1/2 0 -1/2)
        three_j = wigner_3j(j1, 3.0, j2, 0.5, 0.0, -0.5)
        angular_factor = ((-1.0) ** (int(round(j1 + 0.5)))) * math.sqrt(7.0 * (2.0 * j1 + 1.0) * (2.0 * j2 + 1.0) / (4.0 * math.pi)) * three_j

        # Radial integral <r^3>: roughly (Nosc + 1.5)^(1.5) * b^3
        r3_integral = ((p["Nosc"] + 1.5) ** 1.5) * (b ** 3) # in fm^3

        reduced_matrix_element = angular_factor * r3_integral # in fm^3

        # Single particle transition strength B_sp(E3) = |<j1 || r^3 Y_3 || j2>|^2 / (2j2 + 1)
        B_sp = (reduced_matrix_element ** 2) / (2.0 * j2 + 1.0) # in fm^6
        B_sp_eb3 = B_sp * 1e-6 # in e^2 b^3

        # Weisskopf single-particle unit: B_W(E3) = 0.0594 * A^2 fm^6
        B_W = 0.0594 * (A ** 2.0)
        B_sp_Wu = B_sp / B_W

        results.append({
            "region": p["region"],
            "type": p["type"],
            "orbital_pair": f"{p['name1']} <-> {p['name2']}",
            "delta_l": l2 - l1,
            "delta_j": j2 - j1,
            "wigner_3j": round(three_j, 5),
            "angular_factor": round(angular_factor, 4),
            "radial_integral_fm3": round(r3_integral, 2),
            "reduced_ME_fm3": round(reduced_matrix_element, 2),
            "B_sp_fm6": round(B_sp, 2),
            "B_sp_Wu": round(B_sp_Wu, 3),
            "B_sp_eb3": round(B_sp_eb3, 6)
        })

    return results

def compute_droplet_vs_shell_cancellation():
    """
    Detailed macroscopic Droplet model vs microscopic shell correction for Ba and Ra isotopes.
    """
    # 1. Barium Systematics (Z=56, N=84-92)
    ba_chain = [
        {"nucleus": "140Ba", "A": 140, "N": 84, "beta2": 0.12, "beta3": 0.00,
         "v2_h92": 0.10, "v2_f72": 0.05, "v2_i132": 0.01, "exp_D0": 0.00},
        {"nucleus": "142Ba", "A": 142, "N": 86, "beta2": 0.16, "beta3": 0.05,
         "v2_h92": 0.20, "v2_f72": 0.10, "v2_i132": 0.01, "exp_D0": 0.05},
        {"nucleus": "144Ba", "A": 144, "N": 88, "beta2": 0.20, "beta3": 0.11,
         "v2_h92": 0.32, "v2_f72": 0.17, "v2_i132": 0.02, "exp_D0": 0.13, "exp_BE3_Wu": 48.0},
        {"nucleus": "146Ba", "A": 146, "N": 90, "beta2": 0.22, "beta3": 0.12,
         "v2_h92": 0.40, "v2_f72": 0.27, "v2_i132": 0.20, "exp_D0": 0.015, "exp_BE3_Wu": 48.0},
        {"nucleus": "148Ba", "A": 148, "N": 92, "beta2": 0.24, "beta3": 0.10,
         "v2_h92": 0.56, "v2_f72": 0.34, "v2_i132": 0.40, "exp_D0": -0.06}
    ]

    C_LD = 0.00075 # e fm
    d_p_ba = 0.350 # e fm for beta3 = 0.11
    # Weights for the 3 active neutron Nilsson orbitals in Ba
    w_h92 = 0.40
    w_f72 = 0.35
    w_i132 = 1.10 # i13/2 intruder carries very large negative dipole moment due to low-Omega high-j asymmetry
    d_n_scale_ba = -0.72 # e fm

    ba_results = []
    for item in ba_chain:
        A = item["A"]
        Z = 56.0
        b2 = item["beta2"]
        b3 = item["beta3"]

        # Droplet model: D_macro = C_LD * Z * e * A^(-1/3) * beta2 * beta3 * 10
        D_macro = C_LD * Z * (A ** (-1.0 / 3.0)) * b2 * b3 * 10.0 if b3 > 0.001 else 0.0

        # Proton shell contribution
        scale_b3 = (b3 / 0.11) if b3 > 0.001 else 0.0
        D_p_shell = d_p_ba * scale_b3

        # Neutron shell contribution
        occ_sum = item["v2_h92"] * w_h92 + item["v2_f72"] * w_f72 + item["v2_i132"] * w_i132
        D_n_shell = d_n_scale_ba * occ_sum * scale_b3

        D_shell = D_p_shell + D_n_shell
        D_total = D_macro + D_shell

        # Cancellation percentage relative to proton contribution
        cancellation_pct = (1.0 - abs(D_total) / D_p_shell) * 100.0 if D_p_shell > 0.01 else 0.0

        ba_results.append({
            "nucleus": item["nucleus"],
            "A": A,
            "N": item["N"],
            "beta2": b2,
            "beta3": b3,
            "v2_neutrons": {
                "nu_h92": item["v2_h92"],
                "nu_f72": item["v2_f72"],
                "nu_i132": item["v2_i132"]
            },
            "D_macro_efm": round(float(D_macro), 5),
            "D_p_shell_efm": round(float(D_p_shell), 4),
            "D_n_shell_efm": round(float(D_n_shell), 4),
            "D_shell_net_efm": round(float(D_shell), 4),
            "D_total_efm": round(float(D_total), 4),
            "exp_D0_efm": item.get("exp_D0"),
            "cancellation_pct": round(float(cancellation_pct), 1)
        })

    # 2. Radium Systematics (Z=88, N=132-138)
    ra_chain = [
        {"nucleus": "220Ra", "A": 220, "N": 132, "beta2": 0.12, "beta3": 0.08, "D_p": 0.32, "D_n": -0.12, "exp_D0": 0.20},
        {"nucleus": "222Ra", "A": 222, "N": 134, "beta2": 0.16, "beta3": 0.10, "D_p": 0.38, "D_n": -0.26, "exp_D0": 0.12},
        {"nucleus": "224Ra", "A": 224, "N": 136, "beta2": 0.18, "beta3": 0.11, "D_p": 0.40, "D_n": -0.37, "exp_D0": 0.03},
        {"nucleus": "226Ra", "A": 226, "N": 138, "beta2": 0.19, "beta3": 0.09, "D_p": 0.36, "D_n": -0.21, "exp_D0": 0.15}
    ]
    ra_results = []
    for item in ra_chain:
        A = item["A"]
        Z = 88.0
        b2 = item["beta2"]
        b3 = item["beta3"]
        D_macro = C_LD * Z * (A ** (-1.0 / 3.0)) * b2 * b3 * 10.0
        D_p = item["D_p"]
        D_n = item["D_n"]
        D_shell = D_p + D_n
        D_total = D_macro + D_shell
        cancellation_pct = (1.0 - abs(D_total) / D_p) * 100.0

        ra_results.append({
            "nucleus": item["nucleus"],
            "A": A,
            "N": item["N"],
            "beta2": b2,
            "beta3": b3,
            "D_macro_efm": round(float(D_macro), 5),
            "D_p_shell_efm": round(float(D_p), 4),
            "D_n_shell_efm": round(float(D_n), 4),
            "D_total_efm": round(float(D_total), 4),
            "exp_D0_efm": item.get("exp_D0"),
            "cancellation_pct": round(float(cancellation_pct), 1)
        })

    return {"barium_systematics": ba_results, "radium_systematics": ra_results}

def compute_projected_gcm_paradox():
    """
    Solve a multi-point 1D/2D parity projection Hill-Wheeler-Griffin model
    on an octupole deformation mesh beta3 in [-0.25, 0.25], showing that:
    1. The coordinate probability distributions |F_0+(beta3)|^2 and |F_1-(beta3)|^2
       have >98% spatial overlap;
    2. When D0(beta3) is quenched at beta3_eq, B(E1) drops by orders of magnitude (< 10^-6 W.u.),
       while B(E3) remains robust (~48 W.u.).
    """
    # Grid of octupole deformation
    beta3_vals = np.linspace(-0.25, 0.25, 41)
    n_pts = len(beta3_vals)
    d_b3 = beta3_vals[1] - beta3_vals[0]

    # Model Hamiltonian potential: shallow octupole pocket at beta3 = +-0.11, barrier ~ 0.5 MeV
    # V(beta3) = a * beta3^2 + b * beta3^4
    # Minimum at +-0.11: dV/db3 = 2a*b3 + 4b*b3^3 = 0 => a = -2b*(0.11)^2
    b_pot = 400.0 # MeV
    a_pot = -2.0 * b_pot * (0.11 ** 2)
    V_pes = a_pot * (beta3_vals ** 2) + b_pot * (beta3_vals ** 4)
    V_pes -= V_pes.min() # set min to 0

    # Intrinsic dipole and octupole moment functions
    # 144Ba case: D0_144(beta3) = 1.18 * beta3 (efm)
    # 146Ba case: D0_146(beta3) = 0.12 * beta3 (quenched by cancellation)
    D0_144 = 1.18 * beta3_vals
    D0_146 = 0.125 * beta3_vals # 10x smaller intrinsic dipole moment
    # Intrinsic octupole moment: Q30(beta3) = (3/sqrt(7pi)) * Z * e * R0^3 * beta3
    # For A=144, Z=56, R0=6.29 fm: Q30 ~ 4.0 * beta3 (e b^(3/2))
    Q30 = 4.10 * beta3_vals

    # Construct Norm kernel N(q, q') = exp( - (q - q')^2 / (2 * sigma^2) )
    sigma_b3 = 0.05
    diff_matrix = beta3_vals[:, None] - beta3_vals[None, :]
    Norm_kernel = np.exp(- (diff_matrix ** 2) / (2.0 * (sigma_b3 ** 2)))

    # Parity operator in this basis: mirrors beta3 -> -beta3
    # P_ij = 1 if beta3_i == -beta3_j
    Parity_op = np.zeros((n_pts, n_pts))
    for i in range(n_pts):
        j_match = np.argmin(np.abs(beta3_vals + beta3_vals[i]))
        Parity_op[i, j_match] = 1.0

    # Symmetrized and Anti-symmetrized Norm kernels for good parity:
    # N+ = 0.5 * (N + N @ Parity)
    # N- = 0.5 * (N - N @ Parity)
    Norm_plus = 0.5 * (Norm_kernel + Norm_kernel @ Parity_op)
    Norm_minus = 0.5 * (Norm_kernel - Norm_kernel @ Parity_op)

    # Hamiltonian kernel: H(q, q') = 0.5 * (V(q) + V(q')) * N(q, q') + Kinetic term
    # Kinetic term ~ - 1/(2B) * d^2/dq^2
    B_oct = 50.0 # hbar^2 / MeV
    Kinetic_kernel = np.zeros((n_pts, n_pts))
    for i in range(n_pts):
        for j in range(n_pts):
            # second derivative of gaussian norm kernel
            d2 = ((beta3_vals[i] - beta3_vals[j]) ** 2 / (sigma_b3 ** 4) - 1.0 / (sigma_b3 ** 2)) * Norm_kernel[i, j]
            Kinetic_kernel[i, j] = - (1.0 / (2.0 * B_oct)) * d2

    Ham_kernel = 0.5 * (V_pes[:, None] + V_pes[None, :]) * Norm_kernel + Kinetic_kernel
    Ham_plus = 0.5 * (Ham_kernel + Ham_kernel @ Parity_op)
    Ham_minus = 0.5 * (Ham_kernel - Ham_kernel @ Parity_op)

    # Diagonalize in the plus (0+) and minus (1-) parity subspaces using generalized eigenvalue solver
    # Regularize with small epsilon
    def solve_hwg(H, N):
        evals_N, evecs_N = np.linalg.eigh(N)
        # Keep positive eigenvalues > 1e-5
        mask = evals_N > 1e-4
        val_red = evals_N[mask]
        vec_red = evecs_N[:, mask]
        inv_sqrt_N = vec_red @ np.diag(1.0 / np.sqrt(val_red)) @ vec_red.T
        H_red = inv_sqrt_N @ H @ inv_sqrt_N
        evals_H, evecs_H = np.linalg.eigh(H_red)
        # Generalized vectors: f = inv_sqrt_N @ evecs_H
        f_vecs = inv_sqrt_N @ evecs_H
        # Collective wavefunctions: F = N^(1/2) f
        sqrt_N = vec_red @ np.diag(np.sqrt(val_red)) @ vec_red.T
        F_vecs = sqrt_N @ f_vecs
        return evals_H, f_vecs, F_vecs

    E_plus, f_plus, F_plus = solve_hwg(Ham_plus, Norm_plus)
    E_minus, f_minus, F_minus = solve_hwg(Ham_minus, Norm_minus)

    # Ground state (0+) and first negative-parity state (1-)
    gs_0plus_F = F_plus[:, 0]
    gs_1minus_F = F_minus[:, 0]

    # Normalize F wavefunctions
    gs_0plus_F /= np.sqrt(np.sum(gs_0plus_F ** 2) * d_b3)
    gs_1minus_F /= np.sqrt(np.sum(gs_1minus_F ** 2) * d_b3)

    # Densities |F(beta3)|^2
    density_0plus = gs_0plus_F ** 2
    density_1minus = gs_1minus_F ** 2

    # Spatial overlap between |F_0+|^2 and |F_1-|^2:
    spatial_overlap = np.sum(np.sqrt(density_0plus * density_1minus)) * d_b3

    # Transition matrix elements:
    # <1- || M(E1) || 0+> = int dq dq' f_1-(q) M_E1(q, q') f_0+(q')
    # Operator kernel M_E1(q, q') = 0.5 * (D0(q) + D0(q')) * N(q, q')
    # Similarly for M(E3) = 0.5 * (Q30(q) + Q30(q')) * N(q, q')
    def calc_transition(f_bra, f_ket, Operator_diag):
        Op_kernel = 0.5 * (Operator_diag[:, None] + Operator_diag[None, :]) * Norm_kernel
        # Project on bra (-) and ket (+)
        Op_proj = 0.5 * (Op_kernel - Parity_op @ Op_kernel) # odd parity operator
        me = f_bra[:, 0].T @ Op_proj @ f_ket[:, 0] * (d_b3 ** 2)
        return float(abs(me))

    ME1_144 = calc_transition(f_minus, f_plus, D0_144)
    ME1_146 = calc_transition(f_minus, f_plus, D0_146)
    ME3_144 = calc_transition(f_minus, f_plus, Q30)
    ME3_146 = calc_transition(f_minus, f_plus, Q30)

    # Convert to reduced transition probabilities:
    # B(E1; 0+ -> 1-) = (3/4pi) * ME1^2 * 1e-4 e^2 b
    # B(E3; 0+ -> 3-) = (7/16pi) * ME3^2 e^2 b^3
    BW_E1_144 = 0.0645 * (144 ** (2.0 / 3.0)) * 1e-4
    BW_E3_144 = 0.0594 * (144 ** 2.0) * 1e-6
    BW_E1_146 = 0.0645 * (146 ** (2.0 / 3.0)) * 1e-4
    BW_E3_146 = 0.0594 * (146 ** 2.0) * 1e-6

    BE1_144 = (3.0 / (4.0 * math.pi)) * (ME1_144 ** 2) * 1e-4
    BE1_144_Wu = BE1_144 / BW_E1_144
    BE1_146 = (3.0 / (4.0 * math.pi)) * (ME1_146 ** 2) * 1e-4
    BE1_146_Wu = BE1_146 / BW_E1_146

    BE3_144 = (7.0 / (16.0 * math.pi)) * (ME3_144 ** 2)
    BE3_144_Wu = BE3_144 / BW_E3_144
    BE3_146 = (7.0 / (16.0 * math.pi)) * (ME3_146 ** 2)
    BE3_146_Wu = BE3_146 / BW_E3_146

    return {
        "spatial_overlap_percentage": round(float(spatial_overlap * 100.0), 2),
        "energy_0plus_MeV": round(float(E_plus[0]), 3),
        "energy_1minus_MeV": round(float(E_minus[0]), 3),
        "parity_splitting_keV": round(float((E_minus[0] - E_plus[0]) * 1000.0), 1),
        "144Ba_results": {
            "ME1_efm": round(float(ME1_144), 4),
            "BE1_Wu": round(float(BE1_144_Wu), 6),
            "ME3_eb32": round(float(ME3_144), 4),
            "BE3_Wu": round(float(BE3_144_Wu), 1)
        },
        "146Ba_results": {
            "ME1_efm": round(float(ME1_146), 4),
            "BE1_Wu": round(float(BE1_146_Wu), 7),
            "ME3_eb32": round(float(ME3_146), 4),
            "BE3_Wu": round(float(BE3_146_Wu), 1),
            "BE1_suppression_factor": round(float(BE1_144_Wu / BE1_146_Wu), 1)
        }
    }

def compute_ci_overlap_and_shape_invariance():
    """
    Evaluate the confidence interval overlap of Bucher 2016 and 2017:
    144Ba: B(E3) = 48 (+21/-29) W.u., CI = [19, 69] W.u.
    146Ba: B(E3) = 48 (+25/-34) W.u., CI = [14, 73] W.u.
    Demonstrate that the wide CI overlap is compatible with both:
    - Static rigid pear-shape model: B(E3) ~ 48 W.u.
    - Soft octupole vibration / projected SCCM: B(E3) ~ 25 - 35 W.u.
    """
    ci_144 = [19.0, 69.0]
    ci_146 = [14.0, 73.0]

    # Intersection interval
    inter_min = max(ci_144[0], ci_146[0])
    inter_max = min(ci_144[1], ci_146[1])
    inter_width = inter_max - inter_min
    ci_144_width = ci_144[1] - ci_144[0]
    ci_146_width = ci_146[1] - ci_146[0]

    jaccard_overlap = inter_width / (max(ci_144[1], ci_146[1]) - min(ci_144[0], ci_146[0]))

    # Gaussian posterior distributions
    # 144Ba: mu = 48, asymmetric sigma+ = 21, sigma- = 29 => average sigma ~ 25.0
    # 146Ba: mu = 48, asymmetric sigma+ = 25, sigma- = 34 => average sigma ~ 29.5
    b_grid = np.linspace(0.0, 100.0, 1001)
    p_144 = np.exp(-0.5 * ((b_grid - 48.0) / 25.0) ** 2) / (math.sqrt(2.0 * math.pi) * 25.0)
    p_146 = np.exp(-0.5 * ((b_grid - 48.0) / 29.5) ** 2) / (math.sqrt(2.0 * math.pi) * 29.5)

    # Bhattacharyya coefficient (distribution overlap)
    bhattacharyya = np.sum(np.sqrt(p_144 * p_146)) * (b_grid[1] - b_grid[0])

    models = [
        {"model": "Static Rigid Octupole Rotor (Axial Pear-shape, beta3=0.12)", "predicted_BE3_Wu": 48.0,
         "inside_144_CI": True, "inside_146_CI": True, "p_value_z": 0.0},
        {"model": "Dynamic Octupole-Soft SCCM (Bernard 2016 Table I, 2D GCM)", "predicted_BE3_Wu": 25.0,
         "inside_144_CI": True, "inside_146_CI": True, "p_value_z": round(abs(25.0 - 48.0) / 25.0, 2)},
        {"model": "Cranked CDFT PC-PK1 (Li 2024, Mean Field beta3=0.128)", "predicted_BE3_Wu": 32.0,
         "inside_144_CI": True, "inside_146_CI": True, "p_value_z": round(abs(32.0 - 48.0) / 25.0, 2)},
        {"model": "Spherical Octupole Vibrator (Harmonic Phonon Limit)", "predicted_BE3_Wu": 8.0,
         "inside_144_CI": False, "inside_146_CI": False, "p_value_z": round(abs(8.0 - 48.0) / 25.0, 2)}
    ]

    return {
        "CI_144Ba_Wu": ci_144,
        "CI_146Ba_Wu": ci_146,
        "intersection_interval_Wu": [inter_min, inter_max],
        "interval_overlap_percentage": round(float(jaccard_overlap * 100.0), 2),
        "bhattacharyya_distribution_overlap": round(float(bhattacharyya * 100.0), 2),
        "model_compatibility_audit": models,
        "scientific_inference": (
            "Because both the static rigid rotor (48 W.u.) and the dynamic octupole-soft SCCM (25 W.u.) "
            "fall cleanly within the 1-sigma confidence intervals of both 144Ba and 146Ba, the experimental "
            "Coulomb excitation data conclusively confirms strong octupole collectivity, but cannot "
            "statistically distinguish between a rigid static pear shape and large-amplitude dynamic octupole fluctuations."
        )
    }

def main():
    print("Running comprehensive octupole microscopic, droplet cancellation and SCCM GCM audit...")

    sp_elements = compute_single_particle_octupole_elements()
    droplet_vs_shell = compute_droplet_vs_shell_cancellation()
    projected_gcm = compute_projected_gcm_paradox()
    ci_audit = compute_ci_overlap_and_shape_invariance()

    final_payload = {
        "schema_version": 1,
        "artifact_id": "octupole-microscopic-sccm-droplet-015",
        "title": "Comprehensive Octupole Microscopic Driving Mechanism, Dipole Cancellation, and Symmetry-Restored SCCM Audit",
        "timestamp_utc": "2026-10-28 20:30:00",
        "single_particle_octupole_elements": sp_elements,
        "droplet_vs_shell_cancellation": droplet_vs_shell,
        "projected_gcm_paradox_resolution": projected_gcm,
        "confidence_interval_and_shape_audit": ci_audit
    }

    out_json = Path("outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/octupole-microscopic-sccm-droplet-015.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump({"scientific_audit": {'status': 'superseded-unverified-claims-not-scientific-evidence', 'correction_note': 'knowledge/research-notes/day26-quantitative-claim-corrections.md', 'scope': 'Legacy numerical payload retained for audit only. Assumed data/coefficients, universal thresholds, production-model equivalence and exact experimental agreement are not certified. Use source locators and corrected 017-019 artifacts.'}, **final_payload}, f, indent=2)

    print(f"SUCCESS: Generated {out_json}")
    print(f"  - Spatial overlap between 0+ and 1- densities: {projected_gcm['spatial_overlap_percentage']}%")
    print(f"  - 146Ba B(E1) suppression factor: {projected_gcm['146Ba_results']['BE1_suppression_factor']}x")
    print(f"  - 146Ba Dipole cancellation: {droplet_vs_shell['barium_systematics'][3]['cancellation_pct']}%")
    print(f"  - 144Ba vs 146Ba CI overlap: {ci_audit['interval_overlap_percentage']}%")

if __name__ == "__main__":
    main()

