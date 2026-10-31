# Unit 028 — $^{225}$Ac parity-partner audit

## Acquisition

NNDC official ENSDF query returned `225089001,225AC ADOPTED LEVELS, GAMMAS`, evaluation version 2022-07, cutoff 25 October 2019. The retrieved response is archived at `raw/data/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/225ac-adopted-225089001-028.html` with SHA-256 `fb3d87428e000397881227c3dc96973c1765310a7811062cc8c297259872a817` (169 wrapper lines; fixed-column ENSDF text in the `<pre>` block).

## Level and E1 evidence

The adopted scheme lists $(3/2^-)$ at 0.0 keV and $(3/2^+)$ at 40.10(4) keV. Their 40.09(5)-keV E1 transition is assigned $B(E1)=0.00171(15)$ W.u.; the evaluation says the strength comes from L-subshell ratios in $^{225}$Ra beta-minus decay. This is an evaluated data field with a source chain, not a new primary measurement in this run.

Other same-spin levels are repeated across adopted bands. Examples are $(5/2^-)$ at 29.91 keV and 120.81 keV versus $(5/2^+)$ at 64.69 and 155.64 keV; $(7/2^-)$ at 77.13 and 170.75 keV versus $(7/2^+)$ at 105.01 and 199.86 keV. Consequently, differences range from −34.78 to +56.12 keV for the displayed $5/2$ candidates and from −27.88 to +65.74 keV for the displayed $7/2$ candidates. A unique alternating-parity band cannot be selected from the evaluation alone.

## Conditional dipole extraction

For the $I_i=I_f=3/2$ E1 line, an axial strong-coupling convention with $K=3/2$ gives

$$B(E1)=\frac{3}{4\pi}D_0^2\left|\langle I K,1 0|I K\rangle\right|^2,$$

with the squared coefficient $K^2/[I(I+1)]=0.6$. Using $R=1.2A^{1/3}$ fm for the E1 Weisskopf unit gives $D_0=0.1688\pm0.0074\ e\,\mathrm{fm}$. This is a conditional rotor inference: the evaluation does not provide $D_0$, its sign, or a covariance matrix for the E1 strength.

## Interpretation boundary

The low-energy pair is compatible with a parity-partner candidate, but the parenthesized Jπ labels, multiple same-spin states and adopted band assignments prevent a unique parity-doublet claim. The result cannot quantify a single-particle octupole blocking factor. A microscopic comparison requires matched odd/even self-consistent pairing, blocked quasiparticle spectra and an octupole response calculation.

## Reproducibility

The structured values and arithmetic are in `parity-doublet-ac225-028.json`. The raw file was created with exclusive write, then re-read and checked for the 40.10-keV level and `BE1W=0.00171 15` field. No shared page, index, Git staging, commit or push was performed.
