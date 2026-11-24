# PDM error, geometry and grid studies

These are reproducible research studies, not a new GUI release. The published
0.1.0 core is unchanged. The secretary report has the integrated figures,
assumptions and limitations.

- `asymmetric_errors/`: actual legacy fits, current observation PDF,
  continuous split-normal, a smooth quantile-matched alternative, and
  acceptance-aware multistart. The report is titled
  "不对称误差的处理方案". Optimizer success is not fit acceptance.
- `geometry/`: 135Pr's explicit 2:1 weighted intensity formula and P angle,
  reproduction against the user-provided coefficient code, and a ring-average
  versus phi-zero control. This is a response prototype, not a GUI editor.
- `grid_resolution/`: nine grid choices and nine observations, then six held-out
  cases; angle-space 68% interval and per-HDI-component mode comparisons,
  timing, memory and numerical-threshold audit. All retained results matter,
  including cases whose 68% HDI does not include the injected truth.

The studies ran with Python3.12 on Linux and use the already installed shared
`multipolepdm` package. Some reproducibility commands verify originals against
paths in the local research archive. This is separate from normal use of the
public notebooks, which only need the supplied GUI-format example outputs.
Original papers and the private collection workbook are not redistributed here.

The grid recommendation is 0.1 degree in arctan(delta) and 0.005 in sigma/I
for the tested cases, not a universal optimum. The P-error floor0.1075 is a
median of ten audited main-tier lines, not a universal experimental precision.
Public-facing angle plots use radians with pi-fraction ticks; studies may
record degrees explicitly to make the resolution comparison readable.
