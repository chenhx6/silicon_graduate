#!/usr/bin/env python3
"""Reproduce the 2019 Garg et al. polarization-asymmetry erratum table.

The values are printed central values from the erratum, not a reanalysis of
the underlying coincidence counts.  The audit records the change at the two
mixed transitions that had driven the earlier concern.
"""
import json
from pathlib import Path


ROWS = [
    {"E_gamma_keV": 747.5, "old": -0.05, "old_sigma": 0.03, "new": 0.03, "new_sigma": 0.03, "multipolarity": "M1 + E2"},
    {"E_gamma_keV": 813.3, "old": -0.20, "old_sigma": 0.08, "new": 0.04, "new_sigma": 0.03, "multipolarity": "M1 + E2"},
]


def main():
    correction = lambda energy: 1.01229 + 1.17083e-6 * energy
    for row in ROWS:
        row["a_Egamma"] = correction(row["E_gamma_keV"])
        row["delta_new_minus_old"] = row["new"] - row["old"]
    output = {
        "schema": "pr135-erratum-audit-041/v1",
        "evidence_status": "direct-erratum-table-central-values",
        "source": "Garg et al., Phys. Rev. C 100, 069901(E) (2019), Table I p.1",
        "raw_sha256": "c9fbed8bb0a1463c6d083f29e1331ff72102f5fb4edfdd96b76f3c5c0149db30",
        "erratum_pages": 2,
        "correction_factor": "a(Egamma)=1.01229+(1.17083e-6)Egamma_keV",
        "rows": ROWS,
        "interpretation_boundary": {
            "direct_change": "The 747.5 and 813.3 keV lines are assigned mixed M1+E2 character after energy-dependent asymmetry correction.",
            "old_813_claim": "The old -0.20(8) polarization asymmetry is replaced by +0.04(3); the old value must not be used as a current M1-purity discriminator.",
            "author_scope": "The erratum states that the earlier results and interpretations are not affected; it does not provide absolute lifetimes or absolute B(M1).",
            "not_done": "No raw-count likelihood, covariance reconstruction, or independent re-fit was performed."
        },
        "checks": {
            "813_old_to_new_shift": ROWS[1]["delta_new_minus_old"],
            "both_mixed": all(row["multipolarity"] == "M1 + E2" for row in ROWS),
            "no_absolute_lifetime_claim": True
        }
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(output, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
