"""Audit supplied analysis functions and a sign ambiguity; never modify raw files."""
from pathlib import Path
import hashlib
import json
import sys
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/'raw/writing/pado/Upload/analysis'))
import YAnalysis as analysis

def main():
    source = ROOT/'raw/writing/pado/Upload/analysis/YAnalysis.py'
    before = hashlib.sha256(source.read_bytes()).hexdigest()
    x = np.linspace(0, 1, 1001)
    native = {}
    try:
        analysis.normalize_pdf(x, np.ones_like(x))
        native['status'] = 'ran'
    except Exception as exc:
        native = {'status': 'failed', 'type': type(exc).__name__, 'message': str(exc)}
    # Ephemeral API adaptation; not an unmodified environment reproduction.
    analysis._trapz = lambda values, coord, *, axis=-1: np.trapezoid(values, coord, axis=axis)
    flat = analysis.compute_hdi(x, np.ones_like(x), hdi_mass=.68)
    xmix = np.linspace(-5, 5, 5001)
    pdf = (np.exp(-.5*((xmix-2)/.3)**2) + np.exp(-.5*((xmix+2)/.3)**2)) / 2
    mix = analysis.compute_hdi(xmix, pdf, hdi_mass=.68)
    mix_mass = sum(i['mass'] for i in mix['intervals'])
    mix_relative = sum(i['mass_fraction'] for i in mix['intervals'])
    flat_mass = sum(i['mass'] for i in flat['intervals'])
    matrices = [np.array([[1.,1.],[-1.,1.]]), np.array([[1.,1.],[1.,1.]])]
    signs = [{'matrix':m.tolist(), 'intensities':(m*m).tolist(),
              'determinant':float(np.linalg.det(m)), 'singular_values':np.linalg.svd(m,compute_uv=False).tolist(),
              'loop_product':float(m[0,0]*m[1,1]*m[0,1]*m[1,0])} for m in matrices]
    after = hashlib.sha256(source.read_bytes()).hexdigest()
    checks = {
        'raw_analysis_hash_preserved': before == after,
        'native_current_stack_failure_observed': native.get('type') == 'AttributeError',
        'flat_requested_68pct_actual_unit_mass_limitation_observed': abs(flat_mass-1)<1e-12 and flat['mass']==.68,
        'smooth_bimodal_hdi_has_two_components': len(mix['intervals'])==2,
        'smooth_bimodal_actual_hdi_mass_is_68pct': abs(mix_mass-.68)<1e-8,
        'mass_fraction_sums_to_one': abs(mix_relative-1)<1e-12,
        'same_intensity_signed_matrix_pair': np.array_equal(matrices[0]**2,matrices[1]**2),
        'distinct_loop_signs': signs[0]['loop_product']==-1 and signs[1]['loop_product']==1,
        'first_singular_values_degenerate': abs(signs[0]['singular_values'][0]-signs[0]['singular_values'][1])<1e-12,
        'second_singular_values_split': abs(signs[1]['singular_values'][0]-2)<1e-12 and abs(signs[1]['singular_values'][1])<1e-12,
    }
    result = {'scope':'synthetic diagnostics and declared in-memory compatibility adaptation; no nuclear data fit',
              'numpy':np.__version__, 'raw_analysis_sha256':before, 'native_analysis':native,
              'adaptation':'YAnalysis._trapz bound in memory to numpy.trapezoid; raw source unchanged',
              'flat_hdi':flat, 'flat_actual_mass':flat_mass, 'smooth_bimodal_hdi':mix,
              'smooth_actual_mass':mix_mass, 'smooth_mass_fraction_sum':mix_relative,
              'signed_matrix_example':signs, 'checks':checks,'passed':all(checks.values())}
    assert result['passed']
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__ == '__main__':
    main()
