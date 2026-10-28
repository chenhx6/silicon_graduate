#!/usr/bin/env python3
"""Toy symmetry model for a chiral--octupole quadruplet.

The model is deliberately an auditable symmetry toy model, not a fit to 78Br,
134Pr, or 131Ba data.  It uses two localized two-state coordinates: tau for
left/right chirality and xi for the two reflection-asymmetric octupole wells.
The projected basis is labelled by eigenvalues chi=+/-1 of tau_x and
parity p=+/-1 of xi_x.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path


def energy(e0: float, t_chi: float, t_parity: float, t_mix: float,
           chi: int, parity: int) -> float:
    """E = E0 - tχ χ - tπ p - tχπ χp, in keV."""
    return e0 - t_chi * chi - t_parity * parity - t_mix * chi * parity


def symmetry_parameters(I: int, I0: int = 8) -> dict[str, float]:
    """Illustrative spin-dependent tunnelling parameters, all in keV."""
    x = float(I - I0)
    return {
        "e0": 220.0 * (I - I0) + 22.0 * (I * (I + 1) - I0 * (I0 + 1)),
        "t_chiral": 70.0 * math.exp(-0.18 * x),
        "t_parity": 110.0 * math.exp(-0.12 * x),
        "t_mix": 15.0 * math.exp(-0.15 * x),
    }


def angular_factor(Ii: int, lam: int) -> float:
    """Dimensionless stretched-transition factor used only for the toy rates."""
    If = Ii - lam
    return math.sqrt(max(Ii, 1) / (2.0 * Ii + 1.0)) * math.sqrt(If + 1.0)


def transition_rows(levels: dict[int, dict[str, float]]) -> list[dict[str, object]]:
    """Generate four representative channels for each initial projected state."""
    rows: list[dict[str, object]] = []
    # Matrix-element scales are arbitrary but fixed, so the interference signs
    # and selection rules are reproducible. Rates include E_gamma^(2lambda+1).
    m1, e1 = 1.00, 0.82
    q0, qchi, qpar, qchipar = 0.70, 0.22, 0.08, 0.06
    qx0, qxchi, qxpar, qxchipar = 0.12, 0.09, -0.03, 0.04

    for Ii in sorted(levels):
        if Ii < 10:
            continue
        for chi_i in (1, -1):
            for p_i in (1, -1):
                Ei = levels[Ii][f"chi{chi_i:+d}_p{p_i:+d}"]
                channels = [
                    ("M1_chiral_partner", 1, -chi_i, p_i, m1,
                     angular_factor(Ii, 1)),
                    ("E1_parity_partner", 1, chi_i, -p_i, e1,
                     angular_factor(Ii, 1)),
                    ("E2_diagonal_crossover", 2, chi_i, p_i,
                     q0 + chi_i * qchi + p_i * qpar + chi_i * p_i * qchipar,
                     angular_factor(Ii, 2)),
                    ("E2_chiral_crossover_interference", 2, -chi_i, p_i,
                     qx0 + chi_i * qxchi + p_i * qxpar + chi_i * p_i * qxchipar,
                     angular_factor(Ii, 2)),
                ]
                for name, lam, chi_f, p_f, matrix_element, geom in channels:
                    If = Ii - lam
                    Ef = levels[If][f"chi{chi_f:+d}_p{p_f:+d}"]
                    Egamma = Ei - Ef
                    if Egamma <= 0:
                        continue
                    amplitude = matrix_element * geom
                    rate = (Egamma ** (2 * lam + 1)) * amplitude ** 2
                    rows.append({
                        "Ii": Ii, "If": If, "chi_i": chi_i, "p_i": p_i,
                        "chi_f": chi_f, "p_f": p_f, "channel": name,
                        "lambda": lam, "Egamma_keV": Egamma,
                        "matrix_element_toy": matrix_element,
                        "amplitude_toy": amplitude, "rate_arb": rate,
                    })
    peak = max(row["rate_arb"] for row in rows)
    channel_peaks: dict[str, float] = {}
    for row in rows:
        channel_peaks[row["channel"]] = max(
            channel_peaks.get(row["channel"], 0.0), row["rate_arb"]
        )
    for row in rows:
        row["rate_normalized"] = row["rate_arb"] / peak
        row["rate_channel_normalized"] = row["rate_arb"] / channel_peaks[row["channel"]]
    return rows


def build_model(spins: list[int]) -> dict[str, object]:
    level_data: dict[int, dict[str, float]] = {}
    split_rows: list[dict[str, float]] = []
    simplex_rows: list[dict[str, object]] = []
    for I in spins:
        pars = symmetry_parameters(I)
        levels: dict[str, float] = {}
        for chi in (1, -1):
            for p in (1, -1):
                levels[f"chi{chi:+d}_p{p:+d}"] = energy(
                    pars["e0"], pars["t_chiral"], pars["t_parity"],
                    pars["t_mix"], chi, p)
        level_data[I] = levels
        split_rows.append({
            "I": I,
            "delta_chiral_p_plus_keV": levels["chi-1_p+1"] - levels["chi+1_p+1"],
            "delta_chiral_p_minus_keV": levels["chi-1_p-1"] - levels["chi+1_p-1"],
            "delta_parity_chi_plus_keV": levels["chi+1_p-1"] - levels["chi+1_p+1"],
            "delta_parity_chi_minus_keV": levels["chi-1_p-1"] - levels["chi-1_p+1"],
            "t_chiral_keV": pars["t_chiral"],
            "t_parity_keV": pars["t_parity"],
            "t_mix_keV": pars["t_mix"],
        })
    # For integer-spin odd-odd bands alpha=0,1 gives r=+1,-1.  The same
    # formula also handles half-integer alpha and returns +/-i there.
    for parity in (1, -1):
        for alpha in (0, 1):
            r = complex(math.cos(-math.pi * alpha), math.sin(-math.pi * alpha))
            s = parity * r
            simplex_rows.append({
                "I_example": spins[0], "parity": parity, "signature_alpha": alpha,
                "signature_r": [r.real, r.imag], "simplex_s": [s.real, s.imag],
            })

    transitions = transition_rows(level_data)
    return {
        "model_scope": "illustrative symmetry toy model; not a fit to nuclear data",
        "basis_localized": ["|L,+>", "|R,+>", "|L,->", "|R,->"],
        "basis_projected": ["|chi=+,p=+>", "|chi=-,p=+>", "|chi=+,p=->", "|chi=-,p=->"],
        "hamiltonian_keV": "H=E0*1 - t_chi*tau_x - t_parity*xi_x - t_mix*tau_x*xi_x",
        "spins": spins,
        "levels_keV": level_data,
        "splittings": split_rows,
        "simplex_table": simplex_rows,
        "transition_rows": transitions,
        "selection_rules": {
            "E_lambda": "p_f = p_i*(-1)^lambda; |Ii-If| <= lambda <= Ii+If",
            "M_lambda": "p_f = p_i*(-1)^(lambda+1); |Ii-If| <= lambda <= Ii+If",
            "M1_toy": "strong channel: chi_f=-chi_i, p_f=p_i, Delta I=1",
            "E1_toy": "strong channel: chi_f=chi_i, p_f=-p_i, Delta I=1",
            "E2_toy": "p_f=p_i, Delta I=2 crossover; diagonal and chiral-cross terms interfere",
        },
    }


def write_outputs(result: dict[str, object], outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "chiral-octupole-quadruplet-model.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    with (outdir / "chiral-octupole-quadruplet-transitions.csv").open(
        "w", newline="", encoding="utf-8"
    ) as fh:
        rows = result["transition_rows"]
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", type=Path, default=Path(__file__).parent)
    args = parser.parse_args()
    result = build_model([8, 9, 10, 11, 12, 13, 14])
    write_outputs(result, args.outdir)
    print(json.dumps({
        "outdir": str(args.outdir),
        "n_spin_slices": len(result["spins"]),
        "n_transition_rows": len(result["transition_rows"]),
        "max_normalized_rate": max(r["rate_normalized"] for r in result["transition_rows"]),
        "first_splitting": result["splittings"][0],
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
