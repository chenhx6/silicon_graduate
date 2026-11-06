#!/usr/bin/env python3
"""Conditional CAP gap/inertia interpolation, not a microscopic BCS solver.

x = hbar*omega in MeV; Delta = Delta0*sqrt(max(0, 1-(x/xc)^2)).
All three inertias share f = 1-(1-r)*Delta/Delta0, preserving axis ratios.
Solve i = (J_m/hbar^2)*x for dimensionless spin i=I/hbar.
Neither the imposed zero-gap scale nor a sampled threshold establishes a phase
transition or an experimental critical spin. BM-II source BM2-11 (§4-3a,
PDF64/printed42) supports a tentative pairing interpretation, not these formulas.
Legacy names/keys are retained for CLI/API compatibility; presets are synthetic.
"""

import json
import math
import argparse


PRESETS = {
    "163Lu_TSD_superfluid_to_normal_phase_transition": {
        "description": "Synthetic 163Lu-labelled interpolation; hbar*omega scale = 0.45 MeV; not experimental",
        "nucleus": "163Lu",
        "delta_0_MeV": 0.95,
        "omega_crit_MeV": 0.45,
        "J_rigid_hbar2_per_MeV": {"J_s": 45.0, "J_m": 72.0, "J_l": 20.0},
        "J_irrotational_ratio": 0.40,
        "spins_to_evaluate": [10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0]
    },
    "130Ba_transitional_triaxial_cap": {
        "description": "Synthetic 130Ba-labelled interpolation; hbar*omega scale = 0.38 MeV; not experimental",
        "nucleus": "130Ba",
        "delta_0_MeV": 1.15,
        "omega_crit_MeV": 0.38,
        "J_rigid_hbar2_per_MeV": {"J_s": 22.0, "J_m": 35.0, "J_l": 12.0},
        "J_irrotational_ratio": 0.45,
        "spins_to_evaluate": [6.0, 10.0, 14.0, 18.0, 22.0, 26.0, 30.0]
    },
    "rigid_rotor_zero_pairing_limit": {
        "description": "Synthetic zero-gap rigid-inertia limit",
        "nucleus": "Rigid-Limit",
        "delta_0_MeV": 0.0,
        "omega_crit_MeV": 0.50,
        "J_rigid_hbar2_per_MeV": {"J_s": 30.0, "J_m": 50.0, "J_l": 15.0},
        "J_irrotational_ratio": 1.00,
        "spins_to_evaluate": [10.0, 20.0, 30.0, 40.0]
    }
}


