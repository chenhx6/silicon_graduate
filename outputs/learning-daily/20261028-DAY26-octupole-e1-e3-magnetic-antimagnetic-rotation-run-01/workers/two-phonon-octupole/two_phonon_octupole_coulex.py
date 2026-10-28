#!/usr/bin/env python3
"""Toy two-octupole-phonon Coulomb-excitation / doorway-fragmentation model.

This is a reproducible sensitivity calculation, not a fit to Ba/Ra data.
It contains three separable pieces:

1. a harmonic [3 x 3]_J two-phonon multiplet (J=0,2,4,6),
2. doorway coupling to a dense background, and
3. an effective second-order Coulomb amplitude with an optional IVGDR path.

All energies, densities, couplings and phases are explicit input parameters.
The output therefore documents assumptions rather than adding experimental
measurements.  Only numpy from the Python standard scientific environment is
required.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np


J_VALUES = (0, 2, 4, 6)


def harmonic_multiplet(e3_mev: float, shifts_mev: dict[int, float]) -> list[dict]:
    """Return E(2-phonon,J)=2E3+anharmonic shift for J=0,2,4,6."""
    return [
        {
            "J": j,
            "E_harmonic_MeV": float(2.0 * e3_mev),
            "anharmonic_shift_MeV": float(shifts_mev.get(j, 0.0)),
            "E_MeV": float(2.0 * e3_mev + shifts_mev.get(j, 0.0)),
        }
        for j in J_VALUES
    ]


def phonon_b_strengths(t2: float = 1.0) -> dict:
    """Laboratory B ratios from a rank-3 boson creation operator.

    For |3> -> |(3 x 3)J>, the amplitude is sqrt(2) times a Clebsch-Gordan
    coefficient.  With B(3 -> 0)=|t|^2, the four laboratory B values are
    2(2J+1)/7 |t|^2.  Thus the often quoted ``factor two'' is the boson
    occupation factor in a reduced/intrinsic matrix element; individual lab
    B values also carry angular-momentum recoupling factors.
    """
    return {
        str(j): float(2.0 * (2 * j + 1) / 7.0 * t2) for j in J_VALUES
    }


def fragmented_doorway(
    doorway_energy: float,
    n_background: int,
    background_span: tuple[float, float],
    coupling_mev: float,
    seed: int,
) -> dict:
    """Diagonalize one doorway coupled to a random dense background.

    The doorway strength of eigenstate k is |<k|doorway>|^2.  Its weighted
    centroid and variance are invariant under diagonalization; the reported
    FWHM is a descriptive width of the binned strength profile.
    """
    rng = np.random.default_rng(seed)
    bg = np.sort(rng.uniform(background_span[0], background_span[1], n_background))
    h = np.diag(np.r_[doorway_energy, bg])
    v = rng.normal(0.0, coupling_mev, n_background)
    h[0, 1:] = v
    h[1:, 0] = v
    eig, vec = np.linalg.eigh(h)
    strength = np.square(vec[0, :])
    centroid = float(np.sum(strength * eig))
    variance = float(np.sum(strength * (eig - centroid) ** 2))
    # A strength-weighted effective spreading width.  For a Lorentzian this
    # is not exactly the FWHM, but it is robust for a finite toy spectrum.
    gamma_rms = float(2.0 * np.sqrt(max(variance, 0.0)))
    rho = n_background / max(background_span[1] - background_span[0], 1e-12)
    gamma_golden = float(2.0 * np.pi * coupling_mev**2 * rho)
    return {
        "doorway_energy_MeV": doorway_energy,
        "n_background": n_background,
        "background_span_MeV": list(background_span),
        "coupling_sigma_MeV": coupling_mev,
        "seed": seed,
        "level_density_per_MeV": rho,
        "golden_rule_Gamma_down_MeV": gamma_golden,
        "finite_spectrum_Gamma_rms_MeV": gamma_rms,
        "strength_centroid_MeV": centroid,
        "strength_sum": float(np.sum(strength)),
        "eigenenergies_MeV": eig.tolist(),
        "doorway_strengths": strength.tolist(),
    }


def second_order_amplitude(
    e_final: float,
    e_intermediate: float,
    gamma_intermediate: float,
    coupling_product: float,
) -> complex:
    """A = V_fn V_ni /(E_i-E_n+i Gamma/2), with E_i=0 and E_f implicit."""
    del e_final  # retained in the signature to keep the physical contract clear
    return coupling_product / complex(-e_intermediate, gamma_intermediate / 2.0)


def interference_scan(
    e_final: float,
    octupole_path: dict,
    gdr_path: dict,
    phases: np.ndarray,
) -> list[dict]:
    """Scan relative IVGDR phase and return suppression factors."""
    a_oct = second_order_amplitude(e_final, **octupole_path)
    a_gdr = second_order_amplitude(e_final, **gdr_path)
    bare = abs(a_oct) ** 2
    rows = []
    for phase in phases:
        total = a_oct + a_gdr * np.exp(1j * phase)
        rows.append(
            {
                "relative_phase_rad": float(phase),
                "octupole_amplitude_abs": float(abs(a_oct)),
                "gdr_amplitude_abs": float(abs(a_gdr)),
                "coherent_strength": float(abs(total) ** 2),
                "suppression_vs_octupole_only": float(abs(total) ** 2 / bare),
            }
        )
    return rows


def make_case(name: str, e3: float, seed: int, bg_span: tuple[float, float]) -> dict:
    shifts = {0: 0.00, 2: 0.04, 4: 0.09, 6: 0.15}
    multiplet = harmonic_multiplet(e3, shifts)
    # Couplings chosen to span the requested 0.5--1.5 MeV spreading regime
    # through the golden-rule estimate. They are not measured Ba/Ra values.
    fragments = []
    for row in multiplet:
        fragments.append(
            {
                "J": row["J"],
                "fragmentation": fragmented_doorway(
                    row["E_MeV"],
                    n_background=18,
                    background_span=bg_span,
                    coupling_mev=0.150,
                    seed=seed + row["J"],
                ),
            }
        )
    # Effective amplitudes are dimensionless toy couplings.  The gdr path is
    # deliberately allowed to be opposite in phase; this demonstrates a
    # necessary condition for cancellation, not evidence that it occurs.
    scan = interference_scan(
        e_final=multiplet[0]["E_MeV"],
        octupole_path={
            "e_intermediate": e3,
            "gamma_intermediate": 0.20,
            "coupling_product": 1.00,
        },
        gdr_path={
            "e_intermediate": 14.5,
            "gamma_intermediate": 4.0,
            "coupling_product": 10.0,
        },
        phases=np.linspace(0.0, np.pi, 13),
    )
    return {
        "case": name,
        "e3_input_MeV": e3,
        "input_status": "illustrative_model_input_not_experimental_value",
        "two_phonon_multiplet": multiplet,
        "harmonic_B_relative_to_B_3_to_0": phonon_b_strengths(),
        "fragmentation": fragments,
        "ivgdr_interference_scan": scan,
    }


def write_csv(path: Path, results: dict) -> None:
    rows = []
    for case in results["cases"]:
        for item in case["two_phonon_multiplet"]:
            frag = next(x["fragmentation"] for x in case["fragmentation"] if x["J"] == item["J"])
            rows.append(
                {
                    "case": case["case"],
                    "J": item["J"],
                    "E3_input_MeV": case["e3_input_MeV"],
                    "E2phonon_MeV": item["E_MeV"],
                    "Gamma_down_golden_rule_MeV": frag["golden_rule_Gamma_down_MeV"],
                    "Gamma_down_finite_MeV": frag["finite_spectrum_Gamma_rms_MeV"],
                    "strength_sum": frag["strength_sum"],
                }
            )
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, default=Path(__file__).parent)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    cases = [
        # These are deliberately labeled scenarios, not adopted level data.
        make_case("Ba_like_low_energy", 0.90, 14401, (0.8, 4.8)),
        make_case("Ra_like_low_energy", 0.30, 22401, (0.5, 3.5)),
        make_case("generic_3_to_4_MeV_octupole", 1.75, 3501, (2.0, 6.0)),
    ]
    result = {
        "model": "harmonic_two_octupole_phonon_plus_doorway_fragmentation_plus_effective_IVGDR_interference",
        "version": 1,
        "seed_policy": "case seed plus J",
        "caveat": "No case is a fit to 144Ba, 146Ba, or 224Ra data; all background and coupling inputs are illustrative.",
        "cases": cases,
    }
    json_path = args.out_dir / "two_phonon_octupole_coulex_results.json"
    csv_path = args.out_dir / "two_phonon_octupole_coulex_summary.csv"
    json_path.write_text(json.dumps(result, indent=2) + "\n")
    write_csv(csv_path, result)
    print(json_path)
    print(csv_path)


if __name__ == "__main__":
    main()
