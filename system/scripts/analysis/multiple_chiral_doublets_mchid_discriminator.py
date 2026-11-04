#!/usr/bin/env python3
"""Descriptive MChD observables; no automatic identification of chirality.

Source boundaries: Ayangeakaa et al., PRL 110, 172504 (2013), reprint
pp. 3-4 / Fig. 2 / Table I; Kuti et al., PRL 113, 032501 (2014),
pp. 2-5 / Figs. 3-4. Both fulltexts already exist in the Wiki archive.
Different configurations and universal energy/alignment/branching thresholds
are not necessary MChD conditions. All bundled numerical examples are synthetic.

Migration: run_mchid_arbitration retains its positional/keyword arguments.
is_mchid_confirmed is always None; gates_evaluation is removed. The old scalar
alignment_separation_Delta_ix_hbar now means the frequency-weighted absolute
separation on common support, or None. calculate_alignment returns n-1 secants,
not n endpoint/central derivatives. delta_ix_crit is accepted but never applied.
"""

import argparse
from copy import deepcopy
import json

import numpy as np


def _synthetic_preset(same_configuration=False, disjoint=False):
    pair = {
        "name": "Synthetic pair A",
        "data_kind": "synthetic",
        "configuration": "synthetic configuration C" if same_configuration else None,
        "spins": [10.5, 11.5, 12.5, 13.5],
        "energies_B1_keV": [1000.0, 1300.0, 1700.0, 2200.0],
        "energies_B2_keV": [1300.0, 1600.0, 2000.0, 2500.0],
    }
    other = deepcopy(pair)
    other["name"] = "Synthetic pair B"
    other["spins"] = [x + 2 for x in pair["spins"]]
    other["energies_B3_keV"] = other.pop("energies_B1_keV")
    other["energies_B4_keV"] = other.pop("energies_B2_keV")
    if disjoint:
        other["energies_B3_keV"] = [3000.0, 3700.0, 4500.0, 5400.0]
        other["energies_B4_keV"] = [x + 100 for x in other["energies_B3_keV"]]
    return {
        "nucleus": "Synthetic demonstration (no isotope assignment)",
        "description": "Synthetic energies and reference; not measured band data",
        "data_kind": "synthetic",
        "harris_J0": 17.0,
        "harris_J1": 25.0,
        "pair_A": pair,
        "pair_B": other,
        "cross_doublet_branching_ratio": None,
    }


PRESETS = {
    "synthetic_overlap": _synthetic_preset(),
    "synthetic_same_configuration": _synthetic_preset(same_configuration=True),
    "synthetic_no_overlap": _synthetic_preset(disjoint=True),
}
# Preserve unified CLI callers; the historical names no longer designate data.
for _legacy in ("133Ce_classic_mchid", "136Nd_even_even_mchid", "103Rh_A100_mchid"):
    PRESETS[_legacy] = _synthetic_preset()
    PRESETS[_legacy]["description"] += f"; legacy alias {_legacy}"


