# Chapter 2: Theory of Wobbling Motion in Triaxial Nuclei

**Author**: Stefan Frauendorf | **Source**: `raw/books/Chirality and Wobbling in Atomic Nuclei.pdf`
**Physical PDF Pages**: pp. 43–80 (Printed pp. 24–61)

---

## 1. Classical Asymmetric Rotor and Separatrix Topology

Frauendorf establishes the microscopic foundations of nuclear wobbling by contrasting classical rigid-body dynamics with quantum particle-rotor dynamics.

### 1.1 The Intermediate-Axis Instability
For an asymmetric top with moments of inertia $\mathcal{J}_1 < \mathcal{J}_2 < \mathcal{J}_3$:
- Euler equations prove that steady rotation around the minimum ($\mathcal{J}_1$) or maximum ($\mathcal{J}_3$) axis is dynamically stable;
- Steady rotation around the intermediate axis ($\mathcal{J}_2$) is **unconditionally unstable**;
- The classical phase space contains an intermediate-axis separatrix ($2 E \mathcal{J}_2 = M^2$) separating precessional orbits around axis 1 from orbits around axis 3.

### 1.2 Quantum Harmonic Wobbling in Even-Even Nuclei
In quantum mechanics, small-amplitude precession around the principal axis of largest moment of inertia ($\mathcal{J}_3$) produces harmonic wobbling states characterized by phonon quantum number $n_w = 0, 1, 2, \dots$:
$$E(I, n_w) = \frac{\hbar^2 I(I+1)}{2\mathcal{J}_3} + \hbar\omega_w \left( n_w + \frac{1}{2} \right),$$
where the wobbling frequency is given by:
$$\hbar\omega_w = I \sqrt{\left(\frac{1}{\mathcal{J}_1} - \frac{1}{\mathcal{J}_3}\right)\left(\frac{1}{\mathcal{J}_2} - \frac{1}{\mathcal{J}_3}\right)}.$$

---

## 2. Odd-$A$ Particle-Rotor Wobbling: TW vs LW vs FM

When an odd quasiparticle with angular momentum $\vec{j}$ couples to the triaxial core, the Hamiltonian is:
$$H = \sum_{k=1}^3 \frac{(I_k - j_k)^2}{2\mathcal{J}_k} + V_{\text{qp}}.$$
Frauendorf classifies three distinct regimes:

1. **Transverse Wobbling (TW)**:
   - Occurs when the quasiparticle angular momentum $\vec{j}$ aligns along the short axis ($s$, axis 1), while collective rotation $\vec{R}$ occurs around the intermediate axis ($m$, axis 2);
   - Because the particle alignment stabilizes the rotation around axis 2, the effective potential well steepens as spin $I$ increases;
   - **Signature**: The wobbling frequency **decreases with spin**:
     $$\frac{d\hbar\omega_w}{dI} < 0.$$
   - Connecting transitions: $n_w = 1 \to n_w = 0$ interband transitions are strongly enhanced $E2$ crossovers with large mixing ratio $|\delta| \gg 1$.

2. **Longitudinal Wobbling (LW)**:
   - Occurs when the quasiparticle aligns along the same axis as the collective rotation vector;
   - **Signature**: The wobbling frequency **increases with spin**:
     $$\frac{d\hbar\omega_w}{dI} > 0.$$

3. **Full Wobbling (FM)**:
   - High-spin limit where the core angular momentum vastly exceeds the particle angular momentum ($R \gg j$), restoring the symmetric even-even rotor wobbling frequency.

---

## 3. The $^{135}\text{Pr}$ Controversy and $\gamma$-Softness Boundary

- Frauendorf analyzes the Gammasphere claim of transverse wobbling in $^{135}\text{Pr}$ (Matta 2015, Sensharma 2020);
- Points out that while PTRM fits could reproduce the energy spacing, the experimental proof hinges entirely on whether the $747.5\text{ keV}$ transition is predominantly $E2$ or $M1$;
- Explains that in soft nuclei ($\gamma$-soft), zero-point fluctuations $\Delta\gamma \sim 15^\circ - 20^\circ$ wash out the triaxial energy minimum, transforming wobbling phonons into anharmonic $\gamma$-vibrational excursions.
