# CH16 / EM Part II: bounded public-producer readiness check

**Outcome:** no verified author model producer, complete numerical V/B grid, solver input deck, basis-cutoff/endpoint-regularization specification or formal supplementary dataset was established by this bounded check. The complete official Part II author archive contains one article TeX source and four EPS figures. The CH16 archive could only be received partially from two distinct official routes; its complete main TeX was recovered as inert text, but the unseen archive tail prevents a full-content absence claim. These are scoped retrieval results, not proof that no such materials exist elsewhere.

No unknown code, TeX or PostScript was executed. No archive member was extracted using its supplied path. Only regular members were read as bytes/text; no symbolic links or script execution were followed. No new session/run/agent/credit, canonical/raw/PLAN/Bib/Git change. All artifacts stay in worker015 and `tmp/day24-chiral-producer-readiness-015/`.

## Actual entry points and three-route limit

First, existing012/014 temporary directories and receipts were inspected. They contained article PDFs, page extracts/renders and metadata, but no existing author-source archive. The already obtained PDF identities remain CH16 arXiv1609.06967v2, DOI10.1103/PhysRevC.94.044301, and Part II arXiv1809.04418v2, DOI10.1103/PhysRevC.98.064302. No article PDF was downloaded again.

Exactly three new HTTP routes were used. Headers and response bytes are retained, and their hashes/statuses are in `receipt.json`.

|Official route|Actual result|Completeness and interpretation|
|---|---|---|
|`https://arxiv.org/src/1609.06967v2`|HTTP200,application/gzip; curl28 after45s,1863616bytes received of advertised5699559.|Incomplete gzip; safe streaming recovered complete mainTeX and an initial sequence of figure PDFs. No complete-archive hash or exhaustive inventory claimed.|
|`https://arxiv.org/src/1809.04418v2`|HTTP200,application/gzip; curl0,121695bytes.|Complete gzip/tar; all five regular files inventoried and hashed.|
|`https://export.arxiv.org/e-print/1609.06967v2`|Redirected to export.arxiv.org/src/1609.06967v2; HTTP200,application/gzip; curl92 HTTP/2PROTOCOL_ERROR,3145728bytes.|A distinct official mirror route, also incomplete; more figure members were received but no full archive. No failed URL was repeatedly retried.|

The third route exhausted the allowed search budget. Publisher pages/supplement endpoints and institution repositories were not separately queried in this worker; no claim is made about their uninspected content. No broad anonymous-repository search was performed. A future task could check a specifically identified publisher supplement or author-linked repository, but it must establish paper/version linkage before being called the producer.

## Version/header/hash ledger

|Object|SHA256|Status|
|---|---|---|
|CH16 first partial HTTP response|`917ca4c2598e711a66670ef8575176fb06e5b93f902181684c31e680e6aa05de`|Hash only of1863616received bytes; not the archive hash.|
|CH16 mirror partial HTTP response|`b3a7c830a42e44ed8fd1f9658b63e5f87bda75fec86bec0532e9519726344196`|Hash only of3145728received bytes; not the archive hash.|
|Complete Part II source gzip|`b2ed43e6b61dfc867ac8159059a9683e656a6feac06d17db45944d6fcf3d1275`|Complete official version-specific source archive.|
|CH16 regular member `Paper2DCH.tex`,95702bytes|`30c5612025c349b8f791c497a02d2514a0527e965d64957b7f1dabd1219e8394`|Complete member obtained identically in the two partial streams; title/authors match the paper.|
|Part II regular member `EM.tex`,79259bytes|`ce27435b6d600ae8172c0428ac83b020fc4a213d798c6f704879f86c11d87ee7`|Complete raw TeX bytes. Decoded text used for inspection has a separate hash because some comments are not UTF-8.|

Header paths, header SHA256, content-type/content-length/status lines are in `receipt.json`. Complete per-member Part II hashes are in `partII-source-complete-inventory.json`. Partial CH16 member inventories explicitly mark completeness and parsing termination; they are not exhaustive catalogs.

## What the archives actually supply

The complete Part II archive has exactly:

- `EM.tex` (79259bytes);
- `fig1.eps` (129223bytes);
- `fig2.eps` (46143bytes);
- `fig3.eps` (141387bytes);
- `fig4.eps` (55145bytes).

All are regular files. There is no numerical-program file, input deck, grid data file, README, repository link or separate supplement within this complete archive. The EPS members are figure artifacts; their presence does not identify the scientific code that generated them. They were not interpreted or executed.

CH16's complete mainTeX identifies *Two-dimensional collective Hamiltonian for chiral and wobbling modes* at source line54 and the expected five authors at lines56–71. It references only figure PDFs via46 `includegraphics` occurrences, including commented/duplicate figure-source alternatives. No `input`/`include` command for a separate data or solver file was found. The successfully read archive prefix consists of that mainTeX and figure PDFs; the last incompletely read member in the longer mirror stream is `fig2f.pdf`. The archive tail is unknown.

Part II's mainTeX identifies *Two-dimensional collective Hamiltonian for chiral and wobbling modes II: Electromagnetic transitions* at line54, with Wu/Chen/Zhao/Zhang/Meng at lines56–76. Its only included files are the four named EPS figures. Thus these archives are demonstrably article-production source packages; they do **not** thereby qualify as the numerical collective-Hamiltonian producer.

Both complete mainTeX texts were scanned as inert text for supplement/data/repository/code/grid/mesh/cutoff/regularization/convergence indicators. No hits were found for the listed scoped terms; literal terms and includes are preserved in `source-text-scan.json`. This is an entry-point check, not a claim that every method detail has been semantically excluded by keyword search. The actual bodies were already inspected by012/014; this task does not repeat their paper-reading unit or convert formulas/plots into inferred input jobs.

Both sources literally use `\date{\today}` (CH16line79;PartIIline89). This is article typesetting machinery; it supports keeping the CH16PDF's2022typeset date separate from its2016arXiv version/publication identity. It does not create a new scientific edition or supply a code revision.

## L4 readiness boundary and stopping point

Available now: version-linked article PDFs; complete TeX bodies; complete Part II figure-source archive; partial CH16 figure sources; equations and paper-level parameter descriptions. These support source-grounded formula/representation checks and conditional independent implementations.

Not established: an executable author solver with revision/license and paper association; complete V(θ,φ)/B_ab(θ,φ) grids and units; occupation/gap tracking; basis sizes/cutoffs; pole/ridge regularization and endpoint flux/domain; quadrature mesh/convergence; exact output-to-figure mappings; or a reproducible actual job/input/output manifest. No field is filled by inverting plots or recreating a plausible script. The prior114 producer is not used.

The allowed three official routes are complete as retrieval attempts; the CH16 whole archive remains transport-incomplete. The bounded task therefore stops with **actual producer not established**, complete and partial artifacts explicitly separated, and the precise missing inputs recorded. No additional failed-endpoint polling or fabricated actual-job reconstruction is warranted.
