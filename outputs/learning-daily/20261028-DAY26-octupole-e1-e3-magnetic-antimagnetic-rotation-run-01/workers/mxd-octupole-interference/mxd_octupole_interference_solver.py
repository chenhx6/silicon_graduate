#!/usr/bin/env python3
"""Synthetic 2qp/4qp + chiral + octupole eight-band interference model.

The calculation is an effective diagnostic model, not a fit to 78Br or 134Pr.
Basis ordering is (configuration, chirality, parity), with two configurations,
two chiral sectors and two parity sectors.  It exposes coherent E1 paths and
the resulting non-harmonic B(M1)/B(E2) ratios.
"""
from __future__ import annotations
import csv, json
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent

def kron3(a, b, c):
    return np.kron(np.kron(a, b), c)

def operators():
    I2 = np.eye(2); x = np.array([[0., 1.], [1., 0.]])
    z = np.diag([1., -1.])
    # ordering: c (2qp/4qp), chi (L/R), p (+/-)
    # E1: parity flip, with a configuration-changing path of opposite phase
    e1 = 0.10 * kron3(I2, I2, x) + 0.055 * kron3(x, z, x)
    # M1: chiral flip, configuration dependent effective g factor
    m1 = kron3(np.diag([1.0, 0.78]), x, I2)
    # E2: diagonal quadrupole plus a small coherent config-mixing term
    e2 = 3.0 * kron3(np.diag([1.0, 0.88]), I2, I2) + 0.24 * kron3(x, z, I2)
    # E3 follows the octupole coordinate and flips parity
    e3 = 1.35 * kron3(I2, I2, x) + 0.18 * kron3(x, z, x)
    return {"E1": e1, "M1": m1, "E2": e2, "E3": e3}

def hamiltonian(I: int, beta3: float, cfg_mix: float = 0.0):
    I2 = np.eye(2); x = np.array([[0., 1.], [1., 0.]])
    z = np.diag([1., -1.])
    # V(beta3) is retained as an explicit reported quantity; beta3 scans the soft PES.
    V = 0.5 * 1.55 * beta3**2 + 0.25 * 8.0 * beta3**4 - 0.018 * beta3
    # 4qp lies higher but its rotational slope is different, as in a crossing toy model.
    ec = np.diag([0.0 + 0.006 * I*(I+1), 0.72 + 0.003 * I*(I+1)])
    H = kron3(ec, I2, I2)
    tchi = 0.050 + 0.0025 * I + 0.020 * beta3**2
    tpar = 0.115 + 0.16 * abs(beta3)
    H += -tchi * kron3(I2, x, I2)
    H += -tpar * kron3(I2, I2, x)
    # beta3-mediated 2qp <-> 4qp mixing; phase changes across the soft well.
    v = 0.035 + cfg_mix + 0.19 * beta3
    H += v * kron3(x, z, I2)
    H += 0.025 * beta3 * kron3(x, x, x)
    return H + V * np.eye(8), V, tchi, tpar, v

def parity_of(vec):
    p = np.diag(np.tile([1., -1.], 4))
    return float(np.real(vec.conj() @ p @ vec))

def calc(beta3: float, I: int, cfg_mix: float = 0.0):
    H, V, tchi, tpar, v = hamiltonian(I, beta3, cfg_mix)
    en, U = np.linalg.eigh(H)
    ops = operators()
    out = {"beta3": beta3, "I": I, "V_beta3_MeV": V,
           "tchi_MeV": tchi, "tpar_MeV": tpar, "v_cfg_MeV": v,
           "energies_MeV": en.tolist(),
           "parity_expectation": [parity_of(U[:, k]) for k in range(8)],
           "transitions": []}
    for xi, name in ops.items():
        T = U.T @ name @ U
        for i in range(8):
            for f in range(i + 1, 8):
                amp = float(T[f, i])
                if abs(amp) < 1e-9: continue
                dE = float(en[f] - en[i])
                out["transitions"].append({"operator": xi, "initial": i, "final": f,
                    "dE_MeV": dE, "amplitude": amp, "B_relative": amp*amp})
    # diagnostic band ratios: lowest same-parity M1 and E2 links from each state
    m1 = [r for r in out["transitions"] if r["operator"] == "M1"]
    e2 = [r for r in out["transitions"] if r["operator"] == "E2"]
    m1sum, e2sum = sum(r["B_relative"] for r in m1), sum(r["B_relative"] for r in e2)
    out["B_M1_total"] = m1sum; out["B_E2_total"] = e2sum
    out["M1_over_E2"] = m1sum / e2sum if e2sum else 0.0
    e1 = [r for r in out["transitions"] if r["operator"] == "E1"]
    out["B_E1_total"] = sum(r["B_relative"] for r in e1)
    return out

def main():
    betas = np.linspace(-0.34, 0.34, 35)
    rows, networks = [], []
    for I in (8, 10, 12, 14):
        for b in betas:
            r = calc(float(b), I)
            rows.append({k: r[k] for k in ("I", "beta3", "V_beta3_MeV", "tchi_MeV", "tpar_MeV", "v_cfg_MeV", "B_E1_total", "B_M1_total", "B_E2_total", "M1_over_E2")})
            networks.append(r)
    csv_path = OUT / "mxd_octupole_interference_scan.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    json_path = OUT / "mxd_octupole_interference_scan.json"
    json_path.write_text(json.dumps({"model": "2qp/4qp effective eight-band", "rows": rows, "networks": networks}, indent=2), encoding="utf-8")
    try:
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, 2, figsize=(10, 4))
        for I in (8, 10, 12, 14):
            q = [x for x in rows if x["I"] == I]
            ax[0].plot([x["beta3"] for x in q], [x["M1_over_E2"] for x in q], label=f"I={I}")
            ax[1].plot([x["beta3"] for x in q], [x["B_E1_total"] for x in q], label=f"I={I}")
        ax[0].set(xlabel=r"$\beta_3$", ylabel=r"$\sum B(M1)/\sum B(E2)$", title="Non-harmonic ratio")
        ax[1].set(xlabel=r"$\beta_3$", ylabel="relative E1 strength", title="E1 network strength")
        for a in ax: a.grid(alpha=.25); a.legend(frameon=False, fontsize=8)
        fig.tight_layout(); fig.savefig(OUT / "mxd_octupole_interference.svg"); plt.close(fig)
    except Exception as exc:
        (OUT / "plot_skipped.txt").write_text(str(exc), encoding="utf-8")
    print(f"wrote {csv_path.name}, {json_path.name}, mxd_octupole_interference.svg")

if __name__ == "__main__": main()
