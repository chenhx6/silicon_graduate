"""Direct table transcription and conditional algebra, not nuclear-mode validation.

Run: python3 tmp/day23-theses/ce133-s-exercise/analyze.py
Only standard-library modules are required; outputs stay beside this file.
"""
from pathlib import Path
from decimal import Decimal as D
import csv
import io
import itertools
import json
import re

OUT = Path(__file__).parent

# Columns: twice Ji, Ei keV, twice Jf, E_gamma keV, I_gamma literal,
# multipolarity, final band. Each line is one printed table row.
B1 = """11 207.4 9 170.2 100(6) M1+E2 1
13 592.1 11 384.7 27.0(9) M1+E2 1
13 592.1 9 554.9 6.4(4) E2 1
15 827.1 13 235.0 12.1(4) M1+E2 1
15 827.1 11 619.7 34.7(11) E2 1
17 1344.7 15 517.6 9.4(4) M1+E2 1
17 1344.7 13 752.6 10.7(4) E2 1
19 1590.3 17 245.6 1.07(12) M1+E2 1
19 1590.3 15 763.2 15.2(5) E2 1
21 2201.1 19 610.8 3.33(22) M1+E2 1
21 2201.1 17 856.4 3.27(18) E2 1
23 2486.6 21 285.5 0.43(11) M1+E2 1
23 2486.6 19 896.3 6.65(25) E2 1
25 3131.8 23 645.2 0.28(10) M1+E2 1
25 3131.8 21 930.7 1.16(11) E2 1
27 3434.0 25 302.2 0.09(8) M1+E2 1
27 3434.0 23 947.4 2.45(19) E2 1
29 4132.4 25 1000.4 0.21(7) E2 1
31 4406.4 27 972.4 0.27(9) E2 1
35 5401.8 31 995.4 0.05(5) E2 1"""
B4 = """15 1200.8 13 368.8 1.16(16) M1+E2 4
17 1409.8 15 209.0 5.5(6) M1+E2 4
17 1409.8 13 577.8 3.22(21) E2 4
19 1809.1 17 399.3 1.66(18) M1+E2 4
19 1809.1 15 608.3 1.89(18) E2 4
21 2299.5 19 490.4 0.80(16) M1+E2 4
21 2299.5 17 889.7 0.77(13) E2 4
23 2679.9 21 380.4 0.66(12) M1+E2 4
23 2679.9 19 870.8 1.95(18) E2 4
25 3283.9 23 604.0 2.12(20) M1+E2 4
25 3283.9 21 984.4 0.56(10) E2 4
27 3616.2 25 332.3 1.03(16) M1+E2 4
27 3616.2 23 936.3 0.49(11) E2 4
13 832.0 11 624.6 3.3(4) M1+E2 1
13 832.0 9 794.8 8.0(14) E2 1
15 1200.8 13 608.7 8.8(4) M1+E2 1
15 1200.8 11 993.4 0.01(3) E2 1
17 1409.8 15 582.7 3.53(25) M1+E2 1
19 1809.1 17 464.4 1.89(18) M1+E2 1
19 1809.1 15 982.0 1.95(17) E2 1
21 2299.5 17 954.8 6.08(24) E2 1
21 2299.5 19 709.2 1.26(14) M1+E2 1
23 2679.9 21 478.8 0.35(12) M1+E2 1
23 2679.9 19 1089.6 0.53(8) E2 1
25 3283.9 23 797.3 0.92(13) M1+E2 1
25 3283.9 21 1082.8 0.10(8) E2 1
27 3616.2 25 484.4 0.02(8) M1+E2 1
27 3616.2 23 1129.6 0.59(7) E2 1"""
B2 = """9 678.1 7 337.8 2.10(13) M1+E2 2
11 1033.4 9 355.3 0.16(7) M1+E2 2
11 1033.4 7 693.1 1.32(13) E2 2
13 1459.9 11 426.4 0.15(9) M1+E2 2
13 1459.9 9 781.8 0.86(8) E2 2
15 1852.7 13 392.8 0.05(7) M1+E2 2
15 1852.7 11 819.3 0.76(9) E2 2
17 2304.1 15 451.4 0.27(10) M1+E2 2
17 2304.1 13 844.4 0.27(9) E2 2
19a 2733.4 15 881.2 0.25(6) E2 2
19b 2739.5 15 886.8 0.16(6) E2 2
7 340 9 303.1 - E1 1"""

