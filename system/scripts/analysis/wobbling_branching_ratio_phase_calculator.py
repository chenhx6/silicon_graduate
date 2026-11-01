#!/usr/bin/env python3
"""Mixing amplitudes and unresolved angular-distribution roots.

The former hard-coded TW/LW estimate had no verified derivation and could
circularly "confirm" wobbling by choosing the desired root. It is withdrawn.
Signed reduced E2/M1 matrix elements, in a common convention, can instead
be supplied explicitly. The conversion follows Petrache (ed.), CRC 2025,
Chapter 11, Eq. (11.10), printed p. 225 / PDF p. 244.
"""

import argparse
import json
import math
from typing import Any, Dict, Optional


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")
    return value


def mixing_from_matrix_elements(
    E_gamma_keV: float, e2_matrix_element_eb: float, m1_matrix_element_muN: float
) -> Dict[str, Any]:
    """Convert signed reduced matrix elements, not intrinsic Q0, to amplitudes.

    The sign has meaning only after radiation, operator and axis conventions
    are matched to the experiment. Zero M1 is represented without JSON Infinity;
    a zero/zero transition is undefined.
    """
    energy = _finite("E_gamma_keV", E_gamma_keV)
    e2 = _finite("e2_matrix_element_eb", e2_matrix_element_eb)
    m1 = _finite("m1_matrix_element_muN", m1_matrix_element_muN)
    if energy <= 0:
        raise ValueError("E_gamma_keV must be positive")
    e2_amplitude = 0.835 * (energy * 1e-3) * e2
    if not math.isfinite(e2_amplitude):
        raise ValueError("E2 radiation amplitude exceeds finite range")
    scale = max(abs(e2_amplitude), abs(m1))
    if scale == 0:
        raise ValueError("Both transition amplitudes vanish; mixing is undefined")
    a, b = e2_amplitude / scale, m1 / scale
    e2_fraction = a * a / (a * a + b * b)
    delta = e2_amplitude / m1 if m1 else None
    if delta is not None and not math.isfinite(delta):
        raise ValueError("Mixing ratio exceeds finite floating-point range")
    return {
        "theoretical_delta_E2_M1": delta,
        "E2_multipolarity_fraction_percent": 100.0 * e2_fraction,
        "M1_multipolarity_fraction_percent": 100.0 * (1.0 - e2_fraction),
        "phase_sign": (
            "pure E2; no finite delta" if m1 == 0 else
            "zero" if delta == 0 else
            "positive in supplied convention" if delta > 0 else
            "negative in supplied convention"
        ),
        "amplitude_status": "pure-e2" if m1 == 0 else "supplied-matrix-elements",
    }


def calculate_theoretical_wobbling_delta(
    spin_I: float, spin_j: float, gamma_deg: float, E_gamma_keV: float,
    Q_0_eb: float = 3.5, g_j: float = 1.25, g_R: float = 0.40,
    wobbling_mode: str = "TW",
    e2_matrix_element_eb: Optional[float] = None,
    m1_matrix_element_muN: Optional[float] = None,
) -> Dict[str, Any]:
    """Keep the old parameter interface while refusing an unsupported model.

    Intrinsic moments, spin, gyromagnetic factors and a mode label do not
    specify the transition wavefunctions or their relative matrix elements.
    """
    values = {name: _finite(name, val) for name, val in {
        "spin_I": spin_I, "spin_j": spin_j, "gamma_deg": gamma_deg,
        "E_gamma_keV": E_gamma_keV, "Q0_eb": Q_0_eb, "g_j": g_j, "g_R": g_R,
    }.items()}
    if spin_I < 0 or spin_j < 0 or E_gamma_keV <= 0:
        raise ValueError("Spins must be nonnegative and transition energy positive")
    mode = wobbling_mode.upper()
    if mode not in {"TW", "LW"}:
        raise ValueError("Mode label must be TW or LW")
    if (e2_matrix_element_eb is None) != (m1_matrix_element_muN is None):
        raise ValueError("Supply both E2 and M1 reduced matrix elements")
    result = {
        **values,
        "delta_g": g_j - g_R,
        "requested_mode": mode,
        "theoretical_delta_E2_M1": None,
        "E2_multipolarity_fraction_percent": None,
        "M1_multipolarity_fraction_percent": None,
        "phase_sign": "undetermined without signed matrix elements and conventions",
        "amplitude_status": "insufficient-model-input",
        "wobbling_classification": "not inferred from mixing ratio",
        "evidence_boundary": (
            "Former TW formula and LW factor 0.25 withdrawn. Neither the sign "
            "of g_j-g_R nor nearest-root matching establishes an experimental mode."
        ),
    }
    if e2_matrix_element_eb is not None:
        result.update(mixing_from_matrix_elements(
            E_gamma_keV, e2_matrix_element_eb, m1_matrix_element_muN
        ))
    return result


