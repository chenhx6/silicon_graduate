#!/usr/bin/env python3
"""MP80 independent checks of the existing D66 full-beta sign audit."""
from __future__ import annotations
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
from zoneinfo import ZoneInfo
import mpmath as mp
from day16_diamond1966_domain_replay import angular_coefficients,bounds,verify_partition,number


def sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--contract',required=True,type=Path);p.add_argument('--output',required=True,type=Path);a=p.parse_args();c=json.loads(a.contract.read_text());assert c['identity']=='D66-FULLBETA-P-SIGN-INDEPENDENT-REPLAY-01';r=a.contract.parent
    for k in ['result','sign_contract']:assert sha(r/c[k])==c[k+'_sha256']
    data=json.loads((r/c['result']).read_text());sc=json.loads((r/c['sign_contract']).read_text());base=json.loads((r/sc['base_contract']).read_text());domain=json.loads((r/sc['previous_domain_result']).read_text());phases={(x['Ji2'],x['Jf2']):x['native_cross_sign_relative_to_Racah_F12'] for x in domain['coefficient_crosschecks']};mp.mp.dps=c['precision_decimal_digits']
    checked=[];dual_gap=None
    for row in data['results']:
        top,mid,mode,sign=row['top2'],row['mid2'],row['mode'],row['sign_constraint'];z=row['audit']
        if z['status']=='numerically-separated-all-cells':
            assert [top,mid,sign]==[13,11,'P701_nonpositive']
            verify_partition(z['initial_box'],z['negative_cells'])
            assert len(z['negative_cells'])==1
            cell=z['negative_cells'][0];A,b=bounds(top,[('331',mid),('701',9)],cell['box'],mode,base,phases)
            # Pure E2 fixes the photon rank relation exactly for this path.
            A2=angular_coefficients(top,9,2,phases[(top,9)])[1]
            A4=angular_coefficients(top,9,4,phases[(top,9)])[1]
            A.append([mp.mpf('1.5')*x+mp.mpf('.625')*y for x,y in zip(A2,A4)]);b.append(mp.mpf(0))
            lam=list(map(number,cell['lambda']));assert min(lam)>=0
            dual_gap=min(sum(lam[j]*A[j][i] for j in range(len(lam))) for i in range(len(A[0])))-sum(x*y for x,y in zip(lam,b))
            assert dual_gap>mp.mpf('1e-8')
            qlo=mp.mpf('1.5')*mp.mpf('.22')+mp.mpf('.625')*mp.mpf('-.07');assert qlo==mp.mpf('.28625')
            checked.append({'top2':top,'mid2':mid,'constraint':sign,'MP80_negative_dual_gap':str(dual_gap),'analytic_Stokes_Q_lower':str(qlo)})
        else:
            assert z['status']=='strict-nonzero-sign-witness';w=z['witness'];q=list(map(number,w['q_pair']));assert min(q)>0 and abs(sum(q)-1)<mp.mpf('1e-10')
            computed={};P=None
            for line,jf,beta in [('331',mid,w['betas_native_deg'][0]),('701',9,w['betas_native_deg'][1])]:
                C2=angular_coefficients(top,jf,2,phases[(top,jf)]);C4=angular_coefficients(top,jf,4,phases[(top,jf)])
                B=mp.radians(number(beta));co,si=mp.cos(B),mp.sin(B);weights=[co*co,si*si,2*co*si]
                two=sum(weights[j]*sum(x*y for x,y in zip(C2[j],q)) for j in range(3));four=sum(weights[j]*sum(x*y for x,y in zip(C4[j],q)) for j in range(3))
                for k,val in [(2,two),(4,four)]:
                    mean,err=map(number,base['observations'][line]['a'+str(k)]);assert mean-err-mp.mpf('1e-9')<=val<=mean+err+mp.mpf('1e-9')
                if line=='701':
                    cQ=[[mp.mpf('1.5')*x for x in C2[0]],
                        [mp.mpf('1.5')*x+mp.mpf('.625')*y for x,y in zip(C2[1],C4[1])],
                        [-mp.mpf('.5')*x for x in C2[2]]]
                    Q=sum(weights[j]*sum(x*y for x,y in zip(cQ[j],q)) for j in range(3));I=1-two/2+mp.mpf('.375')*four;P=Q/I
                    assert abs(P-number(w['P701']))<mp.mpf('1e-10')
                    assert P<mp.mpf('-1e-6') if sign=='P701_nonpositive' else P>mp.mpf('1e-6')
                computed[line]={'a2':float(two),'a4':float(four)}
            if mode=='extra_lowm_u2nonpositive':
                J=mp.mpf(top)/2;moment=sum(p*(3*(J-i)**2-J*(J+1)) for i,p in enumerate(q));assert moment<=mp.mpf('1e-9')
            checked.append({'top2':top,'mid2':mid,'constraint':sign,'P701_MP80':float(P),
                'min_q_pair':float(min(q)),'AD_MP80':computed})
    assert len(checked)==8 and dual_gap is not None
    assert all(x['equals_minus2_A2interference'] for x in data['interference_identity_controls'])
    out={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),'script_sha256':sha(Path(__file__)),
        'contract_sha256':sha(a.contract),'precision_decimal_digits':mp.mp.dps,'all8_cases_replayed':checked,
        'conclusion':'three mixedspin/populationfamilies allowbothP701signs in declaredsameparitynativepointmodel; pureE2pathpositive',
        'interference_identity_from_pure_and_cross_rank_coefficients':True,
        'scope':{'no_unique_family_identification_from_fixed_points':True,'unknown_EMduality_and_actual_response_cov_remain':True,
            'no_new_experimental_P_delta_spin_or_CI':True,'only_existing_bounded_analysis':True}}
    a.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
