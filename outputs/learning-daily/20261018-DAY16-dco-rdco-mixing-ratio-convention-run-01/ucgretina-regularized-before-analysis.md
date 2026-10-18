# 禁戒CG比值之后的有界问题

同Day16/partial17，原截止19日15:00上海不变。本run已实际复算literalpublicITDecay并发现mixedk0/pureM1高rank的NaN，MorsepureE2控制过；首轮δ坐标错误与v2改正保留。下一段为该当前问题的数学设计与局限，不修写原publiccode、不把模型当实验、不延伸Day18。

待推导：把(CGplus/CGminus)*F先消掉F内CGminus。G4F原式由Wigner3j/6j给，期望有限形式为同一phase和sqrt(2Ji+1)(2L+1)(2Lp+1)乘6j与CGplus；须逐符号推导，不能靠遇0返回0或一并忽略mixedinterference。

验证目标：固定spin/multipole/phase与PSDrho，对原定义有限处一致，对mixedk0/纯高rank finite且同1→1purelimit连续；用独立photontrace检验全Stokes/强度与|S|≤1。增加一般κ/coherence/rotation必须先给明确tensor convention与positive density来源；若general失败保留，不自动改axes或sign凑合。坐标poles的规范轴与true intensityzero要分开；noPSD输入要fail而非clip。

原Geant4v10.7.4函数和实际11.4.2helper可比较，但不认证论文exactproducer；全geometry/event/postprocess/Cov仍缺，不能由内核修复推原Q/beamtime/实验δ。源数据/上游源码在repo tmp保持原hash，另名derivedimplementation。
