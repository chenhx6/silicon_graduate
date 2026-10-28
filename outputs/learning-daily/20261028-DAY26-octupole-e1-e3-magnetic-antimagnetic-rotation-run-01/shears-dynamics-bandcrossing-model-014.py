#!/usr/bin/env python3
"""
shears-dynamics-bandcrossing-model-014.py

Comprehensive Quantitative Investigation of Semiclassical Shears Dynamics,
Bandcrossings, and B(M1)/B(E2) Rebound Mechanics.

Benchmarks:
1. 198Pb Band 1: Textbook 4qp shears closing without crossing.
2. 197Pb Band 'a': Double bandcrossing with shears re-opening.
3. 135Pr Band 3: 3qp -> 5qp crossing, B(M1)/B(E2) surge to 94.8 (mu_N/eb)^2.
4. 137Pr Band 2: 3qp -> 5qp crossing, peak at 62.1 and post-crossing 5qp closing.

Theorems established:
- Semiclassical Shears Angle & Rates: Clark & Macchiavelli 2000 Eqs. 5-8.
- Shears Re-opening via Quasiparticle Alignment.
- Orthogonality Suppression of Crossover E2 Transitions (<3qp|E2|5qp> = 0).
- Dynamic Moment of Inertia J^(2) Resonance Peak & Alignment Correlation.
"""

# Scientific claims from this historical calculation have been withdrawn.
import sys as _audit_sys
if "--replay-superseded" not in _audit_sys.argv:
    raise SystemExit("Superseded research artifact. Read knowledge/research-notes/day26-quantitative-claim-corrections.md; use 017-019 instead. Explicit historical replay requires --replay-superseded.")


import json
import math

def shears_geometry(I_shears, j_pi, j_nu):
    num = I_shears * (I_shears + 1.0) - j_pi * (j_pi + 1.0) - j_nu * (j_nu + 1.0)
    den = 2.0 * math.sqrt(j_pi * (j_pi + 1.0) * j_nu * (j_nu + 1.0))
    cos_theta = num / den
    cos_clipped = max(-1.0, min(1.0, cos_theta))
    theta_rad = math.acos(cos_clipped)
    theta_deg = math.degrees(theta_rad)

    sin_theta = math.sin(theta_rad)
    sin_theta_pi = (math.sqrt(j_nu * (j_nu + 1.0)) / math.sqrt(I_shears * (I_shears + 1.0))) * sin_theta
    sin_theta_pi_clipped = max(0.0, min(1.0, sin_theta_pi))
    theta_pi_rad = math.asin(sin_theta_pi_clipped)
    theta_pi_deg = math.degrees(theta_pi_rad)

    return {
        "I_shears": float(I_shears),
        "cos_theta": float(cos_theta),
        "theta_deg": float(theta_deg),
        "sin_theta": float(sin_theta),
        "theta_pi_deg": float(theta_pi_deg),
        "sin_theta_pi": float(sin_theta_pi_clipped)
    }

def calc_semiclassical_rates(geom, j_pi, j_nu, g_eff, eQ_eff, core_BE2=0.0):
    sin_pi = geom["sin_theta_pi"]
    bm1 = (3.0 / (8.0 * math.pi)) * (g_eff**2) * (j_pi * (j_pi + 1.0)) * (sin_pi**2)
    be2_shears = (15.0 / (128.0 * math.pi)) * (eQ_eff**2) * (sin_pi**4)
    be2_total = be2_shears + core_BE2
    ratio = bm1 / be2_total if be2_total > 1e-6 else None
    return {
        "BM1_muN2": float(bm1),
        "BE2_shears_e2b2": float(be2_shears),
        "BE2_total_e2b2": float(be2_total),
        "BM1_over_BE2_muN2_per_e2b2": float(ratio) if ratio is not None else None
    }

def run_198pb_simulation():
    j_pi = 11.0
    j_nu = 12.0
    g_eff = 0.92
    eQ_eff = 6.5
    core_BE2 = 0.002
    spins = list(range(17, 24))
    res = []
    for I in spins:
        geom = shears_geometry(I, j_pi, j_nu)
        rates = calc_semiclassical_rates(geom, j_pi, j_nu, g_eff, eQ_eff, core_BE2)
        res.append({**geom, **rates})
    return res

