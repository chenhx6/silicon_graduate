---
type: concept
title: "Feldman-Cousins unified confidence intervals with physical boundaries"
aliases: [feldman-cousins-unified-intervals, feldman-cousins-method, poisson-physical-boundary, unified-confidence-belt]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [statistics, feldman-cousins, unified-approach, confidence-intervals, physical-boundary, poisson-process, upper-limits]
---

# Feldman-Cousins unified confidence intervals with physical boundaries

## Definition

In experimental nuclear and particle physics, measurements of small signals (such as rare isomer decays, faint candidate wobbling or chiral linking transitions, or search for neutrinoless double beta decay) frequently involve unknown parameters with an explicit physical boundary:
$$\mu \ge 0$$
where $\mu$ is the expected signal count, accompanied by a known or measured expected background $b \ge 0$.

When the observed total count $n_{\text{obs}}$ fluctuates below the expected background ($n_{\text{obs}} < b$), classical Neyman confidence intervals suffer from two pathological defects:
1. **Unphysical or Empty Intervals**: A classical central interval may yield an interval entirely in the unphysical region ($\mu < 0$) or even an empty set.
2. **Flip-Flopping Undercoverage**: When experimenters decide *post-hoc* whether to report an upper limit (if $n_{\text{obs}}$ is close to or below $b$) or a central two-sided interval (if $n_{\text{obs}}$ appears large), this decision rule breaks Neyman construction guarantees, leading to severe undercoverage (the true coverage probability drops substantially below the nominal confidence level, e.g. down to $60\%$ for a nominal $90\%$ CL).

The **Feldman-Cousins Unified Method** (Feldman & Cousins 1998; 朱永生 2006 第 11 章) eliminates both defects by constructing the confidence belt using the **generalized likelihood ratio ordering principle**:
$$R(n \mid \mu) = \frac{P(n \mid \mu + b)}{P(n \mid \mu_{\text{best}} + b)}$$
where $\mu_{\text{best}} = \max(0, n - b)$ is the physically constrained Maximum Likelihood Estimator (MLE).

For each $\mu \ge 0$, values of $n$ are ranked in descending order of $R(n \mid \mu)$. Probabilities $P(n \mid \mu + b)$ are summed along this rank until:
$$\sum_{r} P(n_r \mid \mu + b) \ge \text{CL}$$
The resulting set of accepted counts $[n_{\text{lo}}(\mu), n_{\text{hi}}(\mu)]$ forms the confidence belt. Inverting this belt for the observed count $n_{\text{obs}}$ yields the unified interval $[\mu_{\text{lo}}, \mu_{\text{hi}}]$:
- When $n_{\text{obs}} \le b$: $\mu_{\text{lo}} = 0.0$, automatically reporting an **Upper Limit** without subjective flip-flopping;
- When $n_{\text{obs}} > b$: smoothly transitions to a **Two-Sided Interval** $[\mu_{\text{lo}}, \mu_{\text{hi}}]$ with non-zero lower bound.

## Necessary Assumptions

1. **Known Stationary Background**: The expected background $b$ is known with negligible uncertainty or determined from a large sideband. (When background has systematic uncertainty, profile likelihood or Cousins-Highland marginalization is required).
2. **Poisson or Gaussian Likelihood**: The total count $n$ obeys a Poisson distribution with mean $\mu + b$, or an observable $x$ obeys a Gaussian distribution $x \sim \mathcal{N}(\mu, \sigma)$ with $\sigma$ known.
3. **Physical Non-negativity Constraint**: The parameter of interest satisfies $\mu \ge 0$.

## Discriminating Observables

1. **Exact Coverage Probability $C(\mu) \ge \text{CL}$**:
   Unlike flip-flopping schemes, the unified construction guarantees that the true coverage probability $C(\mu) = P(n \in [n_{\text{lo}}(\mu), n_{\text{hi}}(\mu)] \mid \mu + b)$ is strictly greater than or equal to the nominal confidence level $\text{CL}$ for all $\mu \ge 0$.
2. **Smooth Boundary Transition**:
   As $n_{\text{obs}}$ increases from below $b$ to above $b$, the interval automatically transitions from an upper limit to a two-sided confidence interval without any subjective boundary switching.
