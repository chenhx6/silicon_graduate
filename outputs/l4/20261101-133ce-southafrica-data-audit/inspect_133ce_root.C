#include <TFile.h>
#include <TH2.h>
#include <TKey.h>
#include <TObject.h>
#include <iostream>

void inspect_one(const char* path) {
  TFile file(path, "READ");
  std::cout << "FILE " << path << " zombie=" << file.IsZombie() << "\n";
  TIter iterator(file.GetListOfKeys());
  TKey* key;
  while ((key = (TKey*)iterator())) {
    TObject* object = key->ReadObj();
    std::cout << "  " << object->GetName() << " class=" << object->ClassName();
    TH2* histogram = dynamic_cast<TH2*>(object);
    if (histogram) {
      std::cout << " nx=" << histogram->GetNbinsX()
                << " ny=" << histogram->GetNbinsY()
                << " entries=" << histogram->GetEntries()
                << " xrange=[" << histogram->GetXaxis()->GetXmin()
                << "," << histogram->GetXaxis()->GetXmax() << "]"
                << " yrange=[" << histogram->GetYaxis()->GetXmin()
                << "," << histogram->GetYaxis()->GetXmax() << "]";
    }
    std::cout << "\n";
    delete object;
  }
}

void inspect_133ce_root() {
  inspect_one("raw/data/SouthAfrica/133Ce_iThemba2019/mat/root/g45allmatprompt.root");
  inspect_one("raw/data/SouthAfrica/133Ce_iThemba2019/mat/root/g90allmatprompt.root");
  inspect_one("raw/data/SouthAfrica/133Ce_iThemba2019/mat/root/gg.root");
  inspect_one("raw/data/SouthAfrica/133Ce_iThemba2019/mat/root/hgg.root");
  inspect_one("raw/data/SouthAfrica/133Ce_iThemba2019/mat/root/vgg.root");
}
