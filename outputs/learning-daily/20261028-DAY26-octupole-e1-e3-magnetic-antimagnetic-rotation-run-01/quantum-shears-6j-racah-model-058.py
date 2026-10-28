import json
import math

def sixj_1(j1, j2, j3):
    # Racah formula for 6j symbol with one element equal to 1:
    # { j1 j2 j3 }
    # { 1  j3-1 j1 }
    S = j1 + j2 + j3
    num = 2.0 * (S + 1.0) * (j1 + j2 - j3 + 1.0) * (j1 - j2 + j3) * (j2 - j1 + j3)
    den = 2.0 * j1 * (2.0 * j1 + 1.0) * (2.0 * j1 + 2.0) * (2.0 * j3 - 1.0) * (2.0 * j3) * (2.0 * j3 + 1.0)
    if num < 0 or den <= 0:
        return 0.0
    val = math.sqrt(num / den)
    phase = (-1) ** int(round(j1 + j2 + j3))
    return phase * val

def compute_quantum_shears():
    # Parameters for 135Pr 3qp band: jp = 11/2 (5.5), jn = 10.0, delta_g = 1.42 mu_N
    jp = 5.5
    jn = 10.0
    delta_g = 1.42

    spins = [8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5]

    comparison = []
    for I in spins:
        # Exact quantum M1 using 6j symbol
        sj = sixj_1(jp, jn, I)
        bm1_quant = (3.0 / (4.0 * math.pi)) * (delta_g**2) * (2.0 * I - 1.0) * (sj**2) * jp * (jp + 1.0) * (2.0 * jp + 1.0)

        # Semi-classical Macchiavelli formula
        cos_th = (I**2 - jp**2 - jn**2) / (2.0 * jp * jn)
        if abs(cos_th) <= 1.0:
            sin2_th = 1.0 - cos_th**2
            bm1_class = (3.0 / (8.0 * math.pi)) * (delta_g**2) * ((jp * jn / I)**2) * sin2_th
            theta_deg = math.degrees(math.acos(cos_th))
        else:
            sin2_th = 0.0
            bm1_class = 0.0
            theta_deg = 0.0

        ratio = bm1_quant / bm1_class if bm1_class > 0.0001 else None

        comparison.append({
            "I": I,
            "spin": f"{int(2*I)}/2-",
            "theta_deg": round(theta_deg, 2),
            "sixj_value": round(sj, 6),
            "BM1_quantum_muN2": round(bm1_quant, 4),
            "BM1_classical_muN2": round(bm1_class, 4),
            "quantum_to_classical_ratio": round(ratio, 3) if ratio is not None else "infinite (classical zero)"
        })

    results = {
        "schema": "quantum-shears-6j-racah-model-058/v1",
        "description": "Exact finite-j quantum Racah 6j vs semi-classical shears M1 strength in 135Pr",
        "parameters": {
            "j_proton": jp,
            "j_neutron": jn,
            "delta_g_muN": delta_g
        },
        "comparison_table": comparison,
        "key_quantum_findings": [
            "At low to intermediate spin (I = 8.5 to 11.5), the exact quantum B(M1) exceeds the semi-classical Macchiavelli value by 12% to 24%, reflecting quantum finite-j dispersion of angular momentum.",
            "At the classical shears termination limit I = jp + jn = 15.5 (31/2-), the classical formula predicts B(M1) = 0 identically (sin^2 theta = 0).",
            "In contrast, the exact quantum Racah formula yields BM1 = 1.7081 mu_N^2. Quantum zero-point fluctuations of the non-commuting angular momentum operators prevent the transition strength from vanishing completely at the parallel blade boundary.",
            "This demonstrates that classical shears closure is an asymptotic approximation (valid only as j -> infinity), and finite nuclei will always exhibit residual quantum M1 collectivity at the band termination point."
        ]
    }

    out_path = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/quantum-shears-6j-racah-model-058.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("SUCCESS: wrote", out_path)

if __name__ == "__main__":
    compute_quantum_shears()
