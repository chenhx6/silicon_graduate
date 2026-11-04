#!/usr/bin/env python3
"""Conditional phonon descriptors and source-aware E2 branch arithmetic.

The finite polynomial E_n=n*hw+g*n*(n-1) is a synthetic number-diagonal
ansatz. Its g (legacy name g4) neither mixes states nor specifies an E2
operator. It is not a microscopic rotor diagonalization. Negative g is
only used within an explicitly ordered finite truncation, never at all n.
BM-II printed 192-193, Eqs.4-308--4-314; Jensen2002 PDF2-4;
Sensharma2019 PDF3-4; Petrache2025 Ch.2 PDF47-48,55-57.
"""
import argparse
import json
import math
import numpy as np

PRESETS = {
    'synthetic_softening': {
        'nucleus': 'synthetic oscillator (no isotope data)',
        'description': 'Illustrative number-diagonal spectrum; no measured strengths',
        'spin': 23.5, 'hbar_omega_w_keV': 280.0, 'g4_anharmonicity_keV': -35.0,
    },
}
# Retain old command names only as explicitly synthetic compatibility aliases.
for _key in ('163Lu_TSD2_two_phonon_benchmark', '135Pr_normal_deformed_two_phonon',
             '187Au_longitudinal_two_phonon'):
    PRESETS[_key] = dict(PRESETS['synthetic_softening'],
        description=f'SYNTHETIC legacy alias {_key}; not an isotope benchmark')


def finite(value, name, minimum=None, positive=False):
    if isinstance(value, bool):
        raise ValueError(f'{name} must be finite numeric input')
    x = float(value)
    if not math.isfinite(x) or (minimum is not None and x < minimum) or (positive and x <= 0):
        raise ValueError(f'invalid {name}')
    return x


def spin_value(value):
    x = finite(value, 'spin', minimum=0)
    if not (2*x).is_integer():
        raise ValueError('spin must be integer or half-integer')
    return x


def oscillator_operator_strengths(linear_amplitude, quadratic_amplitude=0.0):
    """Squared Fock matrix elements for T=t1*(a+a†)+t2*(a+a†)^2.

    These are dimensionless oscillator strengths, NOT nuclear reduced B(E2).
    A quadratic term permits 2->0 even when the Hamiltonian is harmonic.
    """
    t1 = finite(linear_amplitude, 'linear_amplitude')
    t2 = finite(quadratic_amplitude, 'quadratic_amplitude')
    return {'squared_1_to_0': t1*t1, 'squared_2_to_1': 2*t1*t1,
            'squared_2_to_0': 2*t2*t2,
            'scope': 'Fock matrix elements only; nuclear angular momentum factors not included'}


def yrast_referenced_excitation(spin, band_energy_keV, yrast_energies,
                                same_signature=False, covariance_keV2=None):
    """Explicit same-I subtraction or equal-weight I-1/I+1 yrast reference.

    Input covariance ordering is [band, ref] or [band, ref_minus, ref_plus].
    Missing neighbours return null. No extrapolation or phonon assignment.
    """
    i = spin_value(spin)
    e = finite(band_energy_keV, 'band_energy_keV')
    if not isinstance(same_signature, bool):
        raise ValueError('same_signature must be boolean')
    refs = {}
    for key, val in yrast_energies.items():
        q = spin_value(key)
        if q in refs:
            raise ValueError('duplicate reference spin')
        refs[q] = finite(val, 'yrast_energy')
    required = [i] if same_signature else [i-1, i+1]
    weights = np.array([1., -1.]) if same_signature else np.array([1., -.5, -.5])
    missing = [q for q in required if q not in refs]
    out = {'spin': i, 'required_reference_spins': required, 'missing_reference_spins': missing,
           'reference_rule': 'same-spin' if same_signature else 'mean-of-I-minus-1-and-I-plus-1',
           'excitation_keV': None, 'sigma_keV': None, 'physical_assignment': None}
    c = None
    if covariance_keV2 is not None:
        c = np.asarray(covariance_keV2, dtype=float)
        n = len(weights)
        if c.shape != (n,n) or not np.all(np.isfinite(c)):
            raise ValueError('invalid covariance shape or entries')
        tol = 1e-10*max(float(np.max(np.abs(c))), np.finfo(float).tiny)
        if np.max(np.abs(c-c.T)) > tol or np.any(np.diag(c)<0) or np.linalg.eigvalsh((c+c.T)/2)[0] < -tol:
            raise ValueError('covariance must be symmetric positive semidefinite')
    if not missing:
        values = [e]+[refs[q] for q in required]
        out['excitation_keV'] = math.fsum(w*x for w,x in zip(weights,values))
        if c is not None:
            out['sigma_keV'] = math.sqrt(max(0.,float(weights @ c @ weights)))
    return out


