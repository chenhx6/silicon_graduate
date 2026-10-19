#!/usr/bin/env python3
"""Conditional local Eq.3/4 identities, not a source-data or lifetime fit."""
import hashlib
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def main():
    contract = RUN / 'bethge1966-exercise-contract.json'
    c = json.loads(contract.read_text())
    assert hashlib.sha256((ROOT / c['source_pdf']).read_bytes()).hexdigest() == c['source_pdf_sha256']
    K, g, Si, So, b, N0, N, C = s.symbols('K g S_i S_o b N0 N C', positive=True)
    eff = (K*Si + g*So)/(K+g)
    printed = N0*C/(N*(K+g))
    assert s.simplify(eff.subs(So, Si) - Si) == 0
    assert s.limit(eff, g, 0) == Si
    assert s.limit(eff, g, s.oo) == So
    t = s.symbols('t', real=True)
    assert s.simplify(eff.subs({Si: Si+t, So: So-K*t/g}, simultaneous=True)-eff) == 0
    assert s.simplify(printed.subs(N0, b*N0)/printed-b) == 0
    # Two charge components with adjacent integer charge states; this identity
    # concerns moments only and asserts nothing about actual Fig.4/5 fractions.
    f = s.symbols('f', real=True)
    n = s.symbols('n', integer=True, nonnegative=True)
    mean = (1-f)*n + f*(n+1)
    second = (1-f)*n*n + f*(n+1)**2
    assert s.simplify(second-mean**2-f*(1-f)) == 0
    result = {'source_contract': c, 'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'effective_local_stopping': str(eff),
              'unresolved_direction': {'Delta_S_i': 't', 'Delta_S_o': '-K*t/g'},
              'source_N0_scale_response': 'S_inferred -> b*S_inferred when N0_inferred=b*N0_true',
              'conditional_shared_scale_covariance': 'Cov(S_i,S_j)|scale = Var(b)*T_i*T_j; rank1 for fixed T',
              'charge_second_minus_mean_squared': str(s.factor(second-mean**2)),
              'checks': ['equalpaths', 'incominglimit', 'outgoinglimit', 'localnull', 'N0scale', 'chargemoment'],
              'actual_source_Sigma_or_lifetime_recovered': False,
              'IAEA_digitization_normalization_certified': False, 'ok': True}
    (RUN / 'bethge1966-exercise-result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
