# Public data provenance

`zobel83_958_table1.csv` is a manually transcribed benchmark table from a
publicly accessible published paper. Redistribution and publication
authorization for the normalized copy remain pending author/license review;
it is not yet a publicly licensed release:

- source page: `knowledge/sources/zobel-1983-energy-projectile-alignment.md`;
- raw paper: `raw/papers/1983_Zobel et al_Energy and projectile dependence of nuclear alignment in fusion-evaporation reactions.pdf`;
- source locator: printed p.392 / PDF p.4, Table 1, `958.0-keV` `13/2+ -> 9/2+` column;
- quoted uncertainties: the source labels them as statistical fit errors;
- covariance: not supplied by the source and therefore not imputed as known.

The CSV is a normalized public benchmark table, not a copy of the raw spectra or
event data. Any article result must distinguish this table-level analysis from
an event-level reanalysis.

The 1980 and 1983 Zobel papers are retained as related source lineages rather
than silently merged into one experiment. This package uses the 1983 Table 1
fixture as its canonical benchmark because the source locator and reaction
labels are explicit in that paper; the relationship to the 1980 `^{67}Ga`
values remains a source-lineage item for final author review. The 9-MeV row
for the 958-keV transition is empty in the 1983 table and is intentionally
absent from the fixture.
