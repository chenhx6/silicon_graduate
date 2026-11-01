#!/usr/bin/env python3
"""
Electric Dipole Polarizability (alpha_D), Neutron Skin Thickness & Nuclear Matter EOS Calculator.

Based on:
  - A. Tamii et al., Phys. Rev. Lett. 107, 062502 (2011) (Complete dipole response & neutron skin of 208Pb)
  - X. Roca-Maza et al., Phys. Rev. Lett. 106, 252501 (2011) (Droplet model & polarizability)
  - J. Piekarewicz et al., Phys. Rev. C 85, 041302(R) (2012) (Electric dipole polarizability & neutron skin)
  - J. M. Lattimer & M. Prakash, Astrophys. J. 550, 426 (2001) (Neutron star radius & EOS slope L)
  - J. Birkhan et al., Phys. Rev. Lett. 118, 252501 (2017) (Polarizability & skin of 48Ca)

Features:
  1. Computes electric dipole polarizability alpha_D (in fm^3) from photoabsorption inverse-energy-weighted cross section sigma_-2.
  2. Integrates photoabsorption spectra sigma(E) to evaluate sigma_-2 = int sigma(E) / E^2 dE.
  3. Estimates macroscopic droplet model polarizability from volume symmetry energy J and surface stiffness Q.
  4. Inverts neutron skin thickness delta_r_np (in fm) from experimental polarizability across 208Pb, 120Sn, and 48Ca.
  5. Extracts symmetry energy slope parameter L (in MeV), pure neutron matter pressure P_PNM, and neutron star radius R_1.4.
"""

import numpy as np

# Physical constants
HBAR_C_MEV_FM = 197.3269804  # MeV * fm
E2_CONST_MEV_FM = 1.439965   # e^2 in MeV * fm


def calculate_polarizability_from_sigma_minus2(sigma_minus2_mb_MeV_inv):
    """
    Compute electric dipole polarizability alpha_D (in fm^3):
      alpha_D = (hbar*c / (2 * pi^2)) * sigma_-2
      where 1 mb = 0.1 fm^2.
      Conversion factor = (hbar*c / (2 * pi^2)) * 0.1 approx 0.999670 fm^3 / (mb / MeV).
    """
    s_m2 = float(sigma_minus2_mb_MeV_inv)
    if s_m2 <= 0:
        raise ValueError("sigma_-2 must be strictly positive.")

    factor = (HBAR_C_MEV_FM / (2.0 * (np.pi ** 2))) * 0.1
    alpha_d_fm3 = factor * s_m2

    return {
        "sigma_minus2_mb_MeV_inv": s_m2,
        "conversion_factor": float(factor),
        "alpha_D_fm3": float(alpha_d_fm3)
    }


def integrate_dipole_polarizability_from_spectrum(E_grid_MeV, cross_section_mb):
    """
    Numerically integrate experimental photoabsorption cross section spectrum:
      sigma_-2 = int [ sigma(E) / E^2 ] dE
      and compute alpha_D = (hbar*c / (2 * pi^2)) * sigma_-2.
    """
    E = np.array(E_grid_MeV, dtype=float)
    sig = np.array(cross_section_mb, dtype=float)

    if len(E) != len(sig):
        raise ValueError("Energy and cross section arrays must have identical length.")
    if len(E) < 2:
        raise ValueError("At least 2 points required for numerical integration.")
    if np.any(E <= 0):
        raise ValueError("Photon energy E must be strictly positive.")

    integrand = sig / (E ** 2)
    trapezoid_func = getattr(np, 'trapezoid', getattr(np, 'trapz', None))
    sigma_minus2 = float(trapezoid_func(integrand, E))

    factor = (HBAR_C_MEV_FM / (2.0 * (np.pi ** 2))) * 0.1
    alpha_d_fm3 = factor * sigma_minus2

    return {
        "E_min_MeV": float(E[0]),
        "E_max_MeV": float(E[-1]),
        "points_count": len(E),
        "sigma_minus2_integrated_mb_MeV_inv": float(sigma_minus2),
        "alpha_D_fm3": float(alpha_d_fm3)
    }


