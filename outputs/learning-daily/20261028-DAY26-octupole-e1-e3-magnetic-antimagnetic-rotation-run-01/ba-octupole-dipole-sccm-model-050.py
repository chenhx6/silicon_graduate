import json
import math

def compute_ba_octupole_dipole():
    isotopes = {
        "144Ba": {
            "A": 144, "Z": 56, "N": 88,
            "M_E3_eb32": 0.65, "M_E3_unc_pos": 0.17, "M_E3_unc_neg": -0.23,
            "BE3_Wu": 48.0, "BE3_Wu_unc_pos": 25.0, "BE3_Wu_unc_neg": -34.0,
            "exp_D0_efm": 0.13,
            "sccm_D0_efm": 0.14,
            "v2_nu_h9_2": 0.32, "v2_nu_f7_2": 0.17, "v2_nu_i13_2": 0.02
        },
        "146Ba": {
            "A": 146, "Z": 56, "N": 90,
            "M_E3_eb32": 0.65, "M_E3_unc_pos": 0.14, "M_E3_unc_neg": -0.20,
            "BE3_Wu": 48.0, "BE3_Wu_unc_pos": 21.0, "BE3_Wu_unc_neg": -29.0,
            "exp_E1_amp_eb12": 0.000223, "exp_E1_unc_pos": 0.000010, "exp_E1_unc_neg": -0.000008,
            "sccm_E1_amp_eb12": 0.00474,
            "exp_D0_efm_upper": 0.01,
            "sccm_D0_efm": 0.02,
            "v2_nu_h9_2": 0.40, "v2_nu_f7_2": 0.27, "v2_nu_i13_2": 0.20
        }
    }

    results = {
        "schema": "ba-octupole-dipole-sccm-model-050/v1",
        "description": "Microscopic audit of dipole cancellation and E3 collectivity in 144,146Ba",
        "e3_analysis": {},
        "e1_cancellation_analysis": {},
        "static_vs_dynamic_boundary": {}
    }

    for name, data in isotopes.items():
        A = data["A"]
        M = data["M_E3_eb32"]

        BW_E1 = 0.06446 * (A ** (2.0 / 3.0))
        BW_E3_fm6 = 0.05940 * (A ** 2.0)
        BW_E3_eb3 = BW_E3_fm6 * 1e-6

        B_up_eb3 = M ** 2
        B_down_eb3 = B_up_eb3 / 7.0
        B_down_Wu = B_down_eb3 / BW_E3_eb3

        results["e3_analysis"][name] = {
            "BW_E3_fm6": BW_E3_fm6,
            "BW_E3_eb3": BW_E3_eb3,
            "B_down_eb3": B_down_eb3,
            "B_down_Wu_derived": round(B_down_Wu, 2),
            "BE3_Wu_reported": data["BE3_Wu"],
            "BE3_Wu_confidence_interval": [
                data["BE3_Wu"] + data["BE3_Wu_unc_neg"],
                data["BE3_Wu"] + data["BE3_Wu_unc_pos"]
            ]
        }

    ci_144 = results["e3_analysis"]["144Ba"]["BE3_Wu_confidence_interval"]
    ci_146 = results["e3_analysis"]["146Ba"]["BE3_Wu_confidence_interval"]
    overlap_min = max(ci_144[0], ci_146[0])
    overlap_max = min(ci_144[1], ci_146[1])

    results["e3_analysis"]["overlap"] = {
        "ci_144Ba": ci_144,
        "ci_146Ba": ci_146,
        "overlap_range": [overlap_min, overlap_max],
        "overlap_ratio": (overlap_max - overlap_min) / (ci_146[1] - ci_146[0])
    }

    e1_exp = isotopes["146Ba"]["exp_E1_amp_eb12"]
    e1_sccm = isotopes["146Ba"]["sccm_E1_amp_eb12"]
    amp_ratio = e1_sccm / e1_exp
    strength_ratio = amp_ratio ** 2

    results["e1_cancellation_analysis"] = {
        "146Ba_E1_exp_amp_eb12": e1_exp,
        "146Ba_E1_sccm_amp_eb12": e1_sccm,
        "amplitude_ratio_sccm_over_exp": round(amp_ratio, 2),
        "strength_ratio_BE1_sccm_over_exp": round(strength_ratio, 1),
        "dipole_operator": "D_z = e (N/A sum_p z_p - Z/A sum_n z_n) = e (NZ/A) (R_{p,z} - R_{n,z})",
        "proton_driving_orbitals": "pi(1h11/2) <-> pi(2d5/2) with Delta l = Delta j = 3 (positive dipole ~ +0.35 e fm)",
        "neutron_driving_orbitals": "nu(1h9/2, 2f7/2, 1i13/2) with Delta l = Delta j = 3 (negative dipole ~ -0.21 to -0.35 e fm)",
        "net_cancellation_mechanism": "At N=90 (146Ba), occupation of intruder nu 1i13/2 (v2=0.20) and low-Omega nu 1h9/2 (v2=0.40), 2f7/2 (v2=0.27) increases negative neutron polarization to match proton polarization, collapsing D0 from 0.13 e fm in 144Ba to < 0.01 e fm in 146Ba."
    }

    results["static_vs_dynamic_boundary"] = {
        "good_parity_condition": "<0+| Q3 |0+> == 0 identically for all laboratory parity eigenstates; transition matrix elements <0+||M(E3)||3-> do not directly measure intrinsic expectation values.",
        "gogny_d1s_pes": "Bernard 2016 unprojected potential energy surface is extremely flat along beta3 (< 0.5 MeV barrier); ground state wave packet F(beta2, beta3) has broad zero-point octupole spread.",
        "parity_displacement": "Energy displacement delta E(I) = E(I-) - 0.5[E((I+1)+) + E((I-1)+)] in 144,146Ba is 600-800 keV at low spin, demonstrating octupole vibrational softness rather than rigid pear shape (< 50 keV in 224Ra)."
    }

    out_path = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/ba-octupole-dipole-sccm-model-050.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("SUCCESS: wrote", out_path)

if __name__ == "__main__":
    compute_ba_octupole_dipole()
