# Day13：rigidity velocity、integer PID与TOF covariance回忆

2026-10-14T03:06:53.392369+08:00

AS21直接Eq1/7.4已读后的primed计算回忆：

- βγ=Bρ q/(3.107A)（mass-number模型与sourceconstant）；δβ/β=(1−β²)δBρ/Bρ仅在A/q固定时成立。
- 很小的within-class σ不能排wronginteger A或q的systematicmode；实际PIDconfusion、knownreactionchannel及independentline约束要另外提供。
- inferred flight T=L/(βc)的δT/T=δL/L−δβ/β，path/rigidity covariance不可丢；source.2% resolution未标σ/FWHM，toy若取σ.002须明说自己的假设。
- LightTOF由predictedheavyflight与measuredMUGAST-VAMOS时间差相减，再加入clock/walk/calibration covariance；改善分辨率不等new independentclock。
- 自设A20/q8/β.126、L7m；其它Ochargeq7及mass19/21仅测试label模式，不给概率，不重建actual19O/d/p dataset。
