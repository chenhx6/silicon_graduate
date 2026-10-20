#!/usr/bin/env python3
"""Read actual TAC TableI and separate planar from principal-axis geometry.

No original lifetime fit, absolute Qt, B(E2), W.u., or global absence survey.
Old result/contract-042 remain historical and are superseded by this audit.
"""
import hashlib,json,math,re
from pathlib import Path
import pymupdf
RUN=Path("outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01")
HE=Path("raw/papers/2001_Hecht et al_Evidence for chiral symmetry breaking in 136 Pm and 138 Eu.pdf")
PR=Path("raw/papers/gpt/high-spin-20260920/三轴/手征/2006_Petrache et al_Risk of Misinterpretation of Nearly Degenerate Pair Bands as Chiral Partners in.pdf")

def main():
    checks=[]
    def check(name,condition,**evidence):
        checks.append({"name":name,"passed":bool(condition),**evidence});assert condition,name
    hashes={HE:"2f9bd3dce75ec29056ef5a59b26032a6510b7e9dc241a546a3d82a89c7eea161",PR:"ec32a76efbeebf1a924a1c95eb9d404a99158fc9226605414b324e982cfe1d4f"}
    for p,h in hashes.items():check(p.name+" hash",hashlib.sha256(p.read_bytes()).hexdigest()==h)
    with pymupdf.open(HE) as d:
        check("Hecht four pages",len(d)==4)
        text=d[1].get_text();text=text[text.index("TABLE I."):]
        values=list(map(float,re.findall(r"(?m)^([0-9]+\.[0-9]+)$",text)))
        check("69 numeric fields including blank Pm final ratio",len(values)==69)
        raw_rows=[values[i:i+5] for i in range(0,30,5)]+[values[30:34]+[None]]+[values[i:i+5] for i in range(34,69,5)]
        names=["omega_MeV","theta_deg","phi_deg","I_hbar","BM1_over_BE2"]
        rows=[dict(nucleus="136Pm" if i<7 else "138Eu",**dict(zip(names,row))) for i,row in enumerate(raw_rows)]
        author_prose=d[3].get_text()
        check("mean field missing doublet mixing explicit", "cannot account for the mixing" in author_prose)
    check("Pm final actual row",raw_rows[6]==[.425,89.,0.,18.51,None])
    check("Eu final actual row",raw_rows[-1]==[.350,68.40,0.,13.50,1.2])
    check("phi zero in both final sampled rows",rows[6]["phi_deg"]==rows[-1]["phi_deg"]==0)
    def axis_distance(row):
        th,ph=math.radians(row["theta_deg"]),math.radians(row["phi_deg"])
        n=[math.sin(th)*math.cos(ph),math.sin(th)*math.sin(ph),math.cos(th)]
        check(row["nucleus"]+" unit vector",math.isclose(sum(x*x for x in n),1.,abs_tol=1e-12))
        return math.degrees(math.acos(max(abs(x) for x in n)))
    distances={row["nucleus"]:axis_distance(row) for row in [rows[6],rows[-1]]}
    check("Pm conventional spherical distance 1 degree",math.isclose(distances["136Pm"],1,abs_tol=1e-10))
    check("Eu conventional spherical distance 21.6 degrees",math.isclose(distances["138Eu"],21.6,abs_tol=1e-10))
    with pymupdf.open(PR) as d:
        check("Petrache four pages",len(d)==4)
        p2,p3=d[1].get_text(),d[2].get_text()
        check("Petrache offdiagonal and spin dependence assumptions present", "diagonal E2 matrix elements" in p2 and "spin dependence" in p2)
        check("Petrache E2 transition moments definition present", "E2 transition moments" in p3 and "2.0(4)" in p3)
    # New explicitly chosen design: each band's same-parent lifetime cancels
    # in the ratio. Multipole fractions and branch definitions are held fixed.
    rate_ratios=[];strengths=[]
    for tau in [.4,1.2,3.0]:
        m1=.8/tau;e2=.2/tau
        rate_ratios.append(m1/e2);strengths.append({"chosen_tau":tau,"M1_rate":m1,"E2_rate":e2})
    check("same parent lifetime cancels without other band Qt",max(rate_ratios)-min(rate_ratios)<1e-12)
    check("equal ratios coexist with unequal absolute rates",strengths[0]["E2_rate"]!=strengths[-1]["E2_rate"])
    out={"kind":"raw-model-table-and-conditional-geometry-not-lifetime-fit","sources":[{"path":str(p),"sha256":h} for p,h in hashes.items()],"supersedes":["hecht01-136pm-138eu-result-042.json","hecht01-136pm-138eu-contract-042.json"],"actual_TableI":rows,"conventional_spherical_nearest_axis_distance_deg":distances,"geometry_scope":"phi0 is planar; Eu theta68.4 conflicts with generalized principal-axis prose; spherical-coordinate distance is a diagnostic, not new TAC solution","chosen_same_parent_rate_design":strengths,"Petrache_ratio_scope":"2.0(4) E2 transition-moment ratio from branching/spacing and two-band assumptions; not direct lifetime-derived twofold beta","actual_lifetime_or_CI":False,"global_lifetime_absence_verified":False,"checks":checks,"valid":all(c["passed"] for c in checks)}
    path=RUN/"hecht01-planar-reference-correction-result-047.json";path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"valid":out["valid"],"checks":len(checks),"distances":distances,"output":str(path)}))
if __name__=="__main__":main()
