#!/usr/bin/env python3
"""Toy 3-D Routhian for MR, chiral and SD competing minima.

Coordinates are beta2, theta (shears opening angle, rad), and phi
(out-of-plane/chiral angle, rad). Energies are MeV and omega is MeV/hbar.
The model is a reproducible phenomenological diagnostic, not a TAC fit.
"""
from __future__ import annotations
import csv, heapq, json
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent
HBAR = 1.0

def routhian(beta, theta, phi, omega):
    # Shape double well: ND beta~0.12, SD beta~0.60. Rotation lowers SD.
    # Smooth double well retains metastable ND and SD branches during a crossing.
    shape_barrier = 6.0*((beta-0.12)*(beta-0.60))**2
    sd_rot_gain = (0.78 - 0.5*15.0*omega**2)*((beta-0.12)/0.48)**4
    v_shape = 0.78*(beta-0.12)**2 + shape_barrier + sd_rot_gain
    # Shears: blades close with frequency; the term remains finite at theta=0.
    theta_mr = np.clip(1.18 - 0.62*omega, 0.35, 1.18)
    v_shear = 0.34*(theta-theta_mr)**2 + 0.07*(theta-theta_mr)**4
    # A Landau pitchfork in phi, suppressed by large deformation (SD planar).
    aphi = 0.105 - 0.46*omega**2 + 1.55*(beta-0.12)**2
    v_chiral = aphi*phi**2 + 0.22*phi**4 + 0.035*phi**2*(theta-theta_mr)**2
    # Weak beta-phi coupling keeps the SD minimum near phi=0.
    return v_shape + v_shear + v_chiral

def classify(beta, theta, phi):
    if beta > 0.40: return "SD"
    if abs(phi) > 0.10: return "Chirality"
    return "MR"

def local_minima(beta, theta, phi, omega):
    # Fixed physically interpretable seeds, relaxed by coordinatewise local search.
    seeds = [(0.12, np.clip(1.18-0.62*omega, .35, 1.18), 0.0),
             (0.12, np.clip(1.18-0.62*omega, .35, 1.18), .45),
             (0.12, np.clip(1.18-0.62*omega, .35, 1.18), -.45),
             (.60, .45, 0.0)]
    mins=[]
    steps=np.array([0.01, .025, .025])
    bounds=np.array([[.02,.78],[0,1.55],[-.85,.85]])
    for seed in seeds:
        x=np.array(seed,float)
        for _ in range(180):
            improved=False; e=routhian(*x,omega)
            # beta is the generator-coordinate label of the two shape wells;
            # relax only angular coordinates within each well.
            for k in (1, 2):
                for sign in (-1,1):
                    y=x.copy(); y[k]=np.clip(y[k]+sign*steps[k],*bounds[k]); ey=routhian(*y,omega)
                    if ey < e-1e-10: x,e=y,ey; improved=True
            if not improved: break
        if not any(np.linalg.norm(x-m[:3])<.04 for m in mins): mins.append((*x,e,classify(*x)))
    return sorted(mins,key=lambda z:z[3])

def bottleneck_barrier(start, target, omega):
    # Minimax path on a regular 3-D grid; returns barrier above the higher endpoint.
    axes=(np.linspace(.02,.78,31),np.linspace(0,1.55,31),np.linspace(-.85,.85,31))
    shape=tuple(len(a) for a in axes); start=tuple(np.argmin(abs(a-v)) for a,v in zip(axes,start[:3])); target=tuple(np.argmin(abs(a-v)) for a,v in zip(axes,target[:3]))
    cache={}
    def val(s):
        if s not in cache: cache[s]=routhian(*(axes[k][s[k]] for k in range(3)),omega)
        return cache[s]
    inf=float("inf"); dist={start:val(start)}; pq=[(dist[start],start)]; seen=set()
    while pq:
        cost,s=heapq.heappop(pq)
        if s in seen: continue
        seen.add(s)
        if s==target: break
        for k in range(3):
            for d in (-1,1):
                t=list(s); t[k]+=d
                if 0<=t[k]<shape[k]:
                    t=tuple(t); nc=max(cost,val(t))
                    if nc<dist.get(t,inf): dist[t]=nc; heapq.heappush(pq,(nc,t))
    endpoint=max(val(start),val(target)); return max(0.0, dist.get(target, val(target))-endpoint), dist.get(target, val(target))

