# 102-keV未定parent的最小观测设计：量化前冻结

2026-10-16T12:25:15.768864+08:00

正式2012body在本轮选定路线未得，原因/界限见ding2012-prc-access-boundary-042.json，不建空source/不再原样请求。缺body不允许归因ENSDF错误，也不停止仍有信息的current设计route。仍Day14/partial15、formal21/24，无Day16。

问题/预测：source公开三门756.5/764.7/117.8区分101.3和102-keV group，却可能不区分同group102的285→183与270→167 parent。这须逐假设列path并声明观察投影：隐藏15.6、把两近能102仅记录为published102group。仅讨论support，不证明fullintensity/angular/timinglikelihood相同或原detector确实无15.6响应。

H_primary用已报告285→183的102_a、另270→167的102_b；H_evaluation用285→270的15.6及270→167的102，二者均保留285→167的117.8、上方101/764/411/756路径。源未给183下方实际decay，不把15.6能量差补成primary已测边。两个source-level假设都不是本任务重新拟合data。

待核设计：
- 选定acyclicsourcepaths/粗能量投影下，756gate support102、764gate support101/102、117gate support101在两模型可能相同；若是，只限制这几门的支持模式，不把samepositivepeak当topologyuniqueness。
- 同能量/同M1的ICC主要由原子Z/E/multipole决定，不是母态标签；单补一个混峰ICC或更多相同gatecount不必解决parent identity。
- 最直接falsifier是独立辐射前Ex(parent)或辐射后Ex/decay tag区分两node，间隔约15.6keV；或在可解析中间寿命和时序响应已校的条件下ordered15.6/102 timing。实际response/feasibility未得，不承诺能测。
- 若选一个单独声明的Gaussian independent state-tag design、equalwidth/priors/midpoint，wrongtagprob Φ[-Delta/(2sigma)]，要每class≤5%对应FWHM上界由Delta15.6计算。只是设计要求，不是现有detector性能/实验CL；不假装knownnode/tag已可直接获取。非Gaussian tail、unequalpriors、calbias、leakage/Cov与选择相关均需实际校准。

只做这个bounded support/design exercise，保留sourcehash/路径假设与模型分层。研究15:00止，当前约150min窗口；不启动别的日卡或用toy替实际data。
