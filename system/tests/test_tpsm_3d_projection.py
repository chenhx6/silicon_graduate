#!/usr/bin/env python3
"""
Unit tests for tpsm_3d_angular_momentum_projection_diagonalizer.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from tpsm_3d_angular_momentum_projection_diagonalizer import (
    PRESETS,
    calculate_effective_moi_tpsm,
    build_tpsm_matrices,
    diagonalize_spin_tpsm,
    run_tpsm_analysis
)


class TestTPSM3DProjection(unittest.TestCase):

    def test_effective_moi_calculation(self):
        moi = calculate_effective_moi_tpsm(0.23, 25.0, 130)
        self.assertGreater(moi, 20.0)
        self.assertLess(moi, 35.0)

    def test_axial_symmetric_limit(self):
        p = PRESETS["axial_symmetric_limit"]
        res = run_tpsm_analysis(
            A=p["A"],
            epsilon2=p["epsilon2"],
            gamma_deg=p["gamma_deg"],
            core_coupling_keV=p["core_coupling_keV"],
            spins=p["spins"],
            nucleus=p["nucleus"]
        )
        bands = res["diagonalized_bands"]
        # At gamma = 0, K=0 weight in yrast state must be exactly 100%
        for pt in bands:
            self.assertAlmostEqual(pt["k_composition"]["K=0"], 1.0, places=4)
            self.assertAlmostEqual(pt["k_composition"]["K=2"], 0.0, places=4)

    def test_130Ba_triaxial_bands_and_k_mixing(self):
        p = PRESETS["130Ba_TPSM_triaxial_bands"]
        res = run_tpsm_analysis(
            A=p["A"],
            epsilon2=p["epsilon2"],
            gamma_deg=p["gamma_deg"],
            core_coupling_keV=p["core_coupling_keV"],
            spins=p["spins"],
            nucleus=p["nucleus"]
        )
        bands = res["diagonalized_bands"]
        # Yrast energies must increase monotonically with spin
        for i in range(len(bands) - 1):
            self.assertLess(bands[i]["E_yrast_keV"], bands[i+1]["E_yrast_keV"])
            self.assertLess(bands[i]["E_gamma_band_keV"], bands[i+1]["E_gamma_band_keV"])
        # Triaxiality induces K=2 admixture in yrast states (> 0)
        high_spin = bands[-1]
        self.assertGreater(high_spin["k_composition"]["K=2"], 0.01)

    def test_163Lu_tsd_wobbling_energies(self):
        p = PRESETS["163Lu_TSD_TPSM_wobbling"]
        res = run_tpsm_analysis(
            A=p["A"],
            epsilon2=p["epsilon2"],
            gamma_deg=p["gamma_deg"],
            core_coupling_keV=p["core_coupling_keV"],
            spins=p["spins"],
            nucleus=p["nucleus"]
        )
        bands = res["diagonalized_bands"]
        # Wobbling band spacing should be between 1000 and 3000 keV
        self.assertGreater(bands[0]["delta_E_wob_yrast_keV"], 500.0)


if __name__ == "__main__":
    unittest.main()
