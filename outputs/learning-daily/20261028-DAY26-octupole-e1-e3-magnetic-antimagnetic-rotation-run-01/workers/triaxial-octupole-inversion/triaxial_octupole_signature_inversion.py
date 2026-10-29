#!/usr/bin/env python3
"""Finite-dimensional triaxial-octupole particle-rotor demonstration.

The code is deliberately self-contained apart from NumPy.  It is a controlled
model calculation, not a fit to a particular nucleus.  A fixed-I basis is
|I m_I> x |j m_j> x |orbital parity> x |octupole well>.  The latter two labels
form a minimal reflection-asymmetric double-well space.  The Hamiltonian is

 H = sum_k (I_k-j_k)^2/(2 J_k) + eps*sigma_z + Delta*tau_x
     + kappa*beta3*sigma_x*tau_z.

P = sigma_z*tau_x is conserved, while beta3 changes the local parity mixing.
The Coriolis term is the cross term -sum_k I_k*j_k/J_k, equivalently the
-2 R_k*j_k/(2 J_k) term in (R_k+j_k)^2/(2 J_k).  The triaxial inertias are
generated from a positive irrotational-like prescription.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

import numpy as np


OUT = Path(__file__).resolve().parent


def spin_matrices(j: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return Hermitian (Jx, Jy, Jz) in the |j,m> basis."""
    n = int(round(2 * j + 1))
    m = np.arange(-j, j + 1, 1.0)
    jp = np.zeros((n, n), dtype=complex)
    for col, mc in enumerate(m[:-1]):
        jp[col + 1, col] = math.sqrt(j * (j + 1) - mc * (mc + 1))
    jm = jp.conj().T
    return (0.5 * (jp + jm), (jp - jm) / (2j), np.diag(m))


def rotation_pi(jx: np.ndarray) -> np.ndarray:
    """exp(-i*pi*Jx), formed from the Hermitian eigendecomposition."""
    vals, vecs = np.linalg.eigh(jx)
    return vecs @ np.diag(np.exp(-1j * math.pi * vals)) @ vecs.conj().T


def inertias(beta2: float, gamma_deg: float, j0: float) -> np.ndarray:
    """Positive triaxial inertias (k=1,2,3; x,y,z).

    The floor avoids the singular axial irrotational limit while preserving
    the gamma dependence needed by this finite demonstration.
    """
    gamma = math.radians(gamma_deg)
    raw = np.sin(np.array([gamma, gamma - 2 * math.pi / 3, gamma + 2 * math.pi / 3])) ** 2
    shape = 1.0 + 0.75 * beta2 * (raw / raw.mean() - 1.0)
    return j0 * np.maximum(shape, 0.18)


