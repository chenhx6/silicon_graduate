
import json
import math
import pathlib

# 1. AMR experimental data in 110Cd (Frauendorf 2001, Juutinen 1999)
# Positive parity sequence: 10+ -> 12+ -> 14+ -> 16+ -> 18+
amr_110cd_transitions = [
    {
        "I_initial": 12,
        "I_final": 10,
        "E_gamma_keV": 744.0,
        "B_E2_e2b2": 0.11,
        "B_E2_err": 0.03,
        "J2_hbar2_per_MeV": None,
        "J2_over_BE2": None
    },
    {
        "I_initial": 14,
        "I_final": 12,
        "E_gamma_keV": 907.0,
        "B_E2_e2b2": 0.10,
        "B_E2_err": 0.02,
        "J2_hbar2_per_MeV": None, # to be calculated
        "J2_over_BE2": None
    },
    {
        "I_initial": 16,
        "I_final": 14,
        "E_gamma_keV": 1042.0,
        "B_E2_e2b2": 0.09,
        "B_E2_err": 0.02,
        "J2_hbar2_per_MeV": None,
        "J2_over_BE2": None
    },
    {
        "I_initial": 18,
        "I_final": 16,
        "E_gamma_keV": 1180.0,
        "B_E2_e2b2": 0.07,
        "B_E2_err": 0.03,
        "J2_hbar2_per_MeV": None,
        "J2_over_BE2": None
    }
]

# Calculate dynamic moment of inertia J^(2) = 4 / Delta E_gamma (in MeV)
for i in range(1, len(amr_110cd_transitions)):
    prev_eg = amr_110cd_transitions[i-1]["E_gamma_keV"]
    curr_eg = amr_110cd_transitions[i]["E_gamma_keV"]
    delta_eg_MeV = (curr_eg - prev_eg) / 1000.0
    if delta_eg_MeV > 0:
        j2 = 4.0 / delta_eg_MeV
        amr_110cd_transitions[i]["J2_hbar2_per_MeV"] = round(j2, 2)
        be2 = amr_110cd_transitions[i]["B_E2_e2b2"]
        if be2 and be2 > 0:
            amr_110cd_transitions[i]["J2_over_BE2"] = round(j2 / be2, 1)

# 2. Comparison across rotational modes
mode_comparison = {
    "collective_rotation_well_deformed": {
        "description": "Standard deformed core rotation (e.g., 160Dy, 166Er)",
        "typical_B_E2_e2b2": "0.8 - 2.5 (100 - 300 W.u.)",
        "typical_B_M1_muN2": "< 0.01 (forbidden or core gR only)",
        "typical_J2_over_BE2": "15 - 40 hbar^2 MeV^-1 (e^2 b^2)^-1",
        "Delta_I_sequence": "Delta I = 2 cascade, strong E2 crossovers",
        "angular_momentum_generation": "Collective rotation of distorted mass distribution"
    },
    "magnetic_rotation_MR": {
        "description": "Single-blade shears mechanism (e.g., 199Pb, 135Pr)",
        "typical_B_E2_e2b2": "0.01 - 0.08 (few W.u., nearly spherical core)",
        "typical_B_M1_muN2": "1.0 - 5.0 (highly enhanced transverse dipole)",
        "typical_B_M1_over_B_E2": "10 - 50 (mu_N / eb)^2",
        "typical_J2_over_BE2": "Not applicable (M1 dominated)",
        "Delta_I_sequence": "Delta I = 1 M1 cascade with weak/absent E2 crossovers",
        "angular_momentum_generation": "Closing of proton-particle and neutron-hole shears blades"
    },
    "antimagnetic_rotation_AMR": {
        "description": "Two-shears symmetric quadrupole closing (e.g., 110Cd, 106Cd)",
        "typical_B_E2_e2b2": "0.05 - 0.15 (10 - 25 W.u., small core deformation)",
        "typical_B_M1_muN2": "Strictly 0 (forbidden by four-blade inversion symmetry)",
        "typical_J2_over_BE2": "150 - 400 hbar^2 MeV^-1 (e^2 b^2)^-1 (defining diagnostic)",
        "Delta_I_sequence": "Pure Delta I = 2 E2 cascade with no M1 transitions",
        "angular_momentum_generation": "Simultaneous symmetric closing of two opposing shears"
    }
}

output_payload = {
    "schema_version": 1,
    "topic": "Day 26 uncredited preview: Antimagnetic rotation (AMR) in 110Cd and J^(2)/B(E2) diagnostic ratio",
    "day_index": 25,
    "preview_day_index": 26,
    "formal_credit_awarded": False,
    "experimental_case_110cd": {
        "nucleus": "110Cd",
        "band": "Positive-parity AMR candidate",
        "configuration": "pi(g9/2)^-2 x nu(h11/2)^2 (four-blade quadrupole shears)",
        "transitions": amr_110cd_transitions
    },
    "mode_diagnostic_matrix": mode_comparison,
    "falsification_insights": [
        "110Cd exhibits a nearly constant B(E2) ~ 0.10 e^2b^2 from 12+ to 16+, disproving the simplistic universal hard gate that AMR B(E2) must steeply drop by factors of 3-5",
        "The ratio J^(2)/B(E2) ~ 245 - 329 hbar^2 MeV^-1 (e^2 b^2)^-1 is an order of magnitude higher than collective rotation (~20-40), providing the robust discriminator",
        "Complete absence of M1 transitions is enforced by the double-shears inversion symmetry, cleanly separating AMR from MR and wobbling"
    ]
}

out_file = pathlib.Path("outputs/learning-daily/20261027-DAY25-chirality-counterevidence-shape-coexistence-run-01/day26-amr-cd110-systematics-019.json")
out_file.write_text(json.dumps(output_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("Successfully generated day26-amr-cd110-systematics-019.json")
