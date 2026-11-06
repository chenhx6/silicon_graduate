"""Independent case wrapper/source comparison; fixed inputs, no parameter fit.

Uses the existing, SHA-locked single_j_ibfm eigensolver, NOT a second kernel.
Does not invoke ba129_ibfm_prediction.run, transition_rme or core calibration.
Recomputes case-level normalization and photon arithmetic from direct matrix
contractions, and compares to a previously frozen SOURCE-ONLY extraction.
All writes are confined to this review directory.
"""

import csv
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import sys
import time

import numpy as np

ROOT = Path("/workspace/wiki")
OUT = ROOT/"outputs/l4/20261105-ba129-controlled-pairing/ibfm-case-review"
PREDICTION = ROOT/"outputs/l4/20261105-ba129-controlled-pairing/ibfm-case-v1/prediction.json"
SOURCE_POINTS = OUT/"source-points-frozen.json"
SOURCE_SHA = "46b90e618a4c95c377bb61c7f59eb782d05c3f35f4be5418f0dded1d784ac45d"
PREDICTION_SHA = "6dd5371fcaa7d2647e60490d15ca7e2816a1a517756af59515923167f6d1a2a4"

sys.path.insert(0, str(ROOT/"system/scripts/analysis"))
from single_j_ibfm import IBFMParameters, CoreParameters, IBFMKernel, BosonCore
from paired_single_j_em import clebsch_gordan


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def exact_index(solution, tj, ordinal):
    indices = solution.indices_for_J(tj)
    return int(indices[ordinal])


def direct_rme(solution, block_matrix, i, f, rank):
    """Explicit same-M Wigner--Eckart contraction, no production RME routine."""
    ji, jf = int(solution.two_J[i]), int(solution.two_J[f])
    value = np.vdot(solution.vectors[:, f], block_matrix @ solution.vectors[:, i])
    if abs(jf-ji) > 2*rank or jf+ji < 2*rank:
        assert abs(value) < 1e-10
        return 0j
    m = int(solution.basis.two_M)
    cg = clebsch_gordan(ji, m, 2*rank, 0, jf, m)
    if cg == 0:
        raise ValueError("An allowed RME has an unusable q=0 CG denominator")
    return complex(value*math.sqrt(jf+1)/cg)


