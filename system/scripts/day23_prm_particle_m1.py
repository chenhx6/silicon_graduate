#!/usr/bin/env python3
"""Normalized particle-j lab tensor on the unchanged, declared Day23 H variant.

For different I, T(M1)=S_M*j, S_M=sqrt(3/4pi)*(g_j-g_R)*mu_N.
S_M is unknown. Same-I closure below concerns j, not the full magnetic moment.
"""
import argparse
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day23_prm_basis_rotor import clebsch_gordan, transformation
from day23_prm_core_e2 import model_sector, reduced_tensor as core_e2_tensor


def spherical_spin(spin, projection, component):
    """<s,m+q|s_q|s,m> with hbar=1, Condon-Shortley spherical components."""
    if component == 0:
        return projection
    if abs(projection+component) > spin:
        return 0.0
    if component == 1:
        return -math.sqrt((spin-projection)*(spin+projection+1)/2)
    if component == -1:
        return math.sqrt((spin+projection)*(spin-projection+1)/2)
    raise ValueError("Rank-one component must be -1, 0, or +1")


@lru_cache(None)
def coupled_reduced(two_i, two_f, two_j, rotor, lab_offset=0, acts_on="particle"):
    """Explicit lab magnetic-substate sum in |(j R)IM>, independent of K."""
    ii, ff, jj = two_i/2, two_f/2, two_j/2
    if abs(ii-ff) > 1:
        return 0.0
    mi, mf = ii-lab_offset, ff-lab_offset
    component = int(round(mf-mi))
    cg = clebsch_gordan(ii, mi, 1, component, ff, mf)
    if abs(cg) < 1e-13:
        raise ValueError("Chosen lab component cannot extract this reduced element")
    lab = 0.0
    for m in np.arange(-two_j, two_j+1, 2)/2:
        mr = mi-m
        if abs(mr) > rotor:
            continue
        if acts_on == "particle":
            m_final, mr_final = m+component, mr
            amplitude = spherical_spin(jj, m, component)
        elif acts_on == "rotor":
            m_final, mr_final = m, mr+component
            amplitude = spherical_spin(rotor, mr, component)
        else:
            raise ValueError("Unknown tensor constituent")
        lab += (clebsch_gordan(jj, m, rotor, mr, ii, mi)
                * clebsch_gordan(jj, m_final, rotor, mr_final, ff, mf)
                * amplitude)
    return lab*math.sqrt(two_f+1)/cg


@lru_cache(None)
def reduced_tensor(two_i, two_f, two_j=11, lab_offset=0, acts_on="particle"):
    _, wi, ui = transformation(two_i, two_j)
    _, wf, uf = transformation(two_f, two_j)
    weak = np.zeros((len(wf), len(wi)))
    if abs(two_i-two_f) <= 2:
        final_index = {pair: index for index, pair in enumerate(wf)}
        for col, (rotor, kr) in enumerate(wi):
            row = final_index.get((rotor, kr))
            if row is not None:
                weak[row, col] = coupled_reduced(
                    two_i, two_f, two_j, rotor, lab_offset, acts_on)
    return uf@weak@ui.T


