#!/usr/bin/env python3
"""
double_beta_decay_nme_calculator.py
===================================
Neutrinoless Double Beta Decay (0nu-beta-beta) Nuclear Matrix Element (NME),
Phase Space Factor G_0nu & Majorana Mass Sensitivity Analyzer.

Physics & Formulation:
----------------------
1. Half-Life & Effective Majorana Neutrino Mass:
   (T_1/2^0nu)^(-1) = G_0nu(Q, Z) * |M_0nu|^2 * (<m_bb> / m_e)^2
   where:
     G_0nu: Phase space factor (yr^-1).
     M_0nu = M_GT^0nu - (g_V / g_A)^2 * M_F^0nu + M_T^0nu: Nuclear Matrix Element.
     <m_bb> = | sum_i U_ei^2 * m_i |: Effective Majorana neutrino mass.
     m_e = 511 keV.

2. Benchmark Isotope Data (Engel & Menendez 2017 / PDG):
   - 76Ge:  Q_bb = 2039.0 keV, G_0nu = 2.36e-15 yr^-1, NME range = [2.8, 5.5]
   - 130Te: Q_bb = 2527.5 keV, G_0nu = 1.42e-14 yr^-1, NME range = [1.5, 4.0]
   - 136Xe: Q_bb = 2457.8 keV, G_0nu = 1.46e-14 yr^-1, NME range = [1.5, 4.2]
   - 100Mo: Q_bb = 3034.4 keV, G_0nu = 1.59e-14 yr^-1, NME range = [2.5, 6.0]
   - 82Se:  Q_bb = 2997.9 keV, G_0nu = 1.02e-14 yr^-1, NME range = [2.0, 4.5]

3. g_A Quenching Impact:
   Standard decay rate scales as g_A^4:
     Gamma_0nu propto g_A^4 * |M_0nu|^2
   Quenched g_A ~ 1.0 (vs unquenched 1.27) increases required half-life sensitivity
   by a factor of (1.27 / 1.0)^4 ~ 2.6.

4. Inversion Capabilities:
   - Given experimental half-life lower limit T_1/2 -> inverts upper bound on <m_bb> (meV).
   - Given target Majorana mass <m_bb> -> predicts required half-life sensitivity.

References:
  - J. Engel and J. Menendez, Rep. Prog. Phys. 80, 046301 (2017).
  - J. Suhonen and O. Civitarese, Phys. Rep. 300, 123 (1998).
  - S. Dell'Oro et al., Adv. High Energy Phys. 2016, 2162659 (2016).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple

M_E_KEV = 510.99895

ISOTOPES = {
    "76Ge":  {"name": "Germanium-76",  "Q_bb_keV": 2039.0, "G_0nu_yr": 2.36e-15, "nme_nominal": 4.0, "nme_range": [2.8, 5.5]},
    "130Te": {"name": "Tellurium-130", "Q_bb_keV": 2527.5, "G_0nu_yr": 1.42e-14, "nme_nominal": 2.8, "nme_range": [1.5, 4.0]},
    "136Xe": {"name": "Xenon-136",     "Q_bb_keV": 2457.8, "G_0nu_yr": 1.46e-14, "nme_nominal": 3.0, "nme_range": [1.5, 4.2]},
    "100Mo": {"name": "Molybdenum-100", "Q_bb_keV": 3034.4, "G_0nu_yr": 1.59e-14, "nme_nominal": 4.5, "nme_range": [2.5, 6.0]},
    "82Se":  {"name": "Selenium-82",   "Q_bb_keV": 2997.9, "G_0nu_yr": 1.02e-14, "nme_nominal": 3.5, "nme_range": [2.0, 4.5]}
}


def invert_majorana_mass_limit(
    isotope_key: str = "76Ge",
    half_life_limit_yr: float = 1.8e26,
    g_A_factor: float = 1.27
) -> Dict[str, Any]:
    """
    Computes upper bound on effective Majorana mass <m_bb> in meV from experimental
    half-life limit T_1/2^0nu.
    """
    if isotope_key not in ISOTOPES:
        raise ValueError(f"Unknown isotope: {isotope_key}")

    iso = ISOTOPES[isotope_key]
    G_0nu = iso["G_0nu_yr"]
    nme_min, nme_max = iso["nme_range"]

    # g_A scaling relative to unquenched 1.27
    quenching_ratio = (g_A_factor / 1.27) ** 2

    # <m_bb> / m_e = 1 / [ M_0nu * sqrt(G_0nu * T_12) ]
    def get_mass_meV(nme: float) -> float:
        eff_nme = nme * quenching_ratio
        denom = eff_nme * math.sqrt(G_0nu * half_life_limit_yr)
        if denom > 0:
            m_ratio = 1.0 / denom
            return m_ratio * M_E_KEV * 1e6  # to meV
        return float("inf")

    m_bb_max = get_mass_meV(nme_min)  # smaller NME gives larger mass bound
    m_bb_min = get_mass_meV(nme_max)  # larger NME gives smaller mass bound
    m_bb_nom = get_mass_meV(iso["nme_nominal"])

    # Hierarchy regime classification
    if m_bb_nom > 50.0:
        regime = "Degenerate_Mass_Regime (<m_bb> > 50 meV)"
    elif m_bb_nom >= 15.0:
        regime = "Inverted_Hierarchy_Regime (15 <= <m_bb> <= 50 meV)"
    else:
        regime = "Normal_Hierarchy_Regime (<m_bb> < 15 meV, next-generation ton-scale frontier)"

    return {
        "isotope": iso["name"],
        "Q_bb_keV": iso["Q_bb_keV"],
        "phase_space_G0nu_yr": G_0nu,
        "experimental_half_life_limit_yr": half_life_limit_yr,
        "g_A_axial_vector_coupling": g_A_factor,
        "NME_nominal": iso["nme_nominal"],
        "NME_uncertainty_range": iso["nme_range"],
        "effective_majorana_mass_upper_bound_meV": round(m_bb_nom, 1),
        "majorana_mass_interval_meV": [round(m_bb_min, 1), round(m_bb_max, 1)],
        "neutrino_mass_hierarchy_regime": regime
    }


def predict_half_life_for_target_mass(
    isotope_key: str = "76Ge",
    target_mass_meV: float = 20.0,
    g_A_factor: float = 1.27
) -> Dict[str, Any]:
    """
    Predicts required 0nu-beta-beta half-life (in years) to reach a target
    Majorana mass sensitivity (e.g. 20 meV covering the inverted hierarchy).
    """
    iso = ISOTOPES[isotope_key]
    G_0nu = iso["G_0nu_yr"]
    nme = iso["nme_nominal"]

    quenching_ratio = (g_A_factor / 1.27) ** 2
    eff_nme = nme * quenching_ratio

    # <m_bb> in keV
    m_bb_keV = target_mass_meV * 1e-6
    ratio_m = m_bb_keV / M_E_KEV

    # (T_1/2)^(-1) = G * M^2 * ratio^2
    rate = G_0nu * (eff_nme ** 2) * (ratio_m ** 2)
    t_12_pred_yr = 1.0 / max(rate, 1e-40)

    return {
        "isotope": iso["name"],
        "target_majorana_mass_meV": target_mass_meV,
        "effective_NME": round(eff_nme, 2),
        "predicted_required_half_life_yr": t_12_pred_yr,
        "predicted_half_life_scientific": f"{t_12_pred_yr:.2e} yr"
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   0nu-beta-beta NUCLEAR MATRIX ELEMENT & MAJORANA MASS ANALYZER")
    lines.append("=" * 72)

    lim = summary["mass_limit"]
    lines.append(f" ISOTOPE: {lim['isotope']} (Q_bb = {lim['Q_bb_keV']} keV, G_0nu = {lim['phase_space_G0nu_yr']:.2e} yr^-1)")
    lines.append(f"   Experimental Half-Life Limit   : T_1/2 > {lim['experimental_half_life_limit_yr']:.2e} yr")
    lines.append(f"   Axial Coupling g_A             : {lim['g_A_axial_vector_coupling']} (Unquenched = 1.27)")
    lines.append(f"   Nuclear Matrix Element (NME)   : {lim['NME_nominal']} (Range: {lim['NME_uncertainty_range']})")
    lines.append("-" * 72)
    lines.append(" EFFECTIVE MAJORANA MASS SENSITIVITY:")
    lines.append(f"   Nominal Upper Bound <m_bb>     : < {lim['effective_majorana_mass_upper_bound_meV']} meV")
    lines.append(f"   Theoretical NME Range Interval : <m_bb> in [{lim['majorana_mass_interval_meV'][0]} - {lim['majorana_mass_interval_meV'][1]}] meV")
    lines.append(f"   Hierarchy Status               : {lim['neutrino_mass_hierarchy_regime']}")
    lines.append("-" * 72)

    if "predicted_half_life" in summary:
        pr = summary["predicted_half_life"]
        lines.append(f" INVERTED HIERARCHY BENCHMARK COVERAGE (<m_bb> = {pr['target_majorana_mass_meV']} meV):")
        lines.append(f"   Required Half-Life Sensitivity : T_1/2 > {pr['predicted_half_life_scientific']}")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - 0nu-beta-beta is the unique probe of lepton number violation and Majorana mass.")
    lines.append("   - NME uncertainty (~ factor of 2) propagates into neutrino mass extraction.")
    lines.append("   - Connects nuclear structure calculations (QRPA, Shell Model) with cosmology.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="0nu-beta-beta Nuclear Matrix Element & Majorana Mass Analyzer."
    )
    parser.add_argument("--iso", type=str, default="76Ge", choices=list(ISOTOPES.keys()),
                        help="Candidate isotope (76Ge, 130Te, 136Xe, 100Mo, 82Se)")
    parser.add_argument("--t12", type=float, default=1.8e26, help="Experimental half-life limit in years (default: 1.8e26 for LEGEND/GERDA)")
    parser.add_argument("--gA", type=float, default=1.27, help="Axial-vector coupling constant g_A (default: 1.27)")
    parser.add_argument("--target-m", type=float, default=20.0, help="Target Majorana mass in meV to predict required T_1/2")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    limit_res = invert_majorana_mass_limit(args.iso, args.t12, args.gA)
    pred_res = predict_half_life_for_target_mass(args.iso, args.target_m, args.gA)

    summary = {
        "mass_limit": limit_res,
        "predicted_half_life": pred_res
    }

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
