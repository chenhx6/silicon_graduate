# 60Co门角色与角关联源控制前回忆

同原Day16/session，原2026-10-19 15:00上海截止，formal16一次/partial17，goalactive。primed：已读R21 continuum门、L25 calibration、GRUT60Co sorting主线与G411 sourceMC及mathematical angular/Stokes核；尚未打开G411 co60 example本批正文/宏。

回忆：60Co的1173/1332级联是4→2→0的E2序列；实际门方向/有限角、效率、背景、timewindow及selection会改变目标样本。一个gamma能谱合格不代表gatedcorrelation或Q已校准；按gamma能量互换reference/target也会改变polarimeter角色与geometry。真实decayhistory不等DAQ触发event，需核macro/时间来源。

问题：公开G411 co60例究竟用原生nuclear angular correlations还是customPOL？是否实际提供source-level两γ角相关/关联开关和isotropic control、gate/count单位、有限角response？不因命令叫AngularCorrelations就预填运行正确，也不打开偏振EM已知失败配置。只在actualinputs、nativeABI/record/response/Cov完整时开展bounded无偏振angle/gate模型。

设计：先完整读example主线，再决定是否只做readiness或实际simulation。若允许actualrun，冻结source/geometry/开关/seed/事件分母、1173与1332双角色identity、门角和efficiency/归一/误差；用原无角关联control反证，不把两种simulation当独立实验。不调参数追原paperQ。