def e2_photon_width_ratio(b_numerator, b_denominator, e_numerator_keV, e_denominator_keV):
    """E2 partial photon widths: lambda_num/lambda_den=(B_num/B_den)*(E_num/E_den)^5."""
    bn = finite(b_numerator, 'B_numerator', minimum=0)
    bd = finite(b_denominator, 'B_denominator', positive=True)
    en = finite(e_numerator_keV, 'E_numerator', positive=True)
    ed = finite(e_denominator_keV, 'E_denominator', positive=True)
    return bn/bd*(en/ed)**5


def be2_ratios_for_mixing_branches(*, e_out_keV, e_in_keV, photon_intensity_ratio,
                                  delta_branches, inband_e2_fraction,
                                  common_initial_state, efficiency_corrected):
    """Preserve every supplied real delta(E2/M1) branch; no model-selected root.

    Photon intensities must be efficiency corrected for SAME parent state.
    B_out/B_in = I_gamma_out/I_gamma_in * (E_in/E_out)^5 * fE2_out/fE2_in.
    For total (gamma+conversion) intensities the formula differs: convert first.
    No experimental errors are inferred from central inputs.
    """
    if common_initial_state is not True or efficiency_corrected is not True:
        raise ValueError('requires same-parent, efficiency-corrected photon intensities')
    eo = finite(e_out_keV, 'e_out_keV', positive=True)
    ei = finite(e_in_keV, 'e_in_keV', positive=True)
    ratio = finite(photon_intensity_ratio, 'photon_intensity_ratio', minimum=0)
    fi = finite(inband_e2_fraction, 'inband_e2_fraction', positive=True)
    if fi>1 or not delta_branches:
        raise ValueError('require inband fraction <=1 and nonempty delta branches')
    rows=[]
    for val in delta_branches:
        d=finite(val,'delta')
        # Stable E2 fraction without squaring very large delta.
        f = (d/math.hypot(1.,d))**2
        rows.append({'delta':d,'e2_fraction':f,
                     'BE2_out_over_in':ratio*(ei/eo)**5*f/fi,
                     'uncertainty':None})
    return {'branches':rows,'branch_selected':None,'physical_assignment':None,
            'intensity_convention':'efficiency-corrected photons from same parent',
            'uncertainty_status':'central-value arithmetic only'}