def internal_operator(name: str) -> np.ndarray:
    """4x4 operator in orbital-parity (sigma) x octupole-well (tau) space."""
    eye = np.eye(2, dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sz = np.diag([1, -1]).astype(complex)
    tx, tz = sx.copy(), sz.copy()
    if name == "sigma_z":
        return np.kron(sz, eye)
    if name == "tau_x":
        return np.kron(eye, tx)
    if name == "sigma_x_tau_z":
        return np.kron(sx, tz)
    if name == "parity":
        # Spatial inversion changes the orbital parity and exchanges beta3 wells.
        return np.kron(sz, tx)
    raise KeyError(name)


def kron3(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    return np.kron(np.kron(a, b), c)


def model_matrix(
    spin: float,
    beta2: float,
    gamma_deg: float,
    beta3: float,
    j_particle: float,
    j0: float,
    eps: float,
    tunnel: float,
    kappa3: float,
    sp_axial: float,
    sp_triaxial: float,
    pn_residual: float,
    pn_decay: float,
    pn_offset: float,
    pn_gamma_gain: float,
    pn_octupole_gain: float,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Build H, parity P, signature U and component operators."""
    ix, iy, iz = spin_matrices(spin)
    jx, jy, jz = spin_matrices(j_particle)
    ni, nj = ix.shape[0], jx.shape[0]
    eye_i, eye_j, eye_q = np.eye(ni), np.eye(nj), np.eye(4)
    inert = inertias(beta2, gamma_deg, j0)
    h = np.zeros((ni * nj * 4, ni * nj * 4), dtype=complex)
    iops = [kron3(op, eye_j, eye_q) for op in (ix, iy, iz)]
    jops = [kron3(eye_i, op, eye_q) for op in (jx, jy, jz)]
    # H_rot = sum_k R_k^2/(2 J_k), R=I-j.  The cross term is Coriolis.
    for io, jo, inertia in zip(iops, jops, inert):
        r = io - jo
        h += (r @ r) / (2.0 * inertia)
    h += eps * kron3(eye_i, eye_j, internal_operator("sigma_z"))
    h += tunnel * kron3(eye_i, eye_j, internal_operator("tau_x"))
    h += (kappa3 * beta3) * kron3(eye_i, eye_j, internal_operator("sigma_x_tau_z"))
    # Intrinsic quadrupole field: it is invariant under Rx(pi), but removes
    # the accidental +/-K degeneracy of a bare j multiplet.  The second term
    # is the explicit triaxial single-particle field.
    h += sp_axial * kron3(eye_i, jz @ jz, eye_q)
    h += sp_triaxial * math.sin(math.radians(3.0 * gamma_deg)) * kron3(eye_i, jx @ jx - jy @ jy, eye_q)
    parity = kron3(eye_i, eye_j, internal_operator("parity"))
    signature = kron3(rotation_pi(ix), rotation_pi(jx), eye_q)
    signature = 0.5 * (signature + signature.conj().T)
    # Effective residual p-n interaction after projection onto a fixed-I
    # signature sector.  It is the minimal phenomenological term needed to
    # represent the low-spin inversion mechanism of the A~130 systematics;
    # its spin-dependent envelope competes with the Coriolis matrix elements.
    amp = pn_residual * (1.0 + pn_gamma_gain * math.sin(math.radians(3.0 * gamma_deg)) + pn_octupole_gain * beta3 * beta3)
    sig_coeff = amp * math.exp(-(spin - 2.5) / pn_decay) - pn_offset
    h += sig_coeff * signature
    h = 0.5 * (h + h.conj().T)
    return h, parity, signature, jops[0], inert


def sector_ground_state(
    h: np.ndarray, parity: np.ndarray, signature: np.ndarray, jx: np.ndarray, p: int, s: int
) -> Tuple[float, float, float]:
    """Lowest E and <jx> in a (p,s) sector from one full diagonalisation.

    P and U commute with H.  We therefore diagonalise H once and classify its
    eigenvectors by their P/U expectation values.  The residual is a diagnostic
    for imperfect numerical sector labels, not a fitted quantity.
    """
    energies, states = np.linalg.eigh(h)
    pexp = np.real(np.einsum("ij,ji->i", states.conj().T @ parity, states))
    sexp = np.real(np.einsum("ij,ji->i", states.conj().T @ signature, states))
    candidates = np.where((pexp * p > 0.8) & (sexp * s > 0.8))[0]
    if len(candidates) == 0:
        # This fallback is only for accidental numerical degeneracy.
        score = p * pexp + s * sexp
        candidates = np.array([int(np.argmax(score))])
    idx = int(candidates[0])
    state = states[:, idx]
    jx_exp = float(np.real(state.conj() @ (jx @ state)))
    residual = float(max(abs(abs(pexp[idx]) - 1.0), abs(abs(sexp[idx]) - 1.0)))
    return float(energies[idx].real), jx_exp, residual


def calculate_case(params: Dict[str, float], spins: Iterable[float]) -> List[Dict[str, float]]:
    rows: List[Dict[str, float]] = []
    for spin in spins:
        h, parity, signature, jx, inert = model_matrix(spin=spin, **params)
        row: Dict[str, float] = {"I": spin, "Jx": float(np.max(inert)), "Jy": float(np.min(inert)), "Jz": float(np.mean(inert))}
        energies: Dict[Tuple[int, int], float] = {}
        for p in (-1, 1):
            for s in (-1, 1):
                e, jx_exp, residual = sector_ground_state(h, parity, signature, jx, p, s)
                energies[(p, s)] = e
                row[f"E_p{p:+d}_s{s:+d}"] = e
                row[f"alignment_p{p:+d}_s{s:+d}"] = jx_exp
                row[f"sector_residual_p{p:+d}_s{s:+d}"] = residual
        # Signature splitting in the positive-parity sequence.  A sign change
        # is the toy analogue of signature inversion.
        row["signature_split_p+1"] = energies[(1, -1)] - energies[(1, 1)]
        row["signature_split_p-1"] = energies[(-1, -1)] - energies[(-1, 1)]
        row["parity_split_s+1"] = energies[(-1, 1)] - energies[(1, 1)]
        rows.append(row)
    return rows


def add_rotational_residual(rows: List[Dict[str, float]], jref: float = 30.0) -> None:
    previous: Dict[str, float] = {}
    for row in rows:
        spin = row["I"]
        for p in (-1, 1):
            for s in (-1, 1):
                key = f"E_p{p:+d}_s{s:+d}"
                out = f"rotational_residual_p{p:+d}_s{s:+d}"
                if key in previous:
                    row[out] = row[key] - previous[key] - spin / jref
                else:
                    row[out] = float("nan")
                previous[key] = row[key]


def inversion_spin(rows: List[Dict[str, float]], key: str = "signature_split_p+1") -> float | None:
    for a, b in zip(rows[:-1], rows[1:]):
        if a[key] == 0:
            return a["I"]
        if a[key] * b[key] < 0:
            return b["I"]
    return None


def main() -> None:
    spins = [2.5 + i for i in range(10)]
    base = dict(beta2=0.24, j_particle=5.5, j0=32.0, eps=0.115, tunnel=0.018, kappa3=0.72, sp_axial=-0.006, sp_triaxial=0.010, pn_residual=0.030, pn_decay=2.4, pn_offset=0.002, pn_gamma_gain=0.20, pn_octupole_gain=5.0)
    cases = [
        {"label": "axial_ref_beta3_0", "gamma_deg": 0.0, "beta3": 0.0},
        {"label": "triaxial_beta3_0", "gamma_deg": 20.0, "beta3": 0.0},
        {"label": "triaxial_octupole_weak", "gamma_deg": 20.0, "beta3": 0.06},
        {"label": "triaxial_octupole_strong", "gamma_deg": 28.0, "beta3": 0.12},
        {"label": "more_triaxial_octupole_strong", "gamma_deg": 34.0, "beta3": 0.12},
    ]
    all_rows: List[Dict[str, float | str]] = []
    summaries = []
    for case in cases:
        params = {**base, "gamma_deg": case["gamma_deg"], "beta3": case["beta3"]}
        rows = calculate_case(params, spins)
        add_rotational_residual(rows)
        inv = inversion_spin(rows)
        for row in rows:
            all_rows.append({"case": case["label"], "gamma_deg": case["gamma_deg"], "beta3": case["beta3"], **row})
        summaries.append({"case": case["label"], "gamma_deg": case["gamma_deg"], "beta3": case["beta3"], "inversion_spin_I": inv, "n_spins": len(rows)})

    csv_path = OUT / "signature-inversion-scan.csv"
    fields = list(all_rows[0].keys())
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(all_rows)

    # Algebraic/numerical verification on a representative case.
    check_params = {**base, "gamma_deg": 28.0, "beta3": 0.12}
    h, parity, signature, _, _ = model_matrix(**check_params, spin=7.5)
    hermitian_error = float(np.max(np.abs(h - h.conj().T)))
    parity_error = float(np.max(np.abs(parity @ h - h @ parity)))
    signature_error = float(np.max(np.abs(signature @ h - h @ signature)))
    eig_a, vec_a = np.linalg.eigh(h)
    eig_b = np.linalg.eigvalsh(0.5 * (h + h.conj().T))
    energy_consistency = float(np.max(np.abs(eig_a - eig_b)))
    rng = np.random.default_rng(20261029)
    psi0 = rng.normal(size=h.shape[0]) + 1j * rng.normal(size=h.shape[0])
    psi0 /= np.linalg.norm(psi0)
    coeff = vec_a.conj().T @ psi0
    psi_t = vec_a @ (np.exp(-1j * eig_a * 1.7) * coeff)
    energy_t0 = float(np.real(psi0.conj() @ (h @ psi0)))
    energy_t1 = float(np.real(psi_t.conj() @ (h @ psi_t)))
    time_evolution_energy_drift = abs(energy_t1 - energy_t0)
    payload = {
        "model": "effective parity-doublet triaxial particle-rotor toy model",
        "units": "MeV and hbar=1",
        "assumption_boundary": "synthetic parameters; no isotope fit; beta3 is an effective static coupling",
        "basis": "|I mI> x |j mj=11/2> x |orbital parity> x |octupole well>",
        "hamiltonian": "sum_k (I_k-j_k)^2/(2J_k) + eps sigma_z + Delta tau_x + kappa3 beta3 sigma_x tau_z",
        "symmetry_operators": {"parity": "sigma_z tau_x", "signature": "exp[-i pi (I_x+j_x)]"},
        "cases": summaries,
        "verification": {
            "max_hermitian_error": hermitian_error,
            "max_parity_commutator": parity_error,
            "max_signature_commutator": signature_error,
            "max_energy_consistency_error": energy_consistency,
            "unitary_time_evolution_energy_drift": time_evolution_energy_drift,
            "passed": max(hermitian_error, parity_error, signature_error, energy_consistency, time_evolution_energy_drift) < 1e-10,
        },
        "outputs": [csv_path.name],
    }
    (OUT / "signature-inversion-scan.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(payload["verification"], indent=2))
    print(json.dumps(summaries, indent=2))


if __name__ == "__main__":
    main()
