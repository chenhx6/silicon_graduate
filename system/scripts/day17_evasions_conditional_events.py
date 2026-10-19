#!/usr/bin/env python3
"""Read-only conditional track/event descriptors, not original physics selection."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
import numpy as np
import ROOT as R

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'

QUERY = r'''
#include <TFile.h>
#include <TTree.h>
#include <cmath>
#include <sstream>
#include <iomanip>
#include <stdexcept>
#include <vector>
std::string day17_conditional_events(const char* name, double shift, double beta,
    double alo, double ahi, double glo, double ghi, const std::vector<double>& edges) {
    TFile file(name,"READ");
    auto t = dynamic_cast<TTree*>(file.Get("TreeMaster"));
    if(!t || t->GetMaximum("nbTrack")>31) throw std::runtime_error("missing tree or array bound");
    int nt=0; float b=0,ta=0,e[31],x[31],y[31],z[31];
    t->SetBranchStatus("*",0);
    for(auto field:{"nbTrack","Brho","ThetaLdeg","trackE","trackX1","trackY1","trackZ1"}) t->SetBranchStatus(field,1);
    if(t->SetBranchAddress("nbTrack",&nt)<0 || t->SetBranchAddress("Brho",&b)<0 ||
       t->SetBranchAddress("ThetaLdeg",&ta)<0 || t->SetBranchAddress("trackE",e)<0 ||
       t->SetBranchAddress("trackX1",x)<0 || t->SetBranchAddress("trackY1",y)<0 ||
       t->SetBranchAddress("trackZ1",z)<0) throw std::runtime_error("branch binding");
    long long base=0, angular=0, malformed=0; bool first=true;
    std::ostringstream records; records<<std::setprecision(17)<<"[";
    for(long long i=0;i<t->GetEntries();++i) {
        if(t->GetEntry(i)<=0 || nt<0 || nt>31) throw std::runtime_error("event read");
        if(!std::isfinite(b)||!std::isfinite(ta)) {++malformed;continue;}
        if(!(b>0 && ta>=alo && ta<ahi)) continue;
        ++base; int n[3]={0,0,0};
        for(int k=0;k<nt;++k) {
            if(!std::isfinite(e[k])||!std::isfinite(x[k])||!std::isfinite(y[k])||!std::isfinite(z[k])||e[k]<=0) {++malformed;continue;}
            double zz=z[k]+shift, rr=std::sqrt(x[k]*x[k]+y[k]*y[k]+zz*zz);
            if(rr<=0) {++malformed;continue;}
            double theta=std::acos(zz/rr)*180/std::acos(-1.);
            if(theta<glo || theta>ghi) continue;
            ++angular;
            double dc=e[k]*(1-beta*std::cos(theta*std::acos(-1.)/180))/std::sqrt(1-beta*beta);
            for(int w=0;w<3;++w) if(dc>=edges[2*w] && dc<edges[2*w+1]) ++n[w];
        }
        if(n[0]+n[1]+n[2]) {
            if(!first) records<<","; first=false;
            records<<"["<<i<<","<<b<<","<<ta<<","<<n[0]<<","<<n[1]<<","<<n[2]<<"]";
        }
    }
    records<<"]";
    std::ostringstream out; out<<"{\"input_entries\":"<<t->GetEntries()<<",\"base_events\":"<<base
        <<",\"angular_tracks\":"<<angular<<",\"malformed\":"<<malformed<<",\"records\":"<<records.str()<<"}";
    return out.str();
}
'''


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    cp = RUN / 'evasions2023-conditional-event-contract.json'
    c = json.loads(cp.read_text())
    assert sha(ROOT / c['data']) == c['data_sha256']
    manifest = json.loads((ROOT / c['source_manifest']).read_text())
    source = ROOT / 'tmp/day17-fougeres2023/producer-source'
    assert len(manifest['files']) == 34
    assert all(sha(source/x['path']) == x['sha256'] for x in manifest['files'])
    assert R.gInterpreter.Declare(QUERY)
    edges = R.std.vector('double')([v for pair in c['DC_windows_keV'] for v in pair])
    q = json.loads(str(R.day17_conditional_events(str(ROOT/c['data']), c['relative_Z_shift_mm'],
                      c['beta_mean'], *c['thetaAlpha_range_deg'], *c['thetaGamma_lab_range_deg'], edges)))
    assert q['input_entries'] == c['input_entries'] and q['malformed'] == 0
    records = np.asarray(q['records'], dtype=float).reshape(-1, 6)
    counts = records[:,3:6]
    totals = counts.sum(axis=0)
    second = counts.T@counts
    v = np.array([-.5,1,-.5])
    weighted = counts@v
    value = float(weighted.sum())
    cluster = float(weighted@weighted)
    track_diagonal = float((v*v)@totals)
    fixedN = second-np.outer(totals,totals)/q['base_events']
    assert np.linalg.eigvalsh(second).min() > -1e-9
    assert np.linalg.eigvalsh(fixedN).min() > -1e-9
    hist = [np.histogram(records[:,1], bins=c['B_hist_edges_Tm'], weights=counts[:,w])[0].tolist() for w in range(3)]
    b = records[:,1]
    r = b*c['native_reduced_momentum_coefficient']
    valid = r*r<1
    literal = np.full_like(r,np.nan)
    literal[valid] = c['native_energy_MeV_mass']*(1/np.sqrt(1-r[valid]*r[valid])-1)
    momentum = c['native_energy_MeV_mass']*(np.sqrt(1+r*r)-1)
    lo, hi = c['alpha_energy_gate_MeV']
    energy_descriptor = {}
    for label, energy in [('literal_public_conversion',literal),('same_constant_momentum_relation',momentum)]:
        inside = (energy>=lo)&(energy<hi)
        energy_descriptor[label] = {'conditional_signal_tracks_in_gate': int(counts[inside,1].sum()),
                                   'conditional_signal_events_in_gate': int(np.count_nonzero(inside&(counts[:,1]>0))),
                                   'signal_entry_ids': records[inside&(counts[:,1]>0),0].astype(int).tolist(),
                                   'boundary': 'same approximate gamma query, not measured key-state purity or corrected yield'}
    sets = [set(x['signal_entry_ids']) for x in energy_descriptor.values()]
    membership = {'common_signal_entries': sorted(sets[0]&sets[1]),
                  'literal_only_signal_entries': sorted(sets[0]-sets[1]),
                  'momentum_only_signal_entries': sorted(sets[1]-sets[0]),
                  'same_membership': sets[0] == sets[1]}
    out = {'at':datetime.now(timezone.utc).isoformat(),'script_sha256':sha(Path(__file__)),
           'contract_sha256':sha(cp),'ROOT_helper':R.gROOT.GetVersion(),
           'input_entries':q['input_entries'],'base_events':q['base_events'],'angular_tracks':q['angular_tracks'],
           'malformed':q['malformed'],'window_order':['lower','signal','upper'],
           'window_track_totals':totals.tolist(),'events_in_any_window':len(records),
           'events_per_window':np.count_nonzero(counts,axis=0).tolist(),
           'events_with_multiple_window_tracks':int(np.count_nonzero(counts.sum(axis=1)>1)),
           'sum_event_outer_products':second.tolist(),
           'conditional_fixed_N_centered_second_moment':fixedN.tolist(),
           'background_subtraction_operator':v.tolist(),'conditional_signed_descriptor':value,
           'Poissonized_record_cluster_second_moment':cluster,
           'independent_track_diagonal_approximation':track_diagonal,
           'conditional_fixed_N_weight_second_moment':float(v@fixedN@v),
           'B_hist_edges_Tm':c['B_hist_edges_Tm'],'window_B_histograms':hist,
           'energy_gate_descriptors':energy_descriptor,'record_columns':['entry','Brho_Tm','ThetaLdeg','nLower','nSignal','nUpper'],
           'same_count_gate_membership_comparison':membership,
           'selected_records':q['records'], 'source34_and_original_data_hashes_verified':True,
           'not_original_recoil_PiD_contamination_selection':True,
           'no_new_experimental_yield_tau_branch_or_CI':True,'ok':True}
    assert sha(ROOT/c['data']) == c['data_sha256']
    (RUN/'evasions2023-conditional-event-result.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['selected_records','window_B_histograms','B_hist_edges_Tm']},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
