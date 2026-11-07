#!/usr/bin/env python3
"""Small algebra controls for R3 explanations; no real-nucleus calculation.

Angular momenta are dimensionless j=J/hbar. Curvature/rotor examples use an
arbitrary positive energy unit. Source hashes document context, not data fits.
"""

import hashlib
import json
import math
import platform
import sys
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import eigh, expm

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs/l4/20261108-symmetry-projection-controls"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def angular_matrices(spin):
    magnetic = np.arange(-spin, spin + 1, dtype=float)
    raising = np.zeros((len(magnetic), len(magnetic)), complex)
    for index, m in enumerate(magnetic[:-1]):
        raising[index + 1, index] = math.sqrt(spin * (spin + 1) - m * (m + 1))
    lowering = raising.conj().T
    return (raising + lowering) / 2, (raising - lowering) / (2j), np.diag(magnetic)


def d2_projector(spin):
    matrices = angular_matrices(spin)
    identity = np.eye(int(2 * spin + 1))
    rotations = [expm(-1j * math.pi * matrix) for matrix in matrices]
    return (identity + sum(rotations)) / 4


def multiply(first, second):
    result = [Fraction(0) for _ in range(len(first) + len(second) - 1)]
    for i, a in enumerate(first):
        for j, b in enumerate(second):
            result[i + j] += a * b
    return result


def zero_m_three_j_squared(first, second, third):
    total = first + second + third
    if total % 2 or not abs(first - second) <= third <= first + second:
        return Fraction(0)
    half = total // 2
    numerator = math.factorial(half) ** 2
    denominator = math.factorial(total + 1)
    for value in (first, second, third):
        numerator *= math.factorial(total - 2 * value)
        denominator *= math.factorial(half - value) ** 2
    return Fraction(numerator, denominator)


