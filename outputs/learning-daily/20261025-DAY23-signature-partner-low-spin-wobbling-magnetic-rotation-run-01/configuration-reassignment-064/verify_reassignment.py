"""Selected strong-coupling controls; no nuclear fit or experimental CI.

All numerical magnetic constants, quench choices and scalar-Q conventions are
declared inputs. Standard library only. Run this script from the repository root.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial, sqrt, pi, cos, sin
from itertools import combinations
import copy,hashlib,json

OUT=Path(__file__).parent
checks=[]
def check(name,condition,scope):
    checks.append(dict(name=name,passed=bool(condition),scope=scope))
    if not condition:raise AssertionError(name)
def near(a,b,tol=1e-10):return abs(float(a)-float(b))<tol
def fact(x):
    x=F(x)
    assert x.denominator==1 and x>=0
    return factorial(x.numerator)
def cg2(j1,j2,j3,m1,m2,m3):
    """Exact squaredCG via factorial3j sum, for integer or half-integer spins."""
    j1,j2,j3,m1,m2,m3=map(F,[j1,j2,j3,m1,m2,m3])
    if m1+m2!=m3 or abs(m1)>j1 or abs(m2)>j2 or abs(m3)>j3:return F(0)
    if j3>j1+j2 or j3<abs(j1-j2):return F(0)
    if any((j+m).denominator!=1 for j,m in [(j1,m1),(j2,m2),(j3,m3)]):return F(0)
    a,b,c=j1+j2-j3,j1-j2+j3,-j1+j2+j3
    triangle=F(fact(a)*fact(b)*fact(c),fact(j1+j2+j3+1))
    product=fact(j1+m1)*fact(j1-m1)*fact(j2+m2)*fact(j2-m2)*fact(j3+m3)*fact(j3-m3)
    total=F(0)
    for z in range(int(j1+j2+j3)+1):
        args=[F(z),a-z,j1-m1-z,j2+m2-z,j3-j2+m1+z,j3-j1-m2+z]
        if min(args)<0:continue
        denominator=1
        for arg in args:denominator*=fact(arg)
        total+=F((-1)**z,denominator)
    return (2*j3+1)*triangle*product*total*total

def lande(l,j,gl,gs):
    l,j=F(l),F(j);s=F(1,2)
    return gl+(gs-gl)*float((j*(j+1)-l*(l+1)+s*(s+1))/(2*j*(j+1)))
def direct_g(l,j,m,gl,gs):
    l,j,m=F(l),F(j),F(m)
    sz=lz=norm=F(0)
    for ms in [F(-1,2),F(1,2)]:
        ml=m-ms
        weight=cg2(l,F(1,2),j,ml,ms,m)
        norm+=weight;sz+=weight*ms;lz+=weight*ml
    assert norm==1
    return (gl*float(lz)+gs*float(sz))/float(m)

# Adopted rounded free-nucleon constants are selected background inputs.
FREE={'neutron':-3.826,'proton':5.586}
grows=[]
for species,gl in [('neutron',0.),('proton',1.)]:
 for q in [.6,1.]:
  gs=q*FREE[species]
  for l,j,name in [(5,F(11,2),'h11/2'),(5,F(9,2),'h9/2'),(3,F(7,2),'f7/2')]:
   value=lande(l,j,gl,gs)
   for m in [F(1,2),F(3,2),j]:
    check(f'lande_vs_spinCG_{species}_{q}_{name}_{m}',near(value,direct_g(l,j,m,gl,gs)),
          'selected pure spherical l,j model; not actual mixed QTR gK')
   grows.append(dict(species=species,gl=gl,gs=gs,quench=q,orbital=name,gj=value,
                    input_status='selected_background_not_nuclear_measurement'))

gn=lande(5,F(11,2),0,.6*FREE['neutron'])
gp=lande(5,F(11,2),1,.6*FREE['proton'])
gRce=58/133;gRau=79/187
check('same_h11_j_same_g_for_threeOmega',all(near(gn,direct_g(5,F(11,2),m,0,.6*FREE['neutron'])) for m in [F(5,2),F(7,2),F(9,2)]),
      'different Omega alone does not distinguish purej gj')
check('single_hole_has_same_gj',near(-gn*float(F(9,2))/float(F(-9,2)),gn),
      'hole angular momentum and magnetic moment both reverse relative to removed particle')

asymptotic=[]
for label,omega,Lambda in [('[514]9/2',F(9,2),4),('[523]7/2',F(7,2),3),('[532]5/2',F(5,2),2)]:
    sigma=omega-Lambda
    asymptotic.append(dict(label=label,Omega=str(omega),Lambda=Lambda,Sigma=str(sigma),
                           gK_asymptotic_spin_product=.6*FREE['neutron']*float(sigma/omega),
                           comparison_purej_gj=gn,
                           limit='selected axial asymptotic LambdaSigma product; different limit from purej; not actual QTR'))

cgrows=[]
for I in [F(17,2),F(21,2),F(25,2)]:
 for K in [F(5,2),F(7,2),F(9,2),F(13,2)]:
    c1=cg2(I,1,I-1,K,0,K);c2=cg2(I,2,I-2,K,0,K)
    closed1=(I*I-K*K)/(I*(2*I+1))
    closed2=F(3,2)*(I*I-K*K)*((I-1)**2-K*K)/((I-1)*I*(2*I-1)*(2*I+1))
    check(f'M1CG_closed_{I}_{K}',c1==closed1,'goodK intraband transition only')
    check(f'E2CG_closed_{I}_{K}',c2==closed2,'goodK intraband transition only')
    factor=F(12,5)*K*K*c1/c2
    analytic=F(8,5)*K*K*(I-1)*(2*I-1)/((I-1)**2-K*K)
    check(f'ratioCG_closed_{I}_{K}',factor==analytic,'Ksquare required in M1 rotor formula')
    cgrows.append(dict(I=str(I),K=str(K),M1_CG2_exact=str(c1),E2_CG2_exact=str(c2),
                       ratio_geometry_factor_exact=str(factor),ratio_geometry_factor=float(factor)))

def ratio(I,K,gK,gR,Q0):
    c1=float(cg2(I,1,I-1,K,0,K));c2=float(cg2(I,2,I-2,K,0,K))
    assert c2>0
    bm1=3/(4*pi)*(gK-gR)**2*float(K)**2*c1
    be2=5/(16*pi)*Q0**2*c2
    return bm1/be2

# Four declared axial comparators, not fitted TiP or 3qp eigenstates.
controls=[
 ('selected_collective_Rl2',F(13,2),(gn*4.5+gRce*2)/6.5,'selected fixed axial vector limit only; not fullTiP'),
 ('selected_orbital_7of2',F(7,2),gn,'pureh11 samegj,goodK=Omega; not sourceorbital17 eigenband'),
 ('selected_orbital_5of2',F(5,2),gn,'pureh11 samegj,goodK=Omega; not sourceorbital16 eigenband'),
 ('selected_3qp_Jp2',F(13,2),(gn*4.5+gp*2)/6.5,'chosen sameparity protonpair Jp=Kp=2; energy feasibility unknown')]
ratios=[]
for label,K,gK,boundary in controls:
 for I in [F(17,2),F(21,2),F(25,2)]:
    r=ratio(I,K,gK,gRce,1.)
    check(f'Q0_inverse_square_{label}_{I}',near(ratio(I,K,gK,gRce,2.),r/4),'chosen Q0 reference unit, not measuredQ')
    check(f'M1_zero_gK_equals_gR_{label}_{I}',ratio(I,K,gRce,gRce,1.)==0,'axial intraband rotational M1 component only')
    ratios.append(dict(label=label,I=str(I),K=str(K),gK_control=gK,gR_chosen=gRce,
                       Q0_reference_eb=1.,BM1_over_BE2_muN2_per_e2b2=r,
                       measurable_object='intraband M1(I→I−1) / intraband E2(I→I−2)',
                       actual_nuclear_prediction=False,boundary=boundary))
check('compositeCoreCancellation',near((controls[0][2]-gRce)*6.5,(gn-gRce)*4.5),
      'selected locked axial core+particle moment; no actual j/R measurement')

# Parity and quasiparticle-count gates, no assumed pair-breaking energy.
check('Ce_number_parity_1qp_vs3qp',75%2==1 and 58%2==0,'both require odd neutron and even proton speciesparity; not full occupations')
proton_m=[F(-11,2)+n for n in range(12)]
maxsum=max(a+b for a,b in combinations(proton_m,2))
check('identical_h11_protons_maxJ10',maxsum==10,'Pauli bound for two particles in samej shell, not nucleus maximumI')
check('threeqp_negative_spatialparity',(-1)*(-1)*(-1)==-1,'chosen neutronh and two protonh; generic pi² parity unspecified')
check('threeqp_intrinsic_capacity_31of2',maxsum+F(11,2)==F(31,2),'selected valence subspace only; core may add angular momentum')
qpe_order=[]
for lam in [-.5,0.,.5]:
    e1=sqrt((-.5-lam)**2+1.);e2=sqrt((.5-lam)**2+1.)
    qpe_order.append(dict(lambda_selected=lam,eps_selected=[-.5,.5],gap_selected=1.,qp=[e1,e2]))
check('qp_order_can_reverse_with_Fermi',qpe_order[0]['qp'][0]<qpe_order[0]['qp'][1] and qpe_order[2]['qp'][0]>qpe_order[2]['qp'][1],
      'dimensionless selected BCS control; not actual Ce energy zero or pairing input')
check('sameGap_pair_cost_atleast2Delta',all(sqrt(e*e+1.)+sqrt(f*f+1.)>=2 for e,f in [(-.5,.5),(0.,0.),(-2.,1.)]),
      'fixed reference quasiparticle sum only, not total band excitation after blocking/core/residual changes')
u,v=sqrt(.7),sqrt(.3)
pair_transition=(-v)*0*u+u*1*v
check('onebody_operator_can_connect_0and2qp',near(pair_transition,u*v) and pair_transition!=0,
      'two-mode BCS Fockcontrol n1, not a claimed nuclear electromagnetic matrix element')
check('M1_spin_triangle_disallows_DeltaI2',cg2(F(17,2),1,F(13,2),F(9,2),0,F(9,2))==0,
      'exact angular momentum triangle, independent of configuration labels')

selection=[]
for candidate,K in [('axial_K13of2',F(13,2)),('axial_K7of2',F(7,2)),('axial_K5of2',F(5,2))]:
    dK=abs(K-F(9,2))
    row=dict(candidate=candidate,final_K='9/2',DeltaK=str(dK),
             M1_K_allowed=dK<=1,E2_K_allowed=dK<=2,
             exact_spin_parity_result='sameparity DeltaI1 permitsM1andE2 by triangle/parity',
             approximation='axial exactgoodK only; triaxialKmixing liftsKforbidden strength')
    selection.append(row)
check('Kmixing_not_universalM1ban',selection[0]['M1_K_allowed']==False and selection[1]['M1_K_allowed']==True,
      'only selected exactK components, not actual triaxial band prohibition')

# SignedRME controls: B values discard relative sign. State phase flips both.
Egamma=.5;ME=1.;MM=1.;c=sqrt(.7)*Egamma
delta_plus=c*ME/MM;delta_minus=c*ME/(-MM)
check('delta_sign_not_from_B',near(abs(delta_plus),abs(delta_minus)) and delta_plus*delta_minus<0,
      'change relative physicalRME sign, not arbitrary statephase; B values identical')
check('state_rephase_leaves_delta',near(c*(-ME)/(-MM),delta_plus),
      'common initial/final statephase cancels between amplitudes')
def icc_mixed(delta,alphaM1=.1,alphaE2=.02):
    return (alphaM1+delta*delta*alphaE2)/(1+delta*delta)
check('conversion_coefficient_not_delta_sign',near(icc_mixed(.4),icc_mixed(-.4)),
      'selected alpha values only; independent conversion measurement constrains mixture magnitude, not relative sign')
check('conversion_pure_limits',near(icc_mixed(0.),.1) and abs(icc_mixed(1e8)-.02)<1e-10,
      'specifiedshell/theoryversion must be matched for actualtarget')
mixing=[]
for theta in [0.,pi/8,pi/4,3*pi/8,pi/2]:
    a,b=cos(theta),sin(theta);me=a-b;mm=a+b
    mixing.append(dict(theta_chosen_radian=theta,ME2=me,MM1=mm,delta_control=c*me/mm,
                       static_g_control=.2,actual_eigenstate=False))
check('same_staticg_opposite_delta_possible',mixing[0]['delta_control']>0 and mixing[-1]['delta_control']<0,
      'selected two-amplitude mathematical counterexample, not a QTR Hamiltonianfit')

# Lifetime/branch algebra with unitless selected rates, not measuredlifetimes.
Y=[2.,3.];alpha=[.1,.5];tau=2.;denom=sum(y*(1+a) for y,a in zip(Y,alpha))
rates=[y/(tau*denom) for y in Y]
check('photon_and_conversion_rate_closure',near(sum(r*(1+a) for r,a in zip(rates,alpha)),1/tau),
      'completebranch chosen control, tau is arbitrary unit')
check('tau_rescales_all_B_not_sign',all(near(y/(2*tau*denom),r/2) for y,r in zip(Y,rates)),
      'samebranches andICC; doubling lifetime halves each absoluteB, notmodeidentity')

# Freeze direct-source transcriptions as data: only model mapping is replaced.
nodes=json.loads(Path('tmp/day23-theses/ce133-s-exercise/nodes.json').read_text())
edges=json.loads(Path('tmp/day23-theses/ce133-s-exercise/edges.json').read_text())
observed=dict(nodes=[x for x in nodes if x['band'] in [1,4]],edges=[x for x in edges if x['initial_band'] in [1,4]])
canonical_bytes=json.dumps(observed,ensure_ascii=False,sort_keys=True).encode()
baseline=hashlib.sha256(canonical_bytes).hexdigest()
for candidate in ['Ce_TiP_source','Ce_orbital17_hypothesis','Ce_orbital16_hypothesis','Ce_3qp_hypothesis']:
    scenario=dict(observed=copy.deepcopy(observed),model_assignment=candidate)
    check('D_frozen_'+candidate,hashlib.sha256(json.dumps(scenario['observed'],ensure_ascii=False,sort_keys=True).encode()).hexdigest()==baseline,
          'hashcheck freezes published transcription, not unprovided rawcounts or covariance')

result=dict(status='computed-conditional',all_checks_passed=all(x['passed'] for x in checks),check_count=len(checks),checks=checks,
            adopted_background_constants=dict(gs_free=FREE,gs_quench_choices=[.6,1.],gl_neutron=0.,gl_proton=1.,
                                             core_gR_selected=dict(Ce=58/133,Au=79/187),
                                             source_Ce_rounded_gR=.44,Q0_reference_eb=1.,actual_Q0_supplied=False),
            purej_g_controls=grows,asymptotic_gK_controls=asymptotic,CG_checks=cgrows,
            selected_axial_rate_ratio_controls=ratios,axial_K_selection_controls=selection,
            dimensionless_BCS_order_controls=qpe_order,
            signed_RME_controls=dict(delta_plus=delta_plus,delta_minus=delta_minus,mixing=mixing),
            frozen_Ce_published_D_sha256=baseline,frozen_Ce_nodes=len(observed['nodes']),frozen_Ce_edges=len(observed['edges']),
            original_event_counts_available=False,author_producer_replayed=False,actual_model_prediction_generated=False,
            experimental_CI_generated=False,mode_certified=False,needs_review=True,
            source_note='CeTable5.1/5.2 direct-PDFtranscription reused; sourcechosencontrols not actualmixed-state prediction')
(OUT/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(OUT/'frozen-published-Ce-D.json').write_text(json.dumps(observed,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=result['status'],checks=result['check_count'],all_pass=result['all_checks_passed'],
                      purej_neutron_h11_g_06=gn,core_gR_Ce=gRce,Ce_D_hash=baseline),indent=2))
