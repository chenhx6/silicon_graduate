# AMR core-polarization/shears-cutoff calculation

Command:

```text
python3 amr_core_polarization_shears_cutoff.py
```

## Result

The exchange phase for two identical fermions in one half-integer-j orbit is
`(-1)^(2j-J)`.  Antisymmetry therefore leaves even pair spins.  The selected
single-j subspace has `Jp,max=8` for `pi(g9/2)^-2` and `Jn,max=10` for
`nu(h11/2)^2`, hence `J_val,max=18 hbar`.  Treating the four particles as
four freely aligned classical vectors would give 20 hbar and violates this
finite-j pair truncation.

For the 110Cd-like parameters, the stationary solution reaches the valence
endpoint at `I_sat=26.0167 hbar`.  At `I=26`, the calculation gives

```text
theta = 3.3686 deg, J_val = 17.9922 hbar, R_core = 8.0078 hbar
B_shears_only = 2.42e-8 e^2 b^2
B_total = 0.09009 e^2 b^2
```

At `I=26.5` and above the valence coordinate is pinned at 18 hbar; the core
then takes the entire incremental spin.  This explicitly separates the
finite-j cutoff from the core angular-momentum tail.

The 110Cd-like high-spin E2 plateau is `0.1138, 0.1016, 0.0901, 0.0900
e^2 b^2` at `I=22,24,26,28`.  The first two values retain a small coherent
shears amplitude, and the last two are essentially the imposed core amplitude
`Q_core^2=0.09 e^2 b^2`.  The pure shears term itself tends to zero.

The finite-core trajectory delays closure.  At `I=16`, it gives
`theta=90.97 deg` and `dtheta/dI=-5.54 deg/hbar`; the hard pure-shears
reference gives `theta=54.53 deg` and `-13.90 deg/hbar`.  The `J_core` scan
shows the slope magnitude falling from `13.73` to `4.58 deg/hbar` as
`J_core` rises from `0.1` to `30 hbar^2/MeV`.

Using the model energy differences, the 110Cd-like `J^(2)/B(E2)` values at
`I=16,18,20,22,24,26` are approximately
`335.7, 335.2, 342.4, 356.5, 377.6, 285.3
hbar^2 MeV^-1 (e^2 b^2)^-1`.  The endpoint value is a finite-difference point
that straddles the valence pinning kink; it should not be read as a smooth
microscopic derivative.

## Interpretation boundary

The calculation supports a mechanism-level statement: a finite core inertia
adds the term `(J_core/J_val,max)V''` to `dI/dx`, so the same spin increment
produces less shears closure; the residual core quadrupole amplitude then keeps
`B(E2)` finite after the shears factor has collapsed.  The values of `a`, `b`,
`Q_shears`, and `Q_core` are effective demonstration parameters.  They are not
an experimental decomposition of the Roy lifetimes, and the 104Pd rows are not
a new source extraction.  Configuration mixing, pairing, deformation
evolution, side feeding, and phase changes can all alter the plateau.

See `parameters.json`, `results.json`, and the two CSV diagnostics for the
complete reproducible calculation.
