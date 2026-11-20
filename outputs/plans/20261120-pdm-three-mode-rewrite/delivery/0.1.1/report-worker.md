# PDM U07 report and Figure 6

- Canonical report `raw/writing/pado/20261029_review_v1/PDM/main.pdf` has 50 A4 pages. Figure 6 is on page 24. The editable source is `main.tex` in the same directory.
- `figures/empirical_summary.pdf` compares 18 declared models across six nuclei. `figures/data/empirical_summary.csv` records 115 interval, mode, and literature rows, including source locators, both spin identities, and all display offsets. The spin axes follow the U05 target-emitter convention. The width denominator for each PDM result is its Gaussian source spin.
- The report includes 30 independent \(9j\) and 30 same-kernel deterministic injections. The three linked tables contain 180 total rows. The full-precision records are in `figures/data/injection_deterministic.csv`; LaTeX reads `figures/data/injection_tables.tex`. The repeated-observation plot uses 600 fits from 300 independent noise vectors. The PDCO \(\delta_0=-10\) result remains visible at 0/100 angle ETI and 6/100 angle HDI inclusions.
- The 39 final declared literature models and eight refinement runs come from `analysis/cases/results_v0_1_1` and `analysis/cases/followup/results_v0_1_1`. The injection evidence comes from `analysis/benchmarks/sigma03_relP80_relR10` after the primary bound correction to \(\pm89.9^\circ\) and the final symmetry replay. Verified all 10 source hashes and 53 generated output hashes and sizes in `figures/manifest.json`.

## Release candidate refresh

- Rebuilt through `report/audit_render.py` after the queue-manager provenance replay. The manifest changed its two literature input digests. All eight other input digests stayed byte-identical. Parent verification is in `literature/final-release-comparison.json`. The largest change across the 115 Figure 6 data rows was \(5.551\times10^{-15}\). The injection CSV and all three linked LaTeX tables stayed byte-identical.
- Updated the report to 225 Linux regression passes, with the bounded failed-save snapshot and 50 ms deferred drawing behavior documented on page 17. The version status on page 27 remains a source candidate pending PyPI verification.
- The refreshed PDFs passed 14 collision, 14 font, and 13 alignment checks. The two candidate XeLaTeX passes completed and all 50 pages passed the text clipping check. The updated report sections and Figure 6 were checked visually. Render, build, and data audit logs are `report/release-candidate-render.log`, `report/xelatex-release-candidate-1.log`, `report/xelatex-release-candidate-2.log`, and `report/release-candidate-data-check.log`.

## Published revision

- The displayed historical coverage uses only 68% ETI and HDI and two-sided 68% Wilson binomial intervals, using the standard normal quantile at 0.84. The caption identifies the original delta coordinate and observation noise separately from the 0.1.1 angle-space convention. The historical range example and refinement figures were taken from the original 68% records in `analysis/benchmarks/synthetic_benchmarks.json`.
- Ran `plot_historical_coverage(root, analysis)` from `figures/generate_figures.py` under the alignment auditor, then refreshed the existing inventory with `write_manifest`. The other 52 manifest outputs, including the empirical Figure 6 PDF and data, and all 10 inputs are byte-identical. The historical benchmark JSON retains the source records.
- The regenerated historical figure passed alignment, collision, and font audits. XeLaTeX completed twice with `report/xelatex-published-68-1.log` and `report/xelatex-published-68-2.log`. All 50 pages passed the clipping and stale assessment-level checks. Page 19 has the historical coverage figure, page 24 has Figure 6, and page 27 records PyPI publication and installation verification.
- 0.1.1 is published, with both public artifact hashes matched, the imported version and isolated installation verified, and all three Linux offscreen GUI cases passing. Evidence is in `pypi-import.json`, `pypi-gui-smoke-verified.json`, and `raw/code/PDM/analysis/validation_v0_1_1/publication/verification.json`. The report retains 225 final Linux regression passes and the untested Windows and macOS native boundary.

## Reproduction

Run from the Wiki root, using the source candidate in `raw/code/PDM/GUI/src`.

```bash
pdm_report="$PWD/raw/writing/pado/20261029_review_v1/PDM"
pdm_qa="$PWD/tmp/pdm-upgrade-011/report"
pdm_gui="$PWD/raw/code/PDM/GUI/src"
pdm_figure_skill="/root/.codex/skills/nature-figure/scripts"
PYTHONPATH="$pdm_gui" PYTHONDONTWRITEBYTECODE=1 MPLBACKEND=Agg \
  MPLCONFIGDIR="$pdm_qa/matplotlib" python "$pdm_report/figures/generate_figures.py"
PYTHONPATH="$pdm_gui:$pdm_report/figures:$pdm_figure_skill" \
  PYTHONDONTWRITEBYTECODE=1 MPLBACKEND=Agg MPLCONFIGDIR="$pdm_qa/matplotlib" \
  python "$pdm_qa/audit_render.py" > "$pdm_qa/production-render-final.log" 2>&1
(
  cd "$pdm_qa" || exit
  for pass in 1 2; do
    TEXINPUTS=".:$pdm_report:" xelatex -interaction=nonstopmode -halt-on-error \
      "$pdm_report/main.tex" > "xelatex-final-$pass.log" 2>&1 || exit
  done
)
cp "$pdm_qa/main.pdf" "$pdm_report/main.pdf"
cmp "$pdm_qa/main.pdf" "$pdm_report/main.pdf"
```

The audited render invokes the same generator through `audit_render.py`. Run `audit_figure_collisions.py` and `audit_pdf_text.py --min-pt 5` from the nature-figure skill on each of the 14 regenerated figure PDFs. The final render, alignment overlays, collision and font reports, and page previews are in `tmp/pdm-upgrade-011/report/`.

## Verification

- The 14 regenerated PDFs passed collision and font audits. The 13 regenerated multipanel figures passed rendered physical alignment. The overview layout uses explicitly declared comparable `a/b` and `c/d` rows and corresponding columns, with colorbars outside the comparison. The first generic alignment attempt could not infer these groups from absolute axes, so the final driver declares them before export.
- XeLaTeX completed twice without unresolved references, missing-glyph messages, or overfull boxes. Fandol reports font-script warnings, and the prose contains minor underfull lines. Rendered all pages, inspected the report contact sheets plus Figure 6, the interval tables, and the repaginated last page at higher resolution. All new XeLaTeX auxiliaries live in the QA directory. The pre-existing report-directory auxiliary files were outside this task's ownership.
- The startup workspace inspection issued read-only Git status commands before the task-specific no-Git scope was applied. The broad initial filesystem lookup was stopped at the efficiency checkpoint.

## Final SHA-256

```text
be014e1be95388c8fabb1f4631a0a0390ca6c8f504504964da85a4929af8c43f  main.pdf
30bc1b66c49d7d1ac1615d90a8cc06e62d2af5029f1eee4e24898a90d8a4c996  figures/synthetic_coverage.pdf
f861bd72f49e74ca6717dfec683fb5b622fdeb4841933842825b641ad9daec4d  figures/empirical_summary.pdf
fb3cfe3c1367448bec196a265847c8fc63bdf81d2fb744fdd361ffdf9e2ec906  figures/manifest.json
```
