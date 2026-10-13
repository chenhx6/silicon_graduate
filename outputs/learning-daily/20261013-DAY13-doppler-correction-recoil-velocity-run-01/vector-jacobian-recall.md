# Day13：直接vector/position Jacobian回忆

2026-10-14T02:04:07.579509+08:00

已有scalar/covariance/position-source学习后的primed recall，计算前锁定inputs与验收。

- Energy inverse f=E_lab γ(b)(1−b·n)，n=(gammaIP−emissionvertex)/R；所有vectors必须同frame，同长度单位。
- 若b和θ同时作raw输入，需意识到θ已从b/points计算，不能再把相同direction errors叠一次；可直接从Cartesian inputs传播。
- ∂f/∂b需含gamma derivative，∂f/∂r只保留transverse projection；径向delta r在first order不改direction。
- 同一coordinate origin平移两个位置，r不变；这是frame gauge，不等于physicaltarget仅移动而detector固定。所有b/r一起旋转也不改b·n。
- 静止β0时angle-coordinate不定义但Cartesian formula regular；position nuisance本身不改rest energy，δb估计误差仍可影响correction。

验收：finite differences、scalar/vector equivalence、zeroβ、common translation/rotation、MC covariance与单位；拒绝将任意自设Σ当actualsource jointcovariance。
