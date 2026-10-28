import json
import math

def compute_pr_isotopes_comparison():
    # Comparative analysis between 135Pr (N=76) and 137Pr (N=78)
    # Data from Garg 2015 (PRC 92, 054325) and Agarwal 2007 (PRC 76, 024305)
    pr135 = {
        "nucleus": "135Pr",
        "Z": 59, "N": 76,
        "crossing_freq_MeV": 0.37,
        "crossing_spin": "31/2- to 33/2-",
        "initial_shears_config": "3qp: pi(h11/2) x nu(h11/2)^(-2)",
        "crossing_shears_config": "5qp: pi(h11/2)(g7/2/d5/2)^2 x nu(h11/2)^(-2)",
        "jp_initial": 5.5, "jn_initial": 10.0,
        "jp_crossed": 11.5, "jn_crossed": 10.0,
        "max_BM1_BE2_ratio": 94.83,
        "max_BM1_BE2_spin": "35/2-",
        "polarization_erratum": "PRC 100, 069901(E) (2019): 813.3 keV corrected to +0.04(3), confirming mixed M1+E2"
    }

    pr137 = {
        "nucleus": "137Pr",
        "Z": 59, "N": 78,
        "crossing_freq_MeV": 0.30,
        "crossing_spin": "29/2- to 31/2-",
        "initial_shears_config": "3qp: pi(h11/2) x nu(h11/2)^(-2)",
        "crossing_shears_config": "5qp: pi(h11/2)(h11/2)^2 x nu(h11/2)^(-2) or similar alignment",
        "jp_initial": 5.5, "jn_initial": 10.0,
        "jp_crossed": 11.5, "jn_crossed": 10.0,
        "max_BM1_BE2_ratio": 62.1,
        "max_BM1_BE2_spin": "33/2-",
        "polarization_status": "Consistent with magnetic dipole character"
    }

    results = {
        "schema": "pr-isotopes-shears-crossing-comparison-055/v1",
        "135Pr": pr135,
        "137Pr": pr137,
        "systematic_conclusions": [
            "In both 135Pr and 137Pr, the negative-parity shears band does not terminate via simple monotonic blade closing to zero strength.",
            "Instead, centrifugal Coriolis forces drive a 3qp -> 5qp band crossing at rotational frequencies hbar*omega ~ 0.30 - 0.37 MeV.",
            "The alignment of an additional quasiparticle pair elongates the effective blade length, causing the shears angle to mechanically re-open.",
            "The shears re-opening produces a sharp upturn/rebound in B(M1)/B(E2), reaching 94.8 in 135Pr and 62.1 in 137Pr, confirming that non-monotonic B(M1)/B(E2) trajectories are a robust systematic feature of high-spin magnetic rotation across Pr isotopes."
        ]
    }

    out_path = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/pr-isotopes-shears-crossing-comparison-055.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("SUCCESS: wrote", out_path)

if __name__ == "__main__":
    compute_pr_isotopes_comparison()