3. **Absence of Negative Signal Assertions**:
   The lower bound $\mu_{\text{lo}}$ is bounded by 0; unphysical negative signal estimates are strictly eliminated.

## Supporting Evidence

1. **Zero Background Benchmark ($b = 0.0, \text{CL} = 90\%$)**:
   - $n_{\text{obs}} = 0 \implies \mu \in [0.00, 2.44]$
   - $n_{\text{obs}} = 1 \implies \mu \in [0.11, 4.36]$
   - $n_{\text{obs}} = 2 \implies \mu \in [0.53, 5.91]$
   - $n_{\text{obs}} = 3 \implies \mu \in [1.10, 7.42]$
   These values match Feldman-Cousins (1998) Table IV and Zhu Yongsheng (2006) Table 10.1 exactly.
2. **Finite Background Benchmark ($b = 3.0, \text{CL} = 90\%$)**:
   - For $n_{\text{obs}} = 0$: $\mu \in [0.00, 0.95]$ (Upper Limit)
   - For $n_{\text{obs}} = 2$: $\mu \in [0.00, 3.04]$ (Upper Limit)
   - For $n_{\text{obs}} = 6$: $\mu \in [0.16, 8.46]$ (Two-Sided Interval, lower bound emerges above 0).
3. **Gaussian Boundary Constraint ($x \sim \mathcal{N}(\mu, \sigma=1), \mu \ge 0, \text{CL} = 90\%$)**:
   - $x_{\text{obs}} = -2.0 \implies \mu \in [0.00, 0.40]$
   - $x_{\text{obs}} = -1.5 \implies \mu \in [0.00, 0.55]$
   - $x_{\text{obs}} = 0.0 \implies \mu \in [0.00, 1.64]$
   - $x_{\text{obs}} = 2.0 \implies \mu \in [0.58, 3.64]$
   Matches Feldman-Cousins (1998) Table X and Zhu Yongsheng (2006) Fig. 11.8 to 2 decimal places.

## Counter-evidence and Competing Interpretations

1. **Sensitivity to Expected Background When $n = 0$ (Roe-Woodroofe Critique)**:
   As pointed out by Roe & Woodroofe (2000) and Zhu Yongsheng (§11.3), in standard Feldman-Cousins, when $n_{\text{obs}} = 0$, the upper limit decreases as expected background $b$ increases (e.g. $[0, 2.44]$ for $b=0$, but $[0, 1.08]$ for $b=3$). Experimentally, observing 0 events means 0 background events occurred; penalizing or rewarding an experiment with a smaller limit purely because it had a larger expected background is counter-intuitive. The Roe-Woodroofe conditional approach conditions on the fact that background cannot exceed $n_{\text{obs}}$.
2. **Bayesian vs Frequentist Interpretations**:
   Bayesian analysis with a flat prior $\pi(\mu) = \theta(\mu)$ also restricts $\mu \ge 0$, but yields different intervals for downward fluctuations and depends on the choice of prior metric. The Feldman-Cousins unified method maintains strict frequentist coverage without invoking subjective priors.

## Our Current Position

In this wiki, low-count counting experiments with physical boundaries ($\mu \ge 0$) are analyzed using Module 97 (`feldman_cousins_unified_confidence_interval_calculator.py`, CLI subcommand `feldman`). The module implements exact likelihood ratio ordering for Poisson counting with background $b$ and analytical-numerical root solving for Gaussian observables. Ad-hoc flip-flopping and reporting unphysical negative signal rates are strictly avoided.

## Sources

- [[book-zhu-probability-statistics-in-physics]]: 朱永生, 《实验物理中的概率和统计（第二版）》, 科学出版社 (2006), 第11章 小信号测量的区间估计, 印刷 pp. 370–383 / PDF pp. 386–399.
- Feldman, G. J., Cousins, R. D., *Unified approach to the classical statistical analysis of small signals*, Phys. Rev. D 57, 3873 (1998).
- Roe, B. P., Woodroofe, M. B., *Setting confidence belts for bounded parameters*, Phys. Rev. D 60, 053009 (1999).