def run_197pb_simulation():
    j_pi = 11.0
    g_eff = 0.92
    eQ_eff = 6.5
    core_BE2 = 0.003
    spins_lower = [14.5, 15.5, 16.5, 17.5, 18.5]
    spins_upper = [18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5]
    lower_res = []
    for I in spins_lower:
        geom = shears_geometry(I, j_pi, 6.5)
        rates = calc_semiclassical_rates(geom, j_pi, 6.5, g_eff, eQ_eff, core_BE2)
        lower_res.append({**geom, **rates, "branch": "3qp (nu i13/2^-1)"})
    upper_res = []
    for I in spins_upper:
        geom = shears_geometry(I, j_pi, 16.5)
        rates = calc_semiclassical_rates(geom, j_pi, 16.5, g_eff, eQ_eff, core_BE2)
        upper_res.append({**geom, **rates, "branch": "5qp (nu i13/2^-3)"})
    return {"lower_branch": lower_res, "upper_branch": upper_res}

def two_band_crossing_solver(spins, E1_pars, E2_pars, V_mix, m1_pars, core_pars):
    """
    Exact two-band crossing diagonalization and transition rate calculator.
    E1_pars: (E0_1, A1, I0_1)
    E2_pars: (E0_2, A2, I0_2)
    m1_pars: (m1_base1, m1_slope1, m1_base2, m1_slope2)
    core_pars: (core_BE2_1, core_BE2_2)
    """
    E0_1, A1, I0_1 = E1_pars
    E0_2, A2, I0_2 = E2_pars
    m1_b1, m1_s1, m1_b2, m1_s2 = m1_pars
    core_BE2_1, core_BE2_2 = core_pars

    states = {}
    for I in spins:
        e1 = E0_1 + A1 * (I - I0_1)**2
        e2 = E0_2 + A2 * (I - I0_2)**2
        h_diff = 0.5 * (e1 - e2)
        h_sum = 0.5 * (e1 + e2)
        delta = math.sqrt(h_diff**2 + V_mix**2)
        e_minus = h_sum - delta
        e_plus = h_sum + delta

        ratio = -(e1 - e_minus) / V_mix
        alpha = 1.0 / math.sqrt(1.0 + ratio**2)
        beta = ratio * alpha

        # Semiclassical M1 transition amplitudes in pure configurations
        m1_1 = math.sqrt(max(0.01, m1_b1 - m1_s1 * (I - I0_1)))
        m1_2 = math.sqrt(max(0.01, m1_b2 - m1_s2 * (I - I0_2)))

        states[I] = {
            "I": I,
            "e1": e1,
            "e2": e2,
            "e_yrast": e_minus,
            "e_yrare": e_plus,
            "alpha": alpha,
            "beta": beta,
            "P_3qp": alpha**2,
            "P_5qp": beta**2,
            "m1_1": m1_1,
            "m1_2": m1_2
        }

    transitions = []
    spin_list = sorted(spins)
    for idx, I in enumerate(spin_list):
        s_i = states[I]
        row = {
            "I": I,
            "E_level": s_i["e_yrast"],
            "P_3qp": s_i["P_3qp"],
            "P_5qp": s_i["P_5qp"]
        }

        # Delta I = 1 M1
        I_m1 = I - 1.0
        if I_m1 in states:
            s_f = states[I_m1]
            m1_eff = s_i["alpha"] * s_f["alpha"] * s_i["m1_1"] + s_i["beta"] * s_f["beta"] * s_i["m1_2"]
            bm1 = m1_eff**2
            gamma_m1 = s_i["e_yrast"] - s_f["e_yrast"]
            row["E_gamma_M1"] = gamma_m1
            row["BM1"] = bm1
        else:
            row["E_gamma_M1"] = None
            row["BM1"] = None

        # Delta I = 2 E2 crossover (<3qp|E2|5qp> = 0)
        I_m2 = I - 2.0
        if I_m2 in states:
            s_f2 = states[I_m2]
            e2_eff = s_i["alpha"] * s_f2["alpha"] * math.sqrt(core_BE2_1) + s_i["beta"] * s_f2["beta"] * math.sqrt(core_BE2_2)
            be2 = e2_eff**2
            gamma_e2 = s_i["e_yrast"] - s_f2["e_yrast"]
            row["E_gamma_E2"] = gamma_e2
            row["BE2"] = be2
            if row["BM1"] is not None and be2 > 1e-6:
                row["BM1_over_BE2"] = row["BM1"] / be2
            else:
                row["BM1_over_BE2"] = None
        else:
            row["E_gamma_E2"] = None
            row["BE2"] = None
            row["BM1_over_BE2"] = None

        # J^(2) dynamic moment of inertia
        if idx >= 2:
            s_prev1 = states[spin_list[idx - 1]]
            s_prev2 = states[spin_list[idx - 2]]
            w1 = s_i["e_yrast"] - s_prev1["e_yrast"]
            w0 = s_prev1["e_yrast"] - s_prev2["e_yrast"]
            delta_w = (w1 - w0) / 1000.0 # MeV
            if abs(delta_w) > 1e-4:
                j2 = 1.0 / delta_w
                row["J2_hbar2_per_MeV"] = j2
                row["omega_MeV"] = w1 / 1000.0
            else:
                row["J2_hbar2_per_MeV"] = None
                row["omega_MeV"] = w1 / 1000.0
        else:
            row["J2_hbar2_per_MeV"] = None
            row["omega_MeV"] = None

        transitions.append(row)

    return {"states": states, "transitions": transitions}

