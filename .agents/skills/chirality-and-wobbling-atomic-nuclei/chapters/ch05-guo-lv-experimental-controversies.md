# Chapter 5: Experimental In-Beam Spectroscopy and Methodological Controversies

**Authors**: Song Guo and Bing-Feng Lv | **Source**: `raw/books/Chirality and Wobbling in Atomic Nuclei.pdf`
**Physical PDF Pages**: pp. 110–126 (Printed pp. 91–107)

---

## 1. Experimental Methodology: DCO, ADO, and Polarimetry

Guo and Lv review in-beam $\gamma$-ray spectroscopic techniques used to extract multipole mixing ratios $\delta(E2/M1)$ and transition multipolarities in heavy-ion fusion-evaporation reactions.

### 1.1 Directional Correlation from Oriented States (DCO)
- Measured ratio of coincidence counts at two detector angles $(\theta_1, \theta_2)$ gated on a known stretched transition:
  $$R_{\text{DCO}} = \frac{I_\gamma(\theta_1, \text{gated at } \theta_2)}{I_\gamma(\theta_2, \text{gated at } \theta_1)}.$$
- For a stretched $E2$ gate at $\theta_2 \approx 90^\circ$ and unassigned transition at $\theta_1 \a30^\circ$:
  - Pure dipole ($\Delta I = 1, \delta = 0$): $R_{\text{DCO}} \a0.5 - 0.6$;
  - Pure quadrupole ($\Delta I = 2, \delta = 0$): $R_{\text{DCO}} \a1.0$;
  - Mixed $\Delta I = 1$ ($M1 + E2$): $R_{\text{DCO}}$ varies continuously from $0.3$ to $1.5$ with quadratic dependence on $\delta$.

### 1.2 The Quadratic Ambiguity and Dual-Root Degeneracy
The primary source of experimental controversy is the quadratic structure of $R_{\text{DCO}}(\delta)$ and $a_2(\delta)$:
$$a_2(\delta) = \frac{R_{11} + 2 \delta R_{12} + \delta^2 R_{22}}{1 + \delta^2} = a_2^{\text{exp}}.$$
Because $(R_{22} - a_2)\delta^2 + 2 R_{12}\delta + (R_{20} - a_2) = 0$ has two real roots whenever the discriminant is positive, directional measurements **cannot distinguish** between:
- **Root 1 (Wobbling solution)**: Large $|\delta| \sim -2.0$ ($75\% - 85\% E2$);
- **Root 2 (Signature partner solution)**: Small $|\delta| \sim -0.3$ to $-0.5$ ($75\% - 85\% M1$).

---

## 2. Resolving the $^{135}\text{Pr}$ Transverse Wobbling Controversy

Guo and Lv recount the decisive resolution of the $^{135}\text{Pr}$ debate:
1. **The Gammasphere Claim (Matta 2015, Sensharma 2020)**:
   Gammasphere measured $a_2 = -0.42(3)$ for the $747.5\text{ keV}$ line ($17/2^+ \to 15/2^+$) connecting Band 2 to Band 1. Adopting Root 1 ($\delta = -2.14(20)$), they claimed the first observation of transverse wobbling in a normal-deformed nucleus.
2. **The JUROGAM II Falsification (Lv 2022)**:
   Lv et al. deployed the JUROGAM II array equipped with Clover Compton polarimeters to measure the linear polarization asymmetry $P$:
   $$P(\delta) = \frac{3 \delta^2 R_{22} - 2\sqrt{6} \delta R_{12} - R_{20}}{(2 - \delta^2) R_{20} + 1 + \delta^2}.$$
   - Root 1 predicts $P_{\text{calc}} = +0.34$;
   - Root 2 predicts $P_{\text{calc}} = -0.22$;
   - Experimental measurement yielded:
     $$P_{\text{exp}} = -0.21 \pm 0.04.$$
   - Profile likelihood analysis rejects Root 1 at **$11.1\sigma$ ($\Delta\chi^2 = 122.3$)**, establishing that the $747.5\text{ keV}$ transition is $81.9\%\ M1$-dominated, characteristic of an unfavored signature partner band undergoing tilted precession (TiP).

---

## 3. General Methodological Rules

- **Rule 1**: Never publish a claim of wobbling motion without measuring linear polarization or internal conversion coefficients to break the dual-root degeneracy;
- **Rule 2**: Always check the physical feasibility of both roots in terms of single-particle Weisskopf estimates and pairing gaps;
- **Rule 3**: In $\gamma$-soft nuclei, investigate alternative non-axial mechanisms (tilted precession, $\gamma$-vibrational core coupling) before asserting rigid triaxiality.
