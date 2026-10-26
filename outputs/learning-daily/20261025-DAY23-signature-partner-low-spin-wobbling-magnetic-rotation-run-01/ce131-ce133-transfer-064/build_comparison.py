from pathlib import Path
from fractions import Fraction as F
import pymupdf,json,hashlib,datetime
O=Path(__file__).resolve().parent;ROOT=Path('/workspace/wiki')
sources={}
for key,path,offset in [
 ('AW13','raw/papers/degree dissertation/Band structures of 131Ce.pdf',4),
 ('WK22','raw/papers/degree dissertation/Triaxiality and Rotational bands in 133Ce.pdf',11),
 ('D21','raw/papers/2021_Ding et al_Signature splitting of the g 7 - 2 [ 404 ] 7 - 2 + bands in Ba 131 and Ce 133.pdf',0)]:
 f=ROOT/path;d=pymupdf.open(f)
 sources[key]={'path':path,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'pdf_pages':len(d),'printed_page_offset':offset}
def c(value,status,locator,boundary=None):
 return {'value':value,'status':status,'locator':locator,'boundary':boundary}
def unknown(reason,locator):
 return c(None,'unknown_not_reported_or_not_closed',locator,reason)
shared_boundary='Source-local labels only. Similar band numbers are not proof of identical many-body configuration or collective mode.'
pairs=[
 {'family':'negative-parity h11/2 yrast','pair_id':'B1_comparison',
  '131Ce':{'source_band_id':'AW13-Band1','N':73,
   'head_spin_parity':c('9/2- (with11/2- signature branch)','source-assignment','AW13 PDF82/p78'),
   'head_excitation_keV':unknown('The read text identifies161keV depopulation to7/2+; this task has not closed absolute adopted zero/bandhead ledger.','AW13 PDF82/p78; Fig4.1 PDF57'),
   'head_isomer':c({'reported_half_life_ns':'80','depopulation_to':'7/2+','gamma_keV':'161'},'inherited_report_not_new_lifetime','AW13 PDF82/p78 citesRef48'),
   'configuration':c('nu h11/2[514]9/2-; e/f to e/f tensor EF after proton alignment','author-interpretation','AW13 PDF81/82/84 Tables5.2/5.3'),
   'ix_initial_hbar':unknown('No central initial ix digitized from Fig5.3. Do not use Table5.4 orbital input ix2.5 as band measurement.','AW13 PDF87 Fig5.3;PDF90 Table5.4'),
   'alignment_gains':c([{'approx_gain_hbar':9,'approx_frequency_MeV_per_hbar':.3,'interpretation':'pi h11/2 pair EF'},{'approx_gain_hbar':5,'approx_frequency_MeV_per_hbar':.6,'interpretation':'possible AB; author asks more data'}],'author-extracted-and-interpreted','AW13 PDF82/p78;PDF84/p80'),
   'first_crossings':c([{'signature':'-1/2','omega_MeV_per_hbar':.329},{'signature':'+1/2','omega_MeV_per_hbar':.367}],'printed_table_values','AW13 PDF79/p75 Table5.1','Caption says accurate±.002MeV; not promoted to statistical confidence interval.'),
   'S_definition':c('four-level linear combination Eq5.5','direct-definition','AW13 PDF82/p78'),
   'S_evolution':c('Author: grows to I~13hbar, falls after first pair alignment, rises again nearI~25hbar','author-report-and-interpretation','AW13 PDF82/84','Fig5.2 caption saysBand4 while surrounding discussion refersBand1; curve not assigned as cleanBand4 datum.')},
  '133Ce':{'source_band_id':'WK22-Band1','N':75,
   'head_spin_parity':c('9/2-','source-assignment','WK22 PDF61;Table5.1 PDF66'),
   'head_excitation_keV':c('37.2','derived_from_same_table','WK22 PDF66 Table5.1','207.4-170.2; central source energy, no new uncertainty model.'),
   'configuration':c('mainly orbital18 ~nu h11/2[514]9/2-','QTR-author-interpretation','WK22 PDF99/Table6.6'),
   'ix_initial_hbar':unknown('No experimental ix curve/values for this band extracted in thesis main analysis.','WK22 Ch6.3 PDF98-115'),
   'alignment_gains':unknown('Model long-axis R_l is not experimental cranking ix.','WK22 PDF100-106'),
   'first_crossings':unknown('No matched numerical omega_c quoted forBand1 in checked thesis analysis; no cross-nucleus borrowing.','WK22 Ch6.3'),
   'S_definition':c('same four-level linear combination Eq2.37','direct-definition','WK22 PDF35/p24'),
   'S_evolution':c('Nine-orbital QTR describes Band1 S; first9/2 and11/2 ordering not reproduced; no unique gamma inversion','author-model-comparison','WK22 PDF100-101')},
  'comparison_boundary':shared_boundary},
 {'family':'negative-parity h11/2 excited','pair_id':'B4_comparison',
  '131Ce':{'source_band_id':'AW13-Band4','N':73,
   'head_spin_parity':c('15/2-','source-assignment','AW13 PDF85/p81'),
   'head_excitation_keV':c('972','author_prose_literal_not_independently_adopted','AW13 PDF85/p81','Before exact excitation-energy comparison, verify full level/link zero-point ledger. Do not silently alter reported prose.'),
   'configuration':c('possible gamma vibrational excitation coupled to e/f nuh11/2; gamma tensor e/f','author-interpretation','AW13 PDF84/85 Tables5.3 andtext','Not phonon-mode established by measured delta/lifetimes.'),
   'ix_initial_hbar':unknown('Band4 is not a labeled numerical ix series in Fig5.3; no value invented.','AW13 PDF87 Fig5.3'),
   'first_crossings':unknown('Table5.1 onlyBands1/2; cannot copyBand1 omega_c toBand4.','AW13 PDF79 Table5.1'),
   'S_evolution':unknown('Fig5.2 caption/paragraph band-ID conflict; only explicitly selected local gamma-path diagnostics generated here.','AW13 PDF82-85')},
  '133Ce':{'source_band_id':'WK22-Band4','N':75,
   'head_spin_parity':c('13/2-','source-assignment','WK22 PDF62/67'),
   'head_excitation_keV':c('832.0','source-table','WK22 PDF67 Table5.2'),
   'configuration':c('mainly same orbital18 asBand1 with extra~2hbar long-axis rotor projection in QTR/TiP interpretation','author-model-interpretation','WK22 PDF99-100/Table6.6','R_l model projection is not cranking experimental ix or measured phonon number.'),
   'ix_initial_hbar':unknown('No matched experimental ix.','WK22 Ch6.3'),
   'first_crossings':unknown('No source omega_c in current comparable low-spinBand4 analysis.','WK22 Ch6.3'),
   'S_evolution':c('Smaller magnitude/phase change compared withBand1 in Fig6.11; full-QTR reproduction ofBand4 is poor','author-model-comparison','WK22 PDF100-101')},
  'comparison_boundary':'Different head spins, source configurations and model hypotheses. Gamma vibration and TiP are competing source interpretations, not aliases of wobbling.'},
 {'family':'positive-parity g7/2 strong-coupling candidates','pair_id':'B2_comparison',
  '131Ce':{'source_band_id':'AW13-Band2','N':73,
   'head_spin_parity':c('7/2+ lowest endpoint inFig4.1/Tables4.5-6','source-assignment','AW13 PDF57/72/73'),
   'head_excitation_keV':unknown('This task did not independently fix absolute head energy from an adopted level table.','AW13 Fig4.1/PDF57'),
   'configuration':c('nu g7/2[404]7/2+ a/b; after crossing a/b tensor EF','author-interpretation','AW13 PDF81/84/86'),
   'mixed_links':c(['255.8','285.1','344.9','410.1'],'source-photon-energies-keV','AW13 PDF73 Table4.6','M1/E2 multipolarity and angular intensity ratio are not measured delta.'),
   'ix_initial_hbar':c('about1','author_curve_extraction','AW13 PDF86/p82;Fig5.3'),
   'first_crossings':c([{'signature':'-1/2','omega_MeV_per_hbar':.316},{'signature':'+1/2','omega_MeV_per_hbar':.316}],'printed_table_values','AW13 PDF79 Table5.1','Table printsnegative parity forBand2; other scheme/tables/textpositive. Preserve conflict, do not adopt erroneous paritycell.'),
   'alignment_gains':c([{'gain_hbar':'about9','frequency':'about.3MeV/hbar','interpretation':'pi h11/2 EF'},{'gain_hbar':'about2','frequency':'about.6MeV/hbar','interpretation':'possible AB;needs furtherdata'}],'author-interpretation','AW13 PDF86'),
   'low_j_Coriolis_admixture':unknown('No matched quantitative low-j wavefunction decomposition inAW13 CSM analysis; cannot transplantWK22 coefficients.','AW13 Ch5'),
   'S_amplitude_direct_numeric':unknown('No matched sourceBand2 S point list used here; no digitized amplitude.','AW13 Ch5')},
  '133Ce':{'source_band_id':'WK22-Band2','N':75,
   'head_spin_parity':c('7/2+','source-assignment','WK22 PDF69 Table5.3'),
   'head_excitation_keV':c('340 (table label);340.3 from678.1-337.8','table_literal_and_conditional_closure','WK22 PDF69 Table5.3','Do not average integer340 with inferred340.3 or suppress rounding difference.'),
   'configuration':c('predominantnu g7/2[404]7/2+ orbital20;K_l~Omega_l~7/2 athead','QTR-author-interpretation','WK22 PDF78/82'),
   'mixed_links':c(['337.8','355.3','426.4','392.8','451.4'],'source-photon-energies-keV','WK22 PDF69 Table5.3','Band2 delta list not supplied as direct fit in this table.'),
   'ix_initial_hbar':unknown('No matched experimental ix central value extracted here.','WK22 Ch6.2'),
   'first_crossings':unknown('No matched experimental omega_c reported here.','WK22 Ch6.2'),
   'low_j_Coriolis_admixture':c('neighbor s1/2/d3/2 K1/2 components; gamma and chi jointly affectS; chi=.7 needslargergamma~20deg','author-model-interpretation','WK22 PDF82-84','Table6.3 9/2+ printed top3 amplitudes squared sum>1; actual normalized fullwavefunction not recovered.'),
   'S_amplitude_direct_numeric':unknown('Figures6.1-6.5 show model/data; no curve digitization treated as exact table.','WK22 PDF80-86')},
  'comparison_boundary':'Similar proposedg7/2 family, not a source-localBand2 identity proof. AW13 CSM/high-spin pair crossings andWK22 low-spin QTR/mixing probe different aspects; gamma axis/sign conventions not averaged.'},
 {'family':'low-j positive-parity low-energy sequences','pair_id':'B3_comparison',
  '131Ce':{'source_band_id':'AW13-Band3','N':73,
   'head_spin_parity':c('1/2+','source-assignment','AW13 PDF86/p82'),
   'head_excitation_keV':c('61.8','source-prose','AW13 PDF86/p82'),
   'ground_state_band':c(False,'direct_boundary','AW13 PDF86/p82','Do not callthe61.8keV sequencegroundband.'),
   'configuration':c('possible nu s1/2[400]1/2+ c/d','author-interpretation','AW13 PDF81/84/86','No measureds1/2-d3/2 mixture inferred here.'),
   'observed_E2_keV':c(['338.1','509.9','623.4','743.3'],'source-table','AW13 PDF70 Table4.4'),
   'band2_near_degeneracy':unknown('No complete common-zeroBand3 adopted energyledger fromthe checkedpages; no fabricated crossing.','AW13 PDF57/70/86'),
   'ix_initial_hbar':unknown('No numeric matchedBand3 ix curve.','AW13 Fig5.3'),
   'first_crossings':unknown('No fittedomega_c forBand3.','AW13 Table5.1')},
  '133Ce':{'source_band_id':'WK22-Band3','N':75,
   'head_spin_parity':c('1/2+','source-assignment','WK22 PDF64/p53'),
   'head_excitation_keV':c('0','source-groundstate-assignment','WK22 PDF64/71'),
   'ground_state_band':c(True,'source-groundstate-assignment','WK22 PDF64'),
   'configuration':unknown('Band3 is observedpositive low-j sequence; no dedicated microscopics/d mixing fit for this band in the checkedthesis mainline.','WK22 PDF64/71;Ch6focusBand2'),
   'level_energies_keV':c({'3/2':'134.2','5/2':'318.3','7/2':'570.4','9/2':'815.9','11/2':'1201.4','13/2':'1445.8','15/2':'1932.9','17/2':'2171.9'},'source-table','WK22 PDF71 Table5.4'),
   'band2_near_degeneracy':c({'same_spin':'13/2+','Band3_keV':'1445.8','Band2_keV':'1459.9','Band2_minus_Band3_keV':'14.1','new_link_keV':'412.4','link':'Band3 13/2+ toBand2 11/2+'},'task-conditional-energy-difference-plus-source-link','WK22 Tables5.3/5.4 PDF69/71','Same-spin closeness/level ordering reversal is not a measuredavoided-crossing strength or omega_c.'),
   'ix_initial_hbar':unknown('No matchedexperimentalix.','WK22 Ch6'),
   'first_crossings':unknown('No fittedomega_c forBand3; do not reinterpret14.1keV asfrequency.','WK22 PDF69/71')},
  'comparison_boundary':'The requested s1/2/d3/2 category is a candidatecomparison frame, not proof thatbothBand3 microscopic contentsarethe same.'}
]
# Exact selected-gamma-path S control; not full adopted energy network or published S values.
gamma_paths={
 'AW13-B1':{'11/2':'137.4','13/2':'335.4','15/2':'171.8','17/2':'483.8','19/2':'154.8'},
 'WK22-B1':{'11/2':'170.2','13/2':'384.7','15/2':'235.0','17/2':'517.6','19/2':'245.6'},
 'AW13-B4':{'17/2':'243.7','19/2':'382.1','21/2':'390.1','23/2':'363.8'},
 'WK22-B4':{'15/2':'368.8','17/2':'209.0','19/2':'399.3','21/2':'490.4','23/2':'380.4'}
}
S={}
for key,path in gamma_paths.items():
 d={F(k):F(v) for k,v in path.items()};rows=[]
 for i in sorted(d):
  if i-1 in d and i+1 in d:
   val=d[i]-(d[i-1]+d[i+1])/2
   rows.append({'I':str(i),'S_keV':str(val),'S_numeric_keV':float(val),'selected_delta_E_I_minus_1_keV':str(d[i-1]),'selected_delta_E_I_keV':str(d[i]),'selected_delta_E_I_plus_1_keV':str(d[i+1])})
 S[key]=rows
