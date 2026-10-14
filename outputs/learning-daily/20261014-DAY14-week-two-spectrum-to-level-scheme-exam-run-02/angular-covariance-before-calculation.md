# Angular-fit Cov：计算前主动回忆

冻结：2026-10-15T03:14:45.056752+08:00，同Day14/session，primed by刚读Zobel1983全部六页（特别p390setup、p393统计dependence）。没有新的source-before盲读声明；尚未运行这个新设计code。

1. 两个marginalstaterrors不能一般决定covariance；不同sampling/权重/归一化能给不同ρ，需要angular-fit producer和Σ。不能从图中rectangularbars认出jointellipse。
2. 实际sourceC geometry0/57/90/158四angles同时采；alpha geometry两组三angles61/105/146.5与43/87/128.5，fixedmonitor作不同run归一。这些是knownsetup，raw intensities、相对效率误差和monitor counts没有给。
3. 比較prototypefit y=β0+β2P2+β4P4，归一coef A2/A4还含β0 Jacobian；假设已知pureE2最大系数再转alpha。Equal absolute variance、Poisson-like chosenvariance或commonmonitor modes只是设计条件。
4. 预期两个geometry可能给不同相关性，但sign/size须算；全局multiplicative normalization可能在normalizedratio一阶取消，不要把一切Cov归因beamcurrent。
5. 高信息控制：同geometry下寻找两套positivevariance/normalization模型，保持两个marginals而改变Cov；必须标chosen，不重构作者GF或actual event/error input。若sourcegeometry/independent-noise constraints不能支持选定例子，记录失败/边界而不硬拟合。
6. 验证GLS/Schur/数值Jacobian一致、PSD/rank、noise-scale变换及globalmode cancellation；不报告实验significance、新sigma/I或新multipolarity。

Source locators：Z83-12 p393/原Table1 errors；p390实际angles。Scientificscope仍同一noveltyreference-transfer的Day15无学分preview，day_index14、partial15，不研究下一卡。原15:00研究截止、15:00–16:00收束不变。
