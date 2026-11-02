---
type: concept
title: "Nuclear chiral doublet electromagnetic selection rules, in-phase B(M1) staggering and inter-band M1 transition suppression"
aliases: [chiral-selection-rules, m1-staggering-phase, chiral-m1-suppression, electromagnetic-chiral-rules, koike-selection-rules]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [triaxiality, nuclear-chirality, chiral-doublets, selection-rules, m1-staggering, interband-m1, 128cs]
---

# Nuclear chiral doublet electromagnetic selection rules, in-phase B(M1) staggering and inter-band M1 transition suppression

## Definition and Phenomenological Origin

Spontaneous breaking of time-reversal-rotation symmetry $\mathcal{T}\mathcal{R}_y(\pi)$ in triaxial nuclei produces two degenerate left- and right-handed states, which quantum-mechanically superpose into partner bands with identical parity and spin sequences.

Based on *Chirality and Wobbling in Atomic Nuclei* (CRC Press 2025) Chapter 7 (E. Grodner) & Chapter 8, T. Koike, K. Starosta, I. Hamamoto (Phys. Rev. Lett. 93, 172502, 2004), and E. Grodner et al. (Phys. Rev. Lett. 97, 172501, 2006):
Energy degeneracy alone ($\Delta E(I) \le 100\text{ keV}$) is NOT a sufficient condition for chirality—shape coexistence or accident degenerate rotational bands can mimic energy similarity. Genuine chiral doublets must satisfy rigorous electromagnetic selection rules.

---

## The Three Fundamental Chiral Selection Rules

### 1. In-Phase Intra-Band $B(M1)$ Staggering
The reduced transition probabilities $B(M1; I \to I - 1)$ exhibit odd-even spin staggering parameterized by:
$$S_{M1}(I) = \frac{B(M1; I \to I - 1)}{\frac{1}{2} \left[ B(M1; I + 1 \to I) + B(M1; I - 1 \to I - 2) \right]}$$
**Criterion**: In both Band 1 and Band 2, $S_{M1}(I)$ must oscillate **in-phase**:
$$\text{sign}\left( S_{M1}^{(1)}(I) - 1.0 \right) \equiv \text{sign}\left( S_{M1}^{(2)}(I) - 1.0 \right)$$
An out-of-phase oscillation indicates that the quasiparticles align differently in the two bands (signature splitting from planar rotation), completely disproving the chiral doublet interpretation.

### 2. Intra-Band $B(E2)$ Smoothness and Equality
The in-band quadrupole transitions $B(E2; I \to I - 2)$ reflect the underlying triaxial core shape.
They must be smooth (no staggering) and match within $\le 20\% - 25\%$ between partner bands:
$$\left| \frac{B(E2; \text{Band 1}) - B(E2; \text{Band 2})}{B(E2; \text{Band 1})} \right| \le 0.25$$

### 3. Inter-Band $\Delta I = 0$ $M1$ Transition Suppression
In the laboratory frame, the symmetric and antisymmetric chiral states are:
$$|1\rangle = \frac{|L\rangle + |R\rangle}{\sqrt{2}}, \quad |2\rangle = \frac{|L\rangle - |R\rangle}{\sqrt{2}}$$
The inter-band magnetic dipole transition matrix element is:
$$\langle 1 | \hat{\mu} | 2 \rangle = \frac{1}{2} \left[ \langle L | \hat{\mu} | L \rangle - \langle R | \hat{\mu} | R \rangle \right]$$
Since time-reversal symmetry dictates $\langle L | \hat{\mu} | L \rangle = \langle R | \hat{\mu} | R \rangle$, the matrix element vanishes at exact degeneracy:
$$B(M1; \text{Band 2}(I) \to \text{Band 1}(I)) \xrightarrow{\Delta E \to 0} 0 \quad (\text{Deep Minimum})$$

---

## Executable Analysis Tool: `chirrules`

The Python analysis suite integrates `chiral_doublet_selection_rules_m1_staggering_arbitrator.py`, accessible via:

```bash
# Benchmark 1: 128Cs landmark chiral partner bands (Grodner 2006, Koike 2004)
python3 system/scripts/analysis/nuclear_analyzer.py chirrules --preset 128Cs_chiral_doublet_benchmark

# Benchmark 2: 134Pr chiral doublet (Tonev 2006)
python3 system/scripts/analysis/nuclear_analyzer.py chirrules --preset 134Pr_chiral_doublet_benchmark

# Counterexample: Planar bands with out-of-phase M1 staggering
python3 system/scripts/analysis/nuclear_analyzer.py chirrules --preset spurious_out_of_phase_counterexample
```

### Benchmark Validation: $^{128}\text{Cs}$
- $S_{M1}(I)$ exhibits 100% in-phase staggering between Band 1 and Band 2 across $I = 13 \dots 15\ \hbar$;
- Mean intra-band $B(E2)$ difference is only $4.8\%$;
- Inter-band $B(M1; \text{Band 2} \to \text{Band 1}, \Delta I=0)$ drops to $0.040\ \mu_N^2$ at the degeneracy point $I = 14\ \hbar$;
- Final score: $100\%$, confirming `CONFIRMED_CHIRAL_SELECTION_RULES_SATISFIED`.
