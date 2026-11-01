#!/usr/bin/env python3
"""Schematic entrance-barrier and initial-recoil calculations, NOT PACE/HF.

No physical fusion/residue cross section, fission survival, beamtime or target
specification is predicted. The Wong area assumes absorption after penetration
of a single parabolic barrier; its parameters need independent constraints.

Verified local formula locators (see the linked concept page):
  Lin: printed pp. 135-138 (PDF pp. 145-148), especially Eq. (6.15).
  Bertulani/Danielewicz, 2021 2nd ed.: printed p. 179 (PDF p. 190),
    Eqs. (5.86)-(5.88); pp. 150-151 (PDF pp. 161-162), Eq. (4.189).
These support the framework, not the legacy default barrier recipe, SEMF
coefficient set, or optional illustrative Gaussian weights.
"""

import argparse
import json
import math
from numbers import Integral, Real
from typing import Any, Dict, Optional


M_U_MEV = 931.494
HBAR_C_MEV_FM = 197.327


def _validate_nucleus(Z: int, A: int, label: str, charged: bool = False) -> None:
    if (isinstance(Z, bool) or isinstance(A, bool)
            or not isinstance(Z, Integral) or not isinstance(A, Integral)
            or A < 1 or not (int(charged) <= Z <= A)):
        raise ValueError(f"{label}: integer A >= 1 and {int(charged)} <= Z <= A required")


def _finite(name: str, value: float, positive: bool = False) -> float:
    try:
        valid = (not isinstance(value, bool) and isinstance(value, Real)
                 and math.isfinite(value))
    except (OverflowError, TypeError):
        valid = False
    if not valid or (value <= 0 if positive else value < 0):
        qualifier = "positive" if positive else "nonnegative"
        raise ValueError(f"{name} must be finite and {qualifier}")
    return float(value)


def calculate_liquid_drop_mass(Z: int, A: int) -> float:
    """SEMF nuclear rest-energy estimate in MeV, NOT an evaluated mass.

    Retained coefficients are an unvalidated legacy demonstration set. The
    smooth formula lacks shell corrections and does not establish nuclear
    existence, binding, separation thresholds, or a mass uncertainty.
    """
    _validate_nucleus(Z, A, "mass estimate")
    N = A - Z
    if A % 2:
        delta = 0.0
    elif Z % 2 == 0:
        delta = 12.0 / math.sqrt(A)
    else:
        delta = -12.0 / math.sqrt(A)
    binding = (15.67 * A - 17.23 * A**(2.0 / 3.0)
               - 0.714 * Z * (Z - 1) / A**(1.0 / 3.0)
               - 23.285 * (N - Z)**2 / A + delta)
    return Z * 938.272 + N * 939.565 - binding


