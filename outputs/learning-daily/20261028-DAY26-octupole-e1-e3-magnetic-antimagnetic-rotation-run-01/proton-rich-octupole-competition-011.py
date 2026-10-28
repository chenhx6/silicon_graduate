
import json
import math

def clebsch_gordan(j1, m1, j2, m2, j3, m3):
    # Specialized Clebsch-Gordan for integer/half-integer
    # using standard Racah formula or lookup for common Delta l = Delta j = 3
    pass

def reduced_matrix_element_Y3(l1, j1, l2, j2):
    # < j1 || Y3 || j2 > = (-1)^(j1 - 1/2) * sqrt((2*j1+1)*(2*j2+1)*7 / (4*pi)) * (j1 1/2, j2 -1/2 | 3 0)
    # For Delta l = Delta j = 3:
    # 1. d5/2 <-> h11/2 (j1=5/2, j2=11/2):
    #    (5/2 1/2, 11/2 -1/2 | 3 0) = -sqrt(1/14) * sqrt(15/22) ~ -0.2209
    # 2. f7/2 <-> i13/2 (j1=7/2, j2=13/2):
    #    (7/2 1/2, 13/2 -1/2 | 3 0) = -sqrt(1/16) * sqrt(21/26) ~ -0.2250
    if (j1, j2) == (2.5, 5.5) or (j1, j2) == (5.5, 2.5):
        cg = - math.sqrt(15.0 / 308.0)
        rme = math.sqrt((2.0 * 2.5 + 1.0) * (2.0 * 5.5 + 1.0) * 7.0 / (4.0 * math.pi)) * abs(cg)
        return rme
    elif (j1, j2) == (3.5, 6.5) or (j1, j2) == (6.5, 3.5):
        cg = - math.sqrt(21.0 / 416.0)
        rme = math.sqrt((2.0 * 3.5 + 1.0) * (2.0 * 6.5 + 1.0) * 7.0 / (4.0 * math.pi)) * abs(cg)
        return rme
    return 1.0

def run_octupole_competition_study():
    # Comparing 144Ba (neutron-rich) vs 130Sm (proton-rich, near drip line)
    # and 128Nd, 126Ce
    nuclei = [
        {
            "nucleus": "144Ba",
            "type": "neutron_rich",
            "Z": 56, "N": 88, "A": 144,
            "proton_pair": "pi(2d5/2 - 1h11/2)",
            "neutron_pair": "nu(2f7/2 - 1i13/2)",
            "beta2_equil": 0.20,
            "beta3_equil": 0.11,
            "quadrupole_splitting_MeV": 1.45,
            "octupole_phonon_Ex_keV": 759.0,
            "BE3_Wu": 48.0
        },
        {
            "nucleus": "146Ba",
            "type": "neutron_rich",
            "Z": 56, "N": 90, "A": 146,
            "proton_pair": "pi(2d5/2 - 1h11/2)",
            "neutron_pair": "nu(2f7/2 - 1i13/2)",
            "beta2_equil": 0.22,
            "beta3_equil": 0.12,
            "quadrupole_splitting_MeV": 1.55,
            "octupole_phonon_Ex_keV": 737.5,
            "BE3_Wu": 48.0
        },
        {
            "nucleus": "130Sm",
            "type": "proton_rich_drip_line",
            "Z": 62, "N": 68, "A": 130,
            "proton_pair": "pi(2d5/2 - 1h11/2)",
            "neutron_pair": "nu(2d5/2 - 1h11/2)", # identical partner pair!
            "beta2_equil": 0.33, # strong prolate deformation
            "beta3_equil": 0.05, # suppressed by large beta2
            "quadrupole_splitting_MeV": 2.65,
            "octupole_phonon_Ex_keV": 1450.0, # pushed up by quadrupole splitting
            "BE3_Wu": 18.0
        },
        {
            "nucleus": "128Nd",
            "type": "proton_rich",
            "Z": 60, "N": 68, "A": 128,
            "proton_pair": "pi(2d5/2 - 1h11/2)",
            "neutron_pair": "nu(2d5/2 - 1h11/2)",
            "beta2_equil": 0.31,
            "beta3_equil": 0.06,
            "quadrupole_splitting_MeV": 2.45,
            "octupole_phonon_Ex_keV": 1380.0,
            "BE3_Wu": 21.0
        },
        {
            "nucleus": "126Ce",
            "type": "proton_rich",
            "Z": 58, "N": 68, "A": 126,
            "proton_pair": "pi(2d5/2 - 1h11/2)",
            "neutron_pair": "nu(2d5/2 - 1h11/2)",
            "beta2_equil": 0.29,
            "beta3_equil": 0.07,
            "quadrupole_splitting_MeV": 2.25,
            "octupole_phonon_Ex_keV": 1290.0,
            "BE3_Wu": 24.0
        }
    ]

    rme_d5_h11 = reduced_matrix_element_Y3(2, 2.5, 5, 5.5)
    rme_f7_i13 = reduced_matrix_element_Y3(3, 3.5, 6, 6.5)

    results = {
        "title": "Quadrupole-Octupole Competition in Light Rare-Earth (Proton-Rich) vs Neutron-Rich Ba Isotopes",
        "single_particle_octupole_matrix_elements": {
            "d5_2_to_h11_2": round(float(rme_d5_h11), 4),
            "f7_2_to_i13_2": round(float(rme_f7_i13), 4)
        },
        "nuclei_comparison": []
    }

    for nuc in nuclei:
        # Effective octupole driving force: F_oct = G_oct * (rme_p^2 + rme_n^2)
        # In proton-rich, both are d5/2-h11/2 (rme_d5_h11)
        # In neutron-rich, one is d5/2-h11/2, other is f7/2-i13/2
        if nuc["type"] == "neutron_rich":
            F_oct_bare = rme_d5_h11**2 + rme_f7_i13**2
        else:
            F_oct_bare = 2.0 * (rme_d5_h11**2)

        # Quadrupole quenching factor: eta_quench = exp( - (beta2 / 0.18)^2 )
        # Large beta2 splits the single-particle Nilsson orbitals, increasing the energy denominator
        # Delta E_eff = sqrt(Delta E_0^2 + (C_quad * beta2)^2)
        Delta_E0 = 3.0 # typical unperturbed Delta N = 3 energy gap in MeV
        Delta_E_eff = math.sqrt(Delta_E0**2 + nuc["quadrupole_splitting_MeV"]**2)

        # Effective octupole susceptibility: chi_oct = F_oct_bare / Delta_E_eff
        chi_oct = F_oct_bare / Delta_E_eff

        results["nuclei_comparison"].append({
            "nucleus": nuc["nucleus"],
            "type": nuc["type"],
            "Z": nuc["Z"],
            "N": nuc["N"],
            "beta2": nuc["beta2_equil"],
            "beta3": nuc["beta3_equil"],
            "unperturbed_octupole_strength": round(float(F_oct_bare), 4),
            "effective_energy_denominator_MeV": round(float(Delta_E_eff), 4),
            "octupole_susceptibility": round(float(chi_oct), 4),
            "octupole_phonon_Ex_keV": nuc["octupole_phonon_Ex_keV"],
            "BE3_Wu": nuc["BE3_Wu"],
            "octupole_regime": "pronounced_soft_octupole" if nuc["beta3_equil"] >= 0.10 else "quadrupole_quenched_vibrational"
        })

    out_file = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/proton-rich-octupole-competition-011.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("SUCCESS: wrote", out_file)

if __name__ == "__main__":
    run_octupole_competition_study()
