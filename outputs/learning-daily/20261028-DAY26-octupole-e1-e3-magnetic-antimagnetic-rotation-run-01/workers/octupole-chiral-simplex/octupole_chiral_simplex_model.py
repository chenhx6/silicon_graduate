#!/usr/bin/env python3
"""Synthetic octupole-chiral signature and simplex model.

The calculation is a deliberately small diagnostic model.  It keeps one
triaxial high-j particle, two local two-state coordinates (chirality and the
sign of beta_3), and a quartic octupole potential.  It is not a fit to 78Br,
130Cs, or 133Ce.  All energies are in MeV and spins are dimensionless.

The script writes CSV/JSON tables and two SVG/PNG figures in its own folder.
Only numpy and matplotlib are required.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


OUT = Path(__file__).resolve().parent


def pauli() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return identity and Pauli matrices in a two-state local basis."""

    i2 = np.eye(2, dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    return i2, sx, sy, sz


def discrete_algebra() -> dict[str, object]:
    """Check the fixed-spin P, R_x(pi), S algebra.

    In a spin-I irrep, R_x(pi)^2=(-1)^(2I).  Parity commutes with spatial
    rotations.  Thus S=P R_x^{-1} commutes with R_x; a claimed nonzero
    [R_x,S] needs an additional antiunitary or a different operator definition.
    """

    _, sx, _, sz = pauli()
    # Use separate parity and rotational factors.  A rotation eigenbasis makes
    # the commuting tensor-product structure explicit; using sx for one
    # factor and a diagonal parity matrix would be an invalid surrogate.
    parity = np.kron(sz, np.eye(2, dtype=complex))
    rx_integer = np.kron(np.eye(2, dtype=complex), sz)
    simplex_integer = parity @ rx_integer.conj().T
    commutator = rx_integer @ simplex_integer - simplex_integer @ rx_integer
    # Two independent exchange operations generate four local states.
    chirality_exchange = np.kron(sx, np.eye(2, dtype=complex))
    octupole_exchange = np.kron(np.eye(2, dtype=complex), sx)
    local_commutator = chirality_exchange @ octupole_exchange - octupole_exchange @ chirality_exchange
    return {
        "integer_spin": {
            "Rx_squared": "+1",
            "Rx_eigenvalues": ["+1", "-1"],
            "P_commutes_with_Rx": True,
            "S_definition": "P Rx^{-1}(pi)",
            "norm_Rx_S_commutator": float(np.linalg.norm(commutator)),
        },
        "half_integer_spin": {
            "Rx_squared": "-1",
            "Rx_eigenvalues": ["+i", "-i"],
            "simplex_eigenvalues_for_p=+1": ["+i", "-i"],
            "simplex_eigenvalues_for_p=-1": ["-i", "+i"],
        },
        "local_exchange_algebra": {
            "basis": ["|L,+>", "|R,+>", "|L,->", "|R,->"],
            "exchange_operators": ["C_chi=tau_x", "P_oct=xi_x"],
            "norm_C_chi_P_oct_commutator": float(np.linalg.norm(local_commutator)),
            "dimension": 4,
        },
        "interpretation": (
            "P and Rx are commuting spatial symmetries. Four local states require "
            "independent chirality and octupole-sign sectors; antiunitary chiral "
            "operations can add a projective phase but are not represented by [Rx,S]."
        ),
    }


def octupole_landscape(
    spin: float,
    *,
    sign: float,
    a0: float = -0.24,
    centrifugal: float = 0.016,
    scale: float = 10.0,
    b: float = 1.0,
    mass: float = 1.0,
    hbar: float = 1.0,
) -> dict[str, float]:
    """Return quartic octupole well observables at spin I.

    V(q)=a(I)q^2+bq^4, with a(I)=a0-sign*centrifugal*I(I+1)/scale^2.
    sign=+1 deepens the double well (centrifugal stabilization); sign=-1
    drives a continuous restoration of q=0.  The WKB gap is only a proxy.
    """

    a = a0 - sign * centrifugal * spin * (spin + 1.0) / scale**2
    qmin = math.sqrt(max(-a / (2.0 * b), 0.0))
    barrier = a * a / (4.0 * b) if a < 0.0 else 0.0
    omega = math.sqrt(max(2.0 * abs(a) / mass, 1.0e-12))
    # A dimensionless instanton action proxy.  It is calibrated only as a
    # qualitative measure of tunnelling suppression, not as a nucleus fit.
    action = math.pi * barrier / (hbar * omega) if barrier > 0.0 else 0.0
    gap = hbar * omega * math.exp(-2.0 * action)
    return {
        "a": a,
        "q_min": qmin,
        "barrier": barrier,
        "omega": omega,
        "wkb_action": action,
        "simplex_gap": gap,
        "restoration_order_parameter": qmin,
    }


def spectrum() -> list[dict[str, float | int | str]]:
    """Build signature/parity branches and requested residual observables."""

    spins = list(range(8, 25))
    j = 11.0 / 2.0
    k = 5.0 / 2.0
    j_perp = math.sqrt(j * (j + 1.0) - k * k)
    j_eff = 22.0
    gamma_deg = 27.0
    beta3 = 0.055
    v_triax = 0.036 * math.sin(math.radians(3.0 * gamma_deg))
    v_oct = 0.22 * beta3
    delta_parity = 0.085
    rows: list[dict[str, float | int | str]] = []

    for parity in (1, -1):
        phase = 0.27 + parity * 0.62
        for signature in (1, -1):
            energies: dict[int, float] = {}
            for spin in spins:
                omega = (spin + 0.5) / j_eff
                e_rot = spin * (spin + 1.0) / (2.0 * j_eff)
                # Opposite parity changes the relative phase of octupole and
                # Coriolis amplitudes.  This is the double modulation.
                v_coriolis = -0.014 * omega * j_perp * math.cos(phase)
                v_sig = v_triax + parity * v_oct + v_coriolis
                e = e_rot + parity * delta_parity / 2.0 + signature * v_sig
                energies[spin] = e
                rows.append(
                    {
                        "spin_I": spin,
                        "parity": parity,
                        "signature": signature,
                        "simplex_integer": parity * signature,
                        "omega": omega,
                        "E_MeV": e,
                        "V_triax_MeV": v_triax,
                        "V_oct_MeV": parity * v_oct,
                        "V_coriolis_MeV": v_coriolis,
                        "V_signature_MeV": v_sig,
                        "gamma_deg": gamma_deg,
                        "beta3": beta3,
                    }
                )

            for spin in spins[1:]:
                e_i = energies[spin]
                e_prev = energies[spin - 1]
                d_e = e_i - e_prev
                baseline = spin / j_eff
                residual = d_e - baseline
                stagger = ((-1) ** (spin + 1)) * d_e / (2.0 * spin)
                for row in rows:
                    if (
                        row["spin_I"] == spin
                        and row["parity"] == parity
                        and row["signature"] == signature
                    ):
                        row["delta_E_rot_MeV"] = residual
                        row["S_I_MeV"] = stagger
                        break
    return rows


def write_csv(rows: list[dict[str, object]], path: Path) -> None:
    fields: list[str] = []
    for row in rows:
        for field in row:
            if field not in fields:
                fields.append(field)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def make_figures(rows: list[dict[str, object]], landscape_rows: list[dict[str, object]]) -> None:
    # Signature residuals, separated by parity and signature.
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.1), sharey=True)
    for axis, parity in zip(axes, (1, -1)):
        for signature, colour in ((1, "tab:blue"), (-1, "tab:orange")):
            selected = [
                row
                for row in rows
                if row["parity"] == parity
                and row["signature"] == signature
                and "S_I_MeV" in row
            ]
            axis.plot(
                [row["spin_I"] for row in selected],
                [1000.0 * row["S_I_MeV"] for row in selected],
                "o-",
                ms=3,
                lw=1.1,
                color=colour,
                label=f"signature {signature:+d}",
            )
        axis.axhline(0.0, color="k", lw=0.6)
        axis.set_title(f"parity p={parity:+d}")
        axis.set_xlabel("spin I")
        axis.grid(alpha=0.2)
    axes[0].set_ylabel("S(I) [keV]")
    axes[1].legend(frameon=False, fontsize=8)
    fig.suptitle("Synthetic Coriolis phase interference in a triaxial octupole rotor")
    fig.tight_layout()
    fig.savefig(OUT / "signature-splitting.svg")
    fig.savefig(OUT / "signature-splitting.png", dpi=180)
    plt.close(fig)

    # Well depth and simplex tunnelling gap for the two rotational responses.
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.1))
    for sign, label, colour in (
        (1.0, "stabilizing centrifugal term", "tab:red"),
        (-1.0, "restoring centrifugal term", "tab:green"),
    ):
        selected = [row for row in landscape_rows if row["centrifugal_sign"] == sign]
        spins = [row["spin_I"] for row in selected]
        axes[0].plot(spins, [row["barrier"] for row in selected], label=label, color=colour)
        axes[1].semilogy(spins, [max(row["simplex_gap"], 1.0e-14) for row in selected], label=label, color=colour)
    axes[0].set(xlabel="spin I", ylabel="octupole barrier [arb.]")
    axes[1].set(xlabel="spin I", ylabel="WKB simplex gap [arb.]")
    for axis in axes:
        axis.grid(alpha=0.2)
        axis.legend(frameon=False, fontsize=8)
    fig.suptitle("Deepening versus restoration of a quartic octupole double well")
    fig.tight_layout()
    fig.savefig(OUT / "simplex-restoration.svg")
    fig.savefig(OUT / "simplex-restoration.png", dpi=180)
    plt.close(fig)


