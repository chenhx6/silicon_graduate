**135/137Ba source-energy replay: close agreement, with resolved few-keV differences**

The declared fixed kernel reproduces the ordering and approximate energies of all six negative-parity theory series shown for each of \(^{135,137}\)Ba in Nomura2017 Fig. 5(c). It does **not** reproduce every point within a 1-keV plot-grid window. Excluding the common zero reference, the largest differences are **1.896 keV for \(^{135}\)Ba** and **3.128 keV for \(^{137}\)Ba**. These differences are resolved by the vector extraction. They are not evidence that the published calculation is wrong, and they do not identify a unique cause.

This is an energy-only source comparison. It extends the earlier \(^{129}\)Ba check to these two nuclei and this displayed subset. It does not certify the entire isotope chain, higher states, author wavefunctions, electromagnetic predictions, or a correspondence between a calculated state and a particular observed isomer.

**Source extraction was frozen first**

The [source-only JSON](source-points-frozen.json) was frozen at **2026-11-06 09:33:07 UTC**, before the comparison contract at **09:35:30 UTC** and the kernel run at **09:36:57 UTC**. Its SHA-256 is:

```text
bc4dbed2c29f65ae8f9546cd146005efa6dbb64eb08ef23781ede6f907b91d22
```

The [freeze receipt](source-freeze.json) records the source JSON, CSV, and extractor hashes. The extractor reads original PDF/TeX bytes and hashes the previous \(^{129}\)Ba extractor as a method reference; it imports no kernel and reads no chain contract or prediction file. Earlier work in this session had exposed the model identities and the lowest \(11/2\) state energies, so this is a prospective extraction freeze, not a claim of complete blinding to the model family.

The primary evidence is:

- The canonical local [Nomura PDF](</workspace/wiki/raw/papers/2017_Nomura et al_Shape-phase transitions in odd-mass γ -soft nuclei with mass A ≈ 130.pdf>), physical p.7, Fig. 5(c). Its SHA-256 is `481e6a9e0f6b01e9c5db5e2b06d9b350dba0638393c7da7f532c3040e9efaea9`. This is the archived 13-page **arXiv v2**, not a separately verified journal version of record.
- The original `ba.level.pdf` member of [the archived arXiv-v2 source](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/nomura2017-v2-source.tar.gz), also retained byte-for-byte [here](source-assets/ba.level.pdf). The archive SHA-256 is `f7ed6dc746f50f16169d8796e4d12becd8827eaf4ac2ee4d5f1ff9cd04690faf`; the figure SHA-256 is `b6006a11da9e56b14e31f286cedfe339fda90626bba7632fd934cc78ba861ef2`.
- The original [TeX figure inclusion and caption](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:802), and the [discussion of the lowest negative-parity spin](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:851). The separately archived TeX was verified byte-for-byte against the tar member.

The [original figure rendering](source-assets/ba.level.png) and [canonical paper crop](source-assets/canonical-p7-fig5.png) were visually checked. Panel **(c)** is theory with negative parity; panel (d) is experimental and was not used as a theory target. \(Z=56\) makes the two target columns \(N=79,81\). The six legend assignments are green left triangle \(7/2^-\), yellow downward triangle \(9/2^-\), black circle \(11/2^-\), blue upward triangle \(13/2^-\), red square \(15/2^-\), and cyan star \(17/2^-\).

The source legend prints spin and parity without ordinals. Each negative-parity spin has one displayed series. The frozen comparison identifies that series with the requested lowest same-\(J\) kernel state; it does not substitute a higher state chosen for proximity. This identification supports an energy comparison, not an author wavefunction or band-label match.

The original figure has \(E=0\) at \(y=349.1919555664\) PDF points and \(E=2\) MeV at \(y=186.2499542236\), with intermediate labeled ticks at 0.5, 1.0, and 1.5 MeV. Coordinates have a top-left origin. The frozen mapping is

\[
E_{\rm MeV}=4.286088948077022-0.012274306093692159\,y_{\rm pt}.
\]

Neutron-number ticks, all marker coordinates, line-path vertices, colors, and path indices are retained in the JSON. Marker anchors are checked against their connecting curves. The star uses its rotational center rather than the bounding-box midpoint; triangular markers use the tip/base midpoint rather than the vertex centroid.

