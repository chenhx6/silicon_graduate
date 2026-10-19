// Actual installed SDK ground-state mass inputs, not a new mass evaluation.
#include "G4NucleiProperties.hh"
#include "G4SystemOfUnits.hh"
#include "G4Version.hh"
#include <iostream>
#include <iomanip>
int main() {
  std::cout<<std::setprecision(17)<<"SDK,"<<G4VERSION_NUMBER<<'\n';
  for (auto p : {std::pair<int,int>{32,16}, {3,2}, {4,2}, {31,16}})
    std::cout<<"MASS,"<<p.first<<','<<p.second<<','
      <<G4NucleiProperties::GetNuclearMass(p.first,p.second)/MeV<<'\n';
}