def droplet_model_polarizability_estimate(A, Z, J_bulk_MeV=32.0, Q_surf_MeV=35.0, R0_fm=1.2):
    """
    Estimate macroscopic droplet model electric dipole polarizability:
      alpha_D approx (pi * e^2 / 54) * (A * <r^2> / J) * [ 1 + (5/3) * (9*J / (4*Q)) * A^(-1/3) ].
    """
    a_f = float(A)
    z_f = float(Z)
    r2_ms = 0.6 * (float(R0_fm) ** 2) * (a_f ** (2.0 / 3.0))

    j = float(J_bulk_MeV)
    q = float(Q_surf_MeV)

    pre = (np.pi * E2_CONST_MEV_FM / 54.0) * (a_f * r2_ms / j)
    surf_corr = 1.0 + (5.0 / 3.0) * (9.0 * j / (4.0 * q)) * (a_f ** (-1.0 / 3.0))
    alpha_d_drop = pre * surf_corr

    return {
        "A": int(A),
        "Z": int(Z),
        "J_bulk_MeV": j,
        "Q_surf_MeV": q,
        "rms_radius_fm": float(np.sqrt(r2_ms)),
        "surface_correction_factor": float(surf_corr),
        "alpha_D_droplet_fm3": float(alpha_d_drop)
    }


def extract_neutron_skin_from_polarizability(alpha_D_fm3, target_nucleus="208Pb"):
    """
    Extract neutron skin thickness delta_r_np = <r_n^2>^(1/2) - <r_p^2>^(1/2) in fm:
      For 208Pb: delta_r_np approx 0.0125 * (alpha_D - 7.5) +/- 0.024 fm
      For 120Sn: delta_r_np approx 0.0195 * (alpha_D - 1.2) +/- 0.028 fm
      For 48Ca:  delta_r_np approx 0.0750 * (alpha_D - 0.25) +/- 0.035 fm.
    """
    ad = float(alpha_D_fm3)
    nuc = target_nucleus.strip()

    if "208" in nuc or "Pb" in nuc:
        skin = 0.0125 * (ad - 7.5)
        err = 0.024
        target_name = "208Pb"
    elif "120" in nuc or "Sn" in nuc:
        skin = 0.0195 * (ad - 1.2)
        err = 0.028
        target_name = "120Sn"
    elif "48" in nuc or "Ca" in nuc:
        skin = 0.0750 * (ad - 0.25)
        err = 0.035
        target_name = "48Ca"
    else:
        # Default scaling
        skin = 0.0125 * (ad - 7.5)
        err = 0.030
        target_name = target_nucleus

    return {
        "target_nucleus": target_name,
        "input_alpha_D_fm3": ad,
        "delta_r_np_fm": float(skin),
        "uncertainty_fm": float(err)
    }


def extract_symmetry_energy_slope_L(delta_r_np_fm):
    """
    Extract EOS symmetry energy slope parameter L (in MeV) and pure neutron matter pressure:
      L approx 420.0 * delta_r_np - 20.0 (in MeV).
      P_PNM(rho_0) approx (1/3) * rho_0 * L (in MeV / fm^3) with rho_0 = 0.16 fm^-3.
    """
    skin = float(delta_r_np_fm)
    l_slope = 420.0 * skin - 20.0

    # Pressure in MeV / fm^3
    rho_0 = 0.16
    p_pnm = (1.0 / 3.0) * rho_0 * l_slope

    # Convert to dyn / cm^2: 1 MeV / fm^3 = 1.6021766e33 dyn / cm^2
    p_dyn_cm2 = p_pnm * 1.6021766e33

    return {
        "delta_r_np_fm": skin,
        "L_slope_MeV": float(l_slope),
        "P_PNM_rho0_MeV_fm3": float(p_pnm),
        "P_PNM_rho0_dyn_cm2": float(p_dyn_cm2)
    }


def predict_neutron_star_radius_from_L(L_slope_MeV, M_solar=1.4):
    """
    Predict astrophysical neutron star radius R_1.4M (in km) from EOS slope parameter L:
      R_1.4 approx 12.0 * (L / 45.0)^0.20 (km).
    """
    l_val = max(10.0, float(L_slope_MeV))
    r_ns_km = 12.0 * ((l_val / 45.0) ** 0.20)

    return {
        "L_slope_MeV": l_val,
        "M_neutron_star_solar_mass": float(M_solar),
        "predicted_radius_R_NS_km": float(r_ns_km)
    }
