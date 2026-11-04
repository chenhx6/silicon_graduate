# Glossary: Bohr & Mottelson Nuclear Structure Terminology

This glossary cross-references foundational nuclear structure concepts from Bohr & Mottelson Vols. I & II, establishing standardized Chinese and English terminology and mathematical notations.

---

## 1. Symmetry and Conservation Laws (对称性与守恒律)

- **Time-Reversal Invariance (时间反演不变性)**: An anti-unitary symmetry operation $\mathcal{T} = U K_0$ satisfying $\mathcal{T} i \mathcal{T}^{-1} = -i$. For a system of $A$ nucleons with total angular momentum $J$, $\mathcal{T}^2 = (-1)^{2J} = (-1)^A$.
- **Kramers Degeneracy (克拉默斯简并)**: The exact twofold energy degeneracy of single-particle states in an odd-fermion system under a time-reversal-invariant Hamiltonian ($\mathcal{T}^2 = -1$). In deformed nuclei, states with $+K$ and $-K$ (or $+\Omega$ and $-\Omega$) are degenerate in energy.
- **Isospin (同位旋)**: The $SU(2)$ symmetry algebra describing the charge independence of nuclear forces, where proton ($t_z = -1/2$) and neutron ($t_z = +1/2$) form an isospin doublet ($t=1/2$).
- **Morpurgo Selection Rule (莫珀戈 $E1$ 选择定则)**: The strict vanishing of electric dipole transitions with $\Delta T = 0$ in self-conjugate nuclei ($N=Z$, $T_z=0$) due to the exact cancellation of proton and neutron effective dipole charges ($e_{\text{IS}} = (N-Z)/(2A)e = 0$).
- **Signature (旋称)**: The quantum number associated with rotation by $180^\circ$ around an axis perpendicular to the symmetry axis: $\mathcal{R}_x(\pi) = e^{-i \pi I_x}$, with eigenvalue $r = e^{-i \pi \alpha} = (-1)^I$.

---

## 2. Mean Field and Single-Particle Motion (平均场与单粒子运动)

- **Fermi Gas Model (费米气体模型)**: A degenerate zero-temperature Fermi liquid model with saturated density $\rho_0 \a0.16\text{ fm}^{-3}$, Fermi momentum $k_F \a1.36\text{ fm}^{-1}$, and Fermi kinetic energy $\epsilon_F \approx 38.5\text{ MeV}$.
- **Incompressibility (不可压缩系数 $K_\infty$)**: The curvature of the nuclear matter equation of state at saturation: $K_\infty = 9 \rho_0^2 \frac{d^2(E/A)}{d\rho^2} \approx 200 - 250\text{ MeV}$.
- **Spin-Orbit Potential (自旋-轨道势)**: The surface-peaked vector potential $V_{ls}(r) \frac{1}{r} \frac{dV}{dr} (\vec{l}\cdot\vec{s})$ responsible for the nuclear magic numbers (28, 50, 82, 126).
- **Nilsson Asymptotic Quantum Numbers (Nilsson 渐近量子数 $[N n_z \Lambda \Omega]$)**:
  - $N$: Principal oscillator shell quantum number;
  - $n_z$: Number of oscillator quanta along the deformation symmetry axis $z$;
  - $\Lambda$: Component of orbital angular momentum along the symmetry axis ($\Lambda = \Omega - \Sigma$);
  - $\Omega$: Component of total single-particle angular momentum along the symmetry axis ($\Omega = K$ for a single particle).

---

## 3. Collective Rotation and Deformation (集体转动与形变)

- **Adiabatic Decoupling (绝热解耦)**: The factorization of the total nuclear wave function into a rotational Wigner $D$-function and an intrinsic wave function $\chi_K$.
- **Moment of Inertia (转动惯量 $\mathcal{J}$)**:
  - Rigid body limit: $\mathcal{J}_{\text{rig}} = \frac{2}{5} M R_0^2 (1 + \frac{1}{3} \delta)$;
  - Irrotational hydrodynamics: $\mathcal{J}_{\text{irrot}} \propto \beta_2^2 \sin^2(\gamma - \frac{2\pi}{3} k)$;
  - Experimental values in deformed nuclei: $\mathcal{J}_{\text{exp}} \a0.3 - 0.5\ \mathcal{J}_{\text{rig}}$, suppressed by pairing correlations.
- **Coriolis Coupling (科里奥利耦合)**: The kinematic coupling between collective rotation and valence quasiparticle angular momentum in the rotating frame: $H_{\text{cor}} = - \frac{\hbar^2}{\mathcal{J}} (\vec{I}\cdot\vec{j})$.
- **Decoupling Parameter ($a$, 解耦参数)**: The diagonal Coriolis matrix element in a $K=1/2$ band, shifting alternate spin states by $a (-1)^{I+1/2}(I+1/2)$.
- **Backbending (回弯现象)**: The sudden increase of the moment of inertia caused by the alignment of a pair of high-$j$ quasiparticles (e.g. $\pi h_{11/2}^2$ or $\nu i_{13/2}^2$) along the rotation axis.

---

## 4. Electromagnetic Transitions and Sum Rules (电磁跃迁与求和规则)

- **Alaga Rules (阿拉加定则)**: Geometrical branching ratios for transitions between states belonging to pure rotational bands, given by Clebsch-Gordan coefficient squares:
  $$\frac{B(E2; I_i K_i \to I_{f1} K_f)}{B(E2; I_i K_i \to I_{f2} K_f)} = \frac{\langle I_i K_i 2 \Delta K | I_{f1} K_f \rangle^2}{\langle I_i K_i 2 \Delta K | I_{f2} K_f \rangle^2}.$$
- **Mikhailov Plot (米哈伊洛夫图)**: A linear representation plotting the reduced matrix element divided by the Clebsch-Gordan coefficient versus $[I_f(I_f+1) - I_i(I_i+1)]$ to extract non-adiabatic Coriolis mixing matrix elements.
- **$K$-Hindrance (K 禁戒)**: The systematic suppression of transitions where the change in $K$-quantum number exceeds the multipole order: $\Delta K > \lambda$, with degree of hindrance $\nu = \Delta K - \lambda$.
- **Energy-Weighted Sum Rule (EWSR, 能量加权求和规则)**:
  $$S(E\lambda) = \sum_n (E_n - E_0) B(E\lambda; 0 \to n) = \frac{\lambda (2\lambda+1)^2}{8\pi} \frac{\hbar^2}{M} Z R_0^{2\lambda-2} e^2.$$
