#!/usr/bin/env python3
"""
Unit tests for coriolis_anti_pairing_gap_quenching_moi_engine.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from coriolis_anti_pairing_gap_quenching_moi_engine import (
    PRESETS,
    calculate_cap_pairing_gap,
    calculate_cap_moments_of_inertia,
    solve_spin_state_cap,
    run_cap_analysis,
    format_text_report
)


sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from day27_sd_vs_nd_pairing_cap_study import (
    solve_cranked_pairing_bcs, simulate_rotational_band_inertia,
)


class TestCoriolisAntiPairing(unittest.TestCase):

    def test_cap_gap_quenching_function(self):
        gap_zero = calculate_cap_pairing_gap(0.0, 1.0, 0.5)
        self.assertEqual(gap_zero["delta_MeV"], 1.0)
        self.assertEqual(gap_zero["quenching_fraction"], 0.0)
        self.assertTrue(gap_zero["is_superfluid"])

        gap_half = calculate_cap_pairing_gap(0.25, 1.0, 0.5)
        self.assertAlmostEqual(gap_half["delta_MeV"], 0.866, places=3)

        gap_crit = calculate_cap_pairing_gap(0.50, 1.0, 0.5)
        self.assertEqual(gap_crit["delta_MeV"], 0.0)
        self.assertFalse(gap_crit["is_superfluid"])

    def test_legacy_163Lu_label_sampled_indicator(self):
        p = PRESETS["163Lu_TSD_superfluid_to_normal_phase_transition"]
        res = run_cap_analysis(
            nucleus=p["nucleus"],
            delta_0_MeV=p["delta_0_MeV"],
            omega_crit_MeV=p["omega_crit_MeV"],
            J_rig_dict=p["J_rigid_hbar2_per_MeV"],
            irr_ratio=p["J_irrotational_ratio"],
            spins=p["spins_to_evaluate"]
        )
        self.assertIsNotNone(res["critical_transition_spin_I_CAP"])
        self.assertGreaterEqual(res["critical_transition_spin_I_CAP"], 30.0)
        self.assertLessEqual(res["critical_transition_spin_I_CAP"], 40.0)
        # Chosen synthetic curve reaches its prescribed rigid limit
        top_spin = res["spin_evolution"][-1]
        self.assertEqual(top_spin["pairing_gap_MeV"], 0.0)
        self.assertAlmostEqual(top_spin["moments_of_inertia"]["J_m"], 72.0, places=2)

    def test_rigid_limit_preset(self):
        p = PRESETS["rigid_rotor_zero_pairing_limit"]
        res = run_cap_analysis(
            nucleus=p["nucleus"],
            delta_0_MeV=p["delta_0_MeV"],
            omega_crit_MeV=p["omega_crit_MeV"],
            J_rig_dict=p["J_rigid_hbar2_per_MeV"],
            irr_ratio=p["J_irrotational_ratio"],
            spins=p["spins_to_evaluate"]
        )
        for pt in res["spin_evolution"]:
            self.assertEqual(pt["pairing_gap_MeV"], 0.0)
            self.assertFalse(pt["is_superfluid"])

    def test_gap_domain_and_even_limit(self):
        for args in [(0, -1, .5), (0, 1, 0), (0, 1, -.5),
                     (float("nan"), 1, .5), (0, float("inf"), .5),
                     (0, 1, float("nan"))]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                calculate_cap_pairing_gap(*args)
        self.assertEqual(calculate_cap_pairing_gap(-.25, 1, .5),
                         calculate_cap_pairing_gap(.25, 1, .5))
        self.assertEqual(calculate_cap_pairing_gap(1, 0, .5)["delta_MeV"], 0)

    def test_inertia_domain(self):
        j = {"J_s": 30, "J_m": 50, "J_l": 15}
        for delta, d0, inertia, ratio in [
            (1.1, 1, j, .4), (-.1, 1, j, .4), (0, -1, j, .4),
            (0, 1, j, 0), (0, 1, j, 1.1), (0, 1, j, float("nan")),
            (0, 1, {**j, "J_s": 0}, .4),
            (0, 1, {**j, "J_l": float("inf")}, .4),
            (0, 1, {"J_m": 50}, .4), (float("nan"), 1, j, .4)
        ]:
            with self.subTest(delta=delta, ratio=ratio), self.assertRaises(ValueError):
                calculate_cap_moments_of_inertia(delta, d0, inertia, ratio)

    def test_uniform_scaling_preserves_axis_ratios_and_rotor_factor(self):
        j = {"J_s": 30, "J_m": 50, "J_l": 15}
        factors = []
        for delta in [1, .5, 0]:
            moi = calculate_cap_moments_of_inertia(delta, 1, j, .4)
            self.assertAlmostEqual(moi["J_m"] / moi["J_s"], 5 / 3)
            self.assertAlmostEqual(moi["J_m"] / moi["J_l"], 10 / 3)
            factors.append(((moi["J_m"] / moi["J_s"] - 1) *
                            (moi["J_m"] / moi["J_l"] - 1)) ** .5)
        self.assertAlmostEqual(factors[0], factors[-1])
        self.assertEqual(calculate_cap_moments_of_inertia(0, 0, j, .4), j)
        self.assertEqual(calculate_cap_moments_of_inertia(1, 1, j, 1), j)
        # A valid small base fraction must not cancel to zero at x=0.
        tiny = calculate_cap_moments_of_inertia(1, 1, j, 1e-18)
        self.assertGreater(tiny["J_m"], 0)
        self.assertAlmostEqual(tiny["J_m"] / 1e-18, 50)

    def test_root_bracket_rigid_limits_and_residual(self):
        j = {"J_s": 30, "J_m": 50, "J_l": 15}
        for spin in [0, 1e-6, 3, 24.9, 25, 1000]:
            pt = solve_spin_state_cap(spin, 1, .5, j, .4)
            actual = pt["moments_of_inertia"]["J_m"] * pt["rotational_frequency_MeV"]
            self.assertAlmostEqual(actual, spin, delta=max(1e-14, spin * 1e-9))
        for d0, ratio in [(0, .4), (1, 1)]:
            pt = solve_spin_state_cap(1000, d0, .5, j, ratio)
            self.assertAlmostEqual(pt["rotational_frequency_MeV"], 20, places=8)
        for spin in [-1, float("inf"), float("nan")]:
            with self.assertRaises(ValueError):
                solve_spin_state_cap(spin, 1, .5, j, .4)

    def test_sampled_threshold_is_not_exact_zero_gap_spin(self):
        j = {"J_s": 30, "J_m": 50, "J_l": 15}
        # With r=1, x=i/50 exactly. Delta/Delta0=.04 at this x.
        below = 25 * (1 - .04**2) ** .5
        res = run_cap_analysis("synthetic", 1, .5, j, 1, [30, below, 1])
        self.assertEqual(res["critical_transition_spin_I_CAP"], below)
        self.assertEqual(res["spin_evolution"][0]["spin_I"], 30)
        self.assertIsNone(run_cap_analysis("x", 0, .5, j, .4, [30])["critical_transition_spin_I_CAP"])
        self.assertIsNone(run_cap_analysis("x", 1, .5, j, .4, [])["critical_transition_spin_I_CAP"])
        text = format_text_report(res)
        self.assertIn("hbar*omega_scale", text)
        self.assertIn("Sampled", text)
        self.assertNotIn("Phase Transition", text)

    def test_day27_gap_floor_unused_G_and_prescribed_crossing(self):
        gap, aligned = solve_cranked_pairing_bcs(.3, 1, .1, 6, .3, .04)
        self.assertAlmostEqual(gap, (1 - (.3 / .65)**2)**.5)
        self.assertEqual(aligned, 6)
        self.assertEqual((gap, aligned), solve_cranked_pairing_bcs(.3, 1, .9, 6, .3, .04))
        self.assertAlmostEqual(solve_cranked_pairing_bcs(2, 1, .1, 6, .3)[0], .2)
        # Crossing slope j^2/V is independent of the imposed gap.
        h = 1e-7
        left = solve_cranked_pairing_bcs(.3-h, 0, .1, 6, .3, .04)[1]
        right = solve_cranked_pairing_bcs(.3+h, 0, .1, 6, .3, .04)[1]
        self.assertAlmostEqual((right-left)/(2*h), 36/.04, places=4)

    def test_day27_domains(self):
        valid = [.3, 1, .15, 6, .3, .04]
        for index in range(len(valid)):
            for bad in [float("nan"), float("inf"), -1]:
                args = valid.copy()
                args[index] = bad
                with self.subTest(index=index, bad=bad), self.assertRaises(ValueError):
                    solve_cranked_pairing_bcs(*args)
        for index in [3, 5]:
            args = valid.copy()
            args[index] = 0
            with self.assertRaises(ValueError):
                solve_cranked_pairing_bcs(*args)
        for grid in [[], [.1, .2], [.1, .1, .2], [.3, .2, .1],
                     [-.1, 0, .1], [0, .1, float("nan")]]:
            with self.subTest(grid=grid), self.assertRaises(ValueError):
                simulate_rotational_band_inertia("x", 160, .28, 1, 6, .3, .04, grid)

    def test_day27_zero_gap_still_has_nonconstant_alignment_response(self):
        grid = [.2999, .3, .3001]
        res = simulate_rotational_band_inertia("synthetic", 160, .28, 0, 6, .3, .04, grid)
        center = res["states"][1]
        rigid = .014 * 160**(5/3) * (1+.32*.28)
        self.assertAlmostEqual(center["J2_dynamic_MoI_hbar2_per_MeV"], rigid+36/.04, delta=.15)
        self.assertGreater(center["J2_dynamic_MoI_hbar2_per_MeV"], res["J_rigid_hbar2_per_MeV"])
        self.assertIsNone(res["states"][0]["J2_dynamic_MoI_hbar2_per_MeV"])


if __name__ == "__main__":
    unittest.main()
