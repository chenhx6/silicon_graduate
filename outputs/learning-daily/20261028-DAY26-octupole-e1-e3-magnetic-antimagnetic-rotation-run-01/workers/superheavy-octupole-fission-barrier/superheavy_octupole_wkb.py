#!/usr/bin/env python3
"""Toy two-dimensional beta2-beta3 fission WKB scan.

The calculation is deliberately phenomenological: q is an elongation coordinate,
beta3 is the axial reflection-asymmetric coordinate, and the collective masses
are prescribed in hbar^2/MeV.  It is a reproducible sensitivity model, not an
EDF/HFB prediction for either isotope.
"""
from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np


@dataclass(frozen=True)
class Nucleus:
    name: str
    z: int
    n: int
    barrier: float
    octupole_softening: float
    q_center: float
    q_width: float
    mass_scale: float


NUCLEI = (
    Nucleus("254No", 102, 152, 6.20, 23.0, 0.70, 0.18, 1.00),
    Nucleus("256Rf", 104, 152, 6.55, 26.0, 0.72, 0.18, 1.04),
)


def symmetric_potential(q: np.ndarray, p: Nucleus) -> np.ndarray:
    """Reference reflection-symmetric barrier, in MeV, relative to the well."""
    # Localized outer (second) saddle; q^2 enforces V(0)=0.
    shape = q**2 * np.exp(-0.5 * ((q - p.q_center) / 0.22) ** 2)
    return p.barrier * shape / np.max(shape)


def octupole_coefficient(q: np.ndarray, p: Nucleus) -> np.ndarray:
    """Quadratic beta3 stiffness; it becomes negative around the outer saddle."""
    return 5.0 - p.octupole_softening * np.exp(-0.5 * ((q - p.q_center) / p.q_width) ** 2)


def asymmetric_path(q: np.ndarray, p: Nucleus) -> tuple[np.ndarray, np.ndarray]:
    """Analytic minimum of a3*beta3^2 + c3*beta3^4 at each q."""
    a3 = octupole_coefficient(q, p)
    c3 = 20.0
    beta3 = np.sqrt(np.maximum(0.0, -a3 / (2.0 * c3)))
    lowering = np.where(a3 < 0.0, a3**2 / (4.0 * c3), 0.0)
    return beta3, lowering


def path_action(q: np.ndarray, v: np.ndarray, beta3: np.ndarray, p: Nucleus,
                e0: float, mass_scale: float) -> tuple[float, np.ndarray, np.ndarray]:
    """Integrate S/hbar = int sqrt(2 M(s)(V-E)) ds over forbidden segments."""
    dq = np.gradient(q)
    db = np.gradient(beta3, q)
    # Mqq and M33 are in hbar^2/MeV; q and beta3 are dimensionless.
    mqq = mass_scale * p.mass_scale * (24.0 + 10.0 * q)
    m33 = mass_scale * p.mass_scale * 2.0
    metric = mqq + m33 * db**2
    integrand = np.sqrt(np.maximum(0.0, 2.0 * metric * (v - e0)))
    return float(np.trapezoid(integrand, q)), metric, integrand


