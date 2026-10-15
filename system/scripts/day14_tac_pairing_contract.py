#!/usr/bin/env python3
"""Audit a public TAC pairing source and explicit, chosen finite-space controls.

This does not run the author's RHB code or infer any actual nuclear occupation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import pymupdf
from scipy.integrate import quad


ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02"
TEMP = ROOT / "tmp/day14-20261014/tac2017"
EXPECTED_SHA = "15e901a4f5d8ad1b5cf4bffe61e050d8eb6a3c89b0f9f62dea84e5d56c335d87"


def creation(mode: int, modes: int = 4) -> np.ndarray:
    """Canonical Fock ordering: p-up, p-down, n-up, n-down."""
    result = np.zeros((2**modes, 2**modes))
    for occupation in range(2**modes):
        if occupation & (1 << mode):
            continue
        below = (occupation & ((1 << mode) - 1)).bit_count()
        result[occupation | (1 << mode), occupation] = (-1) ** below
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=RUN / "tac-pairing-contract.json")
    args = parser.parse_args()
    checks: dict[str, bool] = {}

    def check(name: str, condition: object) -> None:
        checks[name] = bool(condition)

    manifest = json.loads((TEMP / "manifest.json").read_text())
    pdf = Path(manifest["results"][0]["file"]).resolve()
    check("pdf_inside_wiki", pdf.is_relative_to(ROOT))
    data = pdf.read_bytes()
    check("pdf_magic", data.startswith(b"%PDF"))
    check("actual_pdf_hash", hashlib.sha256(data).hexdigest() == EXPECTED_SHA)
    doc = pymupdf.open(pdf)
    pages = [p.get_text() for p in doc]
    check("nine_pages", len(pages) == 9)
    check("title_and_version", "separable pairing force" in pages[0] and "1708.06117v2" in pages[0])
    check("rhb_and_force_locators", all(f"({i})" in pages[1] for i in [4, 10, 11, 12]))
    check("actual_parameters_present", all(x in pages[2] for x in ["738", "0.636", "0.021%", "0.020%", "12", "14"]))
    check("blocking_definition_present", "trace" in pages[2] and "block" in pages[2])
    check("number_restoration_not_performed", "particle number is not conserved" in " ".join(pages[3].split()) and "restoration" in pages[3])
    check("literal_formula_locators", "(25)" in pages[2] and all(x in pages[7] for x in ["(A18)", "(A19)"]))

    # Eq. (12): a normalized form factor, not a measured pair-density radius.
    a = 0.636  # fm; actual source parameter, Sec. III.
    strength = -738.0  # MeV fm^3; actual source parameter, Sec. III.

    def radial(r: float) -> float:
        return 4 * math.pi * r**2 * math.exp(-r**2 / (4 * a**2)) / (4 * math.pi * a**2) ** 1.5

    integral, integral_error = quad(radial, 0, np.inf, epsabs=1e-12)
    r2, r2_error = quad(lambda r: r**2 * radial(r), 0, np.inf, epsabs=1e-12)
    check("form_factor_normalized", math.isclose(integral, 1, abs_tol=2e-12))
    check("form_factor_second_moment", math.isclose(r2, 6 * a**2, abs_tol=2e-12))
    check("form_factor_nonnegative", all(radial(r) >= 0 for r in [0, a, 2*a, 6*a]))
    # MeV and fm exponents: G * delta^3(R-R') * P(r) * P(r').
    kernel_units = np.array([1, 3]) + np.array([0, -3]) + 2 * np.array([0, -3])
    matrix_units = kernel_units + np.array([0, -6]) + np.array([0, 12])
    check("nonlocal_kernel_units", np.array_equal(kernel_units, [1, -6]))
    check("normalized_two_body_matrix_units", np.array_equal(matrix_units, [1, 0]))

    # Eq. (11) acts on spin. No isospin/projected particle inventory follows from it alone.
    swap = np.array([[1,0,0,0], [0,0,1,0], [0,1,0,0], [0,0,0,1]], dtype=float)
    spin_projector = (np.eye(4) - swap) / 2
    singlet = np.array([0, 1, -1, 0], dtype=float) / math.sqrt(2)
    check("spin_projector_hermitian", np.allclose(spin_projector.T, spin_projector))
    check("spin_projector_idempotent", np.allclose(spin_projector @ spin_projector, spin_projector))
    check("spin_projector_rank_one", np.linalg.matrix_rank(spin_projector) == 1)
    check("spin_singlet_passes", np.allclose(spin_projector @ singlet, singlet))
    check("triplet_removed", np.allclose(spin_projector @ np.array([0, 1, 1, 0]), 0))

    # Explicit chosen states. These are not the author's computed canonical states.
    c = [creation(i) for i in range(4)]
    identity = np.eye(16)
    vacuum = np.eye(16)[:, 0]
    np_values = np.array([(s & 3).bit_count() for s in range(16)])
    nn_values = np.array([((s >> 2) & 3).bit_count() for s in range(16)])
    parity_p, parity_n = (-1.0)**np_values, (-1.0)**nn_values
    pair_p, pair_n = c[0] @ c[1], c[2] @ c[3]
    for i in range(4):
        check(f"creation_CAR_{i}", np.allclose(c[i].T @ c[i] + c[i] @ c[i].T, identity))
    like_rows = []
    for bp, bn in [(0,0), (1,0), (0,1), (1,1)]:
        p_op = c[0] if bp else math.sqrt(.4)*identity + math.sqrt(.6)*pair_p
        n_op = c[2] if bn else math.sqrt(.3)*identity + math.sqrt(.7)*pair_n
        psi = p_op @ n_op @ vacuum
        probability = abs(psi)**2
        pp = float(probability @ parity_p)
        pn = float(probability @ parity_n)
        check(f"like_{bp}{bn}_norm", np.isclose(probability.sum(), 1))
        check(f"like_{bp}{bn}_species_sectors", np.isclose(pp, (-1)**bp) and np.isclose(pn, (-1)**bn))
        check(f"like_{bp}{bn}_total_sector", np.isclose(probability @ (parity_p*parity_n), (-1)**(bp+bn)))
        like_rows.append({"blocked_p":bp, "blocked_n":bn, "mean_Np":float(probability@np_values),
                          "mean_Nn":float(probability@nn_values), "parity_p":pp, "parity_n":pn,
                          "support":[{"Np":int(np_values[s]),"Nn":int(nn_values[s]),"probability":float(probability[s])}
                                     for s in range(16) if probability[s] > 1e-14]})
    # A spin-singlet pn pair is a mathematical channel control, not an assertion
    # that Wang2017/Lv2025 implements proton-neutron pairing.
    pn_pair = (c[0] @ c[3] - c[1] @ c[2]) / math.sqrt(2)
    pn_pair_state = pn_pair @ vacuum
    spin_raise = c[0] @ c[1].T + c[2] @ c[3].T
    check("pn_pair_normalized", np.isclose(pn_pair_state @ pn_pair_state, 1))
    check("pn_pair_spin_singlet", np.allclose(spin_raise @ pn_pair_state, 0))
    mixed = math.sqrt(.6)*vacuum + math.sqrt(.4)*pn_pair_state
    weights = abs(mixed)**2
    check("pn_mixture_normalized", np.isclose(weights.sum(), 1))
    check("pn_mixture_total_even", np.isclose(weights@(parity_p*parity_n), 1))
    check("pn_mixture_species_not_fixed", np.isclose(weights@parity_p, .2) and np.isclose(weights@parity_n, .2))
    even_mean_one = (vacuum + pair_n@vacuum)/math.sqrt(2)
    w = abs(even_mean_one)**2
    check("mean_N1_not_number_projection", np.isclose(w@nn_values, 1) and np.isclose(w[nn_values == 1].sum(), 0))

    # Literal v2 Eq. (25), visually checked against the rendered page.
    mu_x, mu_z, theta = 3., 4., 0.  # chosen, not nuclear magnetic-moment data.
    transverse = mu_x*math.sin(theta) - mu_z*math.cos(theta)
    coefficient = 3/(8*math.pi)
    middle_squared = coefficient*transverse**2
    literal_last = coefficient*transverse
    check("eq25_literal_sign_failure_control", middle_squared > 0 and literal_last < 0)
    check("eq25_literal_scaling_inconsistent", np.isclose(coefficient*(2*transverse)**2/middle_squared, 4)
          and np.isclose(coefficient*(2*transverse)/literal_last, 2))
    appendix = []
    for na, nb, cm in [(1,1,0), (2,0,0), (2,2,2), (0,0,0)]:
        literal = cm-na-nb
        required_by_delta = na+nb-cm
        appendix.append({"n_gamma":na,"n_delta":nb,"N_cm":cm,"A18_literal_n":literal,
                         "A19_delta_requires_n":required_by_delta,"agree":literal == required_by_delta})
    check("appendix_nonzero_relative_counterexample", appendix[0]["A18_literal_n"] == -2 and appendix[0]["A19_delta_requires_n"] == 2)
    check("appendix_zero_relative_case_not_general", appendix[-1]["agree"] and not any(x["agree"] for x in appendix[:-1]))
    reduction = 1 - .87/1.26
    check("printed_gap_percent_not_twenty", not math.isclose(reduction, .2, abs_tol=.01))
    # Eq. (24)/(28), Fig. 8: scale the Dirac component, not every amplitude.
    dirac, anomalous, attenuation = 3., -1., .58
    operator_scaled = (attenuation*dirac + anomalous)**2
    whole_scaled = attenuation**2 * (dirac + anomalous)**2
    check("magnetic_component_scaling_not_whole_B", not np.isclose(operator_scaled, whole_scaled))
    check("magnetic_component_scaling_nochange_control", np.isclose((1*dirac+anomalous)**2, (dirac+anomalous)**2))
    check("magnetic_component_scaling_zero_anomalous_control", np.isclose((attenuation*dirac)**2, attenuation**2*dirac**2))

    result = {
        "kind":"source-parameter/formula audit plus declared finite-Fock-space design; not an RHB rerun",
        "source":{"doi":"10.1103/PhysRevC.96.054324","arxiv":"1708.06117v2", "pdf":str(pdf.relative_to(ROOT)),
                  "sha256":EXPECTED_SHA,"pages":len(pages),"raw_archived":False},
        "actual_source_parameters":{"G_MeV_fm3":strength,"a_fm":a,"locator":"PDF p.3 Sec.III"},
        "form_factor":{"locator":"PDF p.2 Eq.(12)","integral":integral,"quad_error":integral_error,
                       "weighted_r2_fm2":r2,"r2_quad_error":r2_error,"formal_rms_fm":math.sqrt(r2),
                       "note":"moments of normalized P form factor, not a measured or calculated nuclear pair-density radius"},
        "spin_projector":{"locator":"PDF p.2 Eq.(11)","matrix":spin_projector.tolist(),"eigenvalues":np.linalg.eigvalsh(spin_projector).tolist(),
                          "isospin_or_actual_pn_implementation":"not determined by the spin projector"},
        "chosen_like_particle_states":like_rows,
        "chosen_pn_control":{"pair_probability":.4,"parity_p":float(weights@parity_p),"parity_n":float(weights@parity_n),
                             "total_parity":float(weights@(parity_p*parity_n)),"actual_source_implementation":None},
        "literal_version_controls":{"eq25":{"locator":"PDF p.3 Eq.(25)","chosen_mu_x":mu_x,"chosen_mu_z":mu_z,"chosen_theta":theta,
                                    "middle_squared":middle_squared,"last_literal_linear":literal_last,
                                    "actual_author_code":None,"official_erratum_checked":False},
                                    "appendix_A18_A19":appendix,"gap_relative_reduction":reduction},
        "chosen_operator_component_control":{"source":"PDF p.7 Eq.(28), Fig.8", "chosen_D":dirac,"chosen_A":anomalous,
                                             "source_attenuation":attenuation,"component_scaled_square":operator_scaled,
                                             "whole_scaled_square":whole_scaled,"actual_nuclear_components":None},
        "missing_actual_inputs":["Pr136 occupied/blocked list and reference/spectators", "qp-following overlap/logs",
                                 "author implementation/number projection", "experimental event/response/covariance"],
        "checks":checks,"check_count":len(checks),"passed":all(checks.values()),
    }
    args.output.resolve().relative_to(ROOT)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"output":str(args.output.relative_to(ROOT)),"checks":len(checks),"passed":result["passed"],
                      "failed":[k for k,v in checks.items() if not v],"P_integral":integral,"P_r2":r2},ensure_ascii=False))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
