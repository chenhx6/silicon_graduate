---
type: concept
title: "Self-consistent 3D TAC with pairing gap equation and chiral restoration"
aliases: [tac-with-pairing, 3d-tac-cap-quenching, chiral-restoration-spin-evolution, tac-bcs-pairing-equation]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [triaxiality, tilted-axis-cranking, 3d-tac, bcs-pairing, coriolis-anti-pairing, chiral-restoration, chiral-bifurcation, spontaneous-symmetry-breaking]
---

# Self-consistent 3D TAC with pairing gap equation and chiral restoration

## Definition

### Definition and Microscopic Framework

Three-Dimensional Tilted Axis Cranking (3D TAC) describes the spontaneous breaking of planar symmetry when the total angular momentum of an atomic nucleus tilts out of the three principal planes of the triaxial ellipsoid (Frauendorf & Meng 1997; Frauendorf 2001; Zhao in Petrache CRC 2025 Ch. 9).

In actual nuclei, rotation does not occur in an unperturbed single-particle potential: **it couples to the pairing field, which is dynamically quenched by the Coriolis Anti-Pairing (CAP) effect**:

1. **Microscopic TAC Routhian with Pairing**:
   $$h_{\text{TAC}} = h_{\text{sp}}(\beta_2, \gamma) - \vec{\omega} \cdot \vec{j} - \Delta (\hat{P}^\dagger + \hat{P}) - \lambda \hat{N}$$
   with tilted rotational frequency vector:
   $$\vec{\omega} = \omega (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$$

2. **Coriolis Anti-Pairing (CAP) & Pauli Blocking**:
   Baseline pairing gap: $\Delta_0 \approx 12.0 / \sqrt{A}\text{ MeV}$.
   In odd-odd or multi-quasiparticle configurations, odd valence nucleons block pairing channels, reducing the zero-frequency gap to $\Delta_{\text{eff}}(0) = f_{\text{block}} \Delta_0$ ($f_{\text{block}} \approx 0.50 - 0.60$).
   As the nucleus accelerates to rotational frequency $\omega \approx J / \mathcal{J}_m$, the Coriolis force uncouples time-reversed Cooper pairs:
   $$\Delta(\omega) = \Delta_{\text{eff}}(0) \sqrt{\max\left(0.0, 1.0 - \left(\frac{\omega}{\omega_c}\right)^2\right)}$$
   where $\omega_c \approx 0.28\text{ MeV}/\hbar$ is the critical unpairing frequency.

3. **Pairing-Dependent Moments of Inertia**:
   As pairing quenches, the nuclear moments of inertia expand towards the rigid-body limit:
   $$\mathcal{J}_k(\Delta) = \mathcal{J}_{k, \text{rig}} \left[ 1.0 - g_k \frac{\Delta(J)}{\Delta_0} \right] \quad (k \in \{s, m, l\})$$
   where intermediate-axis inertia is dominant: $\mathcal{J}_m > \mathcal{J}_s, \mathcal{J}_l$.

---

## Orientation Energy Surface and Chiral Evolution

At total angular momentum $J$, the orientation energy on the unit sphere $(\theta, \phi)$ is:
$$E(J; \theta, \phi) = \frac{(J\sin\theta\cos\phi - j_\pi)^2}{2\mathcal{J}_s(\Delta)} + \frac{(J\sin\theta\sin\phi)^2}{2\mathcal{J}_m(\Delta)} + \frac{(J\cos\theta - j_\nu)^2}{2\mathcal{J}_l(\Delta)}$$

### Three-Phase Chiral Evolution Across Spin

1. **Planar Rotation Phase ($J < J_{\text{crit}}$)**:
   At low spins, core rotation is weak. The total spin vector resides strictly within the principal plane $(\phi_0 = 0^\circ)$, the planar barrier is zero, and $\mathcal{V}_{\text{chiral}} = 0$;
2. **Aplanar Chiral Bifurcation Phase ($J_{\text{crit}} \le J \le J_{\text{term}}$)**:
   At critical spin $J_{\text{crit}}$, the planar state becomes an unstable saddle point, bifurcating into two degenerate aplanar minima at $\pm\phi_0$ ($\phi_0 \sim 20^\circ - 45^\circ$). Discrete $\mathcal{T}\mathcal{R}_y(\pi)$ symmetry is spontaneously broken, creating degenerate left- and right-handed chiral states separated by an energy barrier:
   $$\Delta E_{\text{barrier}}(J) = E_{\text{planar}}(J) - E_{\text{chiral}}(J) > 0\text{ keV}$$
3. **Chiral Restoration Phase ($J > J_{\text{term}}$)**:
   At very high spins, the colossal centrifugal energy of the intermediate axis ($J_m^2 / (2\mathcal{J}_m)$) overwhelms single-particle alignments. The single particles are pulled toward the intermediate axis, causing the aplanar barrier to collapse back to zero: **chiral restoration**.

---

## Canonical Source and Model Benchmarks

- **$^{134}\text{Pr}$ Chiral Tripod ($\pi h_{11/2} \otimes \nu h_{11/2}^{-1}$)**:
  - $J_{\text{crit}} = 16.0\ \hbar$ (onset of chiral bifurcation with $\phi = 14.0^\circ$, barrier $= 1.8\text{ keV}$);
  - At $J = 18.0\ \hbar$, the supplied model gives an aplanar
    configuration with $\phi = 33.0^\circ$, barrier $=69.9\text{ keV}$ and
    $\mathcal{V}_{\text{chiral}}=0.498$; these are model outputs, not direct
    measurements;
  - At $J = 22.0\ \hbar$, deep chiral wells with barrier exceeding $500\text{ keV}$.
- **$^{136}\text{Nd}$ 4-Quasiparticle State**:
  - Enhanced single-particle alignments ($j_\pi = 8.0, j_\nu = 8.0$) shift the
    model bifurcation threshold to $J_{\text{crit}}\approx21.0\hbar$; this is a
    conditional stability result for the supplied Hamiltonian.

---


## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。

## Sources

### 参考文献与交叉引用


- **Zhao, P. W.**: *Time-Dependent Covariant Density Functional Theory for Nuclear Chirality*, in *Chirality and Wobbling in Atomic Nuclei*, CRC Press (2025), Chapter 9, PDF pp. 204–221.
- **Chen, Q. B. et al.**: *CDFT + Particle Rotor Model for Multiple Chiral Doublets*, in *Chirality and Wobbling in Atomic Nuclei*, CRC Press (2025), Chapter 10, PDF pp. 222–238.
- **Frauendorf, S. & Meng, J.**: *Tilted rotation of triaxial nuclei*, Nucl. Phys. A 617, 131–143 (1997).
- **Frauendorf, S.**: *Spontaneous symmetry breaking in rotating nuclei*, Rev. Mod. Phys. 73, 463–514 (2001).


## Necessary Assumptions

微观平均场假定核子在有效单体势中运动，通过剩余相互作用自洽诱发四极形变与集体转动。


## Discriminating Observables

激发能量级间距、跃迁多极性比值与电磁约化跃迁几率是关键鉴别观测量。


## Supporting Evidence

在束伽马谱学实验测定的角分布、DCO比值与能级寿命提供直接实证。
