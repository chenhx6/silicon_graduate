# Quantitative Analysis of Multipole Mixing Ratio Evolution in 133Ce Band 4
# Derived from Wakudyanaye 2022 Table 5.2 and Table 6.11
import json

ce133_data = {
    "624.6": {"Ji": 6.5, "Jf": 5.5, "delta": -1.5, "delta_err_plus": 0.97, "delta_err_minus": -5.7, "Egamma": 0.625},
    "582.7": {"Ji": 8.5, "Jf": 7.5, "delta": -0.55, "delta_err_plus": 0.12, "delta_err_minus": -0.25, "Egamma": 0.582},
    "464.4": {"Ji": 9.5, "Jf": 8.5, "delta": -0.17, "delta_err_plus": 0.09, "delta_err_minus": -0.20, "Egamma": 0.465}
}

results = {
    "title": "133Ce Band 4 interband transition multipole mixing ratio and photon fraction evolution",
    "transitions": {}
}

for line, d in ce133_data.items():
    delta = d["delta"]
    d2 = delta ** 2
    f_E2 = d2 / (1.0 + d2)
    f_M1 = 1.0 / (1.0 + d2)
    overestimate_factor = 1.0 + d2

    delta_up = delta + d["delta_err_plus"]
    d2_up = delta_up ** 2
    f_M1_up = 1.0 / (1.0 + d2_up)

    delta_low = delta + d["delta_err_minus"]
    d2_low = delta_low ** 2
    f_M1_low = 1.0 / (1.0 + d2_low)

    results["transitions"][line] = {
        "Ji": d["Ji"],
        "Jf": d["Jf"],
        "Egamma_MeV": d["Egamma"],
        "delta_central": delta,
        "delta_squared": round(d2, 5),
        "f_E2_percent": round(f_E2 * 100, 3),
        "f_M1_percent": round(f_M1 * 100, 3),
        "f_M1_interval_percent": [round(min(f_M1_up, f_M1_low) * 100, 3), round(max(f_M1_up, f_M1_low) * 100, 3)],
        "naive_delta_zero_overestimate_percent": round(d2 * 100, 3),
        "correction_factor_1_over_1_plus_d2": round(f_M1, 5)
    }

out_path = "outputs/learning-daily/20261027-DAY25-chirality-counterevidence-shape-coexistence-run-01/ce133-mixing-ratio-evolution-015.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"Successfully generated {out_path}")
