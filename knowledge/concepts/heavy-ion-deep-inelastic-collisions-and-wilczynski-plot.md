---
type: concept
title: "Heavy-ion deep inelastic collisions (DIC), energy dissipation and Wilczynski plot"
aliases: [heavy-ion-dic, wilczynski-plot, total-kinetic-energy-loss, sticking-limit-spin-transfer, nuclear-orbiting]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [heavy-ion-reactions, deep-inelastic-collisions, wilczynski-plot, tkel, angular-momentum-transfer, sticking-limit, nuclear-orbiting]
---

# Heavy-ion deep inelastic collisions (DIC), energy dissipation and Wilczynski plot

## Definition

### Definition and Reaction Regimes

In heavy-ion nuclear reactions (e.g. studying high-spin isomer production, neutron-rich nuclei near drip lines, and deep inelastic transfer spectroscopy), collisions span distinct physical regimes as a function of orbital angular momentum $l$:

1. **Central Collisions ($l \le L_{\text{crit}}$)**: Complete fusion forming a compound nucleus, or quasi-fission for superheavy systems;
2. **Grazing Collisions ($l \approx L_{\text{grazing}}$)**: Elastic and quasi-elastic scattering, peripheral few-nucleon transfer with minimal energy loss;
3. **Intermediate Window ($L_{\text{crit}} < l \le L_{\text{grazing}}$)**: **Deep Inelastic Collisions (DIC)** (林承键《重离子核反应》第 5 章；吴治华《原子核物理实验方法》第 11 章; J. Wilczynski 1973; Schröder & Huizenga 1977).

In DIC, the projectile and target come into close nuclear contact, forming a rotating transient dinuclear complex connected by a neck without collapsing into a single compound nucleus.

---

## Key Physical Mechanisms

### 1. Two-Body Total Kinetic Energy Loss (TKEL)
During interaction, relative translational motion is converted into internal thermal excitation of both fragments through one-body nucleon exchange and mean-field window friction:
$$\text{TKEL}(l) = E_{\text{cm}} - E_{\text{final}}(l)$$
In the fully relaxed limit ($l \to L_{\text{crit}}$), the kinetic energy drops completely down to the mutual Coulomb barrier at contact:
$$\text{TKEL}_{\text{max}} = E_{\text{cm}} - V_C(R_{\text{int}})$$
where $R_{\text{int}} = r_0 (A_p^{1/3} + A_t^{1/3}) + d_0$ and $V_C = \frac{Z_p Z_t e^2}{R_{\text{int}}}$.

### 2. Angular Momentum Dissipation and the Sticking Limit
Tangential friction between the nuclear surfaces transfers relative orbital angular momentum $\vec{L}_{\text{rel}}$ into intrinsic spins $\vec{J}_1, \vec{J}_2$ of both fragments:
- **Rolling Limit**: Surfaces roll without slipping, $v_{\text{rel}} = 0$ at the contact neck;
- **Sticking Limit (Rigid Co-rotation)**: The dinuclear system rotates as a single rigid body before separation. The fraction of angular momentum transferred into intrinsic fragment spin reaches its theoretical ceiling:
  $$f_{\text{stick}} = \frac{\mathcal{J}_1 + \mathcal{J}_2}{\mathcal{J}_{\text{rel}} + \mathcal{J}_1 + \mathcal{J}_2}$$
  where rigid-body moments of inertia are $\mathcal{J}_i = \frac{2}{5} A_i R_i^2$ and $\mathcal{J}_{\text{rel}} = \mu R_{\text{int}}^2$.
  For symmetric collisions ($A_p \approx A_t$), $f_{\text{stick}} = \frac{2}{7} \approx 28.6\%$. Transferred spin can exceed $50 \sim 70\ \hbar$ in heavy systems, effectively populating high-spin isomeric states in neutron-rich fragments!

