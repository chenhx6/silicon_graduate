

# Scientific claims from this historical calculation have been withdrawn.
import sys as _audit_sys
if "--replay-superseded" not in _audit_sys.argv:
    raise SystemExit("Superseded research artifact. Read knowledge/research-notes/day26-quantitative-claim-corrections.md; use 017-019 instead. Explicit historical replay requires --replay-superseded.")

import json
import math

def run_dipole_cancellation_model():
    # Parameters for Barium isotopes (Z=56)
    # N ranges from 84 to 92 (A = 140 to 148)
    ba_data = [
        {"A": 140, "N": 84, "beta2": 0.12, "beta3": 0.00, "v2_h9_2": 0.10, "v2_f7_2": 0.05, "v2_i13_2": 0.01, "exp_D0": 0.00},
        {"A": 142, "N": 86, "beta2": 0.16, "beta3": 0.05, "v2_h9_2": 0.20, "v2_f7_2": 0.10, "v2_i13_2": 0.01, "exp_D0": 0.05},
        {"A": 144, "N": 88, "beta2": 0.20, "beta3": 0.11, "v2_h9_2": 0.32, "v2_f7_2": 0.17, "v2_i13_2": 0.02, "exp_D0": 0.13, "exp_BE3_Wu": 48.0},
        {"A": 146, "N": 90, "beta2": 0.22, "beta3": 0.12, "v2_h9_2": 0.44, "v2_f7_2": 0.24, "v2_i13_2": 0.03, "exp_D0": 0.015, "exp_BE3_Wu": 48.0},
        {"A": 148, "N": 92, "beta2": 0.24, "beta3": 0.10, "v2_h9_2": 0.56, "v2_f7_2": 0.32, "v2_i13_2": 0.04, "exp_D0": -0.06}
    ]

    # Droplet model macroscopic dipole moment formula:
    # D_macro = C_LD * Z * e * A^(-1/3) * beta2 * beta3
    # C_LD ~ 0.0006 - 0.0008 e fm
    C_LD = 0.00075

    # Microscopic shell dipole matrix elements:
    # Proton contribution (almost constant across Ba isotopes since Z=56 fixed):
    # d_p ~ +0.35 e fm
    d_p = 0.35

    # Neutron single-particle dipole contribution per occupied nucleon in active Nilsson orbitals:
    # Low-Omega orbitals from h9/2, f7/2, i13/2 have strong negative dipole matrix element:
    # d_n_active ~ -0.42 e fm
    d_n_active = -0.44

    results = {
        "title": "Microscopic Dipole Moment Cancellation Mechanism in Neutron-Rich Ba Isotopes",
        "description": "Cross-checking macroscopic droplet vs microscopic single-particle shell contributions to D0 across 140-148Ba",
        "isotopes": []
    }

    for item in ba_data:
        A = item["A"]
        N = item["N"]
        b2 = item["beta2"]
        b3 = item["beta3"]

        # 1. Macroscopic droplet component
        D_macro = C_LD * 56.0 * (A ** (-1.0 / 3.0)) * b2 * b3 * 10.0 # e fm

        # 2. Microscopic proton shell contribution (scaled with beta3)
        D_shell_p = d_p * (b3 / 0.11) if b3 > 0.001 else 0.0

        # 3. Microscopic neutron shell contribution:
        # Sum over active neutron orbital occupations
        # Effective active neutron count ~ (v2_h9_2 + v2_f7_2 + v2_i13_2) * (2j+1 weighting factor)
        n_active_weighted = (item["v2_h9_2"] * 10.0 + item["v2_f7_2"] * 8.0 + item["v2_i13_2"] * 14.0) / 10.0
        D_shell_n = d_n_active * n_active_weighted * (b3 / 0.11) if b3 > 0.001 else 0.0

        # Total shell correction
        D_shell = D_shell_p + D_shell_n

        # Total intrinsic dipole moment
        D_total = D_macro + D_shell

        # Intrinsic octupole moment: Q30 = (3 / sqrt(7*pi)) * Z * e * R0^3 * beta3
        R0 = 1.2 * (A ** (1.0 / 3.0))
        Q30 = (3.0 / math.sqrt(7.0 * math.pi)) * 56.0 * (R0 ** 3) * b3 * 0.01 # e b^(3/2)

        # Laboratory B(E1) and B(E3) for ground state 0+ -> 1- and 0+ -> 3-
        # B(E1; 0+ -> 1-) = (3 / 4pi) * D0^2
        BE1 = (3.0 / (4.0 * math.pi)) * (D_total ** 2) * 1e-4 # e^2 b
        # B(E3; 0+ -> 3-) = (7 / 16pi) * Q30^2
        BE3 = (7.0 / (16.0 * math.pi)) * (Q30 ** 2) # e^2 b^3

        # Weisskopf units for E1 and E3
        # B_W(E1) = 0.0645 * A^(2/3) e^2 fm^2 = 0.0645 * A^(2/3) * 1e-4 e^2 b
        # B_W(E3) = 0.0594 * A^2 e^2 fm^6 = 0.0594 * A^2 * 1e-6 e^2 b^3
        BW_E1 = 0.0645 * (A ** (2.0 / 3.0)) * 1e-4
        BW_E3 = 0.0594 * (A ** 2.0) * 1e-6

        BE1_Wu = BE1 / BW_E1 if BW_E1 > 0 else 0.0
        BE3_Wu = BE3 / BW_E3 if BW_E3 > 0 else 0.0

        results["isotopes"].append({
            "nucleus": f"{A}Ba",
            "A": A,
            "N": N,
            "beta2": b2,
            "beta3": b3,
            "D_macro_efm": round(float(D_macro), 4),
            "D_shell_p_efm": round(float(D_shell_p), 4),
            "D_shell_n_efm": round(float(D_shell_n), 4),
            "D_shell_total_efm": round(float(D_shell), 4),
            "D_total_efm": round(float(D_total), 4),
            "exp_D0_efm": item.get("exp_D0"),
            "BE1_Wu": round(float(BE1_Wu), 6),
            "BE3_Wu": round(float(BE3_Wu), 1),
            "ratio_BE1_BE3": round(float(BE1_Wu / BE3_Wu), 8) if BE3_Wu > 0 else 0.0
        })

    out_file = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/ba-dipole-cancellation-mechanism-007.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("SUCCESS: wrote", out_file)

if __name__ == "__main__":
    run_dipole_cancellation_model()