def _finite(name, value):
    try:
        value = float(value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError(f"{name} must be a finite number") from exc
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")
    return value


def _gap_inputs(delta_0_MeV, omega_crit_MeV):
    d0 = _finite("delta_0_MeV", delta_0_MeV)
    xc = _finite("omega_crit_MeV (hbar*omega)", omega_crit_MeV)
    if d0 < 0 or xc <= 0:
        raise ValueError("Require delta_0_MeV >= 0 and omega_crit_MeV > 0")
    return d0, xc


def calculate_cap_pairing_gap(omega_rot_MeV, delta_0_MeV, omega_crit_MeV):
    """Imposed even-in-x gap curve; x=hbar*omega [MeV], not BCS.

    For Delta0=0, quenching_fraction=1 is a legacy zero-gap sentinel, not
    a normalized loss of pairing. is_superfluid means only Delta>0 here.
    """
    x = _finite("omega_rot_MeV (hbar*omega)", omega_rot_MeV)
    d0, xc = _gap_inputs(delta_0_MeV, omega_crit_MeV)
    ratio = abs(x) / xc
    delta = d0 * math.sqrt((1.0 - ratio) * (1.0 + ratio)) if ratio < 1 else 0.0
    return {"delta_MeV": delta,
            "quenching_fraction": 1.0 - delta / d0 if d0 else 1.0,
            "is_superfluid": delta > 0.0}


def calculate_cap_moments_of_inertia(delta_val, delta_0_MeV, J_rig_dict, irr_ratio):
    """Uniform inertia interpolation [hbar^2/MeV]; axis ratios are invariant.

    The legacy irr_ratio is a chosen low-frequency scale, not a derived
    irrotational-flow inertia. Require 0<r<=1 and 0<=Delta<=Delta0.
    """
    d0 = _finite("delta_0_MeV", delta_0_MeV)
    delta = _finite("delta_val", delta_val)
    r = _finite("irr_ratio", irr_ratio)
    if d0 < 0 or not 0 <= delta <= d0 or not 0 < r <= 1:
        raise ValueError("Require 0 <= delta_val <= delta_0_MeV and 0 < irr_ratio <= 1")
    factor = r + (1.0 - r) * (1.0 - delta / d0) if d0 else 1.0
    moi = {}
    for axis in ("J_s", "J_m", "J_l"):
        try:
            j = _finite(axis, J_rig_dict[axis])
        except (KeyError, TypeError) as exc:
            raise ValueError(f"Missing inertia {axis}") from exc
        if j <= 0:
            raise ValueError(f"{axis} must be positive")
        moi[axis] = _finite(axis + " scaled", j * factor)
        if moi[axis] <= 0:
            raise ValueError(f"{axis} scaled inertia underflow")
    return moi


def solve_spin_state_cap(spin_I, delta_0_MeV, omega_crit_MeV, J_rig_dict, irr_ratio):
    """Solve the conditional algebraic map i=J_m(x)*x; no gap/number equation.

    spin_I is i=I/hbar; frequency fields contain x=hbar*omega [MeV].
    A bracket follows from the exact rigid branch x>=xc and is checked.
    """
    spin = _finite("spin_I", spin_I)
    if spin < 0:
        raise ValueError("spin_I must be nonnegative")
    d0, xc = _gap_inputs(delta_0_MeV, omega_crit_MeV)
    rigid = calculate_cap_moments_of_inertia(0.0, d0, J_rig_dict, irr_ratio)

    def state(x):
        gap = calculate_cap_pairing_gap(x, d0, xc)
        moi = calculate_cap_moments_of_inertia(gap["delta_MeV"], d0, rigid, irr_ratio)
        return gap, moi

    lo = 0.0
    hi = _finite("root upper bracket", max(xc, spin / rigid["J_m"]))
    if _finite("upper bracket spin", state(hi)[1]["J_m"] * hi) < spin:
        hi = _finite("rounded-up upper bracket", math.nextafter(hi, math.inf))
    if _finite("upper bracket spin", state(hi)[1]["J_m"] * hi) < spin:
        raise ValueError("Root is not bracketed")
    x = 0.0
    if spin:
        for _ in range(200):
            x = lo + (hi - lo) / 2.0
            actual = _finite("mapped spin", state(x)[1]["J_m"] * x)
            if abs(actual - spin) <= 1e-10 * spin:
                break
            if actual < spin:
                lo = x
            else:
                hi = x
        else:
            raise RuntimeError("Spin mapping did not converge to the requested residual")
    gap, moi = state(x)
    js, jm, jl = (moi[k] for k in ("J_s", "J_m", "J_l"))
    # Rigid principal-axis rotor diagnostic only; zero is a legacy sentinel
    # when m is not the maximum inertia, not evidence of a stable zero mode.
    wob = math.sqrt((jm / js - 1.0) * (jm / jl - 1.0)) if jm > js and jm > jl else 0.0
    return {
        "spin_I": spin,
        "rotational_frequency_MeV": x,
        "pairing_gap_MeV": gap["delta_MeV"],
        "gap_quenching_pct": gap["quenching_fraction"] * 100.0,
        "is_superfluid": gap["is_superfluid"],
        "moments_of_inertia": moi,
        "wobbling_frequency_keV": _finite("wobbling energy", x * wob * 1000.0)
    }


def run_cap_analysis(nucleus, delta_0_MeV, omega_crit_MeV, J_rig_dict, irr_ratio, spins):
    """Replay a conditional curve; legacy critical key is a sampled indicator."""
    d0, xc = _gap_inputs(delta_0_MeV, omega_crit_MeV)
    rigid = calculate_cap_moments_of_inertia(0.0, d0, J_rig_dict, irr_ratio)
    results = [solve_spin_state_cap(i, d0, xc, rigid, irr_ratio) for i in spins]
    qualifying = [p["spin_I"] for p in results
                  if d0 > 0 and p["pairing_gap_MeV"] / d0 < 0.05]
    return {
        "nucleus": nucleus,
        "model_type": "conditional square-root gap and uniform inertia interpolation; not BCS",
        "field_definitions": {
            "rotational_frequency_MeV": "hbar*omega [MeV]",
            "spin_I": "I/hbar (dimensionless)",
            "critical_transition_spin_I_CAP": "minimum sampled I/hbar with Delta/Delta0 < 0.05; null for Delta0=0 or no qualifying sample; not a phase transition",
            "is_superfluid": "legacy flag for positive imposed gap only",
            "irrotational_fluid_ratio": "chosen common low-frequency inertia fraction; not an irrotational-flow calculation",
            "wobbling_frequency_keV": "hbar*omega times rigid principal-axis rotor factor; 0 sentinel if m is not the maximum axis; no transverse-wobbling classification",
            "gap_quenching_pct": "100*(1-Delta/Delta0); legacy 100 sentinel at Delta0=0"
        },
        "parameters": {
            "initial_pairing_gap_Delta0_MeV": d0,
            "critical_CAP_frequency_MeV": xc,
            "irrotational_fluid_ratio": float(irr_ratio),
            "rigid_body_MOI": rigid
        },
        "critical_transition_spin_I_CAP": min(qualifying) if qualifying else None,
        "spin_evolution": results
    }


def format_text_report(res, title="Coriolis Anti-Pairing (CAP) Dynamic Gap Quenching Engine"):
    nuc = res["nucleus"]
    p = res["parameters"]
    evol = res["spin_evolution"]
    I_c = res["critical_transition_spin_I_CAP"]

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Nucleus: {nuc} | Delta_0 = {p['initial_pairing_gap_Delta0_MeV']:.2f} MeV, hbar*omega_scale = {p['critical_CAP_frequency_MeV']:.2f} MeV")
    lines.append("=" * 76)
    lines.append("Rigid-Body Reference Moments of Inertia [J_s, J_m, J_l]:")
    r = p["rigid_body_MOI"]
    lines.append(f"  Rigid Limit: J_s = {r['J_s']:.1f}, J_m = {r['J_m']:.1f}, J_l = {r['J_l']:.1f} hbar^2/MeV (Chosen base = {p['irrotational_fluid_ratio']*100:.0f}%)")
    lines.append(f"  Sampled Delta/Delta0 < 5% indicator : {f'I/hbar = {I_c:.1f}' if I_c is not None else 'None in range'}")
    lines.append("-" * 76)
    lines.append("Spin-Dependent Dynamic Pairing Gap Quenching & MOI Expansion:")
    lines.append("  I/hbar         hbar*w (MeV)   Delta (MeV)   Quench (%)   Gap flag      J_m (hbar^2/MeV)  hbar*w_wob (keV)")
    for pt in evol:
        ph_str = "Positive gap" if pt["is_superfluid"] else "Zero gap"
        lines.append(f"    {pt['spin_I']:4.1f}          {pt['rotational_frequency_MeV']:6.3f}        {pt['pairing_gap_MeV']:6.3f}       {pt['gap_quenching_pct']:5.1f}%     {ph_str:13}     {pt['moments_of_inertia']['J_m']:6.2f}            {pt['wobbling_frequency_keV']:7.1f}")
    lines.append("-" * 76)
    lines.append("Conditional model only: no microscopic BCS solution or phase-order inference.")
    lines.append("Uniform inertia scaling preserves every axis ratio; no mode stabilization inferred.")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Conditional CAP interpolation; frequencies are hbar*omega in MeV."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load benchmark preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        nucleus = p["nucleus"]
        d0 = p["delta_0_MeV"]
        w_c = p["omega_crit_MeV"]
        j_rig = p["J_rigid_hbar2_per_MeV"]
        irr = p["J_irrotational_ratio"]
        spins = p["spins_to_evaluate"]
        title = f"Preset: {args.preset} ({p['description']})"
    else:
        return parser.print_help()

    res = run_cap_analysis(
        nucleus=nucleus,
        delta_0_MeV=d0,
        omega_crit_MeV=w_c,
        J_rig_dict=j_rig,
        irr_ratio=irr,
        spins=spins
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
