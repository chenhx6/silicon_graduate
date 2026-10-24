#!/usr/bin/env python3
"""Declared angular-momentum counterexample and printed inertia ratios only."""
import json
import math
from pathlib import Path
import numpy as np


def calculate():
    gamma = math.radians(22.4)
    # Qi2009 v1 uses k=1 as intermediate, k=2 short, k=3 long here.
    fractions = [math.sin(gamma-2*k*math.pi/3)**2 for k in [1, 2, 3]]
    j = 19.5
    m = np.arange(-j, j+1)
    jp = np.zeros((len(m), len(m)), dtype=complex)
    for i, mi in enumerate(m[:-1]):
        jp[i+1, i] = math.sqrt(j*(j+1)-mi*(mi+1))
    jm = jp.conj().T
    ops = [(jp+jm)/2, (jp-jm)/(2j), np.diag(m)]
    ket = np.zeros(len(m), dtype=complex)
    ket[-1] = 1
    means = [float(np.vdot(ket, op@ket).real) for op in ops]
    seconds = [float(np.vdot(ket, op@op@ket).real) for op in ops]
    return {
        "source_scope": "Qi2009 arxiv0812.4597v1 p.4 Eq2, p.6 inertia ratio, pp.6-8 geometry",
        "inertia_gamma_degrees": 22.4,
        "inertia_fractions_i_s_l": fractions,
        "inertia_ratios_to_long": [v/fractions[-1] for v in fractions],
        "declared_spin_coherent_counterexample": {
            "j": j, "state": "|j,m=j> along z; generic spin state, not a 135Nd fit",
            "mean_Jx_Jy_Jz_hbar": means,
            "second_Jx_Jy_Jz_hbar2": seconds,
            "rms_Jx_Jy_Jz_hbar": [math.sqrt(v) for v in seconds],
            "sum_second_moments": sum(seconds),
            "j_times_jplus1": j*(j+1),
            "matrix_algebra_residual": sum(seconds)-j*(j+1),
            "lesson": "nonzero RMS on three axes alone does not fix a signed aplanar orientation or handedness",
        },
        "model_reproduction": False,
        "actual_wavefunctions": None,
        "actual_parameter_confidence_region": None,
        "experimental_CI": None,
    }


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    p = root / "outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/prm-geometry-scope-053.json"
    r = calculate()
    p.write_text(json.dumps(r, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps(r, ensure_ascii=False))
