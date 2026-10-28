"""Calculations from printed BU16/BU17 values; no new experimental fit or CI."""
import json
import math
from pathlib import Path


def weisskopf(a, rank):
    """One electric W.u. in e^2 fm^(2*rank), R=1.2 A^(1/3) fm."""
    return (3 / (rank + 3)) ** 2 * (1.2 * a ** (1 / 3)) ** (2 * rank) / (4 * math.pi)


rows = []
for a, lower, upper, published in [(144, .23, .17, [48, 34, 25]), (146, .20, .14, [48, 29, 21])]:
    matrix = .65  # e b^(3/2); magnitude applies to both directions
    wu_b3 = weisskopf(a, 3) / 1e6
    b_down = matrix ** 2 / 7
    rows.append({
        "A": a, "matrix_e_b_3over2": matrix,
        "matrix_printed_interval": [matrix-lower, matrix+upper],
        "B_3to0_e2b3": b_down, "B_0to3_e2b3": matrix**2,
        "one_Wu_e2fm6": weisskopf(a, 3), "B_3to0_Wu_from_rounded_matrix": b_down/wu_b3,
        "first_order_Wu_errors_lower_upper": [2*matrix*lower/7/wu_b3, 2*matrix*upper/7/wu_b3],
        "squared_matrix_endpoint_range_Wu": [(matrix-lower)**2/7/wu_b3, (matrix+upper)**2/7/wu_b3],
        "published_B_Wu_central_lower_upper": published,
        "boundary": "Printed rounded inputs; first-order errors and squared endpoints differ. Neither reconstructs the original joint likelihood or supplies a new confidence interval."
    })

e1_exp, e1_model = .000223, .00474  # e b^(1/2), BU17 Table I
e1_b_down = e1_exp**2/3
result = {
    "schema_version": 1,
    "source_locators": ["BU16 printed112503-1/4 Table I", "BU17 arXiv PDF3 Table I"],
    "E3": rows,
    "E1_146Ba": {
        "experimental_matrix_e_b_half": e1_exp,
        "SCCM_matrix_e_b_half": e1_model,
        "model_to_experiment_amplitude_ratio": e1_model/e1_exp,
        "model_to_experiment_strength_ratio": (e1_model/e1_exp)**2,
        "B_1to0_e2b": e1_b_down,
        "B_1to0_Wu": e1_b_down*100/weisskopf(146, 1),
        "rotor_D0_efm_conditional": e1_exp*10/math.sqrt(3/(4*math.pi)),
        "boundary": "Experimental E1 is primarily constrained by prior lifetime/branching information. D0 conversion assumes the axial K=0 rotor convention; no measured sign or independent CoulEx E1 experiment is implied."
    },
    "exclusions": ["no Gaussian significance from interval overlap", "no static/soft shape selection from one E3 strength", "no reconstruction of signed dipole contributions from v^2 alone"]
}
if __name__ == "__main__":
    destination = Path(__file__).with_suffix(".json")
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