def analyze_heavy_ion_fusion(
    Z_p: int, A_p: int, Z_t: int, A_t: int, E_lab_MeV: float,
    target_thickness_mg_cm2: float = 0.5,
    detector_angle_deg: float = 90.0,
    detector_dtheta_deg: float = 8.0,
    E_gamma_keV: float = 1000.0,
    *,
    barrier_radius_fm: Optional[float] = None,
    barrier_height_MeV: Optional[float] = None,
    barrier_curvature_MeV: float = 4.0,
    illustrative_xn: bool = False,
    illustrative_xn_width_MeV: float = 6.0,
) -> Dict[str, Any]:
    """Conditional kinematics, a schematic Wong area, and explicit boundaries.

    Original positional arguments/sections are retained. Physical cross-section,
    survival and FWHM fields now contain None. Numeric Wong areas live only in
    ``schematic_wong_cross_section_mb``. Optional xn weights are dimensionless
    demonstrations, never branching ratios or cross sections.

    Mass-number kinematics assume a stationary target, complete momentum
    transfer and nonrelativistic motion, before evaporation or slowing.
    ``detector_dtheta_deg`` is a FULL polar-angle interval clipped to [0, 180],
    not an angular standard deviation or FWHM. Thickness is metadata only.
    """
    _validate_nucleus(Z_p, A_p, "projectile", charged=True)
    _validate_nucleus(Z_t, A_t, "target", charged=True)
    E_lab_MeV = _finite("E_lab_MeV", E_lab_MeV, positive=True)
    target_thickness_mg_cm2 = _finite("target_thickness_mg_cm2", target_thickness_mg_cm2)
    detector_angle_deg = _finite("detector_angle_deg", detector_angle_deg)
    detector_dtheta_deg = _finite("detector_dtheta_deg", detector_dtheta_deg)
    if detector_angle_deg > 180 or detector_dtheta_deg > 180:
        raise ValueError("detector angle and full polar-angle width must be <= 180 deg")
    E_gamma_keV = _finite("E_gamma_keV", E_gamma_keV, positive=True)
    hbar_omega = _finite("barrier_curvature_MeV", barrier_curvature_MeV, positive=True)
    width = _finite("illustrative_xn_width_MeV", illustrative_xn_width_MeV, positive=True)
    if not isinstance(illustrative_xn, bool):
        raise ValueError("illustrative_xn must be bool")

    Z_cn, A_cn = Z_p + Z_t, A_p + A_t
    Q_fus = (calculate_liquid_drop_mass(Z_p, A_p)
             + calculate_liquid_drop_mass(Z_t, A_t)
             - calculate_liquid_drop_mass(Z_cn, A_cn))
    E_cm = E_lab_MeV * (A_t / A_cn)
    if E_cm == 0:
        raise ValueError("E_cm underflows the positive-energy Wong domain")
    E_ex = E_cm + Q_fus
    mu_MeV = M_U_MEV * A_p * (A_t / A_cn)
    energy_mass_ratio = E_lab_MeV / (M_U_MEV * A_p)
    v_p_over_c = math.sqrt(2.0 * energy_mass_ratio)
    if v_p_over_c >= 1.0:
        raise ValueError("beam energy outside nonrelativistic kinematics (v_p >= c)")
    beta_recoil = v_p_over_c * (A_p / A_cn)

    # Retain the old scale for comparison without attributing it to Bass/CW.
    R_B = (1.07 * (A_p**(1.0 / 3.0) + A_t**(1.0 / 3.0)) + 2.72
           if barrier_radius_fm is None else
           _finite("barrier_radius_fm", barrier_radius_fm, positive=True))
    V_B = ((1.439965 * Z_p * Z_t / R_B) * (1.0 - 0.63 / R_B)
           if barrier_height_MeV is None else
           _finite("barrier_height_MeV", barrier_height_MeV, positive=True))
    if not math.isfinite(V_B) or V_B <= 0:
        raise ValueError("default height recipe invalid here; supply barrier_height_MeV")
    delta = E_cm - V_B
    x_arg = 2.0 * math.pi * (delta / hbar_omega)
    # hbar*omega times softplus: avoid overflow as curvature tends to zero.
    barrier_factor = (2.0 * math.pi * max(0.0, delta)
                      + hbar_omega * math.log1p(math.exp(-abs(x_arg))))
    radius_squared = R_B * R_B
    sigma_wong_mb = _finite(
        "derived schematic Wong area", 5.0 * radius_squared * barrier_factor / E_cm)
    centrifugal_scale = _finite(
        "derived centrifugal scale",
        2.0 * mu_MeV * max(0.0, delta) * radius_squared / HBAR_C_MEV_FM**2)
    # Solve l(l+1) = 2 mu R_B^2 (E_cm - V_B) / hbar^2.
    l_classical = centrifugal_scale / (math.sqrt(centrifugal_scale + 0.25) + 0.5)

    channels = {}
    for x in (3, 4, 5, 6):
        residue_A = A_cn - x
        if residue_A < Z_cn or residue_A < 1:
            continue
        channels[f"{x}n"] = {
            "residue": f"Z={Z_cn}, A={residue_A}",
            "residue_Z": Z_cn, "residue_A": residue_A, "emitted_neutrons": x,
            "status": "A/Z bookkeeping only; thresholds and nuclear existence not checked",
            "cross_section_mb": None, "branching_ratio_pct": None,
            "E_opt_MeV": None, "relative_weight": None,
        }

    illustrative_status = "disabled"
    if illustrative_xn and E_ex > 0 and channels:
        # Arbitrary cost, density scale, offset and width: NOT a cascade.
        delta_E = 8.0 + 2.0 * math.sqrt(E_ex / (A_cn / 8.5))
        centers = {key: item["emitted_neutrons"] * delta_E + 5.0
                   for key, item in channels.items()}
        distances = {key: abs(E_ex - center) for key, center in centers.items()}
        nearest = min(distances.values())
        # Relative log weights avoid both all-zero tails and inf - inf for
        # very narrow widths. Tied nearest centers retain identical weight.
        weights = {
            key: (1.0 if distance == nearest else
                  math.exp(-0.5 * ((distance - nearest) / width)
                           * ((distance + nearest) / width)))
            for key, distance in distances.items()
        }
        normalization = sum(weights.values())
        for key, item in channels.items():
            item["illustrative"] = {
                "center_MeV": centers[key], "width_MeV": width,
                "normalized_weight_within_displayed_xn": weights[key] / normalization,
                "physical_channel_probability": False, "thresholds_checked": False,
            }
        illustrative_status = "heuristic Gaussian weights; not physical branching or yields"
    elif illustrative_xn:
        illustrative_status = "unavailable: nonpositive SEMF excitation or no admissible xn residue"

    theta = math.radians(detector_angle_deg)
    dtheta = math.radians(detector_dtheta_deg)
    theta_lo = max(0.0, detector_angle_deg - detector_dtheta_deg / 2.0)
    theta_hi = min(180.0, detector_angle_deg + detector_dtheta_deg / 2.0)

    def gamma_energy(angle_deg: float) -> float:
        return (E_gamma_keV * math.sqrt(1.0 - beta_recoil**2)
                / (1.0 - beta_recoil * math.cos(math.radians(angle_deg))))

    energy_lo, energy_hi = gamma_energy(theta_hi), gamma_energy(theta_lo)
    warnings = [
        "No evaluated masses, shell corrections, mass covariance or physical thresholds.",
        "Single parabolic barrier with absorption assumed; no coupled channels or P_CN.",
        "No spin/parity population, competing widths, evaporation cascade or fission survival.",
        "Initial compound recoil only; no evaporation kick, stopping, lifetime or angular response.",
        "Thickness is metadata only; no energy loss, yield, beamtime or thickness recommendation.",
    ]
    if energy_mass_ratio > 0.01:
        warnings.append("E_lab/(A_p m_u c^2) > 0.01: nonrelativistic approximation needs review.")
    if E_ex <= 0:
        warnings.append("SEMF E* <= 0: no physical excited-compound formation inferred.")
    return {
        "scientific_boundary": {
            "model": "schematic single-barrier Wong and mass-number kinematics",
            "physical_cross_sections_predicted": False,
            "statistical_evaporation_modeled": False, "evaluated_masses_used": False,
            "mass_model": "SEMF with unvalidated legacy coefficients; no uncertainty assigned",
            "illustrative_xn_status": illustrative_status,
            "beamtime_recommendation": None, "target_thickness_recommendation_mg_cm2": None,
            "warnings": warnings,
        },
        "entrance_channel": {
            "projectile": f"Z={Z_p}, A={A_p}", "target": f"Z={Z_t}, A={A_t}",
            "compound_nucleus": f"Z={Z_cn}, A={A_cn}", "compound_Z": Z_cn, "compound_A": A_cn,
            "E_lab_MeV": E_lab_MeV, "E_cm_MeV": E_cm,
            "Q_fusion_MeV": Q_fus, "Q_fusion_SEMF_MeV": Q_fus,
            "Q_fusion_status": "SEMF estimate, not evaluated-mass Q",
            "E_excitation_MeV": E_ex,
            "E_excitation_status": "conditional on SEMF Q and complete fusion",
            "kinematics_status": "nonrelativistic, m = A m_u, stationary target",
        },
        "barrier_and_fusion": {
            "R_barrier_fm": R_B, "V_barrier_MeV": V_B, "hbar_omega_MeV": hbar_omega,
            "parameter_origin": {
                "radius": "unvalidated legacy recipe" if barrier_radius_fm is None else "user input",
                "height": "unvalidated legacy recipe" if barrier_height_MeV is None else "user input",
                "curvature": "input parameter; default 4 MeV is illustrative",
            },
            "schematic_wong_cross_section_mb": sigma_wong_mb, "sigma_fusion_mb": None,
            "L_max_hbar": l_classical,
            "L_max_status": "classical l(l+1) barrier scale; not CN spin or a tunnelling cutoff",
            "L_fission_limit_hbar": None, "fission_survival_fraction": None,
            "sigma_evaporation_total_mb": None,
        },
        "evaporation_channels": channels,
        "in_beam_spectroscopy": {
            "recoil_velocity_beta": beta_recoil, "recoil_velocity_pct_c": beta_recoil * 100.0,
            "recoil_status": "initial CN, complete momentum transfer, no slowing or evaporation",
            "detector_angle_deg": detector_angle_deg,
            "detector_opening_dtheta_deg": detector_dtheta_deg,
            "angular_width_convention": "full polar width, clipped to [0,180]; not FWHM",
            "polar_angle_interval_deg": [theta_lo, theta_hi], "gamma_energy_keV": E_gamma_keV,
            "doppler_shift_keV": gamma_energy(detector_angle_deg) - E_gamma_keV,
            "doppler_shift_first_order_keV": E_gamma_keV * beta_recoil * math.cos(theta),
            "doppler_angular_energy_interval_keV": [energy_lo, energy_hi],
            "doppler_angular_full_span_keV": energy_hi - energy_lo,
            "doppler_small_angle_full_span_keV": E_gamma_keV * beta_recoil * math.sin(theta) * dtheta,
            "doppler_broadening_fwhm_keV": None,
            "target_thickness_mg_cm2": target_thickness_mg_cm2,
            "target_transport_modeled": False, "target_energy_loss_MeV": None,
        },
    }