def main():
    omegas=np.linspace(.10,.72,32); rows=[]; detail=[]
    for om in omegas:
        mins=local_minima(None,None,None,om); by={m[4]:m for m in mins}
        # At low omega a chiral minimum may not exist; report NaN barriers then.
        rec={"omega":float(om)}
        for name in ("MR","Chirality","SD"):
            m=by.get(name)
            if m:
                rec.update({f"{name.lower()}_{q}": float(m[i]) for i,q in [(0,"beta"),(1,"theta"),(2,"phi"),(3,"energy")]})
            else:
                rec.update({f"{name.lower()}_{q}": None for q in ("beta","theta","phi","energy")})
        for a,b in (("MR","Chirality"),("MR","SD"),("Chirality","SD")):
            key=f"barrier_{a.lower()}_{b.lower()}"; ba=by.get(a); bb=by.get(b)
            rec[key]=float(bottleneck_barrier(ba,bb,om)[0]) if ba and bb else None
        detail.append(rec)
    # Branch ratios use actions S = integral sqrt(2 M (V-E)) ds along minimax scale.
    M=18.0
    for rec in detail:
        for pair in (("mr","chirality"),("mr","sd"),("chirality","sd")):
            b=rec[f"barrier_{pair[0]}_{pair[1]}"]
            # A compact barrier-to-action proxy; path length in dimensionless coordinate is 1.
            rec[f"action_{pair[0]}_{pair[1]}"]=None if b is None else float(np.sqrt(2*M)*b**1.5*1.25/HBAR)
        acts={p:rec[f"action_{p}"] for p in ("mr_chirality","mr_sd","chirality_sd") if rec[f"action_{p}"] is not None}
        weights={p:np.exp(-2*s) for p,s in acts.items()}; norm=sum(weights.values()) or 1
        rec.update({f"branch_{p}":float(w/norm) for p,w in weights.items()})
        rows.append(rec)
    fields=sorted({k for row in rows for k in row})
    with (OUT/"scan.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
    summary={"model":"3D phenomenological Routhian","coordinates":{"beta2":"shape deformation","theta":"shears opening (rad)","phi":"chiral out-of-plane angle (rad)"},"omega_units":"MeV/hbar","mass_parameter_hbar2_per_MeV":M,"notes":"WKB actions use dimensionless path-length proxy; no isotope fit.","scan":rows}
    (OUT/"scan.json").write_text(json.dumps(summary,indent=2))
    try:
        import matplotlib.pyplot as plt
        x=[r["omega"] for r in rows]; plt.figure(figsize=(8,5))
        for n,c in (("mr_energy","tab:blue"),("chirality_energy","tab:orange"),("sd_energy","tab:red")):
            plt.plot(x,[r[n] if r[n] is not None else np.nan for r in rows],label=n.replace("_energy",""),color=c)
        plt.xlabel(r"$\omega$ (MeV/$\hbar$)"); plt.ylabel("Routhian energy (MeV)"); plt.legend(); plt.tight_layout(); plt.savefig(OUT/"energy_minima.svg"); plt.savefig(OUT/"energy_minima.png",dpi=180); plt.close()
        plt.figure(figsize=(8,5));
        for p,c in (("mr_chirality","tab:purple"),("mr_sd","tab:green"),("chirality_sd","tab:brown")):
            plt.plot(x,[r[f"action_{p}"] if r[f"action_{p}"] is not None else np.nan for r in rows],label=p,color=c)
        plt.xlabel(r"$\omega$ (MeV/$\hbar$)"); plt.ylabel(r"WKB action / $\hbar$"); plt.legend(); plt.tight_layout(); plt.savefig(OUT/"wkb_actions.svg"); plt.savefig(OUT/"wkb_actions.png",dpi=180); plt.close()
    except ImportError: pass
    print(json.dumps({"output":str(OUT),"rows":len(rows),"omega_range":[float(omegas[0]),float(omegas[-1])]},indent=2))

if __name__=="__main__": main()
