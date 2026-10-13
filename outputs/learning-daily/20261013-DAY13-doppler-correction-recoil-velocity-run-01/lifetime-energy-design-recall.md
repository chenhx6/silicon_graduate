# Day13：τ/Eγ辨识与shape信息计算前回忆

2026-10-14T05:29:35.492960+08:00

CO19 plannedtwo-parameterfit已读后的primed设计回忆；无actualsourcefit。

- 已知exitβ与自设targetslowingβ(t)、properτ控制early/late mixture；unknownE0可吸收部分meanoffset，不能只看三centroid选τ。
- Fullnormalizedshape可能保留tail/mixture信息；若stopping/response/feeding/calibration未知，statisticaldiscrimination不变成实验结论。
- Modelpredictionsτ200/320fs只能作为designhypotheses；E0=2396、βin.105/exit.10、properduration.13ps、σ1.5keV和threepointangles是selfchosen，不复制originalpipeline。
- 以conditionalisotropic angularJacobian与有限properclockintegral构造profile；比较centroid-only E0optim与fullshape KLoptim。2N KL只是exact-modelexpectedmetric，不是sourceχ²/CL或NNNforce证据。
- 核验normalizedprofile/analyticmoments/MC、timequadrature、largeτ与no-loss限制，保留input/readinessboundary。
