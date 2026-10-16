#!/usr/bin/env python3
"""Exact chosen event-mixing statistics; no GRIFFIN event or detector fit.

Each iid physical event has two binary tags X,Y. Prompt pairs use the same
event; each trigger mixes with K distinct other events, independently by row.
An equality-bin kernel is deliberately chosen to expose event reuse and its
degenerate limit. The real production mixer and its covariance are unavailable.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np


STATES = ((0, 0), (0, 1), (1, 0), (1, 1))


def moments(p: F, q: F, c: F) -> dict:
    r = p*q+c
    prob = (1-p-q+r, q-r, p-r, r)
    if min(prob) < 0 or sum(prob) != 1:
        raise ValueError("Unphysical binary joint probabilities")
    a, m = prob[0]+prob[3], p*q+(1-p)*(1-q)
    influence = lambda z: (2*q-1)*(z[0]-p)+(2*p-1)*(z[1]-q)
    v1 = sum(w*influence(z)**2 for z, w in zip(STATES, prob))
    cross = sum(w*(F(int(z[0] == z[1]))-a)*influence(z) for z, w in zip(STATES, prob))
    hs = lambda z, u: F(int(z[0] == u[1])+int(u[0] == z[1]), 2)
    vh = sum(w*t*(hs(z, u)-m)**2 for z, w in zip(STATES, prob) for u, t in zip(STATES, prob))
    return {"p": p, "q": q, "c": c, "prob": prob, "prompt_mean": a, "mixed_mean": m,
            "prompt_variance_coefficient": a*(1-a), "first_order_coefficient": v1,
            "second_order_coefficient": 2*vh-v1, "cross_covariance_coefficient": cross}


def theory(mo: dict, n: int, k: int) -> dict:
    if not (n >= 2 and 1 <= k < n):
        raise ValueError("Need fixed N>=2 and 1<=K<=N-1")
    va = mo["prompt_variance_coefficient"]/n
    vb_all = mo["first_order_coefficient"]/n+mo["second_order_coefficient"]/(n*(n-1))
    pairing_noise = mo["q"]*(1-mo["q"])*F(n-1-k, n*(n-1)*k)
    return {"var_prompt": va, "var_mixed_all": vb_all, "var_pair_selection": pairing_noise,
            "var_mixed": vb_all+pairing_noise, "cov_prompt_mixed": mo["cross_covariance_coefficient"]/n}


def enumerate_small(mo: dict, n: int, k: int | None = None) -> dict:
    """Independent exact enumeration of states and, optionally, partner choices."""
    sums = [F(0) for _ in range(5)]
    zero = F(0)
    for ids in itertools.product(range(4), repeat=n):
        states = [STATES[t] for t in ids]
        w = math.prod(mo["prob"][t] for t in ids)
        a = F(sum(x == y for x, y in states), n)
        if k is None:
            bs = [F(sum(states[i][0] == states[j][1] for i in range(n) for j in range(n) if i != j), n*(n-1))]
        else:
            rows = [list(itertools.combinations([j for j in range(n) if j != i], k)) for i in range(n)]
            bs = [F(sum(states[i][0] == states[j][1] for i in range(n) for j in selected[i]), n*k)
                  for selected in itertools.product(*rows)]
        for b in bs:
            v = w/len(bs)
            for i, value in enumerate((a, b, a*a, b*b, a*b)):
                sums[i] += v*value
            if b == 0:
                zero += v
    ma, mb, aa, bb, ab = sums
    return {"mean_prompt": ma, "mean_mixed": mb, "var_prompt": aa-ma*ma,
            "var_mixed": bb-mb*mb, "cov_prompt_mixed": ab-ma*mb,
            "zero_mixed_probability": zero}


def sigma_row(mo: dict, n: int, k: int) -> dict:
    t = theory(mo, n, k)
    a, m = mo["prompt_mean"], mo["mixed_mean"]
    terms = (t["var_prompt"]/m**2, a*a*t["var_mixed"]/m**4,
             -2*a*t["cov_prompt_mixed"]/m**3)
    return {"N": n, "K": k, "mixed_sigma": math.sqrt(t["var_mixed"]),
            "independent_pair_sigma_counterfactual": math.sqrt(m*(1-m)/F(n*k)),
            "all_partner_event_floor_sigma": math.sqrt(t["var_mixed_all"]),
            "ratio_sigma_full": math.sqrt(sum(terms)),
            "ratio_sigma_zero_cross_cov": math.sqrt(sum(terms[:2])),
            "ratio_sigma_fixed_denominator": math.sqrt(terms[0]),
            "ratio_variance_components": list(map(float, terms))}


def monte_carlo(cfg: dict, mo: dict) -> list[dict]:
    spec = cfg["monte_carlo"]
    n, repetitions = spec["events"], spec["repetitions"]
    rng = np.random.default_rng(spec["seed"])
    tags = np.asarray(STATES, dtype=np.int8)[rng.choice(4, (repetitions, n), p=np.array(list(map(float, mo["prob"]))))]
    x, y = tags[:, :, 0], tags[:, :, 1]
    a = np.mean(x == y, axis=1)
    sy = y.sum(axis=1)
    sx = x.sum(axis=1)
    sxy = (x*y).sum(axis=1)
    b_all = 1-(sx+sy)/n+2*(sx*sy-sxy)/(n*(n-1))
    successes = np.where(x == 1, sy[:, None], n-sy[:, None])-(x == y)
    results = []
    for k in spec["partner_counts"]:
        # Independent row-wise hypergeometric samples exactly implement distinct partners.
        if k == n-1:
            b = b_all
        else:
            b = rng.hypergeometric(successes, n-1-successes, k).sum(axis=1)/(n*k)
        if np.any(b <= 0):
            raise ValueError("MC ratio encountered zero denominator; no replicas silently removed")
        expected = theory(mo, n, k)
        av, bv = a-a.mean(), b-b.mean()
        varb = float(np.var(b, ddof=1))
        cov = float(np.cov(a, b, ddof=1)[0, 1])
        se_var = np.sqrt(max(float(np.mean(bv**4))-varb*varb, 0.)/repetitions)
        se_cov = float(np.std(av*bv, ddof=1)/np.sqrt(repetitions))
        z_var = (varb-float(expected["var_mixed"]))/se_var
        z_cov = (cov-float(expected["cov_prompt_mixed"]))/se_cov
        assert abs(z_var) < 6 and abs(z_cov) < 6
        ratio_sigma = float(np.std(a/b, ddof=1))
        linear_sigma = sigma_row(mo, n, k)["ratio_sigma_full"]
        assert abs(ratio_sigma/linear_sigma-1) < .05
        results.append({"N": n, "K": k, "repetitions": repetitions, "zero_denominators": 0,
                        "mean_prompt": float(a.mean()), "mean_mixed": float(b.mean()),
                        "variance_mixed": varb, "expected_variance_mixed": float(expected["var_mixed"]),
                        "variance_z_mc": z_var, "cov_prompt_mixed": cov,
                        "expected_cov_prompt_mixed": float(expected["cov_prompt_mixed"]), "covariance_z_mc": z_cov,
                        "ratio_sigma_mc": ratio_sigma, "ratio_sigma_delta": linear_sigma,
                        "ratio_sigma_mc_over_delta": ratio_sigma/linear_sigma})
    return results


def plot_result(result: dict, out: Path, audit_dir: Path) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    sys.path.insert(0, str(audit_dir))
    from audit_panel_alignment import require_matplotlib_panel_alignment
    plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["DejaVu Sans"],
                         "font.size": 8, "axes.labelsize": 8, "axes.titlesize": 8,
                         "xtick.labelsize": 7.5, "ytick.labelsize": 7.5, "legend.fontsize": 7,
                         "svg.fonttype": "none", "pdf.fonttype": 42,
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(7.204724409, 3.149606299))
    fig.subplots_adjust(left=.092, right=.98, bottom=.20, top=.79, wspace=.37)
    rows = result["partner_sensitivity"]
    ks = np.array([r["K"] for r in rows])
    ax = axes[0]
    ax.loglog(ks, [r["mixed_sigma"] for r in rows], color="#35698F", label="Event reuse")
    ax.loglog(ks, [r["independent_pair_sigma_counterfactual"] for r in rows], color="#B3763C", ls="--", label="Independent pairs (assumed)")
    ax.axhline(rows[-1]["all_partner_event_floor_sigma"], color="#737373", ls=":", label="All-partner limit")
    ax.set_ylim(top=2.5*max(r["mixed_sigma"] for r in rows))
    ax.set(xlabel="Distinct partners per trigger, K", ylabel="Standard deviation of mixed mean")
    ax.legend(loc="upper right", frameon=False)
    ax = axes[1]
    ax.semilogx(ks, [r["ratio_sigma_full"] for r in rows], color="#35698F", label="Full prompt / mixed Cov")
    ax.semilogx(ks, [r["ratio_sigma_zero_cross_cov"] for r in rows], color="#B3763C", ls="--", label="Zero cross Cov (assumed)")
    ax.axhline(rows[-1]["ratio_sigma_fixed_denominator"], color="#737373", ls=":", label="Fixed mixed denominator")
    ax.set(xlabel="Distinct partners per trigger, K", ylabel="Delta standard uncertainty of ratio")
    ax.legend(loc="upper right", frameon=False)
    for i, (ax, title) in enumerate(zip(axes, ("Pair count and event count", "Propagation to the ratio"))):
        ax.text(-.14, 1.14, chr(97+i), transform=ax.transAxes, fontweight="bold", fontsize=9)
        ax.set_title(title, loc="left", pad=14)
    fig.text(.5, .96, "Chosen analytic event model; N = 10000 physical events; no experimental data", ha="center", va="top", fontsize=8)
    fig.canvas.draw()
    require_matplotlib_panel_alignment(fig, json_out=out/"mixed-event-partner-sensitivity.alignment.json",
                                       require_panel_labels=True, strict=True)
    fig.savefig(out/"mixed-event-partner-sensitivity.svg")
    fig.savefig(out/"mixed-event-partner-sensitivity.pdf")
    fig.savefig(out/"mixed-event-partner-sensitivity.png", dpi=300)
    svg = out/"mixed-event-partner-sensitivity.svg"
    svg.write_text("\n".join(s.rstrip(" \t") for s in svg.read_text(encoding="utf-8").splitlines())+"\n", encoding="utf-8")
    plt.close(fig)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--plot-audit-dir", type=Path)
    args = parser.parse_args()
    cfg = json.loads(args.input.read_text(encoding="utf-8"))
    mo = moments(*(F(str(cfg[k])) for k in ("p_X1", "p_Y1", "cov_XY_same_event")))
    enumeration = []
    for n, k in ((2, None), (3, None), (4, None), (3, 1)):
        exact = enumerate_small(mo, n, k)
        predicted = theory(mo, n, n-1 if k is None else k)
        assert exact["mean_prompt"] == mo["prompt_mean"] and exact["mean_mixed"] == mo["mixed_mean"]
        for name in ("var_prompt", "var_mixed", "cov_prompt_mixed"):
            assert exact[name] == predicted[name]
        enumeration.append({"N": n, "K": n-1 if k is None else k, **{name: str(value) for name, value in exact.items()}})
    control = cfg["degenerate_control"]
    degenerate = moments(*(F(str(control[k])) for k in ("p_X1", "p_Y1", "cov_XY_same_event")))
    assert degenerate["first_order_coefficient"] == 0
    d_exact = enumerate_small(degenerate, 4)
    assert d_exact["var_mixed"] == theory(degenerate, 4, 3)["var_mixed"]
    n = cfg["fixed_event_count_for_target_table"]
    assert n == 10000, "The fixed figure annotation is specific to this worksheet's N=10000"
    ks = np.unique(np.r_[1, np.geomspace(1, n-1, 260).astype(int), n-1])
    rows = [sigma_row(mo, n, int(k)) for k in ks]
    assert all(rows[i+1]["mixed_sigma"] <= rows[i]["mixed_sigma"] for i in range(len(rows)-1))
    mc = monte_carlo(cfg, mo)
    # A source-inspired ideal-bin bound uses Table1's 48 ordered pairs and 64 crystals.
    mean_degree = F(48, 64)
    fraction = mean_degree-int(mean_degree)
    degree_variance_lower = fraction*(1-fraction)
    result = {"data_identity": cfg["data_identity"], "data_kind": cfg["data_kind"],
              "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "model_moments_exact": {name: [str(x) for x in value] if name == "prob" else str(value) for name, value in mo.items()},
              "enumeration": enumeration, "degenerate_control": {"first_order_coefficient": "0",
                  "second_order_coefficient": str(degenerate["second_order_coefficient"]),
                  "all_partner_variance": "V2 / (N*(N-1)), not a nonzero 1/N floor"},
              "monte_carlo": mc, "partner_sensitivity": rows,
              "selected_table": [sigma_row(mo, n, k) for k in (1, 10, 100, 1000, n-1)],
              "ideal_64_crystal_48_pair_bin_bound": {"source_input": "SG19-2 / v1 Table1: nominal ordered pair counts, not measured efficiencies",
                  "chosen_conditions": "Independent uniform photon tags in 64 crystals; binary adjacency bin; real pair weights/response unspecified",
                  "mean_out_degree": str(mean_degree), "degree_variance_lower_bound": str(degree_variance_lower),
                  "first_order_coefficient_lower_bound": str(2*degree_variance_lower/64**2),
                  "sigma_first_order_lower_bound_at_N10000": math.sqrt(2*degree_variance_lower/(64**2*n))},
              "boundaries": cfg["boundaries"]}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir/"mixed-event-covariance.json").write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    with (args.output_dir/"mixed-event-partner-sensitivity.csv").open("w", newline="", encoding="utf-8") as handle:
        fields = [name for name in rows[0] if name != "ratio_variance_components"]
        writer = csv.DictWriter(handle, fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    if args.plot_audit_dir:
        plot_result(result, args.output_dir, args.plot_audit_dir)
    print(json.dumps({"exact_moments": result["model_moments_exact"], "selected_table": result["selected_table"],
                      "mc_max_abs_z": max(abs(x[k]) for x in mc for k in ("variance_z_mc", "covariance_z_mc")),
                      "degenerate_control": result["degenerate_control"], "input_sha256": result["input_sha256"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
