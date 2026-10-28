#!/usr/bin/env python3
"""Reproducible Cline-style octupole invariant and softness controls.

This is a transparent closure/sum-rule calculator, not a GOSIA replacement.
It accepts laboratory reduced matrix elements, applies the stated
Wigner-Eckart B(Elambda) convention, and reports what can and cannot be
inferred from a finite transition list.  No external packages are required.

The axial convention used here is

    I3 = <Q3 . Q3> = 7/(16*pi) * Q30**2,

where Q30 is the conventional intrinsic electric moment in e fm^3.  For a
0+ -> 3- transition the rotor relation gives
    |<3-||M(E3)||0+>| = sqrt(I3),
so the quoted RME in e b^(3/2) is multiplied by 1000 to obtain e fm^3.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from typing import Dict, Iterable, List

FACTOR_3 = 7.0 / (16.0 * math.pi)
EB32_TO_EFM3 = 1000.0


def b_value(rme: float, ji: float) -> float:
    """B(Elambda; Ji -> Jf) from a reduced matrix element."""
    return rme * rme / (2.0 * ji + 1.0)


def closure_term(rme: float, ji: float) -> float:
    """Contribution to <i|M^dagger.M|i> for one complete final-state term."""
    # With the stated Wigner-Eckart convention this is the upward B value.
    return b_value(rme, ji)


def axial_q30_from_rme_0_to_3(rme_eb32: float) -> float:
    """Rotor-convention Q30 (e fm^3) inferred from a 0+ -> 3- RME."""
    rme_efm3 = rme_eb32 * EB32_TO_EFM3
    return rme_efm3 / math.sqrt(FACTOR_3)


def axial_invariant_from_q30(q30_efm3: float) -> float:
    return FACTOR_3 * q30_efm3 * q30_efm3


def harmonic_q3(B3: float, C3: float, hbar: float = 1.0) -> Dict[str, float]:
    """Ground-state moments of x for H=p^2/(2B3)+C3*x^2/2."""
    if B3 <= 0 or C3 <= 0 or hbar <= 0:
        raise ValueError("B3, C3 and hbar must be positive")
    q2 = hbar / (2.0 * math.sqrt(B3 * C3))
    q4 = 3.0 * q2 * q2
    return {
        "B3": B3,
        "C3": C3,
        "hbar": hbar,
        "omega3": math.sqrt(C3 / B3),
        "zero_point_energy": 0.5 * hbar * math.sqrt(C3 / B3),
        "mean_Q30": 0.0,
        "mean_Q30_sq": q2,
        "mean_Q30_fourth": q4,
        # This is Var(Q30^2), often denoted sigma^2(Q3) in the requested
        # statement; it is not Var(Q30), which equals q2 for this oscillator.
        "variance_Q30_sq": q4 - q2 * q2,
        "invariant_Q3_sq": FACTOR_3 * q2,
        "invariant_Q3_sq_variance": FACTOR_3 * FACTOR_3 * (q4 - q2 * q2),
    }


def intrinsic_quadrupole_controls(q2: float, delta_deg: float, q3: float) -> Dict[str, float]:
    """Canonical intrinsic scalar controls used by Cline-style reconstructions."""
    delta = math.radians(delta_deg)
    return {
        "Q2_sq": q2 * q2,
        "Q2_cube_cos3delta": q2**3 * math.cos(3.0 * delta),
        "Q3_sq": q3 * q3,
        "Q2_Q3_sq": q2 * q3 * q3,
    }


def finite_closure(rows: Iterable[Dict[str, float]]) -> Dict[str, float]:
    rows = list(rows)
    total = sum(closure_term(r["rme_efm3"], r["Ji"]) for r in rows)
    return {
        "observed_transition_terms": len(rows),
        "finite_sum_I3_efm6": total,
        "closure_status": "partial unless all final states and couplings are supplied",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    out = args.out_dir
    out.mkdir(parents=True, exist_ok=True)

    # Inputs are reported central values from the source pages.  146Ba Q30 is
    # deliberately derived under the common axial convention; the source page
    # reports the RME/B(E3), while the 144Ba page reports Q3 explicitly.
    measured = [
        {"nucleus": "144Ba", "transition": "0+ -> 3-", "Ji": 0.0,
         "rme_eb32": 0.65, "rme_efm3": 650.0,
         "rme_uncertainty_eb32": "+0.17/-0.23", "source_locator": "Bucher 2016 PDF pp.3-4, Table I"},
        {"nucleus": "146Ba", "transition": "0+ -> 3-", "Ji": 0.0,
         "rme_eb32": 0.65, "rme_efm3": 650.0,
         "rme_uncertainty_eb32": "+0.14/-0.20", "source_locator": "Bucher 2017 PDF pp.2-3, Table I"},
        {"nucleus": "224Ra", "transition": "0+ -> 3-", "Ji": 0.0,
         "rme_eb32": 0.940, "rme_efm3": 940.0,
         "rme_uncertainty_eb32": "source reports 940(30) e fm^3", "source_locator": "Gaffney 2013 PDF pp.2-4, Tables 1-2"},
    ]
    rows: List[Dict[str, object]] = []
    for item in measured:
        q30_derived = axial_q30_from_rme_0_to_3(item["rme_eb32"])
        I3 = axial_invariant_from_q30(q30_derived)
        rows.append({
            **item,
            "B_down_efm6": b_value(item["rme_efm3"], 3.0),
            "B_up_or_closure_efm6": closure_term(item["rme_efm3"], item["Ji"]),
            "Q30_derived_efm3": q30_derived,
            "I3_Q3sq_efm6": I3,
            "closure_warning": "one observed 0+->3- term; no complete negative-parity closure",
        })

    # A strict rotor check using the explicitly reported 144Ba Q3 and 224Ra Q3.
    reported_q3 = [
        {"nucleus": "144Ba", "Q30_efm3": 1730.0, "uncertainty": "+450/-620", "locator": "Bucher 2016 PDF p.4"},
        {"nucleus": "224Ra", "Q30_efm3": 2520.0, "uncertainty": "90", "locator": "Gaffney 2013 PDF Table 2"},
    ]
    rotor_checks = []
    for item in reported_q3:
        rotor_checks.append({
            **item,
            "I3_efm6": axial_invariant_from_q30(item["Q30_efm3"]),
            "equivalent_0_to_3_rme_efm3": math.sqrt(axial_invariant_from_q30(item["Q30_efm3"])),
        })

    dynamic = harmonic_q3(B3=1.0, C3=1.0, hbar=1.0)
    static_control = {"Q30_efm3": 1730.0, "mean_Q30": 1730.0,
                      "mean_Q30_sq": 1730.0**2, "mean_Q30_fourth": 1730.0**4,
                      "variance_Q30_sq": 0.0,
                      "invariant_Q3_sq": axial_invariant_from_q30(1730.0)}
    quadrupole = intrinsic_quadrupole_controls(q2=1.0, delta_deg=20.0, q3=1.0)

    # 224Ra level audit: the adopted 4+ and 6+ ground-band levels are not
    # counted as two-octupole-phonon states.  The known 0+/2+ candidates do
    # not close a demonstrated 0,2,4,6 quartet around 2*E(3-).
    phonon_audit = {
        "224Ra": {
            "one_phonon_3minus_keV": 290.352,
            "harmonic_two_phonon_target_keV": 2.0 * 290.352,
            "adopted_candidates": [
                {"Jpi": "0+", "E_keV": 916.38, "status": "possible candidate; not a complete quartet"},
                {"Jpi": "2+", "E_keV": 965.65, "status": "possible gamma-band candidate in ENSDF; not assigned two-octupole"},
                {"Jpi": "4+", "E_keV": 250.782, "status": "ground-band member; exclude from two-phonon count"},
                {"Jpi": "6+", "E_keV": 479.12, "status": "ground-band member; exclude from two-phonon count"},
            ],
            "source_locator": "ENSDF 224Ra adopted levels, PDF pp.1-2",
        },
        "144Ba": {"status": "no closure-complete 0+,2+,4+,6+ octupole two-phonon set in the cited Bucher source"},
        "146Ba": {"status": "no closure-complete 0+,2+,4+,6+ octupole two-phonon set in the cited Bucher source"},
    }

    result = {
        "method": "Cline-style rotational invariants from laboratory reduced matrix elements",
        "conventions": {
            "B_definition": "B(Eλ; Ji→Jf)=|<Jf||M(Eλ)||Ji>|^2/(2Ji+1)",
            "I3_definition": "<Q3·Q3>=sum_f B(E3; i→f) for a complete closure sum",
            "axial_conversion": "I3=7/(16π) Q30^2; 0+→3- rotor RME=sqrt(I3)",
            "unit_conversion": "1 e b^(3/2)=1000 e fm^3",
            "dynamic_variance": "variance_Q30_sq=<Q30^4>-<Q30^2>^2; harmonic value=2< Q30^2 >^2",
        },
        "source_inputs": measured,
        "finite_closure_results": rows,
        "reported_q3_rotor_checks": rotor_checks,
        "static_control": static_control,
        "harmonic_zero_point_control": dynamic,
        "quadrupole_and_mixed_controls": quadrupole,
        "two_phonon_level_audit": phonon_audit,
        "evidence_boundary": [
            "The cited Ba experiments provide a strong 0+↔3- E3 term, not a closure-complete octupole invariant.",
            "Cline pp.697-700 warns that missing strength and operator/model assumptions grow in importance at higher invariant order.",
            "E1/E3 ratios are diagnostic only with common feeding, phase and efficiency treatment; E1 can cancel while E3 remains large.",
        ],
    }
    (out / "cline_octupole_invariants_results.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")

    with (out / "cline_octupole_invariants.csv").open("w", newline="") as handle:
        fields = ["nucleus", "transition", "rme_eb32", "rme_efm3", "B_up_or_closure_efm6", "B_down_efm6", "Q30_derived_efm3", "I3_Q3sq_efm6", "closure_warning"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row[key] for key in fields})

    readme = """# Cline octupole invariant worker

Run:

```bash
python3 cline_octupole_invariants.py --out-dir .
```

The JSON and CSV are derived from the central values in the Wiki source pages:

- `knowledge/sources/cline-1986-nuclear-shapes-coulomb-excitation.md` (PDF pp.697--700): finite closure, higher-order missing-strength and operator caveats;
- `knowledge/sources/bucher-2016-144ba-direct-octupole.md` (PDF pp.3--4, Table I);
- `knowledge/sources/bucher-2017-146ba-direct-octupole.md` (PDF pp.2--3, Table I);
- `knowledge/sources/gaffney-2013-pear-shaped-rn-ra.md` (PDF pp.2--4, Tables 1--2);
- ENSDF 224Ra adopted levels (`raw/papers/gpt/day26-20261028/nndc-224ra-adopted-cluster-20261029.pdf`, pp.1--2).

The script is a transparent algebraic control. It does not claim a complete
GOSIA fit or a measured closure sum when the source supplies only one E3 link.
"""
    (out / "README.md").write_text(readme)


if __name__ == "__main__":
    main()