def num(x):
    return float(x) if isinstance(x, D) else x

def save(name, value):
    (OUT/name).write_text(json.dumps(value, ensure_ascii=False, indent=2, default=num)+"\n")

def nodeid(band, spin):
    return f"B{band}-J{spin}of2-{'p' if band == 2 else 'm'}"

def intensity(value):
    if value == '-':
        return None, None
    m = re.fullmatch(r'([0-9.]+)\((\d+)\)', value)
    central = D(m[1])
    error = D(m[2])*D(10)**central.as_tuple().exponent
    return central, error

nodes = {}
edges = []
for band, table, raw in [(1,'5.1',B1),(4,'5.2',B4),(2,'5.3',B2)]:
    for row, line in enumerate(raw.splitlines(), 1):
        spin, ex, finalspin, eg, iraw, multipole, finalband = line.split()
        finalband = int(finalband)
        init = nodeid(band,spin)
        value, error = intensity(iraw)
        nodes[init] = dict(node_id=init, band=band, twice_J=int(re.sub('[ab]','',spin)),
                           state_suffix=re.sub('[0-9]','',spin), parity='+' if band==2 else '-',
                           Ex_keV=D(ex), Ex_literal=ex, Ex_error_keV=None,
                           Ex_status='printed_table_initial_energy', locator=f'Table{table} row{row}')
        bound = D('.3') if (value is not None and value>=10) else D('.7')
        error_rule = 'I_gamma>=10: within0.3; I_gamma<10: up to0.7 keV'
        if band != 1:
            bound = D('.3') if D(eg)<1000 else D('.5')
            error_rule = 'E_gamma<1000: within0.3; E_gamma>1000: up to0.5 keV'
        edges.append(dict(edge_id=f'T{table}-r{row:02d}', initial_node=init,
                          final_node=nodeid(finalband,finalspin), initial_band=band, final_band=finalband,
                          twice_Ji=nodes[init]['twice_J'], twice_Jf=int(finalspin),
                          Egamma_keV=D(eg), Egamma_error_envelope_keV=bound,
                          Egamma_error_type='caption upper envelope, not established 1sigma',
                          Egamma_error_rule=error_rule, Igamma_literal=iraw, Igamma=value,
                          Igamma_parenthetical_error=error, multipolarity=multipole,
                          locator=f'PDF{66 if band==1 else 67 if band==4 else 69}, printed p{55 if band==1 else 56 if band==4 else 58}, Table{table} row{row}'))

# Terminal B1 node is not an Ei row; both printed terminating edges imply37.2.
anchors = [nodes[e['initial_node']]['Ex_keV']-e['Egamma_keV'] for e in edges
           if e['edge_id'] in ['T5.1-r01','T5.1-r03']]
assert anchors == [D('37.2'),D('37.2')]
nid=nodeid(1,'9')
nodes[nid]=dict(node_id=nid,band=1,twice_J=9,state_suffix='',parity='-',Ex_keV=anchors[0],
                Ex_literal=None,Ex_error_keV=None,Ex_status='derived_consistently_from_two_Table5.1_edges',
                locator='Table5.1 rows1/3:207.4−170.2 and592.1−554.9')
