#!/usr/bin/env python3
"""Reproducible geometry and crossing toy model for the 135Pr MR question.

This is an evidence-calibrated comparator, not a TAC-RMF calculation.  It
implements three transparent layers:

1. fixed two-blade shears geometry;
2. the same geometry with a core angular momentum parallel to I;
3. a two-configuration 3qp/5qp crossing proxy and its dynamic moment
   J^(2)=dI/d(hbar*omega).

The 3qp and 5qp blade lengths are limiting vector values used for an
illustrative calculation: j_p=11/2, j_n=10 for pi(h11/2) nu(h11/2)^-2,
and j_p=11/2+6 for pi(h11/2)(g7/2)^2 nu(h11/2)^-2.  They are not extracted
from the Garg TAC code.  Garg's reported TAC tilt angles and deformations are
stored as metadata only, and are not identified with the blade angle.

The output deliberately uses normalized strengths.  No absolute B(M1) or
B(E2) is inferred because Garg et al. report no lifetime for this band.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def _clip(x: float, lo: float = -1.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


def blade_angle_deg(I: float, jp: float, jn: float) -> float | None:
    """Return the classical angle between two blade vectors, or None."""
    if I <= 0 or jp <= 0 or jn <= 0:
        raise ValueError("I, jp and jn must be positive")
    c = (I * I - jp * jp - jn * jn) / (2.0 * jp * jn)
    if c < -1.0 - 1e-10 or c > 1.0 + 1e-10:
        return None
    return math.degrees(math.acos(_clip(c)))


def normalized_strengths(
    I: float,
    jp: float,
    jn: float,
    *,
    core_R: float = 0.0,
    e2_power: int = 2,
    e2_floor: float = 0.0,
) -> dict[str, float | None]:
    """Return normalized M1, E2 and their ratio.

    R is assumed parallel to I.  The blade resultant is L=I-R, so this is a
    deliberately simple "parallel core rotation" extension.  The E2 law is
    selectable because sin^2 and sin^4 forms occur in different semiclassical
    conventions; neither is an absolute 135Pr result here.
    """
    if e2_power not in (2, 4):
        raise ValueError("e2_power must be 2 or 4")
    L = I - core_R
    theta = blade_angle_deg(L, jp, jn) if L > 0 else None
    if theta is None:
        return {"L": L, "theta_deg": None, "m1_norm": None, "e2_norm": None, "ratio_norm": None}
    s = math.sin(math.radians(theta))
    m1 = (jp * jn / L) ** 2 * s * s
    e2 = e2_floor + s**e2_power
    return {
        "L": L,
        "theta_deg": theta,
        "m1_norm": m1,
        "e2_norm": e2,
        "ratio_norm": None if e2 == 0.0 else m1 / e2,
    }


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def finite_difference(values: list[float], xs: list[float]) -> list[float]:
    out: list[float] = []
    for i in range(len(values)):
        if i == 0:
            out.append((values[1] - values[0]) / (xs[1] - xs[0]))
        elif i == len(values) - 1:
            out.append((values[-1] - values[-2]) / (xs[-1] - xs[-2]))
        else:
            out.append((values[i + 1] - values[i - 1]) / (xs[i + 1] - xs[i - 1]))
    return out


def main() -> None:
    configs = {
        "3qp": {
            "jp": 5.5,
            "jn": 10.0,
            "configuration": "pi(h11/2) nu(h11/2)^-2",
            "beta2": 0.14,
            "gamma_deg": 62.0,
            "tac_tilt_deg": 31.6,
        },
        "5qp": {
            "jp": 11.5,
            "jn": 10.0,
            "configuration": "pi(h11/2)(g7/2)^2 nu(h11/2)^-2",
            "beta2": 0.14,
            "gamma_deg": 60.0,
            "tac_tilt_deg": 26.9,
        },
    }

    spins = [13.5, 14.5, 15.5, 16.5, 17.5, 18.5]
    geometry = []
    for I in spins:
        row = {"I": I}
        for label, cfg in configs.items():
            row[label] = normalized_strengths(I, cfg["jp"], cfg["jn"], e2_power=2)
        geometry.append(row)

    core_rotation = []
    for I in spins:
        # The 0.20 fraction is a transparent scenario parameter, not a 135Pr
        # measurement.  It illustrates how a core contribution changes the
        # inferred blade geometry and leaves an E2 floor.
        core_rotation.append({
            "I": I,
            "5qp_core_R_fraction": 0.20,
            "result": normalized_strengths(
                I,
                configs["5qp"]["jp"],
                configs["5qp"]["jn"],
                core_R=0.20 * I,
                e2_power=4,
                e2_floor=0.05,
            ),
        })

    omegas = [0.10 + 0.01 * i for i in range(51)]
    omega_c = 0.37
    width = 0.025
    # A deliberately minimal crossing proxy.  The peak in J2 is a property of
    # this chosen smooth mixing ansatz, not a measured 135Pr J2 value.
    I3 = [10.0 + 15.0 * w for w in omegas]
    I5 = [11.0 + 24.0 * w for w in omegas]
    weights = [sigmoid((w - omega_c) / width) for w in omegas]
    I_mix = [(1.0 - q) * a + q * b for a, b, q in zip(I3, I5, weights)]
    j2 = finite_difference(I_mix, omegas)
    crossing_proxy = []
    for w, a, b, q, im, j in zip(omegas, I3, I5, weights, I_mix, j2):
        b3 = normalized_strengths(a, configs["3qp"]["jp"], configs["3qp"]["jn"], e2_power=2)
        b5 = normalized_strengths(b, configs["5qp"]["jp"], configs["5qp"]["jn"], e2_power=2)
        # Incoherent strength mixture is used only as an interpretable proxy.
        m1 = None if b3["m1_norm"] is None or b5["m1_norm"] is None else (1-q)*b3["m1_norm"] + q*b5["m1_norm"]
        e2 = None if b3["e2_norm"] is None or b5["e2_norm"] is None else (1-q)*b3["e2_norm"] + q*b5["e2_norm"]
        crossing_proxy.append({
            "hbar_omega_MeV": round(w, 3),
            "I_3qp": a,
            "I_5qp": b,
            "w_5qp": q,
            "I_mix": im,
            "J2_proxy_hbar2_per_MeV": j,
            "m1_norm_mix": m1,
            "e2_norm_mix": e2,
            "ratio_norm_mix": None if m1 is None or e2 is None else m1/e2,
        })

    result = {
        "model_status": "toy comparator; not TAC-RMF and not a fit to absolute strengths",
        "conventions": {
            "I_units": "hbar",
            "omega_units": "hbar*omega in MeV",
            "m1_norm": "(jp*jn/L)^2 sin(theta)^2; common g-factor and 3/(8pi) omitted",
            "e2_norm": "sin(theta)^2 or sin(theta)^4 plus optional core floor; normalized only",
            "J2": "dI/d(hbar*omega)",
        },
        "source_anchors": {
            "garg_2015": "PDF pp.7-8: Fig.5/7, TAC 3qp/5qp, hbar*omega~0.37 MeV and I~33/2; no lifetime",
            "garg_2019_erratum": "PDF p.1 Table I: 747.5 and 813.3 keV corrected to mixed M1+E2",
            "lv_2025_136pr": "PDF pp.9-15: PC-PK1 TAC-CDFT comparator in neighboring 136Pr; no 135Pr TAC-CDFT result",
        },
        "configurations": configs,
        "fixed_geometry": geometry,
        "parallel_core_scenario": core_rotation,
        "crossing_proxy": crossing_proxy,
    }
    out = ROOT / "shears_rebound_model_results.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {out}")
    print(f"J2 proxy max = {max(j2):.3f} hbar^2/MeV at omega={omegas[j2.index(max(j2))]:.2f} MeV")
    for I in (15.5, 16.5):
        print(f"I={I:.1f}: 3qp theta={blade_angle_deg(I, 5.5, 10.0)}, 5qp theta={blade_angle_deg(I, 11.5, 10.0)}")


if __name__ == "__main__":
    main()
