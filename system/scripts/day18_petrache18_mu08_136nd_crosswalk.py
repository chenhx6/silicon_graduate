#!/usr/bin/env python3
"""Raw-anchored table audit and bounded low-spin band-identity crosswalk.

Supersedes result/contract-032 without overwriting either historical artifact.
Rounded 2018 figure labels are manually transcribed visual input, not new
precision measurements; low-spin matches do not certify all higher states.
"""
import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path
import pymupdf

RUN = Path("outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01")
MU = Path("raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/三轴/手征/2008_Mukhopadhyay et al_Electromagnetic transition rates in high-spin bands in Nd 136.pdf")
PE = Path("raw/papers/2018_Petrache et al_Evidence of chiral bands in even-even nuclei.pdf")
HASH_MU = "ea77d7d033051369d19aad2f82a542e91e262eb490d518b246f7f04c2d0dcd2c"
HASH_PE = "d2615fc0d95428b06c056eb8946afa2f62940ce58d79c1fc1cc3f50e19c73ef3"

def table_rows(text):
    table = text.split("Band 1",1)[1].split("h0 is",1)[0]
    bands = table.split("Band 2")
    assert len(bands)==2
    result=[]
    for band,block in enumerate(bands,1):
        lines=[x.strip() for x in block.splitlines() if x.strip()]
        assert len(lines)==25, (band,lines)
        for start in range(0,25,5):
            spin,*values=lines[start:start+5]
            assert re.fullmatch(r"1[5-9]−",spin), spin
            row={"band":band,"spin":int(spin[:-1]),"parity":"-","printed":values}
            for name,value in zip(["tau_ps","BM1_muN2","BE2_e2b2","Qt_eb"],values):
                row[name]=None if value=="–" else float(re.match(r"[0-9.]+",value)[0])
            result.append(row)
    return result

def audit():
    checks=[]
    def check(name,condition,**evidence):
        checks.append({"name":name,"passed":bool(condition),**evidence})
        assert condition, name
    check("MU08 hash",hashlib.sha256(MU.read_bytes()).hexdigest()==HASH_MU)
    check("PE18 hash",hashlib.sha256(PE.read_bytes()).hexdigest()==HASH_PE)
    with pymupdf.open(MU) as d:
        check("MU08 6 pages",len(d)==6)
        rows=table_rows(d[3].get_text())
        check("correct bibliographic identity", "034311" in d[0].get_text())
    with pymupdf.open(PE) as d:
        t=d[4].get_text()
        check("PE18 A actual positive parity and beta", "A\n0.335\n+\n0.21\n21" in t)
        check("PE18 B actual positive parity and beta", "B\n3.419\n+\n0.22\n19" in t)
        check("PE18 D actual negative parity and beta", "D\n1.173\n−\n0.22\n19" in t)
        check("PE18 Dstar actual negative parity and beta", "D∗\n1.346\n−\n0.21\n22" in t)
    check("ten actual TableII rows",len(rows)==10)
    check("actual spin domain 15-19",all(15<=r["spin"]<=19 for r in rows))
    check("Band1 I15 unreported E2/Qt",rows[0]["BE2_e2b2"] is None and rows[0]["Qt_eb"] is None)
    check("maximum actual Qt 2.50",max(r["Qt_eb"] or 0 for r in rows)==2.50)
    byid={(r["band"],r["spin"]):r for r in rows}
    ratios=[]
    for spin in range(16,20):
        a=Fraction(str(byid[1,spin]["BE2_e2b2"]))
        b=Fraction(str(byid[2,spin]["BE2_e2b2"]))
        ratios.append(b/a)
    check("actual ratio sequence",ratios==[Fraction(51,26),Fraction(11,2),Fraction(2,7),Fraction(5,11)])
    check("direction reverses at spin18",ratios[1]>1>ratios[2])
    check("contrast 77/4",ratios[1]/ratios[2]==Fraction(77,4))
    # Manual visual transcription of delta-I=1 labels at Ji15-19. Matching
    # tolerance 1 keV is a declared figure-rounding screen, not a fitted sigma.
    entries=[("Band1","D4",[229.3,308.7,356.2,401.2,435.8],[230,309,357,402,436]),
             ("Band2","D3",[199.6,248.1,344.4,434.2,465.5],[200,249,345,434,466])]
    matches=[]
    for old,new,energies,labels in entries:
        residuals=[round(v-u,6) for u,v in zip(energies,labels)]
        check(f"{old} {new} low-spin rounding screen",all(abs(v)<=1 for v in residuals),residuals_keV=residuals)
        matches.append({"old":old,"later":new,"spins":list(range(15,20)),"parity":"-","old_E_keV":energies,"later_rounded_E_keV":labels,"residuals_keV":residuals})
    check("positive D1 D2 fail parity identity", all(r["parity"]=="-" for r in rows))
    out={"kind":"raw-table-and-bounded-low-spin-identity-audit-not-fit", "sources":[{"path":str(MU),"sha256":HASH_MU,"locator":"PDF2 Fig1; PDF3 TableI; PDF4 TableII"},{"path":str(PE),"sha256":HASH_PE,"locator":"PDF3 Fig1; PDF5 TableI"}],"supersedes":["petrache18-mu08-136nd-result-032.json","petrache18-mu08-136nd-contract-032.json"],"actual_MU08_TableII_rows":rows,"B2_over_B1_exact":[str(x) for x in ratios],"double_ratio_exact":str(ratios[1]/ratios[2]),"low_spin_lineage_matches":matches,"high_spin_boundary":"D3 levels above spin20 show rearrangements; 2018 Fig1 lacks absolute Ex; no automatic all-spin identity","interpretation_boundary":"A/B beta .21/.22 are positive configurations, not MU08 bands; D/Dstar labels are model assignments; no measured absolute-strength or microscopic-causality bridge","independent_experiment_or_CI":False,"checks":checks,"valid":all(c["passed"] for c in checks)}
    path=RUN/"mu08-pe18-identity-correction-result-046.json"
    path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"valid":out["valid"],"checks":len(checks),"ratios":out["B2_over_B1_exact"],"output":str(path)}))

if __name__=="__main__":audit()
