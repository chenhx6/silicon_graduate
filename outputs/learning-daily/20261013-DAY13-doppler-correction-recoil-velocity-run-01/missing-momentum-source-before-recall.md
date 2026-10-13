# Day13：missing momentum与velocity stage回忆

2026-10-14T00:50:23.767405+08:00

已有two-body photon与TOF练习后的primed recall，先记录预测，再读反应残核来源原段。

- 实验particle track/TOF可能在靶后或谱仪末端测得，Doppler需要发射时母核的vector，两者之间的能损、γ/particle emission和trajectory必须有stage定义。
- 熔合蒸发的复合核boost不是残核event velocity；未测蒸发粒子带走momentum，在同一channel内仍有event spread。
- 各方向独立、固定energy的isotropic emission模型给sum-momentum每分量variance∝n p²/3；真实顺序能量、anisotropy和channel selection会改变它。
- terminal fragment有准确velocity也不自动还原此前的emitter；若目标γ在所有neutron蒸发后且之后只有低能γ，遗漏particle recoil的阶段可能已不适用。需要先确认γ发射与粒子蒸发顺序。
- 反证：完整测得daughter和photon时以four-momentum conservation恢复parent，应消除stage bias；有unseen particle时可以构造不同parent四矢量产生相同terminal+observedγ。
- 最小设计：事件vector、PID/channel、gamma cascade、target/loss路径、必要particle information；独立geometry/TOF约束而非同谱最窄化。

本轮计算将先锁定missing emission发生在γ前还是γ后，避免把两种问题混为一个velocity correction。
