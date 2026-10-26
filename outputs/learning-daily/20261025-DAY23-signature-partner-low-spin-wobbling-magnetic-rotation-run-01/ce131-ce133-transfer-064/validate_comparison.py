from pathlib import Path
from fractions import Fraction as F
import json,hashlib,re,ast,datetime
O=Path(__file__).resolve().parent;ROOT=Path('/workspace/wiki');checks=[]
def check(n,v):
 checks.append({'name':n,'passed':bool(v)})
 if not v:raise AssertionError(n)
required=['synthesis_report.md','comparison_matrix.json','blueprint_checklist.md','next_day_supplement_questions.md']
check('four_required_artifacts_present',all((O/x).is_file() and (O/x).stat().st_size>500 for x in required))
m=json.loads((O/'comparison_matrix.json').read_text())
for k,s in m['sources'].items():check('source_sha_'+k,hashlib.sha256((ROOT/s['path']).read_bytes()).hexdigest()==s['sha256'])
check('nuclei_neutron_number',m['nuclei']['131Ce']['N']==73 and m['nuclei']['133Ce']['N']==75)
check('source_local_band_ids_unique',len({x[n]['source_band_id'] for x in m['band_pair_matrix'] for n in ['131Ce','133Ce']})==8)
b3=next(x for x in m['band_pair_matrix'] if x['pair_id']=='B3_comparison')
check('band3_not_merged_ground_identity',b3['131Ce']['ground_state_band']['value'] is False and b3['133Ce']['ground_state_band']['value'] is True)
check('band3_131_literal_618',b3['131Ce']['head_excitation_keV']['value']=='61.8')
check('band3_same_spin_nearby_141',F('1459.9')-F('1445.8')==F('14.1'))
check('crosslink_4124_closes',F('1445.8')-F('1033.4')==F('412.4'))
check('crosslink_7677_closes',F('1445.8')-F('678.1')==F('767.7'))
for p in m['band_pair_matrix']:
 check('unknown_133_ix_'+p['pair_id'],p['133Ce']['ix_initial_hbar']['value'] is None)
 check('unknown_133_omega_'+p['pair_id'],p['133Ce']['first_crossings']['value'] is None)
for k,path in m['selected_local_S_control']['gamma_paths'].items():
 d={F(i):F(v) for i,v in path.items()}
 # Independent reconstruction of an arbitrary-zero sequence for the selected continuous path.
 spins=sorted(d);base=spins[0]-1;E={base:F(123)}
 for i in spins:E[i]=E[i-1]+d[i]
 for r in m['selected_local_S_control']['results'][k]:
  i=F(r['I']);viafour=E[i-2]/2-F(3,2)*E[i-1]+F(3,2)*E[i]-E[i+1]/2
  check('independent_four_energy_S_'+k+'_'+str(i),viafour==F(r['S_keV']))
check('608_doublet_energy_sum',F('399.3')+F('209.0')==F('608.3'))
text='\n'.join((O/p).read_text() for p in required if p.endswith('.md'))
for token in ['61.8','14.1','unknown','DSAM','RDDS','out/in','out/out','Gammasphere','AFRODITE','GALILEO','972']:
 check('requested_topic_'+token,token in text)
check('lifetime_existing_evidence_not_lost','Li2004' in text and 'Singh2016' in text and '静态矩' in text)
check('next_day_supplement_not_main_card','附属研究' in (O/'next_day_supplement_questions.md').read_text())
missing=[]
for p in O.glob('*.md'):
 for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if not link.startswith(('#','http')) and not (O/link).exists():missing.append({'file':p.name,'link':link})
check('all_local_links_exist',not missing)
for p in O.glob('*.py'):ast.parse(p.read_text())
check('script_ASTs_parse',True)
v={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'four_artifacts_complete_with_explicit_scientific_gaps','checks':checks,'all_pass':all(c['passed'] for c in checks),'missing_links':missing,'source_hashes':{k:s['sha256'] for k,s in m['sources'].items()},'scientific_limits':['No experimental ix/omega_c fabricated','Selected gamma-path S controls only, no full adopted ledger/Cov','No all-nucleus lifetime absence claim','No universal AD/Rac gate-independence theorem','DSAM/RDDS not sufficient collective-mode certification','No user independent events read'],'canonical_modified':False,'raw_modified':False,'git_operations':False,'new_cards':False,'files':[{'path':str(p.relative_to(O)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(O.rglob('*')) if p.is_file() and p.name!='verification.json']}
(O/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2));print(json.dumps({'all_pass':v['all_pass'],'check_count':len(checks),'required':required,'missing_links':missing,'scientific_limits':v['scientific_limits']},ensure_ascii=False,indent=2))
