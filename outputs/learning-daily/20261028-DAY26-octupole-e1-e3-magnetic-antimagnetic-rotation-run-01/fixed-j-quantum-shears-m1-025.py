#!/usr/bin/env python3
"""Exact two-angular-momentum M1 benchmark; no nucleus or band fit.

Space: |j1 m1> tensor |j2 m2>, fixed j1,j2 and real g1,g2.  There is no
core, pairing, identical-fermion antisymmetrization, or configuration mixing.
In each fixed-M space diagonalize J^2=J1^2+J2^2+2 J1z J2z
                                  +J1+ J2-+J1- J2+.
Apply mu_0=g1 J1z+g2 J2z and mu_+-= -/+ (g1 J1+-+g2 J2+-)/sqrt(2)
directly between eigenvectors. Angular momenta are in hbar units, magnetic
moments in mu_N. Sum all Mi,q and divide by (2Ji+1):
 B(M1;Ji->Jf)=(3/4pi)/(2Ji+1) sum_(Mi,q)|<Jf,Mf|mu_q|Ji,Mi>|^2.

An independent recoupling result is
 <(j1j2)I-1||j1||(j1j2)I>^2
 = [((j1+j2+1)^2-I^2)*(I^2-(j1-j2)^2)]/(4I).
For I' != I, J=j1+j2 has zero matrix element, so j2=-j1 and mu=(g1-g2)j1.
Dividing the reduced squared element by 2I+1 yields the analytic B below.
The direct matrix path never calls this expression.
"""

from __future__ import annotations

import argparse
import json
import math
from functools import lru_cache
from pathlib import Path

import numpy as np


def half_integer_twice(value: float) -> int:
    twice = round(2 * value)
    if value < 0 or abs(2 * value - twice) > 1e-10:
        raise ValueError("j must be a nonnegative integer or half integer")
    return twice


def ladder(j: float, m: float, direction: int) -> float:
    value = j * (j + 1) - m * (m + direction)
    return math.sqrt(max(0.0, value))


class CoupledSpace:
    def __init__(self, j1: float, j2: float):
        self.j1, self.j2 = j1, j2
        self.t1, self.t2 = half_integer_twice(j1), half_integer_twice(j2)
        self.jmin2 = abs(self.t1 - self.t2)
        self.jmax2 = self.t1 + self.t2

    @lru_cache(maxsize=None)
    def basis(self, m2: int) -> tuple[tuple[int, int], ...]:
        return tuple((a, m2 - a) for a in range(-self.t1, self.t1 + 1, 2)
                     if abs(m2 - a) <= self.t2
                     and (m2 - a - self.t2) % 2 == 0)

    @lru_cache(maxsize=None)
    def states(self, m2: int) -> dict[int, np.ndarray]:
        basis = self.basis(m2)
        pos = {pair: i for i, pair in enumerate(basis)}
        matrix = np.zeros((len(basis), len(basis)))
        for col, (a, b) in enumerate(basis):
            ma, mb = a / 2, b / 2
            matrix[col, col] = (self.j1 * (self.j1 + 1)
                                + self.j2 * (self.j2 + 1) + 2 * ma * mb)
            for da in (-2, 2):
                target = (a + da, b - da)
                if target in pos:
                    direction = da // 2
                    matrix[pos[target], col] += (ladder(self.j1, ma, direction)
                                                 * ladder(self.j2, mb, -direction))
        eigenvalues, eigenvectors = np.linalg.eigh(matrix)
        result = {}
        for col, eigenvalue in enumerate(eigenvalues):
            j = (math.sqrt(max(0.0, 1 + 4 * eigenvalue)) - 1) / 2
            i2 = round(2 * j)
            if not math.isclose(eigenvalue, (i2 / 2) * (i2 / 2 + 1),
                                rel_tol=1e-10, abs_tol=1e-10):
                raise ArithmeticError("J² eigenvalue does not match a coupled spin")
            result[i2] = eigenvectors[:, col]
        return result

    def mu(self, mi2: int, q: int, g1: float, g2: float) -> np.ndarray:
        """Rows at Mf=Mi+q, columns at Mi; spherical tensor convention."""
        source = self.basis(mi2)
        target = self.basis(mi2 + 2 * q)
        pos = {pair: i for i, pair in enumerate(target)}
        matrix = np.zeros((len(target), len(source)))
        for col, (a, b) in enumerate(source):
            ma, mb = a / 2, b / 2
            if q == 0:
                matrix[pos[(a, b)], col] = g1 * ma + g2 * mb
            else:
                factor = -q / math.sqrt(2)
                row = pos.get((a + 2 * q, b))
                if row is not None:
                    matrix[row, col] += factor * g1 * ladder(self.j1, ma, q)
                row = pos.get((a, b + 2 * q))
                if row is not None:
                    matrix[row, col] += factor * g2 * ladder(self.j2, mb, q)
        return matrix

    def downward_b_m1(self, i2: int, g1: float, g2: float) -> float:
        if i2 <= self.jmin2 or i2 > self.jmax2 or (i2 - self.jmax2) % 2:
            return 0.0
        f2 = i2 - 2
        strength = 0.0
        for mi2 in range(-i2, i2 + 1, 2):
            vi = self.states(mi2)[i2]
            for q in (-1, 0, 1):
                mf2 = mi2 + 2 * q
                if abs(mf2) > f2:
                    continue
                vf = self.states(mf2)[f2]
                amplitude = vf @ self.mu(mi2, q, g1, g2) @ vi
                strength += float(abs(amplitude) ** 2)
        return 3 / (4 * math.pi) * strength / (i2 + 1)


