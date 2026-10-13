# 持续Day13：新路线来源前回忆

时间：2026-10-13T21:11:02.976652+08:00。基于已有exact energy/Jacobian，尚未打开本轮新论文。

- β应是发射时速度，而target位置/first interaction提供γ方向；TOF或particle kinematics可约束每事件速度，但也需path length、vertex、energy loss、reaction channel。
- 用束轴名义角或晶体中心会增加σθ；position resolution作用约为σθ≈σx/R，远target/近target的finite solid angle不同。
- 对有限角分布，correction of mean angle不一定等于mean of corrected energies；需检查非线性二阶bias和tails。
- 固定energy gate依赖corrected centroid和width；β/geometry错误即使总峰看似合理，也可改变角环不同的gate acceptance，偏置Iγ与angular/yield ratios。
- Stopping/feeding可能造成不同transition或selected gate的有效平均β；较窄峰不证明lifetime-free calibration。校正残差与核形变无直接等价关系。
- 需要新证据：追踪阵列Doppler resolution预算、实际recoil/TOF reconstruction、reaction+target thickness的独立输入、spectral gate migration是否实测。数字先不填，不把搜索摘要当证据。

数值检验计划：明确synthetic E0、β、geometry/covariance/response，检查mean-angle correction的有限bin偏差；在calibration/shift/width下积分固定gate，比较angle组efficiency；zero-β/zero-uncertainty/detector-distance极限与quadrature/MC交叉核对。
