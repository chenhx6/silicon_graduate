#include "src/functions/Extraction_SRIM_stopping_powers.h"
#include "src/functions/kinematics.h"
#include <iomanip>
int LoadSRIMFile(std::string,Double_t[],Double_t[],Double_t[],int);
int main(int argc,char**argv){
 std::cout<<std::setprecision(17);
 if(argc>1 && std::string(argv[1])=="loader"){
  Double_t e[5000]={0},se[5000]={0},sn[5000]={0};int n=-123;
  int status=LoadSRIMFile("src/functions/SP_SRIM/beam_in_matter.dat",e,se,sn,n);
  std::cout<<"{\"mode\":\"loader\",\"status\":"<<status<<",\"caller_n\":"<<n<<",\"first_energy\":"<<e[0]<<",\"first_electronic\":"<<se[0]<<",\"second_energy\":"<<e[1]<<"}\n";return 0;
 }
 Double_t masses[4]={24*931.5-13.933,3*931.5+14.931,23*931.5-5.473,4*931.5+2.425};
 Double_t az[2][4]={{24,3,23,4},{12,2,12,2}};
 Double_t ejectile[2]={4,30},recoil[2]={0,0},pol[3]={0,0,0};double beta=.123456789;
 double status=VAMOS_kinematics(ejectile,recoil,beta,.86,pol,110.826,masses,az);
 std::cout<<"{\"mode\":\"VAMOS scalar output\",\"status\":"<<status<<",\"caller_beta\":"<<beta<<",\"recoil_theta\":"<<recoil[0]<<",\"recoil_phi\":"<<recoil[1]<<"}\n";return 0;
}
