// Client of the frozen SimDSAM stopping-table reader, with declared table mode.
#include "simdsam-compat-prelude.hh"
#define decay SimDSAMDecay
#define main simdsam_original_main_unused
#include "/workspace/wiki/tmp/day17-kirsebom2016/simdsam-source/source/sim_dsam.cpp"
#undef main
#undef decay
#include <iomanip>
int main(int argc,char** argv) {
  if(argc!=2) return 2;
  gROOT->SetBatch(kTRUE);
  globals settings("../InputCards/INPUTDEF.CARD");
  stoppingPowerSource=argv[1];
  if(stoppingPowerSource!="PASS" && stoppingPowerSource!="GEANT") return 2;
  stoppingDataTables tables(12);
  double EA=0;
  std::cout<<std::setprecision(17);
  while(std::cin>>EA) {
    double linear=tables.GetStopping(EA*1000,1);
    double mass_stopping=linear/(19.30*0.1);
    if(!(std::isfinite(linear) && linear>0)) return 3;
    std::cout<<"TABLE_VALUE,"<<stoppingPowerSource<<','<<EA<<','<<linear<<','<<mass_stopping<<'\n';
  }
}