def calculate(p: Nucleus, ngrid: int = 4001, e0: float = 0.80,
              mass_scale: float = 1.0) -> dict:
    q = np.linspace(0.0, 1.0, ngrid)
    vs = symmetric_potential(q, p)
    beta3, lowering = asymmetric_path(q, p)
    va = vs - lowering
    ss, ms, is_ = path_action(q, vs, np.zeros_like(q), p, e0, mass_scale)
    sa, ma, ia = path_action(q, va, beta3, p, e0, mass_scale)
    # T = (ln 2 / nu) exp(2S); nu=1e20 s^-1 is a common assault-scale proxy.
    logt_s = np.log10(np.log(2.0) / 1.0e20) + 2.0 * np.array([ss, sa]) / np.log(10.0)
    return {
        "nucleus": asdict(p), "grid": {"ngrid": ngrid, "e0_mev": e0},
        "mass_scale": mass_scale,
        "barrier_sym_mev": float(np.max(vs)),
        "barrier_asym_mev": float(np.max(va)),
        "barrier_lowering_mev": float(np.max(vs) - np.max(va)),
        "max_beta3": float(np.max(beta3)),
        "action_sym_hbar": ss, "action_asym_hbar": sa,
        "delta_action_hbar": sa - ss,
        "log10_tsf_sym_s": float(logt_s[0]), "log10_tsf_asym_s": float(logt_s[1]),
        "delta_log10_tsf": float(logt_s[1] - logt_s[0]),
        "arrays": {"q": q, "v_sym": vs, "v_asym": va, "beta3": beta3,
                   "mass_sym": ms, "mass_asym": ma,
                   "integrand_sym": is_, "integrand_asym": ia},
    }


def write_outputs(outdir: Path, results: list[dict], ngrid: int) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    summaries = []
    for r in results:
        summaries.append({k: v for k, v in r.items() if k != "arrays"})
        name = r["nucleus"]["name"]
        with (outdir / f"{name}_path.csv").open("w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["q", "v_sym_mev", "v_asym_mev", "beta3", "mass_sym", "mass_asym", "integrand_sym", "integrand_asym"])
            a = r["arrays"]
            for row in zip(a["q"], a["v_sym"], a["v_asym"], a["beta3"], a["mass_sym"], a["mass_asym"], a["integrand_sym"], a["integrand_asym"]):
                w.writerow([f"{x:.10g}" for x in row])
    (outdir / "scan_summary.json").write_text(json.dumps({"model": "beta2-beta3 toy WKB", "results": summaries}, indent=2) + "\n")
    (outdir / "scan_parameters.json").write_text(json.dumps({"ngrid": ngrid, "nuclei": [asdict(x) for x in NUCLEI]}, indent=2) + "\n")
    try:
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(1, 2, figsize=(10, 4), constrained_layout=True)
        for r in results:
            q, a = r["arrays"]["q"], r["arrays"]
            axes[0].plot(q, a["v_sym"], label=f'{r["nucleus"]["name"]} sym')
            axes[0].plot(q, a["v_asym"], "--", label=f'{r["nucleus"]["name"]} beta3>0')
            axes[1].plot(q, a["beta3"], label=r["nucleus"]["name"])
        axes[0].set(xlabel="elongation q", ylabel="V(q) [MeV]", title="Second barrier toy PES")
        axes[1].set(xlabel="elongation q", ylabel=r"$\beta_3$", title="Minimum asymmetric path")
        for ax in axes: ax.grid(alpha=.25); ax.legend(fontsize=8)
        fig.savefig(outdir / "barrier_and_beta3.svg")
        plt.close(fig)
    except ImportError:
        (outdir / "plot_unavailable.txt").write_text("matplotlib unavailable; CSV/JSON remain complete.\n")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", type=Path, default=Path(__file__).parent)
    ap.add_argument("--ngrid", type=int, default=4001)
    ap.add_argument("--e0", type=float, default=0.80)
    ap.add_argument("--mass-scale", type=float, default=1.0)
    args = ap.parse_args()
    results = [calculate(p, args.ngrid, args.e0, args.mass_scale) for p in NUCLEI]
    write_outputs(args.outdir, results, args.ngrid)
    for r in results:
        print(f'{r["nucleus"]["name"]}: Bsym={r["barrier_sym_mev"]:.3f} MeV, '
              f'Basym={r["barrier_asym_mev"]:.3f} MeV, '
              f'dlog10(Tsf)={r["delta_log10_tsf"]:.3f}, '
              f'Ssym={r["action_sym_hbar"]:.3f}, Sasym={r["action_asym_hbar"]:.3f}')


if __name__ == "__main__":
    main()
