#!/usr/bin/env python3
"""New primary-table controls preserving upper-limit and model scopes.

No lifetime/branch CI, actual producer reconstruction, or structural verdict.
Printed B, branch and lifetime values share data. Their closure is diagnostic.
"""
import hashlib,json,math,re
from fractions import Fraction
from pathlib import Path
from lxml import etree
import pymupdf
RUN=Path('outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01')
GR=Path('raw/papers/gpt/learning-daily/20261009-DAY10-electromagnetic-ratios-collective-modes/grodner-2011-126cs.xml')
MO=Path('raw/papers/2021_Musangu et al_Chiral vibrations and collective bands in Mo 104 , 106.pdf')
CE=Path('raw/papers/2016_Petrache et al_Triaxiality and exotic rotations at high spins in Ce 134.pdf')

def central(text):
    m=re.search(r'[0-9]+(?:\.[0-9]+)?',text)
    return float(m[0]) if m else None

def main():
    checks=[]
    def check(name,ok,**evidence):
        checks.append({'name':name,'passed':bool(ok),**evidence});assert ok,name
    hashes={GR:'dfc649e43493debee93c4d9e76694360972f82382ce0b25a04945b7a766b728c',MO:'bbfc8907ca98bcf7439ebda321f60988fd5a3052120532a4ce1d364484912dac',CE:'04ac0eb3179a6cb389c45f9df8b4b56d90edf43bcfd8ee9ffed20fb68c898b4d'}
    for p,h in hashes.items():check(p.name+' hash',hashlib.sha256(p.read_bytes()).hexdigest()==h)
    root=etree.parse(str(GR));rows=[]
    for table in root.xpath('//*[local-name()="table"]'):
        current=None
        for row in table.xpath('.//*[local-name()="tbody"]/*[local-name()="row"]'):
            fields=[''.join(x.itertext()).strip() for x in row.xpath('./*[local-name()="entry"]')]
            check('six source fields row '+str(len(rows)),len(fields)==6)
            if fields[0]:current=int(central(fields[0]));tau=central(fields[1])
            upper=any(x in fields[5] for x in ['⩽','≤','<'])
            rows.append({'table':table.get('id'),'spin':current,'reported_tau_ps':tau,'E_keV':central(fields[2]),'multipolarity':fields[3],'I_printed':fields[4],'B_printed':fields[5],'B_Wu_central_or_cap':central(fields[5]),'upper_limit':upper})
    upper=[r for r in rows if r['upper_limit']]
    check('eight explicit B limits',len(upper)==8)
    check('specific limit energies preserved',sorted(int(r['E_keV']) for r in upper)==[264,274,415,465,475,518,626,683])
    k_e2=1.225187e13*5.940e-6*126**(4/3)
    k_m1=1.758366e13*1.7905
    intervals=[]
    for table,spin in dict.fromkeys((r['table'],r['spin']) for r in rows):
        same=[r for r in rows if r['table']==table and r['spin']==spin]
        known,cap=0.,0.
        for r in same:
            e=r['E_keV']/1000
            rate=(k_e2*e**5 if r['multipolarity']=='E2' else k_m1*e**3)*r['B_Wu_central_or_cap']
            if r['upper_limit']:cap+=rate
            else:known+=rate
        bounds=[1e12/(known+cap),1e12/known]
        check(f'{table} I{spin} endpoint monotonicity',bounds[0]<=bounds[1])
        intervals.append({'table':table,'spin':spin,'reported_tau_ps':same[0]['reported_tau_ps'],'conditional_gamma_only_endpoint_range_ps':bounds,'unknown_upper_branch_count':sum(r['upper_limit'] for r in same),'not_probability_interval':True})
    check('thirteen source parent levels',len(intervals)==13)
    check('upper branches not silently set to central rates',sum(x['unknown_upper_branch_count']>0 for x in intervals)==8)
    # Fixed old total photon rate. No external B(E2) bound is supplied.
    e=.277
    gamma_rate=k_m1*e**3*.55
    unit_e2=k_e2*e**5
    slope=gamma_rate/unit_e2
    purity={'B_E2_Wu_per_fraction':slope,'f_0005_B_E2_Wu':slope*.005,'f_001_B_E2_Wu':slope*.01,'f_01_B_E2_Wu':slope*.1,'f_0005_is_bound':False}
    check('fraction to strength is linear conditional map',math.isclose(purity['f_01_B_E2_Wu'],20*purity['f_0005_B_E2_Wu']))
    check('E5 arithmetic',math.isclose((.961/.277)**5,float(Fraction(961,277)**5),rel_tol=1e-12))
    with pymupdf.open(MO) as d:
        text=d[13].get_text()
        check('Mo table shares measured normalization explicitly','combined with the E2in transition intensities mea-' in text and 'sured from the experimental data' in text)
        check('Mo table includes mixed multipoles','M1 and E2 mixing' in text)
        table=text[text.index('104Mo'):text.index('From the TPSM')]
        check('104Mo experimental limit cells blank in parsed table','<0.' not in table.split('106Mo')[0])
    mo=[]
    for spin,re2,theory,cap in [(7,.294,.26,.2),(8,.766,.20,.15),(9,.745,.12,.1)]:
        mo.append({'spin':spin,'printed_RE2_model':re2,'model_plus_data_intensity':theory,'printed_upper_cap':cap,'central_excess_fraction':theory/cap-1,'conditional_fixed_conversion_RE2_cap':re2*cap/theory,'confidence_level':'not specified by TableIV'})
    with pymupdf.open(CE) as d:
        check('Ce18 article pages',len(d)==18)
        p67=d[5].get_text()+d[6].get_text()
        check('Ce selected four lines in source',all(x in p67 for x in ['664.8','740.9','346.5','372.3']))
    ce=[{'E_keV':energy,'printed_delta':delta,'conditional_E2_photon_fraction':delta**2/(1+delta**2)} for energy,delta in [(664.8,-2.13),(740.9,-1.73),(346.5,-2.05),(372.3,-2.23)]]
    check('E2 fractions are relative not unity',all(.74<x['conditional_E2_photon_fraction']<.84 for x in ce))
    out={'kind':'source-table-semantic-and-conditional-design','sources':[{'path':str(p),'sha256':h} for p,h in hashes.items()],'grodner_actual_branch_rows':rows,'grodner_conditional_endpoint_ranges':intervals,'grodner_purity_sensitivity':purity,'grodner_boundary':'finite central B fixed, upper branches 0..cap, ICC0 and photon-only complete ledger assumed solely for this design; same-data printed rounding; no confidence interval or experiment correction','Mo_printed_limit_controls':mo,'Mo_boundary':'relative intensity, same measured normalization/mixing/response held fixed; no limit CL, likelihood or rigid measured B bound','Ce_fraction_controls':ce,'Ce_boundary':'adopted delta fraction only; no universal W.u. threshold, structural exclusion or source-specific lifetime inferred','checks':checks,'valid':all(c['passed'] for c in checks),'independent_experiment_or_CI':False}
    p=RUN/'source-boundary-controls-result-047.json';p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'valid':out['valid'],'checks':len(checks),'branch_rows':len(rows),'upper_limits':len(upper),'parents':len(intervals),'purity_sensitivity':purity,'output':str(p)}))
if __name__=='__main__':main()
