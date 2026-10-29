# Odd-A octupole transfer surrogate

This worker contains a reproducible, deliberately conditional model for the
zero-phonon spectroscopic strength and core-polarization content of opposite
parity particle-vibration blocks. It is a Nilsson-style two-level surrogate,
not a production DWBA, blocked-HFB, or particle-vibration fit.

## Run

```bash
python3 odd_a_spectroscopic_factors.py
```

The script writes:

- `spectroscopic_factors.csv`: positive and negative parity eigenstates for
  the neutron `f7/2-i13/2` and proton `d5/2-h11/2` octupole-driving pairs;
- `neutron_number_evolution.csv`: graph-ready `beta3`, `omega3`, direct
  spectroscopic strength, phonon content, and parity asymmetry for Ba-like
  (`N=82..96`) and Ra-like (`N=132..142`) scans;
- `results.json`: equations, assumptions, validation and evidence boundary.

For a 0+ target core, the reduced transfer amplitude is represented by the
zero-phonon coefficient `C_direct`, so the reported conditional factor is
`S_0plus_direct = |C_direct|^2`. The complementary coefficient is a
core-polarization proxy. Absolute `(d,p)`, `(p,d)` or `(d,t)` cross sections
still require a reaction calculation:

```text
dSigma/dOmega = C2S * (dSigma/dOmega)_DWBA
```

The Wiki currently contains evaluated 225Ra/225Ac level and E1 records and
odd-Ba particle–phonon calculations, but no state-resolved 225Ra/225Ac
transfer angular distributions, DWBA normalizations, or magnetic moments.
Consequently the numerical scan is a mechanism diagnostic and sensitivity
map, not an experimental extraction.