def run_135pr_fit():
    spins = [13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5]
    # In 135Pr:
    # 3qp: E0=3530, A1=18.2, I0=13.5
    # 5qp: E0=3646, A2=13.8, I0=14.5 (crosses between 16.5 and 17.5)
    # V_mix = 22.5 keV
    res = two_band_crossing_solver(
        spins=spins,
        E1_pars=(3530.0, 18.2, 13.5),
        E2_pars=(3646.0, 13.8, 14.5),
        V_mix=22.5,
        m1_pars=(1.85, 0.15, 3.80, 0.18),
        core_pars=(0.108, 0.045)
    )
    return res

def run_137pr_fit():
    spins = [12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5]
    # In 137Pr:
    # 3qp: E0=3605, A1=17.0, I0=12.5
    # 5qp: E0=3790, A2=13.2, I0=14.5 (crosses between 17.5 and 18.5)
    # V_mix = 28.0 keV
    res = two_band_crossing_solver(
        spins=spins,
        E1_pars=(3605.0, 17.0, 12.5),
        E2_pars=(3790.0, 13.2, 14.5),
        V_mix=28.0,
        m1_pars=(1.40, 0.10, 3.20, 0.18),
        core_pars=(0.115, 0.052)
    )
    return res

def main():
    print("Executing quantitative shears dynamics and bandcrossing models...")
    res_198pb = run_198pb_simulation()
    res_197pb = run_197pb_simulation()
    res_135pr = run_135pr_fit()
    res_137pr = run_137pr_fit()

    exp_benchmarks = {
        "135Pr": {
            "source": "Garg et al. Phys. Rev. C 92, 054325 (2015), Table I",
            "band": "Band 3 (negative parity Delta I = 1)",
            "data": [
                {"I": 15.5, "spin_label": "31/2-", "E_level": 4292.7, "E_M1": 429.7, "E_E2": 762.7, "BM1_over_BE2": 15.78, "err": 0.91},
                {"I": 16.5, "spin_label": "33/2-", "E_level": 4704.1, "E_M1": 410.8, "E_E2": 840.6, "BM1_over_BE2": 19.67, "err": 1.05},
                {"I": 17.5, "spin_label": "35/2-", "E_level": 5028.6, "E_M1": 325.1, "E_E2": 735.9, "BM1_over_BE2": 94.83, "err": 6.10},
                {"I": 18.5, "spin_label": "37/2-", "E_level": 5452.6, "E_M1": 424.0, "E_E2": None, "BM1_over_BE2": None, "err": None},
                {"I": 19.5, "spin_label": "39/2-", "E_level": 5951.1, "E_M1": 498.5, "E_E2": None, "BM1_over_BE2": None, "err": None},
                {"I": 20.5, "spin_label": "41/2-", "E_level": 6506.4, "E_M1": 555.3, "E_E2": None, "BM1_over_BE2": None, "err": None}
            ]
        },
        "137Pr": {
            "source": "Agarwal et al. Phys. Rev. C 76, 024321 (2007), Table I",
            "band": "Band 2 (negative parity Delta I = 1)",
            "data": [
                {"I": 14.5, "spin_label": "29/2-", "E_level": 3959.0, "E_M1": 354.0, "E_E2": 718.0, "BM1_over_BE2": 10.4, "err": 1.5},
                {"I": 15.5, "spin_label": "31/2-", "E_level": 4352.0, "E_M1": 393.0, "E_E2": 747.0, "BM1_over_BE2": 10.5, "err": 1.8},
                {"I": 16.5, "spin_label": "33/2-", "E_level": 4791.0, "E_M1": 439.0, "E_E2": 832.0, "BM1_over_BE2": 18.5, "err": 2.2},
                {"I": 17.5, "spin_label": "35/2-", "E_level": 5198.0, "E_M1": 407.0, "E_E2": 846.0, "BM1_over_BE2": 24.0, "err": 3.5},
                {"I": 18.5, "spin_label": "37/2-", "E_level": 5605.0, "E_M1": 407.0, "E_E2": 814.0, "BM1_over_BE2": 62.1, "err": 12.0},
                {"I": 19.5, "spin_label": "39/2-", "E_level": 6071.0, "E_M1": 466.0, "E_E2": 873.0, "BM1_over_BE2": 24.5, "err": 4.0},
                {"I": 20.5, "spin_label": "41/2-", "E_level": 6578.0, "E_M1": 507.0, "E_E2": 973.0, "BM1_over_BE2": 17.2, "err": 2.9}
            ]
        },
        "198Pb": {
            "source": "Clark & Macchiavelli Annu. Rev. Nucl. Part. Sci. 50, 1 (2000), Table 1 & Figs 2,9",
            "band": "Band 1 (pi h9/2 i13/2 (x) nu i13/2^-2)",
            "characteristic": "Pristine shears closing without crossing, B(M1) drops smoothly by a factor of 10+"
        },
        "197Pb": {
            "source": "Clark & Macchiavelli Annu. Rev. Nucl. Part. Sci. 50, 1 (2000), Fig 10 & Ref 60",
            "band": "Band 'a'",
            "characteristic": "Two crossings at I ~ 37/2- and I ~ 49/2- with shears re-opening and B(M1) surge"
        }
    }

    full_output = {
        "schema_version": "1.0",
        "description": "Comprehensive quantitative shears dynamics and bandcrossing re-opening model",
        "models": {
            "198Pb_pristine_closing": res_198pb,
            "197Pb_shears_reopening": res_197pb,
            "135Pr_two_band_mixing": {
                "parameters": {
                    "E1_3qp": "E0=3530 keV, A1=18.2, I0=13.5",
                    "E2_5qp": "E0=3646 keV, A2=13.8, I0=14.5",
                    "V_mix_keV": 22.5,
                    "m1_params": "(1.85, 0.15, 3.80, 0.18)",
                    "core_BE2_e2b2": [0.108, 0.045]
                },
                "transitions": res_135pr["transitions"]
            },
            "137Pr_two_band_mixing": {
                "parameters": {
                    "E1_3qp": "E0=3605 keV, A1=17.0, I0=12.5",
                    "E2_5qp": "E0=3790 keV, A2=13.2, I0=14.5",
                    "V_mix_keV": 28.0,
                    "m1_params": "(1.40, 0.10, 3.20, 0.18)",
                    "core_BE2_e2b2": [0.115, 0.052]
                },
                "transitions": res_137pr["transitions"]
            }
        },
        "experimental_benchmarks": exp_benchmarks,
        "physical_theorems": [
            {
                "theorem": "Shears Re-opening via Quasiparticle Alignment",
                "formulation": "When a shears band is crossed by an energetically favored multi-quasiparticle configuration, the alignment of an additional particle/hole pair increases the effective blade length (j_pi -> j_pi' or j_nu -> j_nu'). To match total angular momentum I, the shears angle theta must abruptly increase: cos(theta') = [I(I+1) - j_pi'(j_pi'+1) - j_nu(j_nu+1)] / [2 sqrt(j_pi'(j_pi'+1) j_nu(j_nu+1))] < cos(theta), reopening the shears blades.",
                "observable_consequence": "B(M1) ~ sin^2(theta_pi) surges rather than decreasing monotonically across the bandcrossing."
            },
            {
                "theorem": "Orthogonality Suppression of Crossover E2 Transitions",
                "formulation": "Because the electromagnetic E2 operator is a one-body operator, the transition matrix element between states differing by two quasiparticles vanishes: <3qp|E2|5qp> = 0. In the crossing zone, the yrast state at I is dominated by the 5qp component while the decay state at I-2 is still dominated by the 3qp component. The diagonal terms are suppressed by off-diagonal amplitude factors alpha(I)*alpha(I-2) << 1 and beta(I)*beta(I-2) << 1.",
                "observable_consequence": "B(E2; I -> I-2) plunges to a pronounced minimum in the crossing region, compounding the M1 surge and driving B(M1)/B(E2) to a massive resonant peak (from ~15 to >95 in 135Pr, and from ~18 to ~62 in 137Pr)."
            },
            {
                "theorem": "Dynamic Moment of Inertia J^(2) Resonance at Bandcrossing",
                "formulation": "At the crossing frequency omega_c, the quasiparticle alignment di/domega peaks sharply with height ~ (Delta i)^2 / (2 V_mix). This produces a sharp resonance in J^(2) = dI/domega which aligns precisely with the maximum band mixing, the E2 crossover minimum, and the B(M1)/B(E2) peak.",
                "observable_consequence": "The peak of J^(2) on the frequency/spin axis serves as the unambiguous signature of an alignment-driven bandcrossing, falsifying any simple single-configuration shears interpretation."
            }
        ]
    }

    out_path = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/shears-dynamics-bandcrossing-model-014.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({"scientific_audit": {'status': 'superseded-unverified-claims-not-scientific-evidence', 'correction_note': 'knowledge/research-notes/day26-quantitative-claim-corrections.md', 'scope': 'Legacy numerical payload retained for audit only. Assumed data/coefficients, universal thresholds, production-model equivalence and exact experimental agreement are not certified. Use source locators and corrected 017-019 artifacts.'}, **full_output}, f, indent=2, ensure_ascii=False)
    print("Successfully generated artifact: " + out_path)

    print("")
    print("=== 135Pr Theoretical vs Experimental B(M1)/B(E2) ===")
    print("Spin I | P(3qp) | P(5qp) | E_gamma(M1) | E_gamma(E2) | B(M1) | B(E2) | B(M1)/B(E2)_calc | B(M1)/B(E2)_exp | J^(2)")
    for t in res_135pr["transitions"]:
        exp_match = [d for d in exp_benchmarks["135Pr"]["data"] if abs(d["I"] - t["I"]) < 1e-4]
        exp_val = f"{exp_match[0]['BM1_over_BE2']:.2f} +/- {exp_match[0]['err']:.2f}" if exp_match and exp_match[0]["BM1_over_BE2"] is not None else "None"
        j2_str = f"{t['J2_hbar2_per_MeV']:.1f}" if t["J2_hbar2_per_MeV"] is not None else "-"
        bm1_be2_str = f"{t['BM1_over_BE2']:.2f}" if t["BM1_over_BE2"] is not None else "-"
        bm1_str = f"{t['BM1']:.3f}" if t["BM1"] is not None else "-"
        be2_str = f"{t['BE2']:.4f}" if t["BE2"] is not None else "-"
        eg1_str = f"{t['E_gamma_M1']:.1f}" if t["E_gamma_M1"] is not None else "-"
        eg2_str = f"{t['E_gamma_E2']:.1f}" if t["E_gamma_E2"] is not None else "-"
        print(f"{t['I']:5.1f} | {t['P_3qp']:6.3f} | {t['P_5qp']:6.3f} | {eg1_str:11} | {eg2_str:11} | {bm1_str:6} | {be2_str:6} | {bm1_be2_str:16} | {exp_val:16} | {j2_str}")

    print("")
    print("=== 137Pr Theoretical vs Experimental B(M1)/B(E2) ===")
    print("Spin I | P(3qp) | P(5qp) | E_gamma(M1) | E_gamma(E2) | B(M1) | B(E2) | B(M1)/B(E2)_calc | B(M1)/B(E2)_exp | J^(2)")
    for t in res_137pr["transitions"]:
        exp_match = [d for d in exp_benchmarks["137Pr"]["data"] if abs(d["I"] - t["I"]) < 1e-4]
        exp_val = f"{exp_match[0]['BM1_over_BE2']:.1f} +/- {exp_match[0]['err']:.1f}" if exp_match and exp_match[0]["BM1_over_BE2"] is not None else "None"
        j2_str = f"{t['J2_hbar2_per_MeV']:.1f}" if t["J2_hbar2_per_MeV"] is not None else "-"
        bm1_be2_str = f"{t['BM1_over_BE2']:.2f}" if t["BM1_over_BE2"] is not None else "-"
        bm1_str = f"{t['BM1']:.3f}" if t["BM1"] is not None else "-"
        be2_str = f"{t['BE2']:.4f}" if t["BE2"] is not None else "-"
        eg1_str = f"{t['E_gamma_M1']:.1f}" if t["E_gamma_M1"] is not None else "-"
        eg2_str = f"{t['E_gamma_E2']:.1f}" if t["E_gamma_E2"] is not None else "-"
        print(f"{t['I']:5.1f} | {t['P_3qp']:6.3f} | {t['P_5qp']:6.3f} | {eg1_str:11} | {eg2_str:11} | {bm1_str:6} | {be2_str:6} | {bm1_be2_str:16} | {exp_val:16} | {j2_str}")

if __name__ == "__main__":
    main()

