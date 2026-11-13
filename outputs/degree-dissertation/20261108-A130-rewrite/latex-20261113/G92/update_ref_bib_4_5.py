# -*- coding: utf-8 -*-
import re

path = "raw/writing/gpt/A130/these_2023_template/these_template/Biblio/ref.bib"
with open(path, "r", encoding="utf-8") as f:
    bib = f.read()

entries_to_add = r"""
@article{xiao-2022-chirality-octupole-correlations-74as,
  author    = {X. Xiao and S. Y. Wang and C. Liu and R. A. Bark and J. Meng and S. Q. Zhang and B. Qi and H. Hua and P. Jones and S. M. Wyngaardt and S. Wang and D. P. Sun and Z. Q. Li and N. B. Zhang and H. Jia and R. J. Guo and X. C. Han and L. Mu and X. Lu and W. Z. Xu and C. Y. Niu and C. G. Wang and E. A. Lawrie and J. J. Lawrie and J. F. Sharpey-Schafer and M. Wiedeking and S. N. T. Majola and T. D. Bucher and T. Dinoko and B. Maqabuka and L. Makhathini and L. Mdletshe and N. A. Khumalo and O. Shirinda and K. Sowazi},
  title     = {Chirality and octupole correlations in $^{74}\mathrm{As}$},
  journal   = {Physical Review C},
  volume    = {106},
  number    = {6},
  pages     = {064302},
  year      = {2022},
  doi       = {10.1103/PhysRevC.106.064302}
}

@article{butler-1996-octupole-shapes,
  author    = {P. A. Butler and W. Nazarewicz},
  title     = {Intrinsic reflection asymmetry in atomic nuclei},
  journal   = {Reviews of Modern Physics},
  volume    = {68},
  number    = {2},
  pages     = {349--421},
  year      = {1996},
  doi       = {10.1103/RevModPhys.68.349}
}

@article{wang-2019-rat-prm-78br-octupole-correlations,
  author    = {Y. Y. Wang and S. Q. Zhang and P. W. Zhao and J. Meng},
  title     = {Multiple chiral doublet bands with octupole correlations in reflection-asymmetric triaxial particle rotor model},
  journal   = {Physics Letters B},
  volume    = {792},
  pages     = {454--460},
  year      = {2019},
  doi       = {10.1016/j.physletb.2019.04.014}
}
"""

for entry in entries_to_add.strip().split("\n\n"):
    key_match = re.search(r"@\w+\{([^,]+),", entry)
    if key_match:
        k = key_match.group(1).strip()
        if f"{{{k}," not in bib and f"{{{k} ," not in bib:
            bib = bib.strip() + "\n\n" + entry.strip() + "\n"

with open(path, "w", encoding="utf-8") as f:
    f.write(bib)

print("Successfully updated ref.bib with 4.5 citations")
