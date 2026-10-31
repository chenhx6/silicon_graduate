# 133Ce: A13 high-spin MχD families versus WK22 low-lying Band1/4

Bounded worker `ce133-highspin-006`, existing Day24 run. All new conclusions are source-grounded self-audit candidates, `needs_review: true`; existing source review flags are unchanged. No shared canonical/raw/PLAN/Bib/Git writes, new agent/run/session/credit, external retrieval or download. Reusable findings require parent integration into `knowledge/`; this report remains an audit artifact.

**Result:** A13's **Band4** has the low-lying negative-parity sequence corresponding at family/topology level to **WK22 Band1**. A13's negative-parity MχD candidates are **Bands5/6**, not WK22's Bands1/4. Their observed connecting network reaches the low-lying sequence, but connected states are not identical states, nor does a shared decay path establish a shared configuration. No match of WK22's new low-lying Band4 nodes or624.6/582.7/464.4 links to the A13 MχD pair is established. An energy-reference discrepancy prevents silently copying TableI head energies into WK22's ground-referenced Ex ledger.

Machine audit: `crosswalk-ledger.json` (17 selected observed links, nine WK22 nodes compared, source/version hashes, literal heads and conditional energy paths).

## Actual versions and locators

|Version actually read|Raw identity|SHA256|Locator mapping|
|---|---|---|---|
|CHORUS accepted manuscript,8PDF pages|`raw/papers/2013_Ayangeakaa et al_Evidence for Multiple Chiral Doublet Bands in Ce 133 2.pdf`|`91ec60dfa43e7d8748276e18327028d8eabdf6c5047682726b0da4a656d5e837`|PDF1cover;PDF2printed1;PDF3printed2/Fig1;PDF4printed3/Fig2;PDF5printed4/TableI/Fig3;PDF6printed5;PDF7–8references|
|PRL110,172504 five-page electronic reprint|`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/三轴/手征/实验/2013_Ayangeakaa et al_Evidence for Multiple Chiral Doublet Bands in Ce 133 1.pdf`|`3c5a3d7c543140ee25f7cb09376d5aeee760c8ac50c76edd466a010d610c2d0f`|PDF1–5=printed172504-1…-5;Fig1onPDF2;Fig2/3onPDF3;TableIonPDF4|

Same title, author list, DOI10.1103/PhysRevLett.110.172504 and article; the accepted manuscript is dated March20,2013 and the reprint gives publication April24,2013. These are the same-paper versions, not independent experiments. The source page's early “canonical five pages” wording must not replace the actual8-page file mapping.

They are **not numerically identical at every scheme label**: accepted Fig1 prints602keV forB5 49/2−→47/2− and1174keV for49/2−→45/2−; reprint Fig1 prints600 and1173keV. Fresh visual `accepted-pdf03.png` versus `reprint-pdf02.png` confirms both. No cause or correction is inferred. This report uses the reprint for the main observed-link ledger and separately records these differences. Reference numbers also change; A13's37.2keV caption citesRef31 in the accepted version andRef46 in the reprint.

## What is observed and what is interpreted

Direct experimental reporting (reprint172504-1; acceptedPDF2/printed1): two ATLAS experiments,112MeV116Cd(22Ne,5n)133Ce, Gammasphere, combined approximately4.1×10^9 four-fold-and-higher prompt events; DCO and where practical angular distributions support new level spin/parity assignments. This is a different reaction/facility acquisition from WK22's57MeV125Te(12C,4n), AFRODITE (WK22printed50/PDF61).

|A13 pair|Head records actually supplied|Observed-link support|Author/model layer|
|---|---|---|---|
|Positive Bands2/3|TableI givesBand2,19/2+,Ex2.378MeV. Fig1showsBand3's lowest partner level19/2+; noBand3 decimal Ex inTableI. Text says both built on19/2+ and extended to33/2+.|B3→B2 links328/338/391 assignedM1/E2;544/615 assignedE2 (172504-2).|π[(1g7/2)−1(1h11/2)^1]⊗ν(1h11/2)−1 is an author configuration assignment supported byRMF and network/systematics; it is not a direct particle count. TPRM usesRMFshape and fitted rotor inertia, withξ=.7 for this pair (172504-4).|
|Negative Bands5/6|TableI usesBand5,29/2−,Ex3.734MeV. Fig1also drawsB5's lower23/2−,25/2−,27/2− levels. Band6's lowest drawn level is29/2−; noBand6 decimal Ex inTableI.|Strong/weak interlinks andinbandsequences;B6entirelynew, priorB5assignments confirmed and high end extended (172504-2…-3).|π(1h11/2)^2⊗ν(1h11/2)−1 assigned to5/6; proton-pair rotational alignment after a crossing is the author's configuration explanation (172504-3bottomright). It does not turn every lower drawn state into a measured3qp state.|

