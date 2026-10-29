# Chiral–AMR four-blade 3D-TAC bifurcation worker

`chiral_amr_3dtac_bifurcation.py` implements a deterministic constrained
particle–rotor Routhian for two proton-hole and two neutron-particle mirror
blades.  The net blade vectors are

\[
\mathbf j_p=(j_p,0,0),\qquad \mathbf j_n=(0,0,j_n),\qquad
\mathbf R=\mathbf I-\mathbf j_p-\mathbf j_n,
\]

and the diagnostic chirality is
`chi_g = j_p · (j_n × R) = -j_p j_n I_m`.  The scan adds an even
intermediate-axis drive `-kappa_m omega_m² I_m²/(2 I²)`.  Its evenness is the
deliberate symmetry condition for a pitchfork: the two signs of `I_m` remain
degenerate.  A signed linear external field would bias one handedness and is
not a spontaneous bifurcation.

Run:

```bash
python3 chiral_amr_3dtac_bifurcation.py
```

Outputs are `bifurcation_scan.csv`, `bifurcation_scan.json`, and, when
matplotlib is available, `bifurcation_diagram.svg`.  `B_M1_proxy`,
`B_E2_proxy`, and `partner_splitting_proxy_MeV` are dimensionless or
model-scaled diagnostics.  They are not measured transition strengths and do
not establish chirality in `106Ag` or AMR in `106Cd`.

The relevant evidence boundary is recorded in
`knowledge/research-notes/chiral-amr-four-blade-3dtac-topological-bifurcation.md`.
