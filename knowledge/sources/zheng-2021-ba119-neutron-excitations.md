---
type: source
title: "Zheng et al. 2021 - Neutron excitations and mixing-ratio branches in 119Ba"
aliases: [Zheng 2021 119Ba PRC 014326]
created: 2026-11-21
updated: 2026-11-21
status: ai-draft
review_status: unreviewed
source_type: experiment-and-model
reading_depth: deep-read
title_original: "Neutron excitations in 119Ba"
authors: [K. K. Zheng, C. M. Petrache, et al.]
journal: "Physical Review C"
year: 2021
volume: 104
pages: "014326"
doi: "10.1103/PhysRevC.104.014326"
canonical_source: "Zheng et al., Phys. Rev. C 104, 014326 (2021)"
raw_file: "raw/papers/gpt/query/20261121-zheng-ba119-lineage/10.1103_PhysRevC.104.014326-jyx.pdf"
raw_sha256: "24e13d215bc41d29145a40d39a9283351f8a4f7a7bda9e0563292c995a95e274"
archive_required: true
nuclei: [119Ba]
observables: [DCO, Rac, polarization-asymmetry, angular-distribution, mixing-ratio, half-life]
tags: [JUROGAM3, MARA, neutron-excitations, mixing-ratio, isomers]
---

# The \(^{119}\mathrm{Ba}\) angular observables and mixed-transition branches

## Bibliographic Record

K. K. Zheng et al., *Phys. Rev. C* 104, 014326 (2021), DOI `10.1103/PhysRevC.104.014326`. The University of Jyväskylä repository PDF has one cover followed by 11 published pages. PDF p.2 corresponds to 014326-1.

## Scope and Reading Depth

Read the published narrative, apparatus, spectrum and level figures, half-life and configuration discussion, Table I and references. Visually checked the 161.5, 91.9, 146.3 and 184.2 keV rows and compared the independently printed thesis entries. The full table was not transcribed.

## Summary

The \(^{58}\mathrm{Ni}(^{64}\mathrm{Zn},2pn)\) channel at 255 MeV is part of the JUROGAM 3＋MARA acquisition used in [[zheng-2021-collectivity-shape-119cs-119ba-118cs]], [[zheng-2021-cs119-proton-excitations]] and [[zheng-2021-cs118-bands-and-isomers]]. The paper identifies Band 3 on a proposed \(3/2^+\) ground state and measures the Band 1 \(5/2^-\) isomer half-life \(0.36(2)\,\mu\mathrm{s}\) from the 66 keV delayed transition. Weaker 53 and 59 keV time spectra give compatible results with larger errors. The proposed ordering of the weak branches depends on coincidence evidence and conditional Weisskopf estimates. Printed 014326-2, 014326-4 and Fig. 6.

| \(E_\gamma\) (keV) | \(R_{\rm DCO}\), gate | \(a_2\) | \(a_4\) | \(A_p\) | Table I \(\delta(M1/E2)\), original label |
| --- | --- | --- | --- | --- | --- |
| 161.5 | 1.2(1), stretched dipole | −0.72(12) | 0.40(23) | −0.14(5) | −2.3(2) or −0.3(5) |
| 91.9 | 0.5(1), stretched quadrupole | −0.73(15) | 0.66(27) | | −2.0(10) or −0.2(5) |
| 146.3 | 0.5(1), stretched quadrupole | −0.72(4) | 0.32(6) | −0.02(1) | −2.2(8) or −0.2(3) |
| 184.2 | 1.3(3), stretched dipole | −0.47(5) | 0.46(6) | −0.16(9) | −3.8(6) or −0.1(5) |

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| Z21-BA119-1 | Several rows retain two mixing ratios despite a reported polarization asymmetry in the same row. The 91.9 keV line has two tabulated solutions and a blank polarization cell, although the text quotes the large branch when discussing Band 3. | source-table-and-text | direct | 014326-4, 014326-9–10 Table I |
| Z21-BA119-2 | The focal-plane delay of the 66 keV ray gives \(T_{1/2}=0.36(2)\,\mu\mathrm{s}\); coincidence and intensity constraints support the relationships between the observed bands. | experimental-observation | direct | 014326-2, Fig. 6 |
| Z21-BA119-3 | Band systematics and PNC-CSM support alternative neutron configurations with distinct alignment behavior. The inferred orbitals and shape are the authors' model interpretation. | structure-interpretation | direct | 014326-4–8, Secs. III–IV |

## Competing Interpretations and Limitations

- Table I footnotes e/f designate dipole/quadrupole gates respectively. Thesis Table 6.2 reverses the footnote letters and the selected rows use corresponding swapped markers. The 161.5 and 146.3 keV physical gates agree across versions.
- The source leaves the amplitude convention as printed in its caption and gives no explicit conversion from the Table I label to another source's E2/M1 convention. It describes asymmetries via Ref. 19. The \(\delta\) entries and \(A_p\) values alone give insufficient evidence to identify a joint inference pipeline or a fixed/varied \(\sigma/I\) decision.
- The \(^{119}\mathrm{Ba}\) result revises prior placement of the 85 and 92 keV transitions and notes possible contamination of some previously reported high-spin lines. These revisions are separate from the observed spin and half-life constraints.

## Extracted Pages

- Publisher pp.1–6, experimental setup, low-lying scheme, delay fit and γ spectra.
- Publisher pp.7–8, alignment systematics, PNC-CSM and summary.
- Publisher pp.9–11, Table I and bibliography.
