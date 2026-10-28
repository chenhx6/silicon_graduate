#!/usr/bin/env python3
"""Evidence constrained arithmetic for the 144,146Ba E1/E3 comparison.

This is an audit/reproducibility script, not a D1S/SCCM solver.  Numerical
inputs are transcribed from the source ledger and all quantities inferred by
the script are labelled as derived.  In particular, it deliberately does not
invent proton and neutron D_z pieces: BU17 reports their cancellation as a
model interpretation but does not publish a component table or transition
kernel that can be replayed here.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


SQRT_4PI_OVER_3 = math.sqrt(4.0 * math.pi / 3.0)


def e1_weisskopf_efm2(a: int) -> float:
    """One E1 W.u. in e^2 fm^2 using the standard 0.0645 A^(2/3) form."""

    return 0.0645 * a ** (2.0 / 3.0)


def be1_wu_from_amplitude(amplitude_eb_half: float, a: int, initial_spin: int = 1) -> float:
    """Convert a reduced E1 amplitude in e b^(1/2) to W.u.

    Squaring gives e^2 b; 1 b = 100 fm^2.  BU17 Table I writes the
    amplitude for the upward 0+ -> 1- direction, while the requested
    B(E1; 1- -> 0+) is downward and therefore carries the
    1/(2*Ji+1)=1/3 factor.
    """

    be_efm2 = amplitude_eb_half**2 * 100.0
    return be_efm2 / ((2 * initial_spin + 1) * e1_weisskopf_efm2(a))


def be1_wu_from_d0(d0_efm: float, a: int) -> float:
    """Conditional axial-rotor estimate for downward 1- -> 0+ from D0."""

    be_efm2 = (1.0 / (4.0 * math.pi)) * d0_efm**2
    return be_efm2 / e1_weisskopf_efm2(a)


def d0_from_amplitude(amplitude_eb_half: float) -> float:
    """Conditional axial-rotor conversion, with b^(1/2)=10 fm."""

    return SQRT_4PI_OVER_3 * amplitude_eb_half * 10.0


def interval(center: float, plus: float, minus: float) -> tuple[float, float]:
    return center - minus, center + plus


def overlap(a: tuple[float, float], b: tuple[float, float]) -> tuple[float, float] | None:
    lo, hi = max(a[0], b[0]), min(a[1], b[1])
    return (lo, hi) if lo <= hi else None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("ba_e1_e3_cancellation_audit.json"))
    args = parser.parse_args()

    # Direct or source-transcribed quantities.  Locators are kept next to
    # every input so the JSON can be audited without reading this script.
    e3 = {
        "144Ba": {
            "matrix_element_eb32": 0.65,
            "plus": 0.17,
            "minus": 0.23,
            "b_down_wu": 48.0,
            "b_plus": 25.0,
            "b_minus": 34.0,
            "locator": "Bucher 2016 PRL 116 112503, PDF p.4 Table I",
        },
        "146Ba": {
            "matrix_element_eb32": 0.65,
            "plus": 0.14,
            "minus": 0.20,
            "b_down_wu": 48.0,
            "b_plus": 21.0,
            "b_minus": 29.0,
            "locator": "Bucher 2017 PRL 118 152504, PDF p.3 Table I",
        },
    }

    e1_146_amp = {
        "center_eb_half": 0.000223,
        "plus": 0.000010,
        "minus": 0.000008,
        "sccm_eb_half": 0.00474,
        "locator": "Bucher 2017 PRL 118 152504, PDF p.3 Table I and following paragraph",
        "fit_boundary": "E1 is primarily constrained by previous lifetime/branching-ratio data; full GOSIA covariance is unavailable.",
    }

    e3_intervals = {
        name: interval(row["b_down_wu"], row["b_plus"], row["b_minus"])
        for name, row in e3.items()
    }
    e3_overlap = overlap(e3_intervals["144Ba"], e3_intervals["146Ba"])

    # 144Ba D0 is the earlier E1-systematics value quoted in BU17, not a new
    # independent observable from the 2016 E3 table.  We use it only for a
    # clearly labelled conditional conversion to W.u.
    d0_144 = {"center_efm": 0.13, "sigma_efm": 0.01, "locator": "BU17 discussion, PDF p.2; earlier E1 systematics cited there"}
    d0_144_interval = (d0_144["center_efm"] - d0_144["sigma_efm"], d0_144["center_efm"] + d0_144["sigma_efm"])

    amp_146_interval = interval(e1_146_amp["center_eb_half"], e1_146_amp["plus"], e1_146_amp["minus"])
    be1_146 = be1_wu_from_amplitude(e1_146_amp["center_eb_half"], 146)
    be1_146_interval = (
        be1_wu_from_amplitude(amp_146_interval[0], 146, initial_spin=1),
        be1_wu_from_amplitude(amp_146_interval[1], 146, initial_spin=1),
    )
    d0_146_from_fit = d0_from_amplitude(e1_146_amp["center_eb_half"])
    be1_144_conditional = be1_wu_from_d0(d0_144["center_efm"], 144)
    be1_144_conditional_interval = (
        be1_wu_from_d0(d0_144_interval[0], 144),
        be1_wu_from_d0(d0_144_interval[1], 144),
    )

    # BU17 Fig.5 / PDF p.4 reports spherical parentage and v^2 for 146Ba.
    # The normalized exercise below shows the cancellation condition without
    # assigning an unreported e fm coefficient to any orbital.
    occupancies_146 = {"nu_h9/2_K3/2-": 0.40, "nu_f7/2_K5/2-": 0.27, "nu_i13/2_K1/2+": 0.20}
    occupancy_sum = sum(occupancies_146.values())
    normalized_effective_coefficient_for_zero = -1.0 / occupancy_sum

    result = {
        "title": "144Ba/146Ba E1-E3 cancellation evidence audit",
        "status": "evidence-constrained-derived-arithmetic",
        "source_boundary": {
            "direct_experiments": [
                "BU16 direct Coulomb-excitation E3; PDF pp.3-4/Table I",
                "BU17 direct Coulomb-excitation E3 and Table-I matrix elements; PDF pp.2-5",
            ],
            "model": "BU17 SCCM uses Gogny D1S, axial Q20/Q30 coordinates, projection and GCM; it is not replayed here.",
            "missing": ["full GOSIA covariance/joint likelihood", "SCCM projected E1/E3 transition kernels", "published proton/neutron signed D_z component table"],
        },
        "e3": {
            "reported": e3,
            "reported_intervals_wu": e3_intervals,
            "interval_intersection_wu": e3_overlap,
            "interpretation": "The reported intervals overlap; this is compatibility of marginal reported intervals, not a joint confidence statement because the full covariance is unavailable.",
        },
        "e1": {
            "146Ba_amplitude": e1_146_amp,
            "146Ba_B_E1_downward_center_Wu": be1_146,
            "146Ba_B_E1_downward_reported_interval_from_amplitude_Wu": be1_146_interval,
            "146Ba_D0_conditional_from_amplitude_efm": d0_146_from_fit,
            "144Ba_D0_transcribed_efm": d0_144,
            "144Ba_B_E1_conditional_from_D0_Wu": be1_144_conditional,
            "144Ba_B_E1_conditional_interval_Wu": be1_144_conditional_interval,
            "conversion_boundary": "The 144Ba value is an axial-rotor conversion from a prior D0 systematics value; it is not a new BU16 Table-I E1 fit.",
        },
        "orbital_occupancy": {
            "146Ba_v2": occupancies_146,
            "locator": "BU17 PDF p.4 Fig.5 and PDF p.5 opening paragraph",
            "reported_effect": "The paper says these increasing occupancies produce a dipole contribution that nearly cancels the proton contribution and that the total D0 changes sign by 148Ba.",
            "normalized_cancellation_exercise": {
                "sum_v2": occupancy_sum,
                "if_Dp_is_defined_as_1": "D_total/Dp = 1 + c_eff * sum(v2)",
                "c_eff_required_for_zero": normalized_effective_coefficient_for_zero,
                "meaning": "Dimensionless sensitivity illustration only; c_eff is not a published orbital D_z matrix element.",
            },
            "proton_orbital_boundary": "The requested pi(g7/2,d5/2,h11/2) occupancy and signed D_z pieces are not published in BU17 Table/Fig.5 and are not inferred here.",
        },
        "confidence_and_shape": {
            "fit_correlation": "BU16/BU17 state that quoted errors include correlations between fit parameters; BU17 says E1 is primarily constrained by prior lifetimes/branching ratios and the E1/E3 relative sign is insensitive to the data.",
            "static_vs_dynamic": "Large direct E3 supports strong octupole correlations. It does not by itself distinguish a rigid static pear from a large-amplitude soft mode. Bernard 2016 finds a nonzero HFB minimum and a soft beta3 landscape; its projected 2D GCM gives 0.460 eb^(3/2), 25 W.u. for the 0+↔3− E3 matrix element (PDF pp.2-4, Fig.1/Table I).",
            "conclusion": "The evidence favors an occupancy-sensitive E1 cancellation coexisting with strong E3 collectivity; a unique static-pear claim requires additional observables and/or a fully correlated model comparison.",
        },
        "derived_checks": {
            "model_to_experiment_E1_amplitude_ratio_146": e1_146_amp["sccm_eb_half"] / e1_146_amp["center_eb_half"],
            "model_to_experiment_E1_strength_ratio_146": (e1_146_amp["sccm_eb_half"] / e1_146_amp["center_eb_half"]) ** 2,
            "e3_intersection_width_wu": e3_overlap[1] - e3_overlap[0] if e3_overlap else 0.0,
        },
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "e3_intersection_wu": e3_overlap, "be1_146_wu": be1_146, "be1_144_conditional_wu": be1_144_conditional}, ensure_ascii=False))


if __name__ == "__main__":
    main()
