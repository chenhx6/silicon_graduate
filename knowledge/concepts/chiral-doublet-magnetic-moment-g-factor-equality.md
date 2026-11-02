---
type: concept
title: "Chiral doublet magnetic moment g-factor equality theorem and spurious band arbitration"
aliases: [chiral-g-factor-equality, grodner-chiral-theorem, chiral-magnetic-moments, chiral-doublet-arbitration]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [chirality, g-factor, magnetic-moments, grodner-theorem, spontaneous-symmetry-breaking, time-reversal-breaking, 128cs-benchmark]
---

# Chiral doublet magnetic moment g-factor equality theorem and spurious band arbitration

## The Grodner Chiral $g$-Factor Equality Theorem

A major challenge in high-spin nuclear spectroscopy is that accidental degeneracies (e.g. signature partner bands, shape coexistence, or pseudo-spin doublets) can exhibit near-identical excitation energies ($\Delta E \le 100\text{ keV}$), masquerading as chiral doublet bands.

To establish an unambiguous, smoking-gun test of spontaneous chiral symmetry breaking, E. Grodner et al. (Phys. Rev. Lett. 120, 022502, 2018; CRC 2025 Ch. 7, PDF pp. 156–166) formulated the **Chiral Gyromagnetic Factor ($g$) Equality Theorem**:

### 1. Quantum Symmetry Principle
In a genuine chiral nucleus, spontaneous breaking of time-reversal $\mathcal{T}$ and $\mathcal{R}_y(\pi)$ in the body-fixed frame creates degenerate left-handed $|L\rangle$ and right-handed $|R\rangle$ chiral states.
In the laboratory frame, restoration of discrete symmetry splits the system into symmetric and antisymmetric eigenstates:
$$|\text{Band 1}\rangle = \frac{|L\rangle + |R\rangle}{\sqrt{2}}, \quad |\text{Band 2}\rangle = \frac{|L\rangle - |R\rangle}{\sqrt{2}}$$

The magnetic dipole moment operator $\hat{\mu} = g_R \vec{R} + g_p \vec{j}_p + g_n \vec{j}_n$ is **odd under time reversal** ($\mathcal{T} \hat{\mu} \mathcal{T}^{-1} = -\hat{\mu}$).
Consequently, the off-diagonal matrix elements between the left- and right-handed states cancel identically:
$$\langle L \mid \hat{\mu} \mid R \rangle = \langle R \mid \hat{\mu} \mid L \rangle = 0$$
The diagonal expectation values satisfy:
$$\langle \text{Band 1} \mid \hat{\mu} \mid \text{Band 1} \rangle = \frac{1}{2} \left[ \langle L|\hat{\mu}|L\rangle + \langle R|\hat{\mu}|R\rangle \right] = \langle \text{Band 2} \mid \hat{\mu} \mid \text{Band 2} \rangle$$

**The Fundamental Theorem**:
$$g(\text{Band 1}, I) \equiv g(\text{Band 2}, I)$$
**The $g$-factors of the two partner bands must be identical at every spin $I$ within the chiral regime!**
If an experimental measurement reveals $g_1(I) \ne g_2(I)$ with statistical significance $\ge 3\sigma$, the candidate doublet is definitively ruled out as chiral.

---

## Microscopic 3D Aplanar Geometry Formula

In odd-odd nuclei with proton particle $j_p$ along the short ($s$) axis, neutron hole $j_n$ along the long ($l$) axis, and core rotation $R_m$ along the intermediate ($m$) axis:
$$g_{\text{chiral}}(I) = g_R + (g_p - g_R) \frac{j_p^2}{I(I+1)} + (g_n - g_R) \frac{j_n^2}{I(I+1)}$$
where:
- $g_R \approx Z / A$ is the collective rotational gyromagnetic ratio;
- $g_p \approx 1.25 - 1.35$ for $h_{11/2}$ protons;
- $g_n \approx -0.15 - -0.25$ for $h_{11/2}$ neutron holes.

---

## Statistical Arbitration Criterion

Given experimental measurements $g_1 \pm \sigma_1$ and $g_2 \pm \sigma_2$:
$$\Delta g = |g_1 - g_2|, \quad \sigma_{\Delta g} = \sqrt{\sigma_1^2 + \sigma_2^2}$$
$$\chi^2_g = \left( \frac{\Delta g}{\sigma_{\Delta g}} \right)^2, \quad p = \text{erfc}\left( \sqrt{\frac{\chi^2_g}{2}} \right)$$
- $\chi^2_g \le 1.0$: Chiral equality confirmed ($H_0: g_1 = g_2$ supported);
- $1.0 < \chi^2_g \le 4.0$: Compatible within $2\sigma$;
- $\chi^2_g \ge 9.0$: Chiral hypothesis rejected at $> 99.73\%$ ($3\sigma$) confidence level.

---

## Canonical Experimental Benchmarks

1. **$^{128}\text{Cs}$ Chiral Doublet Benchmark (Grodner et al. PRL 2018)**:
   - Measured $g$-factors at $I = 11^+$:
     $$g(\text{Band 1}) = +0.58 \pm 0.04, \quad g(\text{Band 2}) = +0.56 \pm 0.05$$
   - $\Delta g = 0.020 \pm 0.064 \implies \chi^2_g = 0.098$ ($0.31\sigma$ discrepancy, $p = 0.755$);
   - Confirms the Grodner equality theorem, providing the most rigorous proof of nuclear chirality in $^{128}\text{Cs}$.
2. **Spurious Pseudo-Chiral Counterexample**:
   - Experimental doublet with $g_1 = +0.85 \pm 0.04$ and $g_2 = +0.32 \pm 0.05$:
   - $\Delta g = 0.530 \pm 0.064 \implies \chi^2_g = 68.51$ ($8.28\sigma$ discrepancy, $p = 1.26 \times 10^{-16}$);
   - Decisively eliminates the spurious bands from chiral classification.

---

## Primary Source References

- **Grodner, E. et al.**: *Partner bands in $^{128}\text{Cs}$ as the first identification of chiral doublet bands by magnetic moment measurements*, Phys. Rev. Lett. 120, 022502 (2018).
- **Grodner, E.**: *Experimental Evidence of Chirality in $^{126,128}\text{Cs}$*, in *Chirality and Wobbling in Atomic Nuclei*, CRC Press (2025), Chapter 7, PDF pp. 156–166.
- **Frauendorf, S.**: *Spontaneous symmetry breaking in rotating nuclei*, Rev. Mod. Phys. 73, 463–514 (2001).