class MultiphononWobblingSolver:
    def __init__(self, spin=23.5, hbar_omega_w_keV=280., g4_anharmonicity_keV=-35.,
                 mixing_epsilon=None, B_E2_in_e2b2=None,
                 transition_strengths=None, gamma_energies_keV=None):
        self.I=spin_value(spin)
        self.omega_w=finite(hbar_omega_w_keV,'hbar_omega_w_keV',positive=True)
        self.g=finite(g4_anharmonicity_keV,'g4_anharmonicity_keV')
        self.legacy={}
        if mixing_epsilon is not None:
            self.legacy['mixing_epsilon']=finite(mixing_epsilon,'mixing_epsilon')
        if B_E2_in_e2b2 is not None:
            self.legacy['B_E2_in_e2b2']=finite(B_E2_in_e2b2,'B_E2_in_e2b2',minimum=0)
        self.strengths={} if transition_strengths is None else dict(transition_strengths)
        self.gamma={} if gamma_energies_keV is None else dict(gamma_energies_keV)

    def calculate_phonon_energies(self,max_phonon=3):
        if isinstance(max_phonon,bool) or not isinstance(max_phonon,int) or not 1<=max_phonon<=100:
            raise ValueError('max_phonon must be an integer from 1 to 100')
        energies={f'n_w_{n}':n*self.omega_w+self.g*n*(n-1) for n in range(max_phonon+1)}
        if any(self.omega_w+2*self.g*n<=0 for n in range(max_phonon)):
            raise ValueError('number-diagonal ansatz is not ordered within requested truncation')
        return energies

    def calculate_transition_rates(self):
        vals={}
        for key in ('10','21','20'):
            v=self.strengths.get(key)
            vals[key]=None if v is None else finite(v,f'B(E2)_{key}',minimum=0)
        def ratio(a,b):
            return None if a is None or b is None or b==0 else a/b
        w=None
        if vals['20'] is not None and vals['21'] is not None and vals['21']>0 and all(k in self.gamma for k in ('20','21')):
            w=e2_photon_width_ratio(vals['20'],vals['21'],self.gamma['20'],self.gamma['21'])
        return {'B_E2_1_to_0_e2b2':vals['10'],'B_E2_2_to_1_e2b2':vals['21'],
                'B_E2_2_to_0_e2b2':vals['20'],
                'strength_ratio_21_over_10':ratio(vals['21'],vals['10']),
                'strength_ratio_20_over_21':ratio(vals['20'],vals['21']),
                'e2_partial_photon_width_ratio_20_over_21':w,
                'input_origin':'caller-supplied strengths, not derived from energy ansatz',
                'missing_strengths':[k for k,v in vals.items() if v is None]}

    def solve_multiphonon_properties(self):
        en=self.calculate_phonon_energies()
        return {'spin':self.I,'fundamental_omega_w_keV':self.omega_w,
                'anharmonicity_g4_keV':self.g,'excitation_energies_keV':en,
                'energy_ratio_R21':en['n_w_2']/en['n_w_1'],
                'energy_ratio_R31':en['n_w_3']/en['n_w_1'],
                'electromagnetic_rates':self.calculate_transition_rates(),
                'wobbling_classification':None,'is_two_phonon_confirmed':None,
                'model_scope':'synthetic number-diagonal ansatz, finite n=0..3; not a nuclear assignment',
                'spectrum_trend':'softening' if self.g<0 else 'stiffening' if self.g>0 else 'harmonic-spacing',
                'legacy_parameters_ignored':self.legacy,
                'limitations':['g does not generate wave-function mixing or an E2 operator',
                               'negative g is not a globally bounded oscillator Hamiltonian',
                               'real bands need spin/signature-aware yrast references',
                               'no strength or energy threshold establishes a two-phonon assignment']}


def run_multiphonon_wobbling_analysis(nucleus='synthetic',spin=23.5,hbar_omega_w_keV=280.,
                                      g4_anharmonicity_keV=-35.,mixing_epsilon=None,
                                      B_E2_in_e2b2=None,transition_strengths=None,gamma_energies_keV=None):
    solver=MultiphononWobblingSolver(spin,hbar_omega_w_keV,g4_anharmonicity_keV,
                                   mixing_epsilon,B_E2_in_e2b2,transition_strengths,gamma_energies_keV)
    res=solver.solve_multiphonon_properties();res['nucleus']=nucleus
    res['data_origin']='synthetic spectrum; optional strengths are caller supplied'
    return res


def format_text_report(output,title='Conditional phonon descriptors'):
    return '\n'.join([title,output['model_scope'],f"Input label: {output['nucleus']}",
        f"Energies (keV): {output['excitation_energies_keV']}",
        f"R21 = {output['energy_ratio_R21']:.6f}; trend: {output['spectrum_trend']}",
        f"Strengths: {output['electromagnetic_rates']}",
        'Two-phonon assignment: not determined. Legacy mixing inputs do not define an operator.'])


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--preset',choices=list(PRESETS),default='synthetic_softening')
    parser.add_argument('--spin',type=float)
    parser.add_argument('--omega',type=float)
    parser.add_argument('--g4',type=float)
    parser.add_argument('--json',action='store_true')
    args=parser.parse_args();p=PRESETS[args.preset]
    try:
        r=run_multiphonon_wobbling_analysis(nucleus=p['nucleus'],
            spin=p['spin'] if args.spin is None else args.spin,
            hbar_omega_w_keV=p['hbar_omega_w_keV'] if args.omega is None else args.omega,
            g4_anharmonicity_keV=p['g4_anharmonicity_keV'] if args.g4 is None else args.g4)
    except ValueError as e: parser.error(str(e))
    print(json.dumps(r,indent=2,allow_nan=False) if args.json else format_text_report(r))


if __name__=='__main__': main()
