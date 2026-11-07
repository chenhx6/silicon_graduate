#!/usr/bin/env python3
"""Nominal finite differences of the verified Görgen 2004 Tables I/II.

These are derived observables, not a new fit or a unique wobbling assignment.
No energy uncertainty or covariance was supplied in those tables.
"""

import csv
import hashlib
import json
import platform
import sys
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "raw/papers/gpt/query/20261108-r2-g42-inertia-observables/gorgen2004-inputs-parent-verified.csv"
PAPER = ROOT / "raw/papers/gpt/query/20261107-continuation-G23/gorgen-2004-163lu-quadrupole-moments-prc.pdf"
OUT = ROOT / "outputs/l4/20261108-band-response-definitions"
PAPER_SHA = "5dbf88f286183ac22cd762e4f22a69e778d64f59e78f4cbc7533c85589ed992e"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def calculate(rows):
    bands = {}
    for row in rows:
        row = dict(row)
        row["spin"] = float(Fraction(row["spin_initial"].rstrip("+")))
        row["energy"] = float(row["energy_kev"])
        row["be2"] = float(row["be2_e2b2"])
        bands.setdefault(row["band"], []).append(row)
    results = []
    for name in ("TSD1", "TSD2"):
        band = bands[name]
        for index, row in enumerate(band):
            spin, energy = row["spin"], row["energy"] / 1000
            final = float(Fraction(row["spin_final"].rstrip("+")))
            assert spin - final == 2
            result = {
                "kind": "inband",
                "band": name,
                "parent_spin": spin,
                "photon_mid_spin": spin - 1,
                "energy_kev": row["energy"],
                "hbar_omega_mev": energy / 2,
                "J1_midpoint_hbar2_per_mev": 2 * (spin - 1) / energy,
                "J1_quantum_hbar2_per_mev": (2 * spin - 1) / energy,
            }
            if index:
                previous = band[index - 1]
                assert spin - previous["spin"] == 2
                difference = row["energy"] - previous["energy"]
                assert difference > 0
                result.update(
                    J2_center_spin=spin - 2,
                    J2_center_hbar_omega_mev=(row["energy"] + previous["energy"]) / 4000,
                    J2_hbar2_per_mev=4000 / difference,
                )
            results.append(result)
    base = {r["spin"]: r for r in bands["TSD1"]}
    excited = {r["spin"]: r for r in bands["TSD2"]}
    for row in bands["TSD2_to_TSD1"]:
        spin = row["spin"]
        assert spin - float(Fraction(row["spin_final"].rstrip("+"))) == 1
        reference = base[spin + 1]
        results.append(
            {
                "kind": "interband",
                "band": row["band"],
                "parent_spin": spin,
                "energy_kev": row["energy"],
                "reference_parent_spin": spin + 1,
                "reference_energy_kev": reference["energy"],
                "interband_midpoint_energy_kev": row["energy"] - reference["energy"] / 2,
                "same_parent_BE2_out_in": row["be2"] / excited[spin]["be2"],
            }
        )
    return results


def main():
    assert sha(PAPER) == PAPER_SHA
    with INPUT.open(newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == 20
    results = calculate(rows)
    # An exact quantum rotor has E_gamma=A(4I-2), hence both quantum J1
    # and the adjacent-edge J2 return 1/(2A). The midpoint convention differs.
    rotor_a = 0.01
    spins = [20.5, 22.5, 24.5]
    energies = [rotor_a * (4 * spin - 2) for spin in spins]
    quantum = [(2 * spin - 1) / e for spin, e in zip(spins, energies)]
    j2_rotor = [4 / (b - a) for a, b in zip(energies, energies[1:])]
    interband = [r for r in results if r["kind"] == "interband"]
    # These checks use source-labelled inputs and independent analytic limits.
    checks = {
        "published_table_rows_and_spin_paths": len(results) == 20,
        "quantum_rotor_limit": all(abs(x - 50) < 1e-10 for x in quantum + j2_rotor),
        "source_labelled_first_energy": rows[0]["energy_kev"] == "578.6",
        "interband_reference_labels": [r["reference_parent_spin"] for r in interband]
        == [24.5, 26.5, 28.5, 30.5, 32.5],
        "interband_arithmetic": all(
            abs(r["interband_midpoint_energy_kev"] - expected) < 1e-9
            for r, expected in zip(interband, [310.4, 296.9, 284, 272.25, 261.45])
        ),
    }
    assert all(checks.values()), checks
    OUT.mkdir(parents=True, exist_ok=True)
    result_path = OUT / "derived-observables.json"
    result_path.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n")
    provenance = {
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "command": "python3 system/scripts/doctoral_r2_gorgen_band_response.py",
        "script_sha256": sha(Path(__file__)),
        "python": sys.version,
        "platform": platform.platform(),
        "inputs": [
            {"path": str(INPUT.relative_to(ROOT)), "sha256": sha(INPUT)},
            {"path": str(PAPER.relative_to(ROOT)), "sha256": sha(PAPER)},
        ],
        "artifacts": [{"path": str(result_path.relative_to(ROOT)), "sha256": sha(result_path)}],
        "units": "energy keV or MeV as labelled; spin number in hbar; inertia hbar^2/MeV",
        "checks": checks,
        "boundaries": [
            "Nominal transforms of rounded tables; output digits are not measurement precision",
            "No energy covariance or uncertainty available; no confidence intervals calculated",
            "Ew is a declared interband midpoint energy, not an independent mode identification",
            "BE2 ratio uses a common parent; no independent-lifetime uncertainty assumption",
        ],
    }
    (OUT / "run-provenance.json").write_text(
        json.dumps(provenance, ensure_ascii=False, indent=2) + "\n"
    )
    print(json.dumps({"rows": len(results), "checks": checks}))


if __name__ == "__main__":
    main()
