#!/usr/bin/env python3
"""Generate an auditable chiral--octupole selection-rule matrix.

This is a symmetry toy model.  It does not fit 78Br, 131Ba, 134Pr, or any
other nucleus.  The useful output is the discrete-label bookkeeping and the
dimensionless strength proxies used in the research note.  A projected state
is labelled by (eta, parity), where eta is the symmetric/antisymmetric branch
of the effective left/right chiral exchange and parity is the exact laboratory
parity.  The local operators tau_z and xi_z flip eta and parity, respectively.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from typing import Any


State = tuple[int, int]


def d2_character_table() -> list[dict[str, Any]]:
    """Return the D2 character table in the (Rx,Ry,Rz) convention."""
    return [
        {"irrep": "A", "Rx": 1, "Ry": 1, "Rz": 1},
        {"irrep": "Bx", "Rx": 1, "Ry": -1, "Rz": -1},
        {"irrep": "By", "Rx": -1, "Ry": 1, "Rz": -1},
        {"irrep": "Bz", "Rx": -1, "Ry": -1, "Rz": 1},
    ]


def simplex_table() -> list[dict[str, Any]]:
    """Return s_x = p r_x for integer and half-integer sequences."""
    rows: list[dict[str, Any]] = []
    for spin_class, alphas in (("odd-odd integer-I", (0, 1)),
                               ("odd-A half-integer-I", (-0.5, 0.5))):
        for alpha in alphas:
            r = complex(math.cos(-math.pi * alpha), math.sin(-math.pi * alpha))
            for parity in (1, -1):
                s = parity * r
                rows.append({
                    "spin_class": spin_class,
                    "signature_alpha": alpha,
                    "parity": parity,
                    "r_x": [round(r.real, 12), round(r.imag, 12)],
                    "s_x": [round(s.real, 12), round(s.imag, 12)],
                })
    return rows


def symmetry_rows() -> list[dict[str, Any]]:
    """The derived channel matrix, with leading operator orders."""
    return [
        {
            "channel": "intra_band_M1_dI1",
            "multipole": "M1",
            "delta_I": "1",
            "delta_eta": 0,
            "delta_parity": 0,
            "operator_component": "tau_0 xi_0",
            "leading_amplitude": "m_00^(1)",
            "matrix_order": "O(1) or configuration-mixing suppressed",
            "group_status": "allowed",
            "diagnostic": "same-band Delta-I=1 M1; measure mixing ratio/polarization",
        },
        {
            "channel": "intra_band_E2_dI1_mixed",
            "multipole": "E2",
            "delta_I": "1",
            "delta_eta": 0,
            "delta_parity": 0,
            "operator_component": "tau_0 xi_0",
            "leading_amplitude": "q_00^(1)",
            "matrix_order": "O(epsilon_rot) relative to Delta-I=2 E2",
            "group_status": "allowed",
            "diagnostic": "Delta-I=1 E2 component of an M1/E2 mixed transition",
        },
        {
            "channel": "intra_band_E2_dI2",
            "multipole": "E2",
            "delta_I": "2",
            "delta_eta": 0,
            "delta_parity": 0,
            "operator_component": "tau_0 xi_0",
            "leading_amplitude": "q_00^(2)",
            "matrix_order": "O(1)",
            "group_status": "allowed",
            "diagnostic": "rotational crossover; use as the quadrupole collectivity baseline",
        },
        {
            "channel": "chiral_partner_M1_dI1",
            "multipole": "M1",
            "delta_I": "1",
            "delta_eta": 1,
            "delta_parity": 0,
            "operator_component": "tau_z xi_0",
            "leading_amplitude": "m_10^(1)",
            "matrix_order": "O(1) in a chiral-odd current component",
            "group_status": "allowed",
            "diagnostic": "same-parity chiral link; left/right current sum or difference can cancel",
        },
        {
            "channel": "chiral_partner_E2_dI1",
            "multipole": "E2",
            "delta_I": "1",
            "delta_eta": 1,
            "delta_parity": 0,
            "operator_component": "tau_z xi_0",
            "leading_amplitude": "q_10^(1)",
            "matrix_order": "O(epsilon_chi) or configuration-mixing suppressed",
            "group_status": "allowed",
            "diagnostic": "E2 admixture in the Delta-I=1 chiral link; interferes in angular observables with M1",
        },
        {
            "channel": "chiral_partner_E2_dI2",
            "multipole": "E2",
            "delta_I": "2",
            "delta_eta": 1,
            "delta_parity": 0,
            "operator_component": "tau_z xi_0",
            "leading_amplitude": "q_10^(2)",
            "matrix_order": "O(epsilon_chi) or phase-cancellation suppressed",
            "group_status": "allowed",
            "diagnostic": "same-parity chiral crossover; compare with the intra-band E2 baseline",
        },
        {
            "channel": "parity_partner_E1_dI1",
            "multipole": "E1",
            "delta_I": "1",
            "delta_eta": 0,
            "delta_parity": 1,
            "operator_component": "tau_0 xi_z",
            "leading_amplitude": "d_01^(1)",
            "matrix_order": "O(beta_3) or octupole-correlation amplitude",
            "group_status": "allowed",
            "diagnostic": "same-chirality parity link; E1 is cancellation-sensitive and not sufficient for static beta_3",
        },
        {
            "channel": "parity_partner_E3_dI3",
            "multipole": "E3",
            "delta_I": "3 (favored; triangle rule also applies)",
            "delta_eta": 0,
            "delta_parity": 1,
            "operator_component": "tau_0 xi_z",
            "leading_amplitude": "o_01^(3)",
            "matrix_order": "O(beta_3) and collective radial moment",
            "group_status": "allowed",
            "diagnostic": "direct E3 network; more collective than E1 but still requires lifetimes/absolute B(E3)",
        },
        {
            "channel": "cross_E1_dI1",
            "multipole": "E1",
            "delta_I": "1",
            "delta_eta": 1,
            "delta_parity": 1,
            "operator_component": "tau_z xi_z",
            "leading_amplitude": "d_11^(1)",
            "matrix_order": "O(epsilon_chi beta_3) or O(epsilon_chi epsilon_3)",
            "group_status": "leading direct term zero in factorized one-phonon limit",
            "diagnostic": "cross link tests chiral-octupole coupling; B suppression is quadratic in the small amplitude",
        },
        {
            "channel": "cross_E3_dI3",
            "multipole": "E3",
            "delta_I": "3 (favored; triangle rule also applies)",
            "delta_eta": 1,
            "delta_parity": 1,
            "operator_component": "tau_z xi_z",
            "leading_amplitude": "o_11^(3)",
            "matrix_order": "O(epsilon_chi beta_3) or a two-phonon mixed kernel",
            "group_status": "leading direct term zero in factorized one-phonon limit",
            "diagnostic": "cross E3 is a high-value companion test, not a guaranteed strong link",
        },
    ]


def level_energy(I: int, eta: int, parity: int) -> float:
    """Synthetic energies used only to provide reproducible E_gamma factors."""
    x = I - 10
    e0 = 700.0 + 420.0 * x + 23.0 * I * (I + 1)
    t_chi = 46.0 * math.exp(-0.14 * x)
    t_pi = 82.0 * math.exp(-0.10 * x)
    t_mix = 10.0 * math.exp(-0.12 * x)
    return e0 - eta * t_chi - parity * t_pi - eta * parity * t_mix


def b_proxy(amplitude: float, Ii: int) -> float:
    """Dimensionless B/B_W proxy; the W.u. scale is set to one by definition."""
    return amplitude * amplitude / (2.0 * Ii + 1.0)


def gamma_proxy(Egamma: float, b_hat: float, lam: int) -> float:
    """Reduced-width proxy with the universal E_gamma^(2lambda+1) factor."""
    return max(Egamma, 0.0) ** (2 * lam + 1) * b_hat


def numeric_diagnostics(spins: list[int]) -> list[dict[str, Any]]:
    """Create one dimensionless diagnostic row per initial spin."""
    rows: list[dict[str, Any]] = []
    # Coefficients are synthetic reduced amplitudes in Weisskopf-normalized units.
    m_intra = 0.28
    m_chiral = 0.92
    e1_direct = 0.84
    e1_cross = 0.06
    e3_direct = 0.72
    e3_cross = 0.045
    e2_intra = 1.00
    e2_chiral = 0.18
    for Ii in spins:
        If1, If2, If3 = Ii - 1, Ii - 2, Ii - 3
        eg_m1 = level_energy(Ii, 1, 1) - level_energy(If1, -1, 1)
        eg_e1 = level_energy(Ii, 1, 1) - level_energy(If1, 1, -1)
        eg_e3 = level_energy(Ii, 1, 1) - level_energy(If3, 1, -1)
        eg_e2 = level_energy(Ii, 1, 1) - level_energy(If2, 1, 1)
        bm1_same = b_proxy(m_intra, Ii)
        bm1_chiral = b_proxy(m_chiral, Ii)
        be1_direct = b_proxy(e1_direct, Ii)
        be1_cross = b_proxy(e1_cross, Ii)
        be3_direct = b_proxy(e3_direct, Ii)
        be3_cross = b_proxy(e3_cross, Ii)
        be2_intra = b_proxy(e2_intra, Ii)
        be2_chiral = b_proxy(e2_chiral, Ii)
        ratio_b = bm1_chiral / be1_direct
        ratio_gamma = gamma_proxy(eg_m1, bm1_chiral, 1) / gamma_proxy(eg_e1, be1_direct, 1)
        cross_e1_supp = be1_cross / be1_direct
        cross_e3_supp = be3_cross / be3_direct
        # M1/E2 angular-distribution interference proxy.  It is not a total
        # gamma-width sum: distinct multipoles add incoherently to the width.
        delta = -0.30
        mixed_coherent = m_chiral + delta * e2_chiral
        cancellation_index = mixed_coherent * mixed_coherent / (m_chiral * m_chiral + (delta * e2_chiral) ** 2)
        rows.append({
            "Ii": Ii,
            "Egamma_M1_chiral_keV": round(eg_m1, 6),
            "Egamma_E1_direct_keV": round(eg_e1, 6),
            "Egamma_E3_direct_keV": round(eg_e3, 6),
            "Egamma_E2_intra_keV": round(eg_e2, 6),
            "Bhat_M1_intra": bm1_same,
            "Bhat_M1_chiral": bm1_chiral,
            "Bhat_E1_direct": be1_direct,
            "Bhat_E1_cross": be1_cross,
            "Bhat_E3_direct": be3_direct,
            "Bhat_E3_cross": be3_cross,
            "Bhat_E2_intra_dI2": be2_intra,
            "Bhat_E2_chiral_dI2": be2_chiral,
            "R_B_M1chiral_over_E1direct": ratio_b,
            "R_Gamma_M1chiral_over_E1direct": ratio_gamma,
            "sigma_E1_cross_over_direct": cross_e1_supp,
            "sigma_E3_cross_over_direct": cross_e3_supp,
            "R_E2_chiral_over_intra": be2_chiral / be2_intra,
            "M1_E2_angular_cancellation_index": cancellation_index,
            "synthetic_input": True,
        })
    return rows


def build_payload() -> dict[str, Any]:
    spins = [10, 11, 12, 13, 14]
    payload: dict[str, Any] = {
        "model_scope": "symmetry and dimensionless-strength toy model; not a nuclear-data fit",
        "basis_localized": ["|L,+>", "|R,+>", "|L,->", "|R,->"],
        "basis_projected": ["|eta=+,p=+>", "|eta=-,p=+>", "|eta=+,p=->", "|eta=-,p=->"],
        "operator_tensor_basis": "O_ab = tau_z^a xi_z^b; delta_eta=a and delta_p=b modulo 2",
        "hamiltonian": "H_I=E0(I)-t_chi(I) tau_x-t_pi(I) xi_x-t_chipi(I) tau_x xi_x",
        "projected_energy": "E_I(eta,p)=E0(I)-eta*t_chi-p*t_pi-eta*p*t_chipi",
        "parity_operator": "P=xi_x in the local octupole-well basis",
        "chiral_exchange": "effective unitary tau_x in the truncated L/R subspace; the microscopic TR_y(pi) is antiunitary",
        "d2_group": "D2={1,Rx(pi),Ry(pi),Rz(pi)}; odd-A uses the double group",
        "simplex_operator": "S_x=P R_x(pi)^(-1), s_x=p r_x, r_x=exp(-i pi alpha)",
        "d2_character_table": d2_character_table(),
        "simplex_table": simplex_table(),
        "selection_rule_matrix": symmetry_rows(),
        "numeric_diagnostics": numeric_diagnostics(spins),
        "normalization": {
            "Bhat": "B/B_W in a fixed multipole-specific Weisskopf normalization, dimensionless",
            "R_B_M1_over_E1": "Bhat(M1)/Bhat(E1), dimensionless; compare widths after E_gamma^3 and ICC corrections",
            "R_Gamma_M1_over_E1": "[E_M1/E_E1]^3 * R_B for same lambda=1, with a fixed electromagnetic-unit convention",
            "R_E2": "Bhat(E2; I->I-2) or a ratio to the same-band E2 baseline",
            "cross_suppression": "Bhat(cross)/Bhat(direct), expected O(|epsilon_chi|^2) when the amplitude is O(epsilon_chi beta_3)",
        },
        "validation": {
            "parity_rule": "E_lambda: p_f=p_i*(-1)^lambda; M_lambda: p_f=p_i*(-1)^(lambda+1)",
            "triangle_rule": "abs(Ii-If)<=lambda<=Ii+If",
            "simplex_rule": "s_f^* s_i = pi_X * exp(-i*pi*mu) for a fixed x-quantized tensor component mu",
            "factorized_cross_limit": "d_11=o_11=0 when the one-body operator factorizes into a chiral-even times octupole-odd part",
            "interference_boundary": "M1/E2 amplitudes interfere in angular-distribution/polarization observables; total unpolarized gamma widths add multipoles incoherently",
        },
    }
    return payload


def write_outputs(outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    (outdir / "chiral_octupole_selection_rule_matrix.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    rows = payload["selection_rule_matrix"]
    with (outdir / "chiral_octupole_selection_rule_matrix.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    numeric = payload["numeric_diagnostics"]
    with (outdir / "chiral_octupole_dimensionless_criteria.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(numeric[0]))
        writer.writeheader()
        writer.writerows(numeric)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--outdir", type=Path, default=Path(__file__).parent)
    args = parser.parse_args()
    write_outputs(args.outdir)
    payload = build_payload()
    checks = {
        "d2_irreps": len(payload["d2_character_table"]) == 4,
        "simplex_rows": len(payload["simplex_table"]) == 8,
        "selection_rows": len(payload["selection_rule_matrix"]) == 10,
        "numeric_rows": len(payload["numeric_diagnostics"]) == 5,
        "cross_is_suppressed": all(
            row["sigma_E1_cross_over_direct"] < 0.01 and row["sigma_E3_cross_over_direct"] < 0.01
            for row in payload["numeric_diagnostics"]
        ),
    }
    if not all(checks.values()):
        raise SystemExit(json.dumps(checks, indent=2))
    print(json.dumps({"status": "ok", "outdir": str(args.outdir), "checks": checks}, indent=2))


if __name__ == "__main__":
    main()