def format_text_report(res: Dict[str, Any]) -> str:
    ent, bar, spec = (res[key] for key in
                      ("entrance_channel", "barrier_and_fusion", "in_beam_spectroscopy"))
    lines = [
        "SCHEMATIC FUSION ENTRANCE / INITIAL-RECOIL DEMONSTRATION",
        "Not PACE / Hauser-Feshbach; no physical channel cross sections predicted.",
        f"System: {ent['projectile']} + {ent['target']} -> {ent['compound_nucleus']}*",
        f"Beam: {ent['E_lab_MeV']:.3g} MeV; E_cm (m=A m_u): {ent['E_cm_MeV']:.3g} MeV",
        f"SEMF Q estimate: {ent['Q_fusion_MeV']:+.3g} MeV (not evaluated mass)",
        f"Conditional SEMF E*: {ent['E_excitation_MeV']:.3g} MeV",
        f"Barrier inputs: R={bar['R_barrier_fm']:.3g} fm, V={bar['V_barrier_MeV']:.3g} MeV, "
        f"hbar*omega={bar['hbar_omega_MeV']:.3g} MeV",
        f"Schematic Wong area: {bar['schematic_wong_cross_section_mb']:.3g} mb",
        "Barrier defaults are unvalidated legacy parameters, without Bass/CW attribution.",
        f"Classical orbital scale: l={bar['L_max_hbar']:.3g} (not a spin population)",
        "Physical fusion/residue cross sections, fission cutoff and survival: unavailable.",
        f"xn display: {res['scientific_boundary']['illustrative_xn_status']}",
    ]
    for channel, data in res["evaporation_channels"].items():
        line = f"  {channel} -> {data['residue']}: A/Z bookkeeping; physical sigma/branching unavailable"
        if "illustrative" in data:
            weight = data["illustrative"]["normalized_weight_within_displayed_xn"]
            line += f"; illustrative weight within displayed subset={weight:.3g}"
        lines.append(line)
    lines.extend([
        f"Initial CN beta (m=A m_u): {spec['recoil_velocity_beta']:.3g}",
        f"Conditional Doppler shift: {spec['doppler_shift_keV']:+.3g} keV",
        f"Full polar interval: {spec['polar_angle_interval_deg']} deg",
        f"Angular energy span: {spec['doppler_angular_full_span_keV']:.3g} keV; FWHM unavailable",
        f"Thickness input: {spec['target_thickness_mg_cm2']:.3g} mg/cm^2 (metadata; transport not modeled)",
        "No beamtime or target-thickness recommendation.",
    ])
    lines.extend(f"Boundary: {warning}" for warning in res["scientific_boundary"]["warnings"])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--Zp", type=int, default=16, help="Projectile charge")
    parser.add_argument("--Ap", type=int, default=36, help="Projectile mass number")
    parser.add_argument("--Zt", type=int, default=42, help="Target charge")
    parser.add_argument("--At", type=int, default=100, help="Target mass number")
    parser.add_argument("--Elab", type=float, default=155.0, help="Lab energy in MeV, positive")
    parser.add_argument("--target-thick", type=float, default=0.5, help="Thickness metadata in mg/cm^2; no transport")
    parser.add_argument("--th-det", type=float, default=90.0, help="Lab polar angle in degrees")
    parser.add_argument("--dth-det", type=float, default=8.0, help="Full polar-angle width in degrees, NOT FWHM")
    parser.add_argument("--egamma", type=float, default=1000.0, help="Rest-frame gamma energy in keV")
    parser.add_argument("--barrier-radius", type=float, help="Schematic barrier radius, fm")
    parser.add_argument("--barrier-height", type=float, help="Schematic barrier height, MeV")
    parser.add_argument("--barrier-curvature", type=float, default=4.0, help="hbar*omega, MeV")
    parser.add_argument("--illustrative-xn", action="store_true", help="Show nonphysical Gaussian xn weights")
    parser.add_argument("--illustrative-xn-width", type=float, default=6.0, help="Arbitrary Gaussian width, MeV")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()
    try:
        res = analyze_heavy_ion_fusion(
            args.Zp, args.Ap, args.Zt, args.At, args.Elab,
            args.target_thick, args.th_det, args.dth_det, args.egamma,
            barrier_radius_fm=args.barrier_radius, barrier_height_MeV=args.barrier_height,
            barrier_curvature_MeV=args.barrier_curvature, illustrative_xn=args.illustrative_xn,
            illustrative_xn_width_MeV=args.illustrative_xn_width,
        )
    except ValueError as exc:
        parser.error(str(exc))
    if args.json:
        print(json.dumps(res, indent=2, allow_nan=False))
    else:
        print(format_text_report(res))


if __name__ == "__main__":
    main()
