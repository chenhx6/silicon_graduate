# Day13：lineshape statistic source before recall.md

2026-10-14T08:25:27.895652+08:00

已读ZA23的Neyman/rebin≥10/jointΔχ²，以及CM21的final80%totalerrors；为primed续核，Baker–Cousins原文尚未打开。

- Neyman以observedcount作variance，Pearson用expectedcount，Poissonlikelihood处理计数，finitecounts时最优量与uncertainty不必相同。
- ≥10每bin是source的处理选择，不是所有情况下Gaussianerror/coverage已证。背景相减和共享normalization/calibration还改变Σ。
- 用uniformPoissonrate作可解析反例，再用声明的toyline-shape检方向；不由countbias直接判sourceτ偏差。
- τ/E两参数jointregion和profile/projected一参数区间要分开；不以Gaussianellipse练习倒推source误差。
- 需要原histogram/binning/template/background/MCstatisticpacket才能realrefit；当前设计不claim精确差异σ。
