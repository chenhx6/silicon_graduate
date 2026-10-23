"""Exact finite-moment witness in a declared commuting shape distribution.

No source data, nuclear Hamiltonian, experimental covariance or CI is used.
For five positive Q values, barycentric weights annihilate powers of X=Q^2
through degree3. Choose C=cos(3*delta)=Q_min^3/Q^3, in the physical chart.
Perturbed positive probabilities preserve six selected E2 scalar moments.
"""

import argparse
from fractions import Fraction as F
from functools import reduce
import hashlib
import json
import math
from pathlib import Path


def construct(q, epsilon):
    if len(q) != 5 or len(set(q)) != 5 or min(q) <= 0:
        raise ValueError("Use five distinct positive amplitudes")
    x = [z*z for z in q]
    weights = [1 / math.prod(z-y for j, y in enumerate(x) if j != i)
               for i, z in enumerate(x)]
    denominator = math.lcm(*(w.denominator for w in weights))
    integers = [int(w*denominator) for w in weights]
    common = reduce(math.gcd, integers)
    integers = [z // common for z in integers]
    scale = min(q)**3
    cosine = [scale / z**3 for z in q]
    models = []
    for sign in [1, -1]:
        p = [F(1, 5)+sign*epsilon*h for h in integers]
        if min(p) <= 0 or sum(p) != 1:
            raise ValueError("Perturbation must preserve positive normalized weights")

        def moment(power, cosine_power=0):
            return sum(w*z**power*c**cosine_power
                       for w, z, c in zip(p, q, cosine))

        scalars = {"Q2": moment(2), "Q3C": moment(3, 1),
                   "Q4": moment(4), "Q5C": moment(5, 1),
                   "Q6_amplitude": moment(6), "Q6C2": moment(6, 2)}
        angles = [math.degrees(math.acos(float(c)))/3 for c in cosine]
        mean_angle = sum(float(w)*a for w, a in zip(p, angles))
        sd_angle = math.sqrt(sum(float(w)*(a-mean_angle)**2 for w, a in zip(p, angles)))
        models.append({"sign": sign, "probabilities_exact": list(map(str, p)),
                       "six_scalars_exact": {k: str(v) for k, v in scalars.items()},
                       "amplitude_Q3_exact": str(moment(3)),
                       "mean_C_exact": str(moment(0, 1)),
                       "variance_C_exact": str(moment(0, 2)-moment(0, 1)**2),
                       "mean_C": float(moment(0, 1)),
                       "variance_C": float(moment(0, 2)-moment(0, 1)**2),
                       "mean_delta_deg": mean_angle, "sd_delta_deg": sd_angle,
                       "eighth_amplitude_moment_exact": str(moment(8))})
    return {"scope": "Declared commuting positive shape distribution; not an actual nucleus or CI",
            "Q_values_exact": list(map(str, q)), "C_values_exact": list(map(str, cosine)),
            "epsilon_exact": str(epsilon), "integer_null_vector": integers,
            "null_polynomial_moments_degree0_to3_exact": [
                str(sum(F(h)*z**power for h, z in zip(integers, x))) for power in range(4)],
            "models": models,
            "six_scalar_differences_exact": {
                key: str(F(models[0]["six_scalars_exact"][key])-F(models[1]["six_scalars_exact"][key]))
                for key in models[0]["six_scalars_exact"]},
            "not_inferred": ["Actual experimental identifiability from all measured RMEs",
                             "Actual Ge/Ce/Nd shape distribution or rigidity",
                             "Any experiment or fit confidence interval",
                             "A unique nuclear wavefunction or Hamiltonian"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--q", nargs=5, default=["1", "2", "3", "4", "5"])
    parser.add_argument("--epsilon", default="1/600")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = construct(list(map(F, args.q)), F(args.epsilon))
    result["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    with args.output.open("x") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
