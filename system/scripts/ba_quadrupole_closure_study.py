#!/usr/bin/env python3
"""Fixed-parameter odd-Ba E2 closure study, with no shape or energy fit.

The primary operator is calibrated to each even core's first 0->2 strength.
The core-only control uses the same charge, Hamiltonian, and wavefunction.
Both complete lab-component contraction and complete reduced 6j closure are
required to agree. J+2 restrictions contain whole multiplets and remain
rotational scalars; they are not complete charge-polynomial moments.

Run with single-thread BLAS. Output directories must be new. Numerical model
results do not reproduce the source authors' electromagnetic figures, and
rigid-equivalent moment angles do not establish softness or rigidity.
"""

import argparse
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import sys
import time

import numpy as np
from scipy import linalg, sparse

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "system/scripts/analysis"))
from paired_single_j_em import clebsch_gordan
from single_j_ibfm import (
    BosonCore, CoreParameters, IBFMKernel, IBFMParameters, calibrate_core_e2,
)
from quadrupole_scalar_invariants import (
    direct_from_spectrum, j_plus_two_proxy, reduced_invariants,
    reduced_table_from_spectrum,
)

RUN = ROOT / "outputs/l4/20261105-ba129-controlled-pairing"
CONTRACT = RUN / "spin-invariant-chain-contract.json"
CALIBRATION = RUN / "core-E2-calibration/ba-core-E2.json"


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def stamp():
    return datetime.now(timezone.utc).isoformat()


def write_json(path, value):
    with Path(path).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write("\n")


def real(value):
    value = complex(value)
    if abs(value.imag) > 1e-11 * max(1., abs(value.real)):
        raise ValueError("unexpected complex observable")
    return float(value.real)


def folded_angle(ratio):
    if ratio is None or abs(ratio) > 1 + 1e-12:
        return None
    return math.degrees(math.acos(min(1., abs(ratio)))) / 3


def scalar_record(value):
    return {
        "q2_e2b2": value.q2,
        "q3_e3b3": value.q3,
        "signed_ratio": value.raw_ratio,
        "signed_rigid_equivalent_angle_deg": value.rigid_equivalent_angle_deg,
        "folded_rigid_equivalent_angle_deg": folded_angle(value.raw_ratio),
        "angle_status": value.angle_status,
        "imaginary_residual_q2": abs(value.q2_complex.imag),
        "imaginary_residual_q3": abs(value.q3_complex.imag),
    }


