# Article data boundary

`data/` is reserved for the immutable, publication-authorized base data that
the article directly depends on.

At the current stage this directory contains no private experimental matrix or
workbook copy. The local analysis reads the user-supplied originals from
`raw/data/SouthAfrica/` and writes derived, private audit artifacts under
`analysis/` or the corresponding `outputs/l4/` report.

When a public data release is authorized, each file added here must include:

- source path and exact locator;
- units and uncertainty definition;
- SHA-256;
- whether it is an experimental value, a derived value, or a model input;
- the permission/publication status.