def _finite_scalar(value, name):
    if isinstance(value, (bool, np.bool_, str, bytes)) or np.ndim(value) != 0:
        raise ValueError(f"{name} must be a finite number")
    try:
        number = float(value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError(f"{name} must be a finite number") from exc
    if not np.isfinite(number):
        raise ValueError(f"{name} must be finite")
    return number


def _vector(values, name):
    try:
        raw = list(values)
    except TypeError as exc:
        raise ValueError(f"{name} must be a nonempty one-dimensional sequence") from exc
    if not raw:
        raise ValueError(f"{name} must be nonempty")
    return np.array([_finite_scalar(x, name) for x in raw], dtype=float)


def _levels(spins, energies):
    spins = _vector(spins, "spins")
    energies = _vector(energies, "energies_keV")
    if len(spins) != len(energies):
        raise ValueError("spins and energies must have equal lengths")
    if np.any(spins < 0) or not np.allclose(2 * spins, np.rint(2 * spins), rtol=0, atol=1e-8):
        raise ValueError("spins must be nonnegative integer or half-integer values")
    if len(spins) > 1:
        step = np.diff(spins)
        if not (np.allclose(step, 1, rtol=0, atol=1e-8)
                or np.allclose(step, 2, rtol=0, atol=1e-8)):
            raise ValueError("spins must increase on a contiguous Delta I=1 or 2 lattice")
    if np.any(energies < 0) or np.any(np.diff(energies) <= 0):
        raise ValueError("excitation energies must be nonnegative and strictly increasing")
    return spins, energies


def _ratios(pair, keys, spins):
    arrays = []
    for key in keys:
        supplied = pair.get(key)
        if supplied is None:
            arrays.append([None] * len(spins))
            continue
        try:
            supplied = list(supplied)
        except TypeError as exc:
            raise ValueError(f"{key} must be a sequence") from exc
        if len(supplied) != len(spins):
            raise ValueError(f"{key} must match the spins length")
        values = [None if x is None else _finite_scalar(x, key) for x in supplied]
        if any(x is not None and x < 0 for x in values):
            raise ValueError(f"{key} cannot contain negative transition-strength ratios")
        arrays.append(values)
    common = [i for i in range(len(spins)) if all(a[i] is not None for a in arrays)]
    present = any(x is not None for a in arrays for x in a)
    return {
        "status": "supplied" if present else "unknown",
        "band_1": arrays[0],
        "band_2": arrays[1],
        "common_spins_hbar": [float(spins[i]) for i in common],
        "absolute_difference": [abs(arrays[1][i] - arrays[0][i]) for i in common],
        "units": "mu_N^2/(e^2 b^2); caller must supply consistent transition definitions",
        "interpretation": "Caller-supplied ratios; no phase or absolute strengths inferred",
    }


class MultipleChiralDoubletsDiscriminator:
    """Historical class name, now a quantitative descriptor only."""

    def __init__(self, harris_J0=17.0, harris_J1=25.0):
        self.J0 = _finite_scalar(harris_J0, "harris_J0")
        self.J1 = _finite_scalar(harris_J1, "harris_J1")

    def _reference(self, frequency):
        return self.J0 * frequency + self.J1 * frequency**3

    def calculate_alignment(self, spins, energies_keV):
        """Secants: x=hbar*omega=Delta E/Delta I (MeV), at spin midpoints.

        Use I_x ~= I_mid + 1/2 (K=0/high-spin approximation), then subtract
        J0*x + J1*x^3 in hbar units. This is a stated numerical convention,
        not a reconstruction of Kuti's K=1/2 reduction. A single level has no
        frequency. No endpoint frequency is invented.
        """
        spins, energies = _levels(spins, energies_keV)
        frequency = np.diff(energies) * 1e-3 / np.diff(spins)
        projected = (spins[1:] + spins[:-1]) / 2 + 0.5
        return frequency, projected - self._reference(frequency)

    def _curve(self, spins, energies):
        frequency, alignment = self.calculate_alignment(spins, energies)
        midpoints = (spins[1:] + spins[:-1]) / 2
        return {
            "frequency_MeV": frequency.tolist(),
            "spin_midpoints_hbar": midpoints.tolist(),
            "alignment_hbar": alignment.tolist(),
        }

    def _compare(self, first, second):
        """Compare equally weighted band groups on their common support.

        Interpolate I_x linearly and evaluate the same Harris reference at
        shared frequencies, avoiding artifacts from interpolating a cubic
        reference on different grids. Nonmonotonic/duplicate frequencies
        have no single-valued interpolation here and return unknown.
        """
        curves = first + second
        result = {
            "status": "unknown",
            "common_frequency_support_MeV": None,
            "frequency_MeV": [],
            "group_1_alignment_hbar": [],
            "group_2_alignment_hbar": [],
            "absolute_difference_hbar": [],
            "mean_absolute_separation_hbar": None,
        }
        frequencies = [np.array(c["frequency_MeV"]) for c in curves]
        if any(len(x) == 0 for x in frequencies):
            result["status"] = "insufficient_alignment_points"
            return result
        if any(np.any(np.diff(x) <= 0) for x in frequencies):
            result["status"] = "nonmonotonic_frequency"
            return result
        low, high = max(x[0] for x in frequencies), min(x[-1] for x in frequencies)
        if low > high:
            result["status"] = "no_common_frequency_support"
            return result
        grid = np.unique(np.concatenate(([low, high], *[
            x[(x >= low) & (x <= high)] for x in frequencies
        ])))

        def projected(group, points):
            return np.mean([
                np.interp(points, c["frequency_MeV"],
                          np.array(c["spin_midpoints_hbar"]) + 0.5)
                for c in group
            ], axis=0)

        difference = projected(first, grid) - projected(second, grid)
        # Include zero crossings for an exact integral of the piecewise-linear
        # absolute difference when the pairs exchange alignment ordering.
        roots = [
            grid[i] - difference[i] * (grid[i + 1] - grid[i])
            / (difference[i + 1] - difference[i])
            for i in range(len(grid) - 1) if difference[i] * difference[i + 1] < 0
        ]
        grid = np.unique(np.concatenate((grid, roots)))
        projected1, projected2 = projected(first, grid), projected(second, grid)
        ix1 = projected1 - self._reference(grid)
        ix2 = projected2 - self._reference(grid)
        separation = np.abs(projected1 - projected2)
        mean = (float(separation[0]) if low == high else
                float(np.sum((separation[1:] + separation[:-1]) * np.diff(grid) / 2)
                      / (high - low)))
        result.update({
            "status": "available",
            "common_frequency_support_MeV": [float(low), float(high)],
            "frequency_MeV": grid.tolist(),
            "group_1_alignment_hbar": ix1.tolist(),
            "group_2_alignment_hbar": ix2.tolist(),
            "absolute_difference_hbar": separation.tolist(),
            "mean_absolute_separation_hbar": mean,
            "averaging": "single_shared_frequency" if low == high else
                         "integral_absolute_difference_over_frequency_width",
        })
        return result

    def evaluate_pair(self, pair_data):
        """Energies must share the supplied spin grid and excitation zero.

        Optional parities=[band_1, band_2] use '+'/'-' (unknown: None).
        Optional bm1_be2_ratios_B1/B2 (or B3/B4) follow that same spin grid,
        with None for unmeasured transitions. The legacy phase boolean is
        retained only as an unverified caller annotation.
        """
        if not isinstance(pair_data, dict):
            raise ValueError("pair_data must be a mapping")
        if "spins" not in pair_data:
            raise ValueError("pair_data requires spins")
        variants = [
            keys for keys in (("energies_B1_keV", "energies_B2_keV"),
                             ("energies_B3_keV", "energies_B4_keV"))
            if any(k in pair_data for k in keys)
        ]
        if len(variants) != 1 or not all(k in pair_data for k in variants[0]):
            raise ValueError("supply exactly one complete energy pair: B1/B2 or B3/B4")
        keys = variants[0]
        spins, e1 = _levels(pair_data["spins"], pair_data[keys[0]])
        _, e2 = _levels(pair_data["spins"], pair_data[keys[1]])
        parities = pair_data.get("parities", [None, None])
        if (not isinstance(parities, (list, tuple)) or len(parities) != 2
                or any(p not in ("+", "-", None) for p in parities)):
            raise ValueError("parities must contain two entries from '+', '-', None")
        phase = pair_data.get("bm1_be2_staggering_in_phase")
        if phase is not None and not isinstance(phase, bool):
            raise ValueError("bm1_be2_staggering_in_phase must be boolean or None")
        ratio_keys = tuple(k.replace("energies_", "bm1_be2_ratios_").replace("_keV", "")
                           for k in keys)
        curves = [self._curve(spins, e) for e in (e1, e2)]
        delta = np.abs(e2 - e1)
        return {
            "name": pair_data.get("name", "Unlabelled pair"),
            "data_kind": pair_data.get("data_kind", "caller_supplied_unverified"),
            "configuration": pair_data.get("configuration"),
            "configuration_status": "unknown" if pair_data.get("configuration") is None
                                    else "caller_assignment_not_inferred",
            "spins": spins.tolist(),
            "parities": list(parities),
            "same_parity": None if None in parities else parities[0] == parities[1],
            "energy_splittings_keV": delta.tolist(),
            "mean_energy_splitting_keV": float(np.mean(delta)),
            "min_energy_splitting_keV": float(np.min(delta)),
            "alignment_curves": curves,
            "within_pair_alignment": self._compare([curves[0]], [curves[1]]),
            "bm1_be2_ratios": _ratios(pair_data, ratio_keys, spins),
            "staggering_in_phase": phase,
            "staggering_status": "unknown" if phase is None else "caller_annotation_unverified",
            "absolute_transition_strengths": {"status": "unknown",
                                             "reason": "No lifetime/mixing-ratio analysis supplied"},
        }

    def arbitrate_mchid(self, pair_A_data, pair_B_data, cross_branching_ratio=None,
                        delta_ix_crit=None):
        first, second = self.evaluate_pair(pair_A_data), self.evaluate_pair(pair_B_data)
        cross = None if cross_branching_ratio is None else _finite_scalar(
            cross_branching_ratio, "cross_branching_ratio")
        if cross is not None and cross < 0:
            raise ValueError("cross_branching_ratio must be nonnegative")
        legacy = None if delta_ix_crit is None else _finite_scalar(delta_ix_crit, "delta_ix_crit")
        if legacy is not None and legacy < 0:
            raise ValueError("delta_ix_crit must be nonnegative when supplied")
        comparison = self._compare(first["alignment_curves"], second["alignment_curves"])
        kinds = [first["data_kind"], second["data_kind"]]
        kind = ("synthetic" if all(k == "synthetic" for k in kinds) else
                "mixed_synthetic_and_caller_supplied" if "synthetic" in kinds else
                "caller_supplied_unverified")
        return {
            "schema_version": 2,
            "analysis_kind": "quantitative_descriptors_only",
            "data_kind": kind,
            "pair_A_analysis": first,
            "pair_B_analysis": second,
            "alignment_comparison": comparison,
            "alignment_separation_Delta_ix_hbar": comparison["mean_absolute_separation_hbar"],
            "cross_doublet_branching_ratio": cross,
            "cross_branching_status": "unknown" if cross is None else "caller_supplied_unverified",
            "cross_branching_boundary": "Intensity ratio, not a probability; corrections and "
                                       "transition identities require separate evidence",
            "is_mchid_confirmed": None,
            "diagnostic_verdict": "DESCRIPTORS ONLY: physical MChD assignment remains unassessed",
            "legacy_delta_ix_crit_ignored": legacy,
            "alignment_convention": {
                "frequency": "hbar*omega=Delta E/Delta I in MeV; adjacent-level secants",
                "projection": "I_x ~= I_mid + 1/2, K=0/high-spin approximation",
                "harris_J0_hbar2_per_MeV": self.J0,
                "harris_J1_hbar4_per_MeV3": self.J1,
                "reference_status": "caller/default reference, not fitted to a cited experiment",
                "comparison": "linear I_x interpolation on all four bands' common support; "
                              "same Harris reference; no extrapolation",
            },
            "evidence_boundary": "Energies, alignments, ratios and configuration labels do not "
                                 "alone confirm/reject chirality; no universal thresholds applied",
        }


def run_mchid_arbitration(nucleus="Generic", harris_J0=17.0, harris_J1=25.0,
                          pair_A=None, pair_B=None, cross_branching=None, delta_ix_crit=None):
    """Compatibility entry point; any omitted pair is visibly synthetic."""
    default = PRESETS["synthetic_overlap"]
    if pair_A is None:
        pair_A = deepcopy(default["pair_A"])
    if pair_B is None:
        pair_B = deepcopy(default["pair_B"])
    result = MultipleChiralDoubletsDiscriminator(harris_J0, harris_J1).arbitrate_mchid(
        pair_A, pair_B, cross_branching, delta_ix_crit)
    result["nucleus"] = nucleus
    result["nucleus_status"] = "caller label only; synthetic examples are not isotope measurements"
    return result


def format_text_report(output, title="MChD Quantitative Descriptor Report"):
    comparison = output["alignment_comparison"]
    lines = [
        title,
        f"Nucleus label: {output['nucleus']}",
        f"Data kind: {output['data_kind']}",
        output["diagnostic_verdict"],
        f"Common-frequency alignment comparison: {comparison['status']}",
        f"Common hbar*omega support (MeV): {comparison['common_frequency_support_MeV']}",
        f"Mean absolute alignment separation (hbar): {comparison['mean_absolute_separation_hbar']}",
        f"Cross-doublet intensity ratio: {output['cross_doublet_branching_ratio']} "
        f"({output['cross_branching_status']})",
    ]
    for label in ("A", "B"):
        pair = output[f"pair_{label}_analysis"]
        lines.extend([
            f"Pair {label}: {pair['name']} [{pair['data_kind']}]",
            f"  Configuration: {pair['configuration']} ({pair['configuration_status']})",
            f"  Same parity: {pair['same_parity']}",
            f"  Splittings (keV): {pair['energy_splittings_keV']}",
            f"  B(M1)/B(E2): {pair['bm1_be2_ratios']['status']}; "
            f"phase: {pair['staggering_status']}; absolute strengths: unknown",
        ])
    lines.append(output["evidence_boundary"])
    if output["legacy_delta_ix_crit_ignored"] is not None:
        lines.append("Legacy delta_ix_crit was ignored; it is not a physical criterion.")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="MChD descriptors (synthetic demonstrations)")
    parser.add_argument("--preset", choices=list(PRESETS), default="synthetic_overlap")
    parser.add_argument("--cross-br", type=float, help="Caller-supplied cross/intraband intensity ratio")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    cfg = PRESETS[args.preset]
    result = run_mchid_arbitration(
        nucleus=cfg["nucleus"], harris_J0=cfg["harris_J0"], harris_J1=cfg["harris_J1"],
        pair_A=cfg["pair_A"], pair_B=cfg["pair_B"], cross_branching=args.cross_br)
    print(json.dumps(result, indent=2, allow_nan=False) if args.json else
          format_text_report(result, title=f"{args.preset}: {cfg['description']}"))


if __name__ == "__main__":
    main()