def main():
    checks = {}
    antiunitary = []
    for spin in (0.5, 1, 1.5, 2):
        _, jy, _ = angular_matrices(spin)
        rotation = expm(-1j * math.pi * jy)
        # In this Jz basis T=rotation*K, and C=T*R=(rotation*R.conj())*K.
        time_unitary = rotation
        chiral_unitary = time_unitary @ rotation.conj()
        identity = np.eye(int(2 * spin + 1))
        phase = (-1) ** int(2 * spin)
        t_error = np.linalg.norm(time_unitary @ time_unitary.conj() - phase * identity)
        c_error = np.linalg.norm(chiral_unitary @ chiral_unitary.conj() - identity)
        checks[f"T_and_C_squared_I_{spin}"] = bool(max(t_error, c_error) < 1e-11)
        antiunitary.append({"I": spin, "T_squared": phase, "C_squared": 1,
                            "T_error": float(t_error), "C_error": float(c_error)})

    multiplicities = []
    for spin in range(7):
        projector = d2_projector(spin)
        expected = (2 * spin + 1 + 3 * (-1) ** spin) // 4
        residual = max(np.linalg.norm(projector.conj().T - projector),
                       np.linalg.norm(projector @ projector - projector))
        trace = float(np.trace(projector).real)
        checks[f"integer_D2_projector_I_{spin}"] = bool(
            residual < 1e-11 and abs(trace - expected) < 1e-11
        )
        multiplicities.append({"I": spin, "fixed_M_K_channels": expected, "trace": trace})
    half_projector = d2_projector(0.5)
    half_residual = float(np.linalg.norm(half_projector @ half_projector - half_projector))
    checks["integer_D2_average_is_not_spinor_projector"] = half_residual > 1e-3

    parity_cases = []
    for overlap in (0, 0.2, 0.7):
        h, k = 10.0, 1.0
        norm = np.array([[1, overlap], [overlap, 1]])
        hamiltonian = np.array([[h, k], [k, h]])
        expected = np.sort([(h + k) / (1 + overlap), (h - k) / (1 - overlap)])
        computed = eigh(hamiltonian, norm, eigvals_only=True)
        shift = 3.7
        shifted = eigh(hamiltonian + shift * norm, norm, eigvals_only=True)
        checks[f"nonorthogonal_parity_S_{overlap}"] = bool(
            np.max(abs(computed - expected)) < 1e-11
            and np.max(abs(shifted - computed - shift)) < 1e-11
        )
        parity_cases.append({"S": overlap, "E_plus": (h + k) / (1 + overlap),
                             "E_minus": (h - k) / (1 - overlap)})
    overlap, h = 0.3, 10
    k = h * overlap
    checks["nonzero_offdiagonal_does_not_force_parity_splitting"] = (
        abs((h + k) / (1 + overlap) - (h - k) / (1 - overlap)) < 1e-11 and k != 0
    )

    p3 = [Fraction(0), Fraction(-3, 2), Fraction(0), Fraction(5, 2)]
    cube = multiply(multiply(p3, p3), p3)
    integral_x_cube = sum(
        (2 * value / (power + 2) for power, value in enumerate(cube) if (power + 1) % 2 == 0),
        Fraction(0),
    )
    p1_coefficient = Fraction(3, 2) * integral_x_cube
    checks["cubic_octupole_has_allowed_rank_one"] = p1_coefficient == Fraction(36, 385)
    first = zero_m_three_j_squared(1, 3, 2)
    second = zero_m_three_j_squared(1, 3, 4)
    checks["delta_l_three_not_a_universal_three_j_maximum"] = (
        first == Fraction(3, 35) and second == Fraction(4, 63) and first > second
    )

    jx, jy, jz = angular_matrices(4)
    basis = np.zeros((9, 3))
    basis[4, 0] = 1
    basis[[2, 6], 1] = 1 / math.sqrt(2)
    basis[[0, 8], 2] = 1 / math.sqrt(2)
    rigid = basis.T @ (jx @ jx + 2 * jy @ jy + 4 * jz @ jz) @ basis
    analytic = np.array([[30, -3 * math.sqrt(5), 0],
                         [-3 * math.sqrt(5), 40, -math.sqrt(7)],
                         [0, -math.sqrt(7), 70]])
    energies = np.linalg.eigvalsh(rigid)
    gaps = np.diff(energies)
    checks["rigid_rotor_matrix_from_full_J_operators"] = bool(
        np.linalg.norm(rigid - analytic) < 1e-11
        and np.linalg.norm(d2_projector(4) @ basis - basis) < 1e-11
    )
    checks["fixed_inertia_need_not_be_exactly_harmonic"] = bool(abs(gaps[1] - gaps[0]) > 1)

    roots = [2 - math.sqrt(3), 2 + math.sqrt(3)]
    second_observable = [r * r / (1 + r * r) for r in roots]
    checks["two_roots_one_observable_second_can_distinguish"] = bool(
        all(abs(r / (1 + r * r) - 0.25) < 1e-12 for r in roots)
        and abs(second_observable[0] - second_observable[1]) > 0.8
    )
    checks["quadratic_can_have_no_real_root"] = 1 - 4 < 0  # y=1 for F=delta/(1+delta^2)
    assert all(checks.values()), checks

    OUT.mkdir(parents=True, exist_ok=True)
    result = OUT / "controls.json"
    result.write_text(json.dumps({
        "antiunitary": antiunitary, "D2_multiplicities": multiplicities,
        "half_integer_nonprojector_residual": half_residual, "parity_cases": parity_cases,
        "cubic_octupole_P1_coefficient": str(p1_coefficient),
        "cubic_octupole_integral": "3 sqrt(21)/(55 pi)",
        "three_j_squared": [str(first), str(second)],
        "rigid_I4_matrix": analytic.tolist(), "rigid_I4_energies": energies.tolist(),
        "rigid_I4_gaps": gaps.tolist(), "rational_roots": roots,
        "second_observable": second_observable, "checks": checks,
        "boundary": "Algebra controls in declared model spaces; no nuclear fit, coefficient or discovery",
    }, ensure_ascii=False, indent=2) + "\n")
    sources = [
        "raw/papers/gpt/query/20261108-r3-bohr-1952/originals/bohr-1952-mfm26-14.pdf",
        "raw/papers/gpt/query/20261108-r2-g42-inertia-observables/matsuzaki-2004-nuclear-moments-of-inertia-prc69-034306.pdf",
    ]
    (OUT / "run-provenance.json").write_text(json.dumps({
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "command": "python3 system/scripts/doctoral_r3_symmetry_projection_controls.py",
        "script_sha256": sha(Path(__file__)), "python": sys.version,
        "numpy": np.__version__, "scipy": scipy.__version__, "platform": platform.platform(),
        "source_context": [{"path": p, "sha256": sha(ROOT / p)} for p in sources],
        "artifacts": [{"path": str(result.relative_to(ROOT)), "sha256": sha(result)}],
        "units": "dimensionless j=J/hbar; arbitrary positive energy unit in rotor/parity examples",
        "checks_passed": len(checks), "real_nucleus_calculation": False,
    }, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"checks": len(checks), "all_pass": True,
                      "P3_cubed_P1": str(p1_coefficient), "I4_gaps": gaps.tolist()}))


if __name__ == "__main__":
    main()
