# Additional controls for the focused manuscript revision

The original `../manifest.json` and all 45 registered files are preserved.
This directory adds the three completed checks used by the revised manuscript.
They answer one question: how selected-spin convergence and angular coupling
enter a quadrupole shape interpretation, and where the Ba application stops.
None of the new packages fits parameters, selects a more favorable operator,
or substitutes an experimental energy into an unrelated model branch.

| Package | Scientific scope | Reproduction entry |
|---|---|---|
| [rigid-control](rigid-control/README.md) | Fixed20° charge tensor; all five field strengths and20 proxy outcomes | `rigid-control/reproduce.py` |
| [isomer-check](isomer-check/README.md) | All 28 E2 strengths,14 modeled photon-rate sums and84 open branches | `isomer-check/reproduce.py` |
| [source-replay](source-replay/REPLAY.md) | All 12 frozen135/137Ba plotted source energies and fixed-kernel comparison | See `source-replay/REPLAY.md` |

Each package contains unchanged scientific producers or an explicitly identified
adapter, numerical dependencies, frozen inputs/results, hashes and the actual
independent replay record. Follow its documented command and use a new output
directory. Python, NumPy and SciPy are external runtime dependencies.

These are calculated data and published numerical constraints, not newly
measured nuclear observations. Original PDFs, textbook pages, author programs,
private iThemba data and credentials are not included. Historical raw-source
hashes and source-audit statements remain declarations unless the corresponding
original is actually present and checked. In particular, re-extracting the
published source figure requires the original local PDF/archive; the numerical
comparison can be replayed using the frozen points alone.

The assembly manifest records this directory's files and links the three
separate package inventories. Their replay records have distinct meanings:
agreement with the frozen calculations validates transport of the calculation;
it does not make the model an experimentally validated description of Ba,
establish a first-in-literature result or predict journal acceptance.
