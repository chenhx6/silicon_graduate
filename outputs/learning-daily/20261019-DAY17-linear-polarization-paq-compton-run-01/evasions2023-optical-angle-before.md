# 实际optical角的变量合同核验前冻结

已完整Ch3–6/A.2/B、public全部producer与actualSiθ指纹，强priming非盲测。新问题不是再数旧409303/7933，而是actualThetaLdeg到底match哪一种已声明光学角约定。原Θ/Phi单位mrad，source Eq3.5写θlab=acos(cosΘ cosΦ)；常见两个投影斜率的另一约定θlab=atan(hypot(tanΘ,tanΦ))，不能先认为同式。预定只在Bρ>0且0≤ThetaLdeg<12的同样base中，保全部finitepoints，直接比较这两式与storedThetaLdeg的max/RMS/quantile/1e−5deg内比例，不fit角scale/offset、不筛异常使吻合。

必要companion：θ不变于X反射，paperEq3.5的phi正x与CodeA optical转lab的负x形成需要相对frame定义的两个候选。构造单位方向[±cosΦsinΘ,sinΦ,cosΦcosΘ]，两者norm/θ一致；仅报告actualopticalfield下phi差，不能用θ吻合选哪套handedness或裁原Dopplerθ/τ。gamma tracking−π/2与DCT合成角仍要matching，原dataset不提供完整calmatrix/φ真值。

若两θ公式都不match，就保raw/convention缺口，不增加更多候选函数/拟合常数去强配。只做变量/信息损失合同，不用未知vertex-energy-loss做vectorrecoil、fullMC或paperτCI。此为Day18无学分preview/no19。
