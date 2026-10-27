"""Conditional mathematics controls; no event data or PADO producer is run."""
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import pi, tan
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

def main():
    # F(x,s)=(x^2,s), x in [-1,2], s in [0,1], f_O=1/4.
    negative_raw = Q(1, 4)
    positive_raw = Q(4, 4)
    normalizer = negative_raw + positive_raw
    masses = [negative_raw / normalizer, positive_raw / normalizer]
    obs_overlap = Q(1, 4)
    mapped_overlap = Q(2, 4) / normalizer
    split_masses = [Q(1, 8), Q(1, 8) + Q(3, 4)]
    intervals = [(-.42, -.75, -.31), (-.26, -.43, -.19), (-.29, -.43, -.20)]
    fractions = []
    for center, lo, hi in intervals:
        m1 = lambda d: 1 / (1 + d*d)
        fractions.append({"delta_center": center, "delta_bounds": [lo, hi],
                          "M1_center": m1(center), "M1_endpoint_image": [m1(lo), m1(hi)]})
    # Uniform density in xi_rad yields a Cauchy density in delta.
    density_rad = 1/pi
    density_deg = 1/180
    delta = 2.0
    rad_to_delta = density_rad/(1+delta**2)
    deg_to_delta = density_deg*(180/pi)/(1+delta**2)
    checks = {
        "weighted_area_Z_is_5_over_4": normalizer == Q(5,4),
        "normalized_branch_masses_are_1_5_and_4_5": masses == [Q(1,5), Q(4,5)],
        "overlap_reweighted_from_1_4_to_2_5": obs_overlap == Q(1,4) and mapped_overlap == Q(2,5),
        "pointwise_split_recovers_unit_mass": sum(split_masses) == 1,
        "pointwise_split_masses_are_1_8_and_7_8": split_masses == [Q(1,8),Q(7,8)],
        "degree_radian_density_agreement": abs(rad_to_delta-deg_to_delta) < 1e-15,
        "Pr_first_M1_lower_is_64pct": abs(fractions[0]["M1_endpoint_image"][0]-.64) < 1e-15,
        "Pr_all_bounds_exceed_one_half": all(min(x["M1_endpoint_image"])>.5 for x in fractions),
        "Pr_uniform_85pct_lower_bound_fails": any(min(x["M1_endpoint_image"]) < .85 for x in fractions),
        "finite_angle_89deg_delta_is_less_than_58": 57 < tan(89*pi/180) < 58,
    }
    result = {
        "scope": "conditional mathematical exercise, not experiment or PADO benchmark reproduction",
        "F": "(x,s)->(x^2,s)", "parameter_domain": "[-1,2]x[0,1]",
        "observable_density": "1/4 on [0,4]x[0,1]", "w": 1,
        "Z": str(normalizer), "branch_masses": list(map(str,masses)),
        "observable_overlap_original": str(obs_overlap), "observable_overlap_pushforward": str(mapped_overlap),
        "pointwise_split_branch_masses": list(map(str,split_masses)),
        "Pr_M1_endpoint_images": fractions, "delta_89deg": tan(89*pi/180),
        "raw_fingerprints": {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest()
                             for p in [ROOT/'raw/writing/pado/20260722.pdf', ROOT/'raw/writing/pado/nst_sample.pdf', ROOT/'raw/writing/pado/nst_sample.tex']},
        "checks": checks, "passed": all(checks.values())
    }
    assert result['passed']
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__ == '__main__':
    main()
