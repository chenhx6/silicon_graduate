#!/usr/bin/env python3
"""Finite-space constant-pairing BCS solver.

The implementation follows the bounded numerical structure used in Suhonen,
From Nucleons to Nucleus, Chs. 13-14:

    E_a = sqrt((epsilon_a - lambda)^2 + Delta^2)
    v_a^2 = (1 - (epsilon_a - lambda) / E_a) / 2
    N     = sum_a 2*Omega_a*v_a^2
    Delta = G * sum_a Omega_a*u_a*v_a

Here Omega_a is the pair degeneracy (2*j_a + 1)/2.  This is a constant
monopole-pairing baseline.  It does not implement Suhonen's full SDI
self-energy, Lipkin-Nogami number projection, blocking, deformation, or
cranking.
"""

from __future__ import annotations

import math
from typing import Any, Dict, Iterable, List

import numpy as np


def _as_finite_vector(values: Iterable[float], name: str) -> np.ndarray:
    array = np.asarray(list(values), dtype=float)
    if array.ndim != 1 or array.size == 0:
        raise ValueError(f"{name} must be a non-empty one-dimensional sequence.")
    if not np.all(np.isfinite(array)):
        raise ValueError(f"{name} must contain only finite values.")
    return array


def solve_constant_pairing_bcs(
    single_particle_energies_MeV: Iterable[float],
    pair_degeneracies: Iterable[float],
    target_particles: float,
    pairing_strength_MeV: float,
    *,
    initial_gap_MeV: float | None = None,
    max_iterations: int = 1000,
    tolerance: float = 1.0e-10,
    mixing: float = 0.5,
) -> Dict[str, Any]:
    """Solve a finite-space constant-pairing BCS problem.

    Parameters
    ----------
    single_particle_energies_MeV:
        One-body orbital energies epsilon_a.
    pair_degeneracies:
        Omega_a, the number of time-reversed pairs in orbital a.
    target_particles:
        Desired average number of particles in the active space.
    pairing_strength_MeV:
        Positive magnitude G of the attractive pairing force.
    initial_gap_MeV:
        Positive starting gap.  If omitted, use max(G/2, 1e-3 MeV).
    max_iterations, tolerance, mixing:
        Fixed-point controls.  The chemical potential is solved by bisection
        at every gap iteration, so the particle-number constraint is explicit.

    Notes
    -----
    The returned ``gap_MeV`` is a magnitude in the positive-u/v convention.
    A phase-sensitive SDI calculation must carry the orbital phase convention
    and signed matrix elements separately.
    """
    eps = _as_finite_vector(single_particle_energies_MeV, "single_particle_energies_MeV")
    omega = _as_finite_vector(pair_degeneracies, "pair_degeneracies")
    if eps.size != omega.size:
        raise ValueError("single-particle energies and pair degeneracies must have equal length.")
    if np.any(omega <= 0.0):
        raise ValueError("pair degeneracies must be strictly positive.")

    target = float(target_particles)
    strength = float(pairing_strength_MeV)
    tol = float(tolerance)
    mix = float(mixing)
    if not math.isfinite(target) or target < 0.0 or target > 2.0 * float(np.sum(omega)):
        raise ValueError("target_particles must lie within the active-space capacity.")
    if not math.isfinite(strength) or strength <= 0.0:
        raise ValueError("pairing_strength_MeV must be strictly positive.")
    if not math.isfinite(tol) or tol <= 0.0:
        raise ValueError("tolerance must be strictly positive.")
    if not isinstance(max_iterations, int) or max_iterations < 1:
        raise ValueError("max_iterations must be a positive integer.")
    if not math.isfinite(mix) or not 0.0 < mix <= 1.0:
        raise ValueError("mixing must be in the interval (0, 1].")

    capacity = 2.0 * float(np.sum(omega))
    if target == 0.0 or target == capacity:
        occupations = np.zeros_like(eps) if target == 0.0 else np.ones_like(eps)
        return {
            "converged": True,
            "iterations": 0,
            "particle_number": target,
            "target_particles": target,
            "chemical_potential_MeV": (
                float(np.min(eps) - 1.0) if target == 0.0 else float(np.max(eps) + 1.0)
            ),
            "gap_MeV": 0.0,
            "pairing_strength_MeV": strength,
            "phase_convention": "positive u and v; gap reported as magnitude",
            "orbitals": [
                {
                    "epsilon_MeV": float(e),
                    "pair_degeneracy": float(o),
                    "u": float(math.sqrt(max(0.0, 1.0 - v * v))),
                    "v": float(v),
                    "v2": float(v * v),
                    "quasiparticle_energy_MeV": 0.0,
                    "eta_MeV": 0.0,
                }
                for e, v in zip(eps, occupations)
            ],
            "boundary": "Closed active-space endpoint; no finite pairing gap is inferred.",
        }

    scale = max(10.0, 10.0 * strength * float(np.sum(omega)) + 10.0)
    lambda_lo = float(np.min(eps) - scale)
    lambda_hi = float(np.max(eps) + scale)

    def state_at(lambda_value: float, gap_value: float) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
        eta = eps - lambda_value
        energies = np.sqrt(eta * eta + gap_value * gap_value)
        u = np.sqrt(0.5 * (1.0 + eta / energies))
        v = np.sqrt(0.5 * (1.0 - eta / energies))
        particle_number = float(np.sum(2.0 * omega * v * v))
        return eta, energies, u, particle_number

    gap = float(initial_gap_MeV) if initial_gap_MeV is not None else max(strength / 2.0, 1.0e-3)
    if not math.isfinite(gap) or gap <= 0.0:
        raise ValueError("initial_gap_MeV must be finite and strictly positive.")

    converged = False
    lambda_value = 0.5 * (lambda_lo + lambda_hi)
    particle_number = float("nan")
    iterations = 0
    for iterations in range(1, max_iterations + 1):
        # N(lambda) is monotonic, so bisection enforces the number constraint.
        lo, hi = lambda_lo, lambda_hi
        for _ in range(200):
            candidate = 0.5 * (lo + hi)
            _, _, _, n_candidate = state_at(candidate, gap)
            if n_candidate < target:
                lo = candidate
            else:
                hi = candidate
            if abs(n_candidate - target) <= tol:
                lo = candidate
                hi = candidate
                break
        lambda_value = 0.5 * (lo + hi)
        eta, energies, u, particle_number = state_at(lambda_value, gap)
        v = np.sqrt(0.5 * (1.0 - eta / energies))
        gap_fixed_point = strength * float(np.sum(omega * u * v))
        next_gap = (1.0 - mix) * gap + mix * gap_fixed_point
        if abs(particle_number - target) <= tol and abs(next_gap - gap) <= tol:
            gap = next_gap
            converged = True
            break
        gap = next_gap

    eta, energies, u, particle_number = state_at(lambda_value, gap)
    v = np.sqrt(0.5 * (1.0 - eta / energies))
    orbitals: List[Dict[str, float]] = []
    for e, o, et, eqp, ui, vi in zip(eps, omega, eta, energies, u, v):
        orbitals.append(
            {
                "epsilon_MeV": float(e),
                "pair_degeneracy": float(o),
                "eta_MeV": float(et),
                "quasiparticle_energy_MeV": float(eqp),
                "u": float(ui),
                "v": float(vi),
                "v2": float(vi * vi),
            }
        )

    gap_residual = gap - strength * float(np.sum(omega * u * v))
    return {
        "converged": converged,
        "iterations": iterations,
        "particle_number": float(particle_number),
        "target_particles": target,
        "particle_number_residual": float(particle_number - target),
        "chemical_potential_MeV": float(lambda_value),
        "gap_MeV": float(gap),
        "gap_equation_residual_MeV": float(gap_residual),
        "pairing_strength_MeV": strength,
        "phase_convention": "positive u and v; gap reported as magnitude",
        "orbitals": orbitals,
        "boundary": (
            "Constant monopole pairing in a finite spherical space. "
            "No SDI self-energy, Lipkin-Nogami projection, blocking, deformation, "
            "Coriolis term or cranked QRPA response."
        ),
    }


def format_text_report(result: Dict[str, Any]) -> str:
    """Format a compact text report for command-line and notebook use."""
    lines = [
        "BCS constant-pairing finite-space solver",
        f"  converged: {result['converged']} in {result['iterations']} iterations",
        f"  N: {result['particle_number']:.8g} / target {result['target_particles']:.8g}",
        f"  lambda: {result['chemical_potential_MeV']:.8g} MeV",
        f"  Delta: {result['gap_MeV']:.8g} MeV",
        f"  gap residual: {result.get('gap_equation_residual_MeV', 0.0):.3e} MeV",
        "  epsilon [MeV] | Omega | v^2 | E_qp [MeV]",
    ]
    lines.extend(
        f"  {item['epsilon_MeV']:13.6g} | {item['pair_degeneracy']:5.3g} | "
        f"{item['v2']:7.5f} | {item['quasiparticle_energy_MeV']:12.6g}"
        for item in result["orbitals"]
    )
    lines.append(f"  boundary: {result['boundary']}")
    return "\n".join(lines)
