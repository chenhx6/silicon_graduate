# Cline octupole invariant worker

Run:

```bash
python3 cline_octupole_invariants.py --out-dir .
```

The JSON and CSV are derived from the central values in the Wiki source pages:

- `knowledge/sources/cline-1986-nuclear-shapes-coulomb-excitation.md` (PDF pp.697--700): finite closure, higher-order missing-strength and operator caveats;
- `knowledge/sources/bucher-2016-144ba-direct-octupole.md` (PDF pp.3--4, Table I);
- `knowledge/sources/bucher-2017-146ba-direct-octupole.md` (PDF pp.2--3, Table I);
- `knowledge/sources/gaffney-2013-pear-shaped-rn-ra.md` (PDF pp.2--4, Tables 1--2);
- ENSDF 224Ra adopted levels (`raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/nndc-224ra-adopted-cluster-20261029.pdf`, pp.1--2).

The script is a transparent algebraic control. It does not claim a complete
GOSIA fit or a measured closure sum when the source supplies only one E3 link.
