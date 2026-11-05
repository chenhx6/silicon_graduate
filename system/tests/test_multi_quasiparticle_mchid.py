#!/usr/bin/env python3
"""
Unit tests for Multi-Quasiparticle Multiple Chiral Doublets (MchiD)
& 4-QP Angular Momentum Geometry Analyzer (Module 116).
"""

import sys
from pathlib import Path
import unittest
import numpy as np

MODULES_DIR = Path(__file__).resolve().parent.parent / "scripts" / "analysis"
sys.path.insert(0, str(MODULES_DIR))

from multi_quasiparticle_mchid_chirality_calculator import (
    evaluate_chiral_geometry,
    evaluate_doublet_observables,
    analyze_mchid,
    PRESETS
)


class TestMultiQuasiparticleMchiD(unittest.TestCase):

    def test_chiral_geometry(self):
        geom = evaluate_chiral_geometry(j_pi=8.0, j_nu=8.0, total_spin=18.0)
        self.assertEqual(geom["j_pi_short"], 8.0)
        self.assertEqual(geom["j_nu_long"], 8.0)
        self.assertGreater(geom["R_m_intermediate"], 0.0)
        self.assertGreater(geom["scalar_triple_product_chi"], 0.0)
        self.assertGreater(geom["aplanarity_volume_metric"], 0.50)

    def test_doublet_observables(self):
        spins = [15, 16, 17, 18, 19, 20]
        E1 = [5180.0, 5680.0, 6220.0, 6800.0, 7420.0, 8080.0]
        E2 = [5260.0, 5740.0, 6270.0, 6840.0, 7450.0, 8105.0]
        obs = evaluate_doublet_observables(spins, E1, E2, j_pi=8.0, j_nu=8.0)
        self.assertLess(obs["mean_delta_E_keV"], 60.0)
        self.assertLess(obs["mean_delta_S_keV"], 1.0)
        self.assertGreater(obs["chiral_confidence_percent"], 80.0)

    def test_136nd_mchid_confirmation(self):
        p = PRESETS["136Nd_4qp_mchid"]
        res = analyze_mchid(p["doublets"], nucleus_name=p["nucleus"])
        self.assertEqual(res["num_doublets"], 2)
        self.assertTrue(res["screening_pass"])
        self.assertIsNone(res["is_mchid_verified"])
        self.assertIn("MchiD conditional screening pass", res["mchid_summary"])

    def test_103rh_single_doublet(self):
        p = PRESETS["103Rh_mchid"]
        res = analyze_mchid(p["doublets"], nucleus_name=p["nucleus"])
        self.assertEqual(res["num_doublets"], 1)
        self.assertFalse(res["screening_pass"])
        self.assertIsNone(res["is_mchid_verified"])
        self.assertIn("Single chiral doublet", res["mchid_summary"])


if __name__ == "__main__":
    unittest.main()
