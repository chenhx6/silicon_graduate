# Ce-133 state/edge crosswalk audit 080

**Scope.** This is an independent Day24 audit copy. It reads only the existing Wiki source/project pages and the existing Gizon/Emediato tmp text artifacts. It writes no canonical page, raw file, or Git state. Every claim below remains an audit finding (`needs_review` inherited from the source pages), not a new experimental result.

## Decision rule

A crosswalk row is `bound` only when the source/campaign, excitation energy, Jπ and surrounding links agree. A sub-keV energy difference is only a candidate. A lifetime is bound to the measured **parent** state and to the reported clock definition; an evaluation half-life is not silently called mean τ. Gizon intensities are 55° relative Iγ, while WK22 Iγ are relative table quantities; neither is converted into absolute B here.

## Minimal state ledger

| source state | Ei (keV) | Jπ | role | Ei/Jπ status | τ status |
|---|---:|---|---|---|---|
| WK22 Band4 head | 832.0 | 13/2− | parent | direct Table 5.2 | missing |
| WK22 Band4 | 1200.8 | 15/2− | parent/daughter | direct table node; 1409.8−209.0=1200.8 | missing |
| WK22 Band4 | 1409.8 | 17/2− | parent | direct Table 5.2 | missing |
| WK22 Band4 | 1809.1 | 19/2− | parent | direct Table 5.2 | missing |
| WK22 low reference | 37.2 | 9/2− | daughter | NNDC evaluated; thesis decimal was derived | not a Band4 clock |
| WK22 low reference | 207.4 | 11/2− | daughter | NNDC evaluated | not a Band4 clock |
| WK22 low family | 592.1 | 13/2−? | daughter candidate | derived from 554.9+37.2; not independently observed in the cited WK22 table | missing |
| WK22 low family | 827.1 | 15/2− | daughter | table node | missing |
| WK22 low family | 1344.7 | 17/2− | daughter | table node | missing |

Atomic locators: WK22 source `WK22-03`, `WK22-36`, `WK22-44` ([source lines 50, 122, 199](/workspace/wiki/knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md:50)); NNDC low-state record ([lines 67–70](/workspace/wiki/knowledge/sources/nndc-2011-133ce-low-level-reference-records.md:67)); Gizon historical zero and sequence ([source lines 73–75](/workspace/wiki/knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md:73)).

## Nine WK22 Band4 edges

| parent Ei/Jπ | Eγ (keV) | daughter Ei/Jπ | γ binding | τ needed for absolute B | present status |
|---|---:|---|---|---|---|
| 832.0, 13/2− | 624.6 | 207.4, 11/2− | direct | τ(832.0) missing | observed edge; 794.8 same-parent reference candidate |
| 832.0, 13/2− | 794.8 | 37.2, 9/2− | direct | τ(832.0) missing | reference candidate |
| 1409.8, 17/2− | 209.0 | 1200.8, 15/2− | direct | τ(1409.8) missing | observed edge |
| 1409.8, 17/2− | 577.8 | 832.0, 13/2− | direct | τ(1409.8) missing | out/in reference candidate |
| 1409.8, 17/2− | 582.7 | 827.1, 15/2− | direct | τ(1409.8) missing | observed edge; **582 out/out denominator missing** |
| 1809.1, 19/2− | 399.3 | 1409.8, 17/2− | direct | τ(1809.1) missing | observed edge |
| 1809.1, 19/2− | 608.3 | 1200.8, 15/2− | direct but overlapping 608.7 gate | τ(1809.1) missing | edge/reference; gate assignment unresolved |
| 1809.1, 19/2− | 464.4 | 1344.7, 17/2− | direct | τ(1809.1) missing | observed edge; 982.0 denominator candidate |
| 1809.1, 19/2− | 982.0 | 827.1, 15/2− | direct | τ(1809.1) missing | reference candidate; producer not verified |

The table is the exact nine-row node/edge set already present in the project page ([lines 336–350](/workspace/wiki/knowledge/projects/133ce-thesis-analysis-blueprint.md:336)). The key arithmetic check is `1409.8−592.1=817.7 keV`; it creates an energy-only denominator, not an observed γ line. WK22 explicitly preserves this gap ([source lines 66–67](/workspace/wiki/knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md:66)).

## Historical Gizon ↔ modern energy arithmetic

Gizon's 1974 scheme used a historical 9/2−, 5.4 h reference whose ground/isomer ordering was then unknown; the modern NNDC evaluation gives 9/2− at 37.2(7) keV and 1/2+ ground ([Gizon source line 73](/workspace/wiki/knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md:73); [NNDC lines 67–70](/workspace/wiki/knowledge/sources/nndc-2011-133ce-low-level-reference-records.md:67)). Applying +37.2 keV only as a crosswalk arithmetic gives:

