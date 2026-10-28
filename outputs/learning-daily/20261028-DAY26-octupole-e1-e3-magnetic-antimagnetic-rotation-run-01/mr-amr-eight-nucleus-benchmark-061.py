import json

def compute_eight_nucleus_benchmark():
    # Eight definitive benchmark nuclei for Magnetic Rotation (MR) and Antimagnetic Rotation (AMR)
    # Extracted from Clark 2000, Hubel 2005, Frauendorf 2001, Roy 2011, Garg 2015/2019, Agarwal 2007, and Kumar 2025

    mr_nuclei = [
        {
            "nucleus": "198Pb",
            "mass_region": "A ~ 195 (Lead)",
            "mode": "Magnetic Rotation (Monotonic)",
            "configuration": "pi(h9/2 i13/2) x nu(i13/2)^(-2)",
            "spin_range": "15 to 22",
            "cascade_type": "Delta I = 1 M1 regular ladder with crossover E2",
            "BM1_trajectory": "Monotonic collapse from 1.5 mu_N^2 at 16 to 0.2 mu_N^2 at 22",
            "BM1_BE2_ratio": "15 to 45 (mu_N / eb)^2",
            "lifetime_method": "DSAM absolute lifetimes confirmed",
            "shears_angle_closure": "theta closes from ~65 deg to ~20 deg",
            "evidence_tier": "Level 1: Absolute lifetimes and B(M1) confirmed"
        },
        {
            "nucleus": "199Pb",
            "mass_region": "A ~ 195 (Lead)",
            "mode": "Magnetic Rotation (Monotonic)",
            "configuration": "pi(h9/2 i13/2) x nu(i13/2)^(-1)",
            "spin_range": "33/2 to 43/2",
            "cascade_type": "Delta I = 1 M1 ladder",
            "BM1_trajectory": "Decreasing from 2.5 mu_N^2 to 0.5 mu_N^2",
            "BM1_BE2_ratio": "20 to 50 (mu_N / eb)^2",
            "lifetime_method": "DSAM absolute lifetimes confirmed",
            "shears_angle_closure": "theta closes monotonically toward band termination",
            "evidence_tier": "Level 1: Absolute lifetimes confirmed"
        },
        {
            "nucleus": "135Pr",
            "mass_region": "A ~ 135 (Rare Earth)",
            "mode": "Magnetic Rotation (Non-monotonic Rebound)",
            "configuration": "3qp pi(h11/2) x nu(h11/2)^(-2) crossing to 5qp pi(h11/2)(g7/2/d5/2)^2 x nu(h11/2)^(-2)",
            "spin_range": "27/2- to 39/2-",
            "cascade_type": "Delta I = 1 M1 ladder with E2 crossovers",
            "BM1_trajectory": "Re-opening of shears angle at crossing (I ~ 33/2-) produces rebound in B(M1)/B(E2) up to 94.8",
            "BM1_BE2_ratio": "15.8 (31/2-) -> 19.7 (33/2-) -> 94.8 (35/2-)",
            "lifetime_method": "Relative branching only; lacking absolute lifetimes",
            "shears_angle_closure": "theta_3qp closes to 0 deg at 31/2-; 5qp re-opens to ~88 deg",
            "evidence_tier": "Level 2: Relative branches confirmed; erratum confirms M1+E2 mixed nature"
        },
        {
            "nucleus": "137Pr",
            "mass_region": "A ~ 135 (Rare Earth)",
            "mode": "Magnetic Rotation (Non-monotonic Rebound)",
            "configuration": "3qp pi(h11/2) x nu(h11/2)^(-2) crossing to 5qp at hbar*omega ~ 0.30 MeV",
            "spin_range": "29/2- to 41/2-",
            "cascade_type": "Delta I = 1 M1 ladder",
            "BM1_trajectory": "Rebound in B(M1)/B(E2) peaking at 62.1 (mu_N/eb)^2 at 33/2- before declining",
            "BM1_BE2_ratio": "Peaks at 62.1 at 33/2-",
            "lifetime_method": "Relative branching only",
            "shears_angle_closure": "Coriolis alignment elongates proton blade",
            "evidence_tier": "Level 2: Relative branches confirmed"
        }
    ]

    amr_nuclei = [
        {
            "nucleus": "110Cd",
            "mass_region": "A ~ 110 (Cadmium)",
            "mode": "Antimagnetic Rotation (Plateau)",
            "configuration": "pi(g9/2)^(-2) x nu(h11/2)^2 with core rotation (Im_core ~ 19.5)",
            "spin_range": "12+ to 22+",
            "cascade_type": "Delta I = 2 pure E2 cascade; M1 identically forbidden",
            "BE2_trajectory": "Nearly constant plateau at 0.09 - 0.16 e^2b^2 from 12+ to 20+, dropping to 0.069 at 22+",
            "J2_over_BE2_range": "116.0 - 341.3 hbar^2 MeV^-1 (e^2 b^2)^-1",
            "lifetime_method": "Piiparinen 1993 RDDS (12+, 14+) + Roy 2011 DSAM (16+ - 22+)",
            "symmetry": "R_y(pi)*T discrete symmetry cancels transverse magnetic dipole moments exactly (mu_perp == 0)",
            "evidence_tier": "Level 1: Absolute DSAM/RDDS lifetimes and B(E2) plateau confirmed"
        },
        {
            "nucleus": "106Cd",
            "mass_region": "A ~ 110 (Cadmium)",
            "mode": "Antimagnetic Rotation (Pure Shears Collapse)",
            "configuration": "pi(g9/2)^(-2) x nu(h11/2)^2 (near-inert core)",
            "spin_range": "16+ to 24+",
            "cascade_type": "Delta I = 2 pure E2 cascade; no M1",
            "BE2_trajectory": "Steep 20x collapse from 0.14(3) e^2b^2 down to 0.007(3) e^2b^2",
            "J2_over_BE2_range": "150 - 1200 hbar^2 MeV^-1 (e^2 b^2)^-1",
            "lifetime_method": "DSAM lifetimes confirmed",
            "symmetry": "R_y(pi)*T symmetry; textbook sin^4(theta) shears collapse",
            "evidence_tier": "Level 1: Absolute lifetimes and 20x B(E2) collapse confirmed"
        },
        {
            "nucleus": "108Cd",
            "mass_region": "A ~ 110 (Cadmium)",
            "mode": "Antimagnetic Rotation (Intermediate)",
            "configuration": "pi(g9/2)^(-2) x nu(h11/2)^2",
            "spin_range": "16+ to 22+",
            "cascade_type": "Delta I = 2 pure E2 cascade; no M1",
            "BE2_trajectory": "Moderate 8x decline from 0.12(3) e^2b^2 to 0.015(4) e^2b^2",
            "J2_over_BE2_range": "130 - 650 hbar^2 MeV^-1 (e^2 b^2)^-1",
            "lifetime_method": "DSAM lifetimes confirmed",
            "symmetry": "R_y(pi)*T symmetry",
            "evidence_tier": "Level 1: Absolute lifetimes confirmed"
        },
        {
            "nucleus": "105Pd",
            "mass_region": "A ~ 105 (Palladium)",
            "mode": "Antimagnetic Rotation (Odd-A)",
            "configuration": "pi(g9/2)^(-4) x nu(h11/2)^1",
            "spin_range": "19/2- to 31/2-",
            "cascade_type": "Delta I = 2 pure E2 cascade; no M1",
            "BE2_trajectory": "Decreasing from 0.18(4) e^2b^2 to 0.03(1) e^2b^2 (6x drop)",
            "J2_over_BE2_range": "120 - 280 hbar^2 MeV^-1 (e^2 b^2)^-1",
            "lifetime_method": "DSAM lifetimes confirmed",
            "symmetry": "R_y(pi)*T symmetry in 4-proton-hole double shears",
            "evidence_tier": "Level 1: Absolute lifetimes confirmed"
        }
    ]

    results = {
        "schema": "mr-amr-eight-nucleus-benchmark-061/v1",
        "description": "Comprehensive eight-nucleus benchmark database across three mass regions (A~110, A~135, A~195) comparing Magnetic Rotation and Antimagnetic Rotation",
        "magnetic_rotation_nuclei": mr_nuclei,
        "antimagnetic_rotation_nuclei": amr_nuclei,
        "cross_mass_region_conclusions": {
            "MR_behavior": "In A ~ 195 (Pb), MR is characterized by near-pure single-shears monotonic collapse of B(M1) ~ sin^2(theta) toward band termination. In A ~ 135 (Pr), MR is interrupted by centrifugal Coriolis band crossing (3qp -> 5qp), where blade elongation causes shears angle re-opening and sharp B(M1)/B(E2) rebound.",
            "AMR_behavior": "In A ~ 105-110 (Cd-Pd), AMR universally exhibits Delta I = 2 pure E2 cascades with complete absence of M1 transitions due to R_y(pi)*T discrete symmetry. The B(E2) trajectory varies from pure shears 20x collapse (106Cd) to core-decoupled plateau (110Cd) as core rotational inertia Im_core increases with neutron number toward mid-shell.",
            "defining_criterion_contrast": "MR is defined by large B(M1) ~ 1-10 mu_N^2 and high B(M1)/B(E2) ~ 10-100 (mu_N/eb)^2. AMR is defined by identical M1 extinction (B(M1) == 0) and gigantic dynamic inertia to transition ratio J(2)/B(E2) ~ 100-1200 hbar^2 MeV^-1 (e^2 b^2)^-1, ten times higher than conventional collective rotors."
        }
    }

    out_path = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/mr-amr-eight-nucleus-benchmark-061.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("SUCCESS: wrote", out_path)

if __name__ == "__main__":
    compute_eight_nucleus_benchmark()
