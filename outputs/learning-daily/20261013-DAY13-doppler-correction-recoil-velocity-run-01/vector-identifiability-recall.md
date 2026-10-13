# Day13：partial vector/global solutions 回忆

2026-10-14T02:00:51.056866+08:00

来源已读后的primed calculation recall；VD16/C23/LG20提供vector+angle条件，以下是另行声明的common-velocity calibration模型。

- Doppler需要b·n和gamma(b)，known speed只约束方向在unit sphere；一条known-rest-energy photon给一个projection/cone，非唯一vector。
- 两nonparallel photon directions加known speed可留下跨其plane的两个mirror directions；多次共平面energy measurements也不能区分它们。
- Local Jacobian可在每个branch有full local rank，仍有global mirror degeneracy；第三noncoplanar direction或particle track才增加判别。
- 若actual cascade在不同速度/位置/feeding stages发γ，不能将这些energies强制为一个constant vector；本题用同样common velocity的不同calibration emitters，忽略material/photonrecoil作为声明近似。
- Gain/offset、line identity、target/firstpoint与knownspeed covariance未给时，更不应把same-line宽度自校准写成event velocity测量。

反证标准：显式构造两unit vectors与全coplanar directions，使exact Lorentz energies完全相同；给一额外noncoplanar direction产生可算差别，静止极限差别消失。
