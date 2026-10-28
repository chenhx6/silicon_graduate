
import json
import math

def calculate_schmidt_g_factor(l, j, is_proton):
    # Free Schmidt g-factors
    gl = 1.0 if is_proton else 0.0
    gs = 5.586 if is_proton else -3.826
    # Quenched gs by 0.7 for in-medium effective operator
    gs_eff = 0.7 * gs

    if j == l + 0.5:
        # j = l + 1/2
        gj = gl + (gs_eff - gl) / (2.0 * l + 1.0)
    else:
        # j = l - 1/2
        gj = gl - (gs_eff - gl) / (2.0 * l + 1.0)
    return gj

def run_mr_vs_er_study():
    # Orbitals active in A~100 (Ag, Z=47; N=57, 59)
    # Protons (holes in Z=50): p1/2, p3/2, f5/2, g9/2
    # Neutrons (particles above N=50): d5/2, g7/2, s1/2, d3/2, h11/2
    proton_orbitals = [
        {"name": "pi(g9/2)^-1", "l": 4, "j": 4.5, "is_proton": True},
        {"name": "pi(p1/2)^-1", "l": 1, "j": 0.5, "is_proton": True},
        {"name": "pi(p3/2)^-1", "l": 1, "j": 1.5, "is_proton": True},
        {"name": "pi(f5/2)^-1", "l": 3, "j": 2.5, "is_proton": True}
    ]

    neutron_orbitals = [
        {"name": "nu(h11/2)", "l": 5, "j": 5.5, "is_proton": False},
        {"name": "nu(d5/2)",  "l": 2, "j": 2.5, "is_proton": False},
        {"name": "nu(g7/2)",  "l": 4, "j": 3.5, "is_proton": False},
        {"name": "nu(s1/2)",  "l": 0, "j": 0.5, "is_proton": False}
    ]

    # Calculate g-factors
    for p in proton_orbitals:
        p["g_factor"] = round(float(calculate_schmidt_g_factor(p["l"], p["j"], True)), 4)
    for n in neutron_orbitals:
        n["g_factor"] = round(float(calculate_schmidt_g_factor(n["l"], n["j"], False)), 4)

    results = {
        "title": "Microscopic Configuration Selection Rules for MR vs ER Coexistence in 104,106Ag",
        "single_particle_g_factors": {
            "protons": {p["name"]: p["g_factor"] for p in proton_orbitals},
            "neutrons": {n["name"]: n["g_factor"] for n in neutron_orbitals}
        },
        "two_quasiparticle_configurations": []
    }

    # Typical core parameters for 104Ag:
    # beta2 ~ 0.12, Q0 ~ 1.5 eb, B(E2)_coll ~ 0.05 eb^2
    Q0_core = 1.5
    BE2_coll = (15.0 / (128.0 * math.pi)) * (Q0_core ** 2) # ~ 0.083 eb^2

    # Shears angle theta ~ 60 deg
    theta_rad = math.radians(60.0)

    for p in proton_orbitals:
        for n in neutron_orbitals:
            jp = p["j"]
            jn = n["j"]
            gp = p["g_factor"]
            gn = n["g_factor"]

            delta_g = abs(gp - gn)

            # Shears angular momentum capacity:
            # Delta I_shear = jp + jn - |jp - jn| = 2 * min(jp, jn)
            delta_I_shear = 2.0 * min(jp, jn)

            # Transverse magnetic dipole moment:
            # mu_perp = 0.5 * (gp - gn) * sqrt(jp * jn) * sin(theta)
            # If min(jp, jn) <= 1/2, shears mechanism is geometrically suppressed
            if min(jp, jn) >= 1.5 and delta_g >= 0.8:
                # Active shears blade
                mu_perp = 0.5 * delta_g * math.sqrt(jp * jn) * math.sin(theta_rad)
                BM1_shear = (3.0 / (8.0 * math.pi)) * (mu_perp ** 2)
                mode = "Magnetic_Rotation_(Shears)"
            else:
                # Suppressed shears -> collective or single-particle
                mu_perp = 0.1
                BM1_shear = 0.015
                mode = "Electric_Quadrupole_Rotation_(ER)"

            ratio_BM1_BE2 = BM1_shear / BE2_coll if BE2_coll > 0 else 0.0

            results["two_quasiparticle_configurations"].append({
                "configuration": f"{p['name']} (x) {n['name']}",
                "jp": jp,
                "jn": jn,
                "delta_g": round(float(delta_g), 3),
                "shears_capacity_hbar": round(float(delta_I_shear), 1),
                "mu_perp_muN": round(float(mu_perp), 3),
                "BM1_muN2": round(float(BM1_shear), 4),
                "BE2_eb2": round(float(BE2_coll), 4),
                "ratio_BM1_BE2": round(float(ratio_BM1_BE2), 2),
                "predicted_mode": mode
            })

    # Experimental correspondence in 104Ag (Wang 2013 Table I)
    results["104Ag_experimental_correspondence"] = [
        {"band": "Band A / B", "assigned_config": "pi(g9/2)^-1 (x) nu(h11/2)", "exp_character": "Chiral doublet candidate / planar shears precursor", "exp_BM1_BE2": "5 - 15 (mu_N/eb)^2"},
        {"band": "Band D / E", "assigned_config": "pi(p1/2, p3/2)^-1 (x) nu(d5/2, g7/2)", "exp_character": "Electric quadrupole rotation (Delta I = 2 cascade)", "exp_BM1_BE2": "< 0.5 (mu_N/eb)^2"},
        {"band": "Band F", "assigned_config": "pi(g9/2)^-1 (x) nu(h11/2)^2 (x) nu(d5/2)", "exp_character": "Magnetic rotation (Delta I = 1 M1 cascade)", "exp_BM1_BE2": "15 - 35 (mu_N/eb)^2"}
    ]

    out_file = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/mr-vs-er-configuration-selection-012.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("SUCCESS: wrote", out_file)

if __name__ == "__main__":
    run_mr_vs_er_study()
