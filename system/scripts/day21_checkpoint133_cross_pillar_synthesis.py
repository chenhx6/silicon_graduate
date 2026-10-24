#!/usr/bin/env python3
"""Cross-pillar synthesis of experimental inference ladder and claim boundaries in 135Nd and related benchmarks."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'

def main():
    # Load prior results from checkpoints 127, 128, 129, 130, 131, 132
    f_127 = RUN / 'same-parent-covariance-scope-127.json'
    f_128 = RUN / 'chiral-model-domain-scope-128.json'
    f_129 = RUN / 'multispin-chiral-inversion-scope-129.json'
    f_130 = RUN / 'quadrupole-homomorphism-scope-130.json'
    f_131 = RUN / 'm1-staggering-antiphase-scope-131.json'
    f_132 = RUN / 'chiral-phonon-softening-scope-132.json'

    assert all(p.exists() for p in [f_127, f_128, f_129, f_130, f_131, f_132]), "Missing prerequisite checkpoint JSONs"

    d127 = json.loads(f_127.read_text())
    d128 = json.loads(f_128.read_text())
    d129 = json.loads(f_129.read_text())
    d130 = json.loads(f_130.read_text())
    d131 = json.loads(f_131.read_text())
    d132 = json.loads(f_132.read_text())

    synthesis = {
        "title": "Comprehensive Inference Ladder and Claim Boundary Synthesis (Day 21 Exam Milestone)",
        "case_studies": {
            "Case1_135Nd_vs_134Pr_Chirality_and_Quadrupole_Moments": {
                "core_question": "Can near-degeneracy and transition rates establish nuclear chirality over shape coexistence or band crossing?",
                "established_boundaries": [
                    "Energy near-degeneracy is insufficient (134Pr demonstrates 2-band crossing fakes near-degeneracy with 2-fold different intrinsic Qt).",
                    "Lifetime equality is unnecessary (135Nd demonstrates 2-fold lifetime difference due to E_gamma^5 energy and branch factors).",
                    "In-band Qt homomorphism (Qt ratio 0.9356 +- 0.0102, relative dispersion 1.09%) rules out large shape coexistence.",
                    "Lockstep quenching at 39/2- (drop factors 2.46 vs 2.57, ratio 1.043) rules out independent accidental band crossing.",
                    "In-band M1 in-phase staggering and interband strict antiphase staggering (r = -0.998) confirm the quantum signature of chiral doublets.",
                    "Energy splitting Delta E(I) softens monotonically by a factor of 4.39 (423.1 to 96.4 keV), agreeing within 20 keV with the full quantal PRM finite tunneling prediction (76 keV) and refuting symmetric V-shaped crossing."
                ],
                "quantitative_summary": {
                    "mean_Qt_ratio": d130["quadrupole_homomorphism_statistics"]["mean_Qt_ratio_B_over_A"],
                    "lockstep_quench_ratio": d130["lockstep_quenching_at_39_2"]["quench_factor_symmetry_ratio"],
                    "m1_antiphase_correlation_BandA": d131["staggering_phase_rules"]["linear_correlation_Delta_BandA_vs_out"],
                    "R_E2_growth_factor": d129["summary_findings"]["R_E2_growth_factor_31_to_37"],
                    "inferred_inband_delta_range": d129["summary_findings"]["inferred_inband_delta_range"],
                    "energy_softening_factor": d132["monotonic_phonon_softening"]["softening_factor"],
                    "exp_vs_prm_tunneling_39_2_keV": d132["monotonic_phonon_softening"]["total_softening_range_keV"][-1]
                }
            },
            "Case2_34Si_vs_35Si_Bubble_and_Spin_Orbit": {
                "established_boundaries": [
                    "Spectroscopic factor S from knockout reaction is a reaction model-dependent extraction, not a direct measurement of spatial charge density rho(r).",
                    "GCM dynamic fluctuations and finite proton charge radius fold the central bubble depletion parameter Fsat down to ~ 0.09.",
                    "2s1/2 proton removal has zero tensor monopole matrix element (l=0); neutron 2p splitting reduction is carried entirely by two-body spin-orbit force."
                ]
            },
            "Case3_135Pr_Wobbling_and_Multipole_Double_Roots": {
                "established_boundaries": [
                    "Angular distribution yields small and large roots for delta; model preferences must not select the large root.",
                    "Joint linear polarization (Lv 2022) established the small root (|delta| ~ 0.15), confirming M1 dominance and ruling out transverse wobbling."
                ]
            },
            "Case4_133Ce_MChD_and_Cross_Nucleus_Borrowing_Ban": {
                "established_boundaries": [
                    "Strict prohibition against borrowing lifetimes or transition probabilities from neighboring nuclei/isotones.",
                    "MChD requires partner-resolved absolute transition probabilities and lifetimes within the nucleus itself."
                ]
            },
            "Case5_76Ge_Coulex_Sum_Rules_and_Truncation_Bias": {
                "established_boundaries": [
                    "Quadrupole invariants from multi-step Coulex sum rules converge slowly for 4-body loops <Q^4>.",
                    "Truncation to few states artificially compresses <Q^4> -> (<Q^2>)^2, driving variance sigma -> 0 and mimicking rigid deformation.",
                    "Strictly prohibit using invariant variance sigma -> 0 under truncated intermediate states as an exclusive proof of nuclear rigid deformation."
                ]
            }
        },
        "methodological_rules": [
            "Rule 1: Separate experimental reports, author interpretations, model calculations, and our inferences.",
            "Rule 2: Never merge data across different beam energies, detector arrays, or gating conditions without joint covariance.",
            "Rule 3: Single-parameter agreement (e.g. energy degeneracy alone or S(4) alone) is never sufficient to establish a collective mode.",
            "Rule 4: Model breakdown / divergence points (e.g. RPA softening to zero) must not be equated to physical phase transitions."
        ]
    }

    out = RUN / 'cross-pillar-synthesis-scope-133.json'
    out.write_text(json.dumps(synthesis, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({
        "output": str(out.relative_to(ROOT)),
        "pillars_synthesized": len(synthesis["case_studies"]),
        "rules_synthesized": len(synthesis["methodological_rules"]),
        "case1_metrics": synthesis["case_studies"]["Case1_135Nd_vs_134Pr_Chirality_and_Quadrupole_Moments"]["quantitative_summary"]
    }))

if __name__ == '__main__':
    main()