def assess(solution, operator, state, label):
    """Return compact complete-closure evidence; never serialize all loop pairs."""
    direct = direct_from_spectrum(
        solution, operator, state, representation_label=label)
    table = reduced_table_from_spectrum(
        solution, operator, representation_label=label)
    closure = reduced_invariants(table, state)
    if not closure.complete or closure.invariants is None:
        raise ValueError(f"{label}: required reduced elements are missing")
    spectral = closure.invariants
    dq2, dq3 = spectral.q2 - direct.q2, spectral.q3 - direct.q3
    if abs(dq2) > 2e-10 * max(1., direct.q2):
        raise ValueError(f"{label}: quadratic closure failed: {dq2}")
    if abs(dq3) > 2e-10 * max(1., direct.q2 ** 1.5):
        raise ValueError(f"{label}: cubic closure failed: {dq3}")
    tj = int(solution.two_J[state])
    same_label = table.multiplets[state].label
    static_q2 = closure.quadratic_by_state.get(same_label, 0.) or 0.
    same_spin_q2 = closure.quadratic_by_two_J.get(tj, 0.)
    channel_q2 = closure.quadratic_by_two_J[tj + 4]
    spin_pairs = [{
        "two_Ja": a, "two_Jb": b, "q3_e3b3": real(value),
        "normalized_to_q2_power_3_over_2": real(value) / direct.q2 ** 1.5,
    } for (a, b), value in sorted(closure.cubic_by_two_J_pair.items())]
    by_initial_count = {0: 0j, 1: 0j, 2: 0j}
    abs_state_pairs = 0.
    for (a, b), value in closure.cubic_by_state_pair.items():
        if value is None:
            raise ValueError("missing cubic pair despite complete closure")
        by_initial_count[int(a == same_label) + int(b == same_label)] += value
        abs_state_pairs += abs(value)
    proxies = []
    # Spectrum registry is globally energy sorted by the validated diagonalizer.
    for count in (1, 5, 10, None):
        proxy = j_plus_two_proxy(table, state, max_states=count)
        band_cg = clebsch_gordan(tj + 4, tj, 4, 0, tj, tj)
        beta_scale = math.sqrt(
            proxy.quadratic_strength_sum / ((tj + 5) * band_cg ** 2))
        proxies.append({
            "max_states": count, "states_used": len(proxy.selected_labels),
            "quadratic_strength_sum_e2b2": proxy.quadratic_strength_sum,
            "quadratic_closure_contribution_e2b2": proxy.quadratic_closure_contribution,
            "fraction_of_full_q2": proxy.quadratic_closure_contribution / direct.q2,
            "fraction_of_Jplus2_q2": proxy.quadratic_closure_contribution / channel_q2,
            "signed_cubic_chain_e3b3": real(proxy.cubic_chain),
            "absolute_scaled_chain_e3b3": proxy.scaled_absolute_chain,
            "raw_proxy_ratio": proxy.raw_proxy_ratio,
            "proxy_angle_deg": proxy.proxy_angle_deg,
            "angle_status": proxy.angle_status,
            "beta_scale_without_radius_eb": beta_scale,
            "beta_scale_over_sqrt_full_q2": beta_scale / math.sqrt(direct.q2),
        })
    rme_ii = real(table.rme[state, state])
    qs = (math.sqrt(16 * math.pi / 5)
          * clebsch_gordan(tj, tj, 4, 0, tj, tj)
          * rme_ii / math.sqrt(tj + 1))
    transitions = []
    for two_J in sorted(closure.quadratic_by_two_J):
        for ordinal, final in enumerate(solution.indices_for_J(two_J)[:3]):
            final = int(final)
            transitions.append({
                "two_J_final": int(two_J), "ordinal_zero_based": ordinal,
                "same_state": final == state,
                "Efinal_minus_Einitial_MeV": float(
                    solution.energies[final] - solution.energies[state]),
                "signed_RME_eb": real(table.rme[final, state]),
                "B_E2_e2b2": float(abs(table.rme[final, state]) ** 2 / (tj + 1)),
            })
    return {
        "state_index": state, "two_J": tj,
        "full": scalar_record(direct),
        "closure": {
            "complete_declared_model_space": closure.complete,
            "reduced_minus_direct_q2": dq2,
            "reduced_minus_direct_q3": dq3,
            "reduced_reciprocity_residual": closure.reciprocity_residual,
            "missing_required_entries": list(closure.missing_entries),
            "unresolved_entries_elsewhere_in_table": len(table.unresolved),
        },
        "quadratic_channels": [{
            "two_J": spin, "state_count": len(solution.indices_for_J(spin)),
            "q2_e2b2": value, "fraction_of_full": value / direct.q2,
        } for spin, value in sorted(closure.quadratic_by_two_J.items())],
        "same_spin": {
            "static_q2_e2b2": static_q2,
            "other_same_spin_q2_e2b2": same_spin_q2 - static_q2,
            "static_fraction_of_full_q2": static_q2 / direct.q2,
            "other_same_spin_fraction_of_full_q2": (same_spin_q2 - static_q2) / direct.q2,
            "spectroscopic_Qs_eb": qs,
        },
        "signed_cubic_spin_pairs": spin_pairs,
        "cubic_cancellation": {
            "sum_positive_spin_pairs_e3b3": sum(max(0., p["q3_e3b3"]) for p in spin_pairs),
            "sum_negative_spin_pairs_e3b3": sum(min(0., p["q3_e3b3"]) for p in spin_pairs),
            "sum_abs_spin_pairs_e3b3": sum(abs(p["q3_e3b3"]) for p in spin_pairs),
            "sum_abs_state_pairs_e3b3": abs_state_pairs,
            "by_number_of_initial_state_intermediates_e3b3": {
                str(k): real(v) for k, v in by_initial_count.items()},
        },
        "restricted": proxies,
        "selected_matrix_elements": transitions,
        "selected_matrix_element_boundary": (
            "Model predictions, common solver phase convention. Excitation energies "
            "need not match experimental levels; same-state B is a diagonal strength, "
            "not a gamma decay."),
    }


