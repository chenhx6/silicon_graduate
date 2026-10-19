// Thin entry point for the frozen original event main; no physics modification.
#include "simdsam-compat-prelude.hh"
#define decay SimDSAMDecay
#define main simdsam_original_main_unused
#include "/workspace/wiki/tmp/day17-kirsebom2016/simdsam-source/source/sim_dsam.cpp"
#undef main
#undef decay
int main(int argc,char** argv) {
  gROOT->SetBatch(kTRUE);
  std::cout<<"MODEL_RNG,"<<gRandom->ClassName()<<','<<gRandom->GetSeed()<<'\n';
  int result=simdsam_original_main_unused(argc,argv);
  std::cout<<"MODEL_BOOKKEEP,"<<h2d->GetEntries()<<','<<h_Ealpha->GetEntries()<<','
           <<h_Egamma->GetEntries()<<'\n';
  return result;
}
