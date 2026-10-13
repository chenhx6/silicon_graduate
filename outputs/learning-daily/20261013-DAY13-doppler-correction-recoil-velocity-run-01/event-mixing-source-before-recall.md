# Day13：pair acceptance与beam-axis mixing回忆

2026-10-14T01:45:27.348482+08:00

已读LG20及C23后做计算前回忆，非独立考试：

1. True source cascade angle density可写W(u)=1+a2P2(u)+a4P4(u)，known-source原文theoreticalcoeff只作quantitative scale；selected joint response应含两γ互相靠近导致的clustering loss。
2. Tracking后混单γ无法模拟selection S12(n1,n2)；tracking前mix raw IP原则上可复演joint selection，但需matchingevent populations/threshold/occupancy。
3. 不同beam events的γ仍共享beam axis的marginal angular distribution；独立不等于mutual-angle isotropic。若单γq=1+A2P2(n·z)，两独立draws的angle density预计含A2²/5 P2(u)，需addition theorem或积分确认。
4. Source与in-beam异样本，mix normalizer若带物理anisotropy可改变被归一的shape；不能将sourceknown-spin成功验证直接迁移到beam alignment/δ。
5. 反证：构造已声明的smooth joint-acceptance toy，比较aftertracking遗漏pair-loss与beforetracking正确normalizer；另用独立axis-anisotropic photons核验pair-angleharmonic，非真实beam a2测量。

真实对照应持有raw/staged events、source/beam条件、calibration和normalizer covariance；本次没有这些输入。
