#!/usr/bin/env python3
"""SI/nuclear-unit E2 rate audit; no 129Ba absolute B estimate or refit."""
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'


def main():
    # NIST 2022 CODATA allascii snapshot, retrieved during checkpoint046.
    h, e, c = 6.62607015e-34, 1.602176634e-19, 299792458.0
    eps0, alpha = 8.8541878188e-12, 7.2973525643e-3
    hbar = h/(2*math.pi)
    mev_joule = 1e6*e
    fm_metre = 1e-15
    hbar_mev_s = hbar/mev_joule
    hbarc_mev_fm = hbar_mev_s*c/fm_metre
    prefactor = 4*math.pi/75
    si_coeff = prefactor/hbar*(mev_joule/(hbar*c))**5 * e*e/(4*math.pi*eps0) * fm_metre**4
    nuclear_coeff = prefactor/hbar_mev_s/hbarc_mev_fm**5*(alpha*hbarc_mev_fm)
    eb2_coeff = si_coeff*1e4  # 1 b^2 = 10^4 fm^4
    mean_tau_ps_coeff = 1e12/eb2_coeff
    checks = {'SI_and_nuclear_routes_agree':abs(si_coeff/nuclear_coeff-1)<1e-9,
              'E2_coeff_standard_order':1.22e9<si_coeff<1.23e9,
              'barn_conversion':abs(eb2_coeff/si_coeff-1e4)<1e-9,
              'mean_lifetime_coefficient':.081<mean_tau_ps_coeff<.082}
    raw_paths = [
        'raw/papers/2024_Chakraborty et al_Exploring the possibility of wobbling motion in Ba 129.pdf',
        'raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/review/1982_Lange et al_E0-E2-M1 multipole admixtures of transitions in even-even nuclei.pdf']
    out = dict(constants={'h_Js':h,'e_C':e,'c_m_per_s':c,'epsilon0_F_per_m':eps0,'alpha':alpha},
               constants_source='https://physics.nist.gov/cuu/Constants/Table/allascii.txt',
               constants_snapshot='nist-constants-046.txt',
               formula_locator='LKH82 printed p.121 Eq.2.2; SI conversion explicitly inserts 1/(4*pi*epsilon0)',
               coefficient_per_e2fm4_sinv_MeVminus5=si_coeff,
               independent_nuclear_unit_coefficient=nuclear_coeff,
               coefficient_per_e2b2_sinv_MeVminus5=eb2_coeff,
               B_e2b2_mean_tau_ps_coefficient=mean_tau_ps_coeff,
               B_formula='B(E2)[e2 b2]=C*q_line_gamma*f_E2/(tau_mean_ps*E_MeV^5)',
               f_E2_definition='delta^2/(1+delta^2), only within the retained M1/E2 photon components',
               q_definition='absolute probability of a photon in that line per parent decay; not total branch or gamma-relative intensity',
               checks=checks,
               raw_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in raw_paths},
               absolute_B_129Ba_e2b2=None,experimental_CI_recovered=False,delta_refit=False,
               missing=['actual mean lifetime','absolute line photon branch','IC/other inventory','matching angular-response producer and joint covariance'],
               retired_038='missing electromagnetic charge factor and arbitrary b=.65/tau sweep; old W.u. claims and fixed wobbling thresholds remain withdrawn')
    (RUN/'e2-unit-scope-046.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'checks':checks,'rate_coefficient':si_coeff,'mean_tau_coefficient':mean_tau_ps_coeff,'actual_B':None}))
    return 0 if all(checks.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
