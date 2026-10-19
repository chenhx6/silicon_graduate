#!/usr/bin/env python3
"""Two-body vertex constraints with declared inputs, not a DSAM gate refit."""
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def solve(beam_mass, target_mass, alpha_mass, recoil_mass, beam_T, angle):
    beam_p = math.sqrt(beam_T*(beam_T+2*beam_mass))
    total_E = beam_mass+target_mass+beam_T
    invariant_s = total_E**2-beam_p**2
    D = (invariant_s+alpha_mass**2-recoil_mass**2)/2
    b = beam_p*math.cos(math.radians(angle))
    A = total_E**2-b*b
    B = -2*D*b
    C = total_E**2*alpha_mass**2-D*D
    discriminant = B*B-4*A*C
    if discriminant < 0:
        return []
    q = -.5*(B+math.copysign(math.sqrt(discriminant), B))
    roots = [q/A, C/q] if q else [-B/(2*A)]
    out = []
    for p in sorted(roots):
        if p < 0:
            continue
        Ea = math.hypot(alpha_mass,p)
        pr2 = beam_p*beam_p+p*p-2*b*p
        Er = math.sqrt(recoil_mass*recoil_mass+pr2)
        residual = total_E-Ea-Er
        if abs(residual)>1e-7:
            continue  # rejects an extraneous squared-equation root.
        # Check the same solution through the centre-of-mass Lorentz transform.
        root_s=math.sqrt(invariant_s)
        beta_cm=beam_p/total_E
        gamma_cm=total_E/root_s
        expected_cm_E=(invariant_s+alpha_mass**2-recoil_mass**2)/(2*root_s)
        transformed_cm_E=gamma_cm*(Ea-beta_cm*p*math.cos(math.radians(angle)))
        assert abs(transformed_cm_E-expected_cm_E)<1e-7
        pz_cm=gamma_cm*(p*math.cos(math.radians(angle))-beta_cm*Ea)
        pt_cm=p*math.sin(math.radians(angle))
        assert abs((pz_cm*pz_cm+pt_cm*pt_cm)-(expected_cm_E**2-alpha_mass**2))<1e-5
        out.append({'alpha_p_MeV_c':p,'alpha_vertex_T_MeV':Ea-alpha_mass,
                    'recoil_T_MeV':Er-recoil_mass,
                    'fourmomentum_energy_residual_MeV':residual,
                    'CM_energy_residual_MeV':transformed_cm_E-expected_cm_E,
                    'recoil_beta':math.sqrt(pr2)/Er})
    return out


def main():
    contract = RUN/'sun-alpha-kinematic-contract.json'
    c = json.loads(contract.read_text())
    assert c['identity']=='SUN23-ALPHA-GATE-VERTEX-KINEMATIC-01'
    assert hashlib.sha256((RUN/c['input_mass_fixture_receipt']).read_bytes()).hexdigest()==c['input_receipt_sha256']
    m = c['masses_MeV']
    mb, mt, ma, mr = m['32_16'],m['3_2'],m['4_2'],m['31_16']
    sdkQ = mb+mt-ma-mr
    results=[]
    max_Q_difference=0
    for state in c['source_states']:
        ex=state['Ex_MeV']
        rows=[]
        for angle in c['angles_deg']:
            source_recoil = mb+mt-ma-c['source_Q0_MeV']+ex
            roots=solve(mb,mt,ma,source_recoil,c['beam_vertex_kinetic_MeV'],angle)
            sdk_roots=solve(mb,mt,ma,mr+ex,c['beam_vertex_kinetic_MeV'],angle)
            assert roots and sdk_roots
            high, sdk_high=roots[-1],sdk_roots[-1]
            Tb=c['beam_vertex_kinetic_MeV']
            P=math.sqrt(Tb*(Tb+2*mb))
            Etot=mb+mt+Tb
            Ta=high['alpha_vertex_T_MeV']
            pa=high['alpha_p_MeV_c']
            cosine=math.cos(math.radians(angle))
            jacobian=(-Etot+P*cosine*(ma+Ta)/pa)/source_recoil
            def excitation_from_alpha(t):
                pp=math.sqrt(t*(t+2*ma))
                recoil2=(Etot-ma-t)**2-(P*P+pp*pp-2*P*pp*cosine)
                return math.sqrt(recoil2)-(mb+mt-ma-c['source_Q0_MeV'])
            finite=(excitation_from_alpha(Ta+.001)-excitation_from_alpha(Ta-.001))/.002
            assert abs(jacobian-finite)<1e-6
            half=c['gate_full_width_MeV']/2
            exact_width=excitation_from_alpha(Ta-half)-excitation_from_alpha(Ta+half)
            max_Q_difference=max(max_Q_difference,abs(high['alpha_vertex_T_MeV']-sdk_high['alpha_vertex_T_MeV']))
            rows.append({'angle_deg':angle,'all_physical_roots':roots,
                         'SDK_Q_high_root_alpha_T_MeV':sdk_high['alpha_vertex_T_MeV'],
                         'dEx_dTalpha_at_fixed_angle_no_losses':jacobian,
                         'Ex_full_width_from_2MeV_Talpha_window_no_losses':exact_width})
        high_values=[x['all_physical_roots'][-1]['alpha_vertex_T_MeV'] for x in rows]
        assert all(a>=b for a,b in zip(high_values,high_values[1:]))
        dense=[solve(mb,mt,ma,mb+mt-ma-c['source_Q0_MeV']+ex,c['beam_vertex_kinetic_MeV'],i*13/100)[-1]['alpha_vertex_T_MeV'] for i in range(101)]
        assert all(a>=b for a,b in zip(dense,dense[1:]))
        gate=state['gate_center_MeV'];half=c['gate_full_width_MeV']/2
        results.append({'source_state':state,'angle_roots':rows,
                        'declared_high_root_vertex_envelope_MeV':[min(dense),max(dense)],
                        'vertex_minus_printed_gate_center_MeV':[min(dense)-gate,max(dense)-gate],
                        'printed_gate_interval_if_direct_vertex_assumption':[gate-half,gate+half],
                        'gate_interval_overlaps_declared_vertex_envelope':max(gate-half,min(dense))<=min(gate+half,max(dense)),
                        'not_an_inferred_target_loss_or_experiment_disagreement':True})
    out={'identity':c['identity'],'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'contract_sha256':hashlib.sha256(contract.read_bytes()).hexdigest(),
         'SDK_ground_state_Q_MeV':sdkQ,'source_printed_Q0_MeV':c['source_Q0_MeV'],
         'max_high_root_shift_if_SDK_Q_used_MeV':max_Q_difference,
         'states':results,'no_actual_sorter_or_loss_response_recovered':True,'ok':True}
    (RUN/'sun-alpha-kinematic-result.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
