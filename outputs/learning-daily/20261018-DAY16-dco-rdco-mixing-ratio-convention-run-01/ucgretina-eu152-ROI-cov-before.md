# 实际Eu152净ROI与共享归一协方差前置合同

已核实际egam均TH1F1keV8000bins、sumw2N0、integernonnegative、无TTree；完整egam内值可访问但尚未针对下列ROI查数。先冻物理输入/误差条件，再算。已知highwindow[1800,3000]rebin4得到Y13836/B30293，a=.45673918；[1540,3000]a=.49262791。

预选121.782keV附近ROI120–128与1408.022附近ROI1404–1412，以rebin4的bincenters闭区间选入。它们是grossROI而非Gaussian净peak面积；直接n_i=y_i−a b_i，不从这种值测Q或activity。高区与低ROI不重叠。

声明独立Poisson source/background各bin、sourcefree highregion时，Var(a)≈a²(1/Y+1/B)；不同低ROI的共同a给Cov(n_i,n_j)≈b_i b_j Var(a)。同ROI Var(n_i)≈y_i+a²b_i+b_i²Var(a)。输入只有processedhist，sumw2缺失只允许条件演示，不能认证eventindependence/系统误差。检验完整Cov的PSD和对角、固定a对角控制；不要删crossCov后当新独立测量。另给README1540门作为已预选对照，不据差别判显著冲突或选择更合p0的窗口。

保留reader修订和source/bg MC 缺口：无simhist不能重放fullfit/p1/thresholds，两个run/两种simulation处理不增加实验独立性；不分析寿命/强度/Day18。
