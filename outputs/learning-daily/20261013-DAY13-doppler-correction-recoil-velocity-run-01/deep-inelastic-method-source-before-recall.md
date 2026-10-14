# Day13：Ciemała2021方法篇来源前回忆

2026-10-14T07:43:27.203170+08:00

已知2020主论文与2019报告，故为primed recall；尚未打开arXiv2012.05180正文。

- 需要找到从state-conditioned VAMOS终速度重建初速度的generator、direct/dissipative分布和靶depth prior。初速度“准确重建”需控制response与stopping，不自动为independentmeasurement。
- 发射速度、VAMOS测得finalvelocity、Doppler correction使用哪一种，必须逐stage定位；不要从field“velocity”补写真实代码。
- 19O短/长寿命control能验证什么？已知短线重建140fs而参考92fs、long线只有valley；应核χ²与knownfeeding/calibration/systematics，不把two controls当独立newexperiment。
- 如果stoppingscale与τ有相同无量纲比，line-shape本身不能消除这份退化；需要independentstoppinginput，finitegeometry或逐state/材料controls。
- 必须保留feeding、targetthickness与reactiondepth、response/sourcecalibration、Σ与fitstatistic定义，paper未给不填。2023原velocitymeasurement改善specificnuisance但不证明source全部systematiccancelled。
- 竞争解释：真实τ差异、初速度model、未观测feeding、restenergy/gain与非Gaussianresponse；方法篇只能支持提出检验，不能替代两个原χ²面重分析。
