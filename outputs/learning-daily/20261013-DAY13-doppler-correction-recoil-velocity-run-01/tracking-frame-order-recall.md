# Day13：tracking与Doppler的处理顺序回忆

2026-10-14T02:18:15.398482+08:00

已经读LG20 processing和C23 Compton式；下面先写待检验物理逻辑，非来源执行code判错。

- Ge detector中Compton相互作用发生在实验室：electron近似静止、scattered/incident photon energy与angle全用同frame。
- 将full gamma energy校正到emitter frame是tracking完成后的incomingphoton能量变换；即便所有hit energies乘相同D，使总能量正确，也不能再配原lab angle/electron rest假设做Compton FOM。
- 标准cosθ=1−me(1/Eout−1/Ein)，同乘D会改成1−(1−cosθ)/D；强backscatter时可超出[−1,1]，因此会影响classification/efficiency。
- 若真正boost整个scattering的four-vectors，electron不再静止，需用Lorentz-invariant energy-momentum关系；只改能量标签不等于完整boost。
- 独立particle/vertex信息可在tracking前提供source位置，但不意味着把所有deposits改成emitter-rest energy。

验收：构造自由静止electron的物理two-hit photon，lab Compton关系exact；naive pre-scaled test失败；full boosted electron/photon invariants仍满足；β0两顺序一致。实际boundelectron/energy loss等未建模。
