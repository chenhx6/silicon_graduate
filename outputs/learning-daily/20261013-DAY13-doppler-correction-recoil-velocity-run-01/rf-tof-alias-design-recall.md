# Day13：rf tof alias design recall.md

2026-10-14T08:25:27.898189+08:00

已读CM21的102nsRF/TOF与AS21的conditionalinteger A/Q，为source-inspired设计前记录。

- 若只观测RFphase而没有absoluteperiodindex，T=phase+kP+offset有离散branches；连续Jacobian小不保证k/charge正确。实际source是否仅有phase或已经解卷，需productioncode，不能假定。
- 固定Bρ与massnumberA/q确定βγ；Z标签不唯一给ionicq。设计两不同O(A,q)使flighttime差exactP，可展示globaldiscreteambiguity。
- 采用mass=A u proxy、恒定速度/无materialloss与自设path；不是VAMOS真实mass/geometry或失误估计。
- independentETOT/charge/absoluteclock可排除branch；同PID推导出的rigidityspeed不能再次当独立验证。Knownγ能量也与calibration共享，需不同line/angle的hold-out。
- 反证：若rawtimestamp直接给k或已有independentcharge/energy约束，toyalias在该pipeline不成立。
- 验证：exactbranchphase/Bρ闭合、massenergy区分、周期/零噪音极限与propagatedcontinuouserrors；不称source已发生cycle误判。
