#!/usr/bin/env python3
"""Toy, reproducible Ba-chain scan for two-octupole anharmonicity and CoulEx.

Every numerical parameter below is an illustrative model input unless it is
explicitly labelled as a Bucher benchmark.  The program is a sensitivity
study, not a GOSIA replacement or an ENSDF evaluator.
"""
from __future__ import annotations
import argparse, csv, json, math
from pathlib import Path

ISOTOPES = range(140, 151, 2)
J_VALUES = (0, 2, 4, 6)

def logistic(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))

def row(A: int, e3: float, deformation: float, rho: float, v4: float,
        anh: float, phase: float, gdr_ratio: float) -> dict:
    # Symmetric 3x3 phonon coupling gives the ideal occupation enhancement.
    ideal_b_ratio = 2.0
    # Pauli blocking is represented as an amplitude overlap penalty.  The
    # 4p-4h coordinate increases towards the deformed side of the chain.
    pauli_overlap = 0.18 + 0.32 * (A - 140) / 10.0
    q_amp = math.exp(-0.62 * pauli_overlap - 0.78 * v4)
    q_b = q_amp * q_amp
    b_ratio = ideal_b_ratio * q_b
    # Non-harmonic shifts: J=0 is lowered, high J is pushed up.
    shifts = {0: -0.55 * anh, 2: -0.10 * anh, 4: 0.28 * anh, 6: 0.72 * anh}
    energies = {J: 2.0 * e3 + shifts[J] for J in J_VALUES}
    # Doorway spreading estimate and finite-energy intensity fraction.
    sigma_v = 0.145 + 0.035 * v4
    gamma_down = 2.0 * math.pi * sigma_v**2 * rho
    gamma_rms = math.sqrt(sigma_v**2 * (1.0 + rho * 0.35))
    # Two coherent second-order paths. The relative GDR term is an effective
    # fitted ratio, not a measured Ba matrix element.
    a_oct = q_amp * math.sqrt(ideal_b_ratio)
    a_gdr = gdr_ratio * (1.0 / math.sqrt(1.0 + (14.5 / 4.0)**2))
    a_total = a_oct + a_gdr * math.cos(phase)
    interference_factor = (a_total * a_total) / (a_oct * a_oct)
    # A schematic E3 branch competition: E3 width scales E_gamma^7 and a
    # fragmented doorway receives exp(-Gamma_down / spacing) of the strength.
    e_gamma = max(0.15, 2.0 * e3 - 0.45)
    e3_width = (e_gamma / 1.0)**7 * q_b
    e2_competitor = 0.35 * (max(0.15, e_gamma + 0.25) / 1.0)**5
    branch_e3 = e3_width / (e3_width + e2_competitor + 0.20)
    return dict(A=A, N=A-56, e3_mev=e3, two_phonon_harmonic_mev=2*e3,
                deformation_proxy=deformation, rho_background_mev_inv=rho,
                four_p_four_h_mix=v4, anharmonic_scale_mev=anh,
                pauli_overlap=pauli_overlap, q_amplitude=q_amp,
                quenching_factor_B=q_b, ideal_B_ratio=ideal_b_ratio,
                quenched_B_ratio=b_ratio, gamma_down_mev=gamma_down,
                gamma_rms_mev=gamma_rms, gdr_relative_amplitude=gdr_ratio,
                relative_phase_rad=phase, coulex_interference_factor=interference_factor,
                e3_branch_fraction=branch_e3, **{f'E2ph_J{J}_mev': energies[J] for J in J_VALUES})

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--out-dir', type=Path, default=Path('.'))
    args = ap.parse_args(); args.out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    # e3 and deformation are smooth illustrative trends anchored to the
    # measured strong E3 region of 144,146Ba, not adopted level energies.
    for A in ISOTOPES:
        x = (A - 145) / 5.0
        e3 = 0.82 - 0.035 * x
        deformation = 0.12 + 0.045 * logistic((A-144)/2.0)
        rho = 3.8 + 1.15 * (A-140)/10.0
        v4 = 0.08 + 0.34 * logistic((A-145)/1.8)
        anh = 0.06 + 0.28 * deformation + 0.12 * v4
        for phase in (0.0, math.pi):
            rows.append(row(A, e3, deformation, rho, v4, anh, phase,
                            # Tuned effective amplitude deliberately spans the
                            # destructive-interference regime; it is not a
                            # measured GDR matrix element.
                            gdr_ratio=2.25 + 0.55*v4))
    csv_path = args.out_dir/'ba_two_phonon_scan.csv'
    with csv_path.open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    payload = {'schema':'ba-two-phonon-octupole-v1',
               'status':'illustrative_model_scan_not_experimental_data',
               'bucher_benchmarks': {'144Ba_B_E3_Wu':'48 +25/-34', '146Ba_B_E3_Wu':'48 +21/-29'},
               'equations': {'gamma_down':'2*pi*sigma_V^2*rho', 'B_ratio':'2*Q_B',
                             'Q_B':'Q_amplitude^2', 'interference':'|A_oct+A_gdr cos(phi)|^2/|A_oct|^2'},
               'rows': rows}
    (args.out_dir/'ba_two_phonon_scan.json').write_text(json.dumps(payload, indent=2)+'\n')
    try:
        import matplotlib.pyplot as plt
        even = [r for r in rows if r['relative_phase_rad'] == 0.0]
        fig, ax = plt.subplots(1, 2, figsize=(10, 4))
        ax[0].plot([r['A'] for r in even], [r['quenched_B_ratio'] for r in even], 'o-', label='2 Q_B')
        ax[0].axhline(2, color='0.5', ls='--', label='ideal 2')
        ax[0].set(xlabel='A (Ba)', ylabel='B(two-phonon)/B(single)', title='Pauli + 4p–4h quenching'); ax[0].legend()
        ax[1].plot([r['A'] for r in even], [r['E2ph_J0_mev'] for r in even], 'o-', label='J=0')
        ax[1].plot([r['A'] for r in even], [r['E2ph_J6_mev'] for r in even], 's-', label='J=6')
        ax[1].set(xlabel='A (Ba)', ylabel='energy (MeV)', title='anharmonic multiplet endpoints'); ax[1].legend()
        fig.tight_layout(); fig.savefig(args.out_dir/'ba_two_phonon_scan.svg'); plt.close(fig)
    except Exception as exc:
        (args.out_dir/'plot_error.txt').write_text(str(exc)+'\n')

if __name__ == '__main__': main()
