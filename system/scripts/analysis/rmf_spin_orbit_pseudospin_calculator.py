#!/usr/bin/env python3
"""
Relativistic Mean Field (RMF), Spin-Orbit Coupling & Pseudospin Symmetry (PSS) Calculator.

Based on:
  - B. D. Serot & J. D. Walecka, Adv. Nucl. Phys. 16, 1 (1986) (Relativistic nuclear many-body theory)
  - P. Ring, Prog. Part. Nucl. Phys. 37, 193 (1996) (RMF theory in finite nuclei)
  - J. N. Ginocchio, Phys. Rev. Lett. 78, 436 (1997) (Pseudospin as a relativistic symmetry)
  - J. Meng et al., Phys. Rev. C 58, R628 (1998) & PRL 82, 3819 (1999) (RMF pseudospin symmetry)
  - H. Liang, S. Shen, P. Zhao, J. Meng, Phys. Rep. 570, 1 (2015) (Hidden symmetries in relativistic nuclear physics)
  - S. Guo et al., Phys. Rev. Lett. 124, 192501 (2020) (Pseudospin-chiral quartet bands in 131Ba)

Features:
  1. Computes RMF scalar potential S(r), vector potential V(r), central potential V+S, and spin-orbit potential V_SO(r).
  2. Estimates single-particle spin-orbit energy splitting Delta E_SO from the gradient of V(r) - S(r).
  3. Maps pseudospin partner doublets (n, l, j=l+1/2) and (n-1, l+2, j=l+3/2) to pseudo-orbital tilde(l) = l + 1.
  4. Quantifies pseudospin splitting Delta E_PSS and evaluates the Ginocchio relativistic symmetry quality factor.
  5. Diagnoses candidate pseudospin-chiral quartet band manifolds (e.g. 131Ba D3-D6) from experimental level energies.
"""

import numpy as np

# Physical constants
HBAR_C_MEV_FM = 197.3269804  # MeV * fm
M_NUCLEON_MEV = 938.272088    # MeV / c^2


def calculate_rmf_potentials(r_grid_fm, S0_MeV=-420.0, V0_MeV=350.0, R0_fm=6.5, a_fm=0.65):
    """
    Compute Woods-Saxon parametrization of RMF scalar potential S(r),
    vector potential V(r), effective central binding potential V_cent(r) = V + S,
    and relativistic spin-orbit generating potential V_diff(r) = V - S.
    """
    r = np.array(r_grid_fm, dtype=float)
    if np.any(r < 0):
        raise ValueError("Radial coordinate r must be non-negative.")

    # Woods-Saxon form factor
    f = 1.0 / (1.0 + np.exp((r - float(R0_fm)) / float(a_fm)))
    df_dr = - (1.0 / float(a_fm)) * f * (1.0 - f)

    S_r = float(S0_MeV) * f
    V_r = float(V0_MeV) * f
    V_cent = V_r + S_r
    V_diff = V_r - S_r

    # Relativistic spin-orbit potential: (hbar*c / (2 * m * c^2))^2 * (1 / r) * d(V - S)/dr
    # Prefactor = (hbar*c)^2 / [2 * (M_NUCLEON_MEV)^2] in fm^2
    prefactor_so = (HBAR_C_MEV_FM ** 2) / (2.0 * (M_NUCLEON_MEV ** 2))

    # Avoid division by zero at origin
    r_safe = np.maximum(1e-4, r)
    v_diff_deriv = (float(V0_MeV) - float(S0_MeV)) * df_dr
    V_so = prefactor_so * (1.0 / r_safe) * (- v_diff_deriv)

    return {
        "r_grid_fm": r.tolist(),
        "S_r_MeV": S_r.tolist(),
        "V_r_MeV": V_r.tolist(),
        "V_cent_MeV": V_cent.tolist(),
        "V_diff_MeV": V_diff.tolist(),
        "V_SO_MeV_fm2": V_so.tolist(),
        "central_depth_origin_MeV": float(V_cent[0]),
        "diff_potential_origin_MeV": float(V_diff[0])
    }


def estimate_spin_orbit_splitting(l_orbital, A):
    """
    Estimate normal single-particle spin-orbit energy splitting:
      Delta E_SO(l, A) = E(j = l - 1/2) - E(j = l + 1/2)
      Delta E_SO approx (2*l + 1) * 13.0 * A^(-2/3) (in MeV).
    """
    l_f = float(l_orbital)
    a_f = float(A)
    if l_f < 1.0 or a_f <= 0.0:
        raise ValueError("Orbital l must be >= 1 and A must be > 0.")

    delta_so = (2.0 * l_f + 1.0) * 13.0 * (a_f ** (-2.0 / 3.0))

    return {
        "l_orbital": int(l_f),
        "A": int(a_f),
        "j_lower": l_f - 0.5,
        "j_higher": l_f + 0.5,
        "Delta_E_SO_estimated_MeV": float(delta_so)
    }


