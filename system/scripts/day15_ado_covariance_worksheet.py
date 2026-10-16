#!/usr/bin/env python3
"""Day15 synthetic ADO worksheet with an explicit correlated input model.

This is a reproducible L2 exercise, never an experimental multipolarity fit.
Zheng2002 Eq.(1),(3)-(5) supply the separable group-response convention.
The counts, efficiencies, angular coefficients and covariance are chosen inputs.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path

import numpy as np
from scipy.special import eval_legendre


INPUT_NAMES = ["net_S", "net_L", "log_eff_target_S", "log_eff_target_L",
               "log_eff_gate_S", "log_eff_gate_M", "log_eff_gate_L",
               "gate_A2", "gate_A4", "independent_intrinsic_ratio"]
OUTPUT_NAMES = ["R_ADO", "f_geometry", "intrinsic_ratio_geometry",
                "f_independent_reference"]


def geometry(cfg: dict, half_cone_deg: float = 0.0) -> tuple[np.ndarray, np.ndarray]:
    theta = np.deg2rad([g["theta_deg"] for g in cfg["groups"]])
    moments = []
    for k in (2, 4):
        q = 1.0
        if half_cone_deg > 0:
            c = np.cos(np.deg2rad(half_cone_deg))
            q = (eval_legendre(k - 1, c) - eval_legendre(k + 1, c)) / ((2*k+1)*(1-c))
        moments.append(q * eval_legendre(k, np.cos(theta)))
    return moments[0], moments[1]


def evaluate(v: np.ndarray, cfg: dict, half_cone_deg: float = 0.0) -> np.ndarray:
    p2, p4 = geometry(cfg, half_cone_deg)
    w = 1 + v[..., 7, None]*p2 + v[..., 8, None]*p4
    b = np.exp(v[..., 4:7]) * w
    c = b.sum(axis=-1)
    ns, nl = cfg["groups"][0]["detector_count"], cfg["groups"][2]["detector_count"]
    numerator, denominator = c-b[..., 0]/ns, c-b[..., 2]/nl
    if np.any(v[..., :2] <= 0) or np.any(v[..., 9] <= 0) or np.any(w <= 0):
        raise ValueError("Nonpositive count/reference/gate response; no samples are silently dropped")
    if np.any(numerator <= 0) or np.any(denominator <= 0):
        raise ValueError("Undefined self-exclusion ratio")
    ratio = (v[..., 0]/v[..., 1]) * np.exp(v[..., 3]-v[..., 2])
    f = numerator/denominator
    return np.stack([ratio, f, ratio/f, ratio/v[..., 9]], axis=-1)


def input_model(cfg: dict) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    counts, cal, gate = cfg["counts"], cfg["calibration"], cfg["gate"]
    ks, kl, bg = (counts[k] for k in ("background_scale_S", "background_scale_L", "shared_sideband"))
    means = np.array([counts["gross_S"]-ks*bg, counts["gross_L"]-kl*bg])
    target = [cfg["groups"][i]["target_efficiency"] for i in (0, 2)]
    eg = [g["gate_efficiency"] for g in cfg["groups"]]
    v = np.r_[means, np.log(target + eg), gate["A2"], gate["A4"],
              cfg["independent_intrinsic_ratio"]["value"]]
    cov = np.zeros((10, 10))
    cov[:2, :2] = [[counts["gross_S"]+ks*ks*bg, ks*kl*bg],
                  [ks*kl*bg, counts["gross_L"]+kl*kl*bg]]
    # Columns are one common scale, S/M/L geometry, and five independent residuals.
    loading = np.zeros((5, 9))
    loading[:, 0] = cal["common_log_sd"]
    for row, group in enumerate((0, 2, 0, 1, 2)):
        loading[row, 1+group] = cal["group_geometry_log_sd"]
        loading[row, 4+row] = cal["target_residual_log_sd"] if row < 2 else cal["gate_residual_log_sd"]
    cov[2:7, 2:7] = loading @ loading.T
    cov[7:9, 7:9] = gate["coefficient_covariance"]
    cov[9, 9] = cfg["independent_intrinsic_ratio"]["standard_uncertainty"]**2
    return v, cov, loading


def analytic_jacobian(v: np.ndarray, cfg: dict) -> np.ndarray:
    y = evaluate(v, cfg)
    p2, p4 = geometry(cfg)
    eg = np.exp(v[4:7])
    b = eg*(1+v[7]*p2+v[8]*p4)
    c = b.sum()
    ns, nl = cfg["groups"][0]["detector_count"], cfg["groups"][2]["detector_count"]
    ah, al = np.ones(3), np.ones(3)
    ah[0] -= 1/ns
    al[2] -= 1/nl
    dlogf_db = ah/(c-b[0]/ns) - al/(c-b[2]/nl)
    dlogr = np.zeros(10)
    dlogr[:4] = [1/v[0], -1/v[1], -1, 1]
    dlogf = np.zeros(10)
    dlogf[4:7] = b*dlogf_db
    dlogf[7:9] = [np.dot(eg*p2, dlogf_db), np.dot(eg*p4, dlogf_db)]
    dlogfe = dlogr.copy()
    dlogfe[9] = -1/v[9]
    return np.array([y[0]*dlogr, y[1]*dlogf, y[2]*(dlogr-dlogf), y[3]*dlogfe])


def monte_carlo(cfg: dict, v: np.ndarray, loading: np.ndarray) -> np.ndarray:
    rng = np.random.default_rng(cfg["random_seed"])
    m, counts = cfg["monte_carlo_replicates"], cfg["counts"]
    draws = np.broadcast_to(v, (m, 10)).copy()
    primitive = rng.poisson([counts["gross_S"], counts["gross_L"], counts["shared_sideband"]], (m, 3))
    draws[:, 0] = primitive[:, 0]-counts["background_scale_S"]*primitive[:, 2]
    draws[:, 1] = primitive[:, 1]-counts["background_scale_L"]*primitive[:, 2]
    draws[:, 2:7] += rng.standard_normal((m, 9)) @ loading.T
    draws[:, 7:9] += rng.multivariate_normal([0, 0], cfg["gate"]["coefficient_covariance"], m)
    draws[:, 9] += rng.normal(0, cfg["independent_intrinsic_ratio"]["standard_uncertainty"], m)
    return evaluate(draws, cfg)


def save_csv(path: Path, columns: list[str], rows: list | np.ndarray) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(columns)
        writer.writerows(rows)


def make_figure(out: Path, data: dict, audit_dir: Path) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    sys.path.insert(0, str(audit_dir))
    from audit_panel_alignment import require_matplotlib_panel_alignment

    plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["DejaVu Sans"],
                         "font.size": 8, "axes.titlesize": 8, "axes.labelsize": 8,
                         "xtick.labelsize": 7.5, "ytick.labelsize": 7.5, "legend.fontsize": 7,
                         "svg.fonttype": "none", "pdf.fonttype": 42,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "axes.linewidth": .7})
    fig, axes = plt.subplots(1, 2, figsize=(7.204724409, 3.070866142))  # 183 x 78 mm
    fig.subplots_adjust(left=.092, right=.98, bottom=.21, top=.78, wspace=.36)
    e = np.array(data["efficiency_sensitivity"])
    c = np.array(data["background_correlation_sensitivity"])
    ax = axes[0]
    ax.plot(100*(e[:, 0]-1), e[:, 1], color="#737373", ls="--", label="R (measured convention)")
    ax.plot(100*(e[:, 0]-1), e[:, 2], color="#35698F", label="Corrected r = R / f")
    ax.axvline(0, color="#B7B7B7", lw=.7, zorder=0)
    ax.set(xlabel="Efficiency-ratio offset (%)", ylabel="Dimensionless angular ratio")
    ax.legend(loc="upper right", frameon=False, handlelength=1.8)
    ax = axes[1]
    ax.plot(c[:, 0], c[:, 1], color="#35698F", label="Full calibration Cov")
    ax.axhline(data["standard_uncertainty_diagonal"][2], color="#B3763C", ls="--", label="All scalar inputs independent")
    ax.scatter([1], [data["standard_uncertainty_full"][2]], s=15, color="#35698F", zorder=3)
    ax.set(xlabel="Chosen background correlation", ylabel="Standard uncertainty of r", xlim=(-1.05, 1.05))
    ax.legend(loc="upper right", frameon=False, handlelength=1.8)
    for i, (ax, title) in enumerate(zip(axes, ("Efficiency sensitivity", "Covariance sensitivity"))):
        ax.text(-.14, 1.14, chr(97+i), transform=ax.transAxes, fontweight="bold", fontsize=9)
        ax.set_title(title, loc="left", pad=14)
        ax.tick_params(direction="out", length=3)
    fig.text(.5, .955, "Synthetic worksheet: chosen inputs, no experimental data", ha="center", va="top", fontsize=8)
    fig.canvas.draw()
    require_matplotlib_panel_alignment(fig, json_out=out/"ado-covariance-sensitivity.alignment.json",
                                       overlay_svg=out/"ado-covariance-sensitivity.alignment.svg",
                                       require_panel_labels=True, strict=True)
    fig.savefig(out/"ado-covariance-sensitivity.svg")
    fig.savefig(out/"ado-covariance-sensitivity.pdf")
    fig.savefig(out/"ado-covariance-sensitivity.png", dpi=300)
    svg_path = out/"ado-covariance-sensitivity.svg"
    svg_path.write_text("\n".join(line.rstrip(" \t") for line in svg_path.read_text(encoding="utf-8").splitlines())+"\n", encoding="utf-8")
    plt.close(fig)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--plot-audit-dir", type=Path)
    args = parser.parse_args()
    cfg = json.loads(args.input.read_text(encoding="utf-8"))
    if cfg["angle_unit"] != "degree" or [g["label"] for g in cfg["groups"]] != ["S", "M", "L"]:
        raise ValueError("Explicit degree and S/M/L conventions required")
    if any(g["detector_count"] != 4 for g in cfg["groups"]):
        raise ValueError("This fixed worksheet's independent pair control uses four detectors per group")
    v, cov, loading = input_model(cfg)
    y, jac = evaluate(v, cfg), analytic_jacobian(v, cfg)
    eig = np.linalg.eigvalsh(cov)
    assert eig.min() >= -1e-12
    numerical = np.empty_like(jac)
    for k in range(10):
        h = 1e-5*max(abs(v[k]), 1.)
        hi, lo = v.copy(), v.copy()
        hi[k] += h
        lo[k] -= h
        numerical[:, k] = (evaluate(hi, cfg)-evaluate(lo, cfg))/(2*h)
    assert np.allclose(jac, numerical, rtol=3e-6, atol=1e-9)
    propagated = jac @ cov @ jac.T
    sigma = np.sqrt(np.diag(propagated))
    diag_sigma = np.sqrt(np.einsum("ij,j,ij->i", jac, np.diag(cov), jac))
    delta_f = y[3]-y[1]
    delta_f_sigma = np.sqrt(propagated[3, 3]+propagated[1, 1]-2*propagated[3, 1])
    # The same global normalization must cancel, at both energies and in Eq.(4).
    shift = v.copy()
    shift[2:7] += np.log(3.7)
    assert np.allclose(evaluate(shift, cfg), y, rtol=1e-13)
    assert np.allclose(jac[:, 2:7] @ loading[:, 0], 0., atol=1e-13)
    p2, p4 = geometry(cfg)
    wt = np.repeat([v[9], 1., 1.], 4)
    et = np.concatenate([np.repeat(g["target_efficiency"]/4, 4) for g in cfg["groups"]])
    bg = np.exp(v[4:7])*(1+v[7]*p2+v[8]*p4)
    gate_det = np.repeat(bg/4, 4)
    pair = wt[:, None]*et[:, None]*gate_det[None, :]
    np.fill_diagonal(pair, 0.)
    pair_ratio = pair[:4].sum()/pair[8:].sum()/(cfg["groups"][0]["target_efficiency"]/cfg["groups"][2]["target_efficiency"])
    assert np.isclose(pair_ratio/v[9], y[1], rtol=1e-13)
    simulated = monte_carlo(cfg, v, loading)
    mc_sigma = simulated.std(axis=0, ddof=1)
    assert np.all(np.abs(mc_sigma/sigma-1) < .025)
    # No count/reference proxy is manufactured to eliminate the r*f degeneracy.
    equivalent = [[float(y[0]/f), f] for f in (.85, 1., 1.10)]
    assert all(np.isclose(r*f, y[0]) for r, f in equivalent)
    identifiability_rank = int(np.linalg.matrix_rank(np.array([[y[1], y[2]]])))
    assert identifiability_rank == 1
    sensitivity = [[q, y[0]/q, y[2]/q] for q in np.linspace(.96, 1.04, 161)]
    rho_rows = []
    ks, kl, bg_n = (cfg["counts"][k] for k in ("background_scale_S", "background_scale_L", "shared_sideband"))
    for rho in np.linspace(-1, 1, 201):
        changed = cov.copy()
        changed[0, 1] = changed[1, 0] = rho*ks*kl*bg_n
        assert np.linalg.eigvalsh(changed).min() >= -1e-12
        rho_rows.append([rho, np.sqrt(jac[2] @ changed @ jac[2])])
    gate_alt = v.copy()
    gate_alt[7:9] = [-.30, 0.]
    alt = evaluate(gate_alt, cfg)
    cone = evaluate(v, cfg, half_cone_deg=20.)
    result = {
        "data_identity": cfg["data_identity"], "data_kind": cfg["data_kind"],
        "input_path": str(args.input), "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "input_names": INPUT_NAMES, "input_vector": v.tolist(), "input_covariance": cov.tolist(),
        "log_efficiency_latent_loading": loading.tolist(), "output_names": OUTPUT_NAMES,
        "central": dict(zip(OUTPUT_NAMES, map(float, y))), "analytic_jacobian": jac.tolist(),
        "output_covariance": propagated.tolist(), "standard_uncertainty_full": sigma.tolist(),
        "standard_uncertainty_diagonal": diag_sigma.tolist(),
        "independent_route_comparison": {"difference_f_empirical_minus_geometry": float(delta_f),
                                         "difference_standard_uncertainty": float(delta_f_sigma),
                                         "included_cross_covariance": float(propagated[3, 1]),
                                         "standardized_difference_chosen_model": float(delta_f/delta_f_sigma),
                                         "interpretation": "Internal closure of chosen inputs, not evidence for an experimental response"},
        "variance_components": {name: np.diag(jac[:, sl] @ cov[sl, sl] @ jac[:, sl].T).tolist()
                                for name, sl in [("counts", slice(0, 2)), ("log_efficiencies", slice(2, 7)),
                                                 ("gate_coefficients", slice(7, 9)), ("intrinsic_reference", slice(9, 10))]},
        "monte_carlo": {"seed": cfg["random_seed"], "replicates": len(simulated), "discarded": 0,
                        "mean": simulated.mean(axis=0).tolist(), "standard_deviation": mc_sigma.tolist(),
                        "ratio_to_linear_sigma": (mc_sigma/sigma).tolist(),
                        "interpretation": "Chosen sampling model check; not an experimental CI or unbiasedness proof"},
        "controls": {"covariance_psd_min_eigenvalue": float(eig.min()),
                     "gradient_max_abs_discrepancy": float(np.max(np.abs(jac-numerical))),
                     "global_scale_change": 3.7, "global_scale_cancels": True,
                     "ordered_pair_f": float(pair_ratio/v[9]),
                     "unknown_intrinsic_and_f": {"rank": identifiability_rank, "equivalent_r_f": equivalent},
                     "gate_change": {"A2": -.30, "A4": 0., "f": float(alt[1]),
                                     "expected_R_if_same_intrinsic_r0": float(v[9]*alt[1]),
                                     "baseline_expected_R_if_same_intrinsic_r0": float(v[9]*y[1]),
                                     "scope": "Design predictions within the separable response, not measured gate dependence"},
                     "gate_finite_cone_20_degrees": {"f": float(cone[1]),
                                                   "scope": "Only the gate single-photon moments are averaged; target angular response and full pair kernel remain unspecified"}},
        "efficiency_sensitivity": sensitivity, "background_correlation_sensitivity": rho_rows,
        "boundaries": cfg["response_assumptions"] + ["Actual events, response and covariance are unavailable; this exercise assigns no real multipolarity"]}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir/"ado-covariance-worksheet.json").write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    save_csv(args.output_dir/"ado-efficiency-sensitivity.csv", ["efficiency_ratio_relative", "R_ADO", "intrinsic_ratio_geometry"], sensitivity)
    save_csv(args.output_dir/"ado-background-covariance-sensitivity.csv", ["background_estimator_correlation", "standard_uncertainty_intrinsic_ratio"], rho_rows)
    if args.plot_audit_dir:
        make_figure(args.output_dir, result, args.plot_audit_dir)
    print(json.dumps({"data_identity": cfg["data_identity"], "central": result["central"],
                      "sigma_full": sigma.tolist(), "sigma_diagonal": diag_sigma.tolist(),
                      "mc_sigma_relative": result["monte_carlo"]["ratio_to_linear_sigma"],
                      "input_sha256": result["input_sha256"], "controls_passed": True}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