def write_csv(name, rows):
    with (OUT/name).open("x", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def run():
    started = time.perf_counter()
    assert sha(SOURCE_POINTS) == SOURCE_SHA
    assert sha(PREDICTION) == PREDICTION_SHA
    frozen = load(SOURCE_POINTS)
    pred = load(PREDICTION)
    locked = {ROOT/k: v for k, v in pred["input_sha256"].items()}
    locked[PREDICTION] = PREDICTION_SHA
    locked[SOURCE_POINTS] = SOURCE_SHA
    archive = ROOT/frozen["archive"]
    locked[archive] = frozen["archive_sha256"]
    for path, digest in locked.items():
        assert sha(path) == digest, f"Protected input changed: {path}"
    contract = load(ROOT/"outputs/l4/20261105-ba129-controlled-pairing/ibfm-test-contract.json")
    photon_contract = load(ROOT/contract["photon_contract"])
    energy_contract = load(ROOT/"outputs/l4/20261105-ba129-model-readiness/energy-fit-contract.json")
    p = IBFMParameters(**pred["parameters"])
    assert asdict(p) == dict(n_b=8, two_j=11, eps_d=.03, kappa=-.102,
                            chi=-.18, v2=.453, Q_jj=-math.sqrt(525/(143*math.pi)),
                            Gamma0=.6, Lambda0=2.1, A0=-.15)
    assert contract["hamiltonian_inputs"]["boson_core"] == "128Ba"

    # Re-solve the exact declared case. No source-plot number enters the Hamiltonian.
    core = BosonCore(CoreParameters(p.n_b, p.eps_d, p.kappa, p.chi))
    cs = core.solve()
    kernel = IBFMKernel(p)
    sol = kernel.solve()
    i0, i2 = exact_index(cs, 0, 0), exact_index(cs, 4, 0)
    i9 = exact_index(sol, 9, 0)
    assert i0 == np.argmin(cs.energies) and i9 == np.argmin(sol.energies)

    comparison = []
    for fig in frozen["figures"]:
        is_core = fig["figure"] == "even.level.pdf"
        s, origin = (cs, i0) if is_core else (sol, i9)
        for point in fig["points"]:
            idx = exact_index(s, point["two_J"], point["ordinal"])
            exact = float(1000*(s.energies[idx]-s.energies[origin]))
            source = point["reported_plot_grid_energy_keV"]
            comparison.append(dict(
                nucleus="128Ba" if is_core else "129Ba",
                state=point["state"], two_J=point["two_J"], ordinal=point["ordinal"],
                source_locator=fig["locator"], vector_path=point["path_index"],
                source_vector_energy_keV=point["recovered_energy_keV"],
                source_display_energy_keV=source, declared_model_energy_keV=exact,
                model_minus_display_keV=exact-source,
                within_nearest_keV_half_width=bool(abs(exact-source) <= .5),
                within_1keV=bool(abs(exact-source) <= 1),
            ))
    # Verify every core level stored by the parent, not only the plot subset.
    core_record_error = max(
        abs(1000*(cs.energies[exact_index(cs, r["two_J"], r["ordinal"])]-cs.energies[i0])
            - r["excitation_keV"]) for r in pred["core_levels"])
    assert core_record_error < 1e-8

    mapping = {}
    reference_id = energy_contract["energy_reference_level"]
    for row in energy_contract["energy_data"]:
        mapping[row["level_id"]] = dict(row, spectrum_index=exact_index(
            sol, row["twice_I"], row["model_ordinal_assumed"]))
    reference = mapping[reference_id]
    energy_rows = []
    maximum_record_error = 0.
    for recorded in pred["energy_comparison"]:
        r = mapping[recorded["level_id"]]
        assert r["spectrum_index"] == recorded["spectrum_index"]
        exact = float(1000*(sol.energies[r["spectrum_index"]]
                          - sol.energies[reference["spectrum_index"]]))
        observed = r["energy_keV"]-reference["energy_keV"]
        residual = exact-observed
        maximum_record_error = max(maximum_record_error, abs(exact-recorded["model_relative_energy_keV"]),
                                   abs(residual-recorded["residual_keV"]))
        plotted = r["model_ordinal_assumed"] == 0 and r["twice_I"] in (7, 9, 11, 13, 15, 17)
        energy_rows.append(dict(
            level_id=r["level_id"], two_J=r["twice_I"], ordinal=r["model_ordinal_assumed"],
            model_relative_energy_keV=exact, observed_relative_energy_keV=observed,
            residual_keV=residual, in_published_theory_subset=plotted,
            is_fixed_reference=r["level_id"] == reference_id,
        ))
    rms_rows = [r for r in energy_rows if not r["is_fixed_reference"]]
    rms = float(np.sqrt(np.mean([r["residual_keV"]**2 for r in rms_rows])))
    assert abs(rms-pred["energy_RMS_keV_not_refitted"]) < 1e-8
    assert maximum_record_error < 1e-8

    # Directly inspect the fixed ENSDF rows for the core calibration, not a current
    # database substitute. Eq. uses half-life, not mean lifetime.
    ens_path = ROOT/"raw/papers/gpt/query/20261105-ba129-core-constraints/nndc128-adopted-text.ens"
    ens = ens_path.read_text().splitlines()
    lev, gam = ens[47], ens[50]
    assert lev[7] == "L" and gam[7] == "G"
    assert float(lev[9:19]) == 284.00 and lev[21:39].strip() == "2+"
    assert gam[31:41].strip() == "E2" and float(gam[21:29]) == 100
    half = float(lev[39:49].split()[0])
    half_error = float(lev[49:55])
    eg = float(gam[9:19])/1000
    alpha = float(gam[55:62])
    assert half == 105 and half_error == 9 and eg == .2841 and alpha == .0539
    rate_constant = contract["EM_inputs"]["core_calibration"]["rate_coefficient_s-1_MeV-5_per_e2b2"]
    Bdown = math.log(2)/(half*1e-12*(1+alpha)*rate_constant*eg**5)
    assert abs(Bdown-pred["core_calibration"]["target_B_2_to_0_e2b2"]) < 1e-14
    chi_prime = contract["EM_inputs"]["chi_E2"]
    core_Q0 = core.bosons.quadrupole(chi_prime)[0]
    core_block = cs.basis.restrict(core_Q0)
    core_component = np.vdot(cs.vectors[:, i2], core_block @ cs.vectors[:, i0])
    unit_Bup = float(5*abs(core_component)**2)  # CG(0 0,2 0|2 0)=1.
    eB = math.sqrt(5*Bdown/unit_Bup)
    eF = contract["EM_inputs"]["e_F_eb"]
    assert abs(eB-pred["core_calibration"]["eB"]) < 1e-13
    assert abs(unit_Bup-pred["core_calibration"]["unit_B_0_to_2"]) < 1e-10

    # Build physical E2 from its two separately exposed tensors, then divide by eB.
    q0 = sol.basis.restrict(kernel.core_quadrupole(chi_prime).components[0])
    f0 = sol.basis.restrict(kernel.fermion_unit_tensor(2).components[0])
    physical_Q0 = eB*q0-eF*(1-2*p.v2)*p.Q_jj/math.sqrt(5)*f0
    normalized_Q0 = physical_Q0/eB
    j0 = sol.basis.restrict(kernel.particle_j().components[0])
    l0 = sol.basis.restrict(kernel.core_L().components[0])
    producer_Q0 = sol.basis.restrict(kernel.e2(1, eF/eB, chi_prime).components[0])
    normalization_error = float(np.max(abs((producer_Q0-normalized_Q0).data), initial=0))
    assert normalization_error < 1e-13
    direct_rows = []
    numeric_comparisons = []
    for row, old in zip(photon_contract["pairs"], pred["photon_pairs"]):
        assert row["parent_id"] == old["parent_id"] and row["role"] == old["role"]
        ip, it, ir = [mapping[row[k]]["spectrum_index"] for k in
                      ("parent_id", "target_final_id", "reference_final_id")]
        assert abs(int(sol.two_J[ip])-int(sol.two_J[it])) == 2
        assert abs(int(sol.two_J[ip])-int(sol.two_J[ir])) == 4
        stat = int(sol.two_J[ip])+1
        qt, qr = [direct_rme(sol, normalized_Q0, ip, f, 2) for f in (it, ir)]
        jt, jr = [direct_rme(sol, j0, ip, f, 1) for f in (it, ir)]
        lt = direct_rme(sol, l0, ip, it, 1)
        assert abs(jr) < 1e-10 and abs(jt+lt) < 1e-9
        bqt, bqr, bjt = [float(abs(x)**2/stat) for x in (qt, qr, jt)]
        et, er = row["target_energy_MeV"], row["reference_energy_MeV"]
        a = (et/er)**5*bqt/bqr
        b = et**3/er**5*bjt/bqr
        ratio = row["target_RI"]/row["reference_RI"]
        assert abs(ratio-row["reported_photon_ratio"]) < 1e-14
        for field, value in [
            ("unit_BQ_target", bqt), ("unit_BQ_reference", bqr), ("unit_Bj_target", bjt),
            ("physical_BE2_target_e2b2", eB**2*bqt),
            ("physical_BE2_reference_e2b2", eB**2*bqr),
            ("electric_ratio_a", a), ("magnetic_ratio_coefficient_b_per_MeV2", b),
        ]:
            numeric_comparisons.append(dict(field=field, target_keV=1000*et,
                                            absolute_difference=abs(value-old[field])))
            assert abs(value-old[field]) < 2e-10*max(1., abs(old[field]))
        assert abs(qt-complex(*old["signed_RME_Q_normalized"])) < 1e-9
        assert abs(jt-complex(*old["signed_RME_j"])) < 1e-9
        model_et = float(1000*(sol.energies[ip]-sol.energies[it]))
        model_er = float(1000*(sol.energies[ip]-sol.energies[ir]))
        direct_rows.append(dict(
            target_keV=1000*et, reference_keV=1000*er, role=row["role"],
            parent_id=row["parent_id"], target_final_id=row["target_final_id"],
            reference_final_id=row["reference_final_id"],
            electric_ratio_a=a, magnetic_ratio_b_MeV_minus2=b, reported_ratio=ratio,
            model_target_energy_keV=model_et, model_reference_energy_keV=model_er,
            target_downward_in_model=bool(model_et > 0),
            reference_downward_in_model=bool(model_er > 0),
            unit_BQ_target=bqt, unit_BQ_reference=bqr, unit_Bj_target=bjt,
            core_L_plus_particle_j_RME_abs=float(abs(lt+jt)),
            target_RME_Q_real=qt.real, target_RME_j_real=jt.real,
        ))
    anchors = [r for r in direct_rows if r["role"] == "scale-calibration"]
    assert len(anchors) == 1
    anchor = anchors[0]
    assert abs(anchor["target_keV"]-153.8) < 1e-9 and abs(anchor["reference_keV"]-518.6) < 1e-9
    eta = (anchor["reported_ratio"]-anchor["electric_ratio_a"])/anchor["magnetic_ratio_b_MeV_minus2"]
    assert eta >= 0 and abs(eta-pred["anchor_eta_MeV2"]) < 1e-9
    for r, old in zip(direct_rows, pred["photon_pairs"]):
        a, b = r["electric_ratio_a"], r["magnetic_ratio_b_MeV_minus2"]
        estimate = a+eta*b
        r.update(
            recomputed_prediction=estimate, prediction_over_reported=estimate/r["reported_ratio"],
            radiative_E2_fraction=a/estimate,
            eta_required_for_this_central_ratio_MeV2=(r["reported_ratio"]-a)/b,
            E2_alone_exceeds_central_ratio=bool(a > r["reported_ratio"]),
            producer_prediction_difference=estimate-old["predicted_photon_ratio"],
        )
        assert abs(r["producer_prediction_difference"]) < 1e-9
    results = {
        "declared_review_date": "2026-11-06",
        "run_directory_label_retained": "20261105",
        "container_observed_utc": datetime.now(timezone.utc).isoformat(),
        "date_boundary": "Review date follows user instruction. Machine UTC timestamps are retained as observed; no run directory renamed.",
        "source_only_freeze_sha256": SOURCE_SHA,
        "prediction_sha256": PREDICTION_SHA,
        "independence": "New source-vector extraction and case arithmetic; same SHA-locked numerical kernel, not independent diagonalization software or original PBOS.",
        "parameters_unchanged": asdict(p),
        "source_comparison": comparison,
        "core_record_max_difference_keV": core_record_error,
        "energy_record_max_difference_keV": maximum_record_error,
        "energy_comparison": energy_rows,
        "energy_RMS": {
            "mapped_states": len(energy_rows), "residuals_excluding_fixed_reference": len(rms_rows),
            "RMS_keV": rms,
            "including_zero_reference_RMS_keV_for_denominator_clarity": float(np.sqrt(np.mean([r["residual_keV"]**2 for r in energy_rows]))),
            "boundary": "Unweighted descriptive residual, not experimental chi-square or a refit.",
        },
        "core_calibration_audit": {
            "ENSDF_locator": "128Ba adopted lines 48-53",
            "T_half_ps": half, "quoted_T_half_error_ps": half_error,
            "Egamma_MeV": eg, "alpha_total": alpha, "rate_coefficient_declared": rate_constant,
            "recomputed_Bdown_e2b2": Bdown, "unit_Bup": unit_Bup,
            "recomputed_eB_eb": eB, "eF_eb": eF, "eF_over_eB": eF/eB,
            "normalized_Q0_matrix_max_difference": normalization_error,
            "boundary": "Central adopted-input calibration. No uncertainty propagation, author eB certification or new lifetime measurement.",
        },
        "anchor_eta_MeV2": eta,
        "photon_comparison": direct_rows,
        "photon_numeric_field_checks": numeric_comparisons,
        "core_diagnostics": dict(cs.diagnostics),
        "odd_diagnostics": dict(sol.diagnostics),
        "runtime_seconds": time.perf_counter()-started,
        "files_unchanged": {str(path.relative_to(ROOT)): digest for path, digest in locked.items()},
        "boundaries": [
            "Source plots independently calibrate only their displayed theoretical subset.",
            "No Hamiltonian or state-map adjustment and no 130Ba/NB7 substitution.",
            "No claim of original producer/code/run-card identity or complete electromagnetic source replay.",
            "Measured photon energies are used as frozen by the protocol, not model energy differences.",
            "No p-value, posterior, confidence interval, signed physical delta or collective-mode verdict.",
        ],
    }
    for path, digest in locked.items():
        assert sha(path) == digest, f"Input changed during audit: {path}"
    with (OUT/"case-audit.json").open("x", encoding="utf-8") as stream:
        json.dump(results, stream, indent=2, allow_nan=False)
        stream.write("\n")
    write_csv("source-comparison.csv", comparison)
    write_csv("energy-comparison.csv", energy_rows)
    write_csv("photon-comparison.csv", direct_rows)
    for row in comparison:
        print("SOURCE",row["nucleus"],row["state"],row["source_display_energy_keV"],
              row["declared_model_energy_keV"],row["model_minus_display_keV"])
    print("ENERGY_RMS",results["energy_RMS"])
    print("E2",results["core_calibration_audit"])
    for row in direct_rows:
        print("PHOTON",row["target_keV"],row["recomputed_prediction"],row["reported_ratio"],
              "model_Et",row["model_target_energy_keV"],
              "eta_required",row["eta_required_for_this_central_ratio_MeV2"])
    print("RUNTIME",results["runtime_seconds"])


if __name__ == "__main__":
    run()
