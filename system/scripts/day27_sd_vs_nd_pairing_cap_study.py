#!/usr/bin/env python3
"""Day27 conditional gap/inertia and prescribed two-band alignment illustration.

Historical nucleus names label synthetic fixtures, not measured bands or fits.
The gap uses a fixed 0.65-MeV hbar*omega scale and a 0.2*Delta0 floor.
The crossing is prescribed independently of the gap; G_pair is unused. No BCS
or number equation is solved, no experimental mechanism is adjudicated.
Legacy callable names, CLI and result keys remain for replay compatibility.
"""

import argparse
import json
import math
from datetime import datetime, timezone
from pathlib import Path
import numpy as np


def _finite(name, value):
    try:
        value = float(value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError(f"{name} must be a finite number") from exc
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")
    return value


def solve_cranked_pairing_bcs(omega_MeV, Delta_0_MeV, G_pair, j_intruder, omega_c_MeV, gamma_crossing=0.04):
    """Legacy name: imposed gap and independent avoided-crossing alignment.

    omega_MeV and omega_c_MeV mean hbar*omega [MeV]; gamma_crossing is
    V_mix [MeV], j_intruder is in hbar units. G_pair>=0 is validated but
    UNUSED; changing it cannot affect results. V_mix>0 excludes the undefined
    unmixed degeneracy. Delta0=0 gives zero gap but can still have alignment.
    """
    x = _finite("omega_MeV", omega_MeV)
    d0 = _finite("Delta_0_MeV", Delta_0_MeV)
    g = _finite("G_pair (unused)", G_pair)
    j = _finite("j_intruder", j_intruder)
    xc = _finite("omega_c_MeV", omega_c_MeV)
    v = _finite("gamma_crossing (V_mix)", gamma_crossing)
    if min(x, d0, g, xc) < 0 or j <= 0 or v <= 0:
        raise ValueError("Require x, Delta0, G_pair, xc >= 0 and j_intruder, V_mix > 0")
    omega_cap = 0.65  # chosen hbar*omega scale [MeV], not a fitted critical frequency
    ratio = x / omega_cap
    # Branch avoids overflow when squaring large finite frequencies.
    delta = d0 * math.sqrt(max(0.04, 1.0 - ratio ** 2)) if ratio < 1 else 0.2 * d0
    e_diff = _finite("prescribed band energy difference", 2.0 * (xc - x) * j)
    denom = _finite("mixing denominator", math.hypot(e_diff, 2.0 * v))
    aligned_prob = 0.5 * (1.0 - e_diff / denom)
    return delta, _finite("aligned spin", 2.0 * j * aligned_prob)


def simulate_rotational_band_inertia(nucleus_name, A_mass, beta2, Delta_0, j_intruder, omega_c, V_mix, omegas):
    """Synthetic curve: spin=I/hbar, x=hbar*omega [MeV], J(2)=d(spin)/dx.

    Require >=3 strictly increasing nonnegative finite frequencies. The Q_t
    field is a legacy proxy with an assumed Z (66 for A=152/160, else 82),
    not a measured quadrupole moment or a general isotope charge lookup.
    """
    A_mass = _finite("A_mass", A_mass)
    beta2 = _finite("beta2", beta2)
    if A_mass <= 0 or beta2 < 0:
        raise ValueError("Require A_mass > 0 and beta2 >= 0 for this prolate proxy")
    omegas = [_finite("hbar*omega", x) for x in omegas]
    if len(omegas) < 3 or omegas[0] < 0 or any(b <= a for a, b in zip(omegas, omegas[1:])):
        raise ValueError("Require >=3 strictly increasing nonnegative frequencies")
    # Chosen rigid-inertia scale; coefficients are illustrative, not calibrated.
    try:
        J_rig = _finite("rigid inertia proxy", 0.0140 * (A_mass ** (5.0 / 3.0)) * (1.0 + 0.32 * beta2))
    except OverflowError as exc:
        raise ValueError("Rigid inertia proxy overflow") from exc

    # Chosen collective response: J_rig / (1 + (Delta/0.55)^1.8).

    states = []
    I_vals = []

    for om in omegas:
        Delta_om, i_x = solve_cranked_pairing_bcs(om, Delta_0, G_pair=0.15, j_intruder=j_intruder,
                                                 omega_c_MeV=omega_c, gamma_crossing=V_mix)

        # Imposed collective inertia response to the prescribed gap.
        try:
            J_coll = _finite("collective inertia", J_rig / (1.0 + ((Delta_om / 0.55) ** 1.8)))
        except OverflowError as exc:
            raise ValueError("Collective inertia proxy overflow") from exc

        # Dimensionless spin I_x/hbar = (J_coll/hbar^2)*x + i_x, x=hbar*omega.
        I_x = _finite("spin I/hbar", J_coll * om + i_x)
        I_vals.append(I_x)

        states.append({
            "omega_MeV": round(float(om), 3),
            "Delta_pairing_MeV": round(float(Delta_om), 3),
            "I_x_spin": round(float(I_x), 2),
            "i_x_aligned": round(float(i_x), 2),
            "J_coll_hbar2_per_MeV": round(float(J_coll), 1)
        })

    # J(2)/hbar^2 = d(I_x/hbar)/dx from unrounded inputs, x=hbar*omega.
    for k in range(len(states)):
        if 0 < k < len(states) - 1:
            d_om = omegas[k+1] - omegas[k-1]
            d_I = I_vals[k+1] - I_vals[k-1]
            J2 = _finite("dynamic inertia", d_I / d_om)
            states[k]["J2_dynamic_MoI_hbar2_per_MeV"] = round(float(J2), 1)
        else:
            states[k]["J2_dynamic_MoI_hbar2_per_MeV"] = None

    # Legacy leading-order quadrupole proxy with assumed charge, not experimental input.
    Z_val = 66 if A_mass == 160 else (66 if A_mass == 152 else 82)
    R0 = 1.20 * (A_mass ** (1.0 / 3.0))
    Q_t = _finite("Q_t proxy", (3.0 / math.sqrt(5.0 * math.pi)) * Z_val * (R0 ** 2) * beta2 * 0.01)  # in e b

    return {
        "nucleus": nucleus_name,
        "model_type": "synthetic imposed-gap plus prescribed-crossing illustration; not BCS",
        "Q_t_proxy_assumed_Z": Z_val,
        "field_definitions": {
            "omega_MeV": "hbar*omega [MeV]; rounded display value, differentiation uses unrounded input",
            "I_x_spin": "I_x/hbar (dimensionless)",
            "J2_dynamic_MoI_hbar2_per_MeV": "centered secant d(I_x/hbar)/d(hbar*omega); null at endpoints; sampling dependent",
            "Q_t_eb": "leading-order proxy using assumed Z; not experimental"
        },
        "mass_A": A_mass,
        "beta2_deformation": beta2,
        "Q_t_eb": round(float(Q_t), 2),
        "Delta_0_initial_MeV": Delta_0,
        "J_rigid_hbar2_per_MeV": round(float(J_rig), 1),
        "states": states
    }


def main():
    parser = argparse.ArgumentParser(description="Synthetic SD/ND-labelled gap and prescribed-crossing illustration (not BCS).")
    parser.add_argument("--output", type=str, default="outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/sd-nd-pairing-cap/sd_nd_pairing_cap_results.json")
    args = parser.parse_args()

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # Three historical nucleus-labelled synthetic parameter choices.
    omegas_nd = np.linspace(0.16, 0.40, 13)
    dy160_res = simulate_rotational_band_inertia(
        "160Dy (Normal Deformation, A~160)", A_mass=160, beta2=0.28, Delta_0=1.05,
        j_intruder=5.5, omega_c=0.28, V_mix=0.035, omegas=omegas_nd
    )

    omegas_sd150 = np.linspace(0.30, 0.66, 13)
    dy152_res = simulate_rotational_band_inertia(
        "152Dy (Superdeformation, A~150)", A_mass=152, beta2=0.60, Delta_0=0.04,
        j_intruder=6.5, omega_c=0.85, V_mix=0.15, omegas=omegas_sd150
    )

    omegas_sd190 = np.linspace(0.15, 0.45, 13)
    pb194_res = simulate_rotational_band_inertia(
        "194Pb (Superdeformation, A~190)", A_mass=194, beta2=0.48, Delta_0=0.85,
        j_intruder=7.0, omega_c=0.38, V_mix=0.18, omegas=omegas_sd190
    )

    benchmarks = {
        "160Dy_ND": dy160_res,
        "152Dy_SD": dy152_res,
        "194Pb_SD": pb194_res
    }

    # Legacy curve-shape checks on prescribed fixtures; not experimental validation.
    # Fixture 1: prescribed-curve maximum >=120 hbar^2/MeV.
    dy160_j2_vals = [s["J2_dynamic_MoI_hbar2_per_MeV"] for s in dy160_res["states"] if s["J2_dynamic_MoI_hbar2_per_MeV"] is not None]
    test_1_dy160_backbending = bool(max(dy160_j2_vals) >= 120.0)

    # Fixture 2: prescribed-curve full variation <=8% of its mean.
    dy152_j2_vals = [s["J2_dynamic_MoI_hbar2_per_MeV"] for s in dy152_res["states"] if s["J2_dynamic_MoI_hbar2_per_MeV"] is not None]
    j2_mean_152 = np.mean(dy152_j2_vals)
    j2_var_152 = (max(dy152_j2_vals) - min(dy152_j2_vals)) / j2_mean_152
    test_2_dy152_flat_plateau = bool(j2_var_152 <= 0.08)

    # Fixture 3: endpoint rise >=30%; this check alone does not test monotonicity.
    pb194_j2_vals = [s["J2_dynamic_MoI_hbar2_per_MeV"] for s in pb194_res["states"] if s["J2_dynamic_MoI_hbar2_per_MeV"] is not None]
    j2_rise_pb194 = (pb194_j2_vals[-1] - pb194_j2_vals[0]) / pb194_j2_vals[0]
    test_3_pb194_smooth_rise = bool(j2_rise_pb194 >= 0.30)

    # Fixture 4: final imposed gap <75% of first sampled gap.
    pb194_deltas = [s["Delta_pairing_MeV"] for s in pb194_res["states"]]
    test_4_pb194_cap_quenched = bool(pb194_deltas[-1] < pb194_deltas[0] * 0.75)

    all_passed = bool(all([test_1_dy160_backbending, test_2_dy152_flat_plateau, test_3_pb194_smooth_rise, test_4_pb194_cap_quenched]))

    output_data = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "task": "Conditional gap/inertia and prescribed alignment curve comparison",
        "self_tests": {
            "interpretation": "Legacy numerical fixture thresholds only; not BCS convergence or experimental validation",
            "all_passed": all_passed,
            "test_1_dy160_sharp_backbending": test_1_dy160_backbending,
            "test_2_dy152_flat_rigid_plateau": test_2_dy152_flat_plateau,
            "test_3_pb194_smooth_j2_rise": test_3_pb194_smooth_rise,
            "test_4_pb194_coriolis_anti_pairing": test_4_pb194_cap_quenched
        },
        "benchmarks": benchmarks,
        "evidence_boundaries": {
            "model_type": "Imposed square-root gap with 20% floor plus independent two-band avoided crossing",
            "empirical_inputs": [],
            "G_pair_used": False,
            "gap_scale_hbar_omega_MeV": 0.65,
            "gap_floor_fraction": 0.2,
            "limitations": "Synthetic nucleus labels and chosen parameters only. Crossing xc and V_mix do not depend on the imposed gap. No gap/number equation, measured energies, lifetimes or experimental errors are used. Curve checks cannot discriminate mechanisms or establish phase order. Q_t is an assumed-charge proxy."
        }
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Conditional CAP illustration complete (not BCS/experimental validation). Legacy curve checks passed: {all_passed}. Wrote {out_path}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
