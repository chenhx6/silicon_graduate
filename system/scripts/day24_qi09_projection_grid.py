#!/usr/bin/env python3
"""Decode literal Qi09 author figure paths and compare the stored PDF.

No PostScript/TeX is executed. This identifies the drawn positive-K grid and
its representation precision; it does not recover a PRM producer or phases.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import re

import numpy as np
import pymupdf

HASHES = {'pdf':'248546abd4a1d1597bf9ddf39cfffd5f09604802704204f0ff61647bbdb19346',
          'fig5.eps':'728a1b079695dbef66aa9caf3730df372180848ca95ccb9b10af66af66b7b8a0',
          'paper.tex':'aaab1da6ab07275330e7d37bf25eabc41d74e1ae3992da205154452eb75aab76'}


def literal_strokes(text):
    color,width,path=(0.,0.,0.),1.,[]
    out=[]
    for line_number,line in enumerate(text.splitlines(),1):
        m=re.fullmatch(r'(-?\d+(?:\.\d+)?) (-?\d+(?:\.\d+)?) ([ml])',line)
        if m:
            if m[3]=='m':path=[(float(m[1]),float(m[2]))]
            else:path.append((float(m[1]),float(m[2])))
        m=re.fullmatch(r'([\d.]+) sw',line)
        if m:width=float(m[1])
        m=re.fullmatch(r'([\d.]+) ([\d.]+) ([\d.]+) rgb',line)
        if m:color=tuple(map(float,m.groups()))
        if line=='st':
            if len(path)>=2:out.append({'line':line_number,'color':color,'width':width,'points':path})
            path=[]
    return out


def norm_interval(y0,yend,ys):
    # Explicit nearest-integer coordinate rounding assumption only, not a CI.
    n=len(ys)
    values=[.3*(n*(y0+a)-sum(ys)+n*c)/(y0+a-yend-b)
            for a,b,c in itertools.product([-.5,.5],repeat=3)]
    return [min(values),max(values)]


def calculate(pdf_path,source_root):
    data={'pdf':pdf_path.read_bytes(),**{n:(source_root/n).read_bytes() for n in ['fig5.eps','paper.tex']}}
    for n,b in data.items():
        if hashlib.sha256(b).hexdigest()!=HASHES[n]:raise ValueError('Version mismatch: '+n)
    text=data['fig5.eps'].decode('latin1');tex=data['paper.tex'].decode('latin1')
    if '$K_i=0$' not in tex:raise ValueError('Expected author wording missing')
    ss=literal_strokes(text)
    markers=[x for x in ss if x['width']==0 and x['color'] in [(1.,0.,0.),(0.,0.,1.)]]
    axes=[x for x in ss if x['color']==(0.,0.,0.) and len(x['points'])==2 and
          abs(x['points'][0][1]-x['points'][1][1])<1 and
          400<abs(x['points'][0][0]-x['points'][1][0])<450]
    if len(markers)!=690 or len(axes)!=21:raise ValueError('Figure path count changed')
    curves,checks=[],[]
    def check(name,ok):checks.append({'name':name,'passed':bool(ok)})
    for group,axis in enumerate(['l','i','s']):
        frames=axes[group*7:group*7+6]
        lo=axes[group*7]['line'];hi=axes[(group+1)*7]['line'] if group<2 else 10**9
        for color,band in [((1.,0.,0.),'A'),((0.,0.,1.),'B')]:
            pts=[x for x in markers if lo<x['line']<hi and x['color']==color]
            check(axis+band+'_115markers',len(pts)==115)
            pos=0
            for two_I,frame in zip([45,41,39,37,33,29],reversed(frames)):
                n=(two_I+1)//2;block=pts[pos:pos+n];pos+=n
                origin=np.array(frame['points'][0]);span=frame['points'][1][0]-origin[0]
                left=[x for x in ss if x['color']==(0.,0.,0.) and len(x['points'])==2 and
                      x['points'][0]==frame['points'][0] and
                      260<abs(x['points'][1][1]-origin[1])<280]
                if not left:raise ValueError('Probability axis not found')
                end=np.array(left[0]['points'][1]);r=(end[0]-origin[0])/(end[1]-origin[1])
                xy=np.array([np.mean(x['points'],axis=0) for x in block])
                k=(xy[:,0]-origin[0]-r*(xy[:,1]-origin[1]))/(span/24)
                grid=np.arange(n)+.5;error=float(np.max(np.abs(k-grid)))
                check(f'{axis}{band}{two_I}_half_grid',error<.1)
                check(f'{axis}{band}{two_I}_integer_grid_excluded',np.min(np.abs(k-np.rint(k)))>.39)
                prob=.3*(origin[1]-xy[:,1])/(origin[1]-end[1])
                bounds=norm_interval(origin[1],end[1],xy[:,1])
                check(f'{axis}{band}{two_I}_rounded_norm_compatible',bounds[0]<=1<=bounds[1])
                curves.append({'axis':axis,'band':band,'two_I':two_I,'marker_count':n,
                               'maximum_K_grid_deviation':error,'first_drawn_K':float(k[0]),
                               'last_drawn_K':float(k[-1]),'drawn_probability_sum':float(sum(prob)),
                               'rounding_only_sum_bounds':bounds,
                               'source_marker_lines':[x['line'] for x in block]})
    # Check the same vector representation through the existing article PDF.
    ds=pymupdf.open(pdf_path)[15].get_drawings()
    pm=[x for x in ds if x.get('color') in [(1.,0.,0.),(0.,0.,1.)] and x.get('width')==0
        and len(x['items'])==1 and x['items'][0][0]=='l']
    pa=[x for x in ds if x.get('color')==(0.,0.,0.) and len(x['items'])==1 and x['items'][0][0]=='l'
        and abs(x['items'][0][1].y-x['items'][0][2].y)<.01
        and 60<abs(x['items'][0][1].x-x['items'][0][2].x)<80]
    if len(pm)!=690 or len(pa)!=21:raise ValueError('PDF vector count changed')
    source=np.array([list(axes[0]['points'][0])+[1],list(axes[0]['points'][1])+[1],list(axes[1]['points'][0])+[1]])
    target=np.array([tuple(pa[0]['items'][0][1]),tuple(pa[0]['items'][0][2]),tuple(pa[1]['items'][0][1])])
    affine=np.linalg.solve(source,target)
    errors=[]
    for e,p in zip(markers,pm):
        actual=np.mean([tuple(p['items'][0][1]),tuple(p['items'][0][2])],axis=0)
        pred=np.r_[np.mean(e['points'],axis=0),1]@affine
        errors.append(float(np.max(np.abs(pred-actual))))
    check('all_690_color_identities',all(x['color']==y['color'] for x,y in zip(markers,pm)))
    check('all_690_native_PDF_positions',max(errors)<.005)
    # Source gamma sectors preserve the same shape eigenvalues, permuted.
    shapes=[np.sort(np.cos(np.deg2rad(g)-2*np.pi*np.arange(3)/3)) for g in [22.4,97.6,142.4]]
    check('gamma_sectors_same_shape',max(np.max(np.abs(x-shapes[0])) for x in shapes)<2e-15)
    return {'kind':'author-figure-grid-identity-not-model-replay','source':'knowledge/sources/qi-2009-135nd-particle-rotor-chirality.md',
            'sha256':HASHES,'curves':curves,'controls':checks,'all_controls_pass':all(x['passed'] for x in checks),
            'maximum_K_grid_deviation':max(x['maximum_K_grid_deviation'] for x in curves),
            'native_PDF_maximum_position_difference_pt':max(errors),
            'drawn_probability_sum_range':[min(x['drawn_probability_sum'] for x in curves),max(x['drawn_probability_sum'] for x in curves)],
            'limits':['Grid/coordinate checks use drawing units, not a physical-mode acceptance threshold.',
                      'Probability ordinates use the axis endpoint 0.3 and integer drawing coordinates; rounding envelopes are not CIs.',
                      'Positive-K unit-sum compatibility supports a folded/restricted representation, but its actual producer convention is not recovered.',
                      'No literal K=0 eigenprojector, signed wavefunctions, relative phases, joint orientation distribution or tunneling path is reconstructed.',
                      'Archive, EPS and stored PDF are versions/representations of the same paper; no new experiment or independent PRM solution.']}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--pdf',type=Path,required=True)
    p.add_argument('--source-root',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    result=calculate(a.pdf,a.source_root);a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['all_controls_pass','maximum_K_grid_deviation','native_PDF_maximum_position_difference_pt','drawn_probability_sum_range']}))
    print(str(len(result['controls']))+' controls')
    return 0 if result['all_controls_pass'] else 1


if __name__=='__main__':raise SystemExit(main())
