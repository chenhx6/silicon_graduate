# 079：133Ce 独立 primary 入口与 1998 Joss 寿命原件

本单元核对 ENSDF 1991Pa04／1998Jo16 的真实身份，并取得、通读 1998Jo16 正文。1991Pa04 的合法 PDF 路径三次均返回 HTML wrapper，未将其冒作全文；1998Jo16 已取得完整4页、全部图表视觉核。没有修改 canonical/raw/Git/course/session，不运行 producer、旧114或 toy。

## ENSDF identity gate

NNDC/ENSDF 133Ce adopted references（本地已取得的 `tmp/day24-ce133-evaluated-zero-entry-069/adopted-refs-text.txt`）给出：

- **1991Pa04**：E. S. Paul, R. Ma, C. W. Beausang, S. A. Forbes, D. B. Fossan, J. Gizon, J. R. Hughes, Y. Liang, S. M. Mullins, P. J. Nolan, W. F. Piel Jr., R. J. Poynter, P. H. Regan, R. Wadsworth, N. Xu, “Electromagnetic Properties of N=75 Isotones: Evidence for triaxiality at low spin”, *J. Phys. G* **17**,605–617 (1991), DOI `10.1088/0954-3899/17/5/009`. ENSDF reaction fields include `92Mo(50Cr,n2p), E=220 MeV` and `120Sn(16O,3n), E=69 MeV`; measured γγ-coincidence, γγ(θ), levels/Jπ/δ/B(λ) ratios.
- **1998Jo16**：D. T. Joss et al., “Lifetime Measurements of a Triaxial Band in 133Ce”, *Phys. Rev. C* **58**,3219–3222 (1998), DOI `10.1103/PhysRevC.58.3219`. ENSDF identifies `100Mo(36S,3n)` with Gammasphere/DSA and deduced 133Ce transition lifetimes and quadrupole moments.

Crossref exact requests returned 200 for both. Targeted Wiki/raw search found no local 1991Pa04 primary PDF; 1998Jo16 was not previously present as a source page. Existing 2013 133Ce source and 2022 thesis are later/other analyses and do not replace these primary bodies.

## Acquisition and integrity

### 1991Pa04

The three bounded IOP routes (`iopscience` PDF, `stacks.iop` HTTPS/HTTP, download query) each returned a 14,371-byte HTML page beginning `<head><title`, never `%PDF`. Status: `no_authorized_pdf_found` for this entry. The exact DOI, metadata and ENSDF scope are retained; no scientific table or lifetime is transcribed from metadata/snippets.

### 1998Jo16

Authorized APS PDF route succeeded: `tmp/day24-ce133-independent-primary-079/1998Jo16-aps.pdf`, 4 pages, 120,604 bytes, SHA256 `81b6ace5d9ee867220c5425e7f3d9ae4f5074d9484f7063fd04fd137b0deea0a`. `pdfinfo` and `%PDF` signature pass; PDF pages 3219–3222, first/last pages visually checked. All four pages and Figs.1–4/Table I–II were read/visually reviewed. APS metadata links and Crossref are recorded in tmp; no SI was indicated or downloaded.

## Direct experimental record

The 1998 experiment used the independent reaction `100Mo(36S,xn)136−xCe` at Gammasphere and recorded approximately `9×10^8` fold-≥5 prompt coincidences over five days. For 133Ce, the 3n channel was weaker than 132Ce(4n) and 131Ce(5n); relative populations were reported as 5:4:1. In-band gates were 422, 488, 643 and 888 keV. Spectra were sorted by forward (31.7°, 37.4°), 90°, and backward (142.6°,148.3°) detector groups.

The observable was DSAM through Doppler-broadened line-shape analysis with LINESHAPE. Monte Carlo recoil histories used 0.001 ps steps, Ziegler stopping powers, target/backing geometry and angular configurations. Five thousand recoil histories were generated per step batch. Side-feeding intensities were fixed from the data set and modeled as a five-state rotational band with assumed `I_SF=48 ℏ² MeV⁻¹`; side-feeding Q and contaminants/background/normalization were fit variables. Forward, backward and 90° spectra were fitted simultaneously with SEEK/SIMPLEX/MIGRAD; MINOS errors below 8% of measured values were raised to that floor. These are analysis-contract details, not a public raw producer replay.

## Reported lifetime and Q_t results

| transition | Eγ (keV) | τ (ps) | τSF (ps) | Q_t (eb) |
|---|---:|---:|---:|---:|
|43/2−→39/2−|887.4|1.11±0.13|0.48±0.11|1.94±0.10|
|47/2−→43/2−|999.3|0.33±0.04|0.49±0.01|2.65±0.16|
|51/2−→47/2−|1097.6|0.20±0.02|0.37±0.04|2.66±0.21|
|55/2−→51/2−|1188.1|0.21±0.02|0.34±0.04|2.15±0.15|

The weighted mean is `Q_t=2.2±0.1 eb`. Equation (1) converts τ and Eγ to `T(E2)` and Q_t using a Clebsch–Gordan coefficient; the paper does not provide an independent branch/ICC ledger for this table. Q_t is therefore a fitted/derived transition quantity under the line-shape and side-feeding model, not a direct static quadrupole moment.

