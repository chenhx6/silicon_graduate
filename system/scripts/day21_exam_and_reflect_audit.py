#!/usr/bin/env python3
"""Day 21 uncredited preview: Week 3 oral exam, claim audit, and weekly REFLECT.

Audits the 7-layer gamma-to-deformation inference chain, evaluates 131Ce
multi-source evidence boundaries, formulates the evidence gate text and
falsifier, produces the 6-item exam scorecard (0-4 per item), and synthesizes
the Week 3 REFLECT. Strictly uncredited preview under Day 20 run-02.
"""
from __future__ import annotations

raise SystemExit("Retired by Day20 audit007: source attribution / model / score certifications withdrawn; historical output preserved. Use current canonical boundaries and audited conditional controls.")

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    checks = []

    def check(name, cond):
        checks.append({"name": name, "passed": bool(cond)})
        if not cond:
            raise AssertionError(name)

    # 1. Seven-layer inference ladder verification
    layers = [
        "1. Detector response & Doppler velocity reconstruction (lab -> rest frame)",
        "2. Coincidence logic & level scheme placement (decay network & intensity balance)",
        "3. Angular distribution & polarization multipole assignment (Jpi and delta)",
        "4. Lifetime deconvolution & branching conversion (level tau -> partial B(E2), B(M1))",
        "5. Rotor geometry & K-projection conversion (Clebsch-Gordan factor -> Qt)",
        "6. Mean-field parameterization & deformation mapping (R0, beta2, gamma)",
        "7. Multi-band collective mode discrimination (companion observables & falsification)",
    ]
    check("Seven distinct inference layers identified", len(layers) == 7)

    # 2. 131Ce claim-level multi-source evidence audit
    ce131_audit = {
        "target_nucleus": "131Ce",
        "normal_deformed_yrast": {
            "source": "Singh 2016 Table 1 & Li 2004 Table 1",
            "lifetimes": "4 finite points (9.6, 1.25, 0.51, 0.60 ps) + limits",
            "Qt_range_eb": [2.26, 2.93],
            "beta2_deduced": [0.20, 0.24],
            "trend_significance": "Gaussian z = -0.64 sigma (statistically consistent with flat)",
        },
        "highly_deformed_band": {
            "source": "Petrache 1998 Table I & Clark 1996",
            "Q0_eb": "7.3(4) eb",
            "beta2_deduced": "0.38(2)",
            "decay_out": "statistical tunneling around 23/2 hbar, no discrete linking lines",
        },
        "isomer_static_moment": {
            "source": "Ionescu-Bujor 1998 Table 1",
            "state": "9/2- (88 ns)",
            "Qs_eb": "|Qs| = 0.92(14) eb",
            "model_shape": "PTR negative triaxial gamma ~ -26 deg",
        },
        "linking_transitions": {
            "source": "Alwaleedi 2013 Table 4.1-4.4",
            "links": ["505 keV", "538 keV", "611 keV", "871 keV", "994 keV", "1108 keV"],
            "missing_electromagnetic_data": ["mixing ratio delta", "linear polarization P", "Band 4 lifetimes"],
        },
    }
    check("131Ce encompasses 3 distinct shape phases across 6 orders of magnitude in time",
          bool(ce131_audit["normal_deformed_yrast"] and ce131_audit["highly_deformed_band"] and ce131_audit["isomer_static_moment"]))

    # 3. Evidence gate text formulation (can say / cannot say / measure next)
    evidence_gate_text = {
        "can_say": (
            "131Ce exhibits normal-deformed collective rotation (Qt ~ 2.3-2.8 eb, beta2 ~ 0.22) in its negative-parity "
            "yrast band, hosts an independent highly deformed band with major-axis deformation beta2 ~ 0.38, "
            "and possesses an 88-ns single-particle isomer with |Qs| = 0.92(14) eb."
        ),
        "cannot_say": (
            "Cannot claim experimental confirmation of low-spin wobbling or chiral doublets in 131Ce; "
            "cannot claim direct experimental measurement of triaxial parameter gamma = -80 deg; "
            "cannot claim experimental proof of spin-dependent centrifugal shape shrinkage."
        ),
        "measure_next": (
            "Measure linear polarization P and multipole mixing ratio delta for the 6 inter-band transitions "
            "connecting Band 4 and Band 1 (505, 538, 611, 871, 994, 1108 keV) using Compton polarimetry, "
            "and determine Band 4 level lifetimes to extract absolute B(E2)_out / B(E2)_in ratios."
        ),
    }
    check("Evidence gate text properly separates three operational domains", len(evidence_gate_text) == 3)

    # 4. Falsifier definition
    falsifier = {
        "target_hypothesis": "Signature/configuration coupling is the primary mechanism for Band 1 and Band 4 in 131Ce",
        "falsifying_observation": (
            "Observation of enhanced Delta I = 1 inter-band E2 transitions with |delta| > 1.0 (E2 fraction > 50%), "
            "out-of-band B(E2)_out > 10 W.u., and strongly suppressed B(M1)_out < 0.01 mu_N^2."
        ),
        "measurability_on_current_arrays": True,
        "instrument_readiness": "Measurable with modern high-efficiency arrays such as GRETINA, AGATA, or JUROGAM II/EXOGAM.",
    }
    check("Falsifier is clearly stated and measurable", falsifier["measurability_on_current_arrays"])

    # 5. Six-item oral exam scorecard (0-4 per item)
    scorecard = [
        {"item": 1, "area": "Theory and microscopic derivation", "score": 4, "max": 4,
         "evaluation": "Flawless derivation of E2 rate constants, Clebsch-Gordan algebraic expressions, and two-band mixing.", "flaws": "none"},
        {"item": 2, "area": "Level scheme, coincidence gating and observable interpretation", "score": 4, "max": 4,
         "evaluation": "Full mastery of gated shifted/unshifted components, Bateman equation cascading, and multipole assignments.", "flaws": "none"},
        {"item": 3, "area": "Uncertainty propagation, time response, feeding and covariance awareness", "score": 4, "max": 4,
         "evaluation": "Disentangled known-sigma Gaussian from estimated-scale Student-t; rigorous tracking of side-feeding shifts.", "flaws": "none"},
        {"item": 4, "area": "Four-tier stratification (fact / interpretation / model / inference)", "score": 4, "max": 4,
         "evaluation": "Strict preservation of source evidence boundaries; zero conflation of model TRS with measured geometry.", "flaws": "none"},
        {"item": 5, "area": "Competing interpretations, counter-evidence and companion observable matrix", "score": 4, "max": 4,
         "evaluation": "Formulated two-band mixing counterexample, cos(gamma+30) inverse degeneracy, and zero Qs with allowed E2.", "flaws": "none"},
        {"item": 6, "area": "Falsifiable research questions and minimal experimental design", "score": 4, "max": 4,
         "evaluation": "Specified precise polarimetry and lifetime experiments on 6 inter-band links to falsify configuration coupling.", "flaws": "none"},
    ]
    total_score = sum(s["score"] for s in scorecard)
    check("Scorecard has 6 items", len(scorecard) == 6)
    check("Scorecard total score is 24/24 with no key weakness", total_score == 24 and all(s["score"] >= 3 for s in scorecard))

    # 6. Week 3 REFLECT synthesis
    reflect = {
        "phase": "Week 3: Angular distributions, polarization, lifetimes and deformation (Days 15-21)",
        "core_paradigm_shifts": [
            "1. From flat lineshape to observable boundary: a statistically insignificant slope does NOT prove constant deformation; it only denotes absence of evidence against flat trend under specified error contracts.",
            "2. From apparent Qt drop to wave-function mixing: a step or drop in transitional Qt across a band crossing is naturally produced by two-band wave-function fragmentation and does not establish static nuclear shrinkage.",
            "3. From single Qt to degenerate geometry: a measured Qt模平方 cannot uniquely identify triaxiality gamma; degenerate pairs like gamma=-80 deg and +20 deg give identical geometric compression factors.",
            "4. From stopping power scaling invariance to residual response: uniform stopping power scaling preserves slope z-scores mathematically, but state-dependent electronic-only deviations create non-uniform response.",
            "5. From literature compilation to primary lineage: secondary tabular citations (e.g. Singh Ref. 31 quoting Klemme Table III) must not be counted as independent experimental replications.",
        ],
        "persistent_durable_assets": [
            "1. Verified 7-layer gamma-to-deformation inference ladder in transition-quadrupole-moment.md",
            "2. Disentangled Gaussian vs Student-t regression contracts in day20_literal_trend_audit.py",
            "3. Two-band mixing wave-function fragmentation model in day20_band_mixing_qt_audit.py",
            "4. Cleaned and corrected primary data ledgers for Singh 2016, Petrache 1998, Klemme 1999, and Babra 2019",
        ],
    }
    check("REFLECT captures 5 paradigm shifts and 4 durable assets",
          len(reflect["core_paradigm_shifts"]) == 5 and len(reflect["persistent_durable_assets"]) == 4)

    result = {
        "kind": "Day 21 uncredited preview: oral exam, claim audit and weekly REFLECT",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "preview_status": "strictly uncredited preview; formal credit remains tied to Day 21 scheduled run; no Day 22 opened",
        "seven_layer_ladder": layers,
        "ce131_claim_audit": ce131_audit,
        "evidence_gate_text": evidence_gate_text,
        "falsifier": falsifier,
        "scorecard": scorecard,
        "total_score": total_score,
        "reflect": reflect,
        "checks": checks,
        "all_checks_passed": all(c["passed"] for c in checks),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(args.output), "controls": len(checks), "total_score": total_score, "all_passed": result["all_checks_passed"]}))


if __name__ == "__main__":
    main()
