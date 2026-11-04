"""Focused tests for Zhu Ch. 14 Monte Carlo integration utilities."""

import math
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))

from monte_carlo_integrator import adaptive_stratified_integrate_1d, monte_carlo_integrate


class MonteCarloIntegratorTests(unittest.TestCase):
    def test_uniform_integral_has_reproducible_estimate(self):
        result = monte_carlo_integrate(lambda x: x[0] ** 2, [(0.0, 1.0)], 20000, seed=7)
        self.assertAlmostEqual(result["estimate"], 1.0 / 3.0, delta=4.0 * result["standard_error"])
        self.assertEqual(result["sampling_mode"], "uniform-rectangular")

    def test_importance_sampling_matches_same_integral(self):
        # q(x)=2x on [0,1], so g/q is constant for g(x)=2*x/3.
        def sampler(rng, n):
            return np.sqrt(rng.random((n, 1)))

        def density(samples):
            return 2.0 * samples[:, 0]

        import numpy as np
        result = monte_carlo_integrate(
            lambda x: 2.0 * x[0] / 3.0,
            [(0.0, 1.0)],
            1000,
            seed=11,
            proposal_sampler=sampler,
            proposal_density=density,
        )
        self.assertAlmostEqual(result["estimate"], 1.0 / 3.0, places=12)
        self.assertLess(result["standard_error"], 1.0e-12)

    def test_adaptive_stratified_integral(self):
        result = adaptive_stratified_integrate_1d(
            lambda x: math.exp(x),
            0.0,
            1.0,
            2000,
            n_strata=10,
            pilot_samples_per_stratum=10,
            seed=19,
        )
        self.assertAlmostEqual(result["estimate"], math.e - 1.0, delta=5.0 * result["standard_error"])
        self.assertEqual(sum(result["stratum_sample_counts"]), 2000)


if __name__ == "__main__":
    unittest.main()
