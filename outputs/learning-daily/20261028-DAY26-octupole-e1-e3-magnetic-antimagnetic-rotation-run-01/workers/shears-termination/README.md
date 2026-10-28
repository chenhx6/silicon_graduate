# Shears termination endpoint audit

Run:

```bash
python3 shears_termination_trajectory.py
```

The script writes `shears_termination_angular.csv`,
`shears_termination_trajectory.csv`, and `shears_termination_results.json`.
It contains three separable calculations:

1. a fixed two-blade MR angle scan and its `B(M1)` endpoint;
2. a symmetric four-blade AMR scan using Roy et al. Eq. (1),
   `B(E2) = 15 (e Q_eff)^2 sin^4(theta)/(32 pi)`;
3. bounded frequency trajectories for fixed closure, a configuration
   reopening proxy, and a deliberately pathological turnover reverse test.

The endpoint powers and `J^(2)` extrema are algebraic/toy-model checks. They
do not replace lifetimes, configuration assignments, or a self-consistent
TAC/EDF calculation.
