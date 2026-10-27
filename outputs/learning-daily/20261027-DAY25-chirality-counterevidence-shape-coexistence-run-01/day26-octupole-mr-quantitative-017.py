
import math
import json
import pathlib

# 1. Octupole B(E3) Weisskopf and Q3 calculation
def bw_e3(A):
    # R0 = 1.2 * A^(1/3) fm
    # B_W(E3) = (1 / (16 * pi)) * R0^6 (e^2 fm^6)
    # 1 b = 100 fm^2, 1 b^3 = 10^6 fm^6 => 1 e^2 fm^6 = 10^-6 e^2 b^3
    R0 = 1.2 * (A ** (1.0 / 3.0))
    bw_fm6 = (1.0 / (16.0 * math.pi)) * (R0 ** 6)
    bw_b3 = bw_fm6 * 1e-6
    return bw_fm6, bw_b3

octupole_data = {}
for A in [144, 146]:
    bw_fm6, bw_b3 = bw_e3(A)
    # Experimental matrix element magnitude
    M_E3 = 0.65 # e b^(3/2)
    # Transition 3- -> 0+: B(E3) = |M|^2 / (2*3 + 1) = M^2 / 7
    be3_down_b3 = (M_E3 ** 2) / 7.0
    be3_down_fm6 = be3_down_b3 * 1e6
    wu_down = be3_down_b3 / bw_b3
    # Intrinsic Q3 in axial rotor: Q3 = sqrt(16 pi / 7) * M(E3)
    # in e fm^3 (M in e b^(3/2) = M * 1000 e fm^3)
    q3_efm3 = math.sqrt(16.0 * math.pi / 7.0) * (M_E3 * 1000.0)
    
    octupole_data[f"Ba{A}"] = {
        "A": A,
        "M_E3_eb32": M_E3,
        "B_W_E3_b3": bw_b3,
        "B_W_E3_fm6": bw_fm6,
        "B_E3_down_b3": be3_down_b3,
        "B_E3_down_fm6": be3_down_fm6,
        "B_E3_down_Wu": wu_down,
        "Q3_efm3": q3_efm3,
        "beta3_approx": 0.17
    }

# 2. E1 Dipole cancellation systematics
e1_systematics = {
    "Ba144": {
        "N": 88,
        "D0_efm": 0.13,
        "D0_err": 0.02,
        "B_E3_Wu": 48.0,
        "status": "normal_octupole_dipole"
    },
    "Ba146": {
        "N": 90,
        "D0_efm": 0.015,
        "D0_err": 0.005,
        "B_E3_Wu": 48.0,
        "status": "severe_dipole_cancellation",
        "sccm_neutron_occupancies": {
            "h9_2": 0.40,
            "f7_2": 0.27,
            "i13_2": 0.20
        }
    },
    "Ba148": {
        "N": 92,
        "D0_efm": 0.05,
        "D0_err": 0.02,
        "B_E3_Wu": "recovering",
        "status": "sign_inversion_recovery"
    }
}

# 3. Magnetic rotation shears mechanism in 135Pr
# Symmetric shears model: I = 2j cos(theta/2)
# B(M1) = (3 / 8pi) * (g_pi - g_nu)^2 * j^2 * sin^2(theta/2)
# With j_eff = 15.5 / 2 = 7.75 or two blades j1=11/2, j2=10
j_pi = 5.5
j_nu = 10.0
g_pi = 1.21
g_nu = -0.24
g_diff = g_pi - g_nu

shears_curve = []
# Calculate for spin from 13/2 (6.5) to 35/2 (17.5)
j_tot_max = j_pi + j_nu # 15.5
j_tot_min = abs(j_nu - j_pi) # 4.5

# Garg 2015 experimental B(M1)/B(E2) in (mu_N/eb)^2 approx
# From Table I / Fig 5/6:
# 17/2- : ~24.5
# 19/2- : ~18.2
# 21/2- : ~14.1
# 23/2- : ~10.5
# 25/2- : ~8.2
# 27/2- : ~8.0 (band crossing)
# 29/2- : ~11.5
# 31/2- : ~14.2
# 33/2- : ~18.0
# 35/2- : ~22.0
exp_bm1_be2 = {
    8.5: 24.5,
    9.5: 18.2,
    10.5: 14.1,
    11.5: 10.5,
    12.5: 8.2,
    13.5: 8.0,
    14.5: 11.5,
    15.5: 14.2,
    16.5: 18.0,
    17.5: 22.0
}

for I_val in [6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5]:
    # Shears angle
    cos_half_theta = I_val / j_tot_max
    if cos_half_theta <= 1.0:
        half_theta_rad = math.acos(cos_half_theta)
        theta_deg = math.degrees(2.0 * half_theta_rad)
        sin_half_theta = math.sin(half_theta_rad)
        # B(M1) arbitrary scale factor for comparison
        bm1_rel = (sin_half_theta ** 2)
        # Parabolic drop factor: 1 - (I / I_max)^2
        drop_factor = 1.0 - (cos_half_theta ** 2)
    else:
        theta_deg = 0.0
        bm1_rel = 0.0
        drop_factor = 0.0
    
    exp_val = exp_bm1_be2.get(I_val, None)
    shears_curve.append({
        "I": I_val,
        "spin_str": f"{int(2*I_val)}/2",
        "theta_deg": theta_deg,
        "sin_half_theta": sin_half_theta,
        "bm1_rel_drop": drop_factor,
        "exp_bm1_be2": exp_val,
        "regime": "3qp_shears_closing" if I_val <= 13.5 else "5qp_realignment_crossing"
    })

output_data = {
    "schema_version": 1,
    "topic": "Day 26 uncredited preview: octupole E3 Coulex, E1 cancellation, and MR shears mechanism",
    "day_index": 25,
    "preview_day_index": 26,
    "formal_credit_awarded": False,
    "octupole_coulex": octupole_data,
    "e1_systematics": e1_systematics,
    "shears_model_pr135": {
        "j_pi": j_pi,
        "j_nu": j_nu,
        "g_pi": g_pi,
        "g_nu": g_nu,
        "g_diff": g_diff,
        "curve": shears_curve
    },
    "conclusions": [
        "Bucher 2016/2017 B(E3) yields 49.0 and 47.7 W.u., confirming reported 48 W.u. with exact R0=1.2 A^(1/3) fm",
        "Rotor intrinsic Q3 = 1.74 * 10^3 e fm^3 matches Bucher 2016 (1.73 * 10^3 e fm^3)",
        "E1 drop of >10x in Ba146 is decoupled from E3 collectivity, explained by Gogny D1S SCCM neutron orbital cancellation",
        "Symmetric shears model explains B(M1)/B(E2) parabolic drop in low-spin Pr135, while high-spin rise reflects 5qp band crossing",
        "Garg 2015 lacks level lifetimes, keeping Pr135 strictly at candidate MR status"
    ]
}

out_path = pathlib.Path("outputs/learning-daily/20261027-DAY25-chirality-counterevidence-shape-coexistence-run-01/day26-octupole-mr-quantitative-017.json")
out_path.write_text(json.dumps(output_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("Successfully generated day26-octupole-mr-quantitative-017.json")
