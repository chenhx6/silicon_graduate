#!/usr/bin/env python3
"""TwoD2-symmetric mixed spin4 densities with same RMS anddifferentSCS maps; chosen control."""
import argparse,hashlib,json,math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
SOURCES=[('raw/papers/2022_Chen_Frauendorf_Study of wobbling modes by means of spin coherent state maps.pdf','ebe826198cf89f720478f0e525dd0b457b2c6eb227ae055de601b3cdd7c57a6b'),('raw/papers/2022_Chen_Frauendorf_Publisher Erratum.pdf','d0bb7ad17dcac5be0442a0d37b58602b7e4eac01d321fc7bed88bfdec5b5ff82')]
def calculate():
 for p,sha in SOURCES:
  if hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=sha:raise ValueError('source identity mismatch')
 spin=4;ks=[0,2,4];pa=[F(23,60),F(16,60),F(21,60)];pb=[F(17,60),F(24,60),F(19,60)]
 # Basis|K0>,(|K>+|-K>)/sqrt2 forK2/4. AllaretrivialD2 representations forevenI.
 def moments(p):
  z2=sum(p0*k*k for p0,k in zip(p,ks));z4=sum(p0*k**4 for p0,k in zip(p,ks));xy=(spin*(spin+1)-z2)/2
  return {'Jx2':str(xy),'Jy2':str(xy),'Jz2':str(z2),'Jz4':str(z4)}
 def density(p,u,phi):
  c=math.sqrt((1+u)/2);s=math.sqrt((1-u)/2)
  def amplitude(k):return math.sqrt(math.comb(2*spin,spin+k))*c**(spin+k)*s**(spin-k)*complex(math.cos(k*phi),math.sin(k*phi))
  values=[]
  for k in ks:
   a=amplitude(0) if k==0 else (amplitude(k)+amplitude(-k))/math.sqrt(2)
   values.append(abs(a)**2)
  return (2*spin+1)/(4*math.pi)*sum(float(w)*v for w,v in zip(p,values))
 u,w=np.polynomial.legendre.leggauss(16);phis=np.arange(32)*2*np.pi/32
 integrals=[sum(float(weight)*sum(density(p,float(x),float(phi)) for phi in phis)*2*math.pi/len(phis) for x,weight in zip(u,w)) for p in [pa,pb]]
 minq=min(density(p,float(x),float(phi)) for p in [pa,pb] for x in u for phi in phis)
 points=[{'theta':th,'phi':ph,'Qa_per_steradian':density(pa,math.cos(th),ph),'Qb_per_steradian':density(pb,math.cos(th),ph)} for th,ph in [(0,0),(math.pi/2,0),(math.pi/2,math.pi/4),(math.pi/2,math.pi/2)]]
 controls={
  'two_positive_normalized_mixtures':sum(pa)==sum(pb)==1 and min(pa+pb)>0,
  'all_three_exact_second_moments_identical':all(moments(pa)[k]==moments(pb)[k] for k in ['Jx2','Jy2','Jz2']),
  'different_exact_fourth_moments':moments(pa)['Jz4']!=moments(pb)['Jz4'],
  'two_SCS_maps_solid_angle_normalized':max(abs(float(z)-1) for z in integrals)<1e-12,
  'sampled_map_nonnegative':minq>=0,
  'maps_differ_at_verified_point':abs(points[1]['Qa_per_steradian']-points[1]['Qb_per_steradian'])>1e-3,
 }
 return {'source_hashes':dict(SOURCES),'source_formula':'CF22p4Eq17/19D2basis;p7Eq31–32map andmeasure;erratumFig15identity only','chosen_spin':spin,'D2_basis_K':[0,2,4],'mixture_a':[str(z) for z in pa],'mixture_b':[str(z) for z in pb],'moments_a':moments(pa),'moments_b':moments(pb),'map_integrals':list(map(float,integrals)),'point_comparison':points,'controls':{k:bool(v) for k,v in controls.items()},'boundaries':['Arbitrary chosen mixed states inallowedD2subspace, not eigenstates ofthe sameHamiltonian or measurednuclearstates.','NoTW/LW/flip labels assigned; distinctmap aloneisnotanexperimental mode identification.','Thiscalculationuses densityperdOmega;CF22cylindricalP equalsQsin(theta).','Body-fixedphi signdoesnotchangethisrealD2-symmetricexample;generalphaseconventions stillmatter.','NoSCS tomography fromspectroscopicdata,transitiondensity orabsoluteB inferred.']}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True);a=p.parse_args();out=(ROOT/a.output).resolve()
 if not out.is_relative_to(ROOT/'outputs'):p.error('outputmustbeinsideoutputs/')
 d=calculate();out.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'controls':d['controls'],'moments_a':d['moments_a'],'moments_b':d['moments_b'],'map_integrals':d['map_integrals'],'points':d['point_comparison']}));return 0 if all(d['controls'].values()) else 1
if __name__=='__main__':raise SystemExit(main())
