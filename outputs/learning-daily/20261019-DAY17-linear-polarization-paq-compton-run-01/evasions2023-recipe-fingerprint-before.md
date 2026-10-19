# 已读producer与实际data指纹的新问题冻结

旧producer-reading-scope明确Backup/extractionData.C在20:08已读；本轮已在Ch3/B新输入下重看其全部body，不算新source/盲测/独立实验。旧Si_dE>0共7933、Siθ范围11.673–21.525已primed，不重跑它当新结果。

新问题：所有positiveSi_dE记录的Si_theta是否等同Backup固定recipe atan((24+.75+1.5*i)/119.8),i0..15的离散指纹？只用原声明119.8/r24/stripcenter，不拟合Z或新offset；预定float一致阈值1e−5deg。逐uniqueangle存occupancy/i/residual，报告能否推stripindex却不能推quadrant/rawcalibration。此仅生成recipe相容性，不是独立survey精度/原producer认证。

已读body还显示GATCONF1/Brho>0、target1..5链，而QPL/time额外门只comment；abs(trackE−6875)>8的loop只selfassignment，无删track/改nbTrack。新实际query计原publicfile中abs(trackE−6875)≤8的events/tracks，只descriptor、不认全是Si6878污染或需一刀剔；不运行外部/Volumes路径和RECREATE，不修原code。原34hash/data不改，原fullPID/θDS/mask/Σ依旧缺。
