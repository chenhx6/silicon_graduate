# 60Co模型角关联控制图

图a：原生角关联开启／关闭两组各100000个完整模拟衰变history。按事前冻结能窗要求唯一1173与1332目标光子对；分别保留99840/99845对，排除160/155个不完整目标对。100个cosθ bins合并为20个，每bin计数除以条件N与均匀bin宽，使isotropic mean为1。误差棒为条件multinomial counting SE；曲线为原level文件E2/M3δnative−.0025的point/rest-frame理论，不是拟合曲线。

图b：同样两个mode，各以全部100000history为分母。native rawcore的两不同晶体能窗1168–1178/1328–1337keV、最高deposit IP和冻结producer矩阵得到507/549个selected detector pairs。10个角bin均有iso支撑，ratio误差为独立MC控制下固定N counts-Cov的一阶delta-method SE。没有source-truthFEP门、能量smearing、addback或对点W的直接拟合；这条有限几何/门响应不提供实验Q。

两面板共用固定Geant4/输入；它们是模型控制，不是两次独立实验，也没有多随机种子系统学或实验系统误差预算。代码、source-data CSV、SVG/PDF/600dpi PNG及alignment/font/collision/visual QA均在本run目录；详canonical co60-gate-role-response-benchmark及sourceUG24。本图为研究笔记，不主张期刊投稿格式已获审核。
