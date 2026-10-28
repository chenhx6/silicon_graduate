
import json
import math

def calculate_parity_displacement():
    # Experimental level energies (in keV)
    nuclei_data = {
        "224Ra": {
            "name": "224Ra (A=224, Z=88, N=136)",
            "classification": "Rigid reflection-asymmetric rotor",
            "pos_parity": {0: 0.0, 2: 84.4, 4: 250.8, 6: 479.3, 8: 761.3, 10: 1089.0},
            "neg_parity": {1: 216.0, 3: 290.3, 5: 433.3, 7: 640.7, 9: 906.0}
        },
        "220Rn": {
            "name": "220Rn (A=220, Z=86, N=134)",
            "classification": "Octupole vibrational / transitional",
            "pos_parity": {0: 0.0, 2: 241.0, 4: 533.7, 6: 872.8, 8: 1240.2, 10: 1630.0},
            "neg_parity": {1: 536.0, 3: 645.0, 5: 860.0, 7: 1177.0, 9: 1587.0}
        },
        "144Ba": {
            "name": "144Ba (A=144, Z=56, N=88)",
            "classification": "Large-amplitude octupole-soft / beta3-tunneling",
            "pos_parity": {0: 0.0, 2: 199.3, 4: 530.6, 6: 959.0, 8: 1468.2, 10: 2038.0},
            "neg_parity": {1: 759.0, 3: 838.2, 5: 1134.4, 7: 1584.0, 9: 2153.0}
        },
        "146Ba": {
            "name": "146Ba (A=146, Z=56, N=90)",
            "classification": "Large-amplitude octupole-soft (dipole canceled)",
            "pos_parity": {0: 0.0, 2: 181.0, 4: 513.5, 6: 953.5, 8: 1483.5, 10: 2080.0},
            "neg_parity": {1: 737.5, 3: 821.0, 5: 1118.0, 7: 1560.0, 9: 2115.0}
        }
    }

    results = {
        "title": "Systematic Analysis of Parity Displacement Function delta_E(I) across Reflection-Asymmetric Candidates",
        "formula": "delta_E(I) = E(I-) - 0.5 * [E((I-1)+) + E((I+1)+)]",
        "interpretation": "delta_E -> 0 indicates rigid octupole deformation; persistent large delta_E (> 150 keV) indicates soft octupole vibration / tunneling barrier",
        "comparisons": {}
    }

    for nuc, d in nuclei_data.items():
        eval_record = {
            "name": d["name"],
            "classification": d["classification"],
            "delta_E_series": []
        }
        pos = d["pos_parity"]
        neg = d["neg_parity"]

        for spin_neg, E_neg in sorted(neg.items()):
            spin_low = spin_neg - 1
            spin_high = spin_neg + 1
            if spin_low in pos and spin_high in pos:
                E_interpolated = 0.5 * (pos[spin_low] + pos[spin_high])
                delta_E = E_neg - E_interpolated

                # Percentage reduction relative to I=1-
                eval_record["delta_E_series"].append({
                    "spin": spin_neg,
                    "E_neg_keV": E_neg,
                    "E_interpolated_pos_keV": round(float(E_interpolated), 2),
                    "delta_E_keV": round(float(delta_E), 2)
                })

        # Calculate reduction factor from I=1- to I=7-
        dE_1 = eval_record["delta_E_series"][0]["delta_E_keV"]
        dE_7 = eval_record["delta_E_series"][3]["delta_E_keV"]
        collapse_pct = (dE_1 - dE_7) / dE_1 * 100.0
        eval_record["collapse_1_to_7_percent"] = round(float(collapse_pct), 1)
        eval_record["residual_dE_7_keV"] = dE_7

        results["comparisons"][nuc] = eval_record

    out_file = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/parity-displacement-deltaE-systematics-010.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("SUCCESS: wrote", out_file)

if __name__ == "__main__":
    calculate_parity_displacement()
