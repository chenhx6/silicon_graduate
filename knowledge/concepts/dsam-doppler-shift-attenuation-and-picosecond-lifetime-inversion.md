---
type: concept
title: "Doppler shift attenuation method (DSAM) and picosecond nuclear state lifetime inversion"
aliases: [dsam-lifetime-inversion, doppler-attenuation-factor, lss-stopping-power, blaugrund-multiple-scattering]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [in-beam-spectroscopy, dsam, lifetime-measurement, stopping-power, lss-theory, blaugrund, transition-probabilities, b-e2, b-m1]
---

# Doppler shift attenuation method (DSAM) and picosecond nuclear state lifetime inversion

## Definition

In in-beam $\gamma$-ray spectroscopy of high-spin states, excited nuclear states in the picosecond regime ($\tau \sim 0.01 - 2.0\text{ ps}$, or $10 - 2000\text{ fs}$) decay while the recoiling compound residue slows down inside a thick target or backing medium (such as gold, lead, or copper). The Doppler Shift Attenuation Method (DSAM; 吴治华 2005 第 15 章; Nolan & Sharpey-Schafer 1979) extracts the mean lifetime $\tau$ from the centroid shift or lineshape of the detected $\gamma$ ray:
$$E_\gamma(\theta) = E_{\gamma 0} \left[ 1 + F(\tau) \frac{v_0}{c} \cos\theta \right]$$
where:
- $E_{\gamma 0}$ is the unshifted transition energy emitted at rest;
- $v_0$ is the initial recoil velocity along the beam axis ($v_0/c \approx 0.01 - 0.03$ in heavy-ion fusion);
- $\theta$ is the angle of the HPGe detector relative to the beam direction;
- $F(\tau)$ is the dimensionless **Doppler attenuation factor** ($0 \le F \le 1$).

The attenuation factor represents the velocity-weighted expectation value of the decaying nuclei:
$$F(\tau) = \frac{1}{v_0 \tau} \int_0^\infty \overline{v(t) \cos\phi(t)} e^{-t/\tau} dt$$
where $\overline{\cos\phi(t)}$ is the Blaugrund multiple scattering direction cosine.
- When $\tau \ll \alpha_{\text{stop}}$ ($\tau < 0.05\text{ ps}$): The state decays before the recoil slows down, emitting $\gamma$ rays at nearly full initial velocity $\implies F(\tau) \approx 1.0$ (fully shifted peak);
- When $\tau \gg \alpha_{\text{stop}}$ ($\tau > 3.0\text{ ps}$): The state decays after coming to complete rest $\implies F(\tau) \approx 0.0$ (unshifted peak);
- In the optimal window $\tau \approx 0.1 - 1.5\text{ ps}$: $F(\tau)$ varies sensitively and monotonically with $\tau$, enabling exact inversion of the nuclear lifetime $\tau_{\text{exp}}$ from the observed energy shift:
  $$F(\tau_{\text{exp}}) = \frac{E_\gamma(\theta_1) - E_\gamma(\theta_2)}{E_{\gamma 0} \frac{v_0}{c} (\cos\theta_1 - \cos\theta_2)}$$

## Necessary Assumptions

1. **Unidirectional Initial Recoil**: Compound nucleus recoil is strongly focused forward along the beam axis with known initial velocity $v_0 / c = \frac{A_p}{A_p + A_t} \sqrt{2 E_{\text{lab}} / (A_p m_u c^2)}$. (Neutron evaporation momentum kicks produce small angular dispersions).
2. **Lindhard-Scharff-Schiott (LSS) Stopping Power**: The total specific energy loss in the backing consists of electronic stopping $S_e \propto v$ and nuclear stopping $S_n$ from screened Coulomb collisions:
   $$\frac{dE}{dx} = S_e(E) + S_n(E)$$