def core_composition(odd, solution, state, core, cs, core_state):
    basis = solution.basis
    block = basis.restrict(sparse.kron(
        odd.bosons.L2, odd.fermion_identity, format="csr")).toarray()
    values, vectors = linalg.eigh(block)
    r = (np.sqrt(1 + 4 * np.maximum(0., values)) - 1) / 2
    rounded = np.rint(r).astype(int)
    if np.max(abs(r - rounded)) > 1e-8:
        raise ValueError("core angular momentum spectrum is not integral")
    weights = abs(vectors.conj().T @ solution.vectors[:, state]) ** 2
    probabilities = {
        str(int(R)): float(weights[rounded == R].sum()) for R in np.unique(rounded)}
    if abs(sum(probabilities.values()) - 1.) > 1e-10:
        raise ValueError("core R probabilities do not normalize")
    full = np.zeros(basis.full_dimension, complex)
    full[basis.full_indices] = solution.vectors[:, state]
    full = full.reshape(core.bosons.dimension, odd.parameters.two_j + 1)
    zero_core = np.zeros(core.bosons.dimension, complex)
    zero_core[cs.basis.full_indices] = cs.vectors[:, core_state]
    f_index = (odd.parameters.two_j + basis.two_M) // 2
    ground_probability = float(abs(np.vdot(zero_core, full[:, f_index])) ** 2)
    return {
        "probability_by_core_R": probabilities,
        "core_ground_state_probability": ground_probability,
        "boundary": "R=0 also includes excited zero-spin core states.",
    }


def parameters(case):
    keys = ("n_b", "two_j", "eps_d", "kappa", "chi", "v2",
            "Gamma0", "Lambda0", "A0")
    return IBFMParameters(**{key: case[key] for key in keys},
                          Q_jj=-math.sqrt(525 / (143 * math.pi)))


