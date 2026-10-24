
import json
import math
from pathlib import Path

ROOT = Path("/workspace/wiki")
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'

# Hinke 2010 (GSI)
e0_hinke = 3.29
tau_hinke = 1.16
bgt_hinke = 9.1

# Lubos 2016 (RIKEN)
e0_lubos = 3.74
tau_lubos = 1.17
bgt_lubos = 5.26

# Phase space ratio from Checkpoint 099
ratio_sommerfeld = 1.81002
ratio_dirac = 1.78572

# Sensitivity exponent
eta_sommerfeld = math.log(ratio_sommerfeld) / math.log(e0_lubos / e0_hinke)
eta_dirac = math.log(ratio_dirac) / math.log(e0_lubos / e0_hinke)

# Scaled Hinke B(GT) if evaluated at Lubos phase space and half-life:
bgt_hinke_scaled_sommerfeld = bgt_hinke / ratio_sommerfeld * (tau_hinke / tau_lubos)
bgt_hinke_scaled_dirac = bgt_hinke / ratio_dirac * (tau_hinke / tau_lubos)

residual_sommerfeld = abs(bgt_hinke_scaled_sommerfeld - bgt_lubos) / bgt_lubos
residual_dirac = abs(bgt_hinke_scaled_dirac - bgt_lubos) / bgt_lubos

# ESPM free single particle strength
bgt_espm = 160.0 / 9.0  # 17.7778

quench_hinke_nominal = bgt_hinke / bgt_espm
quench_lubos_nominal = bgt_lubos / bgt_espm
quench_hinke_scaled_dirac = bgt_hinke_scaled_dirac / bgt_espm

res = {
    "title": "100Sn Gamow-Teller Phase Space Scaling and Quenching Re-evaluation",
    "primary_data": {
        "Hinke_2010": {"E0_MeV": e0_hinke, "T12_s": tau_hinke, "B_GT": bgt_hinke},
        "Lubos_2016": {"E0_MeV": e0_lubos, "T12_s": tau_lubos, "B_GT": bgt_lubos}
    },
    "phase_space_expansion": {
        "endpoint_shift_percent": (e0_lubos / e0_hinke - 1.0) * 100.0,
        "phase_space_ratio_sommerfeld": ratio_sommerfeld,
        "phase_space_ratio_dirac": ratio_dirac,
        "sensitivity_exponent_sommerfeld": eta_sommerfeld,
        "sensitivity_exponent_dirac": eta_dirac
    },
    "scaled_strength_comparison": {
        "bgt_hinke_scaled_sommerfeld": bgt_hinke_scaled_sommerfeld,
        "bgt_hinke_scaled_dirac": bgt_hinke_scaled_dirac,
        "residual_discrepancy_sommerfeld_percent": residual_sommerfeld * 100.0,
        "residual_discrepancy_dirac_percent": residual_dirac * 100.0,
        "resolution_finding": "The apparent 73% discrepancy between GSI (9.1) and RIKEN (5.26) shrinks to only 3.9% - 5.2% after correcting for the phase-space dilation driven by the 450 keV endpoint shift."
    },
    "quenching_factors": {
        "B_GT_free_ESPM": bgt_espm,
        "quench_factor_Hinke_nominal": quench_hinke_nominal,
        "quench_factor_Lubos_nominal": quench_lubos_nominal,
        "quench_factor_Hinke_scaled": quench_hinke_scaled_dirac,
        "effective_gA_over_gAfree_Lubos": math.sqrt(quench_lubos_nominal),
        "effective_gA_over_gAfree_Hinke_scaled": math.sqrt(quench_hinke_scaled_dirac),
        "quenching_concordance": "Both experiments yield an identical effective gA/gA_free ~ 0.53 - 0.54 once phase-space inputs are harmonized."
    }
}

out = RUN / 'sn100-gt-scaling-scope-137.json'
out.write_text(json.dumps(res, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({
    "output": str(out.relative_to(ROOT)),
    "bgt_scaled_dirac": bgt_hinke_scaled_dirac,
    "residual_percent": residual_dirac * 100.0,
    "effective_gA_ratio": math.sqrt(quench_hinke_scaled_dirac)
}))