assert next(x['S_numeric_keV'] for x in S['AW13-B1'] if x['I']=='13/2')==180.8
assert next(x['S_numeric_keV'] for x in S['WK22-B1'] if x['I']=='13/2')==182.1
r={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Source-grounded partialbandcomparison and operationblueprint, nottargetdataanalysis or modecertification','sources':sources,'nuclei':{'131Ce':{'Z':58,'N':73},'133Ce':{'Z':58,'N':75}},'band_pair_matrix':pairs,'selected_local_S_control':{'definition':'deltaE(I)-[deltaE(I-1)+deltaE(I+1)]/2','same_original_definition':'AW13 Eq5.5/PDF82 andWK22 Eq2.37/PDF35','units':'keV','gamma_paths':gamma_paths,'results':S,'boundary':'Explicitly chosen adjacent intraband mixed-gamma central values, not uniqueglobaladoptedlevel reconstruction; noCov/errorbars; redundantedgesmaydiffer and requireclosure audit.','locators':{'AW13-B1':'Table4.2/PDF68','AW13-B4':'Table4.4/PDF70;intrabranch243.7notinter611.1','WK22-B1':'Table5.1/PDF66','WK22-B4':'Table5.2/PDF67'}},'lifetime_boundary':'AW13 acquisition doesnot supplytargetpartner/links tau/delta/P; independentSI16/LI04lifetimesandIB98staticmoments exist but are not automaticallysamebandnetwork. Notall131Cetaumissing.','scientific_status':'self-auditdraft; allnewclaimsneedreview;nohumanreviewupgrade','canonical_modified':False,'git_operations':False,'raw_modified':False}
(O/'comparison_matrix.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
print(json.dumps({'pairs':len(pairs),'selected_S':S,'source_sha256':{k:v['sha256'] for k,v in sources.items()}},ensure_ascii=False,indent=2))
