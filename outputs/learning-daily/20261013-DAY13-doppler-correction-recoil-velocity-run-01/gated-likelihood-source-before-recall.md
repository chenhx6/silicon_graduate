# Day13：能量门与likelihood回忆

2026-10-14T01:31:09.568525+08:00

已完成fixed-gate fraction/Voigt练习后的primed recall；先推断，再核验source selection及量化。

- 在energy/particle/FOM gate后的event distribution是条件分布，若gate fraction依拟合的β、gain、width、angle或feeding，则likelihood需含selection normalization。
- 窄化门后的Gaussian fit往往得到更小σ，但这是truncation，不自动说明原能量resolution更佳；有offset时门还拉偏mean。
- Gate counts依incident yield×efficiency×acceptance；只看normalized shape不能同时识别全部rate与acceptance。
- Held-out events来自同一setup检查statistical overfit，但共享calibration/basis/geometry的systematic可一起通过；不同已知line、particle calibration或distance scan提供额外约束。
- 反证：模拟已声明的Gaussian母分布，对有偏中心固定gate选择；naive normal MLE和正确truncated MLE比较。若full/selected/normalizer标明后仍不收敛，检查数值与模型，而不是自动给实验β。

源语境：AK12/C23 tracking acceptance，SY14 stage/predicate和CR13 mean-vector自校准；无原event packet，不做真实production likelihood claim。
