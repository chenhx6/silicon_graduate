"""Conditional same-I^pi E0/radius block; no nuclear fit or mixing extraction."""
from pathlib import Path
import json
import numpy as np

OUT=Path(__file__).resolve().parent

def evaluate(delta,W,phi,R1,R2,t):
    D=np.hypot(delta,2*W)
    if D==0:raise ValueError('Degenerate H does not select an eigenvector mixing angle')
    eta=(1-delta/D)/2
    c,s=np.sqrt(1-eta),np.sqrt(eta)
    U=np.array([[c,s],[-np.exp(-1j*phi)*s,np.exp(-1j*phi)*c]])
    H=np.array([[0,W*np.exp(1j*phi)],[W*np.exp(-1j*phi),delta]],complex)
    T=np.array([[R1,t],[np.conj(t),R2]],complex)
    Hp=U.conj().T@H@U;Tp=U.conj().T@T@U
    z=t*np.exp(-1j*phi);x,y=z.real,z.imag;dr=R1-R2
    amp=(W*dr+delta*x)/D+1j*y
    rL=(1-eta)*R1+eta*R2-2*np.sqrt(eta*(1-eta))*x
    rU=eta*R1+(1-eta)*R2+2*np.sqrt(eta*(1-eta))*x
    assert np.allclose(U.conj().T@U,np.eye(2))
    assert abs(Hp[0,1])<1e-14 and np.isclose(Hp[1,1]-Hp[0,0],D)
    assert np.allclose(Tp,[[rL,amp],[np.conj(amp),rU]])
    assert np.isclose((rL-rU)**2+4*abs(amp)**2,dr**2+4*abs(t)**2)
    assert np.isclose(np.linalg.det(Tp),np.linalg.det(T))
    comm=H@T-T@H
    assert np.isclose(np.linalg.norm(comm)**2,2*D**2*abs(amp)**2)
    # Changing configuration-state phases changes coordinates of both operators/U.
    S=np.diag(np.exp(1j*np.array([.27,-.41])))
    Hg=S.conj().T@H@S;Tg=S.conj().T@T@S;Ug=S.conj().T@U
    assert np.allclose(Ug.conj().T@Tg@Ug,Tp)
    assert np.allclose(Tg[0,1]*np.conj(Hg[0,1]),T[0,1]*np.conj(H[0,1]))
    return dict(delta_MeV=delta,W_MeV=W,phi=phi,eta=eta,D_MeV=D,
                config_R1_fm2=R1,config_R2_fm2=R2,t_fm2=[float(t.real),float(t.imag)],
                mixed_radius_lower_fm2=float(rL),mixed_radius_upper_fm2=float(rU),
                mixed_amplitude_fm2=[float(amp.real),float(amp.imag)],
                T_eigenvalues_fm2=np.linalg.eigvalsh(T).tolist(),
                commutator_Frobenius2_MeV2fm4=float(np.linalg.norm(comm)**2))

diagonal=evaluate(.7,.3,0.,10.,12.,0.+0j)
assert np.isclose(abs(complex(*diagonal['mixed_amplitude_fm2']))**2,
                  diagonal['eta']*(1-diagonal['eta'])*4)
general=evaluate(.7,.3,.37,10.,12.,.6+.2j)
cancel=evaluate(1/np.sqrt(2),1/(2*np.sqrt(2)),0.,10.,12.,1.+0j)
assert np.linalg.norm(cancel['mixed_amplitude_fm2'])<1e-14
assert min(cancel['T_eigenvalues_fm2'])>0
at_crossing=evaluate(0.,.5,0.,10.,12.,1.+0j)
assert np.allclose(at_crossing['mixed_amplitude_fm2'],[-1.,0.])
no_H_mixing=evaluate(1.,0.,0.,10.,12.,.4+.2j)
assert no_H_mixing['eta']==0 and np.allclose(no_H_mixing['mixed_amplitude_fm2'],[.4,.2])

result=dict(scope='same-Ipi two-state scalar/radius operator; conditional arbitrary numbers, not any isotope',
            convention='Ucolumns(lower,upper);H12=Wexp(i phi);T12=t;R1/R2mean-square radii',
            units=dict(H='MeV',T='fm2',E0rho='dimensionlessafterZ/R0²factor'),
            diagonal_HW14_limit=diagonal,general_complex_example=general,
            cancellation_without_zero_Hmixing_or_zero_config_radius_difference=cancel,
            exact_unmixed_crossing_real_t_does_not_cancel_Delta=at_crossing,
            zero_Hmixing_but_offdiagonal_T=no_H_mixing,
            no_actual_Z_or_R0_assigned=True,no_data_fit=True,no_nuclear_mixing_percent_assigned=True)
(OUT/'e0-kernel-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(cancel=cancel,maximal_mixing_amplitude=at_crossing['mixed_amplitude_fm2']),indent=2))