- 170.0+37.2=207.2 keV versus modern 207.4 (−0.2 keV);
- 554.9+37.2=592.1 keV (the 13/2 candidate daughter, not a separately adopted WK22 line);
- 789.7+37.2=826.9 keV versus 827.1 (−0.2 keV);
- 1306.3+37.2=1343.5 keV versus 1344.7 (−1.2 keV);
- 1163.6+37.2=1200.8 keV exactly, but Gizon's 1163.6/608.7 side-state topology and spin assignment do not establish the WK22 1200.8/608.3 Band4 node.

Gizon's own primary reports the 170/554.9/789.7/1306.3/1552.3 sequence and the 1163.6 side state ([source lines 73–75](/workspace/wiki/knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md:73)). Its Table 4 is a 55° relative-intensity list, not a modern parent/daughter ledger; the source explicitly preserves unassigned 624.8, 582.2, 464.6 and 817.3 ([lines 79, 106–114](/workspace/wiki/knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md:79)).

## Old-line disposition (all unresolved for modern binding)

| Gizon old line | Iγ(55°) | nearest WK22 candidate | ΔE old−candidate (keV) | disposition |
|---:|---:|---:|---:|---|
| 624.8 | 3.4 | 624.6 | +0.2 | unassigned; cannot bind 832.0 parent |
| 582.2 | 4.7 | 582.7 | −0.5 | unassigned; cannot fill 582 out/out denominator |
| 464.6 | 5.2 | 464.4 | +0.2 | unassigned; cannot bind 1809.1 parent |
| 817.3 | 3.4 | 817.7 (energy-only) | −0.4 | observed old line, but does not upgrade 817.7 to observed |
| 577.3 | 7.5 | 577.8 | −0.5 | unassigned; no common gate/parent |
| 794.7 | 10.8 | 794.8 | −0.1 | unassigned; no common gate/parent |
| 981.6 | 6.6 | 982.0 | −0.4 | unassigned; no common gate/parent |
| 608.7 | 14.5 | 608.3 | +0.4 | **not bound**: old 1163.6 side-state topology vs WK22 1809.1→1200.8; overlap gate unresolved |

This is why energy matching alone is insufficient. Gizon says the upper sideband has unclear ordering and only a short decay “≤3 ns”, not one τ per modern state ([source lines 75, 111–114](/workspace/wiki/knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md:75)).

## Emediato lifetime crosswalk

Emediato's 1997 RDDS gives mean τ=76(3) ps for 170 keV 11/2−→9/2−, 7.9(5) ps for the 13/2− double placement (555/385), 3.8(8) ps for 15/2− (619/235), and ≤1 ps limits for 17/2− (752/517) and 19/2− (763) ([source lines 60–62, 68–82](/workspace/wiki/knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md:60)). The 170-keV clock can be retained for the low-family 11/2−→9/2− edge because Ei/Jπ and 170.2-keV modern energy agree conditionally; the other clocks are same-family/old-line matches only. None is a τ for WK22 Band4 parents 832.0, 1409.8 or 1809.1. Emediato itself warns that modern 832/1409.8/1809.1 parents cannot inherit these clocks ([line 66](/workspace/wiki/knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md:66)).

## Unresolved boundary and minimum next input

1. **Band4 τ:** a parent-specific lifetime measurement is missing for each of 832.0, 1409.8 and 1809.1; no terminal-state or 131Ce clock can substitute.
2. **817.7:** `1409.8−592.1` is only an energy difference. Need an observed line with parent=1409.8, daughter=592.1 (or an equivalent gate/producer row) and intensity/response definition.
3. **582 denominator:** need the actual same-parent 17/2−→13/2− ΔI=2 out/out line identity, Iγ after the same response/normalization, and branch/ICC/Cov metadata. Gizon 582.2 cannot fill this cell.
4. **Old-line parentage:** gate/coincidence and exact Jπ for the old 624.8/582.2/464.6/817.3 (and near lines 577.3/794.7/981.6) are absent; preserve them as observed-unassigned.
5. **608 overlap:** separate 608.3 from 608.7 in the actual gate/spectrum before using it as a denominator or lifetime edge.

`ledger.json` holds all rows, locators and arithmetic; `tmp/day24-ce133-crosswalk-audit-080/` contains the source manifest, arithmetic output and a copy-free audit README.
