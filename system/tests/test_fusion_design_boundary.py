"""Scientific boundary, conservation and conditional-kinematics checks."""

import importlib.util
import json
import math
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "system/scripts/analysis/heavy_ion_fusion_evaporation_channel_calculator.py"
SPEC = importlib.util.spec_from_file_location("fusion_design_boundary", SCRIPT)
fusion = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(fusion)


class FusionDesignBoundaryTests(unittest.TestCase):
    def analyze(self, **overrides):
        inputs = dict(Z_p=16, A_p=36, Z_t=42, A_t=100, E_lab_MeV=155.0)
        inputs.update(overrides)
        return fusion.analyze_heavy_ion_fusion(**inputs)

    def assert_no_physical_prediction(self, result):
        boundary = result["scientific_boundary"]
        self.assertFalse(boundary["physical_cross_sections_predicted"])
        self.assertFalse(boundary["statistical_evaporation_modeled"])
        self.assertFalse(boundary["evaluated_masses_used"])
        self.assertIsNone(boundary["beamtime_recommendation"])
        self.assertIsNone(boundary["target_thickness_recommendation_mg_cm2"])
        bar = result["barrier_and_fusion"]
        for key in ("sigma_fusion_mb", "L_fission_limit_hbar",
                    "fission_survival_fraction", "sigma_evaporation_total_mb"):
            self.assertIsNone(bar[key], key)
        for channel in result["evaporation_channels"].values():
            for key in ("cross_section_mb", "branching_ratio_pct", "E_opt_MeV",
                        "relative_weight"):
                self.assertIsNone(channel[key], key)
        self.assertIsNone(result["in_beam_spectroscopy"]["doppler_broadening_fwhm_keV"])
        json.dumps(result, allow_nan=False)

    def test_default_never_predicts_physical_yields_or_design(self):
        result = self.analyze()
        self.assert_no_physical_prediction(result)
        self.assertEqual(result["scientific_boundary"]["illustrative_xn_status"], "disabled")
        for channel in result["evaporation_channels"].values():
            self.assertNotIn("illustrative", channel)
        self.assertIn("SEMF", result["entrance_channel"]["Q_fusion_status"])
        self.assertIn("unvalidated", result["barrier_and_fusion"]["parameter_origin"]["height"])

    def test_positional_api_and_conservation(self):
        result = fusion.analyze_heavy_ion_fusion(16, 36, 42, 100, 155, 0.5, 90, 8, 1000)
        ent = result["entrance_channel"]
        self.assertEqual(ent["compound_nucleus"], "Z=58, A=136")
        self.assertEqual(ent["compound_A"], 36 + 100)
        self.assertEqual(ent["compound_Z"], 16 + 42)
        self.assertAlmostEqual(ent["E_cm_MeV"], 155 * 100 / 136)
        self.assertAlmostEqual(ent["E_excitation_MeV"], ent["E_cm_MeV"] + ent["Q_fusion_MeV"])
        for channel in result["evaporation_channels"].values():
            self.assertEqual(channel["residue_Z"], ent["compound_Z"])
            self.assertEqual(channel["residue_A"] + channel["emitted_neutrons"],
                             ent["compound_A"])
            self.assertGreaterEqual(channel["residue_A"], channel["residue_Z"])
        self.assertEqual(result["evaporation_channels"]["5n"]["residue_A"], 131)
        self.assertEqual(result["evaporation_channels"]["6n"]["residue_A"], 130)
        self.assertEqual(self.analyze(Z_p=1, A_p=1, Z_t=1, A_t=1)["evaporation_channels"], {})

    def test_wong_at_barrier_has_correct_units(self):
        # At E_cm=V, softplus(0)=log(2); fm^2 -> mb gives a factor 10.
        bar = self.analyze(E_lab_MeV=80 * 136 / 100, barrier_radius_fm=10,
                           barrier_height_MeV=80, barrier_curvature_MeV=4)["barrier_and_fusion"]
        self.assertAlmostEqual(bar["schematic_wong_cross_section_mb"],
                               4 * 10**2 / (2 * 80) * math.log(2) * 10)
        self.assertEqual(bar["L_max_hbar"], 0)

    def test_wong_geometry_barrier_and_curvature_sensitivity(self):
        kwargs = dict(barrier_radius_fm=10, barrier_height_MeV=80)
        def area(**extra):
            return self.analyze(**dict(kwargs, **extra))["barrier_and_fusion"]["schematic_wong_cross_section_mb"]
        base = area()
        self.assertAlmostEqual(area(barrier_radius_fm=20), 4 * base)
        self.assertLess(area(barrier_height_MeV=90), base)
        self.assertGreater(area(E_lab_MeV=170), base)
        below = dict(E_lab_MeV=75 * 136 / 100)
        self.assertGreater(area(**below, barrier_curvature_MeV=5),
                           area(**below, barrier_curvature_MeV=3))
        high = area(E_lab_MeV=1000)
        geometric = math.pi * 10**2 * (1 - 80 / (1000 * 100 / 136)) * 10
        self.assertAlmostEqual(high, geometric)

    def test_classical_orbital_scale_is_not_spin_or_fission_cutoff(self):
        result = self.analyze()
        bar, ent = result["barrier_and_fusion"], result["entrance_channel"]
        mu = fusion.M_U_MEV * 36 * 100 / 136
        centrifugal = (2 * mu * bar["R_barrier_fm"]**2
                       * (ent["E_cm_MeV"] - bar["V_barrier_MeV"]) / fusion.HBAR_C_MEV_FM**2)
        ell = bar["L_max_hbar"]
        self.assertAlmostEqual(ell * (ell + 1), centrifugal)
        self.assertGreater(ell, 52)
        self.assert_no_physical_prediction(self.analyze(E_lab_MeV=400))
        below = self.analyze(E_lab_MeV=100)["barrier_and_fusion"]
        self.assertEqual(below["L_max_hbar"], 0)
        self.assertGreater(below["schematic_wong_cross_section_mb"], 0)

    def test_initial_recoil_momentum_and_beam_scaling(self):
        def beta(result):
            return result["in_beam_spectroscopy"]["recoil_velocity_beta"]
        initial = beta(self.analyze())
        beam_beta = math.sqrt(2 * 155 / (36 * fusion.M_U_MEV))
        self.assertAlmostEqual(136 * initial, 36 * beam_beta)
        self.assertAlmostEqual(beta(self.analyze(E_lab_MeV=620)), 2 * initial)
        # Same E_cm after swapping projectile/target; the lab recoil changes.
        swapped = self.analyze(Z_p=42, A_p=100, Z_t=16, A_t=36, E_lab_MeV=155 * 100 / 36)
        self.assertAlmostEqual(swapped["entrance_channel"]["E_cm_MeV"],
                               self.analyze()["entrance_channel"]["E_cm_MeV"])

    def test_illustrations_are_opt_in_and_never_become_cross_sections(self):
        result = self.analyze(illustrative_xn=True)
        self.assert_no_physical_prediction(result)
        weights = [item["illustrative"]["normalized_weight_within_displayed_xn"]
                   for item in result["evaporation_channels"].values()]
        self.assertAlmostEqual(sum(weights), 1)
        for item in result["evaporation_channels"].values():
            self.assertFalse(item["illustrative"]["physical_channel_probability"])
            self.assertFalse(item["illustrative"]["thresholds_checked"])
        wider = self.analyze(illustrative_xn=True, illustrative_xn_width_MeV=20)
        wider_weights = [item["illustrative"]["normalized_weight_within_displayed_xn"]
                         for item in wider["evaporation_channels"].values()]
        self.assertLess(max(wider_weights), max(weights))
        self.assert_no_physical_prediction(wider)
        low = self.analyze(E_lab_MeV=1, illustrative_xn=True)
        self.assertLess(low["entrance_channel"]["E_excitation_MeV"], 0)
        self.assertIn("unavailable", low["scientific_boundary"]["illustrative_xn_status"])
        self.assertTrue(all("illustrative" not in item for item in low["evaporation_channels"].values()))

    def test_thickness_is_honestly_unmodeled(self):
        thin = self.analyze(target_thickness_mg_cm2=0)
        thick = self.analyze(target_thickness_mg_cm2=10)
        for result in (thin, thick):
            spec = result["in_beam_spectroscopy"]
            self.assertFalse(spec["target_transport_modeled"])
            self.assertIsNone(spec["target_energy_loss_MeV"])
        thin["in_beam_spectroscopy"]["target_thickness_mg_cm2"] = 10.0
        self.assertEqual(thin, thick)

    def test_angular_span_is_endpoint_difference_not_fwhm(self):
        spec = self.analyze()["in_beam_spectroscopy"]
        beta = spec["recoil_velocity_beta"]
        energy = lambda theta: 1000 * math.sqrt(1 - beta**2) / (1 - beta * math.cos(math.radians(theta)))
        self.assertEqual(spec["polar_angle_interval_deg"], [86, 94])
        self.assertAlmostEqual(spec["doppler_angular_full_span_keV"], energy(86) - energy(94))
        self.assertAlmostEqual(spec["doppler_shift_keV"], energy(90) - 1000)
        self.assertLess(spec["doppler_shift_keV"], 0)  # transverse Doppler term
        self.assertIsNone(spec["doppler_broadening_fwhm_keV"])
        double = self.analyze(E_gamma_keV=2000)["in_beam_spectroscopy"]
        self.assertAlmostEqual(double["doppler_angular_full_span_keV"],
                               2 * spec["doppler_angular_full_span_keV"])
        zero = self.analyze(detector_dtheta_deg=0)["in_beam_spectroscopy"]
        self.assertEqual(zero["doppler_angular_full_span_keV"], 0)
        forward = self.analyze(detector_angle_deg=0)["in_beam_spectroscopy"]
        self.assertEqual(forward["polar_angle_interval_deg"], [0, 4])
        self.assertGreater(forward["doppler_angular_full_span_keV"], 0)
        backward = self.analyze(detector_angle_deg=180)["in_beam_spectroscopy"]
        self.assertEqual(backward["polar_angle_interval_deg"], [176, 180])
        self.assertLess(backward["doppler_shift_keV"], 0)

    def test_invalid_nuclei_are_rejected(self):
        for name in ("A_p", "A_t", "Z_p", "Z_t"):
            for value in (0, -1, 1.5, math.nan, math.inf, True, "16", None):
                with self.subTest(name=name, value=value), self.assertRaises(ValueError):
                    self.analyze(**{name: value})
        for values in (dict(Z_p=37), dict(Z_t=101), dict(Z_p=-1)):
            with self.assertRaises(ValueError):
                self.analyze(**values)
        for Z, A in ((2, 1), (-1, 10), (1, 0), (1.5, 10), (True, 10)):
            with self.assertRaises(ValueError):
                fusion.calculate_liquid_drop_mass(Z, A)

    def test_invalid_continuous_parameters_are_rejected(self):
        positive = ("E_lab_MeV", "E_gamma_keV", "barrier_radius_fm",
                    "barrier_height_MeV", "barrier_curvature_MeV", "illustrative_xn_width_MeV")
        nonnegative = ("target_thickness_mg_cm2", "detector_angle_deg", "detector_dtheta_deg")
        for name in positive + nonnegative:
            invalid = (-1, math.nan, math.inf, -math.inf, True, "1", None)
            if name in ("barrier_radius_fm", "barrier_height_MeV"):
                invalid = invalid[:-1]  # None requests the legacy recipe.
            if name in positive:
                invalid += (0,)
            for value in invalid:
                with self.subTest(name=name, value=value), self.assertRaises(ValueError):
                    self.analyze(**{name: value})
        for name in ("detector_angle_deg", "detector_dtheta_deg"):
            with self.assertRaises(ValueError):
                self.analyze(**{name: 181})
        with self.assertRaises(ValueError):
            self.analyze(illustrative_xn="yes")
        with self.assertRaises(ValueError):
            self.analyze(E_lab_MeV=36 * fusion.M_U_MEV)

    def test_numerical_extremes_fail_cleanly_or_preserve_the_boundary(self):
        for overrides in (dict(E_lab_MeV=5e-324),
                          dict(barrier_curvature_MeV=5e-324),
                          dict(illustrative_xn=True, illustrative_xn_width_MeV=5e-324)):
            with self.subTest(**overrides):
                self.assert_no_physical_prediction(self.analyze(**overrides))
        for overrides in (dict(barrier_radius_fm=1e300),
                          dict(barrier_curvature_MeV=1e308)):
            with self.subTest(**overrides), self.assertRaises(ValueError):
                self.analyze(**overrides)

    def test_cli_json_and_text_preserve_the_boundary(self):
        args = [sys.executable, str(SCRIPT)]
        run = subprocess.run(args + ["--json"], capture_output=True, text=True, check=True)
        result = json.loads(run.stdout)
        self.assert_no_physical_prediction(result)
        text = subprocess.run(args, capture_output=True, text=True, check=True).stdout
        self.assertIn("Schematic Wong", text)
        self.assertIn("not evaluated mass", text)
        self.assertIn("FWHM unavailable", text)
        self.assertIn("No beamtime or target-thickness recommendation", text)
        bad = subprocess.run(args + ["--Elab", "0", "--json"], capture_output=True, text=True)
        self.assertEqual(bad.returncode, 2)
        self.assertEqual(bad.stdout, "")
        self.assertNotIn("Traceback", bad.stderr)


if __name__ == "__main__":
    unittest.main()
