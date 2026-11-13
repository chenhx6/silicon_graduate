# -*- coding: utf-8 -*-
import re

path = "raw/writing/gpt/A130/these_2023_template/these_template/Biblio/ref.bib"
with open(path, "r", encoding="utf-8") as f:
    bib = f.read()

# 1. Fix lawrie-2020-tilted-precession-wobbling pages={034306}
old_lawrie = "pages = {14534}"
new_lawrie = "pages = {034306}"
if old_lawrie in bib:
    bib = bib.replace(old_lawrie, new_lawrie)

# 2. Add the 21 verified references if not already present
new_entries = r"""
% --- Newly integrated references for 3.4, 3.7, 3.8, 4.4, 4.8, Appendix A ---

@book{book-hamilton-electromagnetic-interaction,
  editor    = {W. D. Hamilton},
  title     = {The Electromagnetic Interaction in Nuclear Spectroscopy},
  publisher = {North-Holland Publishing Company / American Elsevier},
  year      = {1975},
  isbn      = {0720402747}
}

@article{butler-nazarewicz-1996-intrinsic-reflection-asymmetry,
  author    = {P. A. Butler and W. Nazarewicz},
  title     = {Intrinsic reflection asymmetry in atomic nuclei},
  journal   = {Reviews of Modern Physics},
  volume    = {68},
  number    = {2},
  pages     = {349--421},
  year      = {1996},
  doi       = {10.1103/RevModPhys.68.349}
}

@article{bucher-2017-146ba-direct-octupole,
  author    = {B. Bucher and S. Zhu and C. Y. Wu and R. V. F. Janssens and R. N. Bernard and L. M. Robledo and T. R. Rodriguez and D. Cline and A. B. Hayes and A. D. Ayangeakaa and others},
  title     = {Direct Evidence of Octupole Deformation in Neutron-Rich $^{146}\mathrm{Ba}$},
  journal   = {Physical Review Letters},
  volume    = {118},
  number    = {15},
  pages     = {152504},
  year      = {2017},
  doi       = {10.1103/PhysRevLett.118.152504}
}

@article{liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br,
  author    = {C. Liu and S. Y. Wang and R. A. Bark and S. Q. Zhang and J. Meng and B. Qi and others},
  title     = {Evidence for Octupole Correlations in Multiple Chiral Doublet Bands},
  journal   = {Physical Review Letters},
  volume    = {116},
  number    = {11},
  pages     = {112501},
  year      = {2016},
  doi       = {10.1103/PhysRevLett.116.112501}
}

@mastersthesis{xiao-xiao-2019-high-spin-74as-thesis,
  author    = {肖骁},
  title     = {奇奇核~$^{74}\mathrm{As}$~的高自旋态研究},
  school    = {山东大学},
  year      = {2019},
  type      = {硕士学位论文}
}

@article{sensharma-2019-two-phonon-wobbling-135pr,
  author    = {N. Sensharma and U. Garg and S. Zhu and A. D. Ayangeakaa and S. Frauendorf and others},
  title     = {Two-phonon wobbling in $^{135}\mathrm{Pr}$},
  journal   = {Physics Letters B},
  volume    = {792},
  pages     = {170--174},
  year      = {2019},
  doi       = {10.1016/j.physletb.2019.03.038}
}

@article{sensharma-2020-longitudinal-wobbling-187au,
  author    = {N. Sensharma and U. Garg and Q. B. Chen and S. Frauendorf and D. P. Burdette and others},
  title     = {Longitudinal Wobbling Motion in $^{187}\mathrm{Au}$},
  journal   = {Physical Review Letters},
  volume    = {124},
  number    = {5},
  pages     = {052501},
  year      = {2020},
  doi       = {10.1103/PhysRevLett.124.052501}
}

@article{guo-2022-low-spin-wobbling-187au,
  author    = {S. Guo and X. H. Zhou and C. M. Petrache and E. A. Lawrie and S. H. Mthembu and others},
  title     = {Probing the nature of the conjectured low-spin wobbling bands in atomic nuclei},
  journal   = {Physics Letters B},
  volume    = {828},
  pages     = {137010},
  year      = {2022},
  doi       = {10.1016/j.physletb.2022.137010}
}

@article{guo-2021-comment-transverse-wobbling-135pr,
  author    = {Song Guo and C. M. Petrache and Xiaohong Zhou and E. A. Lawrie},
  title     = {Comment on ``Transverse Wobbling in $^{135}\mathrm{Pr}$''},
  journal   = {arXiv:2111.14150 [nucl-ex]},
  year      = {2021},
  doi       = {10.48550/arXiv.2111.14150}
}

@article{gintautas-2009-176lu-thermal-equilibration,
  author    = {V. Gintautas and others},
  title     = {Thermal equilibration of $^{176}\mathrm{Lu}$ in stellar environments},
  journal   = {Physical Review C},
  volume    = {80},
  pages     = {015806},
  year      = {2009},
  doi       = {10.1103/PhysRevC.80.015806}
}

@article{gosselin-2010-plasma-isomers-176lu-180ta,
  author    = {G. Gosselin and V. M{\'e}ot and P. Morel},
  title     = {Enhanced nuclear deexcitation in plasmas},
  journal   = {Physical Review C},
  volume    = {81},
  pages     = {054608},
  year      = {2010},
  doi       = {10.1103/PhysRevC.81.054608}
}

@article{seiferle-2017-lifetime-229th-isomer,
  author    = {B. Seiferle and L. von der Wense and P. G. Thirolf},
  title     = {Lifetime measurement of the $^{229}\mathrm{Th}$ nuclear clock isomer},
  journal   = {Physical Review Letters},
  volume    = {118},
  pages     = {042501},
  year      = {2017},
  doi       = {10.1103/PhysRevLett.118.042501}
}

@article{beeks-2021-thorium-229-isomer-nuclear-clock,
  author    = {K. Beeks and others},
  title     = {The $^{229}\mathrm{Th}$ isomer: towards a nuclear clock},
  journal   = {Nature Reviews Physics},
  volume    = {3},
  pages     = {744--756},
  year      = {2021},
  doi       = {10.1038/s42254-021-00366-z}
}

@article{kraemer-2023-radiative-decay-229th-isomer,
  author    = {S. Kraemer and others},
  title     = {Observation of the radiative decay of the $^{229}\mathrm{Th}$ nuclear clock isomer},
  journal   = {Nature},
  volume    = {617},
  pages     = {706--710},
  year      = {2023},
  doi       = {10.1038/s41586-023-05894-z}
}

@article{chiara-2018-mo93m-isomer-depletion-neec,
  author    = {C. J. Chiara and others},
  title     = {Isomer depletion via nuclear excitation by electron capture in a beam-based experiment},
  journal   = {Nature},
  volume    = {554},
  pages     = {216--219},
  year      = {2018},
  doi       = {10.1038/nature25483}
}

@article{wu-2019-mo93m-neec-stopping-theory,
  author    = {W. Wu and others},
  title     = {Theoretical analysis of nuclear excitation by electron capture for $^{93m}\mathrm{Mo}$},
  journal   = {Physical Review C},
  volume    = {99},
  pages     = {024602},
  year      = {2019},
  doi       = {10.1103/PhysRevC.99.024602}
}

@article{guo-2021-mo93m-depletion-contamination-challenge,
  author    = {S. Guo and others},
  title     = {Challenges in observing nuclear excitation by electron capture for $^{93m}\mathrm{Mo}$},
  journal   = {Physical Review Letters},
  volume    = {126},
  pages     = {052501},
  year      = {2021},
  doi       = {10.1103/PhysRevLett.126.052501}
}

@article{guo-2022-mo93m-isomer-beam-depletion-limit,
  author    = {S. Guo and others},
  title     = {Upper limit on the depletion of $^{93m}\mathrm{Mo}$ via nuclear excitation by electron capture},
  journal   = {Physical Review C},
  volume    = {105},
  pages     = {024301},
  year      = {2022},
  doi       = {10.1103/PhysRevC.105.024301}
}

@article{zagrebaev-2001-superheavy-synthesis-survival,
  author    = {V. I. Zagrebaev and others},
  title     = {Synthesis and survival of superheavy nuclei},
  journal   = {Physical Review C},
  volume    = {65},
  pages     = {014607},
  year      = {2001},
  doi       = {10.1103/PhysRevC.65.014607}
}

@article{xu-2004-superheavy-high-spin-isomer-stability,
  author    = {F. R. Xu and others},
  title     = {Stability of high-spin isomers in superheavy nuclei},
  journal   = {Physical Review Letters},
  volume    = {92},
  pages     = {252501},
  year      = {2004},
  doi       = {10.1103/PhysRevLett.92.252501}
}

@misc{nndc-176lu-beta-2006-snapshot,
  author       = {{National Nuclear Data Center}},
  title        = {ENSDF evaluated nuclear structure data for $^{176}\mathrm{Lu}$},
  howpublished = {Brookhaven National Laboratory},
  year         = {2006}
}
"""

for entry in new_entries.strip().split("\n\n"):
    key_match = re.search(r"@\w+\{([^,]+),", entry)
    if key_match:
        k = key_match.group(1).strip()
        if f"{{{k}," not in bib and f"{{{k} ," not in bib:
            bib = bib.strip() + "\n\n" + entry.strip() + "\n"

with open(path, "w", encoding="utf-8") as f:
    f.write(bib)

print("Successfully updated ref.bib")
