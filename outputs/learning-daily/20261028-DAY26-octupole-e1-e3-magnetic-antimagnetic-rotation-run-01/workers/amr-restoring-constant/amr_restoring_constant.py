#!/usr/bin/env python3
"""Minimal, reproducible AMR quadrupole-restoring-constant scan.

The microscopic curvature is written in an explicitly normalized collective
coordinate.  A raw four-vector P2 sum is also printed, so the factor-of-two
statement is not confused with a coordinate convention.
"""
from __future__ import annotations
import csv, json, math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent

DATA = {
    "110Cd": {"I": [16,18,20,22,24], "Egamma_keV": [1075,1224,1323,1314,1358],
              "B_E2_e2b2": [0.14,0.12,0.11,0.09,0.06]},
    "104Pd": {"I": [16,18,20,22,24,26], "Egamma_keV": [927,1064,1193,1256,1365,1468],
              "B_E2_e2b2": [0.26,0.22,0.19,0.13,0.07,0.02]},
}

def p2(x): return 0.5*(3*x*x-1.0)

def j2_centered(E):
    out = [None] * len(E)
    for k in range(1, len(E)-1):
        d = E[k+1] - E[k-1]
        out[k] = None if d <= 0 else 4000.0/d
    return out

def main():
    # q_p and q_n are reduced intrinsic quadrupole matrix elements (eb).
    # chi2 is in MeV/(eb)^2; C is in MeV.
    qp, qn = 1.0, 1.0
    chi_grid = np.linspace(0.02, 0.40, 191)
    theta_grid = np.linspace(0.0, math.pi/2, 181)
    # One normalized p-n scissors pair: -chi qp qn P2(cos theta).
    # The four-blade AMR collective coordinate has two equivalent pair
    # channels after the exchange-even projection, hence the curvature doubles.
    c_mr = 1.5 * chi_grid * qp * qn
    c_amr = 3.0 * chi_grid * qp * qn

    rows = []
    for nucleus, d in DATA.items():
        js = j2_centered(d["Egamma_keV"])
        for I, eg, be2, j in zip(d["I"], d["Egamma_keV"], d["B_E2_e2b2"], js):
            # A transparent curvature proxy, not a unique experimental inversion.
            # theta_ref=0.5 rad defines the local harmonic coordinate.
            c_proxy = None if j is None else 0.5 / (j * 0.5**2)
            chi_proxy = None if c_proxy is None else c_proxy/(3*qp*qn)
            rows.append({"nucleus": nucleus, "I": I, "Egamma_keV": eg,
                         "B_E2_e2b2": be2, "J2_hbar2_per_MeV": j,
                         "C_proxy_MeV": c_proxy, "chi2_proxy_MeV_per_eb2": chi_proxy})

    with (OUT/"j2_chi2_scan.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    scan = []
    for chi in chi_grid:
        scan.append({"chi2_MeV_per_eb2": float(chi), "C_MR_MeV": float(1.5*chi),
                     "C_AMR_MeV": float(3.0*chi), "ratio": 2.0})
    with (OUT/"chi2_restoring_scan.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=scan[0].keys()); w.writeheader(); w.writerows(scan)

    # Angular curvature check and raw pair-channel sum.
    x = theta_grid
    v_mr = -p2(np.cos(x))
    v_amr = 2*v_mr
    # Direct four pair count: four equal tensor channels, versus two in MR.
    raw_ratio = 4/2
    fig, ax = plt.subplots(1, 2, figsize=(9, 3.6))
    ax[0].plot(x, v_mr-v_mr[0], label="MR (2 channels)")
    ax[0].plot(x, v_amr-v_amr[0], label="AMR (4 channels)")
    ax[0].set(xlabel=r"collective angle $\theta$ (rad)", ylabel=r"$V(\theta)-V(0)$ / $\chi_2q_pq_n$")
    ax[0].legend(frameon=False); ax[0].grid(alpha=.25)
    ax[1].plot(chi_grid, c_mr, label=r"$C_{MR}$")
    ax[1].plot(chi_grid, c_amr, label=r"$C_{AMR}$")
    ax[1].set(xlabel=r"$\chi_2$ [MeV/(eb)$^2$]", ylabel="curvature [MeV]")
    ax[1].legend(frameon=False); ax[1].grid(alpha=.25)
    fig.tight_layout(); fig.savefig(OUT/"restoring_constant_scan.svg"); plt.close(fig)

    result = {"model": "equal-weight quadrupole P2 pair-channel curvature",
              "q_p_eb": qp, "q_n_eb": qn,
              "C_MR": "(3/2) chi2 q_p q_n",
              "C_AMR": "3 chi2 q_p q_n",
              "ratio": 2.0, "raw_channel_count_ratio": raw_ratio,
              "data_basis": "Roy 2011 Table 1 and Rather 2014 Table I as transcribed in existing Wiki note",
              "proxy_definition": "C_proxy=0.5/(J2*theta_ref^2), theta_ref=0.5 rad; model-dependent",
              "rows": rows,
              "boundary": ["The factor two assumes equal blade weights and the exchange-even collective coordinate.",
                           "chi2_proxy is a curvature proxy, not a unique fit to experimental J2.",
                           "110Cd negative centered finite difference is retained as null rather than forced positive."]}
    (OUT/"amr_restoring_constant.json").write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n")

if __name__ == "__main__": main()
