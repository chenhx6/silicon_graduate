from pathlib import Path
import csv,json,math
OUT=Path('outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-j2-endpoint-20261029');OUT.mkdir(parents=True,exist_ok=True)
# E_gamma is keyed by initial spin I_i in keV. J2 at center I uses Eγ(I+2)-Eγ(I).
trans={'106Cd':{18:980.8,20:1150.6,22:1310.6,24:1487.6,26:1675.5},'108Cd':{16:956.,18:1105.,20:1260.,22:1469.},'110Cd':{16:1075.,18:1224.,20:1323.,22:1314.,24:1358.}}
rows=[]
for nuc,d in trans.items():
    for I in sorted(d):
        if I+2 in d:
            de=d[I+2]-d[I]
            rows.append({'nucleus':nuc,'center_spin':I,'Egamma_I_keV':d[I],'Egamma_Iplus2_keV':d[I+2],'delta_Egamma_keV':de,'omega_center_MeV_over_hbar':d[I]/2000.,'J2_hbar2_per_MeV':4/(de/1000.) if de else None,'interpretation':'finite-difference; negative/large values indicate irregular or unresolved spacing' if de<=0 or abs(de)<100 else 'finite-difference'})
# 104Pd table gives B(E2), J2/B(E2); derive J2 with propagated independent table errors, clearly marked derived.
pd=[(16,.26,.02,112.3,8.6),(18,.22,.02,140.9,12.8),(20,.19,.01,334.2,17.6),(22,.13,.01,282.3,21.7),(24,.07,.01,554.3,79.2)]
for I,B,sB,R,sR in pd:
    J=B*R;sJ=math.sqrt((R*sB)**2+(B*sR)**2)
    rows.append({'nucleus':'104Pd','center_spin':I,'Egamma_I_keV':'','Egamma_Iplus2_keV':'','delta_Egamma_keV':'','omega_center_MeV_over_hbar':'','J2_hbar2_per_MeV':J,'J2_sigma':sJ,'BE2_e2b2':B,'BE2_sigma':sB,'J2_over_BE2':R,'J2_over_BE2_sigma':sR,'interpretation':'derived as B(E2) times tabulated J2/B(E2); not independently extracted from Eγ'})
fields=sorted({k for r in rows for k in r})
with (OUT/'j2_systematics.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
# model formulas and unit checks
model={'direct_user_formula':{'omega':'(I-Js)/Jcore + 3*V2*(I-I0)/(A**2)', 'A':'j1*j2 or a defined shears slope','J2':'1/(1/Jcore + 3*V2/A**2)','condition':'If all quantities are fixed, J2 is constant; theta dependence requires A,V2,Jcore or I0 to vary with theta/I.'},'constrained_particle_rotor_derivation':{'E_s':'V2*P2(c), I_s=I0+A*c, c=cos(theta)','omega_s':'dE_s/dI_s = 3*V2*c/A','total_I':'I=I_s+Jcore*omega_s = I0 + (A + 3*Jcore*V2/A)*c','J2':'dI/domega_s = Jcore + A**2/(3*V2)','closure':'theta->0 gives c->1 and finite omega_s=3V2/A; dE/dtheta and dI/dtheta both vanish as sin(theta), so no singularity in the ratio.'},'signs':{'V2_positive':'positive curvature and positive J2 in the quadratic model','V2_zero':'shears-only linearization has divergent J2; a finite J2 requires core inertia or higher-order terms','negative_finite_difference':'not automatically a physical negative inertia; inspect level ordering, line overlap, backbend and uncertainties'}}
(OUT/'j2_model_derivation.json').write_text(json.dumps(model,ensure_ascii=False,indent=2))
print(json.dumps({'rows':rows,'model':model},ensure_ascii=False,indent=2))
