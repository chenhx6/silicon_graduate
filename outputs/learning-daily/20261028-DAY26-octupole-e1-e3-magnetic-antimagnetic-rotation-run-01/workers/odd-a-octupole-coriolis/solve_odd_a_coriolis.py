#!/usr/bin/env python3
"""Three-parameter parity-doublet rotor model with an octupole-induced term.

The energy formula is deliberately an effective model.  A parity-conserving
Coriolis operator has <+|H_C|-> = 0 exactly.  The fitted odd-parity term is
therefore interpreted as the second-order V_3 H_C (Delta-j=3) contribution,
not as a literal direct matrix element.
"""
import csv, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parent

RA = [
    (0.5, 0.0, 55.16), (1.5, 42.77, 31.56),
    (2.5, 25.41, 120.36), (3.5, 111.60, 69.36),
]
AC = [(1.5, 0.0, 40.10), (2.5, 29.91, 64.69), (3.5, 77.13, 105.01)]

def features(I, K):
    x = I*(I+1.0)-K*K
    # first-order decoupling is present only for K=1/2
    s = ((-1)**int(round(I+0.5))) * (I+0.5) if abs(K-0.5) < 1e-9 else 0.0
    return x, s

def fit(rows, K):
    # Ordinary least squares for Delta=E_minus-E_plus=d0+dA*x+dC*s.
    M, y = [], []
    for I, ep, em in rows:
        x, s = features(I, K); M.append([1.0, x, s]); y.append(em-ep)
    # normal equations, small 3x3 solver by Gaussian elimination
    a = [[sum(M[r][i]*M[r][j] for r in range(len(M))) for j in range(3)] +
         [sum(M[r][i]*y[r] for r in range(len(M))) ] for i in range(3)]
    for i in range(3):
        p = max(range(i,3), key=lambda k: abs(a[k][i])); a[i],a[p]=a[p],a[i]
        for k in range(i+1,3):
            q=a[k][i]/a[i][i]
            for j in range(i,4): a[k][j]-=q*a[i][j]
    b=[0.0,0.0,0.0]
    for i in range(2,-1,-1): b[i]=(a[i][3]-sum(a[i][j]*b[j] for j in range(i+1,3)))/a[i][i]
    out=[]
    for I,ep,em in rows:
        x,s=features(I,K); pred=b[0]+b[1]*x+b[2]*s
        out.append(dict(I=I,E_plus_keV=ep,E_minus_keV=em,delta_exp_keV=em-ep,
                        x=x,signature_kernel=s,delta_calc_keV=pred,residual_keV=em-ep-pred,
                        sign_reversal=(em-ep)*(pred)<0))
    return b,out

def fit_two(rows, K):
    M=[]; y=[]
    for I,ep,em in rows:
        x,_=features(I,K); M.append([1.0,x]); y.append(em-ep)
    a=[[sum(M[r][i]*M[r][j] for r in range(len(M))) for j in range(2)] +
       [sum(M[r][i]*y[r] for r in range(len(M)))] for i in range(2)]
    q=a[1][0]/a[0][0]
    for j in range(3): a[1][j]-=q*a[0][j]
    b1=a[1][2]/a[1][1]; b0=(a[0][2]-a[0][1]*b1)/a[0][0]
    return [b0,b1]

def main():
    ra_p, ra = fit(RA, 0.5)
    # For K=3/2 the third column is identically zero: fit the two active terms.
    ac0 = fit_two(AC, 1.5); ac_p=[ac0[0],ac0[1],0.0]
    ac=[]
    for I,ep,em in AC:
        x,s=features(I,1.5); pred=ac_p[0]+ac_p[1]*x
        ac.append(dict(I=I,E_plus_keV=ep,E_minus_keV=em,delta_exp_keV=em-ep,x=x,
                       signature_kernel=s,delta_calc_keV=pred,residual_keV=em-ep-pred,
                       sign_reversal=(em-ep)*pred<0))
    # 145Ba is a transfer/model control: no adopted parity-doublet ladder is entered.
    ba = [{"I": 2.5, "K": 2.5, "delta_exp_keV": None,
           "role":"model-only blocking control", "source":"nomura-2018-odd-mass-ba-octupole"}]
    scan=[]
    for q3 in [0.0,0.25,0.5,0.75,1.0]:
        for gap in [0.5,1.0,2.0]:
            # dimensionless second-order proxy: a_eff proportional to V3/gap
            kappa=q3/gap
            scan.append({"q3_mix":q3,"delta_j":3,"orbital_gap_MeV":gap,
                         "effective_coriolis_asymmetry":kappa,
                         "interpretation":"V3*HC second-order proxy"})
    all_rows=[]
    for label, rows in [("225Ra",ra),("225Ac",ac)]:
        for r in rows: all_rows.append(dict(nucleus=label,**r))
    with (ROOT/"level_fit.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=all_rows[0].keys()); w.writeheader(); w.writerows(all_rows)
    with (ROOT/"microscopic_scan.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=scan[0].keys()); w.writeheader(); w.writerows(scan)
    result={"schema":"odd-a-octupole-coriolis-inversion/v1",
      "model":"Delta(I)=d0+dA[I(I+1)-K^2]+dC*(-1)^(I+1/2)(I+1/2) for K=1/2; dC=0 for K>=3/2",
      "microscopic_mapping":"dC=A*(a_plus-a_minus), with a difference generated at second order by V3(Delta j=3) and HC; direct <+,K|HC|-,K>=0 by parity",
      "datasets":{"225Ra":{"K":0.5,"parameters":dict(zip(["d0_keV","dA_keV","dC_keV"],ra_p)),"rows":ra},
                  "225Ac":{"K":1.5,"parameters":dict(zip(["d0_keV","dA_keV","dC_keV"],ac_p)),"rows":ac},
                  "145Ba":{"status":"model-only control; no parity-doublet fit","rows":ba}},
      "scan":scan,
      "diagnostics":{"Ra_max_abs_residual_keV":max(abs(x["residual_keV"]) for x in ra),
                      "Ac_max_abs_residual_keV":max(abs(x["residual_keV"]) for x in ac),
                      "Ra_observed_negative_delta_at_I":[x["I"] for x in ra if x["delta_exp_keV"]<0],
                      "Ac_observed_negative_delta_at_I":[x["I"] for x in ac if x["delta_exp_keV"]<0]},
      "evidence_boundary":"ENSDF evaluated energies constrain the effective fit; they do not identify orbital amplitudes or prove static octupole deformation."}
    (ROOT/"results.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    try:
        import matplotlib.pyplot as plt
        for label, rows, color in [("225Ra",ra,"tab:red"),("225Ac",ac,"tab:blue")]:
            plt.plot([x["I"] for x in rows],[x["delta_exp_keV"] for x in rows],"o",color=color,label=label+" ENSDF")
            plt.plot([x["I"] for x in rows],[x["delta_calc_keV"] for x in rows],"-",color=color,alpha=.7)
        plt.axhline(0,color="k",lw=.7); plt.xlabel("I"); plt.ylabel(r"$E_- - E_+$ (keV)"); plt.legend(); plt.tight_layout()
        plt.savefig(ROOT/"parity_splitting.svg"); plt.close()
    except Exception as exc:
        (ROOT/"plot_status.txt").write_text("matplotlib unavailable: "+repr(exc),encoding="utf-8")
    print(json.dumps(result["diagnostics"],indent=2))

if __name__ == "__main__": main()