def map_pseudospin_partner(n_principal, l_orbital):
    """
    Map a single-particle state (n, l, j=l+1/2) to its pseudospin partner:
      Partner state: (n - 1, l + 2, j=l+3/2).
      Pseudo-orbital angular momentum: tilde(l) = l + 1.
      Pseudospin: tilde(s) = 1/2.
      Both states share j = tilde(l) - 1/2 and j = tilde(l) + 1/2.
    """
    n1 = int(n_principal)
    l1 = int(l_orbital)
    j1 = l1 + 0.5

    n2 = n1 - 1
    l2 = l1 + 2
    j2 = l1 + 1.5

    tilde_l = l1 + 1

    return {
        "state_1": f"{n1}{l_to_spectroscopic(l1)}_{int(2*j1)}/2",
        "state_2": f"{n2}{l_to_spectroscopic(l2)}_{int(2*j2)}/2",
        "pseudo_orbital_tilde_l": tilde_l,
        "pseudo_spectroscopic": f"tilde({l_to_spectroscopic(tilde_l)})",
        "pseudospin_j1": j1,
        "pseudospin_j2": j2
    }


def l_to_spectroscopic(l):
    mapping = {0: "s", 1: "p", 2: "d", 3: "f", 4: "g", 5: "h", 6: "i", 7: "j"}
    return mapping.get(l, f"l{l}")


def evaluate_pseudospin_symmetry_quality(E_state1_MeV, E_state2_MeV, Delta_E_SO_MeV):
    """
    Quantify pseudospin symmetry (PSS) quality:
      Delta E_PSS = |E_state1 - E_state2|.
      Quality factor Q_PSS = Delta E_PSS / Delta E_SO.
      If Q_PSS < 0.15: High-grade relativistic pseudospin symmetry.
    """
    e1 = float(E_state1_MeV)
    e2 = float(E_state2_MeV)
    so = float(Delta_E_SO_MeV)

    delta_pss = abs(e1 - e2)
    q_pss = delta_pss / max(1e-5, so)

    if q_pss < 0.15:
        diagnosis = f"High-Grade Pseudospin Symmetry: PSS splitting {delta_pss*1000:.1f} keV is only {q_pss*100:.1f}% of normal spin-orbit split."
        is_good = True
    elif q_pss < 0.35:
        diagnosis = f"Moderate Pseudospin Symmetry: PSS splitting {delta_pss*1000:.1f} keV is {q_pss*100:.1f}% of normal spin-orbit split."
        is_good = True
    else:
        diagnosis = f"Heavily Broken Pseudospin Symmetry: PSS splitting {delta_pss*1000:.1f} keV exceeds 35% of spin-orbit split."
        is_good = False

    return {
        "Delta_E_PSS_MeV": float(delta_pss),
        "Delta_E_SO_MeV": float(so),
        "Q_PSS_ratio": float(q_pss),
        "is_good_pseudospin_symmetry": is_good,
        "diagnosis": diagnosis
    }


def diagnose_pseudospin_chiral_quartet_manifold(spins, band1_keV, band2_keV, band3_keV, band4_keV):
    """
    Analyze a 4-band manifold (e.g. 131Ba D3-D6) for pseudospin-chiral quartet characteristics:
      1. Evaluates energy spread Delta E_quartet(I) across the four bands.
      2. Detects whether quartet dispersion remains below 500 keV across the spin sequence.
    """
    sp = np.array(spins, dtype=float)
    b1 = np.array(band1_keV, dtype=float)
    b2 = np.array(band2_keV, dtype=float)
    b3 = np.array(band3_keV, dtype=float)
    b4 = np.array(band4_keV, dtype=float)

    n_spins = len(sp)
    if not (len(b1) == len(b2) == len(b3) == len(b4) == n_spins):
        raise ValueError("All 4 band energy arrays must have the same length as spins array.")

    dispersions = []
    for i in range(n_spins):
        ens = [b1[i], b2[i], b3[i], b4[i]]
        disp = max(ens) - min(ens)
        dispersions.append(disp)

    avg_dispersion_keV = float(np.mean(dispersions))
    max_dispersion_keV = float(np.max(dispersions))

    if avg_dispersion_keV < 450.0:
        is_candidate = True
        diag = (f"Candidate Pseudospin-Chiral Quartet: Average 4-band dispersion is {avg_dispersion_keV:.1f} keV (< 450 keV), "
                f"supporting dual spontaneous breaking of chiral and pseudospin symmetries.")
    else:
        is_candidate = False
        diag = (f"Excessive 4-band energy dispersion ({avg_dispersion_keV:.1f} keV > 450 keV): "
                f"Bands likely originate from distinct quasiparticle configurations.")

    return {
        "spins": sp.tolist(),
        "dispersions_keV": dispersions,
        "average_dispersion_keV": avg_dispersion_keV,
        "max_dispersion_keV": max_dispersion_keV,
        "is_quartet_candidate": is_candidate,
        "diagnosis": diag
    }
