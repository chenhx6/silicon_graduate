import json
import math

def compute_radium_octupole_patterns():
    # Butler 2020 Table I experimental E3 matrix elements and Q3 values
    # Trans: (Ii -> If)
    # 222Ra (rigid pear-shape candidate) and 228Ra (octupole vibrator candidate)
    data_222 = {
        "0+ -> 3-": {"me_eb32": 1.13, "me_unc": 0.09, "Q3_efm3": 3030, "Q3_unc": 240, "independent": True},
        "2+ -> 1-": {"me_eb32": 0.85, "me_unc": 0.24, "Q3_efm3": 2000, "Q3_unc": 600, "independent": True},
        "2+ -> 3-": {"me_eb32": -0.90, "me_unc": 0.50, "Q3_efm3": 2100, "Q3_unc": 1200, "independent": True},
        "2+ -> 5-": {"me_eb32": 1.79, "me_unc": 0.20, "Q3_efm3": 3100, "Q3_unc": 400, "independent": True},
        "4+ -> 1-": {"me_eb32": -2.10, "me_unc": 0.50, "Q3_efm3": 4400, "Q3_unc": 1000, "independent": False}
    }

    data_228 = {
        "0+ -> 3-": {"me_eb32": 0.87, "me_unc": 0.15, "Q3_efm3": 2300, "Q3_unc": 400, "independent": True},
        "2+ -> 1-": {"me_eb32": 1.36, "me_unc": 0.23, "Q3_efm3": 3200, "Q3_unc": 600, "independent": False},
        "2+ -> 3-": {"me_eb32": -0.06, "me_unc_pos": 0.23, "me_unc_neg": -0.16, "Q3_efm3": 150, "Q3_unc_pos": 360, "Q3_unc_neg": -500, "independent": False},
        "2+ -> 5-": {"me_eb32": 1.71, "me_unc": 0.23, "Q3_efm3": 3000, "Q3_unc": 400, "independent": False},
        "4+ -> 1-": {"me_eb32": 0.40, "me_unc_pos": 0.70, "me_unc_neg": -1.10, "Q3_efm3": -800, "Q3_unc_pos": 2300, "Q3_unc_neg": -1400, "independent": False}
    }

    # Clebsch-Gordan coefficients for K=0 rotor:
    # < I_i 0 3 0 | I_f 0 >
    cg = {
        "0+ -> 3-": 1.0,                                      # <0 0 3 0 | 3 0> = 1.0
        "2+ -> 1-": math.sqrt(2.0 / 5.0),                      # ~ 0.632456
        "2+ -> 3-": -math.sqrt(3.0 / 14.0),                    # ~ -0.462910 (phase convention)
        "2+ -> 5-": math.sqrt(15.0 / 35.0),                    # ~ 0.654654
        "4+ -> 1-": 0.0                                        # |4-1| > 3 forbidden by triangle rule
    }

    # Analysis of Q3 variance across independent transitions:
    q3_vals_222 = [v["Q3_efm3"] for k, v in data_222.items() if v["independent"]]
    mean_222 = sum(q3_vals_222) / len(q3_vals_222)
    std_222 = math.sqrt(sum((x - mean_222)**2 for x in q3_vals_222) / len(q3_vals_222))

    # 228Ra 2+ -> 3- suppression factor relative to 0+ -> 3-
    me_ratio_228 = abs(data_228["2+ -> 3-"]["me_eb32"]) / data_228["0+ -> 3-"]["me_eb32"]
    me_ratio_222 = abs(data_222["2+ -> 3-"]["me_eb32"]) / data_222["0+ -> 3-"]["me_eb32"]

    results = {
        "schema": "butler-radium-octupole-vibrator-model-056/v1",
        "222Ra": {
            "data": data_222,
            "mean_independent_Q3_efm3": round(mean_222, 1),
            "std_independent_Q3_efm3": round(std_222, 1),
            "relative_variation_pct": round(100.0 * std_222 / mean_222, 1),
            "ratio_2plus_to_3minus_over_0plus_to_3minus": round(me_ratio_222, 3),
            "nature": "Stable reflection-asymmetric pear shape; Q3 ~ 2600-3000 e fm^3 is nearly constant across all E3 branches."
        },
        "228Ra": {
            "data": data_228,
            "ratio_2plus_to_3minus_over_0plus_to_3minus": round(me_ratio_228, 3),
            "suppression_factor_228_vs_222": round(me_ratio_222 / me_ratio_228, 1) if me_ratio_228 > 0 else None,
            "nature": "Octupole vibrator; transition 2+ -> 3- is suppressed by more than a factor of 10 relative to 222Ra, consistent with destructive interference in harmonic octupole phonon coupling to quadrupole rotation."
        },
        "scientific_boundary": "In 144,146Ba, only a single direct E3 matrix element (0+ -> 3-) is experimentally available; higher couplings (2+ -> 5-, 4+ -> 7-) only have upper bounds. Therefore, the multi-transition Q3 flatness test that Butler 2020 used to establish rigid pear shape in 222Ra vs vibrator in 228Ra cannot yet be performed for 144,146Ba, reinforcing the necessity of relying on parity-displacement systematics delta E(I)."
    }

    out_path = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/butler-radium-octupole-vibrator-model-056.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("SUCCESS: wrote", out_path)

if __name__ == "__main__":
    compute_radium_octupole_patterns()
