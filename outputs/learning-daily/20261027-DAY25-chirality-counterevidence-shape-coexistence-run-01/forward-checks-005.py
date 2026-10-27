#!/usr/bin/env python3
"""Day25 checkpoint005: conditional algebra, never an event/model replay or CI."""
import hashlib
import json
import math
import re
from pathlib import Path

def main():
    thesis = Path("raw/papers/degree dissertation/Triaxiality and Rotational bands in 133Ce.pdf")
    r465 = 1.89 / 1.95 * (982.0 / 608.3) ** 5
    a, b = .18 / 1.89, .17 / 1.95
    out = {
        "scope": {
            "experiment_refit": False, "author_input_recovered": False,
            "confidence_interval": False, "human_review": False,
            "source": str(thesis), "sha256": hashlib.sha256(thesis.read_bytes()).hexdigest(),
            "locators": ["physicalPDF67 Table5.2", "physicalPDF78 Table6.2",
                         "physicalPDF112 Table6.11", "PE06 physicalPDF3 TableI"],
        },
        "ce133_465": {
            "ratio_from_printed_photon_yields": r465,
            "table611_ratio_E2": 1.06 / .09, "table611_ratio_M1": 5.54 / .47,
            "conditional_sigma_by_assumed_correlation": {
                str(rho): r465 * math.sqrt(max(0, a*a+b*b-2*rho*a*b))
                for rho in [-1, 0, 1]
            },
            "warning": "rho, efficiency/gate covariance and underlying producer unknown; no CI or lineage proof",
        },
        "ce133_582_hypothetical_only": {
            "unobserved_energy_difference_keV": 1409.8 - 592.1,
            "intensity_from_table611_double_ratio_E2": 3.22*(817.7/577.8)**5/(5.06/.33),
            "intensity_from_table611_double_ratio_M1": 3.22*(817.7/577.8)**5/(3.95/.25),
            "intensity_from_printed_delta_yield_and_outout": 3.53*.55**2/(1+.55**2)*(817.7/582.7)**5/5.06,
            "detection_limit": None, "observed_denominator": None,
        },
        "energy_zero_diagnostic": {
            "hbaromega_empirical_MeV": 41*133**(-1/3),
            "backsolved_residual_NOT_a_table_energy": 50.6-5.5*41*133**(-1/3),
            "actual_table62_eps18_19_20_header_MeV": [5.8046,5.8239,5.8985],
            "actual_table62_eps23_N6": 6.4922,
            "actual_conversion": None, "actual_negative_parity_lambda": None,
        },
        "S_equal_independent_energy_variance": {
            "assumption": "Cov(E)=sigma_E^2 identity; not actual level covariance",
            "variance_factor": 5, "lag_covariance_factors": [5,-3.75,1.5,-.25,0],
            "lag_correlations": [1,-.75,.3,-.05,0],
        },
        "ce133_table53_closure": {
            "rows_preserved_separately": [
                {"Ei":2733.4,"Ef_hypothesis":1852.7,"Eg":881.2,"Ei_minus_Ef_minus_Eg":2733.4-1852.7-881.2},
                {"Ei":2739.5,"Ef_hypothesis":1852.7,"Eg":886.8,"Ei_minus_Ef_minus_Eg":2739.5-1852.7-886.8}
            ], "interpretation": "printed row identity not proof of two independently established physical levels",
        },
    }
    # R rows/columns: physical y/ny = R @ bare; Q is a declared real symmetric forward kernel.
    # These alphas came from the original diagonal-Q fit, so this is not an independent refit.
    def ratios(ai,af,x,y,invert):
        bi,bf = math.sqrt(1-ai*ai),math.sqrt(1-af*af)
        m00=af*ai+bf*bi*y+(af*bi+bf*ai)*x
        m10=bf*ai-af*bi*y+(bf*bi-af*ai)*x
        m01=af*bi-bf*ai*y+(bf*bi-af*ai)*x
        m11=bf*bi+af*ai*y-(bf*ai+af*bi)*x
        ry, rn = (m10/m00)**2, (m01/m11)**2
        if invert: ry,rn=1/ry,1/rn
        return [rn,ry]
    pr_source = Path("knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md").read_text()
    pr_pdf = Path(re.search(r'^raw_file:\s*"?(.+?)"?$', pr_source, re.M)[1])
    out["pr134_conditional_forward"] = {
        "source": str(pr_pdf), "sha256": hashlib.sha256(pr_pdf.read_bytes()).hexdigest(),
        "locator": "printed112502-3 TableI/Eqs4-5",
        "experiment_R_17ny_17y_18ny": [.3,.6,.22],
        "printed_errors_17ny_17y_18ny": [.1,.1,.09],
        "experiment_18y_upper_bound": .08, "bound_likelihood": None,
        "original_model_R": [.33,.70,.17,.062],
        "assumptions": "fixed original alphas, positive b; common symmetric real forward Q; invert 17->15 for continuous-band identity",
        "examples": [
            {"x_q12_over_q1":x,"y_q2_over_q1":y,
             "R_17ny_17y_18ny_18y":ratios(.118,.894,x,y,True)+ratios(.099,.427,x,y,False)}
            for x,y in [(0,.5),(.04,.73),(.08,1)]
        ],
        "chi_square": None, "confidence_interval": None,
        "interpretation": "partial observable degeneracy only; equal diagonal Q is not chiral geometry or an equal-shape measurement",
    }
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__ == "__main__":
    main()
