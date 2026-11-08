#!/usr/bin/env python3
"""Finite algebra controls for the A130 antiunitary/two-reference-state audit.

No nuclear spectrum, tunneling rate, matrix element or measurement is fitted.
The general Hermitian pencil is compared with direct orthonormal spectra.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
import scipy
from scipy.linalg import eigh


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs/l4/20261108-A130-chiral-nonorthogonal-controls"


def spectrum(h, k, overlap):
    a = 1 - abs(overlap) ** 2
    assert a > 0
    b = h - np.real(k * np.conj(overlap))
    discriminant = b**2 - a * (h**2 - abs(k) ** 2)
    assert discriminant > -1e-11
    radius = np.sqrt(max(0.0, discriminant))
    return np.array([(b - radius) / a, (b + radius) / a])


def matrices(h, k, overlap):
    return (
        np.array([[h, k], [np.conj(k), h]], dtype=complex),
        np.array([[1, overlap], [np.conj(overlap), 1]], dtype=complex),
    )


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    checks = {}
    original_h = np.array([[0, 1], [1, 0]], dtype=complex)
    left = np.array([np.sqrt(3) / 2, 0.5j])
    right = left.conj()  # antiunitary C=K in this abstract orthonormal basis
    basis = np.column_stack([left, right])
    pencil_h = basis.conj().T @ original_h @ basis
    metric = basis.conj().T @ basis
    h = float(np.real(pencil_h[0, 0]))
    k = pencil_h[0, 1]
    overlap = metric[0, 1]
    checks["C_squared_one_and_H_C_symmetric"] = bool(
        np.allclose(right.conj(), left) and np.allclose(original_h.conj(), original_h)
    )
    checks["equal_diagonals_but_overlap_and_coupling_not_same_phase"] = bool(
        np.allclose(pencil_h[0, 0], pencil_h[1, 1])
        and np.allclose(overlap, 0.5)
        and np.allclose(k, -0.5j * np.sqrt(3))
        and abs(np.imag(k * np.conj(overlap))) > 0.1
    )
    exact = np.linalg.eigvalsh(original_h)
    generalized = eigh(pencil_h, metric, eigvals_only=True)
    formula = spectrum(h, k, overlap)
    checks["general_pencil_recovers_original_real_spectrum"] = bool(
        np.allclose(exact, [-1, 1]) and np.allclose(generalized, exact)
        and np.allclose(formula, exact)
    )
    wrong = np.array([(h + k) / (1 + overlap), (h - k) / (1 - overlap)])
    checks["unqualified_real_branch_formula_fails"] = bool(
        np.max(np.abs(wrong.imag)) > 0.1
    )
    shift = 3.25
    shifted = eigh(pencil_h + shift * metric, metric, eigvals_only=True)
    checks["energy_shift_is_H_plus_cN"] = bool(
        np.allclose(shifted, exact + shift)
        and np.allclose(spectrum(h + shift, k + shift * overlap, overlap), shifted)
    )
    angle = 0.317
    phase = np.exp(-2j * angle)
    checks["relative_phase_invariant"] = bool(
        np.allclose(
            (k * phase) * np.conj(overlap * phase), k * np.conj(overlap)
        ) and np.allclose(spectrum(h, k * phase, overlap * phase), exact)
    )
    real_signed_difference = -2.0  # h=0, k=1, S=0; plus/minus labels not ordered
    checks["signed_branch_difference_is_not_positive_gap"] = bool(
        real_signed_difference < 0 and np.allclose(spectrum(0, 1, 0), [-1, 1])
    )
    constant_h, constant_n = matrices(2, 2 * (0.3 + 0.4j), 0.3 + 0.4j)
    checks["constant_operator_in_nonorthogonal_basis"] = bool(
        np.allclose(constant_h, 2 * constant_n)
        and np.allclose(eigh(constant_h, constant_n, eigvals_only=True), [2, 2])
    )

    channel_rows = []
    for hh, kk, ss in [
        (1.0, 0.4 + 0.2j, 0),
        (0.3, 0.7 - 0.2j, 0.3 + 0.4j),
        (-0.2, -0.8 + 0.3j, -0.2 + 0.6j),
        (0.5, 0.01 + 0.02j, 0.99),
    ]:
        hm, nm = matrices(hh, kk, ss)
        expected = eigh(hm, nm, eigvals_only=True)
        calculated = spectrum(hh, kk, ss)
        assert np.allclose(expected, calculated, rtol=1e-10, atol=1e-11)
        channel_rows.append({
            "h": hh, "k_real_imag": [kk.real, kk.imag],
            "S_real_imag": [complex(ss).real, complex(ss).imag],
            "eigenvalues": expected.tolist(),
        })
    checks["four_declared_complex_pencils"] = True

    angular_momentum = np.array([1.0, 2.0, 3.0])
    transformed = np.diag([1.0, -1.0, 1.0]) @ angular_momentum
    checks["C_m_axis_does_not_restore_full_J_direction"] = bool(
        np.allclose(transformed, [1, -2, 3])
        and not np.allclose(transformed, angular_momentum)
    )
    jp, jh, core = np.array([1, 1, 0]), np.array([0, 1, 1]), np.array([1, 2, 1])
    total = jp + jh + core
    checks["three_nonzero_total_components_do_not_imply_nonzero_triple_product"] = bool(
        np.all(total != 0) and np.dot(jp, np.cross(jh, core)) == 0
    )
    assert all(checks.values()), checks
    OUT.mkdir(parents=True, exist_ok=True)
    result_path = OUT / "controls.json"
    result_path.write_text(json.dumps({
        "checks": checks, "counterexample_eigenvalues": exact.tolist(),
        "metric_eigenvalues": np.linalg.eigvalsh(metric).tolist(),
        "unqualified_branch_eigenvalues_real_imag": [
            [z.real, z.imag] for z in wrong
        ],
        "complex_pencils": channel_rows,
        "vector_example": {
            "J": angular_momentum.tolist(), "C_J": transformed.tolist(),
            "coplanar_vectors_total": total.tolist(), "triple_product": 0,
        },
        "boundary": "Abstract finite Hilbert-space/vector controls; not measured nuclear inputs",
    }, indent=2) + "\n")
    inputs = [
        "raw/writing/gpt/A130/review-inputs/G64-v1/section-3-5.md",
        "raw/papers/1997_Frauendorf et al_Tilted rotation of triaxial nuclei.pdf",
        "raw/papers/2001_Frauendorf_Spontaneous symmetry breaking in rotating nuclei.pdf",
    ]
    (OUT / "run-provenance.json").write_text(json.dumps({
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "producer": str(Path(__file__).relative_to(ROOT)),
        "producer_sha256": sha(Path(__file__)), "python": sys.version,
        "numpy": np.__version__, "scipy": scipy.__version__, "context_inputs": [
            {"path": p, "sha256": sha(ROOT / p)} for p in inputs
        ],
        "artifacts": [{
            "path": str(result_path.relative_to(ROOT)), "sha256": sha(result_path),
        }],
        "check_count": len(checks),
        "four_pencil_tolerances": {"rtol": 1e-10, "atol": 1e-11},
        "real_nucleus_calculation": False,
    }, indent=2) + "\n")
    print(json.dumps({"checks": len(checks), "all_pass": True}))


if __name__ == "__main__":
    main()
