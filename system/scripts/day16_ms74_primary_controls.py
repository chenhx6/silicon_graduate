#!/usr/bin/env python3
"""Original MS74 table/negative-column controls, not an experimental refit."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import sys

import numpy as np

from day14_alignment_formula_contract import polynomial_weights
from day16_pdco_ambiguity_preview import operators, source_parts


def population(j: int | float, ratio: float) -> np.ndarray:
    m = np.arange(-j, j + 1)
    if ratio == 0:
        p = (abs(m) == min(abs(m))).astype(float)
    else:
        p = np.exp(-(m * m - min(m * m)) / (2 * (j * ratio) ** 2))
    return p / p.sum()


def alpha(tj: int, ratio: float) -> np.ndarray:
    spec = polynomial_weights(tj)
    matrix = np.array([[float(x) for x in spec["exact"][k]] for k in (2, 4)])
    return matrix @ population(tj / 2, ratio)


def forward(ji: int, jf: int, delta: float, ratio: float, order: int = 8) -> np.ndarray:
    # Only the integer J=6 worked example uses the earlier mixed photon kernel.
    assert isinstance(ji, int) and isinstance(jf, int)
    rho = np.diag(population(ji, ratio))
    x, weight = np.polynomial.legendre.leggauss(order)
    parts = source_parts(math.atan(delta))
    intensity = np.array([
        sum(np.trace(t @ rho @ t.conj().T).real
            for t in operators(ji, jf, parts, float(np.degrees(np.arccos(c))), 0.))
        for c in x
    ])
    norm = weight @ intensity
    assert norm > 0
    return np.array([(2 * k + 1) * (weight @ (
        intensity * np.polynomial.legendre.legval(x, [0] * k + [1]))) / norm
        for k in (2, 4)])


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", required=True, type=Path)
    p.add_argument("--output", required=True, type=Path)
    args = p.parse_args()
    cfg = json.loads(args.input.read_text())
    root = Path(__file__).resolve().parents[2]
    for source in cfg["sources"]:
        text = (root / source["page"]).read_text()
        path = root / re.search(r'^raw_file: "(.+)"', text, re.M)[1]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == source["raw_sha256"]
    checks = []

    def compare(name: str, calculated: float, printed: str, half_last_digit: str) -> None:
        error = abs(float(calculated) - float(printed))
        ok = bool(error <= float(half_last_digit))
        checks.append({"name": name, "computed": float(calculated), "printed": printed,
                       "absolute_error": error, "half_printed_last_digit": half_last_digit,
                       "rounding_compatible": ok})
        if not ok:
            raise AssertionError(name)

    half = cfg["half_spin_row"]
    predicted = alpha(half["J_twice"], float(half["sigma_over_J"]))
    for k, value in zip((2, 4), predicted):
        compare("DA74_J23p2_alpha" + str(k), value, half["alpha" + str(k) + "_printed"],
                half["half_printed_last_digit"])
    ref = cfg["complete_reference"]
    # Independent, already-derived exact pure-E2 coefficients for the same row.
    ref_exact = [65 / 161, -26 / 161]
    for k, value in zip((2, 4), ref_exact):
        compare("DA74_J23p2_pureE2_Amax" + str(k), value,
                ref["A" + str(k) + "max_printed"], ref["half_printed_last_digit"])
    example = cfg["author_worked"]
    ji, jf = int(example["Ji"]), int(example["Jf"])
    delta = -float(example["delta_magnitude_printed"])
    assert example["negative_column_used_explicitly"]
    maximum = forward(ji, jf, delta, 0.)
    attenuation = alpha(2 * ji, float(example["sigma_over_J"]))
    measured_shape = forward(ji, jf, delta, float(example["sigma_over_J"]))
    convergence = forward(ji, jf, delta, float(example["sigma_over_J"]), order=12)
    wrong_sign = forward(ji, jf, -delta, float(example["sigma_over_J"]))
    assert np.max(abs(measured_shape - maximum * attenuation)) < 1e-13
    assert np.max(abs(measured_shape - convergence)) < 1e-13
    assert abs(wrong_sign[0] - measured_shape[0]) > .1
    assert abs(wrong_sign[1] - measured_shape[1]) < 1e-13
    for index, k in enumerate((2, 4)):
        compare("DMS74_Amax" + str(k), maximum[index],
                example["A2max_negative"] if k == 2 else example["A4max"],
                example["half_printed_last_digit"])
        compare("DMS74_alpha" + str(k), attenuation[index], example["alpha" + str(k)],
                example["half_printed_last_digit"])
        compare("DMS74_expected_A" + str(k), measured_shape[index],
                example["A" + str(k) + "_attenuated"], example["half_printed_last_digit"])
    result = {
        "data_identity": cfg["data_identity"], "kind": cfg["kind"],
        "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "helper_hashes": {name: hashlib.sha256((Path(__file__).parent / name).read_bytes()).hexdigest()
                          for name in ["day14_alignment_formula_contract.py",
                                       "day14_unobserved_feeding_transfer.py",
                                       "day16_pdco_ambiguity_preview.py"]},
        "runtime": {"python": sys.version.split()[0], "numpy": np.__version__},
        "published_rounding_checks": checks,
        "source_example": {
            "delta_signed_negative_column": delta, "sigma_over_J": float(example["sigma_over_J"]),
            "computed_maximum_A2_A4": maximum.tolist(), "computed_alpha": attenuation.tolist(),
            "computed_partial_A2_A4": measured_shape.tolist(),
            "opposite_sign_control_A2_A4": wrong_sign.tolist(),
            "quadrature_8_vs_12_max_difference": float(np.max(abs(measured_shape - convergence))),
            "scope": "Local source-native negative-column implementation control, not a universal sign map"
        },
        "boundaries": cfg["interpretation_boundaries"],
    }
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"identity": result["data_identity"], "rounding_compatible": True,
                      "half_spin_alpha": predicted.tolist(),
                      "source_example": result["source_example"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
