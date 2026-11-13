"""Independent single-j Fock-space checks of seniority-conserving E2 scaling.

The operator is dimensionless T20=sum_m[3m^2-j(j+1)] n_m.  A highest-weight
two-particle J=2j-1 state is raised with the actual fermionic J=0 pair operator.
This checks a diagonal E2 matrix element at fixed J,M, and therefore its RME
particle-number factor. It is not a lifetime, a measured B(E2), or a complete
check of every transition and generalized-seniority model.
"""

import argparse
import json
import math
from pathlib import Path


def create(mask, orbital):
    if mask & (1 << orbital):
        return None
    sign = -1 if (mask & ((1 << orbital) - 1)).bit_count() % 2 else 1
    return mask | (1 << orbital), sign


def raise_pair(state, omega):
    # Orbitals are ordered m=-j,...,+j; rightmost creation acts first.
    j = omega - 0.5
    result = {}
    for mask, amplitude in state.items():
        for plus in range(omega, 2 * omega):
            m = plus - j
            minus = 2 * omega - 1 - plus
            first = create(mask, minus)
            if first is None:
                continue
            second = create(first[0], plus)
            if second is None:
                continue
            phase = (-1) ** round(j - m)
            outmask, sign = second
            result[outmask] = (
                result.get(outmask, 0.0) + amplitude * first[1] * sign * phase
            )
    result = {mask: amp for mask, amp in result.items() if abs(amp) > 1e-13}
    norm = math.sqrt(sum(amp * amp for amp in result.values()))
    if norm == 0:
        return {}
    return {mask: amp / norm for mask, amp in result.items()}


def expectation(state, omega):
    j = omega - 0.5
    weights = [3 * (orbital - j) ** 2 - j * (j + 1) for orbital in range(2 * omega)]
    return sum(
        amplitude**2
        * sum(weight for orbital, weight in enumerate(weights) if mask & (1 << orbital))
        for mask, amplitude in state.items()
    )


def run():
    cases = []
    for omega in (5, 6):
        # c†_j c†_(j-1)|vac> has maximal allowed two-particle M=J=2j-1.
        state = {(1 << (2 * omega - 1)) | (1 << (2 * omega - 2)): 1.0}
        reference = expectation(state, omega)
        rows = []
        for n in range(2, 2 * omega, 2):
            assert state and all(mask.bit_count() == n for mask in state)
            value = expectation(state, omega)
            ratio = value / reference
            expected = (omega - n) / (omega - 2)
            assert math.isclose(ratio, expected, abs_tol=1e-12)
            rows.append(
                {
                    "n": n,
                    "sparse_fock_components": len(state),
                    "T20_expectation": value,
                    "ratio_to_two_particles": ratio,
                    "seniority_formula_ratio": expected,
                }
            )
            state = raise_pair(state, omega)
        assert not state  # Multiplet exhausted; no extension to arbitrary n.
        cases.append({"omega": omega, "j": omega - 0.5, "v": 2, "rows": rows})
    return {
        "kind": "task-owned-independent-fermion-algebra-control",
        "operator": "dimensionless T20=sum_m (3m²-j(j+1)) n_m",
        "method": "Anticommuting fermion creation in a sparse single-j Fock basis",
        "cases": cases,
        "scope": "Diagonal E2 RME particle-number factor at fixed J,M in v=2 multiplets",
        "boundary": "No nucleus fit, physical quadrupole scale, lifetime, or generalized-seniority claim",
        "verdict": "pass",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    text = json.dumps(run(), ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
