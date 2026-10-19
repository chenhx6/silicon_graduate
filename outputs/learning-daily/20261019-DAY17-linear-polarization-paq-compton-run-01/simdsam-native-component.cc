// Separate client of frozen original functions. Original event-loop main is unused.
#include "simdsam-compat-prelude.hh"
#define decay SimDSAMDecay
#define main simdsam_original_main_unused
#include "/workspace/wiki/tmp/day17-kirsebom2016/simdsam-source/source/sim_dsam.cpp"
#undef main
#undef decay
#include <iomanip>
#include <cmath>

void reset_particle(particle& p,double energy,double angle_deg=0) {
  p.elab=energy;
  double norm=std::sqrt(energy*(energy+2*p.mass));
  double mom[3]={norm*std::sin(angle_deg*pi/180),0,norm*std::cos(angle_deg*pi/180)};
  double pos[3]={0,0,0};
  p.set_plab(mom);p.set_position(pos);
}

int main() {
  gROOT->SetBatch(kTRUE);
  globals settings("../InputCards/INPUTDEF.CARD");
  doHe3Implantation=false;
  doEnergyStraggling=false;doAngularStraggling=false;
  thicknessCarbon=0;gaussianWidthCarbon=0;fwhmISACII=0;
  addSiResolution=false;displacementBeamSpot=0;
  massTable masses;
  particle beam(12,24,masses.GetMass(12,24),infinity);
  particle target(2,3,masses.GetMass(2,3),infinity);
  particle compound=beam.fuseWith(target); // includes original unused-Z14 table warnings.
  particle alpha(2,4,masses.GetMass(2,4),infinity);
  particle recoil(12,23,masses.GetMass(12,23),1e-15);
  reset_particle(beam,75000);
  alpha.suppressPropagation=true;recoil.suppressPropagation=true;
  recoil.excitation=2908;
  particle* daughter[2]={&alpha,&recoil};
  SimDSAMDecay one(2,daughter,0);
  double theta[1]={0.1},phi[1]={0.2};
  one.ftheta=theta;one.fphi=phi;
  sequence seq(1,&one,beam,target,compound);
  double sum=0,sum2=0;
  const int N=20000;
  for(int i=0;i<N;++i) {
    seq.simulate_kinematics(0);
    double radius=std::hypot(alpha.get_x(),alpha.get_y())/radiusBeamSpot;
    if(!std::isfinite(radius) || radius<0 || radius>1+1e-12) return 3;
    sum+=radius;sum2+=radius*radius;
  }
  std::cout<<std::setprecision(17)<<"BEAM_RADIAL,"<<N<<','<<radiusBeamSpot<<','<<sum/N<<','<<sum2/N<<'\n';
  recoil.excitation=0;
  stoppingDataTables stop_tables(12);
  double number_density_Au=19.30/(196.966569*1.661e-24);
  for(double ea:{1000.0,1700.0,2000.0}) {
    double pure=stop_tables.GetStopping(ea,1);
    double he=stop_tables.GetStopping(ea,0);
    double zero=stop_tables.GetStopping(ea,1,0,0,0.75);
    double mix=stop_tables.GetStopping(ea,1,0,1.05*number_density_Au,0.75);
    std::cout<<std::setprecision(17)<<"MIXTURE,"<<ea<<','<<pure<<','<<he<<','<<zero<<','<<mix<<'\n';
  }
  for(double beta:{0.059,0.082}) {
    double gamma=1/std::sqrt(1-beta*beta);
    for(double fs:{0.2,0.5}) {
      reset_particle(recoil,recoil.mass*(gamma-1));
      double initial=recoil.elab,x=0;
      recoil.energyLoss(fs*1e-15,0,1,x);
      std::cout<<std::setprecision(17)<<"CLOCK_CONTROL,"<<beta<<','<<fs<<','<<initial<<','
       <<recoil.elab<<','<<recoil.get_z()<<','<<x<<','<<recoil.get_vlabnorm()<<'\n';
    }
  }
  reset_particle(alpha,32000,1.0);
  alpha.propagateToDetector();
  alpha.detection();
  std::cout<<std::setprecision(17)<<"ALPHA_DETECTION,"<<alpha.isDetected()<<','
   <<alpha.getMeasuredEnergy()<<','<<alpha.elab<<','<<alpha.getObservedAngle()<<'\n';
  reset_particle(alpha,32000,1.0);
  alpha.propagateToDetector();
  double de1=0,de2=0,de3=0;
  alpha.SiDeadLayers(de1,de2,de3);
  std::cout<<std::setprecision(17)<<"ALPHA_LAYERS,"<<de1<<','<<de2<<','<<de3<<','
   <<alpha.elab<<','<<(32000-de1-de2-de3)<<'\n';
  return 0;
}