def main() -> None:
    rows = spectrum()
    landscape_rows: list[dict[str, object]] = []
    for sign, name in ((1.0, "stabilizing"), (-1.0, "restoring")):
        for spin in range(0, 31):
            data = octupole_landscape(float(spin), sign=sign)
            landscape_rows.append({"spin_I": spin, "centrifugal_sign": sign, "scenario": name, **data})

    write_csv(rows, OUT / "signature-splitting-results.csv")
    write_csv(landscape_rows, OUT / "simplex-landscape-results.csv")
    make_figures(rows, landscape_rows)

    payload = {
        "model": "triaxial high-j particle plus quartic octupole double well",
        "status": "synthetic diagnostic; not a fit to any nucleus",
        "units": {"energy": "MeV", "spin": "dimensionless", "gap_and_barrier": "arbitrary model units"},
        "parameters": {
            "J_eff_hbar2_per_MeV": 22.0,
            "j": 5.5,
            "K": 2.5,
            "gamma_deg": 27.0,
            "beta3": 0.055,
            "formula_delta_E_rot": "E(I)-E(I-1)-I/J_eff",
            "formula_S": "(-1)^(I+1)[E(I)-E(I-1)]/(2I) for integer I",
            "formula_octupole": "V(q)=a(I)q^2+bq^4; a(I)=a0-sign*c*I(I+1)/scale^2",
            "formula_simplex_gap": "hbar*omega*exp(-2*pi*barrier/(hbar*omega))",
        },
        "discrete_algebra": discrete_algebra(),
        "interpretation": {
            "double_modulation": "V_signature(p,I)=V_triax+p*V_oct+V_Coriolis(p,I), so parity changes the interference phase.",
            "two_regimes": "The residual S(I) branches separate smoothly at low spin and can bifurcate when the Coriolis term becomes comparable to the triaxial and octupole amplitudes.",
            "simplex_boundary": "A deepening double well makes the tunnelling gap exponentially small; q_min grows. A restoring term makes q_min vanish with mean-field exponent 1/2 while the local harmonic gap need not vanish.",
        },
        "files": [
            "signature-splitting-results.csv",
            "simplex-landscape-results.csv",
            "signature-splitting.svg",
            "signature-splitting.png",
            "simplex-restoration.svg",
            "simplex-restoration.png",
        ],
    }
    (OUT / "octupole-chiral-simplex-results.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
