"""
Unit tests for Triaxial Rotor Wobbling, Lawrie TiP Classifier & Chiral Doublets.

Benchmarked against:
  - C. M. Petrache (Ed.), Chirality and Wobbling in Atomic Nuclei, CRC Press (2025):
      * S. Frauendorf, Ch. 2 (pp. 43-80, Eqs. 2.2, 2.20, 2.21)
      * J. Meng & Y. P. Wang, Ch. 3 (pp. 81-93)
      * E. A. Lawrie, Ch. 6 (pp. 127-155, Table 6.1, Fig. 6.10)
      * E. Grodner, Ch. 7 (pp. 156-166)
"""

import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from triaxial_wobbling_tip_chiral_analyzer import (
    calculate_triaxial_rotor_moi_parameters,
    calculate_transverse_wobbling_spectrum,
    classify_tip_vs_phonon_wobbling,
    analyze_chiral_doublet_staggering
)


class TriaxialWobblingTiPChiralTests(unittest.TestCase):

    def test_triaxial_moi_asymmetry_ordering_and_kappa(self):
        """Verify MOI ordering J_m >= J_s >= J_l, rotational parameters A_i, and Ray's kappa."""
        # 163Lu parameters from Frauendorf (2025) Ch. 2
        moi = calculate_triaxial_rotor_moi_parameters(J_m=64.0, J_s=56.0, J_l=13.0)
        self.assertAlmostEqual(moi["A_m_keV"], 7.812, places=2)
        self.assertAlmostEqual(moi["A_s_keV"], 8.929, places=2)
        self.assertAlmostEqual(moi["A_l_keV"], 38.462, places=2)
        self.assertAlmostEqual(moi["asymmetry_parameter_kappa"], 0.9272, places=3)

        # Ordering violation check
        with self.assertRaises(ValueError):
            calculate_triaxial_rotor_moi_parameters(J_m=20.0, J_s=30.0, J_l=10.0) # J_s > J_m
        with self.assertRaises(ValueError):
            calculate_triaxial_rotor_moi_parameters(J_m=20.0, J_s=15.0, J_l=-5.0) # negative MOI

    def test_transverse_wobbling_lu163_and_pr135(self):
        """Verify TW frequencies, critical softening spin Ic, and slope classification."""
        # 1. 163Lu: j = 13/2 (6.5), Ic = 6.5 * 64 / (64 - 56) = 52.0
        tw_lu = calculate_transverse_wobbling_spectrum(
            J_m=64.0, J_s=56.0, J_l=13.0, j_single=6.5,
            spins=[9.5, 11.5, 13.5, 15.5, 17.5, 19.5, 21.5, 25.5, 30.5, 35.5]
        )
        self.assertAlmostEqual(tw_lu["critical_spin_Ic"], 52.0, places=2)
        self.assertAlmostEqual(tw_lu["spectrum"][0]["hbar_omega_TW_keV"], 253.5, places=1)
        self.assertAlmostEqual(tw_lu["spectrum"][7]["hbar_omega_TW_keV"], 309.8, places=1) # Peak near I=25.5

        # 2. 135Pr: j = 11/2 (5.5), Ic = 5.5 * 21 / (21 - 13) = 14.438
        tw_pr = calculate_transverse_wobbling_spectrum(
            J_m=21.0, J_s=13.0, J_l=4.0, j_single=5.5,
            spins=[6.5, 8.5, 10.5, 12.5, 14.5]
        )
        self.assertAlmostEqual(tw_pr["critical_spin_Ic"], 14.438, places=2)
        self.assertAlmostEqual(tw_pr["spectrum"][0]["hbar_omega_TW_keV"], 600.07, places=1)
        self.assertAlmostEqual(tw_pr["spectrum"][3]["hbar_omega_TW_keV"], 383.22, places=1)
        self.assertIsNone(tw_pr["spectrum"][4]["hbar_omega_TW_keV"]) # I = 14.5 > Ic
        self.assertEqual(tw_pr["spectrum"][4]["status"], "above_critical_spin_instability")
        self.assertLess(tw_pr["wobbling_slope_keV_per_hbar"], 0.0)
        self.assertIn("Transverse Wobbling", tw_pr["mode_identification"])

    def test_lawrie_tip_vs_phonon_wobbling_diagnostics(self):
        """Verify Elena Lawrie's Ch. 6 Table 6.1 criteria: sum rule, Delta_k=2 transition, and scaling."""
        # 192Os benchmark: Delta_sum = 205.8 + 489.1 - 690.5 = 4.4 keV ~ 0 (TiP rotational!)
        tip = classify_tip_vs_phonon_wobbling(
            n_or_m_indices=[1, 2],
            energies_keV=[867.0, 1980.0],
            E_2g_keV=205.8,
            E_2gamma_keV=489.1,
            E_3gamma_keV=690.5,
            B_E2_delta2_Wu=15.0
        )
        self.assertAlmostEqual(tip["sum_rule_test"]["delta_sum_keV"], 4.4, places=1)
        self.assertIn("Rotational TiP", tip["sum_rule_test"]["diagnosis"])
        self.assertIn("Rotational TiP", tip["selection_rule_test"]["diagnosis"])

    def test_chiral_doublet_staggering_and_aplanarity(self):
        """Verify chiral doublet energy splitting Delta_E(I), S(I), and odd-even M1/E2 staggering."""
        spins = [9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0]
        e_b1 = [0.0, 235.0, 520.0, 856.0, 1245.0, 1680.0, 2160.0]
        e_b2 = [280.0, 450.0, 680.0, 960.0, 1310.0, 1720.0, 2190.0]
        bm1_be2 = [0.45, 0.85, 0.38, 0.92, 0.40, 0.88, 0.42]

        chiral = analyze_chiral_doublet_staggering(spins, e_b1, e_b2, bm1_be2, j_p=5.5, j_n=5.5)
        # Energy splitting drops from 280 keV down to 30 keV
        self.assertEqual(chiral["band_levels"][0]["energy_splitting_DeltaE_keV"], 280.0)
        self.assertEqual(chiral["band_levels"][-1]["energy_splitting_DeltaE_keV"], 30.0)
        self.assertGreater(chiral["band_levels"][-1]["chiral_aplanarity_volume"], chiral["band_levels"][0]["chiral_aplanarity_volume"])
        self.assertIsNotNone(chiral["m1_e2_staggering_profile"])

    def test_json_strict_serialization(self):
        """Verify strict RFC JSON serialization without NaN or Inf."""
        moi = calculate_triaxial_rotor_moi_parameters(J_m=21.0, J_s=13.0, J_l=4.0)
        tw = calculate_transverse_wobbling_spectrum(21.0, 13.0, 4.0, 5.5, [6.5, 8.5, 14.5])
        payload = {"moi": moi, "tw": tw}
        s = json.dumps(payload, allow_nan=False)
        self.assertIn("critical_spin_Ic", s)


if __name__ == "__main__":
    unittest.main()