“Bandhead” inTableI is the state selected for the configuration comparison; it must not be replaced by “lowest line drawn anywhere in this column.” Likewise theoretical statesa/b and their calculatedEx1.71/3.78MeV are not additional observed heads. ModelA atEx0.00 is a theoretical reference; it is not automatically the true1/2+ ground-state node or an independent measurement of the9/2− isomer.

Reprint172504-4 interprets Bands5/6's approximately400keV separation and trends as chiral vibration and calls them zero-/one-phonon, respectively. Those labels are author/model interpretation, not a measured phonon count or evidence that WK22's low-lyingBand4 is the same excitation. The positive pair's approximately100keV separation and modelξ treatment are separate. The paper explicitly says lifetime measurements were not feasible for the reported bands (172504-3; acceptedPDF4). It offers135Nd analogy as support; no133Ceτ,Qt,g,absoluteB orδ value is transferred here.

## Negative pair: actual selected edges

All following endpoints are visually read from reprintFig1,172504-2; acceptedFig1/PDF3 has the same selected interlinks. Fig1inset supports the gated-line identity; it supplies no complete branching probability or lifetime. Individual multipoIarity claims below are only those explicitly checked in172504-3.

|Band6 parentJπ|Band5 daughterJπ|Eγ,keV|Evidence status|
|---|---|---|---|
|29/2−|27/2−|669|observed/placedFig1; not separately assigned multipolarity here|
|31/2−|29/2−|711|M1/E2 from angular distribution|
|31/2−|27/2−|952|observed/placedFig1|
|33/2−|31/2−|779|M1/E2 from angular distribution|
|33/2−|29/2−|1074|DCO consistent with stretchedE2|
|35/2−|31/2−|1146|DCO consistent with stretchedE2|
|35/2−|33/2−|804|observed/placedFig1|
|37/2−|35/2−|855|observed/placedFig1|

B6's29/2−→45/2− ladder is shown with283,363,367,442,423,468,491,558keVΔI1 edges;283 is31/2−→29/2−,363 is33/2−→31/2−, etc. The text's forward/90° intensity-ratio claim specifically enumerates363/367/442/423/468/491; do not extend that quoted measurement list to every edge simply because it lies in the ladder. No individualδ orfullresponse was obtained in this worker.

Two directly traceable links from the lowerB5 sequence intoA13B4 areB5 23/2−→B4 23/2−,750keV andB5 23/2−→B4 21/2−,1037keV. These establish a physical decay route to the low-lying family. They do not identify B5 23/2− withB4 23/2−;750keV is their separation, not a zero difference. TheB5 23/2−→25/2−→27/2−→29/2− upward construction uses the actually drawn140/155/240keV steps. This is a network connection to the high-spin29/2− comparison node, not a direct observation of pair-breaking occupation.

## Energy-zero audit: preserve literal and conditional values

Fig1caption directly states that the lowest9/2− level is an **isomer at37.2keV above ground**. This is directA13caption evidence for that state identity. In WK22,37.2 remains derived fromTable5.1(207.4−170.2 and592.1−554.9) withFig5.1rounded37; A13does not retroactively makeWK22Table5.1print a decimal37.2 row.

The following are exact sums of the **integer diagram labels**, not remeasured Ex values or uncertainty estimates:

|Target|Path upward fromA13Fig1lowest9/2−|Sum,keV|TableIliteralEx,keV|Conditional sum+caption37.2,keV|
|---|---|---:|---:|---:|
|B2 19/2+|B4 9→13:555;13→17:751;B4 17→B2 19:1072|2378|2378|2415.2|
|B5 29/2−,pathA|B4 9→13:555;13→17:751;17→21:856;21→23:287;B4 23→B5 23:750;B5 steps140+155+240|3734|3734|3771.2|
|B5 29/2−,pathB|555+751+856;B4 21→B5 23:1037;B5steps140+155+240|3734|3734|3771.2|
|B3 19/2+|555+751;B4 17→B3 19:1159|2465|not supplied|2502.2|

BothTableIexperimental numbers equal the scheme sum **above the isomer**, while adding the caption's37.2 produces the last column. This is a source/reference boundary requiring an explicit energy-zero/decimal-level ledger. This worker **does not decide** thatTableIuses a particular zero, that it contains an error, or that the conditional values should replace its printed values. PreserveTableIas2.378/3.734MeV with its literal context, and preserve scheme-ground reconstruction as conditional. Integer labels have no per-line errors in thisFig1; no new precision orCI follows from their sums.

