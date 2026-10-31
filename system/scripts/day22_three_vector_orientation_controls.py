#!/usr/bin/env python3
"""Signed triple product, RMS andGram-of-means in specified coupledspin states; notpaper replay."""
import math,json,argparse,hashlib,itertools
from fractions import Fraction as F
import numpy as np
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def cg(j1,j2,J,m1,m2,M):
 if m1+m2!=M or abs(M)>J or abs(m1)>j1 or abs(m2)>j2 or not abs(j1-j2)<=J<=j1+j2:return 0.
 a,b,c=int(j1+j2-J),int(j1-m1),int(j2+m2);d,e=int(J-j2+m1),int(J-j1-m2)
 pref=F(int(2*J+1)*math.factorial(a)*math.factorial(int(j1-j2+J))*math.factorial(int(-j1+j2+J)),math.factorial(int(j1+j2+J+1)))
 for x in [j1+m1,j1-m1,j2+m2,j2-m2,J+M,J-M]:pref*=math.factorial(int(x))
 total=sum((F((-1)**z,math.factorial(z)*math.factorial(a-z)*math.factorial(b-z)*math.factorial(c-z)*math.factorial(d+z)*math.factorial(e+z)) for z in range(max(0,-d,-e),min(a,b,c)+1)),F(0))
 return math.sqrt(float(pref))*float(total)

def case(R,k,total_spin=9):
 jp=jn=5.5;J=M=total_spin
 states=[(mp/2,mn/2,mr) for mp in range(-11,12,2) for mn in range(-11,12,2) for mr in range(-R,R+1) if mp/2+mn/2+mr==M]
 idx={v:i for i,v in enumerate(states)};D=len(states)
 def dot(i,j):
  out=np.zeros((D,D));spins=[jp,jn,R]
  for col,s in enumerate(states):
   out[col,col]+=s[i]*s[j]
   for delta in [-1,1]:
    new=list(s);new[i]+=delta;new[j]-=delta;new=tuple(new)
    if new not in idx:continue
    val=.5*math.sqrt((spins[i]*(spins[i]+1)-s[i]*(s[i]+delta))*(spins[j]*(spins[j]+1)-s[j]*(s[j]-delta)))
    out[idx[new],col]+=val
  return out
 PN,NR,PR=dot(0,1),dot(1,2),dot(0,2)
 A=(jp*(jp+1)+jn*(jn+1))*np.eye(D)+2*PN
 B=(jn*(jn+1)+R*(R+1))*np.eye(D)+2*NR
 J2=(jp*(jp+1)+jn*(jn+1)+R*(R+1))*np.eye(D)+2*(PN+NR+PR)
 chi=1j/4*(A@B-B@A)
 # Independent Cartesian construction, then select the same fixed-M sector.
 def cartesian(j):
  ms=np.arange(-j,j+1);plus=np.zeros((len(ms),len(ms)),complex)
  for col,m in enumerate(ms[:-1]):plus[col+1,col]=math.sqrt(j*(j+1)-m*(m+1))
  return [(plus+plus.conj().T)/2,(plus-plus.conj().T)/(2j),np.diag(ms)]
 cp,cn,cr=cartesian(jp),cartesian(jn),cartesian(R)
 fullidx=np.array([int(mp+jp)*int(2*jn+1)*int(2*R+1)+int(mn+jn)*int(2*R+1)+int(mr+R) for mp,mn,mr in states])
 direct=np.zeros((D,D),complex)
 for a,b,c,sign in [(0,1,2,1),(1,2,0,1),(2,0,1,1),(0,2,1,-1),(2,1,0,-1),(1,0,2,-1)]:
  term=np.kron(np.kron(cp[a],cn[b]),cr[c]);direct+=sign*term[np.ix_(fullidx,fullidx)]
 direct_error=float(np.max(np.abs(chi-direct)))
 # Exact dimensionless (hbar=1) operator identity, not factorization of means.
 S1=S2=jp*(jp+1);S3=R*(R+1)
 symABC=sum(x@y@z for x,y,z in itertools.permutations([PN,NR,PR]))/6
 anticommutators=PN@NR+NR@PN+NR@PR+PR@NR+PR@PN+PN@PR
 chi2rhs=S1*S2*S3*np.eye(D)-S1*(NR@NR)-S2*(PR@PR)-S3*(PN@PN)+2*symABC-(S3*PN+S2*PR+S1*NR+anticommutators)/3
 square_error=float(np.max(np.abs(direct@direct-chi2rhs)))
 den=math.sqrt(jp*(jp+1)*jn*(jn+1)*R*(R+1))
 v=np.array([cg(jp,jn,k,mp,mn,mp+mn)*cg(k,R,J,mp+mn,mr,M) for mp,mn,mr in states])
 products=[float(v@x@v) for x in [PN,NR,PR]]
 S=jp*(jp+1);G=np.array([[S,products[0],products[2]],[products[0],S,products[1]],[products[2],products[1],R*(R+1)]])
 result={'R':R,'jpn':k,'I':J,'jp_jn':jp,'D_fixed_M':D,'M':M,'norm':float(v@v),'A_eigen_error':float(np.linalg.norm(A@v-k*(k+1)*v)),'J2_eigen_error':float(np.linalg.norm(J2@v-J*(J+1)*v)),'chi_squared_pair_operator_identity_error':square_error,'direct_cartesian_triple_vs_commutator_error':direct_error,'chi_hermitian_error':float(np.max(np.abs(chi-chi.conj().T))),'signed_chi_normalized':float((v.conj()@chi@v).real/den),'signed_imaginary_rounding':float((v.conj()@chi@v).imag/den),'RMS_chi_normalized':float(np.linalg.norm(chi@v)/den),'Gram_of_pair_means_proxy':math.sqrt(max(0,float(np.linalg.det(G))))/den,'Gram_pair_mean_matrix':G.tolist()}
 if (R,k,J)==(2,9,9):
  vnext=np.array([cg(jp,jn,10,mp,mn,mp+mn)*cg(10,R,J,mp+mn,mr,M) for mp,mn,mr in states])
  gdiag=np.array([(1.21*mp-.21*mn+.41*mr)/J for mp,mn,mr in states])
  packets=[]
  for sign in [1,-1]:
   psi=(v+sign*1j*vnext)/math.sqrt(2)
   packets.append({'chosen_relative_phase':sign,'norm':float(np.vdot(psi,psi).real),'g_for_chosen_source_like_operator':float(np.vdot(psi,gdiag*psi).real),'signed_chi_normalized':float(np.vdot(psi,chi@psi).real/den),'J2_error':float(np.linalg.norm(J2@psi-J*(J+1)*psi))})
  result['conjugate_packet_witness']=packets
 return result