def analytic_b_m1(j1: float, j2: float, spin: float,
                  g1: float, g2: float) -> float:
    """Racah two-j result in mu_N², defined only for an allowed step."""
    jmin, jmax = abs(j1 - j2), j1 + j2
    if spin <= jmin or spin > jmax or spin < 1:
        return 0.0
    numerator = ((jmax + 1) ** 2 - spin**2) * (spin**2 - jmin**2)
    return 3 / (4 * math.pi) * (g1 - g2) ** 2 * numerator / (4 * spin * (2 * spin + 1))


def classical_b_m1(j1: float, j2: float, spin: float,
                   g1: float, g2: float) -> float:
    """Large-j interior approximation, not an exact quantum expression."""
    if j1 == 0 or j2 == 0 or spin == 0:
        return 0.0
    cosine = (spin**2 - j1**2 - j2**2) / (2 * j1 * j2)
    if abs(cosine) > 1 + 1e-12:
        return 0.0
    transverse2 = ((j1 * j2 / spin) ** 2
                   * max(0.0, 1 - min(1.0, max(-1.0, cosine)) ** 2))
    return 3 / (8 * math.pi) * (g1 - g2) ** 2 * transverse2


def evaluate_case(label: str, j1: float, j2: float,
                  g1: float, g2: float) -> dict:
    space = CoupledSpace(j1, j2)
    rows = []
    for i2 in range(space.jmin2 + 2, space.jmax2 + 1, 2):
        spin = i2 / 2
        direct = space.downward_b_m1(i2, g1, g2)
        analytic = analytic_b_m1(j1, j2, spin, g1, g2)
        rows.append({"Ji": spin, "Jf": spin - 1,
                     "B_direct_muN2": direct,
                     "B_racah_muN2": analytic,
                     "abs_residual_muN2": abs(direct - analytic),
                     "B_classical_muN2": classical_b_m1(j1, j2, spin, g1, g2)})
    max_residual = max((r["abs_residual_muN2"] for r in rows), default=0.0)
    if max_residual > 1e-10:
        raise ArithmeticError(f"direct/Racah mismatch: {max_residual}")
    return {"label": label, "j1": j1, "j2": j2, "g1": g1, "g2": g2,
            "Jmin": space.jmin2 / 2, "Jmax": space.jmax2 / 2,
            "Jmin_downward_B_muN2": 0.0,
            "rows": rows, "max_abs_residual_muN2": max_residual}


def large_j_limits() -> list[dict]:
    rows = []
    for j in (5, 10, 20, 40, 80):
        g1, g2 = 1.0, 0.0
        maximum = 2 * j
        b_max = analytic_b_m1(j, j, maximum, g1, g2)
        exact_end = 3 / (4 * math.pi) * j / 2
        assert math.isclose(b_max, exact_end, rel_tol=1e-13)
        interior = 1.6 * j
        b_interior = analytic_b_m1(j, j, interior, g1, g2)
        b_classical = classical_b_m1(j, j, interior, g1, g2)
        rows.append({"j1_eq_j2": j, "Jmax": maximum,
                     "B_at_Jmax_quantum_muN2": b_max,
                     "B_at_Jmax_classical_muN2": 0.0,
                     "B_at_0p8_Jmax_quantum_muN2": b_interior,
                     "B_at_0p8_Jmax_classical_muN2": b_classical,
                     "interior_quantum_over_classical": b_interior / b_classical})
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_suffix(".json"))
    args = parser.parse_args()
    cases = [evaluate_case("distinguishable-half-integer-blades", 5.5, 4.5, 1.2, -0.3),
             evaluate_case("small-spin-control", 0.5, 0.5, 1.0, 0.0),
             evaluate_case("g-equality-null", 5.5, 4.5, 0.7, 0.7)]
    output = {
        "schema": "fixed-j-quantum-shears-m1-025/v1",
        "scope": "exact two-j Hilbert space; illustrative dimensionless g factors, no nuclear measurement",
        "units": "j and J in hbar; g dimensionless; B(M1) in mu_N^2",
        "formula": "B=3/(4*pi)*(g1-g2)^2*(((j1+j2+1)^2-I^2)*(I^2-(j1-j2)^2))/(4*I*(2*I+1))",
        "cases": cases,
        "large_j_analytic_limits": large_j_limits(),
        "validation": {
            "global_max_abs_direct_vs_racah_muN2": max(c["max_abs_residual_muN2"] for c in cases),
            "equal_g_null_max_muN2": max((r["B_direct_muN2"] for r in cases[-1]["rows"]), default=0.0),
            "Jmax_nonzero_when_g_unequal": cases[0]["rows"][-1]["B_direct_muN2"] > 0,
            "Jmin_has_no_lower_state": True,
        },
        "assumptions_and_limits": [
            "distinguishable angular momenta; identical-particle Pauli restrictions are not imposed",
            "only fixed j1,j2 and g1,g2; no core, pairing, configuration mixing, or energies",
            "classical comparison uses I^2=j1^2+j2^2+2*j1*j2*cos(theta) and interior large-j approximation",
            "numerical residual is eigensolver roundoff, not uncertainty on a measured transition",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8")
    print(f"wrote {args.output}; max residual {output['validation']['global_max_abs_direct_vs_racah_muN2']:.3e} mu_N²")


if __name__ == "__main__":
    main()
