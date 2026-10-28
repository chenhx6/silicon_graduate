

# Scientific claims from this historical calculation have been withdrawn.
import sys as _audit_sys
if "--replay-superseded" not in _audit_sys.argv:
    raise SystemExit("Superseded research artifact. Read knowledge/research-notes/day26-quantitative-claim-corrections.md; use 017-019 instead. Explicit historical replay requires --replay-superseded.")

import json
import math
import numpy as np

def run_shears_deformation_boundary_study():
    # Grid of beta2 from 0.02 to 0.45
    beta2_vals = np.linspace(0.02, 0.45, 25)

    # Regions to compare:
    # 1. A=198 (Pb region, Z=82)
    # 2. A=135 (Pr region, Z=59)
    # 3. A=110 (Cd region, Z=48)
    # 4. A=165 (Lu/Dy region, Z=71, well-deformed / TSD)
    regions = [
        {"name": "A=110 (Cd)", "A": 110, "Z": 48, "j_pi": 4.5, "j_nu": 5.5, "g_eff": 1.1},
        {"name": "A=135 (Pr)", "A": 135, "Z": 59, "j_pi": 5.5, "j_nu": 5.5, "g_eff": 1.0},
        {"name": "A=198 (Pb)", "A": 198, "Z": 82, "j_pi": 9.0, "j_nu": 6.5, "g_eff": 1.15},
        {"name": "A=165 (Lu)", "A": 165, "Z": 71, "j_pi": 5.5, "j_nu": 6.5, "g_eff": 0.9}
    ]

    results = {
        "title": "Deformation Upper Bound for the Shears Mechanism (beta2 <= 0.20)",
        "description": "Quantitative analysis of the collapse of B(M1)/B(E2) with increasing quadrupole deformation beta2",
        "regions": []
    }

    shears_angle_deg = 60.0 # mid-band shears angle
    theta_rad = math.radians(shears_angle_deg)

    for reg in regions:
        A = reg["A"]
        Z = reg["Z"]
        j_pi = reg["j_pi"]
        g_eff = reg["g_eff"]
        R0 = 1.2 * (A ** (1.0 / 3.0)) # fm

        reg_record = {
            "region": reg["name"],
            "A": A,
            "Z": Z,
            "points": []
        }

        # Shears B(M1) formula:
        # B(M1) = (3 / 8pi) * g_eff^2 * j_pi^2 * sin^2(theta / 2) (in mu_N^2)
        BM1_shear = (3.0 / (8.0 * math.pi)) * (g_eff ** 2) * (j_pi ** 2) * (math.sin(theta_rad / 2.0) ** 2)

        for b2 in beta2_vals:
            # Intrinsic quadrupole moment Q0 (in e b):
            # Q0 = (3 / sqrt(5pi)) * Z * e * R0^2 * beta2 * (1 + 0.36 * beta2) * 0.01 (fm^2 to b)
            Q0 = (3.0 / math.sqrt(5.0 * math.pi)) * Z * (R0 ** 2) * b2 * (1.0 + 0.36 * b2) * 0.01

            # Core collective B(E2):
            # B(E2; I -> I-2) = (15 / 128pi) * Q0^2 (in e^2 b^2)
            BE2_coll = (15.0 / (128.0 * math.pi)) * (Q0 ** 2)

            # Shears blade intrinsic quadrupole contribution:
            # Q_shear ~ 0.15 e b
            Q_shear = 0.15
            BE2_shear = (15.0 / (128.0 * math.pi)) * (Q_shear ** 2) * (math.sin(theta_rad) ** 2)

            # Total effective B(E2)
            BE2_total = BE2_coll + BE2_shear

            # Ratio B(M1) / B(E2) in (mu_N / e b)^2
            ratio = BM1_shear / BE2_total if BE2_total > 0 else 0.0

            # Regime classification:
            # ratio >= 15: Prominent MR (shears dominant)
            # 5 <= ratio < 15: Transitional shears
            # ratio < 5: Collective rotor dominant (shears quenched)
            if ratio >= 15.0:
                regime = "shears_dominant_MR"
            elif ratio >= 5.0:
                regime = "transitional_shears"
            else:
                regime = "collective_rotor_quenched"

            reg_record["points"].append({
                "beta2": round(float(b2), 3),
                "Q0_eb": round(float(Q0), 3),
                "BE2_coll_eb2": round(float(BE2_coll), 5),
                "BE2_total_eb2": round(float(BE2_total), 5),
                "BM1_shear_muN2": round(float(BM1_shear), 3),
                "ratio_BM1_BE2": round(float(ratio), 2),
                "regime": regime
            })

        results["regions"].append(reg_record)

    out_file = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/shears-deformation-boundary-theorem-009.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("SUCCESS: wrote", out_file)

if __name__ == "__main__":
    run_shears_deformation_boundary_study()
