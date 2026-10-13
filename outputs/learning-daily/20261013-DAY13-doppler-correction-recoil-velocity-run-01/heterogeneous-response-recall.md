# Day13：energy-dependent PSA response回忆

2026-10-14T02:10:55.324400+08:00

LG20 Eq4/C23 Eq4/point-response已读后的primed计算回忆。

- Hit deposit energy Ei与full photon Eγ不同；first-IP uncertainty可能依Ei/segment/depth。一个平均pFWHM不能代表每event的误差。
- 小角度、knownvector下sigma_E²条件于Ei，混合后应平均variance，不先平均p再平方；多Gaussian mixture本身通常不是Gaussian，halfheight/FWHM与sigma equivalent不同。
- PeakGaussian fit会依窗口/weights/background定义；报告名义σ/FWHM而不报拟合选择不足以推断全响应。
- 若真正known per-event σi，weighted centroid能提高精度，但错误σi、不同均值或group-correlatedcalibration会破坏此收益；不是已证明改进实际OFT/PSA。
- 核验用LG20公式作为declared template的two-energy toy（未声称范围/参数匹配真实GANIL），检查analyticvariance、mixturehalfheight/gate、conditionalcentroidMC及equal-widthlimit。
