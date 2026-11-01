"""
Unit tests for HPGe Coaxial Electric Field, Shockley-Ramo Pulse Formation & Ballistic Deficit.

Benchmarked against:
  - 吴治华, 《原子核物理实验方法（第三版）》, 原子能出版社 (2005), 第5章 (半导体探测器).
  - 汪晓莲等, 《粒子探测技术》, 中国科学技术大学出版社 (2009), 第5章.
  - M. Nakhostin, 《辐射探测器信号处理》, 科学出版社 (2020), 第1章 & 第4章.
"""

import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from hpge_coaxial_electric_field_ballistic_deficit_calculator import (
    calculate_coaxial_depletion_and_field,
    calculate_shockley_ramo_collection,
    calculate_coaxial_ballistic_deficit,
    reconcile_neutron_damage_p_vs_n
)


class HPGeCoaxialFieldBallisticDeficitTests(unittest.TestCase):

    def test_coaxial_depletion_voltage_and_field_distribution(self):
        """Verify analytical depletion voltage V_dep and electric field at inner/outer contacts."""
        # Standard coaxial detector: r1 = 5 mm, r2 = 35 mm, N_net = 3.0e9 cm^-3, V_bias = 4000 V
        res = calculate_coaxial_depletion_and_field(r1_mm=5.0, r2_mm=35.0, N_net_cm3=3.0e9, V_bias_V=4000.0)
        self.assertAlmostEqual(res["depletion_voltage_V"], 3026.0, places=0)
        self.assertAlmostEqual(res["overbias_ratio"], 1.32, places=2)
        self.assertTrue(res["is_fully_depleted"])
        self.assertTrue(res["is_velocity_saturated"])
        self.assertGreater(res["E_inner_contact_V_per_cm"], 3000.0)
        self.assertGreater(res["E_outer_contact_V_per_cm"], 1000.0)

    def test_shockley_ramo_collection_times(self):
        """Verify electron/hole drift times and max collection time at saturated velocity vs = 10^5 m/s."""
        # Interaction at mid-radius r0 = 25 mm in 5-35 mm crystal
        res = calculate_shockley_ramo_collection(r0_mm=25.0, r1_mm=5.0, r2_mm=35.0, detector_type="p_type")
        self.assertAlmostEqual(res["electron_drift_distance_mm"], 20.0)
        self.assertAlmostEqual(res["hole_drift_distance_mm"], 10.0)
        self.assertAlmostEqual(res["electron_drift_time_ns"], 200.0)
        self.assertAlmostEqual(res["hole_drift_time_ns"], 100.0)
        self.assertAlmostEqual(res["total_collection_time_ns"], 200.0)
        self.assertAlmostEqual(res["max_possible_collection_time_ns"], 300.0)

    def test_digital_trapezoidal_flat_top_immunity(self):
        """Verify digital trapezoidal flat-top T_flat >= t_c completely eliminates ballistic deficit."""
        # 1. Flat-top 800 ns > collection time 200 ns => 0.0 deficit
        b_immune = calculate_coaxial_ballistic_deficit(tc_ns=200.0, flat_top_ns=800.0, rise_time_ns=4000.0)
        self.assertAlmostEqual(b_immune["trapezoidal_ballistic_deficit_pct"], 0.0)
        self.assertIn("Exact Zero Deficit", b_immune["trapezoidal_immunity_status"])

        # 2. Flat-top 100 ns < collection time 200 ns => finite deficit
        b_finite = calculate_coaxial_ballistic_deficit(tc_ns=200.0, flat_top_ns=100.0, rise_time_ns=4000.0)
        self.assertGreater(b_finite["trapezoidal_ballistic_deficit_pct"], 0.0)

        # 3. Analog Gaussian with tau = 2000 ns has finite quadratic deficit ~ 0.083%
        self.assertAlmostEqual(b_immune["gaussian_ballistic_deficit_pct"], 0.0833, places=3)

    def test_neutron_damage_ptype_vs_ntype_reconciliation(self):
        """Verify N-type reverse electrode maintains resolution at fluences where P-type degrades severely."""
        neu = reconcile_neutron_damage_p_vs_n(fast_neutron_fluence_n_cm2=2.0e9)
        self.assertIn("Severe Degradation", neu["p_type_coaxial_status"])
        self.assertIn("Good / Mild", neu["n_type_reverse_coaxial_status"])
        self.assertIn("10-20x", neu["neutron_hardness_advantage"])

    def test_invalid_parameters_raised(self):
        """Invalid geometries (r1 >= r2, r1 <= 0) must raise ValueError."""
        with self.assertRaises(ValueError):
            calculate_coaxial_depletion_and_field(r1_mm=10.0, r2_mm=5.0) # r1 > r2
        with self.assertRaises(ValueError):
            calculate_shockley_ramo_collection(r0_mm=40.0, r1_mm=5.0, r2_mm=35.0) # r0 outside crystal

    def test_strict_json_serialization(self):
        """Verify strict RFC JSON serialization without NaN or Inf."""
        dep = calculate_coaxial_depletion_and_field(r1_mm=5.0, r2_mm=35.0)
        ramo = calculate_shockley_ramo_collection(r0_mm=25.0, r1_mm=5.0, r2_mm=35.0)
        bal = calculate_coaxial_ballistic_deficit(tc_ns=200.0)
        neu = reconcile_neutron_damage_p_vs_n(fast_neutron_fluence_n_cm2=1.0e9)
        payload = {"dep": dep, "ramo": ramo, "bal": bal, "neu": neu}
        s = json.dumps(payload, allow_nan=False)
        self.assertIn("depletion_voltage_V", s)


if __name__ == "__main__":
    unittest.main()
