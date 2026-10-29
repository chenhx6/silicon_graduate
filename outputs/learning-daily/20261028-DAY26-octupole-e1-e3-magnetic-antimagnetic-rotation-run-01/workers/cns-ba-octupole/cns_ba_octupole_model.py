#!/usr/bin/env python3
"""Reduced CNS-inspired beta2-gamma-beta3 energy surfaces for neutron-rich Ba.

This is a transparent surrogate, not a replacement for a self-consistent
Nilsson-Strutinsky calculation.  It keeps the terms that are useful for the
present falsifiable question: a liquid-drop-like macroscopic surface, a
cranked shell term with a Z=56/N=88-90 octupole window, the rotational energy,
and an explicit high-j alignment penalty.  All energies are in MeV and
deformations are dimensionless.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parent
NUCLEI = {
    "144Ba": {
        "A": 144,
        "Z": 56,
        "N": 88,
        "beta20": 0.22,
        "beta3_shell": 0.14,
        "shell_amp": 1.65,
        "alignment_ic": 12.5,
        "alignment_width": 1.8,
        "alignment_quench": 0.88,
        "alignment_penalty": 7.0,
        "J0": 54.0,
        "J_beta2": 1.10,
        "J_beta3": 1.40,
        "E3_Wu": 48.0,
        "D0_efm": 0.13,
    },
    "146Ba": {
        "A": 146,
        "Z": 56,
        "N": 90,
        "beta20": 0.22,
        "beta3_shell": 0.14,
        "shell_amp": 1.70,
        "alignment_ic": 14.0,
        "alignment_width": 1.8,
        "alignment_quench": 0.82,
        "alignment_penalty": 6.0,
        "J0": 54.0,
        "J_beta2": 1.10,
        "J_beta3": 1.40,
        "E3_Wu": 48.0,
        "D0_efm": 0.01,
    },
    "148Ba": {
        "A": 148,
        "Z": 56,
        "N": 92,
        "beta20": 0.21,
        "beta3_shell": 0.12,
        "shell_amp": 1.45,
        "alignment_ic": 15.0,
        "alignment_width": 1.8,
        "alignment_quench": 0.90,
        "alignment_penalty": 7.0,
        "J0": 52.0,
        "J_beta2": 1.10,
        "J_beta3": 1.20,
        "E3_Wu": None,
        "D0_efm": None,
    },
}

I_GRID = list(range(25))
BETA2_GRID = [round(0.12 + 0.01 * i, 2) for i in range(20)]
GAMMA_GRID = list(range(-20, 21, 5))
BETA3_GRID = [round(0.01 * i, 2) for i in range(25)]


def alignment_fraction(spin: int, p: dict) -> float:
    """Smooth high-j alignment onset, normalized to one at I=24."""
    if spin == 0:
        return 0.0
    logistic = 1.0 / (1.0 + math.exp(-(spin - p["alignment_ic"]) / p["alignment_width"]))
    return logistic * (spin / 24.0) ** 1.5


def centrifugal_stabilization(spin: int) -> float:
    """A low-to-intermediate-spin shell-coherent octupole enhancement."""
    if spin == 0:
        return 0.0
    # Peaks around I=10 and then fades as alignment takes over.
    return 0.35 * (spin / 10.0) * math.exp(1.0 - spin / 10.0)


def components(beta2: float, gamma: float, beta3: float, spin: int, p: dict) -> dict:
    """Return macroscopic, shell, rotational, alignment and total terms."""
    f_align = alignment_fraction(spin, p)
    # Yukawa-plus-exponential inspired local liquid-drop expansion.  The
    # coefficients are dimensionless reduced parameters, not a mass fit.
    e_ld = (
        0.5 * 9.0 * beta3**2
        + 0.25 * 20.0 * beta3**4
        + 3.0 * (beta2 - p["beta20"]) ** 2
        + 0.04 * gamma**2
        + 0.9 * (beta2 - p["beta20"]) * beta3**2
    )
    coherence = max(0.0, 1.0 - p["alignment_quench"] * f_align)
    target = p["beta3_shell"] * (1.0 + centrifugal_stabilization(spin)) * (1.0 - 0.85 * f_align)
    shell_window = math.exp(-((beta2 - p["beta20"]) / 0.065) ** 2) * math.exp(-(gamma / 18.0) ** 2)
    e_shell = -p["shell_amp"] * coherence * shell_window * math.exp(-((beta3 - target) / 0.05) ** 2)
    moment = p["J0"] * (1.0 + p["J_beta2"] * beta2 + p["J_beta3"] * beta3**2)
    e_rot = spin * (spin + 1.0) / (2.0 * moment)
    # A positive term represents loss of octupole particle-hole coherence when
    # nu h9/2, nu i13/2 and pi h11/2 components align with the cranking axis.
    e_align = p["alignment_penalty"] * f_align * beta3**2
    return {
        "E_ld": e_ld,
        "E_shell": e_shell,
        "E_rot": e_rot,
        "E_align": e_align,
        "J_eff": moment,
        "alignment_fraction": f_align,
        "shell_coherence": coherence,
        "beta3_target": target,
        "E_total": e_ld + e_shell + e_rot + e_align,
    }


def minimize_surface(spin: int, p: dict) -> dict:
    best = None
    for beta2 in BETA2_GRID:
        for gamma in GAMMA_GRID:
            for beta3 in BETA3_GRID:
                terms = components(beta2, gamma, beta3, spin, p)
                row = {"I": spin, "beta2": beta2, "gamma_deg": gamma, "beta3": beta3, **terms}
                if best is None or row["E_total"] < best["E_total"]:
                    best = row
    assert best is not None
    return best


def parity_staggering(spin: int, beta3: float, f_align: float, p: dict) -> float:
    """Phenomenological S(I), anchored to the measured I=1 displacement.

    The low-spin exponential is a parity-tunnelling surrogate.  The second
    term is deliberately explicit: if alignment quenches beta3, the parity
    displacement reopens.  It is not a fit to all measured levels.
    """
    s1 = 0.6591 if p["N"] == 88 else 0.6474 if p["N"] == 90 else 0.62
    floor = 0.025
    low_spin = (s1 - floor) * math.exp(-(spin - 1.0) / 4.0)
    reopening = 0.48 * (f_align**1.25) * max(0.0, 1.0 - beta3 / max(0.18, p["beta3_shell"]))
    return floor + low_spin + reopening


def experimental_anchors() -> dict:
    return {
        "144Ba": {
            "delta_E_keV": {"I=1": 659.1, "I=13": 168.5},
            "locator": "Bucher 2016 PRL 116 112503 PDF pp.3-4/Table I; values transcribed in the existing research note",
            "B_E3_3_to_0_Wu": "48(+25/-34)",
            "high_spin_and_E1_scope": "observed gamma lines to about 10 hbar; GOSIA network through 14+ and 15-; E1 constrained mainly by prior branching ratios/lifetimes",
        },
        "146Ba": {
            "delta_E_keV": {"I=1": 647.4, "I=11": 78.1},
            "locator": "Bucher 2017 PRL 118 152504 PDF pp.2-5/Fig.2/Table I; values transcribed in the existing research note",
            "B_E3_3_to_0_Wu": "48(+21/-29)",
            "high_spin_and_E1_scope": "GOSIA yields through 10 hbar positive and 9 hbar negative; observed E1 decays mainly from 3- and 5-; no absolute E1/lifetime ledger through I=24",
        },
        "148Ba": {
            "delta_E_keV": {},
            "locator": "No high-spin alternating-parity anchor was used here",
            "B_E3_3_to_0_Wu": None,
        },
    }


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def make_plot(minima: dict[str, list[dict]], staggering: dict[str, list[dict]]) -> str:
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        return "matplotlib unavailable; CSV chart data remain the canonical plot input"
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), constrained_layout=True)
    for name, rows in minima.items():
        axes[0].plot([r["I"] for r in rows], [r["beta3"] for r in rows], marker="o", label=name)
        srows = [r for r in staggering[name] if r["S_MeV"] is not None]
        axes[1].plot([r["I"] for r in srows], [1000 * r["S_MeV"] for r in srows], marker="o", label=name)
    axes[0].axvspan(0, 10, color="tab:blue", alpha=0.08, label="centrifugal window")
    axes[0].axvspan(12, 24, color="tab:red", alpha=0.06, label="alignment window")
    axes[0].set(xlabel="I (hbar)", ylabel="optimized beta3", title="Reduced CNS beta3 path")
    axes[1].set(xlabel="I (hbar)", ylabel="S(I) [keV]", title="Parity displacement surrogate")
    for ax in axes:
        ax.grid(alpha=0.25)
        ax.legend(fontsize=8)
    out = ROOT / "cns_ba_octupole_paths.png"
    fig.savefig(out, dpi=180)
    plt.close(fig)
    return str(out.name)


def main() -> None:
    grid_fields = [
        "nucleus", "I", "beta2", "gamma_deg", "beta3", "E_ld", "E_shell", "E_rot",
        "E_align", "J_eff", "alignment_fraction", "shell_coherence", "beta3_target", "E_total",
    ]
    minima_fields = ["nucleus", "I", "beta2", "gamma_deg", "beta3", "E_total", "E_ld", "E_shell", "E_rot", "E_align", "J_eff", "alignment_fraction", "shell_coherence", "beta3_target"]
    staggering_fields = ["nucleus", "I", "beta3_opt", "alignment_fraction", "S_MeV", "S_keV", "source_or_model"]
    all_grid = []
    minima = {}
    staggering = {}
    for name, p in NUCLEI.items():
        minima[name] = []
        staggering[name] = []
        for spin in I_GRID:
            row = minimize_surface(spin, p)
            minima[name].append({"nucleus": name, **row})
            all_grid.extend({"nucleus": name, **components(beta2, gamma, beta3, spin, p), "I": spin, "beta2": beta2, "gamma_deg": gamma, "beta3": beta3} for beta2 in BETA2_GRID for gamma in GAMMA_GRID for beta3 in BETA3_GRID)
            s = None if spin == 0 else parity_staggering(spin, row["beta3"], row["alignment_fraction"], p)
            staggering[name].append({
                "nucleus": name,
                "I": spin,
                "beta3_opt": row["beta3"],
                "alignment_fraction": row["alignment_fraction"],
                "S_MeV": s,
                "S_keV": None if s is None else 1000.0 * s,
                "source_or_model": "undefined at I=0; model surrogate for I>=1; selected anchors are compared in README/note",
            })
    write_csv(ROOT / "cns_ba_energy_grid.csv", all_grid, grid_fields)
    write_csv(ROOT / "cns_ba_minima.csv", [r for rows in minima.values() for r in rows], minima_fields)
    write_csv(ROOT / "cns_ba_staggering.csv", [r for rows in staggering.values() for r in rows], staggering_fields)
    plot_name = make_plot(minima, staggering)
    result = {
        "title": "Reduced CNS-inspired beta2-gamma-beta3 surfaces for 144,146,148Ba",
        "status": "provisional surrogate, not self-consistent CNS output",
        "units": {"energy": "MeV", "spin": "hbar", "gamma": "degree"},
        "grid": {"I": I_GRID, "beta2": BETA2_GRID, "gamma_deg": GAMMA_GRID, "beta3": BETA3_GRID},
        "nuclei": NUCLEI,
        "model_terms": {
            "macroscopic": "Yukawa-plus-exponential-inspired local liquid-drop expansion",
            "microscopic": "cranked Nilsson shell-coherence surrogate with Z=56/N=88-90 window",
            "alignment": "explicit nu h9/2, nu i13/2 and pi h11/2 high-j coherence penalty",
            "rotation": "I(I+1)/(2 J_eff(beta2,beta3))",
        },
        "minima": minima,
        "staggering": staggering,
        "experimental_anchors": experimental_anchors(),
        "artifacts": ["cns_ba_energy_grid.csv", "cns_ba_minima.csv", "cns_ba_staggering.csv", plot_name, "cns_ba_results.json"],
        "reproducibility": {"command": "python3 cns_ba_octupole_model.py", "python": "3", "numpy_required": False},
    }
    with (ROOT / "cns_ba_results.json").open("w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


if __name__ == "__main__":
    main()