All 12 recovered energies lie within \(0.000204\) keV of an integer-keV grid. Extraction from the original figure and from the canonical paper's embedded figure differs by at most **0.000692 keV**. The predeclared numerical extraction tolerance is 0.002 keV. The observed grid does not establish the authors' rounding rule. The \(\pm0.5\) and \(\pm1\) keV comparison windows are declared rounding sensitivities, not experimental error bars or bounds on unprinted parameter precision.

**Identical energy zero and complete displayed comparison**

The \(11/2^-\) series is at zero in both target source columns. The frozen comparison therefore uses

\[
\Delta E_J=E(J^-_{\rm lowest})-E(11/2^-_{\rm lowest})
\]

in each isotope. The kernel also finds \(11/2^-\) as the global minimum in each negative-parity space. No offset or scale is fitted. The source's parity-separated zero does not supply absolute excitation energies relative to the positive-parity nuclear ground state.

All energies and differences below are in keV; \(\delta\) means kernel minus plotted source. The source integers are recovered plotting values, not a table of author eigenvalues.

| \(J^\pi\) | 135 source | 135 kernel | \(\delta_{135}\) | 137 source | 137 kernel | \(\delta_{137}\) |
|---|---:|---:|---:|---:|---:|---:|
| \(7/2^-\) | 918 | 919.361798 | +1.361798 | 1122 | 1125.043145 | +3.043145 |
| \(9/2^-\) | 448 | 449.895699 | +1.895699 | 414 | 417.128165 | +3.128165 |
| \(11/2^-\) | 0 | 0 | 0 | 0 | 0 | 0 |
| \(13/2^-\) | 404 | 404.585404 | +0.585404 | 607 | 606.856444 | −0.143556 |
| \(15/2^-\) | 691 | 691.863295 | +0.863295 | 968 | 968.873920 | +0.873920 |
| \(17/2^-\) | 1180 | 1181.063643 | +1.063643 | 1880 | 1880.069173 | +0.069173 |

The [CSV](comparison.csv) and [structured comparison](comparison.json) contain every point, its source locator, the selected kernel index, and the reference convention. Excluding \(11/2^-\), the descriptive RMS differences are **1.238344 keV** and **1.991747 keV**, respectively. Of five nonreference points, \(^{135}\)Ba has 0 inside the nearest-keV half-width and 2 inside the one-grid window; \(^{137}\)Ba has 2 and 3. These counts include the independently declared 0.002-keV extraction allowance.

The displayed energy order is reproduced:

- \(^{135}\)Ba: \(11/2,13/2,9/2,15/2,7/2,17/2\).
- \(^{137}\)Ba: \(11/2,9/2,13/2,15/2,7/2,17/2\).

Fig. 5(c) contains no \(19/2^-\) series and no higher same-spin states. The other explicit Ba detail figure, [Fig. 9 / TeX899–913](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:899), concerns **positive-parity \(^{135}\)Ba**. It adds no target negative-parity energies. In particular, the present agreement for the lowest \(15/2^-\) theory series cannot resolve the parent's experimental state-mapping ambiguity or certify a \(19/2^-\) isomer assignment.

**What the source does and does not establish about the model identity**

The existing [chain contract](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-chain-contract.json) is used unchanged. The signed \(h_{11/2}\) matrix element is carried over from the existing [chain parameter wrapper](/workspace/wiki/system/scripts/ba_quadrupole_closure_study.py:220):
\(Q_{jj}=-\sqrt{525/(143\pi)}=-1.081027387032316\). The comparison uses the following inputs, with energies/couplings in the existing MeV convention:

| Input | \(^{135}\)Ba | \(^{137}\)Ba | Source or status |
|---|---:|---:|---|
| Core | \(^{134}\)Ba | \(^{136}\)Ba | \(A-1\) reconstruction |
| \(N_B\) | 5 | 4 | Derived pair counts, not printed run cards |
| \(\epsilon_d\) | 0.38 | 1.15 | Table I, TeX301–302 |
| \(\kappa\) | −0.124 | −0.122 | Table I, TeX301–302 |
| \(\chi_H\) | −0.24 | −0.85 | Table I, TeX301–302 |
| \(v_{h11/2}^2\) | 0.810 | 0.936 | Table III, TeX392–393 |
| \(\Gamma_0^-\) | 0.6 | 0.4 | Table V, TeX517–518 |
| \(\Lambda_0^-\) | 1.0 | 5.0 | Table V, TeX517–518 |
| Monopole input \(A_0\) | −0.9 | −0.6 | Table V's \(A'_{11/2}\), inherited kernel mapping |

