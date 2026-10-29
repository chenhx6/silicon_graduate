#!/usr/bin/env python3
"""Conditional AMR critical-frequency and Landau-damping calculations.

The first block is the analytic two-blade particle-plus-rotor limit used by
Roy et al.  It deliberately separates the intrinsic shear frequency from the
spin at closure: the former depends on V_pinu and j_pi, whereas j_nu and the
core inertia set the closure spin.  The second block is a transparent RPA /
golden-rule proxy for a soft scissors mode coupled to a particle-hole
continuum.  It is a reproducible mechanism demonstration, not an EDF or
projected many-body calculation.
"""
from __future__ import annotations

import csv
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent


def omega_c_intrinsic(v_pinu: float, j_pi: float) -> float:
    """Return hbar*omega_c in MeV in the minimal P2 shear Hamiltonian.

    With E(theta)=V P2(cos(theta))-2*hbar*omega*j_pi*cos(theta), stationarity
    gives cos(theta)=omega/omega_c and hbar*omega_c=3V/(2*j_pi).
    """
    return 3.0 * v_pinu / (2.0 * j_pi)


def closure_spin(j_nu: float, j_pi: float, j_core: float, v_pinu: float) -> float:
    """Classical total spin at c=cos(theta)=1 (in hbar units)."""
    omega_c = omega_c_intrinsic(v_pinu, j_pi)
    return j_nu + 2.0 * j_pi + j_core * omega_c


def fixed_spin_coupling(j_nu: float, j_pi: float, j_core: float,
                        v_pinu: float, spin: float) -> dict[str, float]:
    """Solve the P2 particle-plus-rotor stationary point at fixed spin.

    E(I,c)=(I-j_nu-2*j_pi*c)^2/(2*j_core)+V P2(c).
    The j_core=0 branch is the pure-shears limit.  Frequencies are in MeV
    after setting hbar=1, and spins/inertias retain hbar units.
    """
    omega_c = omega_c_intrinsic(v_pinu, j_pi)
    if j_core == 0.0:
        c = (spin - j_nu) / (2.0 * j_pi)
        omega = omega_c * c
    else:
        denominator = 2.0 * j_pi + j_core * omega_c
        c = (spin - j_nu) / denominator
        omega = omega_c * c
    c_clip = max(-1.0, min(1.0, c))
    theta = math.degrees(math.acos(c_clip))
    return {
        "spin_hbar": spin,
        "cos_theta": c,
        "theta_deg": theta,
        "hbar_omega_MeV": omega,
        "hbar_omega_c_intrinsic_MeV": omega_c,
        "closure_spin_hbar": closure_spin(j_nu, j_pi, j_core, v_pinu),
    }


def gaussian(x: float, mu: float, sigma: float) -> float:
    return math.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * math.sqrt(2.0 * math.pi))


def chi0(energy: float, ph_energies: list[float], couplings: list[float], eta: float) -> complex:
    """Retarded unperturbed response in the convention hbar=1."""
    result = 0j
    for eph, f in zip(ph_energies, couplings):
        result += f * f * (1.0 / (energy - eph + 1j * eta)
                            - 1.0 / (energy + eph + 1j * eta))
    return result


def rpa_response(energy: float, ph_energies: list[float], couplings: list[float],
                 kappa: float, eta: float) -> complex:
    """Separable RPA response chi_RPA=chi0/(1-kappa*chi0)."""
    bare = chi0(energy, ph_energies, couplings, eta)
    return bare / (1.0 - kappa * bare)


def mode_energy(omega: float, omega_c: float, omega0: float = 0.38,
                floor: float = 0.04) -> float:
    """Phenomenological scissors softening energy in MeV."""
    if omega_c <= 0.0:
        return floor
    reduced = max(0.0, 1.0 - (omega / omega_c) ** 2)
    return floor + (omega0 - floor) * math.sqrt(reduced)


