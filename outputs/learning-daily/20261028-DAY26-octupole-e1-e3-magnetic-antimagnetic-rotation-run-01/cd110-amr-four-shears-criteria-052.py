import json
import math

def compute_cd110_amr():
    # 110Cd Band B experimental transitions from Roy 2011 and NNDC ENSDF adopted dataset 110048001
    # 1 W.u. for E2 in A=110:
    # B_W(E2) = 5.940e-2 * A^(4/3) e^2 fm^4 = 5.940e-2 * (110^(4/3)) * 1e-4 e^2 b^2
    A = 110
    BW_E2_eb2 = 5.940e-2 * (A ** (4.0 / 3.0)) * 1e-4 # ~ 0.003133 e^2 b^2

    transitions = [
        {"Ji": 12, "Jf": 10, "E_gamma_keV": 561.0, "BE2_Wu": 40.0, "BE2_Wu_unc": 1.5, "origin": "Piiparinen 1993 RDDS"},
        {"Ji": 14, "Jf": 12, "E_gamma_keV": 854.3, "BE2_Wu": 29.0, "BE2_Wu_unc": 3.0, "origin": "Piiparinen 1993 RDDS"},
        {"Ji": 16, "Jf": 14, "E_gamma_keV": 1074.6, "BE2_Wu": 50.0, "BE2_Wu_unc": 5.0, "origin": "Roy 2011 DSAM"},
        {"Ji": 18, "Jf": 16, "E_gamma_keV": 1224.5, "BE2_Wu": 41.0, "BE2_Wu_unc": 6.0, "origin": "Roy 2011 DSAM"},
        {"Ji": 20, "Jf": 18, "E_gamma_keV": 1323.0, "BE2_Wu": 38.0, "BE2_Wu_unc": 7.0, "origin": "Roy 2011 DSAM"},
        {"Ji": 22, "Jf": 20, "E_gamma_keV": 1314.1, "BE2_Wu": 22.0, "BE2_Wu_unc": 8.0, "origin": "Roy 2011 DSAM (1314 gate)"}
    ]

    results = {
        "schema": "cd110-amr-four-shears-criteria-052/v1",
        "description": "Double-shears symmetry, B(E2) plateau and J(2)/B(E2) ratio in 110Cd antimagnetic rotation",
        "BW_E2_eb2": BW_E2_eb2,
        "transitions": [],
        "amr_criteria_evaluation": {}
    }

    for i, t in enumerate(transitions):
        be2_eb2 = t["BE2_Wu"] * BW_E2_eb2
        be2_eb2_unc = t["BE2_Wu_unc"] * BW_E2_eb2

        # Dynamic moment of inertia: J(2) = 4 / Delta E_gamma
        if i > 0:
            delta_egamma_MeV = (t["E_gamma_keV"] - transitions[i-1]["E_gamma_keV"]) * 1e-3
            if delta_egamma_MeV > 0:
                j2_hbar2_MeV = 4.0 / delta_egamma_MeV
                j2_over_be2 = j2_hbar2_MeV / be2_eb2
            else:
                j2_hbar2_MeV = None
                j2_over_be2 = None
        else:
            delta_egamma_MeV = None
            j2_hbar2_MeV = None
            j2_over_be2 = None

        item = {
            "cascade": f"{t['Ji']}+ -> {t['Jf']}+",
            "E_gamma_keV": t["E_gamma_keV"],
            "BE2_Wu": t["BE2_Wu"],
            "BE2_Wu_unc": t["BE2_Wu_unc"],
            "BE2_eb2": round(be2_eb2, 4),
            "BE2_eb2_unc": round(be2_eb2_unc, 4),
            "Delta_Egamma_MeV": round(delta_egamma_MeV, 4) if delta_egamma_MeV is not None else None,
            "J2_hbar2_MeV": round(j2_hbar2_MeV, 2) if j2_hbar2_MeV is not None else None,
            "J2_over_BE2_ratio": round(j2_over_be2, 1) if j2_over_be2 is not None else None,
            "origin": t["origin"]
        }
        results["transitions"].append(item)

    results["amr_criteria_evaluation"] = {
        "symmetry_principle": "R_y(pi)*T discrete symmetry cancels the transverse magnetic dipole moments identically (mu_perp == 0), strictly forbidding Delta I = 1 M1 transitions.",
        "be2_plateau": "From 12+ to 20+, B(E2) remains nearly constant at 0.09-0.16 e^2b^2 (29-50 W.u.), falling to 0.069 e^2b^2 at 22+, because semi-rigid core rotation (Im_core ~ 19.5 hbar^2/MeV) slows the shears closing.",
        "j2_over_be2_range": "116.0 to 341.3 hbar^2 MeV^-1 (e^2b^2)^-1",
        "comparison_with_collective_rotor": "Normal deformed collective rotation has J(2)/B(E2) ~ 15-40. AMR exceeds this by a factor of 4 to 10.",
        "high_spin_22plus_branch_controversy": "NNDC ENSDF adopted lists a 1100 keV transition with RI=37 and B(E2)=20(10) W.u. from 22+, but Roy 2011 coincidence gates failed to confirm this branch. Roy Table 1 is adopted with B(E2) = 0.06(2) (eb)^2 based on the clean 1314 keV gate."
    }

    out_path = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/cd110-amr-four-shears-criteria-052.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("SUCCESS: wrote", out_path)

if __name__ == "__main__":
    compute_cd110_amr()
