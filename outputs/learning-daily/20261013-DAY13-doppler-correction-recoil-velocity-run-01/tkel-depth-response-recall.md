# Day13：末速度的深度信息与TKEL/prior closure

2026-10-14T10:03:15.774550+08:00

已读CM21final的100层/随机depth/TKELfold/geometry解释，故primed设计。新source未开。

- 问题：最终速度能否独立证明初速度/反应depthprior？应把已测终分布、假设反应kinematics、depth与stopping分开。
- 最小系统：generic mass20u、collinear1Dfoil4um、Ebeam100MeV、selectedchannel loss4MeV、constantSbeam=Sprod2.5MeV/um。不是18O+Ta45degreegeometry或真实两体反应。
- Energybookkeeping Ti(x)=Ebeam-Sbeam*x-loss，Tf=Ebeam-loss-Sprod*L+(Sprod-Sbeam)*x。EqualS的特殊极限Tf与x无关；可用uniform/front/backprior构造相同末速度而不同初速度和gammahistory。
- Photon过程用relativisticproperclock：eta=acosh(1+T/M)，deta/dproper=-S*c/M，在出foil后速度constant。核其与独立数值integral一致。
- 设计true tau80fs、三prior、selfGaussianresponse和pointangles，比较wronguniform depth下tau/E fits；不从nonzeroKL断言真实bias。
- 反证：实际beam/producteffectiveS不同、几何倾角、reaction/TKEL、energy/angle-straggling或independententry测量提供depth信息，此极限竞争者可排除。CM21finaltarget tilted45degree/VAMOS angularacceptance要按实际source写，不能用toy反写。
- 验证：energywork/constantexit、properclockintegral、prior/emissionnormalization、quad/MC/zero-loss/long-tau、Lorentzinverse与已知uniform truth。Sourcef0 actualproductioncode/negativeTKEL residualhandling仍缺。
