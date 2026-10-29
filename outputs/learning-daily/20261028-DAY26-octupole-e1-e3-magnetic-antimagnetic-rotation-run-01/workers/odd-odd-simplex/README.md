# Odd-odd octupole simplex/signature coupling

This worker is a reproducible phenomenological calculation for integer-spin odd-odd nuclei. It scans synthetic four-branch spectra for `220Fr`, `222Fr` and `224Ac`, evaluates the requested two-particle Coriolis operator in a fixed-`M` product basis, and writes E1/E2/M1 selection-rule strengths.

Run from this directory:

```text
python3 odd_odd_simplex_coupling.py
```

Generated files are `four_band_spectrum.csv`, `staggering.csv`, `transition_strengths.csv`, `results.json`, `four_band_spectrum.svg` and `four_band_spectrum.png`.

The four-state Hamiltonian uses `(p,r)` labels with `p=+/-1` and `r=+/-1`. For odd-odd integer-spin sequences, `s=p*r` is a real simplex label. The requested phase convention `p exp(-i pi I)` is recorded separately in the JSON output because signature phase conventions can differ by axis and intrinsic-state gauge. The simplex-preserving off-diagonal coupling connects `(p,r)` to `(-p,-r)`.

The decoupling term is `(-1)^I r (I+1/2)(a_p(p)+a_n(p))`. Effective `a_p` and `a_n` become parity dependent through a two-level octupole mixing angle. The values of `A`, `beta3`, `D0`, `Q0`, decoupling constants and residual proton-neutron coupling are illustrative, and are not fits to the named nuclei.

The explicit Coriolis matrix follows

`H_cor = -A[(I_+ j_p- + I_- j_p+) + (j_p+ j_n- + j_p- j_n+)]`

and reports Hermiticity checks. The spherical pairs `pi h9/2-f7/2` and `nu g9/2-i11/2` named in the task have the same spherical parity; they can alter effective decoupling but are not by themselves opposite-parity octupole drivers. The true `Delta l=Delta j=3` examples used for the octupole boundary are `pi f7/2-i13/2` and `nu g9/2-j15/2`.

Grounded evidence is limited to the local Butler–Nazarewicz 1996 review and Gaffney et al. 2013 adjacent-mass Coulomb-excitation source. A verified absolute-lifetime four-band data set for `220,222Fr` or `224Ac` was not available in the local evidence layer, so no output row is an experimental claim.
