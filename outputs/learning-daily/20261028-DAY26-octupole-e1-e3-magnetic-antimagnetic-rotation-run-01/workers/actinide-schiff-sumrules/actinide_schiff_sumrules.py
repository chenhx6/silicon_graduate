#!/usr/bin/env python3
"""Microscopic perturbation sum rules and sensitivity ledger for actinide Schiff moments.

Reproducible numerical implementation for:
  - 223Ra, 225Ra, 225Ac, 227Ac vs 199Hg Schiff moment comparison
  - WKB double-well parity doublet energy splitting vs octupole deformation beta3
  - Meson exchange channel response coefficients (a0, a1, a2) and nuclear/atomic amplification
  - P,T-odd parameter cancellation blind spots (blind planes and cross-nucleus complementarity)
"""
from __future__ import annotations

import csv
import json
import math
from pathlib import Path


def compute_geometry(A: int, Z: int, beta2: float, beta3: float) -> dict[str, float]:
    """Compute intrinsic Schiff moment scales in e fm^3."""
    r0 = 1.2 * (A ** (1.0 / 3.0))
    exact_coeff = 9.0 / (20.0 * math.pi * math.sqrt(35.0))
    compact_coeff = 3.0 / (20.0 * math.pi)
    s_exact = exact_coeff * Z * (r0 ** 3) * beta2 * beta3
    s_compact = compact_coeff * Z * (r0 ** 3) * beta2 * beta3
    return {
        "R0_fm": r0,
        "S_intr_exact_e_fm3": s_exact,
        "S_intr_compact_e_fm3": s_compact,
    }


def lab_schiff_factor(J: float) -> float:
    """Return projection factor from intrinsic to laboratory Schiff moment for K=J."""
    return J / (J + 1.0)


def wkb_tunneling_splitting(beta3: float, mass_param: float = 75.0, omega0_keV: float = 1100.0) -> float:
    """WKB tunneling splitting in keV as a function of octupole deformation beta3."""
    if beta3 <= 0.01:
        return 2000.0
    action = 0.5 * mass_param * (beta3 ** 2)
    delta_e = omega0_keV * math.exp(-action)
    return max(delta_e, 5.0)


