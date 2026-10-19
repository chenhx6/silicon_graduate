// Conditional SDK component query; no events, experimental fit, or paper producer.
#include "G4RunManager.hh"
#include "G4VUserDetectorConstruction.hh"
#include "G4VModularPhysicsList.hh"
#include "G4EmStandardPhysics.hh"
#include "G4EmStandardPhysics_option4.hh"
#include "G4EmParameters.hh"
#include "G4NistManager.hh"
#include "G4Box.hh"
#include "G4LogicalVolume.hh"
#include "G4PVPlacement.hh"
#include "G4IonTable.hh"
#include "G4GenericIon.hh"
#include "G4EmCalculator.hh"
#include "G4ProcessManager.hh"
#include "G4VEnergyLossProcess.hh"
#include "G4VEmModel.hh"
#include "G4SystemOfUnits.hh"
#include "G4Version.hh"
#include <cfloat>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <string>

class Geometry final : public G4VUserDetectorConstruction {
public:
  G4VPhysicalVolume* Construct() override {
    auto n = G4NistManager::Instance();
    auto wl = new G4LogicalVolume(new G4Box("world", 1*m, 1*m, 1*m),
                                 n->FindOrBuildMaterial("G4_Galactic"), "world");
    auto wp = new G4PVPlacement(nullptr, {}, wl, "world", nullptr, false, 0);
    auto au = new G4LogicalVolume(new G4Box("Au", 1*cm, 1*cm, 1*cm),
                                 n->FindOrBuildMaterial("G4_Au"), "Au");
    auto ta = new G4LogicalVolume(new G4Box("Ta", 1*cm, 1*cm, 1*cm),
                                 n->FindOrBuildMaterial("G4_Ta"), "Ta");
    new G4PVPlacement(nullptr, {0, 0, -5*cm}, au, "Au", wl, false, 0);
    new G4PVPlacement(nullptr, {0, 0, 5*cm}, ta, "Ta", wl, false, 1);
    return wp;
  }
};

class Physics final : public G4VModularPhysicsList {
public:
  explicit Physics(const std::string& mode) {
    SetVerboseLevel(0);
    defaultCutValue = 1*um;
    if (mode == "standard") RegisterPhysics(new G4EmStandardPhysics(0));
    else if (mode == "option4") RegisterPhysics(new G4EmStandardPhysics_option4(0));
    else if (mode == "external") RegisterPhysics(new G4EmStandardPhysics_option4(0, "externalDEDX"));
    else throw std::runtime_error("unknown mode");
  }
  void SetCuts() override { SetCutsWithDefault(); }
};

int main(int argc, char** argv) {
  if (argc != 2) return 2;
  std::string mode = argv[1];
  auto rm = new G4RunManager();
  rm->SetVerboseLevel(0);
  rm->SetUserInitialization(new Geometry());
  rm->SetUserInitialization(new Physics(mode));
  rm->Initialize();
  // Build model/physics tables before querying the calculator; no event loop.
  rm->RunInitialization();
  auto generic = G4GenericIon::Definition();
  auto pv = generic->GetProcessManager()->GetProcessList();
  for (std::size_t i = 0; i < pv->size(); ++i) {
    auto loss = dynamic_cast<G4VEnergyLossProcess*>((*pv)[i]);
    if (loss && loss->EmModel(0)) {
      std::cout << "MODEL," << mode << ',' << loss->GetProcessName() << ','
                << loss->EmModel(0)->GetName() << '\n';
    }
  }
  std::cout << "CONFIG," << mode << ',' << G4VERSION_NUMBER << ','
            << G4EmParameters::Instance()->UseICRU90Data() << ','
            << G4EmParameters::Instance()->MaxNIELEnergy()/MeV << '\n';
  G4EmCalculator calc;
  calc.SetVerbose(0);
  int row, z, a;
  std::string matname;
  double energy_per_A;
  std::cout << std::setprecision(17);
  while (std::cin >> row >> z >> a >> matname >> energy_per_A) {
    auto ion = G4IonTable::GetIonTable()->GetIon(z, a, 0.0);
    auto mat = G4NistManager::Instance()->FindOrBuildMaterial(matname);
    double energy = a * energy_per_A * MeV; // declared database E/A convention.
    double unit = MeV*cm2/mg;
    double values[6];
    for (int q=0; q<6; ++q) {
      double cut = q<3 ? DBL_MAX : 1*keV;
      values[q] = calc.ComputeElectronicDEDX(energy, ion, mat, cut) / mat->GetDensity() / unit;
      if (!(std::isfinite(values[q]) && values[q] >= 0)) return 3;
    }
    if (values[2] <= 0 || std::abs(values[1]-values[2]) > 1e-10*values[2] ||
        std::abs(values[4]-values[5]) > 1e-10*values[2] ||
        values[5] > values[2]*(1+1e-10)) return 4;
    std::cout << "STOPPING," << row << ',' << mode << ',' << z << ',' << a << ','
              << matname << ',' << energy_per_A << ',' << energy/MeV << ','
              << ion->GetPDGMass()/MeV << ',' << mat->GetDensity()/(g/cm3) << ','
              << values[0] << ',' << values[1] << ',' << values[2] << ','
              << values[3] << ',' << values[4] << ',' << values[5] << '\n';
  }
  rm->RunTermination();
  delete rm;
  return 0;
}