def validate(prescription, previous):
    controls, details = {}, {}
    j, two_j = 5.5, 11
    for two_test_j in [1, 11]:
        free = coupled_reduced(two_test_j, two_test_j, two_test_j, 0)
        exact = math.sqrt(two_test_j/2*(two_test_j/2+1)*(two_test_j+1))
        controls[f"j2_{two_test_j}_free_R0_reduced_limit"] = math.isclose(free, exact, abs_tol=1e-13)
    for two_i in [7, 11, 17, 21]:
        i = two_i/2
        _, wi, ui = transformation(two_i, two_j)
        dimension = len(wi)
        closure = np.zeros((dimension, dimension))
        worst_reverse, worst_lab, worst_generator = 0.0, 0.0, 0.0
        for two_f in range(max(1, two_i-2), two_i+3, 2):
            t = reduced_tensor(two_i, two_f)
            reverse = reduced_tensor(two_f, two_i)
            alternate = reduced_tensor(two_i, two_f, lab_offset=1)
            rotor = reduced_tensor(two_i, two_f, acts_on="rotor")
            expected_total = (math.sqrt(i*(i+1)*(two_i+1))*np.eye(dimension)
                              if two_i == two_f else np.zeros_like(t))
            closure += t.T@t/(two_i+1)
            worst_reverse = max(worst_reverse, float(np.max(abs(t-(-1)**((two_f-two_i)//2)*reverse.T))))
            worst_lab = max(worst_lab, float(np.max(abs(t-alternate))))
            worst_generator = max(worst_generator, float(np.max(abs(t+rotor-expected_total))))
        closure_error = float(np.max(abs(closure-j*(j+1)*np.eye(dimension))))
        expected_a = ui@np.diag([(i*(i+1)+j*(j+1)-r*(r+1))/(2*i*(i+1))
                                  for r, kr in wi])@ui.T
        diagonal = reduced_tensor(two_i, two_i)/math.sqrt(i*(i+1)*(two_i+1))
        casimir_error = float(np.max(abs(diagonal-expected_a)))
        tag = f"I2_{two_i}"
        controls[tag+"_particle_j_complete_operator_closure"] = closure_error < 2e-11
        controls[tag+"_Hermitian_reduced_reverse"] = worst_reverse < 2e-11
        controls[tag+"_two_lab_M_choices"] = worst_lab < 2e-11
        controls[tag+"_j_plus_R_equals_total_I_generator"] = worst_generator < 2e-11
        controls[tag+"_same_I_Casimir_full_matrix"] = casimir_error < 2e-12
        details[tag] = {"closure_error_hbar2": closure_error, "reverse_error": worst_reverse,
                        "labM_choice_error": worst_lab, "total_generator_error": worst_generator,
                        "Casimir_coefficient_error": casimir_error}
    controls["rank1_triangle_forbidden_zero"] = bool(np.max(abs(reduced_tensor(17, 11))) == 0)
    same_h_error, static_error = 0.0, 0.0
    for two_i in [17, 21, 25]:
        values, vectors, _ = model_sector(two_i, prescription)
        old = next(r for r in previous["results"] if r["I"] == two_i/2)
        i = two_i/2
        coeff = reduced_tensor(two_i, two_i)/math.sqrt(i*(i+1)*(two_i+1))
        for ordinal in range(3):
            same_h_error = max(same_h_error, abs(float(values[ordinal])-old["states"][ordinal]["energy_MeV"]))
            a = float(np.vdot(vectors[:, ordinal], coeff@vectors[:, ordinal]).real)
            static_error = max(static_error, abs(a-old["states"][ordinal]["g_geometry_a"]))
    controls["same_H_as_frozen009"] = same_h_error < 1e-12
    controls["static_j_coefficient_matches_independent009_body_Casimir"] = static_error < 1e-12
    details["frozen009_energy_error_MeV"] = same_h_error
    details["frozen009_static_a_error"] = static_error
    return {name: bool(value) for name, value in controls.items()}, details


def calculate(prescription, reference_path, e2_path):
    previous, e2 = json.loads(reference_path.read_text()), json.loads(e2_path.read_text())
    if previous["parameters"]["C_prescription"] != prescription or e2["C_prescription"] != prescription:
        raise ValueError("Frozen H reference and E2 must use the same explicit C prescription")
    if not previous["all_controls_pass"] or not e2["all_controls_pass"]:
        raise ValueError("Reference stage has failed implementation controls")
    controls, details = validate(prescription, previous)
    rows = []
    max_e2_error = 0.0
    for two_i in [17, 21, 25]:
        values_i, vi, _ = model_sector(two_i, prescription)
        values_f, vf, _ = model_sector(two_i-2, prescription)
        tj, te = reduced_tensor(two_i, two_i-2), core_e2_tensor(two_i, two_i-2, e2["gamma_E_deg"])
        for ordinal_i in [0, 1]:
            # Target ordinal0 is the declared yrast mapping at the alternating spin.
            jf = np.vdot(vf[:, 0], tj@vi[:, ordinal_i])
            ef = np.vdot(vf[:, 0], te@vi[:, ordinal_i])
            bm, be = float(abs(jf)**2/(two_i+1)), float(abs(ef)**2/(two_i+1))
            old_e2 = next(r for r in e2["results"] if r["I"] == two_i/2 and r["parent_ordinal"] == ordinal_i)
            max_e2_error = max(max_e2_error, abs(be-old_e2["B_out_over_unknown_S_squared"]))
            reverse = np.vdot(vi[:, ordinal_i], reduced_tensor(two_i-2, two_i)@vf[:, 0])
            controls[f"I2_{two_i}_ordinal_{ordinal_i}_detailed_balance"] = math.isclose(
                (two_i+1)*bm, abs(reverse)**2, abs_tol=1e-12)
            rows.append({"I": two_i/2, "parent_ordinal": ordinal_i, "target_Iminus1_ordinal": 0,
                         "delta_E_model_MeV": float(values_i[ordinal_i]-values_f[0]),
                         "reduced_j_amplitude_hbar": float(jf.real),
                         "reduced_core_E2_amplitude_over_SE": float(ef.real),
                         "B_j_hbar2_or_B_M1_over_unknown_SM_squared": bm,
                         "B_E2_over_unknown_SE_squared": be,
                         "normalized_core_E2_over_particle_j_strength_ratio": be/bm if bm > 1e-14 else None,
                         "normalized_core_E2_over_particle_j_signed_amplitude_ratio": float((ef/jf).real) if abs(jf) > 1e-12 else None,
                         "physical_delta": None,
                         "boundary": "Single fixed-j projection and core-only charge; unknown SE/SM and convention/radiative conversion required. No physical g, Q, delta or mode identity."})
    controls["same_core_E2_as_frozen010"] = max_e2_error < 1e-12
    details["frozen010_E2_strength_error"] = max_e2_error
    checks = {name: bool(value) for name, value in controls.items()}
    return {"status": "conditional-particle-j-M1-computed", "C_prescription": prescription,
            "operator": "For Ii!=If, T1=SM*j_lab, SM=sqrt(3/(4pi))*(gj-gR)*muN, unknown; fixed single-j projection. Full mu=gR*I+(gj-gR)*j.",
            "reduced_convention": "labM=CG(IiMi,1mu|IfMf)/sqrt(2If+1)*reduced; B=abs(reduced)^2/(2Ii+1)",
            "scope": "Normalized tensor diagnostic, same H and assumed ordinal mapping; no original author producer, physical effective g or mixing scale calibration.",
            "results": rows, "controls": checks, "control_details": details,
            "all_controls_pass": all(checks.values()),
            "frozen_inputs": {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in [reference_path, e2_path]},
            "implementation_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in [
                Path(__file__), Path(__file__).with_name("day23_prm_basis_rotor.py"),
                Path(__file__).with_name("day23_prm_fixed_state_mapping.py"),
                Path(__file__).with_name("day23_prm_core_e2.py")]},
            "limitations": [
                "j closure includes same-I diagonal/elastic and upward transitions, not measured gamma branch/count completeness or full magnetic-moment closure.",
                "The total-I generator contributes to static moments; it cannot connect different I or distinct orthogonal multiplicity states. A j-only diagonal is not the full magnetic moment.",
                "This finite PRM allows dynamical intrinsic j; a nonzero result alone is not a new frozen-alignment approximation calculation.",
                "Single-j effective gj is an operator projection, not arbitrary adoption of a calibrated multi-orbit gl/gs from another nucleus.",
                "SM=0 if gj=gR; conditional nonzero j matrix elements do not guarantee an actual nonzero physical M1.",
                "Normalized E2/j signed ratios use the declared common tensor/phase conventions and are not physical delta values.",
                "Unknown relative operator scale does not imply real P/Rac likelihoods have equal roots; SH26 fixed sigma/I=.2 conditional AD support remains.",
                "The same-H energy and 526 outlet-direction failures009/010 remain; no likelihood, model-error covariance or actual nuclear assignment supplied."]}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--C-prescription", choices=["Wang2009-Eq11", "Wang2009-Eq3"], required=True)
    p.add_argument("--reference-model", type=Path, required=True)
    p.add_argument("--reference-E2", type=Path, required=True)
    a = p.parse_args()
    result = calculate(a.C_prescription, a.reference_model, a.reference_E2)
    a.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"all_controls_pass": result["all_controls_pass"], "checks": len(result["controls"]),
                      "control_details": result["control_details"], "results": result["results"]}, ensure_ascii=False))
    return 0 if result["all_controls_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
