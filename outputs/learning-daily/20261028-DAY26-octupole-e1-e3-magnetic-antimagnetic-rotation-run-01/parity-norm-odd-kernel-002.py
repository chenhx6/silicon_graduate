"""Finite parity-only example for BE16 Eq4/5, NOT a Ba SCCM calculation."""
import json
from pathlib import Path
import numpy as np


def solve(overlap=.3, h=.5, k=-.1, d1=0., d3=2.):
    if not abs(overlap)<1:
        raise ValueError("Strictly positive norm required; singular |s|=1 excluded")
    norm=np.array([[1.,overlap],[overlap,1.]])
    ham=np.array([[h,k],[k,h]])  # MeV kernels, not ordinary-basis H
    parity=np.array([[0.,1.],[1.,0.]])
    nval,nvec=np.linalg.eigh(norm)
    root=(nvec*np.sqrt(nval))@nvec.T
    inverse_root=(nvec*(1/np.sqrt(nval)))@nvec.T
    # Generalized eigenvectors f from Hf=ENf; F=N^(1/2) f.
    energies,vectors=np.linalg.eigh(inverse_root@ham@inverse_root)
    coeff=inverse_root@vectors
    labels=np.array([coeff[:,i]@norm@parity@coeff[:,i] for i in range(2)])
    plus=int(np.argmax(labels)); minus=1-plus
    fp,fm=coeff[:,plus],coeff[:,minus]
    odd1=np.diag([d1,-d1]);odd3=np.diag([d3,-d3])
    transition1=float(fm@odd1@fp);transition3=float(fm@odd3@fp)
    exact_gap=2*(h*overlap-k)/(1-overlap**2)
    errors={
        "norm_orthonormality":float(np.max(np.abs(coeff.T@norm@coeff-np.eye(2)))),
        "generalized_eigen_residual_MeV":float(np.max(np.abs(ham@coeff-norm@coeff@np.diag(energies)))),
        "parity_label_error":float(max(abs(labels[plus]-1),abs(labels[minus]+1))),
        "parity_state_inner_product":float(abs(fp@norm@fm)),
        "same_coordinate_densities":float(np.max(np.abs((root@fp)**2-(root@fm)**2))),
        "odd_kernel1_closed_form":abs(abs(transition1)-abs(d1)/np.sqrt(1-overlap**2)),
        "odd_kernel3_closed_form":abs(abs(transition3)-abs(d3)/np.sqrt(1-overlap**2)),
        "energy_gap_closed_form_MeV":abs(float(energies[minus]-energies[plus])-exact_gap),
        "norm_parity_covariance":float(np.max(np.abs(parity@norm@parity-norm))),
        "odd_operator_covariance":float(np.max(np.abs(parity@odd3@parity+odd3))),
    }
    return {"s":overlap,"h_MeV":h,"k_MeV":k,"d1_scaled":d1,"d3_scaled":d3,
            "norm_condition_number":float(nval.max()/nval.min()),
            "energies_MeV":energies.tolist(),"Fplus_density":((root@fp)**2).tolist(),
            "Fminus_density":((root@fm)**2).tolist(),
            "M1_scaled_magnitude":abs(transition1),"M3_scaled_magnitude":abs(transition3),
            "diagnostics":errors}


cases=[solve(d1=d) for d in [0.,.01,.05,.1]]
limits=[solve(overlap=s,d1=.05) for s in [0.,.3,.8]]
splittings=[solve(k=k,d1=.05) for k in [-.2,-.1,0.,.1]]
largest=max(v for row in cases+limits+splittings for v in row['diagnostics'].values())
result={"schema_version":1,"model":"Two nonorthogonal parity-related packets; no angular-momentum projection or physical tensor ranks",
        "operator_units":"D/Dref and Q3/Q3ref are separately dimensionless; no physical E1/E3 ratio or W.u. is computed",
        "source_scope":"BE16 PDF2 Eqs4/5 and PDF4-5 Fig4: motivation only; matrices are task-chosen, not production kernels",
        "wavefunctions_fixed_operator_changed":cases,"norm_and_orthogonal_limit":limits,
        "energies_changed_kernels_fixed":splittings,"largest_numerical_identity_residual":largest,
        "boundary":"Identical coordinate densities do not determine odd-operator transitions. This toy does not reproduce Ba occupancies, locate its dipole zero, or discriminate actual static/soft nuclear shapes."}

if __name__=="__main__":
    assert largest<1e-12,largest
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'largest_identity_residual':largest,'cases':[{k:r[k] for k in ['d1_scaled','M1_scaled_magnitude','M3_scaled_magnitude']} for r in cases]},indent=2))
