# Day24 direct-source audit 091: 133Ce lifetime and high-spin sources

**Result: required corrections found; this is not a no-op.** Read-only audit of four canonical source pages against the actual PDFs. No canonical/raw/Git/producer file was changed. All proposed replacements remain direct-source self-audit, not human-reviewed status.

## Source identity and reproducibility

`tmp/day24-ce133-lifetime-source-audit-091/input-manifest.json` records all four hashes, sizes and exact extracted texts. Two frontmatter `actual_body_file` values point to nonexistent files; byte-identical-to-declared-hash originals were located and audited instead:

| Source | Audited original | SHA-256 | Pages |
|---|---|---|---|
| Joss 1998 | `tmp/day24-ce133-independent-primary-079/1998Jo16-aps.pdf` | `81b6ace5d9ee867220c5425e7f3d9ae4f5074d9484f7063fd04fd137b0deea0a` | 4, printed3219–3222 |
| Emediato 1997 | `tmp/day24-emediato1997-ce133-rdds-072/publisher-direct-pdf.pdf` | `39f6d6a7bb4e2da109504aaab2c22c52fa8b1465b860c1dfd58937bc404869df` | 4, printed2105–2108 |
| Hauschild 1995 | `tmp/day24-ce133-primary-followup-081/1995Ha34-full.pdf` | `ce219bb983b42a15cb634f95e9ad99bcfbc8442bc179a5e5f0e613b9ac9958fb` | 6, printed438–443 |
| Hauschild 1996 | `tmp/day24-ce133-independent-primary-079/1996Ha20-aps.pdf` | `560215bbff5898a3e304f4219f35f628b3a4bd03c87ed1745dc25ae147162872` | 7, printed613–619 |

All four texts were extracted directly from these originals. Targeted image checks covered Joss PDF2 TableI and fitting paragraphs, Emediato PDF3 TablesII/III and E1 conflict, Hauschild1995 PDF1 author list and PDF5 spin/Table1 paragraphs. Hauschild1996 original seven-page text and all relevant methods/configuration paragraphs were reread; existing original page images remain available. This is not a new blanket visual certification of every figure.

## Required corrections

