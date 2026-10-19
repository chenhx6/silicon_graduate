// Native first-two-step control with declared artificial termination; no DSAM fit.
#include "G4RunManager.hh"
#include "G4VUserDetectorConstruction.hh"
#include "G4VModularPhysicsList.hh"
#include "G4VUserPrimaryGeneratorAction.hh"
#include "G4UserSteppingAction.hh"
#include "G4EmStandardPhysics_option4.hh"
#include "G4EmParameters.hh"
#include "G4NistManager.hh"
#include "G4Box.hh"
#include "G4LogicalVolume.hh"
#include "G4PVPlacement.hh"
#include "G4UserLimits.hh"
#include "G4StepLimiter.hh"
#include "G4GenericIon.hh"
#include "G4ProcessManager.hh"
#include "G4ParticleGun.hh"
#include "G4IonTable.hh"
#include "G4Step.hh"
#include "G4Event.hh"
#include "G4VProcess.hh"
#include "G4SystemOfUnits.hh"
#include "Randomize.hh"
#include <iomanip>
#include <iostream>
#include <string>

class Detector final : public G4VUserDetectorConstruction {
  double limit;
public:
  explicit Detector(double value) : limit(value) {}
  G4VPhysicalVolume* Construct() override {
    auto material = G4NistManager::Instance()->FindOrBuildMaterial("G4_Ta");
    auto logical = new G4LogicalVolume(new G4Box("world",1*cm,1*cm,1*cm),material,"world");
    logical->SetUserLimits(new G4UserLimits(limit));
    return new G4PVPlacement(nullptr,{},logical,"world",nullptr,false,0);
  }
};

class Physics final : public G4VModularPhysicsList {
public:
  explicit Physics(const std::string& mode) {
    defaultCutValue=1*um;
    SetVerboseLevel(0);
    RegisterPhysics(new G4EmStandardPhysics_option4(0,mode=="external" ? "externalDEDX" : ""));
    G4EmParameters::Instance()->SetLossFluctuations(false);
    G4EmParameters::Instance()->SetMaxNIELEnergy(0.0);
  }
  void ConstructProcess() override {
    G4VModularPhysicsList::ConstructProcess();
    G4GenericIon::Definition()->GetProcessManager()->AddDiscreteProcess(new G4StepLimiter());
  }
  void SetCuts() override { SetCutsWithDefault(); }
};

class Primary final : public G4VUserPrimaryGeneratorAction {
  G4ParticleGun gun{1};
public:
  void GeneratePrimaries(G4Event* event) override {
    gun.SetParticleDefinition(G4IonTable::GetIonTable()->GetIon(8,15,0.0));
    gun.SetParticleEnergy(0.021354261092276033*MeV);
    gun.SetParticlePosition({0,0,0});
    gun.SetParticleMomentumDirection({0,0,1});
    gun.GeneratePrimaryVertex(event);
  }
};

class Steps final : public G4UserSteppingAction {
public:
  void UserSteppingAction(const G4Step* step) override {
    auto track=step->GetTrack();
    if(track->GetParentID()!=0) return;
    int event=G4RunManager::GetRunManager()->GetCurrentEvent()->GetEventID();
    auto pre=step->GetPreStepPoint();
    auto post=step->GetPostStepPoint();
    std::cout<<std::setprecision(17)<<"NATIVE_STEP,"<<event<<','<<track->GetCurrentStepNumber()<<','
      <<pre->GetKineticEnergy()/MeV<<','<<post->GetKineticEnergy()/MeV<<','
      <<step->GetStepLength()/nm<<','<<step->GetTotalEnergyDeposit()/MeV<<','
      <<pre->GetCharge()/eplus<<','<<post->GetCharge()/eplus<<','
      <<post->GetProcessDefinedStep()->GetProcessName()<<'\n';
    if(track->GetCurrentStepNumber()>=2) track->SetTrackStatus(fStopAndKill);
  }
};

int main(int argc,char** argv) {
  if(argc!=3) return 2;
  std::string mode=argv[1];
  if(mode!="option4" && mode!="external") return 2;
  double limit=std::stod(argv[2])*nm;
  G4Random::setTheSeed(13579);
  auto rm=new G4RunManager();
  rm->SetVerboseLevel(0);
  rm->SetUserInitialization(new Detector(limit));
  rm->SetUserInitialization(new Physics(mode));
  rm->SetUserAction(new Primary());
  rm->SetUserAction(new Steps());
  rm->Initialize();
  std::cout<<"CONTROL,"<<mode<<','<<limit/nm<<",seed13579,nuclearoff,fluctuationoff,killafter2\n";
  rm->BeamOn(2);
  delete rm;
  return 0;
}
