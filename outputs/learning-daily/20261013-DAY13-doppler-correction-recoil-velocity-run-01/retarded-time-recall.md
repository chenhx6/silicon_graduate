# Day13：retarded arrival time与energy回忆

2026-10-14T02:32:08.845824+08:00

前序proper decay/vertex、AA09 flight和SY14 TOF后的一次计算前回忆。

- proper waiting time t对应lab emission time γt，但detector arrival还含随发射点变化的photon path/c。subtract prompt R0/c后arrival a(t)=γt+[R(t)−R0]/c。
- fixed detector处n(t)也变；预计da/dt=γ(1−b·n(t))恰好是energyinverse因子，因此E_lab(t)*da/dt=E0。
- Far/small-displacement近似下arrival lifetime scale为Dτ，而不是只乘γ；forward/back angle gates对同proper history的接受率不同。
- fixed-point detected sample有angular Jacobian/projectedarea/distance²权重，不能把unconditional等待直接当observed distribution。
- 此ps尺度toy没有actualclockstart/walk/jitter；SY14 ns-TOF不能据toy获得ps寿命。far andstatic limits、monotonicity、energy-slope identity与conditionalgate需独立核验。