| ID | Affected source location/claim | Exact original locator and evidence | Required correction |
|---|---|---|---|
| A091-01 | Joss frontmatter line24 | Named `attachment-object-response.pdf` does not exist; audited PDF above matches source hash and120604bytes. | Point `actual_body_file` at the extant exact-hash PDF. |
| A091-02 | Emediato frontmatter line24 | Named `attachment-object-response.pdf` does not exist; audited direct PDF matches source hash and102259bytes. | Point `actual_body_file` at extant exact-hash PDF. |
| A091-03 | Joss Experimental/Fit Contract line50 | PDF1/3219 right column first sorting paragraph explicitly: ratios5:4:1 **for132Ce,131Ce,133Ce respectively**. | Replace ambiguous/reversed `133Ce通道相对132/131Ce约5:4:1` with `132Ce:131Ce:133Ce=5:4:1；133Ce为较弱3n通道`. |
| A091-04 | Joss lifetime ledger line74 | PDF2/3220 TableI visually:999.3keV τSF=`0.49±0.01ps`. | `.49(.10)` → `.49(.01)`. Original print and OCR agree. Do not silently inflate this literal table value to enforce the prose8% rule; preserve that apparent original table/prose tension. |
| A091-05 | JO98-D24-003 line60 | PDF2/3220: fitted errors from MINOS; minimum acceptable error limit8% with smaller MINOS errors adjusted upward. PDF4/3222 left column lower paragraph separately warns absoluteQt uncertainties≈10–15% from recoil stopping in target foils. | Withdraw `作者最终误差含约10–15%阻停系统学`. Say `作者报weightedQt=2.2±0.1eb；拟合误差按MINOS并设8%下限；绝对Qt另有约10–15%阻停不确定性，不能由±0.1宣称已含该项`. Do not call table errors pure counting-statistical errors. |
| A091-06 | JO98-D24-002 markdown row line59 | Source table has6 columns but this row7: extra `direct` shifts TableI locator into needs_review and true beyond header. | Delete extra `| direct |` so row has6 cells and locator=`TableI PDF2/3220`, needs_review=true. |
| A091-07 | JO98-D24-008 line65 and TableI ledger | PDF2/3220 TableI all four Jπ pairs are bracketed: `(43/2−→39/2−)`, `(47/2−→43/2−)`, `(51/2−→47/2−)`, `(55/2−→51/2−)`. Same page paragraph afterEq2 says spins of both side-feeding and triaxial bands estimated, no linking transitions found. | Replace `高spin标签多为括号估计` with `TableI四条初末Jπ均括号估计`; add exact parent/daughter columns to ledger if canonical editor wants the table self-contained. Correct locator fromPDF3–4 toPDF2/3220 TableI/Eq2 paragraph. |
| A091-08 | Emediato Scope line42; EM97-D24-002 line59 | PDF2/2106 has **Fig2 level scheme, Fig3 decay curves**, TableI132Ce check; PDF3 TablesII/III. PDF2: `decay and growth curves for14 transitions` fitted simultaneously,340points22parameters. | Scope figures should beFigs1–3, notFig1–2. Replace `14条曲线` with `14条跃迁的decay/growth（shifted/unshifted）曲线`; preserve340/22/χ²ν2.1. PDF4 is references only, so EM97-002 method locator shouldPDF1–2, notPDF4. |
| A091-09 | Emediato EM97-D24-008 line65 and EM97-D24-009 line66 | PDF3/2107 TableIII and right-column `Finally` paragraph are on the **same page**. Table17/2+1269E1=23μWu,19/2+954E1=42μWu; prose names19/2+ then17/2+ and says23then42 respectively. PDF4/2108 onlyrefs. | Keep the genuine table/prose conflict but change `PDF4 discussion` → `PDF3/2107 right-column Finally paragraph` in both relevant rows. |
| A091-10 | Hauschild1995 authors line12 | PDF1/438 image has14authors in order: K.Hauschild,R.Wadsworth,R.M.Clark,**P.Fallon,D.B.Fossan,I.M.Hibbert,A.O.Macchiavelli,P.J.Nolan,H.Schnare,A.T.Semple,I.Thorslund,L.Walker,W.Satula,R.Wyss**. | Replace copied1996-style12-person list with exact1995list; restoreW.Satuła/R.Wyss and correct order. |
| A091-11 | HA95-D24-003 line55 | PDF3/440 initially assumes4ℏ unseen links giving43/2–105/2,37/2–99/2,45/2–101/2. PDF5/442 left upper paragraph later adopts initial43/2 forBand1 and**41/2forBand2**, sayingBand2 links would contribute6ℏ rather than earlier4ℏ. | Retain initial conditional range, explicitly add later41/2Band2/6ℏalternative used forRouthian comparison; current single-range summary omits this important source-internal refinement. No exact spin certification follows. |
| A091-12 | Hauschild1996 Summary line45 | PDF1–2/613–614 repeats same116Cd+22Ne120MeV,2×500μg/cm² targets,31HPGe,1.5×10^9events as1995PDF2/439; PDF2 says6new sequences in addition to3SDbands alreadyreportedRef11; Ref11PDF7/619=1995Ha34. | Replace `独立Gammasphere反应` with `与1995Ha34同一116Cd+22Ne/早期Gammasphere数据集的新增带分析，独立于Joss1998反应`. Current later independence paragraph is correct; eliminate summary-level ambiguity. |
| A091-13 | HA96-D24-002 line54 | PDF2/614 Results right upper paragraph:Band1≈10%;Band2≈2%;Band4≈1.5%;Bands3,5,6,7**each≈0.5%**. | Replace `带3/5/6/7约.5–2%` → `带3/5/6/7各约.5%`. |
| A091-14 | HA96-D24-002 andSummary DCO boundary | PDF3/615 lower left: presentGammasphereDCO cannot be done due90°statistics; **priorRef7 intensity ratiosI(136°,57°)/I(57°,136°) already indicateΔI2 forBand1**; othernewbandsassumedΔI2; stretchedE2 used in spin estimates. | Add priorBand1ΔI2support; distinguish no presentDCO from no evidence ever. Keep unproved stretchedE2 for presentanalysis andotherbands. |
| A091-15 | HA96-D24-003 line55 | PDF2/614 lastResultsparagraph andPDF3/615 top left concern **triaxialBand1/otherΔEγ≈100keVbands→knownnormal-deformedstates**. This is not a claimedSD→lowbandlink in thispaper. | `缺SD/低带link` → `ΔEγ≈100keV三轴带到已知低能normal-deformed态的link未定`; retain isomer speculation as author suggestion, not measured isomer. |
| A091-16 | HA96-D24-004 line56 | PDF5/617 §C assignsBands3/5**7qp**ν(h11/2)^3⊗π(h11/2)^2⊗π(g7/2)^2; PDF6/618 §D/summary assignsBand6 after≈0.6MeVbackbend**7qp**ν(h11/2)^2⊗νs1/2⊗π(h11/2)^2⊗π(g7/2)^2; §EBand7**5qp**ν(h11/2)^2⊗νs1/2⊗πh11/2⊗πg7/2. | Replace blanket`Band6/7其它5qpvariants` with separateBand6pre/postbackbend versusBand7; explicitly nameBand6high-frequency7qp. All remaintentative. |