3. **Blaugrund Semiclassical Scattering**: Multiple elastic nuclear collisions deflect the recoil path, attenuating the forward velocity projection according to:
   $$\overline{\cos\phi(v)} \approx \exp\left[ -\frac{1}{2} \frac{M_2}{M_1} \int_v^{v_0} \frac{S_n(v')}{S_e(v') + S_n(v')} \frac{dv'}{v'} \right]$$

## Discriminating Observables

1. **Angle-Dependent Centroid Shift**:
   Plotting $E_\gamma(\theta)$ versus $\cos\theta$ across forward, $90^\circ$, and backward detectors forms a straight line whose slope directly measures $F(\tau) \frac{v_0}{c} E_{\gamma 0}$.
2. **Monotonic $F(\tau)$ Sensitivity**:
   The attenuation factor $F(\tau)$ decreases monotonically with $\tau$. Measurement of $F \pm \Delta F$ translates directly to a bounded lifetime $\tau \pm \Delta\tau$.
3. **Extraction of Reduced Transition Probabilities**:
   Combined with the measured $\gamma$ branching ratio $b_\gamma$, the internal conversion coefficient $\alpha$, and the transition multipolarity ($E2, M1$), the partial lifetime $\tau_\gamma = \tau (1 + \alpha) / b_\gamma$ yields model-independent reduced transition probabilities $B(E2)$ and $B(M1)$, serving as the definitive test of triaxial wobbling collectivity and chiral selection rules.

## Supporting Evidence

1. **$^{134}\text{Ce}$ Recoil in Gold Backing Benchmark ($Z_1=58, M_1=134; Z_2=79, M_2=197; v_0/c = 0.020$)**:
   - Thomas-Fermi screening length: $a_{\text{TF}} = 0.0811\text{ \AA}$;
   - LSS electronic stopping constant: $k_e = 0.2103$;
   - Stopping scale: $\alpha_{\text{stop}} \approx 0.82\text{ ps}$;
   - For an experimental attenuation factor $F_{\text{exp}} = 0.520 \pm 0.030$: inverted lifetime is $\tau = 0.7487\text{ ps}$ ($748.7\text{ fs}$), with $1\sigma$ range $[0.6528, 0.8581]\text{ ps}$.
2. **$^{163}\text{Lu}$ TSD Wobbling Band Lifetimes**:
   - Inverted lifetimes for $n_w = 1 \to n_w = 0$ inter-band transitions in $^{163}\text{Lu}$ gave $\tau \sim 0.2 - 0.5\text{ ps}$, confirming large transition quadrupole moments $Q_t \approx 10\text{ eb}$ and highly enhanced $B(E2)_{\text{out}} \approx 20 - 30\text{ W.u.}$, proving the existence of the wobbling phonon.

## Counter-evidence and Competing Interpretations

1. **Side-Feeding Time Delay Contamination**:
   Excited high-spin states are populated not only directly by the reaction but also indirectly through a cascade of unobserved side-feeding transitions. If side-feeding transitions have finite lifetimes $\tau_{\text{feed}}$, the apparent attenuation factor $F_{\text{app}}$ is smaller than the true level $F(\tau)$, leading to an overestimation of the lifetime $\tau$. Rigorous analysis requires gate-from-above coincidence slicing or side-feeding deconvolution modeling (Module 21).
2. **Stopping Power Systematics (SRIM vs LSS)**:
   Theoretical LSS stopping powers may carry $5\% - 10\%$ systematic uncertainties depending on ion-target atomic shell matching. Modern DSAM calibrations employ evaluated SRIM/ASTAR tables or independent experimental stopping cross-section calibrations.

## Our Current Position

In this wiki, Doppler shift attenuation factors and picosecond nuclear state lifetimes are calculated and inverted using Module 100 (`dsam_doppler_attenuation_lss_blaugrund_lifetime_calculator.py`, CLI subcommand `dsam`). The engine computes LSS Thomas-Fermi stopping parameters, integrates Blaugrund multiple scattering, evaluates the full $F(\tau)$ calibration curve, and inverts experimental centroid shifts with exact $1\sigma$ uncertainty propagation.

## Sources

- [[book-wu-nuclear-experiment-methods]]: 吴治华, 《原子核物理实验方法（第三版）》, 原子能出版社 (2005), 第15章 核寿命的测量, 印刷 pp. 421–452 / PDF pp. 429–460.
- Nolan, P. J., Sharpey-Schafer, J. F., *The measurement of the lifetimes of excited nuclear states using the Doppler shift attenuation method*, Rep. Prog. Phys. 42, 1 (1979).
- Lindhard, J., Scharff, M., Schiott, H. E., *Range concepts and heavy ion ranges*, Mat. Fys. Medd. Dan. Vid. Selsk. 33, no. 14 (1963).
- Blaugrund, A. E., *Notes on nuclear stopping and energy loss in Doppler shift measurements*, Nucl. Phys. 88, 501 (1966).