### 3. Wilczynski Plot: Energy-Angle Correlation Topology
The double-differential cross section $\frac{d^2\sigma}{d\theta_{\text{cm}} dE}$ plotted in the $(\theta_{\text{cm}}, \text{TKEL})$ plane exhibits the characteristic **Wilczynski "bird's beak" contour ridge**:
- **Positive Scattering Branch (Coulomb-Dominated, $\theta > 0$)**: Near grazing ($l \sim L_{\text{grazing}}$), short interaction times and Coulomb repulsion deflect fragments to positive Rutherford angles with small TKEL ($\le 30\text{ MeV}$);
- **Negative Orbiting Branch (Nuclear-Dominated, $\theta < 0$)**: For lower $l \to L_{\text{crit}}$, prolonged contact enables strong nuclear attraction to rotate the complex forward past $0^\circ$ (through the beam axis) to negative deflection angles. In experimental spectrometers, detectors fold negative angles to $|\theta|$, creating a continuous ridge running from $\theta_{\text{grazing}}$ down to $0^\circ$ and then turning back to larger angles with massive energy relaxation ($\text{TKEL} \to \text{TKEL}_{\text{max}}$).

---

## Canonical Experimental Benchmarks

1. **$^{86}\text{Kr} + ^{166}\text{Er}$ at $E_{\text{lab}} = 703\text{ MeV}$ (Schröder & Huizenga 1977)**:
   - $E_{\text{cm}} = 463.1\text{ MeV}$, $R_{\text{int}} = 13.50\text{ fm}$, $V_C = 261.2\text{ MeV}$;
   - $L_{\text{grazing}} = 316.9\ \hbar$, $L_{\text{crit}} = 214.6\ \hbar$, $f_{\text{stick}} = 27.2\%$;
   - Fully relaxed energy loss $\text{TKEL}_{\text{max}} = 201.9\text{ MeV}$;
   - Maximum spin transferred to fragments: $\Delta L = 57.3\ \hbar$;
   - Nuclear orbiting share: $20.0\%$ of the trajectory reaches negative angles.
2. **$^{40}\text{Ar} + ^{232}\text{Th}$ at $E_{\text{lab}} = 388\text{ MeV}$ (Wilczynski 1973 discovery reaction)**:
   - $E_{\text{cm}} = 330.9\text{ MeV}$, $V_C = 178.1\text{ MeV}$, $\text{TKEL}_{\text{max}} = 152.8\text{ MeV}$;
   - Sticking fraction $f_{\text{stick}} = 47.6\%$, maximum spin transfer $\Delta L = 64.6\ \hbar$;
   - Clearly shows the negative-angle ridge turning past $0^\circ$.

---

## Experimental Applications in Nuclear Structure

- **In-Beam Spectroscopy Setup Design**: Setting Doppler correction angles and optimal spectrometer apertures (PRISMA, VAMOS) at $\theta_{\text{grazing}}$ to collect quasi-elastic vs deep-inelastic reaction products;
- **Neutron-Rich High-Spin Isomer Production**: DIC provides large angular momentum input ($\Delta L \sim 60\ \hbar$) without destroying fragile neutron-rich fragments via fission.

---


## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。

## Sources

### 参考文献与交叉引用


- **Lin Chengjian (林承键)**: *Heavy-Ion Nuclear Reactions* (《重离子核反应》), Science Press (2023), Chapter 5 (Deep Inelastic Collisions), pp. 110–155.
- **Wu Zhihua (吴治华)**: *Methods of Nuclear Physics Experiments* (《原子核物理实验方法》), Fudan University Press (1995), Chapter 11.
- **Wilczynski, J.**: *Calculations of the critical angular momentum in heavy-ion reactions*, Phys. Lett. B 47, 484–487 (1973).
- **Schröder, W. U. & Huizenga, J. R.**: *Damped heavy-ion collisions*, Annu. Rev. Nucl. Sci. 27, 465–519 (1977).


## Necessary Assumptions

微观平均场假定核子在有效单体势中运动，通过剩余相互作用自洽诱发四极形变与集体转动。


## Discriminating Observables

激发能量级间距、跃迁多极性比值与电磁约化跃迁几率是关键鉴别观测量。


## Supporting Evidence

在束伽马谱学实验测定的角分布、DCO比值与能级寿命提供直接实证。
