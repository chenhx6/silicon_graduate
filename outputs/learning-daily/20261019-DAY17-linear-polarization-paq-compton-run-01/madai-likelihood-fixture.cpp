#include "Model.h"
#include "UniformDistribution.h"
#include <cmath>
#include <iomanip>
#include <iostream>
#include <vector>

class Fixture : public madai::Model {
public:
  double mean, variance; mutable int covariance_calls;
  Fixture(double m,double v,bool override_name=false):mean(m),variance(v),covariance_calls(0) {
    AddScalarOutputName(override_name?"log_likelihood":"observable");
    SetObservedScalarValues(std::vector<double>(1,0.));
    SetObservedScalarCovariance(std::vector<double>(1,1.));
    m_StateFlag=READY;
  }
  ErrorType GetScalarOutputs(const std::vector<double>&,std::vector<double>& out) const override {
    out.assign(1,mean);return NO_ERROR;
  }
  ErrorType GetScalarOutputsAndCovariance(const std::vector<double>& x,std::vector<double>& out,std::vector<double>& cov) const override {
    ++covariance_calls;cov.assign(1,variance);return GetScalarOutputs(x,out);
  }
  void AddUniformPrior(){madai::UniformDistribution u;u.SetMinimum(-1.);u.SetMaximum(1.);AddParameter("declared",u);}
};
void run(const char*name,double mean,double variance,bool use,bool custom=false,bool prior=false,double x=0.){
 Fixture model(mean,variance,custom);model.SetUseModelCovarianceToCalulateLogLikelihood(use);if(prior)model.AddUniformPrior();
 std::vector<double> input;if(prior)input.push_back(x);std::vector<double> out;double value;
 int code=model.GetScalarOutputsAndLogLikelihood(input,out,value);
 double alternative;std::vector<double> vg,eg;int second=model.GetScalarOutputsAndLogLikelihoodAndLikelihoodErrorGradient(input,out,alternative,vg,eg);
 std::cout<<name<<","<<code<<","<<value<<","<<model.covariance_calls<<","<<second<<","<<alternative<<"\n";
}
int main(){
 std::cout<<std::setprecision(17);
 run("default_modelcov_off",1.,3.,false);
 run("zerores_totalvar1",0.,0.,true);run("zerores_totalvar4",0.,3.,true);
 run("res1_totalvar1",1.,0.,true);run("res1_totalvar4",1.,3.,true);run("res2_totalvar4",2.,3.,true);
 run("custom_log_likelihood",-.125-.5*std::log(4.),3.,true,true);
 run("finite_uniform_prior",1.,0.,true,false,true,0.);
 run("out_of_prior",1.,0.,true,false,true,2.);
 run("invalid_negative_totalcov",1.,-2.,true);
 return 0;
}
