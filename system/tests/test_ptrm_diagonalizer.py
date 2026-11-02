#!/usr/bin/env python3
"""
Unit tests for Full Microscopic Particle-Triaxial-Rotor Model (PTRM) Diagonalizer (Module 125).
"""

import sys
from pathlib import Path
import unittest
import numpy as np

MODULES_DIR = Path(__file__).resolve().parent.parent / "scripts" / "analysis"
sys.path.insert(0, str(MODULES_DIR))

from particle_triaxial_rotor_model_ptrm_diagonalizer import (
    evaluate_ptrm_matrix_elements,
    diagonalize_ptrm_spectrum,
    run_ptrm_analysis,
    PRESETS
)


class TestPTRMDiagonalizer(unittest.TestCase):

    def test_matrix_construction(self):
        H, basis = evaluate_ptrm_matrix_elements(I_spin=7.5, j_val=5.5, J_s=15.0, J_m=26.0, J_l=6.0,
                                                 C_quad=35.0, gamma_deg=26.0)
        self.assertGreater(H.shape[0], 0)
        self.assertEqual(H.shape[0], H.shape[1])
        # Real symmetric check
        self.assertTrue(np.allclose(H, H.T))

    def test_wobbling_frequency_positive(self):
        traj = diagonalize_ptrm_spectrum(spins=[7.5, 8.5, 9.5], j_val=5.5, J_s=15.0, J_m=26.0, J_l=6.0,
                                         C_quad=35.0, gamma_deg=26.0)
        self.assertEqual(len(traj), 3)
        for pt in traj:
            self.assertGreater(pt["wobbling_energy_keV"], 0.0)
            self.assertGreaterEqual(pt["E_wob1_keV"], pt["E_yrast_keV"])

    def test_run_ptrm_preset_135pr(self):
        p = PRESETS["135Pr_triaxial_wobbler_ptrm"]
        res = run_ptrm_analysis(
            A_mass=p["A_mass"],
            spins=p["spins"],
            j_val=p["j_valence"],
            J_s=p["J_s_hbar2_MeV"],
            J_m=p["J_m_hbar2_MeV"],
            J_l=p["J_l_hbar2_MeV"],
            C_quad=p["C_quadrupole_keV"],
            gamma_deg=p["gamma_deg"]
        )
        self.assertEqual(len(res["levels"]), len(p["spins"]))
        # Ground state excitation energy normalized to 0
        self.assertAlmostEqual(res["levels"][0]["E_ex_yrast_keV"], 0.0)

    def test_run_ptrm_preset_163lu(self):
        p = PRESETS["163Lu_tsw_wobbler_ptrm"]
        res = run_ptrm_analysis(
            A_mass=p["A_mass"],
            spins=[8.5, 9.5],
            j_val=p["j_valence"],
            J_s=p["J_s_hbar2_MeV"],
            J_m=p["J_m_hbar2_MeV"],
            J_l=p["J_l_hbar2_MeV"],
            C_quad=p["C_quadrupole_keV"],
            gamma_deg=p["gamma_deg"]
        )
        self.assertEqual(len(res["levels"]), 2)
        self.assertGreater(res["levels"][0]["wobbling_energy_keV"], 0.0)


if __name__ == "__main__":
    unittest.main()
