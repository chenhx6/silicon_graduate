#!/usr/bin/env python3
"""Primary-anchored high-spin delta-root boundary controls, no new fit."""
import hashlib,json,math
from pathlib import Path
import pymupdf
RUN=Path('outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01')
AM=Path('raw/papers/2003_The wobbling mode in 167Lu.pdf');JE=Path('raw/papers/2002_Jensen et al_Evidence for Second-Phonon Nuclear Wobbling.pdf')
HA='2c28c101a58d920c9cade83a2b166d9fe5d3f80d59eff8d6e1c7c9571b89ec88';HJ='c6fd99c17c09763f742cbe36443f7039f21b3e28a5caa548748bdf0718630a8a'
def f(d):return d*d/(1+d*d)
def main():
 checks=[]
 def check(n,x,**e):checks.append({'name':n,'passed':bool(x),**e});assert x,n
 check('Amro hash',hashlib.sha256(AM.read_bytes()).hexdigest()==HA);check('Jensen hash',hashlib.sha256(JE.read_bytes()).hexdigest()==HJ)
 with pymupdf.open(AM) as d:
  t=''.join(x.get_text() for x in d[:5]);check('Amro table 1 and DCO/SpeeDCO text','Table 1' in t and 'SpeeDCO' in t);check('Amro no fresh polarization evidence','polarization' in t)
 with pymupdf.open(JE) as d:
  t=''.join(x.get_text() for x in d[:4]);check('Jensen table II and polarization failure','Table II' in t and 'polarization' in t and 'impossible' in t);check('Jensen table and two-branch text', 'alternative' in t and 'solution' in t)
 am=[]
 for large,small,reported in [(-3.1,-.07,.23),(-5.1,-.19,.26),(-3.9,-.35,.27)]:
  ratio=f(large)/f(small);am.append({'large_delta':large,'small_delta':small,'reported_ratio':reported,'conditional_large_over_small':ratio,'small_ratio_if_fixed_other_inputs':reported/ratio})
 check('Amro suppression factors exceed one order in selected rows',all(x['conditional_large_over_small']>8 for x in am))
 je_large=-3.60;je_small=-.19;ratio=f(je_large)/f(je_small);check('Jensen conditional suppression',ratio>20)
 out={'kind':'primary-root-branch-and-no-polarization-boundary','sources':[{'path':str(AM),'sha256':HA},{'path':str(JE),'sha256':HJ}],'Amro':am,'Jensen163Lu':{'large_delta':je_large,'small_delta':je_small,'conditional_strength_suppression':ratio,'experimental_selection':'polarization impossible for 476 keV; large root selected using similar rotational properties and PRM, not direct polarization'},'checks':checks,'valid':all(x['passed'] for x in checks),'independent_fit_or_CI':False}
 p=RUN/'highspin-root-boundary-result-051.json';p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'valid':out['valid'],'checks':len(checks),'output':str(p)}))
if __name__=='__main__':main()
