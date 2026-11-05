#!/usr/bin/env python3
"""Read-only audit of frozen predictions; write derived checks only beside this file.

Run with python3 -B and a single BLAS thread. This does not import/run the
prediction runner, refit parameters, or replace the retained Hamiltonian.
Publisher reproductions are deliberately excluded from this output directory.
"""
from collections import Counter
import csv
from dataclasses import replace
import hashlib
import io
import json
import math
from pathlib import Path
import sys

import numpy as np

ROOT = Path("/workspace/wiki")
BASE = ROOT / "outputs/l4/20261105-ba129-model-readiness"
OUT = BASE / "observable-review"
PREDICTIONS = BASE / "observables-v1/observable-predictions.json"
CONTRACT = BASE / "em-branch-test-contract.json"
MEYER = ROOT / "raw/papers/1975_MeyerTerVehn_CollectiveOddANuclei_PartI.pdf"
sys.path.insert(0, str(ROOT / "system/scripts/analysis"))
from paired_single_j_rotor import PairedRotorParameters, solve
from paired_single_j_em import unit_em, clebsch_gordan

METRICS = {}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(name, text):
    path = OUT / name
    assert OUT.resolve() == OUT and path.resolve().parent == OUT
    path.write_text(text, encoding="utf-8")


def write_csv(name, rows):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    write(name, stream.getvalue())


def check(name, actual, expected, atol=2e-11, rtol=5e-11):
    a, b = np.asarray(actual), np.asarray(expected)
    error = float(np.max(abs(a - b))) if a.size else 0.0
    METRICS[name] = max(error, METRICS.get(name, 0.0))
    if not np.allclose(a, b, atol=atol, rtol=rtol):
        raise AssertionError((name, error, actual, expected))


def optional_check(name, actual, expected):
    if actual is None or expected is None:
        assert actual is None and expected is None, (name, actual, expected)
    else:
        check(name, actual, expected)


def spin(two_j):
    j = two_j / 2
    m = np.arange(-two_j, two_j + 1, 2) / 2
    raising = np.diag(np.sqrt((j - m[:-1]) * (j + m[:-1] + 1)), -1).astype(complex)
    return (raising + raising.T) / 2, (raising - raising.T) / (2j), np.diag(m)


def pi_axis_rotation(two_j):
    # Proper pi rotation about (0,1,1)/sqrt(2): (x,y,z) -> (-x,z,y).
    _, jy, jz = spin(two_j)
    value, vector = np.linalg.eigh((jy + jz) / math.sqrt(2))
    return (vector * np.exp(-1j * math.pi * value)) @ vector.conj().T


def dual(p):
    a, b, c = p.inertias_hbar2_per_MeV
    return replace(p, gamma_deg=60 - p.gamma_deg, lambda_F_MeV=-p.lambda_F_MeV,
                   inertias_hbar2_per_MeV=(a, c, b))


def common_rotation(source):
    # Body I is the complex-conjugate ordinary-spin representation.
    product = np.kron(pi_axis_rotation(source.two_I).conj(),
                      pi_axis_rotation(source.parameters.two_j))
    p = source.product_embedding
    reduced = p.conj().T @ product @ p
    check("dual_rotation_D2_sector_leakage", product @ p, p @ reduced)
    check("dual_rotation_unitarity", reduced.conj().T @ reduced, np.eye(len(reduced)))
    return reduced


def raw_rotor(solution):
    two_i, two_j = solution.two_I, solution.parameters.two_j
    i = list(spin(two_i))
    i[1] *= -1
    j = spin(two_j)
    eye_i, eye_j = np.eye(two_i + 1), np.eye(two_j + 1)
    h = np.zeros(((two_i + 1) * (two_j + 1),) * 2, complex)
    for ik, jk, inertia in zip(i, j, solution.parameters.inertias_hbar2_per_MeV):
        h += (np.kron(ik @ ik, eye_j) + np.kron(eye_i, jk @ jk)
              - 2 * np.kron(ik, jk)) / (2 * inertia)
    return h