nodes_order=sorted(nodes, key=lambda k:(nodes[k]['band'],nodes[k]['twice_J'],nodes[k]['state_suffix']))
assert len(nodes)==29 and len(edges)==60
for e in edges:
    assert e['final_node'] in nodes
    ei=nodes[e['initial_node']]['Ex_keV']; ef=nodes[e['final_node']]['Ex_keV']
    e['initial_Ex_keV']=ei
    e['final_Ex_keV']=ef
    e['Ji_pi']=f"{e['twice_Ji']}/2{nodes[e['initial_node']]['parity']}"
    e['Jf_pi']=f"{e['twice_Jf']}/2{nodes[e['final_node']]['parity']}"
    e['needs_review']=True
    e['closure_residual_keV']=ei-ef-e['Egamma_keV']
    e['closure_interpretation']='arithmetic residual only; no chi-square without level/transition covariance'
for node in nodes.values():
    node['J_pi']=f"{node['twice_J']}/2{node['parity']}"
    node['needs_review']=True

# S(I) = 0.5 E(I−2) −1.5 E(I−1) +1.5 E(I) −0.5 E(I+1).
# Spins are stored doubled, so the offsets below are -4,-2,0,+2.
matrix_cols=[n for n in nodes_order if nodes[n]['band'] in (1,4)]
rows=[]; L=[]; missing=[]; checks=[]
weights=[D('.5'),D('-1.5'),D('1.5'),D('-.5')]
for band in [1,4]:
    bn={nodes[k]['twice_J']:k for k in matrix_cols if nodes[k]['band']==band}
    for spin in range(min(bn), max(bn)+1, 2):
        stencil=[spin-4,spin-2,spin,spin+2]
        absent=[j for j in stencil if j not in bn]
        if absent:
            missing.append(dict(band=band,I=f'{spin}/2',missing_twice_J=absent,action='not evaluated; no interpolation'))
            continue
        keys=[bn[j] for j in stencil]; E=[nodes[k]['Ex_keV'] for k in keys]
        direct=sum(w*x for w,x in zip(weights,E))
        gaps=[E[i+1]-E[i] for i in range(3)]
        # Independent path: center gap minus mean of outer gaps.
        finite=gaps[1]-(gaps[0]+gaps[2])/2
        assert direct == finite
        line=[D(0)]*len(matrix_cols)
        for k,w in zip(keys,weights): line[matrix_cols.index(k)]=w
        rowid=f'B{band}-S{spin}of2'
        rows.append(dict(row_id=rowid,band=band,I=f'{spin}/2',S_keV=direct,
                         stencil_nodes=keys,weights=weights,finite_difference_S_keV=finite,
                         uses_derived_terminal_Ex=(nid in keys),uncertainty_keV=None,
                         needs_review=True))
        L.append(line)
        shifted=[x+D('123.456') for x in E]
        assert sum(w*x for w,x in zip(weights,shifted))==direct
        js=[D(j)/2 for j in stencil]
        rotor=[D('7.125')*j*(j+1)+D('325.7') for j in js]
        assert sum(w*x for w,x in zip(weights,rotor))==0
        for idx in range(4):
            perturbed=E.copy();perturbed[idx]+=D('.001')
            assert (sum(w*x for w,x in zip(weights,perturbed))-direct)/D('.001')==weights[idx]
        checks.append(dict(row_id=rowid,independent_gap_difference=True,
                           constant_shift_invariance=True,ideal_quadratic_rotor_zero_S=True,
                           finite_perturbation_gradient_matches_L=True))

# Close-energy lines are retained as separate edges, never merged by energy.
near=[]
for a,b in itertools.combinations(edges,2):
    diff=abs(a['Egamma_keV']-b['Egamma_keV'])
    if diff<=D('1.0'):
        near.append(dict(edge1=a['edge_id'],edge2=b['edge_id'],delta_Egamma_keV=diff,
                         same_initial_node=a['initial_node']==b['initial_node'],
                         same_final_node=a['final_node']==b['final_node'],action='retain distinct identity'))
save('nodes.json',[nodes[k] for k in nodes_order])
save('edges.json',edges)
save('S-results.json',dict(formula='Eq2.37',rows=rows,not_evaluated=missing,
                           central_values_only=True,no_experimental_CI=True))