The paper compares this low-deformation triaxial band with 132,133Ce superdeformed bands (`Q_t≈7.4–7.5 eb`) and normally deformed 132Ce (`T(E2)≈100 W.u.`). It obtains approximately `T(E2)≈35 W.u.` for the triaxial band. Table II gives `β2=0.186±0.007, γ=−83°` from Q_t using theoretical γ, while prior triaxial-band values are approximately `Q_t≈2.3 eb, β2≈0.180, γ≈−80°`. These are model-converted deformation values, not direct γ distributions.

The comparison is strengthened by concurrent population and common stopping conditions for the triaxial 133Ce band and the 132Ce SD band, but absolute Q_t has 10–15% uncertainty from recoil stopping knowledge. The three known 133Ce SD bands were weak in this reaction and were not observed; prior SD measurements are a separate source.

## Model interpretation and limits

TRS Woods–Saxon cranking calculations predict a negative-parity one-neutron `νh11/2` triaxial minimum near `β2≈0.19, γ≈−30°` (Lund convention) and a separate `νh11/2^3` minimum near `γ≈−73°`; Fig.3 displays coexistence with a prolate superdeformed minimum near `β2≈0.4`. These are calculations, not direct observed shapes. The paper calls the measured band triaxial based on Q_t/DSAM and the calculation; the “stable” shape language belongs to the model interpretation.

The authors explicitly note Q_t extraction can include an effective lifetime contribution from side-feeding enhanced by lower in-band gates. They use a fixed side-feeding inertia, estimated from experimental in-band values, and assumed spins because no linking transitions to known low-lying bands had been found. This blocks a full absolute configuration/feeding proof.

The paper references the 1991Pa04 low-spin/triaxiality source only indirectly through its broader lineage (and cites prior 1995/1996 133Ce work); it is an independent 1998 reaction and response, not an independent model calculation. The same 1998 author/community lineage and TRS formalism mean its shape interpretation cannot be counted as a separate theoretical vote from 1991/2013 discussions.

## What this does and does not provide for the 133Ce blueprint

It adds an independent high-spin 133Ce lifetime/transition-quadrupole primary with explicit reaction, detector groups, DSAM response and side-feeding contract. It does not provide the low-spin 1991Pa04 electromagnetic/δ body, complete ICC/branch/Cov, or a direct static γ measurement. The reported `Q_t≈2.2 eb` and `β2≈0.186, γ≈−83°` must remain tied to this high-spin band and its TRS/DSAM assumptions; they cannot replace WK22 low-spin 1qp input, be used as a 133Ce universal shape parameter, or certify chirality/wobbling by themselves.

停止原因：1998Jo16 full primary is complete and high-value; 1991Pa04 remains an explicitly recorded metadata/authorized-PDF gap. No further endpoint repetition or source substitution is justified in this unit.

## Additional direct primary: Hauschild et al. 1996 (ENSDF 1996Ha20)

Because the ENSDF reference search also identified 1996Ha20 as a direct 133Ce high-spin source, the same bounded unit obtained and read it. Crossref exact DOI `10.1103/PhysRevC.54.613`, title “Triaxial bands in 133Ce”, *Phys. Rev. C* **54**,613–619 (1996), 12 authors. APS PDF: `tmp/day24-ce133-independent-primary-079/1996Ha20-aps.pdf`, 7 pages, 229,413 bytes, SHA256 `560215bbff5898a3e304f4219f35f628b3a4bd03c87ed1745dc25ae147162872`; all seven pages and Figs.1–9 were visually reviewed.

The experiment used `116Cd(22Ne,5n)` at 120 MeV with early Gammasphere (31 large-volume HPGe), about `1.5×10^9` fold>3 events, and RADWARE cube/double-gate/triple sorting. Six new ΔEγ≈100-keV sequences (bands 2–7) plus known band 1 and three SD bands were reported. Intensities relative to total 133Ce were estimated as ~10% (band 1), ~2% and ~1.5% (bands 2 and 4), and ~0.5% (bands 3,5,6,7). Band 1 lacked confirmed links to low-lying states; its possible isomeric bandhead was explicitly suggested. DCO statistics were insufficient; ΔI=2 stretched-E2 was assumed for bands 2–7.

The paper’s configurations are **tentative model interpretations**: band 1 proposed `ν(h11/2)^3`; bands 2/4 `ν(h11/2)^3 π(h11/2)^2` (signature-partner speculation itself qualified by unknown linking spins); bands 3/5 add `π(g7/2)^2`; bands 6/7 have further mixed five-quasiparticle proposals. Alignment gains and Harris parameters depend on assumed bandhead spin, K values and a chosen γ≈−30° or −80° reference. The authors explicitly say exact configurations remain open and neighbouring nuclei are needed. These assignments therefore cannot be called direct 3qp observations or converted to WK22 low-spin input.

The experiment is independent of Joss 1998 in reaction and campaign (`116Cd(22Ne,5n)` versus `100Mo(36S,xn)`), though the author community, Gammasphere lineage and prior 133Ce references overlap. Hauschild 1996 reports no lifetimes; its Q_t and triaxial interpretation rely on the earlier Nyberg Q_t≈2.3 eb and model calculations. Joss 1998 supplies the direct DSAM Q_t≈2.2±0.1 eb and lifetimes. Thus these are complementary experimental sources, not duplicate lifetime measurements or independent model votes.

The 1996 paper is useful for high-spin decay paths, tentative configuration alternatives, alignment/shape competition and the explicit missing-link boundary; it does not resolve 1991Pa04 access, modern 582-out references, or the low-spin signed-EM contract.
