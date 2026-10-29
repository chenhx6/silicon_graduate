#!/usr/bin/env python3
"""AMR two-identical-fermion limits and finite-range interaction diagnostic.

The angular-momentum selection rule is exact for two identical particles in a
single half-integer-j orbit: exchange gives (-1)^(2j-J), so antisymmetry keeps
the even J values here.  The distance-dependent Coulomb and short-range terms
are deliberately labelled an effective geometry diagnostic; they are not
substitutes for a full jj-coupled two-body matrix-element calculation.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path


def allowed_pair_J(j_twice: int) -> list[int]:
    j = j_twice / 2
    return [J for J in range(0, int(2 * j) + 1) if (int(2 * j) - J) % 2 == 1]


def effective_potentials(theta_deg: float, radius_fm: float = 4.6,
                        width_fm: float = 2.0, nuclear_range_fm: float = 1.2,
                        nuclear_depth_MeV: float = 35.0) -> dict[str, float]:
    theta = math.radians(theta_deg)
    separation = 2.0 * radius_fm * math.sin(theta)
    coulomb = 1.4399764 / math.sqrt(width_fm**2 + separation**2)
    nuclear = -nuclear_depth_MeV * math.exp(-0.5 * (separation / nuclear_range_fm) ** 2)
    return {"theta_deg": theta_deg, "separation_fm": separation,
            "V_coulomb_MeV": coulomb, "V_short_range_MeV": nuclear,
            "V_total_MeV": coulomb + nuclear}


def main() -> None:
    outdir = Path(__file__).parent
    proton_J = allowed_pair_J(9)
    neutron_J = allowed_pair_J(11)
    rows = [effective_potentials(theta) for theta in range(0, 91, 5)]
    result = {
        "status": "provisional effective interaction diagnostic",
        "exchange_rule": "P12 |(jj)JM> = (-1)^(2j-J) |(jj)JM>; antisymmetry requires this phase = -1",
        "proton_pair": {"orbit": "g9/2", "j": 4.5, "allowed_J": proton_J, "J_max_hbar": max(proton_J)},
        "neutron_pair": {"orbit": "h11/2", "j": 5.5, "allowed_J": neutron_J, "J_max_hbar": max(neutron_J)},
        "valence_limit": {
            "J_val_max_hbar": max(proton_J) + max(neutron_J),
            "coupling": "J_p=8 plus J_n=10 gives J_val=18; classical 2*(9/2)+2*(11/2)=20 ignores Pauli pair truncation",
            "note": "The 18 hbar limit applies to the four-valence-particle single-j truncation, before core rotation and configuration mixing.",
        },
        "effective_geometry": {
            "V_C": "e^2/sqrt(a^2+d(theta)^2)",
            "V_short": "-V0 exp[-d(theta)^2/(2 s_N^2)]",
            "d": "2 r sin(theta)",
            "parameters": {"r_fm": 4.6, "a_fm": 2.0, "s_N_fm": 1.2, "V0_MeV": 35.0},
            "warning": "These distance terms illustrate finite-density renormalization; V_J requires radial wavefunctions and antisymmetrized jj-coupled matrix elements.",
        },
        "rows": rows,
    }
    (outdir / "amr_fermion_pair_limits.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    with (outdir / "amr_fermion_pair_limits.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print("allowed proton J:", proton_J)
    print("allowed neutron J:", neutron_J)
    print("J_val_max:", max(proton_J) + max(neutron_J), "hbar")


if __name__ == "__main__":
    main()
