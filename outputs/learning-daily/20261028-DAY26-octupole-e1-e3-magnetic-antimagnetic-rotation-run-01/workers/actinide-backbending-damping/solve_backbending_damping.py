#!/usr/bin/env python3
"""Toy cranked two-configuration model for octupole backbending damping.

The crossing states are a paired vacuum (A) and an aligned two-quasiparticle
configuration (B).  The off-diagonal matrix element contains a small residual
pairing mixing and an octupole induced mixing V3*beta3.  The latter is the
minimal representation of Delta-l=Delta-j=3 orbital mixing.  Energies are in
MeV, hbar*omega in MeV, and J/J2 in hbar^2/MeV.
"""
from __future__ import annotations
import argparse, csv, json
from pathlib import Path
import numpy as np

PAIRS = {
    "proton": {"orbitals": "1f7/2 <-> 1i13/2", "delta_l": 3, "delta_j": 3,
               "v3": 3.8, "pairing_gap": 0.82},
    "neutron": {"orbitals": "1g9/2 <-> 1j15/2", "delta_l": 3, "delta_j": 3,
                 "v3": 4.2, "pairing_gap": 0.78},
}

def crossing_matrix(omega, beta3, species, pairing_strength=0.030):
    """Return 2x2 Routhian for A/B configurations.

    V_pair is deliberately weak at beta3=0.  Pairing is reduced as
    Delta_eff=Delta0/(1+alpha beta3^2), while the octupole matrix element
    V3*beta3 opens the crossing and redistributes alignment continuously.
    """
    p = PAIRS[species]
    # A is the collective paired configuration; B is the aligned 2-qp band.
    e_a, j_a, inertia_a = 0.0, 8.0, 22.0
    e_b, j_b, inertia_b = 1.20, 14.0, 30.0
    delta_eff = p["pairing_gap"] / (1.0 + 6.0 * beta3**2)
    e_pair = -0.5 * delta_eff**2 / p["pairing_gap"]
    e_a += e_pair
    v_pair = pairing_strength * (delta_eff / p["pairing_gap"])**2
    v_oct = p["v3"] * beta3
    v = v_pair + v_oct
    # A cranked Routhian contains -1/2 J omega^2 - j_align omega.
    # This sign makes I=-dE'/d(hbar omega) and J^(2)=dI/d(hbar omega)
    # positive away from the crossing.
    a = e_a - 0.5 * inertia_a * omega**2 - j_a * omega
    b = e_b - 0.5 * inertia_b * omega**2 - j_b * omega
    return np.array([[a, v], [v, b]], float), delta_eff, v_oct, v_pair

def solve(beta3, n=801, wmax=0.80):
    omega = np.linspace(0.0, wmax, n)
    e = np.empty(n); adiabatic = np.empty(n)
    d_eff = np.empty(n); v_oct = np.empty(n); v_pair = np.empty(n)
    for k, w in enumerate(omega):
        h, d_eff[k], v_oct[k], v_pair[k] = crossing_matrix(w, beta3, "proton")
        vals, vecs = np.linalg.eigh(h)
        e[k] = vals[0]
        # aligned-band weight diagnoses the configuration admixture
        adiabatic[k] = vecs[1, 0] ** 2
    # Routhian convention: I = -dE'/d(hbar omega), J2 = dI/d(hbar omega).
    spin = -np.gradient(e, omega, edge_order=2)
    j2 = np.gradient(spin, omega, edge_order=2)
    return omega, e, spin, j2, adiabatic, d_eff, v_oct, v_pair

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=Path(__file__).parent)
    ap.add_argument("--n", type=int, default=801)
    args = ap.parse_args(); args.out.mkdir(parents=True, exist_ok=True)
    betas = [0.0, 0.03, 0.06, 0.10, 0.15]
    rows=[]; summaries=[]
    for beta in betas:
        vals = solve(beta, args.n)
        w,e,spin,j2,mix,de,vo,vp = vals
        for i in range(len(w)):
            rows.append({"beta3": beta, "hbar_omega_MeV": w[i], "energy_routhian_MeV": e[i],
                         "spin_hbar": spin[i], "J2_hbar2_per_MeV": j2[i],
                         "aligned_config_weight": mix[i], "Delta_eff_MeV": de[i],
                         "V_oct_MeV": vo[i], "V_pair_MeV": vp[i]})
        peak = int(np.argmax(j2))
        summaries.append({"beta3": beta, "peak_J2": float(j2[peak]),
                          "peak_omega_MeV": float(w[peak]),
                          "max_dJ2_width_proxy": float(np.sum(j2 > 0.75*j2[peak])*(w[1]-w[0])),
                          "Delta_eff_MeV": float(de[0]), "V_oct_MeV": float(vo[0]),
                          "crossing_gap_MeV": float(2*(vo[0]+vp[0]))})
    with (args.out/"scan.csv").open("w", newline="") as f:
        writer=csv.DictWriter(f, fieldnames=rows[0].keys()); writer.writeheader(); writer.writerows(rows)
    metadata={"model":"cranked two-configuration avoided-crossing toy model",
              "units":{"energy":"MeV","hbar_omega":"MeV","spin":"hbar","J2":"hbar^2/MeV"},
              "orbit_pairs":PAIRS,"betas":betas,"n_grid":args.n,
              "formulae":{"H":"[[E_A(omega), V_pair+V3 beta3],[..., E_B(omega)]]",
                           "I":"-dE_routhian/d(hbar omega)","J2":"dI/d(hbar omega)"},
              "summaries":summaries,
              "evidence_boundary":"Illustrative mechanism model; parameters are not a self-consistent HFB fit to 220-228Th or 222-228Ra."}
    (args.out/"scan.json").write_text(json.dumps(metadata, indent=2)+"\n")
    try:
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1,2,figsize=(10,4.2), constrained_layout=True)
        colors=plt.cm.viridis(np.linspace(0.08,0.9,len(betas)))
        for beta,c in zip(betas,colors):
            w,e,spin,j2,mix,*_=solve(beta,args.n)
            ax[0].plot(w,j2,label=fr"$\beta_3={beta:.2f}$",color=c)
            ax[1].plot(w,spin,color=c)
        ax[0].set(xlabel=r"$\hbar\omega$ (MeV)",ylabel=r"$\mathcal{J}^{(2)}$ ($\hbar^2$/MeV)")
        ax[1].set(xlabel=r"$\hbar\omega$ (MeV)",ylabel=r"$I$ ($\hbar$)")
        ax[0].legend(frameon=False,fontsize=8); fig.suptitle("Octupole damping of a high-spin crossing")
        fig.savefig(args.out/"backbending_damping.svg"); fig.savefig(args.out/"backbending_damping.png",dpi=180)
        plt.close(fig)
    except Exception as exc:
        (args.out/"plot_error.txt").write_text(repr(exc)+"\n")

if __name__ == "__main__": main()
