# AMR microscopic quadrupole restoring constant

Run:

```bash
python3 amr_restoring_constant.py
```

The model starts from `V_2 = -chi_2 Q_2·Q_2` and evaluates the exchange-even
particle-hole quadrupole channel.  With equal proton and neutron blade weights,
one normalized MR scissors channel has

`-chi_2 q_p q_n P_2(cos(theta)) = const + (3/2) chi_2 q_p q_n theta^2 + O(theta^4)`.

The four-blade AMR exchange-even sum has two equivalent channels after the
collective-coordinate projection, giving
`C_AMR = 3 chi_2 q_p q_n = 2 C_MR`.
The direct four-versus-two channel count is included in the JSON output.

`J2` is calculated only where the centered finite difference is positive:
`J2 = 4 / Delta E_gamma` with energies in MeV.  The reported `chi2_proxy` uses
`C_proxy = 0.5/(J2 theta_ref^2)`, theta_ref=0.5 rad, and is explicitly a
model-dependent scale proxy.  It is not a unique microscopic extraction.

Outputs: `j2_chi2_scan.csv`, `chi2_restoring_scan.csv`,
`amr_restoring_constant.json`, and `restoring_constant_scan.svg`.
