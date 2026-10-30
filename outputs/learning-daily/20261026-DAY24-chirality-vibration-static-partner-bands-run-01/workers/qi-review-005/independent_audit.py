"""Read-only restricted literal-data audit; does not interpret PostScript."""
from pathlib import Path
import collections
import hashlib
import itertools
import json
import math
import re
import numpy as np
import pymupdf

ROOT = Path('/workspace/wiki')
OUT = Path(__file__).parent
eps = ROOT/'tmp/day24-qi09-source/members/fig5.eps'
pdf = ROOT/'tmp/day21-checkpoint053/qi-2009-0812.4597v1.pdf'
tex = ROOT/'tmp/day24-qi09-source/members/paper.tex'
lines = eps.read_text(encoding='latin1').splitlines()
num = r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)'
state = {'rgb': (0.,0.,0.), 'width':1., 'ctm':np.eye(3)}
saved, temporary_matrices, path, strokes = [], [], [], []
transform_ops = []
for line_number,line in enumerate(lines[1349:],1350):
    if line == 'gs':
        saved.append({**state,'ctm':state['ctm'].copy()})
    elif line == 'gr':
        state = saved.pop()
    elif line == 'mtx cmtx mtx smtx':
        temporary_matrices.append(state['ctm'].copy())
        state['ctm'] = np.eye(3)
    elif line == 'smtx':
        state['ctm'] = temporary_matrices.pop()
    elif (m := re.fullmatch(fr'({num}) ({num}) (sc|tr)',line)):
        a,b = map(float,m.groups()[:2]); t = np.eye(3)
        if m[3]=='sc': t[0,0],t[1,1]=a,b
        else: t[:2,2]=a,b
        state['ctm'] = state['ctm']@t
        transform_ops.append([line_number,line])
    elif (m := re.fullmatch(fr'({num}) ro',line)):
        a=math.radians(float(m[1]));c,s=math.cos(a),math.sin(a)
        state['ctm']=state['ctm']@np.array([[c,-s,0],[s,c,0],[0,0,1]])
        transform_ops.append([line_number,line])
    elif line.endswith('] concat'):
        a,b,c,d,e,f=map(float,re.findall(num,line))
        state['ctm']=state['ctm']@np.array([[a,c,e],[b,d,f],[0,0,1]])
        transform_ops.append([line_number,line])
    elif (m := re.fullmatch(fr'({num}) sw',line)):
        state['width']=float(m[1])
    elif (m := re.fullmatch(fr'({num}) ({num}) ({num}) rgb',line)):
        state['rgb']=tuple(map(float,m.groups()))
    elif (m := re.fullmatch(fr'({num}) ({num}) ([ml])',line)):
        p=np.array([float(m[1]),float(m[2]),1.])
        item=(p[:2],(state['ctm']@p)[:2])
        if m[3]=='m': path=[item]
        else: path.append(item)
    elif line=='st':
        if len(path)>=2:
            strokes.append({'line':line_number,'color':state['rgb'],'width':state['width'],
                            'points':np.array([x[0] for x in path]),
                            'device':np.array([x[1] for x in path])})
        path=[]

markers=[s for s in strokes if s['width']==0 and s['color'] in [(1.,0.,0.),(0.,0.,1.)]]
frames=[s for s in strokes if s['color']==(0.,0.,0.) and len(s['points'])==2 and
        np.ptp(s['points'][:,1])==0 and 400<np.ptp(s['points'][:,0])<450]
doc=pymupdf.open(pdf);page=doc[15];drawings=page.get_drawings(extended=True)
pdfmarkers=[s for s in drawings if s.get('width')==0 and s.get('color') in [(1.,0.,0.),(0.,0.,1.)]
            and len(s['items'])==1 and s['items'][0][0]=='l']
pdfframes=[s for s in drawings if s.get('color')==(0.,0.,0.) and len(s.get('items',[]))==1 and
           s['items'][0][0]=='l' and abs(s['items'][0][1].y-s['items'][0][2].y)<.01 and
           60<abs(s['items'][0][1].x-s['items'][0][2].x)<80]
src=np.array([np.r_[frames[0]['points'][0],1],np.r_[frames[0]['points'][1],1],np.r_[frames[1]['points'][0],1]])
dst=np.array([pdfframes[0]['items'][0][1],pdfframes[0]['items'][0][2],pdfframes[1]['items'][0][1]])
affine=np.linalg.solve(src,dst)
all_point_errors=[]
center_errors=[]
for e,p in zip(markers,pdfmarkers):
    expected=np.column_stack((e['points'],np.ones(len(e['points']))))@affine
    actual=np.array(p['items'][0][1:])
    all_point_errors.extend(abs(expected-actual).ravel())
    center_errors.append(float(np.max(abs(expected.mean(axis=0)-actual.mean(axis=0)))))
