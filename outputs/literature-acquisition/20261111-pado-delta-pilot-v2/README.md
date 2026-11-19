# PADO Mixing Ratio & Spin Alignment Review Ledger (Pilot v2)

## 1. Overview & Scope
- **Dataset Count**: 29 audited transitions across 5 reference sources (`W77`: 14, `L22`: 3, `M15`: 4, `G22`: 2, `S20`: 6).
- **Nuclei**: $^{61}\text{Ni}$, $^{135}\text{Pr}$, $^{187}\text{Au}$ (bounded pilot; $^{72}\text{Se}$ integrated via CLI when worker file is ready).
- **Transition Selection**: Strictly numerical $\delta$ results with multipolarity $E2/M1$. Excluded pure $E2$, unextracted weak transitions, and $M3/E2$ / $M2/E1$ control lines.

## 2. Structure & Navigation
- **Primary Key**: `dataset_id` (e.g. `NI77-908`, `PR15-747`, `AU22-376`).
  - `Dataset.dataset_id` hyperlinks directly to the corresponding `Settings` row.
  - `Settings.dataset_id` hyperlinks back to `Dataset`.
- **References**:
  - Concise 6 fields: `ref_id`, `doi`, `extraction`, `local_file`, `supplement_file`, `url`.
  - `doi`: Direct DOI string with clickable `https://doi.org/...` resolver.
  - `url`: Direct publisher full-text landing page.
  - `ref_id`: Hyperlinks to the first data row in `Dataset`.
- **Cross-Dataset Comparison**:
  - `comparison_dataset_id` links independent measurements of the same transition ($\Delta E \le 0.6\text{ keV}$, same $J_i^\pi \to J_f^\pi$).
  - `AU22-376` $\leftrightarrow$ `AU20-376`; `AU22-462` $\leftrightarrow$ `AU20-462`.
  - `PR22-747` $\leftrightarrow$ `PR15-747`; `PR22-813` $\leftrightarrow$ `PR15-813`.
  - `result_origin` is `ORIGINAL_MEASUREMENT` for both pairs; they represent separate, independent experiments with differing $\delta$ values.

## 3. Ratio Classification
- `R_ADO`: Angular distribution of oriented nuclei ratio.
  - G22: Typical two-angle ratio ($154^\circ / 90^\circ$).
  - L22: Grouped detector angles ($157.6^\circ + 133.6^\circ$ vs $75.5^\circ + 104.5^\circ$).
- `NA`: Multi-angle full $W(\theta)$ angular distribution fitting (W77, M15, S20), not an intensity ratio.

## 4. Build Command
```bash
python3 system/scripts/build_pado_delta_review_workbook.py \
  --ledger outputs/literature-acquisition/20261110-pado-delta-pilot/audited-extraction.json \
  --se72 tmp/pado-delta-v2/se72.json \
  --output raw/writing/pado/20261029_review_v1/mixing_ratio_sigma_I_pilot_20261111.xlsx \
  --v2-json outputs/literature-acquisition/20261111-pado-delta-pilot-v2/audited-v2.json
```