ForB6 29/2−,even an isomer-relative conditional reconstruction has two paths:3734+711−283=4162keV versus3734−240+669=4163keV. Retain both; the1keV difference prevents claiming a recovered exact decimal head. It may be consistent with integer presentation but no actual error budget was supplied here. Neither path is aTableIentry. No syntheticB6 “measuredEx4162” node is created.

Traceable crops: `negative-scheme.png` (reprintPDF2nativeclip[312,405,590,667]);`positive-head-links.png` ([199,551,372,666]);fullreprintPDF2andPDF4renders;acceptedPDF3render. These retain arrow endpoints and caption/Tableliteral context. The1072keVlink used above is B2's19/2+→B4's17/2−; the nearby1459keVarrow begins at a separate17/2+level and cannot replace it merely because the labels overlap in a compact scheme.

## Compare against the actual nine-node WK22 ledger

WK22 decimals are from worker005Table5.1/5.2ledger. A13has no decimal Ex row for these higher low-lying nodes; “A13sum” below is a conditional sum of integerFig1labels starting at its caption37.2. It is retained only to check identity, not promoted to an adopted experimental energy.

|WK22 node|A13candidate|A13conditionalEx,keV|Conclusion|
|---|---|---:|---|
|B1,9/2−,37.2derived|B4lowest9/2−isomer|37.2directcaption|Strong state-identity support; source provenance differs.|
|B1,11/2−,207.4|B4,11/2−via170|207.2|Same family/local network; exact decimal match not certified.|
|B1,13/2−,592.1|B4,13/2−via555|592.2|Same family/local network; retain 0.1 keV display difference.|
|B1,15/2−,827.1|B4,15/2−via555+235|827.2|Same family/local network; exact decimal match not certified.|
|B1,17/2−,1344.7|B4,17/2−via555+751(or555+235+516)|1343.2|1.5 keV difference; 751/516 versus WK22 752.6/517.6 is not ordinary nearest-integer rounding. Preserve without declaring experimental error.|
|B4,13/2−,832.0|none established|—|Do not merge with A13 B4 13/2− near 592, or with MχD 5/6.|
|B4,15/2−,1200.8|none established|—|No corresponding new yrare-node crosswalk established.|
|B4,17/2−,1409.8|none established|—|Not A13 B4 17/2−, nor high-spin MχD head.|
|B4,19/2−,1809.1|none established|—|No identity established by shared negative parity or band number.|

The shared 170/385/555/235/620 local network, spin/parity and low 9/2 isomer support the **family crosswalk WK22 B1 ↔ A13 B4**. The differing 516/751 labels prevent certifying every decimal edge as identical from these two schemes alone. A13's B1 is a positive-parity high-spin structure and its B4 is the negative-parity low sequence; neither number can be copied into WK22 without source scope. A13's B2/3 positive pair is also not WK22's positive g7/2 Band2 solely because of “Band2.”

The WK22 new B4 target parents 13/2−,17/2−,19/2− are outside A13's negative MχD 29/2− comparison-head region; its 624.6/582.7/464.4 selected links are not identified in A13 Fig1. This scoped absence is not a claim that no additional data exist. The 582 out/out cell and energy-only 817.7 remain unchanged. A13 has other 608/338/391 labels in different state/band neighborhoods; matching Eγ alone would create false identities.

## Independence, transfer and stopping boundary

A13 accepted/reprint versions share the combined two ATLAS experiments. They add no independent experimental vote. WK22's different reaction/facility establishes a distinct described acquisition; it does not establish independence of every adopted known level, normalization, input or calibration. WK22 states no new Band1 transitions (printed51/PDF62), cites A13 as Ref6 (printed108/PDF119), and shares Ma1987 *Rotational bands in 133Ce* with A13: WK22 Ref47 (printed114/PDF125), A13 reprint Ref33 (172504-5; accepted Ref34). This is explicit literature dependency. Event-level run IDs, which old values were adopted, reused fits/covariance, and relationships to A13/2016 datasets were not established here.

Transfer only source-scoped node/edge matching, the energy-zero check, full-network rather than band-number comparison, and separation of observed links from configuration/crossing interpretation. WK22's continuation to 35/2− does not prove it has measured the A13 proton-pair crossing or 3qp partner family. Reproducing/comparing that claim would require an explicit state crosswalk, actual 3qp space/blocking/pairing/residual interaction and model producer, and appropriate independent observables; a fixed one-qp QTR component change alone is not that producer.

Bounded task complete: main A13 experimental/model argument and key scheme/TableI read, versions and hashes verified, fresh critical visual checks completed, nine WK22 nodes compared, and new source-zero/version boundaries preserved. No τ/δ/g/Qt were filled. Further decimal mapping would require the actual level/energy-reference ledger; none was invented or repeatedly searched for. Parent retains the authorized Day24 continuous-learning interval and canonical-write ownership.