def calculate():
 RAW=ROOT/'raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/g-factor/2018_Grodner et al_First Measurement of the g Factor in the Chiral Band.pdf'
 SHA='c71ec59160c444c34ab7f340db5f045c1f26456bc1741197ec62caea7f4efbf2'
 if hashlib.sha256(RAW.read_bytes()).hexdigest()!=SHA:raise ValueError('raw identity mismatch')
 rows=[case(2,9),case(4,8)]
 checks={'coupled_states_normalized_and_good_jpn_I':all(abs(r['norm']-1)<1e-12 and max(r['A_eigen_error'],r['J2_eigen_error'])<1e-10 for r in rows),'signed_chi_Hermitian_and_zero_in_fixed_jpn_state':all(r['chi_hermitian_error']<1e-12 and abs(r['signed_chi_normalized'])<1e-12 for r in rows),'RMS_positive_and_not_Gram_proxy':all(r['RMS_chi_normalized']>0 and abs(r['RMS_chi_normalized']-r['Gram_of_pair_means_proxy'])>.1 for r in rows)}
 stretched=case(2,11,13)
 checks['chi_squared_exact_symmetrized_pair_identity']=all(r['chi_squared_pair_operator_identity_error']<1e-9 for r in rows+[stretched])
 checks['independent_Cartesian_triple_matches_commutator']=all(r['direct_cartesian_triple_vs_commutator_error']<1e-11 for r in rows+[stretched])
 checks['stretched_Gram_matches_independent_analytic_formula']=abs(stretched['Gram_of_pair_means_proxy']-math.sqrt((13+1)/((5.5+1)**2*(2+1))))<1e-12
 checks['stretched_state_zero_signed_RMS_but_nonzero_Gram_proxy']=stretched['D_fixed_M']==1 and abs(stretched['signed_chi_normalized'])<1e-12 and stretched['RMS_chi_normalized']<1e-12 and stretched['Gram_of_pair_means_proxy']>.1
 packets=rows[0]['conjugate_packet_witness']
 checks['chosen_conjugate_packets_same_g_opposite_nonzero_signed_chi']=all(abs(p['norm']-1)<1e-12 and p['J2_error']<1e-10 for p in packets) and abs(packets[0]['g_for_chosen_source_like_operator']-packets[1]['g_for_chosen_source_like_operator'])<1e-12 and abs(packets[0]['signed_chi_normalized']+packets[1]['signed_chi_normalized'])<1e-12 and abs(packets[0]['signed_chi_normalized'])>.1
 return {'raw_sha256':SHA,'scope':'conditionalindependentlaboratoryspinoperatorprobe;notGR18produceridentification','commutator_identity':'chi=(i/4)[(jp+jn)^2,(jn+R)^2]','chi_squared_identity_hbar1':'A=jp.dot(jn),B=jn.dot(R),C=R.dot(jp),Si=ji(ji+1); chi^2=S1*S2*S3-S1*B^2-S2*C^2-S3*A^2+2*Sym(ABC)-(S3*A+S2*C+S1*B+{A,B}+{B,C}+{C,A})/3','fixed_k_proof':'AnA-eigenstatehassameleft/rightAeigenvalue,soexpectationcommutatoriszero.','rows':rows,'stretched_product_counterexample':stretched,'controls':checks,'boundaries':['GR18Eq3literalformneedsRef14/authoroperatorconventionbeforeanypublication-errorclaim.','DoNOTsilentlyreplaceauthorssignednotationwithRMSorGramofmeans.','Gramproxycanapproach1inchosencouplingsbutdoesnotprovethatistheauthorsactualalgorithm.','Conjugatepacketsarechosencomplexsuperpositions,notstationarynuclearbandstatesorameasuredchiraldoublet.',
 'TheJ13stretchedstateisanadditionalchosencontrol,notGR18isomeroritsreportedcouplingexample.',
 'Experimental g=.59(1)isnotrevised;paper PRMgeometryremainsauthor/modelclaim.','InitialCGprobeomittedabs(M)>Jguardandfailedbeforewriting;guardcorrectedwithsamephysicsinputs.']}

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True);a=p.parse_args();out=(ROOT/a.output).resolve()
 if not out.is_relative_to(ROOT/'outputs'):p.error('outputmustbeinsideoutputs/')
 d=calculate();out.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'controls':d['controls'],'rows':d['rows']}));return 0 if all(d['controls'].values()) else 1
if __name__=='__main__':raise SystemExit(main())
