# Day13：degrader reference、finitefoil、feeding回忆

2026-10-14T04:53:50.790827+08:00

LS23 Fig6/7已读后的计算前primed回忆。

- Measuredβd作为reference使afterdegraderU恢复E0，但beforedegraderβt>βd保留angle-dependent S；U仍是movingemitter，不是β0。
- 对collinearback angles，Ecorr/E0=Dd/Dt<1；若用trueβem全部collapseE0，energy-only lifetimehistory信息消失，需保存lab/reference/stage字段。
- finitefoil crossing会有intermediateβ，不能只用twopeaks拟合而假设其中emission概率0；短distance时fraction可更大。
- τlevel与feeder等待之和改变gap survival/S-Ufraction；sourceτ3.8/7.5ps只作declared examplescale，不用sourcefigurepeakheight直接fit。
- 构造monovelocity/isotropic/selfGaussian idealcap fixture，properclock按lablinearβprofile积分，MC stage fractions与analyticCDF比较；真实Mg dE/dx、straggling、geometry/Σ与population未知。
