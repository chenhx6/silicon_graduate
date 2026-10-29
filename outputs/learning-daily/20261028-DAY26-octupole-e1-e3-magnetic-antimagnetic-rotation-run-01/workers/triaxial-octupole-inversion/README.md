# Triaxial–octupole signature-inversion toy calculation

This directory contains a self-contained NumPy calculation for the mechanism
note `knowledge/research-notes/triaxial-octupole-signature-inversion-coriolis-boundary.md`.
It is a controlled synthetic model; its parameters are not fitted to 130Cs,
131Ba, 133Ce or 225Ra data.

## Model

For each half-integer spin (I), the basis is

`|I m_I> ⊗ |j m_j=11/2> ⊗ |orbital parity> ⊗ |octupole well>`.

The Hamiltonian is

```text
H = sum_k (I_k - j_k)^2/(2 J_k)
    + eps sigma_z + Delta tau_x + kappa3 beta3 sigma_x tau_z
    + H_sp + V_pn(I, gamma, beta3) U_signature.
```

The first line contains the Coriolis cross term
`-sum_k I_k j_k/J_k`, equivalent to the `-2 R_k j_k/(2 J_k)` cross term in
the rotor-plus-particle expansion. `P = sigma_z tau_x` is the conserved
laboratory parity, and `U_signature = exp[-i pi (I_x+j_x)]`. The last term is
an explicitly labelled effective residual proton–neutron interaction used to
make the low-spin inversion window visible in a finite toy space.

## Reproduction

```bash
OPENBLAS_NUM_THREADS=4 OMP_NUM_THREADS=4 \
  python3 triaxial_octupole_signature_inversion.py
```

The script writes:

- `signature-inversion-scan.csv`: sector energies, signature/parity
  splittings, rotational residuals and alignment diagnostics for five
  `(gamma, beta3)` cases;
- `signature-inversion-scan.json`: parameters, inversion-spin summary and
  numerical checks.

The reported inversion-spin markers are `I=19/2` for the reference,
`gamma=20°` and weak-octupole cases, and `I=21/2` for the stronger
octupole cases in this parameterization. These are model outputs, not
experimental assignments.

The JSON verification checks Hermiticity, `[H,P]=0`, `[H,U_signature]=0`,
and consistency of the eigenvalues before and after explicit Hermitian
symmetrization. All are below `1e-14` in the supplied run.
