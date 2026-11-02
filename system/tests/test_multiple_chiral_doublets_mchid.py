#!/usr/bin/env python3
"""
Unit tests for multiple_chiral_doublets_mchid_discriminator.py (Module 162).
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from multiple_chiral_doublets_mchid_discriminator import (
    PRESETS,
    MultipleChiralDoubletsDiscriminator
)

class TestMultipleChiralDoubletsMChD(unittest.TestCase):

    def test_133Ce_classic_mchid_confirmation(self):
        p = PRESETS["133Ce_classic_mchid"]
        discrim = MultipleChiralDoubletsDiscriminator(
            harris_J0=p["harris_J0"],
            harris_J1=p["harris_J1"]
        )
        res = discrim.arbitrate_mchid(
            p["pair_A"], p["pair_B"],
            cross_branching_ratio=p["cross_doublet_branching_ratio"]
        )
        # All 4 gates must pass for 133Ce
        self.assertTrue(res["is_mchid_confirmed"])
        self.assertTrue(res["gates_evaluation"]["gate1_energy_degeneracy"])
        self.assertTrue(res["gates_evaluation"]["gate2_in_phase_staggering"])
        self.assertTrue(res["gates_evaluation"]["gate3_alignment_separation"])
        self.assertTrue(res["gates_evaluation"]["gate4_cross_suppression"])
        # Alignment separation should be > 2 hbar
        self.assertGreater(res["alignment_separation_Delta_ix_hbar"], 2.0)

    def test_energy_degeneracy_violation(self):
        p = PRESETS["133Ce_classic_mchid"]
        discrim = MultipleChiralDoubletsDiscriminator()
        # Create fictitious pair with large splitting (400 keV)
        fake_pair = p["pair_A"].copy()
        fake_pair["energies_B2_keV"] = [e + 400.0 for e in fake_pair["energies_B1_keV"]]
        res = discrim.arbitrate_mchid(fake_pair, p["pair_B"])
        self.assertFalse(res["gates_evaluation"]["gate1_energy_degeneracy"])
        self.assertFalse(res["is_mchid_confirmed"])

    def test_cross_talk_branching_violation(self):
        p = PRESETS["133Ce_classic_mchid"]
        discrim = MultipleChiralDoubletsDiscriminator()
        # Excessive cross-doublet branching (35%)
        res = discrim.arbitrate_mchid(p["pair_A"], p["pair_B"], cross_branching_ratio=0.35)
        self.assertFalse(res["gates_evaluation"]["gate4_cross_suppression"])
        self.assertFalse(res["is_mchid_confirmed"])

if __name__ == "__main__":
    unittest.main()