## Qt arithmetic and uncertainty boundary

Direct TableI Qt values are1.94±.10,2.65±.16,2.66±.21,2.15±.15eb. Under an explicitly **independent diagonal-error arithmetic assumption**, inverse-variance mean=2.198965683eb, standarderror=.069642429eb. Thus source's2.199(.070) arithmetic is correct, but it is not a reconstruction of author's complete covariance or quoted±.1eb. The four values giveχ²=19.5792for3dof against a constant under the same diagonal assumption. This is a useful warning against treating `.070` as a validated constant-band experimental uncertainty; it is not evidence for a physicalshapechange without correlations/systematics. NoBirgescaling ornewmeasurementerror is recommended. A10–15% absolute stopping scale at2.2eb is roughly.22–.33eb, numerically larger than.1eb, so the old“final±.1includesstopping”claim is untenable.

The literal .49±.01psτSF is <8%; the original8%minimum-error prose does not uniquely tell us why that row differs. Preserve source literal and flag tension; do not revise the primary table.

## Checks that support the current scientific ledger

- EmediatoPDF3TableII visually confirms76±3,7.9±.5,3.8±.8ps,≤1.0limits and65±2mWu,17±3Wu,45±4mWu,52±15Wu,56±15mWu,≥65/≥40/≥65limits. No parentclock should be transferred to modernBand4bynearE.
- EmediatoPDF3TableIII confirms5.3±.6,4.5±.5,5.3±.6ps and positiveparity17/2+,19/2+,21/2+ **without brackets**. PureM1extraction,385/235doubleplacementsandE1table/proseorderconflict remainvalid.76ps×ln2=52.679ps supports evaluatedT1/2conversion; it is not a second clock.
- EmediatoPDF2/2106 specifies intensity errors include statistical **and peak-fitting** errors;MINOSintervals useΔχ²=1while refittingotherparameters. Do not call all quoted errors purestatistics or a complete stopping/systematicbudget.
- Jossfourτ/Qtvalues,β2=.186(.007),conditionalγ−83°conversionandT(E2)≈35Wucomparisons survive;JO98-D24-006 equationexplanation beginsPDF3butβ2valueandnohexadecapoleassumption continuePDF4/3222, so preferPDF3–4/TableII/Eq3locator.
- Hauschild1995/1996data dependence and distinct normaltriaxialvsSDbandsets must remain. No newτ/Qtwere measured in either spectroscopypaper. EarlierQtmeasurements quoted by1996introduction are cited inputs, not absence ofalllifetimeknowledgein133Ce.

## SI and original-scope boundary

No new network or SI acquisition was done in091. A mainPDF cannot establish that noSIexists. Keep the restrained wording“本轮所查入口未识别SI”; do not replace it by“原文无SI”or“全部supplementarymaterials已核”. In particular081manifest explicitly used`--no-si`; the1995XML attachmentlist containsMAINandALTIMGsymbolassets, not an identifiedSIobject. This bounds what081actuallychecked, rather than retroactively claiminganSIsearchwasperformed. For1996there is no table in the7-pagepaper (Figs1–9); replaceScope“和表格”withtheactualfigure/bodylistifmakinganexhaustivecoverageclaim.

## Handback

Canonical editor should apply corrections above and propagate the correctedJossτSFanderrorboundarytoanyderivedledgers. Thisauditdoesnotsupplyrawcounts,fitCov,responsekernelsoractualproduceroutputs. Retrievalmetadataandconditionalarithmeticareintheallowedtmpdirectory;reading/reportingdoesnotadvancecoursecreditorcertifymodelinterpretations.
