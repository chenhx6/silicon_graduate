import json
import math

def compute_wobbling_vs_shears():
    # Comparative physical criteria for Transverse Wobbling (TW) vs Magnetic Rotation (MR) in 135Pr
    # Experimental transitions from Matta 2015, Garg 2015, and Garg 2019 erratum

    criteria = [
        {
            "property": "Primary interband multipolarity",
            "transverse_wobbling_prediction": "Predominantly collective E2 (stretched or mixed Delta I = 1 with large E2 fraction)",
            "magnetic_rotation_prediction": "Predominantly magnetic dipole M1 (Delta I = 1 M1 with small E2 crossover)",
            "experimental_fact_135Pr": "813.3 keV polarization P = +0.04(3) and R_DCO = 0.98(5) establish M1 purity >= 96.5% (E2 fraction < 3.5%)",
            "favored_model": "Magnetic Rotation"
        },
        {
            "property": "B(E2)_out / B(E2)_in ratio",
            "transverse_wobbling_prediction": "Enhanced: B(E2)_out / B(E2)_in ~ 0.5 to 2.0 (one-phonon wobbling signature)",
            "magnetic_rotation_prediction": "Suppressed: B(E2)_out / B(E2)_in << 0.1 (weak single-particle crossover)",
            "experimental_fact_135Pr": "Experimental interband E2 crossovers are extremely weak or absent; only B(M1)/B(E2) ~ 15-95 (muN/eb)^2 is extracted",
            "favored_model": "Magnetic Rotation"
        },
        {
            "property": "Energy difference evolution with spin",
            "transverse_wobbling_prediction": "E_wob = E(I, nw=1) - 0.5[E(I+1) + E(I-1)] decreases monotonically with spin (transverse phonon softening)",
            "magnetic_rotation_prediction": "Energy spacing governed by rotor + shears closure: Delta E_gamma ~ (2I)/J_eff, interrupted by band crossing at hbar*omega ~ 0.37 MeV",
            "experimental_fact_135Pr": "Band undergoes sharp Coriolis crossing at 31/2- to 33/2- with 6 hbar alignment gain, not a smooth harmonic phonon decrescendo",
            "favored_model": "Magnetic Rotation"
        },
        {
            "property": "Underlying nuclear shape requirement",
            "transverse_wobbling_prediction": "Rigid or stable triaxial shape (gamma ~ 20-30 deg, beta2 >= 0.16)",
            "magnetic_rotation_prediction": "Near-spherical or weakly deformed prolate/oblate core (beta2 <= 0.15) to prevent core collective E2 from overwhelming M1",
            "experimental_fact_135Pr": "Calculated beta2 ~ 0.12-0.15; core quadrupole deformation is moderate, allowing strong M1 shears dominance",
            "favored_model": "Magnetic Rotation"
        }
    ]

    # Quantitative evaluation of wobbling energy vs rotational frequency for Band 3 and candidate partner
    # Energy levels in keV:
    # Yrast negative parity: 11/2- (0), 15/2- (358), 19/2- (921), 23/2- (1671), 27/2- (2588), 31/2- (3530), 35/2- (4293), 39/2- (5029)
    # Side band levels: 13/2- (594), 17/2- (1082), 21/2- (1744), 25/2- (2557), 29/2- (3479), 33/2- (4704)

    spins_eval = [
        {"I": 13.5, "E_side_keV": 2557.0, "E_yrast_plus_keV": 3530.0, "E_yrast_minus_keV": 1671.0},
        {"I": 15.5, "E_side_keV": 3479.0, "E_yrast_plus_keV": 4293.0, "E_yrast_minus_keV": 2588.0},
        {"I": 17.5, "E_side_keV": 4704.0, "E_yrast_plus_keV": 5029.0, "E_yrast_minus_keV": 3530.0}
    ]

    wob_energies = []
    for item in spins_eval:
        e_wob = item["E_side_keV"] - 0.5 * (item["E_yrast_plus_keV"] + item["E_yrast_minus_keV"])
        wob_energies.append({
            "spin": f"{int(2*item['I'])}/2-",
            "I": item["I"],
            "E_wob_keV": round(e_wob, 1)
        })

    results = {
        "schema": "pr135-wobbling-vs-magnetic-rotation-063/v1",
        "nucleus": "135Pr",
        "comparative_criteria": criteria,
        "wobbling_energy_evaluation": wob_energies,
        "synthesis_conclusion": "The historical claim of transverse wobbling in 135Pr is refuted by three independent lines of evidence: (1) the 2019 erratum definitively shows the interband decay is >96.5% M1 rather than collective E2; (2) the absence of enhanced B(E2)_out/B(E2)_in signatures; and (3) the high-spin behavior is dictated by a Coriolis 3qp -> 5qp band crossing with shears re-opening, rather than harmonic phonon softening. Therefore, 135Pr Band 3 is firmly classified as Magnetic Rotation."
    }

    out_path = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/pr135-wobbling-vs-magnetic-rotation-063.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("SUCCESS: wrote", out_path)

if __name__ == "__main__":
    compute_wobbling_vs_shears()
