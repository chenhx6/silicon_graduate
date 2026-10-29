#!/usr/bin/env python3
"""Toy beta2-beta3-beta4 fission PES and WKB sensitivity study.

This is a transparent response model, not a calibrated EDF calculation.  It
is intended to expose how a reflection-asymmetric valley changes a least
action path.  Energies are MeV, beta coordinates are dimensionless and the
collective mass is an effective dimensionless scale chosen to make the
log-half-life sensitivity visible.  Replace the potential and inertia with
EDF/GCM inputs for quantitative predictions.
"""
from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import numpy as np

try:
    import matplotlib.pyplot as plt
except Exception:  # plotting is optional; CSV/JSON remain reproducible
    plt = None


OUT = Path(__file__).resolve().parent
X = np.linspace(0.18, 1.25, 321)  # beta2 path coordinate
B3 = np.linspace(-0.45, 0.45, 361)


def shell_factor(z: int, n: int) -> float:
    """Smooth proxy for proximity to the Z=120,N=184 shell region."""
    return math.exp(-((z - 120) / 8.0) ** 2 - ((n - 184) / 12.0) ** 2)


def pes_slice(z: int, n: int, octupole_scale: float = 1.0):
    """Minimize a beta2-beta3-beta4 PES over beta3 and beta4 analytically.

    The beta3 stiffness is positive near the normal minimum and becomes
    negative near the outer saddle when the Delta-l=Delta-j=3 shell proxy is
    active.  beta4 is minimized at fixed beta3, retaining a beta2*beta3^2*beta4
    coupling.  The resulting path is deliberately simple and inspectable.
    """
    f = shell_factor(z, n)
    b3_grid = B3[None, :]
    vals, opt_b3, opt_b4 = [], [], []
    for x in X:
        symmetric = (
            6.0 * (x - 0.20) ** 2
            + 6.8 * math.exp(-((x - 0.55) / 0.10) ** 2)
            + 5.5 * math.exp(-((x - 0.95) / 0.11) ** 2)
        )
        # A soft outer region; the octupole shell drive is strongest there.
        a3 = 5.0 - octupole_scale * (28.0 * f + 4.0 * (n - 174) / 16.0)
        a3 *= math.exp(-((x - 0.92) / 0.19) ** 2)
        a3 += 5.0 * (1.0 - math.exp(-((x - 0.92) / 0.19) ** 2))
        b4_target = 0.035 * (x - 0.45)
        c234 = 8.0 * (0.6 + 0.4 * f)
        k4 = 18.0
        b4 = b4_target - c234 * x * b3_grid**2 / (2.0 * k4)
        b4 = np.clip(b4, -0.30, 0.30)
        energy = (
            symmetric
            + a3 * b3_grid**2
            + 80.0 * b3_grid**4
            + k4 * (b4 - b4_target) ** 2
            + c234 * x * b3_grid**2 * b4
            + 0.35 * b4**2
        )
        i = int(np.argmin(energy[0]))
        vals.append(float(energy[0, i]))
        opt_b3.append(float(B3[i]))
        opt_b4.append(float(b4[0, i]))
    v = np.asarray(vals)
    v -= float(v.min())
    return v, np.asarray(opt_b3), np.asarray(opt_b4)


def barrier_info(v: np.ndarray):
    """Return first/second local maxima and their neighboring minima."""
    # Smooth enough for this analytic grid; identify maxima by sign changes.
    maxima = np.where((v[1:-1] > v[:-2]) & (v[1:-1] >= v[2:]))[0] + 1
    # The labels are geometric (inner around beta2=.55, outer around .95),
    # not an ordering by height.  This matters once octupole lowering makes
    # the inner saddle higher than the outer one.
    if len(maxima):
        first = int(maxima[np.argmin(np.abs(X[maxima] - 0.55))])
        outer = maxima[maxima > first]
        second = int(outer[np.argmin(np.abs(X[outer] - 0.95))]) if len(outer) else first
    else:
        first = second = int(np.argmax(v))
    return first, second