def landau_width(two_phonon_energy: float, g: float = 0.022,
                 continuum_mu: float = 0.105, continuum_sigma: float = 0.060) -> float:
    """Golden-rule energy width Gamma=2*pi*g^2*rho(E), in MeV."""
    rho = gaussian(two_phonon_energy, continuum_mu, continuum_sigma)
    return 2.0 * math.pi * g * g * rho


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        fields: list[str] = []
        for row in rows:
            for key in row:
                if key not in fields:
                    fields.append(key)
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    # Roy-style parameter sets.  Cd values are model inputs, not independent
    # measurements of a bare two-body matrix element.
    systems = [
        {"nucleus": "106Cd", "N": 58, "j_nu": 18.0, "j_pi": 4.5,
         "j_core": 0.0, "V_pinu": 1.2, "V_pipi": 0.15,
         "bandhead_hbar": 18, "termination_hbar": 24,
         "observed_top_hbar": 26, "termination_note": "26+ is effective-lifetime top feed"},
        {"nucleus": "108Cd", "N": 60, "j_nu": 16.0, "j_pi": 4.5,
         "j_core": 0.0, "V_pinu": 1.2, "V_pipi": 0.15,
         "bandhead_hbar": 16, "termination_hbar": 24,
         "observed_top_hbar": 22, "termination_note": "AMR configuration quoted through 24+"},
        {"nucleus": "110Cd", "N": 62, "j_nu": 10.0, "j_pi": 4.5,
         "j_core": 19.5, "V_pinu": 1.2, "V_pipi": 0.15,
         "bandhead_hbar": 12, "termination_hbar": None,
         "observed_top_hbar": 28, "termination_note": "28+ not assigned to AMR by Roy et al."},
        {"nucleus": "102Pd", "N": 56, "j_nu": None, "j_pi": None,
         "j_core": None, "V_pinu": None, "V_pipi": None,
         "bandhead_hbar": None, "termination_hbar": None,
         "observed_top_hbar": None, "termination_note": "No verified AMR lifetime table in local evidence"},
        {"nucleus": "104Pd", "N": 58, "j_nu": 16.0, "j_pi": 4.5,
         "j_core": 5.0, "V_pinu": 1.2, "V_pipi": 0.2,
         "bandhead_hbar": 16, "termination_hbar": None,
         "observed_top_hbar": 26, "termination_note": "26+ has effective lifetime"},
    ]

    system_rows: list[dict] = []
    for system in systems:
        if system["j_nu"] is None:
            system_rows.append({**system, "hbar_omega_c_intrinsic_MeV": None,
                                "closure_spin_model_hbar": None,
                                "data_status": "missing-local-evidence"})
            continue
        omega_c = omega_c_intrinsic(system["V_pinu"], system["j_pi"])
        closure = closure_spin(system["j_nu"], system["j_pi"], system["j_core"], system["V_pinu"])
        for spin in range(system["bandhead_hbar"], system["observed_top_hbar"] + 1, 2):
            row = fixed_spin_coupling(system["j_nu"], system["j_pi"], system["j_core"],
                                      system["V_pinu"], float(spin))
            system_rows.append({"nucleus": system["nucleus"], "N": system["N"],
                                "bandhead_hbar": system["bandhead_hbar"],
                                "termination_hbar": system["termination_hbar"],
                                "observed_top_hbar": system["observed_top_hbar"],
                                "termination_note": system["termination_note"],
                                "j_nu": system["j_nu"], "j_pi": system["j_pi"],
                                "j_core_hbar2_per_MeV": system["j_core"],
                                "V_pinu_MeV": system["V_pinu"],
                                "V_pipi_MeV": system["V_pipi"],
                                "hbar_omega_c_intrinsic_MeV": omega_c,
                                "closure_spin_model_hbar": closure,
                                "data_status": "model-row",
                                **row})

    write_csv(HERE / "isotope_systematics.csv", system_rows)

    critical_rows: list[dict] = []
    for v in (0.6, 0.9, 1.2, 1.5, 1.8):
        for jpi in (4.0, 4.5, 5.0):
            for jcore in (0.0, 5.0, 19.5):
                for jnu in (10.0, 16.0, 18.0):
                    oc = omega_c_intrinsic(v, jpi)
                    critical_rows.append({
                        "V_pinu_MeV": v, "j_pi_hbar": jpi, "j_nu_hbar": jnu,
                        "J_core_hbar2_per_MeV": jcore,
                        "hbar_omega_c_intrinsic_MeV": oc,
                        "closure_spin_hbar": closure_spin(jnu, jpi, jcore, v),
                        "formula": "hbar*omega_c=3*V_pinu/(2*j_pi); I_c=j_nu+2*j_pi+J_core*omega_c",
                    })
    write_csv(HERE / "critical_frequency_scan.csv", critical_rows)

    # A discrete particle-hole spectrum used only to evaluate the response.
    ph_energies = [0.030, 0.070, 0.105, 0.145, 0.210, 0.290, 0.410, 0.560]
    couplings = [0.010, 0.014, 0.020, 0.018, 0.014, 0.011, 0.008, 0.006]
    omega_c = omega_c_intrinsic(1.2, 4.5)
    damping_rows: list[dict] = []
    for index in range(101):
        ratio = 0.02 + 0.98 * index / 100.0
        omega = ratio * omega_c
        one_phonon = mode_energy(omega, omega_c)
        two_phonon = 2.0 * one_phonon
        gamma = landau_width(two_phonon)
        response = rpa_response(two_phonon, ph_energies, couplings, kappa=0.85, eta=0.004)
        damping_rows.append({
            "omega_over_omega_c": ratio,
            "hbar_omega_MeV": omega,
            "scissors_one_phonon_MeV": one_phonon,
            "two_phonon_energy_MeV": two_phonon,
            "rho_ph_at_two_phonon_per_MeV": gaussian(two_phonon, 0.105, 0.060),
            "Gamma_Landau_MeV": gamma,
            "Gamma_over_two_phonon": gamma / two_phonon,
            "chi0_real": response.real,
            "chi0_imag": response.imag,
            "RPA_response_abs": abs(response),
        })
    write_csv(HERE / "landau_damping_scan.csv", damping_rows)

    result = {
        "status": "conditional-model-and-evidence-ledger",
        "units": {"energies": "MeV", "spins": "hbar", "inertia": "hbar^2/MeV"},
        "analytic_model": {
            "energy": "E(I,c)=(I-j_nu-2*j_pi*c)^2/(2*J_core)+V_pinu*P2(c)",
            "intrinsic_closure": "c=omega/omega_c, hbar*omega_c=3*V_pinu/(2*j_pi)",
            "closure_spin": "I_c=j_nu+2*j_pi+J_core*omega_c",
            "boundary": "j_nu and J_core do not enter intrinsic omega_c in this minimal Hamiltonian; they set the spin offset and closure spin.",
            "extended_convention": "If frequency is redefined from total spin, a shifted critical point can be quoted, but it is convention-dependent and is not the intrinsic shear frequency.",
            "be2": "B(E2)/B(E2,90deg)=sin(theta)^4=(1-c^2)^2",
        },
        "rpa_model": {
            "chi0": "sum_ph |F_ph|^2[(E-E_ph+i eta)^-1-(E+E_ph+i eta)^-1]",
            "chi_rpa": "chi0/(1-kappa*chi0)",
            "golden_rule": "Gamma=2*pi*g^2*rho_ph(2*Omega_s)",
            "status": "phenomenological response proxy; no claim of microscopic Cd/Pd fit",
            "ph_energies_MeV": ph_energies,
            "couplings": couplings,
            "kappa": 0.85,
            "eta_MeV": 0.004,
        },
        "evidence_ledger": {
            "Roy_2011": "106Cd: bandhead 18, configuration termination 24, observed 26 effective; 108Cd: bandhead 16, AMR interval through 24; 110Cd: 12+ model bandhead, 28+ not assigned to AMR.",
            "Rather_2014": "104Pd: Table 1 B(E2) sequence 16+--26+, fitted J_core=5 hbar^2/MeV, V_pinu=1.2 MeV.",
            "102Pd": "No verified local AMR lifetime/systematics table; retained as missing evidence.",
            "source_independence": "Roy and Rather are related particle-plus-rotor lineages; not independent determinations of V_pinu.",
        },
    }
    (HERE / "amr_critical_frequency_results.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({"files": ["critical_frequency_scan.csv", "landau_damping_scan.csv",
                                  "isotope_systematics.csv", "amr_critical_frequency_results.json"]},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