def nambu_diagnostic(solution):
    """Measure omitted-sector residuals at frozen positive-block eigenstates.

    The negative-BCS-sector block need not have negative *total* eigenvalues.
    Its eigensystem is used only for a resolvent/perturbative diagnostic.
    No full-Nambu eigenstates, replacement energies or new branch predictions
    are produced.
    """
    p = solution.product_embedding
    dim = p.shape[0]
    up = solution.positive_energy_embedding[:dim]
    vp = solution.positive_energy_embedding[dim:]
    hrot = raw_rotor(solution)
    hup, hvp = hrot @ up, hrot @ vp
    hbar = up.conj().T @ hup + vp.conj().T @ hvp
    s = solution.single_particle.eigenvectors
    emat = (s * solution.quasiparticle_energies_MeV) @ s.conj().T
    ee = p.conj().T @ np.kron(np.eye(solution.two_I + 1), emat) @ p
    check("positive_block_from_independent_rotor_MeV", hbar + ee, solution.hamiltonian_MeV)
    hminus = hbar - ee
    # <-|H|+> = U Hrot V - V Hrot U after both D2 embeddings.
    omitted = up.conj().T @ hvp - vp.conj().T @ hup
    check("Nambu_offdiagonal_antiHermitian_MeV", omitted, -omitted.conj().T)
    e_minus, v_minus = np.linalg.eigh(hminus)
    z = solution.eigenvectors
    residual_components = omitted @ z
    residual_norm = np.linalg.norm(residual_components, axis=0)

    # Independent residual in the original particle/hole product coordinates.
    ustate, vstate = up @ z, vp @ z
    xi = np.kron(np.eye(solution.two_I + 1),
                 solution.single_particle.hamiltonian_MeV
                 - solution.parameters.lambda_F_MeV * np.eye(solution.parameters.two_j + 1))
    gap = solution.parameters.Delta_MeV
    full_residual = np.vstack((
        (hrot + xi) @ ustate + gap * vstate - ustate * solution.eigenvalues_MeV,
        gap * ustate + (hrot - xi) @ vstate - vstate * solution.eigenvalues_MeV,
    ))
    expected_residual = np.vstack((-vp, up)) @ residual_components
    check("omitted_block_equals_full_Nambu_residual_MeV", full_residual, expected_residual)
    check("residual_norm_two_routes_MeV", np.linalg.norm(full_residual, axis=0), residual_norm)
    coupling = v_minus.conj().T @ residual_components
    denominators = solution.eigenvalues_MeV[None, :] - e_minus[:, None]
    rows = []
    for n, energy in enumerate(solution.eigenvalues_MeV):
        delta = denominators[:, n]
        near = bool(np.any(abs(delta) < 1e-10))
        weight = abs(coupling[:, n]) ** 2
        norm_first = None if near else float(np.sqrt(np.sum(weight / delta ** 2)))
        shift_second = None if near else float(np.sum(weight / delta))
        dominant = None if near else int(np.argmax(weight / delta ** 2))
        rows.append({
            "ordinal": n, "positive_block_energy_MeV": float(energy),
            "full_Nambu_residual_norm_MeV": float(residual_norm[n]),
            "min_distance_to_negative_BCS_sector_spectrum_MeV": float(np.min(abs(delta))),
            "near_zero_denominator_under_1e_minus10_MeV": near,
            "first_order_negative_sector_norm_formal": norm_first,
            "second_order_shift_MeV_formal_not_applied": shift_second,
            "dominant_denominator_MeV": None if near else float(delta[dominant]),
            "dominant_coupling_abs_MeV": None if near else float(abs(coupling[dominant, n])),
        })
    return rows, {
        "omitted_block_spectral_norm_MeV": float(np.linalg.svd(omitted, compute_uv=False)[0]),
        "max_intrinsic_eta_abs": float(np.max(abs(
            np.outer(solution.u, solution.v) - np.outer(solution.v, solution.u)))),
    }


def parse_raw_records(path):
    result, level_rows, parent = {}, {}, None
    lines = path.read_text().splitlines()
    for number, line in enumerate(lines, 1):
        padded = line.ljust(80)
        if padded[5:8] == "  L":
            parent = padded[9:19].strip()
            level_rows[number] = {"energy_keV": float(parent), "Jpi": padded[21:39].strip()}
        elif padded[5:8] == "  G":
            result[number] = {
                "parent_energy_keV": None if parent is None else float(parent),
                "gamma_keV": float(padded[9:19]), "RI": float(padded[21:29]),
                "M": padded[31:41].strip(),
            }
    return result, level_rows