def run_case(case, calibration, chi_e, e_f):
    start = time.monotonic()
    p = parameters(case)
    core = BosonCore(CoreParameters(p.n_b, p.eps_d, p.kappa, p.chi))
    cs = core.solve()
    c0, c2 = (int(cs.indices_for_J(j)[0]) for j in (0, 4))
    target = calibration["selected_strength"]["B_up_e2b2"]
    charge = calibrate_core_e2(
        core, cs, c0, c2, chi_prime=chi_e, target_B_0_to_2=target)
    even = assess(cs, core.e2(charge.eB, chi_e), c0, f"core-{case['core_A']}")
    odd = IBFMKernel(p)
    solution = odd.solve()
    state = int(solution.indices_for_J(case["two_J_state"])[case["state_ordinal"]])
    primary = assess(
        solution, odd.e2(charge.eB, e_f, chi_e), state, f"odd-{case['odd_A']}-E2")
    control = assess(
        solution, odd.e2(charge.eB, 0., chi_e), state, f"odd-{case['odd_A']}-core-only")
    composition = core_composition(odd, solution, state, core, cs, c0)
    # Resolve the mixed operator polynomial without altering the Hamiltonian.
    f_only = direct_from_spectrum(solution, odd.e2(0., e_f, chi_e), state,
                                  representation_label="fermion-only")
    minus = direct_from_spectrum(solution, odd.e2(charge.eB, -e_f, chi_e), state,
                                 representation_label="boson-minus-fermion")
    q3plus, q3b = (x["full"]["q3_e3b3"] for x in (primary, control))
    mixed = {
        "q2_BB_e2b2": control["full"]["q2_e2b2"],
        "q2_BF_plus_FB_e2b2": (
            primary["full"]["q2_e2b2"] - control["full"]["q2_e2b2"] - f_only.q2),
        "q2_FF_e2b2": f_only.q2,
        "q3_BBB_e3b3": q3b,
        "q3_two_B_one_F_all_orders_e3b3": (q3plus - minus.q3) / 2 - f_only.q3,
        "q3_one_B_two_F_all_orders_e3b3": (q3plus + minus.q3) / 2 - q3b,
        "q3_FFF_e3b3": f_only.q3,
        "boundary": "B and F include their declared charges and BCS factors.",
    }
    p5, pall = primary["restricted"][1], primary["restricted"][-1]
    return {
        "case": case, "parameters": asdict(p),
        "calibration": {
            **asdict(charge), "eF_eb": e_f, "chi_E2": chi_e,
            "core_selected_strength": calibration["selected_strength"],
            "source": calibration["source"],
            "direction": "target is upward 0->2; Bup=5 Bdown",
        },
        "basis": {
            "full_dimension": odd.dimension, "M_half_dimension": solution.basis.dimension,
            "core_M_zero_dimension": cs.basis.dimension,
        },
        "core": even, "primary": primary, "core_only": control,
        "core_composition": composition,
        "operator_polynomial": mixed,
        "comparison": {
            "sqrt_primary_q2_over_even_q2": math.sqrt(
                primary["full"]["q2_e2b2"] / even["full"]["q2_e2b2"]),
            "sqrt_core_only_q2_over_even_q2": math.sqrt(
                control["full"]["q2_e2b2"] / even["full"]["q2_e2b2"]),
            "five_minus_all_proxy_angle_deg": (
                p5["proxy_angle_deg"] - pall["proxy_angle_deg"]
                if p5["proxy_angle_deg"] is not None and pall["proxy_angle_deg"] is not None
                else None),
        },
        "elapsed_seconds": time.monotonic() - start,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--only", type=int, nargs="+")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    contract = json.loads(CONTRACT.read_text())
    calibration = json.loads(CALIBRATION.read_text())
    rows = {row["A"]: row for row in calibration["selected_rows"]}
    files = [Path(__file__), CONTRACT, CALIBRATION,
             ROOT / "system/scripts/analysis/single_j_ibfm.py",
             ROOT / "system/scripts/analysis/quadrupole_scalar_invariants.py",
             ROOT / "system/scripts/analysis/paired_single_j_em.py"]
    hashes = {str(p.relative_to(ROOT)): digest(p) for p in files}
    cases = [case for case in contract["cases"]
             if args.only is None or case["odd_A"] in args.only]
    if args.only and set(args.only) != {c["odd_A"] for c in cases}:
        raise ValueError("requested isotope absent from fixed contract")
    result = {
        "schema": "odd-Ba-calibrated-quadrupole-closure-v1",
        "started_at_utc": stamp(), "input_sha256": hashes,
        "evidence_class": "finite-model calculation, evaluated core E2 calibration",
        "boundary": __doc__,
        "cases": [],
    }
    write_json(args.output / "input-record.json", {
        k: v for k, v in result.items() if k != "cases"})
    for case in cases:
        value = run_case(case, rows[case["core_A"]],
                         contract["E2_policy"]["chi_prime"],
                         contract["E2_policy"]["eF_eb"])
        write_json(args.output / f"ba{case['odd_A']}.json", value)
        result["cases"].append(value)
        p = value["primary"]
        print(json.dumps({
            "A": case["odd_A"], "eB": value["calibration"]["eB"],
            "q2": p["full"]["q2_e2b2"], "signed_ratio": p["full"]["signed_ratio"],
            "folded_angle": p["full"]["folded_rigid_equivalent_angle_deg"],
            "proxy5_angle": p["restricted"][1]["proxy_angle_deg"],
            "proxy_all_angle": p["restricted"][-1]["proxy_angle_deg"],
            "closure": p["closure"], "seconds": value["elapsed_seconds"],
        }), flush=True)
    for relative, expected in hashes.items():
        if digest(ROOT / relative) != expected:
            raise RuntimeError(f"input changed during execution: {relative}")
    result["finished_at_utc"] = stamp()
    write_json(args.output / "study.json", result)


if __name__ == "__main__":
    main()
