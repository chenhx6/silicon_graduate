#!/usr/bin/env python3
"""Deterministic descriptor checks; synthetic fixtures are not isotope data."""

from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))
from multiple_chiral_doublets_mchid_discriminator import (
    PRESETS,
    MultipleChiralDoubletsDiscriminator,
    format_text_report,
    run_mchid_arbitration,
)


def pair(spins=(10, 11, 12), energies=(1000, 1200, 1600), splitting=300):
    return {
        "data_kind": "synthetic",
        "spins": list(spins),
        "energies_B1_keV": list(energies),
        "energies_B2_keV": [e + splitting for e in energies],
    }


class TestMultipleChiralDoubletsMChD(unittest.TestCase):
    def setUp(self):
        self.descriptor = MultipleChiralDoubletsDiscriminator(0, 0)

    def test_same_configuration_and_zero_separation_do_not_reject(self):
        # Kuti pp. 3-5 motivates the counterexample, not these synthetic numbers.
        p = pair(splitting=300)
        p["configuration"] = "synthetic common configuration"
        result = self.descriptor.arbitrate_mchid(p, deepcopy(p))
        self.assertIsNone(result["is_mchid_confirmed"])
        self.assertEqual(result["alignment_separation_Delta_ix_hbar"], 0)
        self.assertNotIn("REJECTED", result["diagnostic_verdict"])
        self.assertNotIn("CONFIRMED", result["diagnostic_verdict"])
        self.assertNotIn("gates_evaluation", result)

    def test_large_gap_and_intensity_ratio_do_not_classify(self):
        result = self.descriptor.arbitrate_mchid(
            pair(splitting=400), pair(splitting=900), cross_branching_ratio=2.5,
            delta_ix_crit=1000)
        self.assertEqual(result["pair_A_analysis"]["energy_splittings_keV"], [400] * 3)
        self.assertEqual(result["cross_doublet_branching_ratio"], 2.5)
        self.assertEqual(result["legacy_delta_ix_crit_ignored"], 1000)
        self.assertIsNone(result["is_mchid_confirmed"])

    def test_secants_and_midpoint_alignment_have_independent_expected_values(self):
        frequency, alignment = MultipleChiralDoubletsDiscriminator(2, 3).calculate_alignment(
            [10, 11, 12], [1000, 1200, 1600])
        np.testing.assert_allclose(frequency, [0.2, 0.4])
        np.testing.assert_allclose(alignment, [11 - 2 * .2 - 3 * .2**3,
                                               12 - 2 * .4 - 3 * .4**3])

    def test_partial_overlap_compares_equal_frequencies_not_spin_means(self):
        a = pair((10, 11, 12, 13), (1000, 1200, 1600, 2200))
        b = pair((11, 12, 13, 14), (2000, 2400, 3000, 3800))
        r = self.descriptor.arbitrate_mchid(a, b)["alignment_comparison"]
        np.testing.assert_allclose(r["common_frequency_support_MeV"], [.4, .6])
        np.testing.assert_allclose(r["absolute_difference_hbar"], 0)
        self.assertEqual(r["mean_absolute_separation_hbar"], 0)

    def test_support_is_intersection_of_all_four_bands(self):
        a = pair((10, 11, 12, 13), (1000, 1200, 1600, 2200))
        a["energies_B2_keV"] = [1300, 1600, 2100, 2800]  # .3, .5, .7
        b = pair((11, 12, 13, 14), (2000, 2400, 3000, 3800))
        b["energies_B2_keV"] = [2300, 2800, 3500, 4400]  # .5, .7, .9
        r = self.descriptor.arbitrate_mchid(a, b)["alignment_comparison"]
        np.testing.assert_allclose(r["common_frequency_support_MeV"], [.5, .6])
        self.assertTrue(all(.5 <= x <= .6 for x in r["frequency_MeV"]))

    def test_disjoint_frequency_support_is_unknown_no_extrapolation(self):
        p = PRESETS["synthetic_no_overlap"]
        r = self.descriptor.arbitrate_mchid(p["pair_A"], p["pair_B"])
        self.assertEqual(r["alignment_comparison"]["status"], "no_common_frequency_support")
        self.assertIsNone(r["alignment_separation_Delta_ix_hbar"])
        self.assertEqual(r["alignment_comparison"]["frequency_MeV"], [])

    def test_single_shared_frequency_has_no_interval_average(self):
        a = pair()
        b = pair((11, 12, 13), (2000, 2400, 3000))
        r = self.descriptor.arbitrate_mchid(a, b)["alignment_comparison"]
        self.assertEqual(r["common_frequency_support_MeV"], [.4, .4])
        self.assertEqual(r["averaging"], "single_shared_frequency")
        self.assertEqual(r["mean_absolute_separation_hbar"], 0)

    def test_crossing_difference_is_integrated_with_zero_crossing(self):
        a = pair((10, 11, 12), (0, 200, 600))
        b = pair((9, 11, 13), (0, 400, 1200))
        r = self.descriptor.arbitrate_mchid(a, b)["alignment_comparison"]
        # Differences .5 and -.5 on [.2,.4]; triangle areas / width = .25.
        self.assertAlmostEqual(r["mean_absolute_separation_hbar"], .25)
        np.testing.assert_allclose(r["frequency_MeV"], [.2, .3, .4])
        np.testing.assert_allclose(r["absolute_difference_hbar"], [.5, 0, .5])

    def test_reference_cancels_on_unequal_frequency_grids(self):
        a = pair((10, 11, 12), (0, 200, 600))
        b = pair((9, 10, 11, 12), (0, 200, 500, 900))
        base = self.descriptor.arbitrate_mchid(a, b)["alignment_separation_Delta_ix_hbar"]
        shifted = MultipleChiralDoubletsDiscriminator(17, 25).arbitrate_mchid(a, b)
        self.assertAlmostEqual(base, shifted["alignment_separation_Delta_ix_hbar"])

    def test_single_level_does_not_get_fabricated_frequency(self):
        a = pair((10.5,), (1000,))
        r = self.descriptor.arbitrate_mchid(a, a)
        self.assertEqual(r["alignment_comparison"]["status"], "insufficient_alignment_points")
        self.assertIsNone(r["alignment_separation_Delta_ix_hbar"])
        self.assertEqual(r["pair_A_analysis"]["alignment_curves"][0]["frequency_MeV"], [])

    def test_backbend_or_duplicate_frequency_is_not_sorted_into_fake_function(self):
        for energies in [(0, 400, 600), (0, 200, 400)]:
            with self.subTest(energies=energies):
                a = pair(energies=energies)
                r = self.descriptor.arbitrate_mchid(a, a)
                self.assertEqual(r["alignment_comparison"]["status"], "nonmonotonic_frequency")
                self.assertIsNone(r["alignment_separation_Delta_ix_hbar"])
                self.assertEqual(len(r["pair_A_analysis"]["alignment_curves"][0]["frequency_MeV"]), 2)

    def test_missing_observables_stay_unknown(self):
        r = self.descriptor.arbitrate_mchid(pair(), pair())
        p = r["pair_A_analysis"]
        for key in ("configuration", "same_parity", "staggering_in_phase"):
            self.assertIsNone(p[key])
        self.assertEqual(p["bm1_be2_ratios"]["status"], "unknown")
        self.assertEqual(p["bm1_be2_ratios"]["band_1"], [None] * 3)
        self.assertEqual(p["absolute_transition_strengths"]["status"], "unknown")
        self.assertIsNone(r["cross_doublet_branching_ratio"])
        self.assertEqual(r["cross_branching_status"], "unknown")

    def test_caller_phase_annotation_does_not_create_measured_ratios(self):
        a = pair()
        a["bm1_be2_staggering_in_phase"] = True
        p = self.descriptor.evaluate_pair(a)
        self.assertTrue(p["staggering_in_phase"])
        self.assertEqual(p["staggering_status"], "caller_annotation_unverified")
        self.assertEqual(p["bm1_be2_ratios"]["status"], "unknown")

    def test_sparse_ratio_measurements_are_not_filled_or_converted_to_strengths(self):
        a = pair()
        a["bm1_be2_ratios_B1"] = [None, 2., 3.]
        a["bm1_be2_ratios_B2"] = [1., 2.5, None]
        p = self.descriptor.evaluate_pair(a)
        self.assertEqual(p["bm1_be2_ratios"]["common_spins_hbar"], [11])
        self.assertEqual(p["bm1_be2_ratios"]["absolute_difference"], [.5])
        self.assertEqual(p["absolute_transition_strengths"]["status"], "unknown")
        self.assertIsNone(p["staggering_in_phase"])

    def test_supplied_parities_are_described_without_physical_verdict(self):
        for parities, expected in [(["+", "+"], True), (["+", "-"], False),
                                   (["-", None], None)]:
            a = pair()
            a["parities"] = parities
            r = self.descriptor.arbitrate_mchid(a, a)
            self.assertIs(r["pair_A_analysis"]["same_parity"], expected)
            self.assertIsNone(r["is_mchid_confirmed"])

    def test_swapping_pairs_and_members_preserves_scalar_descriptors(self):
        p = PRESETS["synthetic_overlap"]
        a, b = deepcopy(p["pair_A"]), deepcopy(p["pair_B"])
        a["energies_B2_keV"] = [1300, 1650, 2100, 2650]
        b["energies_B4_keV"] = [1800, 2125, 2550, 3075]
        original = self.descriptor.arbitrate_mchid(a, b)
        swapped = self.descriptor.arbitrate_mchid(b, a)
        self.assertEqual(original["alignment_separation_Delta_ix_hbar"],
                         swapped["alignment_separation_Delta_ix_hbar"])
        for obj, keys in [(a, ("energies_B1_keV", "energies_B2_keV")),
                          (b, ("energies_B3_keV", "energies_B4_keV"))]:
            obj[keys[0]], obj[keys[1]] = obj[keys[1]], obj[keys[0]]
        flipped = self.descriptor.arbitrate_mchid(a, b)
        self.assertEqual(original["alignment_separation_Delta_ix_hbar"],
                         flipped["alignment_separation_Delta_ix_hbar"])
        self.assertEqual(original["pair_A_analysis"]["energy_splittings_keV"],
                         flipped["pair_A_analysis"]["energy_splittings_keV"])

    def test_every_preset_including_legacy_names_is_explicitly_synthetic(self):
        before = deepcopy(PRESETS)
        for name, p in PRESETS.items():
            with self.subTest(name=name):
                self.assertEqual(p["data_kind"], "synthetic")
                self.assertIn("Synthetic", p["nucleus"])
                for key in ("pair_A", "pair_B"):
                    self.assertEqual(p[key]["data_kind"], "synthetic")
                    self.assertNotIn("bm1_be2_staggering_in_phase", p[key])
                r = run_mchid_arbitration(p["nucleus"], p["harris_J0"], p["harris_J1"],
                                          p["pair_A"], p["pair_B"], None, 1.5)
                self.assertIsNone(r["is_mchid_confirmed"])
                self.assertEqual(r["data_kind"], "synthetic")
                json.dumps(r, allow_nan=False)
        self.assertEqual(PRESETS, before)

    def test_defaults_mixed_inputs_and_reports_distinguish_synthetic_data(self):
        r = run_mchid_arbitration(nucleus="133Ce")
        self.assertEqual(r["data_kind"], "synthetic")
        a = pair()
        del a["data_kind"]
        mixed = run_mchid_arbitration(pair_A=a)
        self.assertEqual(mixed["data_kind"], "mixed_synthetic_and_caller_supplied")
        both = run_mchid_arbitration(pair_A=a, pair_B=a)
        self.assertEqual(both["data_kind"], "caller_supplied_unverified")
        text = format_text_report(r)
        self.assertIn("synthetic", text)
        self.assertIn("unknown", text)
        self.assertNotIn("PASS", text)
        self.assertNotIn("FAIL", text)

    def test_invalid_levels_are_rejected(self):
        cases = [([], []), ([10, 11], [1000]), ([10, 10], [0, 200]),
                 ([11, 10], [0, 200]), ([10, 11.5], [0, 200]),
                 ([10, 11, 13], [0, 200, 600]), ([10.2, 11.2], [0, 200]),
                 ([10, 11], [0, float("nan")]), ([10, 11], [0, float("inf")]),
                 ([10, 11], [200, 100]), ([-.5, .5], [0, 100]),
                 ([10, 11], [-1, 100]), ([True, 2], [0, 100]),
                 ([[10], [11]], [0, 100]),
                 ([np.array([10]), np.array([11])], [0, 100])]
        for spins, energies in cases:
            with self.subTest(spins=spins, energies=energies), self.assertRaises(ValueError):
                self.descriptor.calculate_alignment(spins, energies)

    def test_invalid_pair_observables_are_rejected(self):
        cases = [{"parities": ["?", "-"]}, {"parities": ["+"]},
                 {"bm1_be2_staggering_in_phase": "true"},
                 {"bm1_be2_ratios_B1": [1]},
                 {"bm1_be2_ratios_B2": [1, -2, 3]},
                 {"bm1_be2_ratios_B1": [1, float("nan"), 3]},
                 {"energies_B2_keV": [0]}, {"energies_B3_keV": [0, 200, 600]}]
        for update in cases:
            with self.subTest(update=update), self.assertRaises(ValueError):
                self.descriptor.evaluate_pair(dict(pair(), **update))
        for invalid in [None, {}, {"spins": [10], "energies_B1_keV": [1000]}]:
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                self.descriptor.evaluate_pair(invalid)

    def test_invalid_scalar_inputs_are_rejected(self):
        for value in [float("nan"), float("inf"), True, np.bool_(True), "17", np.array([17])]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                MultipleChiralDoubletsDiscriminator(value, 0)
        for key in ("cross_branching_ratio", "delta_ix_crit"):
            for value in [-.1, float("nan"), float("inf"), True]:
                with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                    self.descriptor.arbitrate_mchid(pair(), pair(), **{key: value})


if __name__ == "__main__":
    unittest.main()
