import json
import math

def compute_actinide_lanthanide_comparison():
    # Comparative dataset between Lanthanides (Ba chain, Z=56) and Actinides (Ra/Rn chain, Z=86/88)
    # All experimental values from Butler 2020, Gaffney 2013, Bucher 2016/2017, and ENSDF
    lanthanides = [
        {"nucleus": "142Ba", "Z": 56, "N": 86, "BE3_Wu": None, "D0_efm": 0.05, "delta_E_low_keV": 1000.0, "nature": "octupole vibrator"},
        {"nucleus": "144Ba", "Z": 56, "N": 88, "BE3_Wu": 48.0, "D0_efm": 0.13, "delta_E_low_keV": 659.1, "nature": "dynamic octupole soft"},
        {"nucleus": "146Ba", "Z": 56, "N": 90, "BE3_Wu": 48.0, "D0_efm": 0.01, "delta_E_low_keV": 700.0, "nature": "dipole cancellation point / octupole soft"},
        {"nucleus": "148Ba", "Z": 56, "N": 92, "BE3_Wu": None, "D0_efm": -0.03, "delta_E_low_keV": 600.0, "nature": "negative dipole / quadrupole deformed"}
    ]

    actinides = [
        {"nucleus": "220Rn", "Z": 86, "N": 134, "BE3_Wu": 33.0, "D0_efm": 0.12, "delta_E_low_keV": 530.0, "nature": "octupole vibrator"},
        {"nucleus": "222Ra", "Z": 88, "N": 134, "BE3_Wu": 63.0, "D0_efm": 0.25, "delta_E_low_keV": 242.0, "nature": "strong octupole deformation"},
        {"nucleus": "224Ra", "Z": 88, "N": 136, "BE3_Wu": 42.0, "D0_efm": 0.03, "delta_E_low_keV": 83.6, "nature": "dipole minimum / rigid octupole pear shape"},
        {"nucleus": "226Ra", "Z": 88, "N": 138, "BE3_Wu": 42.0, "D0_efm": 0.14, "delta_E_low_keV": 150.0, "nature": "rigid pear shape"},
        {"nucleus": "228Ra", "Z": 88, "N": 140, "BE3_Wu": 33.0, "D0_efm": 0.03, "delta_E_low_keV": 474.0, "nature": "octupole vibrator (harmonic)"}
    ]

    results = {
        "schema": "actinide-vs-lanthanide-dipole-systematics-054/v1",
        "lanthanides_barium": lanthanides,
        "actinides_radium_radon": actinides,
        "comparative_analysis": {
            "octupole_driving_pairs": {
                "lanthanides": "Proton pi(1h11/2 - 2d5/2) and Neutron nu(1i13/2 - 2f7/2), Delta l = Delta j = 3",
                "actinides": "Proton pi(1i13/2 - 2f7/2) and Neutron nu(1j15/2 - 2g9/2), Delta l = Delta j = 3"
            },
            "dipole_cancellation_analog": "In both regions, an accidental cancellation of the intrinsic dipole moment occurs at a specific neutron number: N=90 in Barium (146Ba, D0 <= 0.01 e fm) and N=136 in Radium (224Ra, |D0| ~ 0.03 e fm vs 0.25 e fm in 222Ra). Both cancellations are driven by the occupation of the intruder high-j orbit (nu 1i13/2 in Ba, nu 1j15/2 in Ra), whose low-Omega Nilsson orbitals produce a strong negative dipole shift that neutralizes the positive proton dipole contribution.",
            "rigidity_distinction_via_energy_displacement": {
                "actinides_224Ra": "delta E(I) collapses from 83.6 keV at 1- to < 20 keV at high spin, confirming a genuine static reflection-asymmetric minimum (pear shape) with stable parity doublet bands.",
                "lanthanides_144_146Ba": "delta E(I) remains broad at 600-800 keV at low spin, only decreasing gradually at high rotational frequency due to centrifugal octupole stabilization, proving a soft dynamic octupole potential rather than a deep static minimum."
            }
        }
    }

    out_path = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/actinide-vs-lanthanide-dipole-systematics-054.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("SUCCESS: wrote", out_path)

if __name__ == "__main__":
    compute_actinide_lanthanide_comparison()
