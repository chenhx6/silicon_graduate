#!/usr/bin/env python3
"""Reproducible toy sensitivity ledger for Ra Schiff-moment enhancement.

This is a transparent scaling calculation, not an EDF or atomic-structure
calculation.  It reproduces the perturbative 1/Delta-E factor, a centroid
corrected uniform-density beta2*beta3 scale, and the published Skyrme
coefficient ranges used in the accompanying research note.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def intrinsic_schiff(A: int, Z: int, beta2: float, beta3: float) -> dict[str, float]:
    """Return two common beta2-beta3 convention estimates in e fm^3.

    The first coefficient is the centroid-corrected uniform sharp surface
    derived with normalized spherical harmonics.  The second is the compact
    3/(20*pi) convention often quoted in phenomenological estimates.  Keeping
    both prevents a hidden Y_l0 normalization factor from entering comparisons.
    """
    radius = 1.2 * A ** (1.0 / 3.0)
    exact_coeff = 9.0 / (20.0 * math.pi * math.sqrt(35.0))
    compact_coeff = 3.0 / (20.0 * math.pi)
    return {
        "R0_fm": radius,
        "centroid_corrected_e_fm3": exact_coeff * Z * radius**3 * beta2 * beta3,
        "compact_3_over_20pi_e_fm3": compact_coeff * Z * radius**3 * beta2 * beta3,
        "beta2": beta2,
        "beta3": beta3,
    }


def denominator_scale(delta_keV: float, references_keV: tuple[float, ...]) -> list[dict[str, float]]:
    return [
        {
            "delta_E_keV": delta_keV,
            "reference_E_keV": ref,
            "relative_response_ref_over_delta": ref / delta_keV,
        }
        for ref in references_keV
    ]


def spread(values: list[float]) -> dict[str, float]:
    lo, hi = min(values), max(values)
    return {
        "min": lo,
        "max": hi,
        "range": hi - lo,
        "max_abs_over_min_abs": max(abs(v) for v in values) / min(abs(v) for v in values),
    }


def run() -> dict:
    # Same-J opposite-parity spacings from the cited ENSDF objects.
    ra225 = {"A": 225, "Z": 88, "J": "1/2", "delta_E_keV": 55.16}
    ra223 = {"A": 223, "Z": 88, "J": "3/2", "delta_E_keV": 50.128}

    # Engel et al. PRC 68 (2003), PDF p. 6, gives these SkO' deformation
    # parameters for 225Ra.  This is a geometry scale, not an experimental S.
    geometry_225 = intrinsic_schiff(225, 88, 0.190, 0.146)

    # Dobaczewski & Engel PRL 94 (2005), Tables I-II, coefficients a_i in
    # S = a0*g*gbar0 + a1*g*gbar1 + a2*g*gbar2 [e fm^3].
    models = {
        "SkO_prime_zero_range_direct": [-5.1, 10.4, -10.1],
        "SkO_prime_finite_range_direct": [-1.9, 6.3, -3.8],
        "SkO_prime_finite_range_src_direct": [-1.7, 6.0, -3.5],
        "SkO_prime_finite_range_src_direct_exchange": [-1.5, 6.0, -4.0],
        "SIII": [-1.0, 7.0, -3.9],
        "SkM_star": [-4.7, 21.5, -11.0],
        "SLy4": [-3.0, 16.9, -8.8],
    }
    hg199 = [0.0004, 0.055, 0.009]  # PRL 94 (2005), Eq. (8)
    ra_reference = models["SkO_prime_finite_range_src_direct_exchange"]
    channel_rows = []
    for i, label in enumerate(("gbar0", "gbar1", "gbar2")):
        channel_rows.append(
            {
                "channel": label,
                "ra_reference_e_fm3": ra_reference[i],
                "hg199_e_fm3": hg199[i],
                "nuclear_ratio_abs": abs(ra_reference[i] / hg199[i]),
                "atomic_ratio_with_factor_3": 3.0 * abs(ra_reference[i] / hg199[i]),
            }
        )
    equal_coupling_ra = sum(ra_reference)
    equal_coupling_hg = sum(hg199)

    # Dynamic octupole toy envelope.  c_coherence=1 is the rigid limit;
    # lower values represent a signed matrix-element reduction in a soft/GCM
    # calculation.  This does not claim to replace a collective Hamiltonian.
    dynamic_rows = []
    for beta3_rms in (0.05, 0.10, 0.146):
        for coherence in (0.25, 0.50, 1.00):
            scale = geometry_225["centroid_corrected_e_fm3"] * (beta3_rms / 0.146) * coherence
            dynamic_rows.append(
                {
                    "beta3_rms": beta3_rms,
                    "coherence": coherence,
                    "effective_intrinsic_S_e_fm3": scale,
                    "interpretation": "toy dynamic response envelope; not an EDF prediction",
                }
            )

    out = {
        "schema": "ra225-schiff-amplification/v1",
        "status": "reproducible scaling calculation; not an experimental extraction",
        "references": {
            "dobaczewski_engel_2005": {
                "doi": "10.1103/PhysRevLett.94.232502",
                "raw_pdf": "raw/papers/day26-20261028/2005-dobaczewski-ra225-schiff.pdf",
                "locators": "PDF pp. 2-4, Eqs. (1)-(8), Tables I-II",
            },
            "engel_et_al_2003": {
                "doi": "10.1103/PhysRevC.68.025501",
                "raw_pdf": "raw/papers/day26-20261028/2003-engel-ra225-schiff.pdf",
                "locators": "PDF pp. 2-6 and 8-9, Eqs. (2)-(6), Fig. 3, Table I",
            },
            "nndc_225ra": {
                "source_page": "knowledge/sources/nndc-2009-ra225-adopted-parity-doublet.md",
                "locators": "ENSDF 225088001 adopted low-lying 1/2- at 55.16(6) keV",
            },
            "nndc_223ra": {
                "source_page": "knowledge/sources/nndc-2001-223ra-reference-and-2026-intensity-records.md",
                "locators": "ENSDF 223088001 lines 48-58 and 89-106",
            },
        },
        "same_J_parity_doublets": {
            "225Ra": {
                **ra225,
                "denominator_scales": denominator_scale(ra225["delta_E_keV"], (1000.0, 5000.0)),
                "selection_rule": "J=1/2 PT scalar mixes the 1/2- partner; 31.56-keV 3/2- is not the denominator.",
            },
            "223Ra": {
                **ra223,
                "denominator_scales": denominator_scale(ra223["delta_E_keV"], (1000.0, 5000.0)),
                "selection_rule": "J=3/2 PT scalar mixes the 3/2- partner at 50.128 keV.",
            },
        },
        "intrinsic_geometry_225Ra": geometry_225,
        "model_coefficient_table_e_fm3": models,
        "model_coefficient_spreads": {
            channel: spread([row[i] for row in models.values()])
            for i, channel in enumerate(("gbar0", "gbar1", "gbar2"))
        },
        "channel_comparison_to_199Hg": channel_rows,
        "equal_coupling_comparison": {
            "ra_sum_e_fm3": equal_coupling_ra,
            "hg_sum_e_fm3": equal_coupling_hg,
            "nuclear_ratio_abs": abs(equal_coupling_ra / equal_coupling_hg),
            "note": "Equal couplings expose cancellation dependence; channel ratios are more diagnostic.",
        },
        "dynamic_octupole_toy_envelope": dynamic_rows,
        "controls": {
            "225Ra_denominator_factor_at_1MeV": 1000.0 / 55.16,
            "223Ra_denominator_factor_at_1MeV": 1000.0 / 50.128,
            "geometry_positive_for_positive_beta2_beta3": geometry_225["centroid_corrected_e_fm3"] > 0,
            "all_model_rows_have_three_channels": all(len(v) == 3 for v in models.values()),
        },
    }
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", type=Path, default=Path(__file__).with_suffix(".json"))
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
