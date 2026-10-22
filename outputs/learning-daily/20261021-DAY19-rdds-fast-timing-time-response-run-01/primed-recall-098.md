# checkpoint098 primed recall before 106Ag chiral contrast re-audit
Same run/session; original 2026-10-22 15:00 Shanghai research deadline. Strongly primed by 088, 090, 095, 096, 097, and previous chiral band studies. No blind recall and no independent experimental data.
Core purpose: Re-audit the claim in RA14-D19-1 in knowledge/sources/rather-2014-ag106-transition-rates.md:
1. The claim asserted that chirality strictly requires S(I) across spin to be identically 1. This is false: Koike 2004, Hamamoto 2011, and Grodner 2011 demonstrate that chiral bands exhibit odd-even staggering in B(M1), so S(I) can oscillate.
2. The reason Rather et al. rejected chirality for 106Ag was that the B(M1) patterns lacked the required anti-phase staggering and selection rules, and TPSM reproduced the spectra and transition rates via two distinct quasiparticle configurations (K=4 vs K=2) with the same triaxial mean-field core (epsilon=0.15, gamma=30 deg).
3. The double ratio S(15)/S(17) = 7.2863 cancels a uniform stopping scale under strict shared-normalizer assumptions, but does NOT eliminate non-uniform stopping power errors (per checkpoint 090), line-specific branching, conversion coefficients, or unmodeled side-feeding.
Implement day19_ag106_chiral_contrast_audit098.py with explicit mathematical controls.