save('design-matrix-L.json',dict(column_nodes=matrix_cols,row_ids=[r['row_id'] for r in rows],L=L,
                               CovS='L CovE L^T',CovE_supplied=False,
                               note='CovE must include network-fit and common calibration correlations; caption envelopes are not sigma'))
save('controls.json',dict(checks=checks,all_pass=True,
                         scope='Conditional linear algebra only; does not authenticate band identity or a nuclear mode'))
gamma_crosschecks=[]
for row in rows:
    band=row['band']; spin=int(row['I'].split('/')[0])
    gaps={}
    for j in [spin-2,spin,spin+2]:
        matches=[e for e in edges if e['initial_band']==band and e['final_band']==band
                 and e['twice_Ji']==j and e['twice_Jf']==j-2]
        if len(matches)==1:
            gaps[j]=matches[0]
    if len(gaps)==3:
        measured=gaps[spin]['Egamma_keV']-(gaps[spin-2]['Egamma_keV']+gaps[spin+2]['Egamma_keV'])/2
        gamma_crosschecks.append(dict(row_id=row['row_id'],source_edges=[gaps[j]['edge_id'] for j in [spin-2,spin,spin+2]],
                                      gamma_gap_S_keV=measured,level_combination_S_keV=row['S_keV'],
                                      difference_keV=measured-row['S_keV']))
        assert measured==row['S_keV']
save('direct-gamma-gap-crosschecks.json',dict(rows=gamma_crosschecks,all_exactly_agree=True,
                                           scope='Independent transcription path from three adjacent measured DeltaI1 lines; unavailable high-spin gaps not fabricated'))
save('transition-incidence-A.json',dict(column_nodes=nodes_order,row_edges=[e['edge_id'] for e in edges],
                                       A=[[1 if n==e['initial_node'] else -1 if n==e['final_node'] else 0 for n in nodes_order] for e in edges],
                                       model='Egamma=A E + residual; define gauge before weighted network fit',
                                       fit_performed=False))
save('ambiguity-registry.json',dict(
    missing_states=[dict(band=1,twice_J=33,parity='-',Ex_keV=None,status='absent from Table5.1; no interpolation')],
    duplicate_spin_states=[dict(band=2,twice_J=19,parity='+',
                               node_ids=[nodeid(2,'19a'),nodeid(2,'19b')],
                               Ex_keV=[D('2733.4'),D('2739.5')],status='distinct printed rows; do not merge')],
    terminal_anchor=dict(node_id=nid,Ex_keV=D('37.2'),status='derived from Table5.1 rows1/3, not independent measured Ex'),
    close_lines=dict(edge_ids=['T5.2-r05','T5.2-r16'],energies_keV=[D('608.3'),D('608.7')],
                     status='different initial and final states; doublet caution in PDF63 printed52'),
    needs_review=True))
save('near-energy-identities.json',near)
save('closure-summary.json',dict(edge_count=len(edges),max_abs_residual_keV=max(abs(e['closure_residual_keV']) for e in edges),
                                 nonzero=[dict(edge_id=e['edge_id'],residual_keV=e['closure_residual_keV']) for e in edges if e['closure_residual_keV']],
                                 no_statistical_acceptance_test=True))

def csvwrite(name, data):
    fields=list(data[0]); stream=io.StringIO();w=csv.DictWriter(stream,fieldnames=fields,lineterminator="\n")
    w.writeheader();w.writerows(data);(OUT/name).write_text(stream.getvalue())
csvwrite('nodes.csv',[nodes[k] for k in nodes_order])
csvwrite('edges.csv',edges)
csvwrite('S-central.csv',[{k:r[k] for k in ['row_id','band','I','S_keV','uses_derived_terminal_Ex','uncertainty_keV']} for r in rows])
print(json.dumps({'nodes':len(nodes),'edges':len(edges),'S_rows':len(rows),'all_controls':True,
                  'S':[{k:r[k] for k in ['band','I','S_keV']} for r in rows]},default=num,indent=2))
