#!/usr/bin/env python3
"""
Unit tests for in_beam_2d_snip_matrix_background_estimator.py
"""

import sys
import unittest
import numpy as np
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from in_beam_2d_snip_matrix_background_estimator import (
    PRESETS,
    generate_synthetic_2d_matrix,
    execute_2d_snip_algorithm,
    run_2d_snip_analysis
)


class Test2DSNIPBackground(unittest.TestCase):

    def test_2d_snip_matrix_generation(self):
        p = PRESETS["isolated_gaussian_peaks_fidelity_test"]
        E_ax, M_raw, M_bkg, M_peaks, vol = generate_synthetic_2d_matrix(
            p["matrix_dim"], p["energy_min_keV"], p["energy_max_keV"],
            p["peaks"], p["compton_continuum_base"]
        )
        self.assertEqual(M_raw.shape, (p["matrix_dim"], p["matrix_dim"]))
        self.assertGreater(vol, 1000.0)
        self.assertTrue(np.all(M_raw >= 0))

    def test_background_suppression(self):
        p = PRESETS["130Ba_gated_matrix_slice_snip"]
        res = run_2d_snip_analysis(
            matrix_dim=p["matrix_dim"],
            E_min=p["energy_min_keV"],
            E_max=p["energy_max_keV"],
            peaks=p["peaks"],
            bkg_base=p["compton_continuum_base"],
            p_max=p["clipping_window_pmax"]
        )
        st = res["statistics"]
        # Background fraction should be > 60%
        self.assertGreater(st["background_fraction_pct"], 60.0)
        # Net coincidence yield should be positive
        self.assertGreater(st["net_coincidence_counts"], 0.0)
        # Signal-to-background enhancement factor should be > 2.0
        self.assertGreater(st["signal_to_bkg_enhancement_factor"], 2.0)

    def test_peak_preservation(self):
        p = PRESETS["isolated_gaussian_peaks_fidelity_test"]
        res = run_2d_snip_analysis(
            matrix_dim=p["matrix_dim"],
            E_min=p["energy_min_keV"],
            E_max=p["energy_max_keV"],
            peaks=p["peaks"],
            bkg_base=p["compton_continuum_base"],
            p_max=p["clipping_window_pmax"]
        )
        st = res["statistics"]
        # Peak area preservation fidelity should be > 90%
        self.assertGreater(st["peak_area_fidelity_pct"], 90.0)


if __name__ == "__main__":
    unittest.main()
