# QSM Racah benchmark

Run from the repository root:

```bash
python3 outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/quantum-shears/qsm_racah_vs_semiclassical.py
```

The script has no third party dependency. It evaluates the Wigner 6j symbol
with the Racah factorial sum, checks the closed form for
`|<(jp jn) I-1 || jp || (jp jn) I>|^2`, writes one CSV table and one JSON
summary, and compares the exact fixed-j rate with the supplied
Macchiavelli shears expression.

The symmetric `jp=jn=11/2` case is listed on its mathematically allowed
integer-I ladder (`I=5,...,11`). Two half-integer blades cannot couple to a
half-integer total I, so the requested `I=11/2,...,23/2` window is supplied as
the separate `jp=11/2, jn=10` particle-hole-like control. The `I=31/2` row is
an endpoint control: the classical j-length expression is zero while the
finite-j quantum rate is `1.708123 mu_N^2` for `Delta g=1.42`.

The interior ratio has the exact algebraic form

```text
B_quantum/B_classical = 2I/(2I+1)
                       * (((jp+jn+1)^2-I^2)/((jp+jn)^2-I^2))
```

and tends to one in an interior large-j scaling limit. The endpoint limit is
non-uniform because the classical denominator vanishes. These are model
results, not experimental transition strengths.

## Direct literature locators

- Clark and Macchiavelli, *Annu. Rev. Nucl. Part. Sci.* **50**, 1–36 (2000),
  PDF p.15, Sec.4.4, Eqs.(5)–(7): finite-j angle prescription and
  semiclassical `B(M1)` geometry.
- Frauendorf, *Rev. Mod. Phys.* **73**, 463–514 (2001), PDF pp.487–488,
  Sec.IV.A: high-j current-loop/shears interpretation and transverse magnetic
  moment.
- Frauendorf, *Rev. Mod. Phys.* **73**, 463–514 (2001), PDF pp.499–502,
  Sec.VIII: laboratory quantization/projection and the limits of a
  semiclassical TAC description.

The phrase “operator renormalization” in the associated research note refers
to finite-j recoupling of the transition strength. The calculation does not
include effective-g renormalization, core rotation, pairing or configuration
mixing.