def compare_wobbling_with_experimental_roots(
    delta_theo: Optional[float], root_1_exp: float, root_2_exp: float
) -> Dict[str, Any]:
    """Describe both candidate roots; no likelihood or root rejection is implied."""
    roots = [_finite("root_1_exp", root_1_exp), _finite("root_2_exp", root_2_exp)]
    theory = None if delta_theo is None else _finite("delta_theo", delta_theo)
    candidates = []
    for index, root in enumerate(roots, 1):
        fraction = math.sin(math.atan(root)) ** 2
        candidates.append({
            "label": f"Root {index}", "delta": root,
            "E2_fraction_percent": 100.0 * fraction,
            "absolute_distance_to_supplied_theory": (
                None if theory is None else abs(root - theory)
            ),
        })
    return {
        "theoretical_delta": theory,
        "experimental_root_1": roots[0], "experimental_root_2": roots[1],
        "candidates": candidates,
        "selected_matching_root": None,
        "is_wobbling_confirmed": False,
        "root_status": "unresolved-by-this-calculation",
        "verdict": (
            "Both roots retained. Resolve with calibrated independent observables "
            "and a joint likelihood including alignment, geometry and conventions. "
            "An E2 fraction is not an absolute B(E2) measurement."
        ),
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    theory = summary["theory"]
    lines = [
        "MIXING AMPLITUDE CHECK - EXPERIMENTAL MODE NOT INFERRED",
        f"Amplitude status: {theory['amplitude_status']}",
        f"Delta (E2/M1): {theory['theoretical_delta_E2_M1']}",
        f"E2 photon fraction (%): {theory['E2_multipolarity_fraction_percent']}",
        f"Phase: {theory['phase_sign']}",
        theory["evidence_boundary"],
    ]
    if "root_comparison" in summary:
        comparison = summary["root_comparison"]
        for root in comparison["candidates"]:
            lines.append(
                f"{root['label']}: delta={root['delta']:g}; "
                f"E2 fraction={root['E2_fraction_percent']:.3f}% (retained)"
            )
        lines.append(comparison["verdict"])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-I", "--spin", type=float, default=15.5)
    parser.add_argument("-j", "--spinj", type=float, default=5.5)
    parser.add_argument("--gamma", type=float, default=26.0)
    parser.add_argument("--eg", type=float, default=720.0)
    parser.add_argument("--q0", type=float, default=5.0)
    parser.add_argument("--gj", type=float, default=1.25)
    parser.add_argument("--gr", type=float, default=0.40)
    parser.add_argument("--mode", choices=["TW", "LW"], default="TW")
    parser.add_argument("--e2-me", type=float, help="Signed reduced E2 element in eb")
    parser.add_argument("--m1-me", type=float, help="Signed reduced M1 element in mu_N")
    parser.add_argument("--root1", type=float)
    parser.add_argument("--root2", type=float)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if (args.root1 is None) != (args.root2 is None):
        parser.error("Supply both candidate roots")
    try:
        theory = calculate_theoretical_wobbling_delta(
            args.spin, args.spinj, args.gamma, args.eg, args.q0,
            args.gj, args.gr, args.mode, args.e2_me, args.m1_me,
        )
        summary = {"theory": theory}
        if args.root1 is not None:
            summary["root_comparison"] = compare_wobbling_with_experimental_roots(
                theory["theoretical_delta_E2_M1"], args.root1, args.root2
            )
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(summary, indent=2, allow_nan=False) if args.json
          else format_text_report(summary))


if __name__ == "__main__":
    main()
