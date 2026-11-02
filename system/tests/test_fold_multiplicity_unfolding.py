#!/usr/bin/env python3
"""
Unit tests for in_beam_array_fold_multiplicity_entry_state_unfolder.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from in_beam_array_fold_multiplicity_entry_state_unfolder import (
    PRESETS,
    calculate_binomial_response_matrix,
    unfold_multiplicity_distribution,
    map_to_entry_spin_and_energy,
    run_fold_unfolding_analysis
)


class TestFoldMultiplicityUnfolding(unittest.TestCase):

    def test_binomial_response_normalization(self):
        N_det = 16
        eps = 0.80
        resp = calculate_binomial_response_matrix(N_det, eps, max_fold=16, max_mult=25)
        self.assertEqual(resp.shape, (17, 26))
        # For each multiplicity M > 0, sum over folds should equal 1.0 (normalized)
        col_sums = resp.sum(axis=0)
        for M in range(1, 26):
            self.assertAlmostEqual(col_sums[M], 1.0, places=4)

    def test_4pi_bgo_unfolding(self):
        p = PRESETS["4pi_bgo_ball_fusion_evaporation"]
        res = run_fold_unfolding_analysis(
            fold_hist=p["measured_fold_histogram"],
            N_det=p["N_det"],
            eps_det=p["eps_det"],
            eps_sum=p["eps_sum"],
            mean_H_MeV=p["mean_sum_energy_MeV"],
            N_stat=p["N_stat"],
            J_bandhead=p["J_bandhead"]
        )
        ent = res["entry_state"]
        self.assertGreater(ent["mean_multiplicity_M"], 20.0)
        self.assertLess(ent["mean_multiplicity_M"], 30.0)
        self.assertGreater(ent["mean_entry_spin_hbar"], 35.0)
        self.assertGreater(ent["mean_entry_excitation_energy_MeV"], 25.0)

    def test_low_multiplicity_transfer(self):
        p = PRESETS["low_multiplicity_transfer_reaction"]
        res = run_fold_unfolding_analysis(
            fold_hist=p["measured_fold_histogram"],
            N_det=p["N_det"],
            eps_det=p["eps_det"],
            eps_sum=p["eps_sum"],
            mean_H_MeV=p["mean_sum_energy_MeV"],
            N_stat=p["N_stat"],
            J_bandhead=p["J_bandhead"]
        )
        ent = res["entry_state"]
        self.assertLess(ent["mean_multiplicity_M"], 10.0)
        self.assertLess(ent["mean_entry_spin_hbar"], 15.0)

    def test_mapping_spin_consistency(self):
        info = map_to_entry_spin_and_energy(mean_M=20.0, sigma_M=3.0, mean_H_MeV=20.0, N_stat=4.0, delta_I_stat=0.5)
        # Rotational count = 20 - 4 = 16. Spin = 2*16 + 4*0.5 = 32 + 2 = 34.
        self.assertAlmostEqual(info["mean_entry_spin_hbar"], 34.0, places=2)
        self.assertAlmostEqual(info["sigma_entry_spin_hbar"], 6.0, places=2)


if __name__ == "__main__":
    unittest.main()
