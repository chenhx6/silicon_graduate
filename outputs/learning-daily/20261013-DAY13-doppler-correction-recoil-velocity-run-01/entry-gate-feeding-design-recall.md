# Day13：Ex entry gate、feeding 与 line-shape设计练习

2026-10-14T07:57:07.257095+08:00

已读ZA23/CI20/CM21，为source-inspired设计前回忆，非blind考试或实验再拟合。

- 必须把upperstate branching与目标sample f拆开：population、Ex acceptance/迁移、efficiency决定f。
- 连续模型：直接properwaiting Exp(τ2)，feeding为两个指数等待和；概率守恒可由closed survival确认。单指数fitτ不一定等meanwaiting，更不能以70+54f判真实150fs来源。
- 自设入口Ex均值4.071/5.228MeV、branch.28和time70/54fs仅取source-scale，不使用任何真实eventcounts/Exresolution/stopping曲线。
- 选择/transport toy：ExGaussian误差、有限gate；β0=.126→βexit=.08在自设T=.4ps内线性下降，随后constant。精确forward使用emissionβ、correctedoutput使用exitβ；energyresponse假设Gaussianσ2keV。没有真实goldstopping/Geantresponse/侧馈入packet。
- 预期诊断：gateleakage与populationratios决定f；全形wrong-no-feeding模型τ偏移与残余KL分开，可profileE。
- 验证：概率normalization、两个指数相等极限、f0、零velocityloss、independentMonteCarlo time/energy/moments、quadratureconvergence、properclock单位。全部fit只是syntheticexpectedKLdesign，非Neymanχ²/实验CL或realτdiscrepancy裁决。