def wkb_log10_t(v: np.ndarray, b3: np.ndarray, b4: np.ndarray, mass_scale=2000.0):
    """One-coordinate least-action estimate, t=2.86e-21(1+exp(2S))."""
    # beta3/beta4 polarisation changes the effective inertia along beta2.
    mass = mass_scale * (1.0 + 0.35 * b3**2 + 0.12 * b4**2)
    e0 = 0.70
    integrand = np.sqrt(2.0 * mass * np.maximum(v - e0, 0.0))
    s = float(np.trapezoid(integrand, X))
    # Stable logarithm of 2.86e-21 * (1+exp(2S)).
    log10_t = math.log10(2.86e-21) + (2.0 * s) / math.log(10.0)
    return s, log10_t


def one_case(z, n, scale):
    v, b3, b4 = pes_slice(z, n, scale)
    i1, i2 = barrier_info(v)
    s, logt = wkb_log10_t(v, b3, b4)
    return {
        "Z": z, "N": n, "A": z + n, "octupole_scale": scale,
        "beta2_inner_saddle": float(X[i1]),
        "beta3_inner_saddle": float(b3[i1]),
        "beta4_inner_saddle": float(b4[i1]),
        "barrier_I_MeV": float(v[i1]),
        "beta2_outer_saddle": float(X[i2]),
        "beta3_outer_saddle": float(b3[i2]),
        "beta4_outer_saddle": float(b4[i2]),
        "barrier_II_MeV": float(v[i2]),
        "action_S_over_hbar": s,
        "log10_Tsf_s": logt,
    }


def main():
    rows = []
    for z in range(114, 127, 2):
        for n in range(170, 191, 2):
            rows.append(one_case(z, n, 1.0))
    sensitivity = []
    base_v, base_b3, base_b4 = pes_slice(120, 184, 0.0)
    base_s, base_logt = wkb_log10_t(base_v, base_b3, base_b4)
    _, base_outer = barrier_info(base_v)
    for scale in np.linspace(0.0, 1.25, 26):
        r = one_case(120, 184, float(scale))
        r["delta_log10_Tsf_vs_no_octupole"] = r["log10_Tsf_s"] - base_logt
        r["delta_barrier_II_MeV_vs_no_octupole"] = r["barrier_II_MeV"] - float(base_v[base_outer])
        sensitivity.append(r)

    data = {
        "model": "beta2-beta3-beta4 toy PES with one-coordinate WKB",
        "status": "model-result; not an EDF prediction",
        "units": {"energy": "MeV", "half_life": "s", "beta": "dimensionless"},
        "formula": "P=exp(-2S/hbar), S=int ds sqrt(2 M_eff(s)[V(s)-E])",
        "parameters": {
            "E_zero_point_MeV": 0.70,
            "mass_scale": 2000.0,
            "beta2_grid": [float(X[0]), float(X[-1]), len(X)],
            "beta3_grid": [float(B3[0]), float(B3[-1]), len(B3)],
            "coupling": "C234 beta2 beta3^2 beta4",
            "shell_proxy": "Gaussian around Z=120,N=184",
        },
        "systematics": rows,
        "sensitivity_120_184": sensitivity,
        "baseline_action_S_over_hbar": base_s,
        "baseline_log10_Tsf_s": base_logt,
    }
    (OUT / "results.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    fields = list(rows[0])
    with (OUT / "systematics.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)
    fields2 = list(sensitivity[0])
    with (OUT / "sensitivity.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields2); w.writeheader(); w.writerows(sensitivity)

    if plt is not None:
        v0, b30, b40 = pes_slice(120, 184, 0.0)
        v1, b31, b41 = pes_slice(120, 184, 1.0)
        fig, ax = plt.subplots(1, 2, figsize=(10, 4))
        ax[0].plot(X, v0, label=r"$\beta_3$ minimized, no shell drive")
        ax[0].plot(X, v1, label=r"$\beta_3$ minimized, Z=120,N=184")
        ax[0].set(xlabel=r"$\beta_2$", ylabel="V (MeV)")
        ax[0].legend(fontsize=8); ax[0].grid(alpha=.25)
        ax[1].plot([r["octupole_scale"] for r in sensitivity],
                   [r["log10_Tsf_s"] for r in sensitivity])
        ax[1].set(xlabel="octupole shell-drive scale", ylabel=r"$\log_{10} T_{SF}$ (s)")
        ax[1].grid(alpha=.25)
        fig.tight_layout(); fig.savefig(OUT / "octupole_wkb_sensitivity.png", dpi=180)


if __name__ == "__main__":
    main()