def run_calculations() -> tuple[dict, list[dict], list[dict], list[dict]]:
    # 1. Nuclear data ledger
    nuclei_data = [
        {
            "nuclide": "225Ra",
            "Z": 88,
            "N": 137,
            "A": 225,
            "J": 0.5,
            "J_str": "1/2",
            "parity_ground": "+",
            "delta_E_keV": 55.16,
            "partner_energy_keV": 55.16,
            "beta2": 0.190,
            "beta3": 0.146,
            "k_S_atomic": -8.5e-17,
            "a0": -1.5,
            "a1": 6.0,
            "a2": -4.0,
            "model": "Skyrme SkO_prime (finite range + src + direct + exch)",
        },
        {
            "nuclide": "223Ra",
            "Z": 88,
            "N": 135,
            "A": 223,
            "J": 1.5,
            "J_str": "3/2",
            "parity_ground": "+",
            "delta_E_keV": 50.13,
            "partner_energy_keV": 50.128,
            "beta2": 0.180,
            "beta3": 0.130,
            "k_S_atomic": -8.5e-17,
            "a0": -1.3,
            "a1": 5.2,
            "a2": -3.5,
            "model": "Odd-neutron actinide Coriolis-projected scaling",
        },
        {
            "nuclide": "225Ac",
            "Z": 89,
            "N": 136,
            "A": 225,
            "J": 1.5,
            "J_str": "3/2",
            "parity_ground": "-",
            "delta_E_keV": 40.09,
            "partner_energy_keV": 40.09,
            "beta2": 0.185,
            "beta3": 0.140,
            "k_S_atomic": -7.2e-17,
            "a0": 1.2,
            "a1": 4.8,
            "a2": -2.5,
            "model": "Odd-proton core polarization surrogate",
        },
        {
            "nuclide": "227Ac",
            "Z": 89,
            "N": 138,
            "A": 227,
            "J": 1.5,
            "J_str": "3/2",
            "parity_ground": "-",
            "delta_E_keV": 27.37,
            "partner_energy_keV": 27.37,
            "beta2": 0.190,
            "beta3": 0.145,
            "k_S_atomic": -7.2e-17,
            "a0": 1.6,
            "a1": 6.4,
            "a2": -3.3,
            "model": "Odd-proton deep-tunneling actinide surrogate",
        },
        {
            "nuclide": "199Hg",
            "Z": 80,
            "N": 119,
            "A": 199,
            "J": 0.5,
            "J_str": "1/2",
            "parity_ground": "-",
            "delta_E_keV": 2500.0,
            "partner_energy_keV": 2500.0,
            "beta2": 0.050,
            "beta3": 0.010,
            "k_S_atomic": -2.8e-17,
            "a0": 0.0004,
            "a1": 0.055,
            "a2": 0.009,
            "model": "Spherical shell model / QRPA (PRL 94, 232502 Eq. 8)",
        },
    ]

    # Process nuclear ledger
    summary_rows = []
    hg_data = nuclei_data[4]
    for nuc in nuclei_data:
        geom = compute_geometry(nuc["A"], nuc["Z"], nuc["beta2"], nuc["beta3"])
        lab_fac = lab_schiff_factor(nuc["J"])
        s_lab_exact = geom["S_intr_exact_e_fm3"] * lab_fac
        s_lab_compact = geom["S_intr_compact_e_fm3"] * lab_fac

        # Nuclear amplification ratios relative to 199Hg
        r_nuc_a0 = abs(nuc["a0"] / hg_data["a0"])
        r_nuc_a1 = abs(nuc["a1"] / hg_data["a1"])
        r_nuc_a2 = abs(nuc["a2"] / hg_data["a2"])
        sum_coupl_nuc = nuc["a0"] + nuc["a1"] + nuc["a2"]
        sum_coupl_hg = hg_data["a0"] + hg_data["a1"] + hg_data["a2"]
        r_nuc_sum = abs(sum_coupl_nuc / sum_coupl_hg)

        # Atomic EDM amplification ratios
        r_atom_a0 = abs((nuc["k_S_atomic"] * nuc["a0"]) / (hg_data["k_S_atomic"] * hg_data["a0"]))
        r_atom_a1 = abs((nuc["k_S_atomic"] * nuc["a1"]) / (hg_data["k_S_atomic"] * hg_data["a1"]))
        r_atom_a2 = abs((nuc["k_S_atomic"] * nuc["a2"]) / (hg_data["k_S_atomic"] * hg_data["a2"]))
        r_atom_sum = abs((nuc["k_S_atomic"] * sum_coupl_nuc) / (hg_data["k_S_atomic"] * sum_coupl_hg))

        # Denominator factor relative to 199Hg (2.5 MeV baseline)
        denom_gain = hg_data["delta_E_keV"] / nuc["delta_E_keV"]

        row = {
            "nuclide": nuc["nuclide"],
            "Z": nuc["Z"],
            "N": nuc["N"],
            "A": nuc["A"],
            "J_pi": f"{nuc['J_str']}{nuc['parity_ground']}",
            "delta_E_keV": nuc["delta_E_keV"],
            "denominator_gain_vs_hg": round(denom_gain, 2),
            "beta2": nuc["beta2"],
            "beta3": nuc["beta3"],
            "R0_fm": round(geom["R0_fm"], 3),
            "S_intr_exact_e_fm3": round(geom["S_intr_exact_e_fm3"], 3),
            "S_intr_compact_e_fm3": round(geom["S_intr_compact_e_fm3"], 3),
            "lab_factor": round(lab_fac, 3),
            "S_lab_exact_e_fm3": round(s_lab_exact, 3),
            "S_lab_compact_e_fm3": round(s_lab_compact, 3),
            "a0_e_fm3": nuc["a0"],
            "a1_e_fm3": nuc["a1"],
            "a2_e_fm3": nuc["a2"],
            "R_nuc_a0": round(r_nuc_a0, 1),
            "R_nuc_a1": round(r_nuc_a1, 1),
            "R_nuc_a2": round(r_nuc_a2, 1),
            "R_nuc_sum": round(r_nuc_sum, 2),
            "R_atom_a0": round(r_atom_a0, 1),
            "R_atom_a1": round(r_atom_a1, 1),
            "R_atom_a2": round(r_atom_a2, 1),
            "R_atom_sum": round(r_atom_sum, 2),
            "model": nuc["model"],
        }
        summary_rows.append(row)

    # 2. WKB tunneling splitting vs beta3 scan
    wkb_rows = []
    for b3_step in range(2, 23):
        b3 = round(b3_step * 0.01, 2)
        d_e = wkb_tunneling_splitting(b3, mass_param=75.0, omega0_keV=1100.0)
        geom = compute_geometry(225, 88, 0.190, b3)
        wkb_rows.append({
            "beta3": b3,
            "tunneling_delta_E_keV": round(d_e, 2),
            "S_intr_exact_e_fm3": round(geom["S_intr_exact_e_fm3"], 3),
            "relative_response_gain": round((geom["S_intr_exact_e_fm3"] / max(d_e, 1.0)) * 100.0, 2),
        })

    # 3. Skyrme EDF sensitivity table for 225Ra
    skyrme_models = {
        "SkO_prime_zr_dir": {"a0": -5.1, "a1": 10.4, "a2": -10.1},
        "SkO_prime_fr_dir": {"a0": -1.9, "a1": 6.3, "a2": -3.8},
        "SkO_prime_fr_src_dir": {"a0": -1.7, "a1": 6.0, "a2": -3.5},
        "SkO_prime_fr_src_dir_exch": {"a0": -1.5, "a1": 6.0, "a2": -4.0},
        "SIII": {"a0": -1.0, "a1": 7.0, "a2": -3.9},
        "SkM_star": {"a0": -4.7, "a1": 21.5, "a2": -11.0},
        "SLy4": {"a0": -3.0, "a1": 16.9, "a2": -8.8},
    }
    skyrme_rows = []
    for name, coeffs in skyrme_models.items():
        sum_c = coeffs["a0"] + coeffs["a1"] + coeffs["a2"]
        skyrme_rows.append({
            "model": name,
            "a0": coeffs["a0"],
            "a1": coeffs["a1"],
            "a2": coeffs["a2"],
            "sum_coupling": round(sum_c, 3),
            "blind_slope_g2": round(-coeffs["a2"] / coeffs["a1"], 4),
            "blind_intercept": round(-coeffs["a0"] / coeffs["a1"], 4),
        })

    # 4. Cancellation blind spot map grid
    cancellation_rows = []
    g_steps = 21
    g_min, g_max = -2.0, 2.0
    for i in range(g_steps):
        g1_g0 = round(g_min + i * (g_max - g_min) / (g_steps - 1), 3)
        for j in range(g_steps):
            g2_g0 = round(g_min + j * (g_max - g_min) / (g_steps - 1), 3)
            s_ra225 = -1.5 + 6.0 * g1_g0 + (-4.0) * g2_g0
            s_ac225 = 1.2 + 4.8 * g1_g0 + (-2.5) * g2_g0
            s_hg199 = 0.0004 + 0.055 * g1_g0 + 0.009 * g2_g0
            cancellation_rows.append({
                "g1_over_g0": g1_g0,
                "g2_over_g0": g2_g0,
                "S_over_g_g0_ra225": round(s_ra225, 4),
                "S_over_g_g0_ac225": round(s_ac225, 4),
                "S_over_g_g0_hg199": round(s_hg199, 6),
                "blind_ra225": abs(s_ra225) < 0.25,
                "blind_ac225": abs(s_ac225) < 0.25,
                "blind_hg199": abs(s_hg199) < 0.005,
            })

    output_dict = {
        "schema": "actinide-schiff-sumrules/v1",
        "description": "Microscopic perturbation sum rules and sensitivity ledger for actinide Schiff moments",
        "date": "2026-10-29",
        "nuclei_summary": summary_rows,
        "wkb_tunneling_scaling": wkb_rows,
        "skyrme_edf_sensitivity": skyrme_rows,
        "blind_spot_grid_sample_count": len(cancellation_rows),
    }

    return output_dict, summary_rows, wkb_rows, cancellation_rows


def main() -> None:
    base_dir = Path("outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/actinide-schiff-sumrules")
    base_dir.mkdir(parents=True, exist_ok=True)

    out_json, summary_rows, wkb_rows, cancellation_rows = run_calculations()

    json_path = base_dir / "actinide_schiff_sumrules.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(out_json, f, indent=2, ensure_ascii=False)
        f.write("\n")

    csv_path = base_dir / "actinide_schiff_sumrules.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(summary_rows[0].keys()))
        writer.writeheader()
        writer.writerows(summary_rows)

    cancel_path = base_dir / "actinide_schiff_cancellation_map.csv"
    with open(cancel_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(cancellation_rows[0].keys()))
        writer.writeheader()
        writer.writerows(cancellation_rows)

    print(f"Calculations completed successfully. Outputs written to {base_dir}")
    print(f"Nuclei processed: {[r['nuclide'] for r in summary_rows]}")
    for r in summary_rows:
        print(f"  {r['nuclide']}: DeltaE={r['delta_E_keV']} keV, S_intr_exact={r['S_intr_exact_e_fm3']} e fm^3, R_atom(a0,a1,a2)=({r['R_atom_a0']}, {r['R_atom_a1']}, {r['R_atom_a2']})")


if __name__ == "__main__":
    main()