def main():
    data = json.loads(PREDICTIONS.read_text())
    contract = json.loads(CONTRACT.read_text())
    locked = dict(data["hashes"])
    locked[str(PREDICTIONS.relative_to(ROOT))] = sha(PREDICTIONS)
    locked[str(MEYER.relative_to(ROOT))] = sha(MEYER)
    for rel, digest in locked.items():
        assert sha(ROOT / rel) == digest, ("input hash differs from frozen record", rel)
    fit_names = sorted({row["energy_fit"] for row in data["predictions"]})
    fits = {name: json.loads((ROOT / name).read_text()) for name in fit_names}
    fit_contracts = {name: json.loads((ROOT / fit["contract"]).read_text()) for name, fit in fits.items()}
    raw_paths = {item["source_raw"] for item in fit_contracts.values()}
    assert len(raw_paths) == 1
    raw_gamma, raw_levels = parse_raw_records(ROOT / next(iter(raw_paths)))
    with (BASE / "lifetime/branches.csv").open() as stream:
        branches = list(csv.DictReader(stream))
    assert sha(BASE / "lifetime/branches.csv") == contract["normalized_branch_input_sha256"]
    mappings = {}
    mapping_rows = []
    for name, fc in fit_contracts.items():
        mapping = {r["level_id"]: r for r in fc["energy_data"]}
        assert len(mapping) == len(fc["energy_data"])
        mappings[name] = mapping
        anchor = mapping[fc["energy_reference_level"]]
        assert anchor["twice_I"] == fc["twice_j"] and anchor["model_ordinal_assumed"] == 0
        assert len({(r["twice_I"], r["model_ordinal_assumed"]) for r in mapping.values()}) == len(mapping)
        for row in mapping.values():
            source = raw_levels[int(row["reaction_locator"].split(":")[1])]
            check("level_energy_contract_to_ENSDF_keV", row["energy_keV"], source["energy_keV"], rtol=0)
            assert row["Jpi_reaction"] == source["Jpi"]
            assert str(row["twice_I"]) + "/2" in source["Jpi"]
            mapping_rows.append({"energy_fit": name, **row})
        assert fits[name]["best_start"] == min(
            fits[name]["starts"], key=lambda r: r["RMS_residual_keV_excluding_anchor"])["start"]
    assert all(m == next(iter(mappings.values())) for m in mappings.values())
    mapping = next(iter(mappings.values()))
    for pair in contract["pairs"]:
        parent = mapping[pair["parent_id"]]
        for prefix, final_key in (("target", "target_final_id"), ("reference", "reference_final_id")):
            line_no = int(pair[prefix + "_locator"].split(":")[1])
            original = raw_gamma[line_no]
            candidates = [r for r in branches if r["reaction_locator"] == pair[prefix + "_locator"]]
            assert len(candidates) == 1
            branch = candidates[0]
            assert branch["parent_level_id"] == pair["parent_id"]
            assert branch["final_level_id"] == pair[final_key]
            check("branch_parent_ENSDF_keV", original["parent_energy_keV"], parent["energy_keV"], rtol=0)
            check("gamma_energy_contract_to_ENSDF_MeV",
                  pair[prefix + "_energy_MeV"], original["gamma_keV"] / 1000, rtol=0)
            check("RI_contract_to_ENSDF", pair[prefix + "_RI"], original["RI"], rtol=0)
            check("RI_contract_to_CSV", pair[prefix + "_RI"], float(branch["RI_reaction_raw"]), rtol=0)
            assert pair[prefix + "_multipolarity_label"] == original["M"]
        assert parent["twice_I"] - mapping[pair["target_final_id"]]["twice_I"] == 2
        assert parent["twice_I"] - mapping[pair["reference_final_id"]]["twice_I"] == 4
        check("reported_ratio_from_RI", pair["reported_photon_ratio"],
              pair["target_RI"] / pair["reference_RI"], rtol=0)
    anchors = [r for r in contract["pairs"] if r["role"] == "scale-calibration"]
    assert len(anchors) == 1 and anchors[0]["parent_id"] == "129Ba_Ex797p4keV"
    assert sum(r["role"] == "withheld-wavefunction-test" for r in contract["pairs"]) == 5
    expected_keys = {(name, r["start"], dual_flag) for name, fit in fits.items()
                     for r in fit["starts"] for dual_flag in (False, True)}
    count = Counter((r["energy_fit"], r["energy_start"], r["dual_partner"]) for r in data["predictions"])
    assert set(count) == expected_keys and all(n == 1 for n in count.values())

    photon_rows, phase_rows, diagonal_rows, nambu_rows, block_rows, dual_rows = [], [], [], [], [], []
    cache = {}
    for row in data["predictions"]:
        key = row["energy_fit"], row["energy_start"], row["dual_partner"]
        p = PairedRotorParameters(**row["parameters"])
        fit = fits[row["energy_fit"]]
        start = next(s for s in fit["starts"] if s["start"] == row["energy_start"])
        source_p = PairedRotorParameters(**{k: start["model_parameters"][k]
                                           for k in PairedRotorParameters.__dataclass_fields__})
        assert p == (dual(source_p) if row["dual_partner"] else source_p)
        assert row["is_recorded_best_start"] == (row["energy_start"] == fit["best_start"])
        mapping = mappings[row["energy_fit"]]
        fc = fit_contracts[row["energy_fit"]]
        anchor = mapping[fc["energy_reference_level"]]
        spins = sorted({r["twice_I"] for r in mapping.values()} | {p.two_j})
        solutions = {spin_: solve(spin_, p) for spin_ in spins}
        calculated_RMS = []
        for level in mapping.values():
            sol = solutions[level["twice_I"]]
            ordinal = level["model_ordinal_assumed"]
            assert 0 <= ordinal < len(sol.eigenvalues_MeV)
            predicted_energy = 1000 * (sol.eigenvalues_MeV[ordinal]
                                       - solutions[p.two_j].eigenvalues_MeV[0]) + anchor["energy_keV"]
            if level["level_id"] != fc["energy_reference_level"]:
                calculated_RMS.append((predicted_energy - level["energy_keV"]) ** 2)
        check("energy_RMS_recomputed_keV", math.sqrt(np.mean(calculated_RMS)), row["energy_RMS_keV"])
        em_cache = {}

        def em(ii, ff):
            if (ii, ff) not in em_cache:
                em_cache[ii, ff] = unit_em(solutions[ii], solutions[ff])
            return em_cache[ii, ff]

        assert len(row["photon"]["pairs"]) == len(contract["pairs"])
        computed = []
        for declared, stored in zip(contract["pairs"], row["photon"]["pairs"]):
            assert all(stored[k] == v for k, v in declared.items())
            parent, target, ref = [mapping[declared[k]] for k in
                                   ("parent_id", "target_final_id", "reference_final_id")]
            ip, it, ir = [r["model_ordinal_assumed"] for r in (parent, target, ref)]
            t = em(parent["twice_I"], target["twice_I"])
            r = em(parent["twice_I"], ref["twice_I"])
            # Rebuild strengths directly from complex amplitudes, with the
            # common initial-spin denominator explicit.
            denom_spin = parent["twice_I"] + 1
            bq_t = abs(t.collective_quadrupole.rme[it, ip]) ** 2 / denom_spin
            bj_t = abs(t.particle_j.rme[it, ip]) ** 2 / denom_spin
            bq_r = abs(r.collective_quadrupole.rme[ir, ip]) ** 2 / denom_spin
            bj_r = abs(r.particle_j.rme[ir, ip]) ** 2 / denom_spin
            check("reference_rank1_zero", bj_r, 0, atol=1e-20, rtol=0)
            check("stored_BQ_target", bq_t, stored["unit_BQ_target"])
            check("stored_Bj_target", bj_t, stored["unit_Bj_target"])
            check("stored_BQ_reference", bq_r, stored["unit_BQ_reference"])
            et, er = declared["target_energy_MeV"], declared["reference_energy_MeV"]
            rates = float(et ** 5 * bq_t), float(et ** 3 * bj_t), float(er ** 5 * bq_r)
            a, b = rates[0] / rates[2], rates[1] / rates[2]
            check("a_from_partial_radiative_rates", a, stored["electric_ratio_a"])
            check("b_from_partial_radiative_rates_per_MeV2", b, stored["magnetic_ratio_coefficient_b_per_MeV2"])
            computed.append((declared, stored, rates, a, b))
        scale_row = next(x for x in computed if x[0]["role"] == "scale-calibration")
        anchor_b = scale_row[4]
        if anchor_b <= 1e-20:
            eta, status = None, "anchor-has-no-magnetic-sensitivity"
        else:
            rates = scale_row[2]
            eta = (scale_row[0]["reported_photon_ratio"] * rates[2] - rates[0]) / rates[1]
            status = "central-anchor-calibrated" if eta >= 0 else "negative-scale-required-anchor-fails"
        optional_check("anchor_eta_MeV2", eta, row["photon"]["anchor_eta_MeV2"])
        assert status == row["photon"]["status"]
        for declared, stored, rates, a, b in computed:
            prediction = None if eta is None or eta < 0 else (rates[0] + eta * rates[1]) / rates[2]
            optional_check("photon_ratio_recomputed", prediction, stored["predicted_photon_ratio"])
            optional_check("prediction_over_reported_ratio",
                           None if prediction is None else prediction / declared["reported_photon_ratio"],
                           stored["prediction_over_reported_ratio"])
            optional_check("E2_radiative_fraction", None if prediction is None or prediction <= 0 else a / prediction,
                           stored["predicted_radiative_E2_fraction"])
            individual = None if b <= 1e-20 else (declared["reported_photon_ratio"] - a) / b
            optional_check("individual_eta_diagnostic_MeV2", individual,
                           stored["eta_required_by_individual_central_ratio_MeV2"])
            photon_rows.append({
                "energy_fit": key[0], "start": key[1], "dual": key[2],
                "recorded_energy_best": row["is_recorded_best_start"],
                "target_gamma_keV": 1000 * declared["target_energy_MeV"],
                "reference_gamma_keV": 1000 * declared["reference_energy_MeV"],
                "parent_id": declared["parent_id"], "role": declared["role"],
                "reported_ratio": declared["reported_photon_ratio"],
                "electric_floor_a": a, "magnetic_coefficient_b_per_MeV2": b,
                "anchor_eta_gamma_MeV2": eta,
                "anchor_deta_dratio_MeV2": None if anchor_b <= 1e-20 else 1 / anchor_b,
                "predicted_ratio": prediction,
                "individual_eta_MeV2_diagnostic_only": individual,
                "electric_floor_exceeds_reported_central_value": a > declared["reported_photon_ratio"],
            })
        # Independent transfer-coordinate check; do not call the transfer runner.
        ts = solutions[p.two_j]
        n = p.two_j + 1
        r0 = np.eye(n).ravel() / math.sqrt(n)
        xp = ts.positive_energy_embedding[:n * n]
        xh = ts.positive_energy_embedding[n * n:]
        removal = abs(math.sqrt(n) * (r0 @ xh @ ts.eigenvectors)) ** 2
        addition = abs(math.sqrt(n) * (r0 @ xp @ ts.eigenvectors)) ** 2
        transfer = row["transfer"]["states"]
        check("transfer_removal_recomputed", removal, [s["removal_strength"] for s in transfer])
        check("transfer_addition_recomputed", addition, [s["addition_strength"] for s in transfer])
        check("transfer_reported_removal_sum", removal.sum(), row["transfer"]["removal_sum"])
        check("transfer_reported_addition_sum", addition.sum(), row["transfer"]["addition_sum"])
        check("transfer_removal_closure", removal.sum(), np.sum(ts.v ** 2))
        check("transfer_addition_closure", addition.sum(), np.sum(ts.u ** 2))
        check("transfer_total_closure", removal.sum() + addition.sum(), n)
        for n_, state in enumerate(transfer):
            assert state["ordinal"] == n_
            optional_check("transfer_relative_strengths",
                           None if removal[0] <= 0 else float(removal[n_] / removal[0]),
                           state["relative_removal_to_first"])
        energies = 1000 * (ts.eigenvalues_MeV - ts.eigenvalues_MeV[0]) + anchor["energy_keV"]
        check("transfer_anchor_and_ordinals_keV", energies, [s["model_excitation_keV"] for s in transfer])
        window = [n_ for n_, ex in enumerate(energies) if n_ > 0 and ex < 2000]
        window_ratio = None if removal[0] <= 0 else float(sum(removal[k] for k in window) / removal[0])
        optional_check("transfer_window_ratio", window_ratio, row["transfer"]["excited_below_2000keV_removal_over_first"])
        for spin_ in spins:
            sol = solutions[spin_]
            self_em = em(spin_, spin_)
            diagnostics, block = nambu_diagnostic(sol)
            block_rows.append({"energy_fit": key[0], "start": key[1], "dual": key[2], "twice_I": spin_, **block})
            for level in mapping.values():
                if level["twice_I"] != spin_:
                    continue
                n_ = level["model_ordinal_assumed"]
                qdiag = self_em.collective_quadrupole.rme[n_, n_]
                jdiag = self_em.particle_j.rme[n_, n_]
                factor = clebsch_gordan(spin_, spin_, 4, 0, spin_, spin_) / math.sqrt(spin_ + 1)
                diagonal_rows.append({
                    "energy_fit": key[0], "start": key[1], "dual": key[2],
                    "recorded_energy_best": row["is_recorded_best_start"],
                    "level_id": level["level_id"], "twice_I": spin_, "ordinal": n_,
                    "Q_diagonal_RME_real": float(qdiag.real), "Q_diagonal_RME_imag": float(qdiag.imag),
                    "unit_stretched_lab_Q20_real": float((factor * qdiag).real),
                    "particle_j_diagonal_RME_real": float(jdiag.real),
                })
                nambu_rows.append({
                    "energy_fit": key[0], "start": key[1], "dual": key[2],
                    "recorded_energy_best": row["is_recorded_best_start"],
                    "level_id": level["level_id"], "twice_I": spin_, **diagnostics[n_],
                })
        cache[key] = {"row": row, "solutions": solutions, "em": em_cache,
                      "removal": removal, "addition": addition}

    for name, start, dual_flag in sorted(expected_keys):
        if dual_flag:
            continue
        first, second = cache[name, start, False], cache[name, start, True]
        mapping = mappings[name]
        rotations = {}
        minimum_overlap = 1.0
        min_mapped_neighbor_gap = math.inf
        for spin_, source in first["solutions"].items():
            other = second["solutions"][spin_]
            sr = common_rotation(source)
            rotations[spin_] = sr
            check("dual_Hamiltonian_covariance_MeV", other.hamiltonian_MeV,
                  sr @ source.hamiltonian_MeV @ sr.conj().T)
            check("dual_energy_MeV", source.eigenvalues_MeV, other.eigenvalues_MeV)
            overlap = other.eigenvectors.conj().T @ sr @ source.eigenvectors
            for level in mapping.values():
                if level["twice_I"] == spin_:
                    n = level["model_ordinal_assumed"]
                    minimum_overlap = min(minimum_overlap, float(abs(overlap[n, n])))
                    distances = abs(source.eigenvalues_MeV - source.eigenvalues_MeV[n])
                    distances[n] = math.inf
                    min_mapped_neighbor_gap = min(min_mapped_neighbor_gap, float(np.min(distances)))
                    assert abs(overlap[n, n]) > 1 - 1e-8
            qa = first["em"][spin_, spin_].collective_quadrupole.rme.diagonal()
            qb = second["em"][spin_, spin_].collective_quadrupole.rme.diagonal()
            check("signed_diagonal_Q_is_odd", qb, -qa)
            for level in mapping.values():
                if level["twice_I"] == spin_:
                    n = level["model_ordinal_assumed"]
                    check("signed_mapped_diagonal_Q_is_odd", qb[n], -qa[n])
        for pair in contract["pairs"]:
            parent, target = mapping[pair["parent_id"]], mapping[pair["target_final_id"]]
            ii, ff = parent["twice_I"], target["twice_I"]
            ip, it = parent["model_ordinal_assumed"], target["model_ordinal_assumed"]
            em_a, em_b = first["em"][ii, ff], second["em"][ii, ff]
            for op, sign in (("collective_quadrupole", -1), ("particle_j", 1)):
                a, b = getattr(em_a, op), getattr(em_b, op)
                check("dual_" + op + "_operator_covariance",
                      rotations[ff].conj().T @ b.d2_rme @ rotations[ii], sign * a.d2_rme)
                check("dual_" + op + "_B", b.unit_B, a.unit_B)
            qa, ja = em_a.collective_quadrupole.rme[it, ip], em_a.particle_j.rme[it, ip]
            qb, jb = em_b.collective_quadrupole.rme[it, ip], em_b.particle_j.rme[it, ip]
            check("dual_selected_target_BQ", em_a.collective_quadrupole.unit_B[it, ip],
                  em_b.collective_quadrupole.unit_B[it, ip])
            check("dual_selected_target_Bj", em_a.particle_j.unit_B[it, ip],
                  em_b.particle_j.unit_B[it, ip])
            ref = mapping[pair["reference_final_id"]]
            ir, rr = ref["model_ordinal_assumed"], ref["twice_I"]
            check("dual_selected_reference_BQ",
                  first["em"][ii, rr].collective_quadrupole.unit_B[ir, ip],
                  second["em"][ii, rr].collective_quadrupole.unit_B[ir, ip])
            cross_a, cross_b = qa * ja.conjugate(), qb * jb.conjugate()
            check("dual_Q_jstar_product_is_odd", cross_b, -cross_a)
            defined = abs(qa) > 1e-12 and abs(ja) > 1e-12 and abs(qb) > 1e-12 and abs(jb) > 1e-12
            z_a = cross_a / (abs(qa) * abs(ja)) if defined else None
            z_b = cross_b / (abs(qb) * abs(jb)) if defined else None
            if defined:
                check("dual_normalized_relative_phase_is_odd", z_b, -z_a)
            phase_rows.append({
                "energy_fit": name, "start": start,
                "recorded_energy_best": first["row"]["is_recorded_best_start"],
                "target_gamma_keV": 1000 * pair["target_energy_MeV"],
                "parent_id": pair["parent_id"], "target_final_id": pair["target_final_id"],
                "Q_RME_real": float(qa.real), "j_RME_real": float(ja.real),
                "dual_Q_RME_real_unaligned": float(qb.real), "dual_j_RME_real_unaligned": float(jb.real),
                "Q_jstar_real": float(cross_a.real), "Q_jstar_imag": float(cross_a.imag),
                "dual_Q_jstar_real": float(cross_b.real), "dual_Q_jstar_imag": float(cross_b.imag),
                "relative_phase_defined": defined,
                "relative_phase_cos": None if not defined else float(z_a.real),
                "dual_relative_phase_cos": None if not defined else float(z_b.real),
                "phase_change_abs_radians": None if not defined else float(abs(np.angle(z_b / z_a))),
            })
        check("dual_transfer_addition_removal_exchange", first["removal"], second["addition"])
        check("dual_transfer_removal_addition_exchange", first["addition"], second["removal"])
        for level in mapping.values():
            a = next(r for r in nambu_rows if r["energy_fit"] == name and r["start"] == start
                     and not r["dual"] and r["level_id"] == level["level_id"])
            b = next(r for r in nambu_rows if r["energy_fit"] == name and r["start"] == start
                     and r["dual"] and r["level_id"] == level["level_id"])
            check("dual_omitted_Nambu_residual_norm_MeV", a["full_Nambu_residual_norm_MeV"],
                  b["full_Nambu_residual_norm_MeV"])
        dual_rows.append({"energy_fit": name, "start": start,
                          "minimum_matched_state_overlap": minimum_overlap,
                          "minimum_mapped_neighbor_spacing_MeV": min_mapped_neighbor_gap})

    # Two diagnostic controls; no new Hamiltonian is used for a prediction.
    free = solve(5, PairedRotorParameters(3, 0.0, 23.0, (11.0, 8.0, 4.0), 0.31, 0.83))
    free_rows, free_block = nambu_diagnostic(free)
    check("C_zero_omitted_block_vanishes_MeV", free_block["omitted_block_spectral_norm_MeV"], 0, atol=2e-13, rtol=0)
    chosen = next(v for k, v in cache.items() if "C120/" in k[0] and not k[2] and v["row"]["is_recorded_best_start"])
    si, sf = chosen["solutions"][15], chosen["solutions"][13]
    ei = np.exp(1j * (0.2 + 0.27 * np.arange(len(si.eigenvalues_MeV))))
    ef = np.exp(1j * (-0.4 + 0.31 * np.arange(len(sf.eigenvalues_MeV))))
    changed = unit_em(replace(si, eigenvectors=si.eigenvectors * ei),
                      replace(sf, eigenvectors=sf.eigenvectors * ef))
    original = chosen["em"][15, 13]
    check("Q_jstar_invariant_under_independent_state_rephasing",
          changed.collective_quadrupole.rme * changed.particle_j.rme.conj(),
          original.collective_quadrupole.rme * original.particle_j.rme.conj())
    for row in nambu_rows:
        reference_id = fit_contracts[row["energy_fit"]]["energy_reference_level"]
        reference = next(r for r in nambu_rows if
                         (r["energy_fit"], r["start"], r["dual"], r["level_id"])
                         == (row["energy_fit"], row["start"], row["dual"], reference_id))
        value, anchor_value = (r["second_order_shift_MeV_formal_not_applied"] for r in (row, reference))
        row["relative_second_order_shift_MeV_formal_not_applied"] = (
            None if value is None or anchor_value is None else value - anchor_value)
    for rel, digest in locked.items():
        assert sha(ROOT / rel) == digest, ("input changed during audit", rel)

    write_csv("photon-checks.csv", photon_rows)
    write_csv("signed-quadrupoles.csv", diagonal_rows)
    write_csv("transition-phase-checks.csv", phase_rows)
    write_csv("nambu-diagnostics.csv", nambu_rows)
    write_csv("nambu-block-norms.csv", block_rows)
    selected_nambu = {}
    for name in fit_names:
        rows = [r for r in nambu_rows if r["energy_fit"] == name and r["recorded_energy_best"] and not r["dual"]]
        selected_nambu[name] = {
            "residual_range_MeV": [min(r["full_Nambu_residual_norm_MeV"] for r in rows),
                                   max(r["full_Nambu_residual_norm_MeV"] for r in rows)],
            "formal_mixing_norm_range": [min(r["first_order_negative_sector_norm_formal"] for r in rows),
                                         max(r["first_order_negative_sector_norm_formal"] for r in rows)],
            "formal_shift_range_MeV": [min(r["second_order_shift_MeV_formal_not_applied"] for r in rows),
                                       max(r["second_order_shift_MeV_formal_not_applied"] for r in rows)],
            "formal_relative_shift_range_MeV": [
                min(r["relative_second_order_shift_MeV_formal_not_applied"] for r in rows),
                max(r["relative_second_order_shift_MeV_formal_not_applied"] for r in rows)],
            "formal_relative_shift_RMS_MeV_excluding_anchor": float(np.sqrt(np.mean([
                r["relative_second_order_shift_MeV_formal_not_applied"] ** 2 for r in rows
                if r["level_id"] != fit_contracts[name]["energy_reference_level"]]))),
        }
    summary = {
        "status": "frozen_predictions_audited;no_core_runner_or_fit_changes",
        "input_hashes": locked, "input_hashes_unchanged_after_audit": True,
        "counts": {"energy_starts": 7, "parameter_sets_including_duals": 14,
                   "photon_rows_checked": len(photon_rows), "mapped_Nambu_state_diagnostics": len(nambu_rows),
                   "signed_diagonal_rows": len(diagonal_rows), "transition_phase_pairs": len(phase_rows)},
        "maximum_absolute_residuals_by_check": METRICS,
        "duality_state_matching": dual_rows,
        "best_start_Nambu_summaries": selected_nambu,
        "rate_convention": "w_gamma(E2)=kE E^5 BQ; w_gamma(M1)=kM E^3 Bj; eta_gamma=kM/kE>=0 has MeV^2; same-parent photon ratio=(wEt+wMt)/wEr",
        "duality_laws": {
            "parameter_map": "gamma'=60-gamma, lambda'=-lambda, J'=(J1,J3,J2), fixed positive gap",
            "frame_rotation": "pi about (0,1,1)/sqrt2; O:(x,y,z)->(-x,z,y); R_I=U_I* tensor U_j",
            "fixed_positive_gap_Nambu_map": "particle/hole swap sigma_x combined with frame rotation",
            "quadrupole": "S_f^dag Q'_D2 S_i=-Q_D2; signed diagonal Q changes sign",
            "particle_j": "S_f^dag j'_D2 S_i=+j_D2",
            "eigenstate_phase_invariant": "Q_fi*j_fi^* is independent of state rephasing, but is ODD under duality; its normalized phase shifts by pi if both amplitudes are nonzero",
            "even_quantities": "|Q|^2,|j|^2, unit B, photon a/b and anchor eta_gamma",
        },
        "Nambu_diagnostic_definition": {
            "retained": "H+=P^dag(U Hrot U+V Hrot V+E)P",
            "other_sector": "H-=P^dag(U Hrot U+V Hrot V-E)P; total eigenvalues need not be negative",
            "omitted_minus_plus_block": "K=P^dag(U Hrot V-V Hrot U)P",
            "residual": "sigma_n=||K v_n||=||H_full X+ v_n-E_n X+ v_n||",
            "formal_mixing_norm": "sqrt(sum_m |<m-|K|n+>|^2/(E_n+-E_m-)^2); NOT a probability or controlled estimate when not small",
            "formal_second_order_shift": "sum_m |<m-|K|n+>|^2/(E_n+-E_m-); diagnostic only, never applied",
            "warning": "This diagnoses the declared eta-discarding projection; it does not validate a full-Nambu nuclear Hamiltonian or repair photon predictions.",
        },
        "source_locator": {
            "raw_file": str(MEYER.relative_to(ROOT)),
            "printed_pages": "117 Eqs2.19-2.22;118 Eqs2.28-2.31;119 Eq2.33;120 Eqs2.40-2.41",
            "publisher_reproductions_local_only": "tmp/ba129-model-readiness/observable-review/",
        },
        "review_items": [
            "No arithmetic error found in a/b, same-parent normalization, actual ordinal selection, or sole-anchor calibration for this frozen dataset.",
            "The central floors and failed withheld ratios constrain the frozen mapping/model/operator assumptions; they are not a statistical or model-family exclusion.",
            "EM duality difference is recorded by runner but omitted from its failure condition (runner lines172-182); current data satisfy the symmetry.",
            "Chronological predeclaration is declared by contract, not independently established by this read-only code/data audit.",
        ],
    }
    write("audit-results.json", json.dumps(summary, indent=2, ensure_ascii=False, allow_nan=False) + "\n")
    print(json.dumps({"counts": summary["counts"], "checks": METRICS,
                      "best_start_Nambu_summaries": selected_nambu}, indent=2))


if __name__ == "__main__":
    main()