The source explicitly calls \(^{134}\)Ba the corresponding even-even core of \(^{135}\)Ba in the [E(5/4) discussion](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:918). That passage concerns positive parity. The shared-core Hamiltonian description and the even/odd chains support the adopted reconstruction, but there is no explicit archived negative-parity run card. A \(^{137}\)Ba-to-\(^{136}\)Ba executed core assignment is not separately printed.

The [general definition](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:200) sets \(N_B\) equal to valence fermion pairs, with \(N_F=1\); the source identifies the [50–82 shell](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:315) and discusses [neutron holes approaching \(N=82\)](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:692). Under the adopted \(A-1\) core assignment, three proton pairs above \(Z=50\) plus two/one neutron-hole pairs below \(N=82\) give \(N_B=5/4\). This is a text-supported reconstruction with stated counting conventions, not direct evidence of the values in the authors' executed input.

The source names [PBOS diagonalization](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:539). The archived source contains typesetting files and figures, not an executed PBOS deck or its eigenvectors. Agreement of a few energies strengthens consistency with the declared reconstruction but cannot identify the complete author run uniquely.

The unchanged kernel explicitly uses the full \(Q_\chi\cdot Q_\chi\) product including one-body contractions, no \(1/N_B\) scaling, the signed \(Q_{jj}\), the BCS factors, the colon-ordered exchange tensor, and \(A_0n_d\) for one fermion; its convention is documented at [module lines10–30](/workspace/wiki/system/scripts/analysis/single_j_ibfm.py:10), with the [interaction assembly](/workspace/wiki/system/scripts/analysis/single_j_ibfm.py:528). Altering the core/\(N_B\), interaction normalization, particle/hole convention, exchange or monopole mapping, or signed quadrupole input would change the Hamiltonian being tested. None was varied. The omitted single-\(j\) fermion energy is a common shift, which cancels from the present relative energies.

The resolved few-keV differences could depend on unprinted parameter precision, plot-value rounding, or details of the author's executed Hamiltonian conventions. This audit does not determine which, and it performs no parameter-precision scan. In particular, the differences exceeding 1 keV cannot all be described as agreement within the displayed 1-keV grid. They do not justify selecting a different \(N_B\), sign, or normalization because it fits.

**Verification, replay, and stopping boundary**

The source points were independently recovered from two PDF representations before the fixed run. The unchanged kernel was then run once per requested isotope with \(M=1/2\), retaining the full corresponding blocks of dimensions 226 and 119. Both loaded NumPy/SciPy OpenBLAS libraries reported one thread. The largest energy eigenvector residual was \(7.73\times10^{-15}\) MeV; the Hermiticity, angular-momentum, and orthonormality diagnostics are retained without suppressing their actual values in [comparison.json](comparison.json). This numerical precision does not add precision to the source Hamiltonian parameters.

[run.json](run.json) records Python 3.12.3, NumPy 2.5.4, SciPy 1.18.1, native BLAS counts, input hashes and execution times. Source extraction additionally requires PyMuPDF, whose version is recorded in the frozen source JSON. The original driver dependencies are the unchanged IBFM kernel and its two imported angular-momentum helper modules; no EM operation is called.

For an exact comparison replay, preserve the relative Wiki layout in a fresh location, copy the frozen source JSON, freeze receipt, extractor, and comparison contract with all hash-locked dependencies, and run:

```bash
python3 -B outputs/l4/20261106-a130-next-evidence/source-chain-replay/compare_fixed_chain.py
```

Output creation is exclusive, so the completed result directory is not a rerun target. Re-extracting the sources creates a new timestamped JSON hash and therefore needs a separately versioned comparison contract/driver binding; do not overwrite the frozen extraction or silently change its expected hash. The native-thread verifier assumes Linux/OpenBLAS. The [artifact inventory](artifact-inventory.json) inventories the read-only inputs and local artifacts.

The narrow task is complete: source-only extraction, frozen identities, one fixed comparison, and reporting of resolved differences. The unresolved boundary is exact author-run identity and empirical state correspondence. No other isotopes, alternate parameter sets, electromagnetic fits, current manuscript edits, frozen-module changes, or commits were made.