clip=[s for s in drawings if s['type']=='clip'][0]['scissor']
pdfpts=np.concatenate([np.array(s['items'][0][1:]) for s in pdfmarkers])
epspts=np.concatenate([s['device'] for s in markers])

# Independent probability inversion: solve a two-dimensional basis of each frame.
curves=[]
for col,axis in enumerate('lis'):
    starts=frames[col*7:col*7+6]
    segment=[s for s in markers if frames[col*7]['line']<s['line']<
             (frames[(col+1)*7]['line'] if col<2 else float('inf'))]
    for rgb,band in [((1.,0.,0.),'A'),((0.,0.,1.),'B')]:
        selected=[s for s in segment if s['color']==rgb];index=0
        for two_i,frame in zip([45,41,39,37,33,29],reversed(starts)):
            count=(two_i+1)//2;block=selected[index:index+count];index+=count
            origin=frame['points'][0]
            vertical=[s for s in strokes if s['color']==(0.,0.,0.) and len(s['points'])==2 and
                      np.array_equal(s['points'][0],origin) and 260<abs(s['points'][1,1]-origin[1])<280][0]
            endpoint=vertical['points'][1]
            xy=np.array([s['points'].mean(axis=0) for s in block])
            basis=np.column_stack(((frame['points'][1]-origin)/24,(endpoint-origin)/.3))
            kp=np.linalg.solve(basis,(xy-origin).T).T
            # Eight vertices suffice: the sum is linear-fractional with positive denominator.
            y0,yend=origin[1],endpoint[1];ys=xy[:,1]
            corners=[.3*(count*(y0+da)-sum(ys)-count*dc)/(y0+da-yend-db)
                     for da,db,dc in itertools.product([-.5,.5],repeat=3)]
            curves.append({'axis':axis,'band':band,'two_I':two_i,'count':count,
                           'K_residual':float(max(abs(kp[:,0]-(np.arange(count)+.5)))),
                           'sum':float(kp[:,1].sum()),'bounds':[min(corners),max(corners)],
                           'P_range':[float(min(kp[:,1])),float(max(kp[:,1]))],
                           'first_source_line':block[0]['line'],'last_source_line':block[-1]['line']})
assert len(curves)==36 and len(markers)==len(pdfmarkers)==690
assert len(frames)==len(pdfframes)==21
assert all(a['color']==b['color'] for a,b in zip(markers,pdfmarkers))
assert all(c['bounds'][0]<=1<=c['bounds'][1] for c in curves)
assert all(c['K_residual']<.1 for c in curves)
assert all(clip.contains(pymupdf.Point(*p)) for p in pdfpts)
assert ((epspts>=0)&(epspts<=np.array([763.71,1112.77]))).all()
# Explicit TeX includegraphics crop, in the original EPS point coordinate system.
assert ((epspts>=np.array([0,230]))&(epspts<=np.array([710,800]))).all()
existing=json.loads((ROOT/'outputs/learning-daily/20261026-DAY24-chirality-vibration-static-partner-bands-run-01/qi09-projection-grid-003.json').read_text())
assert max(abs(a['sum']-b['drawn_probability_sum']) for a,b in zip(curves,existing['curves']))<1e-12
result={'audit_kind':'independent-restricted-literal-and-PDF-read-no-PostScript-execution',
 'hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [eps,pdf,tex]},
 'marker_counts':dict(collections.Counter(str(s['color']) for s in markers)),
 'marker_count':len(markers),'series_count':len(curves),'frame_count':len(frames),
 'maximum_half_grid_residual':max(c['K_residual'] for c in curves),
 'probability_sum_range':[min(c['sum'] for c in curves),max(c['sum'] for c in curves)],
 'probability_sum_bounds_union':[min(c['bounds'][0] for c in curves),max(c['bounds'][1] for c in curves)],
 'maximum_center_position_error_pt':max(center_errors),
 'maximum_endpoint_position_error_pt':float(max(all_point_errors)),
 'eps_marker_endpoint_bounds': [epspts.min(axis=0).tolist(),epspts.max(axis=0).tolist()],
 'pdf_marker_endpoint_bounds': [pdfpts.min(axis=0).tolist(),pdfpts.max(axis=0).tolist()],
 'pdf_clip_rect':list(clip),'all_690_endpoints_inside_EPS_TeX_and_PDF_clip':True,
 'colors_and_order_identical':True,'all_36_rounding_envelopes_include_one':True,
 'curves':curves,'graphics_stack_depth_at_end':len(saved),'temporary_matrix_stack_at_end':len(temporary_matrices),
 'parser_scope':'Numeric m/l, sw/rgb, gs/gr, sc/tr/ro/concat, marker temporary CTM only; embedded font programs are not interpreted.'}
(OUT/'independent-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['curves','hashes']},indent=2))
