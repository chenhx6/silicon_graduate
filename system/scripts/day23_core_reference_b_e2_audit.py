#!/usr/bin/env python3
"""Audit 186Pt core reference B(E2) across published evaluations and PRM calibrations."""
import argparse
import json
import math
from pathlib import Path


def weisskopf_e2_eb2(mass_a: float) -> float:
    return 5.940e-6 * (mass_a ** (4.0 / 3.0))


def be2_from_half_life(energy_mev: float, t_half_ps: float, total_conv_coeff: float) -> float:
    tau_ps = t_half_ps / math.log(2.0)
    tau_gamma_ps = tau_ps * (1.0 + total_conv_coeff)
    return 0.0816 / ((energy_mev ** 5) * tau_gamma_ps)


def audit():
    bw_186 = weisskopf_e2_eb2(186.0)
    bw_187 = weisskopf_e2_eb2(187.0)
    pt186_e = 0.19153
    pt186_thalf = 240.0
    pt186_thalf_unc = 20.0
    pt186_alpha = 0.417
    pt186_be2_down = be2_from_half_life(pt186_e, pt186_thalf, pt186_alpha)
    pt186_be2_wu = pt186_be2_down / bw_186
    pt186_be2_down_lo = be2_from_half_life(pt186_e, pt186_thalf + pt186_thalf_unc, pt186_alpha)
    pt186_be2_down_hi = be2_from_half_life(pt186_e, pt186_thalf - pt186_thalf_unc, pt186_alpha)
    au187_e = 0.2334
    au187_thalf = 56.0
    au187_thalf_unc = 5.0
    au187_alpha = 0.224
    au187_be2_down = be2_from_half_life(au187_e, au187_thalf, au187_alpha)
    au187_be2_wu = au187_be2_down / bw_187
    s20_letter_pt186 = 0.84
    se21_thesis_pt186 = 1.44
    s20_letter_au187 = 1.49
    guo22_range_wu = [100.0, 200.0]
    guo22_range_eb2_186 = [100.0 * bw_186, 200.0 * bw_186]
    guo22_range_eb2_187 = [100.0 * bw_187, 200.0 * bw_187]
    controls = {
        "IAEA_adopted_102_wu_matches_half_life": abs(pt186_be2_wu - 102.3) < 1.0,
        "IAEA_adopted_188_wu_matches_half_life": abs(au187_be2_wu - 187.6) < 1.0,
        "Guo_100_200_wu_bracket_both_evaluated_values": (
            guo22_range_wu[0] <= pt186_be2_wu <= guo22_range_wu[1] and
            guo22_range_wu[0] <= au187_be2_wu <= guo22_range_wu[1]
        ),
        "thesis_144_is_1p71x_letter_084": abs((se21_thesis_pt186 / s20_letter_pt186) - 1.7142857) < 1e-5,
        "neither_084_nor_144_equals_evaluated_0645": (
            abs(s20_letter_pt186 - pt186_be2_down) > 0.15 and
            abs(se21_thesis_pt186 - pt186_be2_down) > 0.7
        ),
        "letter_084_is_133_wu": abs((s20_letter_pt186 / bw_186) - 133.19) < 0.1,
        "thesis_144_is_228_wu": abs((se21_thesis_pt186 / bw_186) - 228.33) < 0.1,
    }
    return {
        "scope": "Cross-audit of 186Pt core and 187Au reference B(E2) between Sensharma 2020 PRL, Sensharma 2021 thesis, Guo 2022 PLB, and IAEA 2022/2026 evaluated datasets.",
        "sources": [
            "knowledge/sources/sensharma-2020-longitudinal-wobbling-187au.md",
            "knowledge/sources/sensharma-2021-wobbling-motion-135pr-187au.md",
            "knowledge/sources/guo-2022-low-spin-wobbling-187au.md"
        ],
        "locators": ["AU20-D23-1", "SE21-D23-3", "GU22-D23-006"],
        "constants": {
            "B_W_E2_A186_eb2": bw_186,
            "B_W_E2_A187_eb2": bw_187
        },
        "pt186_evaluated": {
            "energy_keV": 191.53,
            "T_half_ps": pt186_thalf,
            "T_half_unc_ps": pt186_thalf_unc,
            "alpha_tot": pt186_alpha,
            "calculated_B_E2_down_eb2": pt186_be2_down,
            "calculated_B_E2_down_range_eb2": [pt186_be2_down_lo, pt186_be2_down_hi],
            "calculated_B_E2_Wu": pt186_be2_wu,
            "IAEA_table_b_e2_Wu": 102.0
        },
        "au187_evaluated": {
            "energy_keV": 233.4,
            "T_half_ps": au187_thalf,
            "T_half_unc_ps": au187_thalf_unc,
            "alpha_tot": au187_alpha,
            "calculated_B_E2_down_eb2": au187_be2_down,
            "calculated_B_E2_Wu": au187_be2_wu,
            "IAEA_table_b_e2_Wu": 188.0
        },
        "quoted_calibrations": {
            "Sensharma_2020_PRL_pt186_eb2": s20_letter_pt186,
            "Sensharma_2020_PRL_pt186_Wu": s20_letter_pt186 / bw_186,
            "Sensharma_2021_thesis_pt186_eb2": se21_thesis_pt186,
            "Sensharma_2021_thesis_pt186_Wu": se21_thesis_pt186 / bw_186,
            "Sensharma_2020_PRL_au187_eb2": s20_letter_au187,
            "Sensharma_2021_thesis_au187_parity_typo": "13/2+ -> 9/2+",
            "Guo_2022_PLB_quoted_bracket_Wu": guo22_range_wu,
            "Guo_2022_PLB_bracket_for_186Pt_eb2": guo22_range_eb2_186,
            "Guo_2022_PLB_bracket_for_187Au_eb2": guo22_range_eb2_187
        },
        "controls": controls,
        "all_controls_pass": all(controls.values()),
        "conclusions": [
            "Guo 2022 100-200 W.u. statement encompasses evaluated values for both 186Pt (102 W.u.) and 187Au (188 W.u.).",
            "Sensharma 2020 PRL quotes 0.84 eb2 (~133 W.u.) while 2021 thesis quotes 1.44 eb2 (~228 W.u.) for the same Baglin 2003 citation.",
            "Neither 0.84 nor 1.44 eb2 matches the ENSDF-adopted 0.645 eb2 (102 W.u.) from T1/2 = 240(20) ps without unstated adjustments.",
            "Thesis printed 128 contains a confirmed positive-parity typo (13/2+ -> 9/2+) for the h9/2 transition.",
            "Model deformation choice beta=0.23 in Sensharma PRM relies on core calibration references that differ by 1.71x across author publications."
        ]
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    res = audit()
    args.output.write_text(json.dumps(res, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"all_controls_pass": res["all_controls_pass"], "controls": res["controls"]}, indent=2))
    return 0 if res["all_controls_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
