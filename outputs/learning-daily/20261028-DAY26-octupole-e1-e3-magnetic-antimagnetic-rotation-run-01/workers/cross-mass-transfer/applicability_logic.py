#!/usr/bin/env python3
"""Transparent, conditional screening logic for cross-mass mode transfer.

This is a decision aid, not a classifier trained on nuclei. It deliberately
returns ``conditional`` when an input is missing; it never turns a review
summary or a model parameter into an experimental fact.
"""
from __future__ import annotations

import json
from pathlib import Path


def screen(*, beta2=None, has_high_j_blades=None, abs_lifetimes=False,
           has_absolute_bm1=False, has_absolute_be2=False,
           has_multiple_e3=False, has_parity_doublet=False,
           delta_i2_only=False, no_m1_observed=False,
           core_inertia_dominant=None, mirrored_shears=None):
    out = {
        "status": "conditional",
        "flags": [],
        "evidence_boundary": "missing inputs remain unresolved; no mode is certified",
    }
    if beta2 is not None and beta2 >= 0.30 and core_inertia_dominant is not False:
        out["flags"].append("strong-quadrupole-core: MR visibility is suppressed conditionally")
    if has_high_j_blades is False:
        out["flags"].append("angular-momentum-budget: continuous high-spin shears sequence is unlikely")
    if has_high_j_blades is None:
        out["flags"].append("angular-momentum-budget: unverified")
    if delta_i2_only and no_m1_observed:
        if mirrored_shears is True and abs_lifetimes and has_absolute_be2:
            out["flags"].append("AMR-supported: mirrored-shears inputs plus absolute E2/lifetime evidence")
        else:
            out["flags"].append("AMR-candidate-only: DeltaI=2/no-M1 is insufficient")
    if abs_lifetimes and has_absolute_bm1 and has_absolute_be2:
        out["flags"].append("MR-observable-closed: absolute M1/E2 and lifetime layer available")
    else:
        out["flags"].append("MR-strength-gap: absolute M1/E2 lifetime layer incomplete")
    if has_multiple_e3:
        out["flags"].append("octupole-discrimination-improved: multi-transition E3 pattern")
    elif has_parity_doublet:
        out["flags"].append("octupole-candidate-only: parity doublet/E1 is not static-shape proof")
    return out


def main():
    cases = {
        "A80_light_high_spin": screen(has_high_j_blades=None),
        "A105_AMR_candidate": screen(delta_i2_only=True, no_m1_observed=True,
                                      mirrored_shears=True, abs_lifetimes=False,
                                      has_absolute_be2=False),
        "A160_strong_ER_control": screen(beta2=0.33, core_inertia_dominant=True,
                                          has_high_j_blades=True),
        "A190_Pb_MR_with_crossing": screen(beta2=0.10, has_high_j_blades=True,
                                           abs_lifetimes=True,
                                           has_absolute_bm1=True,
                                           has_absolute_be2=True),
        "A220_multi_E3": screen(has_multiple_e3=True),
    }
    payload = {
        "schema": "cross-mass-transfer-screen-v1",
        "status": "conditional-screening-only",
        "source_note": "knowledge/research-notes/cross-mass-region-collective-mode-mechanisms-and-breakdown.md",
        "cases": cases,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
